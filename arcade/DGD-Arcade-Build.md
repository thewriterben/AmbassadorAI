# DGD Arcade — build, bundle and hosting notes

Status as of 2026-09-14. The Arcade is a single Flutter codebase (`arcade/app/`) that builds to
Android, iOS and a web bundle. The web bundle is what the PWA pilot ships and what the DGD App's
WebView tab embeds (Integration Brief §"Runtime"). This note records what exists, how it is built,
what it weighs, and what the host has to do.

## What is in the build

| Section | Game | Source | Plan status |
|---|---|---|---|
| Standings | Weekly XP scoreboard | `lib/arcade/leaderboard_screen.dart` | supports §4.2 "XP drives badges and leaderboards" |
| Expeditions | Tablet Run (runner + 3 Knowledge Tablets, spaced retrieval) | `lib/arcade/run/` | MVP |
| Expeditions | Daily Ledger (one shared puzzle a day, 6 tries, streak, share grid) | `lib/arcade/ledger/` | MVP |
| Knowledge mini-games | Pillar Sort · Design or Myth? · Chain Builder | `lib/arcade/mini/` | v1.1 (built early) |
| Arcade | Coin Quest (match-3, 60 vaults across 6 worlds) · Merge · Words · Blocks · Rope | `lib/match3/`, `lib/games/` | not in plan; engagement filler |

The question bank lives only on the server, in `arcade/server/data/bank/` — a directory of
markdown files loaded at startup, so a batch is added by dropping in a new numbered file. It
currently holds **170 items** (A 46 · B 57 · C 41 · D 26) across nine sections, each tracing to a
`LLMWiki/dgd/*` page and a White Paper section. `arcade/tools/bank-lint.py` runs the repo's
communications linter over it and subtracts the reviewed exemptions in `bank/ALLOWLIST.md`;
misconception distractors trip the linter by design, which is what the allow-list is for. That
file is **unreviewed** and needs a compliance sign-off before launch. See `bank/README.md` for the
format and authoring rules.

Explorer track only: XP, levels (500 XP each), badges, ledger streak. No Validator top-ups yet.
Progress is **server-authoritative** (see "Backend" below): the client caches the server's last
snapshot so the home screen renders offline, but nothing it does offline counts. Tablet questions
come from the server's copy of `question-bank-seed.md` and never ship in the client; mini-game
content (pillar statements, myths, chains) lives in `lib/arcade/knowledge/content.dart`, each
item carrying its WP/wiki source.

## Backend (`arcade/server/`)

> **Correction, 2026-09-16.** This section has claimed throughout that the server
> is the sole authority on XP and that the client never submits a score. The
> audit (`AUDIT-2026-09-16.md`) established that this is **false for mini-game
> XP**, which is the majority of obtainable XP: `POST /v1/mini/:game` takes
> `right`/`total` straight from the request body with no issued round and no
> token, and Coin Quest reports through that same path. A second finding, a
> TOCTOU race in `finish`, yields 100× XP from one honest expedition. Both are
> reproduced, both are unfixed, and both must be closed before this is hosted.
> The tablet path — signed single-use questions, nonce, expiry, ordering — was
> attacked directly and does hold.

Node 24 + Hono + `node:sqlite`, TypeScript run directly (no build step). Working copy at
`C:\src\arcade-server`; `npm start` listens on :8787, `npm test` runs the rule tests (9, all
passing). SQLite is the pilot store; the schema is plain SQL so Postgres is a driver swap.

What it enforces (plan §3–5):

