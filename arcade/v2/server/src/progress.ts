import type { Db } from './db.ts';
import { config } from './config.ts';

export interface PlayerRow {
  id: string;
  handle: string | null;
  xp: number;
  expeditions: number;
  expeditions_complete: number;
  tablets_correct: number;
  ledgers_solved: number;
  streak: number;
  last_ledger_day: number | null;
  status: string;
}

export const badgeNames: Record<string, string> = {
  first_expedition: 'First Expedition',
  ten_tablets: 'Ten Tablets',
  fifty_tablets: 'Fifty Tablets',
  streak_3: '3-Day Ledger Streak',
  streak_7: '7-Day Ledger Streak',
  streak_30: '30-Day Ledger Streak',
  level_5: 'Level 5 Explorer',
  sorter: 'Pillar Sorter',
  mythbuster: 'Myth Buster',
  chainsmith: 'Chainsmith',
};

export const level = (xp: number) => 1 + Math.floor(xp / config.xp.levelSize);

// ------------------------------------------------------------------ XP ledger

/** The only place XP is granted. Writes the running total and a dated event. */
export function awardXp(db: Db, playerId: string, amount: number, source: string, refId?: string) {
  if (amount <= 0) return;
  db.prepare('UPDATE players SET xp = xp + ? WHERE id = ?').run(amount, playerId);
  db.prepare('INSERT INTO xp_events (player_id, amount, source, ref_id, created_at) VALUES (?, ?, ?, ?, ?)').run(
    playerId,
    amount,
    source,
    refId ?? null,
    Date.now(),
  );
}

/** Monday 00:00 UTC of the week containing [now]. */
export function weekStart(now = Date.now()): number {
  const d = new Date(now);
  const mondayOffset = (d.getUTCDay() + 6) % 7;
  return Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate()) - mondayOffset * 86_400_000;
}

export interface BoardRow { rank: number; handle: string; xp: number; you: boolean }

/**
 * Weekly XP standings. Resets Monday 00:00 UTC so the board stays winnable
 * and nobody can bank an unbeatable lead. Recognition only — the plan gives
 * XP no monetary value and no prize is attached to a rank.
 */
export function leaderboard(db: Db, playerId: string, limit = 50) {
  const since = weekStart();
  const top = db
    .prepare(
      `WITH weekly AS (
         SELECT p.id AS id, p.handle AS handle, SUM(x.amount) AS xp, MIN(x.created_at) AS first_at
         FROM players p JOIN xp_events x ON x.player_id = p.id
         WHERE x.created_at >= ? AND p.status != 'banned' AND p.handle IS NOT NULL
         GROUP BY p.id
       )
       SELECT id, handle, xp, RANK() OVER (ORDER BY xp DESC) AS rank
       FROM weekly WHERE xp > 0 ORDER BY rank, first_at LIMIT ?`,
    )
    .all(since, limit) as Array<{ id: string; handle: string; xp: number; rank: number }>;

  const rows: BoardRow[] = top.map((r) => ({ rank: r.rank, handle: r.handle, xp: r.xp, you: r.id === playerId }));

  // The player's own standing, even when they are outside the top slice.
  const mine = db
    .prepare('SELECT COALESCE(SUM(amount), 0) AS xp FROM xp_events WHERE player_id = ? AND created_at >= ?')
    .get(playerId, since) as { xp: number };
  const ahead = db
    .prepare(
      `SELECT COUNT(*) AS n FROM (
         SELECT SUM(amount) AS xp FROM xp_events WHERE created_at >= ?
         GROUP BY player_id HAVING xp > ?)`,
    )
    .get(since, mine.xp) as { n: number };
  const players = db
    .prepare(
      `SELECT COUNT(*) AS n FROM (
         SELECT player_id FROM xp_events WHERE created_at >= ? GROUP BY player_id HAVING SUM(amount) > 0)`,
    )
    .get(since) as { n: number };

  return {
    board: 'weekly_xp',
    weekStart: since,
    resetsAt: since + 7 * 86_400_000,
    players: players.n,
    rows,
    you: {
      handle: ensureHandleName(db, playerId),
      xp: mine.xp,
      rank: mine.xp > 0 ? ahead.n + 1 : null,
      inTop: rows.some((r) => r.you),
    },
  };
}

function ensureHandleName(db: Db, playerId: string): string {
  const row = db.prepare('SELECT handle FROM players WHERE id = ?').get(playerId) as { handle: string | null };
  return row?.handle ?? '';
}

