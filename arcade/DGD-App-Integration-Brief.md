---
title: Digital Gold Arcade — Integration brief for the DGD App
status: draft for the DGD App developer
updated: 2026-09-06
owner: Benji
companion: DGD-Arcade-Plan.md (v0.2), question-bank-seed.md
---

# Arcade as a tab in the DGD App — integration brief

The Arcade is not a standalone app. It ships as a **tab inside the DGD App**, the Digital Gold
trading platform. This brief is what the App developer needs: the module boundary, the API the App
provides, what the Arcade provides, release gating, and the constraints that come from living
inside a financial app.

> Not legal advice. Store-policy references are current as of Sept 2026 (Apple guidelines
> updated June 2026; Google Play policy effective July 2026).

---

## 1. What changes when the Arcade lives inside a trading app

| | Standalone arcade (v0.2) | Tab in the DGD App |
|---|---|---|
| Store review posture | Arcade's own; loyalty-credit framing carried the risk | **Inherited from the host.** A trading app already clears Apple 3.1.5(iii)/5.1.1(ix) and Google's exchange-licensing rules or it doesn't ship. The Arcade is incremental — but a reviewer objection to the Arcade can now block a **trading-app** release. Hence the kill switch (§5). |
| Identity | OAuth link to the platform | **Native.** The App already has the verified identity and `validated` flag. No linking step, no PII in the Arcade. |
| Credit ledger | Arcade calls `apply_credit` | Same call, in-process or to the App backend; the platform ledger is the only ledger. |
| Age rating | 18+ by choice | 18+ by necessity; no conflict. |
| Attestation | Arcade's own Play Integrity / App Attest | App's existing attestation, passed through. |
| Framing risk | "Earn crypto" | **"Rewards for trading."** Inside a trading app, any reward is read as a trading incentive. Google forbids glamorizing earnings from trading; Apple treats casino-like visuals in a finance app as simulated gambling. The Arcade must be visibly **learning**, never tied to trades. |
| PWA pilot | Primary channel | Still the pilot: the same web bundle is what the tab embeds. |

Net: integration removes most of the Arcade's store risk and moves the remainder onto the host's
release train. The price is that the Arcade must be **switchable off remotely** and must never
touch trading.

---

## 2. Module boundary

```
DGD App (host)                          Arcade module
┌──────────────────────────┐            ┌──────────────────────────────┐
│ Auth / identity          │──token────▶│ Game runtime (web bundle in   │
│ validated flag           │──flag─────▶│  a WebView, or RN module)     │
│ Device attestation       │──verdict──▶│                               │
│ Credit ledger (platform) │◀─apply────│ Arcade backend (separate svc) │
│ Feature flags / remote   │──enabled──▶│  questions, scoring, caps,    │
│  config                  │            │  review queue, telemetry      │
│ Trading / DEX / wallet   │   ✕ none   │                               │
└──────────────────────────┘            └──────────────────────────────┘
```

- **The Arcade backend is a separate service** owned by the Arcade team. The App never sees the
  question bank or answer keys; the Arcade never sees balances, trades, addresses, or keys.
- **Runtime:** the pilot's web bundle (Phaser) embedded in a WebView with a thin native bridge is
  the fastest path and keeps the Arcade on its own release cadence. A React Native module is the
  alternative if the App is RN and wants shared navigation/theme. Decide with the developer; the
  API below is the same either way.
- **No cross-links into trading.** The Arcade tab may deep-link to *Learn* content and to the
  account/validation screen. It never links to Trade, the DEX, or Marketplace, and no game state
  reads trading activity.

---

## 3. API the App provides to the Arcade

All calls are server-to-server between the App backend and the Arcade backend, except the bridge
calls the WebView needs.

| Call | Direction | Purpose |
|---|---|---|
| `getSessionToken()` | bridge → App | Short-lived JWT: `identity_id` (stable, opaque), `validated: bool`, `country`, `exp`. No email, no name. |
| `getAttestation(nonce)` | bridge → App | Play Integrity / App Attest verdict for the current session, bound to the Arcade's nonce. |
| `openAccountScreen()` | bridge → App | Hand-off for Explorer players ("Ready to validate?"). |
| `POST /credit/apply` | Arcade → App backend | `{identity_id, amount_credit, reason:"arcade_topup", idempotency_key, batch_id}`. Applies validation credit to the identity's platform account. Response carries the ledger entry id. Idempotent. |
| `GET /credit/limits/{identity_id}` | Arcade → App backend | Platform-side view of what this identity has received today/this week/lifetime across *all* programs, so caps hold even if the Arcade's own ledger is wrong. |
| `POST /fraud/flag` | Arcade → App backend | `{identity_id, signals[], severity}`. The platform is the party exposed to identity fraud (the $21 signup credit); Arcade signals feed its review. |
| Remote config | App → Arcade | `arcade.enabled`, `arcade.rewards_enabled`, per-country reward gating, caps, pool size. All read at launch and on foreground. |

