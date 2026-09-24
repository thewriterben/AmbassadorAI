import { DatabaseSync } from 'node:sqlite';
import { mkdirSync } from 'node:fs';
import { dirname } from 'node:path';

// SQLite for the pilot (single process, <10k players). The schema is plain
// SQL on purpose: moving to Postgres is a driver swap, not a rewrite.
export const schema = `
CREATE TABLE IF NOT EXISTS players (
  id TEXT PRIMARY KEY,
  token_hash TEXT NOT NULL UNIQUE,
  created_at INTEGER NOT NULL,
  last_seen INTEGER NOT NULL,
  device_hint TEXT,
  handle TEXT UNIQUE,                        -- assigned, never user-typed
  handle_rerolls INTEGER NOT NULL DEFAULT 0,
  handle_reroll_day INTEGER,
  xp INTEGER NOT NULL DEFAULT 0,
  expeditions INTEGER NOT NULL DEFAULT 0,
  expeditions_complete INTEGER NOT NULL DEFAULT 0,
  tablets_correct INTEGER NOT NULL DEFAULT 0,
  ledgers_solved INTEGER NOT NULL DEFAULT 0,
  streak INTEGER NOT NULL DEFAULT 0,
  last_ledger_day INTEGER,
  status TEXT NOT NULL DEFAULT 'ok'          -- ok | xp_only | banned (abuse ladder §5.6)
);

CREATE TABLE IF NOT EXISTS badges (
  player_id TEXT NOT NULL REFERENCES players(id),
  badge TEXT NOT NULL,
  earned_at INTEGER NOT NULL,
  PRIMARY KEY (player_id, badge)
);

-- Spaced retrieval state per player per question (§4.2 re-serve window).
CREATE TABLE IF NOT EXISTS tablet_state (
  player_id TEXT NOT NULL REFERENCES players(id),
  question_id TEXT NOT NULL,
  due_at INTEGER NOT NULL DEFAULT 0,
  misses INTEGER NOT NULL DEFAULT 0,
  correct INTEGER NOT NULL DEFAULT 0,
  seen INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (player_id, question_id)
);

CREATE TABLE IF NOT EXISTS expeditions (
  id TEXT PRIMARY KEY,
  player_id TEXT NOT NULL REFERENCES players(id),
  started_at INTEGER NOT NULL,
  finished_at INTEGER,
  tablet_count INTEGER NOT NULL,
  rewarded INTEGER NOT NULL DEFAULT 1,       -- 0 = practice run (daily cap hit)
  right_count INTEGER NOT NULL DEFAULT 0,
  complete INTEGER NOT NULL DEFAULT 0,
  xp_gained INTEGER NOT NULL DEFAULT 0,
  stumbles INTEGER,
  client_run_ms INTEGER,
  flags TEXT NOT NULL DEFAULT ''             -- comma list of plausibility flags
);

-- One row per tablet issued. The question id never leaves the server.
CREATE TABLE IF NOT EXISTS tablets (
  expedition_id TEXT NOT NULL REFERENCES expeditions(id),
  idx INTEGER NOT NULL,
  question_id TEXT NOT NULL,
  nonce TEXT,
  issued_at INTEGER,
  expires_at INTEGER,
  option_order TEXT,                         -- JSON: shuffled option indices
  answered_at INTEGER,
  choice INTEGER,
  correct INTEGER,
  latency_ms INTEGER,
  PRIMARY KEY (expedition_id, idx)
);

CREATE TABLE IF NOT EXISTS ledger_plays (
  player_id TEXT NOT NULL REFERENCES players(id),
  day INTEGER NOT NULL,
  guesses TEXT NOT NULL DEFAULT '[]',        -- JSON array of strings
  solved INTEGER NOT NULL DEFAULT 0,
  over INTEGER NOT NULL DEFAULT 0,
  xp_gained INTEGER NOT NULL DEFAULT 0,
  updated_at INTEGER NOT NULL,
  PRIMARY KEY (player_id, day)
);

CREATE TABLE IF NOT EXISTS mini_rounds (
  id TEXT PRIMARY KEY,
  player_id TEXT NOT NULL REFERENCES players(id),
  game TEXT NOT NULL,
  day INTEGER NOT NULL,
  right INTEGER NOT NULL,
  total INTEGER NOT NULL,
  extra INTEGER NOT NULL DEFAULT 0,
  xp_gained INTEGER NOT NULL,
  created_at INTEGER NOT NULL
);

-- Dated XP ledger. players.xp is the running total; this is how it got there,
-- which is what the weekly board reads and what a forfeiture review would
-- reverse (plan §4.4: an abuser loses everything not yet applied).
CREATE TABLE IF NOT EXISTS xp_events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  player_id TEXT NOT NULL REFERENCES players(id),
  amount INTEGER NOT NULL,
  source TEXT NOT NULL,                      -- expedition | ledger | mini
  ref_id TEXT,
  created_at INTEGER NOT NULL
);

-- When Pigs Fly growth. 'lifetime' only ever rises and decides the boar's
-- stage; 'points' is what the shop (phase 4) will spend. They are separate
-- so that spending can never shrink the boar. Like XP, neither has any
-- monetary value.
CREATE TABLE IF NOT EXISTS passage_profile (
  player_id TEXT PRIMARY KEY REFERENCES players(id),
  lifetime INTEGER NOT NULL DEFAULT 0,
  points INTEGER NOT NULL DEFAULT 0,
  updated_at INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS ix_exp_player_day ON expeditions(player_id, started_at);
CREATE INDEX IF NOT EXISTS ix_mini_player_day ON mini_rounds(player_id, game, day);
CREATE INDEX IF NOT EXISTS ix_xp_created ON xp_events(created_at);
CREATE INDEX IF NOT EXISTS ix_xp_player ON xp_events(player_id, created_at);
`;

