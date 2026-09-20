import { serve } from '@hono/node-server';
import { assertProductionConfig, config, DEV_SECRET } from './config.ts';
import { openDb } from './db.ts';
import { QuestionBank } from './bank.ts';
import { createApp } from './app.ts';

// Before anything opens a socket or a file: a misconfigured production process
// is worse than one that refuses to boot.
assertProductionConfig();

const db = openDb(config.dbPath);
const bank = QuestionBank.load(config.bankPath);
if (bank.items.length === 0) {
  console.error(`question bank at ${config.bankPath} parsed to 0 items`);
  process.exit(1);
}
const t = bank.tierCounts;
if (config.secret === DEV_SECRET) {
  console.warn('ARCADE_SECRET is the dev default — set it before exposing this server.');
}

// Containers and process managers restart on SIGTERM; closing the database
// cleanly avoids leaving a WAL behind for the next boot to recover.
for (const sig of ['SIGTERM', 'SIGINT'] as const) {
  process.on(sig, () => {
    try {
      db.close();
    } catch {
      // Already closed, or never opened. Nothing useful to do here.
    }
    process.exit(0);
  });
}

const app = createApp(db, bank);
serve({ fetch: app.fetch, port: config.port, hostname: '0.0.0.0' }, (info) => {
  console.log(
    `DGD Arcade backend on http://0.0.0.0:${info.port}  ` +
      `bank=${bank.items.length} items (A ${t.A} · B ${t.B} · C ${t.C} · D ${t.D})  db=${config.dbPath}`,
  );
});
