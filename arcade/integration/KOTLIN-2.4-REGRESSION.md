# Kotlin 2.0.21 → 2.4.0 regression pass

**2026-09-20.** Verdict up front: **for this codebase the compiler jump is a
non-event.** Nothing in the app's compiled output changed in a way that
matters, the release variant builds and runs, and the two new warnings are
both benign. The residual risk is not in the compiler — it is that the surface
the compiler most affects has no automated tests at all.

## Method, and why it needed one

"Their tests pass" is not a regression pass. The tests are all logic —
formatters, parsing, the view model, the stores — and a Kotlin bump in a
Compose app puts the *Compose* output at risk, which none of them touch.

The problem is that the integrated app **cannot** be built at 2.0.21: the
arcade AAR ships kotlin-stdlib 2.4.0, whose metadata a 2.0 compiler cannot
read. So a throwaway copy was made at `C:\src\ticker-baseline` with the
arcade stripped out (a `make_baseline.py` did it and then
proves no live arcade reference survives), and built **twice from identical
source, changing only the Kotlin version**. One variable, or the comparison
means nothing.

> **The script is not checked in.** It was not saved with this note; the
> stripped copy still exists at `C:\src\ticker-baseline` but the script that
> produced it does not, so this pass cannot be re-run from the repository
> until it is rewritten (audit RC2).

Both runs: `assembleRelease testDebugUnitTest --rerun-tasks`, 69 tasks
executed, BUILD SUCCESSFUL. 2.0.21 in 1m31s, 2.4.0 in 1m15s.

## What was compared

| | 2.0.21 | 2.4.0 |
|---|---|---|
| Release build | ✅ | ✅ |
| Unit tests | ✅ | ✅ |
| Compiler warnings | 0 | **4** (see below) |
| Release APK | 13.97 MB | 14.04 MB |
| dex | 43.53 MB | 43.79 MB |
| APK entries | 174 | 175 |

**The one new APK entry is `kotlin/concurrent/atomics/atomics.kotlin_builtins`**
— a stdlib package that did not exist in 2.0. Every other changed entry is
either a `.kotlin_builtins` metadata blob or a dex file. **No app-specific
entry appeared, disappeared, or moved.** The +253 KB of dex is the newer
stdlib, not generated-code bloat.

## Dependencies: no split, one skew

Resolved versions are identical across the debug and release classpaths, and
there is **exactly one `kotlin-stdlib`, at 2.4.0** — the failure mode where an
old stdlib lingers alongside a new one is not present.

| | |
|---|---|
| kotlin-stdlib | 2.4.0 |
| kotlinx-coroutines | 1.9.0 |
| androidx.compose runtime / ui | **1.7.6** |
| material3 | 1.3.1 |
| androidx.core / core-ktx | 1.17.0 |
| okhttp | 4.12.0 |

`kotlin-stdlib-jdk8` resolves to 1.9.10, which looks alarming and is not: since
Kotlin 1.8 that artefact is an empty shim that redirects to `kotlin-stdlib`.

**The one thing worth naming: the Compose compiler is 2.4.0 while the Compose
runtime is 1.7.6**, from a BOM dated 2024.12.01. A compiler roughly a year
ahead of the runtime it emits calls into is the sort of skew that can bite.
Here it does not — the compiler accepted it, the feature flags it chose are
the same on both sides (StrongSkipping on, IntrinsicRemember on,
OptimizeNonSkippingGroups off), and the app runs. But updating the Compose BOM
is a sensible, low-risk follow-up rather than something to leave indefinitely.

## The four new warnings

Two are in their source, and both are correct and harmless:

1. **`TickerContent.kt:239` — "Elvis operator always returns the left operand
   of non-nullable type 'Long'."** The code is
   `val start = waveStartedAtMillis ?: return@LaunchedEffect`. Above it,
   `animating` holds `waveStartedAtMillis != null && !reduceMotion`, and the
   function returns early `if (!animating)`. K2 tracks null-checks through a
   local `val` like that, so by line 239 it has proved the value non-null and
   the elvis is unreachable. **Accurate, and the behaviour is identical either
   way** — it is a defensive guard the compiler can now see is redundant.
   Leave it; removing it buys nothing and loses a guard if the logic above
   ever changes.
2. **`PriceExplosion.kt:155` — "Redundant call of conversion method."**
   Cosmetic.

The third is forward-looking and **is a real action item**: the Kotlin Gradle
plugin warns that **Gradle 8.11.1 is deprecated and Kotlin 2.5 will require
8.14.4**. Not urgent, but it is now on the clock.

