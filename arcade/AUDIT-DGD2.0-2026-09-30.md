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
