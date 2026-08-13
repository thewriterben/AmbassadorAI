"""Texas — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL loaded during research (Aug 2026).
Empty string or "UNVERIFIED" means not published / not reachable at time of research
— a gap to close by phone, NOT a finding of absence.

⚠ COVERAGE WARNING: the WebSearch budget for this research session ran out partway
through campus 6 (UT Dallas). Campuses 1–5 and 7–12 have good policy/calendar/phone
coverage. Sections F (courses), G (events) and most faculty rows are thin or missing
for the later campuses and are marked UNVERIFIED in-field. Read `gaps` on every record.

STATE-LEVEL FINDING (repeated into policy_key of all 9 public campuses, because there
is no state-level field): Tex. Educ. Code §51.9315 (SB 18, 2019) makes common outdoor
areas traditional public forums but EXPRESSLY EXCLUDES COMMERCIAL SPEECH from the
definition of "expressive activities". The Texas campus free-speech statute gives a
crypto project nothing.

Schema: reference/data-schema.md
"""

STATE = "Texas"

_SB18 = (
    "⚠ STATE LAW — Tex. Educ. Code §51.9315 (SB 18, 86th Leg. Ch. 568, eff. Sep 1 2019) "
    "makes common outdoor areas of public institutions traditional public forums and bans "
    "free-speech zones. IT DOES NOT HELP DGD. §51.9315(a) defines 'expressive activities' as "
    "'any speech or expressive conduct protected by the First Amendment... and includes "
    "assemblies, protests, speeches, the distribution of written material, the carrying of "
    "signs, and the circulation of petitions' — and then EXCLUDES 'COMMERCIAL SPEECH; "
    "defamation; unlawful harassment; incitement to imminent unlawful activity; obscenity; or "
    "threats to engage in unlawful activity.' §51.9315(c) extends free outdoor access only to "
    "'STUDENTS ENROLLED AT AND EMPLOYEES OF the institution'. A token/product pitch is "
    "commercial speech by an outsider — outside the statute twice over. ONE USEFUL LEVER: "
    "§51.9315(h) — when approving speakers or setting facility fees an institution may use only "
    "content-neutral and viewpoint-neutral criteria and 'MAY NOT CONSIDER ANY ANTICIPATED "
    "CONTROVERSY RELATED TO THE EVENT.' Invoke that ONLY if you are refused for being crypto; "
    "it will not defeat a straight commercial-solicitation denial. "
    "[https://law.justia.com/codes/texas/education-code/title-3/subtitle-a/chapter-51/subchapter-z/section-51-9315/] "
)

