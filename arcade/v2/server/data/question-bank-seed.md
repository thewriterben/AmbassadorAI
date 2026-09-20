---
title: Knowledge Tablet question bank — seed set
updated: 2026-09-06
source: LLMWiki/dgd/* (White Paper section refs as cited there)
rules: every item must trace to a wiki page; no price forecasts; distractors = known misconceptions
---

# Knowledge Tablet question bank — seed set (40 items)

Format: `Tier | Pillar/Topic | Question | Correct | Distractors | Explanation shown after answer | Source`

Tiers: **A** definitions · **B** mechanics · **C** misconception traps · **D** numbers/sections.
Each item ships with ≥2 paraphrase variants in production; only the base wording is listed here.
Numbers marked ⚠ are snapshots that move — serve from config, not hard-coded.

> **Platform change pending (Sept 2026):** validated new accounts will receive **$21 of validation
> credit at signup**. Items about funding with USDC/USDT and the $20 minimum (⚠) must be re-authored
> from the platform's final wording before launch; release-mechanics items are unaffected.

## Six Pillars (six-pillars.md)

| Tier | Topic | Question | Correct | Distractors | Explanation | Source |
|---|---|---|---|---|---|---|
| A | Pillars | How many "pillars of perfect money" does the framework describe? | 6 | 4 · 8 · 12 | Scarcity, Stable Pricing, Free Adoption, Decentralized Governance, Freedom to Transact, Adequate Circulation. | WP §2.2 |
| A | Scarcity | Which pillar says supply must be limited by transparent, predictable rules? | Scarcity | Stable Pricing · Free Adoption · Adequate Circulation | DGD's answer is a fixed 21M cap. | WP §2.2 |
| A | Free Adoption | "Money must be chosen, not imposed by decree" describes which pillar? | Free Adoption | Decentralized Governance · Freedom to Transact · Scarcity | Participation is voluntary. | WP §2.2 |
| A | Freedom to Transact | Which privacy technology does DGD integrate natively? | Tor V3 onion addressing | Zero-knowledge proofs · Mixers · VPN routing | Encrypted, anonymous transactions without permission from an intermediary. | WP §2.2 |
| B | Adequate Circulation | According to the framework, when does a coin "become money" in the operational sense? | When it flows link by link through the supply chain to the raw-material owner | When it's listed on an exchange · When a merchant accepts it once · When its market cap passes Bitcoin's | A coin converted to dollars after one payment was only a payment instrument. | WP Abstract, §9 |
| B | Decentralized Governance | Why does the White Paper call DGD's governance an "inversion of governance"? | The rules were fixed at inception and can't be changed, so there is nothing to govern | Token holders vote monthly · The Foundation can veto changes · Governance moves to validators later | "Rules rather than discretion." | WP §12.14–12.15 |
| C | Stable Pricing | True or false: the Stable Pricing pillar means DGD's price can never go down. | False | True | The framework explicitly does not guarantee appreciation; after distribution the CFV can produce a lower price. | WP §11.2 |
| D | Scarcity | Roughly how much has the US dollar lost in purchasing power since 1913, per the White Paper? | More than 96% | About 50% · About 75% · About 30% | Cited in the Abstract. | WP Abstract |
| D | Scarcity | US money supply grew from about $3 billion in 1913 to over $21 trillion — that is roughly a: | 7,000-fold increase | 7,000% increase · 70-fold increase · 700% increase | Wiki flags that "7,000 percent" is a misstatement; the math is ~7,000× (~700,000%). | six-pillars.md note |
| D | Stable Pricing | At a 2% inflation target, the dollar loses half its purchasing power about every: | 35 years | 10 years · 70 years · 100 years | WP §2.2. | WP §2.2 |

## Supply & distribution (supply-and-distribution.md)

| Tier | Topic | Question | Correct | Distractors | Explanation | Source |
|---|---|---|---|---|---|---|
| A | Supply | What is DGD's total supply cap? | 21,000,000 | 19,000,000 · 100,000,000 · Unlimited | 19M can circulate; 2M is permanently locked for staking. | WP §5 |
| A | Supply | How many DGD can ever circulate? | 19,000,000 | 21,000,000 · 13,712,952 · 11,712,952 | 2M is locked, non-circulating. | WP §5 |
| A | Distribution | What single number drives each step of the distribution curve? | N, the count of confirmed network accounts | Total transaction volume · Bitcoin's price · Number of validators online | Each confirmed account advances the curve one step. | WP §5 |
| A | Wallet | Where do released coins land? | The participant's self-custody QT wallet | The web account balance · An exchange account · The Foundation treasury until claimed | Web account = validation interface; wallet = custody. | WP §5.6 |
| B | Distribution | Who receives coins when a release occurs? ⚠ | Every account with an active validation balance, equally | Every registered user · The newest account only · Accounts weighted by balance size | Changed 2026-07: releases go to funded accounts only. | supply-and-distribution.md |
| B | Distribution | Does a larger validation balance receive a larger share of each release? | No — same amount per funded account; a larger balance just lasts longer | Yes, proportionally · Yes, up to a cap · Only for referrers | The most common wrong inference. | WP §5.6 |
| B | Fees | What happens to transaction fees and staking rewards? | They are burned | Paid to validators · Paid to the Foundation · Returned to the treasury for redistribution | Supply can only decrease. | WP §5 |
| B | Curve | What happens to the per-account release amount as the network grows? | It shrinks toward zero | It grows · It stays constant · It doubles at each milestone | Near N=1,000 ≈ 88.69 coins; near the end ≈ 0.05. | WP §5 |
| C | Distribution | True or false: if some participants fail to validate, their unclaimed coins are redistributed to everyone else. | False | True | Unclaimed coins stay in / return to the treasury (WP §5.6). Your share does not grow. | WP §5.6 |
| C | Referrals | How many referral levels does DGD have? | One — single-level, one-time bonus | Three · Unlimited · Five with overrides | There is no second level and no cascade; recruiting-for-income language fails the linter. | WP §10.1 |
| C | Referrals | Does a referral change how much DGD anyone earns from releases? | No | Yes, +10% · Yes, for the referrer only · Yes, for both parties | Referral recognition is separate from releases. | participation-pathways.md |
| C | Tiers | How many discrete distribution levels or tiers are there? | None — the curve is continuous | 10 · 80 · 3 | WP §5.1. | WP §5.1 |
| D | Supply | How many DGD are permanently locked for staking? | 2,000,000 | 5,000,000 · 1,000,000 · 2,287,048 | Makes a 51% attack impractical. | WP §5 |
| D | Supply | Total per-signup releases across the whole curve sum to: | 11,712,952 | 13,712,952 · 19,000,000 · 7,287,048 | 13,712,952 = releases + the 2M staking lock. | WP §5 |
| D | Curve | At what account count does distribution end permanently? | 80,000,000 | 21,000,000 · 10,000,000 · 100,000,000 | 19M coins circulating at that point. | WP §5 |
| D | Validation | What do participants fund a DigitalGoldX account with? ⚠ | ERC-20 USDC or USDT | DGD · Bitcoin · Bank wire only | $20 minimum, $500 current cap (policy setting). | platform-and-tools.md |

## Valuation: CFV & DGSB (valuation-cfv-dgsb.md)

| Tier | Topic | Question | Correct | Distractors | Explanation | Source |
|---|---|---|---|---|---|---|
| A | DGSB | What does DGSB stand for? | Digital Gold Standard Benchmark | Digital Gold Staking Bonus · Decentralized Governance Standards Board · Digital Gold Supply Base | A frozen reference point. | WP §3 |
| A | CFV | CFV stands for: | Crypto Fair Value | Coin Flow Velocity · Certified Fund Valuation · Continuous Fixed Value | Measures fundamentals against the DGSB. | WP §4 |
| B | DGSB | What moment does the DGSB freeze? | Bitcoin first touching $100,000 in December 2024 | Bitcoin's 2017 peak · DGD's launch · The 2008 Bitcoin white paper | Market cap ≈ $1.983T at that moment. | WP §3.2 |
| B | CFV | Which metric carries 70% of the CFV weight? | Adoption (unique holders) | Annual transactions · Transaction value · Active developers | Others are 10% each. | WP §4 |
| B | CFV | What sets DGD's price after distribution ends? | The full CFV calculation on DGD's own metrics, recalculated monthly | The last curve price forever · An exchange order book · A Foundation vote | WP §11. | WP §11 |
| C | CFV | True or false: the CFV framework guarantees the published price will rise over time. | False | True | If metrics deteriorate, the Fair Coin Price falls and the published price declines. | WP §11.2 |
| C | Analogy | The White Paper compares the DGSB to: | A fixed measurement standard like the meter or kilogram | A stock index · A central bank target · A price prediction model | Standards don't change to flatter what's measured. | WP §3.1 |
| D | DGSB | Approximate Bitcoin unique holders used in the benchmark: | ~80 million | ~8 million · ~800 million · ~21 million | Adoption metric. | WP §3.2 |

## Platform, wallet, single price (platform-and-tools.md, dgd-overview.md)

| Tier | Topic | Question | Correct | Distractors | Explanation | Source |
|---|---|---|---|---|---|---|
| A | Wallet | On which platforms does the DGD QT wallet run? ⚠ | Windows, macOS, Linux (desktop) | iOS and Android · Browser extension · All of the above | No mobile or browser wallet exists — state it early. | platform-and-tools.md |
| A | Origin | Who created Digital Gold and donated it to the Foundation? | John Wright Gotts | Satoshi Nakamoto · Friedrich Hayek · Carl Menger | Developed 2014–2026, funded personally. | WP title page, Abstract |
| A | Origin | Which economist's idea of competing private currencies inspired DGD? | Friedrich Hayek (*The Denationalisation of Money*, 1976) | John Maynard Keynes · Milton Friedman · Adam Smith | "Let the best money win." | dgd-overview.md |
| B | Single price | Why does the single-price architecture matter for circulation? | A merchant can hold DGD and pay suppliers in it instead of converting to dollars immediately | It makes DGD cheaper to buy · It removes transaction fees · It lets the Foundation set prices | Cooperating-venue exclusivity removes bid/ask trading. | WP §8–9 |
| B | Node | What does every running QT wallet also do? | Act as a full node supporting the network | Mine new coins · Earn fees · Vote on governance | Fees are burned; there's nothing to vote on. | platform-and-tools.md |
| C | Safe harbor | In DGD materials, "safe harbor" refers to: | A legal position about staying outside securities law | A safe investment · Regulator approval · A guarantee you can't lose | It is a reasoned design position, not an approval (WP §12.16). | positioning-safe-harbor.md |
| C | Marketplace | Which is accurate about the DGD Marketplace & Escrow? ⚠ | It is planned (Q3/Q4 2026), not live | It is live today · It was cancelled · It runs on Ethereum | Say "coming," never "available." | platform-and-tools.md |

## Daily Ledger puzzle seeds (first 10 days)

| Day | Clue | Answer |
|---|---|---|
| 1 | The pillar that asks money to actually flow (2 words) | ADEQUATE CIRCULATION |
| 2 | Coins that can never circulate, in millions | 2 |
| 3 | The economist behind competing private currencies (surname) | HAYEK |
| 4 | What happens to every transaction fee (6 letters) | BURNED |
| 5 | The self-custody wallet's name (2 letters) | QT |
| 6 | The count that drives the curve (1 letter) | N |
| 7 | Metric with 70% of the CFV weight | ADOPTION |
| 8 | Privacy network built into the wallet (3 letters) | TOR |
| 9 | Number of referral levels | ONE |
| 10 | Month/year the DGSB was frozen | DECEMBER 2024 |

## Authoring rules for new items

1. Every item cites a wiki page and, where possible, a White Paper section.
2. No item asks the player to predict, estimate, or compare prices or financial outcomes. Curve numbers may
   be asked as *mechanics* (release amounts, account counts, caps), never as "what will it be worth."
3. Distractors come from the wiki's documented misconceptions (the balance-size misconception;
   the unclaimed-coins misconception; the referral-levels misconception; a mobile wallet; the marketplace being live).
4. Items marked ⚠ read from config so snapshot facts can be updated without re-authoring.
5. Run `python3 tools/dgd.py lint --doc-context --json` on this file before every merge; run the plain
   linter on any string that will appear on screen. **Distractors that state a misconception will
   trip the linter by design** — they need a reviewed allow-list entry, and the on-screen explanation
   that follows must state the correct mechanic in the linter's approved wording.
