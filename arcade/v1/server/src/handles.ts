import type { Db } from './db.ts';

// Display names are assigned, never typed. No free text means no profanity
// queue, no impersonation, no PII on a public board — and nothing a store
// reviewer can read as a promise. Vocabulary is deliberately drawn from how
// DGD works (ledgers, pillars, the frozen benchmark), never from earning.

const FIRST = [
  'Gold', 'Silver', 'Rose', 'Copper', 'Sapphire', 'Emerald',
  'Burnished', 'Minted', 'Frozen', 'Steady', 'Quiet', 'Patient',
  'Open', 'Fixed', 'Verified', 'Circulating', 'Transparent', 'Voluntary',
  'Northern', 'Deep', 'Bright', 'Iron', 'Amber', 'Still',
];

const SECOND = [
  'Ledger', 'Tablet', 'Vault', 'Pillar', 'Benchmark', 'Standard',
  'Wallet', 'Treasury', 'Chain', 'Node', 'Beacon', 'Archive',
  'Compass', 'Lantern', 'Anvil', 'Circuit', 'Relay', 'Cipher',
  'Mesh', 'Signal', 'Keystone', 'Foundry', 'Almanac', 'Meridian',
];

const pick = <T>(a: T[]) => a[Math.floor(Math.random() * a.length)];

/** e.g. "Steady Ledger 417". Unique across players; retries on collision. */
export function generateHandle(db: Db): string {
  const taken = db.prepare('SELECT 1 FROM players WHERE handle = ?');
  for (let attempt = 0; attempt < 40; attempt++) {
    const digits = attempt < 30 ? 900 : 9000;
    const offset = attempt < 30 ? 100 : 1000;
    const h = `${pick(FIRST)} ${pick(SECOND)} ${Math.floor(Math.random() * digits) + offset}`;
    if (!taken.get(h)) return h;
  }
  // Vanishingly unlikely; keep it deterministic rather than looping forever.
  return `Steady Ledger ${Date.now().toString().slice(-7)}`;
}

/** Assigns a handle if the player has none. Returns the current handle. */
export function ensureHandle(db: Db, playerId: string): string {
  const row = db.prepare('SELECT handle FROM players WHERE id = ?').get(playerId) as { handle: string | null } | undefined;
  if (row?.handle) return row.handle;
  const h = generateHandle(db);
  db.prepare('UPDATE players SET handle = ? WHERE id = ?').run(h, playerId);
  return h;
}

export function rerollHandle(db: Db, playerId: string): string {
  const h = generateHandle(db);
  db.prepare('UPDATE players SET handle = ?, handle_rerolls = handle_rerolls + 1 WHERE id = ?').run(h, playerId);
  return h;
}

export const maxRerollsPerDay = 3;
