import { createHash, createHmac, randomBytes, timingSafeEqual } from 'node:crypto';
import type { Context, Next } from 'hono';
import type { Db } from './db.ts';
import { config } from './config.ts';

// Pilot identity: anonymous player + opaque bearer token, created once per
// install and kept in the client's prefs. Phase 3 replaces this with OAuth
// account linking (plan §5.3); the player row and everything hanging off it
// survive that change — linking just attaches identity_id + validated.

export const sha256 = (s: string) => createHash('sha256').update(s).digest('hex');

export function createPlayer(db: Db, deviceHint?: string) {
  const id = 'p_' + randomBytes(8).toString('hex');
  const token = randomBytes(24).toString('base64url');
  const now = Date.now();
  db.prepare(
    'INSERT INTO players (id, token_hash, created_at, last_seen, device_hint) VALUES (?, ?, ?, ?, ?)',
  ).run(id, sha256(token), now, now, deviceHint ?? null);
  return { id, token };
}

export function playerFromToken(db: Db, token: string): string | undefined {
  const row = db.prepare('SELECT id FROM players WHERE token_hash = ?').get(sha256(token)) as { id: string } | undefined;
  if (row) db.prepare('UPDATE players SET last_seen = ? WHERE id = ?').run(Date.now(), row.id);
  return row?.id;
}

// ---- signed question tokens (plan §5.1: issued signed, single-use, expiring)

export function signTablet(expeditionId: string, idx: number, nonce: string, expiresAt: number): string {
  const body = `${expeditionId}.${idx}.${nonce}.${expiresAt}`;
  const sig = createHmac('sha256', config.secret).update(body).digest('base64url');
  return `${body}.${sig}`;
}

/** Constant-time compare that cannot throw on attacker-controlled input.
 *
 * `timingSafeEqual` compares *bytes* and throws if the lengths differ, so a
 * guard on string length is not enough: 43 multibyte characters is 43 chars but
 * 86 bytes, which passed the old check and then threw `RangeError`. Build the
 * buffers first and compare their real lengths.
 */
function sigEqual(want: string, got: string): boolean {
  const a = Buffer.from(want);
  const b = Buffer.from(got);
  return a.length === b.length && timingSafeEqual(a, b);
}

export function verifyTablet(token: string): { expeditionId: string; idx: number; nonce: string; expiresAt: number } | null {
  const parts = token.split('.');
  if (parts.length !== 5) return null;
  const [expeditionId, idxS, nonce, expS, sig] = parts;
  const body = `${expeditionId}.${idxS}.${nonce}.${expS}`;
  const want = createHmac('sha256', config.secret).update(body).digest('base64url');
  if (!sigEqual(want, sig)) return null;
  return { expeditionId, idx: Number(idxS), nonce, expiresAt: Number(expS) };
}

// ---- signed mini-game rounds
//
// Mini-game content lives in the client, so the server cannot mark the answers.
// What it can do — and now does — is refuse to pay for a round it never issued.
// A round must be started here, is claimed exactly once, and must have taken a
// plausible amount of wall-clock time. That turns "XP from a bare curl" into
// "XP requires a real round, played at human speed, claimed once."
//
// This is not the same as verifying the answers. Doing that needs the content
// moved server-side, the way the question bank already is. See AUDIT.

export function signMini(roundId: string, nonce: string, expiresAt: number): string {
  const body = `${roundId}.${nonce}.${expiresAt}`;
  const sig = createHmac('sha256', config.secret).update(body).digest('base64url');
  return `${body}.${sig}`;
}

export function verifyMini(token: string): { roundId: string; nonce: string; expiresAt: number } | null {
  const parts = token.split('.');
  if (parts.length !== 4) return null;
  const [roundId, nonce, expS, sig] = parts;
  const want = createHmac('sha256', config.secret).update(`${roundId}.${nonce}.${expS}`).digest('base64url');
  if (!sigEqual(want, sig)) return null;
  return { roundId, nonce, expiresAt: Number(expS) };
}

