# Clean-room red-team run — 20260920T233407Z

Commit `db7c2a1277d7937a01198b11949eac9560bff361` (`HEAD`). Policy: `arcade/REDTEAM-POLICY.md`.
Worktree is detached at the hash; the working copy is not consulted.

| Check | Result | Detail |
|---|---|---|
| worktree | PASS | detached at db7c2a1277d7 |
| apk debuggable | REVIEW | android:debuggable=true — a test build, not for distribution |
| apk hosts | PASS | only allowlisted hosts in the app's dex (7 files) |
| apk secrets | PASS | none in the app's dex |
| apk native libs | REVIEW | arm64-v8a/libandroidx.graphics.path.so arm64-v8a/libapp.so arm64-v8a/libdartjni.so arm64-v8a/libdatastore_shared_counter.so arm64-v8a/libflutter.so armeabi-v7a/libandroidx.graphics.path.so armeabi-v7a/libapp.so armeabi-v7a/libdartjni.so armeabi-v7a/libdatastore_shared_counter.so armeabi-v7a/libflutter.so x86/libandroidx.graphics.path.so x86/libdartjni.so x86/libdatastore_shared_counter.so x86_64/libandroidx.graphics.path.so x86_64/libapp.so x86_64/libdartjni.so x86_64/libdatastore_shared_counter.so x86_64/libflutter.so  |


### Shipped APK: `DGD-merged-arcade-v1.0.1-debug.apk`

sha256 `07aabe7f4652c2c7ec57acbb7762f210887abe968cbe2efa579adca178513e4d`

```
package: name='com.digitalgold.ticker' versionCode='1' versionName='1.0.0' platformBuildVersionName='16' platformBuildVersionCode='36' compileSdkVersion='36' compileSdkVersionCodename='16'
targetSdkVersion:'35'
uses-permission: name='android.permission.INTERNET'
uses-permission: name='android.permission.VIBRATE'
uses-permission: name='com.digitalgold.ticker.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION'
```

Exported components: Raw: "androidx.compose.ui.tooling.PreviewActivity" Raw: "androidx.profileinstaller.ProfileInstallReceiver" Raw: "com.digitalgold.ticker.MainActivity" 

**Verdict: REVIEW** — 2 item(s) need a human read. Report: C:\Users\Benji\AppData\Local/Temp/rc/run/report.md
