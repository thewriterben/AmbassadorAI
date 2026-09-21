Emulator pass on `DGD-merged-arcade-v1.0.3-demo-debug.apk` (sha256 0f8dd848…),
wiped Android 16 (API 36, Google APIs, x86_64) emulator, `-gpu host -feature -Vulkan`.

Phase 1, offline, localhost:8787 routed to the impostor backend:
- `impostor-requests.log` — empty across cold start, arcade, Coin Quest, a
  board with two swaps, the login flow.
- `p1-board.png` — the board on Android 16.
- `backup103.tar` — what the local backup transport received: neither signup
  preference file; the arcade's own preferences file is included (W1).

Phase 2, network on through the logging proxy:
- `proxy-egress.log` — every CONNECT/GET the emulator made; the app's only
  remote is 15.204.87.31:443 (digitalgold.co), for the stats fetch.
- `p2-verify.png`, `p2-verify-scrolled.png` — the verification step with the
  new copy; the wallet and receive steps were not reached by automation
  (see the audit, O1 and O2).

Findings: `../../AUDIT-v1.0.3-2026-09-21.md`.
