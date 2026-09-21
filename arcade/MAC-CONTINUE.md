# Continuing on the Mac — B2

**2026-09-21.** How to move this session to the Mac and finish the iOS work.
`IOS-B2-RUNBOOK.md` says *what* to change; this says how to get there and how
to work together once you have.

---

## Short answer: yes, install Claude Desktop on the Mac

Not because it is nicer, but because of what this particular task is.

Every Swift file waiting on the Mac — `HomeStatsPanel.swift`,
`SpinningCoinView.swift` — was written on Windows with no Xcode and **has never
been compiled**. The runbook says outright to expect the first build to find
something. So the work is not "run these commands"; it is a compile, read the
error, fix, compile loop, probably several rounds, on code I wrote and can
therefore fix fastest.

Relaying that by hand — you paste an error, I send a patch, you apply it, you
paste the next one — works, but it is the slowest possible shape for this job.
With Cowork on the Mac I run `xcodegen`, `xcodebuild`, read the actual
compiler output, and edit the file directly.

Cowork is on all paid plans and installs automatically with Claude Desktop for
macOS; the Universal build covers both Intel and Apple Silicon. It needs
hardware virtualisation, and there is a standalone readiness check on the
download page if you want to confirm the machine before installing.

**You do not need this for B2a alone.** If all you want is the compliance item
and you are comfortable in Xcode, the runbook's §B2a is genuinely a
twenty-minute job by hand. The case for Cowork gets much stronger at B2b, which
is a half-day of Flutter and framework wiring.

---

## 1. Move the code across

Two repositories are involved, and — **this matters** — neither has a git
remote. They exist on this PC and nowhere else:

| Repo | What it is | On the Mac for |
|---|---|---|
| `dgd-native` | DGD's app, Android + Apple | B2a **and** B2b |
| `puzzle-app` | the arcade, v1 | B2b only |

Fresh git bundles of both are waiting for you. A bundle is the whole
repository, all history and tags, in one file — no accounts, no remote, no
network. Same trick `MAC-SETUP.md` used before, but these are current as of
today's commits.

```
C:\src\mac-handoff\dgd-native.bundle    27.3 MB   HEAD 783c6ba, + 2 tags
C:\src\mac-handoff\puzzle-app.bundle    11.6 MB   HEAD 284710d, + v2 branch, 3 tags
```

Both verified with `git bundle verify`. Move them over however is easiest —
USB stick, AirDrop, iCloud, Drive.

### Why not just push to GitHub

You could, and it would be more convenient. But `dgd-native` is DGD's source,
delivered to us — pushing it to a personal account is a disclosure decision,
not a convenience one, and it is yours to make rather than mine. If you do want
a remote, a **private** repo under DGD's own org is the clean version. The
bundle needs no such decision, which is why it is the default here.

### Landing them

```sh
cd ~/src                                    # or wherever you keep work
git clone ~/Downloads/dgd-native.bundle dgd-native
git clone ~/Downloads/puzzle-app.bundle puzzle-app   # B2b only

# The clone leaves the bundle as 'origin' — a file that will not be there
# forever. Drop it so nothing tries to fetch from it later.
cd dgd-native  && git remote remove origin && git log --oneline -3 && cd ..
cd puzzle-app  && git remote remove origin && git log --oneline -3 && cd ..
```

Expect `783c6ba Large screens: cap the content column instead of opting out` at
the top of `dgd-native`, and `284710d` with the same subject on `puzzle-app`.
If you see anything older, the bundle did not copy cleanly — check the file
size before debugging anything else.

The docs — this file, the runbook, the readiness doc — travel separately:
`AmbassadorAI` **does** have a remote, so just clone it.

```sh
git clone https://github.com/thewriterben/AmbassadorAI.git
cd AmbassadorAI && git checkout arcade-redteam
```

---

## 2. What the Mac needs installed

For **B2a** (the compliance item):

| | Check | Notes |
|---|---|---|
| Xcode | `xcodebuild -version` | Open it once so it finishes installing components |
| Command line tools | `xcode-select -p` | |
| Homebrew | `brew --version` | |
| XcodeGen | `xcodegen --version` | `brew install xcodegen` — **required**, the pbxproj is generated |
| An iOS simulator | `xcrun simctl list devices available \| grep iPhone` | The runbook's command names iPhone 16; use whatever you have |

For **B2b** as well:

| | Check | Notes |
|---|---|---|
| Flutter **3.47.2** | `flutter --version` | Must be this version — see `MAC-SETUP.md` §2. The PC is on 3.47.2 / Dart 3.13.2, and a different one resolves different packages |
| Python 3 | `python3 --version` | For `sync_module.py` |
| CocoaPods | — | **Not needed, and deliberately not used.** The runbook explains why: Pods writes into the pbxproj, which `xcodegen generate` then discards |

`MAC-SETUP.md` has the Flutter install in full, including a correction worth
reading: an earlier version of that file wrongly claimed Xcode 27 could not
build Flutter. It can. Do not let the old warning send you down a 15 GB detour.

---

## 3. Starting the session with me

In Cowork on the Mac, connect **two folders**: `~/src/dgd-native` and the
`AmbassadorAI` clone. Add `~/src/puzzle-app` too if you are doing B2b.

Then open with something like:

> Continuing the DGD iOS work from the Windows session. Read
> `arcade/integration/IOS-B2-RUNBOOK.md` and `arcade/MAC-CONTINUE.md` in
> AmbassadorAI, then start on B2a: the deletions, `xcodegen generate`, and get
> it building. `HomeStatsPanel.swift` has never been compiled — expect the
> first build to fail and fix what it finds.

That is enough. The runbook carries the detail, and everything I would need to
know about how we got here is in the readiness doc.

**Do B2a first, and stop there if time is short.** It is the one genuine
consumer-protection finding in Oleksandr's review — a fabricated performance
curve for a financial asset — and it is still shipping on iOS today. B2b is
scope; B2a is the thing that should not wait.

---

## 4. Getting the work back

Whatever the Mac produces has to come home, or the two trees diverge silently —
which is the same class of problem as the `arcade-repo` staleness that cost a
day on 2026-09-20.

Easiest is a bundle in the other direction:

```sh
cd ~/src/dgd-native
git bundle create ~/Desktop/dgd-native-from-mac.bundle --all
```

Back on the PC:

```
cd /d C:\src\dgd-native
git fetch C:\path\to\dgd-native-from-mac.bundle main:mac-work
git log --oneline main..mac-work
git merge mac-work        # or rebase, whichever reads better at the time
```

If instead you decide the **Mac becomes the iOS machine** — a reasonable call,
since it is the only one that can build iOS at all — then say so explicitly and
write it down, so nobody later edits `apple/` on Windows and wonders why it
never compiled.

---

## 5. One thing worth doing regardless

Fifteen commits of `dgd-native` and the entire arcade history exist on **one
disk, with no remote and no backup**. Today's bundles are, right now, the only
second copy. Whatever you decide about GitHub, keep a copy of those two bundles
somewhere that is not this PC.

---

*Related: `arcade/integration/IOS-B2-RUNBOOK.md` (what to change),
`arcade/MAC-SETUP.md` (Flutter and device setup, and the Xcode 27 correction),
`arcade/STORE-READINESS-2026-09-20.md` §5 (why B2 exists).*
