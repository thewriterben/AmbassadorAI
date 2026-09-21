Emulator pass on `DGD-merged-arcade-v1.0.2-demo-debug.apk` (sha256 72837584…).

- `report.md` — static inspection from `tools/redteam.sh --apk`.
- `impostor-requests.log` — offline phase, localhost:8787 routed to the impostor:
  empty across cold start, arcade, Coin Quest, level sheet and board.
- `proxy-egress.log` — online phase, every CONNECT/GET the emulator made. The
  app's only remote is 15.204.87.31:443 (digitalgold.co); the rest is Google
  system traffic.
- `emulator-coinquest-board.png`, `emulator-signup-filled.png`,
  `emulator-signup-verification.png` — the screens reached.

Findings: `../../AUDIT-v1.0.2-2026-09-20.md`.
