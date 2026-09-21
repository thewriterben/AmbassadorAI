# Continuing on the Mac — B2a

**2026-09-21.** How to move the iOS work to the Mac and finish B2a.
`IOS-B2-RUNBOOK.md` says *what* to change; this says how to get there.

---

## Decisions taken, 2026-09-21

Recorded here so nobody re-opens them later:

| | Decision |
|---|---|
| **Remotes** | `dgd-native` and `puzzle-app` stay **local and private**. No GitHub until DGD's company org is ready. Transfer by git bundle. |
| **B2a** | **Benji, on the Mac**, with Claude running on that machine. It is copy-and-paste plus a compile-fix loop. |
| **B2b — the iOS arcade** | **Deferred.** Not until this version has been reviewed and the backend is being wired in. |
| **Priority** | Launch. Anything that does not move a store submission forward waits. |

That makes this document a B2a run sheet. B2b's instructions still stand in
the runbook for when it comes back around; nothing below depends on them.

---

## 1. Move the code across

`dgd-native` has **no git remote** — it exists on the PC and nowhere else. A
fresh bundle is waiting. A bundle is the whole repository, all history and
tags, in one file: no accounts, no remote, no network, which is exactly what
the decision above calls for.

```
F:\Documents\dgdappsource\mac-handoff\dgd-native.bundle   27.3 MB   HEAD 783c6ba, + 2 tags
```

`puzzle-app.bundle` is beside it, but **you do not need it for B2a** — that is
the arcade, and the arcade is B2b. Leave it.

There is a `READ-ME-FIRST.md` in that folder with the same clone commands, so
the handoff stands on its own if it gets copied to a USB stick without this
file. (The originals were written to `C:\src\mac-handoff\`, which is outside
the connected folders and therefore invisible from Cowork — `dgdappsource` is
the copy to use.)

Move the file over however is easiest — USB stick, AirDrop, iCloud. Then:

```sh
cd ~/src                                   # or wherever you keep work
git clone ~/Downloads/dgd-native.bundle dgd-native
cd dgd-native

# The clone leaves the bundle as 'origin' — a file that will not be there
# forever, and we are deliberately not adding a real remote yet.
git remote remove origin
git log --oneline -3
```

Expect `783c6ba Large screens: cap the content column instead of opting out`
at the top. Anything older means the bundle did not copy cleanly — check the
file size before debugging anything else.

The docs travel separately. `AmbassadorAI` does have a remote:

```sh
git clone https://github.com/thewriterben/AmbassadorAI.git
cd AmbassadorAI && git checkout arcade-redteam
```

---

## 2. What the Mac needs

B2a only — no Flutter, no CocoaPods, no Python.

| | Check | If missing |
|---|---|---|
| Xcode | `xcodebuild -version` | Open it once so it finishes installing components |
| Command line tools | `xcode-select -p` | `xcode-select --install` |
| Homebrew | `brew --version` | brew.sh |
| **XcodeGen** | `xcodegen --version` | `brew install xcodegen` |
| A simulator | `xcrun simctl list devices available \| grep iPhone` | Any iPhone will do |

XcodeGen is the one that is genuinely required rather than merely convenient.
`DigitalGoldTicker.xcodeproj` is **generated** from `project.yml`, and B2a
deletes two files the current pbxproj still lists. Editing the pbxproj by hand
works until the next `xcodegen generate` throws the edit away.

---

## 3. What to tell Claude on the Mac

Connect two folders: `~/src/dgd-native` and the `AmbassadorAI` clone. Then
open with something close to this:

> Continuing DGD iOS work from a Windows session. Read
> `arcade/integration/IOS-B2-RUNBOOK.md` and `arcade/MAC-CONTINUE.md` in the
> AmbassadorAI folder, then do **B2a only** — B2b is deferred.
>
> B2a removes a synthetic stats chart from the iOS app. `HomeStatsPanel.swift`
> has already been rewritten but **has never been compiled** — it was written
> on a machine with no Xcode. Expect the first build to fail and fix what it
> finds. The deletions, the hand-edits and the two greps that define "done"
> are all in the runbook.
>
> The project is XcodeGen output, so run `xcodegen generate` after the
> deletions rather than editing the pbxproj.

Two things worth pasting in as well, because they are the traps:

- **`SpinningCoinView.swift` is also uncompiled** and is not part of B2a. If
  it breaks the build, delete it and restore `Image("DGDCoin")` in
  `TickerView.swift` — details in `COIN-AND-ICON.md`. Do not spend B2a's hour
  debugging a coin animation.
- **Do not add CocoaPods.** Nothing in B2a needs it, and it writes into the
  generated pbxproj.

---

## 4. What "done" looks like

From the runbook, unchanged:

```sh
grep -rn "Illustrative" apple/          # must return nothing
grep -rn "PreviewStatsSeries" apple/    # must return nothing outside git history
```

And on the simulator: open Stats, see three figures — Accounts, Price, Market
cap — and one line reading *"Live figures from digitalgold.co, updated
HH:MM."* No chart, no timeframe pills, no motion.

Android lost fourteen tests when it made this change (106 → 92), and all
fourteen tested the generator. If iOS loses a similar number, that is correct,
not a regression.

---

## 5. Getting the work back

The two trees must not drift. When B2a is done:

```sh
cd ~/src/dgd-native
git bundle create ~/Desktop/dgd-native-from-mac.bundle --all
```

Back on the PC:

```
cd /d C:\src\dgd-native
git fetch C:\path\to\dgd-native-from-mac.bundle main:mac-work
git log --oneline main..mac-work
git merge mac-work
```

Alternatively, declare the **Mac the iOS machine** — reasonable, since it is
the only one that can build iOS at all — and write that down, so nobody later
edits `apple/` on Windows and wonders why it never compiled.

---

## 6. Backups, since there is no remote

Keeping the repos private is the right call, but it means `dgd-native`'s
fifteen commits and the whole arcade history sit on **one disk**. The bundles
are currently the only second copy. Keep them somewhere that is not the PC —
that is a backup, not a remote, and it does not pre-empt the company GitHub
decision.

---

*Related: `arcade/integration/IOS-B2-RUNBOOK.md` (what to change, including
B2b for later), `arcade/MAC-SETUP.md` (Flutter and device setup — B2b only,
and note its Xcode 27 correction), `arcade/STORE-READINESS-2026-09-20.md` §5.*
