# iOS 2.0: the Mac job (2026-10-01)

*Repository copy. The Mac works from `F:\Documents\dgdappsource\mac-handoff\`, and the paths below (`ios-2.0-assets/`, `ios-2.0-scripts/`, `reference/`) are relative to that folder. The build script is also kept here, as `integration/ios/build_ios_frameworks.sh`.*

**What this is.** The complete work package to bring the iOS app (`apple/`)
up to Android DGD App 2.0, as one job. It supersedes the three earlier
jobs in `READ-ME-FIRST.md` (the 1.0.6 Path A request, the 1.0.7 web link,
and the 1.0.8 arcade source). Those were never done on iOS, and everything
they asked for is in this job.

**Where iOS is.** `apple/` has not changed since `2948702` (B2a, 21 Sep).
That means:

- a single ticker screen with two sheets;
- system serif fonts and the old gradient;
- the referral surface still in place;
- no arcade;
- no web link.

**Where it must get to.** It must match Android 2.0.0 rc2 (dgd-native
`dgd-2.0` at `16394ec`):

- three tabs;
- the 30 Sep design system;
- the arcade embedded in demo mode;
- the web arcade link as a card;
- no referral surface anywhere.

**Decisions already made (the owner, 1 Oct):**

1. **Straight to 2.0 parity** in one job, in the order below. Path A comes first, because it is a compliance prerequisite.
2. **A native tab bar.** A SwiftUI `TabView` with Home, Arcade and Account, styled with the tokens. It is not a pixel copy of Android's floating pill.
3. **Reproducibility on iOS means two builds on the Mac.** The arcade frameworks are built twice from a fresh clone at the pinned commit (the second with pub offline) and must match. `ios-2.0-scripts/build_ios_frameworks.sh` does it.

**The rule that stays:** the Mac owns `apple/`, and the PC does not edit it
(there is a pre-commit hook to stop it). This job is done on the Mac and
comes back as a bundle.

---

## 0. Get set up

```sh
cd ~/src/dgd-native
git fetch ~/Downloads/dgd-native-2.0.bundle 'refs/heads/*:refs/remotes/pc/*'
git switch -c ios-2.0 pc/dgd-2.0          # 16394ec: Android 2.0.0 rc3
git log --oneline -1                      # 16394ec DGD 2.0.0 rc3: …
```

The 2.0 bundle also carries `main` (`a22c194`, Android 1.0.8) and
`dgd-2.1-live` (`f1c1f43`, the live build, for later). `2948702`, the Mac's
last commit, is already in all of them.

**The arcade source** comes from the bundle. There is nothing to check out by
hand, because the build script clones it:

```sh
git bundle verify ~/Downloads/puzzle-app-v2.bundle   # v2/ten-games 85e621c, main 99a5c36
```

**The toolchain:**

| | |
|---|---|
| Flutter | 3.47.2 / Dart 3.13.2. This must match the PC. Check `flutter --version`. |
| Xcode | 27.0, as for B2a |
| XcodeGen | 2.46.0, as for B2a |
| Python 3 | for `sync_module.py` |
| CocoaPods | **not used.** See phase 3. |

The Android source is the reference for every screen. It is in the same
repo, so read it at `android/app/src/main/java/com/digitalgold/ticker/` on
this branch. Paths below are relative to that folder.

---

## 1. Path A: remove the referral surface

**Do `IOS-PATH-A-CHANGE-REQUEST.md` (in this folder), sections 1 to 8, as
written.** Android did the same in 1.0.6. The reference is `android/README.md`,
"Invite Friends shares the app, not a referral", and
`ReferralSurfaceGuardTest.kt`.

**A survey of the iOS source on 1 Oct found every item still open:**

- **Universal links:** `DigitalGoldTicker.entitlements:7-8` still has `applinks:digitalgold.co` and `applinks:www.digitalgold.co`.
- **Incoming links:** `DigitalGoldTickerApp.swift:125-127` still has `.onOpenURL` (`consumeReferrer`).
- **Referral helpers:** lines 78-117 of the same file.
- **The friend's code:** `SignupPreviewView.swift` still has the `friendCode` storage (:18), its field (682-728) and `hasFriendCode` (:1086).
- **Copy buttons:** Copy Invite Link and Copy Invite Code (814, 818), and the `canShareInvite` gate (851 and others).
- **Copy:** "Username is your invite code" (:542), and the accessibility hint at :764.
- **The QR:** it still encodes `/app?ref=` (:959).
- **Share templates:** `InviteShareCopy.swift` still has `{USERNAME}` and "Use my invitation code" (53, 64).
- **Tests:** the referral tests in `DigitalGoldSiteTests` (`/signup?ref=`, `/app?ref=`, `testConsumeReferrerPrefillsFriendCodeFromHandoff`) and the "Use my invitation code, alice" tests in `InviteShareCopyTests`.
- **Docs:** `APP_STORE_REVIEW_NOTES.md` (24-25, 30, 42, 99-100), `README.md:142-145`, `docs/APP_INVITE_HANDOFF.md`, and the `apple-app-site-association` sample.

**Acceptance:**

- `grep -rn "ref=\|friendCode\|applinks\|invitation code\|Copy Invite" apple/` finds nothing outside comments that explain the removal.
- The tests are updated, and a guard test equivalent to `ReferralSurfaceGuardTest.kt` is added.
- `xcodebuild test` passes.

**Commit this phase on its own.**

---

## 2. The 2.0 shell: tokens, type, icons, three tabs

### Tokens

Take these from `ui/GoldTheme.kt` and from the design return's
`tokens/design-tokens.json`, `phoneAppRedesign` section (`reference/design-return-implementation-notes.txt` has the handoff notes). Replace the gradient
with the flat page colour.

| Token | Hex | Use |
|---|---|---|
| page | `#09090B` | every screen background |
| card | `#141414` | cards |
| surface | `#202020` | insets, the selected tab, wells |
| edge | `#303030` | hairline borders |
| text | `#E8E8E8` | primary text |
| secondary | `#A7A7A7` | secondary text, unselected icons |
| gold (accent) | `#EA952D` | primary buttons, selected tab, live dot |
| goldBright | `#FFAF4E` | pressed and hover |
| danger | `#FF6B6B` | errors |
| onGold | `#09090B` | text on gold buttons |

