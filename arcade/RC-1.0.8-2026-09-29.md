# Android 1.0.8 — release candidate

**2026-09-29.** dgd-native `0520865` (tag `android-1.0.8-rc1`). versionCode 8,
targetSdk 36, minSdk 26. Supersedes the 1.0.7 candidate: 1.0.8 is 1.0.7 plus
the arcade change below, so only one of them needs to go to Play.

| Artefact | Bytes | SHA-256 | For |
|---|---|---|---|
| `DigitalGold-1.0.8-unsigned.aab` | 57,189,687 | `43E1F5FD36ABEAA05E492FB19B2F4BDF06E6816829A5EDE8D09AF10893D14B67` | **Play.** Unsigned: DGD signs it with the upload key (steps in `RC-1.0.7-2026-09-29.md`). |
| `DigitalGold-1.0.8-review.apk` | 64,127,072 | `7C2567C26A23F84C628A0CD891EF24DA76A41C7228488B922E2D02CDD8B6C6A8` | Installing and looking. Debug-signed, says `1.0.8-review`; Play refuses it. |

## What changed since 1.0.7

The embedded arcade (Coin Quest, from puzzle-app v1 `99a5c36`), at the owner's
request:

- **Music only inside the game.** The arcade's home is silent. Coin Quest
  plays **Quest Tune**, the owner's own track, from the level map through
  every level — one continuous tune, not restarted between the map and a
  level — and it fades out on the way back to the arcade home.
- The four old music beds are gone from the app. Quest Tune is encoded mono
  at 96 kbps and levelled to about -20 LUFS, where the old beds sat; the
  arcade module is 3.2 MB larger for it.
- The embed build is unchanged in kind: `DGD_EMBED=demo` (no backend, zero
  requests) and `DGD_APP_TAB=true` (no fireworks or winner voice line).

The ticker app itself is unchanged, including the 1.0.7 web-arcade link.

## Verification

| Check | Result |
|---|---|
| puzzle-app v1 | analyzer clean; both required test runs pass (58 + 52, with the network suite live); new `music_scope_test` |
| Unit tests (app) | **95 / 95** |
| Lint (release) | 0 errors, 43 warnings (unchanged from 1.0.7) |
| Manifest vs 1.0.7 | identical except the version |
| AAB | unsigned; contains `music_quest.mp3` and no other music; the 1.0.7 dex checks (link, wording, no referral strings) all still pass |
| API 36 emulator, R8 build, read from the audio mixer | arcade home: **no track playing**. Level map: one 44.1 kHz track from the app (Quest Tune). Into level 1 and back to the map: **the same track, still playing** (not restarted). Back to the arcade home: **stopped**. Backgrounded and brought back: still silent. Screens in `rc-1.0.8-shots/` |

The Pixel was not used this pass.

## Play Console text

**What's new (en-US):**

> New music for Coin Quest. The arcade menu is now quiet; music plays while
> you play. The Arcade button opens a menu: play in the app, or open DGD
> Arcade for Web in your browser.

The reviewer note and the policy reading in `RC-1.0.7-2026-09-29.md` apply
unchanged.
