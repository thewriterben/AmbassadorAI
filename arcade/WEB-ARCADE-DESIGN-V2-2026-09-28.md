# DGD web arcade V2 — digitalgold.co/arcade

**Status 2026-09-28: V2 working prototype, rewards in dry run.** Two featured
games, Coin Quest and When Pigs Fly, both verified by replay; a knowledge
check; a leaderboard; payout tooling for DGD operations; guest play and a
rules page, so the phone app's neutral link lands on games (§7, §7a). Every result is
verified and recorded; every amount is zero; nothing is owed or paid. This
document is for DGD backend engineering (hosting, sign-in, payout) and for
counsel (the gates before rewards go live).

---

## 1. What it is

| Part | What | Where |
|---|---|---|
| **Web client** | Flutter web. Depends on the phone game (`puzzle-app-v2`) by path, so both games run the identical engine, art and sound. | `client/` |
| **Rewards server** | Node 24 + Hono + SQLite. Issues seeds, verifies results by replay, runs the shop, the board and the knowledge check, keeps the ledger. | `server/` |
| **Replay engine** | Both games' pure-Dart rules (Coin Quest's model; When Pigs Fly's simulation), compiled to JavaScript and run inside the server in a sealed VM context. | `engine/` → `server/engine/replay.js` |
| **Operations CLI** | Review, batch, export, settle. | `tools/admin.mjs` |

The home page features the two games; the knowledge check, the leaderboard
and the player's own record sit below them. The phone app is unchanged: it
keeps its own arcade and never links here (§7).

## 2. Why the server can trust a result it did not see

The server never takes the browser's word for a score.

**Coin Quest.** The server picks the seed; the browser records only the swaps
the engine accepted; the server rebuilds the board from *its* seed and
replays them.

**When Pigs Fly.** The game was split so its whole simulation is pure Dart
(`puzzle-app-v2`, `lib/arcade/passage/sim/`) and steps at a fixed 120 ticks a
second with exact arithmetic (no platform `sin`/`cos`). On the web it always
runs at one fixed size, 450×800, scaled to the window. The server picks the
seed **and** the boar stage and abilities the run flies with; the browser
records `[tick, input]` for each flap or ability; the server replays those
inputs against its own seed, stage and loadout. A flight claiming a loadout
the player does not own, a reordered or invented input, or an input that
would have done nothing is refused.

The browser's own score is kept only to detect disagreement
(`client-mismatch`), which would mean either a tampered client (harmless) or a
determinism bug (serious).

**Proven, not assumed:**

| Check | Result |
|---|---|
| Coin Quest: 300 VM transcripts replayed by the server's dart2js build | identical |
| When Pigs Fly: 24 VM transcripts (every stage, every ability, a full three-star passage) replayed by the server's build | identical |
| Phone game after the simulation split: its existing test suite | 118/118 pass, plus 9 new replay tests (frame jitter, abilities, forged transcripts) |
| Coin Quest in headless Chrome, coins dragged on the canvas | 6 levels (5 wins, 1 loss): every score agreed |
| When Pigs Fly in headless Chrome, whole flights at real frame timing | 5 flights (scores 321–638, one three-star clean landing): every score and every tick agreed |
| Engine copy vs phone game source | drift test fails the build on any difference |

**What replay stops, and what it does not.** It stops invented scores, edited
transcripts, runs on someone else's seed, loadouts not owned, and finishing a
run twice. It does **not** stop a program that plays well: the seed has to
reach the browser. That is contained by what a first is worth (§5), by caps,
and by review of anything implausibly fast — a flight whose wall-clock time
is under 90% of its simulated time is held, because the game cannot run
faster than real time.

## 3. Sign-in: what DGD needs to provide

The arcade has no accounts. A player is a digitalgold.co account.

```
GET https://digitalgold.co/api/arcade/token
  signed in  -> 200 {"token": "<JWT>"}
  signed out -> 401
```

