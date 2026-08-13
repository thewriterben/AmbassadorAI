import json, html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dataset import (CAMPUSES, DEADLINES, PAST, ACCESS_LABEL, ROUTE, BUDGET, TODAY,
                     TERM, ORG, STATE_ORDER, CFG, C, summary)

OUT = os.environ.get("DGD_OUT","out"); os.makedirs(OUT, exist_ok=True)
SLUG = os.environ.get("DGD_SLUG","Campus-Tour")

def e(s): return html.escape(str(s or ""))
def linkify(u): return f'<a href="{e(u)}" target="_blank" rel="noopener">{e(u[:70])}{"…" if len(u)>70 else ""}</a>' if u else "—"
def warn(s):
    s=e(s)
    return s.replace("⚠⚠",'<span class="w2">⚠⚠</span>').replace("⚠",'<span class="w">⚠</span>')

data=[]
for c in CAMPUSES:
    data.append({k:c.get(k) for k in
        ["state","name","city","type","tier","access","start","adddrop","fallbreak","thanksgiving",
         "lastclass","finals","cal_url","cal_status","fair","fair_date","fair_outside","fair_cost",
         "fair_deadline","fair_url","policy","policy_url","policy_key","sponsor_required","play","gaps",
         "clubs","faculty","courses","events"]})

DL=[{"date":d,"days":days,"campus":cp,"action":a,"detail":dt,"url":u,"contact":ct}
    for d,days,cp,a,dt,u,ct in DEADLINES]

CSS = """
*{box-sizing:border-box}
body{margin:0;font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
 background:#0d1117;color:#e6edf3}
a{color:#79b8ff;text-decoration:none}a:hover{text-decoration:underline}
header{background:linear-gradient(135deg,#0b1f3a,#132f56);padding:26px 30px;border-bottom:3px solid #c8a34a}
h1{margin:0;font-size:23px;letter-spacing:.2px}
.sub{color:#9fb0c4;font-size:13px;margin-top:5px}
nav{display:flex;gap:2px;background:#161b22;padding:0 20px;border-bottom:1px solid #30363d;
 position:sticky;top:0;z-index:50;overflow-x:auto}
nav button{background:none;border:0;color:#9fb0c4;padding:13px 15px;font-size:13.5px;cursor:pointer;
 border-bottom:3px solid transparent;white-space:nowrap;font-weight:500}
nav button:hover{color:#e6edf3}
nav button.on{color:#c8a34a;border-bottom-color:#c8a34a}
main{padding:22px 30px 90px;max-width:1500px}
section{display:none}section.on{display:block}
.bar{display:flex;gap:9px;flex-wrap:wrap;align-items:center;margin-bottom:16px;
 background:#161b22;padding:12px 14px;border-radius:9px;border:1px solid #30363d}
select,input{background:#0d1117;color:#e6edf3;border:1px solid #30363d;border-radius:6px;
 padding:7px 10px;font-size:13.5px}
input{min-width:230px}
.count{color:#9fb0c4;font-size:12.5px;margin-left:auto}
table{width:100%;border-collapse:collapse;font-size:13px}
th{background:#0b1f3a;text-align:left;padding:9px 10px;border:1px solid #30363d;
 position:sticky;top:47px;font-weight:600;cursor:pointer;user-select:none}
th:hover{background:#132f56}
td{padding:9px 10px;border:1px solid #21262d;vertical-align:top}
tbody tr:nth-child(even){background:#11161d}
tbody tr:hover{background:#1a2230}
.w{color:#f0a020;font-weight:700}.w2{color:#ff6b6b;font-weight:700}
.pill{display:inline-block;padding:2px 8px;border-radius:11px;font-size:11px;font-weight:700;white-space:nowrap}
.a5{background:#0f3d1e;color:#7ee787}.a4{background:#1a3a24;color:#56d364}
.a3{background:#3d3416;color:#e3b341}.a2{background:#4a2318;color:#ffa198}
.a1{background:#4a1519;color:#ff7b72}
.card{background:#161b22;border:1px solid #30363d;border-left:4px solid #c8a34a;border-radius:9px;
 padding:16px 18px;margin-bottom:14px}
.card h3{margin:0 0 4px;font-size:16.5px;color:#fff}
.card .meta{color:#8b949e;font-size:12.5px;margin-bottom:10px}
.play{background:#0f1720;border-left:3px solid #56d364;padding:11px 14px;border-radius:0 6px 6px 0;
 margin:10px 0;font-size:13.5px;line-height:1.6}
.kv{display:grid;grid-template-columns:170px 1fr;gap:5px 14px;font-size:13px;margin:10px 0}
.kv div:nth-child(odd){color:#8b949e;font-weight:600}
details{margin:7px 0;background:#0d1117;border:1px solid #21262d;border-radius:6px}
summary{padding:9px 13px;cursor:pointer;font-weight:600;font-size:13.5px;color:#c8a34a}
details>div{padding:0 13px 13px}
.hero{background:linear-gradient(135deg,#2a1215,#3d1a1f);border:1px solid #ff7b72;border-radius:11px;
 padding:20px 24px;margin-bottom:20px}
.hero h2{margin:0 0 10px;color:#ff9d95;font-size:18px}
.hero p{margin:0 0 11px;font-size:14px;line-height:1.65;color:#e6d5d3}
.hero p:last-child{margin-bottom:0}
.note{background:#0f1720;border:1px solid #30363d;border-radius:9px;padding:15px 18px;margin-bottom:16px;font-size:13.5px}
.d-hot td{background:#2a1215}.d-soon td{background:#241d10}
h2.sec{font-size:17px;color:#c8a34a;margin:26px 0 11px;border-bottom:1px solid #30363d;padding-bottom:6px}
.leg{background:#161b22;border:1px solid #30363d;border-radius:9px;padding:15px 18px;margin-bottom:12px}
.leg h3{margin:0 0 3px;font-size:15px;color:#c8a34a}
.leg .s{color:#8b949e;font-size:12.5px;font-style:italic;margin-bottom:9px}
.leg ul{margin:0;padding-left:19px;font-size:13.5px}.leg li{margin:4px 0}
.tiny{font-size:11.5px;color:#8b949e}
footer{padding:22px 30px;border-top:1px solid #30363d;color:#8b949e;font-size:12px}
"""

