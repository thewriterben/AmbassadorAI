# Data Schema — `data/<state>.py`

One file per state. Copy `data/_TEMPLATE.py` and fill it in. The file exports three names:

```python
STATE     = "Colorado"        # display name; must match what goes in config.json "states"
CAMPUSES  = [ {...}, {...} ]  # one dict per campus, in whatever order you want them read
DEADLINES = [ (...), (...) ]  # date-certain action items for this state
```

The loader (`scripts/dataset.py`) imports only the states listed in `config.json`, merges
them, and computes countdowns from the run date. Nothing else reads these files.

---

## The campus record

### Identity

| Field | Notes |
|---|---|
| `state` | Must match `STATE` exactly — the builders group by it. |
| `name` | Full official name. Used as the dedupe key in `exclude_campuses`, so be consistent. |
| `city` | `"Boulder, CO"` |
| `type` | `Public` · `Private` · `Private (religious)` · `Public (community college)`. Religious and private matters: they have no public-forum obligation. |
| `tier` | Your priority call — `A — Named target`, `B — Regional`, `C — Opportunistic`. |
| `access` | **1–5. The most important number in the file.** See below. |

**The `access` rating answers one question:** *what does the written policy permit an
outside for-profit organization to do here?* Not how good the audience is.

| | Meaning | Typical marker |
|---|---|---|
| **5** | Open — outside orgs explicitly admitted | A published for-profit vendor tier |
| **4** | Workable — a paid or documented route exists | Rentable space with published rates |
| **3** | Gated — approval or sponsorship required | "Must be sponsored by a recognized student organization" |
| **2** | Hard — commercial activity restricted | A commercial-gain ban with narrow exceptions |
| **1** | Effectively closed | A flat prohibition with no sponsorship path |

A campus with an excellent blockchain club and a flat solicitation ban is a **1**, with the
club noted in `clubs` and the situation explained in `play`. Conflating audience quality
with access sends ambassadors to campuses that turn them away.

### A. Calendar

`start` · `adddrop` · `fallbreak` · `thanksgiving` · `lastclass` · `finals` · `cal_url` ·
`cal_status`

Write dates as a human reads them: `"Mon Aug 24, 2026"`. Put caveats inline — the packet
is read by a person, not parsed. `cal_status` is `CONFIRMED`, `PARTIAL`, or `UNVERIFIED`.

Flag anything unusual directly in the field, because it changes the whole trip:
`"Mon Sep 14, 2026 ⚠ LATEST START IN THE STATE"`, or `"⚠ Term ENDS Nov 20 — no December
window."` Quarter schools start about five weeks after semester schools; that single fact
reorders a tour.

### B. The fair

`fair` · `fair_date` · `fair_outside` · `fair_cost` · `fair_deadline` · `fair_url`

`fair_outside` is the field ambassadors read first. Give the answer *and the sentence that
supports it*: `"YES — 'Community organizations may register…'"` or `"⚠ NO — 'No
organization may sell products, recruit for job openings, or promote a business.'"`

When a date isn't published, don't leave it blank — say what you know:
`"UNVERIFIED — pattern: Wednesday of the first week of classes, 2–5pm. Will post at <url>."`
That's actionable. Blank isn't.

`fair_cost` feeds the budget table automatically, so lead with the number.

### C. The policy — the field that does the real work

`policy` · `policy_url` · `policy_key` · `sponsor_required`

`policy_key` is the longest field in the schema on purpose. An ambassador challenged at a
table needs **the actual sentence**, not your paraphrase. Quote verbatim, in caps for the
operative clause, and keep the citation attached:

> WAC 504-35-050(1): 'University facilities may not be used for private or commercial gain
> including, but not limited to: Commercial advertising; solicitation and merchandising.'

Always capture, if present:

- **Anti-fronting rules.** Language forbidding a campus group from reserving space for an
  outside entity. Six campuses have one, and it closes the workaround that works elsewhere.
- **Whether sponsorship cures the problem.** At EWU, approval is required "whether
  sponsored or not" — sponsorship is irrelevant there. That's worth knowing before you
  spend three weeks courting a club.
- **Deposits, insurance and cancellation terms.** Non-refundable deposits are common.
- **Anything naming financial products or payment credentials.** Rare, and decisive.

### D–G. People, curriculum, events

All four are lists of tuples. Keep positions stable — the builders index them.

```python
"clubs":   [(name, notes, url)],
"faculty": [(name_or_office, title_and_why, dept, "email · phone", url)],
"courses": [(code, title_and_description, url)],
"events":  [(name, detail_including_date, url)],
```

For `faculty`, the second element carries the *why*, and it's what makes the row worth
having. `"Directs the Blockchain Research Lab AND advises the student club — one email
reaches both"` is useful. `"Professor"` is not.

Prefix a row with `⚠` when it's the standout at that campus; the builders highlight those
and the report's derived summary picks the first one as the headline contact.

Where you couldn't confirm an individual, say so in a row of its own rather than omitting
the section: `("(Faculty)", "NOT CONFIRMED — look up at the Finance dept directory", "", "", url)`.

### The judgement fields

**`play`** — one paragraph. What should the ambassador actually do here, and why. Name the
single best door. If the answer is "skip this campus," say it plainly with the reason.
This is the field people actually read, and a clear "no" is more valuable than a hedge.

**`gaps`** — a list of what could not be confirmed, each with the URL or phone number to
close it. Prefix genuinely blocking items with `⚠`. These roll up into a consolidated
to-do list across the whole packet.

**`note`** — optional. Use for a caveat that doesn't fit elsewhere, e.g. a campus commonly
confused with another institution.

---

## The deadline rows

```python
DEADLINES = [
 ("2026-08-27", "Aug 27, 2026", "Oregon State",
  "⚠⚠ BEAVER COMMUNITY FAIR VENDOR REGISTRATION CLOSES, 5:00pm PST",
  "External business $200; tax-exempt $150. Event Sep 25. Fees due Sep 11.",
  "https://…", "ella.tenido@oregonstate.edu · 541-737-1566"),
]
```

Positions: `(iso_date, display_date, campus, action, detail, url, contact)`.

**The ISO date is what makes the packet survive the term.** Countdowns are computed from
it against the run date, so the same data file produces correct "days out" next year
without anyone editing it. Use `""` for monitor-only items with no date — they sort last
and show no countdown.

Include every date-certain item, not just the alarming ones: registration deadlines, event
days, term starts, payment due dates. Term-start rows give the calendar its shape.

`⚠` marks something that needs action; `⚠⚠` marks a hard deadline with money attached.
The builders colour on these and the dashboard's headline is derived from them, so use
them deliberately rather than decoratively.

---

## What "verified" means here

Every value traces to a page you actually loaded. When you couldn't confirm something,
write `UNVERIFIED` and put the URL in `gaps`.

This matters more than it sounds. An ambassador standing on a quad can work with "we don't
know the fee, call this number." They cannot recover from emailing a professor who doesn't
exist, or driving to a fair that moved. **A gap is data. A fabrication is damage.**
