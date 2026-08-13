"""Config-driven loader for the DGD Campus Tour packet builders.

Reads config.json (written by the agent for this run), imports only the state
modules the ambassador selected, merges campuses and dated action items, and
computes "days out" from the run date so a packet never ships stale.

Every builder imports from here. Nothing else reads the data/ directory.
"""
import json, os, sys, importlib.util, datetime

ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA   = os.path.join(ROOT, "data")
CONFIG = os.environ.get("DGD_CONFIG", os.path.join(os.getcwd(), "config.json"))

def _load(path, mod):
    spec = importlib.util.spec_from_file_location(mod, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def _slug(s):
    return s.strip().lower().replace(" ", "-")

# ── config ───────────────────────────────────────────────────────────────────
if not os.path.exists(CONFIG):
    sys.exit(f"No config.json at {CONFIG}. See reference/build-and-deliver.md — "
             "the agent writes this file before building.")
CFG = json.load(open(CONFIG, encoding="utf-8"))

STATE_ORDER = CFG["states"]                     # tour order, agent-chosen
TODAY_ISO   = CFG.get("today") or datetime.date.today().isoformat()
TODAY       = datetime.date.fromisoformat(TODAY_ISO).strftime("%B %-d, %Y")
TERM        = CFG.get("term", "")
ORG         = CFG.get("org", "Digital Gold")
ROUTE       = [tuple(r) for r in CFG.get("route", [])]
EXTRA_BUDGET= [tuple(r) for r in CFG.get("budget_extra", [])]
EXCLUDE     = set(CFG.get("exclude_campuses", []))

_today = datetime.date.fromisoformat(TODAY_ISO)

# ── states ───────────────────────────────────────────────────────────────────
CAMPUSES, _dl = [], []
_missing = []
for st in STATE_ORDER:
    p = os.path.join(DATA, _slug(st) + ".py")
    if not os.path.exists(p):
        _missing.append(st); continue
    m = _load(p, "st_" + _slug(st).replace("-", "_"))
    CAMPUSES += [c for c in m.CAMPUSES if c["name"] not in EXCLUDE]
    _dl += list(getattr(m, "DEADLINES", []))

if _missing:
    sys.exit("No data file for: " + ", ".join(_missing) +
             "\nResearch these first — see reference/research-protocol.md, then write "
             "data/<state>.py from data/_TEMPLATE.py.")
if not CAMPUSES:
    sys.exit("No campuses selected. Check config.json states/exclude_campuses.")

# Shared multi-state rows: include only when every state they name is selected.
_sel = {s.lower() for s in STATE_ORDER}
try:
    SHARED = _load(os.path.join(DATA, "_shared_deadlines.py"), "shared").SHARED
except Exception:
    SHARED = []
_names = {c["name"].lower() for c in CAMPUSES}
for row in SHARED:
    blob = (row[2] + " " + row[4]).lower()
    if any(n.split("—")[0].strip()[:14] in blob for n in _names):
        _dl.append(row)

# ── deadlines: dedupe, compute days out, sort ────────────────────────────────
def _days(iso):
    if not iso: return 9999
    try: return (datetime.date.fromisoformat(iso) - _today).days
    except ValueError: return 9999

_seen, DEADLINES = set(), []
for iso, disp, camp, act, det, url, contact in sorted(_dl, key=lambda r: (r[0] or "9999", r[2])):
    k = (disp, camp, act)
    if k in _seen: continue
    _seen.add(k)
    DEADLINES.append((disp, _days(iso), camp, act, det, url, contact))
DEADLINES.sort(key=lambda r: (r[1], r[2]))

PAST     = [d for d in DEADLINES if d[1] < 0]
DEADLINES= [d for d in DEADLINES if d[1] >= 0]

# ── compliance (locked, national) ────────────────────────────────────────────
C = _load(os.path.join(DATA, "compliance.py"), "compliance")

ACCESS_LABEL = {
 5:"Open — outside orgs explicitly admitted",
 4:"Workable — paid or documented route",
 3:"Gated — approval or sponsorship required",
 2:"Hard — commercial activity restricted",
 1:"Effectively closed",
}

# ── budget: derived from campus fair_cost, plus anything the agent added ──────
BUDGET = []
for c in CAMPUSES:
    if c.get("fair_cost") and "not published" not in c["fair_cost"].lower():
        short = c["fair_cost"].split(".")[0][:120]
        BUDGET.append((f"{c['name']} — {c['fair'].split('(')[0].strip()[:44]}", short, c["fair_cost"]))
BUDGET += EXTRA_BUDGET
BUDGET.append(("Insurance (where required)", "Varies",
  "$1M CGL / $2M aggregate is the common ask; some campuses want $3M property. "
  "TULIP is the usual short-term vehicle. See the per-campus policy field."))

def summary():
    nc, ns = len(CAMPUSES), len(STATE_ORDER)
    return (f"{nc} campus{'es' if nc != 1 else ''} · {ns} state{'s' if ns != 1 else ''}"
            f" · compiled {TODAY}")
