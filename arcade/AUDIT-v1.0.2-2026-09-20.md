# DGD merged app v1.0.2 — red-team pass in the emulator, 2026-09-20

> **Scope and authorisation.** `arcade/integration/DGD-merged-arcade-v1.0.2-demo-debug.apk`
> (sha256 `72837584f16b2e18cfde55b1841f7a08d0509701c4fecc1cf9d8ce433aa5ffa4`,
> 81,017,640 bytes; gitignored): the native ticker with arcade v1.0.2 embedded
> as a demo AAR, the build that closed RC1. Policy: `REDTEAM-POLICY.md`.
> Static inspection via `tools/redteam.sh --apk` from a detached worktree at
> `main`. Dynamic work on a **wiped `dgd_api35` emulator**, in two phases:
> offline with `localhost:8787` routed to an impostor backend, then online
> behind a logging proxy so every egress host is recorded. No fixes applied.
>
> **One exception to §2, deliberate.** The online phase let the ticker's own
> stats fetch reach `digitalgold.co`, once per launch, because the point of
> that phase was to record what the app talks to.
>
> **Verdict in one line.** RC1 stays closed under a wider workout than the
> fix pass gave it, the app's only remote host is `digitalgold.co`, the
> password never leaves the encrypted store, and nothing new above INFO. Two
> notes for DGD, one of them copy.

---

## What was exercised

| Step | Offline, impostor on localhost | Online, via proxy |
|---|---|---|
| Cold start, arcade never opened | 0 requests | stats fetch to `digitalgold.co` only |
| Arcade → Coin Quest → level 1 sheet → board (coach tip shown) | 0 requests, no crash | — |
| Back out to the ticker | ticker intact | — |
| Deep link `https://digitalgold.co/app/<script>…?ref='"><img…&x=A×400` | handled, no crash, ticker shown | — |
| Signup preview: username, email, password entered | — | 0 requests |
| Continue → "Check your email" step, Resend, step 3 | — | 0 requests |
| At rest, after all of it | see below | see below |

## Verified

- **RC1 stays closed** (`HOLDS`). With the impostor answering `localhost:8787`,
  the impostor log is empty across cold start, opening the arcade, opening
  Coin Quest, the level sheet and the board. Nothing identity-shaped is
  written: after a level the arcade's only preference is
  `flutter.cq.coach.basics=true`.
- **Egress is one host.** Behind the proxy, the app's only remote endpoint is
  `15.204.87.31:443`, which is `digitalgold.co`, confirmed both in the proxy
  log and by a socket owned by the app's uid (`10209`). Every other line in
  the proxy log is Google system traffic: the connectivity check, FCM on
  port 5228, and one `googleusercontent.com` address that appeared while the
  keyboard was up. None of those hosts is in the app's binaries; the earlier
  static pass found only `digitalgold.co`, `play.google.com` and
  `apps.apple.com` in the dex and nothing in `libapp.so`.
- **The password stays encrypted.** After filling the form, `dgd.signup.xml`
  holds `dgd.username` and `dgd.email` in plaintext, exactly as
  `SignupPreferences.kt` documents; `dgd.signup.secure.xml` holds one
  AES-SIV-encrypted key with an AES-GCM value. A recursive search of the
  app's private storage finds the username and email in that one file and
  the password nowhere.
- **The signup preview sends nothing.** Zero proxy lines from the app during
  entry, Continue, and the verification step.
- **Hostile deep link.** The exported `MainActivity` takes the
  `digitalgold.co/app` intent with a script-tag path, quote-laden query and a
  400-character parameter without crashing; the ticker renders.
- **No crashes** in either phase. Static: RC3 (`versionName 1.0.0`,
  `versionCode 1`) and RC4 (32-bit x86 declared without an engine) are
  unchanged; debug flags as before.

## Notes

### V1. INFO — the verification step asserts an email that was not sent
The screen is headed **PREVIEW · NOT LIVE** and its accessibility label reads
"Demo only. This app does not send email." Below that the body copy says
*"We sent a verification code to redteam@example.edu. Enter it below to
continue. Didn't get it? Check your spam or junk folder…"*, with a Resend
link. Nothing was sent; the proxy is silent. The header is the mitigation,
and for a screen reader the label is unambiguous, but a sighted user reads
a sentence in the past tense about an action that did not happen and is
told where to look for it. A copy decision for DGD, and one to settle before
store review reads the same screen: "In the live app a code would be sent
to …" says the same thing without asserting it.

### V2. INFO — the email address is at rest in plaintext, under backup
Pre-existing and documented: username and email are ordinary
`SharedPreferences`, only the password is encrypted, and the host manifest
has `allowBackup="true"`. The email is personal data that will ride along in
device backups. Belongs in `PRIVACY-DRAFT.md`'s data-at-rest list, not in
code.

### Environment, not the app
The emulator host process segfaults (exit 139) when the arcade is opened
while the emulator runs with `-http-proxy`, twice, at the same instant;
without the proxy flag the same build opens the arcade and plays. That is
why the run is in two phases. Anyone reproducing the egress capture should
keep the arcade closed during it.

## Not in scope
No won level, so the app-tab fireworks suppression remains unverified by eye
(RC5). No real backend, so the online arcade path is untested. No iOS.

## How to re-run
```
arcade/tools/redteam.sh --ref main --mirror none --apk arcade/integration/DGD-merged-arcade-v1.0.2-demo-debug.apk

# phase 1, offline + impostor (arcade open is safe here)
emulator -avd dgd_api35 -wipe-data -no-snapshot -no-window -gpu swiftshader_indirect -feature -Vulkan
adb -e shell "svc wifi disable; svc data disable"; python impostor.py 18788 impostor.log; adb -e reverse tcp:8787 tcp:18788
# phase 2, online through the logging proxy (keep the arcade closed)
python egress_proxy.py 18790 egress.log
emulator -avd dgd_api35 -wipe-data -no-snapshot -no-window -gpu swiftshader_indirect -feature -Vulkan -http-proxy http://127.0.0.1:18790
```

*Earlier passes: `AUDIT-RC-2026-09-20.md` (the RC this build replaces).
Run artefacts: `redteam-runs/20260920T235500Z-v1.0.2-7283758/`.*
