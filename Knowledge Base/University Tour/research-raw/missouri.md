# Missouri — DGD Campus Tour Research, Fall 2026

Research date: 12 August 2026. Nine campuses. Every claim carries the URL it came from.
Where a page could not be retrieved, that is stated plainly with the URL — a gap, not a finding of absence.

**Tooling constraints that shaped this research (report these, they are findings):**
- Direct `curl` to arbitrary hosts is blocked by the session egress proxy (403 on CONNECT). All retrieval
  was via the fetch tool, which converts pages to markdown and caps individual quotes at ~125 characters.
  Long policy text was therefore extracted as consecutive short verbatim fragments and reassembled.
- Every general web search engine tested (Google, Bing, DuckDuckGo HTML + lite, Mojeek) is ROBOTS-BLOCKED
  to this tooling. After the search budget was exhausted, navigation was by direct URL. Several campuses
  (Missouri State, SEMO, SLU) hide their policy libraries behind JavaScript site-search, and those policies
  could not be reached. Those campuses are rated `access 3 PROVISIONAL` per the standing rule.

---

## STATEWIDE LAYER 1 — the campus free-expression statute

**RSMo § 173.1550, the "Campus Free Expression Act."** Effective **28 August 2015** (L. 2015 S.B. 93).
Confirmed on the Missouri Revisor of Statutes.
https://revisor.mo.gov/main/OneSection.aspx?section=173.1550
FIRE's mirror: https://www.fire.org/research-learn/enacted-campus-free-speech-statutes-missouri

Verbatim, the operative parts:

- §1 — "The provisions of this section shall be known and cited as the 'Campus Free Expression Act'.
  Expressive activities protected under the provisions of this section include, but are not limited to,
  all forms of peaceful assembly, protests, speeches, distribution of literature, carrying signs, and
  circulating petitions."
- §2 — "The outdoor areas of campuses of public institutions of higher education in this state shall be
  deemed traditional public forums. Public institutions of higher education may maintain and enforce
  reasonable time, place, and manner restrictions in service of a significant institutional interest only
  when such restrictions employ clear, published, content, and viewpoint-neutral criteria, and provide for
  ample alternative means of expression. Any such restrictions shall allow for members of the university
  community to spontaneously and contemporaneously assemble."
- §3 — **"Any person who wishes to engage in NONCOMMERCIAL expressive activity on campus shall be permitted
  to do so freely, as long as the person's conduct is not unlawful and does not materially and substantially
  disrupt the functioning of the institution subject to the requirements of subsection 2 of this section."**
- §5 — the attorney general, or "Persons whose expressive rights were violated," may sue to enjoin or recover
  compensatory damages, costs and fees.
- §6 — on a finding of violation the court "shall award the aggrieved persons no less than five hundred
  dollars for the initial violation, plus fifty dollars for each day the violation remains ongoing."
- §7 — one-year limitation; each day the violation or the offending policy persists is a new accrual.

**THE OPERATIVE POINT FOR AN AMBASSADOR.** The statute's affirmative grant in §3 runs only to
**NONCOMMERCIAL** expressive activity. DGD is a for-profit cryptocurrency project; its tabling is commercial
speech. The statute does **not** give DGD a right to table, and every fee, permit and approval requirement
documented below is lawful under it. §2 does deem outdoor areas traditional public forums, and that is a real
constraint on the seven public campuses — but it is a tool for *student* advocates, not a shield for a vendor.

Note the drafting difference from Oklahoma's analogue: Missouri's §2 spontaneity clause is limited to
"members of the university community," while §3 says "any person." §3 is the broader grant and it is the one
carrying the noncommercial limiter. Do not let an ambassador read §3's "any person" without the adjective.

**Binds (public):** Mizzou, Missouri S&T, UMKC, UMSL, Missouri State, Truman State, SEMO.
**Does NOT bind (private):** Washington University in St. Louis, Saint Louis University. Both are private and
neither has a public-forum obligation. WashU says so on its own face — see below.

---

## STATEWIDE LAYER 2 — the UM System Collected Rules and Regulations (four campuses at once)

