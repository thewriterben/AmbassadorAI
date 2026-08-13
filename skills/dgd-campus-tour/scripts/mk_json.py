import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dataset import (CAMPUSES, DEADLINES, PAST, ROUTE, BUDGET, TODAY, TERM, ORG,
                     STATE_ORDER, CFG, C, summary)

OUT = os.environ.get("DGD_OUT","out"); os.makedirs(OUT, exist_ok=True)

def derive_top5():
    """Prefer the agent's own headline items from config.json. If none were written,
    derive five from the data so the report always opens with something real."""
    if CFG.get("top5"):
        return [tuple(t) for t in CFG["top5"]]
    out=[]
    hot=[d for d in DEADLINES if d[1]<=21 and "⚠" in d[3]]
    if hot:
        d=hot[0]
        out.append((f"{d[2]} — {d[3].replace('⚠','').strip()} in {d[1]} days ({d[0]}).", d[4]))
    open_c=[c for c in CAMPUSES if c["access"]>=4]
    if open_c:
        out.append((f"{len(open_c)} of {len(CAMPUSES)} campuses have a documented route for an outside organization.",
          "Ranked 4/5 or better: " + "; ".join(f"{c['name']} ({c['fair_cost'].split('.')[0][:60] or 'see brief'})"
          for c in open_c[:6]) + ". Everything else needs sponsorship, written approval, or is closed outright."))
    closed=[c for c in CAMPUSES if c["access"]<=1]
    if closed:
        out.append((f"{len(closed)} campus{'es' if len(closed)!=1 else ''} should come off the list entirely.",
          "; ".join(f"{c['name']}: {c['play'].split('.')[0]}" for c in closed[:4]) + "."))
    strip=lambda t:(t or "").replace("⚠⚠","").replace("⚠","").strip()
    fac=[(c,f) for c in CAMPUSES for f in c["faculty"] if f[3] and "⚠" in (f[1] or "")]
    if fac:
        c,f=fac[0]
        out.append((f"The highest-leverage single contact is {strip(f[0])} at {c['name']}.",
                    f"{strip(f[1])} Contact: {f[3]}"))
    out.append(("Campus policy, not statute, is what will actually stop the program.",
      "Every public university researched requires written approval, departmental or student-organization "
      "sponsorship, or both, before an outside entity may solicit — and several foreclose the "
      "club-sponsorship workaround by name with anti-fronting rules. Read the compliance section before "
      "any money is committed."))
    return out[:5]

TOP5 = derive_top5()

by={}
for c in CAMPUSES: by.setdefault(c["state"],[]).append(c)
states=[(s, sorted(by[s], key=lambda x:-x["access"])) for s in STATE_ORDER if s in by]

out={
 "n":len(CAMPUSES),"today":TODAY,"headline":C.HEADLINE,"top5":[list(t) for t in TOP5],
 "term":TERM,"org":ORG,"summary":summary(),"states_line":" · ".join(STATE_ORDER),
 "deadlines":[list(x) for x in DEADLINES],
 "premises":[list(x) for x in C.PREMISE_CORRECTIONS],
 "issues":[{"n":i["n"],"title":i["title"],"severity":i["severity"],"risk":i["risk"],
            "table":i["table"],"cites":[list(c) for c in i["cites"]]} for i in C.ISSUES],
 "redflags":[list(x) for x in C.REDFLAGS],
 "attorney":[list(x) for x in C.ATTORNEY_QUESTIONS],
 "booth":[list(x) for x in C.BOOTH_MODEL],
 "insurance":[list(x) for x in C.INSURANCE],
 "route":[list(x) for x in ROUTE],
 "budget":[list(x) for x in BUDGET],
 "states":[[s,[{k:(list(map(list,v)) if k in ("clubs","faculty","courses","events") else v)
                for k,v in c.items()} for c in cl]] for s,cl in states],
 "gaps":[[c["state"],c["name"],g] for c in CAMPUSES for g in c["gaps"]],
}
json.dump(out,open(os.path.join(OUT,"_docx_data.json"),"w",encoding="utf-8"))
print(f"JSON  {len(json.dumps(out))//1024} KB payload for the report")
