# Arcade versions

Two versions exist and they do not touch each other.

| | **v1** | **v2** |
|---|---|---|
| What | Coin Quest and the Explorer track | Coin Quest plus the new catalogue, starting with Passage |
| Status | **Frozen.** Merge candidate for the main DGD app | In development |
| Version | `1.0.0+100` | `2.0.0+200` |
| Branch | `main` | `v2/ten-games` |
| App folder | `C:\src\puzzle-app` | `C:\src\puzzle-app-v2` |
| Server folder | `C:\src\arcade-server` | `C:\src\arcade-server-v2` |
| Repo mirror | `arcade/v1/` | `arcade/v2/` |
| Build scripts | `arcade/v1/*.cmd` | `arcade/v2/*.cmd` |
| Artefacts | `arcade/v1/dist/` | `arcade/v2/dist/` |
| Tag | `v1.0.0` in both repos | untagged until it ships |

## The one rule

**Nothing from v2 goes into v1.** v1 is what gets merged into the main DGD
app; it was soak-tested at 6000/6000 and is the version the compliance
answers, the store listing and the privacy draft describe. A change that
lands in it silently invalidates all of that.

Fixes travel **v1 → v2 only**:

```
cd C:\src\puzzle-app-v2
git merge main
```

Never the reverse, and never `git merge v2/ten-games` from `main`.

## Why worktrees rather than branches

The two folders are [git worktrees](https://git-scm.com/docs/git-worktree) of
the same repository: one history, two checkouts, each pinned to its own
branch. That buys the thing branches alone do not — **a session working in
`C:\src\puzzle-app-v2` cannot edit a v1 file, because the v1 files are not
there.** No `git checkout` to forget.

Two further guards, in order of how likely they are to matter:

1. **The build scripts live next to the version they build** and each one
   hard-codes its source folder. `arcade\v2\devbuild.cmd` builds
   `C:\src\puzzle-app-v2` and nothing else.
2. **Each script checks the branch before it builds** and refuses if it is
   wrong. This only fires if someone has manually checked out the other
   branch in a worktree, which git already resists.

## Starting a v2 session

Point the working folder at `C:\src\puzzle-app-v2` (and
`C:\src\arcade-server-v2` if the backend is in scope). Then say what you are
doing — for instance *"continue the ten-game catalogue, next game is Assay
Line"* — and give it `arcade/TEN-GAMES.md` as the plan.

Do **not** start a v2 session in `C:\src\puzzle-app`.

## Build numbers

Play rejects an upload whose build number is not higher than the last one,
and it never forgets a number once used. So the bands are reserved up front:

| Version line | Build numbers |
|---|---|
| v1.x | 100–199 |
| v2.x | 200–299 |

v1 can therefore ship ninety-nine patches without ever colliding with v2, and
v2 can be uploaded to a test track at any point without burning a number v1
still needs. Bump within the band on every upload, never reuse.

## If a bug is found in v1

v1 being frozen means "no new features", not "no fixes". A genuine defect:

1. Fix it on `main`, in `C:\src\puzzle-app`.
2. Bump to `1.0.1+101` and tag `v1.0.1`.
3. Rebuild and re-mirror into `arcade/v1/`.
4. Merge `main` into `v2/ten-games` so v2 inherits the fix.
5. Say so in the merge thread — the other team may already be integrating.

## What is in each artefact folder

**`arcade/v1/dist/`**

| File | What |
|---|---|
| `DGD-Arcade-v1.0.0-demo.apk` | Sideload build, Coin Quest only, no backend. The tester build |
| `DGD-Arcade-v1.0.0.bundle` | Complete git history at the `v1.0.0` tag. `git clone` it |
| `DGD-Arcade-v0.1.0-demo.apk` | Kept deliberately: the exact binary testers already have, built before this version scheme existed |
| `DGD-Arcade-v0.1.0-shipcfg.apk` | Same, ship configuration |
| `mac-setup.sh`, `mac-demobuild.sh` | iOS toolchain scripts. See `IOS.md` and `MAC-SETUP.md` |

**`arcade/v2/dist/`**

| File | What |
|---|---|
| `DGD-Arcade-v2.0.0-dev.apk` | DEV build with Passage. Not for anyone outside the team |
| `shots/` | Device screenshots from the Passage build |

## Documentation

The `.md` files at `arcade/` root are shared and mostly describe **v1**,
because v1 is the version going to stores and into the merge: `RELEASE.md`,
`STORE-LISTING.md`, `PRIVACY-DRAFT.md`, `MERGE.md`, `MEETING-BRIEF.md`,
`APK-FINDINGS.md`, `TESTERS.md`, `PLAYTEST.md`, the audits. Their paths were
repointed at `arcade/v1/` when the tree was split.

`TEN-GAMES.md` is the v2 plan. `DGD-Arcade-Plan.md`, `DGD-Arcade-Build.md`
and `REMOVED-GAMES.md` span both.

When v2 gets its own release and store material, those documents fork; until
then, one copy describing v1 is correct and duplicating them early would
guarantee they drift.

## Still open, and not version-specific

The release keystore, the hosted backend and its real `ARCADE_SECRET`, and
the compliance sign-offs all belong to DGD rather than to a version. They
block v1 shipping and they will block v2 shipping too. `RELEASE.md` and
`MEETING-BRIEF.md` track them.

---

*Established 2026-09-20, when Passage made v1 and v2 genuinely different
products rather than two points on one line.*