### Type

- **Fonts:** register `ios-2.0-assets/fonts/InterVariable.ttf` as Inter and `GeistMono-Variable.ttf` as Geist Mono (`UIAppFonts`).
- **Where each goes:** Inter for the UI. Geist Mono for figures, kickers such as "MATCH-3 · 60 LEVELS", and labels.
- **No more serif.** The `design: .serif` usage goes.
- **Licences:** ship the OFL notices in the app, as Android does in `assets/licenses`.

### Icons

- **The source:** Hugeicons SVGs in `ios-2.0-assets/icons-svg/` (MIT; `LICENSE-hugeicons.md` is next to them).
- **How to use them:** add them to the asset catalogue as **template** images with *Preserve Vector Data*, and tint them in code.
- **The mapping to Android:** `Home01` → home, `GameController03` → arcade, `UserCircle` → account, `Settings02`, `ArrowRight01`, `ArrowUpRight01` (the web link), `Internet`, `InformationCircle`, `Play`, `Reload`, `Star`, `LockKey`.

### App icon

- Use `ios-2.0-assets/app-icon/AppIcon.png`: opaque, 1024 px, and iOS applies the mask.
- `InviteAppIcon.png` replaces whatever the invite sheet shows.
- The design notes say not to reuse an app icon as a header logo.

### Navigation

A `TabView` with three tabs: Home, Arcade and Account.

- **Look:** dark tab bar. Selected icon and label in `#EA952D`, unselected in `#A7A7A7`.
- **Labels:** "Home", "Arcade", "Account".
- **Android reference:** `AppTabs.kt` (`AppTab`, `BottomBar`) and `TickerScreen.kt` (the shell).

### Home ("Market")

- **Reference:** `TickerContent.kt` and `HomeStatsPanel.kt`, and `reference/design-mockups/01-ticker-live.png`.
- **Layout:**
  - the title "Market", with the subtitle "Digital Gold network";
  - the price card: the DGD coin, "DGD" over "Digital Gold", the Live dot, "USD per DGD", the five-decimal price, and "Last updated" with the refresh button;
  - *The network* card, whose **Stats** button expands the live snapshot in place (Accounts, Market cap).
- **No chart.** Remove the stale hint at `TickerView.swift:180`, which still says "Shows Network Growth and Price charts… preview". Remove `chartPriceString` / `chartPriceFormatter` and their tests if nothing else uses them.
- **Get Digital Gold / Log in** move to the Account tab.

### Arcade tab

- **Reference:** `AppTabs.kt`, `ArcadeTab()` and `CoinQuestCard`; `DgdKit.kt` (`ScreenHeader`, `RowCard`, `InfoNotice`, `PrimaryButton`, `SquareIconButton`, `HugeIcon`).
- **Top to bottom:**
  1. **Header:** "Arcade", with the subtitle "Discover through play.", and a settings square button on the right. Its accessibility label is "Arcade settings", and it opens the arcade at `settings`.
  2. **The Coin Quest card:**
     - the kicker "MATCH-3 · 60 LEVELS" (Geist Mono);
     - "Coin Quest: DGD" (large; it wraps to three lines, as on Android), and "Match.\nLearn.\nExplore." (secondary);
     - the 3×3 board art from `ios-2.0-assets/card-art/cq_piece_*.png`, in Android's order;
     - the gold button "Play Coin Quest: DGD", which opens `coin_quest`.

     The game's name is **"Coin Quest: DGD"** in titles and on buttons (the owner's call, 1 Oct). Sentences keep the short "Coin Quest".
  3. **The When Pigs Fly row:** `pigs_card.png`, the title "When Pigs Fly", the subtitle "Fly a winged piggy bank through nine eras of money, and land it.", opening `pigs`.
  4. **"More ways to play"** section label, then the web link card (phase 4).
  5. **The notice, verbatim:** "Educational only. XP and badges have no monetary value."
