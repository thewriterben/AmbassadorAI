# Reference — Tool Matcher

Decision logic for Stage 3 (matching a free tool stack to the ambassador's constraints).
Current free-tier *facts* live in `../../LLMWiki/tools/` — read those for specifics and
always tell the user to re-confirm on the tool's site (free tiers shift monthly). This
file is the **reasoning**, not the price sheet.

## Step 1 — Ask four questions (or infer them)

1. **Camera or faceless?** On camera builds the most trust for finance-adjacent content;
   faceless is fastest and needs no AI-voice disclosure only if you use real recorded voice.
2. **Primary platform?** X / YouTube Shorts / Instagram Reels / TikTok — drives length,
   specs, and policy (see `../../LLMWiki/craft/platform-specs.md`).
3. **Time budget?** ~1 hr (single faceless explainer) vs. half-day (batch a week).
4. **Cross-posting?** If yes, **watermark-free export matters** — a watermark from one app
   can get a video down-ranked or rejected on another.

## Step 2 — Pick the pipeline

| Situation | Pipeline (from `tools/workflows.md`) |
|---|---|
| No camera, fastest | **A — Faceless Explainer** |
| Wants trust / personal brand | **B — Talking Head + B-roll** |
| Consistency at scale | **C — Batch & Schedule** |

## Step 3 — Match each job to a free tool

Name a **primary + a backup** for every job. Defaults (verify via `tools/`):

- **Script:** ChatGPT / Claude / Gemini free tier. (Always with the master guardrail block.)
- **Voice:** ElevenLabs free (label as AI) → backup Microsoft Edge "Read Aloud". Real
  recorded voice = highest trust, no AI-voice label needed.
- **AI video / b-roll:** decide by the watermark question —
  - *Top quality, has Google account:* **Veo** (route export through Google Vids for a
    clean export; free Google Flow now carries a visible "Made with Veo" mark).
  - *Watermark-free, no fuss:* **Pika** or **Pixverse** (clean free exports).
  - *Need daily volume:* **Kling** or **Hailuo** (mind/crop the watermark).
  - *Quick image→motion:* **Vheer / Wan**.
- **Still images / title cards:** Bing Image Creator, Gemini/Imagen, Leonardo, Firefly.
  Generate title cards **without text** (AI misspells); add crisp text later in CapCut/Canva.
- **Edit + captions:** **CapCut** (free full editor, auto-captions). Keep a reusable
  template project with caption style + disclosure overlays pre-built.
- **Music / SFX:** YouTube Audio Library, Pixabay, Uppbeat — confirm the license covers
  commercial + this platform + short-form; save the license.
- **Schedule:** native schedulers (YouTube, Meta Business Suite) or a free Postiz/Buffer
  tier. Mind X automation rules — tailor captions per platform, no spammy duplicates.

## Step 4 — Match the *visuals* to the DGD topic

Suggest abstract/illustrative b-roll that's both on-theme and low-compliance-risk:

| Topic | Suggested generation theme |
|---|---|
| Scarcity / sound money | Single gold coin, vault, engraved fixed-supply grid |
| Inflation / debasement | Banknotes eroding to dust, shrinking stack (illustrative, no real person) |
| Decentralization | Abstract glowing node network, no center |
| Circulation | Isometric supply chain: store → truck → factory → mine, gold line of light |
| Monetary history | Vintage-engraving busts, printing presses, old market floors |

Never generate realistic fake people/events or fake news/charts implying gains.

## Step 5 — State the caveats every time
- Free tiers (credits, watermarks, resolution, even tool names) change monthly — re-check.
- Prefer no-watermark exports when cross-posting.
- No tool excuses a compliance slip; the message rails apply no matter how it's made.

→ Facts: `../../LLMWiki/tools/toolkit-overview.md` and per-job pages. Pipelines:
`../../LLMWiki/tools/workflows.md`.
