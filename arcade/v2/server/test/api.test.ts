import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
import { openDb } from '../src/db.ts';
import { QuestionBank } from '../src/bank.ts';
import { createApp } from '../src/app.ts';
import { config } from '../src/config.ts';
import { markGuess, puzzleFor, todayIndex } from '../src/ledger.ts';

// Time control: the app reads Date.now(); we shift a global offset so tests
// can "wait" without sleeping.
let offset = 0;
const realNow = Date.now;
before(() => {
  Date.now = () => realNow() + offset;
});
after(() => {
  Date.now = realNow;
});
const advance = (ms: number) => (offset += ms);

const db = openDb(':memory:');
const bank = QuestionBank.fromFile(fileURLToPath(new URL('../data/question-bank-seed.md', import.meta.url)));
const app = createApp(db, bank);

// Each unauthenticated call comes from its own address. Registration now has
// an hourly per-address cap (audit R3), and this file creates well over ten
// players; without distinct sockets they would all share one bucket and the
// eleventh would be a 429 that has nothing to do with the test in hand.
let nextAddr = 0;
async function call(method: string, path: string, body?: unknown, token?: string) {
  const env = token ? undefined : { incoming: { socket: { remoteAddress: `198.18.${(nextAddr >> 8) & 255}.${nextAddr++ & 255}` } } };
  const res = await app.request(
    path,
    {
      method,
      headers: { 'content-type': 'application/json', ...(token ? { authorization: `Bearer ${token}` } : {}) },
      body: body === undefined ? undefined : JSON.stringify(body),
    },
    env as any,
  );
  return { status: res.status, json: (await res.json()) as any };
}

let token = '';

test('bank parses the seed', () => {
  assert.ok(bank.items.length >= 40, `only ${bank.items.length} items`);
  for (const q of bank.items) {
    assert.ok(q.correct && q.source, q.prompt);
    // True/false traps have one distractor; everything else needs at least two.
    assert.ok(q.distractors.length >= (/^true or false/i.test(q.prompt) ? 1 : 2), q.prompt);
  }
});

test('anonymous player + me', async () => {
  const r = await call('POST', '/v1/players', { deviceHint: 'test' });
  assert.equal(r.status, 201);
  token = r.json.token;
  assert.equal(r.json.progress.xp, 0);
  const me = await call('GET', '/v1/me', undefined, token);
  assert.equal(me.status, 200);
  assert.equal(me.json.level, 1);
  assert.equal((await call('GET', '/v1/me', undefined, 'nope')).status, 401);
});

/** Plays one expedition; `answerFn` decides each tablet. Returns the finish body. */
async function playExpedition(answerFn: (t: any, idx: number) => Promise<{ choice: number | null; token: string }>, finishEarly = false) {
  const start = await call('POST', '/v1/expeditions', {}, token);
  assert.equal(start.status, 201);
  const exp = start.json.expeditionId;
  const n = start.json.tabletCount as number;
  for (let i = 0; i < n; i++) {
    // Reach the tablet at a human pace.
    advance(Math.ceil(start.json.tabletFractions[i] * config.run.minFinishMs) + 2000 - (i ? 0 : 0));
    const t = await call('POST', `/v1/expeditions/${exp}/tablets/${i}`, {}, token);
    assert.equal(t.status, 200, JSON.stringify(t.json));
    assert.ok(!('correctText' in t.json), 'answer key must not be sent with the question');
    const a = await answerFn(t.json, i);
    const ans = await call('POST', `/v1/expeditions/${exp}/tablets/${i}/answer`, a, token);
    assert.equal(ans.status, 200, JSON.stringify(ans.json));
  }
  if (!finishEarly) advance(config.run.minFinishMs + 5000);
  const fin = await call('POST', `/v1/expeditions/${exp}/finish`, { stumbles: 1, runMs: 100000 }, token);
  assert.equal(fin.status, 200);
  return { exp, fin: fin.json, n };
}

const pickCorrect = (t: any) => {
  // Test-only oracle: look the prompt up in the bank.
  const q = bank.items.find((q) => q.prompt === t.prompt)!;
  return t.options.indexOf(q.correct);
};

test('honest full expedition scores tablets + completion', async () => {
  offset = 0;
  const { fin, n } = await playExpedition(async (t) => {
    advance(t.minLatencyMs + 800);
    return { choice: pickCorrect(t), token: t.token };
  });
  assert.equal(fin.plausible, true, JSON.stringify(fin.flags));
  assert.equal(fin.right, n);
  assert.equal(fin.complete, true);
  assert.equal(fin.xpGained, n * config.xp.tablet + config.xp.expedition);
  assert.ok(fin.badges.includes('first_expedition'));
});

