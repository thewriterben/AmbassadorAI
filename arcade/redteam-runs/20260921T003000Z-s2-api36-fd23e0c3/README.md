S2 retest: `DGD-merged-arcade-v1.0.3-demo-debug.apk` (targetSdk 36, 1.0.3 (3),
sha256 fd23e0c3…) on a wiped Android 16 (API 36, Google APIs, x86_64)
emulator booted with `-gpu host -feature -Vulkan`, Wi-Fi and data off,
localhost:8787 routed to the impostor backend.

- `impostor-requests.log` — empty across cold start, arcade, Coin Quest, a
  level, and the login sheet.
- `36-home.png`, `36-arcade.png`, `36-board.png`, `36-login.png`,
  `36-login-keyboard.png` — insets under Android 16 edge-to-edge, with the
  keyboard up on the last one.
- The hostile deep link opened Chrome, not the app: app links are unverified
  (`pm get-app-links` → legacy_failure), tracked as S7.

Findings: `../../STORE-READINESS-2026-09-20.md`, S2.
