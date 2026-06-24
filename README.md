# AmbassadorAI

AmbassadorAI is a curated collection of agent "skills", templates, knowledge, and documentation designed to produce short-form, educational "Digital Gold" style videos and to be installed into agent runtimes (Claude, Hermes-style agents, or local skill runners). The repository is documentation-first: skill descriptors (SKILL.md), templates, prompts, and a knowledge base the agent or creators can reference.

This README is written for Claude users and explains how to install, run, and extend the skills in this repository.

---

## Quick links

- HOW-TO-USE-SKILLS.md — installation and operational guide (read this first)
- skills/dgd-video-studio/SKILL.md — example skill (Digital Gold video workflow)
- LLMWiki/ — prompts, templates, compliance, and supporting documentation
- Knowledge Base/ — PDFs and reference material (Digital Gold whitepaper, crypto analysis)

---

## The toolchain — one command

The agent's stages are backed by runnable tools in `tools/`, all driven from a single
entry point, `tools/dgd.py`:

```bash
python3 tools/dgd.py doctor                      # health check (tools, rails, deps)
python3 tools/dgd.py assets kit --headline "…" --outdir raw/ep1   # Stage 5 assets
python3 tools/dgd.py lint script.md --require-disclosure          # Stage 7 linter
python3 tools/dgd.py evals                        # red-team rails regression (21 cases)
python3 tools/dgd.py publish --caption "…" --media v.mp4 --schedule … --outdir raw/ep1/publish
python3 tools/dgd.py perf sync --dir raw/ep1/publish              # auto-record metrics
python3 tools/dgd.py perf report                                  # evidence report
python3 tools/dgd.py dashboard --out dashboard.html               # visual ledger
```

Two web front-ends:

```bash
python3 tools/dgd.py site      # -> site/  public Ambassador Resource Hub (static, deploy to GitHub Pages)
python3 tools/dgd.py serve     # -> http://127.0.0.1:8000  local creator cockpit — runs the tools + true AI generation; never posts
```

The **hub** is an audience-facing docs site built from the wiki (talking points, hooks,
do/don't language, compliance, templates, toolkit) plus a client-side **idea & prompt
generator** (compliance-safe, lint-checked at build) — no internal tooling. The **local
server** is the ambassador's private workspace (lint, asset render, gated publish, live
ledger). A GitHub Pages workflow (`.github/workflows/pages.yml`) deploys the hub on push.
See `skills/dgd-video-studio/reference/web-dashboard.md`.

| Tool | Stage | What it does |
|---|---|---|
| `dgd_assets.py` | 5 | Renders on-brand title cards, thumbnails, disclosure overlays, abstract b-roll motifs; `kit` builds a whole set + contact sheet. |
| `compliance_lint.py` | 7 | Deterministic, fail-closed scan for banned investment/price/return/solicitation framing. |
| `run_compliance_evals.py` | 7 | 21-case red-team suite proving the rails hold (also runs in CI). |
| `dgd_publish.py` | 6 | Tailors compliant per-platform captions, gates each, emits a Postiz `--json` campaign + `publish.sh`. |
| `dgd_performance.py` | C/D | Records post metrics to a ledger, writes evidence reports + an HTML dashboard. |
| `dgd.py` | — | Umbrella router + `doctor` health check. |
| `build_hub.py` | — | Builds the public hub from the wiki + the idea/prompt generator (`dgd site`). |
| `dgd_web.py` | — | Local control-panel **server** that runs the tools (`dgd serve`). |
| `dgd_ai.py` | — | True AI generation (script/ideas/hooks/caption), compliance-gated (`dgd ai`). |

Every text-bearing tool enforces the same communications discipline; nothing publishable
escapes the compliance gate.

## What this repository contains

Top-level structure (important files and directories):

```
README.md
HOW-TO-USE-SKILLS.md         # Usage and installation guidance for skills
LLMWiki/                     # Templates, prompts, documentation, compliance notes
Knowledge Base/              # Reference PDFs and whitepapers
skills/                      # Agent-installable skills (SKILL.md files)
  dgd-video-studio/
    SKILL.md                 # Example skill flow: brief → script → shots → assets
    reference/               # Supporting materials for the skill
DGD-Ambassador-Wiki.zip      # Archive with additional handbook material
.gitattributes
```