test('answers faster than the tier minimum are scored wrong and flagged', async () => {
  const { exp, fin } = await playExpedition(async (t, i) => {
    advance(i === 0 ? 200 : t.minLatencyMs + 500); // first tablet: bot speed
    return { choice: pickCorrect(t), token: t.token };
  });
  assert.equal(fin.right, fin.total - 1);
  assert.equal(fin.complete, false);
  assert.equal(fin.plausible, true); // the run itself was fine; the fast answer is a per-tablet flag
  const row = db.prepare('SELECT flags FROM expeditions WHERE id = ?').get(exp) as any;
  assert.match(row.flags, /tablet0_fast/);
});

test('a question token cannot be replayed or answered after expiry', async () => {
  const start = await call('POST', '/v1/expeditions', {}, token);
  const exp = start.json.expeditionId;
  advance(40_000);
  const t = await call('POST', `/v1/expeditions/${exp}/tablets/0`, {}, token);
  advance(t.json.minLatencyMs + 100);
  const first = await call('POST', `/v1/expeditions/${exp}/tablets/0/answer`, { choice: 0, token: t.json.token }, token);
  assert.equal(first.status, 200);
  const replay = await call('POST', `/v1/expeditions/${exp}/tablets/0/answer`, { choice: 1, token: t.json.token }, token);
  assert.equal(replay.status, 409);
  const reissue = await call('POST', `/v1/expeditions/${exp}/tablets/0`, {}, token);
  assert.equal(reissue.status, 409);
  // Tablet 2 before tablet 1 → out of order.
  assert.equal((await call('POST', `/v1/expeditions/${exp}/tablets/2`, {}, token)).status, 409);
  // Forged signature.
  const forged = t.json.token.replace(/\.[^.]+$/, '.AAAA');
  advance(70_000);
  const t1 = await call('POST', `/v1/expeditions/${exp}/tablets/1`, {}, token);
  assert.equal((await call('POST', `/v1/expeditions/${exp}/tablets/1/answer`, { choice: 0, token: forged }, token)).status, 400);
  // Let it expire.
  advance(config.tablets.answerWindowMs + config.tablets.graceMs + 1000);
  const late = await call('POST', `/v1/expeditions/${exp}/tablets/1/answer`, { choice: pickCorrect(t1.json), token: t1.json.token }, token);
  assert.equal(late.json.correct, false);
  assert.equal(late.json.reason, 'timed_out');
});

test('finishing a 100-second run in 9 seconds earns nothing', async () => {
  const before = (await call('GET', '/v1/me', undefined, token)).json.xp;
  const start = await call('POST', '/v1/expeditions', {}, token);
  const exp = start.json.expeditionId;
  for (let i = 0; i < start.json.tabletCount; i++) {
    advance(3000);
    const t = await call('POST', `/v1/expeditions/${exp}/tablets/${i}`, {}, token);
    advance(t.json.minLatencyMs + 100);
    await call('POST', `/v1/expeditions/${exp}/tablets/${i}/answer`, { choice: pickCorrect(t.json), token: t.json.token }, token);
  }
  const fin = await call('POST', `/v1/expeditions/${exp}/finish`, {}, token);
  assert.equal(fin.json.plausible, false);
  assert.ok(fin.json.flags.includes('finish_early'));
  assert.equal(fin.json.xpGained, 0);
  assert.equal((await call('GET', '/v1/me', undefined, token)).json.xp, before);
  // Finish is idempotent.
  const again = await call('POST', `/v1/expeditions/${exp}/finish`, {}, token);
  assert.equal(again.json.replay, true);
});

test('rewarded expeditions are capped per day; extra runs are practice', async () => {
  const fresh = (await call('POST', '/v1/players', {})).json.token;
  const saved = token;
  token = fresh;
  let rewardedCount = 0;
  for (let k = 0; k < config.tablets.rewardedPerDay + 1; k++) {
    const start = await call('POST', '/v1/expeditions', {}, token);
    if (start.json.rewarded) rewardedCount++;
    await call('POST', `/v1/expeditions/${start.json.expeditionId}/finish`, {}, token);
  }
  assert.equal(rewardedCount, config.tablets.rewardedPerDay);
  token = saved;
});

