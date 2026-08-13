const fs = require('fs');
const d = require('docx');
const {Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, Table, TableRow, TableCell,
       WidthType, ShadingType, BorderStyle, PageBreak, TableOfContents, Header, Footer, PageNumber,
       LevelFormat, convertInchesToTwip, PageOrientation} = d;

const OUT  = process.env.DGD_OUT  || 'out';
const SLUG = process.env.DGD_SLUG || 'Campus-Tour';
const DATA = JSON.parse(fs.readFileSync(require('path').join(OUT,'_docx_data.json'),'utf8'));
const NAVY="0B1F3A", GOLD="C8A34A", RED="B3261E", AMBER="8A6100", GREY="F4F5F7", DGREY="5A6472";

// US Letter portrait; content width 12240 - 2*1080 = 10080 dxa
const W = 10080;

const P = (t,o={}) => new Paragraph({ ...o, children: Array.isArray(t)?t:[new TextRun({text:String(t||""),...(o.run||{})})] });
const H1 = t => new Paragraph({text:t, heading:HeadingLevel.HEADING_1, spacing:{before:360,after:160}});
const H2 = t => new Paragraph({text:t, heading:HeadingLevel.HEADING_2, spacing:{before:280,after:120}});
const H3 = t => new Paragraph({text:t, heading:HeadingLevel.HEADING_3, spacing:{before:200,after:90}});
const BR = () => new Paragraph({children:[new PageBreak()]});
const SPACE = (n=1) => Array.from({length:n},()=>new Paragraph({text:"",spacing:{after:60}}));

function body(t,o={}){
  return new Paragraph({ spacing:{after:110, line:280}, ...o,
    children:[new TextRun({text:String(t||""), size:20, ...(o.run||{})})] });
}
function bullet(t,o={}){
  return new Paragraph({ numbering:{reference:"bul",level:0}, spacing:{after:60,line:270},
    children:[new TextRun({text:String(t||""), size:20, ...(o.run||{})})] });
}
function callout(label, txt, color){
  return new Table({
    columnWidths:[W], width:{size:W,type:WidthType.DXA},
    borders:{ top:{style:BorderStyle.SINGLE,size:2,color:color}, bottom:{style:BorderStyle.SINGLE,size:2,color:color},
              left:{style:BorderStyle.SINGLE,size:18,color:color}, right:{style:BorderStyle.SINGLE,size:2,color:color},
              insideHorizontal:{style:BorderStyle.NONE}, insideVertical:{style:BorderStyle.NONE}},
    rows:[ new TableRow({ children:[ new TableCell({
      width:{size:W,type:WidthType.DXA},
      shading:{type:ShadingType.CLEAR, fill:"FBFBFC"},
      margins:{top:150,bottom:150,left:190,right:150},
      children:[
        ...(label?[new Paragraph({spacing:{after:70},children:[new TextRun({text:label,bold:true,size:19,color:color})]})]:[]),
        ...String(txt).split("\n\n").map(p=>new Paragraph({spacing:{after:90,line:280},
          children:[new TextRun({text:p.replace(/\n/g," "),size:19})]}))
      ]})]})]});
}
function table(headers, rows, widths, opts={}){
  const cw = widths.map(f=>Math.round(W*f));
  cw[cw.length-1] += W - cw.reduce((a,b)=>a+b,0);
  const hdr = new TableRow({tableHeader:true, children: headers.map((h,i)=>new TableCell({
    width:{size:cw[i],type:WidthType.DXA}, shading:{type:ShadingType.CLEAR,fill:NAVY},
    margins:{top:80,bottom:80,left:100,right:100},
    children:[new Paragraph({children:[new TextRun({text:h,bold:true,color:"FFFFFF",size:17})]})]})) });
  const trs = rows.map((r,ri)=> new TableRow({children: r.map((c,i)=>new TableCell({
    width:{size:cw[i],type:WidthType.DXA},
    shading:{type:ShadingType.CLEAR, fill: ri%2 ? "FFFFFF" : GREY},
    margins:{top:70,bottom:70,left:100,right:100},
    children: String(c==null?"":c).split("\n").map(line=>new Paragraph({spacing:{after:20,line:250},
      children:[new TextRun({text:line, size:16,
        bold: (opts.boldCols||[]).includes(i),
        color: (opts.redRows&&opts.redRows(r)) ? RED : (i===0&&opts.firstColColor ? opts.firstColColor : "000000")})]}))
  }))}));
  const showHdr = headers.some(h=>String(h).trim().length>0);
  return new Table({ columnWidths:cw, width:{size:W,type:WidthType.DXA},
    borders:{ top:{style:BorderStyle.SINGLE,size:2,color:"BBBBBB"}, bottom:{style:BorderStyle.SINGLE,size:2,color:"BBBBBB"},
              left:{style:BorderStyle.SINGLE,size:2,color:"BBBBBB"}, right:{style:BorderStyle.SINGLE,size:2,color:"BBBBBB"},
              insideHorizontal:{style:BorderStyle.SINGLE,size:1,color:"DDDDDD"},
              insideVertical:{style:BorderStyle.SINGLE,size:1,color:"DDDDDD"}},
    rows: showHdr ? [hdr,...trs] : trs});
}
const STARS={5:"5/5",4:"4/5",3:"3/5",2:"2/5",1:"1/5"};