JS = """
const D=DATA, DL=DEADLINES;
function tab(id,btn){document.querySelectorAll('section').forEach(s=>s.classList.remove('on'));
 document.querySelectorAll('nav button').forEach(b=>b.classList.remove('on'));
 document.getElementById(id).classList.add('on'); btn.classList.add('on'); window.scrollTo(0,0);}
function pill(a){return '<span class="pill a'+a+'">'+a+'/5</span>';}
function W(s){s=(s||'');return s.replace(/⚠⚠/g,'<span class="w2">⚠⚠</span>').replace(/⚠/g,'<span class="w">⚠</span>');}
function esc(s){const d=document.createElement('div');d.textContent=s||'';return d.innerHTML;}

function renderCampuses(){
 const st=document.getElementById('fState').value, ac=document.getElementById('fAcc').value,
       q=document.getElementById('fQ').value.toLowerCase();
 const rows=D.filter(c=>(!st||c.state===st)&&(!ac||c.access>=+ac)&&
   (!q||JSON.stringify(c).toLowerCase().includes(q)));
 document.getElementById('cCount').textContent=rows.length+' of '+D.length+' campuses';
 document.getElementById('cards').innerHTML=rows.map(c=>{
  const tbl=(a,cols)=>!a||!a.length?'<p class="tiny">None recorded.</p>':
   '<table><tbody>'+a.map(r=>'<tr>'+cols.map((ci,i)=>'<td'+(i===0?' style="width:26%"':'')+'>'+
    (typeof r[ci]==='string'&&r[ci].startsWith('http')?'<a href="'+r[ci]+'" target="_blank">link</a>':W(esc(r[ci]))||'—')+
    '</td>').join('')+'</tr>').join('')+'</tbody></table>';
  return `<div class="card">
   <h3>${esc(c.name)} ${pill(c.access)}</h3>
   <div class="meta">${esc(c.city)} · ${esc(c.type)} · ${esc(c.tier)}</div>
   <div class="play"><b>RECOMMENDED PLAY</b><br>${W(esc(c.play))}</div>
   <div class="kv">
    <div>Classes begin</div><div>${W(esc(c.start))}</div>
    <div>Add/drop</div><div>${esc(c.adddrop)||'—'}</div>
    <div>Thanksgiving</div><div>${esc(c.thanksgiving)||'—'}</div>
    <div>Last class / finals</div><div>${esc(c.lastclass)||'—'} / ${esc(c.finals)||'—'}</div>
    <div>Fair</div><div>${esc(c.fair)}</div>
    <div>Fair date</div><div>${W(esc(c.fair_date))}</div>
    <div>Outside orgs?</div><div>${W(esc(c.fair_outside))||'UNVERIFIED'}</div>
    <div>Cost</div><div>${esc(c.fair_cost)||'Not published'}</div>
    <div>Deadline</div><div>${W(esc(c.fair_deadline))||'Not published'}</div>
   </div>
   <details><summary>Solicitation policy — ${esc(c.policy)}</summary><div>
     <p>${W(esc(c.policy_key))}</p>
     <p><b>Sponsorship:</b> ${esc(c.sponsor_required)}</p>
     <p><a href="${esc(c.policy_url)}" target="_blank">${esc(c.policy_url)}</a></p></div></details>
   <details><summary>Clubs (${c.clubs.length})</summary><div>${tbl(c.clubs,[0,1,2])}</div></details>
   <details><summary>Faculty &amp; staff (${c.faculty.length})</summary><div>${tbl(c.faculty,[0,1,3,4])}</div></details>
   <details><summary>Courses (${c.courses.length})</summary><div>${tbl(c.courses,[0,1,2])}</div></details>
   <details><summary>Events (${c.events.length})</summary><div>${tbl(c.events,[0,1,2])}</div></details>
   <details><summary>Open questions (${c.gaps.length})</summary><div><ul>${
     c.gaps.map(g=>'<li>'+W(esc(g))+'</li>').join('')}</ul></div></details>
  </div>`}).join('');
}
let sortCol=1,sortDir=1;
function renderDeadlines(){
 const q=document.getElementById('dQ').value.toLowerCase();
 let rows=DL.filter(d=>!q||JSON.stringify(d).toLowerCase().includes(q));
 const keys=['date','days','campus','action','detail','contact'];
 rows.sort((a,b)=>{const k=keys[sortCol];let x=a[k],y=b[k];
  if(k==='days')return (x-y)*sortDir; return String(x).localeCompare(String(y))*sortDir;});
 document.getElementById('dCount').textContent=rows.length+' items';
 document.getElementById('dBody').innerHTML=rows.map(d=>{
  const cls=(d.days<=20&&d.action.includes('⚠'))?'d-hot':(d.days<=45?'d-soon':'');
  return `<tr class="${cls}"><td><b>${esc(d.date)}</b></td><td>${d.days}</td><td>${esc(d.campus)}</td>
   <td>${W(esc(d.action))}</td><td>${W(esc(d.detail))}</td><td>${esc(d.contact)||'—'}</td>
   <td>${d.url?'<a href="'+d.url+'" target="_blank">link</a>':'—'}</td></tr>`}).join('');
}
function sortBy(i){if(sortCol===i)sortDir=-sortDir;else{sortCol=i;sortDir=1;}renderDeadlines();}
window.addEventListener('DOMContentLoaded',()=>{
 const sel=document.getElementById('fState');
 [...new Set(D.map(c=>c.state))].forEach(s=>{const o=document.createElement('option');o.value=o.textContent=s;sel.appendChild(o);});
 ['fState','fAcc'].forEach(id=>document.getElementById(id).addEventListener('change',renderCampuses));
 document.getElementById('fQ').addEventListener('input',renderCampuses);
 document.getElementById('dQ').addEventListener('input',renderDeadlines);
 renderCampuses(); renderDeadlines();
});
"""

