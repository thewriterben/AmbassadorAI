# iOS — neutral link to the web arcade (with the Arcade entry point)

**2026-09-28.** Android 1.0.7 (`dgd-native` commit `5840218`) added a neutral
link to the web arcade. iOS has no Arcade entry point yet (it arrives with
`IOS-B2-RUNBOOK.md`), so this is a note to apply **when that entry point is
added**, not a separate change. Apply `IOS-PATH-A-CHANGE-REQUEST.md` first.

Why and the limits: `arcade/B1-DECISION-2026-09-21.md`, "Asked 2026-09-28"
and its follow-up. DGD chose the neutral tier; counsel still has the final say.

**Updated 2026-09-30 for DGD App 2.0.** Android 2.0 replaced the Arcade menu
with an Arcade tab (`RC-2.0.0-2026-09-30.md`). iOS should follow 2.0, so the
link is a card on that tab. The 1.0.7 menu is described at the end of this
document, for the record.

## What to build

On the **Arcade tab**, below the game cards, add one card, mirroring Android's
`ArcadeTab` in `AppTabs.kt`:

| Part | Content |
|---|---|
| Title | **DGD Arcade for Web** |
| Subtitle | *Play in your browser* |
| Trailing | `arrow.up.right.square` |
| Accessibility label | `DGD Arcade for Web — Play in your browser` (the design return requires this string verbatim) |
| Action | opens the web arcade in Safari |

```swift
// DigitalGoldSite.swift
/// Always this exact string: no query, fragment, user, handle, ref or src.
/// The web arcade must not be able to tell a visitor came from the app.
static let webArcade = URL(string: "https://digitalgold.co/arcade/")!
```

```swift
// Opening it: Safari itself, never a WKWebView or SFSafariViewController.
UIApplication.shared.open(DigitalGoldSite.webArcade)
```

## Rules (each is why it is safe)

1. **Copy exactly as above.** No reward, earn, bonus, prize, opportunity,
   enhanced, premium or pay wording anywhere in the app about the web arcade.
2. **URL exactly as above**, never extended.
3. **Opens Safari** via `UIApplication.shared.open`. Not `WKWebView`, not
   `SFSafariViewController` (both keep the paying site inside the app).
4. **Only on the Arcade tab.** Never on a result, level-complete or badge
   screen.
5. **Add a test** like Android's `WebArcadeLinkTest`: pins the URL, the
   wording, and fails if the source ever builds on `webArcade` or uses
   `WKWebView` / `SFSafariViewController`.
6. **Describe it in `apple/APP_STORE_REVIEW_NOTES.md`** (text below). Hiding
   the web arcade from the reviewer is the 2.3.1 problem the decision document
   warns about.

## Review-notes text

> **Arcade tab → "DGD Arcade for Web".** Opens digitalgold.co/arcade in
> Safari. It is DGD's website, playable by anyone without signing in. Signed-in
> digitalgold.co account holders can also receive DGD there for verified
> results, under official rules published on that page. None of that is
> offered, described or tracked in this app: the link carries no parameters,
> the site cannot tell visitors from the app apart from anyone else, and
> nothing done in the app counts there. The in-app arcade remains
> educational only; its XP and badges have no monetary value.

The Android 2.0 text in `RC-2.0.0-2026-09-30.md` also discloses the Top 100
credits DGD added on 28 Sep. Use that fuller text, with "Safari" for "the
phone's default browser".

## Screens to capture

1. The Arcade tab, with the card.

## Before 2.0: the 1.0.7 menu

Android 1.0.7 to 1.0.8 put the link in a two-item menu behind the top-left
Arcade button: **Play in the app**, and **DGD Arcade for Web** with *Play in
your browser* under it. The rules above applied to it unchanged. Android 2.0
removed the menu.
