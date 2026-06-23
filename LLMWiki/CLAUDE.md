# CLAUDE.md — Schema & Operating Instructions for the DGD Ambassador Video Wiki

This file tells an LLM agent how this wiki is structured and how to maintain it. Read it first at the start of any session. (Pattern: see `../Knowledge Base/Core/llm-wiki.md`.)

## What this wiki is

A persistent, interlinked knowledge base that helps **Digital Gold (DGD) Ambassadors** create **educational short-form video** about Digital Gold using **free AI tools**, while staying **compliant** with the Digital Gold Foundation's communications discipline and with each social platform's Terms of Service.

The audience is ambassadors with **some social-media experience** but who are **new to AI video generation**. Write for that level: practical, step-by-step, jargon defined on first use, no condescension.

Primary platforms (in the order ambassadors care about): **X (Twitter), YouTube Shorts, Instagram Reels, TikTok.**

## The prime directive (never violate)

DGD content is **educational, not promotional or financial advice.** The Foundation's White Paper §12.11 ("Marketing and Communications Discipline") binds all public representations. Content must **never**:

- characterize DGD as an investment,
- project or predict price appreciation,
- promise returns or profit from any activity,
- solicit participation on the basis of expected profits,
- give financial, investment, legal, or tax advice.

Every content page in this wiki must be consistent with `compliance/communications-discipline.md`. If a request would produce content that violates the prime directive, refuse and explain why, citing that page. When in doubt, frame as: *"Here is how the system is designed to work"* — never *"here is how you will profit."*

## Layers (from the llm-wiki pattern)

1. **Raw sources** — `../Knowledge Base/` (PDFs: Digital Gold White Paper, Cryptocurrency Analysis, TII). Immutable. Read, never edit. The White Paper is the source of truth for all DGD facts.
2. **The wiki** — this `LLMWiki/` directory of markdown. The agent owns it entirely.
3. **The schema** — this file.

## Directory structure

```
LLMWiki/
  README.md          <- human entry point; start-here for ambassadors
  CLAUDE.md          <- this file (agent instructions)
  index.md           <- catalog of every page, one-line summaries
  log.md             <- append-only chronological record
  dgd/               <- SUBJECT knowledge: what Digital Gold is
  compliance/        <- ToS + Foundation discipline + FTC + AI disclosure
  tools/             <- free AI tools by job (script, voice, video, etc.)
  craft/             <- hooks, structure, viral principles, platform specs
  prompts/           <- copy-paste prompt library
  templates/         <- calendars, briefs, checklists
```

## Page conventions

- Every page starts with a `#` H1 title and a one-sentence purpose line.
- Use YAML frontmatter where useful: `tags`, `updated` (ISO date), `source`.
- Cross-link with relative wiki links. Resolve the path from the current file's folder: from a `compliance/` page use `../dgd/six-pillars.md`; from a root file use `dgd/six-pillars.md`.
- Cite the White Paper as `(WP §X)` when stating a DGD fact.
- Tool/price facts are time-sensitive: tag them `verified: 2026-06` and tell readers to re-check the source link, because free tiers change often.
- Compliance pages are authoritative. Content pages defer to them.

## Workflows

**Ingest** (new source dropped in `../Knowledge Base/`): read it, discuss takeaways, write/refresh the relevant `dgd/` pages, update `index.md`, append to `log.md`.

**Query** (ambassador asks a question): read `index.md` first, drill into pages, answer with citations. File reusable answers back as new pages.

**Draft content** (ambassador wants a video/script): pull from `craft/`, `prompts/`, and `dgd/approved-talking-points.md`; run the result against `compliance/pre-publish-checklist` (in `templates/`) before delivering.

**Lint** (periodic health check): look for contradictions, stale tool facts, orphan pages, missing cross-links, and — most important — any drift toward investment/promotional framing. Flag and fix.

## Maintenance rules

- Update `index.md` whenever you add/rename a page.
- Append to `log.md` on every ingest, major edit, or lint pass. Entry format: `## [YYYY-MM-DD] <type> | <summary>`.
- Re-verify tool free-tiers and platform policies quarterly; they move fast.