test('daily ledger: answer hidden until over, fixed XP, streak', async () => {
  const fresh = (await call('POST', '/v1/players', {})).json.token;
  const day = todayIndex();
  const p = puzzleFor(day);
  const today = await call('GET', '/v1/ledger/today', undefined, fresh);
  assert.equal(today.json.length, p.answer.length);
  assert.equal(today.json.answer, undefined);
  const bad = await call('POST', '/v1/ledger/guess', { guess: 'x' }, fresh);
  assert.equal(bad.status, 400);
  // One wrong guess of the right shape, then the answer.
  const wrong = p.kind === 'word' ? 'A'.repeat(p.answer.length) : '9'.repeat(p.answer.length);
  const g1 = await call('POST', '/v1/ledger/guess', { guess: wrong }, fresh);
  assert.equal(g1.status, 200);
  assert.deepEqual(g1.json.marks[0], markGuess(wrong, p.answer));
  assert.equal(g1.json.over, false);
  const g2 = await call('POST', '/v1/ledger/guess', { guess: p.answer }, fresh);
  assert.equal(g2.json.solved, true);
  assert.equal(g2.json.answer, p.answer);
  assert.equal(g2.json.xpGained, config.xp.ledger);
  assert.equal(g2.json.streak, 1);
  assert.equal((await call('POST', '/v1/ledger/guess', { guess: p.answer }, fresh)).status, 409);
});

test('every player gets an assigned handle, never a typed one', async () => {
  const r = await call('POST', '/v1/players', {});
  assert.match(r.json.progress.handle, /^[A-Z][a-z]+ [A-Z][a-z]+ \d{3,4}$/);
  const me = await call('GET', '/v1/me', undefined, r.json.token);
  assert.equal(me.json.handle, r.json.progress.handle);
  // Re-roll gives a different handle and is capped per day.
  const first = me.json.handle;
  let last = first;
  for (let i = 0; i < 3; i++) {
    const roll = await call('POST', '/v1/me/handle/reroll', {}, r.json.token);
    assert.equal(roll.status, 200);
    last = roll.json.handle;
  }
  assert.notEqual(last, first);
  const over = await call('POST', '/v1/me/handle/reroll', {}, r.json.token);
  assert.equal(over.status, 429);
});

test('weekly board ranks by XP earned this week and shows your own standing', async () => {
  // Three fresh players with different weekly XP (the board is global, so
  // assert their order relative to each other, not absolute positions).
  const tokens: string[] = [];
  const handles: string[] = [];
  for (let i = 0; i < 3; i++) {
    const p = await call('POST', '/v1/players', {});
    tokens.push(p.json.token);
    handles.push(p.json.progress.handle);
  }
  await playMini('pillar_sort', { right: 20, total: 20 }, tokens[0]); // 100 + 40
  await playMini('pillar_sort', { right: 4, total: 9 }, tokens[1]); // 20
  await playMini('pillar_sort', { right: 10, total: 19 }, tokens[2]); // 50

  const board = (await call('GET', '/v1/leaderboard', undefined, tokens[1])).json;
  assert.equal(board.board, 'weekly_xp');
  const scores = board.rows.map((r: any) => r.xp);
  assert.deepEqual([...scores].sort((a, b) => b - a), scores, 'rows must be descending');
  const at = (h: string) => board.rows.findIndex((r: any) => r.handle === h);
  assert.ok(at(handles[0]) >= 0 && at(handles[1]) >= 0 && at(handles[2]) >= 0);
  assert.ok(at(handles[0]) < at(handles[2]) && at(handles[2]) < at(handles[1]), 'ordered 140 > 50 > 20');
  assert.equal(board.rows[at(handles[0])].xp, 140);
  // The caller is marked, and their own standing is reported either way.
  assert.equal(board.rows.filter((r: any) => r.you).length, 1);
  assert.equal(board.rows[at(handles[1])].you, true);
  assert.equal(board.you.xp, 20);
  assert.equal(board.you.handle, handles[1]);
  assert.equal(board.you.rank, board.rows[at(handles[1])].rank);
  // No player ids or tokens leak onto a public board.
  const text = JSON.stringify(board);
  assert.ok(!text.includes('p_'), 'player ids must not appear on the board');
  assert.ok(!text.includes(tokens[1]));
});

test('XP earned before this week does not count toward the weekly board', async () => {
  const t = (await call('POST', '/v1/players', {})).json.token;
  await playMini('design_or_myth', { right: 16, total: 16 }, t); // 80 + 40 this week
  const before = (await call('GET', '/v1/leaderboard', undefined, t)).json;
  assert.equal(before.you.xp, 120);
  advance(8 * 86_400_000); // next week
  const after = (await call('GET', '/v1/leaderboard', undefined, t)).json;
  assert.equal(after.you.xp, 0);
  assert.equal(after.you.rank, null);
  assert.ok(after.weekStart > before.weekStart);
  // Lifetime XP is untouched by the reset.
  assert.equal((await call('GET', '/v1/me', undefined, t)).json.xp, 120);
  advance(-8 * 86_400_000);
});

