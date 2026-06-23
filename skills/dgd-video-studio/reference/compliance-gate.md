# Reference — Compliance Gate

Stage 7. Run this over every produced script, caption, on-screen text, hook, thumbnail,
and hashtag set **before** green-lighting. It is a fast pre-filter; the authoritative,
fuller list is `../../LLMWiki/templates/pre-publish-checklist.md`, and the rules behind it
are `../../LLMWiki/compliance/communications-discipline.md` and `do-and-dont-language.md`.

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
