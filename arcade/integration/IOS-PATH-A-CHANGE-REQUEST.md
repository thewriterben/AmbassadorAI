# iOS change request — B1 Path A (remove the referral surface)

**For the Mac.** `apple/` is Mac-owned; nothing below was edited from Windows.
Android equivalent shipped as **1.0.6** on 2026-09-26 (dgd-native, see the
Android commit of that date). Mirror it, build, run the tests, and send back a
bundle as usual.

**Why:** referrals pay DGD, and App Review 3.1.5(v) prohibits crypto apps
offering currency for "encouraging other users to download". Decision recorded
in `arcade/B1-DECISION-2026-09-21.md` (Path A, "recommended"). The app carries
**no referral surface in either direction**: it builds no referral URL, reads
none from an incoming link, stores no friend's username, and never describes
the programme. Invite codes are entered on digitalgold.co.

Line numbers are from `apple/` at dgd-native `f6f9a6e`; treat them as a guide.

---

## 1. Remove

| Where | What |
|---|---|
| `DigitalGoldTicker.entitlements:7–8` | Both `applinks:` entries. No Universal Links for digitalgold.co. |
| `DigitalGoldTickerApp.swift:125–127` | The `.onOpenURL { DigitalGoldSite.consumeReferrer(...) }` modifier. |
| `DigitalGoldTickerApp.swift:78–120` | `inviteLinkURL`, `appInviteURL`, `inviteURL`, `referrer(from:)`, `consumeReferrer(from:)`, and the private `url(base:username:)` builder. |
| `SignupPreviewView.swift:18` | `@AppStorage(friendCodeStorageKey) friendCode` and `hasFriendCode` (~1085). |
| `SignupPreviewView.swift:276–277, 682–728` | `friendCodeField` / `friendCodeValue` and the "Learn how friend usernames work at" line. |
| `SignupPreviewView.swift:813–820, 909–1000` | Copy Invite Link, Copy Invite Code, `inviteCopyButton`, `copyInvite`, `InviteCopyKind`, `copiedInvite`. `inviteRevealLastStep` 6 → **4** (hint, socials, QR, email); the scroll target `"inviteCopyCode"` becomes the email row. |
| `SignupPreviewView.swift:767–790` | The `canShareInvite` gate and the "Add your username on Credentials first / Go to Credentials" branch. Nothing is per-user any more, so sharing needs no username. Delete `canShareInvite` and every `.opacity`/`.allowsHitTesting` keyed on it. |

## 2. Keep, but rename

- `friendCodeStorageKey` → **`legacyFriendCodeStorageKey`** (`"dgd.friendCode"`),
  used only to delete it. Add, once at launch:
  `UserDefaults.standard.removeObject(forKey: DigitalGoldSite.legacyFriendCodeStorageKey)`.
  1.0.5 stored a captured `?ref=` here; an upgraded install must not keep it.
  (Android verified this on an upgraded emulator: `testfriend` present on
  1.0.5, gone after the 1.0.6 upgrade and first launch.)

## 3. Change copy

| Where | Old | New |
|---|---|---|
| `SignupPreviewView.swift:542` | Username is your invite code. 3+ characters, no spaces. | **3+ characters, no spaces.** |
| `SignupPreviewView.swift:736` | Every new node makes the network stronger. Learn how invites work on | **Every new node makes the network stronger. Learn more at** |
| `InviteShareCopy.optionsHelper` | Show a QR, share by email or socials, or copy your invite link or code. | **Share by email or socials, or show a QR a friend can scan.** |
| a11y hint `:764` | …copy invite link, and copy invite code. | **Shows X, Facebook, and LinkedIn, display QR, and email.** |
| new, under the QR | — | **Scanning this opens the app download. Take a screenshot and text it to a friend.** (centred, muted, 14pt serif) |

## 4. The QR

`SignupPreviewView.swift:959` encodes `appInviteURL(username:)`. Replace with a
constant **identical for every user**:

