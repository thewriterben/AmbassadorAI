# iOS — neutral link to the web arcade (with the Arcade entry point)

**2026-09-28.** Android 1.0.7 (`dgd-native` commit `5840218`) added a neutral
link to the web arcade. iOS has no Arcade entry point yet (it arrives with
`IOS-B2-RUNBOOK.md`), so this is a note to apply **when that entry point is
added**, not a separate change. Apply `IOS-PATH-A-CHANGE-REQUEST.md` first.

Why and the limits: `arcade/B1-DECISION-2026-09-21.md`, "Asked 2026-09-28"
and its follow-up. DGD chose the neutral tier; counsel still has the final say.

## What to build

The Arcade button opens a two-item menu (SwiftUI `Menu`), mirroring Android:

| Item | Action |
|---|---|
| **Play in the app** | opens the embedded arcade, as the runbook describes |
| **DGD Arcade for Web** — secondary line *Play in your browser*, trailing `arrow.up.right.square` | opens the web arcade in Safari |

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
4. **Only in the Arcade menu.** Never on a result, level-complete or badge
   screen.
5. **Add a test** like Android's `WebArcadeLinkTest`: pins the URL, the
   wording, and fails if the source ever builds on `webArcade` or uses
   `WKWebView` / `SFSafariViewController`.
6. **Describe it in `apple/APP_STORE_REVIEW_NOTES.md`** (text below). Hiding
   the web arcade from the reviewer is the 2.3.1 problem the decision document
   warns about.

## Review-notes text

> **Arcade menu → "DGD Arcade for Web".** Opens digitalgold.co/arcade in
> Safari. It is DGD's website, playable by anyone without signing in. Signed-in
> digitalgold.co account holders can also receive DGD there for verified
> results, under official rules published on that page. None of that is
> offered, described or tracked in this app: the link carries no parameters,
> the site cannot tell visitors from the app apart from anyone else, and
> nothing done in the app counts there. The in-app arcade remains
> educational only; its XP and badges have no monetary value.

## Screens to capture

1. Home with the Arcade button.
2. The menu open.
