---
tags: [dgd, subject, platform, tools, specs]
updated: 2026-07-19
source: digitalgold.co (verified 2026-07-19) · Digital Gold White Paper §5, §6, §8
---

# The Platform, Tools & Protocol Specs

What actually exists at **digitalgold.co** — the live tools, the wallet, the technical specs, and
the surrounding ecosystem. Useful for two things: getting your facts right on camera, and pointing
viewers at something real instead of a landing page.

> Live figures below are a **snapshot verified 2026-07-19**. They move constantly. Never state a
> current price or account count from memory — open the Stats page and read it, or say "as of
> today" and show it on screen. See [do & don't language](../compliance/do-and-dont-language.md).

## Live tools you can actually show

| Tool | Status | What it's good for on camera |
|---|---|---|
| **[Stats](https://digitalgold.co/stats)** | Live | The model calculator. Drag to any account count and watch price, supply, market cap and per-account release change. **The single best screen-recording asset the project has.** |
| **[Block Explorer](https://explorer.digitalgold.co/)** | Live | Real on-chain data — blocks, transactions, the oracle price feed. Proof the thing exists. |
| **[P2P DEX](https://digitalgold.co/trade)** | Preview | Swapping at the published price with no order book or spread. Preview only for now. |
| **Marketplace & Escrow** | Q3/Q4 2026 | Goods and services at the published price with decentralised escrow. **Not live — say "coming," never "available."** |
| **[GitHub](https://github.com/DigitalGoldFoundation/DGD)** | v26.2.0-beta | MIT-licensed source: burn mechanism, oracle pricing, Tor V3 engine, consensus. |

**The Stats calculator is the demo to lead with.** It turns the abstract "price follows a published
curve" claim into something a viewer watches happen. Screen-record it, don't describe it.

## Snapshot — verified 2026-07-19

| Metric | Value |
|---|---|
| Confirmed accounts | 3,210 |
| Published price | $9.84630 |
| Circulating supply | 7,413,838 DGD |
| Market cap | $72,998,838 |
| Release at next account | ~40.9978 DGD |
| Per funded account | ~0.01277191 DGD |

Note the last two lines together — they're the clearest illustration of how the split works. A
release of ~41 DGD divided across the funded base is a fraction of a coin each. That's the mechanic,
and it's honest about scale.

## The wallet

The **DGD QT wallet** is a self-custodial desktop full node — **Windows, macOS, Linux only.
No iOS, Android, or browser wallet.** That constraint trips people up constantly, so state it early
in any onboarding content.

- Current build: **v26.2.0-beta**, published with SHA-256 hashes on the download page.
- Every running wallet is a **node** — running one supports the network.
- Delivered DGD lands in the QT wallet, **not** the web account. Keys stay with the participant.
- Linux ships as a portable archive, not a `.deb` — the Software Centre won't recognise it, so
  Linux users need the terminal (`tar -xzf`, `chmod +x`, run). Qt5 dependencies may be needed.

**Always tell people to verify the hash** on the download page. An ambassador sending viewers to a
wallet download without mentioning verification is doing them a disservice.

## Protocol specs

| Spec | Value |
|---|---|
| Max supply | 21,000,000 DGD (fully premined) |
| Max circulating | 19,000,000 DGD |
| Permanent treasury lock | 2,000,000 DGD (staking, non-circulating, anti-51%) |
| Block target | 64 seconds |
| Block size | 2 MB dynamic |
| Transaction fee | 0.00001 DGD — **burned** |
| Staking rewards | **Burned** — zero staking inflation |
| Privacy | Native **Tor V3** onion addressing |
| Consensus | Hybrid Proof-of-Stake |
| SegWit | Implemented |
| Licence | MIT open source |

**Lineage matters and is a good story:** DGD forks **Blackcoin**, launched in early 2014 by the same
core contributors — one of the first pure Proof-of-Stake chains, with over a decade of production
history. "Built on twelve years of proof-of-stake" is a verifiable, non-promotional credibility
point that doesn't touch price.

Because both staking rewards and transaction fees are burned, **no new coins are ever created and
supply can only fall**. That's a cleaner scarcity story than most chains can tell.

## The ecosystem

| Property | What it is |
|---|---|
| **digitalgold.co** (DigitalGoldX) | The platform — validation, wallet downloads, stats, DEX, marketplace |
| **[digitalgoldfoundation.org](https://digitalgoldfoundation.org)** | The Foundation — the self-regulating body setting CFV fair-value standards |
| **[@DigitalGoldOrg](https://x.com/DigitalGoldOrg)** | Official Foundation account — network updates |
| **[@DigitalGoldTalk](https://x.com/DigitalGoldTalk)** | Podcast / news, **and where recognition structures are announced** |
| **[DGD Ambassadors](https://t.me/DGDAmbassadors)** | The ambassador Telegram |

The Foundation and the platform are **different entities** doing different jobs — the Foundation
sets standards, the platform operates validation. Blurring them is a small inaccuracy that a
sceptical viewer will notice.

## Using this material without breaking the rails

**Safe:**
- Screen-record the Stats calculator and narrate the *mechanism*.
- Show the Explorer to demonstrate the chain is real and public.
- Walk through wallet download + hash verification as a security lesson.
- Explain the burn mechanics, block time, or Tor V3 as engineering.
- "Here's what the protocol specifies" framing throughout.

**Not safe:**
- Dragging the Stats slider to 80,000,000 and lingering on **$100,000**. That's a price projection
  with extra steps, and it's the most tempting thing on the whole site. If you show the far end of
  the curve, say plainly that it's a **conditional maximum** requiring all four CFV metrics to
  scale, and that the framework does not guarantee appreciation.
- Describing the Marketplace or DEX as available. They aren't yet.
- Quoting a live price without showing it and dating it.
- Implying that running a node or holding a balance produces yield — **it doesn't**; staking
  rewards are burned.

## Connects to
- [Supply & distribution](supply-and-distribution.md) · [Valuation: CFV & DGSB](valuation-cfv-dgsb.md)
- [Six Pillars](six-pillars.md) · [Participation pathways](participation-pathways.md) · [Glossary](glossary.md)
- Rails: [communications discipline](../compliance/communications-discipline.md) · [do & don't language](../compliance/do-and-dont-language.md)
