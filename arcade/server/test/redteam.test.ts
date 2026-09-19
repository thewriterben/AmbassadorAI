// Red-team regression file, 18 Sep 2026. See ../../AUDIT-2026-09-18.md.
//
// Every case here is an attack or an abuse-shaped edge run against a fresh
// in-memory app. Three kinds of case, named so the intent survives a grep:
//
//   OPEN      — a finding that is still open. The test asserts the SECURE
//               behaviour and is tagged `todo`, so it stays green while the
//               hole exists and shows up as a passing todo the moment a fix
//               lands. That flip is the signal to drop the tag and close the
//               finding in the audit.
//   ACCEPTED  — a behaviour we have decided to live with for now. The test
//               documents exactly what it is and must keep passing.
//   HOLDS     — a property that should already hold. A hard regression test.
//
// Nothing here talks to a network. Each case gets its own database and its
// own rate-limiter map, so nothing bleeds between them.

import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
import { openDb } from '../src/db.ts';
import { QuestionBank } from '../src/bank.ts';
import { createApp } from '../src/app.ts';
import { config } from '../src/config.ts';
import { todayIndex } from '../src/ledger.ts';
import { maxRerollsPerDay } from '../src/handles.ts';

// Time control, same trick as api.test.ts: the app reads Date.now().
let offset = 0;
const realNow = Date.now;
before(() => {
  Date.now = () => realNow() + offset;
});
after(() => {
  Date.now = realNow;
});
const advance = (ms: number) => (offset += ms);

const BANK_DIR = fileURLToPath(new URL('../data/bank', import.meta.url));
const bank = QuestionBank.load(BANK_DIR);
const DAY = 86_400_000;

type Reply = { status: number; headers: Headers; json: any };
type CallOpts = { token?: string; socket?: string; xff?: string };

/** A fresh app, database and limiter for one case. */
function fresh(b: QuestionBank = bank) {
  const db = openDb(':memory:');
  const app = createApp(db, b);
  const call = async (method: string, path: string, body?: unknown, opts: CallOpts = {}): Promise<Reply> => {
    const headers: Record<string, string> = { 'content-type': 'application/json' };
    if (opts.token) headers.authorization = `Bearer ${opts.token}`;
    if (opts.xff) headers['x-forwarded-for'] = opts.xff;
    // The third argument becomes c.env, which is where the limiter reads the
    // socket address from when no proxy is trusted.
    const env = opts.socket ? { incoming: { socket: { remoteAddress: opts.socket } } } : undefined;
    const res = await app.request(path, { method, headers, body: body === undefined ? undefined : JSON.stringify(body) }, env as any);
    return { status: res.status, headers: res.headers, json: await res.json().catch(() => ({})) };
  };
  const player = async () => (await call('POST', '/v1/players', {})).json.token as string;
  return { db, app, call, player };
}

const openFinding = (name: string, fn: () => Promise<void> | void) => test(`OPEN ${name}`, { todo: true }, fn);
const accepted = (name: string, fn: () => Promise<void> | void) => test(`ACCEPTED ${name}`, fn);
const holds = (name: string, fn: () => Promise<void> | void) => test(`HOLDS ${name}`, fn);

/** Opens a round, waits out its floor, claims it with the given score. */
async function playMini(call: ReturnType<typeof fresh>['call'], game: string, token: string, body: Record<string, unknown>) {
  const s = await call('POST', `/v1/mini/${game}/start`, {}, { token });
  assert.equal(s.status, 201, JSON.stringify(s.json));
  advance(config.mini.minDurationMs[game] + 1000);
  return call('POST', `/v1/mini/${game}`, { ...body, token: s.json.token }, { token });
}

// ---------------------------------------------------------------------------

holds('R1 the mini-game daily cap still binds when rounds straddle UTC midnight', async () => {
  // Found open on 2026-09-18, fixed the same day. mini_rounds.day is stamped
  // when the round is OPENED, and the cap used to count claimed rounds whose
  // day equalled the CLAIM day. Rounds opened before midnight and claimed
  // after it were counted against a day that contained none of them, so the
  // count was 0 for every claim and all 15 paid. The cap now counts by the
  // round's own day.
  const { call, player } = fresh();
  const tok = await player();
  const game = 'pillar_sort';
  const cap = config.mini.rewardedRoundsPerDay;

  // Land 60 s before the next UTC midnight.
  const now = Date.now();
  const idx = Math.floor((now - config.ledger.epochUtc) / DAY);
  advance(config.ledger.epochUtc + (idx + 1) * DAY - now - 60_000);
  assert.equal(todayIndex(), idx);

  const tokens: string[] = [];
  for (let i = 0; i < cap + 5; i++) {
    const s = await call('POST', `/v1/mini/${game}/start`, {}, { token: tok });
    assert.equal(s.status, 201);
    tokens.push(s.json.token);
  }

  // Two minutes later it is tomorrow. Past the 25 s floor, far inside the 1 h life.
  advance(120_000);
  assert.equal(todayIndex(), idx + 1);

  let paid = 0;
  for (const t of tokens) {
    const r = await call('POST', `/v1/mini/${game}`, { right: 24, total: 24, token: t }, { token: tok });
    assert.equal(r.status, 200, JSON.stringify(r.json));
    if (r.json.xpGained > 0) paid++;
  }
  assert.ok(paid <= cap, `${paid} of ${cap + 5} rounds paid across midnight; the cap is ${cap}`);
});

