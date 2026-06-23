---
tags: [templates, automation, content-engine, system]
updated: 2026-06-16
---

# The Content Engine — Daily Drops & Weekly Maintenance

Two automated routines keep the wiki fresh and feed ambassadors a constant stream of quality, compliant ideas. Both run automatically (while the Claude app is open; if it's closed when due, they run on next launch).

## 1. Daily Content Drop — every day, 6:00 AM

A fresh, ready-to-use content brief lands each morning. Each drop includes:

- **Trend radar** — what's spreading in short-form right now + how to ride it *educationally* (never hype).
- **New tool spotlight** — any new/updated free AI tool worth trying, with the free-tier caveat.
- **3 ready idea sets** — each = a hook + a one-line angle + a tie-in to a DGD educational topic + a suggested visual.
- **Prompt of the day** — a copy-paste, compliance-locked script or visual prompt.
- **Topical angle** — a current money/inflation/crypto story turned into a safe educational explainer.
- **Compliance reminder** — the rail most relevant to today's ideas.

**Where it lands:** `daily/YYYY-MM-DD.md`, with the newest entry linked at the top of [`daily/index.md`](../daily/index.md).

## 2. Weekly Verification — every Monday morning

Keeps the wiki's facts trustworthy (free tiers and platform policies move fast):

- Re-checks the **free tiers** of tools in [`tools/`](../tools/toolkit-overview.md) (video, voice, images, captions, music).
- Re-checks **platform policies** for crypto/financial promotion, branded content, and AI-disclosure changes ([`compliance/platform-policies.md`](../compliance/platform-policies.md), [`ai-disclosure.md`](../compliance/ai-disclosure.md)).
- Updates any changed facts, bumps each page's `verified:` date, and writes a changelog to `maintenance/YYYY-MM-DD-verification.md`.
- Appends a summary to [`log.md`](../log.md).

## How the two work together
The weekly pass keeps the **reference** accurate; the daily drop keeps the **inspiration** flowing. Ambassadors should skim the daily drop with coffee, pick one idea, and run it through a [workflow](../tools/workflows.md) → [pre-publish checklist](pre-publish-checklist.md).

## Guardrails (apply to every automated output)
- Educational only; never investment/price/return framing. → [communications discipline](../compliance/communications-discipline.md)
- Safe-harbor = legal, not financial; degen lingo for reach, never to sell a play. → [do & don't](../compliance/do-and-dont-language.md)
- All DGD facts traceable to the white paper.
- Flag disclosure (FTC) and AI-label needs.

## Managing the schedule
Ask Claude to "list my scheduled tasks" to see them, or "change my daily content drop to 7am" to adjust. Task IDs: `dgd-daily-content-drop` and `dgd-weekly-verification`.

## Connects to
- [Daily drops index](../daily/index.md) · [Maintenance log](../maintenance/) · [Series ideas](series-ideas.md) · [Prompt library](../prompts/script-prompts.md)
