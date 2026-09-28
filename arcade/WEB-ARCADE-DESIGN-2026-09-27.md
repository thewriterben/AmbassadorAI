# DGD web arcade — digitalgold.co/arcade

**Status 2026-09-27: working prototype, rewards in dry run.** Every result is
verified and recorded; every amount is zero; nothing is owed or paid. This
document is for DGD backend engineering (hosting, sign-in, payout) and for
counsel (the gates before rewards go live).

---

## 1. What it is

The same Coin Quest levels as the phone app, played in a browser at
`digitalgold.co/arcade`, with the ability to reward results.

| Part | What | Where |
|---|---|---|
| **Web client** | Flutter web app. Depends on the phone game (`puzzle-app`) by path, so it plays the identical engine, art and sound. | `client/` |
| **Rewards server** | Node 24 + Hono + SQLite. Issues seeds, verifies results by replay, keeps the reward ledger. | `server/` |
| **Replay engine** | The game's four pure-Dart model files, compiled to JavaScript, run inside the server in a sealed VM context. | `engine/` → `server/engine/replay.js` |

## 2. Why the server can trust a result it did not see

The server never takes the browser's word for a score.

1. **Start**: the player picks a level; the server picks a random seed, stores
   it with the run, and returns it.
2. **Play**: the browser builds the board from that seed and records only the
   swaps the engine accepted. Nothing else is reported.
3. **Finish**: the browser sends the list of swaps. The server rebuilds the
   board from *its* seed and replays them through the same engine. The score,
   stars and win/loss the server computes are the only ones it records. The
   browser's own score is kept only to detect disagreement (`client-mismatch`).

**Proven, not assumed:**

- 300 game transcripts played on the Dart VM replay identically on the
  dart2js build the server uses (`server/test/engine.test.ts`).
- Four real levels were played in headless Chrome by dragging coins on the
  canvas, 58 swaps in all, three wins and one loss. Browser and server agreed
  on every score, every time (`tools/e2e`).
- A drift test fails the build if the engine copy differs by one byte from
  the phone game's model (`engine/test/replay_test.dart`).

**What replay stops, and what it does not.** It stops invented scores, edited
move lists, moves on someone else's board and "finishing" a run twice. It
does **not** stop a program that plays well: the seed has to reach the
browser, so a bot can read the board. That is contained by what a first is
worth, not by detection — see §5.

## 3. Sign-in: what DGD needs to provide

The arcade has no accounts. A player is a digitalgold.co account.

**DGD adds one endpoint on the main site**, served under the site's own session
cookie:

```
GET https://digitalgold.co/api/arcade/token
  signed in  -> 200 {"token": "<JWT>"}
  signed out -> 401
```

The JWT:

| Field | Value |
|---|---|
| header | `{"alg":"ES256","typ":"JWT"}` — exactly ES256 |
| `sub` | stable account id (not the username: usernames are invite codes) |
| `iss` | `https://digitalgold.co` |
| `aud` | `digitalgold.co/arcade` |
| `iat`, `exp` | lifetime at most 15 minutes |
| `email_verified` | boolean |
| `eligible` | boolean — DGD's decision on age, region and anything counsel requires |

DGD keeps the private key. The arcade gets the **public** key only
(`DGD_TOKEN_PUBLIC_KEY`, PEM, P-256). The arcade therefore cannot mint
tokens, never sees a DGD password or cookie, and stores only `sub`.

Tests cover: missing token, garbage, wrong key, `alg: none`, HS256 signed
with the public key, wrong issuer, wrong audience, expired, over-long
lifetime, tampered payload.

## 4. Deploying at /arcade

Same origin as the main site, so no CORS and no third-party cookies.

| Path | Serves |
|---|---|
| `/arcade/` | `build/web` (Flutter, built with `--base-href /arcade/`). Static; any web server. |
| `/arcade/api/*` | the rewards server (reverse proxy to `PORT`, default 8790) |
| `/api/arcade/token` | **DGD's** endpoint above, on the main site |

Environment (production refuses to start without these):

| Variable | |
|---|---|
| `ARCADE_ENV=production` | enables the checks below |
| `AUTH_MODE=dgd` | dev sign-in refused in production |
| `DGD_TOKEN_PUBLIC_KEY` | PEM, P-256 |
| `DB_PATH` | SQLite file on persistent disk. Separate from the phone arcade's database; they share nothing. |
| `RULES_PATH` | `rules.json` |
| `ADMIN_TOKEN` | optional, ≥ 32 chars; enables `/arcade/api/admin/ledger.csv` |
| `REWARDS_LIVE_ACK` | must equal `counsel-approved-rewards-live` for `dry_run: false` to be accepted |

