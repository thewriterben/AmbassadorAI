Clean-room dynamic run of `arcade/integration/DGD-merged-arcade-v1.0.1-debug.apk`
(sha256 07aabe7f…3e4d) on a wiped `dgd_api35` emulator (API 35, Google APIs,
x86_64) in airplane mode, with the device's `localhost:8787` routed by
`adb reverse` to a host listener that impersonates the arcade backend.

- `report.md` — the static inspection from `tools/redteam.sh --apk`.
- `impostor-requests.log` — every request the app made to the impostor. Both
  lines arrived at ticker launch, before the arcade was opened.
- `emulator-arcade-after-impostor.png` — the arcade as it then rendered.

Full findings: `../../AUDIT-RC-2026-09-20.md`.