| Rule | Implementation |
|---|---|
| Client never holds the bank or the key (§5.1) | `POST /v1/expeditions/:id/tablets/:i` issues one question: prompt + shuffled options + an HMAC-signed token; the answer key stays server-side |
| Single-use, expiring questions | Token = expedition·index·nonce·expiry·signature; DB marks it answered; 20 s window + 4 s grace |
| Minimum answer latency (§4.2) | Server clock: 1.5 s (A) → 3 s (D). Faster answers score wrong and flag `tabletN_fast` |
| Run plausibility (§5.1) | Tablet *i* can't be opened before its run-fraction × 85 s × 0.8; a finish under 85 s or with skipped tablets earns 0 XP and flags `finish_early` / `tablets_skipped` |
| Spaced retrieval (§4.2) | Per-player `tablet_state`: correct → retired 14 d; missed → 1/3/7 d; due misses served first |
| Rewarded expeditions/day | `REWARDED_EXPEDITIONS_PER_DAY` (default 2); further runs are practice — tablets still count toward mastery |
| Daily Ledger | Same UTC-day puzzle for everyone; answer revealed only when the play is over; fixed +50 XP, +100 every 7-day streak; 6 attempts |
| Mini-games | XP-only; server applies the formula and caps rewarded rounds at 10/game/day |
| Idempotency | `finish` replays return the stored result; abandoned expeditions time out after 30 min |
| Abuse ladder (§5.6) | `players.status`: `ok` / `xp_only` / `banned`; every plausibility flag is stored per expedition for review |

### Coin Quest: Digital Gold

60 levels in six worlds.

**Look.** Board pieces are flat Material discs — one tonal fill, an outline ring, the DGD mark in a
darker tint of the same hue, a soft elevation shadow. No lettering, no gradients, no specular
sweep; `GemComponent._renderShine` is a deliberate no-op. The DGD mark on each piece is an
"on-colour" — near-black or white, whichever contrasts more with that fill — at 54% of the sprite,
with no decorative inner ring. It was previously a dark tint of the piece's own hue at 44% with a
faint inner ring, and was close to invisible on the flag blue and the money green: a dark tint is a
small luminance step, hue contrast does very little at this size, and the inner ring was concentric
with the mark's own circular form so the two merged into rings-inside-rings. `tools/gen_mark_options.py`
renders the treatments that were compared, at a real board cell size rather than at authoring size —
which is the part that had been getting this wrong.

Coins fill ~85% of a cell: the sprite draws at `Match3Game._gemScale` (0.96) and the art is inset a
further 6% a side. It was 0.88 against a 8.5% inset, so the coin took only 73% of its cell and read
as small. The shadow offset and blur are sized to fit inside that tighter padding.

