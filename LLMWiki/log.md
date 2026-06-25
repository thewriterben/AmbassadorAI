# Log — DGD Ambassador Video Wiki

Append-only. Format: `## [YYYY-MM-DD] <type> | <summary>`. Newest at bottom. Quick view: `grep "^## \[" log.md | tail -5`.

## [2026-06-16] init | Wiki created
- Ingested **Digital Gold White Paper** (58pp) as the source of truth for DGD facts (six pillars, CFV/DGSB, PoP distribution, single-price circulation, four participation pathways, §12 non-security & communications discipline). Noted **Cryptocurrency Analysis.pdf** (1086pp) and **TII.pdf** (269pp) as supporting, not yet deep-ingested.
- Researched (web, June 2026) current free AI tools: video (Veo via Gemini, Kling, Hailuo, Pika, Vheer/Wan), voice (ElevenLabs, Edge TTS), images (Bing, Gemini/Imagen, Firefly, Leonardo, Ideogram), captions/editing (CapCut, AutoSubtitles, Submagic), music (YouTube Audio Library, Pixabay, Uppbeat).
- Researched platform policies: TikTok (crypto/financial barred in branded content; educational crypto allowed), Instagram/Meta (Paid Partnership + in-video disclosure), YouTube (mandatory altered/synthetic disclosure since 2025-05-21; "paid promotion"), X ("Made with AI"/"Manipulated Media" labels). FTC material-connection + front-loaded disclosure standard; Shorts 2026 ranking favors replays/shares over raw watch time; 1-second hook.
- Built full LLM-wiki structure per `../Knowledge Base/Core/llm-wiki.md`: schema (CLAUDE.md), README, index, log.
- Wrote 7 `dgd/` pages, 6 `compliance/` pages, 8 `tools/` pages, 4 `craft/` pages, 3 `prompts/` pages, 4 `templates/` pages.
- Decisions captured: platforms = X, YouTube Shorts, Reels, TikTok; structure = full LLM-wiki pattern; audience = some social-media experience, new to AI video.
- **Prime directive baked into every content page:** educational, never investment framing (WP §12.11).

## [2026-06-16] lint | Cross-reference & compliance verification pass
- Verified all 36 markdown pages: **every internal cross-link resolves** (automated check).
- Ran a compliance-drift scan for profit-framing language; all hits were inside intentional "do-not"/negative-example contexts on compliance pages. **No investment-framing violations in instructional content.**
- Confirmed core DGD figures (21M cap, 19M circulating, 80M user target, $1.983T benchmark, 70% adoption weight, 64s block) are consistent across `dgd/` pages and cited to the White Paper.
- Wiki ready for ambassador use.

## [2026-06-16] add | "6 Rules of Real Money" ready-to-shoot script pack
- Added `templates/six-pillars-series-scripts.md`: 8 episodes (intro + 6 pillars + synthesis), each with timed Spoken / On-screen / Visual columns, hooks, hashtags, reusable disclosure, and compliance notes. All lines educational; figures cited to WP. Linked from index.

## [2026-06-16] export | PDF handbook
- Compiled a shareable, branded PDF handbook from core wiki content for ambassador distribution.

## [2026-06-16] add | Positioning topics: "safe harbor coin" & "degen"
- Ingested WP §12.7–12.9 (March 2026 Joint Interpretive Release five-part taxonomy; digital-commodity definition "...rather than from expectations of profit"; Atkins "Regulation Crypto Assets" framework / Peirce Token Safe Harbor; DAO Report & Ripple lineage).
- Confirmed "degen" appears in **no** source PDF; positioned DGD as the **anti-degen** ("not a speculative instrument").
- New `dgd/positioning-safe-harbor.md`: the legal meaning of "safe harbor," why DGD aligns as a digital commodity, and the central trap (profit framing both breaks the discipline AND attacks the digital-commodity status). Includes ready-to-shoot script + hooks.
- New `craft/positioning-and-audiences.md`: "boring on purpose" identity, the degen angle (speak-to-not-sell), 7 audience segments, Bitcoin-vs-DGD complementary framing, 6 content franchises, more idea seeds, ready-to-shoot anti-degen script.
- Wove into glossary (digital commodity, Atkins Safe Harbor, degen, rekt, store of value), do-and-dont (two new trap tables), hooks-library (positioning hooks), series-ideas (#8–10), approved-talking-points (positioning lines + topics 13–16). Updated index.
- Repaired index.md (had been physically truncated mid-line during an edit); rewrote complete and verified utf-8 + links.

## [2026-06-16] add | Positioning mini-series script pack
- Added `templates/positioning-series-scripts.md`: 8 ready-to-shoot episodes across two themes — "Is It a Security?" (A1–A4: safe harbor, digital commodity, the 'rather than from expectations of profit' phrase, boring-infrastructure) and "Casino vs Money" (B1–B4: anti-degen, exit liquidity, getting rekt, 'degen' defined). Timed tables, hooks, hashtags, reusable disclosure, and the two pack-specific compliance rails. Linked from index.

## [2026-06-16] export | PDF handbook v2
- Rebuilt the PDF handbook to add a Positioning section (safe harbor = legal not financial; anti-degen 'boring on purpose'); renumbered sections and verified rendering.

## [2026-06-17] daily | content drop generated

## [2026-06-18] daily | content drop generated

## [2026-06-19] daily | content drop generated

## [2026-06-23] daily | content drop generated

## [2026-06-23] verify | weekly tool & policy check
- Re-verified free-tier tools and platform policies; ~8 facts changed, all toward stricter disclosure / tighter free tiers. Biggest: **Veo free export now carries a visible "Made with Veo" watermark** (use Google Vids for clean export); **TikTok & YouTube now auto-detect and auto-label AI content**. Updated 4 tool pages + 2 compliance pages; full report in `maintenance/2026-06-23-verification.md`.

## [2026-06-23] agent | Built DGD Video Studio skill (../skills/dgd-video-studio/) — end-to-end video walkthrough agent; added trends/ folder + dgd-ai-video-trend-radar scheduled task (Fri 7AM); registered both in index.md.

## [2026-06-24] daily | content drop generated
## [2026-06-25] daily | content drop generated