| JWT field | Value |
|---|---|
| header | `{"alg":"ES256","typ":"JWT"}` — exactly ES256 |
| `sub` | stable account id (**not** the username: usernames are invite codes) |
| `iss` / `aud` | `https://digitalgold.co` / `digitalgold.co/arcade` |
| `iat`, `exp` | lifetime at most 15 minutes |
| `email_verified`, `eligible` | booleans; `eligible` is DGD's decision (age, region, whatever counsel requires) |

DGD keeps the private key; the arcade gets the public key only. It never sees
a DGD password or cookie and stores only `sub` plus an **assigned handle**
(e.g. "Steady Ledger 418") for the leaderboard.

## 4. Deploying at /arcade

| Path | Serves |
|---|---|
| `/arcade/` | `build/web` (static; built with `--base-href /arcade/ --no-web-resources-cdn`) |
| `/arcade/api/*` | the rewards server (reverse proxy to `PORT`, default 8790) |
| `/arcade/api/admin/*` | operations; needs `ADMIN_TOKEN`. DGD may prefer to expose it only on an internal network. |
| `/api/arcade/token` | **DGD's** endpoint above, on the main site |

| Variable | |
|---|---|
| `ARCADE_ENV=production` | enables the refusal checks |
| `AUTH_MODE=dgd`, `DGD_TOKEN_PUBLIC_KEY` | required in production |
| `DB_PATH` | SQLite on persistent disk; separate from the phone arcade's |
| `RULES_PATH` | `rules.json` |
| `BANK_PATH` | the knowledge-check bank (default `./bank`; server only) |
| `ADMIN_TOKEN` | ≥ 32 chars; absent = every admin path answers 404 |
| `REWARDS_LIVE_ACK` | must equal `counsel-approved-rewards-live` for `dry_run: false` |
| `NETWORK_HASH_KEY` | optional, ≥ 32 chars; enables the keyed network hash for the shared-network signal (§5b) |
| `TRUST_PROXY=1` | behind DGD's reverse proxy: read the client address from `X-Forwarded-For` |
| `REVIEW_DIR` | optional; serves the reviewer console (`build/review`) at `/arcade/review/` |

## 5. Rewards

All in `rules.json`; the shipped file has every amount at 0 and `dry_run: true`.
**Every reward is a first**, so repeating something earns nothing:

| Game | Trigger | Rule | Ceiling per player, ever |
|---|---|---|---|
| Coin Quest | first win of a level | `coin_quest.first_win` (`by_level` overrides) | 60 |
| Coin Quest | each new best star on a level | `coin_quest.new_star` | 180 |
| When Pigs Fly | first whole passage (2 stars) | `pigs.first_two_stars` | 1 |
| When Pigs Fly | first clean landing (3 stars) | `pigs.first_three_stars` | 1 |
| When Pigs Fly | each new best-score tier (`best_score_tier_size` points) | `pigs.best_score_tier` | `max_best_tiers` (20) |
| Knowledge check | first right answer to each stable question | `quiz.first_correct` | ~170 (the bank); volatile items never reward |

Bounds on top: `daily_cap_per_player`, `daily_budget_total` (both 0 now),
`max_runs_started_per_hour`, `quiz_questions_per_day`, one open run per player
(starting another abandons it, so no seed shopping).

**Held for review, not paid:** Coin Quest faster than `min_ms_per_move`; a
flight faster than `pigs_min_realtime_percent` of real time; a quiz answer
faster than `quiz_min_answer_ms` is recorded but not rewarded; any player DGD
has put on hold. A held run does not move the player's best, so a later clean
run is measured from the old bar.

**Not yet eligible** accounts record nothing — their firsts stay available for
when DGD marks them eligible. (Recording them as void would forfeit them.)

**Play points** in When Pigs Fly (growth and the ability shop) come from the
first `pigs_credited_runs_per_day` clean flights a day. They buy only
abilities and are not in the ledger; they have no value outside the game.
Prices and growth thresholds match the phone game's, but the two are separate
ledgers: nothing earned on the phone counts here.