The repo is intended to be used with an existing agent runtime. It does not include an LLM server or hosted agent — instead it supplies skills and docs that you upload or copy into your Claude (or other) environment.

---

## Before you start (prerequisites)

1. A working Claude access method:
   - Claude/Cowork web interface that supports uploading skills (CoWorker/skills UI), or
   - An environment that uses Claude API/SDK where you can load skill files into an agent runner.
2. A local shell (macOS / Linux / WSL) or file access to the agent runtime to copy files if you prefer local installation.
3. Familiarity with editing Markdown and simple YAML frontmatter (SKILL.md files use frontmatter).

Optional but useful:
- A local editor (VS Code, Vim)
- A place to host video assets (stock library or a small S3 bucket)

---

## Quickstart — install the example skill into Claude

There are two common installation flows for Claude users: (A) use the Cowork / web UI upload (if available), or (B) copy the SKILL.md into a local agent runtime that runs Claude-facing skills. The repository's HOW-TO-USE-SKILLS.md contains additional platform-specific notes; these steps are the shortest path to try something now.

1) Clone the repo locally:

```bash
git clone https://github.com/thewriterben/AmbassadorAI.git
cd AmbassadorAI
```

2) Inspect the example skill and docs:

```bash
less HOW-TO-USE-SKILLS.md
less skills/dgd-video-studio/SKILL.md
less LLMWiki/index.md
```

3A) Install via Claude Cowork (web) — Upload SKILL.md
- Open your Claude Cowork / skills UI.
- Find the "upload skill" or "import" button.
- Upload `skills/dgd-video-studio/SKILL.md` (or open and paste the contents into the UI).
- Follow the UI steps to enable the skill.

3B) Install into a local agent runtime that uses Claude (copy-file method)
- If your agent runtime stores skills on disk, copy the skill folder to the agent's skills directory and restart the agent service. Example (replace destination path with your runtime):

```bash
# Example: copy to a local agent running at /opt/claude-agent/skills
cp -r skills/dgd-video-studio /opt/claude-agent/skills/
# Restart your agent service if required (service name depends on your runtime)
# sudo systemctl restart claude-agent
```

3C) Verify in the agent UI or CLI that "dgd-video-studio" appears in the skill list. The HOW-TO-USE-SKILLS.md file has more troubleshooting steps if the skill does not appear.

---

## Example: Running the sample workflow in Claude (manual / chat-mode)

If you want to try the skill without installing it as a formal skill in Claude, you can run the workflow manually by copying the prompts from the SKILL.md and running them in a Claude chat. The following example is a minimal manual run you can paste into Claude to emulate the end-to-end workflow.

Prompt (paste into a Claude chat):

"You are a video-writing assistant that produces short (45–75s) educational 'Digital Gold' style videos.

Task: Create a short video plan and deliverables from this brief.

Brief: "Produce a 60-second explainer about why 'Digital Gold' (Bitcoin) is considered 'sound money' by some investors. Audience: general-interest viewers, 45–65 years old, curious but not expert. Tone: confident, calm, educational. Deliverables: (1) 60s script (with time-stamped beats), (2) 6-shot storyboard with short visual descriptions, (3) suggested on-screen captions, (4) 3 thumbnail/title options, (5) suggested hashtags and keywords."

Instructions: Reply with clearly labeled sections: Script, Storyboard (shots 1..6), On-screen text, Title & thumbnails, Tags. Keep the script suitable for a single narrator and include cues for B-roll (stock footage suggestions)."

Claude will respond with structured sections. Copy the generated script into your video editor or use the generated shot list to assemble assets.

---

## Recommended Claude-specific installation notes

- If using an official Claude "CoWorker" web skill uploader: upload the SKILL.md and any supporting templates you want to make available to the skill (templates from `LLMWiki/templates/`).
- If your organization runs a managed skill repository for Claude, follow that repository's registration process — typically you upload SKILL.md and optionally a small JSON or metadata file so the platform can index the skill.
- If you run a local wrapper (a small agent runner that proxies to the Anthropic/Claude API), place `skills/dgd-video-studio` in the runner's skills path. Make sure the runner can access any tools the SKILL.md references (tool matchers are documented in HOW-TO-USE-SKILLS.md).