test('banned accounts are excluded from the board', async () => {
  const t = (await call('POST', '/v1/players', {})).json.token;
  const me = await call('GET', '/v1/me', undefined, t);
  await playMini('pillar_sort', { right: 24, total: 24 }, t); // would be top
  const handle = me.json.handle;
  assert.ok((await call('GET', '/v1/leaderboard', undefined, t)).json.rows.some((r: any) => r.handle === handle));
  db.prepare("UPDATE players SET status = 'banned' WHERE id = ?").run(me.json.playerId);
  const other = (await call('POST', '/v1/players', {})).json.token;
  const board = (await call('GET', '/v1/leaderboard', undefined, other)).json;
  assert.ok(!board.rows.some((r: any) => r.handle === handle));
  assert.equal((await call('GET', '/v1/leaderboard', undefined, t)).status, 403);
});

/** Opens a server round, waits out its duration floor, and claims it. */
async function playMini(game: string, body: Record<string, unknown>, tok: string) {
  const s = await call('POST', `/v1/mini/${game}/start`, {}, tok);
  assert.equal(s.status, 201, `start ${game}: ${JSON.stringify(s.json)}`);
  advance((config.mini.minDurationMs[game] ?? 10_000) + 1000);
  return call('POST', `/v1/mini/${game}`, { ...body, token: s.json.token }, tok);
}

test('mini-game XP follows the formula and stops after the daily cap', async () => {
  const fresh = (await call('POST', '/v1/players', {})).json.token;
  const r = await playMini('pillar_sort', { right: 14, total: 14 }, fresh);
  assert.equal(r.json.xpGained, 14 * config.xp.miniPerRight + config.xp.miniCleanBonus);
  const c = await playMini('chain_builder', { right: 3, total: 3, extra: 2 }, fresh);
  assert.equal(c.json.xpGained, 3 * config.xp.chainSolved - 2 * config.xp.chainExtraCheck);
  assert.equal((await call('POST', '/v1/mini/slots', { right: 1, total: 1 }, fresh)).status, 404);
  let last = 0;
  for (let i = 0; i < config.mini.rewardedRoundsPerDay + 2; i++) {
    last = (await playMini('design_or_myth', { right: 5, total: 16 }, fresh)).json.xpGained;
  }
  assert.equal(last, 0);
});

test('passage pays for stars, the full passage, and a capped coin score', async () => {
  const fresh = (await call('POST', '/v1/players', {})).json.token;
  const { perPoints, cap } = config.mini.scoreXp.passage;
  // A short landing with no coins: one star, nothing else.
  assert.equal((await playMini('passage', { right: 1, total: 3, extra: 3 }, fresh)).json.xpGained, 12);
  // The whole passage, hard landing, a modest score.
  assert.equal(
    (await playMini('passage', { right: 2, total: 3, extra: 9, score: perPoints * 2 }, fresh)).json.xpGained,
    2 * 12 + 24 + 2,
  );
  // Three stars and a score past the cap: the bonus stops at the cap.
  assert.equal(
    (await playMini('passage', { right: 3, total: 3, extra: 9, score: 999_999 }, fresh)).json.xpGained,
    3 * 12 + 24 + cap,
  );
  // A score that would round below one point of XP pays no bonus.
  assert.equal(
    (await playMini('passage', { right: 3, total: 3, extra: 9, score: perPoints - 1 }, fresh)).json.xpGained,
    3 * 12 + 24,
  );
  // The stored score is the clamped one, not what was sent.
  const stored = db.prepare('SELECT MAX(score) AS s FROM mini_rounds WHERE game = ?').get('passage') as { s: number };
  assert.equal(stored.s, config.mini.maxScore.passage);
  // A game without a score ignores one.
  const r = await playMini('pillar_sort', { right: 14, total: 14, score: 999 }, fresh);
  assert.equal(r.json.xpGained, 14 * config.xp.miniPerRight + config.xp.miniCleanBonus);
  const row = db.prepare('SELECT score FROM mini_rounds WHERE game = ? ORDER BY created_at DESC LIMIT 1').get('pillar_sort') as { score: number };
  assert.equal(row.score, 0);
});

