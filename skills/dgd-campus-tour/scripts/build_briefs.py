import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dataset import (CAMPUSES, DEADLINES, PAST, ACCESS_LABEL, ROUTE, BUDGET, TODAY,
                     TERM, ORG, STATE_ORDER, C, summary)

OUT = os.path.join(os.environ.get("DGD_OUT","out"), "briefs")
def slug(s):
    s=re.sub(r"[^a-zA-Z0-9]+","-",s).strip("-").lower()
    return re.sub(r"-+","-",s)

STARS={5:"●●●●●",4:"●●●●○",3:"●●●○○",2:"●●○○○",1:"●○○○○"}

def brief(c):
    L=[]
    L.append(f"# {c['name']}")
    L.append(f"**{c['city']} · {c['type']}**  ")
    L.append(f"**Tier:** {c['tier']}  ")
    L.append(f"**Access:** {STARS[c['access']]} {ACCESS_LABEL[c['access']]}")
    L.append("")
    L.append("> **RECOMMENDED PLAY**  ")
    L.append("> "+c["play"].replace("\n"," "))
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"## A. {TERM} calendar")
    L.append("")
    L.append("| | |")
    L.append("|---|---|")
    for lbl,k in [("Classes begin","start"),("Add/drop","adddrop"),("Fall break","fallbreak"),
                  ("Thanksgiving","thanksgiving"),("Last day of classes","lastclass"),("Finals","finals")]:
        L.append(f"| **{lbl}** | {c[k] or '—'} |")
    L.append(f"| **Source status** | {c['cal_status']} |")
    L.append("")
    L.append(f"Source: <{c['cal_url']}>")
    L.append("")
    L.append("## B. Involvement fair / tabling event")
    L.append("")
    L.append("| | |")
    L.append("|---|---|")
    L.append(f"| **Event** | {c['fair'] or '—'} |")
    L.append(f"| **Date** | {c['fair_date'] or '—'} |")
    L.append(f"| **Outside orgs admitted?** | {c['fair_outside'] or 'UNVERIFIED'} |")
    L.append(f"| **Cost** | {c['fair_cost'] or 'Not published'} |")
    L.append(f"| **Registration deadline** | {c['fair_deadline'] or 'Not published'} |")
    if c["fair_url"]: L.append(f"| **URL** | <{c['fair_url']}> |")
    L.append("")
    L.append("## C. Solicitation / outside-vendor policy")
    L.append("")
    L.append(f"**{c['policy']}**")
    L.append("")
    L.append(c["policy_key"])
    L.append("")
    L.append(f"**Sponsorship requirement:** {c['sponsor_required']}")
    L.append("")
    L.append(f"Source: <{c['policy_url']}>")
    L.append("")
    L.append("## D. Relevant student clubs")
    L.append("")
    L.append("| Club | Notes | Link |")
    L.append("|---|---|---|")
    for club in c["clubs"]:
        nm,note,url=(list(club)+["","",""])[:3]
        L.append(f"| **{nm}** | {note or '—'} | {('<'+url+'>') if url else '—'} |")
    L.append("")
    L.append("## E. Faculty & staff contacts")
    L.append("")
    L.append("| Name / office | Title & notes | Dept | Contact | Source |")
    L.append("|---|---|---|---|---|")
    for f5 in c["faculty"]:
        nm,ti,dp,ct,url=(list(f5)+["","","","",""])[:5]
        L.append(f"| **{nm}** | {ti or '—'} | {dp or '—'} | {ct or '—'} | {('<'+url+'>') if url else '—'} |")
    L.append("")
    L.append("## F. Courses")
    L.append("")
    L.append("| Code | Title / description | Link |")
    L.append("|---|---|---|")
    for co in c["courses"]:
        cd,ti,url=(list(co)+["","",""])[:3]
        L.append(f"| **{cd}** | {ti} | {('<'+url+'>') if url else '—'} |")
    L.append("")
    L.append(f"## G. {TERM} events")
    L.append("")
    L.append("| Event | Detail | Link |")
    L.append("|---|---|---|")
    for e in c["events"]:
        nm,det,url=(list(e)+["","",""])[:3]
        L.append(f"| **{nm}** | {det} | {('<'+url+'>') if url else '—'} |")
    L.append("")
    L.append("## H. Open questions to close by phone")
    L.append("")
    for g in c["gaps"]: L.append(f"- {g}")
    if c.get("note"):
        L.append(""); L.append(f"> {c['note']}")
    L.append("")
    L.append("---")
    L.append("")
    L.append("**Booth conduct at this campus** — apply the national model in `00-BOOTH-MODEL.md`: "
             "age-gate at 18, educate at the table, capture an email, complete validation off-campus. "
             "No ID scanning, no raffles, no on-site contract signing, no 'free money' language.")
    L.append("")
    L.append(f"*Compiled {TODAY}. Blank fields and 'UNVERIFIED' mean not published on a live page — "
             "research gaps, not findings of absence.*")
    return "\n".join(L)

