# Run 20260929T2330Z — DGD 1.0.8 RC (review APK `7c2567c2…`, AAB `43e1f5fd…`)

Findings and verdict: `arcade/AUDIT-v1.0.8-2026-09-29.md`.

Source: dgd-native `android-1.0.8-rc1` (`0520865`); arcade from puzzle-app v1 `99a5c36`, Flutter 3.47.2.

## Files

| File | What it is |
|---|---|
| `api36-*.png`, `api36-logcat.txt` | Android 16, offline, impostor on `localhost:8787` |
| `api36-backup.tar`, `api36-backup-after-login.tar` | local-transport backups, before and after login: `_manifest`, `r/app_flutter`, `f/profileInstalled` only |
| `online-*.png`, `online-logcat.txt` | Android 16, online behind the logging proxy; signup preview walked through to Receive |
| `api26-*.png`, `api26-logcat.txt`, `api26-backup.tar` | Android 8.0 (the minSdk), offline |
| `impostor-requests.log` | 0 lines: nothing reached the fake backend (gitignored, `*.log`) |
| `online-proxy-egress.log` | 12 lines (gitignored, `*.log`); summary below |
| `cleanroom/` | Dockerfiles, scripts, offline lint, `aab-compare.txt`, `aar-compare.txt`, hashes, the module lock and the Dart private-key calculation |

## Proxy egress, online phase

```
3 CONNECT 15.204.87.31:443            digitalgold.co, the app's stats fetch
2 CONNECT 74.125.137.188:5228         GMS
2 CONNECT 142.251.108.94:443          Google
1 GET     connectivitycheck.gstatic.com
1 GET     clients2.google.com
1 CONNECT [2001:4860:4844:400::]:443  Google
1 CONNECT 192.178.142.100:443         Google
1 CONNECT 142.251.153.119:443         Google
```

The on-device sampler of the app uid's sockets saw only `15.204.87.31:443`.

## Clean-room hashes

- AAB rebuilt offline from the tag: `ED2E310ADB08510FE44CB21AF26515EA5DEFFCF4F208BE7F34E2CA53B90E6E90`
  (636/642 entries identical to the shipped AAB; see `cleanroom/aab-compare.txt`).
- AAR rebuilds and the checked-in AAR: `cleanroom/aar-rebuilds.sha256`.
- Images: `dgd-cleanroom:1` `sha256:0ef9b2810304…`, `dgd-cleanroom-flutter:1` `sha256:966e6843be6c…`.