// ══ BUILD ════════════════════════════════════════════════════════════════════
const kids = [];

// Cover
kids.push(
  ...SPACE(6),
  new Paragraph({alignment:AlignmentType.CENTER, spacing:{after:60},
    children:[new TextRun({text:DATA.org.toUpperCase(), bold:true, size:56, color:NAVY, characterSpacing:60})]}),
  new Paragraph({alignment:AlignmentType.CENTER, spacing:{after:400},
    children:[new TextRun({text:"CAMPUS TOUR", bold:true, size:30, color:GOLD, characterSpacing:80})]}),
  new Paragraph({alignment:AlignmentType.CENTER, spacing:{after:120},
    children:[new TextRun({text:`${DATA.term} Information Packet`, size:32, color:NAVY})]}),
  new Paragraph({alignment:AlignmentType.CENTER, spacing:{after:600},
    children:[new TextRun({text:`${DATA.summary} · sorted by state and campus`, size:22, color:DGREY})]}),
  ...SPACE(4),
  new Paragraph({alignment:AlignmentType.CENTER,
    children:[new TextRun({text:"Compiled "+DATA.today, size:20, color:DGREY})]}),
  new Paragraph({alignment:AlignmentType.CENTER, spacing:{after:40},
    children:[new TextRun({text:DATA.states_line, size:18, color:DGREY, italics:true})]}),
  BR());

// TOC
kids.push(H1("Contents"),
  new TableOfContents("Contents",{hyperlink:true, headingStyleRange:"1-2"}), BR());

// 1. Executive summary
kids.push(H1("1. Executive summary"));
kids.push(callout("THE HEADLINE FINDING — READ BEFORE BOOKING ANYTHING", DATA.headline, RED));
kids.push(...SPACE(1));
kids.push(H2("What this packet contains"));
kids.push(body(`${DATA.summary}, researched against live university pages. `+
  `For each campus: the ${DATA.term} academic calendar, the involvement fair or tabling event and whether outside `+
  "organizations are admitted, the written solicitation policy quoted with its citation, relevant student clubs, "+
  `verified faculty and staff contacts, catalog courses touching blockchain and fintech, ${DATA.term} events, and a `+
  "recommended approach."));
kids.push(body("Verification standard: every named person, email address, phone number, date and policy quotation "+
  "in this packet was confirmed on a live university page. Where a fact could not be confirmed it is marked "+
  "UNVERIFIED with the URL to check. Those are research gaps, not findings of absence — and most are one phone call each.",
  {run:{italics:true}}));
kids.push(...SPACE(1));
kids.push(H2("The five things that matter most"));
DATA.top5.forEach((t,i)=>{
  kids.push(new Paragraph({spacing:{before:140,after:50},
    children:[new TextRun({text:`${i+1}. ${t[0]}`, bold:true, size:21, color:NAVY})]}));
  kids.push(body(t[1]));
});
kids.push(BR());

