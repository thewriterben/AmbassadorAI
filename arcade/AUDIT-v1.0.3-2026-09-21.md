# DGD merged app v1.0.3 — red-team pass in the emulator, 2026-09-21

> **Scope and authorisation.** `arcade/integration/DGD-merged-arcade-v1.0.3-demo-debug.apk`
> (sha256 `0f8dd848…`, 80,821,760 bytes; gitignored): the build that carries
> S2 (targetSdk 36), S5 (live-only Stats panel) and S6 (1.0.3 (3)) on top of
> everything the v1.0.2 audit covered. Policy: `REDTEAM-POLICY.md`. Static
> inspection via `tools/redteam.sh --apk` from a detached worktree at
> `11a74cf`. Dynamic work on a **wiped Android 16 (API 36, Google APIs)
> emulator**, the platform the app now targets, in two phases: offline with
> `localhost:8787` routed to an impostor backend, then online behind a
> logging proxy. No fixes applied.
>
> **One exception to §2, deliberate.** The online phase let the ticker's own
> stats fetch reach `digitalgold.co`, once per launch, so the egress could be
> recorded.
>
> **Verdict in one line.** Nothing regressed and nothing new above LOW: the
> arcade still makes zero requests, the app's only remote host is still
> `digitalgold.co`, the encrypted store still holds the email and password
> and the signup files still stay out of backups, and a battery of hostile
> intents aimed straight at the activity crashed nothing. One new LOW that
> only matters once a backend exists, and two observations about the
> preview's verification step that a human should tap through.

---

## What was exercised

| Step | Offline, impostor | Online, proxy |
|---|---|---|
| Cold start, arcade never opened | 0 requests | stats fetch to `digitalgold.co` only |
| Arcade → Coin Quest → level 1 → board → two swaps → abandon | 0 requests, no crash | — |
| Hostile `VIEW` intents delivered to `MainActivity` by component (script-tag path, `javascript:`, `file:///etc/hosts`, `intent://…;end`, NUL bytes, a 4,000-character path, a 600-character query) | no crash, ticker renders | — |
| Login sheet: email and password | at rest checked | — |
| Backup through the local transport, as root | captured and listed | — |
| Signup preview: three fields → Continue → verification step | — | 0 requests |
| Verification → wallet → receive | **not reached by automation** (O1, O2) | — |

## Verified

- **RC1 holds.** Zero requests to the impostor across every arcade screen
  reached, including a board with moves made. Nothing identity-shaped at
  rest: the arcade's only preference is the coach-tip flag.
- **Egress is one host.** Across launch, the Stats panel and the preview's
  first step, the app's only remote endpoint is `15.204.87.31:443`, which is
  `digitalgold.co`. Everything else in the proxy log is Google system traffic.
- **V1 holds.** The verification step reads "Verify your email" and "In the
  live app, a verification code is sent to …"; the old sentence is absent
  from the dex.
- **V2 holds on Android 16.** After a login, `dgd.signup.xml` holds only the
  username, the secure file holds the email and password as two encrypted
  entries, and a recursive search finds neither value in plaintext. The
  local-transport backup contains neither signup file.
- **S2 holds.** targetSdk 36 on Android 16: insets, predictive back and the
  keyboard behave; no crash anywhere.
- **S5 holds.** The static scan finds no "Illustrative" string; the Stats
  panel shows the three live figures and the source line.
- **Hostile intents.** Seven malformed or hostile `VIEW` intents sent
  directly to the activity, bypassing link verification, produced no crash
  and left the ticker in the foreground. The app reads the intent and shows
  its home; it does not act on the path or query.

## Findings

### W1. LOW — the arcade's own preferences file is backed up, and will one day hold the bearer token
The local-transport backup on Android 16 contained `sp/FlutterSharedPreferences.xml`
alongside the ticker's snapshot. Today that file holds one boolean. Once the
embed is built with `ARCADE_API` the same file holds `api.token`, the bearer
credential for the player's XP and board identity, in plaintext, and it
would ride along in cloud backups and device transfers. Two fixes, either
sufficient: add `FlutterSharedPreferences.xml` to both backup rule files, or
keep the token in `flutter_secure_storage` (Keystore-backed) instead of
`shared_preferences`. Gated on a backend existing; worth doing before one
does. **Owner: here, in v1 (`api.dart`) or in the host's backup rules.
Status: open.**

### O1. INFO — the keyboard's action key on the verification code field closed the whole sheet
With `000000` typed in the code field, sending the IME's action key
(`KEYCODE_ENTER`) dismissed the signup sheet entirely and returned to the
ticker home, discarding the typed credentials, instead of verifying.
Observed once, not reproduced a second time because the automation could
not reach the step again the same way. A human should tap through: type a
code, press the keyboard's arrow key, and see whether the sheet closes. If
it does, the field's `onIme` is wired to the wrong action.

### O2. INFO — Back with the keyboard up on the verification step goes back a step and discards the code
Pressing Back while the keyboard was open on the verification step did not
dismiss the keyboard; it returned the sheet to the Credentials step and
cleared the code. On Android 16 with targetSdk 36 predictive back is on by
default and the sheet's own back handling wins over the IME's. Defensible
behaviour, but a user who reaches for Back to hide the keyboard loses their
place. Worth a decision rather than a fix.

### Not walked: wallet and receive steps
Verify sits below the keyboard at y=1396 on this screen and the sheet does
not scroll it into view while the keyboard is open, so the automation could
not press it. The INTEGRATION.md verification on the Pixel walked those
steps by hand on 20 Sept. Their content — the desktop wallet download link,
the QR and invite links with the placeholder App Store ID (S3) — is
unchanged in this build per the static scan.

### Environment
The Android 16 emulator runs only with `-gpu host`; with `-http-proxy` the
arcade was deliberately kept closed, since opening it under the proxy
segfaulted the API 35 emulator twice. The static strings inventory for
reference: `PREVIEW` ×4, `NOT LIVE`, `Demo only` and `id0000000000` in the
native dex (S3, S4), `More games coming soon` in the arcade (S4), nothing
illustrative, nothing localhost.

## How to re-run
```
arcade/tools/redteam.sh --ref main --mirror none --apk arcade/integration/DGD-merged-arcade-v1.0.3-demo-debug.apk
emulator -avd dgd_api36 -wipe-data -no-snapshot -no-window -gpu host -feature -Vulkan   # phase 1 (offline + impostor; arcade open is safe)
emulator -avd dgd_api36 ... -http-proxy http://127.0.0.1:18790                           # phase 2 (keep the arcade closed)
```
Scripts used: `rt103_phase1.sh`, `rt103_phase2.sh` (session scratch; the
steps are listed above). Run artefacts: `redteam-runs/20260921T013000Z-v1.0.3-0f8dd848/`.

*Earlier passes: `AUDIT-v1.0.2-2026-09-20.md`, `AUDIT-RC-2026-09-20.md`.
Readiness items: `STORE-READINESS-2026-09-20.md`.*
