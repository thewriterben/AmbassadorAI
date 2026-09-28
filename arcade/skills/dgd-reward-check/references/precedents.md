# Answered already — six versions of the question

Each of these was worked through and recorded in
`arcade/B1-DECISION-2026-09-21.md`. If a new proposal matches one, use the
recorded reasoning rather than re-deriving it.

## 1. Referrals pay DGD — the original problem (answered 21 Sep 2026: yes, they do)

**Status: this is the live exposure and the launch critical path.**

The app builds two referral URLs:

- `https://digitalgold.co/app?ref=USERNAME` — Display QR. An **app-download
  link carrying a code that earns DGD**, which is 3.1.5(v)'s own example.
- `https://digitalgold.co/signup?ref=USERNAME` — Copy Invite Link.

The "the app doesn't pay, the site does" defence is real but thin: the app
ships the mechanism, the code, the QR and the share sheet, and only settlement
happens elsewhere.

Five options were documented, with costs:

| | Option | Engineering | Residual risk |
|---|---|---|---|
| **A** | Remove invites from the app entirely | ~half a day, both platforms | Lowest |
| **B** | Remove the app-download QR only | ~2 hours | Partial — do not rely on it alone |
| **C** | Don't credit app-originated referrals | Backend, if possible at all | See below |
| **D** | Drop QR only | subset of B | Partial |
| **E** | Submit and argue it | none now | Highest, and asymmetric |

**Path C's blocker:** the QR is distinguishable by path, but `/signup?ref=`
carries no channel marker at all, and a `&src=app` marker is
clipboard-strippable. Path C survives only with an unforgeable server-side
signal the user cannot edit — that is the open question to backend, and a plain
"no" is as useful as a yes.

## 2. Skill-based game or quiz awards (answered 21 Sep 2026: no help)

3.1.5(v) says "completing tasks" and ends in "etc." — illustrative, not
exhaustive. Clearing a level is a task; answering a quiz question is a task.
Skill-versus-chance is a gambling-law distinction and 3.1.5(v) is not a
gambling rule; it never mentions chance. Removing chance stops something being
a lottery under §5.3.4 while doing nothing about 3.1.5(v).

It would also newly engage rules that currently do not apply: 5.3.1/5.3.2
(developer-sponsored contest, official rules in the app), 3.1.5(i)/(iii)
(wallet/exchange licensing), state prize-competition law, tax, and DGD's legal
character.

**Sequencing point:** referrals already pay DGD, so adding this enlarges the
undecided critical path rather than opening a new front. Worst ordering.

**On "validation credits":** one question decides it — can the credit become
anything of value, ever, by any route? No path, ever: fine, that is what XP
already is. Converts at any point: same rule, one step added. The name is not
the question, and "validation credits" is itself a small flag because it sounds
like it accrues toward something.

## 3. DGD to top scorers, off-app, not mentioned in the app (answered 21 Sep 2026: weakest version)

Stronger than the referral case in one way — no download-encouragement element.
**Weaker in the way that matters:** the rewarded activity happens entirely
inside the app. A referral at least has an off-app leg; a top score has none.

"Not mentioned in the app" makes it worse, not safer:

- The arcade states XP and badges have no monetary value. Converting scores to
  DGD makes that **false** — a contradicted disclaimer reads as concealment.
- Unmentioned means no engagement value, which defeats the purpose.
- It cannot stay unmentioned: it gets announced on the site or socials, and
  winners talk.

Plus **R2** (see `app-facts.md`): scores are client-asserted, so a top-scorer
prize goes to whoever edits the request first.

## 4. Move the arcade to the web, pay DGD in the browser, carry app progress over (answered 25 Sep 2026: first half clean, carryover self-defeating)

Moving the games to the web genuinely changes jurisdiction — Apple governs the
app, not a website paying for web games. Real change of footing.

**The carryover undoes it.** If in-app progress feeds the web reward, the app is
the earning surface and the browser is a cashier — worse than the payout-location
arguments, because the sync is a deliberate, documented mechanism.

| Sync | Verdict |
|---|---|
| None | **Clean** |
| Web → app, read-only display of standing | **Fine**, recovers most of the product benefit |
| App → web earning | **Same problem, with a receipt** |

Two further costs of carryover: it requires the app to know which DGD account
the player is, reopening the assigned-handles and Data Safety decision; and it
makes server-authoritative scoring a prerequisite rather than an accepted risk,
since a browser client is easier to edit than an APK.

Product cost of moving the arcade out at all: it is the app's engagement piece.

## 5. Signup, verification and referral earnings entirely online, separate from any app activity (answered 25 Sep 2026: yes — recommended)

**This is Path A, and the cheapest exit from B1.** It does not ask Apple to
accept a theory; it removes the thing the rule is about.

Requires, to be true:

- Invite surface out of the app — QR, Copy Invite Link, Copy Invite Code, share
  buttons, and both URL builders. ~half a day, both platforms.
- No in-app copy describing the programme. The pitch is an offer even without a
  mechanism.
- **No attribution path from app to signup, of any kind** — written down as a
  positive requirement. This makes the Path C question moot, so tell backend
  before they build the signal.

A plain link to `digitalgold.co` with no `ref` parameter is fine.

Buys: 3.1.5(v) stops applying; the reviewer notes become true again;
verification stays off the app (no KYC surface, nothing new in Data Safety);
iOS unblocks without a legal opinion on payout locations.

Costs: the in-app viral loop, and only that. Does not settle Play's
incentivised-installs and financial-services policies, or the securities and tax
treatment of paying DGD for referrals at all — those move off the launch
critical path rather than getting answered.

## 6. Validation credits, not disclosed at all (answered 26 Sep 2026: no — declined as a design request)

The only recorded version that puts the **developer account** at risk rather
than the app. 2.3.1(a) prohibits hidden or undocumented features; 2.3.1(b) and
5.6 escalate dishonest or manipulative conduct to program removal.

It also does not work: credits are either visible (disclosed) or invisible (no
behavioural effect); DGD payouts leave a trail; and it falsifies the arcade
disclaimer while concealing from users what they are accruing.

Disclosed alternatives: non-convertible credits described like XP (fine), or a
DGD-paying validation programme on the website with the app uninvolved (Path A
shape).

## 7. Link from the app to the web arcade (answered 28 Sep 2026: neutral only — shipped on Android 1.0.7)

Proposed as an "Enhanced Arcade" link offering "additional features or
opportunities" and DGD rewards: **exposed** — the app becomes the
advertisement for the reward, and "Enhanced" makes the in-app arcade the free
tier of a paying one. "Opportunities" is the renaming trap.

| In the app | Exposure |
|---|---|
| Plain `digitalgold.co` link | Clean |
| Neutral link to `/arcade/` — no reward/earn/enhanced/opportunity wording, bare URL, phone's own browser, menu only, described in review notes | **Grey — DGD chose this; counsel's final say** |
| Link offering rewards or "opportunities" | Exposed |

Shipped wording: *"DGD Arcade for Web — Play in your browser"*. The web side
helps by landing on games: guest play, rewards disclosed in one line (not
hidden, not the headline), a rules page, and no special treatment of app
visitors. Any later proposal to add reward wording, parameters, a WebView, or
placement on a results screen moves it back to exposed.
