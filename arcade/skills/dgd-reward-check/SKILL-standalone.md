---
name: dgd-reward-check
description: Decide whether a proposed DGD reward, prize, bonus, airdrop, referral payout, leaderboard prize, or "credit" can ship, and what it would cost. Use this whenever anyone asks whether users can earn, be paid, be rewarded, or be credited DGD — or points, credits, tokens, or anything convertible to DGD — for playing games, taking quizzes, referring friends, inviting people, signing up, posting to social, topping a leaderboard, or any other activity. Also use it whenever someone proposes moving a reward off-app, onto the website, into the browser, or simply "not mentioning it in the app" in order to make it acceptable, or proposes syncing app progress to a web reward. Covers Apple App Store guideline 3.1.5(v) and the DGD decisions already recorded. Use it even when the question sounds purely commercial or purely technical, because the answer almost always turns on where the earning happens rather than where the money moves.
---

# dgd-reward-check

*Can we reward DGD for this?*

This skill answers one recurring family of questions at Digital Gold: *may we
give users DGD (or anything convertible to it) for doing something?*

It exists because the same wrong intuition keeps producing the same wrong
answer. The intuition is that the problem is **where the payout settles**, so
moving the payout — to the website, to a browser, to a manual process, to a
thing with a different name — should fix it.

It does not. **The test is whether activity in the app is what earns the
reward.** Hold onto that and every version of the question becomes tractable.

## Not legal advice, and where that bites

You can settle the *structure* of a proposal with confidence: which bucket it
falls in, what would make it clean, what it costs. You cannot settle whether
DGD's referral programme is lawful, whether DGD is security-like, or how a
prize is taxed. Say which is which, plainly, and name counsel for the second
kind rather than producing a confident-sounding guess.

Do not tell anyone Apple "will" approve or reject something. Describe exposure,
not outcomes.

## The three questions

Ask them in order. They decide the answer.

1. **Does anything of value change hands?** DGD, anything convertible to DGD,
   money, goods, discounts, priority access, allocation weighting. "Later",
   "manually", "at a redemption" and "as airdrop weighting" all count as yes.
2. **Is activity in the app any part of what earns it?** Playing, scoring,
   completing a level or quiz, referring from the app, progress synced out of
   the app.
3. **Does the app carry, describe, or enable the earning?** A referral code,
   link, QR, share button, "invite and earn" copy — or any attribution signal
   that lets the server know a visitor came from the app.

| Answers | Where it stands |
|---|---|
| 1 = no | **Fine.** No exposure. Apply the vocabulary rules below. |
| 1 = yes, 2 and 3 both no | **Off Apple's turf.** Still counsel's on prize law, tax, securities. |
| 1 = yes, and 2 or 3 = yes | **Exposed under 3.1.5(v).** Say so and give the cheapest way out. |

Appendix C below holds the verbatim guideline. Read it before quoting.
Never paraphrase a guideline as though quoting it — the exact words are what
the argument turns on, and the appendix records what was checked and when.

## Then look up whether it has already been answered

Six versions of this question have been worked through and recorded.
**Appendix A** holds them. Read it before answering — if the proposal matches
one, say so and give the recorded reasoning rather than re-deriving it, which risks
landing somewhere subtly different and undermining a decision already taken.

**Appendix B** holds the engineering facts that constrain answers — what the
app actually emits, what the arcade server actually trusts, what the on-screen disclaimers actually say. Check it before asserting anything about
how the app behaves. Several proposals that sound fine collide with one of
these, and the collision is usually the most useful thing you can tell someone.

## The traps

These are the ways a proposal looks clean and is not. Each has been hit at
least once.

**Attribution plumbing.** Play's Install Referrer API, deferred deep links,
Branch/Adjust/AppsFlyer-style SDKs, fingerprinting handoffs. Any of these lets
the site know a visitor came from the app, which means app activity is feeding
the reward through a pipe nobody thought of as a referral feature. When a
proposal depends on the app and the site being unlinked, say that "no
attribution path, of any kind" is a positive engineering requirement, not just
an absence.

**A disclaimer that becomes false.** The arcade states on screen that XP and
badges have no monetary value. If a proposal makes that untrue, it is worse
than silence — a contradicted disclaimer reads as concealment. Flag it every
time; people propose this without noticing.

**"We just won't mention it in the app."** Three problems, and they compound:
an unmentioned reward drives no engagement, so it defeats its own purpose; it
cannot stay unmentioned, because it gets announced on the site or socials and
winners talk; and it usually requires the disclaimer above to be false.

**"We won't disclose it at all."** Not a stronger version of the above — a
different category. Hiding a reward from users or App Review moves the exposure
from the app to the developer account (2.3.1 and 5.6, Appendix C). Do not
help design a reward to be concealed from users or reviewers. Say so once,
plainly, without lecturing, and go straight to the disclosed versions.

**A marker the user can delete.** Adding `&src=app` to a URL the user copies to
their clipboard makes a claim that any motivated user can falsify. Worse than
not making the claim.