// ---- middleware

export type Env = { Variables: { playerId: string; db: Db } };

export function requirePlayer(db: Db) {
  return async (c: Context<Env>, next: Next) => {
    const h = c.req.header('authorization') ?? '';
    const token = h.startsWith('Bearer ') ? h.slice(7) : '';
    const id = token ? playerFromToken(db, token) : undefined;
    if (!id) return c.json({ error: 'unauthorized' }, 401);
    const status = (db.prepare('SELECT status FROM players WHERE id = ?').get(id) as { status: string }).status;
    if (status === 'banned') return c.json({ error: 'account_closed' }, 403);
    c.set('playerId', id);
    await next();
  };
}

/** The identity a rate limit is charged against.
 *
 * Two rules, both learned the hard way in the audit:
 *
 * 1. `X-Forwarded-For` is attacker-controlled unless something trusted set it.
 *    Reading it unconditionally meant a fresh spoofed header per request, which
 *    is no limit at all. It is now consulted only when ARCADE_TRUST_PROXY says
 *    a proxy is in front, and then only the last hop, which that proxy appends.
 * 2. There must be no shared fallback bucket. The old code fell back to the
 *    literal string 'anon', so one host could exhaust the window and deny
 *    signup to every other anonymous caller on earth.
 */
function limitKey(c: Context): string {
  const auth = c.req.header('authorization');
  if (auth) return 't:' + sha256(auth);

  if (config.trustProxy) {
    const xff = c.req.header('x-forwarded-for');
    if (xff) {
      const hops = xff.split(',').map((s) => s.trim()).filter(Boolean);
      // The nearest proxy appends the address it saw, so the last hop is the
      // only one a client cannot forge.
      const last = hops[hops.length - 1];
      if (last) return 'p:' + last;
    }
  }

  // Falls back to the socket, which a client cannot choose.
  const env = c.env as { incoming?: { socket?: { remoteAddress?: string } } } | undefined;
  const addr = env?.incoming?.socket?.remoteAddress;
  return addr ? 'a:' + addr : 'u:unattributable';
}

/**
 * Sliding-window per-key limiter.
 *
 * The first version was a fixed window that reset the first time a hit landed
 * more than `windowMs` after the window opened, so a burst of `limit` at t=0
 * and another at t=61 s admitted twice the limit inside 61 s (audit R4). This
 * one keeps the previous window's count and weights it by how much of that
 * window still overlaps the last `windowMs`: at t=61 s the first burst still
 * counts for 59/60 of itself, so the second window admits only what the limit
 * leaves. Windows are anchored to each key's first hit rather than the wall
 * clock, which keeps the arithmetic deterministic under the tests' clock
 * control. Enough for a pilot; put a real one at the edge later.
 */
export function rateLimit(limit: number, windowMs = 60_000, error = 'rate_limited') {
  const buckets = new Map<string, { start: number; count: number; prev: number }>();
  return async (c: Context, next: Next) => {
    const key = limitKey(c);
    const now = Date.now();
    let b = buckets.get(key);
    if (!b || now - b.start >= 2 * windowMs) {
      b = { start: now, count: 0, prev: 0 };
      buckets.set(key, b);
    } else if (now - b.start >= windowMs) {
      b.prev = b.count;
      b.count = 0;
      b.start += windowMs;
    }
    const weight = 1 - (now - b.start) / windowMs;
    if (b.prev * weight + b.count >= limit) return c.json({ error }, 429);
    b.count++;
    // Evict only what has expired. Clearing the whole map let an attacker flush
    // every legitimate counter by cycling enough distinct keys.
    if (buckets.size > 50_000) {
      for (const [k, v] of buckets) if (now - v.start >= 2 * windowMs) buckets.delete(k);
    }
    await next();
  };
}
