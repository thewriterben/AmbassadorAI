# Android 1.0.7 — release candidate

**2026-09-29.** dgd-native `5840218`. versionCode 7, targetSdk 36, minSdk 26,
ABIs arm64-v8a / armeabi-v7a / x86_64. R8 on (shrink + obfuscate).

| Artefact | Bytes | SHA-256 | For |
|---|---|---|---|
| `DigitalGold-1.0.7-unsigned.aab` | 53,946,633 | `FEB9D06061AB62F6BB8E9663253A47EFC995F2695044921B5F77F31438691A04` | **Play.** Unsigned: DGD signs it with the upload key (below). |
| `DigitalGold-1.0.7-review.apk` | 61,281,687 | `A59860F6D713EDA4D493A6B45C1DB2C591E65F63C36A389E728A741619A2D3CF` | Installing and looking. Debug-signed, says `1.0.7-review` in the app; Play refuses it. |

Both come from the same commit and the same R8 configuration. The AAB carries
the R8 mapping and Flutter's native symbols in `BUNDLE-METADATA/`, so Play
de-obfuscates crash reports without a separate upload.

## What changed since 1.0.6

One thing. The top-left **Arcade** button opens a two-item menu:

- **Play in the app** — the in-app arcade, as before.
- **DGD Arcade for Web** · *Play in your browser* — opens exactly
  `https://digitalgold.co/arcade/` in the phone's own browser (a plain VIEW
  intent: not a WebView, not an in-app browser tab), with no parameters.

This is the neutral link DGD chose on 2026-09-28 (`B1-DECISION-2026-09-21.md`).
The manifest is **identical to 1.0.6's except the version** (same two
permissions; no new intent filters, no `<queries>`).

## Verification

| Check | Result |
|---|---|
| Unit tests | **95 / 95** (the 1.0.7 commit message says 96; it is 95 — 92 from 1.0.6 plus 3 in `WebArcadeLinkTest`) |
| Lint (release) | **0 errors**, 43 warnings; the one new warning is `UseKtx` (style) in `WebArcadeLink.kt` |
| Manifest vs 1.0.6 | identical except versionCode / versionName |
| AAB signature | none — unsigned, as intended |
| Dex strings (AAB and APK) | `https://digitalgold.co/arcade/`, *DGD Arcade for Web*, *Play in your browser*, *Play in the app* present; `ref=`, `src=app`, `utm_`, `invite code`, `invitation code`, `Copy Invite`, `Enhanced`, `App Store`, `CustomTabsIntent` all **0** |
| R8 build on the API 36 emulator | launches; the menu renders; **Play in the app** opens the Flutter arcade (R8 did not break it) — `rc-1.0.7-shots/01–03` |
| The web link, with the emulator's network **off** | tapping it starts `VIEW` + `BROWSABLE`, `capturedLink=https://digitalgold.co/arcade/`, in Chrome's own task (the app goes to the back) — `04`. With no network, nothing reached digitalgold.co; Chrome's data was cleared afterwards |
| Pixel 9a | the debug 1.0.7 was checked there on 28 Sep (menu, in-app arcade, link resolves to Chrome, not tapped). The Pixel was locked this pass, so the R8 build was checked on the emulator only |

R8 prints "An error occurred when parsing kotlin metadata" (8×): the Kotlin
compiler is newer than this R8 knows. It is a warning, the build and the
emulator run are clean, and it clears when AGP is next updated.

## Signing and uploading (DGD)

The upload key is DGD's and is not on this machine. With it:

```
jarsigner -keystore <dgd-upload.jks> -sigalg SHA256withRSA -digestalg SHA-256 ^
  DigitalGold-1.0.7-unsigned.aab <upload-key-alias>
jarsigner -verify DigitalGold-1.0.7-unsigned.aab      :: "jar verified."
```

Then Play Console → the app → a track (internal testing first) → create
release → upload the signed `.aab`. versionCode 7 must be higher than any
version already uploaded.

## Play Console text

**What's new (en-US)** — 96 characters of 500:

> The Arcade button now opens a menu: play in the app, or open DGD Arcade for
> Web in your browser.

**Notes for the reviewer** (App access, or any policy query about the link):

> **Arcade menu → "DGD Arcade for Web".** Opens https://digitalgold.co/arcade/
> in the phone's default browser. It is DGD's website, free to play for anyone
> without signing in; nothing is sold there and no payment is ever needed to
> take part. Signed-in digitalgold.co account holders may receive DGD, and DGD
> validation credits for Top 100 places, for results the site verifies, under
> official rules published at digitalgold.co/arcade/rules.html (currently in
> test mode: nothing is owed or paid). None of that is offered, described or
> tracked in this app: the link carries no parameters, the site cannot tell
> visitors from the app apart from anyone else, and nothing done in the app
> counts there. The in-app arcade is educational only; its XP and badges have
> no monetary value.

This matches the iOS text in `integration/IOS-WEB-ARCADE-LINK.md`, plus the
Top 100 credits DGD added on 28 Sep. Disclosing the web rewards plainly is
deliberate: a reviewer who finds them unaided is the worse outcome.

## Play policy — read on 2026-09-29, not settled

Not legal advice; counsel's to confirm, as `B1-DECISION` already says for Play.

- **Real-Money Gambling, Games, and Contests.** What it bars outside licensed
  apps is letting users "wager, stake, or participate using real money" for a
  prize of real-world value, including menu items or buttons that are a "call
  to action" to do so (its example: "COMPETE!" for a cash prize). The web
  arcade takes no money from anyone and the menu item says only *Play in your
  browser*. On its text this policy is not triggered; free-entry prizes still
  carry prize-promotion law, which is counsel's.
- **Blockchain-based Content.** An app that "sells or enables users to earn"
  tokenized digital assets must say so in the **Financial features
  declaration**, and "may not promote or glamorize any potential earning".
  The app enables no earning and the link copy promotes none; whether linking
  to a site where DGD can be received needs declaring is for DGD to decide
  when completing that form — answer it as the app actually is.

## Not done here

- **iOS** — Mac-owned; `integration/IOS-WEB-ARCADE-LINK.md` and
  `mac-handoff/dgd-native-1.0.7.bundle` have what it needs.
- **The Pixel on the R8 build** — unlock it and I can repeat 01–03 there
  (never the web item: no traffic to digitalgold.co from test devices).
- **Social follow links** — still waiting on DGD's URLs.

Sources: [Real-Money Gambling, Games, and Contests](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en),
[Blockchain-based Content](https://support.google.com/googleplay/android-developer/answer/13607354?hl=en).