def section_deadlines():
    """The hero is DERIVED, not written — it surfaces whatever is actually urgent
    in the selected states, so it stays true when the states or the date change."""
    hot = [d for d in DEADLINES if d[1] <= 21 and "⚠" in d[3]][:6]
    if hot:
        n = len(hot)
        soonest = hot[0][1]
        head = (f"⚠ {n} dated action{'s' if n!=1 else ''} inside three weeks"
                + (" — one is in the next 72 hours" if soonest <= 3 else ""))
        rows = "".join(
            f"<p><b>{e(d[0])} ({d[1]} day{'s' if d[1]!=1 else ''}) — {e(d[2])}.</b> "
            f"{warn(d[3])}. {warn(d[4])}{' Contact: '+e(d[6]) if d[6] else ''}</p>"
            for d in hot)
    else:
        head = "No dated action items inside three weeks"
        rows = ("<p>Nothing in the selected states carries a registration deadline in the next "
                "21 days. That usually means either the fairs have passed for this term or the "
                "campuses have not published their dates yet — check the Gaps tab, which lists "
                "every unpublished date with the URL to watch.</p>")
    past = ""
    if PAST:
        past = ("<p class=\"tiny\" style=\"color:#e6d5d3\"><b>"
                + str(len(PAST)) + " item" + ("s" if len(PAST)!=1 else "")
                + " already passed</b> and were moved out of the live list — they are kept in the "
                "workbook and the markdown calendar so next cycle's packet inherits the pattern.</p>")
    return f"""<section id="deadlines" class="on">
<div class="hero"><h2>{head}</h2>{rows}{past}
<p class="tiny" style="color:#e6d5d3"><b>Read the Compliance tab before booking anything.</b>
Campus policy — not statute — is what usually stops a program like this, and the rules that matter
most are the ones about what you may do <i>at the table</i>.</p></div>
<div class="bar"><input id="dQ" placeholder="Search deadlines…">
<span class="count" id="dCount"></span></div>
<table><thead><tr>
<th onclick="sortBy(0)">Date</th><th onclick="sortBy(1)">Days out</th><th onclick="sortBy(2)">Campus</th>
<th onclick="sortBy(3)">Action</th><th onclick="sortBy(4)">Detail</th><th onclick="sortBy(5)">Contact</th><th>Link</th>
</tr></thead><tbody id="dBody"></tbody></table></section>"""

