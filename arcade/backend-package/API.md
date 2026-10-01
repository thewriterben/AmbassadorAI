# What DGD App 2.1 calls

## Basics

- **Base URL:** `https://arcade-api.digitalgold.co`, which is what DGD App 2.1.0 is built with (`ARCADE_API`).
- **Format:** every body is JSON.
- **Auth:** everything except registration and health sends `Authorization: Bearer <token>`.
- **Errors:** the body is `{"error":"<code>"}` with the status shown in the tables below.

**When the client registers.** The client calls `POST /v1/players` once, on first use, and stores the token on the device.

**There are no accounts:**

- no name, email or phone number;
- the handle is assigned by the server and never typed;
- the token is the only credential, and the server keeps only its SHA-256.

**Errors common to every route:**

| Status | Code | When |
|---|---|---|
| 401 | `unauthorized` | Missing or unknown token |
| 403 | `account_closed` | The player has been banned |
| 409 | `corrupt_state` | A JSON column failed to parse, which means a damaged database. This is handled; the server returns no stack trace. |
| 429 | `rate_limited` | Over `RATE_PER_MINUTE` |
| 500 | `internal` | Anything else. The detail goes to the log, not to the client. |

## Routes

### `GET /healthz`

No auth. Returns `{ ok, bank, day }`.

### `POST /v1/players`

No auth. The body is `{ deviceHint }`: the platform name, such as `android`, cut to 120 characters.

- Returns `201 { playerId, token, progress }`.
- Has its own bucket, `PLAYERS_PER_HOUR` per address. Over it, the call gets `429 signup_rate_limited`.

### `GET /v1/me`

Returns the progress snapshot plus today's state:

- **Snapshot:** `playerId`, `handle`, `xp`, `weeklyXp`, `level`, `levelProgress`, `badges`, `miniPlays`, `passage` (the When Pigs Fly growth, points, abilities and loadout), and `status`.
- **Today:** `day`, plus the caps.

### `DELETE /v1/me`

Erases the player and every row keyed to them, in one transaction.

- Returns `{ deleted: true, rows: { <table>: n } }`.
- The token stops working at once.
- Settings in the app calls this route.

### `POST /v1/me/handle/reroll`

Assigns a new generated handle.

- Allowed 3 times per UTC day.
- After that, the call gets `429 reroll_limit` with the current handle.

### `GET /v1/leaderboard?limit=n`

The weekly XP board, which resets at Monday 00:00 UTC.

- `limit` is clamped to between 3 and 100; junk values fall back to 50.
- Banned players are excluded.
- Each row is `{ rank, handle, xp, you }`.

### `POST /v1/mini/:game/start`

`game` is `coin_quest` or `passage` (When Pigs Fly).

- Opens a round and returns `201 { token }`, a signed round token.
- An unknown game gets `404 unknown_game`.

### `POST /v1/mini/:game`

Claims a round with `{ token, right, total, extra, score, loadout }`. See "Claims" below.

### `POST /v1/passage/abilities/:ability/upgrade`

Spends When Pigs Fly points on the next level of an ability.

- Returns the new progress.
- `404 unknown_ability`.
- `409 not_enough_points` or `409 max_level`, plus the current progress.

### `POST /v1/passage/loadout`

Equips up to 2 owned abilities, sent as `{ abilities: [...] }`.

- A loadout of abilities the player does not own gets `400 invalid_loadout`.

## Claims

**What the fields mean depends on the game:**

| Game | `right` | `extra` | `score` | `loadout` |
|---|---|---|---|---|
| `coin_quest` | Stars earned, 0 to 3 | Level id | Ignored | Ignored |
| `passage` | Stars, 1 to 3 | Eras reached, 0 to 9 | Coin score, at most 1999 | The abilities flown with, and their levels |

**What the server enforces:**

- **One claim per round token.** A second claim gets `409 already_claimed`. The claim is atomic, so two simultaneous claims cannot both pay.
- **Expiry and the minimum duration.**
  - The round must still be open. After an hour, the claim gets `409 round_expired`.
  - It must have been open for the game's minimum duration. A faster claim gets `409 too_fast`.
- **Belonging.** The round must belong to this player and this game, or the claim gets `404 round_not_found`. A claim with no token gets `400 round_token_required`.
- **Clamping.** Every number is clamped to the game's ceiling, and non-numbers become 0.
- **Daily rewarded rounds.**
  - Only the first `MINI_REWARDED_ROUNDS_PER_DAY` claimed rounds per game per UTC day pay XP and growth.
  - The day counted is the day the round was opened.
- **Loadout checks.** A When Pigs Fly claim with abilities the player does not own, or at a higher level than owned, is recorded and pays nothing. The response says `loadoutRejected: true`.

**Response:** `{ xpGained, badges, rewardedRoundsLeft, progress }`. When Pigs Fly claims also return `passageCredited`.

**XP per round:**

| Game | XP |
|---|---|
| Coin Quest | 20 per star, plus 20 for three stars |
| When Pigs Fly | 12 per star, plus 24 for two stars or more, plus up to 12 from the score (1 per 50 points) |

The When Pigs Fly score also grows the boar and funds the shop.

**None of this has monetary value.** XP, points and standings are recognition only, and the app says so on screen.
