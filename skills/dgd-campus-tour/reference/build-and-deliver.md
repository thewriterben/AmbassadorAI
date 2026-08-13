# Building and Delivering a Packet

## The short version

```bash
mkdir -p ~/tour-co-az && cd ~/tour-co-az
cp <skill>/data/_TEMPLATE_config.json config.json    # edit it
DGD_SLUG="DGD-Tour-CO-AZ" python3 <skill>/scripts/build_all.py
```

Four deliverables land in `out/`. Send all of them, then say in three sentences what is
urgent, what is closed, and what still needs a phone call.

---

## config.json

Only `states` is required. Everything else has a sensible default.

| Key | Default | Notes |
|---|---|---|
| `states` | — | **Required.** Display names matching a `data/<state>.py` file. Order = tour order. |
| `term` | `""` | `"Fall 2026"`. Titles the packet and labels every calendar section. |
| `today` | system date | ISO. Drives every countdown. Set it explicitly for reproducible builds. |
| `org` | `"Digital Gold"` | Cover page and headers. |
| `exclude_campuses` | `[]` | Exact `name` values to drop — for campuses already covered by another ambassador. |
| `route` | `[]` | **You write this.** `[leg_title, one_line_summary, [stops…]]`. |
| `budget_extra` | `[]` | `[line_item, cost, note]`. Fuel, lodging, printing — things not derived from fair fees. |
| `top5` | `[]` | Override the report's derived headline items. Leave empty unless you have better. |

### Writing the route

Nothing but you can do this — it needs judgement about drive distance, staggered term
starts, and which stops justify the miles. Group campuses into legs that are genuinely
drivable in sequence, and open each leg with one line explaining why it holds together:

```json
["LEG 1 — Palouse", "WSU is the only semester school here, so its term is already five weeks old when the quarter schools start.",
 ["Aug 21 — WSU Pullman, All-Campus Picnic",
  "Aug 24 — U of Idaho, Moscow (8 miles from Pullman)"]]
```

Say what to **skip** and why, in the route itself. "SKIP Colorado State: payment-credential
ban plus an anti-fronting rule" saves an ambassador a day.

---

## The four outputs

| Format | File | Who it's for |
|---|---|---|
| Dashboard | `<slug>-Dashboard.html` | The ambassador. Filter by state and access level, search across clubs, faculty and policy text. Self-contained — works offline, opens on a phone. |
| Workbook | `<slug>-Master-Workbook.xlsx` | Planning and coordination. 17 sortable tabs. |
| Report | `<slug>-Report.docx` / `.pdf` | Partners and anyone who needs to read it linearly. Sorted state → campus. |
| Briefs | `briefs/**.md` | The repo, and per-campus reading. One file per campus, grouped by state. |

The HTML dashboard is the one most people actually use. If a Claude desktop app is
connected, also persist it with `create_artifact` so it survives the conversation and can
be reopened and updated later.

### Flags

```bash
python3 scripts/build_all.py --only html,md      # subset: xlsx, md, html, docx
python3 scripts/build_all.py --no-pdf            # DOCX without the LibreOffice render
python3 scripts/build_all.py --config path.json  # config elsewhere
DGD_OUT=/some/dir python3 scripts/build_all.py   # output elsewhere
```

`DGD_SLUG` sets the filename stem — use something that names the states, like
`DGD-Tour-CO-AZ`, so an ambassador with several packets can tell them apart.

---

## Requirements

| Need | For | If missing |
|---|---|---|
| Python 3 + `xlsxwriter` | workbook | `pip install xlsxwriter --break-system-packages` |
| Node + `docx` | report | Skipped with a warning. The other three formats carry the same content. |
| LibreOffice (`soffice`) | PDF render | DOCX still written; PDF skipped. |

Nothing else. No network access is needed to build — only to research.

---

## When something fails

**`No config.json at …`** — the builder is telling you exactly what it needs. Copy
`data/_TEMPLATE_config.json` into your working directory.

**`No data file for: <state>`** — that state isn't bundled. Either fix the spelling in
`states` (display names, not slugs — `"New Mexico"`, not `"new-mexico"`) or research it
per `reference/research-protocol.md`.

**`No campuses selected`** — `exclude_campuses` removed everything, or the names in it
don't match the `name` field exactly. They must match exactly.

**A builder raises on a campus record** — almost always a tuple with the wrong number of
elements in `clubs`, `faculty`, `courses` or `events`. The positions are indexed by the
builders; check against `reference/data-schema.md`.

**The report is missing but the others built** — Node isn't installed. Say so rather than
silently shipping three files when the ambassador expected four.

---

## Sanity-check before sending

Open the dashboard and look at it. Thirty seconds catches most problems:

- Does the headline show the right urgent item, or nothing when nothing is urgent?
- Do the campus counts match what you expect?
- Do the access ratings look right — is anything rated 4–5 that actually has a flat ban?
- Does the route read as drivable?

Then check the countdowns against today's date. If the packet says "3 days" for something
that already passed, `today` in the config is wrong.

---

## Delivering it

Send every file, then **read it back in three sentences**: what is urgent, what is closed,
what still needs a phone call. A 120-page PDF nobody opens is not a deliverable.

Two things to state explicitly every time, because they are easy to assume and expensive
to get wrong:

- The compliance material is **not legal advice** — it's a sourced issue map for counsel.
- Fields marked `UNVERIFIED` are **research gaps, not findings of absence**. The URL to
  check is right there, and most are one phone call.

If the ambassador is heading to a campus this week, walk them through
`reference/booth-model.md` out loud rather than pointing at the file. The paragraph at the
end of that file is written to be read aloud.