def section_campuses():
    return """<section id="campuses">
<div class="bar">
<select id="fState"><option value="">All states</option></select>
<select id="fAcc"><option value="">Any access level</option>
<option value="5">5 — Open to outside orgs</option><option value="4">4+ — Workable or better</option>
<option value="3">3+ — Gated or better</option></select>
<input id="fQ" placeholder="Search campuses, clubs, faculty, policy…">
<span class="count" id="cCount"></span></div>
<div id="cards"></div></section>"""

def section_compliance():
    h="".join(f"<p>{warn(p).replace(chr(10),' ')}</p>" for p in C.HEADLINE.split("\n\n"))
    s=[f'<section id="compliance"><div class="hero"><h2>The headline finding</h2>{h}</div>']
    s.append('<h2 class="sec">Assumptions that did not survive checking</h2><table><thead><tr>'
             '<th>Assumption</th><th>What the research found</th><th>So what</th></tr></thead><tbody>')
    for a,f_,so in C.PREMISE_CORRECTIONS:
        s.append(f"<tr><td><b>{e(a)}</b></td><td>{warn(f_)}</td><td>{warn(so)}</td></tr>")
    s.append("</tbody></table>")
    s.append('<h2 class="sec">Issue map</h2>')
    for iss in C.ISSUES:
        cites="".join(f"<tr><td style='width:24%'><b>{e(c1)}</b></td><td>{warn(c2)}</td>"
                      f"<td style='width:12%'>{linkify(c3)}</td></tr>" for c1,c2,c3 in iss["cites"])
        s.append(f"""<div class="card"><h3>{iss['n']}. {e(iss['title'])}</h3>
<div class="meta">Severity: {warn(iss['severity'])}</div><p>{warn(iss['risk'])}</p>
<div class="play"><b>What this means for a campus table:</b><br>{warn(iss['table'])}</div>
<details><summary>Citations ({len(iss['cites'])})</summary><div><table><tbody>{cites}</tbody></table></div></details></div>""")
    s.append('<h2 class="sec">Red flags, ranked</h2><table><thead><tr><th>#</th><th>Risk</th>'
             '<th>Detail</th><th>Severity</th></tr></thead><tbody>')
    for n,t,d,sv in C.REDFLAGS:
        s.append(f"<tr><td>{n}</td><td><b>{e(t)}</b></td><td>{warn(d)}</td><td>{warn(sv)}</td></tr>")
    s.append("</tbody></table>")
    s.append('<h2 class="sec">Questions that require a licensed attorney</h2><table><thead><tr>'
             '<th style="width:18%">Jurisdiction</th><th>Question</th></tr></thead><tbody>')
    for j,q in C.ATTORNEY_QUESTIONS:
        s.append(f"<tr><td><b>{e(j)}</b></td><td>{warn(q)}</td></tr>")
    s.append("</tbody></table></section>")
    return "".join(s)

