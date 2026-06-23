---
tags: [dgd, subject, supply, distribution]
updated: 2026-06-16
source: Digital Gold White Paper §5, §8, §9
---

# Supply, Distribution & Circulation

How DGD coins are released and how the design tries to make the coin actually *circulate* as money.

> Present the mechanics as **design**. The dollar figures describe how the curve works, not what anyone will earn. See [do & don't language](../compliance/do-and-dont-language.md).

## Proof-of-Participation (PoP): continuous distribution

Most coins concentrate supply among early insiders or large "whales." DGD instead releases coins **continuously as the network grows**, driven by one number: **`N`, the current total number of users** (WP Abstract, §5).

How it works each time someone joins:
1. A new user signs up → `N` increases by one.
2. The protocol advances the price one step along a **fixed curve**.
3. A small number of coins is released from the treasury, **split equally among all current users** (WP Abstract).

Because the per-user share is split across everyone, the number of coins released per signup **shrinks** as the network grows. The very first signup (when `N` is near 1,000) releases about **88.6 coins**; near the target it approaches zero (WP §5). The per-signup releases across the whole journey sum to exactly **11,712,952 coins** (WP §5).

| Milestone | Value (WP) |
|---|---|
| Starting users | 1,000 |
| Target users | 80,000,000 |
| Starting price | ~$3.40 |
| Ending price | $100,000 |
| Max circulating supply at target | 19,000,000 |
| Coin release after target | Ends permanently |

At 80 million users, exactly **19 million coins** are in circulation and release **ends forever** (WP Abstract, §5).

> ⚠️ The $3.40→$100,000 curve is a **distribution mechanism**, not a forecast. Saying "get in early before it hits $100k" is a compliance violation. Say instead: *"The price moves along a fixed curve as the network grows — it's set by the protocol, not by trading."*

## How participation works mechanically (for accurate explainers)

- Participants use a **DigitalGoldX** web account as the interface to "validate" as the network grows; they pre-load funds and validate up to their per-user share each release (WP §5, §10).
- Validated coins are delivered to the participant's **QT wallet**, which only they control — coins arrive even if the web account is unavailable (WP §5).
- There's a **$20 minimum entry threshold** (WP §12.14). Partial validation is possible if a balance only covers part of a share.

You don't need to teach all the mechanics in a video — but get them right if you do.

## Single-price architecture (the circulation engine)

Here's the design idea that distinguishes DGD from every other coin (WP §8, §9):

- Every other coin has a fluctuating **bid/ask** price. A merchant who accepts it faces a choice: hold and eat the volatility, or convert to dollars immediately. The rational merchant converts — so **the coin transacts once and exits**. It never became money.
- DGD eliminates bid/ask trading via **cooperating-venue exclusivity agreements**, producing a single stable price. A merchant can **hold** DGD and **pay suppliers** in DGD. The supplier does the same. The chain continues link by link.

When the chain runs all the way to the raw-material owner, "DGD has become money" in the operational sense (WP Abstract, §9).

**The lumber example (WP §10):** the White Paper walks through dimensional lumber from retail point-of-sale back through wholesaler, manufacturer, and raw-material extraction to show what full supply-chain circulation looks like. This concrete example makes excellent video material.

## Teaching angles
- **"Why most crypto payments aren't really money"** (the convert-to-dollars problem)
- **"What if everyone who joined a currency got a share — automatically?"** (PoP split)
- **"The whale problem, and one attempt to fix it"** (continuous vs. front-loaded distribution)

## Connects to
- [Six Pillars](six-pillars.md) (Adequate Circulation, Scarcity) · [Participation pathways](participation-pathways.md)
- [Valuation: CFV & DGSB](valuation-cfv-dgsb.md) · [Glossary](glossary.md)
