import xlsxwriter, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dataset import (CAMPUSES, DEADLINES, PAST, ACCESS_LABEL, BUDGET, ROUTE, TODAY,
                     TERM, ORG, STATE_ORDER, C, summary)

OUT = os.environ.get("DGD_OUT", "out"); os.makedirs(OUT, exist_ok=True)
SLUG = os.environ.get("DGD_SLUG", "Campus-Tour")
wb = xlsxwriter.Workbook(os.path.join(OUT, f"{SLUG}-Master-Workbook.xlsx"))

NAVY="#0B1F3A"; GOLD="#C8A34A"; RED="#B3261E"; AMBER="#8A6100"; GREEN="#1B5E20"; LGREY="#F4F5F7"
title = wb.add_format({"bold":True,"font_size":16,"font_color":NAVY})
sub   = wb.add_format({"font_size":10,"font_color":"#555555","italic":True})
hdr   = wb.add_format({"bold":True,"bg_color":NAVY,"font_color":"white","border":1,
                       "text_wrap":True,"valign":"top","align":"left"})
cell  = wb.add_format({"border":1,"text_wrap":True,"valign":"top","font_size":9})
cellb = wb.add_format({"border":1,"text_wrap":True,"valign":"top","font_size":9,"bold":True})
cellr = wb.add_format({"border":1,"text_wrap":True,"valign":"top","font_size":9,"font_color":RED,"bold":True})
cella = wb.add_format({"border":1,"text_wrap":True,"valign":"top","font_size":9,"font_color":AMBER})
cellg = wb.add_format({"border":1,"text_wrap":True,"valign":"top","font_size":9,"font_color":GREEN,"bold":True})
link  = wb.add_format({"border":1,"text_wrap":True,"valign":"top","font_size":8,"font_color":"#1155CC","underline":1})
band  = wb.add_format({"border":1,"text_wrap":True,"valign":"top","font_size":9,"bg_color":LGREY})
big   = wb.add_format({"text_wrap":True,"valign":"top","font_size":10})

def sheet(name, headers, widths, freeze=(1,0)):
    ws = wb.add_worksheet(name)
    ws.freeze_panes(*freeze)
    for i,(h,w) in enumerate(zip(headers,widths)):
        ws.set_column(i,i,w); ws.write(0,i,h,hdr)
    ws.set_row(0,30)
    return ws

def acc_fmt(a): return cellg if a>=4 else (cella if a==3 else cellr)

# ── 1. READ ME ────────────────────────────────────────────────────────────────
ws = wb.add_worksheet("READ ME FIRST")
ws.set_column(0,0,120); ws.hide_gridlines(2)
r=0
ws.write(r,0,f"{ORG} Campus Tour — {TERM} Master Workbook",title); r+=2
ws.write(r,0,f"{summary()}. Every campus fact traces to a live university URL. Blanks and 'UNVERIFIED' "
             "mean not published — they are research gaps, not findings of absence.",sub); r+=2
ws.write(r,0,"THE HEADLINE FINDING",cellb); r+=1
for para in C.HEADLINE.split("\n\n"):
    ws.write(r,0,para.replace("\n"," "),big); ws.set_row(r,None); r+=2
ws.write(r,0,"HOW TO USE THIS WORKBOOK",cellb); r+=1
for t in ["Deadline Calendar — start here. Four registrations and three phone calls this week decide most of the fall.",
          "Campus Master — one row per campus, sortable by state, access rating, and term start.",
          "Access & Policy — the written rule at each campus, quoted, with the URL.",
          "Clubs / Faculty / Courses / Events — the people and programs, verified-only.",
          "Compliance — the legal issue map, red flags, and the questions that need an attorney.",
          "Booth Model — the single compliant booth design derived from the strictest rules in the dataset.",
          "Budget, Route, Gaps — money, sequencing, and what still has to be phoned in."]:
    ws.write(r,0,"• "+t,big); r+=1
r+=1
ws.write(r,0,"NOT LEGAL ADVICE. The compliance material is a sourced issue map for licensed counsel to work from.",cellr)

# ── 2. DEADLINE CALENDAR ──────────────────────────────────────────────────────
ws = sheet("Deadline Calendar",["Date","Days out","Campus","Action","Detail","Contact","URL"],
           [14,9,22,44,60,30,42])
for i,(d,days,camp,act,det,url,contact) in enumerate(DEADLINES,1):
    f = cellr if days<=20 and ("⚠" in act) else (cella if days<=45 else cell)
    ws.write(i,0,d,f); ws.write(i,1,days,f); ws.write(i,2,camp,f)
    ws.write(i,3,act,f); ws.write(i,4,det,cell); ws.write(i,5,contact,cell)
    ws.write_url(i,6,url,link,url) if url else ws.write(i,6,"",cell)
r = len(DEADLINES)+1
if PAST:
    ws.write(r+1,0,"ALREADY PASSED — kept for next cycle",hdr); r+=2
    for d,days,camp,act,det,url,contact in PAST:
        ws.write(r,0,d,band); ws.write(r,1,days,band); ws.write(r,2,camp,band)
        ws.write(r,3,act,band); ws.write(r,4,det,band); ws.write(r,5,contact,band); r+=1
