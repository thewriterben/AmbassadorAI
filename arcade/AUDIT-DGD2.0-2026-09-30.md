# DGD App 2.0 (arcade v2 demo embed) — source review and fix pass, 2026-09-30

> **Scope and authorisation.** The owner's call of 2026-09-30: DGD App 2.0
> embeds arcade v2 as a demo (no backend, zero requests), Android first, for
> Play internal testing. The embed is built with `DGD_APP_TAB=true` and
> `DGD_DEMO=true`. Source: puzzle-app v2, branch `v2/ten-games`, reviewed at
> `5f04e8b`, fixed at `4e7c607`. Host app: dgd-native branch `dgd-2.0`,
> version 2.0.0, version code 200.
>
> **What this is, and what it is not yet.** A source-level adversarial
> review, a fix pass, and the runner. It is **not** yet the artefact audit.
> No clean-room AAR exists at the fixed commit: Docker Desktop stopped
> responding mid-build, and the release bundle has not been built. Those
> come next and get their own section, or their own file.
>
> **One exception to the policy, stated.** The adversarial reviewer was a
> separate agent with no hand in writing the code and no edit rights. It was
> started from the session that wrote the code, though, not from a separate
> clean room. It read source at a pinned commit and ran nothing.

## Suites, with defines and counts (at `4e7c607`)

