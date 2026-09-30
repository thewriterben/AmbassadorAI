// When Pigs Fly tuning report. Read-only.
//
//   npm run report:passage -- [--db data/arcade.sqlite] [--since-days 14] [--json]
//
// See src/report.ts for what each figure means and why.
import { DatabaseSync } from 'node:sqlite';
import { config } from '../src/config.ts';
import { passageReport } from '../src/report.ts';

const args = process.argv.slice(2);
const arg = (name: string) => {
  const i = args.indexOf(name);
  return i >= 0 ? args[i + 1] : undefined;
};
const path = arg('--db') ?? config.dbPath;
const sinceDays = arg('--since-days');
const db = new DatabaseSync(path, { readOnly: true });
const r = passageReport(db, {
  since: sinceDays ? Date.now() - Number(sinceDays) * 86_400_000 : undefined,
});

if (args.includes('--json')) {
  console.log(JSON.stringify(r, null, 2));
} else {
  const n = (x: number | null) => (x === null ? '-' : x.toLocaleString('en-GB'));
  console.log(`When Pigs Fly — ${r.runs} claimed runs from ${r.players} players (${path})`);
  console.log(
    `score  p10 ${n(r.score.p10)}  p25 ${n(r.score.p25)}  median ${n(r.score.median)}  p75 ${n(r.score.p75)}  p90 ${n(r.score.p90)}  mean ${n(r.score.mean)}`,
  );
  console.log(`stars  1: ${r.stars.one}  2: ${r.stars.two}  3: ${r.stars.three}   eras reached, mean ${r.erasReachedMean}`);
  console.log(
    `typical player: ${n(r.typicalPlayer.pointsPerActiveDay)} points and ${r.typicalPlayer.runsPerActiveDay} runs on a day they play`,
  );
  for (const [stage, at] of Object.entries(r.currentThresholds)) {
    console.log(`  ${stage.padEnd(10)} at ${n(at as number)}: ${n(r.daysToStage[stage] as number | null)} active days`);
  }
  if (!r.enoughData) {
    console.log(`too few players (${r.players}) to suggest thresholds; keep the calibrated ones`);
  } else if (r.suggestedThresholds) {
    console.log(
      `suggested for ${r.targetDays.juvenile} / ${r.targetDays.razorback} active days: ` +
        `PASSAGE_JUVENILE_AT=${r.suggestedThresholds.juvenile} PASSAGE_RAZORBACK_AT=${r.suggestedThresholds.razorback}`,
    );
  }
  console.log(`boars: ${Object.entries(r.boars).map(([k, v]) => `${k} ${v}`).join(', ')}`);
  console.log(`unlocks: ${r.shop.unlocks.map((u) => `${u.ability} L${u.level} ×${u.n}`).join(', ') || 'none'}`);
  console.log(
    `flown with: ${Object.entries(r.shop.flownWith).map(([k, v]) => `${k} ${v}`).join(', ') || 'none'}   rejected loadouts: ${r.shop.rejectedLoadouts}`,
  );
}
