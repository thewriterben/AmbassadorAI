# DGD native Android fix — red-team check, 2026-09-20

> **Scope and authorisation.** The fix drop in `dgd-native-fix/` (three
> patched Kotlin files and a debug APK) and the write-up in
> `FIX-ANDROID-TICKER.md`, checked against the source as delivered in
> `F:\Documents\dgdappsource\DigitalGold-native-source-for-Benjamin.zip`, the
> working tree at `C:\src\dgd-native`, and Benji's own Pixel 9a. The one
> outbound request was a single GET to the public stats endpoint, with no
> `Origin` header, to confirm what it returns. No fixes were applied; every
> item below is a verification or an observation, and fixing is a separate
> change.
>
> **Clean room.** Everything was reproduced from scratch rather than from the
> working copies: the pristine zip copied to an isolated directory with only
> the three patched files applied, a fresh Gradle home, JDK 21; and for the
> arcade, a detached git worktree at `00fb50d` with `npm ci`, `flutter pub
> get` and the suites run from there. Both were deleted afterwards.
>
> **Verdict in one line.** The fix is real, minimal, reproducible, and works
> on the device. Five observations below are things the write-up does not
> say; none of them blocks forwarding it.

---

## 1. The fix drop — verified

### 1.1 Scope claim holds
`FIX-ANDROID-TICKER.md` says three files changed and "the rest of the tree is
exactly as delivered." Checked, not trusted:

| Check | Result |
|---|---|
| `dgd-native-fix/*.kt` vs `C:\src\dgd-native` working tree | byte-identical |
| `C:\src\dgd-native\android` vs the delivered zip | exactly the three `.kt` files differ, plus a `.kotlin/` cache dir |
| Kotlin plugin version in `build.gradle.kts` | 2.0.21, as delivered (the diagnostic-time bumps are reverted) |
| Pristine zip contains any of the three changes | no (`withContext`, `safeDrawingPadding`, `imePadding` all absent) |

### 1.2 Clean-room build reproduces the delivered APK
Pristine zip → isolated directory → apply the three files → fresh
`GRADLE_USER_HOME` → JDK 21.0.12 → `gradlew test assembleDebug`.

- **104 unit tests, 0 failures**, across 16 classes, including
  `LiveStatsClientTest.doesNotSendOriginHeader`.
- The resulting APK vs `DigitalGold-Android-FIXED-debug.apk`, entry by entry:
  all ten `classes*.dex`, `AndroidManifest.xml`, `resources.arsc`,
  `assets/stats-source.json` and `DebugProbesKt.bin` are **byte-identical**,
  with one exception: `classes3.dex` differs in a single line, D8's
  incremental-build per-class checksum map. The map lists 232 classes in both;
  13 checksums differ, all lambdas of the two edited UI files. **No bytecode
  differs** — the dex bodies are identical, so this records that the drop was
  compiled incrementally while the clean room compiled from scratch, nothing
  more.

Two environment notes from getting there, both mine and not the project's:
Gradle 8.11.1 needs a JDK 21 or 17 (the doc says so; confirmed by building
with it), and AAPT2's daemon refuses to start when the build path is deep
(the session scratchpad path was; a short path fixed it).

### 1.3 The installed APK is the delivered one
`adb pull` of `base.apk` from the Pixel 9a, hashed:

```
5c950e1b4e4d85371faf017199ab6a8b47371cddc30e812bbc1b63ae157aa276  installed
5c950e1b4e4d85371faf017199ab6a8b47371cddc30e812bbc1b63ae157aa276  dgd-native-fix/
```

Manifest and signing, from `aapt2` and `apksigner`: `com.digitalgold.ticker`
1.0.0 (1), minSdk 26, targetSdk 35, `INTERNET` and `VIBRATE` only,
`usesCleartextTraffic=false`, `debuggable=true`, `allowBackup=true`, v2
signature by the `Android Debug` certificate. The second exported activity is
Compose's `PreviewActivity` from `debugImplementation("ui-tooling")`, which
is correct for a debug build and absent from release. One asset,
`stats-source.json`. No secret-shaped strings in any dex; the only hosts are
`digitalgold.co` and vendor issue-tracker URLs inside library code.

### 1.4 Device behaviour
Force-stop, clear logcat, cold start, read eight seconds of log:

- no `NetworkOnMainThreadException`, no `StrictMode`, no `AndroidRuntime`
  crash, no `LiveStatsClient` warning (the success path logs nothing, so a
  silent log is the expected outcome now — the opposite of before);
- screencap at 14:35 shows the live price, 3,815 accounts, the market cap and
  a LIVE footer timestamped 14:34, all inside the safe area.

The screenshots in `dgd-native-shots/` are consistent with the write-up's own
timeline: `ticker-fixed-clean.png` (13:58, after the network fix, before the
inset fix) still has the footer under the navigation bar; `ui-01-home.png`
(14:08, after) does not. `ui-05-signup-bottom.png` shows the password field
and the Continue button clear of the bar; `ui-06-keyboard.png` shows the
focused field above the keyboard, and the footnote wraps to "no spaces."

