import type { Db } from './db.ts';
import type { Question, QuestionBank } from './bank.ts';
import { config } from './config.ts';

// Spaced retrieval (plan §4.2): correct → retired 14 days; missed → back at
// 1, 3, 7 days. Per player, server-side, so nobody can grind the same items.

interface State {
  due_at: number;
  misses: number;
  correct: number;
  seen: number;
}

function shuffle<T>(a: T[], rnd = Math.random): T[] {
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rnd() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export function loadStates(db: Db, playerId: string): Map<string, State> {
  const rows = db
    .prepare('SELECT question_id, due_at, misses, correct, seen FROM tablet_state WHERE player_id = ?')
    .all(playerId) as Array<State & { question_id: string }>;
  return new Map(rows.map((r) => [r.question_id, r]));
}

/** Picks `count` due items: due misses first, then unseen, then the rest, one per section first. */
export function pick(db: Db, bank: QuestionBank, playerId: string, count: number, requireHard = false): Question[] {
  const now = Date.now();
  const st = loadStates(db, playerId);
  const due = bank.items.filter((q) => (st.get(q.id)?.due_at ?? 0) <= now);
  const missed = shuffle(due.filter((q) => (st.get(q.id)?.misses ?? 0) > 0));
  const unseen = shuffle(due.filter((q) => !st.has(q.id)));
  const rest = shuffle(due.filter((q) => !missed.includes(q) && !unseen.includes(q)));
  const pool = [...missed, ...unseen, ...rest];
  const picked: Question[] = [];
  const sections = new Set<string>();
  for (const q of pool) {
    if (picked.length >= count) break;
    if (!sections.has(q.section)) {
      sections.add(q.section);
      picked.push(q);
    }
  }
  for (const q of pool) {
    if (picked.length >= count) break;
    if (!picked.includes(q)) picked.push(q);
  }
  if (requireHard && picked.filter((q) => q.tier === 'C' || q.tier === 'D').length < 2) {
    const hard = pool.filter((q) => (q.tier === 'C' || q.tier === 'D') && !picked.includes(q)).slice(0, 2);
    for (const h of hard) if (picked.length) picked[picked.length - 1] = h;
  }
  if (picked.length < count) {
    const extra = shuffle(bank.items.filter((q) => !picked.includes(q)));
    picked.push(...extra.slice(0, count - picked.length));
  }
  return picked;
}

export function record(db: Db, playerId: string, questionId: string, correct: boolean) {
  const now = Date.now();
  const s = (db
    .prepare('SELECT due_at, misses, correct, seen FROM tablet_state WHERE player_id = ? AND question_id = ?')
    .get(playerId, questionId) as State | undefined) ?? { due_at: 0, misses: 0, correct: 0, seen: 0 };
  const day = 86_400_000;
  if (correct) {
    s.due_at = now + config.tablets.retireDays * day;
    s.misses = 0;
    s.correct++;
  } else {
    s.due_at = now + config.tablets.missDays[Math.min(s.misses, 2)] * day;
    s.misses++;
  }
  s.seen++;
  db.prepare(
    `INSERT INTO tablet_state (player_id, question_id, due_at, misses, correct, seen)
     VALUES (?, ?, ?, ?, ?, ?)
     ON CONFLICT(player_id, question_id) DO UPDATE SET
       due_at = excluded.due_at, misses = excluded.misses, correct = excluded.correct, seen = excluded.seen`,
  ).run(playerId, questionId, s.due_at, s.misses, s.correct, s.seen);
}

/** Share of bank items answered correctly at least once. */
export function mastery(db: Db, bank: QuestionBank, playerId: string): number {
  if (bank.items.length === 0) return 0;
  const row = db
    .prepare('SELECT COUNT(*) AS n FROM tablet_state WHERE player_id = ? AND correct > 0')
    .get(playerId) as { n: number };
  return row.n / bank.items.length;
}