**Renaming.** "Validation credits", "points", "rewards", "recognition tokens".
Substance governs. If it converts, at any point, by any route, it is the same
question with one step added. A thing designed to *feel* like it accrues value
while being *called* something else carries the compliance exposure **and** the
user disappointment of turning out to be worthless.

**Skill versus chance.** That distinction comes from gambling law. 3.1.5(v) does
not mention chance and is not a gambling rule — it says "completing tasks", and
clearing a level is a task. Where skill matters is §5.3, and there it cuts the
other way. Do not let a skill framing carry weight it cannot bear.

**Progress carryover, and its direction.** Web → app display, read-only, is
fine: recognition flows in, value never flows out. App → web earning is the
problem, and it is worse than an argument about payout location, because the
sync is a deliberate mechanism somebody built and documented.

## How to answer

Lead with the verdict. People are asking because they want to plan.

```
**Short answer:** <yes / no / yes-if>

**Why** — the one structural reason, in two or three sentences.

**What would make it clean** — the concrete change, and roughly what it costs.

**What this does not settle** — the parts that are counsel's, named as theirs.
```

**Match the length to the answer.** A proposal where nothing of value changes
hands is a plain yes and deserves a few sentences plus any condition that keeps
it in that bucket — not a structural analysis. Reserve the full shape above for
proposals that are exposed or conditional. This skill is not a reason to
manufacture concern, and a long answer to an easy question teaches people not to
ask.

When a proposal is not fine, always offer the cheapest thing that works rather
than only the objection. There is almost always a version that gets most of the
product benefit: non-monetary recognition in the app, real value on the web,
read-only display of web standing.

## Vocabulary, when writing anything user-facing

The arcade's compliance language is settled and worth keeping consistent: XP,
badges, expedition, tablet. Not "earn", "cash", "dollars", "prize" or "win
money". The current on-screen line is *"Educational only. XP and badges have no
monetary value."* Keep it true.

The arcade plan also bars prize-style celebration — coin showers, jackpots,
casino visuals — and that is enforced in the build rather than left to a
reviewer's eye. Do not propose adding them back as a "feel" improvement.

## Recording the answer

If the question is new — not in Appendix A — and you have the AmbassadorAI repo to
hand, append the reasoning to `arcade/B1-DECISION-2026-09-21.md` under a dated
heading and copy the file to `backend-package/`. That document is what
counsel and backend read, and an answer that lives only in a chat gets asked
again in a fortnight.

Do this as a quiet housekeeping step *after* answering. It is bookkeeping, not
part of the answer — the person asked about their proposal, not about document
management. If you have no write access, or you were asked not to touch files,
just leave it; do not explain the omission or add a note about what someone else
should file. One line at most, and only if the file was actually written.

## If the answer depends on guideline text you do not have

Appendix C holds what was verified, with the date. Guidelines
change. If the proposal turns on wording not in that file, fetch the live
guidelines at `https://developer.apple.com/app-store/review/guidelines/` and
quote from what you read, and say that you checked it live.
Saying "I did not check that clause" is a fine answer; recalling it is not.

---

# Appendix A — Six versions of the question, already answered

Each of these was worked through and recorded in
`arcade/B1-DECISION-2026-09-21.md`. If a new proposal matches one, use the
recorded reasoning rather than re-deriving it.

### 1. Referrals pay DGD — the original problem (answered 21 Sep 2026: yes, they do)

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

### 2. Skill-based game or quiz awards (answered 21 Sep 2026: no help)

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

### 3. DGD to top scorers, off-app, not mentioned in the app (answered 21 Sep 2026: weakest version)

Stronger than the referral case in one way — no download-encouragement element.
**Weaker in the way that matters:** the rewarded activity happens entirely
inside the app. A referral at least has an off-app leg; a top score has none.

"Not mentioned in the app" makes it worse, not safer:

- The arcade states XP and badges have no monetary value. Converting scores to
  DGD makes that **false** — a contradicted disclaimer reads as concealment.
- Unmentioned means no engagement value, which defeats the purpose.
- It cannot stay unmentioned: it gets announced on the site or socials, and
  winners talk.

Plus **R2** (see Appendix B): scores are client-asserted, so a top-scorer
prize goes to whoever edits the request first.

### 4. Move the arcade to the web, pay DGD in the browser, carry app progress over (answered 25 Sep 2026: first half clean, carryover self-defeating)

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

### 5. Signup, verification and referral earnings entirely online, separate from any app activity (answered 25 Sep 2026: yes — recommended)

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

### 6. Validation credits, not disclosed at all (answered 26 Sep 2026: no — declined as a design request)

The only recorded version that puts the **developer account** at risk rather
than the app. 2.3.1(a) prohibits hidden or undocumented features; 2.3.1(b) and
5.6 escalate dishonest or manipulative conduct to program removal.

It also does not work: credits are either visible (disclosed) or invisible (no
behavioural effect); DGD payouts leave a trail; and it falsifies the arcade
disclaimer while concealing from users what they are accruing.

Disclosed alternatives: non-convertible credits described like XP (fine), or a
DGD-paying validation programme on the website with the app uninvolved (Path A
shape).

---

# Appendix B — What the app and server actually do