os.makedirs(OUT,exist_ok=True)
by_state={}
for c in CAMPUSES: by_state.setdefault(c["state"],[]).append(c)

n=0
for st in STATE_ORDER:
    d=os.path.join(OUT,f"{STATE_ORDER.index(st)+1:02d}-{slug(st)}")
    os.makedirs(d,exist_ok=True)
    for c in by_state.get(st,[]):
        open(os.path.join(d,f"{slug(c['name'])}.md"),"w").write(brief(c)); n+=1

# ── 00 — Deadline calendar ────────────────────────────────────────────────────
L=[f"# ⚠ Action Calendar — {TERM}","",f"*{summary()}. 'Days out' counts from {TODAY}.*","",
   "Four registrations and three phone calls this week decide most of the fall.","",
   "| Date | Days out | Campus | Action | Detail | Contact |","|---|---|---|---|---|---|"]
for d,days,camp,act,det,url,contact in DEADLINES:
    mark = "🔴" if (days<=20 and "⚠" in act) else ("🟠" if days<=45 else "")
    dd = "—" if days>=9999 else days
    L.append(f"| {mark} **{d}** | {dd} | {camp} | {act} | {det} | {contact or '—'} |")
if PAST:
    L += ["","## Already passed — kept for the next cycle","",
          "| Date | Campus | Action | Detail |","|---|---|---|---|"]
    for d,days,camp,act,det,url,contact in PAST:
        L.append(f"| {d} | {camp} | {act} | {det} |")
open(os.path.join(OUT,"00-ACTION-CALENDAR.md"),"w").write("\n".join(L))

# ── 00 — Booth model ──────────────────────────────────────────────────────────
L=["# The Compliant Booth Model","",
   f"*One booth design that satisfies the strictest written rule found at any of the {len(CAMPUSES)} campuses "
   "in this packet — and at every campus researched so far.*","",
   "This is not a conservative reading. It is the literal intersection of four real policies:","",
   "- **Montana State (Catapalooza):** *\"Vendors are prohibited from seeking a monetary exchange for products, "
   "services, or donations\"* — but expressly permits *\"informational items, coupons, hand-outs, freebies, company "
   "contact information\"* and collecting contact info for post-event follow-up.",
   "- **Weber State (Block Party):** *\"Vendors may not have students sign any kind of contract for services on site.\"*",
   "- **Colorado State (LSC):** *\"No financial transactions (including requesting credit card information, Venmo or "
   "similar app info, etc) are permitted on the Plaza.\"*",
   "- **WSU (WAC 504-34-140):** distribution *\"by means of accosting, confronting, detaining, or waylaying "
   "individuals or by hawking is prohibited.\"*","",
   "These four are load-bearing regardless of which states you selected: they are the strictest rules "
   "found anywhere, so a booth built to them is compliant everywhere. Designed this way it removes the CARD Act pattern-match "
   "(*a tangible inducement offered to a student, on campus, to open a financial account*) that will otherwise "
   "alarm every dean of students who sees it.","",
   "---","","| # | Rule | Why |","|---|---|---|"]
for i,(rule,why) in enumerate(C.BOOTH_MODEL,1):
    L.append(f"| {i} | **{rule}** | {why} |")
L += ["","## Insurance requirements found","","| Campus | Requirement |","|---|---|"]
for camp,req,url in C.INSURANCE: L.append(f"| **{camp}** | {req} |")
open(os.path.join(OUT,"00-BOOTH-MODEL.md"),"w").write("\n".join(L))