accepted('R2 a mini-game score is whatever the client says, bounded only by the per-round and per-day caps', async () => {
  // B2 residual, on the record in app.ts:346-349. The server cannot mark the
  // answers because the content ships in the client. What it can do is clamp:
  // right ≤ maxRight[game], XP ≤ maxXpPerRound, rounds ≤ rewardedRoundsPerDay.
  const { call, player } = fresh();
  const tok = await player();
  const r = await playMini(call, 'coin_quest', tok, { right: 999, total: 999, extra: 0 });
  assert.equal(r.status, 200);
  assert.equal(r.json.xpGained, 3 * 20 + 20, 'right is clamped to maxRight before the formula');
  assert.ok(r.json.xpGained <= config.mini.maxXpPerRound);

  // The honest daily ceiling per game path, so nobody widens it silently.
  let total = r.json.xpGained;
  for (let i = 1; i < config.mini.rewardedRoundsPerDay + 3; i++) {
    total += (await playMini(call, 'coin_quest', tok, { right: 3, total: 3 })).json.xpGained;
  }
  assert.equal(total, config.mini.rewardedRoundsPerDay * 80, 'coin_quest pays at most 10 × 80 XP per UTC day');
});

openFinding('R3 anonymous player creation is throttled by something other than the generic limiter', async () => {
  // POST /v1/players is unauthenticated and has no cap of its own. Anything
  // under rateLimit.perMinute from one bucket mints that many identities, each
  // of which can climb the board. No attestation, no device binding, no
  // proof-of-work. The client (api.dart) also re-registers silently on any 401.
  const { call } = fresh();
  const ids = new Set<string>();
  for (let i = 0; i < 60; i++) {
    const r = await call('POST', '/v1/players', { deviceHint: 'sybil' }, { socket: '203.0.113.9' });
    assert.equal(r.status, 201);
    ids.add(r.json.playerId);
  }
  assert.equal(ids.size, 60, 'sixty distinct players from one address in one window');
  // The control we want: bulk anonymous creation from one source slows down
  // well before the generic per-minute limit. Encoded as the assertion this
  // test should eventually make.
  assert.fail('no creation cap exists; only rateLimit.perMinute bounds signup from one address');
});

openFinding('R4 the rate limiter does not admit a double burst at the window boundary', async () => {
  // Fixed window (auth.ts:139-146): the counter resets the first time a hit
  // lands more than 60 s after the window opened. perMinute hits at t=0 and
  // perMinute more at t=61 s is 2× the limit inside 61 s. Known residual from
  // audit B3, unchanged.
  const { call } = fresh();
  const hit = () => call('GET', '/v1/leaderboard', undefined, { socket: '198.51.100.7' }); // 401s still count
  let admitted = 0;
  for (let i = 0; i < config.rateLimit.perMinute; i++) if ((await hit()).status !== 429) admitted++;
  assert.equal((await hit()).status, 429, 'the limiter does engage inside a window');
  advance(61_000);
  for (let i = 0; i < config.rateLimit.perMinute; i++) if ((await hit()).status !== 429) admitted++;
  assert.ok(admitted <= config.rateLimit.perMinute + 5, `${admitted} requests admitted in 61 s from one address`);
});

