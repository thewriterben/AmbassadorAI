# DGD App 2.1.0 (live arcade): release candidate rc3, NOT FOR UPLOAD YET

**2026-09-30. Status: built and checked, waiting on the server.** This is
the first DGD App whose arcade talks to a server, at
`https://arcade-api.digitalgold.co`. That host does not exist yet. Until
backend has it up and `smoke.mjs` passes against it, **2.0.0 rc3 (demo) is
the build to ship** (`RC-2.0.0-2026-09-30.md`).

## Artefacts

These are in `C:\src\dgd-native\android\dist-2.1.0-rc3\`, built from
dgd-native `dgd-2.1-live` at `f1c1f43`. That branch carries the live-only
changes on top of the 2.0 line, so the demo line stays as it is. The earlier
candidates are superseded:

- **rc2** (`dist-2.1.0-rc2`, `2791096`) has the old name.
- **rc1** (`dist-2.1.0-rc1`, `89d1e38`) also has L3 and L4 below.

| File | Bytes | SHA-256 |
|---|---|---|
| `DigitalGold-2.1.0-unsigned.aab` | 64,866,179 | `4F2D23E121E290D1D85B411F62D988F4AAD9BCF3063F5A32004B0EB9EF8B2F45` |
| `DigitalGold-2.1.0-review.apk` | 72,492,005 | `B2804B139D2EBF92CCB2659C3986FBEF7F80C0747DD09C433CF62D3152E45617` |

**rc3 changes one thing from rc2:** the game is "Coin Quest: DGD" in titles
and on buttons, as in 2.0.0 rc3.

The release is version 2.1.0, versionCode 210. That leaves 201–209 for any
2.0.x demo fix.

**The arcade embed** is puzzle-app v2 at `85e621c` (the same commit as 2.0.0 rc3), built in the clean room
with `DGD_APP_TAB=true` and `ARCADE_API=https://arcade-api.digitalgold.co`,
and no `DGD_DEMO`. Builds A and B came out identical. `ARCADE-PROVENANCE.md`
is next to the AAB.

**The checks behind it:**

- **The native half reproduces in the clean room,** offline: 785 of 789 entries are identical. The 4 that differ are the same as in every earlier pass: R8 metadata, and two service files that differ only in line endings. Evidence: `redteam-runs/20261001T1727Z-dgd2.1.0-rc3-native-f1c1f43/`.
- 97 unit tests and lint pass. `ArcadeLiveFlagTest` pins the standings row's flag to the embed.
- The red-team runner passes 11 of 11 at AmbassadorAI `e65c347`: the server's 39 tests, plus 190 plain, 201 loopback and 190 demo arcade tests.

## What changes from 2.0.0

**For the player:**

- **XP and levels,** an assigned leaderboard name, When Pigs Fly's growth and
  its ability shop.
- **The weekly standings** (recognition only), from a new "Weekly standings"
  row on the Arcade tab, under the game cards. The row appears only when the
  embedded arcade was built against a server, so the 2.0 demo tab is as
  designed.
- **Delete my play record** in the arcade's Settings.

**Underneath:**

- **The first time a player opens the arcade,** it registers an anonymous
  record on `arcade-api.digitalgold.co`. From then on it reports each round,
  and fetches progress and the standings.
- **Nothing is sent before then.** A network capture on the emulator found no
  lookup of `arcade-api.digitalgold.co` while the app sat on Home and the
  Arcade tab. The lookups came only after Coin Quest was opened (finding L1).
- **The ticker is unchanged.** It still makes the same one request.

## Findings fixed on the way to this build

| | What | Fix |
|---|---|---|
| L1 | The app warms the arcade engine at every launch, and the arcade loaded server progress in `main()`. So every DGD App user would have been registered and would have called the server on each launch, even with no game ever opened. Players behind a carrier's shared address would also have hit the 10-signups-an-hour limit. | Inside the app, the server load runs on the first open only (`ArcadeEntry.onFirstOpen`, `8a613c1`), with a test. Confirmed by the network capture above. |
| L2 | With the server unreachable, When Pigs Fly showed a new piglet as "Fully grown", with a full bar. | Growth shows only once a figure has arrived, and until then the card says it waits for the server (`ef16aa6`), with a test. |
| E6 | The grow-up moment (white flash, sparkles, fanfare) wasn't gated for the app. Only a server makes it reachable. | It is calm inside the app (`cd52381`), with tests. |
| R12 | Deleting the play record also resets the boar's growth and abilities, and the wording didn't say so. | The dialog and blurb now name them (`7471447`). |
| — | `Progress.load()` notified mid-build when called again from the level map. | It always completes asynchronously (`8a613c1`). |
| L3 | The app had no way to reach the weekly standings (see below). | A "Weekly standings" row on the Arcade tab, opening the redrawn standings screen (`d70534a`, `2791096`). |
| L4 | After "Delete my play record", play was silently unrecorded until the next cold start (see below). | Rounds register when there is no identity (`d70534a`), with tests. |

## With the server not up (checked on the emulator)

- The ticker works as before.
- Coin Quest plays, with progress kept on the phone.
- When Pigs Fly flies. The card and the shop both say they wait for the server.
- Settings shows the anonymous record as empty. "Delete my play record" says it could not reach the server, so nothing was deleted.
- Nothing crashes. Each refresh is one attempt with an 8-second timeout, and there is no retry loop.

## Before this can go to DGD to sign

1. **Backend:** `arcade-api.digitalgold.co` is up with a real `ARCADE_SECRET`,
   separate from the web arcade's rewards server, and `node smoke.mjs
   https://arcade-api.digitalgold.co` passes (`backend-package/`).