**CRR 110.010, "Regulations" (Chapter 110: Use of Facilities and Equipment).**
Amendment history printed on the rule: 12-10-49, 7-22-65, 9-26-69, 5-18-73, 11-19-82, 9-16-88, **11-18-21,
12-10-21, 6-29-23**.
https://www.umsystem.edu/ums/rules/collected_rules/facilities/ch110/110.010_regulations
(mirror: https://www.umsystem.edu/policies/collected-rules/facilities-and-equipment-management/ch110/110.010-regulations)

This one rule resolves the threshold access question at **Mizzou, UMKC, UMSL and Missouri S&T simultaneously.**
Verbatim fragments, with section numbers as printed:

**Solicitation and sales — 110.010.G**
- G.1 — "The sale of anything, the soliciting of subscriptions or the collection of dues is prohibited …
  without prior authorization of the Chancellor."
- G.2 — "Recognized student organizations may not solicit subscriptions or collect dues from prospective
  students or guests."

**Outside groups — 110.010.E**
- E.4 — "Use of available University facilities may be granted to nonstudent groups for meetings, programs
  and activities" —
  - E.4.a — "When the meeting, program and activity is sponsored by or the group is invited by an
    instructional or administrative division";
  - E.4.b — "When sponsored by a learned, educational, professional, or scientific society … when
    recommended by a dean";
  - E.4.c — "Other nonaffiliated and nonsponsored groups may make use of the facilities … upon written
    approval of the Chancellor."
- E.3 — "Persons who are not current students or employees … without specific permission or authorization or
  without an appropriate purpose may be deemed guilty of trespass."
- E.2 — "Persons who are not students or employees of the University … are required to abide by University
  policies and regulations."

**Student organizations — 110.010.D**
- D.2 — "University buildings and grounds may be utilized … for appropriate activities and programs sponsored
  by an officially recognized student organization," provided "The organization file a written request for
  approval of the activity or program at least ten days prior to the event." "The Chancellor is authorized to
  make an exception to the ten day rule in special circumstances."
- D.4 — "Such groups may do so only by written permission of the Chancellor."

**Fees — 110.010.E.5 / E.6**
- E.5 — "Affiliated groups … may be charged an approved fee."
- E.6 — "Nonaffiliated, nonsponsored groups … will be charged a fee approved by the Chancellor."

**What this means.** The UM System does **not** ban outside entities. It routes them to a
Chancellor-level written approval and a Chancellor-approved fee, with a ten-day floor on advance notice where
a student org is the requester. There is **no anti-fronting clause in CRR 110.010 itself** — that appears at
campus level (Missouri S&T has one; Mizzou's does not). Each of the four campuses then layers its own
procedure on top, and the four procedures are materially different: Mizzou publishes an actual vendor
reservation route, S&T publishes a rule that reads directly onto a crypto project, UMSL publishes free-speech
guidelines pointing back at 110.010, and UMKC publishes nothing retrievable at all.

Chapter 110 also contains 110.020 Service and Use Fees, 110.040 Sound Amplification Devices, and 110.100
"Use of Information Gathered from Credit Card Transactions on University Websites" — none of which were
retrieved in full; 110.020 is the likely home of any published rate card and is a gap worth closing.
https://www.umsystem.edu/ums/rules/collected_rules/facilities/ch110

---

## STATEWIDE LAYER 3 — geography

All nine campuses are on **SEMESTERS**. There is no quarter school, no trimester and no true block school in
this set. Two campuses run parallel sub-terms worth knowing about: **Truman State** runs block courses inside
the semester (first block ends Oct 6) and **SEMO** runs concurrent eight-week sessions with their own add/drop
deadlines. Neither changes the tour shape the way a quarter calendar would.

Start dates cluster into two waves one week apart:
- **Wave 1, Mon Aug 17:** Missouri State, Truman State. **Wed Aug 19:** SLU (earliest in the state).
- **Wave 2, Mon Aug 24:** Mizzou, WashU, Missouri S&T, UMSL, SEMO. UMKC unknown.

The clustering fact that actually reorders the trip: **St. Louis holds WashU, SLU and UMSL inside about
thirty minutes of one another** — three campuses, one hotel, one day. **Kansas City holds UMKC alone.**
Columbia (Mizzou) sits roughly midway on I-70. Rolla (S&T) is ~100 miles southwest of St. Louis on I-44 and
combines naturally with the St. Louis cluster. Springfield (Missouri State) and Cape Girardeau (SEMO) are the
outliers; Kirksville (Truman) is the most isolated stop in the set.

The cruel part: the St. Louis cluster is the **least** open in the state. WashU and SLU are private, and UMSL
is the thinnest of the three UM campuses. The money is in Columbia.

---

# 1. UNIVERSITY OF MISSOURI–COLUMBIA (MIZZOU) — Columbia, MO — Public — Tier A — **access 5**

### A. Academic calendar — Fall 2026 (SEMESTERS)
Confirmed on the Registrar's published 2026-2027 calendar PDF.
- **First day of classes: Mon Aug 24, 2026.**
- **⚠ NO FALL BREAK.** The calendar has none. Mizzou runs at full density Aug 24 straight through Nov 21 —
  thirteen uninterrupted weeks, the best sustained access window in Missouri.
- Thanksgiving recess: begins at close of day **Sat Nov 21**; classwork resumes 8:00 a.m. **Mon Nov 30**.
- Classwork ends at close of day **Thu Dec 10**. Reading day **Fri Dec 11**.
- Final examinations **Mon Dec 14 – Fri Dec 18**. Commencement Dec 18, 19 and 20.
- Add/drop deadlines are **not printed** on the 2026-2027 calendar PDF.
- ⚠ **Calendar conflict.** The registrar also posted a file titled
  "2026-2027-Academic-Calendar-Revised-to-exclude-Reading-Day-1.docx". Two versions of the same calendar
  exist and they disagree about whether Fri Dec 11 is a reading day. Immaterial for tabling, but confirm if
  a December stop is planned.
https://registrar.missouri.edu/wp-content/uploads/2024/12/2026-2027-Academic-Calendar-.pdf
https://registrar.missouri.edu/academic-calendar/

### B. Involvement fair
**Involvement Week, Aug 30 – Sept 5. "Get Involved Fair," Aug 31, 11 a.m. – 2 p.m., Kuhlman Court, 600+ orgs.**

⚠ **NO YEAR IS PRINTED ANYWHERE ON THE PAGE.** The footer says "© 2026." I resolved it by weekday, which is
the test the page itself fails to make easy:

| Date on page | If 2025 | If 2026 |
|---|---|---|
| Aug 31, Get Involved Fair, 11–2 | **Sunday** | **Monday** |
| Sep 3, Mizzou Football, Memorial Stadium, 7 p.m. | **Wednesday** | **Thursday** |

A Sunday involvement fair and a Wednesday-night home football game are both implausible; a Monday fair in
week two of a term that starts Aug 24, and a Thursday-night season opener, are both ordinary. **The page reads
as Fall 2026.** It is nonetheless unlabelled, so confirm by phone: **(573) 882-3780**.

Full published schedule, verbatim: Get Involved Fair "Aug. 31 | 11 a.m. - 2 p.m. | Kuhlman Court";
Volunteer Fair "Sept. 1 | 11 a.m. - 2 p.m. | Lowry Mall"; Meet Columbia "Sept. 1 | 5:30 - 7:30 p.m.";
Yoga on Rothwell Lawn and MGC 101 Sept 2; Power the Roar Pep Rally "Sept. 2 | 7:30-9:30 p.m. | Traditions
Plaza"; Gear Up for Game Day and Part-Time Job Fair "Sept. 3 | 10 a.m. – 1 p.m. | Lowry Mall"; Mizzou
Football Sept 3; Fall Fest "Sept. 4 | 4 - 8 p.m."

**Can outside organisations table?** Not stated, and the fair is a student-org fair. The one slot on the week
that admits outside entities by its own description is the **Volunteer Fair, Sept 1, 11 a.m.–2 p.m., Lowry
Mall — "Connect with local organizations"** — but that is a volunteering/nonprofit framing and a commercial
crypto project is a poor fit. No cost, no registration deadline and no eligibility rule are published.
https://getinvolved.missouri.edu/involvement-week/
https://getinvolved.missouri.edu/events/  (shows only Spring 2026 events; no fall listings)

### C. Solicitation / outside-vendor policy — **the best-documented commercial route in Missouri**

**BPPM 6:053, "Sales, Solicitations, Collections & Advertising."** Revised 08/22/2017; 09/30/2022; **7/17/2025**.
https://bppm.missouri.edu/policy/sales-solicitations-collections-advertising/

Verbatim:
- "All sales, solicitations, and collections in University buildings or on University grounds … are
  prohibited without prior authorization"
- **"The University shall not be used for commercial or promotional advertising purposes"**
- **"Non-University Groups will be allowed to request a reservation to sell on campus."**
- **"limited to conducting Sales or Solicitation activities for a maximum of five (5) days during the fall
  semester, five (5) days during the spring semester"** (and five in summer)
- **"Reservations must be requested not later than fifteen (15) business days in advance of the date
  requested"**
- Maximum **three vendor reservations per day** at approved locations, **10 a.m. – 2 p.m. CST**
- Applications are denied if inconsistent with the university mission or with existing contracts
- Gross sales above **$5,000** require Vice Chancellor for Finance approval
- "Recognized Student Organizations must get approval from the Division of Student Affairs" (and BPPM 1:090
  governs their fundraising; "fund-raising" is defined as any income-producing activity, including donations)

**Missouri Student Unions — Non-University Reservations.**
https://unions.missouri.edu/space-non-university
- "The off-campus vendor must fill out the University approved Facilities Use Agreement, and fulfill all
  requirements contained therein in its entirety."
- **"Vendors must also fill out a product approval form listing a detailed description of products and/or
  services they intend to offer"** — for a crypto project this is the form that decides everything. Fill it
  out honestly and early.
- "All reservations are tentative until approved. The Facilities Use Agreement and all other appropriate
  forms must be completed and returned with **full payment not less than one week prior** to the scheduled
  reservation date"
- "The reservation will be considered null and void if no contract or payment or an incomplete contract is
  received after this deadline."

**Outdoor space.** https://unions.missouri.edu/space-outdoor
- "All outdoor spaces are traditional public forums subject to reasonable time, place, and manner regulations."
- Activities may not **"Involve solicitations or promotion of commercial enterprises."**
- "Non-commercial pamphlets, handbills, circulars, newspapers, magazines and other written materials may be
  distributed on a person-to-person basis in open areas outside of buildings." — note **non-commercial**;
  the outdoor public-forum right does not carry DGD.
- Kuhlman Court "may be reserved and in which spontaneous events or activities may occur in the absence of a
  prior reservation" — reservable by "officially recognized MU student organizations."

**Absences — verified-not-found, NOT verified-permitted.** No anti-fronting clause was found. No clause
barring an RSO from sponsoring an outside group was found. No insurance requirement or dollar limit, no
deposit and no cancellation schedule appear on any retrieved page. **No dollar rate for a vendor table is
published anywhere** — the outdoor and indoor info-table pages carry no rate card. That is the single
biggest money gap at Mizzou: **(573) 884-8793**.
https://reservations.missouri.edu/event-spaces/outdoor-info-tables-1-3-rollins-4-6-kuhlman/

**⚠ THE PUBLISHED FOR-PROFIT TIER — this is why Mizzou rates 5.** Business Career Services prices employer
attendance at the **Mizzou Fall 2026 BUSINESS & ACCOUNTANCY Career Fair, Thu Sep 17, 2026, 10 a.m.–3 p.m.,
MizzouRec**: **for-profit organizations $600 ($630 with the 5% credit-card fee); non-profit and
Mizzou-affiliated $250 ($262.50)**. Registration via Handshake; **no deadline is published**.
Sep 17, 2026 is a Thursday — the listing is internally consistent and explicitly labelled 2026, not stale.
https://business.missouri.edu/student-development/career-preparedness/business-career-services/career-fairs

### D. Clubs
- **Financial Management Association (FMA)** — advisor **Dave Johnson**. Confirmed on the Trulaske student
  organizations page.
- **University of Missouri Investment Group** — advisor **Dave Johnson** (same advisor; one call reaches both).
- Association of Accountancy Students (advisor Kari Gingrich) · Beta Alpha Psi · National Association of Black
  Accountants (advisors Hayley Harned / Sijie Yao) · University of Missouri Insurance Association (advisor
  Dave Fischer) · Trulaske Consulting Association · Collegiate DECA · Collegiate FBLA · Delta Sigma Pi ·
  Alpha Kappa Psi · Mizzou Marketing Club · Pi Sigma Epsilon · SHRM · Student Center for the Public Trust ·
  Association of Trulaske Businesswomen · Black Business Students Association · ALPFA · Global Professionals ·
  Health Sales Club · Diverse Student Organization · Business Week · Trulaske Study Abroad · STUCO ·
  Alumni Mentor Program.
  https://business.missouri.edu/student-organization  (advisor names only — **no emails or phones published**)
- **⚠ NO blockchain, cryptocurrency, bitcoin or Web3 organisation was found at Mizzou.**
- ⚠ The full MU Engage directory (`engage.missouri.edu/club_signup?view=all`) **returned HTTP 504 through the
  proxy** and could not be enumerated. Absence of a crypto club is therefore *probable, not proven*.
- Do not use student officer names; Trulaske publishes none, and rosters rotate.

### E. Faculty / staff and phone numbers
Faculty: **no Mizzou faculty member working on blockchain, cryptocurrency or digital assets could be confirmed
on a live page.** David Johnson (Associate Teaching Professor of Finance, 339 Cornell Hall) is the FMA and
Investment Group advisor — his published expertise is reverse mortgages and financial planning, **not** digital
assets; his faculty page publishes **no email and no phone**. Do not represent him as a crypto researcher.
https://business.missouri.edu/departments-faculty/people-directory/david-johnson

Offices, all confirmed:

| Office / person | Number | Controls |
|---|---|---|
| **MU Reservations & Events (main)**, S4 Memorial Union | **(573) 884-8793** | The vendor reservation. Start here. |
| Kate Fleming, Director, Reservations & Events | (573) 884-8793 | Escalation on a vendor request |
| Sam Cohen, Reservations & Events Coordinator | (573) 882-0960 | Books the table |
| Lauren Northern, Reservations & Events Coordinator | (573) 884-8818 | Books the table |
| Rachel Allen, Senior Event Support Specialist | (573) 884-1504 | Event support |
| John Cattanach, Associate Director – Theaters | (573) 882-5998 | Venue |
| Emily Stoker, Senior Event Coordinator | (573) 882-2155 | Student-development events |
| Josh Ramsey, EMS software admin | (573) 882-8935 | The booking system itself |
| **Division of Finance & Business Services**, 311 Jesse Hall | **(573) 882-2094** | Authorises sales & solicitation under 6:053 |
| MU Joint Office of Strategic Communications | (573) 882-4523 | Advertising questions |
| Missouri Student Unions, administrative office | (573) 882-6310 | Second number on the non-university page |
| Student Center Information Desk | (573) 882-1174 | Building |
| **Get Involved / Student Activities & Engagement**, 2500 MU Student Center | **(573) 882-3780** | The Involvement Fair; confirms the year |
| Division of Student Affairs, 2202 MU Student Center | (573) 882-0157 | RSO approvals under 6:053 |
| **Dr. Michelle Froese, Dean of Students** | **(573) 882-5397** | Escalation |
| **Business Career Services**, 111 Cornell Hall | **(573) 882-2565** | The $600 for-profit career-fair slot |
| MU Career Center, 201 Student Success Center | (573) 882-6801 | The other four fairs |
| Campus Facilities | (573) 882-3094 | Tent stakes, utilities |
| Sound amplification approval, 304 Jesse Hall | (573) 882-7255 | Amplified sound |

Emails: reservations@missouri.edu · engagement@missouri.edu · studentaffairs@missouri.edu ·
mudosdeanofstudents@missouri.edu · bcs@missouri.edu · career@missouri.edu · unions@missouri.edu

### F. Courses
- **CMP_SC 4460 Introduction to Cryptography** — the closest catalog course. "Cryptography is an important
  technique used to achieve security goals in an untrusted and possibly adversarial environment…" No mention
  of blockchain or digital currency. Fall 2026 offering not confirmed.
  https://catalog.missouri.edu/courseofferings/cmp_sc/
- **No blockchain, cryptocurrency or distributed-ledger course was found in Computer Science.**
- The Finance course-offerings URL (`catalog.missouri.edu/courseofferings/finance/`) **404s**; the finance
  course list was not reached.

### G. Events
- **⚠ TigerHacks** — Mizzou's largest hackathon, Lafferre Hall, run by the College of Engineering. Live site
  shows **Nov 7–9, 2025**, a 48-hour event; the MLH "2026 Hackathon Season" badge is a season label, not a
  2026 date. **Fall 2026 dates not published; pattern is one weekend in early November.**
  Sponsorship prospectus (**covers 2024 — a year stale, treat amounts as indicative**):
  **Seed $1,700** (logo, marketing, meal sponsorship, judging); **Sprout $3,000** (+ t-shirt logo, **"Career
  Fair Participant"**, bring mentors/reps, early participant data); **Sapling $5,000** (+ host a workshop,
  custom prize category, **"Present at Opening and Closing Ceremony,"** **"Schedule On-Site Interviews,"** full
  participant data). 2024 attendance "over 300 students from across the Midwest." Past sponsors: Garmin,
  Veterans United, Enterprise Mobility, Shelter Insurance, H&R Block. Custom packages available.
  Contact **muengrtigerhacks@umsystem.edu**.
  https://tigerhacks.missouri.edu/ · https://tigerhacks.missouri.edu/prospectus.pdf
  A hackathon sponsorship is a private student-run arrangement and sidesteps BPPM 6:053 entirely.
- **Five confirmed Fall 2026 career fairs**, all explicitly labelled 2026:
  Sep 10 Mizzou Engineering · Sep 16 Textile & Apparel Management · **Sep 17 Business & Accountancy** ·
  Sep 30 CAFNR/Arts & Science Career & Internship Expo · Sep 30 Health & Wellness Career and Graduate Fair.
  https://career.missouri.edu/jobs-and-internships/career-fairs/
- Part-Time Job Fair, Sept 3, 10 a.m.–1 p.m., Lowry Mall (Involvement Week).

**Sources:** all URLs above.

---

# 2. WASHINGTON UNIVERSITY IN ST. LOUIS — St. Louis, MO — Private — Tier A — **access 2**

### A. Academic calendar — Fall 2026 (SEMESTERS)
- **First day of classes: Mon Aug 24, 2026.**
- **Fall Break: Sat–Tue Oct 3–6, 2026** — the only real mid-semester fall break among the St. Louis three.
- Thanksgiving: **Wed Nov 25 – Sun Nov 29, 2026.**
- **Last day of classes: Mon Dec 7.** Reading days **Tue–Wed Dec 8–9.**
  **Finals Thu Dec 10 – Wed Dec 16.** (Commencement is May 2027.)
- Add/drop deadline **not printed** on the bulletin calendar.
https://bulletin.wustl.edu/washu/calendar/ · PDF: https://bulletin.wustl.edu/washu/calendar/calendar.pdf

### B. Involvement fair
Campus Life refers to "the annual Activates Fair" (typo in the original) but **publishes no date, time,
location, eligibility rule or cost.** UNVERIFIED. Confirmed First Week events only: Aug 24 Carnival 6 p.m.,
Aug 25 Customize your Crib 6 p.m., Aug 26 Pantry Bingo 6 p.m.
Will post at https://campuslife.washu.edu/ — confirm at **(314) 935-3443**.

### C. Solicitation / outside-vendor policy — **a flat bar with one narrow door**

**Danforth Campus Facilities Access Policy**, last updated **7 November 2024**.
https://washu.edu/policies/danforth-campus-facilities-access-policy/

- **⚠ "Except as otherwise described herein, external individuals and organizations not affiliated with the
  university are NOT PERMITTED TO RESERVE UNIVERSITY SPACE DURING THE ACADEMIC YEAR FROM AUGUST 1-MAY 31."**
  That window is the entire tour.
- "External individuals and organizations not affiliated with the university may reserve certain spaces during
  the summer months of June and July and do not require sponsorship."
- **"The university is a private institution and retains the ability to prohibit or deny use of its facilities
  or spaces for any reason at the sole discretion of the university."** WashU states its own status; do not
  argue public-forum doctrine or § 173.1550 here, neither applies.
- "Solicitation of funds on university property or at university events by persons not employed by the
  university or otherwise authorized by the university is prohibited."
- "Persons not employed or otherwise authorized by the university are prohibited from soliciting funds or
  signatures, distributing literature or gifts."
- "Solicitation of any kind in any university residential facility is prohibited."
- **SPONSORSHIP DOES CURE IT — this is the door:** "Subject to certain restrictions around political activity,
  if an event is co-sponsored by a university recognized student organization or department, the department or
  student organization may reserve the space and invite the external individual or organization to participate."
- Reservations: "no less than two weeks prior"; DUC/Oak Walk banners, South 40 underpass panels and **DUC
  tables: no less than five days prior**; changes "no less than three (3) business days prior."
- Anonymous postings without an identified sponsoring RSO, department or individual "may be removed."

**Solicitation and Distribution Policy (Human Resources), updated January 2024** — the broader, blunter rule:
> **"Persons not employed or otherwise authorized by the university are prohibited from soliciting funds or
> signatures, distributing literature or gifts, OFFERING TO SELL MERCHANDISE OR SERVICES or engaging in any
> other solicitations or similar activity on university property."**
No policy number is assigned on the page. https://hr.wustl.edu/items/solicitation-and-distribution-policy/

**External Events (Event Management).** https://eventmanagement.wustl.edu/special-events/
- Academic year: "non-university / external events require sponsorship by a Washington University department."
  Note this says **department**, not student organisation — a stricter reading than the Danforth policy's.
  The two documents are not perfectly aligned; ask which controls.
- June–July: external events "do not require sponsorship."
- **"External inquiries must be placed a minimum of 30 days in advance, and are subject to availability,
  staffing, and resources."**
- Sponsored academic-year events: "rental fee will be **50% of the 'Non-University / External Events'** listed
  on the rates page."
- **⚠ THE RATES PAGE IS AN IMAGE.** https://eventmanagement.wustl.edu/rates/ names three tiers — Premier Level
  Spaces, Standard Level Spaces, Pooled Classrooms — and carries **no machine-readable dollar amounts at all**.
  "Venue rates include furniture and some built-in technology"; excluded are "housekeeping, some A/V additions,
  additional furniture not associated with the room, decor, parking, or catering."
- Insurance, deposits and cancellation terms: **not published anywhere retrieved.**

**DUC tabling.** https://eventmanagement.wustl.edu/items/duc-tabling/
Only "university recognized student organizations and departments" may reserve. "Standard tabling hours are
11:00 AM to 2:00 PM"; forfeited if unstaffed past 11:15. **"Each group may only table 5 days per month in the
DUC."** No amplified sound. No pricing published.

**Nothing was found reaching payment credentials or on-site contract signing at WashU.**

### D. Clubs
⚠ **WUGO (Washington University Group Organizer) at `wustl.presence.io` is JAVASCRIPT-RENDERED** — "the actual
organization directory content is not included in the source material." It is not login-gated as far as could
be told, but it is not machine-readable. **No WashU club of any kind could be confirmed.** Do not assume the
absence of a blockchain club; assume it was unreadable.

### E. Faculty / staff and phone numbers
⚠ **The Olin Business School faculty directory is JAVASCRIPT-RENDERED** and returned an empty result set
(`olin.washu.edu/faculty-and-research/faculty-directory/`). No WashU faculty member could be confirmed on any
topic. Olin publishes **no main phone number** on the directory page — only website@olin.wustl.edu.

| Office / person | Number | Controls |
|---|---|---|
| **Event Management (main)**, DUC Suite 270 | **(314) 935-3443** | Every reservation; also the Campus Life line |
| **Indra Russell, Event Manager** | **(314) 935-8264** · irussell@wustl.edu | The named human for external events |
| Office of Campus Life, DUC Suite 160 | (314) 935-3443 · campuslife@wustl.edu | Student orgs, the Activities Fair |

### F. Courses
⚠ **The WashU bulletin course search is ROBOTS-BLOCKED** (`bulletin.wustl.edu/search/?P=blockchain` returned
ROBOTS_DISALLOWED). No WashU course could be checked. Gap.

### G. Events
First Week: Aug 24 Carnival, Aug 25, Aug 26 — confirmed. Nothing else retrievable. No hackathon confirmed.

---

# 3. MISSOURI UNIVERSITY OF SCIENCE AND TECHNOLOGY — Rolla, MO — Public (UM System) — Tier A — **access 2**

### A. Academic calendar — Fall 2026 (SEMESTERS; 16-week regular session)
Confirmed on the Registrar's Fall 2026 Dates and Deadlines PDF.
- **First day of classes: Mon Aug 24, 2026.** Free add Aug 24 (permission numbers required for the first two
  weeks). **Free drop / 100% refund: Sun Aug 30.** Last day to drop without "WD" on the transcript: **Mon Oct 5.**
- **Fall Break: 8:00 a.m. Thu Oct 8 – 8:00 a.m. Mon Oct 12, 2026.**
- **⚠ Thanksgiving recess: 8:00 a.m. Sun Nov 22 – 8:00 a.m. Mon Nov 30, 2026 — NINE DAYS, the longest
  Thanksgiving shutdown of any campus in this set.** Rolla is empty for over a week.
- Last day of classes **Fri Dec 11**. Finals **Mon Dec 14 (from 7:30 a.m.) – Fri Dec 18.**
- Commencement Dec 18 6:00 p.m. (PhD/Master's); Dec 19 10:00 a.m. and 3:00 p.m. (undergraduate).
https://registrar.mst.edu/media/administrative/registrar/documents/calendars/2026/FS2026%20Dates%20and%20Deadlines.pdf

### B. Involvement fair
**Not published on any retrievable page.** Student Involvement (218 Havener Center) claims "more than 200
student organizations" but publishes no fair. UNVERIFIED — call **(573) 341-4025** or **(573) 341-6771**.
https://involvement.mst.edu/

### C. Solicitation / outside-vendor policy — **⚠⚠ THE DECISIVE POLICY IN MISSOURI FOR A CRYPTO PROJECT**

**Havener Center Policies** (Events and Hospitality Management). https://havener.mst.edu/policies/
No policy number or effective date is printed on the page. Verbatim:

> **"CREDIT CARD, TELEPHONE CARD, OR OTHER FINANCIAL SERVICES VENDORS ARE NOT ALLOWED AT THE HAVENER CENTER
> OR ON THE MISSOURI S&T CAMPUS."**

That is a **campus-wide** prohibition naming a category of vendor by financial function, with no exception
process printed, and it is the only sentence of its kind found anywhere in Missouri. Whether a
non-custodial protocol counts as an "other financial services vendor" is a live question — but it is the
question S&T will ask, and the ambassador must not be surprised by it.

> **"Direct solicitation of money, regardless of the intended use, is not permitted on University property."**

> **⚠ ANTI-FRONTING: "Non-university groups or individuals may not reserve facilities in the name of a student
> group or university department to avoid payment of usage fees."**

The club workaround that works at Truman and (in a limited form) at WashU is closed here.

Also verbatim:
- "Users of Havener Center who are not associated with Missouri S&T must complete an usage agreement in order
  to hosts events in the facility." (typo in the original)
- "Reservation requests will only be accepted in the name of the group or individual sponsoring the event"
- Table space, **Informational**: "The organization distributes information to the campus community or gives
  away items at no charge." Table space, **Commercial**: "The organization gathers information or sells goods
  and/or services for a profit." Both require **two full business days** notice, and both carry a rental fee —
  but **"Please contact Events and Hospitality Management for pricing." NO DOLLAR AMOUNTS ARE PUBLISHED.**
- Cancellation: "Groups failing to cancel a reservation at least two full business days in advance of event …
  will receive a warning after the first infraction and a **$50 administrative fee** for each time thereafter."
  No-show: "Groups who have a confirmed reservation that do not utilize meeting room(s) or space will be
  subject to a **$50 administrative fee**."
- Decoration violations: fee "not less than $50." Technician services: "minimum $25 charge." Overtime:
  "minimum fee assessed is $50." **A 3% convenience fee applies to credit card payments.**
- Insurance: "Proof of general liability insurance in the amount of **one million dollars ($1,000,000.00)**"
  — as printed, this requirement attaches to **events with alcoholic beverages**. No general insurance
  requirement or limit for a table was found.
- "As a state and student fee-funded building, Havener Center offers its services to student organizations
  first and foremost." https://havener.mst.edu/reservations/

Above it sits **CRR 110.010** (see statewide layer 2): sales and solicitation need "prior authorization of the
Chancellor," and nonaffiliated nonsponsored groups pay "a fee approved by the Chancellor."

### D. Clubs
⚠ **MinerLink (`minerlink.mst.edu`) is JAVASCRIPT-RENDERED** — the fetch returned only
`{"title":"StudentsCommunityPlatform"}` metadata and no organisation list. 200+ orgs claimed; **none could be
enumerated.** No blockchain or crypto club confirmed either way.

### E. Faculty / staff and phone numbers
No S&T faculty member working on blockchain or digital assets could be confirmed. The Computer Science
department publishes its research areas as **Systems and Networking; Cyber Security; Artificial Intelligence
and Data Science; Theory and Quantum Computation; High-Performance and Cloud Computing** — **blockchain is not
among them.** No department chair is named on the CS landing page.

| Office / person | Number | Controls |
|---|---|---|
| **Events and Hospitality Management** | **(573) 341-4399** | Writes the policy above; sets table pricing; the usage agreement |
| Havener Center (main), 1346 N. Bishop Ave | (573) 341-4564 · reserve@mst.edu | Reservations desk |
| **Student Involvement**, 218 Havener Center | **(573) 341-4025** · involvement@mst.edu | Orgs, MinerLink, any fair |
| Student Involvement (second published number) | (573) 341-6771 | Same office |
| **Career Opportunities & Employer Relations** | **(573) 341-4343** · career@mst.edu | The Sep 22 career fair — the real door |
| Computer Science, 325 CS Building | (573) 341-4492 · csdept@mst.edu | Whether any blockchain course/faculty exists |
| Office of the Registrar | (573) 341-4181 · registrar@mst.edu | Calendar |
| S&T Dining Services | (573) 341-7019 | Food at an event |
| Missouri S&T main line | (800) 522-0938 | Operator, last resort |

### F. Courses
⚠ **`catalog.mst.edu` is ROBOTS-BLOCKED** to research tooling (`/search/?P=blockchain` returned
ROBOTS_DISALLOWED; `/coursesofinstruction/comp_sci/` and `/undergraduate/coursesofinstruction/comp_sci/` both
404). **No S&T course could be checked.** Call (573) 341-4492.

### G. Events
**⚠ Missouri S&T Career Fair — Tue Sep 22, 2026, 9:00 a.m. – 2:00 p.m.** Confirmed on the career services
landing page; Sep 22, 2026 is a Tuesday, so the listing is internally consistent. **Employer registration cost
is not published.** career@mst.edu · (573) 341-4343. https://career.mst.edu/
This is the one route into S&T that does not run through the Havener financial-services clause: a career fair
is an employer-recruiting framework, not a vendor-solicitation framework.

---

# 4. SAINT LOUIS UNIVERSITY — St. Louis, MO — Private (religious, Jesuit) — Tier B — **access 3 PROVISIONAL**

### A. Academic calendar — Fall 2026 (SEMESTERS)
- **⚠ First day of classes: Wed Aug 19, 2026 — THE EARLIEST START IN MISSOURI**, five days ahead of the Aug 24
  wave and the only midweek start in the set.
- Fall break **Oct 22–23, 2026.** Thanksgiving **Nov 25–27, 2026.**
- **Last day of classes Fri Dec 4.** Finals **Mon Dec 7 – Fri Dec 11.**
- Add/drop deadline is not on the summary calendar; the full PDF was not retrieved
  (`slu.edu/registrar/pdfs/2026-2027-academic-calendar.pdf` — referenced by the registrar but the copy at
  `slu.edu/pdfs/...` 404s).
https://www.slu.edu/registrar/calendars/index.php

### B. Involvement fair
**Not found on any live SLU page.** UNVERIFIED. Call Student Involvement, **(314) 977-2805**.

### C. Solicitation / outside-vendor policy — **⚠ NOT RETRIEVED**
SLU's governing solicitation or facility-use policy could not be reached. Every candidate URL tested returned
404 (`/about/catholic-jesuit-identity/policies/solicitation.php`, `/human-resources/pdfs/policies/
solicitation-policy.pdf`, `/event-services/index.php`, `/life-at-slu/student-responsibility-and-community-
standards/index.php`), the Busch Student Center page carries no reservation rules, the student-organization
resources page carries **no handbook, no PDF, no policy text and no phone number**, and `catalog.slu.edu` is
ROBOTS-BLOCKED.

**Per the standing rule this is rated 3, PROVISIONAL, and named as a gap — not guessed in either direction.**

What is certain: SLU is a **private, Catholic, Jesuit** institution. It has **no public-forum obligation** and
**RSMo § 173.1550 does not reach it.** Do not cite the statute at SLU. A Jesuit mission-alignment argument is
available and worth more here than a rights argument — but a for-profit crypto project is a hard fit for it,
and that should be said honestly rather than dressed up.

### D. Clubs
⚠ **SLU Groups (`groups.sluconnection.com`) is JAVASCRIPT-RENDERED** — the page returns "This application
requires JavaScript to be enabled." 200+ organisations claimed; **none could be enumerated.** No SLU club of
any kind confirmed.

### E. Faculty / staff and phone numbers
No SLU faculty member could be confirmed on any relevant topic.

| Office | Number | Controls |
|---|---|---|
| **Student Involvement Center**, Busch Student Center Room 319 | **(314) 977-2805** · involvement@slu.edu | Orgs, SLU Groups, any fair; the office to ask for the solicitation policy |
| Busch Student Center Information Desk | (314) 977-2820 · BSC@slu.edu | Space reservations and tabling — the page names this number explicitly for that purpose |
| Office of the University Registrar, DuBourg Hall Rm 22 | (314) 977-2269 · registrar@slu.edu | Calendar |
| Classroom Scheduling | (314) 977-3017 | Rooms |

### F. Courses — not retrieved (catalog robots-blocked).
### G. Events — not retrieved.

---

# 5. MISSOURI STATE UNIVERSITY — Springfield, MO — Public — Tier B — **access 3 PROVISIONAL**

### A. Academic calendar — Fall 2026 (SEMESTERS)
- **⚠ First day of classes: Mon Aug 17, 2026** — first wave, a week ahead of Mizzou.
- Late registration with full refund eligibility: **Aug 24 – Aug 28, 2026.**
- **Fall break: Oct 8 – Oct 11, 2026** (no classes, offices open).
- **Thanksgiving: Nov 21 – Nov 29, 2026** (offices closed Nov 25–27) — a nine-day student absence.
- **⚠ Last day of classes: Thu Dec 3, 2026 — MISSOURI STATE FINISHES FIRST IN THE STATE.**
  Finals **Dec 5 – Dec 10.** Anything scheduled in Springfield after about Nov 18 is worthless.
https://www.missouristate.edu/registrar/academic-calendar.htm

### B. Involvement fair — **not published on any retrievable page.** UNVERIFIED.

### C. Solicitation / outside-vendor policy — **⚠ NOT RETRIEVED**
- `https://www.missouristate.edu/policy/` returns **TOO MANY REDIRECTS** (redirect loop).
- `https://policies.missouristate.edu/` **does not resolve — DNS failure** (`Name or service not known`).
- `https://www.missouristate.edu/search/` redirects to `search.missouristate.edu`, which is a
  **JavaScript-rendered** search shell returning no results to tooling.
- Every guessed Plaster Student Union URL 404s (`/PSU/`, `/PSU/reservations.htm`, `/psu/index.htm`,
  `/PlasterStudentUnion/`, `/eventservices/`). Every guessed Student Engagement sub-page 404s.
- FIRE's school page redirects to a generic college index and yields nothing.

Rated **3, PROVISIONAL**. Missouri State is a public institution and **is bound by RSMo § 173.1550** — its
outdoor areas are traditional public forums — but § 173.1550(3) protects only *noncommercial* activity, so
that does not carry DGD. **One phone call closes this campus's entire policy picture.**

### D. Clubs
⚠ **The directory (`missouristate.presence.io/organizations`, "Real Bears Get Involved") is
JAVASCRIPT-RENDERED.** 300+ organisations claimed; **none could be enumerated.**
https://www.missouristate.edu/StudentEngagement/student-organizations.htm

### E. Faculty / staff and phone numbers
⚠ **This is the thinnest contact picture in the set.** The Office of Student Engagement publishes **no direct
phone number** — the student-organizations page gives only the university switchboard. The Registrar publishes
an email and a room (Carrington Hall 320, Mon–Fri 8–5, unavailable Thu 8–9 a.m.) but **no direct number**.

| Office | Number | Controls |
|---|---|---|
| Missouri State University main line | **(417) 836-5000** (MAIN LINE) · Info@MissouriState.edu | The only confirmed number. Ask the operator for Student Engagement and for Event/Facility Scheduling. |
| Office of the Registrar, Carrington Hall 320 | no number published — look up here · Registrar@MissouriState.edu | Calendar |

### F. Courses — not retrieved.
### G. Events — not retrieved.

---

# 6. UNIVERSITY OF MISSOURI–KANSAS CITY (UMKC) — Kansas City, MO — Public (UM System) — Tier B — **access 3**

### A. Academic calendar — Fall 2026 — **⚠ NOT RETRIEVABLE**
`https://www.umkc.edu/registrar/academic-calendar.html` **returns an EMPTY PAGE BODY** — confirmed twice; the
content is JavaScript-injected or the page is broken. `catalog.umkc.edu/undergraduate-academic-regulations-
information/academic-calendar/` returns navigation chrome only, with no calendar content. Every other URL
variant tested 404s.

**Fall 2026 dates are UNVERIFIED.** For planning only, and explicitly *not* a finding: the three sibling UM
System campuses whose calendars were confirmed — Mizzou, Missouri S&T and UMSL — **all begin Mon Aug 24, 2026**.
UMKC very likely matches. **Do not schedule on that assumption.** Registrar: **(816) 235-1125**.

### B. Involvement fair — not published on any retrievable page. UNVERIFIED. (816) 235-1407.

### C. Solicitation / outside-vendor policy
**CRR 110.010 governs** — the full text is in the statewide layer above and is the operative document until a
campus procedure is produced. In short: sales and solicitation require **"prior authorization of the
Chancellor"**; nonaffiliated, nonsponsored groups "may make use of the facilities … upon written approval of
the Chancellor" and "will be charged a fee approved by the Chancellor"; a sponsoring student organisation must
file a written request **at least ten days prior**; and non-students present "without specific permission or
authorization or without an appropriate purpose may be deemed guilty of trespass."

**No UMKC-specific solicitation, tabling or vendor page could be retrieved.** The Student Union page publishes
a reservations email (`umkcsureservations@umkc.edu`) but **no reservations phone number, no rates, no tabling
rules and no external-group terms**. `info.umkc.edu/studentunion/` 302-redirects to `umkc.edu/campus`, which
carries none of it either.

UMKC is public and bound by § 173.1550 — noncommercial activity only.

### D. Clubs — directory not located. UNVERIFIED.

### E. Phone numbers

| Office | Number | Controls |
|---|---|---|
| **Office of Student Involvement**, Student Union Ste 320 | **(816) 235-1407** · getinvolved@umkc.edu | Orgs, any fair |
| **Student Union**, 5100 Cherry St. Ste 320 | **(816) 235-5555** | The building; ask them to route the reservations question |
| Division of Student Affairs | (816) 235-1141 · umkccares@umkc.edu | Escalation; no Dean of Students office is listed |
| Office of the Registrar, Administrative Center Rm 115 | (816) 235-1125 · registrar@umkc.edu | **The Fall 2026 calendar — call this first** |
| UMKC main line | (816) 235-1000 (MAIN LINE) | Operator |
| Student Union reservations | no number published — look up here · umkcsureservations@umkc.edu | Space |

### F. Courses — not retrieved.
### G. Events — not retrieved.

---

# 7. UNIVERSITY OF MISSOURI–ST. LOUIS (UMSL) — St. Louis, MO — Public (UM System) — Tier C — **access 3**

### A. Academic calendar — Fall 2026 (SEMESTERS) — confirmed
- **Classes begin 8:00 a.m. Mon Aug 24, 2026.**
- **Last day any student may enroll: Sun Aug 30, 2026.**
- **Fall break: 12:00 a.m. Thu Oct 8 – classes resume Mon Oct 12, 2026.**
- **Thanksgiving recess: 5:00 p.m. Sat Nov 21 – 8:00 a.m. Mon Nov 30, 2026.**
- **Classes end 5:00 p.m. Sat Dec 12, 2026.** Finals begin **Mon Dec 14**; semester closes **Sat Dec 19.**
https://www.umsl.edu/registration/resources/students/semester-calendars-important-dates.html

### B. Involvement fair
"Weeks of Welcome" orientation activities are referenced; **no fair name, date or eligibility rule is
published.** UNVERIFIED — (314) 516-5291.

### C. Solicitation / outside-vendor policy
**UMSL Campus Free Speech Guidelines** — https://www.umsl.edu/free-speech.html — verbatim:
- "The outdoor areas of UMSL have been deemed a traditional public forum. Therefore, members of the public are
  free to exercise expressive activities outdoors"
- Activities may not **"Involve solicitations or promotion of commercial enterprises."**
- **"Non-commercial pamphlets, handbills, circulars, newspapers, magazines and other written materials may be
  distributed on a person-to-person basis"** — the permission is expressly limited to *non-commercial* material.
- "Remain 20 feet from entrances/exits"
- **"Policies related to use of facilities, including for solicitation or sales are outlined in the Collected
  Rules and Regulations (CRR 110.010)."** — UMSL points straight back at the systemwide rule.

So UMSL is the cleanest illustration of the Missouri structure: the outdoor forum is genuinely open to the
public, and commercial solicitation is carved straight out of it. The route is CRR 110.010's Chancellor
authorisation, plus a Chancellor-approved fee. No UMSL rate card was found. No anti-fronting clause was found.

No office name, no email and no direct phone appears anywhere on the free-speech page — only the campus
switchboard. That is a notable omission on a page telling people how to exercise a right.

### D. Clubs — Triton Connect, **partially readable**
`tritonconnect.umsl.edu/club_signup` is **JavaScript-rendered** ("Loading…", "Load all 169 groups") but a
partial list surfaced. Confirmed present: **Accounting Club**, **Beta Alpha Psi – Gamma Psi** (business/finance
honour society), UMSL Esports, American Institute of Graphic Arts, Chess Club, Biological Society, Chemistry
Club. **No blockchain, crypto, bitcoin or Web3 organisation appeared, and no dedicated computer-science, data
science, ACM, economics, entrepreneurship or investment club appeared** — but only a fraction of the 169
groups loaded, so this is *partial*, not exhaustive.

### E. Phone numbers

| Office | Number | Controls |
|---|---|---|
| **Office of Student Involvement**, 366 Millennium Student Center | **(314) 516-5291** · studentinvolvement@umsl.edu | Orgs, Weeks of Welcome, any fair |
| Office of Registration | (314) 516-5545 · registration@umsl.edu | Calendar |
| UMSL main line | (314) 516-5000 (MAIN LINE) | Operator; the only number on the free-speech page |

### F. Courses — not retrieved.
### G. Events — not retrieved.

---

# 8. TRUMAN STATE UNIVERSITY — Kirksville, MO — Public — Tier C — **access 3**

### A. Academic calendar — Fall 2026 (SEMESTERS, **with block courses inside the term**)
- **⚠ Classes begin Mon Aug 17, 2026** — first wave.
- **⚠ BLOCK STRUCTURE: first block courses conclude Tue Oct 6, 2026.** Truman is the one campus in this set
  where a sub-term boundary sits in the middle of the tour window; student attention resets there.
- **Midterm break: Thu–Fri Oct 8–9, 2026.**
- Thanksgiving break: **Mon–Fri Nov 23–27, 2026.**
- **Last day of instruction Fri Dec 4.** Finals start **Mon Dec 7**; **reading day Wed Dec 9**; exams end
  **Fri Dec 11.** Commencement **Sat Dec 12, 11 a.m.**
- Add/drop deadlines are **not printed** on the 2026-27 calendar.
https://www.truman.edu/majors-programs/academic-resources/academic-calendar-schedules/academic-calendar/2026-27-academic-calendar/

### B. Involvement fair — not published. UNVERIFIED — (660) 785-4222, orgs@truman.edu.

### C. Solicitation / outside-vendor policy
**Board of Governors Code of Policies, Chapter 12 — "Facilities – Uses and Priorities."** Chapter revised
**August 2, 2014**; the facilities-use provisions carry a "1987 Compilation (Established practice)" citation.
https://c3c5e312.delivery.rocketcdn.me/wp-content/uploads/2014/02/CHAPTER-12-REVISED-August-2-2014.pdf
(index: https://www.truman.edu/about/our-people/board-of-governors/board-of-governors-codes-of-policies/)

Verbatim:
- 12.010 — "University buildings and grounds are intended for use by faculty, staff, and students for
  educational, administrative, and recreational purposes, and such uses have the highest priority"
- 12.010 — **"Other persons and groups may use University facilities on a space available basis"**
- 12.010 — "in accordance with the policies and procedures, including **possible rental fees**, established by
  the President"
- 12.020.1(3) — "Speakers invited by the faculty sponsor and president of a university-chartered organization"
- 12.020.2 — "Speakers invited by faculty sponsor and president of a chartered student organization shall also
  be the responsibility of the membership of that chartered organization"

**⚠ NOTABLE ABSENCES — verified-not-found, NOT verified-permitted.** Chapter 12 contains **no solicitation
clause, no sales clause, no commercial-activity ban, no anti-fronting clause and no insurance provision** that
could be found. The Campus Protests policy (`/wp-content/uploads/2014/11/Campus-Protests.pdf`) is a general
First Amendment and civility statement with **no commercial provision, no advance-notice requirement and no
designated-area rule.** Truman's own policy index states plainly: "This webpage does not contain an exhaustive
list of university policies." **A rental rate card and any operating procedure under 12.010 were not found.**

That combination makes Truman, on the retrievable text, the **most permissively worded public policy in the
set** — an outside group "may use University facilities on a space available basis" for a fee. It is rated 3
rather than 4 only because no rate, no procedure and no application form could be produced. Confirm before
relying on it.

Truman is public and bound by § 173.1550 — noncommercial activity only.

### D. Clubs — **⚠ THE ONLY FULLY READABLE ORG DIRECTORY IN MISSOURI**
Truman publishes a static, non-JavaScript organisation list with advisors and student contacts.
https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/

- **⚠ Bulldog Student Investment Fund (BSIF)** — **"manages $200,000 of the university's endowment funds,
  strategically investing in stocks and passive vehicles every semester."** Faculty advisor **Sunghan Bae,
  sbae@truman.edu**. This is the single highest-fit student group confirmed anywhere in Missouri: real money,
  a real mandate, a named stable advisor.
- **Society of Actuaries at Truman State (SATSU)** — advisor **Steven Smith, sjsmith@truman.edu**;
  site satsu.truman.edu
- **Beta Alpha Psi** — "Accounting and Business fraternity aimed at helping members develop their professional
  skillset" — advisor **Liz Diers, lizdiers@truman.edu**
- **Association for Computing Machinery (ACM)** — advisor **Kafi Rahman, kafi@truman.edu**
- **Google Developer Group (GDG)** — advisor **Nazmul Shahadat, nshahadat@truman.edu**
- **Community of College Entrepreneurs (CCE)** — advisor **Yung-hwal Park, yhpark@truman.edu**
- **No blockchain, crypto, bitcoin or Web3 organisation is listed.**

⚠ The directory also publishes **student officer names and emails**. They are real and were read from a live
page, but **rosters rotate every year and this data will be stale by September.** Use the faculty advisors —
they are staff and stable. No phone number is published for any advisor or for any club.

### E. Phone numbers

| Office | Number | Controls |
|---|---|---|
| **Union & Involvement Services**, Student Union Building Rm 2000 | **(660) 785-4222** · orgs@truman.edu | Orgs, the SUB, any fair. The one number that matters at Truman. |
| Truman State University main line / Registrar | (660) 785-4000 (MAIN LINE) | Operator; the registrar page gives only this |

### F. Courses — not retrieved.
### G. Events — not retrieved.

---

# 9. SOUTHEAST MISSOURI STATE UNIVERSITY (SEMO) — Cape Girardeau, MO — Public — Tier C — **access 3 PROVISIONAL**

### A. Academic calendar — Fall 2026 (SEMESTERS, with concurrent **eight-week sessions**)
- **First day of classes: Mon Aug 24, 2026.**
- Full-semester courses: **add by Fri Aug 28; drop by Fri Nov 20.**
- First Eight-Week session: **add by Wed Aug 26; drop by Fri Sep 25.** (A Second Eight-Week session runs
  concurrently.)
- **Fall break: Thu–Fri Oct 8–9, 2026.** Thanksgiving: **Wed–Fri Nov 25–27, 2026.**
- **Final exams: Mon–Fri Dec 14–18, 2026.** SEMO is among the last three campuses in the state still in
  session in December, alongside Mizzou and UMSL.
https://semo.edu/student-support/academic-support/registrar/academic-calendar

### B. Involvement fair — not published on any retrievable page. UNVERIFIED — (573) 651-2280.

### C. Solicitation / outside-vendor policy — **⚠ NOT RETRIEVED**
SEMO's Campus Life page **explicitly references an "Expression Policy" handbook link related to exchange of
ideas on campus** — so the document exists — but it could not be reached. `semo.edu/policies/` and
`semo.edu/policies/index.html` **404**; `semo.edu/campus-life/student-conduct/student-handbook.html` and
`/student-conduct/index.html` **404**; `semo.edu/campus-life/university-center/index.html` and
`/campus-life/event-services/index.html` **404**; `semo.edu/pdf/…` is **ROBOTS-BLOCKED**; and the site search
(`semo.edu/search/`) is **JavaScript-rendered** and returns nothing to tooling.

Rated **3, PROVISIONAL**, with the gap named. SEMO is public and bound by § 173.1550 — noncommercial only.
**Ask specifically for the Expression Policy by name; Campus Life knows what it is.**

### D. Clubs
"More than 275 social and special interest organizations." The directory is **Engage SEMO at
`semo.presence.io`** — the same Presence platform that is JavaScript-rendered at Missouri State. **Not
enumerated.** https://semo.edu/life-at-semo/student-life/student-orgs/index

### E. Phone numbers

| Office | Number | Controls |
|---|---|---|
| **Campus Life & Event Services**, University Center Rm 414 | **(573) 651-2280** · campuslife@semo.edu · campredhawk@semo.edu | Orgs, events, space — **and the Expression Policy**. One office covers everything at SEMO. |
| Office of the Registrar, Academic Hall 057 | (573) 651-2250 | Calendar |
| SEMO main line | (573) 651-2000 (MAIN LINE) | Operator |

### F. Courses — not retrieved.
### G. Events — not retrieved.

---

# CROSS-CAMPUS SUMMARY — MISSOURI

## 1. Fall 2026 term starts at a glance — ALL NINE ARE SEMESTER SCHOOLS

| Campus | First day | Last class | Finals | Fall break | Notes |
|---|---|---|---|---|---|
| **Saint Louis University** | **Wed Aug 19** ⚠ earliest | Fri Dec 4 | Dec 7–11 | Oct 22–23 | Only midweek start |
| **Missouri State** | **Mon Aug 17** | **Thu Dec 3** ⚠ finishes first | Dec 5–10 | Oct 8–11 | Thanksgiving Nov 21–29 |
| **Truman State** | **Mon Aug 17** | Fri Dec 4 | Dec 7–11 | Oct 8–9 | ⚠ block courses end Oct 6 |
| **Mizzou** | Mon Aug 24 | Thu Dec 10 | Dec 14–18 | **⚠ NONE** | 13 uninterrupted weeks Aug 24–Nov 21 |
| **WashU** | Mon Aug 24 | Mon Dec 7 | Dec 10–16 | Oct 3–6 | Reading days Dec 8–9 |
| **Missouri S&T** | Mon Aug 24 | Fri Dec 11 | Dec 14–18 | Oct 8–12 | ⚠ 9-day Thanksgiving Nov 22–30 |
| **UMSL** | Mon Aug 24 | Sat Dec 12 | Dec 14–19 | Oct 8–12 | Thanksgiving Nov 21–30 |
| **SEMO** | Mon Aug 24 | — | Dec 14–18 | Oct 8–9 | 8-week sessions run concurrently |
| **UMKC** | **⚠ UNVERIFIED** | — | — | — | Registrar calendar page returns an EMPTY BODY |

No quarter school, no trimester, no true block school. The whole state is inside a one-week start band, which
means there is no five-week quarter-school tail to plan around — an unusually simple calendar picture. The two
things that actually reshape the trip are **Mizzou's absence of a fall break** (the longest clean run in the
state) and **the Oct 8–12 fall-break cluster**, when five campuses go dark in the same week.

## 2. Outside-entity access, most to least open

1. **Mizzou — 5.** The only campus in Missouri with a **published for-profit rate**: $600 (+5% card fee) for a
   for-profit at the Sep 17 Business & Accountancy Career Fair. Separately, BPPM 6:053 states outright that
   "Non-University Groups will be allowed to request a reservation to sell on campus," capped at five days a
   semester, three vendors a day, 10 a.m.–2 p.m., fifteen business days ahead. Two independent doors.
2. **Truman State — 3.** Board Chapter 12: "Other persons and groups may use University facilities on a space
   available basis" with "possible rental fees." **No solicitation or commercial ban was found anywhere in the
   Code.** The most permissively *worded* public policy in the set — but no rate, form or procedure is
   published, so it is unproven.
3. **UMSL — 3.** CRR 110.010 route: Chancellor's written authorisation plus a Chancellor-approved fee. The
   outdoor forum is genuinely open to the public but commercial solicitation is expressly carved out.
4. **UMKC — 3.** Same CRR route; **no campus procedure of any kind could be retrieved**, so the gate exists but
   nobody has published how to pass it.
5. **Saint Louis University — 3 PROVISIONAL.** Policy not retrieved. Private and Jesuit; no public-forum
   obligation; § 173.1550 does not apply.
6. **Missouri State — 3 PROVISIONAL.** Policy not retrieved (redirect loop + DNS failure + JS search).
7. **SEMO — 3 PROVISIONAL.** An "Expression Policy" is referenced by name but every route to it 404s or is
   robots-blocked.
8. **Missouri S&T — 2.** A commercial table tier is published, but **"Credit card, telephone card, or other
   financial services vendors are not allowed at the Havener Center or on the Missouri S&T campus,"** direct
   solicitation of money is banned outright, and an explicit **anti-fronting** rule closes the club workaround.
   The best technical audience in Missouri behind the worst-fitting sentence in Missouri.
9. **WashU — 2.** "External individuals and organizations not affiliated with the university are not permitted
   to reserve university space during the academic year from August 1-May 31," plus a flat ban on non-employees
   "offering to sell merchandise or services." One narrow door: co-sponsorship by a recognised student
   organisation or department, 30 days ahead, at 50% of unpublished external rates.

## 3. Every confirmed phone number

| Campus | Office / person | Number | Controls |
|---|---|---|---|
| Mizzou | MU Reservations & Events (main) | (573) 884-8793 | The vendor reservation |
| Mizzou | Kate Fleming, Director | (573) 884-8793 | Escalation |
| Mizzou | Sam Cohen, Reservations Coordinator | (573) 882-0960 | Books the table |
| Mizzou | Lauren Northern, Reservations Coordinator | (573) 884-8818 | Books the table |
| Mizzou | Rachel Allen, Sr Event Support Specialist | (573) 884-1504 | Event support |
| Mizzou | John Cattanach, Assoc. Dir. – Theaters | (573) 882-5998 | Venues |
| Mizzou | Emily Stoker, Sr Event Coordinator | (573) 882-2155 | Student-development events |
| Mizzou | Josh Ramsey, EMS system admin | (573) 882-8935 | Booking system |
| Mizzou | Division of Finance & Business Services | (573) 882-2094 | **Authorises sales/solicitation (BPPM 6:053)** |
| Mizzou | Strategic Communications | (573) 882-4523 | Advertising |
| Mizzou | Missouri Student Unions admin | (573) 882-6310 | Non-university reservations |
| Mizzou | Student Center Information Desk | (573) 882-1174 | Building |
| Mizzou | Get Involved / Student Activities & Engagement | (573) 882-3780 | **The Involvement Fair; confirms the year** |
| Mizzou | Division of Student Affairs | (573) 882-0157 | RSO approvals |
| Mizzou | Dr. Michelle Froese, Dean of Students | (573) 882-5397 | Escalation |
| Mizzou | Business Career Services | (573) 882-2565 | **The $600 for-profit slot, Sep 17** |
| Mizzou | MU Career Center | (573) 882-6801 | The other four Fall 2026 fairs |
| Mizzou | Campus Facilities | (573) 882-3094 | Tent stakes, utilities |
| Mizzou | Sound amplification, 304 Jesse Hall | (573) 882-7255 | Amplified sound |
| WashU | Event Management (main) | (314) 935-3443 | Every reservation |
| WashU | Indra Russell, Event Manager | (314) 935-8264 | **External events — the named human** |
| WashU | Office of Campus Life | (314) 935-3443 | Student orgs, Activities Fair |
| Missouri S&T | Events & Hospitality Management | (573) 341-4399 | **Writes the financial-services ban; sets table pricing** |
| Missouri S&T | Havener Center reservations | (573) 341-4564 | Reservations desk |
| Missouri S&T | Student Involvement | (573) 341-4025 | Orgs, MinerLink |
| Missouri S&T | Student Involvement (second number) | (573) 341-6771 | Same office |
| Missouri S&T | Career Opportunities & Employer Relations | (573) 341-4343 | **The Sep 22 career fair — the real door** |
| Missouri S&T | Computer Science department | (573) 341-4492 | Courses, faculty |
| Missouri S&T | Office of the Registrar | (573) 341-4181 | Calendar |
| Missouri S&T | Dining Services | (573) 341-7019 | Food |
| Missouri S&T | Missouri S&T main line | (800) 522-0938 (MAIN LINE) | Operator |
| SLU | Student Involvement Center, BSC 319 | (314) 977-2805 | Orgs; **ask for the solicitation policy** |
| SLU | Busch Student Center Information Desk | (314) 977-2820 | **Space reservations and tabling** |
| SLU | Office of the University Registrar | (314) 977-2269 | Calendar |
| SLU | Classroom Scheduling | (314) 977-3017 | Rooms |
| Missouri State | University main line | (417) 836-5000 (MAIN LINE) | **The only confirmed MSU number** |
| UMKC | Office of Student Involvement | (816) 235-1407 | Orgs, any fair |
| UMKC | Student Union | (816) 235-5555 | Building; routes reservations |
| UMKC | Division of Student Affairs | (816) 235-1141 | Escalation |
| UMKC | Office of the Registrar | (816) 235-1125 | **The missing Fall 2026 calendar** |
| UMKC | UMKC main line | (816) 235-1000 (MAIN LINE) | Operator |
| UMSL | Office of Student Involvement | (314) 516-5291 | Orgs, Weeks of Welcome |
| UMSL | Office of Registration | (314) 516-5545 | Calendar |
| UMSL | UMSL main line | (314) 516-5000 (MAIN LINE) | Operator |
| Truman State | Union & Involvement Services, SUB 2000 | (660) 785-4222 | **Orgs, the SUB, any fair** |
| Truman State | Truman main line / Registrar | (660) 785-4000 (MAIN LINE) | Operator |
| SEMO | Campus Life & Event Services, UC 414 | (573) 651-2280 | **Orgs, events, space, the Expression Policy** |
| SEMO | Office of the Registrar | (573) 651-2250 | Calendar |
| SEMO | SEMO main line | (573) 651-2000 (MAIN LINE) | Operator |

**48 numbers across nine campuses.** Weakest coverage: Missouri State (one switchboard number and nothing
else) and UMKC (no reservations number at all).

## 4. The state campus free-speech statute
**RSMo § 173.1550, the Campus Free Expression Act, effective 28 August 2015 (S.B. 93, 2015).** It deems the
outdoor areas of public campuses traditional public forums and creates a private right of action with a $500
floor plus $50 per day. **But § 173.1550(3) protects only NONCOMMERCIAL expressive activity.** DGD's tabling is
commercial. The statute is a tool for student allies and a reason campuses cannot banish outdoor speech — it is
**not** a right to table, and it does not defeat a single fee or approval requirement in this packet. It binds
the seven public campuses and **does not reach WashU or SLU**, both private.
https://revisor.mo.gov/main/OneSection.aspx?section=173.1550

## 5. Gaps to close by phone

1. **⚠⚠ UMKC's entire Fall 2026 calendar.** The registrar page returns an empty body. (816) 235-1125.
2. **⚠⚠ Mizzou's vendor table rate.** BPPM 6:053 grants the right to request; no dollar figure exists on any
   page. (573) 884-8793 / (573) 882-2094.
3. **⚠⚠ Whether Missouri S&T reads a crypto protocol as an "other financial services vendor."** The whole
   campus turns on this one sentence. (573) 341-4399.
4. **⚠ The Mizzou Involvement Week year.** The page prints no year; weekday analysis says Fall 2026.
   (573) 882-3780.
5. **⚠ SLU's solicitation/facility-use policy** — not retrievable. (314) 977-2805 / (314) 977-2820.
6. **⚠ Missouri State's policy library** — redirect loop + DNS failure + JS-only search. (417) 836-5000.
7. **⚠ SEMO's "Expression Policy"** — referenced by name, every route 404s or is robots-blocked.
   (573) 651-2280.
8. **⚠ WashU's external rate card** — the rates page is an IMAGE. (314) 935-3443 / (314) 935-8264.
9. **⚠ Truman's rental rate and procedure under Chapter 12.010** — "possible rental fees" with no schedule.
   (660) 785-4222.
10. TigerHacks Fall 2026 dates and current tier prices (the prospectus is the 2024 edition).
    muengrtigerhacks@umsystem.edu.
11. Missouri S&T career fair employer registration cost — not published. (573) 341-4343.
12. Mizzou career fair registration deadlines — none published for any of the five. (573) 882-2565.
13. Six of nine org directories are JavaScript-rendered and could not be enumerated: MU Engage (also returned
    HTTP 504), WUGO, MinerLink, SLU Groups, Missouri State Presence, Engage SEMO. **No blockchain club was
    confirmed anywhere in Missouri, and no blockchain club was ruled out anywhere either.**
14. **No faculty member working on blockchain, cryptocurrency, digital assets or fintech was confirmed at any
    of the nine campuses.** Two faculty directories (Olin, and Mizzou's finance course list) were
    JS-rendered or 404. This is the largest single hole in the packet: Missouri has no confirmed academic door,
    whereas the academic door is the cheapest route past every commercial rule above.