## 5a. Top 100 boards and their prizes (DGD's decision, 2026-09-28)

Four boards: **When Pigs Fly** and **Coin Quest**, each **daily** (UTC day) and
**yearly** (UTC calendar year), 100 places each.

| Board | Ranked by | Each winner (`rules.json`) |
|---|---|---|
| When Pigs Fly, daily / yearly | best single verified flight score in the period | $5.00 / $50.00 validation credit |
| Coin Quest, daily / yearly | sum of the best verified *winning* score on each level in the period | $5.00 / $50.00 validation credit |

- **The prize** is a *non-transferable DGD validation credit*, recorded in its
  own unit (`USD_VALIDATION_CREDIT`, cents) alongside, never mixed with, DGD.
  What it may be spent on, how it is delivered and how long it lasts are
  counsel's and DGD's to define (rules page placeholders).
- **Order**: value, then who reached it first, then account id, so exactly
  100 win. Too-fast runs and players under review are off the board.
- **Eligibility** is stored from each sign-in token (`players.eligible`).
  Ineligible players keep their place; the prize goes to the next eligible.
- **Settlement**: the server settles every closed day and year at start and
  every 10 minutes (`settleBoards`, also `POST /admin/boards/settle`); each
  period is settled once (`board_settlements`) and each prize can be
  recorded once (ledger UNIQUE).
- **Every prize is held.** A person at DGD reviews the run(s) behind it
  (`admin.mjs review`, `runs <sub>`, `board <game> <period> <at>`) and
  approves or voids. Prizes are not bounded by the DGD daily caps; their cost
  is fixed by the number of places. Batches are per unit
  (`admin.mjs batch --credit`).
- **Cost at the top end**: 2 games × 100 × $5 × 365 = **$365,000 a year**,
  plus 2 × 100 × $50 = **$10,000** for the yearly boards.