// 2. Action calendar
kids.push(H1("2. Action calendar"));
{
  const hot = DATA.deadlines.filter(d=>d[1]<=21 && String(d[3]).includes("⚠"));
  const txt = hot.length
    ? `${hot.length} dated action${hot.length!==1?"s":""} in the selected states fall inside three weeks. `+
      `The nearest is ${hot[0][2]} — ${String(hot[0][3]).replace(/⚠/g,"").trim()}, ${hot[0][1]} day`+
      `${hot[0][1]!==1?"s":""} out (${hot[0][0]}).\n\n`+
      hot.slice(0,5).map(d=>`${d[0]} — ${d[2]}: ${String(d[3]).replace(/⚠/g,"").trim()}.`).join(" ")
    : "Nothing in the selected states carries a registration deadline in the next 21 days. That usually means "+
      "the fairs have passed for this term, or the campuses have not published their dates yet — section 7 "+
      "lists every unpublished date with the URL to watch.";
  kids.push(callout(hot.length ? "DATED ACTIONS INSIDE THREE WEEKS" : "NO NEAR-TERM DEADLINES", txt, RED));
}
kids.push(...SPACE(1));
kids.push(table(["Date","Days","Campus","Action","Detail","Contact"],
  DATA.deadlines.map(x=>[x[0],String(x[1]),x[2],x[3],x[4],x[6]||"—"]),
  [.10,.05,.14,.24,.32,.15], {boldCols:[0], redRows:r=>Number(r[1])<=20 && r[3].includes("⚠")}));
kids.push(BR());

// 3. Compliance
kids.push(H1("3. Compliance and regulatory constraints"));
kids.push(callout("NOT LEGAL ADVICE — AND NOT OPTIONAL READING",
 "What follows is a sourced issue map for licensed counsel to work from, not legal advice. Items marked [ATTORNEY] "+
 "require a licensed practitioner in the relevant state. Several statutory citations could not be verified and are "+
 "flagged as such — do not cite those without checking.", AMBER));
kids.push(...SPACE(1));
kids.push(H2("3.1 Assumptions that did not survive checking"));
kids.push(body("Eleven working assumptions behind the brief turned out to be wrong. Several change the risk ranking materially."));
kids.push(table(["Assumption","What the research found","So what"],
  DATA.premises, [.20,.50,.30], {boldCols:[0]}));
kids.push(...SPACE(1));
kids.push(H2("3.2 Issue map"));
DATA.issues.forEach(iss=>{
  kids.push(H3(`${iss.n}. ${iss.title}`));
  kids.push(new Paragraph({spacing:{after:100},
    children:[new TextRun({text:"Severity: "+iss.severity, bold:true, size:19,
      color: /HIGHEST|MOST LIKELY|HIGH/.test(iss.severity)?RED:AMBER})]}));
  kids.push(body(iss.risk));
  kids.push(callout("What this means for a campus table", iss.table, NAVY));
  kids.push(...SPACE(1));
  kids.push(table(["Citation","What it says"], iss.cites.map(c=>[c[0]+(c[2]?"\n"+c[2]:""),c[1]]),
    [.30,.70], {boldCols:[0]}));
  kids.push(...SPACE(1));
});
kids.push(H2("3.3 Red flags, ranked"));
kids.push(table(["#","Risk","Detail","Severity"], DATA.redflags, [.04,.28,.48,.20],
  {boldCols:[1], redRows:r=>Number(r[0])<=5}));
kids.push(...SPACE(1));
kids.push(H2("3.4 Questions that require a licensed attorney"));
kids.push(table(["Jurisdiction","Question"], DATA.attorney, [.18,.82], {boldCols:[0]}));
kids.push(BR());

