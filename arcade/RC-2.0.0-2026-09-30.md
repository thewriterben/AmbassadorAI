# DGD App 2.0.0: Android release candidate

**2026-09-30.** This is the release record for DGD to sign and upload. It
replaces the Play Console text in `RC-1.0.7-2026-09-29.md` and
`RC-1.0.8-2026-09-29.md`, which describe the old layout: those two stay as the
record of what shipped then.

## Artefacts

`C:\src\dgd-native\android\dist-2.0.0\`, built from dgd-native `dgd-2.0` at
`f04b884`.

| File | Bytes | SHA-256 | For |
|---|---|---|---|
| `DigitalGold-2.0.0-unsigned.aab` | 64,752,897 | `FE22CAA16CDC8536E01EE9A0AF1AF964A6E32188FA9672303A6837827D009594` | Play, once DGD signs it |
| `DigitalGold-2.0.0-review.apk` | 72,275,537 | `D253C3719F604A4D752AA2CF1C40B73F04E520526748B5BB5D6DC9CAA424B8E4` | Installing and looking. It is debug-signed and says `2.0.0-review` in the app; Play refuses it. |

The release is version 2.0.0, versionCode 200.

**The arcade embed** is puzzle-app v2 at `7fc97da`, built in the clean room in
demo mode (`DGD_APP_TAB=true`, `DGD_DEMO=true`). It has no server and makes no
requests. `ARCADE-PROVENANCE.md` is next to the AAB.

**The checks behind it:**

- The native half was reproduced in the clean room: 782 of 788 bundle entries are identical. The six that differ are R8 and profile metadata.
- 95 unit tests and 4 of 4 instrumented tests pass.
- The red-team runner passes.
- The details are in `AUDIT-DGD2.0-2026-09-30.md` and `redteam-runs/`.

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
upload the signed `.aab`. versionCode 200 is higher than anything uploaded so
far (1.0.8 is 8).

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
1080 × 1920 (9:16, inside Play's 2:1 limit). They were taken from the 2.0.0
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

**These screenshots show 2.0.0 exactly,** including Coin Quest's rose red
coin, which is now deep red in source. Retake them for the build that
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

## Found while taking the screenshots: fixed in source, not in this AAB

| | What | State |
|---|---|---|
| S1 | **Status bar icons were dark on the dark page** when the phone is in light mode, so the clock and battery were barely visible. `enableEdgeToEdge()` with no arguments follows the system theme and overrode `windowLightStatusBar=false`. The arcade's own screens were unaffected. | Fixed in dgd-native `MainActivity` (`83119d7`): the system bars are always dark-style. A review build of it showed light icons in light mode on the emulator, and the 95 unit tests pass. It is in the next build. |
| S2 | **The Arcade tab's Coin Quest card** carries its own copy of the coin art, still in rose. | Replaced with the deep red sprite (arcade `faa63bf`), and checked in the same review build. It is in the next build. |
| S3 | **The bottom edge of the Coin Quest board is clipped** by about 10 px on a 16:9 screen (1080 × 1920). The last row is whole, but the frame's lower edge is cut. | Open. This is a LOW in the arcade. |

**If DGD wants S1 in the first 2.0 release,** we rebuild. It is a one-file
change, and the clean-room steps are the same.