The fourth, "Failed to compile with Kotlin daemon", was **caused by this
investigation, not by their build** — see below.

## What could not be checked, and a retraction

The sharpest available signal for a Compose compiler bump is the compiler's
own stability report: it says which composables are skippable, and a
composable that quietly stops being skippable recomposes on every frame its
parent does. That shows up in no test, no lint rule, and no smoke test.

**That comparison could not be completed.** At 2.4.0 the Compose plugin's
report writer throws `IOException: Invalid file path`, takes the Kotlin daemon
down with it, and leaves **empty** files behind. Retried with a short absolute
destination outside `build/`; same result — two zero-byte files.

**A first version of this document said the metrics were byte-for-byte
identical across both compilers. That was wrong and is retracted.** The
reports are written into the shared copy's `build/` directory, which was not
wiped between the two runs. The 2.4.0 run wrote nothing, so the 2.0.21 files
survived and were compared against themselves. Timestamps settled it: every
report file was stamped 17:06:17, while the 2.4.0 run did not finish until
17:09:15. A clean result that measured nothing.

So: the per-composable skippability comparison is **unavailable**, and the
confidence below rests on the other evidence instead.

## On device

Release variant, built for the first time ever and signed with the **local
debug keystore** purely so it could be installed — the real release keystore
is DGD's and is deliberately not created or held here. This proves the release
*build configuration* runs; it says nothing about release *signing*.

| Check | Result |
|---|---|
| Ticker | ✅ live price, coin, Stats and CTA |
| Stats panel | ✅ Network Growth chart, +169 accounts this week |
| Arcade opens | ✅ fully drawn in 190 ms |
| Crashes / fatals | ✅ none |

Installed APK on the device measured at **74,167,305 bytes**, matching
`dgd-release-debugsigned.apk` exactly, `firstInstallTime` 17:25.

### Correction: the first run of this check tested the wrong build

An earlier version of this table reported the release variant fully drawing in
124 ms and called it "faster than debug's 235 ms, as AOT should be". **That
was the debug build.** The script that was supposed to install the release APK
died after signing it, before `adb install` ran, so the device still had the
debug APK from 16:44 and every screenshot and timing came from it. The
reasoning about AOT was built on a premise that was never checked.

It surfaced only because someone asked which build was current and the
device's `lastUpdateTime` predated the release APK's own file timestamp. The
lesson is cheap and worth keeping: **assert which artefact is installed by
measuring it — `ls -l` on the device's `base.apk` against the candidate file
sizes — rather than inferring it from a script that appeared to run.** The
numbers above come from a run that did that check first.

Treat 190 ms as indicative rather than a benchmark: the figure moves with
whether the engine and the app are already warm.

The one repeated log line is
`AppOps: attributionTag not declared in manifest`, emitted by `system_server`
roughly every 25 seconds — the stats poll interval. It is platform noise about
a manifest attribution tag, unrelated to Kotlin, and predates this work.

Note `release { isMinifyEnabled = false }`: R8 runs but does not shrink or
obfuscate. That removes a whole class of risk from this bump, and is also a
separate decision someone should make deliberately before shipping.

## The finding that actually matters

**There are no instrumented tests.** `app/src/androidTest` does not exist. The
17 unit-test files are all non-UI logic.

So the part of the app the Compose compiler governs — every composable, every
recomposition, every remember — is covered by nothing but a human looking at
it. That was true before this bump and is not caused by it, but it is what
makes a bump like this hard to clear with confidence, and it is why the
missing stability report stings.

Worth adding even two or three Compose UI tests (`createAndroidComposeRule`,
assert the ticker renders a price and the Arcade button exists). Cheap, and it
converts the next compiler bump from a judgement call into a test run.

## Summary

| | |
|---|---|
| Compiles, tests, builds release, runs | ✅ evidenced at both versions |
| Dependency hygiene | ✅ single stdlib, no splits |
| Compiled output | ✅ no app-level change; growth is stdlib |
| New warnings | ✅ 2 benign, analysed |
| Compose skippability | ⚠️ **unverifiable** — tooling broken at 2.4.0 |
| Compose test coverage | ⚠️ **none exists** |
| Gradle 8.11.1 | ⚠️ must reach 8.14.4 before Kotlin 2.5 |

Confidence that the bump is safe: **high**, on the strength of identical
compiled shape, a clean dependency graph, a working release build and a clean
device run — not on the strength of the test suite, which does not reach the
code at risk.

Throwaway artefacts, deletable: `C:\src\ticker-baseline`, `C:\src\kotlin-ab`,
`C:\cm`. Their own project was not modified by any of this.
