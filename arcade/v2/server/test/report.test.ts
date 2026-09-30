import { test } from 'node:test';
import assert from 'node:assert/strict';
import { openDb } from '../src/db.ts';
import { config } from '../src/config.ts';
import { passageReport } from '../src/report.ts';

// The tuning report reads real runs. These rows are hand-made so every
// figure can be checked by eye.
test('the passage report summarises real runs and suggests thresholds', () => {
  const db = openDb(':memory:');
  const player = db.prepare(
    "INSERT INTO players (id, token_hash, created_at, last_seen, status) VALUES (?, ?, 0, 0, 'ok')",
  );
  const round = db.prepare(
    `INSERT INTO mini_rounds (id, player_id, game, day, right, total, extra, score, xp_gained, created_at, claimed_at, loadout)
     VALUES (?, ?, 'passage', ?, ?, 3, ?, ?, ?, 0, 1, ?)`,
  );
  let n = 0;
  // Player a: two days, 300 and 500 points (median 400). Player b: one day
  // of 200, and a practice run (no XP) that must not count toward growth.
  player.run('a', 'ha');
  player.run('b', 'hb');
  round.run(`r${n++}`, 'a', 1, 1, 2, 100, 12, null);
  round.run(`r${n++}`, 'a', 1, 2, 9, 200, 60, '["dash"]');
  round.run(`r${n++}`, 'a', 2, 3, 9, 500, 72, '["dash","grapple"]');
  round.run(`r${n++}`, 'b', 1, 1, 3, 200, 12, null);
  round.run(`r${n++}`, 'b', 1, 1, 3, 900, 0, '{"rejected":[{"id":"teleport","level":1}]}');
  // Another game is ignored.
  db.prepare(
    `INSERT INTO mini_rounds (id, player_id, game, day, right, total, extra, score, xp_gained, created_at, claimed_at)
     VALUES ('x', 'a', 'coin_quest', 1, 3, 3, 0, 0, 80, 0, 1)`,
  ).run();
  db.prepare("INSERT INTO passage_profile (player_id, lifetime, points, updated_at) VALUES ('a', 800, 800, 0), ('b', 200, 200, 0)").run();
  db.prepare("INSERT INTO passage_abilities (player_id, ability, level) VALUES ('a', 'dash', 1), ('a', 'grapple', 1)").run();

  // Two players is below the default floor: figures, but no suggestion.
  assert.equal(passageReport(db).suggestedThresholds, null);
  const r = passageReport(db, { juvenileDays: 2, razorbackDays: 10, minPlayers: 2 });
  assert.equal(r.runs, 5);
  assert.equal(r.players, 2);
  assert.equal(r.score.median, 200);
  assert.deepEqual(r.stars, { one: 3, two: 1, three: 1 });
  // a: days of 300 and 500 -> 400; b: 200 (the practice run is not growth).
  // The typical player is the median of those: 300.
  assert.equal(r.typicalPlayer.pointsPerActiveDay, 300);
  assert.deepEqual(r.suggestedThresholds, { juvenile: 600, razorback: 3000 });
  assert.equal(r.daysToStage.juvenile, Math.round((config.passage.stages[1].at / 300) * 10) / 10);
  assert.deepEqual(r.boars, { piglet: 2, juvenile: 0, razorback: 0 });
  assert.deepEqual(r.shop.flownWith, { dash: 2, grapple: 1 });
  assert.equal(r.shop.rejectedLoadouts, 1);
});
