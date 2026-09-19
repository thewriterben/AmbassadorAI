---
title: Digital Gold Arcade — Product Plan v0.2
status: draft for Foundation review
updated: 2026-09-06
owner: Benji
sources: LLMWiki/dgd/*, LLMWiki/compliance/*, web research (see Sources)
supersedes: v0.1 (DGD-denominated rewards to QT wallets)
delivery: a tab inside the DGD App (trading platform) — see DGD-App-Integration-Brief.md
---

# Digital Gold Arcade — Product Plan v0.2

Mobile arcade of short, skill-and-knowledge games that teaches how Digital Gold is designed.
Validated platform accounts earn small, capped **validation-credit top-ups**; everyone else earns
XP, badges and a clear hand-off to sign up on digitalgold.co.

> Nothing here is legal or tax advice. The compliance section is a sourced issue map for licensed
> counsel. Same rule as the rest of this repo: never describe DGD as an investment, predict price,
> or promise returns — including inside the game.

## What changed from v0.1

The platform is changing: **every validated new account receives $21 of validation credit at
signup**, so it is funded from day one. Three consequences drive this revision:

1. The arcade no longer needs to give anyone DGD, dollars, or an activation. The platform already
   activates every validated account. The arcade's job is **education and retention**.
2. The only monetary reward left is a **small top-up** that extends how long a validated account's
   balance lasts. That is a loyalty credit at a fixed ratio — the category app stores explicitly
   tolerate — not "earn crypto."
3. Identity, `N` integrity, tax aggregation and the legal status of the $21 program all live on the
   **platform**, where they belong. The arcade reads platform identity through an API and never
   runs its own verification, wallet, or payout.
4. **Delivery is a tab in the DGD App**, not a standalone app. The App supplies identity, the
   `validated` flag, attestation, the credit ledger and remote flags; the Arcade supplies the game
   runtime and its own backend. Store review is inherited from the host, so the tab ships behind
   server-side flags in a post-approval update and never links to trading. Details, API contract
   and work split: `DGD-App-Integration-Brief.md`.

---

## 1. Concept in one paragraph

An educational arcade, not a casino. Games are the wrapper that makes repetition fun; the quiz is
the gate. Two tracks. **Explorer** (anyone, no account needed): plays everything, earns XP,
badges and a mastery certificate, and is handed off to digitalgold.co when ready — **no reward of
monetary value**. **Validator** (account validated on the platform): the same games, plus a
**deterministic, capped validation-credit top-up** for completed expeditions, applied to the
player's existing platform account through the platform API. No chance elements anywhere. Nothing
is ever paid for signing up, referring, sharing or installing.

Why this works as education: retrieval practice beats re-reading (~61% vs 40% recall after a week,
Roediger & Karpicke 2006), and spaced retrieval compounds it (Cepeda 2006 meta-analysis, d≈0.71).
A runner-style game carrying embedded questions produced the same learning outcomes as a richer
genre in a 2023 controlled study, so the wrapper doesn't hurt learning. Trivia as a *standalone*
genre retains worst of all mobile genres (D7 ≈ 3.3%), while arcade hooks early (D1 ≈ 22%) and
card/puzzle retain best (D7 5–7%). So: arcade + puzzle loops, trivia as the gate.

---

## 2. What the precedents teach (research summary)

| Precedent | Model | What happened | Lesson for us |
|---|---|---|---|
| Coinbase Learning Rewards | lesson + 1–3 Q quiz, $1–5 in token, one reward/course, full KYC | Answers leaked to "answer sites" within hours; program **discontinued May 2025** | A static quiz never gates knowledge. KYC was the real Sybil control. Rotate and paraphrase questions; never expose the key. |
| Binance Learn & Earn / CMC Earn | quiz → fixed token amount, per-region caps, paid into locked products | First-come pools; bulk-registered accounts disqualified; rewards often below withdrawal minimums | Per-user + per-region + global caps; lock/delay payouts; make the minimum withdrawal reachable. |
| HQ Trivia | live quiz, shared cash pot | Bots scraped search engines via the API; pots split to cents; shut down | Any prize keyed to a **publicly searchable** answer must assume instant lookup. Enforce minimum answer latency; use design-specific questions. |
| THNDR Games (Bitcoin Bounce, Turbo '84, Solitaire) | free-to-play, ad-funded, tickets → **daily raffle** in sats, Lightning withdrawal | Survived years on both stores; pivoted to B2B | Small, expiring prizes and a fixed daily cost survive. (We must **not** copy the raffle — chance is the one element we avoid.) |
| Bling / Bitcoin Blast | match-3, points per level, cash-out every ~5 days, tiny amounts | Google Play suspended it in 2020 for "Earn Free Bitcoin!" marketing; reinstated in 10 days | Never market "earn free crypto." Frame as knowledge rewards. |
| Layer3 / Galxe / Zealy quests | on-chain credentials, tiered Sybil settings, liveness checks | Quest farming is industrialized (Arbitrum: ~150k Sybil addresses took ~22%) | Assume farms exist from day one; layer device attestation + proof-of-human + graph analysis. |
| Duolingo streaks | streak + freeze/repair | 17M DAU; streak users retain far better (secondary sources) | Deterministic streak bonuses are the cheapest retention lever and are chance-free. |
| Sweatcoin | step rewards | Hard daily cap, one device per account, per-account model + graph-based multi-account detection + manual review | Copy this layered model almost verbatim. |

---

## 3. Game shortlist

Scoring (1–5): **Engagement** (genre retention data + habit fit), **Knowledge fit** (how naturally
the DGD content sits inside the loop), **Cheat resistance** (server-authoritative, hard to
script), **Build cost** (5 = cheapest), **Chance-free** (must be 5 to ship with rewards).

| # | Game | Loop | Eng | Know | Cheat-res | Cost | Chance-free | Phase |
|---|---|---|---|---|---|---|---|---|
| 1 | **Tablet Run** (your side-scroller) | Auto-run through a "monetary history" world; 3–5 Knowledge Tablets gate progress; finish = expedition complete | 4 | 5 | 4 | 3 | 5 | **MVP** |
| 2 | **Daily Ledger** (Wordle-style) | One puzzle a day: a glossary term / pillar / number to deduce from clues; same puzzle for everyone; 6 attempts | 5 | 4 | 4 | 5 | 5 | **MVP** |
| 3 | **Pillar Sort** | 60-second drag-sort: statements fly in, sort them under the right Pillar (Scarcity, Stable Pricing, …) | 4 | 5 | 3 | 5 | 5 | MVP |
| 4 | **Design or Myth?** | Swipe left/right rapid-fire on statements ("Unclaimed coins are redistributed to everyone else" → Myth) | 4 | 5 | 3 | 5 | 5 | MVP |
| 5 | **Chain Builder** | Order the supply chain from retail POS back to raw material (the WP §10 lumber example); harder chains unlock | 3 | 5 | 4 | 4 | 5 | v1.1 |
| 6 | **Ledger Solitaire** | Solitaire/card loop (best long-term retention genre) with a Tablet gate every N wins | 5 | 3 | 4 | 3 | 5 | v1.2 |
| 7 | **Merchant Chain** (idle/tycoon) | Grow a circulating economy; unlock links by passing Tablets; illustrates Adequate Circulation | 4 | 4 | 3 | 2 | 5 | v2 |
| 8 | **Live Pillar Quiz** (HQ-style event) | Weekly synchronous quiz with ambassadors as hosts | 4 | 5 | 2 | 3 | 5 | v2 (needs the anti-bot stack proven first) |

Rejected: anything with a spin/raffle/loot element (turns a skill contest into a sweepstakes),
price-guessing games (invites price framing), referral-gated rewards (Apple 3.1.5(v), the
recruiting-for-income reading the wiki warns about, and — now that every validated signup carries
$21 — the single most attractive target for a farm).

### 3.1 Tablet Run — design detail (MVP flagship)

- **World:** side-scrolling run from "1913" to "the network." Background beats tell the story the
  wiki already tells (96% purchasing-power loss, 7,000-fold money-supply expansion, the Hayek idea,
  the 21M cap). Obstacles are debasement hazards — printing presses, inflation clouds.
- **Knowledge Tablets:** 3 (Explorer) or 5 (Validator) per expedition. The run pauses at a tablet;
  the server sends **one signed question** (nonce + expiry); the player has 20 s. Correct → the
  tablet opens and the run continues. Wrong → tablet shows the correct explanation (learning
  moment), the run resumes, and the expedition **cannot complete** — but the player keeps going for
  the mastery XP. **One retry per day per expedition**, never for the same question.
- **Completion:** all tablets answered correctly → expedition complete → XP for everyone; for
  Validator accounts, a top-up request is queued to the platform (see §4, §6). Tablets that were missed get **scheduled back** 1, 3, 7 days later
  (spaced retrieval) — the player can't "finish" the content until they've re-answered them.
- **Difficulty ladder:** Tier A (definitions), Tier B (mechanics: who receives a release?),
  Tier C (traps: "unclaimed coins are redistributed" → false), Tier D (numbers and sections you can
  only know from the WP). Validator track requires ≥2 Tier C/D tablets.
- **Skill layer (cheap, and keeps it a game):** jumping and sliding matter, but the reward is
  never gated by reflexes alone — the tablets are the gate, so a slow player still finishes.
- **Two-minute rule:** an expedition is 90–150 s. That's the session length arcade games actually
  get (3.3 min/session median).

### 3.2 Daily Ledger — design detail

- Same puzzle for everyone each UTC day (like Wordle) — shareable result grid with no answer.
- Clue types: a pillar from its definition, a glossary term from letters, a number from the
  supply table ("coins locked for staking: __,___,___"), a section from a paraphrase.
- Solve in ≤6 attempts → **fixed** XP, and for Validator accounts a fixed top-up (no bonus for
  fewer attempts, so there's nothing to brute-force with alts). Streak (7/30 days) adds a
  **deterministic** bonus.
- Cheapest game to build, highest daily-habit value, and the numbers are exactly the ones the
  wiki tells ambassadors to get right.

---

## 4. Reward economy and limits

### 4.1 What a top-up is

A validated account's balance is drawn down as releases occur and stops receiving when exhausted.
A **top-up** adds validation credit to that balance so it lasts longer. It is denominated in credit,
not DGD; it is non-cashable, non-transferable, and applied only to the one platform account bound
to the player's verified identity. The DGD side is untouched: the protocol releases coins to funded
accounts exactly as it does for everyone else. Snapshot for scale: **$9.85 per DGD (verified
2026-07-19)**, so a $1 top-up ≈ 0.1 DGD of eventual releases at today's price.

Never call it "dollars," "cash," or "earnings" anywhere a player or a store reviewer can see it.
The in-app word is **validation credit**.

### 4.2 Limits (all enforced server-side, all config-driven)

| Limit | Explorer | Validator | Why |
|---|---|---|---|
| Rewarded expeditions (Tablet Run) | XP only | 1 top-up / day | One headline reward a day, full stop |
| Daily Ledger | XP + streak | 1 fixed top-up / day | Same puzzle for all; no attempt bonus |
| Mini-games (Pillar Sort, Design or Myth) | XP | XP | Most play is unpaid; XP drives badges and leaderboards |
| **Per-identity daily cap** | — | $1.00 credit (config; pilot default) | Hard ceiling regardless of games |
| Per-identity weekly cap | — | $5.00 credit | Forces rest days; kills 24/7 grinding |
| Per-identity lifetime cap | — | $100 credit, then badges only (config) | Bounds exposure; revisit with data |
| **Global daily pool** | — | fixed credit amount set weekly by the Foundation | When exhausted, top-ups convert to XP with "pool refills at 00:00 UTC" |
| Question re-serve window | correctly answered item retired 14 days; missed item comes back at 1/3/7 days | same | Nobody can grind the same 20 questions |
| Minimum answer latency | 1.5 s (Tier A) – 3 s (Tier D) | same | Bots answer in milliseconds |
| Cooldown between rewarded expeditions | — | 4 h (unrewarded replays allowed for XP) | Rate limit without punishing genuine play |
| Top-up cadence | — | queued instantly, **applied daily** in one batch after fraud review | Gives review a window; one API call per day |

### 4.3 Budget scenarios ($1 top-up/day, Validator accounts only)

| Daily rewarded Validators | Credit/day | Credit/month |
|---|---|---|
| 500 (pilot) | $500 | ~$15k |
| 2,000 | $2,000 | ~$60k |
| 10,000 | $10,000 | ~$300k |

Compare v0.1: 1 DGD/day to the same 10,000 players was ~$3.0M/month and rising with `N`. Costs are
now fixed in credit, small next to the platform's own $21-per-signup spend, and the global pool is
the throttle. Recommended pilot pool: **$300/day**.

### 4.4 Why these limits also stop cheating

- One rewarded account per verified identity, enforced by the platform, means a farm needs rented
  identities — and at $1/day, $100 lifetime, renting identities doesn't pay. (It *does* pay for the
  platform's $21 signup credit; see §7.)
- Deterministic rewards remove the "try again for a better roll" incentive.
- Retiring answered questions plus minimum latency defeats the two attacks that killed Coinbase
  Earn and HQ: published answer keys and search bots.
- Daily batch application means a detected abuser loses **everything not yet applied**, and the
  Terms say so.

---

## 5. Anti-abuse architecture

Identity is the platform's job. The arcade's job is to make sure a real, verified person is
actually playing and actually answering.

1. **Server-authoritative gameplay.** The client never holds the question bank or the answer
   key. Each question is issued signed, single-use, with expiry; scoring happens on the server;
   game-state checkpoints (tablet reached, run time) are validated for plausibility (a 90-second
   run can't complete in 9 seconds).
2. **Device attestation on every Validator session.** Google **Play Integrity** (require
   `MEETS_DEVICE_INTEGRITY`; reject emulators, uncertified ROMs, and `appAccessRisk` overlays) and
   Apple **App Attest** (per-install key; verify assertions; use the **fraud-risk metric** to flag
   devices with many keys) plus **DeviceCheck** bits to mark "already rewarded today" across
   reinstalls. PWA pilot uses a vendor fingerprint SDK until the native wrapper ships.
3. **Account linking, not verification.** A player links the arcade to their platform account via
   OAuth; the platform sends back a stable identity id and a `validated` flag. The arcade stores
   nothing else — no ID documents, no biometrics, no phone numbers. **One identity ↔ one arcade
   account ↔ at most two devices** (phone + tablet); a further device is XP-only.
4. **Behavioral and graph signals.** Answer-latency distributions, identical run traces, IP/ASN
   clustering, VPN/proxy, time-of-day patterns across accounts. Farms score high on **similarity**,
   not on any single signal. Flagged accounts go to a **manual review queue** before the daily batch,
   and flags are shared back to the platform, which is the party most exposed to identity fraud.
5. **Question-bank hygiene.** ≥ 300 items at launch, paraphrase variants for each, distractors
   drawn from the wiki's known misconceptions, weekly additions. Items are never shown with their
   ID; screenshots therefore don't map to a key.
6. **Abuse response ladder.** Soft (XP-only for 7 days) → hold top-ups pending review → forfeiture
   of unapplied credit and arcade ban, with the identity flagged to the platform. Terms state that
   top-ups are recognition for demonstrated learning, are discretionary until applied, and are
   forfeited on abuse.

---

## 6. Top-up flow (arcade → platform API)

- The arcade never touches DGD, wallets, addresses or keys. It calls one platform endpoint:
  `apply_credit(identity_id, amount, reason, idempotency_key)`, once per identity per day, from the
  reviewed batch.
- The platform owns: identity uniqueness, the `validated` flag, the per-identity credit ledger
  (the $21 signup credit **plus** arcade top-ups **plus** anything else), and any tax aggregation
  and reporting against that ledger. The arcade only reports into it.
- Explorer players see their XP, badges and a "Ready to validate? Create your account" hand-off
  that deep-links to digitalgold.co. The arcade receives nothing for that signup and never shows
  the $21 figure as a reward for playing — it's the platform's promotion, described in the
  platform's words.
- Since coins still land in the desktop-only **QT wallet**, wallet download + hash verification
  remains a Tablet topic and an onboarding lesson; the arcade doesn't need an address.

---

## 7. Compliance issue map (for counsel — not legal advice)

Split into what the **arcade** raises and what the **platform's $21 program** raises, because the
second is now the larger question and it exists whether or not the arcade ships.

### 7.1 Arcade

| Area | Issue | Plan position | Open question |
|---|---|---|---|
| **Foundation discipline / WP §12.11** | Every in-game string, tablet, and store listing is a public statement | Run every string through `tools/dgd.py lint`; question bank uses only wiki-sourced facts; no price content, no "earn" language | — |
| **Apple 3.1.5(v)** ("may not offer currency for completing tasks") | A top-up is credit toward a service, not currency; nothing is paid for installs, referrals, follows or shares | Loyalty-credit framing; official rules in-app; **pilot as a PWA first**; appeal memo ready | Reviewer discretion; no public precedent either way |
| **Apple 5.3 / Google Real-Money Gaming & Contests** | Contest rules in-app; no IAP for reward credit; Google forbids "glamorizing earnings"; gamified loyalty in games must pay at a **fixed, documented ratio** | Fixed ratio published in-app; no IAP tied to rewards; Financial Features declaration filed on Play | — |
| **Lottery / sweepstakes** | Prize exists; chance and consideration removed | Pure skill contest; Official Rules (18+, period, scoring criteria, ARV of credit, sponsor, tax responsibility, "Apple/Google not a sponsor") | Some states treat heavy effort as consideration: keep expeditions short |
| **Securities** | Arcade top-ups are incremental to the platform's own credit distribution | Whatever answer counsel gives for the $21 program covers the arcade; the arcade adds no new mechanism | Depends on 7.2 |
| **Tax** | Top-ups are likely income at FMV to the recipient | Reported into the platform ledger; the platform, not the arcade, tracks the $2,000 1099-MISC threshold per identity | — |
| **FTC** | Ambassadors promoting the arcade are paid promoters | Existing FTC disclosure rules apply | — |
| **Age / privacy** | Apple 13+/16+/18+ tiers; COPPA amendments in force | App is **18+** to match the platform; no PII stored beyond identity id + email | UK/state age-assurance scope |
| **UK / EU** | Prize-competition and financial-promotion rules | Top-ups geo-gated to the US for the pilot; XP-only elsewhere | FCA treatment of DGD |

### 7.2 Platform — the $21 signup credit (out of the arcade's scope, but load-bearing)

| Area | Issue | Why it matters to the arcade |
|---|---|---|
| **Identity farming** | $21 of credit (≈ 2 DGD of eventual releases at today's price) per verified identity is a bounty; rented-identity KYC farms clear that bar. Every fake account also increments `N` and moves the published price. | If the platform's verification is weak, arcade top-ups reach farm accounts too. The arcade's per-identity caps limit damage but can't fix `N`. If users pay a signup fee ≥ $21 the arbitrage disappears; below $21 it doesn't. |
| **Securities (SEC/CFTC Mar 2026 release)** | The Foundation automatically distributes value to every new account — a "central party distributing rewards" question on the core product | Counsel's answer here decides whether any arcade top-up is acceptable |
| **Tax** | Signup credit that becomes DGD is likely income; per-identity aggregation and 1099-MISC at $2,000 | The arcade must report into the platform ledger, never keep its own |
| **Content** | Wiki pages and question items that say "fund with USDC/USDT, $20 minimum" become wrong the day the change ships | Question-bank items marked ⚠ are served from config and must be updated with the platform change |

---

## 8. Roadmap

| Phase | Weeks | Scope | Exit criteria |
|---|---|---|---|
| **0 — Decide** | 1–2 | Counsel review of §7 (7.2 first); Foundation confirms platform API (`validated` flag, `apply_credit`), pilot pool and caps; write Official Rules; update wiki pages affected by the $21 change | Written go/no-go; API contract signed off |
| **1 — Content** | 2–5 | 300-item question bank from the wiki (see `question-bank-seed.md`), paraphrase variants, linted; Daily Ledger puzzle calendar (90 days) | Bank passes lint; two ambassadors blind-test for accuracy |
| **2 — PWA pilot, Explorer only** | 4–8 | Tablet Run + Daily Ledger as a mobile web app; server-authoritative backend; XP, badges, hand-off link; invite-only 500 players (ambassadors + campus clubs from the Fall tour) | D7 ≥ 8%; zero lint failures in shipped strings; hand-off click-through measured |
| **3 — Validator top-ups** | 8–12 | Platform OAuth linking; daily batch + review queue; fraud signals; top-ups live for validated accounts at pilot caps | Fraud rate < 2% of applied credit; pool never exhausted before 18:00 UTC |
| **4 — Embed in the DGD App** | 12–20 | Same web bundle behind the App's bridge (identity, attestation, credit, flags); Pillar Sort + Design or Myth; tab ships in a post-approval App update with rewards **off**, then on for validated US accounts | Tab live on both stores; kill switch tested; PWA stays as fallback |
| **5 — Retention** | 20–28 | Chain Builder, Ledger Solitaire, seasons, mastery exam | D30 ≥ 3% (above genre median) |
| **6 — Scale** | 28+ | Live Pillar Quiz events, non-US top-ups after per-country review, Merchant Chain | Pool economics stable at 10× users |

Team for phases 2–4: 1 game dev (Phaser/Unity), 1 backend (Node/Go + Postgres), 1 designer,
content lead (can be an ambassador), part-time fraud/ops reviewer, plus platform engineering time
for the two API endpoints.

---

## 9. Success metrics

Learning: mastery rate per pillar (share of items answered correctly on first re-serve at day 7),
misconception decay (Tier C trap items). Engagement: D1/D7/D30 vs genre medians (22/4/1% arcade),
Daily Ledger streak distribution. Funnel: Explorer → hand-off click → validated account linked → Validator play.
Integrity: rejected attestations, flagged-account rate, top-up reversals, cost per honest credit applied.

---

## 10. Open decisions for the Foundation

1. **Platform first:** how strong is verification behind the $21 signup credit, and does a signup
   fee offset it? This decides whether `N` can be trusted — nothing in the arcade fixes it.
2. Counsel's view of the $21 program under the March 2026 release; the arcade top-ups ride on it.
3. Pilot caps: $1/day, $5/week, $100 lifetime and a $300/day pool are proposed defaults.
4. API contract: OAuth linking with a `validated` flag, and an idempotent `apply_credit` call.
5. Runtime inside the App: WebView-embedded web bundle (recommended, keeps the Arcade on its own release cadence) vs. a native/RN module.
6. Whether ambassadors can author question-bank items (with review) as a recognized promotional-pathway contribution.

---

## Sources

Internal: `LLMWiki/dgd/six-pillars.md`, `supply-and-distribution.md`, `valuation-cfv-dgsb.md`,
`participation-pathways.md`, `platform-and-tools.md`; `LLMWiki/compliance/*`.

External (accessed 2026-09-06):
- Coinbase Learning Rewards FAQ (discontinued) — https://help.coinbase.com/en/coinbase/getting-started/getting-started-with-coinbase/learning-rewards-faq-and-terms
- Binance Learn & Earn FAQ — https://www.binance.com/en/support/faq/binance-learn-earn-frequently-asked-questions-3819c21bd5fb493fa5057c727043cb14
- CoinMarketCap Earn (1INCH campaign) — https://coinmarketcap.com/academy/article/coinmarketcap-earn-campaign-with-1inch
- HQ Trivia bots — https://money.com/hq-trivia-bots-cheaters/ ; https://www.coveros.com/blog/cheated-hq-trivia-stop/
- THNDR withdrawals — https://www.thndr.games/article/how-do-i-withdraw-from-your-games ; CoinDesk on Club Bitcoin Solitaire — https://www.coindesk.com/tech/2022/09/19/thndr-games-launches-play-to-earn-bitcoin-solitaire-mobile-game
- Bling suspension — https://www.coindesk.com/markets/2020/01/29/developers-say-google-play-unfairly-booted-their-bitcoin-rewards-game
- Sweatcoin fraud model — https://medium.com/sweat-economy/step-verification-and-fraud-detection-a2f0f8947f3c
- Zealy + Humanode BotBasher — https://blog.humanode.io/sybil-resistant-quests-on-zealy-with-botbasher/
- Duolingo streaks (Sensor Tower) — https://sensortower.com/blog/duolingo-streak-feature-app-engagement-growth
- GameAnalytics 2025 benchmarks — https://www.gameanalytics.com/reports/2025-mobile-gaming-benchmarks
- AppsFlyer D30 by genre — https://gamedevreports.substack.com/p/appsflyer-d30-retention-in-games
- Karpicke & Roediger 2007 — https://learninglab.psych.purdue.edu/downloads/2007/2007_Karpicke_Roediger_JML.pdf
- Cepeda et al. 2006 — https://augmentingcognition.com/assets/Cepeda2006.pdf
- Runner vs shooter learning study (2023) — https://www.sciencedirect.com/science/article/pii/S1875952123000435
- Apple App Store Review Guidelines — https://developer.apple.com/app-store/review/guidelines/
- Google Play blockchain content policy — https://support.google.com/googleplay/android-developer/answer/13607354
- Google Play real-money gaming/contests — https://support.google.com/googleplay/android-developer/answer/9877032
- SEC/CFTC March 2026 interpretive release summary — https://www.fintechanddigitalassets.com/2026/04/sec-clarifies-the-application-of-the-securities-laws-to-cryptoassets/
- Sweepstakes basics — https://www.olshanlaw.com/sweepstakes-law-basics ; state rules — https://www.sweeppeasweeps.com/sweepstakes-and-contest-rules-by-state.html ; skill-contest fees — https://fasthofflawfirm.com/blog/skill-contests-versus-sweepstakes-entry-fees
- Kraken sweepstakes terms (crypto prize rules template) — https://www.kraken.com/legal/bitcoin-sweepstakes-terms
- UK prize competitions — https://www.pinsentmasons.com/out-law/guides/running-a-competition
- 1099-MISC $2,000 threshold — https://www.verrill-law.com/blog/the-new-2000-threshold-for-sending-irs-form-1099-misc-to-prize-winners/ ; 1099-DA — https://www.withum.com/resources/form-1099-da-for-crypto-in-2026-what-taxpayers-and-issuers-need-to-know/
- Play Integrity API — https://developer.android.com/google/play/integrity/overview ; Oct 2025 update — https://android-developers.googleblog.com/2025/10/stronger-threat-detection-simpler.html
- App Attest / DeviceCheck — https://developer.apple.com/documentation/devicecheck ; fraud risk — https://developer.apple.com/documentation/devicecheck/assessing-fraud-risk
- Device-farm detection — https://fingerprint.com/blog/how-to-detect-device-farm-fraud/
- COPPA amendments — https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data
- Apple age ratings — https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions/
