# iOS captures for the v1.0.5 review package

**2026-09-21.** Short Mac task. The review package covers both platforms;
Android is built and captured here, iOS cannot be, so these six screenshots
are the gap.

Nothing to change. Build what is already in `main` after `2948702` and
photograph it.

## Setup

```sh
cd ~/src/dgd-native
git fetch <the refreshed bundle> main:mac-work && git merge --ff-only mac-work
cd apple
xcodegen generate
open DigitalGoldTicker.xcodeproj
```

Run on an **iPhone 16 Pro** simulator if you have one — it matches the App
Store 6.7" screenshot slot, so these double as a first cut at store assets.
Any modern iPhone is fine otherwise; just say which in the filename.

Capture with `Cmd+S` in the simulator, or:

```sh
xcrun simctl io booted screenshot ~/Desktop/ios-01-ticker.png
```

## The six

| # | Screen | How to get there | What it must show |
|---|---|---|---|
| 1 | Ticker home, guest | Launch, let the count-up finish | Coin, price to five decimals, Accounts / Market cap, **Stats** above **Get Digital Gold**, **Log in** top-right |
| 2 | **Stats expanded** | Tap **Stats** | Three live figures and the line *"Live figures from digitalgold.co, updated HH:MM."* **No chart, no timeframe pills, no percent captions.** This is the B2a evidence — the most important frame in the set |
| 3 | Signup step 1 | Tap **Get Digital Gold** | **PREVIEW · NOT LIVE**, *Join the Digital Gold Ecosystem*, the three step pills |
| 4 | Email verification | Fill the three fields → Continue | The demo code screen, and its present-tense "in the live app" wording |
| 5 | Receive + Invite | Any code → Verify → through Wallet → Receive | **Receive on your desktop wallet**, and Invite Friends with **no dollar amounts anywhere** |
| 6 | Logged-in home | **Finish** | CTA is **My Membership**, **Log in** is gone |

Frame 2 is the one to check twice. If any chart, pill or percentage is still
on screen, stop and say so — it would mean the build is not the merged one.

## Two things that will not be there, and should not be

- **No Arcade button.** B2b is deferred; the arcade is Android-only for now.
  iOS has no second entry point on the ticker home.
- **No spinning coin**, if `SpinningCoinView` was left out of the header. It
  compiled, but it is cosmetic and not part of B2a.

Say which of those you see, either way — the package needs to state the iOS
gap accurately rather than guess at it.

## One small fix while you are there — `apple/stats-source.json`

Android's copy of this file was trimmed today (red-team F2). The iOS copy
still carries the full version, and it is the same problem: ~8 KB of API
investigation shipped inside the product, of which the app reads three fields.

What it currently discloses to anyone who unpacks the `.ipa`: five endpoints
rather than one, which of them 404s, the note that **a foreign `Origin` header
returns HTTP 500**, and `digitalgoldx.com`.

Replace it with `android/app/src/main/assets/stats-source.json` from the same
commit (`bc8c614`) — the two are meant to be the same contract, and the Swift
decoder reads the same three keys. Check `StatsEndpoint.swift` agrees before
building.

Safe: the decoder falls back to the hardcoded `published` endpoint if the file
is missing or unparseable, so a bad edit degrades to the default rather than
breaking the ticker.

## Send back

The six PNGs, and one line for each of: Xcode version, simulator device, iOS
version. Drop them beside the bundle in `mac-handoff/` and they will be folded
into `RELEASE-CANDIDATE-1.0.5.md`.

No bundle needed on the way back unless you changed something — captures are
not commits.
