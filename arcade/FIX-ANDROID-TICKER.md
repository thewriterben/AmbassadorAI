# The Android ticker: found, fixed, verified on a device

**2026-09-20.** Everything below the line is written to be forwarded.

Five fixes in total: one that stopped the app working at all, and four UI
faults found by using it on a phone afterwards. All verified on a Pixel.
Patched files and a working debug APK are in `dgd-native-fix/`; screenshots
of every state in `dgd-native-shots/`.

---

## Summary

The Android ticker never loaded. It is one line.

`LiveStatsClient.fetchSnapshot()` is a `suspend` function, but it calls
OkHttp's **blocking** `execute()` without moving off the caller's thread. A
`suspend` function does not get its own thread — it runs on whatever
dispatcher its caller used, and the caller is a Compose `LaunchedEffect`,
which is the **main thread**. Android's StrictMode refuses network I/O there,
so every single fetch threw `android.os.NetworkOnMainThreadException` before
a packet left the device.

The exception was then discarded by `catch (_: Exception)`, so nothing ever
reached logcat and the UI fell back to its "Stats unavailable" state.

**The fix**, in `android/app/src/main/java/com/digitalgold/ticker/networking/LiveStatsClient.kt`:

```kotlin
// add
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

// change
override suspend fun fetchSnapshot(): StatsSnapshot {
// to
override suspend fun fetchSnapshot(): StatsSnapshot = withContext(Dispatchers.IO) {
```

The body needs the trailing `return` dropped, since it becomes the value of
the `withContext` block — the patched file is in `dgd-native-fix/`.

**Verified on a Pixel:** HTTP 200, live data, `$11.52425`, 3,815 accounts,
`$85,708,608` market cap, LIVE indicator running. Screenshots in
`dgd-native-shots/`. A working debug APK is in `dgd-native-fix/`.

## Why nobody caught it

This is the interesting part, and it is not anybody's carelessness.

1. **The unit tests cannot catch it.** They run on the JVM with MockWebServer.
   `NetworkOnMainThreadException` is thrown by Android's StrictMode, which
   does not exist on a desktop JVM. The tests are correct and they pass —
   including `doesNotSendOriginHeader`, which I ran.
2. **iOS cannot catch it.** `URLSession` on the main thread is legal on Apple
   platforms. The Swift app has the same shape and works fine, which is
   exactly why "Apple works, Android doesn't" was so confusing.
3. **A source review cannot catch it.** The OkHttp diagnostic that concluded
   "should get 200 JSON" was right about everything it examined. The bug is
   not in the request; it is in the thread the request is made on.
4. **The silent catch hid it.** With the exception discarded, the app showed a
   tidy empty state and said nothing. That is the difference between a
   five-minute fix and three weeks of guessing.

**It only appears on real Android hardware.** The team has none — which is
precisely why this sat.

## Four UI faults, found by using the app once it ran

None of these could be seen before the ticker loaded. All four are on the
phone, none are on the Simulator, and the first three share one cause.

### 1. Content drew under the status bar and the navigation bar

`MainActivity` calls `enableEdgeToEdge()`, and **nothing in the app ever
applies window insets.** On `targetSdk 35` Android 15 enforces edge-to-edge
whether an app asks for it or not, so every child drew under both system
bars: "Log in" sat behind the battery icon, the LIVE footer behind the
gesture bar, and the decorative hairline frame ran off both ends.

`TickerScreen.kt` — wrap the content in one inset:

```kotlin
Box(Modifier.fillMaxSize().safeDrawingPadding()) { … }
```

The inset goes on the *content*, not on the outer Box that paints the
gradient. The gradient should still run edge to edge behind the bars — that
is the point of drawing edge to edge — and only the content is pulled in.

### 2. The signup sheet's last field was cut off

The scrollable form Column in `SignupPreviewScreen.kt` had no
`navigationBarsPadding()`, so the password field ran under the gesture bar.

### 3. The keyboard covered the field being typed into

Same Column, no `imePadding()`. This is worse than it sounds: on a three-field
signup form the keyboard hid the field in focus, and on the password field
that means typing blind.