test('the boar grows from points scored on rewarded passage rounds, and only those', async () => {
  const fresh = (await call('POST', '/v1/players', {})).json.token;
  const [, juvenile, razorback] = config.passage.stages;
  const max = config.mini.maxScore.passage;
  const me = (await call('GET', '/v1/me', undefined, fresh)).json;
  const p0 = me.passage;
  assert.deepEqual(
    {
      lifetime: p0.lifetime,
      points: p0.points,
      stage: p0.stage,
      stageAt: p0.stageAt,
      nextStage: p0.nextStage,
      nextAt: p0.nextAt,
      loadout: p0.loadout,
    },
    { lifetime: 0, points: 0, stage: 'piglet', stageAt: 0, nextStage: 'juvenile', nextAt: juvenile.at, loadout: [] },
  );

  // A run's score goes to both totals and comes back on the claim.
  let r = await playMini('passage', { right: 1, total: 3, extra: 2, score: 120 }, fresh);
  assert.equal(r.json.passageCredited, 120);
  assert.equal(r.json.progress.passage.lifetime, 120);
  assert.equal(r.json.progress.passage.points, 120);

  // Another game's score grows nothing, and says nothing about the boar.
  r = await playMini('pillar_sort', { right: 9, total: 9, score: 999 }, fresh);
  assert.equal(r.json.passageCredited, undefined);
  assert.equal(r.json.progress.passage.lifetime, 120);

  // Enough full-score runs cross the juvenile line.
  let lifetime = 120;
  let rounds = 1;
  while (lifetime < juvenile.at) {
    r = await playMini('passage', { right: 3, total: 3, extra: 9, score: max }, fresh);
    lifetime += max;
    rounds++;
  }
  assert.equal(r.json.progress.passage.lifetime, lifetime);
  assert.equal(r.json.progress.passage.stage, 'juvenile');
  assert.equal(r.json.progress.passage.nextStage, 'razorback');

  // Past the daily cap a run is practice: no XP and no growth.
  while (rounds < config.mini.rewardedRoundsPerDay) {
    r = await playMini('passage', { right: 1, total: 3, extra: 1, score: 1 }, fresh);
    lifetime += 1;
    rounds++;
  }
  r = await playMini('passage', { right: 3, total: 3, extra: 9, score: max }, fresh);
  assert.equal(r.json.xpGained, 0);
  assert.equal(r.json.passageCredited, 0);
  assert.equal(r.json.progress.passage.lifetime, lifetime);

  // The last stage has nothing after it.
  const id = (db.prepare('SELECT id FROM players WHERE handle = ?').get(me.handle) as { id: string }).id;
  db.prepare('UPDATE passage_profile SET lifetime = ? WHERE player_id = ?').run(razorback.at, id);
  const top = (await call('GET', '/v1/me', undefined, fresh)).json.passage;
  assert.equal(top.stage, 'razorback');
  assert.equal(top.nextStage, null);
  assert.equal(top.nextAt, null);
});

test('an account on the abuse ladder flies for practice and grows nothing', async () => {
  const fresh = (await call('POST', '/v1/players', {})).json.token;
  const me = (await call('GET', '/v1/me', undefined, fresh)).json;
  db.prepare("UPDATE players SET status = 'xp_only' WHERE handle = ?").run(me.handle);
  const r = await playMini('passage', { right: 3, total: 3, extra: 9, score: 500 }, fresh);
  assert.equal(r.json.passageCredited, 0);
  assert.equal(r.json.progress.passage.lifetime, 0);
});

// --- When Pigs Fly shop and loadout (phase 4)

async function boarWith(points: number) {
  const tok = (await call('POST', '/v1/players', {})).json.token;
  const handle = (await call('GET', '/v1/me', undefined, tok)).json.handle;
  const pid = (db.prepare('SELECT id FROM players WHERE handle = ?').get(handle) as { id: string }).id;
  db.prepare(
    `INSERT INTO passage_profile (player_id, lifetime, points, updated_at) VALUES (?, ?, ?, 0)
     ON CONFLICT(player_id) DO UPDATE SET lifetime = excluded.lifetime, points = excluded.points`,
  ).run(pid, points, points);
  return { tok, pid };
}

const levelOf = (progress: any, ability: string) =>
  progress.passage.abilities.find((a: any) => a.id === ability).level as number;

