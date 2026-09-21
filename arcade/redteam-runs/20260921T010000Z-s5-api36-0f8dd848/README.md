S5 check: `DGD-merged-arcade-v1.0.3-demo-debug.apk` after the Stats panel rewrite
(sha256 0f8dd848…) on the Android 16 emulator with the network on, so the
ticker fetched live stats once from digitalgold.co (the app's own behaviour).

- `36-stats-panel.png` — the Stats button expands to Accounts, Price, Market
  cap and "Live figures from digitalgold.co, updated 9:37 PM." No chart, no
  timeframes, no percent captions, no "illustrative" line.

Findings: `../../STORE-READINESS-2026-09-20.md`, S5.