What the Arcade provides back: a `/health` endpoint, daily batch reports (applied credit by
identity, review outcomes), and telemetry events (§6).

---

## 4. Constraints inside a financial app

1. **Rewards only for demonstrated learning.** Never for trades, deposits, holding, referrals,
   installs, shares, or opening screens. This is Apple 3.1.5(v) and Google's "don't glamorize
   earnings from trading" in one rule.
2. **Fixed, published ratio.** Top-up per completed expedition is a constant shown in-app (Google's
   gamified-loyalty rule). No multipliers, no chance.
3. **No casino aesthetics.** No spinners, slot reels, coin showers, "jackpot"/"win big" copy. Tablets,
   ledgers, expeditions. Apple's age-rating questionnaire asks about simulated gambling; the honest
   answer must be "none."
4. **Official Rules in the tab** (Apple 5.3.2): eligibility 18+, period, scoring criteria, credit
   value, sponsor, tax responsibility, "Apple and Google are not sponsors."
5. **Vocabulary.** "Validation credit," "top-up," "expedition," "tablet." Never "earn," "cash,"
   "dollars," "win money," or anything implying the player ends up better off financially. Every string passes `tools/dgd.py lint` in CI.
6. **Geo-gating is a legal requirement, not arbitrary** (Apple 3.2.2 vs 5.3.4): rewards on for US
   only at pilot; XP everywhere.
7. **Wiki compliance rails apply to game content** exactly as to videos: educational, never
   investment framing; no price predictions; no "get in early."

---

## 5. Release gating — the kill switch

Because an Arcade objection can now block a trading-app release:

- `arcade.enabled` and `arcade.rewards_enabled` are **server-side flags, default off** in any
  build submitted for review until the Foundation decides otherwise. Off = tab hidden, or tab shown
  with XP only.
- Ship the tab in an **update after** the trading app is already approved, not in the first
  submission.
- Reviewer notes for that update: describe the tab as an educational quiz-game with a small,
  fixed-ratio loyalty credit for verified account holders; point to Official Rules; state no
  chance, no purchase, no rewards for trading.
- If a reviewer objects, flip `rewards_enabled` off and resubmit within the day; the tab survives
  as pure education.

---

## 6. Telemetry and review

Events (all with `identity_id` hashed, no PII): `expedition_start/complete/fail`, `tablet_answered`
(item id, tier, latency, correct), `daily_ledger_solved`, `topup_queued/applied/reversed`,
`fraud_flag`, `handoff_click`, `attestation_result`. These feed the plan's success metrics
(mastery per pillar, D1/D7/D30, funnel, integrity) and the daily review queue.

---

## 7. Work split

| Arcade team | DGD App developer |
|---|---|
| Game runtime (web bundle), Arcade backend, question bank + lint CI, caps/pool logic, review queue, Official Rules text, telemetry | Tab + WebView/RN host, bridge (`getSessionToken`, `getAttestation`, `openAccountScreen`), `/credit/apply`, `/credit/limits`, `/fraud/flag`, remote-config flags, reviewer notes in the store submission |

Sequence: (1) agree the API contract above → (2) Arcade PWA pilot runs standalone with a stub
bridge → (3) developer embeds the same bundle behind flags → (4) tab ships in a post-approval
update, rewards off → (5) rewards on for validated US accounts at pilot caps.

---

## 8. Questions for the developer

1. Stack: React Native, Flutter, or native? (decides WebView vs module)
2. Does the App backend already expose a per-identity credit ledger with the $21 signup credit, or
   does that need building? The Arcade needs `/credit/apply` and `/credit/limits` against it.
3. Which attestation is already in place (Play Integrity tier, App Attest)? Can the verdict be
   bound to a caller-supplied nonce?
4. Remote-config system in use (Firebase, LaunchDarkly, in-house)?
5. Store status: submitted, approved, or pre-submission? This sets when the tab can ship.
6. Existing age rating and Financial Features declaration answers — the Arcade must not change
   them.