ws.autofilter(0,0,len(DEADLINES),6)

# ── 3. CAMPUS MASTER ──────────────────────────────────────────────────────────
ws = sheet("Campus Master",["State","Campus","City","Type","Tier","Access","Access rating",
                            "Classes begin","Add/drop","Fall break","Thanksgiving","Last class","Finals",
                            "Calendar status","Calendar URL"],
           [11,32,20,26,26,32,7,26,26,26,26,26,26,30,44])
for i,c in enumerate(CAMPUSES,1):
    f=acc_fmt(c["access"])
    row=[c["state"],c["name"],c["city"],c["type"],c["tier"],ACCESS_LABEL[c["access"]],c["access"],
         c["start"],c["adddrop"],c["fallbreak"],c["thanksgiving"],c["lastclass"],c["finals"],c["cal_status"]]
    for j,v in enumerate(row): ws.write(i,j,v, f if j in (5,6) else cell)
    ws.write_url(i,14,c["cal_url"],link,c["cal_url"])
ws.autofilter(0,0,len(CAMPUSES),14)

# ── 4. ACCESS & POLICY ────────────────────────────────────────────────────────
ws = sheet("Access & Policy",["State","Campus","Access rating","Fair / event","Fair date",
                              "Outside orgs?","Cost","Deadline","Sponsor required?","Policy name",
                              "Key restriction (quoted)","Policy URL","Fair URL"],
           [11,32,8,34,40,40,34,40,34,40,90,40,40])
for i,c in enumerate(CAMPUSES,1):
    f=acc_fmt(c["access"])
    ws.write(i,0,c["state"],cell); ws.write(i,1,c["name"],cellb); ws.write(i,2,c["access"],f)
    ws.write(i,3,c["fair"],cell); ws.write(i,4,c["fair_date"], cellr if "⚠" in c["fair_date"] else cell)
    ws.write(i,5,c["fair_outside"], cellr if c["fair_outside"].strip().startswith(("NO","⚠ NO")) else cell)
    ws.write(i,6,c["fair_cost"],cell); ws.write(i,7,c["fair_deadline"], cellr if "⚠" in c["fair_deadline"] else cell)
    ws.write(i,8,c["sponsor_required"],cell); ws.write(i,9,c["policy"],cell)
    ws.write(i,10,c["policy_key"],band)
    ws.write_url(i,11,c["policy_url"],link,c["policy_url"])
    ws.write_url(i,12,c["fair_url"],link,c["fair_url"]) if c["fair_url"] else ws.write(i,12,"",cell)
ws.autofilter(0,0,len(CAMPUSES),12)

# ── 5. CLUBS ──────────────────────────────────────────────────────────────────
ws = sheet("Clubs",["State","Campus","Club","Notes / status","URL"],[11,30,42,90,44])
r=1
for c in CAMPUSES:
    for club in c["clubs"]:
        nm,note,url = (list(club)+["",""])[:3]
        f = cellg if ("blockchain" in nm.lower() or "crypto" in nm.lower()) and "NO " not in nm else cell
        ws.write(r,0,c["state"],cell); ws.write(r,1,c["name"],cell); ws.write(r,2,nm,f); ws.write(r,3,note,cell)
        ws.write_url(r,4,url,link,url) if url else ws.write(r,4,"",cell)
        r+=1
ws.autofilter(0,0,r-1,4)

# ── 6. FACULTY & STAFF ────────────────────────────────────────────────────────
ws = sheet("Faculty & Staff",["State","Campus","Name / office","Title / notes","Dept","Contact","Source URL"],
           [11,30,32,80,28,44,44])
r=1
for c in CAMPUSES:
    for f5 in c["faculty"]:
        nm,ti,dp,ct,url = (list(f5)+["","","","",""])[:5]
        f = cellg if ct.strip() else cell
        ws.write(r,0,c["state"],cell); ws.write(r,1,c["name"],cell); ws.write(r,2,nm,cellb)
        ws.write(r,3,ti,cell); ws.write(r,4,dp,cell); ws.write(r,5,ct,f)
        ws.write_url(r,6,url,link,url) if url else ws.write(r,6,"",cell)
        r+=1
ws.autofilter(0,0,r-1,6)

# ── 7. COURSES ────────────────────────────────────────────────────────────────
ws = sheet("Courses",["State","Campus","Code","Title / description","URL"],[11,30,18,110,44])
r=1
for c in CAMPUSES:
    for co in c["courses"]:
        cd,ti,url = (list(co)+["","",""])[:3]
        f = cellg if "CONFIRMED OFFERED FALL 2026" in ti else cell
        ws.write(r,0,c["state"],cell); ws.write(r,1,c["name"],cell); ws.write(r,2,cd,cellb); ws.write(r,3,ti,f)
        ws.write_url(r,4,url,link,url) if url else ws.write(r,4,"",cell)
        r+=1
ws.autofilter(0,0,r-1,4)