// 4. Booth model
kids.push(H1("4. The compliant booth model"));
kids.push(callout("ONE BOOTH DESIGN THAT WORKS EVERYWHERE",
 "This is not a conservative reading. It is the literal intersection of four real policies found in this research: "+
 "Montana State bans any monetary exchange at Catapalooza but expressly permits handouts and collecting contact "+
 "information for post-event follow-up; Weber State bars vendors from having students sign any contract for services "+
 "on site; Colorado State bans requesting credit card information, Venmo or similar app information; and WSU bars "+
 "distribution by accosting, confronting, detaining or waylaying individuals.\n\n"+
 "Designed this way, the same booth is compliant at every campus in the packet — and it removes the CARD Act "+
 "pattern-match (a tangible inducement offered to a student, on campus, to open a financial account) that will "+
 "otherwise alarm every dean of students who sees it.", NAVY));
kids.push(...SPACE(1));
kids.push(table(["#","Rule","Why — the policy or statute behind it"], DATA.booth.map((b,i)=>[String(i+1),b[0],b[1]]),
  [.04,.30,.66], {boldCols:[1]}));
kids.push(...SPACE(1));
kids.push(H2("Insurance requirements found"));
kids.push(table(["Campus","Requirement"], DATA.insurance.map(x=>[x[0],x[1]]), [.24,.76], {boldCols:[0]}));
kids.push(BR());

// 5. Route & budget
kids.push(H1("5. Recommended route and budget"));
DATA.route.forEach(([leg,summ,stops])=>{
  kids.push(H2(leg));
  kids.push(body(summ,{run:{italics:true,color:DGREY}}));
  stops.forEach(s=>kids.push(bullet(s)));
  kids.push(...SPACE(1));
});
kids.push(H2("Budget — published costs only"));
kids.push(table(["Line item","Cost","Notes"], DATA.budget, [.26,.12,.62], {boldCols:[0]}));
kids.push(body("Costs are what each institution publishes. Where a fee is unpublished it is marked as such — "+
  "assume for-profit rates and no discount.", {run:{italics:true, color:DGREY}}));
kids.push(BR());

// 6. Campus briefs
kids.push(H1("6. Campus briefs, by state"));
kids.push(body("Campuses are grouped by state in tour order, and within each state by access rating — the campuses "+
  "most open to an outside organization appear first. The access rating reflects what the written policy permits, "+
  "not how promising the audience is."));
kids.push(...SPACE(1));
kids.push(table(["Rating","Meaning"], [["5/5","Open — outside organizations explicitly admitted"],
  ["4/5","Workable — a paid or documented route exists"],["3/5","Gated — approval or sponsorship required"],
  ["2/5","Hard — commercial activity restricted"],["1/5","Effectively closed"]], [.12,.88], {boldCols:[0]}));