holds('R5 X-Forwarded-For is ignored unless a proxy is trusted, and then only its last hop counts', async () => {
  const { call } = fresh();
  const prev = config.trustProxy;
  try {
    // Untrusted: a fresh spoofed header per request must not buy a fresh bucket.
    config.trustProxy = false;
    let limitedAt = -1;
    for (let i = 0; i < config.rateLimit.perMinute + 5; i++) {
      const r = await call('GET', '/v1/leaderboard', undefined, { socket: '10.0.0.1', xff: `spoof-${i}` });
      if (r.status === 429) {
        limitedAt = i;
        break;
      }
    }
    assert.equal(limitedAt, config.rateLimit.perMinute, 'spoofed XFF defeated the socket-keyed limiter');

    // Trusted: the client-supplied first hop is ignored; the proxy-appended
    // last hop is the key. Two different first hops share one bucket.
    config.trustProxy = true;
    advance(61_000);
    for (let i = 0; i < config.rateLimit.perMinute; i++) {
      const r = await call('GET', '/v1/leaderboard', undefined, { socket: '10.0.0.1', xff: `1.1.1.${i % 250}, 2.2.2.2` });
      assert.notEqual(r.status, 429);
    }
    const overflow = await call('GET', '/v1/leaderboard', undefined, { socket: '10.0.0.1', xff: '9.9.9.9, 2.2.2.2' });
    assert.equal(overflow.status, 429, 'last hop must be the key when the proxy is trusted');
    const otherHop = await call('GET', '/v1/leaderboard', undefined, { socket: '10.0.0.1', xff: '9.9.9.9, 3.3.3.3' });
    assert.notEqual(otherHop.status, 429, 'a different last hop is a different client');
  } finally {
    config.trustProxy = prev;
  }
});

openFinding('R6 a tablet cannot be answered once its expedition is finished', async () => {
  // The issue path checks finished_at (app.ts:136); the answer path does not
  // (app.ts:177-218). A tablet left open survives `finish`, and answering it
  // afterwards still writes the tablet row and updates spaced-retrieval
  // mastery through record(). XP is unaffected because finish has already
  // paid, but the run's own state machine is not closed.
  const { call, player } = fresh();
  const tok = await player();
  const start = await call('POST', '/v1/expeditions', {}, { token: tok });
  const exp = start.json.expeditionId;
  advance(40_000);
  const t0 = await call('POST', `/v1/expeditions/${exp}/tablets/0`, {}, { token: tok });
  assert.equal(t0.status, 200);
  advance(config.run.minFinishMs);
  const fin = await call('POST', `/v1/expeditions/${exp}/finish`, {}, { token: tok });
  assert.equal(fin.status, 200);
  const late = await call('POST', `/v1/expeditions/${exp}/tablets/0/answer`, { token: t0.json.token, choice: 0 }, { token: tok });
  assert.equal(late.status, 409, `answer after finish returned ${late.status}: ${JSON.stringify(late.json)}`);
});

openFinding('R7 a bank question that disappears between issue and answer is a 4xx, not a 500', async () => {
  // Audit B8, still open. A question's id is sha1(section + prompt), so
  // editing a prompt gives it a new id and every tablet row that references
  // the old one hits `bank.get(...)!` (app.ts:150, 189) and throws forever.
  // Simulated here by removing the id from a private bank instance — the same
  // state a reload after an edit produces.
  const own = QuestionBank.load(BANK_DIR);
  const { db, call, player } = fresh(own);
  const tok = await player();
  const start = await call('POST', '/v1/expeditions', {}, { token: tok });
  const exp = start.json.expeditionId;
  const row = db.prepare('SELECT question_id FROM tablets WHERE expedition_id = ? AND idx = 0').get(exp) as { question_id: string };
  (own as any).byId.delete(row.question_id);
  advance(40_000);
  const issue = await call('POST', `/v1/expeditions/${exp}/tablets/0`, {}, { token: tok });
  assert.ok(issue.status >= 400 && issue.status < 500, `issuing a tablet for a vanished question returned ${issue.status}`);
});