export function getPlayer(db: Db, id: string): PlayerRow | undefined {
  return db
    .prepare(
      `SELECT id, handle, xp, expeditions, expeditions_complete, tablets_correct, ledgers_solved, streak,
              last_ledger_day, status FROM players WHERE id = ?`,
    )
    .get(id) as PlayerRow | undefined;
}

export function badgesOf(db: Db, id: string): string[] {
  return (db.prepare('SELECT badge FROM badges WHERE player_id = ? ORDER BY earned_at').all(id) as { badge: string }[]).map(
    (r) => r.badge,
  );
}

export function miniPlays(db: Db, id: string): Record<string, number> {
  const rows = db.prepare('SELECT game, COUNT(*) AS n FROM mini_rounds WHERE player_id = ? GROUP BY game').all(id) as {
    game: string;
    n: number;
  }[];
  return Object.fromEntries(rows.map((r) => [r.game, r.n]));
}

/** Re-evaluates every badge rule; returns the ones newly earned. */
export function checkBadges(db: Db, id: string): string[] {
  const p = getPlayer(db, id)!;
  const have = new Set(badgesOf(db, id));
  const plays = miniPlays(db, id);
  const rules: Array<[string, boolean]> = [
    ['first_expedition', p.expeditions_complete >= 1],
    ['ten_tablets', p.tablets_correct >= 10],
    ['fifty_tablets', p.tablets_correct >= 50],
    ['streak_3', p.streak >= 3],
    ['streak_7', p.streak >= 7],
    ['streak_30', p.streak >= 30],
    ['level_5', level(p.xp) >= 5],
    ['sorter', (plays.pillar_sort ?? 0) >= 5],
    ['mythbuster', (plays.design_or_myth ?? 0) >= 5],
    ['chainsmith', (plays.chain_builder ?? 0) >= 5],
  ];
  const fresh: string[] = [];
  const ins = db.prepare('INSERT OR IGNORE INTO badges (player_id, badge, earned_at) VALUES (?, ?, ?)');
  for (const [b, ok] of rules) {
    if (ok && !have.has(b)) {
      ins.run(id, b, Date.now());
      fresh.push(b);
    }
  }
  return fresh;
}

/** The shape the client caches as ArcadeProgress. */
/**
 * The player's boar: points scored in When Pigs Fly, and the stage those
 * points have grown it to. The stage is decided here and nowhere else — the
 * app draws whatever this says — so a threshold change needs no app release.
 */
export function passageProfile(db: Db, id: string) {
  const row = db.prepare('SELECT lifetime, points, loadout FROM passage_profile WHERE player_id = ?').get(id) as
    | { lifetime: number; points: number; loadout: string }
    | undefined;
  const owned = ownedAbilities(db, id);
  const lifetime = row?.lifetime ?? 0;
  const stages = config.passage.stages;
  let i = 0;
  while (i + 1 < stages.length && lifetime >= stages[i + 1].at) i++;
  const next = stages[i + 1];
  return {
    lifetime,
    points: row?.points ?? 0,
    stage: stages[i].id,
    stageAt: stages[i].at,
    nextStage: next?.id ?? null,
    nextAt: next?.at ?? null,
    // Every ability in the shop, owned or not, with what the next level
    // costs — so the app never hard-codes a price.
    abilities: Object.entries(config.passage.abilities).map(([ability, costs]) => {
      const level = owned.get(ability) ?? 0;
      return { id: ability, level, maxLevel: costs.length, nextCost: level < costs.length ? costs[level] : null };
    }),
    loadout: parseLoadout(row?.loadout).filter((a) => owned.has(a)),
  };
}

function ownedAbilities(db: Db, id: string): Map<string, number> {
  const rows = db.prepare('SELECT ability, level FROM passage_abilities WHERE player_id = ?').all(id) as Array<{
    ability: string;
    level: number;
  }>;
  return new Map(rows.map((r) => [r.ability, r.level]));
}

function parseLoadout(json: string | undefined): string[] {
  try {
    const v = JSON.parse(json ?? '[]');
    return Array.isArray(v) ? v.filter((x): x is string => typeof x === 'string') : [];
  } catch {
    return [];
  }
}

const isAbility = (a: unknown): a is string =>
  typeof a === 'string' && Object.prototype.hasOwnProperty.call(config.passage.abilities, a);