Facts as of **Android 1.0.6 / iOS 1.0.5 (26 September 2026)**. Check these before asserting
anything about how the app behaves — several proposals that sound fine collide
with one of them, and the collision is usually the most useful thing to say.

### What the app emits

**Android 1.0.6 (26 Sep 2026) emits no referral URL at all** — Path A is
shipped there. Invite Friends sends one fixed message (no username, code or
link) and shows one QR for everyone, `https://digitalgold.co/app`. No
friend's-username field, no Copy Invite Link/Code, no "your username is your
invite code" wording, no App Links, and upgraded installs delete the old
`dgd.friendCode` key. `ReferralSurfaceGuardTest` fails the build if any of it
comes back.

**iOS still carries the 1.0.5 surface until the Mac applies
`integration/IOS-PATH-A-CHANGE-REQUEST.md`:** Copy Invite Link
(`/signup?ref=USERNAME`), a per-user QR (`/app?ref=USERNAME`), Copy Invite
Code, the friend field, and Universal Links that capture `?ref=`. Until that
lands, answer iOS questions against the old surface.

**The username *is* the invite code** on the website. This is why the
leaderboard cannot show DGD usernames — doing so would publish invite codes.

### What the arcade server trusts — R2

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

### Identity and the leaderboard decision

The arcade uses **assigned handles** and deliberately does not know the DGD
username. That is what makes the in-app anonymity statement true and what keeps
the Play Data Safety declaration accurate.

Any proposal that links arcade activity to a DGD account reopens this. It is a
Data Safety change, not just a feature.

### On-screen text that must stay true

- Arcade: **"Educational only. XP and badges have no monetary value."**
- Member preview: marked **PREVIEW · NOT LIVE** throughout. Creates no account,
  takes no payment, delivers nothing.
- `apple/APP_STORE_REVIEW_NOTES.md` asserts the app does not pay for inviting —
  true of the app, and materially incomplete as a description of the programme
  now that referrals pay DGD. Removing invites makes it straightforwardly true
  again.

### Enforced compliance decisions

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

### What is still outstanding, so nobody promises a date

- The B1 decision itself — DGD and counsel.
- Backend's Path C questions, chiefly the unforgeable app-origin signal (moot
  under Path A).
- The Play Store signing key, which is DGD's to hold.
- Hosting for the arcade server.
- iOS screen captures.

---

# Appendix C — Verbatim guideline text

**Verified 21 September 2026** against
`https://developer.apple.com/app-store/review/guidelines/`.

Guidelines change without notice. If a proposal turns on wording that is not
here, fetch the live page, quote what you read, and say you checked it live. "I did not check that clause" is a fine answer; recalling one is not.

---

### 3.1.5(v) — the clause this is all about

> "Cryptocurrency apps may not offer currency for completing tasks, such as
> downloading other apps, encouraging other users to download, posting to social
> networks, etc."

Two features of the text do most of the work:

- **"completing tasks"** — not "completing tasks by chance". Clearing a level or
  answering a quiz question is a task in ordinary English.
- **"etc."** — the list is illustrative, not exhaustive. The three named
  examples are promotional, which is why referrals were the sharpest case, but
  nothing confines the rule to promotion.

### 3.1.5(i) and (iii) — wallets and exchanges

Apps that store, transmit or exchange cryptocurrency carry organisation
enrolment and licensing requirements. Relevant because an app that *distributes*
DGD starts to look like one of these, which is a second front beyond (v).

### 2.3.1 and 5.6 — hidden features and the Developer Code of Conduct

*Verified 26 September 2026.*

2.3.1(a) opens: *"Don't include any hidden, dormant, or undocumented features in
your app."* It goes on to require that functionality be clear to end users and
to App Review, and that new features be described specifically in the review
notes — generic descriptions are rejected.

2.3.1(b) makes egregious or repeated behaviour grounds for removal from the
Developer Program. 5.6, the Developer Code of Conduct, says repeated manipulative
or misleading behaviour leads to removal, that apps must not engage in
manipulative practices within or outside the app, and that non-compliance means
account termination.

Why it matters here: a disclosed reward programme risks a rejection of one app.
A concealed one risks the account — every app, update and future submission.

### 5.3.1 / 5.3.2 — contests and sweepstakes

A contest or sweepstakes must be sponsored by the developer, and its official
rules must appear in the app, stating that Apple is not a sponsor or involved in
the activity.

### 5.3.4 — lotteries

> "Lottery apps must have consideration, chance, and a prize."

This is where skill-versus-chance genuinely matters: removing chance stops
something being a lottery. It does nothing about 3.1.5(v), which is the usual
confusion.

---

### Google Play — what was and was not established

Apple's clause is explicit. **No equivalent explicit clause was found in Play
policy**, and Play does host crypto apps with referral programmes.

Do not treat that as clearance. Store listings are not policy text. The
conclusion recorded on 21 September was that Play's Financial Services and
incentivised-installs policies need checking directly by counsel before Android
is treated as clear — and that "Android is probably not blocked" has the word
"probably" doing real work in it.

If someone asks for the Android position, give them that, not a guess.
