# Android 1.0.8 — release candidate

## rc2 (2026-09-30) — supersedes rc1

dgd-native `a22c194` (tag `android-1.0.8-rc2`). Same app and same arcade
program as rc1, with versionCode 8 and versionName 1.0.8 kept. The
difference is where the arcade was built. rc1's arcade AAR was built on
Windows, and the clean room cannot reproduce that byte for byte, so the
red-team policy's ship gate refused it (`AUDIT-v1.0.8-2026-09-29.md`, P1).
rc2's arcade is built in the pinned Linux clean-room container, from
puzzle-app v1 tag `embed-android-1.0.8` (`99a5c36`).

| Artefact | Bytes | SHA-256 | For |
|---|---|---|---|
| `dist-1.0.8-rc2/DigitalGold-1.0.8-unsigned.aab` | 57,175,121 | `2F768698B79944EBB777FAD8D0B8EC8D83446709293A7FBF911901102297ED95` | **Play.** Unsigned; DGD signs it with the upload key. |
| `dist-1.0.8-rc2/DigitalGold-1.0.8-review.apk` | 64,127,176 | `46573FFE09BB7E302B557E6C772397807CAC92523EAE582B132A4984FDA99378` | Installing and looking. Debug-signed, `1.0.8-review`. |

rc1 was never uploaded to Play (confirmed 2026-09-30), so versionCode 8
stands for rc2.

### What differs from rc1

The rc1 bundle has 642 entries; 631 are unchanged in rc2, including
`classes.dex`, the manifest and every asset except one. The 11 that differ:

- **`libapp.so`, in all three ABIs.** This is the arcade, compiled by
  Linux `gen_snapshot` instead of Windows. The program is the same (see
  the audit's token comparison), and this file now equals the independent
  clean-room build byte for byte.
- **`libdartjni.so`, in all three ABIs.** The jni plugin's small C
  library, now compiled by the container's NDK. It has the same symbols
  and strings as rc1's, and is about 150 bytes smaller.
- **`NOTICES`**, the licence text the app displays. It gained the `lints`
  and `flutter_lints` licences, because the module now resolves exactly
  v1's lockfile.
- **Build metadata:** `dependencies.pb`, `r8.json` and the two baseline
  profile files.

### Verification

| Check | Result |
|---|---|
| Arcade AAR, container | online build A and offline build B are identical in all six AARs; `PROVENANCE.md` in `arcade-repo` |
| Arcade AAR vs the audit's independent clean build | 170 / 171 entries identical, including `libapp.so` in every ABI; `NOTICES` as above |
| Ship gate (`verifyArcadeProvenance`) | passed in the bundle, review and lint builds (36 files match); refuses a corrupted hash and a host build (tested) |
| Built from | committed tree `a22c194`, nothing modified |
| Unit tests (app) | **95 / 95** |
| Lint (release) | 0 errors, 43 warnings (unchanged) |
| Review APK vs the bundle | dex identical, 180 / 180 libraries and assets identical |

**Not yet done:** a fresh clean-room reproduction of the rc2 bundle, and an
emulator smoke test of the new binary. The audit's dynamic results carry
over only as far as the program is the same, which the token comparison
supports but does not prove.

---

## rc1 (2026-09-29)

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
