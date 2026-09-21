# Session state — read this when picking the work up somewhere new

**Last updated 2026-09-21.** Written so that a session on a different machine,
or after a long gap, can carry on without re-deriving anything.

The other documents say what to do. This one says **where things stand and
what must not be done**, which is the part that otherwise lives only in a
conversation.

---

## 1. Where the launch stands

Three real blockers. Only one is engineering.

| | Blocker | Owner |
|---|---|---|
| **S1** | release keystore, App Bundle | **DGD** — nothing ships without it |
| **B1** | primary category + who signs the 3.1.5(v) defence | **DGD** — answer early; it can change the invite feature itself |
| **B2a** | the synthetic stats chart on iOS | Benji, on the Mac |

Everything else is gated on one of those, or on an artefact DGD has not
produced (App Store ID). Full table in
`STORE-READINESS-2026-09-20.md` §6b.

**B2b — the iOS arcade — is deferred** until this version is reviewed and the
backend is being wired in.

---

## 2. What changed on 20–21 September

Android is in good shape; the work below is all verified on device.

| Commit | Tree | What |
|---|---|---|
| `bab02c8` | dgd-native | **B4** — the signup preview could not be completed at all on a fresh install. Deterministic first-run blocker, not cosmetic. v1.0.4 |
| `2dc1635` | dgd-native | Instrumented tests, first minified R8 release build, Gradle 8.14.4 |
| `d6ad633` | dgd-native | iOS stats panel rewritten — **uncompiled**, this is B2a |
| `783c6ba` | dgd-native | **S2** — large-screen width caps at targetSdk 36 |
| `284710d` | puzzle-app | the arcade half of the same S2 change |

Also closed: `DGD_APP_TAB` suppression, proved by an A/B build diff rather
than by eye — `voWinner` and `fireworkShow` vanish from the flagged snapshot
while control strings are untouched.

---

## 3. Standing constraints — these survive any session change

Not preferences. Several were learned the hard way.

**The phone**

- **Never** run `monkey`, a fuzzer, or any unattended input storm on Benji's
  Pixel. Single `adb shell input tap` for a specific verified step is fine.
- Never type the phone's PIN or passcode.

**Credentials**

- **Do not create or hold the release keystore or its password.** It is a DGD
  credential and belongs in DGD's password manager. See `RELEASE.md`.
- The admin Swagger credential is DGD's to rotate. Nothing here touches it.
- `ARCADE_SECRET` must be set to a real value before the server is exposed.
- Red-team policy forbids traffic to `digitalgold.co`.

**Compliance vocabulary** — this is not style, it is the 3.1.5(v) defence

- Say: XP, badges, expedition, tablet.
- **Never**: "earn", "cash", "dollars", or anything implying monetary value or
  an investment return.
- Arcade plan §4.3 bars prize-style celebration inside the DGD app: no coin
  showers, no jackpot, no casino visuals.

**Build rules**

- `DGD_APP_TAB=true` is **mandatory** for any embed build. It is what
  suppresses the fireworks and the spoken winner line. `build_aar.cmd` carries
  it so it cannot be forgotten; iOS has no equivalent wrapper yet.
- `build_aar.cmd` also refuses to build without `ARCADE_API` or
  `DGD_EMBED=demo`. Currently **demo** — the backend is not hosted.
- Never edit `C:\src\dgd_arcade_module\lib/` or `assets/`. It is generated.
  Edit v1 (`puzzle-app`) and re-run `sync_module.py`.
- Building the AAR without mirroring it into `android/arcade-repo` leaves the
  app silently on the previous arcade. That cost a day on 2026-09-20; the
  publish step is now inside the script.
- Flutter **3.47.2** / Dart 3.13.2, and JDK **21** for AAR builds (Flutter
  ignores `JAVA_HOME` and prefers Android Studio's bundled JDK 25, on which
  the Dokka tasks die with errors that never mention Java).
- iOS: `.xcframework` declared in `project.yml`, **not CocoaPods** — the
  pbxproj is XcodeGen output and Pods edits are discarded on regeneration.

---

## 4. Where things live

| | Path | Remote? |
|---|---|---|
| DGD's app (Android + Apple) | `C:\src\dgd-native` | **none — local only** |
| The arcade, v1 | `C:\src\puzzle-app` | **none — local only** |
| Arcade v2 worktree | `C:\src\puzzle-app-v2` | branch `v2/ten-games` |
| Generated Flutter module | `C:\src\dgd_arcade_module` | generated, never edited |
| Docs and this file | `AmbassadorAI`, branch `arcade-redteam` | GitHub |
| Transfer bundles | `F:\Documents\dgdappsource\mac-handoff\` | — |

Repos stay **local and private** until DGD's company GitHub exists. That is a
decision, not an oversight. The bundles are currently the only second copy of
either repository.

---

## 5. Habits worth keeping

Three mistakes from this stretch, each of which produced a rule:

- **Assert which artefact you are measuring.** A "release build ran at 124 ms"
  claim turned out to be the debug build. Check `ls -l base.apk` rather than
  trusting which build you think is installed.
- **Check that a comparison is comparing two things.** A Compose metrics diff
  was invalid because the new run wrote empty files and the old reports were
  being compared against themselves. Timestamps caught it.
- **Read the stack before guessing the dependency.** An instrumented-test
  failure was blamed on `androidx.test:runner`; it was espresso, and only
  3.7.0 fixes it.

When something is corrected, correct it in the document by name rather than
quietly overwriting — `STORE-READINESS-2026-09-20.md` has worked examples.

---

## 6. What to read, in order

1. This file.
2. `MAC-CONTINUE.md` — if you are on the Mac.
3. `integration/IOS-B2-RUNBOOK.md` — the iOS changes.
4. `STORE-READINESS-2026-09-20.md` — the full picture, §6b for the launch view.
