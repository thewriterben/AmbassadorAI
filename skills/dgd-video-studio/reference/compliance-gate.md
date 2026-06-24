# Reference — Compliance Gate

Stage 7. Run this over every produced script, caption, on-screen text, hook, thumbnail,
and hashtag set **before** green-lighting. It is a fast pre-filter; the authoritative,
fuller list is `../../LLMWiki/templates/pre-publish-checklist.md`, and the rules behind it
are `../../LLMWiki/compliance/communications-discipline.md` and `do-and-dont-language.md`.

## 0. Run the automated linter first (mechanical pre-filter)

Before the human checks below, run every text surface through the deterministic linter
— it encodes Section A as code so a banned word can't slip through reviewer fatigue:

```bash
python3 tools/compliance_lint.py path/to/script.md --require-disclosure
# or pipe a caption/hook:  echo "$CAPTION" | python3 tools/compliance_lint.py -
```

Exit **2 = FAIL** (banned investment/price/return/solicitation/"safe"-drift framing) —
do not green-light; apply the printed rewrite and re-run. Exit **1 = WARN** (degen-
contrast lingo, bare dollar figures, missing "not financial advice") — a human must
confirm each. Exit **0 = clean**. The linter is necessary but not sufficient; still run
the structural and disclosure checks below. Rules live in
`../../LLMWiki/compliance/do-and-dont-language.md`; the regression guard is
`tools/run_compliance_evals.py` (21 red-team cases — run it whenever the rules, the
linter, or the runtime model change).

## A. Banned-word / banned-framing scan (auto-fail any hit)

Scan ALL text surfaces (spoken, on-screen, caption, hashtags, title, thumbnail) for:

- **Investment framing:** "investment," "invest," "asset to hold," "store your wealth in,"
  "portfolio," "hold for the long term."
- **Price prediction:** "$X target," "to the moon," "moon," "pump," "100x," "early,"
  "get in now," "next [bitcoin/gem]," charts implying gains.
- **Return/profit promises:** "returns," "ROI," "profit," "gains," "passive income,"
  "I made money," "this prints."
- **Solicitation:** "buy," "don't miss out," "FOMO," "ape in," "load up," "secure your bag."
- **The "safe" drift:** "safe investment," "safe haven," "safe bet," "can't lose,"
  "regulators approved it." ("Safe harbor" is OK **only** as a legal/digital-commodity term.)

Any hit → rewrite to design/idea framing, then re-scan.

## B. The structural checks

- [ ] **One honest idea**, framed as *how the system is designed*, not *how you'll profit*.
- [ ] **"Safe harbor"** (if present) used only as: *designed to qualify as a digital
      commodity, not a security.* Never conflated with a financial "safe."
- [ ] **Degen lingo** (if present) is a contrast/attention hook — sells no play.
- [ ] **Facts verified vs the White Paper.** No invented numbers; price-curve numbers (if
      used) described as a *mechanism*, never a forecast or promise.
- [ ] **No realistic fake people/events** in any generated visual; no false attribution.

## C. Disclosure checks (when applicable)

- [ ] **FTC / sponsorship** (if the ambassador earns DGD recognition): disclosed spoken in
      the first seconds **+** on-screen **+** front-loaded in the caption **+** platform
      branded-content toggle ON.
- [ ] **AI media** (if realistic AI voice/avatar/video): platform AI label ON **+**
      on-screen note. This is a **separate** label from the sponsorship one — neither
      covers the other; both belong in the first 3–5 seconds.
- [ ] **"Not financial advice"** stated (spoken + caption).

## D. The final gut check
> *"If a viewer never acquires a single coin, is this still a useful, honest, educational
> video?"* If **no** → it's a pitch. Rewrite before publishing.

## Output of the gate
- If everything passes: say so, then hand the user
  `../../LLMWiki/templates/pre-publish-checklist.md` to tick off during the actual export.
- If anything fails: list each failing line, the rule it breaks (with the wiki link), and a
  compliant rewrite. Do **not** describe the content as ready until it clears.