```swift
/// What Display QR encodes. Identical for every user — a per-user QR is
/// attribution even without the word `ref`, so this is a constant.
static let shareQRURL = appHandoff   // https://digitalgold.co/app
```

Android's QR decodes to exactly `https://digitalgold.co/app`.

## 5. The share message

`InviteShareCopy.swift`: one template for email and socials, **no
`{USERNAME}`**, and `emailBody()` / `socialsBody()` take no argument.
`InviteSharePresenter.presentEmail` / `presentSocial` drop `username:`.

```
Join me in the Digital Gold community today and learn about predictably-priced, wealth-preserving digital money.

They’re giving students priority now, but Digital Gold will be open to the public soon. Just get the app, create a Digital Gold account, and download the free Digital Gold QT wallet. Learn more details at digitalgold.co.

If you’re not a student, join the waitlist at digitalgold.co to be first in line.

Search “digital gold” in the App Store to get the app, or visit digitalgold.co.
```

- **App Store only.** App Review 2.3.10 (checked 2026-09-26) says not to name
  other mobile platforms in the app. Android's message says "Play Store"; the
  "or visit digitalgold.co" covers the other platform.
- Keep the zero-width-space delinking of `digitalgold.co`.
- The Mail composer may keep attaching the rounded icon (it is the same for
  everyone); drop the "look for this icon:" line so the text matches the
  agreed message.
- "predictably-priced, wealth-preserving" is unchanged and **flagged for
  counsel** as a claim about a crypto asset's value; not an App Review rule.
  Do not reword it without DGD.

## 6. Tests to add (mirror Android)

1. **Share message is the agreed text**, email == socials, and contains none of:
   `invitation code`, `invite code`, `{USERNAME}`, `share yours`, `ref=`,
   `https://`, `digitalgold.co/app`, `digitalgold.co/signup`, `Play Store`.
2. **QR constant** equals `https://digitalgold.co/app`, contains no `?` and no `ref`.
3. **No referral API on `DigitalGoldSite`** — delete the old
   `testConsumeReferrerPrefillsFriendCodeFromHandoff` and URL-builder tests.
4. **Credentials has three editable fields**, not four (UI test).
5. **Legacy key is purged** at launch.
6. **Source guard**: a test (or a build-phase script) that scans
   `DigitalGoldTicker/` with comments stripped and fails on `?ref=`, `"ref"`,
   `friendCode` (except the legacy constant), `invite code`,
   `invitation code`, `Copy Invite`, `applinks:digitalgold.co`. Android's
   `ReferralSurfaceGuardTest` is the model; it was proven to fail by planting a
   `?ref=` builder and watching it go red.

## 7. Docs in `apple/`

- **`APP_STORE_REVIEW_NOTES.md`** — this is pasted into App Store Connect, so it
  must describe the build exactly. Lines 24–25, 30, 42, 98–100 describe Copy
  Invite Link/Code, the silent `?ref=` prefill and the friend field. Replace
  with, in substance: *"Invite Friends shares one fixed message by email or
  X/Facebook/LinkedIn, and shows a QR to the App Store download page. Both are
  identical for every user and carry no referral code, link or username. The
  app does not receive or handle incoming links."* Do **not** add a sentence
  about the website's programme; describe the app.
- `README.md:140–148` and `docs/APP_INVITE_HANDOFF.md` — rewrite or delete; the
  handoff doc is a design for the removed feature. Android deleted its
  equivalent `invite-handoff/` stubs rather than leave a template.

## 8. Done when

- Build, unit and UI tests green on the Mac.
- A screenshot of Receive → Invite Friends → Display QR, and of Credentials
  (three fields), in `rc-1.0.6-shots/ios/`.
- The QR in that screenshot decodes to `https://digitalgold.co/app`.
- Bundle back to Windows as usual.

**Not in scope:** social *follow* links (blocked on DGD supplying official
URLs) and real in-app signup (needs backend, plus in-app account deletion under
5.1.1(v)).