/**
 * Raises an ability one level, paying from `points`. Never touches
 * `lifetime`: spending must not shrink the boar. The level read, the balance
 * check and both writes happen with no await between them, inside one
 * transaction, so two taps landing together pay once.
 */
export function upgradeAbility(
  db: Db,
  id: string,
  ability: string,
): 'ok' | 'unknown_ability' | 'max_level' | 'not_enough_points' {
  if (!isAbility(ability)) return 'unknown_ability';
  const costs = config.passage.abilities[ability];
  db.exec('BEGIN');
  try {
    const level = ownedAbilities(db, id).get(ability) ?? 0;
    if (level >= costs.length) {
      db.exec('ROLLBACK');
      return 'max_level';
    }
    const cost = costs[level];
    const paid = db
      .prepare('UPDATE passage_profile SET points = points - ?, updated_at = ? WHERE player_id = ? AND points >= ?')
      .run(cost, Date.now(), id, cost);
    if (paid.changes === 0) {
      db.exec('ROLLBACK');
      return 'not_enough_points';
    }
    db.prepare(
      `INSERT INTO passage_abilities (player_id, ability, level) VALUES (?, ?, 1)
       ON CONFLICT(player_id, ability) DO UPDATE SET level = level + 1`,
    ).run(id, ability);
    db.exec('COMMIT');
    return 'ok';
  } catch (err) {
    db.exec('ROLLBACK');
    throw err;
  }
}

/**
 * Validates what a player says they will fly with, or flew with: at most
 * [config.passage.loadoutSlots] distinct abilities, each owned — and, for a
 * claimed round, each at no more than the owned level. Returns the ids, or
 * null for anything else.
 */
export function checkLoadout(db: Db, id: string, v: unknown, withLevels: boolean): string[] | null {
  if (!Array.isArray(v) || v.length > config.passage.loadoutSlots) return null;
  const owned = ownedAbilities(db, id);
  const ids: string[] = [];
  for (const e of v) {
    const ability = withLevels ? (e as { id?: unknown })?.id : e;
    if (!isAbility(ability) || ids.includes(ability)) return null;
    const have = owned.get(ability) ?? 0;
    if (have < 1) return null;
    if (withLevels) {
      const level = Number((e as { level?: unknown }).level);
      if (!Number.isInteger(level) || level < 1 || level > have) return null;
    }
    ids.push(ability);
  }
  return ids;
}

export function setLoadout(db: Db, id: string, ids: string[]) {
  db.prepare(
    `INSERT INTO passage_profile (player_id, lifetime, points, updated_at, loadout) VALUES (?, 0, 0, ?, ?)
     ON CONFLICT(player_id) DO UPDATE SET loadout = excluded.loadout, updated_at = excluded.updated_at`,
  ).run(id, Date.now(), JSON.stringify(ids));
}

/** Adds a claimed run's score to both totals. See the table comment in db.ts. */
export function creditPassage(db: Db, id: string, amount: number) {
  if (amount <= 0) return;
  db.prepare(
    `INSERT INTO passage_profile (player_id, lifetime, points, updated_at) VALUES (?, ?, ?, ?)
     ON CONFLICT(player_id) DO UPDATE SET
       lifetime = lifetime + excluded.lifetime,
       points = points + excluded.points,
       updated_at = excluded.updated_at`,
  ).run(id, amount, amount, Date.now());
}

export function snapshot(db: Db, id: string, extra: Record<string, unknown> = {}) {
  const p = getPlayer(db, id)!;
  return {
    playerId: p.id,
    handle: p.handle,
    xp: p.xp,
    weeklyXp: (db.prepare('SELECT COALESCE(SUM(amount), 0) AS xp FROM xp_events WHERE player_id = ? AND created_at >= ?')
      .get(id, weekStart()) as { xp: number }).xp,
    level: level(p.xp),
    levelProgress: (p.xp % config.xp.levelSize) / config.xp.levelSize,
    expeditions: p.expeditions,
    expeditionsComplete: p.expeditions_complete,
    tabletsCorrect: p.tablets_correct,
    ledgersSolved: p.ledgers_solved,
    streak: p.streak,
    lastLedgerDay: p.last_ledger_day,
    badges: badgesOf(db, id),
    miniPlays: miniPlays(db, id),
    passage: passageProfile(db, id),
    status: p.status,
    ...extra,
  };
}
