# Performance loop

`tools/dgd_performance.py` records how each published post performed (pulled live from
`postiz analytics:post`, or ingested from a metrics JSON / flags) into `ledger.jsonl`,
keyed to the hook type, topic, pillar, platform, and format that produced it. The
`report` subcommand ranks those choices by **engagement rate** and **follows-per-1k**
and writes a dated `PERF-YYYY-MM-DD.md` here.

The easiest way to populate it: build the post with `dgd_publish.py --hook … --topic …` (writes `post_meta.json`), run the generated `publish.sh` (logs post-ids to `published.tsv`), then `dgd_performance.py sync --dir <publishdir>` to auto-record from Postiz analytics. A weekly scheduled task runs `report` and messages you the leaders; `dgd_performance.py dashboard` writes a visual HTML view of the ledger.

This is what lets the agent (DGD Video Studio Jobs C & D) recommend hooks and topics
from evidence instead of guesses. The reports are compliance-safe by construction —
engagement is treated as a craft signal, the framing stays educational, and report text is lint-clean.

Privacy: `ledger.jsonl` holds your own post IDs and aggregate counts only.
