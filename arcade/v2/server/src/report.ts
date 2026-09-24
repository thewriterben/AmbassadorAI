import type { Db } from './db.ts';
import { config } from './config.ts';

/**
 * When Pigs Fly tuning report, from real claimed runs.
 *
 * The growth thresholds and shop prices in config.passage were first set
 * from a guess, then from simulated players (the app's
 * passage_calibration_test.dart). This is what replaces both once people
 * are playing: what runs actually score, how many points a player actually
 * makes on a day they play, how long that makes each stage take, and what
 * the thresholds would be to hit the pacing we want.
 *
 * Read-only. Nothing here writes to the database or changes config; a
 * threshold change is still a deliberate edit (or an env override).
 */
export interface PassageReportOptions {
  /** Only runs claimed at or after this time (ms). Default: all. */
  since?: number;
  /** Target days to each stage, for a typical player. */
  juvenileDays?: number;
  razorbackDays?: number;
  /** Fewest players to suggest thresholds from. Default 20. */
  minPlayers?: number;
}

const pct = (sorted: number[], q: number) =>
  sorted.length === 0 ? 0 : sorted[Math.min(sorted.length - 1, Math.round((sorted.length - 1) * q))];
/** A true median: the mean of the middle two for an even count. */
const median = (xs: number[]) => {
  if (xs.length === 0) return 0;
  const s = [...xs].sort((a, b) => a - b);
  const m = s.length >> 1;
  return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2;
};

export function passageReport(db: Db, opts: PassageReportOptions = {}) {
  const since = opts.since ?? 0;
  const runs = db
    .prepare(
      `SELECT player_id, day, right, extra, score, xp_gained, loadout FROM mini_rounds
       WHERE game = 'passage' AND claimed_at IS NOT NULL AND claimed_at >= ?`,
    )
    .all(since) as Array<{
    player_id: string;
    day: number;
    right: number;
    extra: number;
    score: number;
    xp_gained: number;
    loadout: string | null;
  }>;

  const scores = runs.map((r) => r.score).sort((a, b) => a - b);

  // Points a player makes on a day they play: only paid runs grow the boar
  // (the same gate as XP), so only those count. One number per player — the
  // median of their active days — so a handful of heavy players cannot drag
  // the typical figure up.
  const byPlayerDay = new Map<string, Map<number, { points: number; runs: number }>>();
  for (const r of runs) {
    const days = byPlayerDay.get(r.player_id) ?? new Map();
    const d = days.get(r.day) ?? { points: 0, runs: 0 };
    d.runs++;
    if (r.xp_gained > 0) d.points += r.score;
    days.set(r.day, d);
    byPlayerDay.set(r.player_id, days);
  }
  const playerDaily = [...byPlayerDay.values()].map((days) => median([...days.values()].map((d) => d.points)));
  const playerRuns = [...byPlayerDay.values()].map((days) => median([...days.values()].map((d) => d.runs)));
  const typicalDaily = median(playerDaily);

  const stages = config.passage.stages;
  const daysTo = (at: number) => (typicalDaily > 0 ? Math.round((at / typicalDaily) * 10) / 10 : null);

  const lifetimes = (db.prepare('SELECT lifetime FROM passage_profile').all() as Array<{ lifetime: number }>).map(
    (r) => r.lifetime,
  );
  const stageCounts = Object.fromEntries(stages.map((s) => [s.id, 0]));
  for (const l of lifetimes) {
    let i = 0;
    while (i + 1 < stages.length && l >= stages[i + 1].at) i++;
    stageCounts[stages[i].id]++;
  }

  const unlocks = db
    .prepare('SELECT ability, level, COUNT(*) AS n FROM passage_abilities GROUP BY ability, level ORDER BY ability, level')
    .all() as Array<{ ability: string; level: number; n: number }>;
  const flownWith: Record<string, number> = {};
  let rejected = 0;
  for (const r of runs) {
    if (!r.loadout) continue;
    try {
      const v = JSON.parse(r.loadout);
      // An accepted loadout is stored as a list of ids; a rejected one as
      // {rejected: ...}. See the claim in app.ts.
      if (Array.isArray(v)) {
        for (const a of v) if (typeof a === 'string') flownWith[a] = (flownWith[a] ?? 0) + 1;
      } else {
        rejected++;
      }
    } catch {
      rejected++;
    }
  }

  const round50 = (n: number) => Math.max(50, Math.round(n / 50) * 50);
  // A handful of players — the team, a test phone — says nothing about the
  // public. Below this the report still shows what it has, but suggests
  // nothing: a threshold tuned to three testers is worse than the guess.
  const enoughData = byPlayerDay.size >= (opts.minPlayers ?? 20);
  const jDays = opts.juvenileDays ?? 2.5;
  const rDays = opts.razorbackDays ?? 10;

  return {
    runs: runs.length,
    players: byPlayerDay.size,
    score: {
      p10: pct(scores, 0.1),
      p25: pct(scores, 0.25),
      median: pct(scores, 0.5),
      p75: pct(scores, 0.75),
      p90: pct(scores, 0.9),
      mean: scores.length ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : 0,
    },
    stars: {
      one: runs.filter((r) => r.right <= 1).length,
      two: runs.filter((r) => r.right === 2).length,
      three: runs.filter((r) => r.right >= 3).length,
    },
    erasReachedMean: runs.length ? Math.round((runs.reduce((a, r) => a + r.extra, 0) / runs.length) * 10) / 10 : 0,
    typicalPlayer: { pointsPerActiveDay: typicalDaily, runsPerActiveDay: median(playerRuns) },
    daysToStage: Object.fromEntries(stages.slice(1).map((s) => [s.id, daysTo(s.at)])),
    // What the thresholds would be for the typical player to reach each stage
    // in the target number of days they play. A suggestion, not an action.
    enoughData,
    suggestedThresholds:
      enoughData && typicalDaily > 0 ? { juvenile: round50(typicalDaily * jDays), razorback: round50(typicalDaily * rDays) } : null,
    targetDays: { juvenile: jDays, razorback: rDays },
    currentThresholds: Object.fromEntries(stages.slice(1).map((s) => [s.id, s.at])),
    boars: stageCounts,
    shop: { unlocks, flownWith, rejectedLoadouts: rejected },
  };
}
