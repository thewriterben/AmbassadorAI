---
tags: [how-to, beginner, workflow, video-production, compliance-safe]
date: 2026-06-17
type: guide
source_script: ./2026-06-17-boring-1pct.md
verified: 2026-06
---

# How to Make "The Boring 1%" Video — A Beginner's Step-by-Step Guide

> For ambassadors who are comfortable on social media but **new to AI video**. We'll turn the [script package](./2026-06-17-boring-1pct.md) into a finished ~38-second vertical video using **free tools only**. No prior editing experience needed. Take your time — the first one is the slow one; your fifth will take 30 minutes.

**What you'll end up with:** a 9:16 (vertical) video, ~38 seconds, with AI voiceover, AI b-roll, burned-in captions, the required disclosures on screen, and a music bed — ready to post to TikTok, Reels, Shorts, and X.

**Time:** ~1.5–2 hours your first time. **Cost:** $0.
**Free-tier caveat:** every tool below has a free tier as of June 2026, but caps change monthly — if one is full for the day, use the backup listed.

---

## Before you start: the toolkit (all free)

| Job | Tool | Notes |
|---|---|---|
| Voiceover | **Microsoft Edge "Read aloud"** or **ElevenLabs free tier** | Edge is unlimited & built into the browser. ElevenLabs sounds better but caps monthly characters. |
| B-roll (the moving pictures) | **Google Veo 3.1** in [Google AI Studio](https://aistudio.google.com) | Free daily generations, 720p, no watermark. Backup: **Kling AI**. |
| Editing + captions | **CapCut** (free, desktop or mobile) | Auto-captions, timeline, text, export. This is your "workbench." |
| Music | **YouTube Audio Library** or **Pixabay Music** | Royalty-free. Pick something calm/minimal. |

> Open the [script package](./2026-06-17-boring-1pct.md) in another window now — you'll copy from it constantly. The columns you need: **Spoken (VO)**, **On-screen text**, **Visual**.

---

## Phase 1 — Make the voiceover (15 min)

The voiceover (VO) is your backbone: you'll match every picture to it. Make it first.

1. Open the script package and copy the entire **Spoken (VO)** column — all six lines, in order, into one block of text.
2. **Easiest option (Edge):** open Microsoft Edge → paste the text into a blank page or Word Online → select it → right-click → **Read aloud** → click **Voice options** and pick a calm voice (try "Guy" or "Aria"). Slow the speed slightly. To save the audio, use a free screen/audio recorder, or…
3. **Better-sounding option (ElevenLabs):** go to elevenlabs.io → sign up free → paste the script → choose a calm, dry voice → set stability ~50% → **Generate** → **Download** the MP3.
4. **Delivery direction (paste this as guidance / pick a matching voice):** *calm, dry, slightly amused — like a smart friend cutting through noise, not a hype narrator. Unhurried.*
5. Save the file as `vo.mp3`. Play it once — it should run ~35–40 seconds. If it's rushed, lower the speed and regenerate.

✅ **Compliance check:** read the [do & don't list](../../compliance/do-and-dont-language.md) once while you listen. The VO must never say invest, returns, moon, buy, etc. (The script is already clean — just confirm nothing changed.)

---

## Phase 2 — Generate the b-roll clips (30–40 min)

"B-roll" = the background video. You need **3 short silent clips** (the script's three visual prompts) plus you'll reuse the calm-coin clip for the open and close.

1. Go to [Google AI Studio](https://aistudio.google.com) → sign in with a Google account (free) → find **Veo** / "Generate video."
2. Set aspect ratio to **9:16 (vertical/portrait)** if offered.
3. Copy the **first** AI visual prompt from the script package (the gold-coin one) → paste → **Generate**. It takes 1–3 minutes.
4. Repeat for the **slot machine powering down** prompt and the **code-lattice + ember burn** prompt.
5. **Download** each clip. Name them clearly: `01-coin.mp4`, `02-slot.mp4`, `03-burn.mp4`.
6. If a clip looks wrong, tweak the prompt (add "minimal, calm, no text, no logos") and regenerate. **Never** add real people, real logos, or ticker symbols — keep it abstract.

> **Daily cap hit?** Switch to **Kling AI** (free daily credits) and paste the same prompts. Or generate over two days — there's no rush.
> **Keep it abstract on purpose:** abstract gold/network/casino imagery is safer and avoids accidental claims. Charts that look like a real price = a compliance risk.

---

## Phase 3 — Assemble in CapCut (30 min)

CapCut is where it all comes together. Think of it as stacking layers: video on the bottom, voice and music as audio tracks, text on top.

1. Download **CapCut** (free) from capcut.com, or use the mobile app. Click **New project**.
2. **Set the canvas to 9:16** (portrait). Look for the aspect-ratio button — pick 9:16.
3. **Import** your clips (`01-coin`, `02-slot`, `03-burn`) and `vo.mp3`.
4. Drag `vo.mp3` onto the timeline first. This sets your total length.
5. Now drag video clips onto the track **above** the audio, in script order, lining each visual up with the line it belongs to:
   - **0:00–0:07** → `01-coin` (open) — let it sit calm during the disclosure + hook.
   - **0:07–0:14** → `02-slot` (the casino line).
   - **0:14–0:23** → `01-coin` again (the "picture the opposite" lock-in — reuse it).
   - **0:23–0:31** → `03-burn` (fees burned / steady design).
   - **0:31–0:38** → `01-coin` (calm end card).
6. **Trim** each clip to fit its time slot: click a clip, drag its edge. Don't worry about perfection — get it close to the script's timecodes.

> Beginner tip: if a clip is too short to fill its slot, right-click → **Freeze** a frame, or slow it down (Speed → 0.8x). If too long, just trim the end.

---

## Phase 4 — Add captions (auto, then clean up) (15 min)

Captions massively boost watch time and accessibility — most people watch muted.

1. In CapCut, go to **Text → Auto captions** → select your `vo.mp3` track → **Generate**. It transcribes the voiceover automatically.
2. **Proofread every caption.** Auto-captions mishear things — fix any errors so wording matches the script exactly (compliance applies to captions too).
3. Style them: large, bold, high-contrast (white text, subtle dark box). Position in the lower-middle so they don't collide with the disclosure bar up top.
4. Keep captions to a few words on screen at a time.

---

## Phase 5 — Add on-screen text + the REQUIRED disclosures (15 min)

This is the step beginners skip — **don't.** These are not optional.

1. **Disclosure bar (pin it for the first ~3 seconds, ideally longer):** add a **Text** layer at the very top reading **"#Ad · Sponsored"** and **"AI-generated visuals."** This is the FTC sponsorship disclosure + the AI-content label. → [FTC disclosure](../../compliance/ftc-disclosure.md) · [AI disclosure](../../compliance/ai-disclosure.md)
2. **Headline text beats** (from the script's *On-screen text* column), each appearing over its scene:
   - "The boring 1%." (over the hook)
   - "Casino ≠ money" (over the slot)
   - "Built boring on purpose" (over the lock-in)
   - "Fees burned · no rewards by design" (over the burn)
   - "Follow • White paper in bio" (end card)
3. Keep on-screen text short and high-contrast. Animate gently (fade in) — avoid frantic motion; "calm" is the whole point of this video.

> ⚠️ The disclosure must be **clear and hard to miss** — front-loaded, not buried at the end. A clean script with a hidden disclosure still breaks the rules.

---

## Phase 6 — Music + final polish (10 min)

1. Grab a **calm, minimal** track from the YouTube Audio Library or Pixabay Music. Avoid anything hype/EDM — it fights the message.
2. Drag it onto a new audio track. **Lower its volume to ~15–20%** so the voiceover is always clearly on top.
3. Add a 0.5s fade-in at the start and fade-out at the end (audio + video).
4. Watch the whole thing once, muted, then once with sound. Check: does the picture match the words? Are captions readable? Is the disclosure visible early?

---

## Phase 7 — Export the right way (5 min)

1. Click **Export**.
2. Settings: **Resolution 1080p**, **9:16**, **30 fps**. Filename: `boring-1pct-final.mp4`.
3. Toggle **off** any CapCut watermark/end-card if the free version added one.
4. Save it to your computer.

---

## Phase 8 — Post it (with the platform AI label ON) (10 min)

Upload natively to each platform. **Turn on each platform's AI-content toggle** in addition to your on-screen label.

1. **Caption (disclosure first):** start with **#Ad**, then:
   > "#Ad The most contrarian thing in crypto might be… boring money. Here's the 1% nobody posts. Educational, not financial advice — white paper in bio. 🪙"
2. **Hashtags:** `#soundmoney #cryptoeducation #monetarypolicy #austrianeconomics #fintecheducation`
3. **Flip the AI-content switch:**
   - **TikTok:** "More options" → **AI-generated content** toggle → ON.
   - **Instagram Reels:** advanced settings → label as **AI**.
   - **YouTube Shorts:** in details, mark **"Altered or synthetic content."**
   - **X:** add the post label / note that visuals are AI-made.
4. Put the white-paper link **in your bio** (link-in-bio), not as "buy" — the CTA is *learn*, never *buy*.

---

## ✅ Final pre-publish checklist (do this every time)

Run the full [pre-publish checklist](../../templates/pre-publish-checklist.md). The essentials:

- [ ] No banned words anywhere — VO, **captions**, on-screen text, hashtags. → [do & don't](../../compliance/do-and-dont-language.md)
- [ ] No price prediction, no "buy / early / don't miss out," no profit/return implication.
- [ ] Every DGD fact is design/mechanics only (fixed supply, no staking rewards, fees burned). → [approved talking points](../../dgd/approved-talking-points.md)
- [ ] **FTC sponsorship disclosure** is spoken AND on-screen in the first seconds.
- [ ] **AI label** is on-screen AND the platform's AI toggle is ON.
- [ ] CTA is "follow / read the white paper" — never "buy."

---

## Common beginner mistakes (and the fix)

- **Voiceover too fast →** lower TTS speed; aim for a calm read.
- **Clips don't fill the time →** freeze-frame or slow to 0.8x; or trim the VO pause.
- **Captions out of sync →** in CapCut, drag the caption block left/right to nudge timing.
- **Forgot the disclosure →** add the top bar before you export; it's the one non-negotiable.
- **Music too loud →** voiceover should always win; music ~15%.
- **Charts look like a real price →** swap for abstract b-roll; never imply a forecast.

## Connects to
- [The script package](./2026-06-17-boring-1pct.md) · [Animated preview](./2026-06-17-boring-1pct-preview.html) · [Today's drop](../2026-06-17.md)
- [Video generation tools](../../tools/video-generation.md) · [Do & don't language](../../compliance/do-and-dont-language.md) · [Pre-publish checklist](../../templates/pre-publish-checklist.md)
