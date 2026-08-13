"""<STATE NAME> — copy this file to data/<state>.py and fill it in.

Read reference/data-schema.md for what each field means and reference/research-protocol.md
for how to gather it. The rule that matters most: every value here must trace to a page you
actually loaded. If you could not confirm something, write "UNVERIFIED" and put the URL to
check in `gaps` — an honest gap is useful to the ambassador standing on the quad; an
invented phone number is worse than useless.
"""

STATE = "<State Name>"

CAMPUSES = [
{
 # ── identity ────────────────────────────────────────────────────────────────
 "state":"<State Name>",
 "name":"<Full official name>",
 "city":"<City, ST>",
 "type":"Public | Private | Private (religious) | Public (community college)",
 "tier":"A — Named target | B — Regional | C — Opportunistic",
 "access":3,   # 5 open · 4 workable · 3 gated · 2 hard · 1 effectively closed

 # ── A. academic calendar ────────────────────────────────────────────────────
 "start":"Mon Aug 24, 2026",
 "adddrop":"", "fallbreak":"", "thanksgiving":"", "lastclass":"", "finals":"",
 "cal_url":"", "cal_status":"CONFIRMED | PARTIAL | UNVERIFIED",

 # ── B. the fair / tabling event ─────────────────────────────────────────────
 "fair":"<event name>",
 "fair_date":"<date, or 'UNVERIFIED — pattern: ...' with where it will post>",
 "fair_outside":"<YES/NO + the sentence that says so>",
 "fair_cost":"<published fee, or ''>",
 "fair_deadline":"<registration deadline, or ''>",
 "fair_url":"",

 # ── C. the written rule ─────────────────────────────────────────────────────
 "policy":"<policy name and number, with effective date>",
 "policy_url":"",
 "policy_key":"<quote the operative restrictions verbatim. This field does the real work: "
              "an ambassador reads it at the table when someone challenges them.>",
 "sponsor_required":"<who must sponsor, or 'No — pay the fee', or 'No route exists'>",

 # ── D–G. people, curriculum, events ─────────────────────────────────────────
 "clubs":   [("<club>","<status / why it fits>","<url>")],
 "faculty": [("<name or office>","<title and why they matter>","<dept>","<email · phone>","<url>")],
 "courses": [("<code>","<title and description>","<url>")],
 "events":  [("<event>","<detail incl. date>","<url>")],

 # ── the judgement call ──────────────────────────────────────────────────────
 "play":"<What should the ambassador actually do here, and why. Name the single best door. "
        "If the answer is 'skip this campus', say so plainly and give the reason.>",
 "gaps":["<what could not be confirmed, and the URL or number to close it>"],
 # "note":"<optional caveat — e.g. a campus commonly confused with another>",
},
]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; those sort last and never show a countdown.
DEADLINES = [
 ("2026-08-27","Aug 27, 2026","<Campus>","⚠ <ACTION>","<detail incl. fee>","<url>","<contact>"),
]