# ── 8. EVENTS ─────────────────────────────────────────────────────────────────
ws = sheet("Events",["State","Campus","Event","Detail","URL"],[11,30,44,100,44])
r=1
for c in CAMPUSES:
    for e in c["events"]:
        nm,det,url = (list(e)+["","",""])[:3]
        f = cellr if "⚠" in det or "⚠" in nm else cell
        ws.write(r,0,c["state"],cell); ws.write(r,1,c["name"],cell); ws.write(r,2,nm,cellb); ws.write(r,3,det,f)
        ws.write_url(r,4,url,link,url) if url else ws.write(r,4,"",cell)
        r+=1
ws.autofilter(0,0,r-1,4)

# ── 9. RECOMMENDED PLAY ───────────────────────────────────────────────────────
ws = sheet("Recommended Play",["State","Campus","Access","Recommended approach"],[11,30,10,150])
for i,c in enumerate(CAMPUSES,1):
    ws.write(i,0,c["state"],cell); ws.write(i,1,c["name"],cellb)
    ws.write(i,2,c["access"],acc_fmt(c["access"])); ws.write(i,3,c["play"],band)
ws.autofilter(0,0,len(CAMPUSES),3)

# ── 10. BOOTH MODEL ───────────────────────────────────────────────────────────
ws = sheet("Booth Model",["#","Rule","Why — the campus policy or statute behind it"],[5,52,120])
for i,(rule,why) in enumerate(C.BOOTH_MODEL,1):
    ws.write(i,0,i,cell); ws.write(i,1,rule,cellb); ws.write(i,2,why,band)
r=len(C.BOOTH_MODEL)+2
ws.write(r,1,"INSURANCE REQUIREMENTS FOUND",hdr); r+=1
for camp,req,url in C.INSURANCE:
    ws.write(r,1,camp,cellb); ws.write(r,2,req,cell); r+=1

# ── 11. COMPLIANCE ────────────────────────────────────────────────────────────
ws = sheet("Compliance",["#","Issue","Severity","The risk","What this means for a campus table"],
           [5,44,40,150,110])
for i,iss in enumerate(C.ISSUES,1):
    f = cellr if "HIGHEST" in iss["severity"] or "MOST LIKELY" in iss["severity"] else cell
    ws.write(i,0,iss["n"],cell); ws.write(i,1,iss["title"],cellb); ws.write(i,2,iss["severity"],f)
    ws.write(i,3,iss["risk"],band); ws.write(i,4,iss["table"],cell)

ws = sheet("Compliance Citations",["Issue","Citation","What it says","URL"],[44,52,120,44])
r=1
for iss in C.ISSUES:
    for cite,what,url in iss["cites"]:
        f = cellr if "⚠" in what else cell
        ws.write(r,0,iss["title"],cell); ws.write(r,1,cite,cellb); ws.write(r,2,what,f)
        ws.write_url(r,3,url,link,url) if url else ws.write(r,3,"",cell)
        r+=1
ws.autofilter(0,0,r-1,3)

ws = sheet("Red Flags",["Rank","Risk","Detail","Severity"],[6,80,130,40])
for i,(n,t,d,s) in enumerate(C.REDFLAGS,1):
    f = cellr if i<=5 else cell
    ws.write(i,0,n,f); ws.write(i,1,t,cellb); ws.write(i,2,d,band); ws.write(i,3,s,f)

ws = sheet("Attorney Questions",["Jurisdiction","Question"],[26,150])
for i,(j,q) in enumerate(C.ATTORNEY_QUESTIONS,1):
    ws.write(i,0,j,cellb); ws.write(i,1,q,cell)

ws = sheet("Premise Corrections",["Assumption","What the research actually found","So what"],[46,120,90])
for i,(a,f_,s) in enumerate(C.PREMISE_CORRECTIONS,1):
    ws.write(i,0,a,cellb); ws.write(i,1,f_,cellr); ws.write(i,2,s,band)

# ── 12. BUDGET ────────────────────────────────────────────────────────────────
ws = sheet("Budget",["Line item","Cost","Notes"],[44,22,120])
for i,(n,c_,note) in enumerate(BUDGET,1):
    ws.write(i,0,n,cellb); ws.write(i,1,c_,cell); ws.write(i,2,note,cell)

# ── 13. ROUTE ─────────────────────────────────────────────────────────────────
ws = sheet("Route",["Leg","Summary","Stop"],[44,80,110])
r=1
for leg,summ,stops in ROUTE:
    for k,s in enumerate(stops):
        ws.write(r,0,leg if k==0 else "",cellb if k==0 else cell)
        ws.write(r,1,summ if k==0 else "",band if k==0 else cell)
        ws.write(r,2,s, cellr if "⚠" in s else cell); r+=1

# ── 14. GAPS ──────────────────────────────────────────────────────────────────
ws = sheet("Gaps to Close",["State","Campus","Open question"],[11,32,130])
r=1
for c in CAMPUSES:
    for g in c["gaps"]:
        ws.write(r,0,c["state"],cell); ws.write(r,1,c["name"],cell)
        ws.write(r,2,g, cellr if "⚠" in g else cell); r+=1
ws.autofilter(0,0,r-1,2)

wb.close()
print(f"XLSX  {summary()}, {len(DEADLINES)} action items")
