# Android 1.0.6-review — B1 Path A

**2026-09-26.** dgd-native `e8395bb`. APK sha256
`3EBFF75EF7CC9EE597DC6E4C751BF4C71B039D8171196E1E84E251722D076940`,
61,265,307 bytes, versionCode 6, targetSdk 36. Debug-signed review build
(Play refuses it; the in-app version says `1.0.6-review`).

## What changed

The app now carries **no referral surface, in either direction** — the Path A
shape recorded in `B1-DECISION-2026-09-21.md`.

| Removed | Replaced by |
|---|---|
| Friend's-username field on Credentials | nothing — codes are entered on digitalgold.co |
| "Username is your invite code." | "3+ characters, no spaces." |
| "Learn how invites work on digitalgold.co" | "Learn more at digitalgold.co" |
| Copy Invite Link, Copy Invite Code | nothing |
| Per-user QR `digitalgold.co/app?ref=USERNAME` | one QR for everyone, `digitalgold.co/app`, plus "Take a screenshot and text it to a friend" |
| Share message with "Use my invitation code, USERNAME" | Benji's 26 Sep text, identical for every sender |
| App Links on `digitalgold.co/app`; incoming `?ref=` stored in `dgd.friendCode` | no incoming-link handling at all; the stored key is deleted on upgrade |
| `android/invite-handoff/` stubs | deleted |

Two agreed edits to Benji's message: the waitlist is "**at digitalgold.co**"
(it said "in the app", but the app's own line and link both go to the site),
and Android names only the **Play Store** (iOS will name only the App Store,
per App Review 2.3.10). "Predictably-priced, wealth-preserving" is unchanged
and stays flagged for counsel.

## Verification

| Check | Result |
|---|---|
| Unit tests | **92 / 92** |
| Instrumented tests, API 36 emulator | **4 / 4**, including new *Credentials has three fields, not four* |
| `ReferralSurfaceGuardTest` | passes; **proven to fail** when a `?ref=` builder was planted, then reverted |
| Lint (release) | **0 errors**, 42 warnings — all style, none new in kind |
| Static sweep vs 1.0.5 | differs **only** in: VIEW action gone, `autoVerify` gone, the two `?ref=` URLs gone. `dgd.friendCode` survives once in dex, as the key used to delete it |
| Dex strings | `ref=` 0, `invitation code` 0, `invite code` 0, `Copy Invite` 0, `App Store` 0 |
| Upgrade path, emulator | 1.0.5 opened `digitalgold.co/app?ref=testfriend` and stored `testfriend`; after installing 1.0.6 over it and launching, **the key is gone**; the same link now **does not resolve** to the app |
| QR | decodes to exactly `https://digitalgold.co/app` |
| Screenshots | `rc-1.0.6-shots/` — Credentials (no friend field), Invite Friends, the QR with its hint |

**Correction to an earlier note:** the "emulator DNS is broken" finding from
the 1.0.5 pass was the AVD's Wi-Fi and mobile data being switched off.
`svc wifi enable` / `svc data enable` and it resolves and loads live stats.

## Not done here

- **iOS** — `apple/` is Mac-owned. Exact change list:
  `integration/IOS-PATH-A-CHANGE-REQUEST.md`, with `dgd-native-1.0.6.bundle`
  in `mac-handoff/`.
- **Social follow links** — blocked on DGD. The only official profiles in any
  DGD material are `x.com/DigitalGoldOrg` (network updates) and
  `x.com/DigitalGoldTalk`, and the white paper routes referral-recognition
  announcements through the latter, so linking it from the app would point
  users at the programme. No Facebook or LinkedIn URL exists in DGD material.
  DGD to supply the URLs it wants.
- **Real in-app signup** — needs the backend, and App Review 5.1.1(v) then
  requires in-app account deletion.
- **Physical device** — the Pixel wasn't connected; emulator only this pass.