### 1.5 The "also noticed" section is right
A plain `GET https://digitalgold.co/api/forms/stats` with `Accept:
application/json` and no `Origin`, at 14:3x on 2026-09-20:

```
HTTP 200
{"userLevel":{"level":3815,"count":3815,"price":11.52,...,"marketCap":85690474},"count":3815}
```

So the API does now publish `price` and `marketCap`, and the app's derived
`$85,708,608` is above the API's `$85,690,474` by the amount the write-up
states. That is a decision for DGD, as the write-up says; not a defect.

---

## 2. Observations the write-up does not make

Ordered by what I would want to know first. None blocks forwarding.

### N1. LOW — the fetch is now off the main thread but still not cancellable
`LiveStatsClient.kt:38-47`. `withContext(Dispatchers.IO)` moves the blocking
`execute()` off main, but a blocking call ignores coroutine cancellation.
Leaving the screen mid-fetch keeps an IO thread blocked for up to the 15 s
connect/read timeouts, and the `LaunchedEffect` that cancelled it does not
get the thread back until then. One line: `invokeOnCancellation { call.cancel() }`
around a `suspendCancellableCoroutine`, or OkHttp's `Call.await` extension.

### N2. LOW — the silent catch survives one layer up
The write-up rightly replaces `catch (_: Exception)` in the client with a
logged rethrow. The same pattern is still in the caller:
`TickerViewModel.kt:76` in the delivered tree catches any non-`StatsClientError`
exception and maps it to `Unavailable` without logging. A parse-time runtime
exception that is not a `StatsClientError` would still be invisible. Same
fix, same cost.

### N3. INFO — `safeDrawingPadding()` includes the keyboard inset
`TickerScreen.kt:191`. Safe-drawing is system bars plus display cutout plus
IME. The activity is `adjustResize`, and the login and signup sheets are
`ModalBottomSheet`s, so when the sheet's keyboard opens the ticker behind the
scrim may re-lay out. Cosmetic if it happens; **not tested on the device**.
If a jump is ever seen, `systemBarsPadding()` plus `displayCutoutPadding()`
on the ticker is the narrower choice.

### N4. INFO (pre-existing, for `MERGE.md`) — backup is on, and the password store is device-bound
`allowBackup="true"` in the manifest, and the password lives in
`EncryptedSharedPreferences`. The master key is in the Keystore and is never
backed up, so a restore to a new device brings the ciphertext without the
key. The app must tolerate an unreadable preferences file on first open after
restore (typically an `AEADBadTagException`), or set backup rules that exclude
it. Not part of this fix, and not something this session tested; it belongs
in the privacy and merge notes because the arcade will ship in this binary.

### N5. INFO — wording
The write-up says the footer sat "behind the gesture bar." The Pixel in the
screenshots is in three-button navigation. `safeDrawingPadding()` handles
both, so nothing changes; just do not let anyone read "gesture" as a
gesture-only bug.

---

## 3. Arcade red-team suites, from a fresh worktree

Detached worktree at `00fb50d`, dependencies installed fresh, run from there
and then deleted.

| Suite | Result |
|---|---|
| `v1/server` `npm test` | 30 tests: **25 pass, 5 todo, 0 fail** |
| `v2/server` `npm test` | 31 tests: **26 pass, 5 todo, 0 fail** |
| `v1/app` `flutter test` | **34 pass**, 6 skipped by default; `flutter analyze` clean |
| `v2/app` `flutter test` | **62 pass**, 6 skipped by default; `flutter analyze` clean |
| `v1/app` and `v2/app` with `--dart-define=ARCADE_API=http://127.0.0.1:<port>` | **5 pass** each (network and identity layer) |
| `v1/app` and `v2/app` with that plus `--dart-define=DGD_DEMO=true` | **1 pass** each (demo build makes zero requests) |

In both mirrors R1, R5, R10 and R11 **hold**, R2, R8 and R12 are
**accepted**, and R4, R6, R7 and R9 are still **open under `todo`**, exactly
as the 18 Sept audit left them.

### One thing worth knowing about the Flutter numbers
A plain `flutter test` prints "All tests passed!" while **silently skipping
the six network and identity cases**, including the demo zero-request test
that closed A1. They run only when `ARCADE_API` points at a loopback port
other than 8787 — by design, so the suite never touches a dev server by
accident — but it means a green run without the define has not exercised the
network layer at all. CI should pass the define explicitly, and the "39 + 1"
figures in the 18 Sept audit should be read as "with the define."

---

## 4. Housekeeping

- `dgd-native-fix/` (three `.kt` files and the 20 MB debug APK),
  `dgd-native-shots/` (nine screenshots) and `FIX-ANDROID-TICKER.md` are
  committed alongside this audit so the audit is self-contained, following
  the precedent of the APKs already under `dist/`.
- The clean-room worktree and build directories were removed;
  `git worktree list` shows only the main tree.
- Nothing in `C:\src\dgd-native` or the delivered zip was modified.

*Earlier passes: `AUDIT-2026-09-16.md`, `AUDIT-2026-09-18.md`. The source
review behind this drop is `NATIVE-SOURCE-REVIEW.md`; the merge questions are
in `MERGE.md`.*