The palette is gold, silver, copper plus
Old Glory Red (#B31942), Old Glory Blue (#0A3161) and money green (#1E8A4C). Flag blue is
very dark against a near-black board, which is what the light outline ring on every piece is for.
The green was first cut as a dark money green (#14663B) and changed: below roughly 30% luminance a
green and the navy stop being two colours at a glance and become "the dark one" twice. Kelly keeps
the money association and holds the distinction. `tools/gen_green_options.py` renders the seven
candidates that were compared, in board context.
Regenerate with `tools/gen_material_pieces.py`. Only `piece_*.png` changed — `coin_*.png` is still
the rendered DGD coin used by the arcade home, the leaderboard medals and Tablet Run, and is
untouched brand art.

**Sound.** Percussion, not metal: `tools/gen_cq_percussion.py` builds everything from four
synthesised primitives (kick, tom, snare, pop). Cascade depth walks up a tom tuning so a long chain
plays as a drum fill rather than one sample twelve times, and the combo cues are short tom runs.
The level and tension music beds carry a kick/snare layer.

**Voice.** Eleven lines, ElevenLabs voice "Hannah", sources kept in `arcade/voice-sources/`.
`Audio.voPraise()` rotates them in two tiers: a cascade of 4-5 draws from "You rock!", "Wow!",
"Great work!", "Way to go!", "Keep it going!"; a cascade of 6 or more draws from "So big!",
"Fire!", "Unstoppable!", "Oh my gosh, that was incredible!". A four-chain and a nine-chain are not
the same event and praising them identically flattens both. The 7-second minimum gap is held across
both tiers rather than per line, since two different affirmations back to back is still two
affirmations back to back, and every cursor starts at a random index so a session doesn't always
open on the same one. Level completion alternates "Level complete, you legend!" and "You win!",
standalone builds only.

Running out of moves plays one of five encouragements — "Almost had it", "One more try", "You've
got this", "Don't give up", "I believe in you" — 600 ms after the lose sting so it lands behind it
rather than over it. This list is rotated in order and its cursor starts at zero, unlike every
other pool: the first failure on a level should get the lightest line, and only someone stuck on
the same level works down to "I believe in you". Shuffling would open a near-miss with the big
reassurance, which reads as pity. Unlike the winner line it is not gated on `DGD_APP_TAB`, since
encouragement after a failure is not the prize-style celebration §4.3 restricts.

Two uploads did not say what their filenames claimed — "nice 3" is "You win!", "You're on fire!" is
just "Fire!" — so `tools/gen_vo.py` keys on the transcribed line, not the filename. Transcribe a
new set before wiring it up.

Finished by `tools/gen_vo.py`, deliberately light: these are performed takes, not synthesis, so
they get a trim to the first syllable, -2.5 dB above 7.5 kHz (any bright vocal fights the snare and
the coin pops for that band), a high-pass at 85 Hz and loudness matched to the effects bed. No
added room — they already have one, and layering a fake reflection over a good take is what makes
it sound cheap. Two earlier passes of OpenAI TTS (`nova`, then `tts-1-hd` `shimmer`) were rejected
for sounding synthetic; the TTS chain needed a fake reflection to sit at all, which is the tell.

**Audio engine.** `lib/audio.dart` holds one persistent `AudioPlayer` per sound file and replays it
with `stop()` then `resume()`. The obvious call, `FlameAudio.play(name)`, must not be used here: it
builds a fresh player per call and appends it to the SoundPool's per-URL player list, and nothing
takes it back down, because low-latency playback fires no completion event and so the
`ReleaseMode.release` that was meant to clean up never runs. Players accumulate, each one adding
work to every later sample load, and effects lag and then stop outright — the bug reported
2026-09-14. Effects and the music bed both use `AudioContextConfigFocus.mixWithOthers`, so a 200 ms
coin pop never grabs audio focus.

**Progression.** `Progress` tracks clears (`m3.clear.<id>`) separately from stars, and `unlocked`
walks the clears. It has to: on an objective level the win condition is the objective and
`targetScore` is only the par the star thresholds are measured against, so finishing a vault level
under par is a legitimate zero-star win. The original code both gated `unlocked` on stars and
guarded its write with `stars > _stars[level]`, which is false for `0 > 0` — so a cleared vault
level saved nothing at all and re-locked itself, and because the walk stops at the first gap, one
such level re-locked everything after it. `load()` also now clears its maps before reading, since
`main()` and the level map both call it. Covered by `test/progress_test.dart`.

**DEV menu.** `lib/dev.dart` gates test shortcuts on `Dev.enabled`, a `const bool.fromEnvironment`
read. In a build without `--dart-define=DGD_DEV=true` every `if (Dev.enabled)` folds to `if (false)`
and the compiler drops the branch, so the shortcuts are absent from a store build rather than
hidden in it. `arcade/devbuild.cmd` builds the test APK: release-optimised, so memory stays
representative, with the menu compiled in.

An amber DEV chip then appears in two places. In a level: end it now at 3, 1 or 0 stars, or lose.
These route through the real `_onEnd`, so the clear is persisted, XP is posted, and the celebration
and fireworks play — a shortcut that only bumped the unlock counter would skip the parts most worth
looking at, and the 0-star option is precisely the case that used to re-lock a level. On the level
map: open any of the six worlds, or reset all progress. `devUnlockThrough` deliberately awards no
stars, for the same reason.

**Build type matters here.** `tools/build-apk.cmd` runs `assembleDebug`, and the debug build is not
representative: measured on a Pixel 9a it reached 1.9 GB PSS with the Java heap climbing past
185 MB, which thrashes swap and freezes the UI for tens of seconds — and gets the app reaped by the
low-memory killer, which is a silent death with no stack trace and reads as a random crash. The
release build over the same ~16 minutes of play holds 310-360 MB with the Java heap oscillating
21-27 MB and no upward trend. Measure memory against `flutter build apk --release` only.

**Fireworks.** Nine shells over the finished board: six at a walking pace, then a muted trio as a
finale. Each shell climbs from below the board trailing sparks, decelerating towards its apex, and
breaks into three layers — an outer ring of fast stars, a slower whiter core, and seven heavy
"willows" that arc over and fall for another 2.4 s. Stars are drawn as a streak from where the
particle was a moment ago to where it is now, not as a dot: a circle at 60 fps reads as stationary
however fast it is actually moving. Position comes from a closed-form solution of linear drag plus
gravity, so the trail can be sampled at any earlier time without keeping history.

Audio is `tools/gen_fireworks.py`, synthesised, three takes of each stage: a lift (hiss plus a thin
whistle gliding up), a break (hard transient, low body delayed behind it by distance, debris tail)
and a crackle (70-odd ticks thinning out over a second). One sound per firework is what makes game
fireworks read as a door slamming; the transient is what gives a break a position and the crackle
is what it actually sounds like a second later. The finale trio plays one prebuilt `fw_finale.wav`
instead of three individual breaks 70 ms apart, which sum to mush.

**`DGD_APP_TAB`.** `--dart-define=DGD_APP_TAB=true` marks a build as the in-App tab. It suppresses
the winner line and the fireworks, which are prize-style celebration the arcade plan bars in-App —
the same rule that turned the coin fountain into a shine wave. Everything else is identical, so the
store/PWA build keeps the full celebration. Three board mechanics beyond plain matching:

- **Ledger seals** — layers under a cell, stripped by clearing a coin on top. Placed as a centred
  contiguous band, never scattered: scattered seals each need a clear on one exact cell, which bot
  testing put at a 7% win rate for 28 of them. A band is reachable by ordinary cascades.
- **Sealed vaults** — unswappable obstacles broken by a clear in an adjacent cell. They carry
  *armour* (1 or 2 hits) because without it difficulty could only scale by count, and the tuner
  pinned four different levels to an identical "21 vaults".
- **Bullion ingots** — unswappable and indestructible; worked down to the bottom row and delivered.

Both obstacles **fall with gravity**. That is load-bearing: a fixed obstacle strands the cells
beneath it in its column, because refill only spawns from the top, so the column drains and never
recovers. Ingots start mid-board rather than at the top — from the top, every ingot level collapsed
under tuning to a single ingot.

Difficulty is machine-tuned. `tools/calibrate_levels.dart` reports a win rate per level for a
greedy bot; `tools/tune_levels.dart` searches objective count and then move budget until each level
lands in an intended band (88–100% for the tutorial, down to 35–68% by world 6) and prints the Dart
to paste back. 55 of 60 currently land inside; the five outliers are noted in the tuner output.

First-run coaching (`lib/match3/ui/coach.dart`) shows one card the first time each mechanic can
appear, keyed in prefs. The board tells the player when it reshuffles itself instead of silently
rearranging. Level completions post to the backend as a `coin_quest` mini-game round, so Coin Quest
feeds the same XP and weekly board as everything else.

Audio was rebuilt in `tools/gen_cq_audio2.py`: every repeatable effect ships as three round-robin
takes, `Audio.play` enforces a per-sound minimum gap and a global six-voices-per-half-second
ceiling, and there are four music beds (menu, map, level, tension) in a shared key that crossfade.

### Scoreboard

One board: **weekly XP**, reset Monday 00:00 UTC. A weekly reset keeps the board winnable for
someone who joins on day 30 and matches the plan's rest-day ethos — nobody banks an unbeatable
lifetime lead. Ranking is computed server-side from `xp_events`; the client never submits a score.

Display names are **assigned, never typed**: `handles.ts` mints e.g. "Burnished Cipher 416" from a
DGD vocabulary (ledger, pillar, benchmark, vault — nothing about earning). No free text means no
profanity queue, no impersonation, no PII on a shared board, and nothing a store reviewer can read
as a promise. Players may re-roll three times a day, which is enough to escape a name they dislike
and few enough that the board stays recognizable week to week.

Guardrails: `status='banned'` accounts are excluded from the board and get 403 on the endpoint;
`xp_only` accounts earn nothing and so never climb; the response carries handles and XP only —
no player ids, tokens or device hints. The screen's footer states that XP is recognition only,
has no monetary value and cannot be exchanged, and no prize attaches to a rank.

The dated ledger was added after XP already existed, so `openDb` reconstructs it once from
`expeditions`, `ledger_plays` and `mini_rounds` (each already carries a timestamp and an amount)
rather than starting the board from a fiction; it logs a warning if the reconstruction and the
running totals disagree.

Identity in the pilot is an anonymous player + bearer token minted on first launch
(`POST /v1/players`) and kept in the client's prefs. Phase 3 attaches the platform's OAuth
`identity_id` + `validated` flag to that same player row; nothing else changes.

API surface: `GET /healthz` · `POST /v1/players` · `GET /v1/me` · `POST /v1/expeditions` ·
`POST /v1/expeditions/:id/tablets/:i` · `…/tablets/:i/answer` · `…/finish` ·
`GET /v1/ledger/today` · `POST /v1/ledger/guess` · `POST /v1/mini/:game` ·
`GET /v1/leaderboard` · `POST /v1/me/handle/reroll`.

Config is environment-driven (`src/config.ts`): `PORT`, `ARCADE_DB`, `ARCADE_BANK`,
`ARCADE_SECRET` (**must** be set in production — the token HMAC key), `ARCADE_CORS`,
`TABLETS_PER_EXPEDITION` (3 Explorer / 5 Validator), `REWARDED_EXPEDITIONS_PER_DAY`,
`RUN_MIN_FINISH_MS`, `MINI_REWARDED_ROUNDS_PER_DAY`, `RATE_PER_MINUTE`.

Client wiring: `lib/arcade/api.dart` (base URL from `--dart-define=ARCADE_API`, else same-origin
`/api` on web and `localhost:8787` on native), `lib/arcade/progress.dart` (snapshot cache with an
OFFLINE pill on the home screen). Phone testing against the dev server: `adb reverse tcp:8787
tcp:8787`; the Android manifest permits cleartext to localhost only.

Compliance choices already made in code: the win celebration in Coin Quest is a shine wave over
the coins on the board (no coin shower, no jackpot visuals — plan §4.3); vocabulary is
XP/badges/expedition/tablet, never earn/cash; the footer on every home screen reads
"Educational only. XP and badges have no monetary value."

## Building

Toolchain on the build PC: Flutter 3.47 at `C:\src\flutter`, Android Studio + SDK 35/36, Python 3
with Pillow (asset pipelines). Working copy at `C:\src\puzzle-app`; `arcade/app/` in this repo is a
mirror without `build/`, `.dart_tool/` and the full-resolution image backups.

```
tools\check.cmd       pub get + analyze + test           → C:\src\check.log
tools\build-apk.cmd   debug APK for the Pixel            → C:\src\build.log
tools\build-web.cmd   release web bundle (wasm)          → C:\src\web.log, output build\web\
tools\serve_web.py    local server with the right headers (see Hosting)
```

`build-web.cmd` runs `flutter build web --release --wasm --no-web-resources-cdn --base-href /arcade/`.
Change `--base-href` to wherever the bundle will be mounted (must start and end with `/`).

Asset pipelines (all regenerate from source, nothing is hand-edited):

- `tools/gen_coin_variants.py` — six metal finishes from `DGD_coin_gold.png` (HSV remap).
- `tools/gen_dgd_assets.py`, `gen_coinquest_assets.py` — cards, nodes, backgrounds, wordmark.
- `tools/gen_cq_sfx.py` — every sound is synthesized (numpy); `TRIM_DB` and `SFX_PITCH_SEMI` at the top.
- `tools/shrink_assets.py` — quantizes runtime PNGs to a dithered 256-colour palette (6.1 MB → 1.5 MB,
  no visible change at render size). Originals are kept in `assets/_images_full/` on the build PC.
- `tools/gen_web_icons.py` — PWA icons + maskable variants from `assets/app_icon.png`.

## What the web bundle weighs

Measured 2026-09-14 in Chromium, cold cache, gzip on:

| Fetched on first load | Size |
|---|---|
| Renderer (`canvaskit/skwasm.wasm`, self-hosted) | 1.5 MB |
| App code (`main.dart.wasm` + `.mjs`) | 0.8 MB |
| Fonts (Instrument Sans, Geist Mono ×2, PT Serif Bold Italic) | 0.42 MB |
| Home-screen images | 0.35 MB |
| Audio (7 core sounds + ambient loop; the other 19 load on first play) | ~0.6 MB |
| **Total** | **≈ 3.7 MB** |

Splash (branded, in `web/index.html`) paints at ~0.4 s; app first frame ~1.4 s on localhost.
Coin Quest runs at the display refresh rate with skwasm multi-threaded. The bundle folder is
~38 MB on disk because Flutter ships every renderer variant; a browser fetches exactly one.

For comparison the plan assumed a Phaser bundle (~0.3 MB gz before assets). The ~1.5 MB renderer
is the structural cost of Flutter on web; everything else is within ~0.5 MB of what the same art
and fonts would weigh under Phaser. Trade: one codebase for PWA + App tab + native stores, vs. the
"1 game dev (Phaser/Unity)" hire in the plan becoming a Flutter hire.

## Hosting requirements

1. **MIME types.** `.mjs` and `.js` → `text/javascript`; `.wasm` → `application/wasm`. Python's
   default `http.server` gets `.mjs` wrong and the app silently fails to start.
2. **Cross-origin isolation** so skwasm can use threads (it degrades to single-threaded without it,
   with a console warning):
   `Cross-Origin-Opener-Policy: same-origin` and `Cross-Origin-Embedder-Policy: require-corp`.
   Every sub-resource must then be same-origin or CORP-tagged — the build is self-contained, so
   this holds unless the host injects third-party scripts.
3. **Compression.** gzip or brotli on `.wasm`, `.js`, `.mjs`, `.json`, fonts. Cuts the wire size
   roughly 2.5×.
4. **Caching.** `index.html` and `flutter_bootstrap.js` short-lived; everything else is
   content-hashed by Flutter's service worker and can be cached for a year.
5. **Base path.** Rebuild with the matching `--base-href`; the bundle cannot be relocated after
   the fact.
6. **WebView embed (DGD App).** Same bundle. `--no-web-resources-cdn` is already on, so nothing is
   fetched from gstatic.com — a strict WebView allowlist only needs the Arcade host. The bridge
   calls the Integration Brief names (`getSessionToken`, `getAttestation`, `openAccountScreen`)
   are not wired yet; today the hand-off is a plain `https://digitalgold.co/` link on the results
   sheets.

`tools/serve_web.py <dir> <port>` does 1–3 for local testing.

## Known gaps vs. the plan

- Backend covers §5.1 (server-authoritative gameplay) and the §4.2 limits, but not §5.2
  (device attestation — Play Integrity / App Attest / fingerprint SDK), §5.3 (OAuth account
  linking, `validated` flag), §5.4 (graph/behavioral signals — the raw material is stored per
  expedition, nothing analyses it yet), §6 (the `apply_credit` batch) or the review queue.
- SQLite, single process, no auth on an admin surface (there is none yet). Fine for the 500-player
  pilot; move to Postgres + a real rate limiter at the edge before Phase 3.
- Question bank is at 170 items against the 300-item Phase 1 target; no paraphrase variants
  yet; lint is a manual rule set, not CI.
- Daily Ledger's 90-day calendar is a seeded generator over 20 words / 15 numbers, not a curated list.
- Coin Quest's older sibling games (Merge/Words/Blocks/Rope) carry no DGD knowledge; they exist as
  retention filler and could be cut for the App tab review.
- iOS not yet built or tested (no Mac in the loop); Android tested on a Pixel 9a.
