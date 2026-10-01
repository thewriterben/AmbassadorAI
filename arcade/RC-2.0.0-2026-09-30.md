# DGD App 2.0.0: Android release candidate (rc2)

**2026-09-30.** This is the release record for DGD to sign and upload. It
replaces the Play Console text in `RC-1.0.7-2026-09-29.md` and
`RC-1.0.8-2026-09-29.md`, which describe the old layout: those two stay as the
record of what shipped then.

## Artefacts

**Upload rc2.** It is in `C:\src\dgd-native\android\dist-2.0.0-rc2\`, built from
dgd-native `dgd-2.0` at `ab23aef`.

| File | Bytes | SHA-256 | For |
|---|---|---|---|
| `DigitalGold-2.0.0-unsigned.aab` | 64,736,687 | `954377CAC2D836BDCE840D7AAAA212EDD02BAF82E21F9CC7A3CD0DCCC4D8A685` | Play, once DGD signs it |
| `DigitalGold-2.0.0-review.apk` | 72,260,461 | `74B74BB6A4FEDE528CF900CF39C22FEC756E52435BE57D7D0BF88CBCC517FA92` | Installing and looking. It is debug-signed and says `2.0.0-review` in the app; Play refuses it. |

The release is still version 2.0.0, versionCode 200: rc1 never went to Play.
rc1 (`dist-2.0.0\`, `f04b884`, AAB `FE22CAA1…9594`) is kept as the record. It
has the three findings below that rc2 fixes, so do not upload it.

**The arcade embed** is puzzle-app v2 at `3c4e42d`, built in the clean room in
demo mode (`DGD_APP_TAB=true`, `DGD_DEMO=true`). Builds A and B came out
identical in all 6 AARs. It has no server and makes no requests.
`ARCADE-PROVENANCE.md` is next to the AAB.

**The checks behind rc2:**

- **The native half reproduces in the clean room,** offline: 784 of 788 bundle entries are identical. The 4 that differ are R8's map and `r8.json`, which are build metadata, and two service files that differ only in line endings, CRLF on Windows against LF on Linux. Evidence: `redteam-runs/20261001T0346Z-dgd2.0-rc2-native-ab23aef/`.
- 95 unit tests pass, lint passes, and 4 of 4 instrumented tests pass on the API 36 emulator.
- The red-team runner passes 11 of 11 at `fc0f3f1` (`redteam-runs/20261001T031548Z-fc0f3f1/`). That covers the server's 39 tests, 183 plain, 192 loopback and 184 demo arcade tests, the analyzer, and the host and secret scans.
- The rc1 review is in `AUDIT-DGD2.0-2026-09-30.md`.

**What rc2 changes from rc1:**

- **S1:** light status-bar icons in light mode.
- **S2:** the deep red coin, on the board and on the Arcade tab's card.
- **S3:** the board's frame is no longer clipped at 16:9.
- **R9:** opening a game from the Arcade tab no longer shows the previous game first.
- **Star wording:** "Star N saved" replaces "recorded".

## What changed since 1.0.8

- **A redesign.** The 30 Sep design return replaces the single ticker screen with three tabs on a bottom bar:
  - **Home:** the live price, and *The network*. Its **Stats** button expands the live snapshot in place, with no chart.
  - **Arcade:** the games, and the web link.
  - **Account:** the membership preview, still marked **PREVIEW · NOT LIVE**, with its locked copy unchanged.
- **The Arcade menu is gone.** **DGD Arcade for Web** is now a card on the Arcade tab, below the games. Its wording, URL (`https://digitalgold.co/arcade/`, no parameters) and behaviour (the phone's own browser, through a plain VIEW intent) are unchanged, and `WebArcadeLinkTest` still pins all three. It is still never on a result or level-complete screen.
- **A second game, When Pigs Fly.** You fly a winged piggy bank through nine eras of monetary history and land it. Its screens say "Points and coins have no monetary value."
- **The arcade embed moves from v1 to v2,** in demo mode. Progress is kept on the phone. There are no XP, no standings and no server.
- **New type and icons.** Inter and Geist Mono (OFL), and Hugeicons (MIT). Their licences ship in the app's assets.

**What did not change:**

- The only network request is still the ticker's `GET https://digitalgold.co/api/forms/stats`.
- There is no referral surface. Invite Friends shares the app and nothing else (B1 Path A).
- There are no ads, no analytics and no crash reporter.

## Signing and uploading (DGD)

The upload key is DGD's, and it is not on this machine. With it:

```
jarsigner -keystore <dgd-upload.jks> -sigalg SHA256withRSA -digestalg SHA-256 ^
  DigitalGold-2.0.0-unsigned.aab <upload-key-alias>
jarsigner -verify DigitalGold-2.0.0-unsigned.aab      :: "jar verified."
```

Then go to Play Console → the app → internal testing → create release, and
upload the signed `.aab` from `dist-2.0.0-rc2`. versionCode 200 is higher than
anything uploaded so far (1.0.8 is 8).