- **Later, in the live build only:** a "Weekly standings" row. See section 7. It is **not** in 2.0.

### Account tab

- **Reference:** `AppTabs.kt`, `AccountTab()`, and `SignupPreviewScreen.kt`.
- **Layout:** the header "Account", tagged **PREVIEW · NOT LIVE**, then the Digital Gold card with "Get Digital Gold", then a "Log in" row.
- **The flows stay as they are** (the not-live preview and the local login), with **the locked copy unchanged.**
  - Android keeps it in `LockedCopy.kt` and pins it with `LockedCopyTest.kt`.
  - On iOS it lives in `CredentialsSignupCopy.swift`, `InviteShareCopy.swift` and `HomeStatsPanel`'s `Copy` enum.
- **Presentation:** push the flows inside the tab, or use a full-screen cover. Android moved from dialogs to in-window flows only because of an Android status-bar strip, so iOS sheets are acceptable if they look right.

### Status bar (Android finding S1)

- iOS forces dark mode already (`UIUserInterfaceStyle: Dark` and `.preferredColorScheme(.dark)`), so the status bar should stay light.
- **Check it anyway with the iPhone in Light mode,** on the Home, Arcade and Account tabs and inside the arcade. Android shipped dark icons on a dark page because of exactly this gap.

**Acceptance:**

- Simulator screenshots of the three tabs sit next to Android's `reference/android-2.0-screenshots/01-market.png` and `02-arcade.png`: same content, same order, same copy.
- `xcodebuild test` passes.
- **Commit.**

---

## 3. The arcade: Coin Quest and When Pigs Fly, demo mode

### Build the frameworks

`ios-2.0-scripts/build_ios_frameworks.sh` was written on the PC and has not
been run. Its first run is its test.

```sh
cd ios-2.0-scripts
./build_ios_frameworks.sh ~/Downloads/puzzle-app-v2.bundle 85e621c demo ~/dgd-ios-frameworks
```

- **`85e621c`** is the arcade Android 2.0.0 rc3 and 2.1.0 rc3 embed. Use exactly this commit.
- **The script:**
  - clones it to a fixed path;
  - generates the module (`sync_module.py`, never edited by hand);
  - runs `pub get --enforce-lockfile`;
  - builds Release xcframeworks with `DGD_APP_TAB=true DGD_DEMO=true`;
  - does all of that twice, the second time with pub offline;
  - writes `PROVENANCE.md`.
- **A and B must match.** If they differ, explain every difference in `PROVENANCE.md` before going on; differences inside `App.framework/App` are not acceptable.
- **The size:** the app grows by about 4×. Android went from 18.8 MB to about 77 MB.

### Embed

- Copy **build B's** xcframeworks into `apple/Frameworks/`.
- Declare each with `embed: true` under the target's `dependencies:` in `project.yml`, then run `xcodegen generate`.
- Commit `PROVENANCE.md` next to them, as Android does with `arcade-repo/PROVENANCE.md`.
- **No CocoaPods.** A Pods integration writes into the generated project, and the next `xcodegen generate` silently discards it (`IOS-B2-RUNBOOK.md`).

### `Arcade.swift`, mirroring `arcade/Arcade.kt`

- **One cached `FlutterEngine`,** warmed after the Home tab's first frame (a `.task`), never at launch. The ticker's request comes first.
- **`open(_ destination:)`:**
  1. Debounce taps within 1 s.
  2. Warm the engine if needed.
  3. Send `open` with the destination name on the MethodChannel **`dgd/arcade`**, *before* presenting.
  4. Present a `FlutterViewController(engine:)` full screen.
- **The destination names are fixed by the arcade:** `coin_quest`, `pigs`, `settings`, `home`. In 2.1 there is also `standings`.
- **Present it with UIKit,** from the top view controller, with `modalPresentationStyle = .fullScreen`. Do not use SwiftUI's `.fullScreenCover`.
  - **Why:** the arcade's back buttons call Flutter's `SystemNavigator.pop()`. On iOS that dismisses a presented `FlutterViewController`. A SwiftUI cover would be dismissed underneath its own `isPresented` state.
  - **Verify on a device that Back from every arcade screen returns to the Arcade tab:** the level map, a level, When Pigs Fly, and Settings. If it doesn't, tell the PC: the fix would be a small `leave` call on the channel.
