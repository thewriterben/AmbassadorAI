# Knowledge Tablet question bank

The server loads every `.md` in this directory (`README.md` and `ALLOWLIST.md` excepted) and
serves items from it as signed, single-use Knowledge Tablets. **The bank never ships in the
client** — that is the whole point of plan §5.1, so do not copy these files into `app/assets`.

Add a batch by dropping in a new numbered file. Nothing else needs to change.

## Status

| | Count |
|---|---|
| Items | 170 |
| Tier A (definitions) | 46 |
| Tier B (mechanics) | 57 |
| Tier C (misconception traps) | 41 |
| Tier D (numbers and sections) | 26 |
| Phase 1 target (plan §9) | 300 |

Sections, and why the split matters: the scheduler prefers one item per section per expedition, so
a section is a topic boundary, not a file boundary. Several files contribute to the same section
on purpose.

## File format

One `## Section name (source-file.md)` heading, then a table:

```
| Tier | Topic | Question | Correct | Distractors | Explanation | Source |
```

- **Distractors** are separated by `·` and must number at least two, except for true/false items.
- **Explanation** is shown on screen after the answer. It must state the correct mechanic in
  approved wording — this is the one place a banned term is never acceptable.
- **Source** cites a wiki page and, where possible, a White Paper section.
- The parenthetical in the heading is stripped, so `## Six Pillars (six-pillars.md)` serves as
  section "Six Pillars".
- Items are identified by a hash of section + prompt. Duplicate prompts within a section are
  dropped at load time, so re-using a prompt is safe but pointless.

## Authoring rules

1. Every item traces to a wiki page. If the wiki does not say it, it does not go in the bank.
2. No item asks a player to predict, estimate or compare prices or financial outcomes. Curve
   numbers are asked as **mechanics** — release amounts, account counts, caps — never as
   "what will it be worth".
3. Distractors come from the wiki's documented misconceptions: the balance-size misconception,
   the unclaimed-coins misconception, the referral-levels misconception, a mobile wallet, the
   marketplace being live, safe-harbor-as-safe-investment.
4. Items marked ⚠ contain a snapshot that moves and must be served from config, not hard-coded.
   Anything about the platform's funding rules is ⚠ until the Sept 2026 credit change is final.
5. **A Tier C distractor will trip the compliance linter by design** — stating the misconception
   is the teaching mechanism. Those need a reviewed entry in `ALLOWLIST.md`, scoped to one file
   and one term. Explanations are never exempted; reword them instead.

## Linting

```
python arcade/tools/bank-lint.py            # subtracts reviewed exemptions, fails on the rest
python arcade/tools/bank-lint.py --json
```

WARN findings are advisory and shown but do not fail the run: most are dollar figures quoted from
the White Paper and referral mentions the linter asks you to confirm. FAIL findings must be fixed
or reviewed onto the allow-list.

`ALLOWLIST.md` is currently **unreviewed** and needs a compliance sign-off before launch — it is
the artifact a reviewer should read, not the 170 items.

## Gaps against the plan

- 130 items short of the 300-item Phase 1 target.
- No paraphrase variants yet. The plan wants ≥2 per item so a screenshot of one wording does not
  retire the fact.
- Coverage is thin on `compliance/*` (FTC disclosure, AI disclosure, platform policies) and on
  `craft/citable-data.md`. Those are the obvious next batches.
- Two ambassador-facing wiki areas are deliberately absent: anything quoting recognition amounts
  (not in the White Paper, announced on channel) and anything using a live price or account count.
