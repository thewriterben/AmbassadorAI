---
tags: [maintenance, verification]
updated: 2026-07-19
---

# 2026-07-19 — digitalgold.co relaunch: distribution model corrected

Triggered by the digitalgold.co upgrade. Verified against the live site on 2026-07-19.

## What changed in the product

1. **Releases go to funded accounts, not all users.** The site states releases are "allocated
   equally across funded accounts" / "accounts with an active validation balance." The wiki had
   said "split equally among all current users" in 8 places. **This was the highest-risk error in
   the wiki** — under the old wording an unfunded account appears to earn coins, and an ambassador
   could also wrongly infer that unclaimed shares inflate everyone else's. They return to treasury.
2. **No levels, tiers or downlines.** Inviting is single-level with a one-time bonus that never
   changes release amounts. Recorded explicitly because it's the assumption a sceptical viewer
   reaches for first.
3. **Validation range** is $20–$500 in ERC-20 USDC/USDT (the $500 cap is new; it's a policy setting).
4. **Delivery** is immediate to the QT wallet on each new confirmed account.

## Source conflict found

The white paper published on digitalgold.co describes the **superseded 1,000-level model**; the
repo's copy describes the **continuous** model the site actually runs, and reconciles with the
site's live figures. Recorded in `Knowledge Base/SOURCES.md` so nobody "updates" the repo by
overwriting it with the site's version.

**Correction:** this was first written as "the site's PDF is older." That is not established —
both bodies end at the same date (17 March 2026), both are 58 pages, and no creation metadata was
retrieved for the site's copy. The original claim compared the repo copy's *file metadata* to the
site copy's *body content*. The distinction that holds is **which model is shipped**, not which
document is newer.

The repo's WP still says "all current users" and describes funded-account gating only as a
hypothetical (§5.6). The wiki follows the **site** for shipped behaviour. Flagged as the first
thing to revisit if the Foundation clarifies.

## Files changed

- `dgd/supply-and-distribution.md` — rewritten: who receives, the curve table, allocation table, `$20–$500` flow
- `dgd/platform-and-tools.md` — **new**: live tools, wallet, protocol specs, ecosystem
- `dgd/participation-pathways.md` — referral is single-level/one-time; supply-chain cascade distinguished from a downline
- `dgd/valuation-cfv-dgsb.md` — post-distribution monthly recalculation; $100k as a conditional maximum; no guaranteed appreciation
- `dgd/glossary.md`, `dgd/approved-talking-points.md`, `compliance/do-and-dont-language.md` — phrasing corrected
- `daily/2026-06-19|25|30.md` — annotated as superseded (archives left otherwise intact)
- `tools/compliance_lint.py` — new `mlm_framing` + `distribution_error` rules; `return_promise` narrowed so "returns to the treasury" is no longer a false positive
- `tools/compliance_cases.json` — 9 new red-team cases; `mech-2` corrected (it asserted the stale model was safe)

## Next review

- Re-verify the live model and the $500 cap on digitalgold.co; both are policy settings.
- Watch for a revised white paper that adopts the funded-account language.
- Marketplace/DEX are Q3/Q4 2026 — say "coming," not "available," until confirmed.