- **Why review matters most here.** Firsts cap what any player can accrue;
  ranked prizes pay whoever is best every day. Replay proves a run obeyed the
  game, not that a person played it — the test autopilot flies 300–600.
  One verified person per account (DGD's `eligible`) and review of every
  winner are what stand between the prize pool and a bot farm.

## 5b. The reviewer console and its signals

Every Top 100 prize, and every first from a held run or player, waits for a
person. The **reviewer console** (`client/lib/review/`, its own build,
`build/review`, served at `/arcade/review/` when `REVIEW_DIR` is set) is where
they work:

- **Queue**: every held entry, flagged ones first, with its amount.
- **Entry**: the plain-language flags, the account's signals, the run(s)
  behind it (for a Coin Quest prize, the best winning run on each level), and
  Approve / Void (with a reason) / Hold this player. Every decision is in the
  audit log under the reviewer's name.
- **Watch a run**: the console runs the same simulation as the server with the
  run's seed, stage, abilities and inputs, and draws it plainly — openings,
  coins, the boar's collision capsule, each flap — with play at 1–8×,
  scrubbing, and a timeline of every flap (red: within 67 ms of the last).
  Coin Quest steps through the board swap by swap. At the top it says whether
  its own result matches the server's; they must agree.

The token and name are held in memory for the tab only, never stored or put
in a URL. The console's files hold no secrets; its data needs `ADMIN_TOKEN`.
DGD may prefer to serve it only on an internal network.

**Signals** (`server/src/signals.ts`) — hints for a person, never verdicts;
nothing is held, voided or paid because of them:

| Signal | Flagged when | Why |
|---|---|---|
| Fast flaps | > 10% of flaps within 67 ms of the last | people cannot sustain it; our transcript bot does it on 40–90% of flaps |
| Flap rate | > 8 a second over the flight | the same, averaged |
| One rhythm | > 35% of intervals within ±1 tick of one value | timer-driven play repeats itself |
| Coin Quest pace | < 900 ms a move on average | fast, though above the hard 300 ms hold |
| New account | first seen < 2 days before the winning run | throwaway accounts |
| Round the clock | play in ≥ 20 hours of the day in a week | people sleep |
| Shared network | ≥ 2 other accounts played from the same network in the period | account farms |
| Score disagreement | the browser reported a different score from the replay | tampering, or a bug |

**The thresholds are uncalibrated**: there is no real play yet, only our own
bots. `GET /admin/signals?game=&days=` gives their distribution over recent
runs; move them once real players have played for a few weeks.

**Network**: with `NETWORK_HASH_KEY` set (≥ 32 chars), the server keeps a
keyed HMAC of the network each run started from (IPv4 /24, IPv6 /48) — not the
address — and clears it after 90 days. Behind DGD's proxy set `TRUST_PROXY=1`
so it reads `X-Forwarded-For`. Unset, nothing is recorded and the shared-network
signal is simply absent. The rules page's privacy section says so.

## 6. Payout tooling — the server never pays

Ledger statuses: `would_award` (dry run) → `owed` → `batched` → `settled`;
side exits `held` (review) and `void`.

```
OPERATOR="Jane Ops" ADMIN_TOKEN=... ARCADE_URL=https://digitalgold.co/arcade/api node tools/admin.mjs <cmd>
  review                         held entries, held/banned players, flagged runs
  approve <entry> | void <entry> [reason]
  player <sub> ok|held|banned [reason]
  settle-boards | board <game> <day|year> <at> | runs <sub> | run <id> | signals [game] [days]
  batch [--credit] [note]        every owed entry of one unit (DGD, or --credit) into a new open batch
  export <batch> [file]          one row per player: sub, unit, entries, amount
  settle <batch> <reference>     after DGD has paid, with DGD's own payment reference
  cancel <batch>                 back to owed
  ledger [file] | audit
```

`settle` records an operator's statement, with a reference, that DGD paid
outside this system. The server holds no wallet addresses and moves nothing;
DGD maps `sub` to a payout destination in its own systems. Every admin action
is in the append-only audit log with the operator's name. Approvals still
respect the day's caps.

## 7. What must stay separate from the phone app

This arcade exists because the phone app may not reward play (App Review
3.1.5(v); `B1-DECISION-2026-09-21.md`). So:

- **The phone app links here only neutrally** (DGD's choice, 2026-09-28;
  counsel has the final say). Android 1.0.7's Arcade menu has one item,
  *"DGD Arcade for Web — Play in your browser"*, that opens exactly
  `https://digitalgold.co/arcade/` in the phone's own browser. No reward,
  earn or opportunity wording; no parameters; never a WebView; never on a
  result screen. Pinned by `WebArcadeLinkTest` in `dgd-native`. iOS follows
  with its Arcade entry point (`integration/IOS-WEB-ARCADE-LINK.md`).
- **This site treats app visitors like anyone else.** It never reads the
  Referer, the User-Agent or any campaign parameter, sends
  `Referrer-Policy: no-referrer`, and has no app-only anything. A server test
  fails if a source file starts reading those.
- **The link lands on games, not on a reward offer.** `/arcade/` is playable
  as a guest; rewards are disclosed in one line on the landing with the
  rules a tap away (§7a).
- **No progress crosses from app to web.** Web boars start as piglets; web
  levels start locked.
- **No shared identity or database.** The phone arcade has its own handles and
  server; the web client's production build contains none of the phone
  arcade's endpoints (checked in the compiled JavaScript).
- **No reward code in the phone app.** The web client depends on the game; the
  game does not depend on the web client.
- **No attribution** from the app to the web arcade.

## 7a. Guests, the landing, and the rules page

- **Guest play.** A visitor who is not signed in plays both games in full
  (Coin Quest levels unlock in order; When Pigs Fly flies the piglet with no
  abilities). Guest games are seeded in the browser and **never sent to the
  server** — not while playing and not after signing in; there is no endpoint
  that would accept them. Guest progress is kept in that browser only. A
  guest can read the leaderboard (`GET /v1/public/leaderboard`) but is never
  on it. `tools/e2e/e2e_guest.mjs` fails if a guest game makes any request
  other than the public rules and board.
- **Signing in is the opt-in** to a verified record, the board, growth and
  the shop, the knowledge check, and rewards. Guests who tap *Sign in* go to
  `DGD_SIGNIN_URL` (default `/login?next=/arcade/` — **DGD to confirm**).
- **Landing.** Leads with the two games. One plain line under the title
  discloses that signed-in, eligible players can receive DGD for firsts (and
  that it is test mode while `dry_run` holds), with a *Rules* link.
- **`/arcade/rules.html`.** Static, readable without the game or JavaScript
  for its text; the amounts table is filled live from `/v1/rules` so it always
  matches what the server enforces. Sections marked COUNSEL are placeholders:
  eligibility, review and appeal, delivery, privacy, sponsor, changes. States
  plainly that nothing done in the mobile app counts and that Apple and Google
  are not sponsors.

## 8. Gates before `dry_run: false` — counsel's, not engineering's

1. **Official rules**: `/arcade/rules.html` has the structure and live
   figures; counsel writes the sections marked COUNSEL.
2. **Eligibility**: minimum age, excluded jurisdictions, employee exclusion —
   DGD sets `eligible` in the token.
3. **Prize and skill-contest law** where players are. When Pigs Fly is a
   game of skill with a seeded layout; counsel should confirm that framing.
   The Top 100 boards are ranked prize contests: official-rules content,
   any state registration or bonding thresholds (the yearly pool alone is
   $10,000), and what a "validation credit" is legally.
4. **Tax** thresholds and what DGD collects to meet them. A daily Top 100
   winner can pass common reporting thresholds within a year ($5 × 365 =
   $1,825 per board).
5. **Payout**: destination, KYC threshold, who runs `settle`.
6. **DGD's legal character**: what paying it for play means.
7. **Privacy notice**: the server stores `sub`, a handle, run times, moves
   and inputs, quiz answers, and (if enabled) a keyed network hash for 90
   days; staff may watch replays of winning runs.

`REWARDS_LIVE_ACK` must also be set by whoever deploys, so a `rules.json` edit
alone cannot start owing money.

## 9. Not in V2

- **Other phone mini-games.** Their scores are client-asserted; not rewardable
  until each gets a replayable core like When Pigs Fly's.
- **Web → app read-only display** of the board (allowed by the decision
  document; not built).
- **Level unlock order** is UI only; the server does not need it.

## 10. Running it locally

```sh
powershell tools/sync_assets.ps1          # after any change to puzzle-app-v2 or the bank

cd engine && dart test && dart run tool/gen_transcripts.dart
dart compile js -O2 --no-source-maps -o ../server/engine/replay.js bin/replay_js.dart

cd server && npm ci --ignore-scripts && npm test
STATIC_DIR=../build/web-dev node src/index.ts          # dev auth, dry run

cd client && flutter test
flutter build web --release --base-href /arcade/ --no-web-resources-cdn \
  --dart-define=ARCADE_DEV_AUTH=true -o ../build/web-dev   # never deploy this one

powershell tools/e2e/run_all.ps1          # both games in headless Chrome
```

The production client is the same build command **without** `ARCADE_DEV_AUTH`.
`puzzle-app-v2` must be a sibling folder at the current V2 build: branch
`v2/ten-games`, commit `62296ce` or later (which includes
`web/replayable-passage`). Built against `62296ce` on 2026-09-28: new boar art
with room for the wings, the boar's and the abilities' own sounds, polished
coins, and the growing-up moment (played on the web when a verified flight's
points carry the boar into its next stage). That build also adds an easier
passage behind a DEV toggle; the web always flies the standard one, which is
the only one the server replays. Its simulation numbers for the standard
passage are unchanged: all 324 recorded transcripts still replay identically.
