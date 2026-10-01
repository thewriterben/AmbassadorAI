# DGD App 2.1.0 (live arcade): release candidate, NOT FOR UPLOAD YET

**2026-09-30. Status: built and checked, waiting on the server.** This is
the first DGD App whose arcade talks to a server, at
`https://arcade-api.digitalgold.co`. That host does not exist yet. Until
backend has it up and `smoke.mjs` passes against it, **2.0.0 rc2 (demo) is
the build to ship** (`RC-2.0.0-2026-09-30.md`).

## Artefacts

These are in `C:\src\dgd-native\android\dist-2.1.0-rc1\`, built from
dgd-native `dgd-2.1-live` at `89d1e38`. That branch comes off `dgd-2.0`
at `ab23aef` (2.0.0 rc2), so the demo line stays as it is.

| File | Bytes | SHA-256 |
|---|---|---|
| `DigitalGold-2.1.0-unsigned.aab` | 64,862,492 | `1D989C6F9753D9B0E3A81B497ED2E194DA2933FC3B99C6A39AA29EBBB75F1910` |
| `DigitalGold-2.1.0-review.apk` | 72,489,833 | `12720E6AC6D18AD132480CE4DCA275824FD7DCD11500784B7B8F72602A1D6531` |

The release is version 2.1.0, versionCode 210. That leaves 201–209 for any
2.0.x demo fix.

**The arcade embed** is puzzle-app v2 at `ef16aa6`, built in the clean room
with `DGD_APP_TAB=true` and `ARCADE_API=https://arcade-api.digitalgold.co`,
and no `DGD_DEMO`. Builds A and B came out identical. `ARCADE-PROVENANCE.md`
is next to the AAB.

**The checks behind it:**

- **The native half reproduces in the clean room,** offline: 784 of 788 entries are identical. The 4 that differ are the same as in 2.0.0 rc2: R8 metadata, and two service files that differ only in line endings. Evidence: `redteam-runs/20261001T0455Z-dgd2.1.0-rc1-native-89d1e38/`.
- 95 unit tests and lint pass.
- The red-team runner passes 11 of 11 at AmbassadorAI `7a0998d`: the server's 39 tests, plus 187 plain, 196 loopback and 187 demo arcade tests.

## What changes from 2.0.0

**For the player:**

- **XP and levels,** the weekly standings (recognition only), an assigned
  leaderboard name, When Pigs Fly's growth and its ability shop.
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

> Coin Quest and When Pigs Fly now save your progress online. Collect XP,
> see the weekly standings, and grow your boar to unlock abilities. XP and
> points have no monetary value.

**Notes for the reviewer.** Keep the 2.0.0 note about "DGD Arcade for Web",
and replace the in-app arcade paragraph with this:

> **The in-app arcade** (Coin Quest, When Pigs Fly) is educational. The first
> time it is opened, it creates an anonymous play record on DGD's arcade
> server (arcade-api.digitalgold.co), with no name, email or login. XP,
> points, badges and the weekly standings are recognition only: they have no
> monetary value, cannot be exchanged or withdrawn, and no prize attaches to
> any rank. This server is separate from DGD Arcade for Web. Nothing done in
> the app counts there, and the web arcade's rewards are not offered,
> described or tracked in the app. Players can delete their record in the
> arcade's Settings.
