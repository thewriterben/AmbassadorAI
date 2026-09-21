# B1 and B3 — the category defence, and linking out to buy

**2026-09-21.** Written after the Path B decisions: **the arcade stays in the
binary, and Finance stays as the primary category.** Both of these are
positions to be argued at review, not code. I am not a lawyer and this is not
legal advice; it is the engineering read of published guidelines, with the
current text checked today rather than recalled.

---

# B3 — "Get Digital Gold" and the outbound purchase link

## The position has moved, and in your favour

The readiness doc flagged this as a HIGH risk on the assumption that Apple's
anti-steering rules still bit. **On the US storefront they largely do not.**

Following the Epic injunction, Apple updated the guidelines in May 2025:

- **3.1.1** — on the United States storefront there is no prohibition on an
  app including buttons, external links or other calls to action, and **no
  entitlement is required**.
- **3.1.3** — the prohibition on encouraging users to use a purchasing method
  other than in-app purchase does not apply on the US storefront.

So a "Get Digital Gold" button that opens `digitalgold.co` is, today, a normal
thing for a US-storefront app to do.

## Three caveats that matter

1. **It is storefront-specific.** Outside the US the older regime still
   applies: you need the External Link Account entitlement, or the
   StoreKit External Purchase Link APIs, with their disclosure sheets. If the
   app ships worldwide, the button's behaviour has to vary by storefront, or
   the app has to be US-only at launch.
2. **It is under appeal.** Apple changed the text to comply with a court order
   while appealing it. A position that rests on an injunction can move.
   Anything built here should be easy to put back behind an entitlement.
3. **It does not make the destination safe.** Anti-steering was never the only
   rule in play. What the user finds at the other end — a purchase flow for a
   cryptocurrency — is judged under 3.1.5, below.

## What this means for Path B

Keep the button, point it at the web, and do not build an in-app purchase
path. That was already the plan; the difference is that it is now the
low-risk option rather than the risky one. Worth telling Oleksandr, because
his review predates none of this — but his framing assumed the stricter rule.

---

# B1 — Finance, and the 3.1.5(v) defence

## The rule, verbatim

> **3.1.5(v)** Cryptocurrency apps may not offer currency for completing
> tasks, such as downloading other apps, encouraging other users to download,
> posting to social networks, etc.

Note what it names: *encouraging other users to download*. That is a referral
programme, described exactly.

## The defence that already exists, and still holds

DGD's review notes argue the app "does not award currency in-app". With the
arcade in the same binary, that sentence has to cover the arcade too, and it
does:

- **XP is not currency.** It cannot be exchanged, transferred, redeemed,
  withdrawn or bought. It has no price and no counterparty.
- **It is not issued for tasks of the kind the rule names.** XP comes from
  playing a match-3 game. Not from downloading apps, not from posting, not
  from recruiting.
- **The app says so, on screen.** The arcade home carries *"Educational only.
  XP and badges have no monetary value."*
- **The server is authoritative and capped**, which is what stops XP behaving
  like a balance someone could farm.

That is a good defence and I would sign it.

## The exposure that is *not* the arcade

**The referral system is the sharper edge, and it is on the ticker side.**

The app encodes `?ref=USERNAME` in invite links and has a Copy Invite Link
flow. The arcade's XP is not currency — but the question a reviewer will
actually ask is:

> *Does a user who invites someone through this app end up with DGD?*

If digitalgold.co credits referrers with Digital Gold — the actual
cryptocurrency — for signups arriving on an app-generated `?ref=` link, then
the app is a funnel for exactly the arrangement 3.1.5(v) describes, and the
fact that the reward is granted on the website rather than in the app is not
obviously a defence. This is contested enough that there is a standing Apple
Developer Forums thread asking whether crypto referral programmes always
violate 3.1.5(v).

**Nobody here knows the answer, because it is a question about DGD's
business, not about this code.** It needs a direct answer before submission:

> Does any user receive DGD, or anything convertible to DGD, as a result of a
> referral — whether credited on the site, off-app, manually, or at any later
> date?

If **no**, the defence is clean and the referral system is just a signup
attribution mechanism; say so explicitly in the reviewer notes.

If **yes**, the referral reward and the app need separating before
submission. That is a product change, and a bigger one than anything in
track B.

## Finance, not Games

The decision is Finance. The reasoning, for the record:

- The app's primary purpose under Path B genuinely is an informational
  ticker. Category should describe the app's purpose, and this one does.
- `project.yml` already declares `public.app-category.finance`, and the review
  notes are written around it. Changing to Games rewrites all of that.
- Games would place a live USD cryptocurrency price inside a game, which
  invites the crypto question from a worse angle — and the 3.1.5 family
  applies either way, so the category does not buy an exemption.

The cost is the honest one: a game catalogue in a Finance app is unexpected,
and a reviewer will look at it. Which is why the notes below lead with it
rather than burying it.

## Draft additions to the reviewer notes

Offered as text to adapt, not to paste unread. Someone at DGD has to be
willing to sign their name under it.

> **About DGD Arcade**
>
> This app includes DGD Arcade, an educational match-3 game about the history
> of money. It is reached from a single entry point on the home screen and is
> optional; the app's primary purpose is the informational price and network
> ticker described above.
>
> The arcade awards XP and badges for completing levels. **XP is not currency
> and is not Digital Gold.** It cannot be exchanged, transferred, redeemed,
> withdrawn, sold or bought; it has no monetary value and no counterparty.
> It is a score. The arcade states this on screen: "Educational only. XP and
> badges have no monetary value."
>
> XP is awarded only for playing the game. It is not awarded for downloading
> other apps, for inviting other users, for posting to social networks, or for
> any other task of the kind described in Guideline 3.1.5(v).
>
> The app does not sell, buy, trade, transfer, custody or mine cryptocurrency.
> It does not contain a wallet. [Purchases of Digital Gold happen on
> digitalgold.co, outside the app.] Any Digital Gold a user holds is held in
> self-custody in the desktop QT wallet, which is not part of this app.

The bracketed sentence is where the B3 question lands: keep it if the button
links out, and be sure the referral answer above is settled before it goes in.

## Age rating

Not previously tracked, and it changes under Path B: one binary now contains a
game *and* cryptocurrency content. The IARC questionnaire has to be answered
for the combined app, and the answers will not be the ones given for a ticker
alone. Cheap to get right, awkward to get wrong.

---

*Related: `STORE-READINESS-2026-09-20.md` §5 (B1, B3),
`NATIVE-SOURCE-REVIEW.md` (the category analysis this builds on).*

Sources checked 2026-09-21:
[Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) ·
[Guidelines updated for Epic anti-steering, May 2025](https://appleinsider.com/articles/25/05/02/apples-app-store-guidelines-updated-to-reflect-court-order-over-external-purchases) ·
[Apple allows external purchase links in the US](https://www.iclarified.com/97192/apple-updates-app-store-rules-to-allow-external-purchase-links-in-us) ·
[Guideline 3.1.5 explained](https://acceptmy.app/guidelines/3-1-5-cryptocurrencies) ·
[Are crypto referral programmes always a 3.1.5(v) violation?](https://developer.apple.com/forums/thread/693770)