def section_booth():
    rows="".join(f"<tr><td>{i}</td><td><b>{e(r)}</b></td><td>{warn(w)}</td></tr>"
                 for i,(r,w) in enumerate(C.BOOTH_MODEL,1))
    ins="".join(f"<tr><td><b>{e(c)}</b></td><td>{e(r)}</td><td>{linkify(u)}</td></tr>" for c,r,u in C.INSURANCE)
    return f"""<section id="booth">
<div class="note"><b>One booth design that satisfies the strictest written rule found at any campus researched so far.</b>
This is not a conservative reading — it is the literal intersection of four real policies:
<b>Montana State</b> ("Vendors are prohibited from seeking a monetary exchange… " but expressly permits
handouts and collecting contact info for post-event follow-up), <b>Weber State</b> ("Vendors may not have
students sign any kind of contract for services on site"), <b>Colorado State</b> ("No financial transactions
including requesting credit card information, Venmo or similar app info"), and <b>WSU</b> (distribution "by
means of accosting, confronting, detaining, or waylaying individuals or by hawking is prohibited").
<br><br>Designed this way the same booth works everywhere — and it removes the CARD Act pattern-match
(<i>a tangible inducement offered to a student, on campus, to open a financial account</i>) that will otherwise
alarm every dean of students who sees it.</div>
<table><thead><tr><th style="width:4%">#</th><th style="width:30%">Rule</th><th>Why</th></tr></thead>
<tbody>{rows}</tbody></table>
<h2 class="sec">Insurance requirements found</h2>
<table><thead><tr><th style="width:20%">Campus</th><th>Requirement</th><th style="width:16%">Source</th></tr></thead>
<tbody>{ins}</tbody></table></section>"""

def section_route():
    legs="".join(f"""<div class="leg"><h3>{e(l)}</h3><div class="s">{e(s)}</div>
<ul>{''.join('<li>'+warn(x)+'</li>' for x in st)}</ul></div>""" for l,s,st in ROUTE)
    bud="".join(f"<tr><td><b>{e(n)}</b></td><td>{e(c)}</td><td>{warn(x)}</td></tr>" for n,c,x in BUDGET)
    return f"""<section id="route">{legs}
<h2 class="sec">Budget — published costs only</h2>
<table><thead><tr><th style="width:26%">Line item</th><th style="width:12%">Cost</th><th>Notes</th></tr></thead>
<tbody>{bud}</tbody></table>
<p class="tiny">Costs are what each institution publishes. Where a fee is unpublished it is marked as such —
assume for-profit rates and no discount.</p></section>"""

def section_gaps():
    rows="".join(f"<tr><td>{e(c['state'])}</td><td>{e(c['name'])}</td><td>{warn(g)}</td></tr>"
                 for c in CAMPUSES for g in c["gaps"])
    return f"""<section id="gaps">
<div class="note">Every item below is something that could <b>not</b> be confirmed on a live university page.
These are research gaps, not findings of absence. Most are one phone call each.</div>
<table><thead><tr><th style="width:10%">State</th><th style="width:22%">Campus</th>
<th>Open question</th></tr></thead><tbody>{rows}</tbody></table></section>"""

HTML=f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{ORG} Campus Tour — {TERM}</title><style>{CSS}</style></head><body>
<header><h1>{e(ORG)} — Campus Tour, {e(TERM)}</h1>
<div class="sub">{summary()} · {e(" · ".join(STATE_ORDER))} · every fact traced to a live university URL</div></header>
<nav>
<button class="on" onclick="tab('deadlines',this)">⚠ Action Calendar</button>
<button onclick="tab('campuses',this)">Campuses</button>
<button onclick="tab('compliance',this)">Compliance</button>
<button onclick="tab('booth',this)">Booth Model</button>
<button onclick="tab('route',this)">Route &amp; Budget</button>
<button onclick="tab('gaps',this)">Gaps to Close</button>
</nav><main>
{section_deadlines()}{section_campuses()}{section_compliance()}{section_booth()}{section_route()}{section_gaps()}
</main>
<footer><b>Verification standard:</b> every named person, email, phone number, date and policy quotation was
confirmed on a live university page. Fields marked UNVERIFIED could not be confirmed — the URL to check is
given. &nbsp;·&nbsp; <b>Not legal advice.</b> The compliance material is a sourced issue map for licensed
counsel to work from.</footer>
<script>const DATA={json.dumps(data)};const DEADLINES={json.dumps(DL)};{JS}</script>
</body></html>"""

open(os.path.join(OUT, f"{SLUG}-Dashboard.html"),"w",encoding="utf-8").write(HTML)
print(f"HTML  {len(HTML)//1024} KB, {summary()}")
