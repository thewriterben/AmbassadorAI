---
title: Knowledge Tablet question bank — protocol and engineering
updated: 2026-09-14
source: LLMWiki/dgd/platform-and-tools.md · glossary.md · White Paper §5, §6, §8, §12
rules: engineering facts only; build numbers and live figures are snapshots and marked ⚠
---

## Protocol & engineering (platform-and-tools.md)

Specs are the most durable question material in the bank: they are checkable, they do not move,
and none of them touch price. Live figures are marked ⚠ and served from config.

| Tier | Topic | Question | Correct | Distractors | Explanation | Source |
|---|---|---|---|---|---|---|
| A | Consensus | What consensus model does DGD use? | Hybrid Proof-of-Work and Proof-of-Stake | Proof-of-Work only · Proof-of-Stake only · Proof-of-Authority | Refined by SegWit. | platform-and-tools.md |
| A | Licence | Under what licence is the DGD source published? | MIT open source | Proprietary · GPL v3 · Business Source Licence | The repository carries the burn mechanism, oracle pricing, Tor V3 engine and consensus. | platform-and-tools.md |
| A | Layer-1 | What does it mean that DGD is a Layer-1? | It is a base blockchain that runs on its own rather than on top of another chain | It settles transactions on Ethereum · It is a payment channel · It is a wrapped asset | Like Bitcoin or Ethereum. | glossary.md |
| A | Wallet | Which operating systems does the QT wallet run on? | Windows, macOS and Linux | iOS and Android · Browser extension only · All of the above | There is no mobile or browser wallet. State this at the start of any onboarding content. | platform-and-tools.md |
| B | Block time | What is DGD's block target? | 64 seconds | 10 minutes · 15 seconds · 2 minutes | Block size is 2 MB dynamic. | platform-and-tools.md |
| B | Fees | What is the transaction fee, and what happens to it? | 0.00001 DGD, and it is burned | 0.001 DGD paid to validators · A percentage paid to the Foundation · There is no fee | Fees are burned by design rather than paid to anyone. | platform-and-tools.md |
| B | Staking | What do stakers receive as a reward? | Nothing — staking rewards are burned, so there is zero staking inflation | A share of fees · Newly minted coins · Governance votes | This is the critical modification to the model DGD's Proof-of-Stake half came from. | platform-and-tools.md |
| B | Lineage | DGD's Proof-of-Stake component derives from which earlier chain? | Blackcoin | Peercoin · Nxt · Cardano | Launched in 2014 by the same core contributors, and one of the first pure Proof-of-Stake chains. | platform-and-tools.md |
| B | Supply effect | Because both fees and staking rewards are burned, total supply can: | Only fall | Only rise · Rise or fall with demand · Stay exactly constant | No new coins are ever created. | platform-and-tools.md |
| B | Node | What does running a QT wallet also do? | It runs a full node that supports the network | It mines new coins · It earns fees · It grants a governance vote | Fees are burned and the rules cannot change, so there is nothing to mine for or vote on. | platform-and-tools.md |
| B | Tools | Which live tool best demonstrates that price follows a published curve? | The Stats calculator | The Marketplace · The P2P DEX · The ambassador Telegram | Drag to any account count and watch price, supply, market cap and per-account release change. | platform-and-tools.md |
| B | Entities | The Foundation and the platform are: | Different entities — the Foundation sets standards, the platform operates validation | The same organisation under two names · Parent and subsidiary · Unrelated projects | Blurring them is a small inaccuracy a sceptical viewer will notice. | platform-and-tools.md |
| C | Wallet | Is there an official DGD mobile wallet? | No — desktop only | Yes, on iOS and Android · Yes, Android only · Yes, as a browser extension | The constraint trips people up constantly. | platform-and-tools.md |
| C | Marketplace | What is the correct status language for the Marketplace and Escrow? ⚠ | Coming — planned for Q3/Q4 2026 | Available now · Cancelled · In closed beta | Say "coming," never "available." | platform-and-tools.md |
| C | DEX | What is the current status of the P2P DEX? ⚠ | Preview | Fully live · Not built · Retired | Swapping at the published price with no order book or spread, in preview for now. | platform-and-tools.md |
| C | Yield | Does running a node or holding a balance produce yield? | No | Yes, a staking yield · Yes, a share of fees · Yes, for nodes only | Staking rewards are burned. Implying yield is both wrong and non-compliant. | platform-and-tools.md |
| C | Downloads | What should an ambassador always tell viewers to do when downloading the wallet? | Verify the published SHA-256 hash | Disable antivirus first · Download from a mirror · Skip the checksum to save time | Sending viewers to a wallet download without mentioning verification does them a disservice. | platform-and-tools.md |
| C | Channels | Which X account does the White Paper name for recognition announcements? | @DigitalGoldTalk | @DigitalGoldOrg · @DigitalGoldX · The ambassador Telegram | The site lists @DigitalGoldOrg for network updates; watch both and call neither "the" official channel. | WP §10.1, platform-and-tools.md |
| D | Supply | What is the maximum circulating supply, as a protocol spec? | 19,000,000 DGD | 21,000,000 DGD · 13,712,952 DGD · 7,413,838 DGD | 21M total, 2M permanently locked. | platform-and-tools.md |
| D | Privacy | Which privacy technology is native to the protocol? | Tor V3 onion addressing | Zero-knowledge proofs · CoinJoin mixing · Stealth addresses | For encrypted, anonymous transactions without permission from an intermediary. | WP §2.2 |
| D | Premine | The 21,000,000 DGD supply is: | Fully premined | Mined over 100 years · Minted on demand · Issued by the Foundation monthly | Distribution is by release from the treasury along the curve, not by mining. | platform-and-tools.md |