```kotlin
.verticalScroll(scroll)
.imePadding()            // before navigationBars: the keyboard replaces the
.navigationBarsPadding() // nav bar, so this order stops them stacking
.padding(22.dp)
```

### 4. Step pill 1 lost its label, and a footnote lost half a sentence

Two separate `maxLines = 1` clips, both silent:

- **The pill** read a bare **"1"** while "2 Wallet" and "3 Receive" rendered
  fine — which is exactly what made it look deliberate. The three pills are
  equal thirds, so the longest label sets the budget, and "1 Credentials" at
  14sp did not fit in a third of a 411dp screen. With the default `Clip`
  overflow it was cut to nothing. Now 12sp, tighter padding, and
  `TextOverflow.Ellipsis` as a backstop so a narrower phone degrades to
  "1 Creden…" rather than losing the word silently.
- **The username footnote** rendered as *"Username is your invite code. 3+
  characters,"* — the clip removed "no spaces.", which is the half that
  states a rule. `maxLines = 1` removed; a footnote should wrap.

**The pattern worth taking away:** three of these four were silent. Nothing
crashed, nothing logged, and the screens looked intentional. That is the same
failure mode as the swallowed exception above — the app was confidently
showing something wrong.

## Two things worth changing beyond the one line

**Stop swallowing the exception.** `catch (_: Exception)` is what made this
invisible. The patched file logs it and still throws the same error type, so
no behaviour changes but a failure now says why. This cost nothing and would
have saved everything.

**Turn on StrictMode in debug builds.** Add to `MainActivity.onCreate`,
guarded by `BuildConfig.DEBUG`:

```kotlin
StrictMode.setThreadPolicy(
    StrictMode.ThreadPolicy.Builder().detectNetwork().penaltyLog().penaltyDeath().build()
)
```

That converts this whole class of bug from a silent empty screen into an
immediate, obvious crash during development.

## Files changed

| File | Change |
|---|---|
| `networking/LiveStatsClient.kt` | `withContext(Dispatchers.IO)`; stop discarding the exception |
| `ui/TickerScreen.kt` | `safeDrawingPadding()` on the content |
| `ui/SignupPreviewScreen.kt` | `imePadding()` + `navigationBarsPadding()`; footnote wraps; pill label fits |

Nothing else. I reverted the two Kotlin-version edits I made while diagnosing
a separate local toolchain problem. The rest of the tree is exactly as
delivered.

## Still not checked

The **iOS app**, at all. I have no Mac. Fault 1 is Android-specific, but
faults 2 to 4 have iOS equivalents worth a look on a device rather than the
Simulator: keyboard avoidance on the signup sheet, safe-area insets on a
notched iPhone, and whether the same step-pill label fits at the iPhone SE
width. The Simulator will not reliably show the first two.

## One unrelated note, from building it

Their `gradle-wrapper.properties` pins **Gradle 8.11.1**, whose embedded
Kotlin DSL compiler cannot parse a two-digit Java version. It fails while
compiling `settings.gradle.kts` on **JDK 25** — which is what ships with
current Android Studio. I built with JDK 21.

Not urgent, and not a defect: their CI uses a compatible JDK. But anyone
picking this up on a new machine will hit it, and the error message
(`IllegalArgumentException: 25.0.3`) says nothing useful. A Gradle bump fixes
it when convenient.

## Also noticed

The stats API **now publishes `price` and `marketCap` directly**:

```json
{"userLevel":{"level":3815,"count":3815,"price":11.52,...,"marketCap":85690474},"count":3815}
```

`DATA_SOURCE.md` says only `count` is available and the rest must be derived
on-device with the CFV constants. That was true when it was written; it is not
true now.

The app derives `$11.52425` and `$85,708,608`; the API says `11.52` and
`85,690,474`. The derived market cap is **~$18,000 higher**. Both are
defensible — the derived figure matches the website's own five-decimal
display, which is the stated goal — but the gap is real and someone should
decide which is authoritative. `stats-source.json` already lists
`model_constants_change` as a known failure mode, and this is the first
evidence of that risk being live rather than theoretical.

Not a bug. Worth a decision.
