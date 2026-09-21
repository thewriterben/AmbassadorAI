---
title: Reviewed compliance-lint exemptions for the question bank
updated: 2026-09-14
reviewer: unreviewed — awaiting sign-off
---

# Reviewed lint exemptions

The bank's authoring rules (01-seed.md, rule 5) anticipate this: **a distractor that states a
misconception trips the linter by design.** Tier C items exist to put the wrong answer in front of
a player and mark it false, so the banned phrase has to appear — that is the entire teaching
mechanism. Removing the phrase would remove the trap.

The same applies to two other categories: real legal vocabulary ("investment contract" is the
Howey term; there is no synonym), and the glossary terms the wiki itself defines
("store of value", "safe harbor").

Every exemption below is scoped to one file and one term. `tools/bank-lint.py` subtracts these and
fails on anything left over, so a genuinely new violation cannot hide behind a blanket waiver.

**Nothing here exempts on-screen explanation text.** Every explanation must state the correct
mechanic in approved wording; those were reworded rather than exempted.

| File | Category | Term | Why it is allowed |
|---|---|---|---|
| 02-participation-pathways.md | mlm_framing | MLM | Prose and explanation naming the misreading the section exists to refute. |
| 02-participation-pathways.md | mlm_framing | Multi-level | Distractor. The correct answer is "single-level, one-time". |
| 02-participation-pathways.md | mlm_framing | downline | Distractor quoting the vocabulary the wiki tells ambassadors never to use. |
| 02-participation-pathways.md | mlm_framing | Build your team | Distractor, verbatim from the wiki's list of banned phrasings. |
| 02-participation-pathways.md | mlm_framing | residual income | Distractor, verbatim from the wiki's list of banned phrasings. |
| 02-participation-pathways.md | mlm_framing | referral | The pathway's actual name; every item using it states it is single-level and one-time. |
| 02-participation-pathways.md | solicitation | buy | Plain verb in "buy a bigger share", asked in order to answer "no". |
| 03-legal-positioning.md | investment | Investing | Distractor. The correct answer is that safe harbor is a term from law and regulation. |
| 03-legal-positioning.md | investment | investment | "Investment contract" is the Howey test's legal term and the name of the Atkins safe harbor. |
| 03-legal-positioning.md | investment | store of value | Distractor in the anti-degen item. |
| 03-legal-positioning.md | safe_drift | safe investment | The precise misreading this whole section traps. Correct answer marks it false. |
| 03-legal-positioning.md | safe_drift | safe place | Distractor: "a safe place to park your money". |
| 03-legal-positioning.md | safe_drift | regulator approved | Distractor. The correct answer is that no regulator has approved anything. |
| 03-legal-positioning.md | safe_drift | Regulators approved | As above, sentence-initial form. |
| 03-legal-positioning.md | return_promise | profit | Quoting the digital-commodity test: value "rather than from expectations of profit". |
| 03-legal-positioning.md | return_promise | make money | The trap item: framing DGD as a way to make money attacks the classification. |
| 07-valuation-extended.md | price_prediction | undervalued | Correct answer to "which use of the CFV is off-limits". |
| 09-glossary-terms.md | investment | store of value | A glossary term the wiki defines and ambassadors must use precisely. |
| 09-glossary-terms.md | investment | Store of value | Distractor, sentence-initial form. |
| 09-glossary-terms.md | investment | investment | Distractor "safe investment" in the safe-harbor definition item. |
| 09-glossary-terms.md | safe_drift | safe investment | Distractor. The item's whole point is that safe harbor is not this. |
| 09-glossary-terms.md | safe_drift | Safe haven | Distractor in the same item. |
| 09-glossary-terms.md | return_promise | profit | Quoting "no party profits" in a fee-burning definition. |
| 01-seed.md | * | * | Pre-existing seed set, reviewed at authoring time (2026-09-06). |
