# Hosting runbook

## Shape

**One Node 24 process with one SQLite file.** The rest of the shape:

- **No build step.** Node 24 runs the TypeScript directly.
- **Two runtime dependencies:** `hono` and `@hono/node-server`.
- **Run exactly one replica.** Rate limits are held in process memory, and SQLite is single-writer. A second replica would split the limits and fight over the file. (Per-day caps are counted from the database, so they are unaffected.)
- **Scale:** sized for the pilot, under 10,000 players. Moving to Postgres is possible later, because the schema is plain SQL, but it has not been done.

## Environment

All variables are listed in `env.example`.

| Variable | Production value | Notes |
|---|---|---|
| `NODE_ENV` | `production` | Already set by the Dockerfile |
| `ARCADE_SECRET` | 32+ random characters | Signs the round tokens. **Required.** The server refuses to start on the published development default. |
| `ARCADE_CORS` | `https://arcade-api.digitalgold.co` | **Must not be `*`** in production; the server refuses to start with it. The Android app sends no `Origin`, and no web page should call this API (the web arcade has its own server), so name only the host itself. |
| `ARCADE_TRUST_PROXY` | `1` behind a reverse proxy | See "Behind a proxy" below |
| `ARCADE_DB` | Default `data/arcade.sqlite` | Inside the volume |
| `ARCADE_BANK` | Default `data/bank` | Baked into the image |
| `PORT` | Default `8787` | |

To generate a secret:

```bash
node -e "console.log(crypto.randomUUID()+crypto.randomUUID())"
```

**What a refused start looks like.** The process exits before it opens a socket or the database:

```
Error: Refusing to start:
  - ARCADE_SECRET is the development default, which is published in this repo.
```

`ARCADE_ALLOW_DEV_SECRET=1` exists for local development only. Never set it on a host.

## Docker

```bash
docker build -t dgd-arcade:50b46d5 .
```

```bash
docker run -d --name dgd-arcade --restart unless-stopped -p 127.0.0.1:8787:8787 -v dgd-arcade-data:/app/data --env-file arcade.env dgd-arcade:50b46d5
```

- **Mount a volume at `/app/data`.** Without one, every redeploy starts players, XP and growth from nothing.
- **The volume holds `arcade.sqlite`** and its `-wal` and `-shm` files.
- **The question bank sits inside the volume path.** The image copies it to `/app/data/bank`, under the volume.
  - **Named volume:** Docker seeds a new named volume from the image, so the bank arrives on first run. It is never refreshed after that, so a bank update in a later image does not reach an existing volume.
  - **Bind mount:** hides the bank entirely.
  - **Does it matter for DGD App 2.1?** Not much, because the bank only feeds Tablet Run. But the server refuses to start if the bank parses to zero items, so a hidden bank fails loudly.
  - **The fix:** a one-line Dockerfile change, moving the bank to `/app/bank` and setting `ARCADE_BANK`. Say if you want it, and we will make it in the server repo.
- **The process closes the database cleanly** on SIGTERM and SIGINT.

## Host and TLS

Production is `https://arcade-api.digitalgold.co`, which is compiled into DGD App 2.1.0.

- **The host needs** a DNS record and a TLS certificate for it.
- **Serve the API at the root:** `/healthz` and `/v1/...`, with no path prefix. The app calls `https://arcade-api.digitalgold.co/v1/players` and so on.
- **Keep it off the web arcade's proxy and database.** README, "Separate from the web arcade", says why.

## Behind a proxy

The intended deployment is TLS terminated at a reverse proxy, with `ARCADE_TRUST_PROXY=1`.

**Why one proxy hop matters.** The rate limiter keys anonymous calls on the last address in `X-Forwarded-For`. That entry is the one appended by the proxy nearest the server, so the setup assumes exactly one trusted hop:

- **Chained proxies** (a CDN in front of a load balancer, say) would make every client look like the CDN. In that case, have the inner proxy overwrite `X-Forwarded-For` with the real client address.
- **Without `ARCADE_TRUST_PROXY`,** the limiter keys on the socket address. That is correct for a direct bind and wrong behind a proxy, where every client looks like the proxy. The server prints a warning at start in that case.

Authenticated calls are keyed on a hash of the bearer token, so they are unaffected by any of this.

## Health

- **`GET /healthz` returns `{"ok":true,"bank":170,"day":273}`.** It answers once the bank has parsed and the database has opened. The image's `HEALTHCHECK` polls it every 30 s.
- **`bank` is the number of questions.** It should be 170 at this commit.
- **`day` counts UTC days since 1 Jan 2026.**

## Backups

This command is safe while the server is live. It takes a consistent copy, WAL included:

```bash
docker exec dgd-arcade node -e "new (require('node:sqlite').DatabaseSync)('data/arcade.sqlite').exec(\"VACUUM INTO 'data/backup-\"+new Date().toISOString().slice(0,10)+\".sqlite'\")"
```

Afterwards, copy the dated file off the host and delete it from the volume.

**Restoring:** stop the container, replace `arcade.sqlite` and remove its `-wal` and `-shm` files, then start the container again.

## Limits and caps

All of these are environment-overridable, so they can be retuned without a deploy.

| Variable | Default | What it bounds |
|---|---|---|
| `RATE_PER_MINUTE` | 120 | Requests per minute per token or address on `/v1/*` |
| `PLAYERS_PER_HOUR` | 10 | New registrations per address per hour. Phones behind a carrier's shared address count as one, so watch for `429 signup_rate_limited` at launch and raise it if needed (README, "What traffic to expect") |
| `MINI_REWARDED_ROUNDS_PER_DAY` | 10 | Rounds per game per player per UTC day that earn XP and growth; later rounds are practice |
| `PASSAGE_JUVENILE_AT` | 1200 | Lifetime When Pigs Fly points for the second growth stage |
| `PASSAGE_RAZORBACK_AT` | 4000 | Lifetime points for the third stage |

**Fixed in code:**

- **Minimum round durations:** 15 s for Coin Quest and 4 s for When Pigs Fly. A faster claim gets `409 too_fast`.
- **Round expiry:** a round left open for more than an hour can no longer be claimed.
- **Per-round ceilings:** 200 XP per round, at most 3 stars, and a When Pigs Fly score of at most 1999.

## Tuning When Pigs Fly from real runs

The growth thresholds were set from simulated players. Once real runs exist:

```bash
docker exec dgd-arcade npm run report:passage -- --since-days 14
```

- The report is read-only. It covers score percentiles, star counts and eras reached.
- Add `--json` for machine-readable output.
- Send it to us after the first couple of weeks, and we will propose new values for the two `PASSAGE_*` variables.

## Routes present but unused by DGD App 2.1

The server also carries Tablet Run (`/v1/expeditions/...`), the Daily Ledger (`/v1/ledger/...`), and three older mini games (`pillar_sort`, `design_or_myth`, `chain_builder`).

- DGD App 2.1 calls none of them.
- They need a registered token like everything else, and they are covered by the same tests.

They can stay. If you would rather not expose them, block those path prefixes at the proxy.

## After every deploy

```bash
node smoke.mjs https://<host>
```

The smoke test registers one throwaway player, walks the routes in `API.md`, checks the refusals, and deletes the player. It exits non-zero on any failure.