| Run | Defines | Result |
|---|---|---|
| Loopback | `ARCADE_API=http://127.0.0.1:18787` | 188 pass, 5 skipped |
| Demo | `ARCADE_API=…:18787`, `DGD_DEMO=true` | 180 pass, 13 skipped (the shop's own tests and the non-demo network cases) |
| Plain baseline | `DGD_ALLOW_PARTIAL=true` (the gate's documented waiver) | 179 pass, 14 skipped |
| Analyzer | | clean |

Runner, `arcade/tools/redteam.sh --ref aace895 --mirror v2`: 10 of 11
checks pass. They cover the server suites (39/39), hosts, secrets,
analyze, loopback, the demo zero-request group and "network cases ran".
The failure was the plain run, a conflict between tools: v1's `gate_test`
(`afb03ab`) fails any run without the loopback define, on purpose, and the
runner's plain baseline predated it. Fixed in `3e543ac`: the baseline takes
the gate's waiver, and the demo run now covers the whole suite. **The
author of the code made that tooling change, so it wants a second reader.**

**Rerun at `e896fa2` (the fix pass, mirrored): PASS, 11 of 11.** The
server's 39 tests, plain baseline 179, loopback 188, demo 180, 9 more cases
with the define, analyzer, and the host and secret scans. Report:
`redteam-runs/20260930T210729Z-e896fa2/report.md`.

## Findings

| ID | Sev | State | What |
|---|---|---|---|
| E1 | MEDIUM | **OPEN**, deferred to before production (owner, 2026-09-30) | Pickups are the DGD-branded coin renders, worth 10/3/1 points, and the results count "coins taken"; inside a finance app that can read as the token having in-game value. Part-fixed: the home disclaimer now covers "XP, points, coins and badges". Remaining: unbranded coin art, and a look at the "coins taken" wording |
| E2 | LOW | fixed `4e7c607` | When Pigs Fly's dev menu wasn't guarded at the call site (the 1.0.5 F1 pattern), so its closures were compiled into a store build. Now `Dev.enabled ? … : null`, and the autopilot, start-era and hitbox hooks check `Dev.enabled`. **Verified in a demo `libapp.so`:** none of the menu's strings are present |
| E3 | LOW | fixed `4e7c607` | "A soft landing earns the third star" used banned copy; now "gets". The 1979 fact said the Fed raised "its policy rate" above 19%, but it targeted reserves from 1979; it now says the funds rate passed 19% by 1981, as its source line does |
| E4 | LOW | fixed `4e7c607` | A build with no backend applied a cached `ar.snapshot` that an earlier backend build could leave; it no longer reads it. Its "Delete my play record" said "The server refused the request"; it now says there is no server record. The control stays, because the stores' deletion answer rests on it (`widget_test`) |
| E5 | INFO | fixed `4e7c607` | The transport's own gate ignored `DGD_DEMO`. It now refuses in a demo build even with `ARCADE_API` set, pinned by a demo-group test that counts zero arrivals |
| E6 | INFO | open, not reachable in the demo | The grow-up flash, sparkles and `stageUp` aren't gated on `inAppTab`. It needs a backend, so it matters when a backend build ships inside the app |
| E7 | INFO | accepted as not prize-style (reviewer's judgement) | A soft landing plays `win()`, and a strike spills up to four coins with `coinsPour`. Coin Quest already plays both in the tab. The spoken winner line is gated. Worth rereading together with E1 |
| E8 | INFO | as v1 | `url_launcher` has no Dart caller but still registers its activity in the host |

**Nothing HIGH.** The review found the following properties hold:
- **Zero requests in this build.** The transport throws before any get,
  post or delete, and every caller also checks `noBackend`.
- **Build flags.** Only four are read: `DGD_DEV`, `DGD_DEMO`, `DGD_APP_TAB`
  and `ARCADE_API`.
- **Hosts and secrets.** The only host is the debug-only localhost. Nothing
  secret-shaped appears in `lib/` or `assets/`.
- **Dependencies.** `pubspec.lock` is identical to v1's.
- **Device storage.** The demo writes only local game state.

## Still to do before the upload

1. The clean-room AAR at the final commit (`DGD_ARCADE=v2
   build_aar_cleanroom.sh <commit> --publish`), once Docker is back.
2. ~~The runner at the final commit.~~ Done: PASS at `e896fa2`.
3. DGD App 2.0: the unsigned bundle and a review APK, with the clean-room
   AAR, so the provenance gate passes without `-PdgdAllowHostArcade`. Then a
   check on the Pixel.
4. The artefact checks from the v1.0.8 audit: hashes, a size note, and
   `strings` checks on the shipped `libapp.so`.


---

## Second pass: the design return (redesign), 2026-09-30

**Scope.** The design return of 2026-09-30 applied to both halves:
- arcade v2 `4e7c607..7fc97da`: the redesign (`50a8009`) and the
  `dgd/arcade` entry channel (`7fc97da`);
- dgd-native `18d4a67..a0fba92` on `dgd-2.0`: the bottom bar, Market, the
  Arcade and Account tabs, and the restyled Join, Log in and Invite.

The reviewer was a separate agent with no hand in the code (the same
exception to the policy as above). The fix pass is dgd-native `f04b884`.

| ID | Sev | State | What |
|---|---|---|---|
| R1 | HIGH | fixed `f04b884` | The committed AAR was still v1 1.0.8, so a build of `a0fba92` would open the old arcade from every card. Now `arcade-repo` holds the **clean-room build of v2 `7fc97da`**, with A and B byte-identical (6/6 AARs) and PROVENANCE committed. A 2.x build refuses a PROVENANCE that is not v2 |
| R2 | MEDIUM | fixed | The full-size price could lose its last digits, with no ellipsis, on a narrow phone or at large text. It now sizes itself to the card |
| R3 | MEDIUM | fixed | The status detail and the market cap wrap instead of being cut off |
| R4 | MEDIUM | fixed | A double tap started two arcade activities on one engine, one of them blank. Opening is now debounced (checked on the Pixel) |
| R5 | MEDIUM | fixed | The Account card showed preview headers and step lines outside the preview. It now carries only what home had: the coin, the name and the locked button |
| R6 | MEDIUM | **fixed 2026-09-30, docs** | Review and store notes describe the old layout. *Fix: `RC-2.0.0-2026-09-30.md` carries the 2.0 What's new, reviewer notes and screenshot set (`store/dgd-app-2.0/`); the iOS link guide, the B1-B3 draft notes, `INTEGRATION.md` and dgd-native's README and handover facts are updated; the 1.0.7 and 1.0.8 RC records are left as history.* Originally: They must be rewritten before any reviewed track (internal testing has no review): `RC-1.0.7-2026-09-29.md:17`, `RC-1.0.8-2026-09-29.md:121-123`, `integration/IOS-WEB-ARCADE-LINK.md` rule 4, the draft notes in `B1-B3-CATEGORY-AND-PURCHASE.md`, `INTEGRATION.md:172`, dgd-native `HANDOVER_FACTS.md:40` and `android/README.md:88` |
| R7 | LOW | fixed | The CTA's accessibility hint is back on the button |
| R8 | LOW | fixed | The Stats pill, step pills, address actions and the help button are 44 dp |
| R9 | LOW | **fixed in rc2** (arcade `3c4e42d`: the open is a zero-duration route, so the requested screen is the first frame; checked by screen recording, `RC-2.0.0-2026-09-30.md`) | Back on a tab returns Home, and Back in the preview steps back. **Open:** a warm open briefly shows the last arcade screen and then a page transition. It is an arcade change, left for the next clean-room build |
| R10 | LOW | fixed | Refresh is throttled to one request per ten seconds |
| R11 | INFO | owner | The Facebook and LinkedIn logos are the return's white versions (Meta prefers Facebook Blue), and X uses Hugeicons' mark. Both are the design's choice; confirm |
| R12 | INFO | open | The Settings record text is the designer's wording; check it against the Data safety answers. "Star N recorded" means recorded on the phone (now "saved", rc2). `registerDesignLicences` says the licences appear on a licence page the arcade does not show; the notices still ship as assets |

**What holds**, per the reviewer:
- The channel can only be driven by the app's own code: the arcade
  activity is not exported, and no intent data is parsed.
- No new request, URL, WebView or define, and the DEV guards are intact.
- `LockedCopy.kt` is unchanged.
- The web-arcade link keeps its rules: neutral copy, a bare URL, the
  external browser, and no result screen.
- No referral surface.
- Every asset is byte-identical to the return, and the licences ship.
- No prize-style celebration.
- All 68 new strings pass `compliance_lint --strict`.

**Runner on the redesigned arcade** (`03e121d`, v2 `7fc97da` mirrored): PASS, 11 of 11:
- the server's 39 tests;
- the app tests: plain 183, loopback 192, demo 184;
- 9 more network cases with the define;
- the analyzer, and the host and secret scans.

Report: `redteam-runs/20260930T223223Z-03e121d/report.md`.

## The artefacts

Built on this Windows host against the clean-room arcade; the provenance gate
passed with no override. The files are in
`C:\src\dgd-native\android\dist-2.0.0\`:

| File | sha256 | Bytes |
|---|---|---|
| `DigitalGold-2.0.0-unsigned.aab` (for Play, signed by DGD) | `fe22caa16cdc8536e01ee9a0af1af964a6e32188fa9672303a6837827d009594` | 64,752,897 |
| `DigitalGold-2.0.0-review.apk` (debug-signed, `2.0.0-review`, code 200) | `d253c3719f604a4d752aa2cf1c40b73f04e520526748b5bb5d6dc9caa424b8e4` | 72,275,537 |

- **The arcade inside:** clean-room v2 `7fc97da`, with
  `DGD_APP_TAB=true DGD_DEMO=true` (`ARCADE-PROVENANCE.md` beside the
  files).
- **Native:** 95 unit tests pass.
- **Instrumented tests:** 4 of 4 pass, run on the `dgd_api36` emulator
  only (`ANDROID_SERIAL`), never on the test phone. This includes the
  first-run join flow.
- **The native half, reproduced** (`redteam-runs/20260930T2304Z-dgd2.0-native-f04b884/`,
  `integration/cleanroom/build_native_cleanroom.sh`):
  - dgd-native `f04b884` rebuilt in `dgd-cleanroom:1` with no mounts and
    the network cut;
  - the offline `bundleRelease` passes the arcade gate, the 95 unit tests
    pass, and lint passes;
  - against the host bundle, **782 of 788 entries are byte-identical**. The
    six that differ are the same R8 and baseline-profile metadata as in the
    v1.0.8 pass. No dex, library, resource or asset differs.
- **Still to do before a reviewed track:** nothing from this review. R6 is fixed in the docs (`RC-2.0.0-2026-09-30.md`).
