# Reference — In-Agent Asset Generation

How the agent **produces** Stage-5 visuals itself, instead of only handing the
ambassador prompts to paste elsewhere. This closes the loop: idea → script →
**finished, on-brand, compliance-safe image assets** in one session, for $0, with
no external account or upload.

The generator is `tools/dgd_assets.py` (Pillow only — no internet, no API key).
It renders the brand's gold + deep-navy editorial style deterministically, so text
is always crisp and never misspelled (the failure mode that makes AI title cards
unusable — see `tool-matcher.md` Step 3).

## What it produces

| Command | Output | Use |
|---|---|---|
| `title` | 1080×1920 cover/title card (serif headline, kicker, subtitle, brand mark, disclosure chip) | First frame / cover / hook card |
| `thumb` | 1280×720 thumbnail | YouTube/X thumbnail |
| `motif` | 1080×1920 abstract b-roll background | Behind captions, scene changes, intros |
| `disclosure` | transparent "SPONSORED · NOT FINANCIAL ADVICE" overlay PNG | The reusable compliance overlay the workflows ask you to keep on hand |
| `lower` | transparent lower-third caption strip | Persistent disclosure / context strip |
| `contact-sheet` | one labelled preview image of a whole asset folder | Show the ambassador every asset at a glance |

**Motif themes** (abstract/illustrative only, mapped to the approved visual table in
`tool-matcher.md` Step 4 and `prompts/image-and-video-prompts.md`):
`network` (decentralization, no center) · `scarcity` (fixed-supply grid + single coin) ·
`erosion` (a stack debasing into dust — illustrative, no people) ·
`supply-chain` (store → truck → factory → mine, gold line of light) ·
`monetary-history` (classical temple, antiquity) · `vault` (vault door ajar to golden light).

## How to run it

From the repo root (the sandbox has Python 3 + Pillow preinstalled):

```bash
python3 tools/dgd_assets.py title \
  --headline "Why your money quietly loses value" \
  --kicker "Sound Money - Ep. 1" \
  --subtitle "A two-minute explainer on how inflation works." \
  --out raw/cover.png

python3 tools/dgd_assets.py thumb --headline "The 1% rule nobody explains" \
  --kicker "Digital Gold" --out raw/thumb.png

python3 tools/dgd_assets.py motif --theme network   --out raw/broll_network.png
python3 tools/dgd_assets.py motif --theme erosion    --out raw/broll_erosion.png
python3 tools/dgd_assets.py disclosure --out raw/disclosure_overlay.png
python3 tools/dgd_assets.py lower --text "Not financial advice - Educational" --out raw/lt.png
```

**One command for a whole episode** — renders the title, thumbnail, both disclosure
overlays, and the motif b-roll set into one folder:

```bash
python3 tools/dgd_assets.py kit \
  --headline "Why your money quietly loses value" \
  --kicker "Sound Money - Ep. 1" \
  --subtitle "A two-minute explainer on how inflation works." \
  --outdir raw/ep1
# optional: --themes "monetary-history,vault" picks specific b-roll
```

Save outputs into the ambassador's **`/raw` asset folder** (the reuse convention from
`tools/workflows.md`). `--seed N` re-rolls the dust/motif layout for variety while
holding the brand.

## The compliance rail is built in (fail-closed)

Every text argument (`--headline`, `--kicker`, `--subtitle`, `--text`) is scanned for
banned investment / price / return / solicitation framing **before** anything renders.
A hit aborts with **exit code 2** and prints the offending term — the asset is *not*
written. This mirrors `compliance-gate.md` Section A at the toolchain level, so an
on-screen word can't slip the rail even if a script does. (Reframe to *mechanism, not
forecast* and re-run.) The generated motifs are abstract vector-style art — **not**
realistic synthetic media — so they do not, by themselves, trigger the realistic-AI
media label; sponsorship (FTC) and "not financial advice" disclosure still apply per
`compliance-gate.md` Sections C–D.

## Kit filenames -> CapCut timeline (Stage 6)

`kit` writes predictable filenames so the assembly step is paint-by-numbers. Map them
onto the `tools/workflows.md` pipeline like this:

| File | Timeline role | Placement |
|---|---|---|
| `01_title.png` | Cover / hook card | First frame, ~0:00-0:02 (strong first frame) |
| `02_thumb.png` | Upload thumbnail | Not on the timeline - set at publish |
| `03_disclosure.png` | Disclosure overlay | Overlay track, pinned in the **first 3-5s** (FTC + not-financial-advice) |
| `04_lower_third.png` | Persistent context strip | Overlay track, full duration or key beats |
| `05-10_motif_*.png` | B-roll backgrounds | Base/background track behind captions and scene changes (visual change ~every 2s) |
| `_contact.png` | Preview only | Reference - never placed in the edit |

Drop these into the reusable **CapCut template project** (caption style + disclosure
overlays pre-built) from `tools/workflows.md`, then auto-caption and proofread. Because
`03`/`04` are the exact reusable disclosure PNGs the workflow tells you to keep, the
template's overlay slots line up 1:1 with the kit output.

## Where this fits the seven-stage loop

- **Stage 5 (Visual & voice).** Offer the ambassador a choice: (a) generate the title
  card, thumbnail, and abstract b-roll **right now** with this tool, and/or (b) take the
  copy-paste prompts from `prompts/image-and-video-prompts.md` into an external tool
  (Veo / Kling / Pika / Bing) when they want **photoreal** b-roll this script can't draw.
  Use this tool for everything text-on-brand and abstract; use external AI for realism.
- **Stage 6 (Assembly & disclosure).** The `disclosure` and `lower` overlays are the
  exact reusable PNGs `tools/workflows.md` tells creators to keep — hand them over here.
- **Stage 7 (Compliance gate).** Because the rail already ran at render time, the gate
  only needs to confirm placement/timing of disclosures, not re-scan the card text.

## When to still reach for an external tool
This generator does **not** make photoreal footage or motion video. For realistic b-roll
(rotating coin, drifting dust, vault reveal) keep using the prompt library + Veo/Kling/
Pika per `video-generation.md`, and **label realistic AI media** per `ai-disclosure.md`.
This tool covers the instant, reliable, perfectly-on-brand layer; external AI covers
photoreal motion. Both obey the same prime directive.

## Connects to
- Logic: `tool-matcher.md` (Step 3 tool choice, Step 4 visual themes) · `compliance-gate.md`
- Prompts (external path): `../../LLMWiki/prompts/image-and-video-prompts.md`
- Pipelines & `/raw` convention: `../../LLMWiki/tools/workflows.md`
- Disclosure rules: `../../LLMWiki/compliance/ftc-disclosure.md` · `../../LLMWiki/compliance/ai-disclosure.md`
