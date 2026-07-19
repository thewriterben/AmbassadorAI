# Knowledge Base — source provenance

Read this before replacing anything in this folder.

## Digital Gold White Paper.pdf — KEEP THIS COPY

**Do not overwrite it with the PDF published on digitalgold.co.** The site's copy describes the
superseded 1,000-level model; this one describes the continuous model the site actually runs.

| | This folder's copy | `digitalgold.co/Digital_Gold_White_Paper_2026.pdf` |
|---|---|---|
| Distribution model | **Continuous** — "*There are no discrete levels… driven by a single quantity: N*" | **1,000 discrete levels**, account growth 1.136518147%/level |
| Release event | per signup (~88.62 DGD at N≈1,000) | per level; **no per-signup concept exists** |
| Minimum entry | ~$20 | ~$40 |
| Initial circulating | 7,287,048 | 7,286,048 |
| Pages | 58 | 58 |
| Latest date in the **body** | March 17, 2026 | March 17, 2026 |
| Creation **metadata** | 2026-06-16 (Pages / macOS Quartz) | not obtained |

**Which one is chronologically newer is NOT established.** Both bodies terminate at the same event
(the 17 March 2026 SEC/CFTC Joint Interpretive Release), both are 58 pages, and no creation
metadata was ever retrieved for the site's copy. Do not repeat the claim that one is "newer" —
an earlier version of this note asserted it by comparing this copy's *file metadata* against the
site copy's *body content*, which is not a like-for-like comparison.

**What IS established** is which copy matches shipped behaviour:

1. The live site describes the **continuous** model — "continuous-N model", each signup advances
   the curve and triggers a distribution. That is this folder's copy, not the site's PDF.
2. The levels system was **eliminated** in favour of per-validation distribution (per the project).
   Continuous is therefore the current direction, and the levels paper the superseded one.
3. This copy's figures reconcile with the site's live numbers: 11,712,952 of per-signup releases +
   the 2,000,000 staking lock = the 13,712,952 shown as "Community Distribution & Staked Treasury",
   and 5,000,000 + 2,287,048 = the 7,287,048 initial circulating supply.

Neither PDF carries a version number or a revision history, and the two share a filename stem, a
page count and a terminal date. That is the root problem — **there is no reliable way to tell these
two documents apart except by reading their distribution mechanics.** That is why this note exists.

## Known open point — who receives a release

The two sources disagree on one operative fact, and the wiki follows the **live site**:

- **This white paper** says releases are "*split equally among all current users*" (Abstract, §5.1,
  §5.3), and describes balance-gating only as a hypothetical: "*If the design were later changed to
  exclude zero-balance users, the only change would be the divisor…*" (§5.6).
- **digitalgold.co (verified 2026-07-19)** states releases are "allocated equally across **funded
  accounts**" / "accounts with an **active validation balance**."

The site describes shipped behaviour, so the wiki documents **funded accounts**. The white paper
anticipated the change; it just hasn't been revised to reflect it.

**If the Foundation confirms otherwise, this is the first thing to correct**, because it changes who
an ambassador can accurately say receives coins. See
`LLMWiki/dgd/supply-and-distribution.md` for how it's currently written.

## Other files

| File | What it is |
|---|---|
| `Cryptocurrency Analysis.pdf` | Background analysis |
| `TII.pdf` | Background |
| `Coin Ref/` | **Required by the toolchain.** `nbgdgd.png` drives all coin rendering — see `skills/dgd-video-studio/reference/coin-assets.md`. Do not remove. |

---
*Reviewed 2026-07-19.*