DATA.states.forEach(([state, campuses])=>{
  kids.push(BR());
  kids.push(H1(state));
  kids.push(table(["Campus","Access","Classes begin","Fair / access window"],
    campuses.map(c=>[c.name, STARS[c.access], c.start, c.fair_date||"—"]),
    [.30,.10,.24,.36], {boldCols:[0]}));

  campuses.forEach(c=>{
    kids.push(BR());
    kids.push(H2(c.name));
    kids.push(new Paragraph({spacing:{after:140},
      children:[new TextRun({text:`${c.city} · ${c.type} · ${c.tier} · Access ${STARS[c.access]}`,
        size:19, color:DGREY, italics:true})]}));
    kids.push(callout("RECOMMENDED PLAY", c.play, GOLD));
    kids.push(...SPACE(1));

    kids.push(H3("A. Fall 2026 calendar"));
    kids.push(table(["",""],[["Classes begin",c.start],["Add/drop",c.adddrop||"—"],
      ["Fall break",c.fallbreak||"—"],["Thanksgiving",c.thanksgiving||"—"],
      ["Last day of classes",c.lastclass||"—"],["Finals",c.finals||"—"],
      ["Source status",c.cal_status],["Source",c.cal_url]],
      [.24,.76], {boldCols:[0]}));

    kids.push(H3("B. Involvement fair / tabling event"));
    kids.push(table(["",""],[["Event",c.fair||"—"],["Date",c.fair_date||"—"],
      ["Outside orgs admitted?",c.fair_outside||"UNVERIFIED"],["Cost",c.fair_cost||"Not published"],
      ["Registration deadline",c.fair_deadline||"Not published"],["URL",c.fair_url||"—"]],
      [.24,.76], {boldCols:[0]}));

    kids.push(H3("C. Solicitation / outside-vendor policy"));
    kids.push(body(c.policy,{run:{bold:true}}));
    kids.push(body(c.policy_key));
    kids.push(body("Sponsorship requirement: "+c.sponsor_required, {run:{bold:true}}));
    kids.push(body("Source: "+c.policy_url, {run:{size:17,color:DGREY}}));

    kids.push(H3("D. Relevant student clubs"));
    kids.push(table(["Club","Notes"], c.clubs.map(x=>[x[0],x[1]||"—"]), [.30,.70], {boldCols:[0]}));

    kids.push(H3("E. Faculty and staff contacts"));
    kids.push(table(["Name / office","Title & notes","Contact"],
      c.faculty.map(x=>[x[0],x[1]||"—",x[3]||"—"]), [.22,.55,.23], {boldCols:[0]}));

    kids.push(H3("F. Courses"));
    kids.push(table(["Code","Title / description"], c.courses.map(x=>[x[0],x[1]]), [.16,.84], {boldCols:[0]}));

    kids.push(H3("G. Fall 2026 events"));
    kids.push(table(["Event","Detail"], c.events.map(x=>[x[0],x[1]]), [.26,.74], {boldCols:[0]}));

    kids.push(H3("H. Open questions to close by phone"));
    c.gaps.forEach(g=>kids.push(bullet(g)));
    if(c.note) kids.push(body(c.note,{run:{italics:true,color:RED}}));
  });
});

// 7. Gaps
kids.push(BR());
kids.push(H1("7. Consolidated research gaps"));
kids.push(body("Every item below could not be confirmed on a live university page. These are research gaps, not "+
  "findings of absence. Most are a single phone call. Items marked with a warning symbol are blocking — they should "+
  "be closed before travel or money is committed to that campus."));
kids.push(...SPACE(1));
kids.push(table(["State","Campus","Open question"], DATA.gaps, [.10,.24,.66], {boldCols:[1]}));

const doc = new Document({
  creator:DATA.org,
  title:`${DATA.org} Campus Tour — ${DATA.term} Information Packet`,
  description:"Campus-by-campus tour planning packet with compliance issue map",
  numbering:{config:[{reference:"bul", levels:[
    {level:0, format:LevelFormat.BULLET, text:"•", alignment:AlignmentType.LEFT,
     style:{paragraph:{indent:{left:convertInchesToTwip(0.32), hanging:convertInchesToTwip(0.18)}}}}]}]},
  styles:{ default:{
      document:{run:{font:"Calibri", size:21, color:"1A1A1A"}, paragraph:{spacing:{line:290}}},
      heading1:{run:{font:"Calibri", size:32, bold:true, color:NAVY}},
      heading2:{run:{font:"Calibri", size:26, bold:true, color:NAVY}},
      heading3:{run:{font:"Calibri", size:22, bold:true, color:GOLD}} } },
  sections:[{
    properties:{ page:{ size:{width:12240, height:15840},
      margin:{top:1080, right:1080, bottom:1080, left:1080} } },
    headers:{ default: new Header({children:[new Paragraph({alignment:AlignmentType.RIGHT,
      border:{bottom:{style:BorderStyle.SINGLE,size:4,color:GOLD,space:6}},
      children:[new TextRun({text:`${DATA.org} — Campus Tour, ${DATA.term}`,
        size:16, color:DGREY})]})]}) },
    footers:{ default: new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,
      children:[new TextRun({children:["Page ", PageNumber.CURRENT, " of ", PageNumber.TOTAL_PAGES],
        size:16, color:DGREY})]})]}) },
    children: kids
  }]
});

Packer.toBuffer(doc).then(b=>{
  const out = require('path').join(OUT, `${SLUG}-Report.docx`);
  fs.writeFileSync(out, b);
  console.log(`DOCX  ${(b.length/1024|0)} KB → ${out}`); });