2. **Us:** run the app end to end against it on the emulator and on a phone:
   - registration on first open;
   - a Coin Quest level claimed after its 15 s minimum;
   - a flight;
   - the shop and the loadout;
   - the standings;
   - deletion.

   Then re-run the runner and record it here.
3. **DGD:**
   - approve the privacy policy section and the new Data safety answers
     (`PRIVACY-DRAFT.md`, "DGD App 2.1.0");
   - decide retention;
   - check the reviewer notes below.

## Play Console text (draft)

**What's new (en-US).** It avoids "earn", "reward" and "win", as the arcade's
own copy does:

> Coin Quest: DGD and When Pigs Fly now save your progress online. Collect XP,
> see the weekly standings, and grow your boar to unlock abilities. XP and
> points have no monetary value.

**Notes for the reviewer.** Keep the 2.0.0 note about "DGD Arcade for Web",
and replace the in-app arcade paragraph with this:

> **The in-app arcade** (Coin Quest: DGD, When Pigs Fly) is educational. The first
> time it is opened, it creates an anonymous play record on DGD's arcade
> server (arcade-api.digitalgold.co), with no name, email or login. XP,
> points, badges and the weekly standings are recognition only: they have no
> monetary value, cannot be exchanged or withdrawn, and no prize attaches to
> any rank. This server is separate from DGD Arcade for Web. Nothing done in
> the app counts there, and the web arcade's rewards are not offered,
> described or tracked in the app. Players can delete their record in the
> arcade's Settings.

## Rehearsal against a local server (2026-09-30)

This was a dress rehearsal of the go-live, before `arcade-api.digitalgold.co`
exists. The setup:

- **The server:** the arcade server ran on this machine in production mode,
  with a throwaway secret held in memory only and a named `ARCADE_CORS`. For
  the rehearsal its growth thresholds were 150 and 400, so one flight could
  grow the boar. `smoke.mjs` passed against it.
- **The app:** the standalone arcade, built in release mode with the dev menu
  and `ARCADE_API=http://10.0.2.2:8787`, on the API 36 emulator.
- **One difference from the shipping build:** the standalone arcade loads at
  startup rather than on first open. The first-open path was checked
  separately, with the network capture on the real 2.1.0 build.

Every step was checked against the server's own database.

| # | Step | Server saw | Result |
|---|---|---|---|
| 1 | First launch | one player, `device_hint` `android`, assigned handle | pass |
| 2 | Coin Quest level 1, won with 3 stars after the 15 s minimum | round: 3 stars, level 1, claimed 34 s after opening; **80 XP** (3 × 20 + 20) | pass |
| 3 | When Pigs Fly, a full passage on autopilot | 2 stars, 9 eras, score 692, **60 XP** (24 + 24 + capped 12); 693 points credited; the boar grew to razorback, shown on the result sheet | pass |
| 4 | Shop: unlock Dash (600) | points 693 → 93; Dash level 1; loadout `["dash"]` (the app equips a first ability itself) | pass |
| 5 | A flight carrying Dash | loadout accepted and recorded, paid in full (60 XP, 937 points) | pass |
| 6 | Weekly standings, then a new name | rank 1, **236 XP**, which matches every round above; re-roll stored, 1 used | pass |
| 7 | Settings → Delete my play record | every table emptied; the dialog names the boar's growth | pass |
| 8 | Keep playing after deleting | **nothing recorded, no new player** | **fail → L4, fixed** |

### L4: after a delete, play was silently unrecorded (fixed)

**What happened:** `startMini`, which opens a round, never registered a
player. Only the startup refresh did. So after a deletion, or any 401, every
round went out with no token and was refused, and the run was quietly
treated as offline. That lasted until the next cold start, which in the DGD
App means the next launch plus opening the arcade. The delete dialog
promises a new record.

**The fix:** `startMini` now registers when there is no identity, and retries
once with a fresh registration after a 401, as `refresh` does.

**Tests:** two loopback tests, both of which fail against the old code. On
the emulator, after a delete in the same session, the next flight registered
a fresh player and its round was recorded at 12 XP. The When Pigs Fly line
before any growth arrives now reads "Growth shows here after a flight with
the arcade server reachable.", which is true in both cases: offline from the
start, and just deleted.

### L3: the standings were not reachable inside the DGD app (fixed in rc2)

**What happened:** DGD App 2.x opens the arcade straight into Coin Quest,
When Pigs Fly or Settings. The XP bar and the weekly standings lived on the
arcade's own home screen, which the app never opens. So in rc1 the standings
could not be reached at all.

**The decision (owner, 30 Sep):** a row on the Arcade tab. The fix has three
parts.

**Native:**

- A "Weekly standings" row under the game cards, styled like the other
  rows, with a podium icon drawn in the same stroke style.
- It opens a new `standings` destination.
- It shows only when `BuildConfig.ARCADE_LIVE` is set. The build sets that
  from the embed's own `PROVENANCE.md` (`ARCADE_API`, and no `DGD_DEMO`), so
  the row can never appear over a demo embed, and a test pins the flag to it.

**Arcade:**

- The standings screen is redrawn in the 30 Sep design system: the header
  with the reset countdown, your name and your week with "New name", and
  plain ranks.
- The gold, silver and rose coin medals for the top three are gone. They are
  prize imagery, on a board that pays nothing.
- The v1 copy (Expeditions, the Daily Ledger) is gone.
- Back leaves to the app, because the screen is the whole stack when the app
  opens it.

**Checked:**

- On the emulator, rc2's Arcade tab shows the row, and the row opens the
  standings.
- With the server not up, the standings say plainly that they are kept on
  the server, and offer to try again.
- Against the local production-mode server, with five players, the screen
  ranks ties correctly and picks out your own row.