test('the shop lists every ability with its next price, and sells only for points', async () => {
  const { tok } = await boarWith(0);
  const me = (await call('GET', '/v1/me', undefined, tok)).json;
  assert.deepEqual(
    me.passage.abilities.map((a: any) => [a.id, a.level, a.nextCost]),
    Object.entries(config.passage.abilities).map(([id, costs]) => [id, 0, costs[0]]),
  );
  const broke = await call('POST', '/v1/passage/abilities/dash/upgrade', {}, tok);
  assert.equal(broke.status, 409);
  assert.equal(broke.json.error, 'not_enough_points');
  assert.equal((await call('POST', '/v1/passage/abilities/jetpack/upgrade', {}, tok)).status, 404);
  assert.equal((await call('POST', '/v1/passage/abilities/__proto__/upgrade', {}, tok)).status, 404);
});

test('an upgrade pays from points and never shrinks the boar', async () => {
  const costs = config.passage.abilities.dash;
  const total = costs.reduce((a, b) => a + b, 0);
  const { tok } = await boarWith(total + 5);
  let r;
  for (let lvl = 1; lvl <= costs.length; lvl++) {
    r = await call('POST', '/v1/passage/abilities/dash/upgrade', {}, tok);
    assert.equal(r.status, 200);
    assert.equal(levelOf(r.json.progress, 'dash'), lvl);
  }
  assert.equal(r!.json.progress.passage.points, 5);
  assert.equal(r!.json.progress.passage.lifetime, total + 5, 'spending must not shrink the boar');
  const maxed = await call('POST', '/v1/passage/abilities/dash/upgrade', {}, tok);
  assert.equal(maxed.status, 409);
  assert.equal(maxed.json.error, 'max_level');
});

test('two upgrades landing together pay once', async () => {
  const { tok } = await boarWith(config.passage.abilities.freeze[0]);
  const both = await Promise.all([
    call('POST', '/v1/passage/abilities/freeze/upgrade', {}, tok),
    call('POST', '/v1/passage/abilities/freeze/upgrade', {}, tok),
  ]);
  assert.deepEqual(both.map((r) => r.status).sort(), [200, 409]);
  const me = (await call('GET', '/v1/me', undefined, tok)).json;
  assert.equal(levelOf(me, 'freeze'), 1);
  assert.equal(me.passage.points, 0);
});

test('a loadout is at most two owned abilities', async () => {
  const [d, g, t] = [config.passage.abilities.dash[0], config.passage.abilities.grapple[0], config.passage.abilities.teleport[0]];
  const { tok } = await boarWith(d + g + t);
  for (const a of ['dash', 'grapple', 'teleport']) await call('POST', `/v1/passage/abilities/${a}/upgrade`, {}, tok);
  const set = (abilities: unknown) => call('POST', '/v1/passage/loadout', { abilities }, tok);
  assert.equal((await set(['freeze'])).status, 400, 'not owned');
  assert.equal((await set(['dash', 'dash'])).status, 400, 'duplicate');
  assert.equal((await set(['dash', 'grapple', 'teleport'])).status, 400, 'three');
  assert.equal((await set('dash')).status, 400, 'not a list');
  const ok = await set(['teleport', 'dash']);
  assert.equal(ok.status, 200);
  assert.deepEqual(ok.json.progress.passage.loadout, ['teleport', 'dash']);
  assert.deepEqual((await set([])).json.progress.passage.loadout, []);
});

test('a run that flew with abilities it does not own pays nothing', async () => {
  const { tok } = await boarWith(config.passage.abilities.dash[0]);
  await call('POST', '/v1/passage/abilities/dash/upgrade', {}, tok);
  const honest = await playMini('passage', { right: 1, total: 3, extra: 2, score: 50, loadout: [{ id: 'dash', level: 1 }] }, tok);
  assert.ok(honest.json.xpGained > 0);
  assert.equal(honest.json.passageCredited, 50);
  const unowned = await playMini('passage', { right: 3, total: 3, extra: 9, score: 900, loadout: [{ id: 'teleport', level: 1 }] }, tok);
  assert.equal(unowned.json.xpGained, 0);
  assert.equal(unowned.json.passageCredited, 0);
  assert.equal(unowned.json.loadoutRejected, true);
  const overLevel = await playMini('passage', { right: 3, total: 3, extra: 9, score: 900, loadout: [{ id: 'dash', level: 3 }] }, tok);
  assert.equal(overLevel.json.xpGained, 0);
  assert.equal(overLevel.json.passageCredited, 0);
  assert.equal(overLevel.json.loadoutRejected, true);
  // A run with no abilities at all is always fine, and needs no field.
  assert.ok((await playMini('passage', { right: 1, total: 3, extra: 1, score: 10 }, tok)).json.xpGained > 0);
});