CAMPUSES = [

# ═══════════════════════════════════════════════════════════════════════════════
{
 "state": "Texas",
 "name": "University of Texas at Austin",
 "city": "Austin, TX",
 "type": "Public",
 "tier": "B — Regional (A-grade audience, access 1 — do not plan a table here)",
 "access": 1,

 "start": "Mon Aug 24, 2026",
 "adddrop": "Aug 31 (6th class day, undergrad add) · Sep 9 (12th class day, drop without permission) · Nov 18 Q-drop/withdraw/pass-fail",
 "fallbreak": "None separate — Thanksgiving week serves as the break",
 "thanksgiving": "Nov 23–28, 2026 (FULL WEEK, no classes)",
 "lastclass": "Mon Dec 7, 2026 (study days Dec 8–9)",
 "finals": "Dec 10–12 & Dec 14, 2026 · official graduation date Dec 19 (no public exercises)",
 "cal_url": "https://registrar.utexas.edu/calendars/26-27",
 "cal_status": "CONFIRMED",

 "fair": "Student Organization Fair (Dean of Students / Student Activities)",
 "fair_date": "UNVERIFIED — Fall 2026 date not published on any page reached. Recurring: a Fall and a Spring Student Organization Fair, listed on the Texas Today events calendar. Will post at https://calendar.utexas.edu/ and https://deanofstudents.utexas.edu/so/",
 "fair_outside": "⚠ NO — and not by omission. The tabling rule states 'ONLY CURRENT UT STUDENTS, FACULTY, AND STAFF MAY TABLE', and student orgs 'may not cosponsor with off-campus persons or organizations on campus.' A DGD rep cannot lawfully stand at a table on this campus.",
 "fair_cost": "",
 "fair_deadline": "Tabling requests 21 days in advance; Outdoor Event Consultation 14 days ahead",
 "fair_url": "https://deanofstudents.utexas.edu/so/student-organization-support.php",

 "policy": "UT Austin Institutional Rules, Appendix C — Chapter 13 (Speech, Expression, and Assembly) and Chapter 10 (Use of University Property, Rooms, and Spaces)",
 "policy_url": "https://catalog.utexas.edu/general-information/appendices/appendix-c/use-of-university-property-rooms-and-spaces/use-of-university-property-rooms-and-spaces.pdf",
 "policy_key": _SB18 + (
    "UT AUSTIN'S OWN RULES CLOSE THE DOOR ON THREE INDEPENDENT GROUNDS. "
    "(1) COMMERCIAL SPEECH, Sec. 13-205(1)(A) — prohibited commercial speech includes statements that "
    "'PROMOTE, OFFER, OR ADVERTISE A PRODUCT OR SERVICE FOR SALE OR LEASE' or that 'INCLUDE COMMERCIAL "
    "IDENTIFIERS LIKE LOGOS, TRADEMARKS, OR SERVICE MARKS ASSOCIATED WITH A FOR-PROFIT ENTITY', or that "
    "'request gift or donations unless it is specifically authorized under University rule or policy, or "
    "Regents' Rules.' (Personal apparel and vehicle decals are excluded.) A DGD-branded banner, flyer, "
    "shirt-on-a-table or QR code is inside this definition. "
    "(2) NO CO-SPONSORSHIP, Sec. 10-304(b) — 'Registered Student, Faculty, or Staff Organizations, "
    "individual students, faculty members, and staff members MAY NOT CO-SPONSOR ANY EVENT ON CAMPUS WITH "
    "AN OFF-CAMPUS PERSON OR ORGANIZATION.' Sec. 10-304(c) further bars depending on an off-campus entity "
    "for 'planning, staffing, or management of the event' or advertising co-sponsorship. "
    "(3) ⚠ ANTI-FRONTING, Sec. 10-304(c)(5) — organizations are prohibited from 'RESERVING A ROOM OR SPACE "
    "FOR THE PRIMARY USE OF AN OFF-CAMPUS PERSON OR ORGANIZATION.' "
    "SPONSORSHIP DOES NOT CURE THIS. The rule bans the arrangement itself, not merely unapproved presence. "
    "Sec. 13-103(5) defines 'off-campus person or organization' as 'any person, organization, or BUSINESS "
    "that is not an academic or administrative unit, a registered student, faculty, or staff organization, "
    "or a student, faculty member, or staff member.' "
    "TABLING MECHANICS (for a sponsoring RSO, not for you): no tabling on the Main Mall or the west side of "
    "Speedway at any time; indoor tabling needs building-manager approval; and 'DISTRIBUTING FOOD, USING "
    "AMPLIFIED SOUND, SELLING ITEMS, setting up equipment and/or constructing temporary exhibits are not "
    "permitted' without an outdoor space reservation and additional approval. "
    "No fee schedule, deposit, insurance limit or cancellation term appears in Chapter 10 — those live with "
    "University Unions via the Mazevo system. No language found reaching payment credentials or on-site "
    "contract signing; 'selling items' and 13-205 cover the practical case."),
 "sponsor_required": "No route exists. Sec. 10-304(c)(5) forbids a student org from reserving space for the primary use of an off-campus entity, and 10-304(b) forbids co-sponsorship outright. Courting a club here wastes the term.",

 "clubs": [
   ("⚠ Texas Blockchain",
    "The flagship undergraduate blockchain org, and the reason UT Austin still matters despite access 1. "
    "⚠ HornsLink is FULLY JAVASCRIPT-RENDERED and returned no content to automated fetch — description, "
    "contact email, officer roster and current active status are all UNVERIFIED. Open in a browser. "
    "Public socials exist: @txblockchain on Instagram and X, plus a LinkedIn company page.",
    "https://utexas.campuslabs.com/engage/organization/txblockchain"),
   ("Graduate Blockchain Society",
    "Distinct graduate-level org, referenced on the McCombs Blockchain Initiative site as having a co-president. "
    "No directory page located. UNVERIFIED.",
    "https://www.mccombs.utexas.edu/centers-initiatives/blockchain-initiative/"),
   ("(Other categories — FMA, ACM, data science, entrepreneurship, investment)",
    "NOT ENUMERATED. The HornsLink directory is JS-gated end-to-end; nothing could be read. This is a "
    "platform limitation, not evidence that the clubs do not exist.",
    "https://deanofstudents.utexas.edu/so/find-a-student-organization.php"),
   ("⚠ Officer names deliberately omitted",
    "The McCombs Blockchain Initiative page names current student leaders of Texas Blockchain and the "
    "Graduate Blockchain Society. The page carries no date stamp and rosters rotate annually, so the names "
    "are NOT reproduced here. Read them off the live page on the day you need them.",
    "https://www.mccombs.utexas.edu/centers-initiatives/blockchain-initiative/"),
 ],

 "faculty": [
   ("⚠ Student Organizations Office / Student Activities",
    "THE decision-maker for tabling approvals, org sponsorship rules and outdoor event consultations. "
    "If any door opens at UT Austin it opens here, and it opens for a club, not for you.",
    "Office of the Dean of Students",
    "studentorganizations@austin.utexas.edu · soc@austin.utexas.edu · (512) 471-3065",
    "https://deanofstudents.utexas.edu/so/student-organization-support.php"),
   ("Office of the Dean of Students",
    "Escalation above Student Activities; owns Institutional Rules Ch. 13 interpretation",
    "Dean of Students",
    "deanofstudents@austin.utexas.edu · (512) 471-5017 (MAIN LINE)",
    "https://deanofstudents.utexas.edu/contact.php"),
   ("Cesare Fracassi",
    "Associate Professor of Finance and DIRECTOR of the McCombs Blockchain Initiative. Teaches the "
    "Financial Technology course covering cryptocurrencies and blockchain regulation, and the Initiative "
    "is the hub the student clubs orbit — one relationship reaches faculty, curriculum and both clubs.",
    "Finance, McCombs School of Business",
    "Initiative line (512) 471-5921 — individual direct line NOT published",
    "https://www.mccombs.utexas.edu/centers-initiatives/blockchain-initiative/"),
   ("Mira Ganor",
    "Judge Solomon Casseb, Jr. Research Professor; Blockchain Initiative faculty advisory board. Legal/regulatory angle.",
    "School of Law",
    "no direct number published — look up here",
    "https://law.utexas.edu/faculty/"),
   ("Sriram Vishwanath",
    "Raytheon Fellowship Professor; Blockchain Initiative advisory board; co-teaches Emerging Technologies II "
    "(blockchain application development)",
    "Cockrell School of Engineering",
    "no direct number published — look up here",
    "https://www.ece.utexas.edu/people/faculty"),
   ("Jimmy Song",
    "Teaches Programming Blockchain (MS IROM) — the most explicitly crypto-native instructor on the list",
    "IROM, McCombs",
    "no direct number published — look up here",
    "https://www.mccombs.utexas.edu/centers-initiatives/blockchain-initiative/teaching/"),
   ("Laura Starks · Doug Morrice · Eric Meyer",
    "Blockchain Initiative faculty advisory board (Finance Regents' Chair; IROM Sublett Centennial Professor; "
    "Dean of the School of Information)",
    "McCombs / School of Information",
    "no direct numbers published — look up here",
    "https://www.mccombs.utexas.edu/centers-initiatives/blockchain-initiative/"),
   ("University Unions — front desk",
    "Union venues; reservations actually run through Mazevo (mymazevo.com/ssocustomer/utexas), not by phone",
    "University Unions",
    "(512) 475-6636 (MAIN LINE) · Hospitality (512) 475-6677",
    "https://universityunions.utexas.edu/visit/SSB"),
   ("SSB Building Management",
    "Student Services Building space requests",
    "University Unions",
    "ssbstaff@austin.utexas.edu · (512) 232-2890",
    "https://universityunions.utexas.edu/visit/SSB"),
 ],

 "courses": [
   ("⚠ NO COURSE CODES PUBLISHED",
    "The McCombs Blockchain Initiative teaching page lists courses by TITLE AND INSTRUCTOR ONLY — it "
    "publishes no course numbers and no term-offered information. Codes must be pulled from the Fall 2026 "
    "course schedule. Fall 2026 offering status for every course below is UNVERIFIED.",
    "https://registrar.utexas.edu/schedules/269"),
   ("Financial Technology",
    "Prof. Cesare Fracassi. Undergrad, MS Finance, MS Business Analytics, MBA. Covers 'Cryptography, "
    "Blockchain mechanics, Financial applications of blockchain (cryptocurrencies, market clearing), "
    "Blockchain ventures financing, and Blockchain regulatory environment' — the single best-fit course in Texas.",
    "https://www.mccombs.utexas.edu/centers-initiatives/blockchain-initiative/teaching/"),
   ("Programming Blockchain",
    "Jimmy Song. MS Information, Risk and Operations Management. Programming skills for blockchain.",
    "https://www.mccombs.utexas.edu/centers-initiatives/blockchain-initiative/teaching/"),
   ("Emerging Technologies II",
    "Tej Anand, Sriram Vishwanath, Karl Creder. MS IROM. 'Blockchain application development'.",
    "https://www.mccombs.utexas.edu/centers-initiatives/blockchain-initiative/teaching/"),
   ("Strategies for Networked Economy",
    "Prof. Prabhudev Konana. MBA and Undergraduate Honors. Blockchain concepts module.",
    "https://www.mccombs.utexas.edu/centers-initiatives/blockchain-initiative/teaching/"),
   ("Introduction to Information Technology Management",
    "Prof. Ashish Agarwal. Undergraduate Honors. Blockchain concepts module.",
    "https://www.mccombs.utexas.edu/centers-initiatives/blockchain-initiative/teaching/"),
   ("Intro to Data Management",
    "Prof. Abhay Samant. MS Business Analytics. Blockchain infrastructure technology needs.",
    "https://www.mccombs.utexas.edu/centers-initiatives/blockchain-initiative/teaching/"),
   ("Fintech: The Future of Finance",
    "UT Austin professional certificate delivered online via edX — not a campus course, but a warm-audience list.",
    "https://www.mccombs.utexas.edu/centers-initiatives/blockchain-initiative/"),
 ],

 "events": [
   ("⚠ HackTX — UT Austin's flagship hackathon",
    "⚠⚠ HIGHEST-VALUE UNKNOWN ON THIS CAMPUS. hacktx.com is a FULLY JAVASCRIPT-RENDERED SHELL — dates, "
    "venue, size and sponsorship contact could not be read at all. A student-run hackathon is the one route "
    "that sidesteps Chapter 10/13 entirely, so this must be opened in a browser before the Austin leg is planned.",
    "https://hacktx.com/"),
   ("BlockTalk panel series",
    "Run by the McCombs Blockchain Initiative alongside a news blog and the FinTech Research Lab. "
    "Fall 2026 schedule NOT published on the page fetched.",
    "https://www.mccombs.utexas.edu/centers-initiatives/blockchain-initiative/"),
   ("Blockchain Research Symposium",
    "Historical UT-linked symposium at brs.utlinc.org. Fall 2026 status UNVERIFIED.",
    "https://brs.utlinc.org/"),
   ("Texas Blockchain Council (off-campus, Austin)",
    "Founded 2019, 100+ member companies, runs the North American Blockchain Summit (NABS25 held 2025). "
    "⚠ Its site publishes NO university chapter list, NO student program and NO contact info — whether campus "
    "chapters exist COULD NOT BE ESTABLISHED. No Fall 2026 event announced. Austin Blockchain Collective is a "
    "second off-campus route to the same students.",
    "https://texasblockchaincouncil.org/"),
   ("(Career fairs, startup weeks, speaker series)",
    "UNVERIFIED — search budget exhausted before these were researched.",
    "https://calendar.utexas.edu/"),
 ],

 "play":
   "Do not plan a table here — plan a room and a relationship. UT Austin has the best crypto audience in "
   "Texas (Texas Blockchain, a Graduate Blockchain Society, a funded McCombs Blockchain Initiative with a "
   "named director and six blockchain-touching courses) and simultaneously the most airtight closure: "
   "Sec. 13-205(1)(A) makes any for-profit logo commercial speech, 10-304(b) bans co-sponsorship, and "
   "10-304(c)(5) is a true anti-fronting rule that specifically forbids a club from reserving space for your "
   "primary use. Courting a club to front for you is the one strategy that is expressly illegal here, so "
   "don't spend the term on it. THE SINGLE BEST DOOR: the McCombs Blockchain Initiative on (512) 471-5921 — "
   "ask for Cesare Fracassi's office, and ask about BlockTalk, not about tabling. A speaker slot in an "
   "Initiative-run panel is content, not commercial solicitation, and it reaches both student clubs and the "
   "faculty in one move. SECOND DOOR, and possibly the better one: HackTX. Student-run hackathons are private "
   "events outside campus commercial-use rules, and this is how sponsors legitimately reach UT students — but "
   "hacktx.com is a JS shell that gave up nothing, so someone must open it in a browser THIS WEEK; hackathon "
   "sponsorship tiers for a November event typically close in September. If you speak to Student Activities at "
   "(512) 471-3065, understand you are asking them to tell you no on the record.",

 "gaps": [
   "⚠ HackTX Fall 2026 dates, size and sponsorship contact — hacktx.com is fully JS-rendered and unreadable. Open in a browser. This is the most valuable single unknown at UT Austin.",
   "⚠ Texas Blockchain active status, officer contacts and meeting schedule — HornsLink is JS-gated: https://utexas.campuslabs.com/engage/organization/txblockchain",
   "Fall 2026 Student Organization Fair date — not published: https://calendar.utexas.edu/",
   "Course codes for all six McCombs blockchain courses, and whether any run Fall 2026: https://registrar.utexas.edu/schedules/269",
   "University Unions / Mazevo fee schedule, deposits, insurance limits and cancellation terms — none published in Chapter 10: (512) 475-6636",
   "Direct phone lines for Fracassi, Ganor, Vishwanath, Song — only the Initiative line (512) 471-5921 is published",
   "Career fairs, entrepreneurship weeks and business-school speaker series for Fall 2026 — not researched (search budget exhausted)",
 ],
 "note": "Do not confuse UT Austin's Institutional Rules with UT System Regents' Rules or with UTSA/UTA/UTD policy — the UT System institutions in this file have materially different local rules despite a shared parent.",
},

# ═══════════════════════════════════════════════════════════════════════════════
{
 "state": "Texas",
 "name": "Texas A&M University",
 "city": "College Station, TX",
 "type": "Public",
 "tier": "B — Regional (largest student body in the state; access 2)",
 "access": 2,

 "start": "⚠ NOT CONFIRMED — see cal_status. Anchor: Club Crawl is Sun Sep 6, and the event page says it is 'strategically scheduled later in the semester', so classes begin meaningfully before Sep 6.",
 "adddrop": "UNVERIFIED",
 "fallbreak": "UNVERIFIED",
 "thanksgiving": "UNVERIFIED",
 "lastclass": "UNVERIFIED",
 "finals": "UNVERIFIED",
 "cal_url": "https://registrar.tamu.edu/academic-calendar/fall-2026.html",
 "cal_status": "UNVERIFIED — ⚠ the registrar's Fall 2026 page is a JAVASCRIPT EVENT SHELL: the HTML contains a 'Download Semester Calendar' button and event titles but NO DATES. The catalog calendar page is a navigation stub. DO NOT ASSUME A&M MATCHES UT AUSTIN'S Aug 24. Open the page in a browser and use the download button, or call the Registrar.",

 "fair": "Club Crawl (formerly MSC Open House) — 'The Official Involvement Festival at Texas A&M'",
 "fair_date": "CONFIRMED — Sun Sep 6, 2026, 1:00–5:00 p.m.",
 "fair_outside": "⚠ NO — registration is for 'recognized student organizations' only, and the Student Organization Manual lists Club Crawl participation as a BENEFIT OF RECOGNITION. 1,300+ orgs attend. You cannot buy in; there is no vendor tier.",
 "fair_cost": "Not published on the event page or on clubcrawl.tamu.edu",
 "fair_deadline": "Not published — register via clubcrawl.tamu.edu; call (979) 845-1515",
 "fair_url": "https://getinvolved.tamu.edu/org/clubcrawl/events/22441/499876",

 "policy": "Texas A&M Student Rule 39 — 'Soliciting on Campus' (revision noted: 2026); routes to University Rule 21.99.09.M1 for the full solicitation rule",
 "policy_url": "https://student-rules.tamu.edu/rule39/",
 "policy_key": _SB18 + (
    "RULE 39 — SOLICITING ON CAMPUS (rev. 2026). "
    "39.1 DEFINITION: 'THE TERM \"SOLICIT\" IS DEFINED AS THE TAKING OF ORDERS, SALES, RENTALS OR DONATIONS.' "
    "All campus solicitation requires approval from the UNIVERSITY SALES AND SOLICITATIONS COMMITTEE through "
    "Student Activities — and 39.1 says this applies to 'recognized student organizations, university "
    "organizations, governmental agencies, AND OTHERS', so approval is required whether sponsored or not. "
    "'Door-to-door solicitation by outside organizations or companies is prohibited in the residence halls and "
    "University Apartments.' "
    "39.2 Recognized or university organizations selling ONLY to their own members need no permit. "
    "39.3 Charity/welfare drives must be sponsored by an officially recognized student organization and must "
    "obtain a permit through Student Activities. "
    "⚠ 39.4 IS THE OPERATIVE BAR: 'ONLY RECOGNIZED CAMPUS ORGANIZATIONS, STUDENTS, STAFF, AND INSTRUCTORS MAY "
    "USE UNIVERSITY FACILITIES FOR PUBLICITY. NON-UNIVERSITY AFFILIATED VENDORS MAY ADVERTISE THROUGH USE OF "
    "THE BATTALION, U.S. MAIL, OR TELECOMMUNICATIONS.' "
    "READ THAT AS AN INSTRUCTION, NOT ONLY AS A PROHIBITION. A&M affirmatively channels outside vendors into "
    "PAID ADVERTISING — the student newspaper, mail, telecom. It is the only Texas campus that names a legitimate "
    "commercial channel on the face of its rule. For DGD that is a feature: a Battalion ad buy is policy-blessed. "
    "39.5 points to University Rule 21.99.09.M1 for the full rule. "
    "⚠ GAPS IN THE RULE AS WRITTEN: Rule 39 contains NO separate definition of 'commercial solicitation', NO "
    "anti-fronting language, NO fee schedule, NO insurance requirement, NO deposit or cancellation terms, and NO "
    "language reaching payment credentials or on-site contract signing. 21.99.09.M1 — where those would live — "
    "COULD NOT BE RETRIEVED (search budget exhausted). Try rulesadmin.tamu.edu/rules/download/21.99.09.M1 before "
    "assuming any of them is absent."),
 "sponsor_required": "A recognized student organization must sponsor charity/welfare drives (39.3), and only recognized orgs/students/staff/instructors may use facilities for publicity (39.4). But ALL solicitation — by anyone, sponsored or not — needs University Sales and Solicitations Committee approval via Student Activities. Route: SOLAD, (979) 458-4371.",

 "clubs": [
   ("Texas A&M Blockchain club",
    "⚠ Existence confirmed via search index only — tamublockchain.com is ROBOTS-BLOCKED to automated fetch, so "
    "status, contacts, meeting schedule and sponsorship terms are ALL UNVERIFIED. Open in a browser.",
    "https://www.tamublockchain.com/"),
   ("Aggie Coding Club",
    "Listed on the Get Involved directory. Fit: developer audience. Status UNVERIFIED (Campus Labs Engage is JS-rendered).",
    "https://getinvolved.tamu.edu/org/aggiecodingclub"),
   ("Aggie Investment Club",
    "Listed on the Get Involved directory. Fit: finance audience. Status UNVERIFIED.",
    "https://getinvolved.tamu.edu/org/aic"),
   ("(Full directory — 1,300+ recognized orgs)",
    "NOT ENUMERATED. Get Involved is Campus Labs Engage and JS-rendered; it is browsable by tag "
    "(tag=3064, 3090, 2470, 3052, 3029 were seen but their meanings were not resolved). No officer names are "
    "reported anywhere in this record — with 1,300 orgs and annual turnover, a stale name is worse than none.",
    "https://getinvolved.tamu.edu/"),
 ],

 "faculty": [
   ("⚠ Student Organization Leadership and Development (SOLAD)",
    "Routes ALL University Sales and Solicitations Committee permits — this is the office that says yes or no to "
    "any solicitation on this campus. ⚠ This direct number appears ONLY inside the Student Organization Manual "
    "PDF (rev. June 2026); it is not on the Student Activities landing page.",
    "Student Activities",
    "solad@tamu.edu · (979) 458-4371",
    "https://studentactivities.tamu.edu/wp-content/uploads/2026/07/Student-Organization-Manual-revised-June-2026.pdf"),
   ("Club Crawl / MSC Programs",
    "Runs the Sep 6 involvement festival — 1,300+ orgs. Ask them who buys sponsorship, even though orgs-only applies to tabling.",
    "Memorial Student Center",
    "clubcrawl@tamu.edu · (979) 845-1515",
    "https://clubcrawl.tamu.edu/"),
   ("MSC scheduling office",
    "no number published — look up here (reservations portal only)",
    "Memorial Student Center",
    "",
    "https://msc.ucenter.tamu.edu/reservations"),
   ("Dean of Students",
    "no number published on any page reached — look up here",
    "Division of Student Affairs",
    "",
    "https://studentlife.tamu.edu/"),
   ("University Police Department",
    "Listed in the Student Organization Manual for crisis notification",
    "UPD",
    "(979) 845-2345",
    "https://studentactivities.tamu.edu/wp-content/uploads/2026/07/Student-Organization-Manual-revised-June-2026.pdf"),
   ("(Blockchain / fintech / digital-asset faculty)",
    "NOT CONFIRMED — no A&M faculty in this area were verified on a live page. Search budget exhausted. "
    "Start with Mays Business School Finance and the Department of Computer Science & Engineering.",
    "Mays Business School / CSE",
    "",
    "https://mays.tamu.edu/directory/"),
 ],

 "courses": [
   ("(All courses)",
    "UNVERIFIED — not researched; search budget exhausted before Section F for this campus. Check the catalog "
    "course search for FINC, ISTM and CSCE listings touching blockchain, cryptocurrency, fintech or digital money.",
    "https://catalog.tamu.edu/"),
 ],

 "events": [
   ("⚠ HowdyHack — the FALL Texas A&M hackathon",
    "⚠⚠ THE KEY UNKNOWN FOR THIS CAMPUS. TAMUhack's flagship event is TAMUhack (Jan 24–25, 2026 — already past). "
    "HowdyHack is the beginner-focused FALL hackathon, 'designed for Texas A&M students by students'. "
    "tamuhack.org/hh RETURNED AN EMPTY JAVASCRIPT SHELL — Fall 2026 dates and the sponsorship contact could not "
    "be read. Given that Rule 39.4 bars you from campus facilities, a student-run hackathon is the single "
    "cleanest legitimate route to A&M students. Open tamuhack.org in a browser.",
    "https://tamuhack.org/"),
   ("Club Crawl 2026",
    "Sun Sep 6, 2026, 1–5 p.m., MSC · Rudder · ILCB · Texas A&M Hotel. 1,300+ orgs. Orgs-only for tabling, but "
    "the campus is at maximum density that afternoon — worth being in College Station even if you cannot table.",
    "https://clubcrawl.tamu.edu/"),
   ("(Career fairs, startup weeks, speaker series)",
    "UNVERIFIED — not researched (search budget exhausted).",
    "https://calendar.tamu.edu/"),
 ],

 "play":
   "A&M is the largest audience in Texas and it tells you, in writing, exactly how to reach it: BUY AN AD. "
   "Rule 39.4 is unusual — instead of a flat ban it names the permitted channel, 'NON-UNIVERSITY AFFILIATED "
   "VENDORS MAY ADVERTISE THROUGH USE OF THE BATTALION, U.S. MAIL, OR TELECOMMUNICATIONS.' That is a "
   "policy-blessed, defensible commercial channel that costs money and no goodwill, and it is available now. "
   "Do that. THE SINGLE BEST DOOR for anything more than an ad is HowdyHack, A&M's student-run fall hackathon — "
   "private student events sit outside Rule 39 entirely — but tamuhack.org/hh is a JS shell that gave up nothing, "
   "so it must be opened in a browser immediately; fall hackathon sponsorship tiers typically close weeks ahead. "
   "⚠ TIME-CRITICAL AND UNRESOLVED: the Fall 2026 academic calendar is genuinely unknown — the registrar page is "
   "a JavaScript shell with no dates on it. The only anchor is Club Crawl on Sun Sep 6. Nothing about an A&M leg "
   "can be scheduled until someone downloads that calendar. Do not table: Club Crawl is recognized-orgs-only and "
   "all other solicitation needs University Sales and Solicitations Committee approval through SOLAD at "
   "(979) 458-4371 — a number that exists only inside a PDF handbook, and worth calling to ask what the Committee "
   "will actually entertain from an outside company before assuming the answer.",

 "gaps": [
   "⚠⚠ ENTIRE Fall 2026 academic calendar — registrar page is a JS shell with no dates. BLOCKING. https://registrar.tamu.edu/academic-calendar/fall-2026.html",
   "⚠ HowdyHack Fall 2026 dates and sponsorship contact — tamuhack.org/hh is an empty JS shell. This is the campus's best access route. https://tamuhack.org/",
   "⚠ University Rule 21.99.09.M1 — the full solicitation rule behind Student Rule 39; would contain any formal 'commercial solicitation' definition, fee schedule, insurance and deposit terms. Try https://rulesadmin.tamu.edu/rules/download/21.99.09.M1",
   "Texas A&M Blockchain club status and contacts — tamublockchain.com is robots-blocked; open in a browser",
   "Club Crawl participation cost and registration deadline — not published: (979) 845-1515",
   "Whether the University Sales and Solicitations Committee will hear an outside for-profit at all, and on what terms: SOLAD (979) 458-4371",
   "Dean of Students and MSC scheduling direct phone numbers — none published",
   "All blockchain/fintech faculty; all courses; all career fairs and speaker series — not researched (search budget exhausted)",
 ],
},

# ═══════════════════════════════════════════════════════════════════════════════
{
 "state": "Texas",
 "name": "University of Houston",
 "city": "Houston, TX",
 "type": "Public",
 "tier": "A — Named target (best genuine sponsorship route among the big publics)",
 "access": 3,

 "start": "Mon Aug 24, 2026",
 "adddrop": "Sep 2 last day to add · Sep 9 last day to drop without a grade · Nov 18 last day to withdraw with a 'W'",
 "fallbreak": "None separate — Labor Day Sep 7 only",
 "thanksgiving": "Nov 25–29, 2026",
 "lastclass": "Sat Dec 5, 2026 (Session 1 / full term ends)",
 "finals": "Dec 8–14, 2026",
 "cal_url": "https://www.uh.edu/online/sessions/fall.php",
 "cal_status": "CONFIRMED (via the Fall 2026 sessions page — ⚠ the registrar's own Fall 2026 calendar page renders interactively and returned NO dates to fetch). ⚠ UH runs SIX sessions in fall; Session 1 is the full term and the dates above are Session 1 only. 8-week and other part-of-term students are on different clocks.",

 "fair": "The Cat's Back (flagship fall involvement fair, part of Weeks of Welcome)",
 "fair_date": "UNVERIFIED — ⚠ the Get Involved event page is Campus Labs Engage and returned only 'This application requires JavaScript to be enabled.' ⚠ AND the Weeks of Welcome page at uh.edu/wow/ IS STALE — it served content describing an AUGUST 2021 t-shirt swap. Pattern: Cat's Back runs over MULTIPLE DAYS at the start of the fall semester (a 'Cat's Back 2025 – Day 1' listing exists), with a Spring Cat's Back in January. Will post at https://getinvolved.uh.edu/ and https://uh.campuslabs.com/engage/",
 "fair_outside": "UNVERIFIED for the fair itself. BUT the governing Student Centers rule is favourable: an RSO 'can sponsor external entities if they actively participate, assume all reservation responsibility, maintain direct communication with the Conference and Reservation Services office, and ensure an RSO member attends the entire event.' Ask CARS whether that extends to a Cat's Back table.",
 "fair_cost": "UNVERIFIED — RSOs are not charged for facility use unless the event involves 'fundraising, has an admission fee, or is joint programming', in which case billing is at the Fundraiser or Sponsored rate. Rate card not published.",
 "fair_deadline": "General events: 5 business days. ⚠ OUTDOOR events: 15 BUSINESS DAYS. Events booked more than six months out need a policy waiver (cars@uh.edu).",
 "fair_url": "https://getinvolved.uh.edu/event/8197700",

 "policy": "MAPP 01.05.01 — Freedom of Expression (last reviewed/revised 10/09/2025); plus the Student Centers RSO reservation rules",
 "policy_url": "https://www.uh.edu/policies/mapps/01-general-information/010501/",
 "policy_key": _SB18 + (
    "UH IS THE MOST WORKABLE LARGE PUBLIC IN TEXAS — THE DOOR IS IN THE COMMERCIAL CLAUSE ITSELF. "
    "MAPP 01.05.01: 'COMMON OUTDOOR AREAS OF THE UNIVERSITY ARE DEEMED TRADITIONAL PUBLIC FORUMS.' "
    "'NON-UNIVERSITY AFFILIATED INDIVIDUALS OR GROUPS ARE ONLY ELIGIBLE TO RESERVE LYNN EUSAN PARK (FOR A FEE).' "
    "⚠ THE OPENING — non-permitted commercial activities are defined as 'commercial use of University space by "
    "non-University affiliated individuals or groups WHERE SUCH USE IS NOT AUTHORIZED BY A WRITTEN AGREEMENT WITH "
    "THE UNIVERSITY.' Read that clause forward: commercial use IS permitted where there IS a written agreement. "
    "UH also contemplates outside co-sponsors on the face of its own form, which requires naming both the "
    "'Campus sponsoring organization name' AND 'If any, external sponsoring organization name (co-sponsor)'. "
    "⚠ RSO SPONSORSHIP IS EXPRESSLY PERMITTED (Student Centers RSO rules): RSOs cannot directly HOST non-university "
    "groups, 'HOWEVER, RSOs CAN SPONSOR EXTERNAL ENTITIES IF THEY ACTIVELY PARTICIPATE, ASSUME ALL RESERVATION "
    "RESPONSIBILITY, MAINTAIN DIRECT COMMUNICATION WITH THE CONFERENCE AND RESERVATION SERVICES OFFICE, AND ENSURE "
    "AN RSO MEMBER ATTENDS THE ENTIRE EVENT.' This is a genuine pathway, not a fig leaf — it is the exact mirror "
    "image of the UT Austin and Texas Tech bans. NO ANTI-FRONTING RULE WAS FOUND AT UH; what UH substitutes is an "
    "active-participation requirement. "
    "SIX RESERVABLE EXPRESSIVE-ACTIVITY AREAS: Lynn Eusan Park, Student Center Plaza, Student Center North Lawn, "
    "Butler Plaza, Cougar Woods Arboretum, Student Center Circle. RSO tabling spots: Student Center South (Food "
    "Court Tables, Outdoor North Tables, Indoor South Tables) and Butler Plaza. "
    "⚠ CONFLICTING DEADLINES — VERIFY BY PHONE: MAPP 01.05.01 says submit the Expressive Activity Description Form "
    "'at least SEVEN business days in advance'; the Student Centers' own freedom-of-expression page says 'at least "
    "FIVE business days in advance.' Two live UH pages disagree. RSO events need 5 business days, OUTDOOR events 15. "
    "Cancellations: written notice 2 business days prior. Non-decision rule: decisions 'will not be based on the "
    "content or viewpoint of a proposed expressive activity... or upon the expected reaction of others.' "
    "EXTERNAL CLIENT TRACK: Conference & Reservations serves 'Non-profit organizations, companies, groups or "
    "individuals requesting to reserve spaces for non-university related events'; rates described as 'economical' "
    "but NO FEE SCHEDULE IS PUBLISHED. No insurance limit, deposit or cancellation penalty published. No language "
    "found reaching payment credentials or on-site contract signing."),
 "sponsor_required": "YES and it works — an RSO may sponsor an external entity provided the RSO actively participates, owns the reservation, talks directly to CARS, and has a member present for the whole event. Alternatively pay as an external client, or reserve Lynn Eusan Park for a fee with no sponsor at all. Three routes; the RSO route is cheapest.",

 "clubs": [
   ("(Blockchain / crypto / fintech clubs)",
    "⚠ NOT CONFIRMED — NOT a finding of absence. UH has 600+ RSOs and the Get Involved directory "
    "(uh.campuslabs.com/engage) is JAVASCRIPT-RENDERED and returned nothing to automated fetch. No blockchain "
    "club was confirmed and none was ruled out. This needs a browser session before the Houston leg.",
    "https://uh.campuslabs.com/engage/"),
   ("NSM student organizations (separate list)",
    "The College of Natural Sciences & Mathematics maintains its own org list outside the Engage platform — "
    "a second place to look for a crypto/CS club.",
    "https://www.uh.edu/nsm/students/student-organizations/"),
 ],

 "faculty": [
   ("⚠ Student Centers — Conference & Reservations Services (CARS)",
    "THE number that decides the outcome at UH. Controls all tabling, the RSO-sponsors-an-external-entity route, "
    "external client bookings and policy waivers. One call resolves the 5-vs-7-business-day conflict, the "
    "unpublished external rate card, and whether an RSO can sponsor you at Cat's Back.",
    "Student Centers",
    "cars@uh.edu · (832) 842-6167",
    "https://www.uh.edu/studentcenters/reservations/"),
   ("Center for Student Involvement",
    "no direct number published — look up here. uh.edu/csi and /csi/about carry NO phone, and "
    "/csi/about/contact/ 404s. Located on the 1st floor of Student Center North. Route via the UH main line.",
    "Division of Student Affairs",
    "",
    "https://www.uh.edu/csi/"),
   ("University of Houston — general information",
    "Switchboard; use to reach CSI or Dean of Students, neither of which publishes a direct line",
    "UH",
    "(713) 743-2255 (MAIN LINE)",
    "https://www.uh.edu/"),
   ("UH Police Department",
    "Named in MAPP 01.05.01 as the contact for expressive-activity grievances and violations",
    "UHPD",
    "police@uh.edu · (713) 743-3333",
    "https://www.uh.edu/policies/mapps/01-general-information/010501/"),
   ("(Blockchain / fintech / digital-asset faculty)",
    "NOT CONFIRMED — not researched; search budget exhausted. Start with the C. T. Bauer College of Business "
    "finance faculty and the Department of Computer Science.",
    "Bauer College of Business",
    "",
    "https://www.bauer.uh.edu/faculty/"),
 ],

 "courses": [
   ("(All courses)",
    "UNVERIFIED — not researched, and ⚠ the UH course catalog at publications.uh.edu is NOT MACHINE-READABLE "
    "from here: it returned a robots.txt SSL failure (CERTIFICATE_VERIFY_FAILED). Browse it manually.",
    "https://publications.uh.edu/"),
 ],

 "events": [
   ("The Cat's Back / Weeks of Welcome",
    "Fall 2026 dates UNVERIFIED — the Engage event page is JS-gated and uh.edu/wow/ is serving 2021 content. "
    "Multi-day, at the start of the fall semester.",
    "https://getinvolved.uh.edu/event/8197700"),
   ("HackRice 16 — nearby, not UH",
    "Sep 11–13, 2026 at Rice, 4 miles away, 500+ developers, sponsorship open at officialhackrice@gmail.com. "
    "Houston-metro student populations overlap heavily; work it as one trip.",
    "https://hackrice.com/"),
   ("(UH hackathons, career fairs, Bauer entrepreneurship programming)",
    "UNVERIFIED — not researched (search budget exhausted). CougarCS is the likely hackathon host.",
    "https://www.uh.edu/calendar/"),
 ],

 "play":
   "Houston is where a sponsorship strategy actually works on a big public campus, and it is worth the trip for "
   "that reason alone. UH is the only large Texas public whose written rule says an RSO MAY sponsor an external "
   "entity — 'RSOs can sponsor external entities if they actively participate, assume all reservation "
   "responsibility... and ensure an RSO member attends the entire event' — and whose commercial-activity clause "
   "bars only commercial use 'WHERE SUCH USE IS NOT AUTHORIZED BY A WRITTEN AGREEMENT WITH THE UNIVERSITY', which "
   "is an invitation to get an agreement. No anti-fronting rule exists here. THE SINGLE BEST DOOR: Conference & "
   "Reservations Services, cars@uh.edu, (832) 842-6167. One call gets you the unpublished external rate card, "
   "resolves the live contradiction between MAPP (7 business days) and the Student Centers page (5 business days), "
   "and tells you whether an RSO can sponsor you into Cat's Back. ⚠ TIME-CRITICAL: OUTDOOR events require FIFTEEN "
   "BUSINESS DAYS' notice — three working weeks — so any outdoor activation in September must be filed by late "
   "August. Book the call before you book the flight. Two open threads to close in a browser first: the Cat's Back "
   "Fall 2026 dates (the Engage page is JS-gated and uh.edu/wow is serving 2021 content, so nobody currently knows "
   "when it is), and whether UH has a blockchain club at all among its 600+ RSOs — the directory is JS-gated, so "
   "its absence from this record means nothing. Pair the trip with HackRice on Sep 11–13, four miles away.",

 "gaps": [
   "⚠ The Cat's Back Fall 2026 dates — Engage page is JS-gated AND uh.edu/wow/ is stale (serves Aug 2021 content). https://getinvolved.uh.edu/event/8197700",
   "⚠ Deadline conflict: MAPP 01.05.01 says 7 business days, the Student Centers page says 5. Two live UH pages disagree. Resolve at (832) 842-6167.",
   "⚠ Whether any blockchain/crypto/fintech RSO exists among UH's 600+ orgs — directory is JS-rendered: https://uh.campuslabs.com/engage/",
   "External client rate card, Lynn Eusan Park fee, insurance limits, deposits and cancellation penalties — none published: cars@uh.edu · (832) 842-6167",
   "Center for Student Involvement direct phone — none published anywhere; /csi/about/contact/ 404s",
   "All blockchain/fintech faculty; all courses (publications.uh.edu is robots/SSL-blocked); UH hackathons and career fairs — not researched (search budget exhausted)",
 ],
 "note": "UH Main Campus only. Do not confuse with UH-Downtown, UH-Clear Lake or UH-Victoria — separate institutions with separate calendars and separate policies, all of which surfaced during research.",
},

# ═══════════════════════════════════════════════════════════════════════════════
{
 "state": "Texas",
 "name": "University of North Texas",
 "city": "Denton, TX",
 "type": "Public",
 "tier": "B — Regional (DFW; three fall fairs but all RSO-only)",
 "access": 2,

 "start": "Mon Aug 17, 2026 ⚠ EARLIEST START IN TEXAS (tied with UT Arlington) — a full week ahead of the Aug 24 cluster",
 "adddrop": "Aug 28 census/add-drop, full semester ('Courses dropped before this date will not appear on official transcript') · 8-week I: Aug 22 · 8-week II: Oct 17",
 "fallbreak": "⚠ NONE — no fall break appears on the Fall 2026 calendar. Labor Day Sep 7 (university closed) is the only autumn holiday before Thanksgiving.",
 "thanksgiving": "Nov 23–29, 2026 (FULL WEEK, no classes)",
 "lastclass": "Thu Dec 3, 2026 (full semester) · reading day Fri Dec 4, no classes · 8-week II runs to Dec 10",
 "finals": "Dec 7–11, 2026 (full semester) · 8-week I: Oct 9 · 8-week II: Dec 11 · commencement not specified in the PDF",
 "cal_url": "https://registrar.unt.edu/sites/default/files/fall-2026-academic-calendar.pdf",
 "cal_status": "CONFIRMED. ⚠ UNT runs parallel 8-WEEK I and 8-WEEK II sessions inside the term with materially different dates — confirm which population a given date reaches.",

 "fair": "Student Organization Fairs — ⚠ UNT runs THREE per fall, not one",
 "fair_date": "CONFIRMED — all three at Library Mall, 11:30 a.m.–1:30 p.m.: (1) Wed Aug 19, 2026 · (2) Mon Sep 14, 2026 (registration opens Aug 20) · (3) Wed Oct 14, 2026 (registration opens Sep 15)",
 "fair_outside": "⚠ NO — verbatim: 'ONLY RSOs ARE ELIGIBLE TO PARTICIPATE.' Outside and community organizations cannot participate in any of the three fairs. There is no vendor tier.",
 "fair_cost": "Not stated — the page references a 'table rental fee' reimbursement for RSOs but never gives the amount. Call (940) 565-3807.",
 "fair_deadline": "Rolling per fair; 'Sign-ups could potentially close early if all available spots fill up.' Registration opens Aug 20 for the Sep 14 fair and Sep 15 for the Oct 14 fair.",
 "fair_url": "https://studentaffairs.unt.edu/student-activities-center/programs-and-services/student-organizations/involvement-fairs.html",

 "policy": "UNT Policy 04.013 — Solicitation, Signs and Postings (eff. 08/22/1986, last revised 11/30/2020); and UNT Policy 07.006 — Free Speech and Public Assembly on Campus Grounds (eff. 08/14/2025)",
 "policy_url": "https://policy.unt.edu/sites/default/files/04.013%20Solicitation,%20Signs,%20and%20Postings.pdf",
 "policy_key": _SB18 + (
    "TWO POLICIES APPLY AND THEY POINT THE SAME WAY: THIS IS A PROCUREMENT CONVERSATION, NOT A SPEECH ONE. "
    "04.013 DEFINITION: solicitation is 'a request by an individual or group on the campus premises for a student, "
    "employee, or visitor to provide time or resources, including but not limited to selling merchandise, tickets, "
    "or services, recruiting, and DISPLAYING OR DISTRIBUTING ADVERTISEMENTS FOR COMMERCIAL OR BUSINESS PURPOSES.' "
    "⚠ 04.013 GATE: 'ONLY APPROVED CONTRACTED VENDORS, ORGANIZATIONS, AND DEPARTMENTS ARE ELIGIBLE TO SOLICIT.' "
    "And: 'OUTSIDE SALESPERSONS ARE REQUIRED TO ABIDE BY DESIGNATED UNIVERSITY AND STATE PROCEDURES FOR CONDUCTING "
    "COMMERCIAL ACTIVITIES ON STATE PROPERTY. WRITTEN PERMISSION MUST BE OBTAINED IN ADVANCE.' "
    "Registered student organizations may solicit for recruitment, promotion, donations or fundraising following "
    "'procedures outlined by the Student Activities Center'. Offices named in the policy: Associate Vice President "
    "of Auxiliary Services (AVPAS), Student Activities Center, Housing & Residence Life, Risk Management Services. "
    "07.006 (eff. 08/14/2025) SHUTS THE SPEECH ROUTE: expressive activities are 'verbal or symbolic expression of "
    "an idea, thought or opinion' and expressly '⚠ DO NOT INCLUDE COMMERCIAL SPEECH FOR PURPOSES OF THIS POLICY.' "
    "It also excludes incitement, fighting words, intimidation, threats, obscenity and unlawful harassment. "
    "⚠ AND UNT DOES NOT OPEN ALL COMMON OUTDOOR AREAS TO NON-AFFILIATES: visitors may engage in expressive activity "
    "'ONLY IN A DESIGNATED AREA OR AREAS' published by the University — narrower than the UTSA/UH approach. "
    "Reservation required 5+ business days ahead when using amplified sound, outdoor structures, or anticipating "
    "50+ people. ⚠ HARD CAP: limited to 15 TOTAL DAYS with a MAXIMUM 5 CONSECUTIVE DAYS PER FOUR-MONTH PERIOD, "
    "first-come first-served. "
    "⚠ WHAT IS ABSENT: NO anti-fronting language in either policy, NO sponsorship requirement in 07.006, NO fee "
    "schedule, NO permit-process detail, NO insurance requirement, NO deposit or cancellation terms, and NO "
    "language reaching payment credentials or on-site contract signing. Their absence is genuine in the text of "
    "these two documents but the operative procedures sit with Auxiliary Services and were not retrieved."),
 "sponsor_required": "Not sponsorship — CONTRACT. 04.013 admits 'approved contracted vendors' and requires advance WRITTEN PERMISSION for outside salespersons. The route runs through the Associate VP of Auxiliary Services and the Student Activities Center, not through a club. The three fall fairs are RSO-only regardless.",

 "clubs": [
   ("(Blockchain / crypto / fintech / finance clubs)",
    "⚠ NOT CONFIRMED — not enumerated. ⚠ AND NOTE A STALE PAGE: the Student Activities Center still links an "
    "ORGSYNC page for student organizations. OrgSync was retired industry-wide years ago, so that link is dead "
    "weight and the live directory is elsewhere. Do not use it.",
    "https://studentaffairs.unt.edu/student-activities-center/programs-and-services/student-organizations/orgsync.html"),
   ("(Directory)",
    "Start here instead of the OrgSync link.",
    "https://studentaffairs.unt.edu/student-activities-center/programs-and-services/student-organizations/index.html"),
 ],

 "faculty": [
   ("⚠ Student Activities Center",
    "Runs all three fall Student Organization Fairs and owns the RSO solicitation procedures that 04.013 points to. "
    "The first call at UNT.",
    "Division of Student Affairs",
    "student.activities@unt.edu · (940) 565-3807",
    "https://studentaffairs.unt.edu/student-activities-center/contact.html"),
   ("⚠ Laura Smith — Dean of Students",
    "Named policy contact for 07.006 Free Speech and Public Assembly. ⚠ This name and direct line were printed on "
    "the POLICY RECORD at policy.unt.edu — they appear NOWHERE on any Student Affairs contact page. Exactly the "
    "kind of number that only a policy document carries.",
    "Dean of Students",
    "laura.smith@unt.edu · (940) 565-2648",
    "https://policy.unt.edu/policy/07-006"),
   ("University Union",
    "Union space and event planning. No separate scheduling number is published — the Union lists only its main line.",
    "University Union",
    "union@unt.edu · (940) 565-3805 (MAIN LINE)",
    "https://studentaffairs.unt.edu/university-union/contact.html"),
   ("Associate Vice President of Auxiliary Services (AVPAS)",
    "no number published — look up here. Named in Policy 04.013 as an owner of the contracted-vendor route; this "
    "is who actually grants 'written permission' to an outside salesperson. Get the number from (940) 565-3807.",
    "Auxiliary Services",
    "",
    "https://policy.unt.edu/policy/04-013"),
   ("Risk Management Services",
    "no number published — look up here. Named in 04.013; would own any insurance requirement.",
    "Risk Management Services",
    "",
    "https://policy.unt.edu/policy/04-013"),
   ("(Blockchain / fintech faculty)",
    "NOT CONFIRMED — not researched; search budget exhausted. Start with the G. Brint Ryan College of Business.",
    "G. Brint Ryan College of Business",
    "",
    "https://cob.unt.edu/"),
 ],

 "courses": [
   ("(All courses)",
    "UNVERIFIED — not researched; search budget exhausted before Section F for this campus.",
    "https://catalog.unt.edu/"),
 ],

 "events": [
   ("Student Organization Fairs ×3",
    "Aug 19, Sep 14 and Oct 14, 2026 — Library Mall, 11:30 a.m.–1:30 p.m. RSO-only, but three separate high-density "
    "days on one campus is unusual and useful if a club ever sponsors you.",
    "https://studentaffairs.unt.edu/student-activities-center/programs-and-services/student-organizations/involvement-fairs.html"),
   ("Mean Green Fling",
    "Larger campus festival (a Spring counterpart, Mean Green Spring Fling, also runs). Fall 2026 date UNVERIFIED.",
    "https://calendar.unt.edu/event/mean_green_fling_69"),
   ("(Hackathons, career fairs, entrepreneurship weeks, speaker series)",
    "UNVERIFIED — not researched (search budget exhausted).",
    "https://calendar.unt.edu/"),
 ],

 "play":
   "UNT's value is timing, not access. It starts Mon Aug 17 — a full week before most of Texas — so together with "
   "UT Arlington it lets you open the tour in DFW while every other campus is still empty, and its FIRST org fair "
   "is Wed Aug 19, two days into term. But all three fall fairs are closed to you in terms: 'ONLY RSOs ARE ELIGIBLE "
   "TO PARTICIPATE.' And Policy 07.006 was rewritten in Aug 2025 to say expressive activities 'do not include "
   "commercial speech', while confining non-affiliates to Designated Areas with a hard cap of 15 days and 5 "
   "consecutive days per four months. THE SINGLE BEST DOOR is therefore not the fair and not the quad: it is "
   "Policy 04.013's contracted-vendor route — 'ONLY APPROVED CONTRACTED VENDORS, ORGANIZATIONS, AND DEPARTMENTS ARE "
   "ELIGIBLE TO SOLICIT' and outside salespersons need advance WRITTEN PERMISSION. That permission is granted by "
   "the Associate VP of Auxiliary Services, whose number is not published; get it by calling the Student Activities "
   "Center on (940) 565-3807. ⚠ TIME-CRITICAL: if UNT is to be a stop at all, that call has to happen before "
   "mid-August, because the Aug 19 fair and the Aug 17 term start are the whole advantage and a vendor contract is "
   "not a two-week process. Second, cheaper option: call Dean of Students Laura Smith directly on (940) 565-2648 — "
   "a number that exists only inside the policy record — and ask what a Designated Area actually permits before "
   "assuming the commercial carve-out ends the conversation.",

 "gaps": [
   "⚠ Associate VP of Auxiliary Services direct number — the actual grantor of written permission under 04.013; not published: (940) 565-3807",
   "⚠ Whether any blockchain/crypto/finance RSO exists — directory not enumerated, and the linked OrgSync page is dead",
   "The 'table rental fee' amount for org fairs — referenced but never stated: (940) 565-3807",
   "Which areas are UNT's published 'Designated Areas' for non-affiliate expressive activity under 07.006",
   "Fee schedule, insurance requirement, deposit and cancellation terms for a contracted vendor — absent from 04.013",
   "Mean Green Fling Fall 2026 date: https://calendar.unt.edu/",
   "All faculty; all courses; all hackathons, career fairs and speaker series — not researched (search budget exhausted)",
 ],
 "note": "UNT Denton only. UNT Dallas is a separate institution with its own registrar and calendar (untdallas.edu) and surfaced repeatedly in search — do not conflate.",
},

# ═══════════════════════════════════════════════════════════════════════════════
{
 "state": "Texas",
 "name": "Texas Tech University",
 "city": "Lubbock, TX",
 "type": "Public",
 "tier": "C — Opportunistic (access 1; the most hostile written rule in the state)",
 "access": 1,

 "start": "Mon Aug 24, 2026",
 "adddrop": "Wed Sep 9, 2026 — last day for student-initiated drop on MyTech without academic penalty",
 "fallbreak": "⚠ NONE designated. Instead: a 'Period of no examinations except for makeup exams or scheduled lab exams' runs Nov 24 – Dec 3. Labor Day Mon Sep 7 is a university holiday.",
 "thanksgiving": "Nov 25–29, 2026 (Wed–Sun; all Hospitality Services closed Nov 26–29)",
 "lastclass": "Wed Dec 2, 2026 · Dead Day (individual study day) Thu Dec 3",
 "finals": "Dec 4–9, 2026 (marked 'Tentative Final schedule') · commencement Dec 11–12",
 "cal_url": "https://www.depts.ttu.edu/officialpublications/calendar/26-27_cal_detailed.php",
 "cal_status": "CONFIRMED. ⚠ Texas Tech ALSO runs a separate TTU Online+ 8-WEEK calendar (26-27_8week_cal_detailed.php) — that population is online and unreachable by tabling; do not count it in audience estimates.",

 "fair": "Raider Welcome Student Org Fair (a Winter Raider Welcome Student Org Fair runs in January)",
 "fair_date": "UNVERIFIED — ⚠ the canonical listings are TechConnect / Campus Labs Engage event pages, which are JS-rendered. Pattern: held during Raider Welcome, the week around the start of fall classes — so roughly Aug 20–28, 2026. Will post at https://techconnect.dsa.ttu.edu/",
 "fair_outside": "UNVERIFIED for the fair specifically, but the governing rules make the answer near-certain: off-campus groups cannot independently reserve anything, and 'Outside groups are not allowed to be sponsored in the Student Union for financial gain.' Assume NO.",
 "fair_cost": "",
 "fair_deadline": "Grounds use generally: at least 10 UNIVERSITY WORKING DAYS before intended use, up to one semester in advance",
 "fair_url": "https://techconnect.dsa.ttu.edu/",

 "policy": "TTU OP 61.02 — Use of University Grounds, Facilities, and Amplification Equipment (eff. Oct 26, 2023); OP 61.44 — Freedom of Expression (a pointer only); plus Student Union reservation rules",
 "policy_url": "https://www.depts.ttu.edu/opmanual/OP61.02.php",
 "policy_key": _SB18 + (
    "TEXAS TECH HAS THE MOST EXPLICIT ANTI-FRONTING LANGUAGE IN TEXAS, AND IT CARRIES A PENALTY. "
    "OP 61.02 (eff. 10/26/2023) PRIORITY OF USE: '(1) Regular institutional programs; (2) Programs sponsored and "
    "conducted by the TTU System... academic and administrative departments...; and (3) Activities... sponsored by "
    "registered student organizations.' OUTSIDE GROUPS ARE NOT ON THE LIST. They may only attend 'public functions "
    "on Texas Tech University property that are sponsored by or affiliated with a Texas Tech University department.' "
    "⚠⚠ ANTI-FRONTING, VERBATIM: 'A DEPARTMENT OR REGISTERED STUDENT ORGANIZATION MAY NOT GAIN PERMISSION TO USE "
    "SPACE OR FACILITIES ON CAMPUS AND THEN PERMIT THE SPACE OR FACILITIES TO BE UTILIZED BY ANY OTHER PERSON, "
    "ORGANIZATION, OR OFF-CAMPUS GROUP.' PENALTY: forfeiture of facility privileges FOR UP TO ONE YEAR. "
    "⚠ AND THE STUDENT UNION RULE IS BLUNTER STILL: 'OUTSIDE GROUPS ARE NOT ALLOWED TO BE SPONSORED IN THE STUDENT "
    "UNION FOR FINANCIAL GAIN.' Student organizations 'cannot represent off-campus groups or university departments "
    "unless directly affiliated,' and must complete FINANCIAL LIABILITY FORMS clarifying their relationship with any "
    "outside entity — i.e. Tech asks the club, in writing, whether it is fronting for someone. "
    "COMMERCIAL ENDORSEMENT BAN: facilities must not appear to 'endorse any political party or cause, religious "
    "faith, or COMMERCIAL PRODUCT.' Departments also cannot 'contractually agree to rent, lease, or make available "
    "space inside any university facility' without written permission from the OUTDOOR EVENTS COORDINATING COMMITTEE. "
    "PROCESS: requests at least 10 UNIVERSITY WORKING DAYS ahead and up to a semester in advance, via "
    "www.groundsuse.ttu.edu or Student Union Room 304. RSO applications must be signed by the applicant AND by their "
    "faculty/staff advisor or department head. "
    "INSURANCE: 'Individuals, departments, and registered student organizations desiring grounds use MAY BE REQUIRED "
    "TO PROVIDE EVIDENCE OF APPROPRIATE LIABILITY INSURANCE' — limits not stated. "
    "PUBLISHED FEES: Visitors Center $200 rental (extra for before/after hours); International Cultural Center "
    "assesses 'resource encumbrance charges'; West Hall Presentation Room free; RSOs get a discount on City Bank "
    "Conference Center rooms. STUDENT UNION: free to RSOs; ⚠ CANCELLATION $15 within 48 hours (96 hours for the "
    "Ballroom, Matador Room and Allen Theatre); $25 minimum custodial charge; $50/hour for use during closed hours; "
    "bills due within 30 days or privileges revoked. Food must go through Top Tier Catering. "
    "⚠ OP 61.44 (Freedom of Expression) CARRIES NO SUBSTANTIVE TEXT — it says only that 'Expressive activities on "
    "the TTU campus are governed by Texas Tech University System Regulation 07.04.' THAT REGULATION WAS NOT "
    "RETRIEVED and is a gap."),
 "sponsor_required": "No route exists. Sponsorship is the thing that is banned: a department or RSO may not obtain space and then let an off-campus group use it (penalty up to one year), and outside groups may not be sponsored in the Student Union for financial gain at all. Do not court a club here.",

 "clubs": [
   ("(Blockchain / crypto / fintech clubs)",
    "⚠ NOT CONFIRMED — not a finding of absence. TechConnect is Campus Labs Engage and JS-rendered; nothing could "
    "be read. Student org Instagram is @ttustudentorgs.",
    "https://techconnect.dsa.ttu.edu/"),
 ],

 "faculty": [
   ("⚠ Student Union & Activities Office",
    "Books every Student Union room and enforces the 'outside groups are not allowed to be sponsored in the Student "
    "Union for financial gain' rule. ⚠ This number appears inside the student-org room reservation page, NOT on the "
    "Center for Campus Life landing page — and /centerforcampuslife/contact.php 404s.",
    "Center for Campus Life",
    "(806) 742-3636",
    "https://www.depts.ttu.edu/centerforcampuslife/Involvement/Student_Orgs/Room_Reservations.php"),
   ("Events & Instructional Space Management (EISM)",
    "Academic building space; 1–2 business days to confirm; academic programs take priority and student groups may "
    "be moved. ⚠ Number recovered from the reservation page, not from any contact page.",
    "Office of the Provost",
    "(806) 742-2102",
    "https://www.depts.ttu.edu/centerforcampuslife/Involvement/Student_Orgs/Room_Reservations.php"),
   ("Outdoor Events Coordinating Committee",
    "no number published — look up here. The body whose WRITTEN permission is required before any department can "
    "make space available, and the gate on all grounds use. Submit via groundsuse.ttu.edu or in person at Student "
    "Union Room 304.",
    "Texas Tech University",
    "",
    "https://www.groundsuse.ttu.edu"),
   ("Center for Campus Life / Student Life",
    "Student organizations and Raider Welcome",
    "Division of Student Affairs",
    "studentlife@ttu.edu · (806) 742-2977",
    "https://www.depts.ttu.edu/centerforcampuslife/"),
   ("Environmental Health & Safety",
    "Named in OP 61.02 — grounds-use safety sign-off",
    "EH&S",
    "(806) 742-3876",
    "https://www.depts.ttu.edu/opmanual/OP61.02.php"),
   ("Transportation & Parking Services",
    "Named in OP 61.02 — event parking",
    "Transportation & Parking",
    "(806) 742-7275",
    "https://www.depts.ttu.edu/opmanual/OP61.02.php"),
   ("(Blockchain / fintech faculty)",
    "NOT CONFIRMED — not researched; search budget exhausted. Start with the Rawls College of Business.",
    "Rawls College of Business",
    "",
    "https://www.depts.ttu.edu/rawlsbusiness/"),
 ],

 "courses": [
   ("(All courses)",
    "UNVERIFIED — not researched; search budget exhausted before Section F for this campus.",
    "https://catalog.ttu.edu/"),
 ],

 "events": [
   ("Raider Welcome Student Org Fair",
    "Fall 2026 date UNVERIFIED (TechConnect is JS-rendered). Pattern: the week around the start of classes, so "
    "roughly Aug 20–28, 2026.",
    "https://techconnect.dsa.ttu.edu/"),
   ("(Hackathons, career fairs, speaker series)",
    "UNVERIFIED — not researched (search budget exhausted). ⚠ Also unverified: Lubbock is a significant "
    "bitcoin-mining region and a state-legislative or industry tie to the campus is plausible, but NONE was "
    "confirmed on any live page. Treat that as unresearched, not as absent.",
    "https://www.depts.ttu.edu/"),
 ],

 "play":
   "Skip Texas Tech as a tabling stop. This is the clearest 'no' in the state and it is written down twice: "
   "OP 61.02 says 'A DEPARTMENT OR REGISTERED STUDENT ORGANIZATION MAY NOT GAIN PERMISSION TO USE SPACE OR "
   "FACILITIES ON CAMPUS AND THEN PERMIT THE SPACE OR FACILITIES TO BE UTILIZED BY ANY OTHER PERSON, ORGANIZATION, "
   "OR OFF-CAMPUS GROUP' — with forfeiture of privileges for up to a year — and the Student Union rule adds "
   "'Outside groups are not allowed to be sponsored in the Student Union for financial gain.' Off-campus groups "
   "cannot reserve anything independently; they may only attend functions a TTU department sponsors. Clubs are even "
   "made to sign financial liability forms declaring their relationship with outside entities, so the fronting "
   "route is not merely banned, it is actively screened for. Attempting it risks the club's privileges, not just "
   "yours. THE ONLY DOORS WORTH A CALL: (1) a DEPARTMENT-sponsored speaking invitation — the one lawful way an "
   "outsider appears on this campus — via Rawls College of Business or Computer Science; and (2) a student-run "
   "hackathon, if one exists, which was not researched. Lubbock is also a real bitcoin-mining region, so an "
   "industry-side Texas connection may be more productive than the campus itself; that too is unresearched. If you "
   "make one call, make it (806) 742-3636 to confirm the Student Union answer on the record, then spend the travel "
   "budget on UT Arlington or Texas State instead. 550 miles from Austin for an access-1 campus is not a trip.",

 "gaps": [
   "⚠ TTU System Regulation 07.04 — the ACTUAL expressive-activity rule. OP 61.44 is only a pointer and carries no substantive text. Not retrieved.",
   "⚠ Raider Welcome Student Org Fair Fall 2026 date — TechConnect is JS-rendered: https://techconnect.dsa.ttu.edu/",
   "Outdoor Events Coordinating Committee direct phone — none published; the gate on all grounds use: https://www.groundsuse.ttu.edu",
   "Whether any blockchain/crypto club exists on TechConnect",
   "Insurance limits — OP 61.02 says evidence 'may be required' but states no amounts",
   "Whether any TTU department would host a speaker — the one lawful route: Rawls College of Business",
   "All faculty; all courses; all hackathons and career fairs — not researched (search budget exhausted)",
   "Any Lubbock mining-industry or state-legislative tie to the campus — flagged as plausible but NOT researched and NOT confirmed",
 ],
},

# ═══════════════════════════════════════════════════════════════════════════════
{
 "state": "Texas",
 "name": "University of Texas at Dallas",
 "city": "Richardson, TX",
 "type": "Public",
 "tier": "A — Named target (for HackUTD, not for the campus)",
 "access": 2,

 "start": "Mon Aug 24, 2026 (CONFIRMED — Comet Calendar, Office of the Registrar)",
 "adddrop": "Wed Sep 9, 2026 — Census Day, full term; also the last day to drop full-term (CONFIRMED)",
 "fallbreak": "UNVERIFIED — none found on the official calendar events reached",
 "thanksgiving": "⚠ UNVERIFIED — a 'Fall 2026 University Closings: Thanksgiving Holiday' event EXISTS on the Comet Calendar but its dates were not fetched. Third-party aggregator says Nov 23–25 no classes, university closed Nov 26–29 — NOT OFFICIAL.",
 "lastclass": "⚠ UNVERIFIED — third-party aggregator says Wed Dec 9, 2026 (full term and 2nd 8-week). NOT OFFICIAL.",
 "finals": "⚠ UNVERIFIED — third-party aggregator says Dec 11–16, 2026; commencement Dec 17–21; degree conferral Dec 26. NOT OFFICIAL.",
 "cal_url": "https://calendar.utdallas.edu/event/fall-2026-classes-begin-full-term-session",
 "cal_status": "PARTIAL — ⚠ ONLY the Aug 24 start and the Sep 9 census day are officially confirmed. Everything from Thanksgiving onward comes from the third-party site acadcalendar.com and MUST be confirmed before use. The official Fall 2026 calendar is a PDF hosted on Box (utdallas.box.com/s/1cxqtl25bnuguhwz8xiaq5pjpe3a3v3w) and BOX REQUIRES JAVASCRIPT — it returned no content. Open it in a browser.",

 "fair": "Student organization involvement fair (name not confirmed) — run by Student Involvement & Engagement / the Student Organization Center",
 "fair_date": "UNVERIFIED — no fair page reached. ⚠ Both studentorgs.utdallas.edu and studentunion.utdallas.edu returned DNS/robots failures ('Name or service not known') — those hostnames may not resolve; the live paths sit under studentaffairs.utdallas.edu/units/. The org platform is Comet Connection.",
 "fair_outside": "UNVERIFIED — no policy or fair page retrieved. Do not assume either way.",
 "fair_cost": "",
 "fair_deadline": "",
 "fair_url": "https://studentaffairs.utdallas.edu/units/",

 "policy": "⚠ NOT RETRIEVED — UT Dallas policy lives in the UTDBP (UT Dallas Policy Memoranda) at policy.utdallas.edu",
 "policy_url": "https://policy.utdallas.edu/",
 "policy_key": _SB18 + (
    "⚠⚠ UT DALLAS'S OWN SOLICITATION POLICY WAS NOT RETRIEVED — SEARCH BUDGET EXHAUSTED ON THIS EXACT QUERY. "
    "THIS IS A GAP, NOT A FINDING THAT NO RESTRICTION EXISTS. The access rating of 2 above is a CONSERVATIVE "
    "PLACEHOLDER inferred from UT System peers, not a reading of UTD's text. "
    "WHAT CAN BE SAID: UTD is a UT System institution and is bound by the same Regents' Rules framework and the same "
    "SB 18 obligations as UT Austin, UTSA and UT Arlington. But those three peers have MATERIALLY DIFFERENT local "
    "rules — UT Austin bans fronting outright, UTSA bans commercial expressive activity outright, and UT Arlington "
    "SELLS sponsorship packages to outside companies. The spread across a single system is enormous, so DO NOT "
    "assume UT Austin's Chapter 10/13 text applies here, and equally do not assume UT Arlington's open storefront "
    "does. Retrieve the actual UTDBP before an ambassador relies on anything. "
    "PRACTICAL CONSEQUENCE: the HackUTD route below does not depend on this policy at all — a student-run hackathon "
    "is a private event and is how sponsors legitimately reach UTD students. Pursue that first and treat the campus "
    "policy question as unresolved."),
 "sponsor_required": "⚠ UNKNOWN — policy not retrieved. Check policy.utdallas.edu and call (972) 883-6236.",

 "clubs": [
   ("⚠ Blockchain and Cryptographic Systems",
    "A UTD Computer Science student club profiled by the CS department: blockchain development workshops, "
    "cryptocurrency trading instruction, hackathons, industry job placement. Faculty advisor named on that page is "
    "Dr. Murat Kantarcioglu. ⚠⚠ THE ARTICLE IS STALE — it directs readers to the club's profile on ORGSYNC, a "
    "platform retired years ago, and names a student president who has long since graduated. THE NAME IS "
    "DELIBERATELY NOT REPRODUCED HERE. CURRENT STATUS OF THIS CLUB IS UNKNOWN — verify on Comet Connection before "
    "relying on it. The advisor is the durable thread, not the club.",
    "https://cs.utdallas.edu/?p=7714"),
   ("(All other clubs)",
    "NOT ENUMERATED — the directory is Comet Connection and was not reached.",
    "https://studentaffairs.utdallas.edu/units/"),
 ],

 "faculty": [
   ("⚠ Dr. Murat Kantarcioglu",
    "CS Professor and DIRECTOR of the Data Security and Privacy Lab; named faculty advisor of the Blockchain and "
    "Cryptographic Systems club. He is the single confirmable blockchain-adjacent person at UTD and the only "
    "durable link to a club whose current status is unknown — one call reaches both the lab and whatever remains "
    "of the club.",
    "Computer Science",
    "no direct line published — route via the CS department, (972) 883-2974",
    "https://cs.utdallas.edu/?p=7714"),
   ("Department of Computer Science",
    "Route to Kantarcioglu and to the blockchain club advisor role",
    "Erik Jonsson School of Engineering & Computer Science",
    "(972) 883-2974",
    "https://cs.utdallas.edu/"),
   ("Division of Student Affairs",
    "⚠ Only published number for the whole division — UTD publishes NO direct line for the Student Organization "
    "Center, the Student Union, the Dean of Students or event reservations on either studentaffairs.utdallas.edu "
    "or /units/. Call this and ask to be transferred to the Student Organization Center.",
    "Student Affairs",
    "studentaffairs@utdallas.edu · (972) 883-6236 (MAIN LINE)",
    "https://studentaffairs.utdallas.edu/"),
   ("Student Organization Center / Student Involvement & Engagement",
    "no number published — look up here. Sits inside Student Involvement & Engagement, which also runs Spirit "
    "Programs, Student Government and large campus events.",
    "Student Affairs",
    "",
    "https://studentaffairs.utdallas.edu/units/"),
   ("Student Union",
    "no number published — look up here",
    "Student Affairs",
    "",
    "https://studentaffairs.utdallas.edu/units/"),
   ("Dean of Students",
    "no number published — look up here",
    "Student Affairs",
    "",
    "https://studentaffairs.utdallas.edu/units/"),
 ],

 "courses": [
   ("(All courses)",
    "UNVERIFIED — not researched; search budget exhausted. Given a Data Security and Privacy Lab and a blockchain "
    "club, CS course listings are the place to start.",
    "https://catalog.utdallas.edu/"),
 ],

 "events": [
   ("⚠⚠ HackUTD — 'North America's largest 24 hour university-run hackathon'",
    "PROSPECTIVE DATES: Nov 14–15, 2026. Location: UT Dallas, Engineering and Computer Science (ECS) West building, "
    "Richardson TX. An INDUSTRY TEAM actively solicits sponsors — 'learn how supporting HackUTD will benefit you.' "
    "⚠ The sponsorship email is obfuscated in automated renders as '[email protected]' — READ IT OFF THE LIVE PAGE. "
    "No downloadable prospectus; contact the Industry Team directly. THIS IS A STUDENT-RUN PRIVATE EVENT: it "
    "sidesteps campus commercial-use rules in a way tabling cannot, and it is the largest such pipeline in Texas.",
    "https://hackutd.co/"),
   ("(Career fairs, entrepreneurship weeks, speaker series)",
    "UNVERIFIED — not researched (search budget exhausted).",
    "https://calendar.utdallas.edu/"),
 ],

 "play":
   "Come to UTD for HackUTD and treat the campus itself as unresolved. HackUTD bills itself as North America's "
   "largest university-run 24-hour hackathon, runs Nov 14–15, 2026 at ECS West, and has a standing Industry Team "
   "whose entire job is signing sponsors — 'learn how supporting HackUTD will benefit you.' It is a student-run "
   "private event, so it does not turn on UTD's solicitation policy at all, which matters because THAT POLICY WAS "
   "NEVER RETRIEVED; the access-2 rating here is a conservative placeholder from UT System peers, not a reading of "
   "UTD's own text, and the spread across that system is enormous (UT Austin bans fronting, UTSA bans commercial "
   "speech, UT Arlington sells sponsorships). ⚠⚠ TIME-CRITICAL AND THE REASON THIS CAMPUS IS TIER A: hackathon "
   "sponsorship tiers for a mid-November event typically close in SEPTEMBER, and the sponsorship email is "
   "obfuscated in automated page renders — someone must open hackutd.co in a browser, read the real address, and "
   "write this month. THE SINGLE BEST DOOR is that email. Second door, and the better long-term one: Dr. Murat "
   "Kantarcioglu, who directs the Data Security and Privacy Lab and advised the Blockchain and Cryptographic "
   "Systems club — reach him via CS on (972) 883-2974. Note the club's own status is unknown: the only source is a "
   "CS article that still points at OrgSync, a platform dead for years. Pair UTD with UT Arlington (25 minutes away, "
   "access 5) into a single DFW leg.",

 "gaps": [
   "⚠⚠ UT Dallas solicitation / facilities-use policy — NEVER RETRIEVED (search budget exhausted on this query). The access rating is a placeholder. https://policy.utdallas.edu/ · (972) 883-6236",
   "⚠⚠ HackUTD sponsorship email — obfuscated as '[email protected]' in automated renders. Open https://hackutd.co/ in a browser. Tiers likely close in September.",
   "⚠ Official Fall 2026 calendar beyond Aug 24 and Sep 9 — the official PDF is on Box and Box requires JavaScript. Thanksgiving, last class, finals and commencement are currently THIRD-PARTY ONLY. https://utdallas.box.com/s/1cxqtl25bnuguhwz8xiaq5pjpe3a3v3w",
   "⚠ Whether the Blockchain and Cryptographic Systems club still exists — only source is a stale CS article pointing at the retired OrgSync platform. Check Comet Connection.",
   "Involvement fair name, Fall 2026 date, cost and whether outsiders may participate — no page reached; studentorgs.utdallas.edu and studentunion.utdallas.edu both DNS-fail",
   "Direct phone numbers for the Student Organization Center, Student Union, Dean of Students and event reservations — UTD publishes none; only the divisional line (972) 883-6236",
   "All courses; career fairs; speaker series — not researched (search budget exhausted)",
 ],
 "note": "UT Dallas is in Richardson, not Dallas proper, and is ~25 minutes from UT Arlington — the two are one DFW leg. Do not confuse with UNT Dallas or the University of Dallas (udallas.edu), both of which surfaced in search.",
},

# ═══════════════════════════════════════════════════════════════════════════════
{
 "state": "Texas",
 "name": "Rice University",
 "city": "Houston, TX",
 "type": "Private",
 "tier": "A — Named target (access 4 + HackRice; the cleanest access rules in the state)",
 "access": 4,

 "start": "Mon Aug 24, 2026",
 "adddrop": "Fri Sep 4, 2026",
 "fallbreak": "Midterm Recess Oct 12–13, 2026 (no scheduled classes)",
 "thanksgiving": "Nov 25–27, 2026 (Thanksgiving Recess)",
 "lastclass": "Fri Dec 4, 2026 · ⚠ STUDY DAYS Dec 5–8 (four days — unusually long)",
 "finals": "Dec 9–15, 2026",
 "cal_url": "https://registrar.rice.edu/calendars/fall-semester-2026",
 "cal_status": "CONFIRMED. ⚠ DISTINCTIVE STRUCTURE: Rice maintains a SEPARATE FALL QUADMESTER 2026 calendar running alongside the semester calendar (registrar.rice.edu/calendars/fall-quadmester-2026), plus 'Part of Term Courses [that] have different dates and deadlines'. The quadmester population — largely professional/executive programmes — is on a different clock from the undergraduates. Confirm which audience any given date reaches.",

 "fair": "Student Activities Fairs (referenced on the Student Activities page; org platform is OwlNest)",
 "fair_date": "UNVERIFIED — no Fall 2026 date, time or location published on any page reached. Close it by calling (713) 348-4097.",
 "fair_outside": "UNVERIFIED for the fair specifically. But Rice's general tabling rule is favourable and unusual: 'Internal customers: Reserve through rooms.rice.edu. EXTERNAL CUSTOMERS: EMAIL scevents@rice.edu (FEES APPLY).' External parties are contemplated by name.",
 "fair_cost": "Tabling fees for external customers exist but the amount is not published — email scevents@rice.edu",
 "fair_deadline": "",
 "fair_url": "https://studentcenter.rice.edu/student-activities",

 "policy": "Rice Student Center General Policies; Grand Hall Lobby and Ley Student Center Tables policy; General Information for External Customers",
 "policy_url": "https://studentcenter.rice.edu/facilities-events/general-policies",
 "policy_key": (
    "⚠ RICE IS PRIVATE. Tex. Educ. Code §51.9315 (SB 18) DOES NOT BIND IT, and Rice owes no First Amendment forum "
    "access to anyone. Do not cite the statute here — it will read as ignorance. Rice's rules are CONTRACT AND "
    "PROPERTY rules, and they are more transactionally OPEN than the publics: you pay, you get access. "
    "GENERAL POLICIES: 'Unauthorized Solicitation and Canvassing' is prohibited within the Student Center. "
    "⚠ ANTI-FRONTING, VERBATIM AND NARROW: 'STUDENT ORGANIZATIONS AND DEPARTMENTS MAY NOT SPONSOR EXTERNAL "
    "CUSTOMERS TO ALLOW THEM TO RECEIVE REDUCED RATES.' READ THE SCOPE CAREFULLY — Rice does NOT forbid an external "
    "entity from being present. It forbids a student org from LAUNDERING THE RATE. External customers are welcome "
    "at the external rate. This is the most honest access rule of any campus in this file. "
    "TABLING — GRAND HALL LOBBY / LEY STUDENT CENTER: both Rice groups AND external customers may reserve. "
    "Internal via rooms.rice.edu; 'EXTERNAL CUSTOMERS: EMAIL scevents@rice.edu (fees apply).' Each space includes "
    "one 3x6 table and two chairs, pre-set by staff. '⚠ NO AGGRESSIVE SOLICITATION IS PERMITTED.' Tables cannot be "
    "relocated, and 'all materials and people must remain behind the table perimeter.' ⚠ THE LEY INFORMATION TABLE "
    "IS RESTRICTED TO 'INFORMATION DISSEMINATION ONLY' — no sales, no giveaways there; ask for the GRAND HALL LOBBY "
    "tables instead. Duration limits not specified. "
    "EXTERNAL CUSTOMER VENUE TERMS (anything larger than a table): base facilities fee covers up to 6 hours "
    "including tables, chairs, setup and cleanup. Extra hours $50/hr; early opening $50; late closing $50; "
    "building-hour additions $100 each; additional cleanup $35/hr per custodian, $70 minimum. "
    "⚠⚠ MONEY TERMS: NON-REFUNDABLE DEPOSIT $500 (applied to the final invoice); hold period 5 business days; "
    "FULL PAYMENT DUE 30 DAYS BEFORE THE EVENT; non-payment cancels the reservation and restricts future access. "
    "⚠⚠ INSURANCE: outside organizations must provide liability insurance before the event at $1 MILLION PER "
    "OCCURRENCE / $2 MILLION AGGREGATE, covering bodily injury, property damage and host liquor liability. "
    "⚠⚠ CANCELLATION: events cancelled within ONE MONTH of the date incur 100% OF THE FACILITIES USE FEE. "
    "Classrooms are separately governed (registrar.rice.edu/facstaff/room-use-by-external-organizations). "
    "⚠ STALE DOCUMENT WARNING: a 'Rice Memorial Center/Ley Student Center Policies and Procedures Handbook' PDF is "
    "indexed publicly but the copy that surfaces is FY10 — DATED 2010, SIXTEEN YEARS OLD. Do not quote it as "
    "current. The live General Policies page links the current handbook. "
    "No language found reaching payment credentials or on-site contract signing."),
 "sponsor_required": "No — pay the external rate. In fact sponsorship is the ONE thing barred: a student org may not sponsor you in order to get you a reduced rate. Email scevents@rice.edu as an external customer and pay.",

 "clubs": [
   ("(Blockchain / crypto / fintech clubs)",
    "⚠ NOT CONFIRMED — not enumerated. Rice's directory is OwlNest and was not reached. Not a finding of absence.",
    "https://studentcenter.rice.edu/student-activities"),
 ],

 "faculty": [
   ("⚠ Rice Student Center / Student Activities",
    "ONE number and one purpose-built email cover everything at Rice: external tabling, external venue bookings, "
    "student organizations and the fair. scevents@rice.edu is a dedicated EXTERNAL-CUSTOMER address — the clearest "
    "signal in this file that outside parties are routine business here. Easiest campus in Texas to actually reach.",
    "Rice Student Center",
    "studentcenter@rice.edu (general) · scevents@rice.edu (EXTERNAL CUSTOMERS) · studentactivities@rice.edu · (713) 348-4097",
    "https://studentcenter.rice.edu/facilities-events/general-policies"),
   ("(Blockchain / fintech / digital-asset faculty)",
    "NOT CONFIRMED — not researched; search budget exhausted. Start with the Jones Graduate School of Business.",
    "Jones Graduate School of Business",
    "",
    "https://business.rice.edu/faculty-research"),
 ],

 "courses": [
   ("(All courses)",
    "UNVERIFIED — not researched; search budget exhausted before Section F for this campus.",
    "https://courses.rice.edu/"),
 ],

 "events": [
   ("⚠⚠ HackRice 16",
    "CONFIRMED — Sep 11–13, 2026, at the RICE STUDENT CENTER, Rice University, Houston. Sponsorship contact "
    "PUBLISHED PLAINLY: officialhackrice@gmail.com. The live pitch: 'Want to get your company in front of 500+ "
    "top-tier developers, designers, and engineers?' No formal prospectus document is linked — email to request "
    "terms. Timing: three weeks into the Rice semester and five days after A&M's Club Crawl, so it sequences "
    "naturally into a Houston/College Station swing.",
    "https://hackrice.com/"),
   ("(Career fairs, entrepreneurship weeks, speaker series)",
    "UNVERIFIED — not researched (search budget exhausted).",
    "https://events.rice.edu/"),
 ],

 "play":
   "Rice is the campus where you can simply buy a table and be entirely above board, and it is the campus where "
   "you should NOT mention SB 18 — it is private, the statute does not touch it, and citing it signals you have "
   "not read their rules. Their rules are better than the statute anyway: external customers may reserve Grand "
   "Hall Lobby tables directly, and the only anti-fronting language is narrow and honest — 'STUDENT ORGANIZATIONS "
   "AND DEPARTMENTS MAY NOT SPONSOR EXTERNAL CUSTOMERS TO ALLOW THEM TO RECEIVE REDUCED RATES' — which bars rate "
   "laundering, not presence. Two operational notes that will save an embarrassment: ask for the GRAND HALL LOBBY "
   "tables, because the Ley Information Table is 'information dissemination only' with no sales or giveaways; and "
   "'no aggressive solicitation is permitted', with all materials and people required to stay behind the table "
   "perimeter. ⚠⚠ THE SINGLE BEST DOOR IS NOT THE TABLE — IT IS HACKRICE 16, Sep 11–13, 2026, held in the Rice "
   "Student Center itself, 500+ developers, sponsorship contact published in the clear at "
   "officialhackrice@gmail.com. That is the most valuable confirmed date in this entire file and it is FOUR WEEKS "
   "OUT; email this week, because hackathon tiers close well before the event and no prospectus is posted, so "
   "terms have to be negotiated by hand. Then call (713) 348-4097 — one number covers external tabling, the fair "
   "and student activities — and get the unpublished external tabling fee. ⚠ IF YOU BOOK A VENUE rather than a "
   "table, budget properly: $500 non-refundable deposit, full payment 30 days ahead, $1M/$2M liability insurance, "
   "and 100% of the fee forfeited on cancellation inside one month.",

 "gaps": [
   "⚠⚠ HackRice 16 sponsorship tiers and pricing — no prospectus published; email officialhackrice@gmail.com. Event is Sep 11–13, 2026.",
   "⚠ External tabling fee for Grand Hall Lobby — 'fees apply' but no amount published: scevents@rice.edu · (713) 348-4097",
   "Student Activities Fair Fall 2026 date, time and location — not published: (713) 348-4097",
   "Whether any blockchain/crypto club exists — OwlNest directory not reached",
   "Table duration limits — not specified in the tabling policy",
   "Rice's specific insurance CERTIFICATE requirements beyond the $1M/$2M limits",
   "All faculty; all courses; career fairs and speaker series — not researched (search budget exhausted)",
   "The CURRENT Student Center policies handbook — the publicly indexed copy is FY10 (2010) and must not be quoted",
 ],
 "note": "PRIVATE — no public-forum obligation, and SB 18 does not apply. Rice is 4 miles from the University of Houston; work Houston as one trip, and note HackRice (Sep 11–13) sits five days after Texas A&M's Club Crawl (Sep 6).",
},

# ═══════════════════════════════════════════════════════════════════════════════
{
 "state": "Texas",
 "name": "Texas State University",
 "city": "San Marcos, TX",
 "type": "Public",
 "tier": "A — Named target (the most permissive sponsorship rule of any Texas public)",
 "access": 3,

 "start": "Wed Aug 19, 2026 ⚠ EARLY START — five days ahead of the Aug 24 cluster",
 "adddrop": "Census (full term) Thu Sep 3, 2026",
 "fallbreak": "UNVERIFIED — none listed on the One Stop key dates page. Labor Day Mon Sep 7 (no classes).",
 "thanksgiving": "From Wed Nov 25, 2026 (no classes)",
 "lastclass": "Wed Dec 2, 2026",
 "finals": "Begin Thu Dec 3, 2026",
 "cal_url": "https://onestop.txst.edu/important-dates.html",
 "cal_status": "CONFIRMED via TXST One Stop, which explicitly displays Fall 2026. ⚠⚠ DO NOT USE THE REGISTRAR PAGE: registrar.txst.edu/registration/ac/academic-calendar.html SERVED FALL 2025 DATES when fetched (classes begin Aug 25 2025, census Sep 10 2025, Thanksgiving Nov 26–30 2025, commencement Dec 12–13 2025). It is stale. ⚠ TXST also runs multiple session types (16-week AP, full term and others) with divergent dates. Commencement Fri Dec 11, 2026.",

 "fair": "Student Involvement Fair",
 "fair_date": "⚠⚠ YEAR AMBIGUOUS — VERIFY BEFORE TRAVELLING. The page prints 'August 27th from 4:00pm - 6:00pm' WITH NO YEAR. Aug 27, 2026 is a Thursday (8 days after the Aug 19 start — plausible). Aug 27, 2025 was a Wednesday (2 days after the 2025 Aug 25 start — also plausible). Given that the registrar page on this same domain is serving stale 2025 content, DO NOT ASSUME 2026. Confirm on (512) 245-3219.",
 "fair_outside": "UNVERIFIED for the fair itself — the description is framed around RSOs recruiting members and does not address outside organizations. BUT the governing solicitation policy expressly permits a department or student organization to sponsor an outside vendor, so ask rather than assume.",
 "fair_cost": "Not stated on the page",
 "fair_deadline": "Registration link exists; no deadline stated. ⚠ Separately, solicitation requests need 10 UNIVERSITY BUSINESS DAYS.",
 "fair_url": "https://studentinvolvement.txst.edu/involvement/student-orgs/involvementfair.html",

 "policy": "UPPS No. 07.04.03 — Solicitation on University Property (eff. 8/01/2025, next review 12/01/2030); companion UPPS 07.04.01 — Expressive Activities",
 "policy_url": "https://policies.txst.edu/university-policies/07-04-03.html",
 "policy_key": _SB18 + (
    "⚠⚠ TEXAS STATE IS THE INVERSE OF EVERY OTHER TEXAS PUBLIC: IT EXPRESSLY PERMITS WHAT UT AUSTIN AND TEXAS TECH "
    "EXPRESSLY BAN. THIS IS THE MOST IMPORTANT POLICY FINDING IN THE STATE FOR AN OUTSIDE VENDOR. "
    "UPPS 07.04.03 (eff. 8/01/2025). DEFINITION, per TSUS regulation: solicitation encompasses 'the sale or offer "
    "for sale of any property, goods, products or services' or 'the receipt of or request for any gift or "
    "contribution.' ⚠ NOTABLY GENEROUS FRAMING: the policy addresses COMMERCIAL SPEECH separately, describing it as "
    "'advertisement and promotion of products or services' that RECEIVES FIRST AMENDMENT PROTECTION IN TRADITIONAL "
    "AND DESIGNATED PUBLIC FORUMS — the opposite of UTSA's flat prohibition on for-profit expressive activity. "
    "⚠⚠ THE OPERATIVE PROVISION: 'A TEXAS STATE DEPARTMENT OR STUDENT ORGANIZATION MAY SPONSOR OUTSIDE VENDORS' if "
    "they 'complete all required forms' and the request 'MUST NOT VIOLATE EXISTING UNIVERSITY CONTRACTUAL "
    "RELATIONSHIPS.' The condition: the sponsoring organization 'SHALL BE PHYSICALLY PRESENT WITH THE VENDOR WHILE "
    "THEY ARE ON CAMPUS.' "
    "THIS IS NOT AN ANTI-FRONTING RULE — IT IS THE OPPOSITE. Texas State does not forbid the arrangement; it "
    "conditions it on physical co-presence and on not colliding with an existing exclusive contract. Sponsorship "
    "genuinely cures the problem here. "
    "⚠ THE ONE REAL TRAP is the contractual-relationships clause: ASK WHETHER TXST HAS AN EXCLUSIVE "
    "BANKING/FINANCIAL-SERVICES VENDOR AGREEMENT before investing in this route. That clause, not the speech rules, "
    "is what could kill a crypto vendor. "
    "PROCESS: submit a SOLICITATION REQUEST FORM AT LEAST 10 UNIVERSITY BUSINESS DAYS before the first day of "
    "scheduled solicitation. ⚠ 'AN APPROVED VENDOR IS ONLY ALLOWED TO SOLICIT ON UNIVERSITY PROPERTY FOR UP TO TWO "
    "CONSECUTIVE WEEKS.' Sponsor accountability and compliance certifications required. "
    "WHERE TO FILE: LBJ Student Center spaces (Meeting Rooms, Ballrooms, Amphitheater, Bobcat Trail, The Mall, "
    "THE QUAD) go through the MAZEVO reservation system via lbjsc.txst.edu event services. All other campus areas "
    "(Administration/Academic buildings, Sewell Park, Round Rock Quad) go through the BOBCAT ORGANIZATION HUB, "
    "where the VENDOR AGREEMENT FORM is also submitted. "
    "⚠ WHAT IS NOT PUBLISHED: NO fee schedule, NO table rental cost, NO rate card by vendor type, NO insurance "
    "requirement, NO deposit, NO cancellation terms, and NO language reaching payment credentials or on-site "
    "contract signing. All of that must be obtained by phone on (512) 245-3219."),
 "sponsor_required": "YES, and it WORKS — uniquely among Texas publics. A TXST department OR a student organization may sponsor an outside vendor, provided the sponsor is PHYSICALLY PRESENT with the vendor on campus and the request does not violate an existing university contract. File 10 university business days ahead; approved vendors get up to two consecutive weeks.",

 "clubs": [
   ("(Blockchain / crypto / fintech / finance clubs)",
    "⚠ NOT CONFIRMED — not enumerated. The directory is the Bobcat Organization Hub and was not reached. Not a "
    "finding of absence. You need a sponsoring org OR a sponsoring department, so this list matters more here than "
    "at most campuses — but note a DEPARTMENT can sponsor you too, which is often easier than a club.",
    "https://studentinvolvement.txst.edu/involvement/student-orgs.html"),
 ],

 "faculty": [
   ("⚠⚠ Operations & Assessment — Student Involvement & Engagement",
    "OWNS THE SOLICITATION AND OUTSIDE-VENDOR PROCESS. The dedicated campusaccess@txstate.edu address is the "
    "strongest signal in this entire file that a Texas public processes outside-vendor requests as routine "
    "business. THE HIGHEST-YIELD SINGLE CALL IN THE STATE FOR A COMMERCIAL ENTITY.",
    "Student Involvement & Engagement",
    "campusaccess@txstate.edu (solicitation) · getinvolved@txstate.edu (orgs) · (512) 245-3219",
    "https://studentinvolvement.txst.edu/operations-and-assessment/campus-access/solicitation.html"),
   ("LBJ Student Center — Event Services",
    "no direct number published — look up here. Handles Mazevo reservations for the Quad, The Mall, Bobcat Trail, "
    "Ballrooms and Amphitheater — i.e. all the high-traffic outdoor space. Route via (512) 245-3219.",
    "LBJ Student Center, Suite 425 & 204, 109 Student Center Drive, San Marcos TX 78666",
    "",
    "https://lbjsc.txst.edu/"),
   ("(Blockchain / fintech faculty)",
    "NOT CONFIRMED — not researched; search budget exhausted. Start with the McCoy College of Business. Note that a "
    "DEPARTMENT can sponsor an outside vendor here, so a faculty relationship is a direct route to campus access, "
    "not merely to an audience.",
    "McCoy College of Business",
    "",
    "https://www.mccoy.txst.edu/"),
 ],

 "courses": [
   ("(All courses)",
    "UNVERIFIED — not researched; search budget exhausted before Section F for this campus.",
    "https://mycatalog.txst.edu/"),
 ],

 "events": [
   ("Student Involvement Fair",
    "'August 27th, 4:00–6:00 p.m., LBJ Student Center Ballrooms' — ⚠ YEAR NOT PRINTED ON THE PAGE. See fair_date.",
    "https://studentinvolvement.txst.edu/involvement/student-orgs/involvementfair.html"),
   ("(Hackathons, career fairs, entrepreneurship weeks, speaker series)",
    "UNVERIFIED — not researched (search budget exhausted).",
    "https://www.txst.edu/news/events.html"),
 ],

 "play":
   "Make this the first call of the whole tour. Texas State is the only public university in Texas whose written "
   "policy says, in terms, that 'A TEXAS STATE DEPARTMENT OR STUDENT ORGANIZATION MAY SPONSOR OUTSIDE VENDORS' — "
   "conditioned only on the sponsor being 'PHYSICALLY PRESENT WITH THE VENDOR WHILE THEY ARE ON CAMPUS.' Where UT "
   "Austin and Texas Tech write anti-fronting bans, TXST writes a permission. It even treats commercial speech as "
   "protected in public forums rather than carved out. And it maintains a dedicated address, "
   "campusaccess@txstate.edu, for exactly this. THE SINGLE BEST DOOR: (512) 245-3219, Operations & Assessment, "
   "Student Involvement & Engagement. Ask three things on that one call — the unpublished vendor fee and table "
   "rate; whether any EXISTING UNIVERSITY CONTRACTUAL RELATIONSHIP (a banking or financial-services exclusive) "
   "would block a crypto vendor, which is the one clause that can actually kill this route; and whether the "
   "Involvement Fair is Aug 27 in 2026 or whether that page is stale like the registrar's. ⚠⚠ TIME-CRITICAL: "
   "solicitation requests need TEN UNIVERSITY BUSINESS DAYS — two working weeks — and TXST starts early on Wed "
   "Aug 19, so a September activation must be filed in late August. An approved vendor gets up to TWO CONSECUTIVE "
   "WEEKS on campus, which is the longest sanctioned run available anywhere in this file. Note also that a "
   "DEPARTMENT can sponsor you, not just a club — often a faster path, and worth trying McCoy College of Business "
   "if no student org fits.",

 "gaps": [
   "⚠⚠ Whether an EXISTING UNIVERSITY CONTRACTUAL RELATIONSHIP (banking/financial-services exclusive) blocks a crypto vendor — the one clause that could kill this route: campusaccess@txstate.edu · (512) 245-3219",
   "⚠⚠ Vendor fees, table rental cost and rate card by vendor type — NONE published in the policy or on the solicitation page: (512) 245-3219",
   "⚠ Student Involvement Fair YEAR — the page prints 'August 27th' with no year, on a domain whose registrar page is serving stale 2025 dates: (512) 245-3219",
   "Insurance requirements, deposits and cancellation terms — absent from UPPS 07.04.03",
   "UPPS 07.04.01 (Expressive Activities) — the companion policy; not fetched: https://policies.txst.edu/university-policies/07-04-01.html",
   "Whether any blockchain/crypto/finance RSO exists — Bobcat Organization Hub not reached",
   "LBJ Student Center Event Services direct number",
   "All faculty; all courses; all events — not researched (search budget exhausted)",
 ],
 "note": "⚠ The registrar's own academic calendar page serves FALL 2025 dates. Use onestop.txst.edu for anything date-related at this campus.",
},

# ═══════════════════════════════════════════════════════════════════════════════
{
 "state": "Texas",
 "name": "University of Texas at San Antonio",
 "city": "San Antonio, TX",
 "type": "Public",
 "tier": "C — Opportunistic (access 1; one narrow speaker carve-out)",
 "access": 1,

 "start": "Wed Aug 19, 2026 ⚠ EARLY START (late registration and add/drop open Aug 10)",
 "adddrop": "Census date and final payment deadline Thu Sep 3, 2026 (2nd 8-week term: Oct 26). Add/drop for the full term runs to Oct 23.",
 "fallbreak": "Fall Break Oct 12–13, 2026 — 'Classes do not meet'",
 "thanksgiving": "Nov 26–27, 2026 — university closed",
 "lastclass": "Thu Dec 3, 2026 (16-week) · ⚠ Student Study Day Fri Dec 4, classes do not meet · first 8-week term ends Oct 14",
 "finals": "Dec 7–11, 2026 — 'No Final Exams on Saturday or Sunday'. Commencement listed as TBD.",
 "cal_url": "https://www.utsa.edu/registrar/reg_materials/reg_calendar_fall.pdf",
 "cal_status": "CONFIRMED (registrar PDF, updated 4/17/2026). ⚠ UTSA runs parallel 8-week terms with different dates.",

 "fair": "Get Involved Fair (plus two larger campus festivals, Fiesta UTSA and BestFest)",
 "fair_date": "UNVERIFIED — the canonical listings are RowdyLink event pages (rowdylink.utsa.edu/event/7141358 and /10832645), and RowdyLink is Campus Labs Engage and JS-rendered. Pattern: the Get Involved Fair runs 'at semester start'. Will post at https://rowdylink.utsa.edu/ and https://www.utsa.edu/students/events/",
 "fair_outside": "⚠ NO. Commercial/for-profit expressive activity is prohibited outright, and student orgs may not jointly sponsor any event with an off-campus person or organization. ⚠ NOTE A SECOND RESTRICTION THAT SURPRISES PEOPLE: student organizations themselves 'will not be allowed' to table DURING Fiesta UTSA, BestFest and the Involvement Fair — UTSA reserves those windows — and tabling is barred entirely during summer Orientation.",
 "fair_cost": "",
 "fair_deadline": "Expressive-activity form: recommended at least 5 business days but no later than 48 hours prior",
 "fair_url": "https://rowdylink.utsa.edu/",

 "policy": "UTSA HOP 9.37 — Peaceful Public Assembly Policy (published Aug 29, 2025); HOP 8.06 — Special Use Facilities; Student Organization Handbook (Events & Activities on Campus)",
 "policy_url": "https://www.utsa.edu/hop/chapter9/9-37.html",
 "policy_key": _SB18 + (
    "⚠⚠ UTSA HAS THE FLATTEST COMMERCIAL BAN IN TEXAS, AND ITS OPEN-LOOKING CLAUSE IS A TRAP. READ BOTH SENTENCES. "
    "HOP 9.37 (pub. 8/29/2025) DEFINITION: 'Common Outdoor Area' means outdoor space not used for dedicated "
    "University business, educational or research functions on a permanent or temporary basis. "
    "THE OPEN-LOOKING SENTENCE: 'MEMBERS OF THE PUBLIC MAY DISTRIBUTE OR DISPLAY LITERATURE IN THE COMMON OUTSIDE "
    "AREAS. IN EITHER CASE, NO ADVANCED PERMISSION IS REQUIRED.' Members of the public may engage in expressive "
    "activities in Common Outdoor Areas subject to time, place and manner rules. "
    "⚠⚠ THE VERY NEXT RULE CLOSES IT: 'EXPRESSIVE ACTIVITIES CARRIED OUT FOR THE PURPOSE OF COMMERCIAL/FOR-PROFIT "
    "BENEFIT (COMMERCIAL SPEECH) ARE PROHIBITED.' A DGD ambassador handing out flyers looks permitted right up "
    "until the commercial-purpose test is applied, at which point it is FLATLY PROHIBITED. DO NOT READ THE 'no "
    "advanced permission is required' SENTENCE IN ISOLATION — it is the single most likely way to get an "
    "ambassador removed from a Texas campus. "
    "⚠ CO-SPONSORSHIP BAN, VERBATIM: 'NO REGISTERED STUDENT, FACULTY, OR STAFF ORGANIZATIONS... MAY JOINTLY SPONSOR "
    "ANY EVENT ON CAMPUS WITH AN OFF-CAMPUS PERSON OR ORGANIZATION.' The Student Organization Handbook extends this "
    "to any event that 'RELIES ON AN OFF-CAMPUS PERSON OR ORGANIZATION FOR PLANNING, STAFFING, FUNDING, ADVERTISING "
    "OR MANAGING THE EVENT.' "
    "⚠⚠ BUT THREE THINGS ARE EXPRESSLY *NOT* JOINT SPONSORSHIP, AND THIS IS THE ONLY VIABLE UTSA ROUTE: "
    "'INVITING GUEST SPEAKERS, PURCHASING FROM OUTSIDE VENDORS, AND RECEIVING FUNDING FROM NON-UNIVERSITY ENTITIES "
    "ARE PERMITTED WITHOUT CONSTITUTING PROHIBITED JOINT SPONSORSHIP.' A student org may therefore invite you to "
    "SPEAK, and may accept your money — it simply may not co-sponsor an event with you. "
    "PROCESS: all on-campus events must be registered and approved on ROWDYLINK, with FINAL APPROVAL BY THE DEAN OF "
    "STUDENTS. Expressive-activity form 'recommended... at least five (5) business days but no later than 48 hours "
    "prior.' FEES: 'A reasonable and nondiscriminatory fee for the additional police work will be charged for "
    "events that require additional police presence.' Orgs must check out tables/chairs from Events Management or "
    "bring their own — they may not repurpose Sombrilla or McKinney Building furniture. Catering by approved "
    "caterers only; no propane on campus. "
    "HOP 8.06 (SPECIAL USE FACILITIES, for larger venues): external users may reserve for conferences, performing "
    "arts and 'business associations aligned with institutional mission'. 'RATES MUST BE CHARGED... THAT, AT A "
    "MINIMUM, ENSURE RECOVERY OF THAT PART OF THE OPERATING COST.' Users sign a facilities usage agreement 'in "
    "accordance with the model contracts developed by the UT System Office of General Counsel.' All publicity 'must "
    "carry a disclaimer... that use of The University of Texas at San Antonio facilities does not imply "
    "endorsement.' And: 'DESIGNATION AS A SPECIAL USE FACILITY DOES NOT CONSTITUTE THE FACILITY A PUBLIC FACILITY "
    "OR FORUM that is open to use... on a first come, first served basis.' "
    "No published rate card, deposit, insurance limit or cancellation term. No language reaching payment "
    "credentials or on-site contract signing."),
 "sponsor_required": "Sponsorship is banned for events — no org may jointly sponsor with an off-campus entity, including reliance on you for funding, staffing or advertising. BUT a student org MAY invite you as a GUEST SPEAKER and MAY receive funding from you; the handbook says so expressly. That carve-out is the only route in.",

 "clubs": [
   ("(Blockchain / crypto / fintech clubs)",
    "⚠ NOT CONFIRMED — not enumerated. UTSA has 'more than 300 student organizations registered' and the directory "
    "is RowdyLink (Campus Labs Engage), which is JS-rendered and unreadable by fetch. Not a finding of absence. "
    "UTSA also offers a consultation form to meet an Involvement Specialist, which is a legitimate way to be "
    "pointed at the right org.",
    "https://www.utsa.edu/students/getinvolved/RSO/"),
 ],

 "faculty": [
   ("⚠ Student Involvement Center",
    "RSOs, RowdyLink event approvals, and the Involvement Specialist consultations. ⚠ This number was recovered "
    "from the Student Organization Handbook page — BOTH published contact pages "
    "(/getinvolved/contact.html and /getinvolved/about/contact.html) RETURN 404.",
    "Student Involvement Center",
    "getinvolved@utsa.edu · (210) 458-4160 · Mon–Thu 8a–6p, Fri 8a–5p",
    "https://www.utsa.edu/students/getinvolved/policies/handbook/events-activities-on-campus.html"),
   ("⚠ Office of Events, Conferences and Camps Services (Events Management)",
    "Controls table and chair checkout — orgs may not repurpose campus furniture — and administers HOP 8.06 Special "
    "Use Facilities for external users. ⚠ Number recovered from HOP 8.06, not from any contact page.",
    "Events, Conferences and Camps Services",
    "EMCSevents@utsa.edu · (210) 458-4155 · request form utsa.edu/calendar/request.cfm",
    "https://www.utsa.edu/hop/chapter8/8.06.html"),
   ("Dean of Students",
    "no number published — look up here. FINAL APPROVER of every registered student organization event on campus, "
    "so this is the office that would clear a guest-speaker invitation. Get the number via (210) 458-4160.",
    "Student Affairs",
    "",
    "https://www.utsa.edu/students/"),
   ("University of Texas at San Antonio — general information",
    "Switchboard; the fallback given that both Student Involvement contact pages 404",
    "UTSA",
    "webteam@utsa.edu · (210) 458-4011 (MAIN LINE) · directories: utsa.edu/about/directories/",
    "https://www.utsa.edu/about/directories/"),
   ("(Blockchain / fintech faculty)",
    "NOT CONFIRMED — not researched; search budget exhausted. Start with the Carlos Alvarez College of Business.",
    "Carlos Alvarez College of Business",
    "",
    "https://business.utsa.edu/"),
 ],

 "courses": [
   ("(All courses)",
    "UNVERIFIED — not researched; search budget exhausted before Section F for this campus.",
    "https://catalog.utsa.edu/"),
 ],

 "events": [
   ("Get Involved Fair · Fiesta UTSA · BestFest",
    "Fall 2026 dates UNVERIFIED (RowdyLink is JS-rendered). ⚠ Note orgs cannot table DURING these three events — "
    "UTSA reserves those windows for the events themselves.",
    "https://www.utsa.edu/students/events/"),
   ("(Hackathons, career fairs, speaker series)",
    "UNVERIFIED — not researched (search budget exhausted).",
    "https://www.utsa.edu/students/events/"),
 ],

 "play":
   "Do not table at UTSA, and above all do not let anyone talk themselves into the 'no advanced permission is "
   "required' sentence. HOP 9.37 does say members of the public may distribute literature in common outdoor areas "
   "with no permission — and then says 'EXPRESSIVE ACTIVITIES CARRIED OUT FOR THE PURPOSE OF COMMERCIAL/FOR-PROFIT "
   "BENEFIT (COMMERCIAL SPEECH) ARE PROHIBITED.' Reading the first sentence without the second is the single most "
   "likely way to get an ambassador removed from a Texas campus. Co-sponsorship is banned outright, extending to "
   "any reliance on an outsider for planning, staffing, funding or advertising. THE ONE REAL DOOR, and it is "
   "written down: the Student Organization Handbook states that 'inviting guest speakers, purchasing from outside "
   "vendors, and receiving funding from non-University entities' are PERMITTED and do NOT constitute prohibited "
   "joint sponsorship. So a student org may invite you to SPEAK, and may take your money — it simply may not "
   "co-sponsor an event with you. Work that: call the Student Involvement Center on (210) 458-4160, ask for an "
   "Involvement Specialist consultation to be pointed at the right org among 300+, and pitch a talk rather than a "
   "table. Every event still needs RowdyLink registration and FINAL APPROVAL BY THE DEAN OF STUDENTS, so build in "
   "time. Practical note: neither UTSA contact page works — both 404 — so the two direct numbers in this record "
   "came out of the handbook and HOP 8.06 respectively; they are the ones that will actually connect. Given "
   "access 1 and no confirmed club, treat San Antonio as a lower-priority stop than nearby Texas State (35 miles, "
   "access 3, and a policy that explicitly permits vendor sponsorship).",

 "gaps": [
   "⚠ Get Involved Fair / Fiesta UTSA / BestFest Fall 2026 dates — RowdyLink is JS-rendered: https://rowdylink.utsa.edu/",
   "⚠ Whether any blockchain/crypto club exists among UTSA's 300+ orgs — RowdyLink unreadable",
   "Dean of Students direct phone — final approver of every org event; none published: (210) 458-4160",
   "HOP 8.06 Special Use Facility rate card, deposits, insurance limits and cancellation terms — none published",
   "The 'reasonable and nondiscriminatory' police fee schedule — amount not published",
   "Whether a student org would host a guest-speaker slot, and what the Dean of Students lead time really is",
   "All faculty; all courses; all hackathons and career fairs — not researched (search budget exhausted)",
 ],
 "note": "⚠ Both UTSA Student Involvement Center contact pages return 404 (/students/getinvolved/contact.html and /students/getinvolved/about/contact.html). The working numbers in this record were extracted from policy and handbook pages instead.",
},

# ═══════════════════════════════════════════════════════════════════════════════
{
 "state": "Texas",
 "name": "Baylor University",
 "city": "Waco, TX",
 "type": "Private (religious)",
 "tier": "C — Opportunistic (access 2; discretionary Christian-mission test)",
 "access": 2,

 "start": "Mon Aug 24, 2026 (Welcome Week Aug 20–23)",
 "adddrop": "Aug 28 last day to add or register · Sep 9 last day to drop without a 'W'",
 "fallbreak": "Fall Break Fri Oct 9, 2026 (single day)",
 "thanksgiving": "Nov 23–27, 2026 (students)",
 "lastclass": "Wed Dec 9, 2026 · Study Day Thu Dec 10",
 "finals": "Dec 11–16, 2026 · Commencement Sat Dec 19, 2026",
 "cal_url": "https://calendar.web.baylor.edu/academic-calendar?calendar=351&category=936",
 "cal_status": "CONFIRMED. ⚠ The catalog PDF at catalog.baylor.edu is ROBOTS-BLOCKED (robots.txt fetch failed: HTTP 202); the calendar site rendered fine and is the source here. ⚠ The semester also contains TWO 7-WEEK SESSIONS — flag if targeting those students. Other dated events: Family Weekend Sep 19, Homecoming Nov 7.",

 "fair": "Fall student organization fair (name not confirmed — historically run during Welcome Week)",
 "fair_date": "UNVERIFIED — no Fall 2026 fair page reached. Welcome Week is Aug 20–23, 2026, so a fair, if held, falls in that window. Org platform is Baylor Connect. Will post at https://studentactivities.web.baylor.edu/",
 "fair_outside": "UNVERIFIED for the fair. But the Student Union rules bar 'outside business solicitations' in the building, and student org policy states 'Groups of students not chartered by the University may not affiliate themselves with Baylor University.' Assume NO without confirmation.",
 "fair_cost": "",
 "fair_deadline": "Student org space requests: at least 7 business days; 10 business days for events of 100+",
 "fair_url": "https://studentactivities.web.baylor.edu/",

 "policy": "Baylor 'Campus Facilities Use and Campus Solicitation Policy' (modification date on the located copy: 12-12-05); plus Bill Daniel Student Center (BDSC) Building Guidelines and Student Organization Policies",
 "policy_url": "https://studentactivities.web.baylor.edu/see-our-spaces/student-union/reservation-services/student-union-building-guidelines",
 "policy_key": (
    "⚠ BAYLOR IS PRIVATE AND RELIGIOUS. Tex. Educ. Code §51.9315 (SB 18) DOES NOT BIND IT and Baylor owes no "
    "public-forum access to anyone. Do not cite the statute here. The real gate is a discretionary MISSION test. "
    "⚠⚠ CURRENCY WARNING: the governing 'Campus Facilities Use and Campus Solicitation Policy' located during "
    "research carries a modification date of 12-12-05 — OVER TWENTY YEARS OLD — and was retrieved from FIRE's "
    "document archive, NOT from a Baylor URL. Treat its currency as uncertain and confirm with the University Host "
    "before relying on any clause below. "
    "DEFINITION: 'SOLICIT (or any derivative thereof) MEANS TO USE PERSUASION OR ENTREATY TO PROMOTE OR SELL A "
    "PRODUCT, SERVICE, OR ACTIVITY.' No separate definition of 'commercial solicitation' exists. "
    "SCOPE: applies to 'Any enrolled student, faculty member, staff member OR ANY OTHER INDIVIDUAL, CAMPUS "
    "ORGANIZATION, PARTNERSHIP, ASSOCIATION, OR CORPORATION desiring to use campus facilities' — all must comply "
    "and obtain WRITTEN PERMISSION. "
    "⚠ THE ROUTING RULE: 'ALL OFF-CAMPUS REQUESTS FOR FACILITIES USAGE AND SOLICITATIONS MUST BE SUBMITTED TO AND "
    "COORDINATED BY THE UNIVERSITY HOST.' That office is the decision-maker and NO PHONE NUMBER FOR IT IS PUBLISHED "
    "ANYWHERE — the most valuable missing field at this campus. "
    "⚠ THE REAL TEST: approval turns on alignment with 'THE UNIVERSITY'S CHRISTIAN MISSION AND EDUCATIONAL "
    "FUNCTIONS.' There is no explicit commercial ban, but this discretionary standard should be expected to be "
    "applied substantively to a cryptocurrency project, not as a formality. "
    "BDSC BUILDING GUIDELINES — three reservation tracks: (1) Student Organizations via Baylor Connect + AdAstra, "
    "at least 7 BUSINESS DAYS ahead, 10 BUSINESS DAYS for 100+; (2) Baylor Departments via AdAstra, minimum 4 "
    "business days; (3) ⚠ EXTERNAL GROUPS through a SEPARATE PROCESS at BAYLOR INSTITUTIONAL EVENTS. Same-day "
    "reservations are never accepted. "
    "⚠ BDSC PROHIBITIONS: the building prohibits 'OUTSIDE BUSINESS SOLICITATIONS' and 'HARASSING OR SOLICITING "
    "OTHER PATRONS OF THE BUILDING WHILE TABLING.' Violators are removed by Baylor DPS. "
    "FEES: 'you will NOT be charged for using the facility UNLESS MONEY IS BEING CHARGED FOR THE EVENT.' Security, "
    "where required, is the sponsoring group's responsibility. Insurance requirements exist for certain events "
    "(limits not published). Approval by Student Activities 'DOES NOT GUARANTEE SPACE' — the final call rests with "
    "the Senior Coordinator of Student Union Events. Catering by Baylor Eats – Field + Fork only; furniture through "
    "designated vendors (TDIndustries). "
    "STUDENT ORGANIZATION POLICIES: 'GROUPS OF STUDENTS NOT CHARTERED BY THE UNIVERSITY MAY NOT AFFILIATE "
    "THEMSELVES WITH BAYLOR UNIVERSITY,' plus restrictions on outside vendors conducting business THROUGH student "
    "organizations, and rules governing DEBIT AND CREDIT CARD TRANSACTIONS by student orgs. "
    "⚠ THAT LAST ITEM IS THE CLOSEST THING FOUND ANYWHERE IN TEXAS TO LANGUAGE REACHING PAYMENT CREDENTIALS — but "
    "the exact text was NOT captured precisely enough to rely on. VERIFY IT before assuming it reaches Venmo or "
    "on-site card acceptance. "
    "No anti-fronting language was found in the facilities policy."),
 "sponsor_required": "Neither sponsorship nor payment is the gate — COORDINATION BY THE UNIVERSITY HOST is, for every off-campus facilities request and solicitation, and approval turns on fit with Baylor's Christian mission. External groups also have their own separate track via Baylor Institutional Events.",

 "clubs": [
   ("(Blockchain / crypto / fintech / finance clubs)",
    "⚠ NOT CONFIRMED — not enumerated. The directory is Baylor Connect and was not reached. Not a finding of "
    "absence. Hankamer School of Business is the natural home for a finance or investment club.",
    "https://studentactivities.web.baylor.edu/"),
 ],

 "faculty": [
   ("⚠⚠ University Host",
    "no number published — look up here. THE DECISION-MAKER: 'All off-campus requests for facilities usage and "
    "solicitations must be submitted to and coordinated by the University Host.' Everything at Baylor routes "
    "through this office and NO phone number for it surfaced on any page. THIS IS THE SINGLE MOST VALUABLE MISSING "
    "FIELD AT THIS CAMPUS — get it by calling Student Activities on (254) 710-2371.",
    "Baylor University",
    "",
    "https://www.baylor.edu/"),
   ("Student Activities",
    "Student organization policies, and the practical gateway to the University Host",
    "Division of Student Life · Bill Daniel Student Center, 1st floor, 1311 S. 5th St, Waco TX 76798-7074",
    "student_activities@baylor.edu · (254) 710-2371",
    "https://studentactivities.web.baylor.edu/lead/student-organization-policies"),
   ("BDSC Reservations Desk",
    "Books Bill Daniel Student Center space; note approval here 'does not guarantee space'",
    "Student Union",
    "BDSCReservations@baylor.edu · (254) 710-3211 · M–F 8:00a–5:00p",
    "https://studentactivities.web.baylor.edu/see-our-spaces/student-union/reservation-services/student-union-building-guidelines"),
   ("Baylor Institutional Events",
    "no number published — look up here. The separate track external groups must use, distinct from the student-org "
    "and department tracks.",
    "Baylor University",
    "",
    "https://www.baylor.edu/"),
   ("Senior Coordinator of Student Union Events",
    "no number published — look up here. Holds the FINAL call on Student Union space regardless of Student "
    "Activities approval.",
    "Student Union",
    "",
    "https://studentactivities.web.baylor.edu/see-our-spaces/student-union"),
   ("(Blockchain / fintech faculty)",
    "NOT CONFIRMED — not researched; search budget exhausted. Start with the Hankamer School of Business.",
    "Hankamer School of Business",
    "",
    "https://www.baylor.edu/business/"),
 ],

 "courses": [
   ("(All courses)",
    "UNVERIFIED — not researched; search budget exhausted before Section F for this campus.",
    "https://catalog.baylor.edu/"),
 ],

 "events": [
   ("Welcome Week 2026",
    "Aug 20–23, 2026 — the likely window for a fall org fair, though no fair page was reached.",
    "https://calendar.web.baylor.edu/academic-calendar?calendar=351&category=936"),
   ("Family Weekend · Homecoming",
    "Family Weekend Sep 19, 2026 · Homecoming Nov 7, 2026 — high-footfall campus days confirmed on the academic calendar.",
    "https://calendar.web.baylor.edu/academic-calendar?calendar=351&category=936"),
   ("(Hackathons, career fairs, speaker series)",
    "UNVERIFIED — not researched (search budget exhausted).",
    "https://calendar.web.baylor.edu/"),
 ],

 "play":
   "Treat Baylor as a low-priority stop and make exactly one phone call before deciding. Baylor is private and "
   "religious, so SB 18 is irrelevant and there is no public-forum argument to make — the gate is a discretionary "
   "test of alignment with 'the university's Christian mission and educational functions', applied by an office "
   "called the University Host through which 'ALL OFF-CAMPUS REQUESTS FOR FACILITIES USAGE AND SOLICITATIONS MUST "
   "BE SUBMITTED AND COORDINATED.' A cryptocurrency project should expect that standard to be applied "
   "substantively rather than as a formality, and the Student Union separately prohibits 'outside business "
   "solicitations' with removal by Baylor DPS. THE SINGLE BEST DOOR is therefore the University Host — and its "
   "phone number is published NOWHERE, which is the most valuable missing field at this campus. Get it by calling "
   "Student Activities on (254) 710-2371, then ask the Host directly whether a digital-asset education project can "
   "clear the mission test before spending anything else here. Two cautions for whoever makes that call: the "
   "governing solicitation policy that could be located is dated 12-12-05 and came from FIRE's archive rather than "
   "a Baylor URL, so ask what the current version says; and Baylor's student-org rules contain restrictions on "
   "DEBIT AND CREDIT CARD TRANSACTIONS — the closest thing found anywhere in Texas to a rule reaching payment "
   "credentials — whose exact wording was not captured and which should be read before any on-site sign-up flow is "
   "designed. If the Host says no, that is a clean answer; take it and reallocate the day to UT Arlington or SMU.",

 "gaps": [
   "⚠⚠ University Host direct phone number — the decision-maker for ALL off-campus requests; published nowhere. Get it from (254) 710-2371.",
   "⚠ Current version of the Campus Facilities Use and Campus Solicitation Policy — the located copy is dated 12-12-05 and came from FIRE's archive, not a Baylor URL",
   "⚠ Exact text of the student-org DEBIT AND CREDIT CARD transaction rules — closest thing in Texas to language reaching payment credentials; wording not captured: https://studentactivities.web.baylor.edu/lead/student-organization-policies",
   "Fall 2026 org fair name, date and whether outsiders may participate — no page reached; Welcome Week is Aug 20–23",
   "Baylor Institutional Events contact and the external-group rate card, deposits and cancellation terms",
   "Insurance limits — 'requirements exist for certain events' but no amounts published",
   "Whether any blockchain/crypto/finance club exists — Baylor Connect not reached",
   "All faculty; all courses; all hackathons and career fairs — not researched (search budget exhausted)",
 ],
 "note": "PRIVATE (religious) — no public-forum obligation and SB 18 does not apply. Approval turns on a Christian-mission test, which is a substantive gate for a crypto project, not a formality.",
},

# ═══════════════════════════════════════════════════════════════════════════════
{
 "state": "Texas",
 "name": "Southern Methodist University",
 "city": "Dallas, TX",
 "type": "Private",
 "tier": "A — Named target (published external tabling rates; lowest-friction paid access in Texas)",
 "access": 4,

 "start": "Mon Aug 24, 2026",
 "adddrop": "Fri Aug 28, 2026 — 'Last day to enroll, add a course, or drop a course without tuition billing while remaining enrolled for the term'",
 "fallbreak": "Fall Break Mon–Tue Oct 12–13, 2026",
 "thanksgiving": "⚠ Nov 24–25 (Tue–Wed) NO CLASSES, then Nov 26–27 (Thu–Fri) Thanksgiving holiday with university offices closed — SMU takes the whole back half of that week",
 "lastclass": "Tue Dec 8, 2026 · Reading day Wed Dec 9",
 "finals": "Dec 10–16, 2026 (Thu–Wed; no examinations scheduled for Sunday)",
 "cal_url": "https://www.smu.edu/-/media/site/enrollmentservices/registrar/calendars/official-university-calendar-2026-27_7126.pdf",
 "cal_status": "CONFIRMED. ⚠ NOTE: Dec 19 is the 'official close of term and conferral of degrees' — SMU holds NO traditional fall commencement ceremony, so there is no December graduation crowd here.",

 "fair": "Fall involvement / student organization fair (name not confirmed)",
 "fair_date": "UNVERIFIED — no fair page reached. ⚠ Several SMU Student Activities URL patterns tried during research ALL RETURNED 404 (/studentaffairs/studentactivities, /studentaffairs/student-involvement, /studentaffairs/student-activities-multicultural-student-affairs); the live student-facing hub sits under Hughes-Trigg. Org platform is STABLE. Close it on (214) 768-4400.",
 "fair_outside": "UNVERIFIED for the fair. But the campus-wide answer is clear and favourable: 'EXTERNAL GROUPS CAN ONLY CONDUCT ACTIVITIES THROUGH PAID SPACE RESERVATIONS' — and SMU publishes the tabling rates.",
 "fair_cost": "$200 indoor table (Main Atrium) · $150 outdoor table (West Bridge) — these are the published EXTERNAL tabling rates, applicable year-round; fair-specific pricing UNVERIFIED",
 "fair_deadline": "Not published for the fair. General rule: invoice arrives no later than two weeks before the event and ALL COSTS MUST BE PAID ONE WEEK PRIOR.",
 "fair_url": "https://www.smu.edu/studentaffairs/hughes-trigg/external",

 "policy": "SMU campus no-solicitation policy (Hughes-Trigg Student Center, external customers); Hughes-Trigg Reservations & Fees; General Facilities Agreement",
 "policy_url": "https://www.smu.edu/studentaffairs/hughes-trigg/external",
 "policy_key": (
    "⚠ SMU IS PRIVATE. Tex. Educ. Code §51.9315 (SB 18) DOES NOT BIND IT and SMU owes no public-forum access to "
    "anyone. Do not cite the statute here. SMU is CLOSED AS A MATTER OF RIGHT AND OPEN AS A MATTER OF CONTRACT — "
    "and unusually, it publishes the price list. "
    "⚠ THE DEFINITION IS THE BROADEST IN THIS ENTIRE FILE: solicitation is 'PRESENCE WITH THE INTENT TO GARNER "
    "INFORMATION, FUNDS, ATTENTION, OR ACTION' from the SMU community. It expressly includes product distribution, "
    "sales, recruiting, advertising and surveying. 'Presence with the intent to garner... ATTENTION' sweeps in "
    "essentially any brand activation, INCLUDING A PURELY INFORMATIONAL TABLE. There is no arguing round this one. "
    "⚠⚠ BUT THE SAME PAGE STATES THE CURE: 'EXTERNAL GROUPS CAN ONLY CONDUCT ACTIVITIES THROUGH PAID SPACE "
    "RESERVATIONS.' Pay and you are compliant. This is the most legible campus in the file. "
    "PUBLISHED EXTERNAL RATES (Hughes-Trigg Student Center): ⚠⚠ INDOOR TABLE (MAIN ATRIUM) $200 · OUTDOOR WEST "
    "BRIDGE TABLE $150. Meeting rooms $20–$100/hr, daily max $100–$500 for 5+ hours. Ballroom $100–$300/hr "
    "depending on sections, $500–$1,500 daily max. Auditorium and Chamber $100/hr, $500 daily max. "
    "SETUP AND SERVICE FEES: stage $200; table configurations $100–$400; chairs $250; audio/visual $50–$300; "
    "custodial $75–$350 depending on space; HTSC staff assistance $20/hour. "
    "⚠ REQUIREMENTS: clients must provide 'A CERTIFICATE OF INSURANCE WHICH MEETS SMU'S REQUIREMENTS' (limits NOT "
    "published) and must sign the GENERAL FACILITIES AGREEMENT. "
    "⚠⚠ PAYMENT: invoice arrives no later than two weeks before the event, and 'ALL COSTS MUST BE PAID ONE (1) WEEK "
    "PRIOR TO THE EVENT.' "
    "CANCELLATION: clients should notify HTSC 'as soon as possible' by email — NO PUBLISHED CANCELLATION PENALTY "
    "SCHEDULE, which is unusually lenient compared with Rice's 100%-inside-30-days rule. No deposit is published. "
    "Student organizations reserve separately through the STABLE system — that is their track, not yours. "
    "No language found specifically reaching payment credentials or on-site contract signing, though the breadth of "
    "the solicitation definition ('funds... action') very likely covers both."),
 "sponsor_required": "No — pay the fee. $150–$200 buys a compliant contracted table. No sponsoring student organization is needed or contemplated for the external track; orgs use STABLE separately.",

 "clubs": [
   ("(Blockchain / crypto / fintech / finance clubs)",
    "⚠ NOT CONFIRMED — not enumerated. The directory is STABLE and was not reached, and every Student Activities "
    "URL tried returned 404. Not a finding of absence. Cox School of Business is the natural target.",
    "https://www.smu.edu/studentaffairs/hughes-trigg/students"),
 ],

 "faculty": [
   ("⚠ Hughes-Trigg Student Center — Student Center and Activities",
    "ONE number covers external reservations, the published $150/$200 table rates, the General Facilities "
    "Agreement and student activities. This is the whole of SMU's access process in a single call.",
    "Student Affairs · Hughes-Trigg Student Center, 3140 Dyer Street, Suite 201 (Level 2), Dallas TX 75205",
    "htsc@smu.edu · (214) 768-4400",
    "https://www.smu.edu/studentaffairs/hughes-trigg/external/reservations-fees"),
   ("(Student Activities / Student Involvement office)",
    "no separate number published — look up here. ⚠ Every URL pattern tried returned 404 "
    "(/studentaffairs/studentactivities, /studentaffairs/student-involvement, "
    "/studentaffairs/student-activities-multicultural-student-affairs). Route via Hughes-Trigg.",
    "Student Affairs",
    "",
    "https://www.smu.edu/studentaffairs/hughes-trigg/students"),
   ("(Blockchain / fintech faculty)",
    "NOT CONFIRMED — not researched; search budget exhausted. Start with the Cox School of Business.",
    "Cox School of Business",
    "",
    "https://www.smu.edu/cox"),
 ],

 "courses": [
   ("(All courses)",
    "UNVERIFIED — not researched; search budget exhausted before Section F for this campus.",
    "https://catalog.smu.edu/"),
 ],

 "events": [
   ("(Fall involvement fair, career fairs, hackathons, speaker series)",
    "UNVERIFIED — not researched, and every Student Activities URL tried 404'd. Call (214) 768-4400.",
    "https://www.smu.edu/studentaffairs/hughes-trigg/students"),
 ],

 "play":
   "SMU is the cleanest transaction in Texas: $200 buys an indoor table in the Hughes-Trigg Main Atrium, $150 buys "
   "the outdoor West Bridge table, and those are published rates on a live page. Do not be put off by the "
   "no-solicitation policy — SMU's definition is the broadest in this file, 'PRESENCE WITH THE INTENT TO GARNER "
   "INFORMATION, FUNDS, ATTENTION, OR ACTION', which sweeps in even a purely informational table — because the "
   "same page immediately supplies the cure: 'EXTERNAL GROUPS CAN ONLY CONDUCT ACTIVITIES THROUGH PAID SPACE "
   "RESERVATIONS.' Pay and you are compliant, with a signed General Facilities Agreement to prove it. Being "
   "private, SMU has no public-forum obligation and SB 18 is irrelevant, which paradoxically makes it EASIER than "
   "the publics: nobody has to litigate whether you are commercial speech, because everyone agrees you are and "
   "there is a price for it. THE SINGLE BEST DOOR: htsc@smu.edu / (214) 768-4400 — one call books the table, "
   "quotes the fees and sends the agreement. Two things to settle on that call, because neither is published: "
   "SMU's insurance certificate LIMITS, and whether a table can be booked on a specific high-traffic day. "
   "⚠ TIME-CRITICAL: ALL COSTS MUST BE PAID ONE FULL WEEK BEFORE THE EVENT and the invoice only arrives two weeks "
   "out, so a September table needs booking in August. The trade-off is audience size — SMU is small relative to "
   "the publics — so pair it with UT Arlington and UT Dallas into one DFW leg rather than treating it as a "
   "standalone trip. Note also there is NO fall commencement ceremony here, so December offers no crowd.",

 "gaps": [
   "⚠ SMU's insurance certificate REQUIREMENTS and LIMITS — required but the amounts are not published: (214) 768-4400",
   "⚠ Fall 2026 involvement fair name and date — every Student Activities URL tried returned 404: (214) 768-4400",
   "Whether external tabling can be booked on specific high-traffic days, and any date restrictions",
   "Deposit requirement (none published) and cancellation penalty schedule (none published)",
   "Whether any blockchain/crypto/finance club exists — STABLE directory not reached",
   "All faculty; all courses; all career fairs, hackathons and speaker series — not researched (search budget exhausted)",
 ],
 "note": "PRIVATE — no public-forum obligation and SB 18 does not apply; do not cite the statute here. SMU is ~25 minutes from UT Dallas and ~35 from UT Arlington — one DFW leg covers all three.",
},

# ═══════════════════════════════════════════════════════════════════════════════
{
 "state": "Texas",
 "name": "University of Texas at Arlington",
 "city": "Arlington, TX",
 "type": "Public",
 "tier": "A — ANCHOR CAMPUS (the only campus in Texas that SELLS access to outside companies)",
 "access": 5,

 "start": "Mon Aug 17, 2026 ⚠ EARLIEST START IN TEXAS (tied with UNT) — a full week ahead of the Aug 24 cluster",
 "adddrop": "Census date Tue Sep 1, 2026 · Last day to drop classes Fri Oct 30, 2026 (submit in MyMav before 4:00pm)",
 "fallbreak": "⚠ NONE — no fall break is designated for the 2026 regular session. Labor Day Mon Sep 7 only.",
 "thanksgiving": "Nov 25–27, 2026 (one no-class day plus two official holidays)",
 "lastclass": "Tue Dec 1, 2026",
 "finals": "Dec 3–9, 2026 · ⚠⚠ commencement listed as Dec 2 — SEE cal_status, THIS IS NOT COHERENT",
 "cal_url": "https://www.uta.edu/academics/academic-calendar/fall-2026",
 "cal_status": "PARTIAL — ⚠⚠ INTERNALLY INCONSISTENT AT THE END OF TERM. The calendar lists commencement Dec 2 SITTING BEFORE a Dec 3–9 final exam period, which cannot be right. Either the Dec 2 entry is something other than commencement or the page's rows merged on render. Everything from Aug 17 through Dec 1 reads consistently and can be relied on; VERIFY THE DECEMBER DATES before scheduling anything in that window.",

 "fair": "Activity Fair Day (start of term) · Involvement Fairs (mid-semester) · End of Year Celebration — run by the Office of Student Organizations on the UC Mall",
 "fair_date": "⚠⚠ FALL 2026 DATES NOT PUBLISHED — AND BOTH SOURCE PAGES ARE STALE. The events calendar entry shows Tue Nov 11, 2025, 11:00am–1:00pm, UC Mall, and is MARKED PAST. The sponsorship page lists only SPRING 2026 events (Activity Fair Day Jan 21; Involvement Fairs Feb 18 and Mar 25; End of Year Celebration Apr 28) — a sponsorship page still advertising the previous spring in August 2026 is stale, and should be treated that way. Pattern: an Activity Fair Day near the start of each semester plus mid-semester Involvement Fairs, all on the UC Mall. Will post at https://events.uta.edu/",
 "fair_outside": "⚠⚠ YES — UNIQUELY IN TEXAS. UTA 'invites external organizations to partner with student groups through various campus events,' offering 'valuable brand visibility,' and sells sponsorship packages through a TouchNet storefront. Separately, companies can BOOK BOOTH SPACE 'any day when the campus is open.' The page states NO restrictions on sponsor type and NO prohibited industries.",
 "fair_cost": "⚠ NOT PUBLISHED ON THE PAGE — tiers are referenced but amounts appear only inside the TouchNet portal (secure.touchnet.net). Get pricing on (817) 272-2293.",
 "fair_deadline": "Not published. Purchase via the 'Purchase Packages Now' and 'Book Here' links to TouchNet.",
 "fair_url": "https://www.uta.edu/student-affairs/student-organizations/sponsorships",

 "policy": "⚠ UTA's own solicitation policy NOT RETRIEVED (search budget exhausted). The operative published route is the Office of Student Organizations sponsorship/booth storefront.",
 "policy_url": "https://www.uta.edu/student-affairs/student-organizations/sponsorships",
 "policy_key": _SB18 + (
    "⚠⚠ UTA IS THE FINDING OF THIS ENTIRE PROJECT: IT IS THE ONLY CAMPUS IN THIS FILE THAT HAS PRODUCTIZED "
    "OUTSIDE-COMPANY ACCESS AND SELLS IT THROUGH THE UNIVERSITY'S OWN BURSAR SYSTEM. "
    "FROM UTA'S OWN 'BECOME A SPONSOR FOR UTA STUDENT ORGANIZATIONS' PAGE: UTA 'INVITES EXTERNAL ORGANIZATIONS TO "
    "PARTNER WITH STUDENT GROUPS THROUGH VARIOUS CAMPUS EVENTS,' offering 'VALUABLE BRAND VISIBILITY.' Sponsorship "
    "packages are purchased through a TOUCHNET STOREFRONT (secure.touchnet.net) via a 'Purchase Packages Now' "
    "button. Separately, companies can 'BOOK' BOOTH SPACE ON CAMPUS 'ANY DAY WHEN THE CAMPUS IS OPEN' — a "
    "year-round, non-event tabling option, also via a 'Book Here' link to TouchNet. "
    "⚠ THE PAGE STATES NO RESTRICTIONS ON SPONSOR TYPE, NO PROHIBITED INDUSTRIES AND NO ELIGIBILITY CRITERIA. "
    "NO SPONSORSHIP-CURES-FRONTING ANALYSIS IS NEEDED HERE, because UTA is not treating outside-entity presence as "
    "a problem to be cured — it is selling it, and the university itself is the counterparty. For a "
    "financial-product marketer this is the lowest-legal-risk paid access in Texas. "
    "⚠⚠ THREE CAVEATS TO VERIFY BY PHONE BEFORE RELYING ON ANY OF THIS: "
    "(1) THE ABSENCE OF PUBLISHED INDUSTRY RESTRICTIONS IS NOT THE SAME AS THEIR ABSENCE IN THE TERMS OF SALE — "
    "read the TouchNet package terms, where a financial-services or crypto exclusion could well live. "
    "(2) THE PAGE IS STALE: in August 2026 it still advertises Spring 2026 events. Confirm the Fall 2026 "
    "booth-booking calendar and that the storefront is live. "
    "(3) UTA IS A UT SYSTEM INSTITUTION and remains bound by SB 18 and the Regents' Rules; a booth contract does "
    "not override a system-level commercial-solicitation restriction if one applies. ⚠ UTA'S OWN SOLICITATION "
    "POLICY WAS NOT RETRIEVED — the search budget expired on that query — so the interaction between the storefront "
    "and any formal policy is UNVERIFIED. Supplier-side material sits at uta.edu/business-affairs/suppliers and "
    "/how-to-do-business-with-uta. "
    "No fee schedule, insurance requirement, deposit or cancellation term is published outside the portal, and no "
    "language reaching payment credentials or on-site contract signing was found."),
 "sponsor_required": "No — PAY THE FEE. UTA sells sponsorship packages and booth space to external organizations directly through its own TouchNet storefront, with the university as counterparty. No student-organization sponsor is needed.",

 "clubs": [
   ("(Blockchain / crypto / fintech / finance clubs)",
    "⚠ NOT CONFIRMED — not enumerated. The directory is MavEngage and was not reached. Not a finding of absence. "
    "Less critical here than elsewhere, since the sponsorship route does not depend on finding a club.",
    "https://www.uta.edu/student-affairs/student-organizations"),
 ],

 "faculty": [
   ("⚠⚠ Office of Student Organizations / MavEngage",
    "SELLS SPONSORSHIP PACKAGES AND BOOTH SPACE TO OUTSIDE COMPANIES — the only office in Texas that does. This is "
    "the highest-priority call on the entire tour. The same number and email are published on BOTH the "
    "student-organizations landing page and the sponsorship page, so it is confirmed twice.",
    "Student Affairs · E.H. Hereford University Center, 300 W. 1st Street, Suite 180H, Arlington TX 76019",
    "mavengage@uta.edu · (817) 272-2293",
    "https://www.uta.edu/student-affairs/student-organizations/sponsorships"),
   ("(Blockchain / fintech faculty)",
    "NOT CONFIRMED — not researched; search budget exhausted. Start with the College of Business and the "
    "Department of Computer Science and Engineering.",
    "College of Business",
    "",
    "https://www.uta.edu/academics/schools-colleges/business"),
 ],

 "courses": [
   ("(All courses)",
    "UNVERIFIED — not researched; search budget exhausted before Section F for this campus.",
    "https://catalog.uta.edu/"),
 ],

 "events": [
   ("⚠ Activity Fair Day / Involvement Fairs — UC Mall",
    "⚠⚠ FALL 2026 DATES NOT PUBLISHED and both source pages are stale (events calendar shows Nov 2025 marked past; "
    "sponsorship page advertises Spring 2026). Pattern: Activity Fair Day near the start of term, Involvement Fairs "
    "mid-semester. Sponsorship packages sold for these events via TouchNet.",
    "https://www.uta.edu/student-affairs/student-organizations/sponsorships"),
   ("Year-round booth booking",
    "Not an event but the most useful line on the page: companies can book booth space 'any day when the campus is "
    "open', independent of any fair. This decouples a UTA visit from the fair calendar entirely.",
    "https://www.uta.edu/student-affairs/student-organizations/sponsorships"),
   ("HackUTD — nearby, not UTA",
    "Nov 14–15, 2026 at UT Dallas, ~25 minutes away. Work DFW as one leg.",
    "https://hackutd.co/"),
   ("(UTA hackathons, career fairs, speaker series)",
    "UNVERIFIED — not researched (search budget exhausted).",
    "https://events.uta.edu/"),
 ],

 "play":
   "⚠⚠ START HERE. UT Arlington is the only campus in Texas that has turned outside-company access into a product: "
   "it 'invites external organizations to partner with student groups', sells sponsorship packages through its own "
   "TouchNet storefront, and lets companies book booth space 'ANY DAY WHEN THE CAMPUS IS OPEN' — with no published "
   "restriction on sponsor type or industry. That inverts the whole Texas picture, where SB 18's commercial-speech "
   "carve-out means the publics are usually the hardest doors. Here the university is the counterparty and the "
   "money goes through the bursar, which is the lowest-legal-risk arrangement available anywhere in this file. "
   "It also starts Mon Aug 17, the earliest in the state alongside UNT, so DFW can open the tour a week before "
   "anyone else is back. THE SINGLE BEST DOOR, and the highest-priority call on the entire tour: (817) 272-2293 / "
   "mavengage@uta.edu, Office of Student Organizations. ⚠⚠ MAKE THAT CALL BEFORE ANYTHING ELSE, and settle three "
   "things, because the public page cannot answer them: what the packages actually COST (tiers exist but pricing "
   "sits behind the TouchNet portal); whether the terms of sale carry a financial-services or crypto EXCLUSION, "
   "since the absence of published restrictions is not the same as their absence in the contract; and what the "
   "FALL 2026 fair and booth calendar is — because the sponsorship page is stale, still advertising Spring 2026 "
   "events in August 2026, and the events-calendar entry shows a November 2025 fair marked past. One caveat to "
   "hold in mind: UTA's own solicitation policy was never retrieved, so how the storefront interacts with any "
   "formal UT System commercial-solicitation rule is unverified — ask on the same call. Pair with UT Dallas "
   "(25 minutes, HackUTD Nov 14–15) and SMU (35 minutes, $150–$200 tables) into a single DFW leg.",

 "gaps": [
   "⚠⚠ TouchNet sponsorship package PRICING and TERMS OF SALE — including whether a financial-services or crypto exclusion applies. Pricing is behind the portal: (817) 272-2293 · mavengage@uta.edu",
   "⚠⚠ Fall 2026 Activity Fair Day / Involvement Fair dates and the booth-booking calendar — BOTH source pages are stale (events calendar shows Nov 2025 marked past; sponsorship page advertises Spring 2026): https://events.uta.edu/",
   "⚠ UTA's own solicitation policy — NEVER RETRIEVED (search budget exhausted). How the storefront interacts with any UT System commercial-solicitation rule is unverified. Check the UTA policy library and uta.edu/business-affairs/suppliers.",
   "⚠ December 2026 calendar dates — commencement is listed as Dec 2, BEFORE a Dec 3–9 finals period, which is not coherent: https://www.uta.edu/academics/academic-calendar/fall-2026",
   "Insurance requirements, deposits and cancellation terms for a booth or sponsorship — none published outside the portal",
   "Whether any blockchain/crypto/finance club exists — MavEngage not reached (less critical here, since access does not depend on a club)",
   "All faculty; all courses; UTA hackathons, career fairs and speaker series — not researched (search budget exhausted)",
 ],
 "note": "UT Arlington is ~25 minutes from UT Dallas and ~35 from SMU — one DFW leg covers all three, and between them they hold the state's only access-5 campus, an access-4 private with published rates, and the largest hackathon.",
},

]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; sorts last, no countdown.
DEADLINES = [

 # ── the money calls, undated but urgent — these gate everything else ──────────
 ("", "AS SOON AS POSSIBLE", "UT Arlington",
  "⚠⚠ CALL THE ONLY OFFICE IN TEXAS THAT SELLS CAMPUS ACCESS — GET PRICING AND TERMS",
  "UTA sells sponsorship packages and year-round booth space to external companies via its own TouchNet "
  "storefront, with no published industry restriction. Pricing sits BEHIND the portal. Settle three things on one "
  "call: package cost; whether the terms of sale carry a financial-services or crypto exclusion; and the Fall 2026 "
  "fair/booth calendar — the sponsorship page is STALE, still advertising Spring 2026 events in August 2026.",
  "https://www.uta.edu/student-affairs/student-organizations/sponsorships",
  "mavengage@uta.edu · (817) 272-2293"),

 ("", "AS SOON AS POSSIBLE", "Texas State",
  "⚠⚠ CALL THE MOST PERMISSIVE PUBLIC-CAMPUS VENDOR RULE IN TEXAS",
  "UPPS 07.04.03 expressly permits a department OR student organization to sponsor an outside vendor if the "
  "sponsor is physically present. Ask for: the unpublished vendor fee and table rate; whether an EXISTING "
  "UNIVERSITY CONTRACTUAL RELATIONSHIP (banking/financial-services exclusive) blocks a crypto vendor — the one "
  "clause that can kill this route; and whether the Involvement Fair is Aug 27 in 2026. Requests need 10 "
  "UNIVERSITY BUSINESS DAYS; approved vendors get up to TWO CONSECUTIVE WEEKS on campus.",
  "https://studentinvolvement.txst.edu/operations-and-assessment/campus-access/solicitation.html",
  "campusaccess@txstate.edu · (512) 245-3219"),

 ("", "AS SOON AS POSSIBLE", "Rice University",
  "⚠⚠ EMAIL HACKRICE 16 SPONSORSHIP — EVENT IS SEP 11–13, 2026",
  "500+ developers, held in the Rice Student Center. Sponsorship contact published in the clear. NO PROSPECTUS IS "
  "POSTED, so tiers and pricing must be negotiated by hand — and hackathon tiers close well before the event. This "
  "is the most valuable confirmed date in the Texas file and it is roughly four weeks out.",
  "https://hackrice.com/",
  "officialhackrice@gmail.com"),

 ("", "AS SOON AS POSSIBLE", "UT Dallas",
  "⚠⚠ OPEN hackutd.co IN A BROWSER AND EMAIL THE INDUSTRY TEAM — EVENT NOV 14–15, 2026",
  "'North America's largest 24 hour university-run hackathon', ECS West. A standing Industry Team solicits "
  "sponsors. ⚠ The sponsorship email is OBFUSCATED as '[email protected]' in automated page renders — it must be "
  "read off the live page. Tiers for a mid-November event typically close in SEPTEMBER. This is a private "
  "student-run event and does not depend on UTD's (unretrieved) campus policy.",
  "https://hackutd.co/",
  "read the address off the live page · UTD CS dept (972) 883-2974"),

 ("", "AS SOON AS POSSIBLE", "SMU",
  "⚠⚠ BOOK A PAID TABLE — PUBLISHED RATES, LOWEST-FRICTION ACCESS IN TEXAS",
  "$200 indoor table (Hughes-Trigg Main Atrium) · $150 outdoor (West Bridge). 'External groups can only conduct "
  "activities through paid space reservations.' Requires a certificate of insurance meeting SMU's requirements "
  "(LIMITS NOT PUBLISHED — ask) and a signed General Facilities Agreement. ⚠ ALL COSTS MUST BE PAID ONE FULL WEEK "
  "BEFORE THE EVENT and the invoice only arrives two weeks out, so a September table needs booking in August.",
  "https://www.smu.edu/studentaffairs/hughes-trigg/external/reservations-fees",
  "htsc@smu.edu · (214) 768-4400"),

 ("", "AS SOON AS POSSIBLE", "University of Houston",
  "⚠ CALL CARS — RSO SPONSORSHIP OF AN EXTERNAL ENTITY IS EXPRESSLY PERMITTED HERE",
  "UH is the only large Texas public whose rule says an RSO 'can sponsor external entities if they actively "
  "participate... and ensure an RSO member attends the entire event.' Ask for the unpublished external rate card, "
  "and resolve the live contradiction between MAPP 01.05.01 (SEVEN business days) and the Student Centers page "
  "(FIVE business days). ⚠ OUTDOOR EVENTS NEED FIFTEEN BUSINESS DAYS — three working weeks — so a September "
  "outdoor activation must be filed in late August.",
  "https://www.uh.edu/studentcenters/reservations/",
  "cars@uh.edu · (832) 842-6167"),

 ("", "BEFORE MID-AUGUST", "UNT",
  "⚠ CALL FOR THE CONTRACTED-VENDOR ROUTE — UNT STARTS AUG 17 AND ITS FIRST FAIR IS AUG 19",
  "Policy 04.013: 'ONLY APPROVED CONTRACTED VENDORS, ORGANIZATIONS, AND DEPARTMENTS ARE ELIGIBLE TO SOLICIT', and "
  "outside salespersons need advance WRITTEN PERMISSION from the Associate VP of Auxiliary Services — whose number "
  "is not published. All three fall org fairs are RSO-only ('Only RSOs are eligible to participate'). A vendor "
  "contract is not a two-week process, so the early start is only an advantage if this call happens now.",
  "https://policy.unt.edu/sites/default/files/04.013%20Solicitation,%20Signs,%20and%20Postings.pdf",
  "student.activities@unt.edu · (940) 565-3807 · Dean of Students Laura Smith (940) 565-2648"),

 # ── term starts ──────────────────────────────────────────────────────────────
 ("2026-08-17", "Mon Aug 17, 2026", "UT Arlington",
  "Fall 2026 classes begin — ⚠ EARLIEST START IN TEXAS (tied with UNT)",
  "A full week ahead of the Aug 24 cluster. No fall break all term. Census Sep 1; last day to drop Oct 30. "
  "Together with UNT this lets the tour open in DFW while every other Texas campus is still empty.",
  "https://www.uta.edu/academics/academic-calendar/fall-2026",
  "mavengage@uta.edu · (817) 272-2293"),

 ("2026-08-17", "Mon Aug 17, 2026", "UNT",
  "Fall 2026 classes begin — ⚠ EARLIEST START IN TEXAS (tied with UT Arlington)",
  "Census/add-drop Aug 28. No fall break. Runs parallel 8-week I and 8-week II sessions with different dates.",
  "https://registrar.unt.edu/sites/default/files/fall-2026-academic-calendar.pdf",
  "student.activities@unt.edu · (940) 565-3807"),

 ("2026-08-19", "Wed Aug 19, 2026", "Texas State",
  "Fall 2026 classes begin — ⚠ EARLY START",
  "Census Sep 3. ⚠ Use onestop.txst.edu for dates — the registrar's own academic calendar page is STALE and "
  "serves Fall 2025 dates.",
  "https://onestop.txst.edu/important-dates.html",
  "campusaccess@txstate.edu · (512) 245-3219"),

 ("2026-08-19", "Wed Aug 19, 2026", "UT San Antonio",
  "Fall 2026 classes begin — ⚠ EARLY START",
  "Census and final payment deadline Sep 3. Fall Break Oct 12–13. Parallel 8-week terms run inside the semester.",
  "https://www.utsa.edu/registrar/reg_materials/reg_calendar_fall.pdf",
  "getinvolved@utsa.edu · (210) 458-4160"),

 ("2026-08-19", "Wed Aug 19, 2026", "UNT",
  "UNT Student Organization Fair #1 of 3 — 11:30am–1:30pm, Library Mall",
  "⚠ RSO-ONLY, verbatim: 'Only RSOs are eligible to participate.' Two days into term. Listed because the campus is "
  "at maximum density and because a sponsoring RSO, if one is ever secured, would table here.",
  "https://studentaffairs.unt.edu/student-activities-center/programs-and-services/student-organizations/involvement-fairs.html",
  "student.activities@unt.edu · (940) 565-3807"),

 ("2026-08-20", "Aug 20–23, 2026", "Baylor",
  "Baylor Welcome Week — the likely window for a fall org fair",
  "No fair page could be reached, so the fair itself is UNVERIFIED; Welcome Week is confirmed on the academic "
  "calendar and is when a fair would fall. Classes begin Aug 24.",
  "https://calendar.web.baylor.edu/academic-calendar?calendar=351&category=936",
  "student_activities@baylor.edu · (254) 710-2371"),

 ("2026-08-24", "Mon Aug 24, 2026", "UT Austin",
  "Fall 2026 classes begin",
  "12th class day / drop deadline Sep 9; Q-drop Nov 18. Full Thanksgiving week off (Nov 23–28). Access 1 — plan a "
  "speaker slot or HackTX, not a table.",
  "https://registrar.utexas.edu/calendars/26-27",
  "studentorganizations@austin.utexas.edu · (512) 471-3065"),

 ("2026-08-24", "Mon Aug 24, 2026", "University of Houston",
  "Fall 2026 classes begin (Session 1 / full term)",
  "Add Sep 2; drop without grade Sep 9; 'W' deadline Nov 18. ⚠ UH runs SIX sessions — these dates are Session 1 "
  "only. Registrar's own Fall 2026 page renders interactively and returned no dates; source is the sessions page.",
  "https://www.uh.edu/online/sessions/fall.php",
  "cars@uh.edu · (832) 842-6167"),

 ("2026-08-24", "Mon Aug 24, 2026", "Texas Tech",
  "Fall 2026 classes begin",
  "Drop without penalty Sep 9. No fall break. Dead Day Dec 3. ⚠ Access 1 with an explicit anti-fronting rule "
  "carrying a one-year penalty — do not plan a table.",
  "https://www.depts.ttu.edu/officialpublications/calendar/26-27_cal_detailed.php",
  "Student Union & Activities (806) 742-3636"),

 ("2026-08-24", "Mon Aug 24, 2026", "UT Dallas",
  "Fall 2026 classes begin (full term)",
  "Census Day Sep 9. ⚠ Only these two dates are officially confirmed — everything from Thanksgiving onward is "
  "third-party only, because the official calendar PDF sits on Box and Box requires JavaScript.",
  "https://calendar.utdallas.edu/event/fall-2026-classes-begin-full-term-session",
  "Student Affairs (972) 883-6236"),

 ("2026-08-24", "Mon Aug 24, 2026", "Rice University",
  "Fall 2026 classes begin",
  "Add/drop Sep 4; Midterm Recess Oct 12–13. ⚠ Rice also runs a SEPARATE FALL QUADMESTER calendar alongside the "
  "semester — a different audience on a different clock.",
  "https://registrar.rice.edu/calendars/fall-semester-2026",
  "scevents@rice.edu · (713) 348-4097"),

 ("2026-08-24", "Mon Aug 24, 2026", "Baylor",
  "Fall 2026 classes begin",
  "Add/register Aug 28; drop without 'W' Sep 9. Fall Break is a single day, Fri Oct 9. Two 7-week sessions run "
  "inside the term.",
  "https://calendar.web.baylor.edu/academic-calendar?calendar=351&category=936",
  "student_activities@baylor.edu · (254) 710-2371"),

 ("2026-08-24", "Mon Aug 24, 2026", "SMU",
  "Fall 2026 classes begin",
  "Add/drop Aug 28; Fall Break Oct 12–13. ⚠ No traditional fall commencement ceremony — Dec 19 is conferral of "
  "degrees only, so December offers no graduation crowd.",
  "https://www.smu.edu/-/media/site/enrollmentservices/registrar/calendars/official-university-calendar-2026-27_7126.pdf",
  "htsc@smu.edu · (214) 768-4400"),

 # ── the fairs and the hackathons ─────────────────────────────────────────────
 ("2026-08-27", "Thu Aug 27, 2026 (⚠ YEAR UNCONFIRMED)", "Texas State",
  "⚠ Student Involvement Fair — 4:00–6:00pm, LBJ Student Center Ballrooms",
  "⚠⚠ THE PAGE PRINTS 'August 27th' WITH NO YEAR. Aug 27, 2026 is a Thursday (8 days after the Aug 19 start — "
  "plausible); Aug 27, 2025 was a Wednesday (2 days after the 2025 start — also plausible). The registrar page on "
  "this same domain is serving stale 2025 content, so DO NOT ASSUME 2026. Confirm before travelling.",
  "https://studentinvolvement.txst.edu/involvement/student-orgs/involvementfair.html",
  "getinvolved@txstate.edu · (512) 245-3219"),

 ("2026-09-06", "Sun Sep 6, 2026", "Texas A&M",
  "Club Crawl — 1:00–5:00pm, MSC · Rudder · ILCB · Texas A&M Hotel",
  "'The Official Involvement Festival at Texas A&M' — 1,300+ recognized student organizations. ⚠ RECOGNIZED-ORGS "
  "ONLY; there is no vendor tier and participation is a benefit of recognition. Listed because it is the single "
  "densest student day in Texas and the only confirmed Fall 2026 date at A&M, whose academic calendar is unknown.",
  "https://clubcrawl.tamu.edu/",
  "clubcrawl@tamu.edu · (979) 845-1515"),

 ("2026-09-11", "Sep 11–13, 2026", "Rice University",
  "⚠⚠ HACKRICE 16 — 500+ DEVELOPERS, RICE STUDENT CENTER, SPONSORSHIP OPEN",
  "The highest-value confirmed date in the Texas file. Student-run private event, so it sits outside campus "
  "commercial-use rules. 'Want to get your company in front of 500+ top-tier developers, designers, and "
  "engineers?' No prospectus posted — email for terms. Sequences five days after A&M's Club Crawl; Rice is 4 miles "
  "from the University of Houston.",
  "https://hackrice.com/",
  "officialhackrice@gmail.com"),

 ("2026-09-14", "Mon Sep 14, 2026", "UNT",
  "UNT Student Organization Fair #2 of 3 — 11:30am–1:30pm, Library Mall",
  "⚠ RSO-only. Registration for this fair opens Aug 20 and may close early if spots fill.",
  "https://studentaffairs.unt.edu/student-activities-center/programs-and-services/student-organizations/involvement-fairs.html",
  "student.activities@unt.edu · (940) 565-3807"),

 ("2026-09-19", "Sat Sep 19, 2026", "Baylor",
  "Baylor Family Weekend — high-footfall campus day",
  "Confirmed on the undergraduate academic calendar. Access here is gated by the University Host and a Christian-"
  "mission test, so treat this as context rather than an opportunity until that call is made.",
  "https://calendar.web.baylor.edu/academic-calendar?calendar=351&category=936",
  "student_activities@baylor.edu · (254) 710-2371"),

 ("2026-10-14", "Wed Oct 14, 2026", "UNT",
  "UNT Student Organization Fair #3 of 3 — 11:30am–1:30pm, Library Mall",
  "⚠ RSO-only. Registration opens Sep 15. Three separate fall fairs on one campus is unusual and useful if a "
  "sponsoring RSO is ever secured.",
  "https://studentaffairs.unt.edu/student-activities-center/programs-and-services/student-organizations/involvement-fairs.html",
  "student.activities@unt.edu · (940) 565-3807"),

 ("2026-11-07", "Sat Nov 7, 2026", "Baylor",
  "Baylor Homecoming — high-footfall campus day",
  "Confirmed on the undergraduate academic calendar.",
  "https://calendar.web.baylor.edu/academic-calendar?calendar=351&category=936",
  "student_activities@baylor.edu · (254) 710-2371"),

 ("2026-11-14", "Nov 14–15, 2026", "UT Dallas",
  "⚠⚠ HACKUTD — 'NORTH AMERICA'S LARGEST 24 HOUR UNIVERSITY-RUN HACKATHON'",
  "Prospective dates, ECS West building, Richardson TX. A standing Industry Team actively solicits sponsors. "
  "Student-run private event — sidesteps campus commercial-use rules entirely, which matters because UTD's own "
  "policy was never retrieved. ⚠ Sponsorship tiers for a mid-November event typically close in September, and the "
  "contact email is obfuscated in automated renders — open the site in a browser now.",
  "https://hackutd.co/",
  "read the address off hackutd.co · UTD CS (972) 883-2974"),

 # ── monitor-only: unpublished dates and unresolved blockers ──────────────────
 ("", "MONITOR — BLOCKING", "Texas A&M",
  "⚠⚠ ENTIRE FALL 2026 ACADEMIC CALENDAR IS UNKNOWN",
  "The registrar's Fall 2026 page is a JavaScript event shell: it carries a 'Download Semester Calendar' button "
  "and event titles but NO DATES, and the catalog page is a navigation stub. The only Fall 2026 anchor at A&M is "
  "Club Crawl on Sep 6. NOTHING about an A&M leg can be scheduled until someone opens that page in a browser and "
  "downloads the calendar. Do not assume A&M matches UT Austin's Aug 24.",
  "https://registrar.tamu.edu/academic-calendar/fall-2026.html",
  "SOLAD solad@tamu.edu · (979) 458-4371"),

 ("", "MONITOR — BLOCKING", "UT Dallas",
  "⚠⚠ UTD SOLICITATION POLICY WAS NEVER RETRIEVED",
  "The search budget expired on this exact query. The access-2 rating in this file is a CONSERVATIVE PLACEHOLDER "
  "inferred from UT System peers, not a reading of UTD's own text — and the spread across that system is enormous "
  "(UT Austin bans fronting; UTSA bans commercial speech; UT Arlington sells sponsorships). This is a gap, not a "
  "finding that no restriction exists.",
  "https://policy.utdallas.edu/",
  "Student Affairs (972) 883-6236"),

 ("", "MONITOR", "UT Austin",
  "⚠ HACKTX DATES AND SPONSORSHIP CONTACT UNKNOWN — hacktx.com is an unreadable JS shell",
  "UT Austin's flagship hackathon and the single most valuable unknown on that campus. A student-run hackathon is "
  "the one route that sidesteps Institutional Rules Chapters 10 and 13, which otherwise close UT Austin "
  "completely. Nothing — dates, venue, size, sponsorship contact — could be read. Open in a browser.",
  "https://hacktx.com/",
  "Student Organizations (512) 471-3065"),

 ("", "MONITOR", "Texas A&M",
  "⚠ HOWDYHACK (FALL HACKATHON) DATES AND SPONSORSHIP CONTACT UNKNOWN",
  "TAMUhack's flagship runs in January; HowdyHack is the FALL event. tamuhack.org/hh returned an EMPTY JAVASCRIPT "
  "SHELL. Given that Student Rule 39.4 bars non-university vendors from campus facilities and redirects them to "
  "advertising, a student-run hackathon is the cleanest legitimate route to A&M students. Open in a browser.",
  "https://tamuhack.org/",
  "SOLAD solad@tamu.edu · (979) 458-4371"),

 ("", "MONITOR", "Baylor",
  "⚠ UNIVERSITY HOST PHONE NUMBER IS PUBLISHED NOWHERE",
  "'All off-campus requests for facilities usage and solicitations must be submitted to and coordinated by the "
  "University Host.' That office decides everything at Baylor and no number for it surfaced on any page — the most "
  "valuable missing field at this campus. Get it from Student Activities, then ask the Host directly whether a "
  "digital-asset project can clear the Christian-mission test before spending anything else here.",
  "https://studentactivities.web.baylor.edu/lead/student-organization-policies",
  "student_activities@baylor.edu · (254) 710-2371"),

 ("", "MONITOR", "University of Houston",
  "⚠ THE CAT'S BACK FALL 2026 DATES UNKNOWN — both sources are broken or stale",
  "The Get Involved event page is Campus Labs Engage and returned only 'This application requires JavaScript to be "
  "enabled', AND uh.edu/wow/ is STALE — it served content describing an AUGUST 2021 t-shirt swap. Pattern: "
  "multi-day, at the start of the fall semester. Nobody currently knows when UH's flagship fair is.",
  "https://getinvolved.uh.edu/event/8197700",
  "cars@uh.edu · (832) 842-6167"),

 ("", "MONITOR", "UT Arlington",
  "⚠ FALL 2026 FAIR AND BOOTH CALENDAR UNPUBLISHED — BOTH SOURCE PAGES ARE STALE",
  "The events-calendar entry shows Tue Nov 11, 2025 and is marked PAST; the sponsorship page lists only Spring "
  "2026 events (Jan 21, Feb 18, Mar 25, Apr 28) — still advertising the previous spring in August 2026. Note the "
  "booth option decouples a visit from the fair calendar entirely: companies may book 'any day when the campus is "
  "open'.",
  "https://events.uta.edu/",
  "mavengage@uta.edu · (817) 272-2293"),

 ("", "MONITOR", "UT Austin · Texas Tech · UT San Antonio · SMU · Rice · UT Dallas",
  "⚠ SIX FALL 2026 INVOLVEMENT-FAIR DATES UNPUBLISHED OR UNREADABLE",
  "UT Austin Student Organization Fair (calendar.utexas.edu); Texas Tech Raider Welcome Student Org Fair "
  "(techconnect.dsa.ttu.edu, JS-rendered); UTSA Get Involved Fair (rowdylink.utsa.edu, JS-rendered); SMU fall fair "
  "(every Student Activities URL tried 404s); Rice Student Activities Fair (not published); UTD fair (studentorgs "
  "and studentunion hostnames DNS-fail). ⚠ In every case the platform is JavaScript-gated or the page is broken — "
  "these are unread pages, NOT cancelled events.",
  "https://calendar.utexas.edu/",
  "see each campus record for the office phone"),

 ("", "MONITOR", "All 10 campuses except UT Austin and UT Dallas",
  "⚠ NO BLOCKCHAIN/CRYPTO CLUB CONFIRMED — because every org directory is JavaScript-gated",
  "Campus Labs Engage, RowdyLink, OwlNest, Baylor Connect, STABLE, MavEngage, Comet Connection, TechConnect, "
  "Bobcat Organization Hub and HornsLink ALL returned nothing to automated fetch. ⚠⚠ THIS IS A PLATFORM "
  "LIMITATION, NOT EVIDENCE THAT THE CLUBS DO NOT EXIST. Only UT Austin (Texas Blockchain, itself unreadable "
  "behind HornsLink), Texas A&M (tamublockchain.com, robots-blocked) and UT Dallas (a stale CS article) surfaced "
  "any crypto club at all. One browser session would close most of this.",
  "https://utexas.campuslabs.com/engage/organization/txblockchain",
  "see each campus record"),

 ("", "MONITOR", "Statewide",
  "⚠ SECTIONS F (COURSES) AND G (EVENTS) ARE LARGELY UNRESEARCHED — SEARCH BUDGET EXHAUSTED",
  "Only UT Austin has course data, and even there NO COURSE CODES ARE PUBLISHED (the McCombs Blockchain Initiative "
  "lists titles and instructors only) and Fall 2026 offering status is unconfirmed. Faculty were confirmed only at "
  "UT Austin and one name at UT Dallas. Career fairs, entrepreneurship weeks and speaker series were not "
  "researched at 11 of 12 campuses. Also unresearched: Texas Blockchain Council UNIVERSITY CHAPTERS — its site "
  "publishes no chapter list, no student programme and no contact, so whether campus chapters exist COULD NOT BE "
  "ESTABLISHED; and any Lubbock mining-industry or state-legislative tie to Texas Tech.",
  "https://registrar.utexas.edu/schedules/269",
  "see each campus record"),
]