The build has no CDN dependency (`--no-web-resources-cdn`): CanvasKit and the
fonts are served from `/arcade/` itself.

## 5. Rewards

Configured entirely in `rules.json`. The shipped file has every amount at 0 and
`dry_run: true`.

| Rule | Meaning |
|---|---|
| `first_win` | once per player per level, the first time it is won (`by_level` overrides) |
| `new_star` | once per new best star on a level |
| `daily_cap_per_player` | most one player can accrue per UTC day; 0 = nothing |
| `daily_budget_total` | most everyone together can accrue per UTC day; 0 = nothing |
| `min_ms_per_move` | faster than this, the run is **held** for a person, not paid |
| `max_runs_started_per_hour` | per player |
| `run_ttl_minutes` | an unfinished run expires |

**Only firsts are rewarded.** Replaying a level earns nothing. That is the main
defence against bots and farming: the most a perfect player can ever accrue
is 60 first wins plus 180 stars, whatever they do, and caps bound it per day.
DGD can price that ceiling before choosing amounts.

Ledger statuses: `would_award` (dry run), `owed`, `held` (review), `void`
(ineligible). **The server never records `paid`.** Paying is an operation DGD
performs against `owed` entries elsewhere; the ledger says who earned what
under which rules. Every trigger is recorded even at zero, so the dry run is
also a cost model: `ledger.csv` shows what any set of amounts would have
cost against real play.

One open run per player: starting another abandons the first, so a player
cannot hold several seeds and play the best board.

## 6. What must stay separate from the phone app

This arcade exists because the phone app may not reward play (App Review
3.1.5(v); `B1-DECISION-2026-09-21.md`, question 4). That separation is the
whole basis, so:

- **The phone app never links here.** Not a button, not a QR, not a share
  message. It links to `digitalgold.co` plainly and nothing more.
- **No progress crosses from app to web.** Web levels start from zero; nothing
  from the phone arcade counts here. (Web → app read-only display is allowed
  later, per the decision document.)
- **No shared identity or database.** The phone arcade uses assigned handles
  and its own server; this uses digitalgold.co accounts and its own database.
- **No reward code in the phone app.** The web client depends on the game;
  the game does not depend on the web client. `puzzle-app` contains none of
  this.
- **No attribution** from the app to the web arcade.

## 7. Gates before `dry_run: false` — counsel's, not engineering's

The server enforces the mechanics; it cannot decide these:

1. **Official rules** published at `/arcade`, stating eligibility, what can be
   earned, caps, review, and that no purchase is needed.
2. **Eligibility**: minimum age, excluded jurisdictions, employee exclusion.
   DGD sets `eligible` in the token accordingly.
3. **Prize and skill-contest law** in each jurisdiction where players are.
4. **Tax** reporting thresholds for recipients, and what DGD collects to meet them.
5. **Payout**: to which address, KYC at what threshold, and who runs it.
6. **DGD's legal character**: what paying it for play means.
7. **Privacy notice** for the arcade (the server stores `sub`, run times and
   moves).

Switching on also needs `REWARDS_LIVE_ACK` set by whoever deploys, so a
`rules.json` edit alone cannot start owing money.

## 8. Not in this prototype

- **Quiz rewards.** The phone arcade's knowledge tablets are server-graded and
  could be rewarded the same way; not wired here yet.
- **Mini-games.** Their scores are client-asserted (R2 in the phone audit), so
  they are not rewardable until they get their own replay or server-side grading.
- **Leaderboard.** If added, it must not show DGD usernames (they are invite
  codes); use assigned handles as the phone app does.
- **Level unlock order** is enforced in the UI only. The server does not need
  it, since every reward is a first.

## 9. Running it locally

```sh
# engine (after any change to puzzle-app's model: tools/sync_assets.ps1 first)
cd engine && dart test && dart run tool/gen_transcripts.dart
dart compile js -O2 --no-source-maps -o ../server/engine/replay.js bin/replay_js.dart

# server
cd server && npm ci --ignore-scripts && npm test
STATIC_DIR=../build/web-dev node src/index.ts          # dev auth, dry run

# client (dev build signs in via the server; never deploy it)
cd client && flutter test
flutter build web --release --base-href /arcade/ --no-web-resources-cdn \
  --dart-define=ARCADE_DEV_AUTH=true -o ../build/web-dev

# end to end
cd tools/e2e && npm ci && node e2e.mjs http://localhost:8790/arcade/ 1 2 3 7
```

The production client is the same command **without** `ARCADE_DEV_AUTH`.
