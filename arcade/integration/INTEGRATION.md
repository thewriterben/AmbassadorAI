# Arcade v1 embedded in the native DGD app — Android

**2026-09-20.** The merged Android app builds, installs, and is 77.4 MB.
Everything below was measured, not estimated.

Now carrying **arcade v1.0.1** — see `COIN-AND-ICON.md` for the shared coin,
the spin/flip split and the new launcher icon, and the two fixes below.

## What the shape is

```
arcade v1 (Flutter app, frozen, untouched)
        │  sync_module.py   generates
        ▼
dgd_arcade_module (Flutter module, generated — never edited by hand)
        │  flutter build aar
        ▼
android/arcade-repo (local Maven repo, 13.8 MB, checked in)
        │  implementation("co.digitalgold.arcade.module:flutter_release:1.0")
        ▼
DigitalGoldTicker (their native app)
```

**Rebuild with `arcade/integration/build_aar.cmd`.** That one script
regenerates the module from v1, selects JDK 21, builds the AAR, publishes it
into `android/arcade-repo`, and is also what passes `DGD_APP_TAB=true`.

### That script was broken until 2026-09-20, and quietly

It was written to match this document and did two fewer things than the
document claimed. On the first clean run after v1 changed it failed, and the
failure named neither missing step:

1. **No JDK selection.** Flutter ignores `JAVA_HOME` and prefers Android
   Studio's bundled JBR, which here is JDK 25. On 25 the plugins' Dokka
   javadoc tasks die, and the build ends in six identical
   `JavaDocGenerationTask` errors that say nothing about Java versions. The
   working incantation existed in a scratch script and had never been folded
   in. It now is, and is restored afterwards so the override cannot leak into
   other Flutter builds on the machine.
2. **No publish step.** The AAR was built into the module's own output
   directory and never copied to `android/arcade-repo`, which is what the app
   actually resolves against. Building without mirroring leaves the app
   silently on the *previous* arcade — a failure with no error at all. That
   copy is now step 5 of the script rather than a thing to remember.

Worth stating plainly because it is the same shape as the other defects
recorded here: a documented claim that no one had executed end to end.

## Why a generated module rather than a second copy

`flutter build aar` only works on a Flutter *module*, and **a project cannot
be both a module and an app** — I tested it: adding a `module:` descriptor to
v1's pubspec breaks `flutter build apk` outright. v1 has to stay a standalone
app because it is also a store candidate in its own right, so the module is
generated from v1 on every build. There is one place the arcade is edited, and
it is v1.

`sync_module.py` refuses to run if v1 is not on `main`, or if Passage is
present — the embed cannot silently become v2.

## Why an AAR rather than a source subproject

Only one machine here has the Flutter SDK. An AAR means **the native app
builds on any machine and in CI with no Flutter installed**. Same reasoning as
the `.xcframework` recommendation for iOS.

## What the integration cost their project

Six changes. Five were forced; the sixth is the entry point.

| Change | From → to | Why |
|---|---|---|
| AGP | 8.7.3 → **8.9.1** | Flutter's androidx deps declare a minimum of 8.9.1. Fails at resolution otherwise |
| Kotlin | 2.0.21 → **2.4.0** | The engine AAR brings kotlin-stdlib 2.4.0; older compilers cannot read its metadata |
| `kotlinOptions` | → `compilerOptions` | Kotlin 2.4 removed the old DSL. An error, not a warning |
| compileSdk | 35 → **36** | Engine and plugins are compiled against 36 |
| `ndkVersion` | unset → **28.2.13676358** | Needed so symbol stripping can run. See below |
| Entry point | — | `Arcade` object, a manifest entry, a theme, one button |

**Host version is `1.0.2 (2)`** as of 2026-09-20 — `versionCode` must rise
on every upload, and until this bump the merged app was indistinguishable
from the pre-merge ticker on a device (`AUDIT-RC-2026-09-20.md`, RC3).

**`targetSdk` is 36 as of 2026-09-20** (it had stayed at 35 when compileSdk
moved, deliberately); Play requires it, and the bump was retested on an
Android 16 emulator — `STORE-READINESS-2026-09-20.md`, S2. **`minSdk` stays
26**: no device dropped.