- **The opening frame:** opening a different game than last time must show the new screen as its first frame (Android finding R9, fixed in the arcade at `3c4e42d`). Check it by opening Coin Quest, backing out, then opening When Pigs Fly.

**Acceptance:**

- Both games open from their cards, play, and return.
- The Settings button opens arcade Settings.
- In demo mode the arcade makes **no network requests.**
- The red coin is deep red.
- A fresh install shows Coin Quest at "0 / 180".
- **Commit.**

---

## 4. The web arcade link card

Follow `IOS-WEB-ARCADE-LINK.md` (updated 30 Sep for the tab design):

- **The card:** "DGD Arcade for Web" over "Play in your browser", with a trailing `ArrowUpRight01`. Its accessibility label is **exactly** "DGD Arcade for Web — Play in your browser".
- **The URL:** exactly `https://digitalgold.co/arcade/`, with no parameters.
- **Opening it:** `UIApplication.shared.open`. Never `WKWebView`, never `SFSafariViewController`.
- **Placement:** only on the Arcade tab. Never on a result or level-complete screen; the arcade's own screens never link out.
- **A test,** equivalent to Android's `WebArcadeLinkTest.kt`: it pins the URL, the wording, and the absence of web views.

---

## 5. Tests, screenshots, review notes

- **Tests:**
  - port what Android pins and iOS lacks: `WebArcadeLinkTest`, `ReferralSurfaceGuardTest`, `LockedCopyTest`;
  - keep the 93 existing tests passing, minus the removed referral ones;
  - add a test that `Arcade.swift`'s destination names are exactly `coin_quest`, `pigs`, `settings`, `home`.
- **Screenshots:** on a 6.9" and a 6.5" simulator, in dark mode with a clean status bar, of the same six screens as Android's `reference/android-2.0-screenshots/`:
  1. Market;
  2. Arcade;
  3. the Coin Quest map;
  4. a level sheet;
  5. the board;
  6. When Pigs Fly.

  Leave out Account (a "Get Digital Gold" button in a store screenshot puts acquiring the asset first), *The network* (it leads with market cap), and a When Pigs Fly flight (its coin art is still to be replaced before public release).
- **`APP_STORE_REVIEW_NOTES.md`:** take the three reviewer-note paragraphs from `reference/RC-2.0.0-2026-09-30.md`, with "Safari" in place of "the phone's default browser": the web link, the in-app arcade, and the Account tab. Remove the referral material (phase 1).
- **App Privacy (the nutrition label):** 2.0 adds nothing sent off the phone. The arcade is local in demo mode.
- **Version:** `MARKETING_VERSION 2.0.0`, `CURRENT_PROJECT_VERSION 200`, to match Android.

## 6. Send it back

```sh
cd ~/src/dgd-native
git bundle create ~/Desktop/dgd-native-ios-2.0.bundle ios-2.0
```

Send back with it:

- `~/dgd-ios-frameworks/PROVENANCE.md`, plus `A.sha256` and `B.sha256`;
- the screenshots;
- the `xcodebuild test` output;
- a short note of anything that didn't go as this document says.

**Still blocking the App Store,** and not part of this job:

- DGD's organisation Apple Developer account, with Bob;
- a privacy policy URL (`/privacy` returned 404) and a support URL.

---

## 7. Later: the live build (2.1), once the arcade server is up

This is not part of this job. It is written down so the 2.0 work leaves room
for it.

- **Rebuild the frameworks with the live URL:**

  ```sh
  ./build_ios_frameworks.sh ~/Downloads/puzzle-app-v2.bundle 85e621c https://arcade-api.digitalgold.co ~/dgd-ios-frameworks-live
  ```

  `85e621c` is the arcade Android 2.1.0 rc3 embeds, the same commit as 2.0.
- **Add the "Weekly standings" row** under the When Pigs Fly row.
  - The title is "Weekly standings", the subtitle "This week's XP from Coin Quest and When Pigs Fly. Recognition only.", the icon `card-art/standings_podium.png`, and it opens `standings`.
  - **It shows only when the embedded frameworks were built with `ARCADE_API` and without `DGD_DEMO`.** Derive that from the frameworks' `PROVENANCE.md` at build time, as Android derives `BuildConfig.ARCADE_LIVE` from its own. Never use a hand-set flag.
- **What the arcade itself already handles** in the shared Dart: it contacts the server only from the first open, never at launch; a round registers a new record after a delete; and growth waits for the server.
- **App Privacy changes.** `reference/PRIVACY-DRAFT.md`, "DGD App 2.1.0", has the draft for DGD to approve.