## Play Console text

**What's new (en-US)**, 266 characters of the 500 allowed:

> A new look. Home, Arcade and Account now sit on a bar at the bottom of the
> screen. The Arcade tab has Coin Quest and a new game, When Pigs Fly: fly a
> winged piggy bank through nine eras of monetary history and land it. DGD
> Arcade for Web has moved to the Arcade tab.

**Notes for the reviewer** go under App access, or answer any policy query.
The first paragraph is the 1.0.7 text with the new location. The other two
are new.

> **Arcade tab → "DGD Arcade for Web".** Opens https://digitalgold.co/arcade/
> in the phone's default browser. It is DGD's website, free to play for anyone
> without signing in; nothing is sold there and no payment is ever needed to
> take part. Signed-in digitalgold.co account holders may receive DGD, and DGD
> validation credits for Top 100 places, for results the site verifies, under
> official rules published at digitalgold.co/arcade/rules.html (currently in
> test mode: nothing is owed or paid). None of that is offered, described or
> tracked in this app: the link carries no parameters, the site cannot tell
> visitors from the app apart from anyone else, and nothing done in the app
> counts there.
>
> **The in-app arcade** (Coin Quest, When Pigs Fly) is educational and runs
> entirely on the phone in this version: it sends nothing and has no
> accounts. Nothing in it has monetary value, and the Arcade tab and the
> game screens say so.
>
> **Account tab.** A preview of DGD membership, marked PREVIEW · NOT LIVE.
> It creates no account, signs in to nothing, and holds or moves no DGD.

**Check one thing before pasting:** that the Top 100 credits and the rules
page are still as described. They are DGD's facts, last confirmed on 28 Sep.

## Store listing graphics

**The phone screenshots are in `store/dgd-app-2.0/`.** There are six, each
1080 × 1920 (9:16, inside Play's 2:1 limit). They were taken from the rc2
review APK on the API 36 emulator in dark mode, with a clean status bar.

| File | Screen |
|---|---|
| `01-market.png` | Home: the live price |
| `02-arcade.png` | The Arcade tab |
| `03-coin-quest-map.png` | Coin Quest level map |
| `04-coin-quest-level.png` | A level's goal sheet |
| `05-coin-quest-board.png` | The board |
| `06-when-pigs-fly.png` | When Pigs Fly, before a flight |

**Some screens are left out on purpose:**

- **The Account tab.** A "Get Digital Gold" button in a store screenshot puts acquiring the asset first, and the listing should lead with what the app does.
- ***The network* panel.** It leads with market cap.
- **A When Pigs Fly flight.** Its pickup coins are due to be redrawn before public release (review E1).

**The old screenshots are not usable.** `store/screenshots/` is 1080 × 2424,
which is over Play's 2:1 limit, and it shows the standalone DGD Arcade, not
this app.

**These screenshots show rc2 exactly.** Retake them for the build that
connects to the arcade server: the arcade screens gain an XP bar and the
When Pigs Fly shop.

## Data safety

2.0.0 adds no network traffic, and it stores nothing new except arcade
progress on the phone. So the answers given for 1.0.8 stand for this build.
The build that connects to the arcade server changes them:
`backend-package/DATA-AND-PRIVACY.md` lists what it will need.

## Play policy

The reading in `RC-1.0.7-2026-09-29.md` stands. The link is the same link in
a new place. The new game has no prizes, purchases or wagering, and its
points never leave the phone.

## Found while taking the rc1 screenshots: all fixed in rc2

| | What | Fix, and how it was checked |
|---|---|---|
| S1 | **Status bar icons were dark on the dark page** when the phone is in light mode, so the clock and battery were barely visible. `enableEdgeToEdge()` with no arguments follows the system theme and overrode `windowLightStatusBar=false`. The arcade's own screens were unaffected. | dgd-native `MainActivity` (`83119d7`): the system bars are always dark-style. Light icons in light mode on the emulator. |
| S2 | **The Coin Quest red coin was rose pink.** The Arcade tab's card carries its own copy of the art. | Deep red #C21F2C in the arcade (`faa63bf`) and on the card (`83119d7`). Visible in the rc2 screenshots. |
| S3 | **The Coin Quest board's frame was clipped** top and bottom on a 16:9 screen (1080 × 1920). The board's `Stack` clipped the plate's 6 px surround. | Arcade `3c4e42d`: the stack no longer clips. The frame is whole in `05-coin-quest-board.png`. |

**From the rc1 review, also in rc2:**

- **R9.** A warm open showed the last arcade screen sliding away. The screen
  the app asks for is now the arcade's first frame (`3c4e42d`). A screen
  recording of a warm open, with When Pigs Fly as the last screen, goes from
  the Arcade tab straight to Coin Quest.
- **"Star N recorded"** (noted under R12) is now "Star N saved", which is
  accurate with or without a server.
