# What the app and server actually do

Facts as of **build 1.0.5 (25 September 2026)**. Check these before asserting
anything about how the app behaves — several proposals that sound fine collide
with one of them, and the collision is usually the most useful thing to say.

## What the app emits

Two referral URLs, built in `DigitalGoldSite.kt` (Android) and its iOS
counterpart:

- `inviteLinkURL` → `https://digitalgold.co/signup?ref=USERNAME` — Copy Invite
  Link. **Carries no channel information at all**, byte-identical to a website
  referral.
- `appInviteURL` → `https://digitalgold.co/app?ref=USERNAME` — Display QR. An
  app-download link with a referral code.

Surfaced in the member preview: **Get Digital Gold → Credentials → Wallet →
Receive → Invite Friends**. Any email address and any verification code gets you
there; nothing is sent and no account is created.

**The username *is* the invite code.** This is why the leaderboard cannot show
DGD usernames — doing so would publish invite codes.

## What the arcade server trusts — R2

**Mini-game scores are whatever the client asserts**, bounded only by the
per-round and per-day caps. This is an *accepted* risk in the audit precisely
because nothing of value currently rides on a score.

Any proposal that attaches value to a score needs server-authoritative scoring
first — deterministic replay or server-side move validation. That is real work
on both the server and the game, and it is the largest single engineering item
in most reward proposals. A browser client would be *easier* to fake than the
APK, not harder.

Also open at deploy time: **R12** (CORS is a wildcard unless `ARCADE_CORS` is
set, and it does not key off `NODE_ENV`) and **`ARCADE_SECRET` is still unset**
— it signs the single-use question tokens, and without a real value the server's
authority over XP is decorative.

## Identity and the leaderboard decision

The arcade uses **assigned handles** and deliberately does not know the DGD
username. That is what makes the in-app anonymity statement true and what keeps
the Play Data Safety declaration accurate.

Any proposal that links arcade activity to a DGD account reopens this. It is a
Data Safety change, not just a feature.

## On-screen text that must stay true

- Arcade: **"Educational only. XP and badges have no monetary value."**
- Member preview: marked **PREVIEW · NOT LIVE** throughout. Creates no account,
  takes no payment, delivers nothing.
- `apple/APP_STORE_REVIEW_NOTES.md` asserts the app does not pay for inviting —
  true of the app, and materially incomplete as a description of the programme
  now that referrals pay DGD. Removing invites makes it straightforwardly true
  again.

## Enforced compliance decisions

- **No prize-style celebration** on a level win — no coin showers, jackpots or
  casino visuals. Enforced in the build rather than left to a reviewer's eye
  (arcade plan §4.3).
- **The generated chart was removed.** The Stats panel used to draw price
  history and network growth **generated on the phone** — plausible-looking,
  ending on the real number, footnoted as illustrative, and not a measurement of
  anything. Gone from both platforms. Do not propose anything shaped like it;
  invented performance figures for a financial product are a problem no footnote
  fixes.
- The demo build makes **zero network calls from the game** (`DGD_EMBED=demo`),
  which is why the team demo shows no scores or leaderboard.

## What is still outstanding, so nobody promises a date

- The B1 decision itself — DGD and counsel.
- Backend's Path C questions, chiefly the unforgeable app-origin signal (moot
  under Path A).
- The Play Store signing key, which is DGD's to hold.
- Hosting for the arcade server.
- iOS screen captures.
