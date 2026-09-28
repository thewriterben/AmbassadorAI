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

Read `references/rule-text.md` for the verbatim guideline before quoting it.
Never paraphrase a guideline as though quoting it — the exact words are what
the argument turns on, and the file records what was checked and when.

## Then look up whether it has already been answered

Seven versions of this question have been worked through and recorded. Read
`references/precedents.md` before answering — if the proposal matches one, say
so and give the recorded reasoning rather than re-deriving it, which risks
landing somewhere subtly different and undermining a decision already taken.

`references/app-facts.md` holds the engineering facts that constrain answers —
what the app actually emits, what the arcade server actually trusts, what the
on-screen disclaimers actually say. Check it before asserting anything about
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
from the app to the developer account (2.3.1 and 5.6, in `references/rule-text.md`). Do not
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

If the question is new — not in `references/precedents.md` — append the
reasoning to `arcade/B1-DECISION-2026-09-21.md` in the AmbassadorAI repo, under
a dated heading, and copy the file to `backend-package/`. That document is what
counsel and backend read, and an answer that lives only in a chat gets asked
again in a fortnight.

Do this as a quiet housekeeping step *after* answering. It is bookkeeping, not
part of the answer — the person asked about their proposal, not about document
management. If you have no write access, or you were asked not to touch files,
just leave it; do not explain the omission or add a note about what someone else
should file. One line at most, and only if the file was actually written.

## If the answer depends on guideline text you do not have

`references/rule-text.md` holds what was verified, with the date. Guidelines
change. If the proposal turns on wording not in that file, fetch the live
guidelines at `https://developer.apple.com/app-store/review/guidelines/` and
quote from what you read — then add it to the reference file with the date.
Saying "I did not check that clause" is a fine answer; recalling it is not.