// --- the two findings the audit reproduced, which the old suite could not see.
// Both are concurrency or forgery, and the whole suite was sequential and
// honest, so neither had anywhere to show up.

test('a mini round cannot be claimed without a server-issued token', async () => {
  const fresh = (await call('POST', '/v1/players', {})).json.token;

  // The original attack: no round, no token, straight to the payout.
  const bare = await call('POST', '/v1/mini/pillar_sort', { right: 24, total: 24 }, fresh);
  assert.equal(bare.status, 400);
  assert.equal(bare.json.error, 'round_token_required');

  // A forged signature over a plausible-looking round id.
  const forged = await call('POST', '/v1/mini/pillar_sort', { right: 24, total: 24, token: 'm_dead.nonce.99999999999999.sig' }, fresh);
  assert.equal(forged.status, 400);

  const s = await call('POST', '/v1/mini/pillar_sort/start', {}, fresh);
  // Claiming instantly is not a human playing a 60-second game.
  const tooFast = await call('POST', '/v1/mini/pillar_sort', { right: 24, total: 24, token: s.json.token }, fresh);
  assert.equal(tooFast.status, 409);
  assert.equal(tooFast.json.error, 'too_fast');

  advance(config.mini.minDurationMs.pillar_sort + 1000);
  const ok = await call('POST', '/v1/mini/pillar_sort', { right: 24, total: 24, token: s.json.token }, fresh);
  assert.equal(ok.status, 200);
  assert.ok(ok.json.xpGained > 0);

  // Single use, including against a concurrent burst.
  const replays = await Promise.all(
    Array.from({ length: 8 }, () => call('POST', '/v1/mini/pillar_sort', { right: 24, total: 24, token: s.json.token }, fresh)),
  );
  assert.ok(replays.every((r) => r.status === 409), 'a claimed round was paid twice');

  // Another player's round is not claimable.
  const other = (await call('POST', '/v1/players', {})).json.token;
  const s2 = await call('POST', '/v1/mini/pillar_sort/start', {}, fresh);
  advance(config.mini.minDurationMs.pillar_sort + 1000);
  const stolen = await call('POST', '/v1/mini/pillar_sort', { right: 24, total: 24, token: s2.json.token }, other);
  assert.equal(stolen.status, 404);
});

test('concurrent finishes pay exactly once', async () => {
  const fresh = (await call('POST', '/v1/players', {})).json.token;
  const start = await call('POST', '/v1/expeditions', {}, fresh);
  const exp = start.json.expeditionId;
  const n = start.json.tabletCount as number;
  for (let i = 0; i < n; i++) {
    advance(Math.ceil(start.json.tabletFractions[i] * config.run.minFinishMs) + 2000);
    const t = await call('POST', `/v1/expeditions/${exp}/tablets/${i}`, {}, fresh);
    await call('POST', `/v1/expeditions/${exp}/tablets/${i}/answer`, { token: t.json.token, choice: 0 }, fresh);
  }
  advance(config.run.minFinishMs + 5000);

  const before = (await call('GET', '/v1/me', undefined, fresh)).json.xp;
  // The attack: fire many finishes at once. Every one of them used to pass the
  // "already finished?" guard while parked on the body, and every one paid.
  const results = await Promise.all(
    Array.from({ length: 25 }, () => call('POST', `/v1/expeditions/${exp}/finish`, { runMs: 120_000 }, fresh)),
  );
  const after = (await call('GET', '/v1/me', undefined, fresh)).json.xp;

  const paid = results.filter((r) => !r.json.replay).length;
  assert.equal(paid, 1, `${paid} of 25 concurrent finishes were treated as the first`);
  assert.equal(after - before, results.find((r) => !r.json.replay)!.json.xpGained);

  // Answering `choice: 0` is a guess, so this run may legitimately be worth
  // nothing — and awardXp writes no row for a zero award. The invariant that
  // matters either way is that one expedition never produces two ledger rows.
  const events = db.prepare('SELECT COUNT(*) AS n FROM xp_events WHERE ref_id = ?').get(exp) as { n: number };
  assert.ok(events.n <= 1, `${events.n} XP events for a single expedition`);
});