### The Kotlin bump is the one to take seriously

2.0.21 → 2.4.0 is four minor versions. It is forced, not chosen, and it took
two attempts to even see why: at 2.0.21 Kotlin does not report the metadata
mismatch, it **crashes** with `Internal compiler error ... source must not be
null` from `FirIncompatibleClassExpressionChecker` — the checker whose job is
to report exactly this. Only at 2.2.20 does it say what is wrong.

Their app compiled and its unit tests still pass at 2.4.0.

**The regression pass has since been done** — `KOTLIN-2.4-REGRESSION.md`. The
same source was built at both compiler versions in a stripped copy (the
integrated app cannot be built at 2.0.21, since the arcade AAR brings the
2.4.0 stdlib) and the outputs compared. Verdict: a non-event for this
codebase. No app-level change in the compiled output, one stdlib package
added, two benign new warnings. Two things came out of it that are worth
someone's attention — Gradle 8.11.1 must reach 8.14.4 before Kotlin 2.5, and
the app has **no instrumented tests at all**, so the Compose surface the bump
governs is covered only by eye.

## The silent failure worth knowing about

The first merged APK was **505 MB** and so malformed that `adb` rejected it
with `INSTALL_PARSE_FAILED_NOT_APK`. Gradle reported **BUILD SUCCESSFUL**.

Cause: AGP strips debug symbols from native libraries using the NDK. With no
`ndkVersion` pinned it could not find one, logged

> Unable to strip the following libraries, packaging them as they are

as an ordinary message among hundreds, and carried on — packaging the
unstripped Flutter engine at **157 MB per ABI**.

Pinning `ndkVersion` took the APK from 505 MB to **76.9 MB**.

I got the diagnosis wrong twice first. I assumed a debug engine was being
pulled and added `matchingFallbacks`, which changed nothing; the dependency
tree then showed plainly that every Flutter artefact resolved to `_release`.
The fix only appeared once I read the build log for the word "strip" instead
of theorising. `matchingFallbacks` is still in place and still correct — the
arcade genuinely has no debug variant — but it was not the cause.

## Size

| | |
|---|---|
| Their ticker alone | 18.8 MB |
| Merged debug APK, 4 ABIs | **77.4 MB** |
| Estimated Play download, per device | ~30 MB |

The 76.9 → 77.4 MB change is the new launcher icon's density mipmaps, +0.5 MB
of `res/`, confirmed by diffing the two APKs entry by entry.

**Measure a clean build, not an incremental one.** An incremental
`assembleDebug` produced a 92 MB APK that installed and ran perfectly: AGP
leaves the bytes of replaced entries as dead space in the zip rather than
rewriting it. Summing the entries gave 80.8 MB against a 92 MB file, and the
11 MB gap sat in holes between entries. `gradlew clean assembleDebug` returns
it to 77.4 MB. Alarming-looking and completely benign — but it wastes the
same half hour every time unless it is written down.

A Play App Bundle splits by ABI, so a user downloads one architecture, not
four. That ~30 MB figure is the one to quote to anyone who asks — but it is an
estimate from the ABI split, not a measurement. Build the bundle to confirm.

## Compliance

The AAR is built with **`DGD_APP_TAB=true`**, which suppresses the arcade's
fireworks and spoken winner line — arcade plan §4.3 bars prize-style
celebration inside the DGD app. `build_aar.cmd` is the only place that flag is
set, so it cannot be forgotten by building the AAR some other way.

**This does not touch the larger question.** Their app is Finance-category and
already carries a Guideline 3.1.5(v) defence; putting a game catalogue that
awards XP inside it is the thing `NATIVE-SOURCE-REVIEW.md` flags as needing a
decision before submission. The embedding working is not the same as the
embedding being approved.

## Verified on the Pixel

| Check | Result |
|---|---|
| Ticker still works, Arcade entry present | ✅ live price, entry top-left |
| Arcade opens | ✅ **fully drawn in 235 ms** — the warm engine earns its keep |
| Correct version embedded | ✅ Coin Quest only, v1 tagline, no Passage |
| OFFLINE chip | ✅ as expected, no backend yet |
| Compliance disclaimer readable | ✅ "XP and badges have no monetary value" |
| A game actually plays | ✅ level map → level sheet → board, HUD, coach tip |
| Back returns to the ticker | ✅ single back, ticker still live |
| Crashes | ✅ none in logcat across the whole run |

