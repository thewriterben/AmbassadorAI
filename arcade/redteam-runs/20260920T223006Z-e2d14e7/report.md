# Clean-room red-team run — 20260920T223006Z

Commit `e2d14e7766600d8befb60941f759b8630928057b` (`HEAD`). Policy: `arcade/REDTEAM-POLICY.md`.
Worktree is detached at the hash; the working copy is not consulted.

| Check | Result | Detail |
|---|---|---|
| worktree | PASS | detached at e2d14e776660 |
| v2 server tests | PASS | 31 tests: 26 pass, 5 todo |
| v2 server hosts | PASS | only allowlisted hosts in src/ |
| v2 server secrets | PASS | no secret-shaped strings |
| v2 app analyze | PASS | no issues |
| v2 app tests (plain) | PASS | +62 ~6: All tests passed |
| v2 app tests (ARCADE_API loopback) | PASS | +67 ~1: All tests passed |
| v2 app demo zero-request group | PASS | +1 ~5: All tests passed |
| v2 app network cases ran | PASS | 5 more cases with the define |
| v2 app hosts | PASS | only allowlisted hosts in lib/ |
| v2 app secrets | PASS | no secret-shaped strings |
| apk debuggable | REVIEW | android:debuggable=true — a test build, not for distribution |
| apk hosts | PASS | only allowlisted hosts in the app's dex (7 files) |
| apk secrets | PASS | none in the app's dex |
| apk native libs | REVIEW | arm64-v8a/libandroidx.graphics.path.so armeabi-v7a/libandroidx.graphics.path.so x86/libandroidx.graphics.path.so x86_64/libandroidx.graphics.path.so  |
| native patch | PASS | 3 source files applied |
| native unit tests | PASS | 104 tests, 0 failures |
| native reproducibility | PASS | 94 entries byte-identical; classes3.dex differ only in D8's incremental checksum map (no bytecode difference) |


### v2 server red-team ledger

- ✔ HOLDS R1 the mini-game daily cap still binds when rounds straddle UTC midnight
- ✔ ACCEPTED R2 a mini-game score is whatever the client says, bounded only by the per-round and per-day caps
- ⚠ OPEN R3 anonymous player creation is throttled by something other than the generic limiter # TODO
- ⚠ OPEN R4 the rate limiter does not admit a double burst at the window boundary # TODO
- ✔ HOLDS R5 X-Forwarded-For is ignored unless a proxy is trusted, and then only its last hop counts
- ⚠ OPEN R6 a tablet cannot be answered once its expedition is finished # TODO
- ⚠ OPEN R7 a bank question that disappears between issue and answer is a 4xx, not a 500 # TODO
- ✔ ACCEPTED R8 status="xp_only" means zero XP, not "XP only", and is never set by the server
- ⚠ OPEN R9 a corrupt server-written JSON column is a handled error, not a 500 # TODO
- ✔ HOLDS R10 the board never carries ids or tokens, and handle rerolls stop at the daily cap
- ✔ HOLDS R11 /healthz is the only unauthenticated read and says only that the bank is loaded
- ✔ ACCEPTED R12 CORS is a wildcard unless ARCADE_CORS is set, whatever NODE_ENV says

### v2 server routes (from source)

```
DELETE /v1/me
GET /healthz
GET /v1/leaderboard
GET /v1/ledger/today
GET /v1/me
POST /v1/expeditions
POST /v1/expeditions/:id/finish
POST /v1/expeditions/:id/tablets/:idx
POST /v1/expeditions/:id/tablets/:idx/answer
POST /v1/ledger/guess
POST /v1/me/handle/reroll
POST /v1/mini/:game
POST /v1/mini/:game/start
POST /v1/players
```

### v2 server environment flags

```
ARCADE_ALLOW_DEV_SECRET ARCADE_BANK ARCADE_CORS ARCADE_DB ARCADE_SECRET ARCADE_TRUST_PROXY NODE_ENV 
```

### v2 app dart-defines read by the code

```
ARCADE_API DGD_APP_TAB DGD_DEMO DGD_DEV 
```

### Shipped APK: `DigitalGold-Android-FIXED-debug.apk`

sha256 `5c950e1b4e4d85371faf017199ab6a8b47371cddc30e812bbc1b63ae157aa276`

```
package: name='com.digitalgold.ticker' versionCode='1' versionName='1.0.0' platformBuildVersionName='15' platformBuildVersionCode='35' compileSdkVersion='35' compileSdkVersionCodename='15'
targetSdkVersion:'35'
uses-permission: name='android.permission.INTERNET'
uses-permission: name='android.permission.VIBRATE'
uses-permission: name='com.digitalgold.ticker.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION'
```

Exported components: Raw: "androidx.compose.ui.tooling.PreviewActivity" Raw: "androidx.profileinstaller.ProfileInstallReceiver" Raw: "com.digitalgold.ticker.MainActivity" 

### Native clean room

zip sha256 `a7e7bf0813a532fb08ab646b9b00c1ff1320d97732d8132a83e33cc0515e88a1`, patch dir `/f/Documents/GitHub/AmbassadorAI/arcade/dgd-native-fix`

```
android/app/src/main/java/com/digitalgold/ticker/networking/LiveStatsClient.kt
android/app/src/main/java/com/digitalgold/ticker/ui/SignupPreviewScreen.kt
android/app/src/main/java/com/digitalgold/ticker/ui/TickerScreen.kt
```

**Verdict: REVIEW** — 2 item(s) need a human read. Report: F:/Documents/GitHub/AmbassadorAI/arcade/redteam-runs/20260920T223006Z-e2d14e7/report.md
