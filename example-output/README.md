# Example output for dgd-video-studio

This folder contains a small, human-reviewed example output for the `dgd-video-studio` skill. Use these files as a baseline to verify skill behavior when prompts change.

**Regenerated 2026-07-19 from an end-to-end dry run of the seven-stage loop.**
The previous baseline was a generic *Bitcoin* explainer with zero mentions of
DGD, no "not financial advice" line, no FTC or AI disclosure, and soft
investment framing ("a hedge against inflation", "treat it like an experiment",
"check the description for links") — and it PASSED the linter, which is how four
of those phrases became new rules. A baseline that models non-compliant output
is worse than no baseline.

Files:
- script.md — a 45-second script on how releases are split, as a 4-column table
- shot-list.md — six shots mapped to the actual asset commands that produce them

Both are linted on every CI run via the compliance evals; regenerate them
whenever the substance or the prompts change.