Re-verified after the v1.0.1 rebuild: ticker live, arcade opens, no crash or
fatal in logcat. Screenshots in `shots/`.

### Also verified, from the coin work

| Check | Result |
|---|---|
| Ticker and arcade show the same coin | ✅ `shots/ticker-and-arcade.png` |
| Header coin spins | ✅ caught edge-on mid-turn, milled edge visible — `shots/app-coin-spin.png` |
| Arcade coin flips | ✅ edge-on on the *other* axis — `shots/arcade-coin-flip.png` |
| Launcher icon through the system mask | ✅ `shots/launcher-icon-masked.png` |

Catching a 1.1s animation needs the capture loop to run **on the device**, in
one `adb shell`. A round-trip per frame costs ~400ms and misses the turn
entirely.

### One thing found, and it is v1's, not the embedding's — now fixed

The level sheet's bottom edge was clipped by the navigation bar, with the Play
button sitting right on it. I checked this properly rather than assuming:
installed the standalone v1 demo APK alongside and drove it to the same
screen. **Identical.** So it was a pre-existing v1 cosmetic defect, not
something the embedding introduced.

Cause: `showModalBottomSheet` does not inset its child for system UI, so a
sheet with a plain `EdgeInsets.all(16)` margin ends up underneath the nav bar.
Both sheets in v1 had it. Fixed once in `AppTheme.sheetMargin` rather than
twice at the call sites, so the next sheet inherits it, and shipped as
**v1.0.1+101, tagged `v1.0.1`** per the procedure in `VERSIONS.md`.

Verified on the Pixel: the card and the Play button now clear the nav bar
(`shots/level-sheet-fixed.png`).

v2 has the identical defect in the same two files and the same fix has been
applied there by hand — **uncommitted**, because v2's worktree has in-progress
Passage work belonging to another session. `flutter analyze` is clean on both.
Whoever owns v2 can keep those edits or drop them and take `git merge main`
instead. v2's own cabinet sheets (`arcade/cabinet/cabinet.dart`) have not been
audited against this.

## Still to do

- **The `DGD_APP_TAB` suppression is unverified by eye.** The flag is passed
  by `build_aar.cmd` and is a compile-time constant, but confirming that the
  fireworks and winner line are actually absent needs a won level, and the
  embedded build has no DEV menu to force one. Worth a human playing a level
  through before anyone relies on §4.3 being satisfied.
- **iOS.** Not started, needs a Mac. Route is specced in
  `NATIVE-SOURCE-REVIEW.md`: `flutter build ios-framework` into `.xcframework`s
  declared in `project.yml`, *not* CocoaPods, because their `pbxproj` is
  generated by XcodeGen and would discard a Pods integration on regeneration.
- **`ARCADE_API`.** Not yet passed to the AAR build. Until a backend is
  hosted the embed is built with `set DGD_EMBED=demo`, and `build_aar.cmd`
  refuses to run unless that or `ARCADE_API` is set. The earlier build with
  neither fell back to `http://localhost:8787` at every ticker launch
  (`AUDIT-RC-2026-09-20.md` RC1, fixed in arcade v1.0.2). When the backend
  exists: `set ARCADE_API=https://...` and rebuild.
- ~~Regression pass on their app after the Kotlin 2.4 jump.~~ **Done** —
  `KOTLIN-2.4-REGRESSION.md`. It raised two follow-ups of its own: Gradle
  8.11.1 → 8.14.4 before Kotlin 2.5, and the complete absence of Compose UI
  tests.
- **The iOS coin spin is unbuilt.** `apple/.../SpinningCoinView.swift` was
  written without a Mac and has never been compiled. Details and the one-line
  revert are in `COIN-AND-ICON.md`.
- **Two near-identical launcher icons**, if v1 ever also ships standalone.
  A branding call, not a technical one — `COIN-AND-ICON.md` sets it out.
