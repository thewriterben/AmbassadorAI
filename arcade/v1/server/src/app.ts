import { Hono } from 'hono';
import { cors } from 'hono/cors';
import { randomBytes } from 'node:crypto';
import type { Db } from './db.ts';
import type { QuestionBank } from './bank.ts';
import { config } from './config.ts';
import { createPlayer, rateLimit, requirePlayer, signMini, signTablet, verifyMini, verifyTablet, type Env } from './auth.ts';
import { pick, record, mastery } from './scheduler.ts';
import { awardXp, checkBadges, getPlayer, leaderboard, snapshot } from './progress.ts';
import { ensureHandle, maxRerollsPerDay, rerollHandle } from './handles.ts';
import { markGuess, puzzleFor, todayIndex, validGuess } from './ledger.ts';

const dayOf = (ms: number) => Math.floor((ms - config.ledger.epochUtc) / 86_400_000);
const startOfDay = (day: number) => config.ledger.epochUtc + day * 86_400_000;

/** A finite non-negative integer from untrusted JSON, clamped.
 *
 * `Number({})` and `Number('x')` are both NaN, and node:sqlite rejects NaN with
 * "NOT NULL constraint failed" — a 500 with a stack trace, from a one-line
 * request body. Every number arriving from a client goes through here.
 */
function uint(v: unknown, max: number, fallback = 0): number {
  const n = Number(v);
  if (!Number.isFinite(n)) return fallback;
  return Math.max(0, Math.min(max, Math.floor(n)));
}

/** Same, but preserves "not supplied" as null for nullable columns. */
function intOrNull(v: unknown): number | null {
  if (v === undefined || v === null) return null;
  const n = Number(v);
  return Number.isFinite(n) ? Math.floor(n) : null;
}

/** Fisher-Yates.
 *
 * `sort(() => Math.random() - 0.5)` is not a shuffle: with a 4-option question
 * it left the correct answer in slot 0 nearly 36% of the time instead of 25%,
 * so always picking the first option beat guessing by half again.
 */