accepted('R8 status="xp_only" means zero XP, not "XP only", and is never set by the server', async () => {
  // db.ts declares ok | xp_only | banned. Every award path gates on
  // status === 'ok' (app.ts:110, 315, 412); only 'banned' is refused at the
  // door (auth.ts:97) or dropped from the board (progress.ts:68). Nothing in
  // the codebase ever writes 'xp_only'. So the middle rung of the abuse
  // ladder is a manual SQL update whose name reads as the opposite of what it
  // does. Plausibility flags are stored but never escalate anyone.
  const { db, call, player } = fresh();
  const tok = await player();
  const me = await call('GET', '/v1/me', undefined, { token: tok });
  db.prepare("UPDATE players SET status = 'xp_only' WHERE id = ?").run(me.json.playerId);
  const r = await playMini(call, 'pillar_sort', tok, { right: 24, total: 24 });
  assert.equal(r.status, 200);
  assert.equal(r.json.xpGained, 0);
  assert.equal((await call('GET', '/v1/me', undefined, { token: tok })).status, 200, 'not blocked');
  const board = await call('GET', '/v1/leaderboard', undefined, { token: tok });
  assert.equal(board.status, 200, 'not excluded');
  const src = await import('node:fs');
  const code = ['app.ts', 'auth.ts', 'progress.ts', 'scheduler.ts', 'handles.ts', 'db.ts']
    .map((f) => src.readFileSync(fileURLToPath(new URL(`../src/${f}`, import.meta.url)), 'utf8'))
    .join('\n');
  assert.ok(!/SET status\s*=\s*'xp_only'|status\s*=\s*['"]xp_only['"]\s*WHERE/i.test(code), 'nothing writes xp_only');
});

openFinding('R9 a corrupt server-written JSON column is a handled error, not a 500', async () => {
  // JSON.parse on tablets.option_order (app.ts:190) and ledger_plays.guesses
  // (app.ts:274, 304) is unguarded. Only reachable through a damaged database,
  // so low severity — but a reader that throws on its own stored data is the
  // wrong shape, and Hono's default handler turns it into a stack trace.
  const { db, call, player } = fresh();
  const tok = await player();
  const start = await call('POST', '/v1/expeditions', {}, { token: tok });
  const exp = start.json.expeditionId;
  advance(40_000);
  const t0 = await call('POST', `/v1/expeditions/${exp}/tablets/0`, {}, { token: tok });
  db.prepare('UPDATE tablets SET option_order = ? WHERE expedition_id = ? AND idx = 0').run('{not json', exp);
  advance(t0.json.minLatencyMs + 100);
  const r = await call('POST', `/v1/expeditions/${exp}/tablets/0/answer`, { token: t0.json.token, choice: 0 }, { token: tok });
  assert.ok(r.status < 500, `answer over a corrupt option_order returned ${r.status}`);
});

holds('R10 the board never carries ids or tokens, and handle rerolls stop at the daily cap', async () => {
  const { call, player } = fresh();
  const a = await player();
  const b = await player();
  await playMini(call, 'pillar_sort', a, { right: 24, total: 24 });
  const board = await call('GET', '/v1/leaderboard', undefined, { token: b });
  assert.equal(board.status, 200);
  const text = JSON.stringify(board.json);
  assert.ok(!text.includes('p_'), 'player ids on the board');
  assert.ok(!text.includes(a) && !text.includes(b), 'tokens on the board');
  for (const row of board.json.rows) assert.deepEqual(Object.keys(row).sort(), ['handle', 'rank', 'xp', 'you']);
  for (let i = 0; i < maxRerollsPerDay; i++) assert.equal((await call('POST', '/v1/me/handle/reroll', {}, { token: a })).status, 200);
  assert.equal((await call('POST', '/v1/me/handle/reroll', {}, { token: a })).status, 429);
});

holds('R11 /healthz is the only unauthenticated read and says only that the bank is loaded', async () => {
  // It is also outside the /v1/* limiter (app.ts:53-55). What it returns is
  // the bank size and the day index — not secrets, but the exact numbers a
  // scraper would want to know whether the bank changed.
  const { call } = fresh();
  const h = await call('GET', '/healthz');
  assert.equal(h.status, 200);
  assert.deepEqual(Object.keys(h.json).sort(), ['bank', 'day', 'ok']);
  for (const path of ['/v1/me', '/v1/leaderboard', '/v1/ledger/today']) {
    assert.equal((await call('GET', path)).status, 401, path);
  }
  for (const path of ['/v1/expeditions', '/v1/mini/pillar_sort/start', '/v1/mini/pillar_sort', '/v1/ledger/guess', '/v1/me/handle/reroll']) {
    assert.equal((await call('POST', path, {})).status, 401, path);
  }
});

accepted('R12 CORS is a wildcard unless ARCADE_CORS is set, whatever NODE_ENV says', async () => {
  // config.corsOrigins defaults to ['*'] (config.ts:14). assertProductionConfig
  // refuses that only when NODE_ENV=production (config.ts:114), so a public
  // deploy that forgets the label keeps the wildcard. Low severity: auth is a
  // bearer header and cors() is not configured with credentials, so a browser
  // page on another origin cannot ride a logged-in session. It can still call
  // the registration endpoint.
  const prev = config.corsOrigins;
  try {
    config.corsOrigins = ['*'];
    const { app } = fresh();
    const r = await app.request('/healthz', { headers: { origin: 'https://evil.example' } });
    assert.equal(r.headers.get('access-control-allow-origin'), '*');
    assert.equal(r.headers.get('access-control-allow-credentials'), null);
  } finally {
    config.corsOrigins = prev;
  }
});
