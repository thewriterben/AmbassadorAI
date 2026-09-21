# Digital Gold app — where we are

**21 September 2026. For the team.** A demo build is attached so you can put
the app on your own phone and look at it.

No technical background needed for this document. Nothing here is confidential
to engineering — keys, endpoints and credentials live in a separate backend
document and are not repeated anywhere below.

---

## The short version

The Android app is **feature-complete for a first release and has nothing
engineering-side blocking it.** What is left is two decisions and one piece of
paperwork, all of which sit with DGD rather than with the build.

iOS is close behind, with one piece deliberately postponed.

---

## Try it: the demo build

`DigitalGold-1.0.5-review.apk`, Android only.

**It will say `1.0.5-review` inside the app. That is on purpose** — it is how
you can always tell a review build from a real one, whatever the file is
called.

To install: copy it to an Android phone, tap it, and allow installing from
this source when prompted. It sits alongside anything else on the phone and
can be uninstalled normally.

### What to look at, in order

1. **The ticker.** Live account count, price and market cap, pulled from the
   public site. The price counts up and lands with a flourish.
2. **Stats.** Three live figures and a line saying where they came from and
   when. *Nothing else* — see "The chart we removed" below.
3. **Get Digital Gold.** The three-step member preview: credentials, wallet,
   receive. It is clearly marked **PREVIEW · NOT LIVE** throughout. It does not
   create an account, take payment or deliver anything.
4. **Arcade**, top-left. Coin Quest, sixty levels. This is the engagement piece.

### Two things you will notice are missing, and should be

- **No scores, XP bar or leaderboard in the arcade.** The demo has no server
  behind it and makes no network calls at all. Those features exist and are
  tested; they switch on when the backend is hosted.
- **No prize-style celebration** when you win a level. No coin showers, no
  jackpot. That is a compliance decision, enforced in the build rather than
  left to a reviewer's eye, and it is deliberate.

---

## What changed recently

### A first-run blocker — the one that mattered most

No new user could finish the signup preview. Not "it was awkward" — it was
impossible. Progress was blocked by a check that only progress itself could
unlock, and it failed **silently**, so the screen simply did nothing.

It never showed up in testing because anyone who had used the app once already
had the gate open. It only appears on a genuinely fresh install. Fixed, and
there are now automated tests that install fresh every time so it cannot come
back.

### The chart we removed

The Stats panel used to draw a price history and a network-growth curve. Those
lines were **generated on the phone** — plausible-looking, ending on the real
number, footnoted as illustrative. They were not measurements of anything.

Invented performance figures for a financial product are a problem no footnote
fixes, and both app stores take a dim view. They are gone from Android and, as
of today, from iOS too. Real history goes back in when the site can serve it.

This was flagged by DGD's own backend reviewer and was the most substantive
finding in that review.

### A crash on older Android phones

Found this week: the invite link, the QR code and any invite link opened from
outside the app all crashed on **Android 8 through 12**. Newer phones were
fine, which is why nobody had hit it. Fixed.

Worth saying plainly: this was caught by a code-quality check that had never
been run on this project before. It was added as a standing part of the
release checklist.

And the fix was then checked **on an actual Android 11 device**, not just on a
modern phone. The test phone here runs the newest Android, which never had the
problem — so "it works on my phone" would have proved nothing. That is exactly
how the bug got in.

### Tablets and folding phones

Android changed the rules this year: apps no longer get to stay locked in
portrait on larger screens. Tested on a tablet-sized device — the app was not
broken, but buttons stretched the full width of the screen and looked
unfinished. Fixed so the layout stays a sensible column at any size. Phones are
unchanged.

---

### It has been security-reviewed

Two passes on the build you are holding: one reading the app as a file, one
running it.

Four things came out, all small, **none of them affecting what you will see**:
a screen meant only for developers was still inside the app (switched off and
unreachable, but it should not have been there); a configuration file was
carrying internal notes about our own website that nobody needed; and two
issues with how we *check* the app rather than with the app itself — one where
a test run could report "all passed" while quietly skipping the most important
test.

The first three are fixed. The fourth is a decision about our own process.

Worth saying because it is the point of doing this: the checking found
problems with the checking. That is what you want a review to do.

## What is left

Three things. **Two of them are decisions, not work.**

| | What | Who |
|---|---|---|
| 1 | **The signing key** for the Play Store. Standard, one-off, and it has to come from DGD — it is the credential that proves future updates are genuinely from us, so it is not something an outside machine should ever hold. | DGD |
| 2 | **A question about invites.** See below. | DGD |
| 3 | **The arcade's server** needs a home. Built and tested; not yet hosted. | backend |

### The invite question, in plain terms

App store rules prohibit paying people — in cryptocurrency or anything
convertible to it — for tasks like getting others to download an app.

The arcade is fine: XP and badges, stated on screen to have no monetary value.

The question is about the **invite links on the main app**:

> Does anyone receive DGD, or anything that can be turned into DGD, for
> referring someone — on the website, off-app, by hand, or at any point later?

**Answered on 21 September: yes.** Referrals do earn DGD.

So this is now a decision rather than a question, and it is the one thing that
changes what the app does rather than just when it ships. Apple's rule names
"encouraging other users to download" specifically, and our Display QR is an
app-download link with a referral code attached — which is close enough to the
rule's own wording that we should not plan on talking our way past it.

The realistic choices are to take the invite feature out of the app (the
website keeps it), or for referrals to stop paying in DGD. Neither is an
engineering problem — removing the feature is about half a day — and the call
sits with DGD and its legal advisers, not with the build.

**What this means for timing:** iOS is the constrained side. Android is
probably unaffected, but that word is doing real work and it needs checking
rather than assuming.

---

## iOS

The iOS app is the same ticker and the same member preview, and it now matches
Android on the removed chart.

**It does not have the arcade yet.** That was a deliberate call: get this
version reviewed first, add the arcade when the backend work happens. So iOS is
the full ticker without the game.

Screenshots are being captured and will be added here.

---

## Where things stand overall

The build is in good shape. The engineering work that remains is the arcade's
server, and that is waiting on hosting rather than on code.

The honest summary: **nothing about the app is holding up a submission.** A
signing key and an answer about invites are.

---

*Questions about anything above are welcome. The technical detail sits in
`STORE-READINESS-2026-09-20.md`; backend and credential matters are in a
separate document held by backend engineering.*