test('DELETE /v1/me erases the player from every table', async () => {
  const fresh = (await call('POST', '/v1/players', {})).json.token;
  const me = await call('GET', '/v1/me', undefined, fresh);
  const playerId = db.prepare('SELECT id FROM players WHERE handle = ?').get(me.json.handle) as { id: string };
  assert.ok(playerId, 'could not find the player we just made');
  const id = playerId.id;

  // Leave a trail in as many tables as a player can touch: an expedition with
  // issued tablets, a ledger play, a mini round, and the XP ledger rows those
  // produce. A delete that only clears `players` would leave all of it.
  const start = await call('POST', '/v1/expeditions', {}, fresh);
  const exp = start.json.expeditionId;
  for (let i = 0; i < start.json.tabletCount; i++) {
    advance(Math.ceil(start.json.tabletFractions[i] * config.run.minFinishMs) + 2000);
    const t = await call('POST', `/v1/expeditions/${exp}/tablets/${i}`, {}, fresh);
    await call('POST', `/v1/expeditions/${exp}/tablets/${i}/answer`, { token: t.json.token, choice: 0 }, fresh);
  }
  advance(config.run.minFinishMs + 5000);
  await call('POST', `/v1/expeditions/${exp}/finish`, { runMs: 120_000 }, fresh);
  await playMini('pillar_sort', { right: 9, total: 9 }, fresh);
  await playMini('passage', { right: 1, total: 3, extra: 1, score: 40 }, fresh);
  db.prepare('UPDATE passage_profile SET points = 10000 WHERE player_id = ?').run(id);
  await call('POST', '/v1/passage/abilities/dash/upgrade', {}, fresh);
  const today = todayIndex();
  await call('POST', '/v1/ledger/guess', { guess: puzzleFor(today).answer }, fresh);

  const countFor = (table: string, col = 'player_id') =>
    (db.prepare(`SELECT COUNT(*) AS n FROM ${table} WHERE ${col} = ?`).get(id) as { n: number }).n;
  const tabletRows = () =>
    (
      db
        .prepare('SELECT COUNT(*) AS n FROM tablets WHERE expedition_id IN (SELECT id FROM expeditions WHERE player_id = ?)')
        .get(id) as { n: number }
    ).n;

  // Guard the guard: if the trail were empty the assertions below would pass
  // against a delete that does nothing at all.
  assert.ok(countFor('expeditions') > 0, 'no expedition to delete');
  assert.ok(tabletRows() > 0, 'no tablet rows to delete');
  assert.ok(countFor('xp_events') > 0, 'no XP events to delete');
  assert.ok(countFor('ledger_plays') > 0, 'no ledger play to delete');
  assert.ok(countFor('mini_rounds') > 0, 'no mini round to delete');
  assert.ok(countFor('passage_profile') > 0, 'no boar to delete');
  assert.ok(countFor('passage_abilities') > 0, 'no ability to delete');

  const del = await call('DELETE', '/v1/me', undefined, fresh);
  assert.equal(del.status, 200);
  assert.equal(del.json.deleted, true);
  assert.equal(del.json.rows.players, 1);

  for (const table of ['expeditions', 'badges', 'tablet_state', 'ledger_plays', 'mini_rounds', 'xp_events', 'passage_profile', 'passage_abilities']) {
    assert.equal(countFor(table), 0, `${table} still holds rows for a deleted player`);
  }
  // `tablets` is keyed to the expedition, not the player — the case a naive
  // "DELETE ... WHERE player_id" sweep silently misses.
  assert.equal(tabletRows(), 0, 'tablets rows survived, orphaned');
  assert.equal((db.prepare('SELECT COUNT(*) AS n FROM players WHERE id = ?').get(id) as { n: number }).n, 0);

  // The token resolved against the row that is now gone, so it stops working.
  assert.equal((await call('GET', '/v1/me', undefined, fresh)).status, 401);
  assert.equal((await call('DELETE', '/v1/me', undefined, fresh)).status, 401);
});

test('deletion needs a valid token', async () => {
  assert.equal((await call('DELETE', '/v1/me')).status, 401);
  assert.equal((await call('DELETE', '/v1/me', undefined, 'not-a-token')).status, 401);
});

test('junk in a request body is rejected, not 500', async () => {
  const fresh = (await call('POST', '/v1/players', {})).json.token;
  const s = await call('POST', '/v1/mini/coin_quest/start', {}, fresh);
  advance(config.mini.minDurationMs.coin_quest + 1000);
  // Number({}) is NaN, which node:sqlite used to reject with a 500.
  const r = await call('POST', '/v1/mini/coin_quest', { right: {}, total: 'x', extra: [], token: s.json.token }, fresh);
  assert.equal(r.status, 200);
  assert.equal(r.json.xpGained, 0);
  assert.equal((await call('GET', '/v1/leaderboard?limit=abc', undefined, fresh)).status, 200);
});
