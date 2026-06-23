# Reference — Trend Application (Job D)

How the agent learns the latest AI-video trends, themes, and styles, then turns them into
**compliant** DGD content. The dedicated scheduled radar writes reports into
`../../LLMWiki/trends/`; this file is how to read those, refresh them live, and apply them.

## Where the intel comes from (check in this order)
1. **Newest `../../LLMWiki/trends/*.md`** (linked top-of-list in `trends/index.md`) — the
   scheduled radar's latest compliance-filtered report.
2. **Newest `../../LLMWiki/daily/*.md`** — daily drops include a short trend-radar section.
3. **Live `WebSearch`** — only if the above are stale (>~1 week) or the user wants fresh intel.

## What to search for (keep it to ~3–6 queries)
- Trending **short-form formats & hooks** this week (TikTok / Reels / YouTube Shorts / X)
  and any **algorithm/ranking shifts** (e.g., what gates distribution now).
- New or updated **free AI video/voice/image/caption tools**, new **models**, and emerging
  **visual styles** (e.g., a popular b-roll aesthetic, a transition, a caption style).
- One timely **money / inflation / crypto-education** angle that can become a safe explainer.

Prefer recent, reputable sources; note the date; flag anything you can't verify.

## The translation rule (this is the whole point)
A raw trend says *"what's getting views."* Your job is to output *"how a DGD ambassador
rides it educationally."* For each trend, produce a small mapping:

| Field | Example |
|---|---|
| **Trend** | "Outcome-first openers (payoff in first 2s) are out-pulling slow builds ~2×." |
| **Why it works** | Algorithms gate on who passes second ~3; curiosity gap up front. |
| **DGD application** | Open on the surprising fact, not "today I'll explain…". |
| **Topic tie-in** | Scarcity pillar — "Inflation 'cooled.' Your savings still shrank." (`dgd/six-pillars.md`) |
| **Style/visual** | A $100 bill shrinking frame-by-frame; gold+navy. |
| **Compliance note** | Mechanism, not "so buy." Double-disclose if AI + sponsored. |

## Hard filter — never let a trend override the prime directive
Reject or reframe any trend that can only be ridden by:
- implying price/profit/returns or a "get in early" urgency,
- a "safe investment / safe haven" angle,
- realistic AI footage of real people (e.g., a fake central-banker clip),
- fabricated "news," fake gain charts, rocket/casino/money-rain aesthetics used to sell.

A trend is only usable if the educational version still works. If it doesn't, say so and
suggest the nearest compliant adaptation.

## Style adoption
When a *visual style* trends (a caption look, a transition, a color grade), adopt it **only
within the DGD identity**: gold/amber + deep navy/charcoal + white, clean editorial,
abstract/illustrative b-roll, smooth slow motion. Borrow the structure, keep the brand.

→ Filter logic: `compliance-gate.md`. Substance to attach trends to:
`../../LLMWiki/dgd/six-pillars.md`, `dgd/approved-talking-points.md`,
`craft/positioning-and-audiences.md`.