function shuffled<T>(xs: readonly T[]): T[] {
  const a = [...xs];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export function createApp(db: Db, bank: QuestionBank) {
  const app = new Hono<Env>();
  app.use('*', cors({ origin: config.corsOrigins.includes('*') ? '*' : config.corsOrigins }));
  app.use('/v1/*', rateLimit(config.rateLimit.perMinute));

  app.get('/healthz', (c) => c.json({ ok: true, bank: bank.items.length, day: todayIndex() }));

  // ---------------------------------------------------------------- players
  app.post('/v1/players', async (c) => {
    const body = (await c.req.json().catch(() => ({}))) as { deviceHint?: string };
    const { id, token } = createPlayer(db, typeof body.deviceHint === 'string' ? body.deviceHint.slice(0, 120) : undefined);
    ensureHandle(db, id);
    return c.json({ playerId: id, token, progress: snapshot(db, id) }, 201);
  });

  const auth = requirePlayer(db);

  app.get('/v1/me', auth, (c) => {
    const id = c.get('playerId');
    const day = todayIndex();
    ensureHandle(db, id); // players created before handles existed
    const p = getPlayer(db, id)!;
    const rewardedToday = (
      db
        .prepare('SELECT COUNT(*) AS n FROM expeditions WHERE player_id = ? AND rewarded = 1 AND started_at >= ?')
        .get(id, startOfDay(day)) as { n: number }
    ).n;
    return c.json(
      snapshot(db, id, {
        day,
        ledgerDoneToday: p.last_ledger_day === day,
        rewardedExpeditionsToday: rewardedToday,
        rewardedExpeditionsPerDay: config.tablets.rewardedPerDay,
        mastery: mastery(db, bank, id),
      }),
    );
  });

  // ------------------------------------------------------------ expeditions
  const fractions = (n: number) => Array.from({ length: n }, (_, i) => ((i + 1) / (n + 1)) * 0.92 + 0.04);

  app.post('/v1/expeditions', auth, (c) => {
    const id = c.get('playerId');
    const now = Date.now();
    const day = dayOf(now);
    // Abandon stale open expeditions so a crash never wedges the player.
    db.prepare('UPDATE expeditions SET finished_at = ?, flags = flags || \'abandoned,\' WHERE player_id = ? AND finished_at IS NULL AND started_at < ?').run(
      now,
      id,
      now - config.run.maxOpenExpeditionsMs,
    );
    const open = db.prepare('SELECT id FROM expeditions WHERE player_id = ? AND finished_at IS NULL').get(id) as { id: string } | undefined;
    if (open) db.prepare('UPDATE expeditions SET finished_at = ?, flags = flags || \'restarted,\' WHERE id = ?').run(now, open.id);

    const rewardedToday = (
      db
        .prepare('SELECT COUNT(*) AS n FROM expeditions WHERE player_id = ? AND rewarded = 1 AND started_at >= ?')
        .get(id, startOfDay(day)) as { n: number }
    ).n;
    const status = getPlayer(db, id)!.status;
    const rewarded = status === 'ok' && rewardedToday < config.tablets.rewardedPerDay;
    const n = config.tablets.perExpedition;
    const qs = pick(db, bank, id, n);
    const expId = 'e_' + randomBytes(8).toString('hex');
    db.prepare('INSERT INTO expeditions (id, player_id, started_at, tablet_count, rewarded) VALUES (?, ?, ?, ?, ?)').run(
      expId,
      id,
      now,
      n,
      rewarded ? 1 : 0,
    );
    const ins = db.prepare('INSERT INTO tablets (expedition_id, idx, question_id) VALUES (?, ?, ?)');
    qs.forEach((q, i) => ins.run(expId, i, q.id));
    return c.json({ expeditionId: expId, tabletCount: n, rewarded, tabletFractions: fractions(n), startedAt: now }, 201);
  });

  interface ExpRow { id: string; player_id: string; started_at: number; finished_at: number | null; tablet_count: number; rewarded: number }
  const getExp = (c: any): ExpRow | null => {
    const row = db.prepare('SELECT * FROM expeditions WHERE id = ?').get(c.req.param('id')) as ExpRow | undefined;
    return row && row.player_id === c.get('playerId') ? row : null;
  };

  /** Issue one signed, single-use question. The tablet's run-fraction is checked for plausibility. */
  app.post('/v1/expeditions/:id/tablets/:idx', auth, (c) => {
    const exp = getExp(c);
    if (!exp) return c.json({ error: 'not_found' }, 404);
    if (exp.finished_at) return c.json({ error: 'expedition_over' }, 409);
    const idx = Number(c.req.param('idx'));
    const t = db.prepare('SELECT * FROM tablets WHERE expedition_id = ? AND idx = ?').get(exp.id, idx) as any;
    if (!t) return c.json({ error: 'not_found' }, 404);
    if (t.issued_at) return c.json({ error: 'already_issued' }, 409);
    // Earlier tablets must be answered first — the run is linear.
    const unanswered = db
      .prepare('SELECT COUNT(*) AS n FROM tablets WHERE expedition_id = ? AND idx < ? AND answered_at IS NULL')
      .get(exp.id, idx) as { n: number };
    if (unanswered.n > 0) return c.json({ error: 'out_of_order' }, 409);
    const now = Date.now();
    const minReach = fractions(exp.tablet_count)[idx] * config.run.minFinishMs * config.run.tabletFractionSlack;
    const flags: string[] = [];
    if (now - exp.started_at < minReach) flags.push(`tablet${idx}_early`);
    const q = bank.get(t.question_id)!;
    const order = shuffled([0, ...q.distractors.map((_, i) => i + 1)]);
    const nonce = randomBytes(9).toString('base64url');
    const expiresAt = now + config.tablets.answerWindowMs + config.tablets.graceMs;
    db.prepare('UPDATE tablets SET nonce = ?, issued_at = ?, expires_at = ?, option_order = ? WHERE expedition_id = ? AND idx = ?').run(
      nonce,
      now,
      expiresAt,
      JSON.stringify(order),
      exp.id,
      idx,
    );
    if (flags.length) db.prepare('UPDATE expeditions SET flags = flags || ? WHERE id = ?').run(flags.join(',') + ',', exp.id);
    const all = [q.correct, ...q.distractors];
    return c.json({
      token: signTablet(exp.id, idx, nonce, expiresAt),
      index: idx + 1,
      total: exp.tablet_count,
      tier: q.tier,
      section: q.section,
      prompt: q.prompt,
      options: order.map((i) => all[i]),
      minLatencyMs: config.tablets.minLatencyMs[q.tier],
      windowMs: config.tablets.answerWindowMs,
    });
  });

  app.post('/v1/expeditions/:id/tablets/:idx/answer', auth, async (c) => {
    const exp = getExp(c);
    if (!exp) return c.json({ error: 'not_found' }, 404);
    const idx = Number(c.req.param('idx'));
    const body = (await c.req.json().catch(() => ({}))) as { token?: string; choice?: number | null };
    const sig = typeof body.token === 'string' ? verifyTablet(body.token) : null;
    if (!sig || sig.expeditionId !== exp.id || sig.idx !== idx) return c.json({ error: 'bad_token' }, 400);
    const t = db.prepare('SELECT * FROM tablets WHERE expedition_id = ? AND idx = ?').get(exp.id, idx) as any;
    if (!t || t.nonce !== sig.nonce) return c.json({ error: 'bad_token' }, 400);
    if (t.answered_at) return c.json({ error: 'already_answered' }, 409);
    const now = Date.now();
    const latency = now - t.issued_at;
    const q = bank.get(t.question_id)!;
    const order = JSON.parse(t.option_order) as number[];
    const all = [q.correct, ...q.distractors];
    // choice = index into the options array we sent; null = timed out.
    const choice = typeof body.choice === 'number' && body.choice >= 0 && body.choice < order.length ? body.choice : null;
    const tooFast = latency < config.tablets.minLatencyMs[q.tier];
    const tooLate = now > t.expires_at;
    const correct = choice !== null && !tooFast && !tooLate && order[choice] === 0;
    const flags: string[] = [];
    if (tooFast) flags.push(`tablet${idx}_fast`);
    if (tooLate) flags.push(`tablet${idx}_late`);
    db.prepare('UPDATE tablets SET answered_at = ?, choice = ?, correct = ?, latency_ms = ? WHERE expedition_id = ? AND idx = ?').run(
      now,
      choice,
      correct ? 1 : 0,
      latency,
      exp.id,
      idx,
    );
    if (flags.length) db.prepare('UPDATE expeditions SET flags = flags || ? WHERE id = ?').run(flags.join(',') + ',', exp.id);
    record(db, exp.player_id, q.id, correct);
    return c.json({
      correct,
      correctOption: order.indexOf(0),
      correctText: all[0],
      explanation: q.explanation,
      source: q.source,
      reason: tooFast ? 'too_fast' : tooLate ? 'timed_out' : choice === null ? 'timed_out' : undefined,
    });
  });

  app.post('/v1/expeditions/:id/finish', auth, async (c) => {
    // The body is read FIRST, deliberately. An `await` between the
    // already-finished check and the write is a TOCTOU window: concurrent
    // requests all parked on the body, all passed the guard, and all paid out.
    // One honest 160 XP expedition became 16,000 XP from 100 held-back finishes.
    const body = (await c.req.json().catch(() => ({}))) as { stumbles?: number; runMs?: number };

    const exp = getExp(c);
    if (!exp) return c.json({ error: 'not_found' }, 404);
    const id = exp.player_id;
    const now = Date.now();

    const replay = () => {
      const row = db.prepare('SELECT right_count, complete, xp_gained, rewarded FROM expeditions WHERE id = ?').get(exp.id) as any;
      return c.json({ xpGained: row.xp_gained, badges: [], complete: !!row.complete, right: row.right_count, total: exp.tablet_count, rewarded: !!row.rewarded, replay: true, progress: snapshot(db, id) });
    };
    if (exp.finished_at) return replay(); // fast path for an honest retry

    // Claim the expedition atomically. A single SQLite UPDATE is the whole
    // check-and-set, so of any number of concurrent finishes exactly one sees
    // changes === 1 and the rest fall through to the idempotent replay. There
    // is no `await` anywhere below this line.
    const claimed = db
      .prepare('UPDATE expeditions SET finished_at = ? WHERE id = ? AND finished_at IS NULL')
      .run(now, exp.id);
    if (claimed.changes === 0) return replay();
    const tabs = db.prepare('SELECT correct, answered_at FROM tablets WHERE expedition_id = ? ORDER BY idx').all(exp.id) as any[];
    const answered = tabs.filter((t) => t.answered_at).length;
    const right = tabs.filter((t) => t.correct).length;
    const flags: string[] = [];
    if (answered < exp.tablet_count) flags.push('tablets_skipped');
    if (now - exp.started_at < config.run.minFinishMs) flags.push('finish_early');
    const plausible = flags.length === 0;
    const complete = plausible && right === exp.tablet_count;
    let gained = 0;
    if (exp.rewarded && plausible) {
      gained = right * config.xp.tablet + (complete ? config.xp.expedition : 0);
    }
    db.prepare(
      `UPDATE expeditions SET right_count = ?, complete = ?, xp_gained = ?, stumbles = ?, client_run_ms = ?,
       flags = flags || ? WHERE id = ?`,
    ).run(right, complete ? 1 : 0, gained, intOrNull(body.stumbles), intOrNull(body.runMs), flags.length ? flags.join(',') + ',' : '', exp.id);
    db.prepare(
      'UPDATE players SET expeditions = expeditions + 1, expeditions_complete = expeditions_complete + ?, tablets_correct = tablets_correct + ? WHERE id = ?',
    ).run(complete ? 1 : 0, plausible ? right : 0, id);
    awardXp(db, id, gained, 'expedition', exp.id);
    const badges = checkBadges(db, id);
    return c.json({ xpGained: gained, badges, complete, right, total: exp.tablet_count, rewarded: !!exp.rewarded, plausible, flags, progress: snapshot(db, id) });
  });

  // ----------------------------------------------------------------- ledger
  const ledgerState = (id: string, day: number) => {
    const p = puzzleFor(day);
    const row = db.prepare('SELECT * FROM ledger_plays WHERE player_id = ? AND day = ?').get(id, day) as any;
    const guesses: string[] = row ? JSON.parse(row.guesses) : [];
    const over = !!row?.over;
    return {
      day,
      kind: p.kind,
      length: p.answer.length,
      clue: p.clue,
      attempts: config.ledger.attempts,
      guesses,
      marks: guesses.map((g) => markGuess(g, p.answer)),
      solved: !!row?.solved,
      over,
      xpGained: row?.xp_gained ?? 0,
      // The answer and its source are revealed only once the play is over.
      answer: over ? p.answer : undefined,
      source: over ? p.source : undefined,
      streak: getPlayer(db, id)!.streak,
    };
  };

  app.get('/v1/ledger/today', auth, (c) => c.json(ledgerState(c.get('playerId'), todayIndex())));

  app.post('/v1/ledger/guess', auth, async (c) => {
    const id = c.get('playerId');
    const day = todayIndex();
    const p = puzzleFor(day);
    const body = (await c.req.json().catch(() => ({}))) as { guess?: string };
    const guess = String(body.guess ?? '').toUpperCase();
    if (!validGuess(guess, p)) return c.json({ error: 'invalid_guess', ...ledgerState(id, day) }, 400);
    const row = db.prepare('SELECT * FROM ledger_plays WHERE player_id = ? AND day = ?').get(id, day) as any;
    const guesses: string[] = row ? JSON.parse(row.guesses) : [];
    if (row?.over) return c.json({ error: 'ledger_over', ...ledgerState(id, day) }, 409);
    guesses.push(guess);
    const solved = guess === p.answer;
    const over = solved || guesses.length >= config.ledger.attempts;
    const now = Date.now();
    let gained = 0;
    if (over) {
      const pl = getPlayer(db, id)!;
      let streak = pl.streak;
      if (pl.last_ledger_day !== day) streak = pl.last_ledger_day === day - 1 ? streak + 1 : 1;
      if (solved && pl.status === 'ok') {
        gained = config.xp.ledger + (streak > 0 && streak % 7 === 0 ? config.xp.streak7 : 0);
      }
      db.prepare('UPDATE players SET ledgers_solved = ledgers_solved + ?, streak = ?, last_ledger_day = ? WHERE id = ?').run(
        solved ? 1 : 0,
        streak,
        day,
        id,
      );
      awardXp(db, id, gained, 'ledger', String(day));
    }
    db.prepare(
      `INSERT INTO ledger_plays (player_id, day, guesses, solved, over, xp_gained, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)
       ON CONFLICT(player_id, day) DO UPDATE SET guesses = excluded.guesses, solved = excluded.solved, over = excluded.over,
       xp_gained = excluded.xp_gained, updated_at = excluded.updated_at`,
    ).run(id, day, JSON.stringify(guesses), solved ? 1 : 0, over ? 1 : 0, gained, now);
    const badges = over ? checkBadges(db, id) : [];
    return c.json({ ...ledgerState(id, day), badges, progress: snapshot(db, id) });
  });

  // ------------------------------------------------------------- mini-games
  //
  // XP only (plan §4.2). The content for these games lives in the client, so
  // the server cannot mark the answers — but it can, and now does, refuse to
  // pay for a round it never issued.
  //
  // A round is opened by POST /v1/mini/:game/start, which returns a signed
  // single-use token, and claimed by POST /v1/mini/:game. The claim checks the
  // signature, that the round belongs to the caller, that it has not already
  // been claimed, and that it took a plausible amount of wall-clock time.
  //
  // What this does NOT do is verify that the reported score is the score the
  // player achieved. That needs the content moved server-side the way the
  // question bank already is. Until then the weekly board is best understood
  // as "played a lot", not "played well", and the daily cap is what bounds it.
  const miniGames = new Set(['pillar_sort', 'design_or_myth', 'chain_builder', 'coin_quest']);

  app.post('/v1/mini/:game/start', auth, (c) => {
    const id = c.get('playerId');
    const game = c.req.param('game');
    if (!miniGames.has(game)) return c.json({ error: 'unknown_game' }, 404);
    const now = Date.now();
    const day = todayIndex();
    const roundId = 'm_' + randomBytes(8).toString('hex');
    const nonce = randomBytes(9).toString('base64url');
    db.prepare(
      'INSERT INTO mini_rounds (id, player_id, game, day, right, total, extra, xp_gained, created_at, nonce, started_at) VALUES (?, ?, ?, ?, 0, 0, 0, 0, ?, ?, ?)',
    ).run(roundId, id, game, day, now, nonce, now);
    return c.json({ token: signMini(roundId, nonce, now + config.mini.maxDurationMs) }, 201);
  });

  app.post('/v1/mini/:game', auth, async (c) => {
    const id = c.get('playerId');
    const game = c.req.param('game');
    if (!miniGames.has(game)) return c.json({ error: 'unknown_game' }, 404);
    // Read the body before any check-then-write, for the same TOCTOU reason as
    // the expedition finish above.
    const body = (await c.req.json().catch(() => ({}))) as { right?: number; total?: number; extra?: number; token?: string };

    const parsed = typeof body.token === 'string' ? verifyMini(body.token) : null;
    if (!parsed) return c.json({ error: 'round_token_required' }, 400);
    const now = Date.now();
    if (now > parsed.expiresAt) return c.json({ error: 'round_expired' }, 409);

    const round = db
      .prepare('SELECT id, player_id, game, day, nonce, started_at, claimed_at FROM mini_rounds WHERE id = ?')
      .get(parsed.roundId) as
      | { id: string; player_id: string; game: string; day: number; nonce: string | null; started_at: number | null; claimed_at: number | null }
      | undefined;
    if (!round || round.player_id !== id || round.game !== game) return c.json({ error: 'round_not_found' }, 404);
    if (round.nonce !== parsed.nonce) return c.json({ error: 'round_not_found' }, 404);
    if (round.claimed_at) return c.json({ error: 'already_claimed' }, 409);
    if (round.started_at === null) return c.json({ error: 'round_not_found' }, 404);

    const elapsed = now - round.started_at;
    const floor = config.mini.minDurationMs[game] ?? 10_000;
    if (elapsed < floor) return c.json({ error: 'too_fast' }, 409);

    // Claim atomically: exactly one concurrent request can set claimed_at.
    const claimed = db
      .prepare('UPDATE mini_rounds SET claimed_at = ? WHERE id = ? AND claimed_at IS NULL')
      .run(now, round.id);
    if (claimed.changes === 0) return c.json({ error: 'already_claimed' }, 409);

    const cap = config.mini.maxRight[game] ?? 24;
    const right = uint(body.right, cap);
    const total = Math.max(right, uint(body.total, cap));
    const extra = uint(body.extra, 10_000);
    // A round belongs to the day it was OPENED, and the cap counts that day.
    // Counting by the claim day let rounds opened before UTC midnight and
    // claimed after it pay in full: none of them carried the new day, so the
    // count was 0 for every claim (audit 2026-09-18, R1).
    // The open round itself is one of the day's rounds, so exclude it.
    const rounds = (
      db
        .prepare('SELECT COUNT(*) AS n FROM mini_rounds WHERE player_id = ? AND game = ? AND day = ? AND id != ? AND claimed_at IS NOT NULL')
        .get(id, game, round.day, round.id) as { n: number }
    ).n;
    let gained = 0;
    const status = getPlayer(db, id)!.status;
    if (status === 'ok' && rounds < config.mini.rewardedRoundsPerDay) {
      if (game === 'coin_quest') {
        // right = stars earned (0-3), extra = level id. Clearing a level is
        // worth XP; replaying a cleared level for a better star is worth less.
        gained = Math.min(3, right) * 20 + (right >= 3 ? 20 : 0);
      } else if (game === 'chain_builder') {
        gained = Math.min(right, 3) * config.xp.chainSolved - extra * config.xp.chainExtraCheck;
      } else {
        const cap = game === 'pillar_sort' ? 24 : 16;
        const clean = game === 'pillar_sort' ? 12 : 10;
        const r = Math.min(right, cap);
        gained = r * config.xp.miniPerRight + (r >= clean && r === total ? config.xp.miniCleanBonus : 0);
      }
      gained = Math.max(0, Math.min(config.mini.maxXpPerRound, gained));
    }
    db.prepare('UPDATE mini_rounds SET right = ?, total = ?, extra = ?, xp_gained = ? WHERE id = ?').run(
      right,
      total,
      extra,
      gained,
      round.id,
    );
    awardXp(db, id, gained, 'mini', round.id);
    const badges = checkBadges(db, id);
    return c.json({ xpGained: gained, badges, rewardedRoundsLeft: Math.max(0, config.mini.rewardedRoundsPerDay - rounds - 1), progress: snapshot(db, id) });
  });

  // ------------------------------------------------------------ scoreboard
  // Weekly XP, Monday 00:00 UTC reset. Recognition only: no prize attaches to
  // a rank, and XP has no monetary value (plan §4.2). Banned accounts are
  // excluded; flagged accounts earn no XP and so never climb.
  app.get('/v1/leaderboard', auth, (c) => {
    const id = c.get('playerId');
    ensureHandle(db, id);
    // Math.min/max propagate NaN, so `?limit=abc` used to reach SQLite as
    // `LIMIT NaN` and 500. uint() rejects non-finite input before the clamp.
    const limit = Math.max(3, uint(c.req.query('limit') ?? 50, 100, 50));
    return c.json(leaderboard(db, id, limit));
  });

  /** Assigns a fresh handle. Capped per day so the board stays recognizable. */
  app.post('/v1/me/handle/reroll', auth, (c) => {
    const id = c.get('playerId');
    const day = todayIndex();
    const row = db.prepare('SELECT handle_rerolls, handle_reroll_day FROM players WHERE id = ?').get(id) as {
      handle_rerolls: number;
      handle_reroll_day: number | null;
    };
    const usedToday = row.handle_reroll_day === day ? row.handle_rerolls : 0;
    if (usedToday >= maxRerollsPerDay) {
      return c.json({ error: 'reroll_limit', rerollsLeft: 0, handle: ensureHandle(db, id) }, 429);
    }
    if (row.handle_reroll_day !== day) {
      db.prepare('UPDATE players SET handle_rerolls = 0, handle_reroll_day = ? WHERE id = ?').run(day, id);
    }
    const handle = rerollHandle(db, id);
    return c.json({ handle, rerollsLeft: maxRerollsPerDay - usedToday - 1 });
  });

  /**
   * Erases the player and everything keyed to them. Irreversible.
   *
   * Both app stores ask whether users can request deletion of their data, and
   * "no" is a poor answer for an app that could simply support it. There are no
   * accounts here — no name, email or phone is ever collected — so this is the
   * only deletion there is to offer.
   *
   * Two things are easy to get wrong and are handled explicitly:
   *
   *  - **`tablets` is keyed to `expedition_id`, not `player_id`.** Deleting by
   *    player alone would leave its rows behind, orphaned and still holding
   *    which questions this person was asked. It is deleted through the
   *    expedition join, and it has to go first.
   *  - **All of it, or none of it.** A half-finished delete would leave a
   *    player row gone but its XP ledger intact, which is worse than not
   *    deleting at all — the record survives with nothing left to explain it.
   *    The whole thing runs in one transaction.
   *
   * The bearer token is not revoked separately: it is only ever resolved by
   * hashing it against `players.token_hash`, so removing the row is what makes
   * it stop working. The client is expected to discard its stored token and
   * register again if the player keeps playing.
   */
  app.delete('/v1/me', auth, (c) => {
    const id = c.get('playerId');

    // node:sqlite has no transaction() wrapper — that is better-sqlite3's API —
    // so BEGIN/COMMIT are explicit, with a ROLLBACK on any failure.
    const rows: Record<string, number> = {};
    db.exec('BEGIN');
    try {
      rows.tablets = Number(
        db
          .prepare('DELETE FROM tablets WHERE expedition_id IN (SELECT id FROM expeditions WHERE player_id = ?)')
          .run(id).changes,
      );
      // Children before parents: foreign_keys is ON, so players must be last.
      for (const table of ['expeditions', 'badges', 'tablet_state', 'ledger_plays', 'mini_rounds', 'xp_events']) {
        rows[table] = Number(db.prepare(`DELETE FROM ${table} WHERE player_id = ?`).run(id).changes);
      }
      rows.players = Number(db.prepare('DELETE FROM players WHERE id = ?').run(id).changes);
      db.exec('COMMIT');
    } catch (err) {
      db.exec('ROLLBACK');
      throw err;
    }

    return c.json({ deleted: true, rows });
  });

  return app;
}