# ── 00 — Compliance ───────────────────────────────────────────────────────────
L=[f"# Compliance Issue Map — the {ORG} credit + referral model","",
   "> **NOT LEGAL ADVICE.** A sourced issue map for licensed counsel to work from. "
   "Items marked **[ATTORNEY]** require a licensed practitioner in the relevant state.","",
   "## The headline finding",""]
L += ["> "+p.replace("\n"," ")+"\n>" for p in C.HEADLINE.split("\n\n")]
L += ["","---","","## Assumptions that did not survive checking","",
      "| Assumption | What the research found | So what |","|---|---|---|"]
for a,f_,s in C.PREMISE_CORRECTIONS:
    L.append(f"| {a} | {f_} | {s} |")
L += ["","---",""]
for iss in C.ISSUES:
    L += [f"## {iss['n']}. {iss['title']}","",f"**Severity: {iss['severity']}**","",iss["risk"],"",
          "### Citations","","| Citation | What it says | Source |","|---|---|---|"]
    for cite,what,url in iss["cites"]:
        L.append(f"| **{cite}** | {what} | {('<'+url+'>') if url else '—'} |")
    L += ["",f"**What this means for a campus table:** {iss['table']}","","---",""]
L += ["## Red flags, ranked","","| # | Risk | Detail | Severity |","|---|---|---|---|"]
for n_,t,d,s in C.REDFLAGS: L.append(f"| {n_} | **{t}** | {d} | {s} |")
L += ["","## Questions that require a licensed attorney","",
      "| Jurisdiction | Question |","|---|---|"]
for j,q in C.ATTORNEY_QUESTIONS: L.append(f"| **{j}** | {q} |")
open(os.path.join(OUT,"00-COMPLIANCE.md"),"w").write("\n".join(L))

# ── 00 — Route & budget ───────────────────────────────────────────────────────
L=[f"# Recommended Route & Budget — {TERM}","",f"*{summary()}.*","","## Route",""]
if not ROUTE:
    L.append("*No route authored for this run. The agent writes `route` into config.json — "
             "see reference/build-and-deliver.md.*")
for leg,summ,stops in ROUTE:
    L += [f"### {leg}","",f"*{summ}*",""]
    for s in stops: L.append(f"- {s}")
    L.append("")
L += ["## Budget — published costs only","","| Line item | Cost | Notes |","|---|---|---|"]
for n_,c_,note in BUDGET: L.append(f"| **{n_}** | {c_} | {note} |")
L += ["","*Costs are what each institution publishes. Where a fee is unpublished, it is marked as such — "
      "assume for-profit rates and no discount.*"]
open(os.path.join(OUT,"00-ROUTE-AND-BUDGET.md"),"w").write("\n".join(L))

# ── 00 — Index ────────────────────────────────────────────────────────────────
L=[f"# {ORG} Campus Tour — {TERM}","",f"*{summary()}.*","",
   "## Start here","",
   "1. **[Action Calendar](00-ACTION-CALENDAR.md)** — every date-certain deadline, soonest first",
   "2. **[Compliance Issue Map](00-COMPLIANCE.md)** — read the headline finding before booking anything",
   "3. **[The Compliant Booth Model](00-BOOTH-MODEL.md)** — one booth design that works everywhere",
   "4. **[Route & Budget](00-ROUTE-AND-BUDGET.md)** — sequencing and published costs","",
   "## Campus briefs",""]
for st in STATE_ORDER:
    cl=by_state.get(st,[])
    if not cl: continue
    d=f"{STATE_ORDER.index(st)+1:02d}-{slug(st)}"
    L += [f"### {st}","","| Campus | Access | Tier | Classes begin |","|---|---|---|---|"]
    for c in sorted(cl,key=lambda x:-x["access"]):
        L.append(f"| [{c['name']}]({d}/{slug(c['name'])}.md) | {STARS[c['access']]} | {c['tier']} | {c['start']} |")
    L.append("")
L += ["---","","**Verification standard:** every named person, email, phone number, date and policy quotation in "
      "these briefs was confirmed on a live university page. Where a fact could not be confirmed it is marked "
      "**UNVERIFIED** with the URL to check — those are research gaps, not findings of absence."]
open(os.path.join(OUT,"README.md"),"w").write("\n".join(L))

print(f"MD    {n} campus briefs + 5 index docs → {OUT}/")
