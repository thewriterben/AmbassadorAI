# Knowledge Base — source provenance

Read this before replacing anything in this folder.

## Digital Gold White Paper.pdf — KEEP THIS COPY

**Do not overwrite it with the PDF published on digitalgold.co.** The site's copy is older.

| | This folder's copy | `digitalgold.co/Digital_Gold_White_Paper_2026.pdf` |
|---|---|---|
| Distribution model | **Continuous** — "*There are no discrete levels… driven by a single quantity: N*" (§5.1) | **1,000 discrete levels**, account growth 1.136518147%/level (§5.3) |
| Release event | per signup (~88.62 DGD at N≈1,000) | per level; **no per-signup concept exists** |
| Minimum entry | ~$20 (§5.8, §12.14) | ~$40 (§5.7, §12.14) |
| Initial circulating | 7,287,048 | 7,286,048 |
| Latest internal date | June 2026 (PDF metadata 2026-06-16) | March 17, 2026 |

The local copy is the **newer** document, and it is the one whose numbers reconcile with the live
site: its 11,712,952 of per-signup releases + the 2,000,000 staking lock = the 13,712,952 the site
shows as "Community Distribution & Staked Treasury," and its 5,000,000 + 2,287,048 = the 7,287,048
initial circulating supply.

Neither PDF carries a version number, so filenames and dates are the only way to tell them apart.
That is why this note exists.

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
