---
tags: [dgd, subject, supply, distribution]
updated: 2026-07-19
source: Digital Gold White Paper §5, §8, §9 · digitalgold.co (live model, verified 2026-07-19)
---

# Supply, Distribution & Circulation

How DGD coins are released and how the design tries to make the coin actually *circulate* as money.

> Present the mechanics as **design**. The dollar figures describe how the curve works, not what anyone will earn. See [do & don't language](../compliance/do-and-dont-language.md).

> **⚠️ Changed 2026-07: releases go to FUNDED accounts, not all users.** Earlier versions of this
> page said releases were "split equally among all current users." The live model on
> digitalgold.co distributes only to accounts holding an **active validation balance**. The White
> Paper anticipated exactly this in §5.6 ("*if the design were later changed to exclude
> zero-balance users, the only change would be the divisor*"). If you published content using the
> old wording, it overstates who receives coins — correct it.

## Proof of Participation: continuous distribution

Most coins concentrate supply among early insiders or large "whales." DGD instead releases coins
**continuously as the network grows**, driven by one number: **`N`, the count of confirmed network
accounts** (WP Abstract, §5).

There are **no discrete levels or tiers** (WP §5.1). The curve is continuous.

What happens each time someone joins:

1. A new account is confirmed → `N` increases by one.
2. The protocol advances the price one step along a **fixed published curve**.
3. A small number of coins is released from the treasury and **split equally across accounts with
   an active validation balance** — every funded account receives the *same amount*.
4. Coins are delivered **immediately** to the participant's **QT wallet**, not to their web account.

Because the release is split across the funded base, the amount per account **shrinks** as the
network grows. Near `N` = 1,000 a signup releases about **88.69 coins**; near the target it
approaches zero. Per-signup releases across the whole journey sum to exactly **11,712,952 coins**
(WP §5), carrying circulating supply from 7,287,048 to 19,000,000.

### Who receives — and who doesn't

| | Receives from a release? |
|---|---|
| Account with an active validation balance | **Yes** — the same amount as every other funded account |
| Account with no balance | **No** |
| Larger balance | **Same amount per release** — a bigger balance lasts *longer*, it does not pay *more* |
| Referrer | Referral recognition is **separate**; it never changes release amounts |

**Unclaimed coins are not redistributed.** They remain in / return to the Foundation treasury
(WP §5.6). Your share does **not** grow because someone else failed to validate — this is the
single most tempting wrong inference, and stating it would be false.

## The published curve

| Accounts | Price | Release at that point |
|---|---|---|
| 1,000 | $3.40 | 88.6858 DGD |
| 10,000 | $27.73 | 19.3349 DGD |
| 100,000 | $226.12 | 4.2164 DGD |
| 1,000,000 | $1,843.58 | 0.9195 DGD |
| 10,000,000 | $15,031.06 | 0.2005 DGD |
| 80,000,000 | $100,000.00 | 0.0507 DGD |

At 80 million accounts, **19 million coins** are circulating and release **ends permanently**.

> ⚠️ The $3.40 → $100,000 curve is a **distribution mechanism, not a forecast.** "Get in early
> before it hits $100k" is a compliance violation. Say instead: *"The price moves along a
> published curve as the network grows — it's set by the protocol, not by trading."*
>
> The $100,000 figure is also a **conditional maximum**, not a destination. It only arises if
> adoption, transactions, transaction value **and** developer activity all scale together. The
> framework explicitly **does not guarantee price appreciation**, and the published price can
> fall if metrics deteriorate. See [CFV & DGSB](valuation-cfv-dgsb.md).

## Total supply allocation — 21,000,000 DGD

| Allocation | Amount | Share |
|---|---|---|
| Community distribution + staked treasury | 13,712,952 DGD | 65.3% |
| NotFiat, LLC retained treasury | 5,000,000 DGD | 23.8% |
| Founding team, developers, beta testers | 2,287,048 DGD | 10.9% |

Of the 21M, **19M is the maximum that can ever circulate**. The remaining **2,000,000 is
permanently locked** in the treasury for staking — non-circulating, and there to make a 51% attack
impractical. Staking rewards and all transaction fees are **burned**, so supply can only decrease.

(The community figure of 13,712,952 = the 11,712,952 of per-signup releases **plus** the 2,000,000
staking lock. Both numbers are correct; they're counting different things.)

## How validation works mechanically

- Participants fund a **DigitalGoldX** web account at **digitalgold.co** with **ERC-20 USDC or
  USDT** — **$20 minimum, $500 current cap** (the cap is a policy setting and can change).
- Checkout shows an **Estimated DGD** figure before payment. It can shift slightly if more accounts
  confirm before the payment clears.
- The balance is drawn down as releases occur, and **earns for as long as it lasts**. When it's
  exhausted, that account stops receiving until it's funded again.
- Delivered coins land in the participant's **QT wallet** — self-custody, keys held by the
  participant, and they arrive even if the web account is unavailable (WP §5.6).

**The web account and the wallet are different things.** The account is the validation interface;
the wallet is custody. Getting this distinction right matters — it's the most common point of
confusion for newcomers, and it's also the heart of the self-custody story.

## Single-price architecture (the circulation engine)

Here's the design idea that distinguishes DGD from every other coin (WP §8, §9):

- Every other coin has a fluctuating **bid/ask** price. A merchant who accepts it faces a choice:
  hold and eat the volatility, or convert to dollars immediately. The rational merchant converts —
  so **the coin transacts once and exits**. It never became money.
- DGD eliminates bid/ask trading via **cooperating-venue exclusivity agreements**, producing a
  single published price. A merchant can **hold** DGD and **pay suppliers** in DGD. The supplier
  does the same. The chain continues link by link.

When the chain runs all the way to the raw-material owner, "DGD has become money" in the
operational sense (WP Abstract, §9).

**The lumber example (WP §10):** the White Paper walks dimensional lumber from retail point-of-sale
back through wholesaler, manufacturer, and raw-material extraction. Concrete, visual, and excellent
video material.

## Teaching angles

- **"Why most crypto payments aren't really money"** (the convert-to-dollars problem)
- **"A currency where everyone participating gets the same amount"** (equal-per-funded-account split)
- **"The whale problem, and one attempt to fix it"** (continuous vs. front-loaded distribution)
- **"A bigger balance doesn't get you a bigger share — it just lasts longer"** (counter-intuitive, true, and safely non-promotional)

## Connects to
- [Six Pillars](six-pillars.md) (Adequate Circulation, Scarcity) · [Participation pathways](participation-pathways.md)
- [Valuation: CFV & DGSB](valuation-cfv-dgsb.md) · [Platform & tools](platform-and-tools.md) · [Glossary](glossary.md)