/** Adds columns to databases created before those columns existed. */
const migrations: Array<[string, string]> = [
  ['players', 'handle TEXT'],
  ['players', 'handle_rerolls INTEGER NOT NULL DEFAULT 0'],
  ['players', 'handle_reroll_day INTEGER'],
  // Mini-game rounds became server-issued: a round is opened here, claimed
  // once, and must have taken a plausible amount of time. Rows written before
  // that get started_at = NULL and are simply never claimable.
  ['mini_rounds', 'nonce TEXT'],
  ['mini_rounds', 'started_at INTEGER'],
  ['mini_rounds', 'claimed_at INTEGER'],
  // Points from games that have them (Passage coins). Kept for the same
  // reason `right` and `extra` are: a forfeiture review reads the row.
  ['mini_rounds', 'score INTEGER NOT NULL DEFAULT 0'],
];

export function openDb(path: string): DatabaseSync {
  if (path !== ':memory:') mkdirSync(dirname(path), { recursive: true });
  const db = new DatabaseSync(path);
  db.exec('PRAGMA journal_mode = WAL; PRAGMA foreign_keys = ON;');
  db.exec(schema);
  for (const [table, column] of migrations) {
    const name = column.split(' ')[0];
    const cols = db.prepare(`PRAGMA table_info(${table})`).all() as { name: string }[];
    if (!cols.some((c) => c.name === name)) db.exec(`ALTER TABLE ${table} ADD COLUMN ${column}`);
  }
  db.exec('CREATE UNIQUE INDEX IF NOT EXISTS ux_players_handle ON players(handle)');
  backfillXpEvents(db);
  return db;
}

/**
 * The dated XP ledger was added after XP already existed. Every award is
 * still recorded in its source table with a timestamp and an amount, so the
 * ledger can be reconstructed exactly rather than starting the weekly board
 * from a fiction. Runs once: skipped as soon as any event exists.
 */
function backfillXpEvents(db: DatabaseSync) {
  const existing = db.prepare('SELECT COUNT(*) AS n FROM xp_events').get() as { n: number };
  if (existing.n > 0) return;
  const awarded = db.prepare('SELECT COALESCE(SUM(xp), 0) AS n FROM players').get() as { n: number };
  if (awarded.n === 0) return;
  db.exec(`
    INSERT INTO xp_events (player_id, amount, source, ref_id, created_at)
      SELECT player_id, xp_gained, 'expedition', id, COALESCE(finished_at, started_at)
      FROM expeditions WHERE xp_gained > 0;
    INSERT INTO xp_events (player_id, amount, source, ref_id, created_at)
      SELECT player_id, xp_gained, 'ledger', CAST(day AS TEXT), updated_at
      FROM ledger_plays WHERE xp_gained > 0;
    INSERT INTO xp_events (player_id, amount, source, ref_id, created_at)
      SELECT player_id, xp_gained, 'mini', id, created_at
      FROM mini_rounds WHERE xp_gained > 0;
  `);
  const got = db.prepare('SELECT COALESCE(SUM(amount), 0) AS n FROM xp_events').get() as { n: number };
  if (got.n !== awarded.n) {
    console.warn(`xp backfill: reconstructed ${got.n} XP but players hold ${awarded.n}; ` +
      'the difference predates the source tables and is lifetime-only.');
  }
}

export type Db = DatabaseSync;
