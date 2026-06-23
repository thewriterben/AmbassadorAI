---
title: How to Use Skills (Claude Cowork + Hermes Agent)
updated: 2026-06-23
audience: DGD ambassadors and operators of the AmbassadorAI setup
---

# How to Use Skills — a complete how-to guide

This guide explains what **skills** are, how to use them inside **Claude (Cowork)**, and how
to use the *same* skills with the **Hermes Agent** (Nous Research's self-improving agent).
It uses your own **`dgd-video-studio`** skill as the running example.

> **The one big idea:** A skill is just a folder with a `SKILL.md` file. Both Claude Cowork
> and Hermes follow the **[agentskills.io](https://agentskills.io) open standard**, so a
> single skill folder works in *both* tools. You write it once and point each tool at it.

---

## Part 1 — What a skill actually is

A **skill** is an on-demand instruction document the agent loads only when it's relevant.
It turns "a thing you know how to do" into "a thing the agent reliably does the same way
every time."

**Anatomy of a skill folder:**

```
dgd-video-studio/
├── SKILL.md            # required — the instructions + YAML frontmatter
└── reference/          # optional — extra docs the agent loads only when needed
    ├── tool-matcher.md
    ├── compliance-gate.md
    └── trend-application.md
```

**The SKILL.md frontmatter** is what makes it discoverable. At minimum:

```yaml
---
name: dgd-video-studio
description: >-
  When to trigger this skill. The agent reads this to decide whether to load it,
  so write it as "use this when the user wants to ...".
---
```

**Progressive disclosure** is why skills are cheap to keep around. The agent sees only a
short index until it needs more:

| Level | What loads | Cost |
|---|---|---|
| 0 | The list: every skill's `name` + `description` | tiny (~3k tokens) |
| 1 | The full `SKILL.md` body, once the skill is triggered | medium |
| 2 | A specific `reference/*.md` file, only when the procedure calls for it | as needed |

So a 5-file skill costs almost nothing until the moment it's actually used.

---

## Part 2 — Using skills in Claude (Cowork)

This is the app you're in right now.

### 2.1 Install / register a skill
Skills live in your connected folder. Your DGD skill is at
`F:\Documents\AmbassadorAI\skills\dgd-video-studio\`. To make Claude treat it as an
invokable skill, register it in **Settings → Capabilities** (where Cowork manages skills
and plugins) and point it at that folder. Skills you build in a session aren't auto-
installed — registering them there is what turns them into a reusable `/command`.

### 2.2 Invoke a skill — three ways
1. **Slash command:** type `/dgd-video-studio` (optionally with a request after it, e.g.
   `/dgd-video-studio make a Scarcity Short for TikTok`).
2. **Natural language:** just describe the task — "help me make a DGD video about
   inflation." If the skill's `description` matches, Claude loads it automatically.
3. **Ask what's available:** "what skills do I have?" lists them.

### 2.3 Scheduled skills
Claude can run a skill-like task on a schedule. You already have three:
`dgd-daily-content-drop` (6 AM daily), `dgd-weekly-verification` (Mon), and
`dgd-ai-video-trend-radar` (Fri 7 AM). Manage them with "list my scheduled tasks" or
"change my daily drop to 7am."

### 2.4 Good habits
- Keep the **canonical copy** of every skill in `AmbassadorAI\skills\` (your source of truth).
- A skill's `description` is the trigger — make it specific, or the agent won't reach for it.
- The skill carries its own rules with it (the DGD prime directive lives inside the skill),
  so the guardrails travel wherever the skill goes.

---

## Part 3 — Using skills with the Hermes Agent

**Hermes Agent** (by Nous Research) is an open-source, self-improving agent that runs on a
server, VPS, or your machine, and that you can talk to from the terminal *or* from
Telegram / Discord / Slack / WhatsApp / Signal. It has a native skills system that is
**compatible with the same agentskills.io standard** — so your `dgd-video-studio` skill
works in Hermes with little or no change.

> **Windows note:** Hermes has no native Windows build — install it under **WSL2**
> (Windows Subsystem for Linux). Inside WSL, your `F:` drive is at `/mnt/f/`, so
> `F:\Documents\AmbassadorAI\skills` becomes `/mnt/f/Documents/AmbassadorAI/skills`.

### 3.1 Install Hermes

```bash
# inside WSL2 / Linux / macOS:
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc        # reload the shell
hermes setup            # one-time wizard: pick a model provider, configure tools
hermes                  # start chatting
```

`hermes model` switches the LLM (Nous Portal, OpenRouter, OpenAI, your own endpoint, etc.);
`hermes tools` toggles tools; `hermes doctor` diagnoses problems.

### 3.2 Where Hermes keeps skills
The source of truth is **`~/.hermes/skills/`**, organized into category folders, e.g.
`~/.hermes/skills/marketing/dgd-video-studio/`. Bundled, hub-installed, and agent-created
skills all land here.

### 3.3 The clean way to use your DGD skill: point Hermes at your existing folder

Rather than copying, tell Hermes to *also scan* your AmbassadorAI skills folder. Edit
**`~/.hermes/config.yaml`**:

```yaml
skills:
  external_dirs:
    - /mnt/f/Documents/AmbassadorAI/skills
```

Now `dgd-video-studio` appears in Hermes exactly like a native skill — in the index, in
`skills_list`, and as the slash command `/dgd-video-studio`. One folder, both tools, no
duplication. (If the same skill name exists locally and externally, the **local copy
wins**.)

**Alternative (copy it in):**
```bash
mkdir -p ~/.hermes/skills/marketing
cp -r /mnt/f/Documents/AmbassadorAI/skills/dgd-video-studio ~/.hermes/skills/marketing/
```

### 3.4 Invoke the skill in Hermes — three ways
1. **Slash command** (works in the CLI *and* in Telegram/Discord/etc.):
   ```
   /dgd-video-studio make a 35s Six Pillars: Scarcity Short for TikTok
   ```
2. **Natural language:** "help me script a DGD video on why money loses value."
3. **One-shot from the shell:**
   ```bash
   hermes chat --toolsets skills -q "Use dgd-video-studio to draft an inflation explainer"
   ```

### 3.5 Make the skill "Hermes-optimal" (optional polish)
Your current frontmatter (`name` + `description`) is valid everywhere. Hermes can use a few
extra optional fields for better categorization and discovery. You can add them without
breaking Claude (it ignores what it doesn't use):

```yaml
---
name: dgd-video-studio
description: >-
  Use when the user wants to make, plan, script, storyboard, or get tools/prompts
  for a Digital Gold (DGD) educational short-form video. Enforces the Foundation's
  communications discipline.
version: 1.0.0
metadata:
  hermes:
    tags: [video, marketing, compliance, crypto-education]
    category: marketing
---
```

Hermes' recommended body sections are **When to Use → Procedure → Pitfalls →
Verification**. Your skill already maps cleanly: the prime directive + the seven-stage
walkthrough are the procedure, and the compliance gate is the verification step.

### 3.6 Reference files work the same way
Hermes loads a reference file on demand via `skill_view(name, path)` — the same progressive
disclosure as Claude. Your `reference/tool-matcher.md`, `compliance-gate.md`, and
`trend-application.md` come along automatically. (Hermes' own examples use a `references/`
folder; either name is fine because your `SKILL.md` points to the paths explicitly.)

### 3.7 Bundle the DGD skills under one command (optional)
If you later add more DGD skills, Hermes **bundles** let you load several at once. Create
`~/.hermes/skill-bundles/dgd.yaml`:

```yaml
name: dgd
description: Everything for making a compliant DGD video.
skills:
  - dgd-video-studio
instruction: |
  Always enforce the DGD communications discipline (educational, never investment).
  End any publishable output at the pre-publish checklist.
```

Then `/dgd make a Reel about sound money` loads the whole set with that instruction prepended.

### 3.8 Run it unattended (Hermes cron)
Hermes has a built-in cron scheduler with delivery to any platform — the direct analogue
of your Claude scheduled tasks. You could, for example, have Hermes run a weekly trend scan
and **deliver the report to your Telegram**. Describe it in natural language ("every Friday
at 7am, run the trend radar and message me the summary") or see the
[Cron Scheduling docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron).

### 3.9 ⚠️ Important: protect compliance-critical skills from auto-editing
Hermes is **self-improving** — after complex tasks it can create skills, and an autonomous
**Curator** grades, consolidates, and prunes the skill library on a ~7-day cycle. That's
great for general skills, but for a **compliance-critical** skill like `dgd-video-studio`
you do not want the rails silently rewritten. Two safeguards:

- **Keep the canonical copy read-only to Hermes.** Point Hermes at your folder via
  `external_dirs`, and make that directory read-only to the Hermes process (filesystem
  permissions), so agent edits can't change it. The docs are explicit that an external dir
  is *not* a write boundary unless you make it one.
- **Keep the source under version control / backup** (your `AmbassadorAI` folder is your
  master). If Hermes ever proposes changes, review the diff against the canonical copy and
  re-confirm the prime directive and compliance gate survived intact before accepting.

> The skill carries the DGD prime directive inside it, but **the model still has to obey
> it.** On Hermes you choose the model (`hermes model`); pick a capable one and keep the
> compliance gate (`reference/compliance-gate.md`) as the mandatory last step.

---

## Part 4 — One source of truth, two agents

The setup that keeps everything sane:

```
F:\Documents\AmbassadorAI\skills\         ← master copy (edit here, back up here)
        │
        ├── Claude Cowork  → register in Settings → Capabilities
        └── Hermes Agent   → config.yaml: skills.external_dirs → /mnt/f/Documents/AmbassadorAI/skills
```

Edit the skill once; both agents see the change. Claude is your in-app, folder-connected
workspace; Hermes is your always-on, message-from-anywhere agent. Same skill, same rules.

---

## Part 5 — Quick reference

**Claude Cowork**

| Do this | How |
|---|---|
| See your skills | "what skills do I have?" |
| Run a skill | `/dgd-video-studio …` or just describe the task |
| Register a new skill | Settings → Capabilities → point at the folder |
| Schedule a skill | "list my scheduled tasks" / "schedule … every Friday 7am" |

**Hermes Agent**

| Do this | How |
|---|---|
| Install | `curl -fsSL …/install.sh | bash` (WSL2 on Windows) |
| First-time setup | `hermes setup`, then `hermes` |
| Use your folder's skills | add `skills.external_dirs` in `~/.hermes/config.yaml` |
| List skills | `/skills` (in chat) or `hermes chat --toolsets skills -q "what skills do you have?"` |
| Run a skill | `/dgd-video-studio …` (CLI or Telegram/Discord/etc.) |
| Group skills | `hermes bundles create …` → `/<bundle>` |
| Change model | `hermes model` · diagnose: `hermes doctor` · update: `hermes update` |

---

## Sources
- [Hermes Agent — GitHub (NousResearch/hermes-agent)](https://github.com/NousResearch/hermes-agent)
- [Hermes Agent — Skills System docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [Hermes Agent — full documentation](https://hermes-agent.nousresearch.com/docs/)
- [agentskills.io — the open skill standard](https://agentskills.io)

---
*Nothing in this guide is financial, investment, legal, or tax advice. The DGD
communications discipline applies to all content produced by these skills, on any agent.*
