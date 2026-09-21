# v1.0.4 for review — and one correction to an assumption

**2026-09-21.** For Oleksandr, following "DGD App Store Readiness" of
2026-09-20.

| | |
|---|---|
| Build | `DGD-merged-arcade-v1.0.4-demo-debug.apk` |
| sha256 | `e803e800692267ecca882aa41e5334cbf0dcc581ed05d7a1d72f12b47c34a008` |
| Size | 80,821,836 bytes |
| Version | **1.0.4 (4)** — the code is new, per your note that Play never reuses one |
| You reviewed | v1.0.2, sha256 `72837584…` |

Install it on a **wiped** device or run `adb uninstall com.digitalgold.ticker`
first. That matters, for the reason below.

---

## The correction

Your review assessed the signup preview as a finished-looking flow that was
framed as a preview — the PREVIEW · NOT LIVE watermarks, the "creates
accounts, so it needs in-app deletion" point, the Apple 4.2 / 2.1 risk. All of
that stands. But it rested on an assumption none of us had tested:

**A new user could not complete the signup preview at all.**

On a fresh install, pressing Verify — or the keyboard's Go key — on the email
verification step returned the user to Credentials, silently discarded the
code they had just typed, and left Wallet and Receive locked. There was no
path past step 1 for any account that had not already completed the flow once.

The cause was one function doing two incompatible jobs:

```kotlin
awaitingEmailVerification = false
verificationCode = ""
moveToStep(2)          // silently refuses
```

`moveToStep` asks `isSignupStepUnlocked`, which answers "has the user already
reached this step?" A fresh install has `signupMaxReached = 1`, so for step 2
the question is `2 <= 1` and the answer is no. **Forward progress was gated by
a ceiling that only forward progress could raise.** `moveToStep` returns
`Unit`, so the refusal was invisible — and the caller had already thrown away
the verification state believing it had worked.

It is now split: `moveToStep` still guards the step pills, and a new
`advanceToStep` raises the ceiling. `handlePrimary` advances *before* it
clears, so a future refusal does nothing rather than destroying state. A unit
test pins the invariant.

Two more on the same step, both fixed:

- The primary button sat below the keyboard and the sheet did not scroll it
  into view, so the step showed a code field and no visible way to submit.
  This is also why our 21 Sept red-team automation never reached Verify and
  logged it as "not reached".
- Back with the keyboard up cleared the code. Same root cause.

**Why it survived every previous check.** Every manual walk was done on a
device that had already completed the preview once, which sets
`membershipPreviewCompleted` and opens the gate permanently. The defect is
invisible unless the install is wiped. Our own audit saw the symptom twice —
logged as O1 and O2, "observed once, not reproduced" — and read it as a flaky
IME quirk rather than one deterministic blocker.

Verified on a wiped Pixel against this exact artefact: Credentials → Verify →
**Wallet** → **Receive**, no crashes. Wallet and Receive had never been
reached by an automated run.

## What else changed since the build you reviewed

| Your item | State |
|---|---|
| targetSdk 35, Play requires 36 | **done** — 36, retested on a wiped Android 16 emulator (S2) |
| Illustrative financial figures shown as performance | **done on Android** — the generated series is deleted; the panel shows the live snapshot and its source. **iOS still draws the chart** (S5) |
| Version 1.0.0 (1) under a v1.0.2 filename | **done** — now 1.0.4 (4) (S6) |
| 32-bit x86 declared with no engine | **done** before your review arrived |
| Arcade preferences in cloud backup | **done** — excluded from backup and transfer (W1) |

## What is still open, and whose it is

**Yours, and still ahead of everything else:** the admin Swagger credential
and the public `/api/doki/` endpoint (§0 of our reconciliation). Nothing here
has touched that host — our red-team policy forbids traffic to it — and a
defensive scan found no such credential anywhere in our repos.

**Yours, and gating the rest:** the Path A / B / C decision. We have assumed
**B with the arcade kept in the binary, Finance category** for planning
purposes. Under B the signup flow above stops being a preview and becomes the
product, which is why its being broken mattered more than its framing.

**Ours, waiting on artefacts only DGD can create:** release keystore and
Apple Distribution certificate (S1), the real App Store ID to replace
`id0000000000` (S3), and `assetlinks.json` with the release certificate's
SHA-256 (S7, gated on S1).

**Ours, in progress:** the iOS half of S5 and the arcade's iOS embed (B2), the
first minified release build, and Compose UI tests — the app currently has no
instrumented tests at all, which is precisely why a first-run blocker on the
main flow could live this long.

*Full detail: `STORE-READINESS-2026-09-20.md` (§5 is the Path B residue),
`AUDIT-v1.0.3-2026-09-21.md`, `INTEGRATION.md`.*
