# DGD Arcade — internal demo

Send this note with `dist/DGD-Arcade-demo.apk`.

---

## Installing

Android only, and it installs by hand rather than through the Play Store — we
are not on Play yet.

1. Download the `.apk` on the phone (email, Drive, Slack, whatever reaches
   them).
2. Tap it. Android will ask permission to install from that app the first time;
   allow it, then tap the file again.
3. Play Protect will warn that the app is from an unknown developer. That is
   expected — this build is signed with a development key, not DGD's. Choose
   **Install anyway**.
4. It appears as **DGD Arcade**, a gold coin icon.

To remove it: long-press the icon → Uninstall. Nothing is left behind.

## What is in this build

**Coin Quest: Digital Gold** — a 60-level match-3 across six worlds, and
nothing else. That is the whole app right now, not a trimmed-down demo: the
earlier games were removed in September while a new set of ten is built, so
Coin Quest is the one we want eyes on.

The weekly standings are hidden too. They need our server, which is not hosted
yet.

## What it does with data

Nothing leaves the phone. This build has no server behind it, no sign-in, no
account, and no analytics. Progress lives on the device and goes away with the
app.

## What we want to hear about

In rough order of usefulness:

1. **Anything that crashes, freezes, or looks broken.** Say which level and
   what you were doing. A screenshot or screen recording is worth a lot.
2. **Sound.** Does it stay healthy over a long session, or do effects start
   lagging and then stop? This is the one we most want a second opinion on.
3. **Difficulty.** Which level first made you want to put it down? Which felt
   too easy to bother with?
4. **Anything confusing** — a goal you could not work out, a button that did
   not do what you expected, text you had to read twice.

Not useful yet: the missing games, the missing leaderboard, or anything about
signing in. We know.

## Known and expected

- **Play Protect warning on install** — see above.
- **"PROOF OF PLAY" on the home screen** is aspirational in this build. It
  describes the server-verified scoring that turns on once the backend is
  hosted; nothing is verifying anything here.
- **"More games coming soon"** is a promise about work in progress, not about
  games hidden in this build. Ten new ones are being built.
- XP and badges have no monetary value and are not connected to any wallet,
  exchange, or trading function. The footer says so in the app.

## Version

`co.digitalgold.arcade` 0.1.0 (1). Built 2026-09-16, ~55 MB.

A new build replaces this one in place and keeps your progress, as long as the
version code goes up. If an install ever refuses, uninstall first and reinstall.