Security & data handling: the repository contains public templates and PDFs. Do not upload private keys, API tokens, or user data into the repo. For hosted Claude usage, follow your org's secrets policy: use environment-level keys rather than embedding credentials in SKILL.md.

---

## Skill authoring — how to add or edit a SKILL.md

If you want to add new skills or change the `dgd-video-studio` skill, follow these guidelines:

1. SKILL frontmatter: Each skill uses a small YAML frontmatter block describing `name`, `description`, `version`, and tags. Keep the frontmatter minimal and descriptive.
2. Clear steps: The body of SKILL.md should contain the step-by-step prompts the agent will run: brief intake, script generation, shot/asset list, quality checks, and output packaging.
3. Templates and prompts: Put reusable prompts or templates into `LLMWiki/templates/` and reference them from the SKILL.md with a path or clear name.
4. Tools: If the skill expects tool usage (image fetch, voiceover, video render), document the required tool names and the expected interface in the `reference/` folder.
5. Licensing & citation: If a skill uses third-party content (the Knowledge Base PDFs), cite the source and include any license notes.

Suggested workflow when authoring:
- Create `skills/<skill-name>/SKILL.md` with frontmatter and a human-friendly README at the top.
- Add example outputs in `skills/<skill-name>/example-output/` if useful.
- Add templates to `LLMWiki/templates` and link them in the SKILL.md.
- Submit a PR with the new skill; reviewers should run the prompts locally or in a Claude sandbox to verify.

---

## Contributor checklist

- Run the prompts locally in a Claude sandbox or QA environment before opening a PR.
- Include example output (script + shots) in the skill folder when possible.
- Keep templates small and modular — prefer single-purpose templates (e.g., `script-template.md`, `shot-list-template.md`).
- Add or update index pages in `LLMWiki/` so people can find the new skill and templates.

---

## Troubleshooting

- Skill doesn’t appear in Claude UI after upload: check the SKILL.md frontmatter for required fields (name/version) and ensure the UI supports the SKILL.md format. Try a minimal SKILL.md that only contains frontmatter and a short prompt to confirm upload works.
- Generated script is too long or too short: add explicit constraints in the prompt (e.g., "keep the script to 55–70 words" or "60 seconds at conversational pace ~130 words").
- Agent returns irrelevant answers: add more structure to the prompts and include example outputs or a short rubric (what counts as a good script, shot examples).

If you still have problems, open an issue in this repository with the `skills/<skill-name>/SKILL.md` attached and a brief reproduction step.

---

## Example: Minimal script template

You can copy this prompt into Claude to quickly produce the script skeleton used by the skill:

```
You are a short-form video writer. Create a 60-second script (approx. 120–160 words) about: <INSERT TOPIC HERE>. Audience: general-interest adults. Tone: confident, calm, educational. Deliverables: (1) 60s script broken into 6 time-stamped beats, (2) 6 short shot descriptions for B-roll, (3) 3 headline options.
```

Replace `<INSERT TOPIC HERE>` with your brief.

---

## File of record & additional reading

- HOW-TO-USE-SKILLS.md — definitive installation/operation notes
- skills/dgd-video-studio/SKILL.md — example skill
- LLMWiki/ — index and templates
- Knowledge Base/ — reference PDFs (Digital Gold whitepaper, Cryptocurrency Analysis)

---

## License & authorship

AmbassadorAI materials in this repository are provided as-is for use and experimentation. If you plan to republish skill content or templates commercially, check the license of any included assets in Knowledge Base and follow the attribution requirements of those sources. (If you want a formal license file added to the repo, tell me which license you prefer and I will add LICENSE.md.)

---

## Next steps I can help with

- Add a Claude-specific installation script or a single-command import that uses your organization's Claude skill API (if you share which Claude product you run).
- Create a one-click example that runs the dgd-video-studio prompts in a Claude chat (a copy-paste prompt bundle).
- Draft a CONTRIBUTING.md and a small PR template for skill submissions.

If you want me to commit any of those now, tell me which one to add next.
