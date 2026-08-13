"""New Mexico — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL loaded during research on Aug 11-12, 2026.
Empty string or "UNVERIFIED" means not published at time of research — a gap to close by
phone, not a finding of absence. Full research prose: research50/new-mexico.md
Schema: reference/data-schema.md

⚠ RESEARCH COVERAGE CAVEAT: the web-search budget was exhausted partway through this
state (200/200 calls). Coverage of UNM and NMSU is deep; NM Tech, ENMU, NMHU and CNM were
finished by direct URL fetching only, which cannot discover pages that are not linked from
a page already known. Where that thinned coverage, the field says so and the item is in
`gaps`. Read an "UNVERIFIED" on the four smaller campuses as "not looked for exhaustively",
not as "does not exist".

⚑ STATE-LEVEL FINDING: NEW MEXICO HAS NO CAMPUS FREE-SPEECH STATUTE. All six campuses in
this file are PUBLIC and therefore bound by First Amendment public-forum doctrine — but
there is no state FORUM-Act equivalent, no statutory ban on free-speech zones, and no
private right of action to invoke. Recorded in the policy_key of every campus below.
"""

STATE = "New Mexico"

CAMPUSES = [

# ══════════════════════════════════════════════════════════════════════════════
# 1. UNIVERSITY OF NEW MEXICO
# ══════════════════════════════════════════════════════════════════════════════
{
 "state": "New Mexico",
 "name": "University of New Mexico",
 "city": "Albuquerque, NM",
 "type": "Public",
 "tier": "A — Named target",
 "access": 4,

 "start": "Mon Aug 17, 2026",
 "adddrop": "UNVERIFIED — not retrievable. The detailed term calendar is a JavaScript "
            "widget at unmevents.unm.edu that returns no dates; the registrar's calendar "
            "directory holds only the ten-year PDF. Call the Registrar, (505) 277-8900.",
 "fallbreak": "Thu-Fri Oct 8-9, 2026 (4-day weekend)",
 "thanksgiving": "UNVERIFIED — not published in retrievable form. Call the Registrar, "
                 "(505) 277-8900.",
 "lastclass": "Sat Dec 12, 2026 — this is the SEMESTER-END date from the ten-year "
              "calendar, not necessarily the last lecture day",
 "finals": "UNVERIFIED — not published in retrievable form. Call the Registrar, "
           "(505) 277-8900.",
 "cal_url": "https://registrar.unm.edu/academic-calendar/ten-year-semester-dates-calendar.html",
 "cal_status": "PARTIAL",

 "fair": "Welcome Back Days 2026 — Student Organization Day + Campus Employment & "
         "Community Service Day",
 "fair_date": "⚠⚠ CONFIRMED FOR FALL 2026 AND HAPPENING NOW: Aug 14-21, 2026. "
              "STUDENT ORGANIZATION DAY = Thu Aug 20, 10am-2pm, Duck Pond (~200 of 350+ "
              "orgs table). CAMPUS EMPLOYMENT & COMMUNITY SERVICE DAY = Fri Aug 21, "
              "10am-2pm, Duck Pond — this is the slot structurally aimed at off-campus "
              "entities. Page is CURRENT, not stale: every weekday verified against the "
              "2026 calendar (Aug 14=Fri, 16=Sun, 17=Mon, 20=Thu, 21=Fri, all correct).",
 "fair_outside": "PROBABLY YES, BUT UNDEFINED — the SAC page states 'Departments, student "
                 "organizations, AND COMMUNITY AGENCIES may participate in Welcome Back "
                 "Days events.' ⚠ 'Community agencies' is nowhere defined and a for-profit "
                 "crypto project is not obviously one. This is the most permissive "
                 "documented on-campus tabling language in New Mexico — VERIFY BY PHONE "
                 "before travelling on it: SAC (505) 277-4706.",
 "fair_cost": "UNVERIFIED — NO FEE IS PUBLISHED anywhere on the SAC pages. Do not assume "
              "free. Ask SAC (505) 277-4706.",
 "fair_deadline": "⚠⚠ GENERAL REGISTRATION CLOSES MON AUG 17, 2026 (per the UNM news "
                  "release). Friday Night Live tabling deadline was Aug 1, 2026 — ALREADY "
                  "PASSED. Sign-ups opened Jul 10, 2026.",
 "fair_url": "https://sac.unm.edu/events/welcome-back-days.html",

 "policy": "RPM 2.12 Advertising, Sales and Solicitations on Campus (adopted 09-12-1996, "
           "amended 06-12-2012) · UAP 5250 Use of University Facilities (eff. 06-11-2018) · "
           "UAP 2220 Freedom of Expression and Dissent (eff. 01-14-2002) · SUB General "
           "Policy · SUB Chartered Student Organization Booking Guidelines (approved "
           "02-12-2024)",
 "policy_url": "https://policy.unm.edu/regents-policies/section-2/2-12.html",
 "policy_key":
   "SUB General Policy: 'NO PERSON SHALL SELL FOOD, GOODS, OR SERVICES OR CARRY ON A TRADE "
   "OR BUSINESS ON UNIVERSITY PROPERTY WITHOUT THE EXPRESSED CONSENT OF THE UNIVERSITY.' "
   "⚠ ANTI-FRONTING — CSO Booking Guidelines (approved 2.12.2024): 'In the event a "
   "Chartered Student Organization reserves meeting rooms and/or event space in the SUB "
   "for a UNM Department (OR OTHER CHARGEABLE ENTITY)' the CSO RISKS LOSING BOOKING "
   "PRIVILEGES FOR THE YEAR. ⚠ AND SPONSORSHIP DOES NOT CURE THE FEE: 'UNM Departments and "
   "External Organizations may partner with Chartered Student Organizations for rooms, "
   "conferences and other events, BUT THEY WILL BE CHARGED THE STANDARD UNM DEPARTMENTAL "
   "RATE AND EXTERNAL ORGANIZATIONAL RATES ACCORDINGLY.' — so having a club book for you "
   "is both penalised and pointless. UAP 5250: 'University units and off-campus "
   "organizations may request use of University buildings and grounds, subject to the "
   "payment of applicable fees'; 'THE FACILITY USER RESERVING THE SPACE MUST BE THE PRIMARY "
   "ORGANIZER OF THE EVENT'; 'Facility users may not sell, sublease, or transfer their "
   "reservations.' INSURANCE: 'a certificate of insurance for general liability in an "
   "amount NO LESS THAN $1,000,000 and workman's compensation for employees', naming 'the "
   "Regents of the University of New Mexico, the University of New Mexico, its agents, "
   "officers, and employees as additional insured.' CANCELLATION: 'Labor charges will be "
   "assessed for canceled functions when any such costs have been incurred'; SUB requires "
   "3 business days notice or you are logged a 'No Show' — three no-shows in a semester "
   "terminates privileges for the remaining academic year. "
   "⚑ THE OPENING, AND IT IS A REAL ONE — UAP 2220: 'SCHEDULING TO USE UNIVERSITY "
   "FACILITIES FOR SPEECH ACTIVITIES IS NOT REQUIRED.' Protected activity expressly "
   "includes 'Speechmaking, praying, THE DISTRIBUTION OF WRITTEN MATERIALS, picketing, "
   "assembling in groups, demonstrating, sidewalk chalking, erecting symbolic structures.' "
   "Only three things must be scheduled: 'Assemblies or large events in a University "
   "auditorium or similar facility; Planned demonstrations on campus; Building a symbolic "
   "structure on campus.' NET EFFECT: LEAFLET FREELY ON THE OPEN CAMPUS; SELL OR TRANSACT "
   "NOTHING WITHOUT EXPRESS CONSENT. "
   "⚠ RPM 2.12 is the controlling commercial-solicitation policy and ITS NUMBERED "
   "SUBSECTIONS WOULD NOT RENDER on either the http or https URL — only the preamble is "
   "readable ('Unregulated advertising, solicitation, and sales can create chaos, disturb "
   "the University's educational environment... and create unwarranted risks for "
   "consumers'). THE OPERATIVE TEXT IS UNVERIFIED — Policy Office (505) 277-2069. "
   "⚠ NO NEW MEXICO CAMPUS FREE-SPEECH STATUTE EXISTS. UNM's own free-speech portal "
   "(freespeech.unm.edu/policies-law) lists the state statutes it considers applicable and "
   "EVERY ONE IS A CRIMINAL-CODE PROVISION — §30-14-1 Criminal Trespass, §30-20-1 "
   "Disorderly Conduct, §30-20-3 Unlawful Assembly, §30-14-4(2) Wrongful Use of Public "
   "Property, §30-3A-2 Harassment. None confers campus forum rights. There is no FORUM-Act "
   "equivalent to cite. Public-forum doctrine plus institutional policy is the whole of "
   "the law here.",
 "sponsor_required": "⚠ NO — and do not try. Student-org sponsorship is affirmatively "
                     "PENALISED (the CSO loses booking privileges) and still incurs the "
                     "External Organizational Rate. Route as a paying external renter via "
                     "Event Planning & Scheduling (505) 277-5498, or stay inside UAP 2220 "
                     "and distribute literature without reserving anything.",

 "clubs": [
   ("⚠ DIRECTORY IS UNREADABLE — read this before trusting any negative below",
    "UNM Involve (unm.presence.io/organizations) is JavaScript-rendered and returns no org "
    "data. The SAC org-list page is TWO YEARS STALE — it still shows a banner reading 'The "
    "Student Activities Center is in the process of updating the computer software... It "
    "will be down until August 7th, 2024.' The list below is a PARTIAL recovery via the "
    "Presence backend API and is NOT the full 350+ org roster.",
    "https://unm.presence.io/organizations"),
   ("AI@UNM",
    "Listed active. 'Explores technical principles of artificial intelligence and societal "
    "implementation' — the closest technical-audience match confirmed at UNM.",
    "https://api.presence.io/unm/v1/organizations"),
   ("Beta Alpha Psi",
    "Listed active. Accounting / business-information honor org — Anderson School audience.",
    "https://api.presence.io/unm/v1/organizations"),
   ("Association of Graduate Business Students",
    "Listed active. Anderson MBA audience.",
    "https://api.presence.io/unm/v1/organizations"),
   ("Business Law Society",
    "Listed active. Regulatory-angle audience.",
    "https://api.presence.io/unm/v1/organizations"),
   ("Association of Latino Professionals for America (ALPFA)",
    "Listed active. Professional networking chapter.",
    "https://api.presence.io/unm/v1/organizations"),
   ("(Blockchain / crypto / Web3 club)",
    "NONE FOUND — but the directory is only partially readable, so this is UNVERIFIED, not "
    "established absence. Also NO investment club, NO finance club and NO Financial "
    "Management Association chapter surfaced. Confirm by asking SAC to read the org list "
    "by category: (505) 277-4706.",
    "https://sac.unm.edu/student-organizations/student-organizations.html"),
   ("(CS department orgs)",
    "NOT RETRIEVED — the UNM CS department keeps a separate org page that was never "
    "loaded. Likely home of any ACM chapter. Look up here.",
    "https://www.cs.unm.edu/students/organizations.html"),
 ],

 "faculty": [
   ("⚠ UNM Event Planning & Scheduling Office",
    "THE SINGLE MOST IMPORTANT NUMBER IN NEW MEXICO. Controls all SUB room and event space, "
    "sets and quotes the External Organizational Rate (unpublished on the web), and "
    "processes cancellations. SUB Suite 1094, Mon-Fri 8-5.",
    "Student Union Building",
    "subevent@unm.edu · (505) 277-5498 [direct]",
    "https://events.unm.edu/about-us/faqs.html"),
   ("Student Activities Center",
    "Runs Welcome Back Days, charters student orgs, books involvement advising. THE call "
    "for fair eligibility and fee. SUB Room 1018. Fax (505) 277-2987.",
    "Student Affairs",
    "sac@unm.edu · (505) 277-4706 [main line, SAC]",
    "https://sac.unm.edu/"),
   ("Haley Johnson",
    "Advisor / Student Activities Specialist — NAMED COORDINATOR of Welcome Back Days 2026. "
    "The person who decides whether DGD counts as a 'community agency'. No direct extension "
    "published; ask for her by name on the SAC line.",
    "Student Activities Center",
    "hagjohnson44@unm.edu · (505) 277-4706 [SAC main line — no direct extension published]",
    "https://sac.unm.edu/about/staff/index.html"),
   ("Ryan Lindquist",
    "Director, Student Activities Center — escalation above Johnson if the fair answer is "
    "no. No direct extension published.",
    "Student Activities Center",
    "depar@unm.edu · (505) 277-4706 [SAC main line — no direct extension published]",
    "https://sac.unm.edu/about/staff/index.html"),
   ("⚠ UNM Policy Office / University Counsel",
    "Interprets RPM 2.12, UAP 5250 and UAP 2220. HOLDS THE UNRETRIEVED TEXT of RPM 2.12 — "
    "the policy that actually decides whether DGD may solicit at UNM. Scholes Hall 114 A-B.",
    "Office of University Counsel",
    "(505) 277-2069 [direct]",
    "https://policy.unm.edu/university-policies/2000/2220.html"),
   ("SUB Administration Office",
    "Building-level authority above the scheduling desk — the escalation if Event Planning "
    "says no.",
    "Student Union Building",
    "(505) 277-2331 [direct]",
    "https://sub.unm.edu/assets/documents/sub-general-policy.pdf"),
   ("SUB Marketing Department",
    "Sells advertising and sponsorship INSIDE the SUB — a paid channel that sidesteps the "
    "tabling question entirely. Worth one call.",
    "Student Union Building",
    "(505) 277-7885 [direct]",
    "https://sub.unm.edu/assets/documents/sub-general-policy.pdf"),
   ("SUB Welcome Desk",
    "Day-of front line — use on the ground, not for approvals.",
    "Student Union Building",
    "(505) 277-5626 [direct]",
    "https://sub.unm.edu/assets/documents/sub-general-policy.pdf"),
   ("Student Union Project Coordinator",
    "Listed in the SUB general policy PDF; scope not described on any HTML page.",
    "Student Union Building",
    "(505) 277-0794 [direct]",
    "https://sub.unm.edu/assets/documents/sub-general-policy.pdf"),
   ("Office of Career Services",
    "Controls all three Fall 2026 career fairs. Employer registration runs through "
    "Handshake; cost and deadline are behind the employer login and unpublished. "
    "UAEC Building 85, Room 220.",
    "Career Services",
    "career4u@unm.edu · (505) 277-2531 [direct]",
    "https://career.unm.edu/students--alumni/career-fairs.html"),
   ("⚠ UNM Registrar",
    "CLOSES THE CALENDAR GAPS — add/drop, Thanksgiving and finals are all unretrievable "
    "from the web because the detailed calendar is a JavaScript widget.",
    "Office of the Registrar",
    "(505) 277-8900 [direct]",
    "https://registrar.unm.edu/academic-calendar/"),
   ("UNM Rainforest Innovations",
    "Runs the Lobo Hackathon. The hackathon is SPRING ONLY (Apr 9-10, 2026, already run) — "
    "so this is the SPRING 2027 SPONSORSHIP call, and it should be made during the fall.",
    "Technology transfer / innovation",
    "Info@innovations.unm.edu · cmichaliszyn@innovations.unm.edu · (505) 272-7900 [direct]",
    "https://innovations.unm.edu/program-activities/lobo-hackathon/"),
   ("Student Government Accounting Office",
    "Handles student-org money — relevant only if co-funding a club event.",
    "Student Affairs",
    "(505) 277-7888 [direct]",
    "https://sac.unm.edu/about/staff/index.html"),
   ("ASUNM (undergraduate student government)",
    "Chris Ruybalid, ASUNM Administrator. Undergraduate governance route.",
    "Student government",
    "cruybali@unm.edu · (505) 277-5528 [direct]",
    "https://sac.unm.edu/about/staff/index.html"),
   ("GPSA (graduate student government)",
    "Kaya Sheets, Admin Assistant. Graduate/professional route.",
    "Student government",
    "gpsaoff@unm.edu · (505) 277-3803 [direct]",
    "https://sac.unm.edu/about/staff/index.html"),
   ("Department of Computer Science",
    "Technical-audience door; also holds the CS student-org page that was never retrieved.",
    "School of Engineering",
    "(505) 277-3112 [direct]",
    "https://www.cs.unm.edu/"),
   ("(Faculty — blockchain / crypto / fintech / monetary economics)",
    "⚠ NOT CONFIRMED. NO UNM faculty member teaching or researching blockchain, "
    "cryptocurrency, digital assets or fintech could be verified on a live page. The only "
    "crypto items found were a news article on mining's environmental cost and an alumni "
    "'Lobo Living Room' conversation — neither names a researcher. DO NOT GUESS. Look up "
    "at the CS and Anderson directories.",
    "—",
    "(505) 277-3112 [CS dept] · (505) 277-6471 UNVERIFIED — use the Anderson site",
    "https://www.mgt.unm.edu/"),
   ("UNM main switchboard",
    "MAIN LINE — last resort only.",
    "—",
    "(505) 277-0111 [MAIN LINE]",
    "https://www.unm.edu/"),
 ],

 "courses": [
   ("CS 444 / 544",
    "Introduction to Cybersecurity (3 cr) — 'This class will focus on proactive security, "
    "i.e. designing networks, algorithms and data structures which are provably robust to "
    "attack.' ⚠ Sourced from the 2021-2022 catalog; the 2025-26 course-description page "
    "404s. WHETHER IT RUNS IN FALL 2026 IS UNVERIFIED.",
    "https://catalog.unm.edu/catalogs/2021-2022/colleges/engineering/computer-science/index.html"),
   ("(Blockchain / crypto / fintech course)",
    "⚠ NONE EXISTS THAT COULD BE CONFIRMED. catalog.unm.edu/search/?search=blockchain "
    "returns 404. UNM has no credit-bearing blockchain, cryptocurrency, fintech or "
    "digital-money course on any page loaded.",
    "https://catalog.unm.edu/"),
   ("(Non-credit only) Blockchain Fundamentals",
    "UNM Continuing Education RESELLS a third-party ed2go course under UNM branding. This "
    "is a vendor-hosted product with no enrolled campus cohort — NOT a UNM catalog course "
    "and NOT worth a visit. A related UNM continuing-ed blockchain page "
    "(blockchainhub360.com/unm) is marked ARCHIVED.",
    "https://www.ed2go.com/unm/online-courses/blockchain-fundamentals/"),
 ],

 "events": [
   ("⚠⚠ Welcome Back Days 2026",
    "Aug 14-21, 2026. Student Organization Day Thu Aug 20, 10am-2pm, Duck Pond (~200 orgs). "
    "Campus Employment & Community Service Day Fri Aug 21, 10am-2pm, Duck Pond — the "
    "off-campus-facing slot. Registration closes Aug 17. HAPPENING NOW.",
    "https://sac.unm.edu/events/welcome-back-days.html"),
   ("Engineering & Science Career Fair",
    "Wed Sep 9, 2026, 10am-2pm, SUB Ballrooms. Handshake registration; employer cost "
    "UNVERIFIED (behind login).",
    "https://career.unm.edu/students--alumni/career-fairs.html"),
   ("⚠ Business & Accounting Career Fair",
    "Thu Sep 24, 2026, 10am-2pm, SUB Ballrooms. THE BEST AUDIENCE-MATCHED PAID CHANNEL AT "
    "UNM — a finance-major room you can buy into rather than argue your way into. Handshake "
    "registration; cost UNVERIFIED.",
    "https://career.unm.edu/students--alumni/career-fairs.html"),
   ("Graduate & Professional School Fair",
    "Thu Oct 29, 2026, 10am-2pm, SUB Ballrooms.",
    "https://career.unm.edu/students--alumni/career-fairs.html"),
   ("⚠ Lobo Hackathon — SPRING ONLY, NOT AVAILABLE THIS TERM",
    "Apr 9-10, 2026 — ALREADY RUN, registration closed. Next cycle Spring 2027. THE "
    "HACKATHON-SPONSORSHIP LEVER DOES NOT EXIST AT UNM IN FALL 2026. Open the Spring 2027 "
    "conversation with Rainforest Innovations (505) 272-7900 during the fall.",
    "https://innovations.unm.edu/program-activities/lobo-hackathon/"),
   ("⚠ STALE PAGE — UNM employer-facing career fair page",
    "career.unm.edu/employers/career-fairs/ STILL DISPLAYS FALL 2016 DATES (Sep 14 2016, "
    "Sep 15 2016, Sep 29 2016) — TEN YEARS STALE. Two conflicting PDF calendars on the same "
    "server also fail a weekday check (one gives Sep 10 as a 'Wednesday'; it is a "
    "Thursday in 2026). USE THE STUDENT-FACING HTML PAGE, which is correct.",
    "https://career.unm.edu/employers/career-fairs/"),
   ("⚠ STALE PAGE — NM Hack",
    "nmhack.unm.edu still advertises NMHack2020, October 18 2020 — SIX YEARS STALE. It is "
    "also a HIGH SCHOOL event, not a university one. Wrong audience and dead. Ignore.",
    "https://nmhack.unm.edu/"),
   ("UNM HSC Health Hackathon",
    "Exists, health-sciences audience. Not a fintech fit. Listed only so nobody chases it.",
    "https://hsc.unm.edu/ctsc/events/hackathon/"),
 ],

 "play":
   "⚠⚠ ACT TODAY OR LOSE THE TERM'S BEST WINDOW. Welcome Back Days is running RIGHT NOW "
   "(Aug 14-21) and GENERAL REGISTRATION CLOSES MON AUG 17, 2026. Student Organization Day "
   "is Thu Aug 20 (~200 orgs, Duck Pond) and Campus Employment & Community Service Day — "
   "the slot aimed at off-campus entities — is Fri Aug 21. The SAC page says 'Departments, "
   "student organizations, AND COMMUNITY AGENCIES may participate', which is the most "
   "permissive tabling language in New Mexico, but 'community agency' is undefined and no "
   "fee is published. ONE PHONE CALL DECIDES IT: SAC (505) 277-4706, ask for Haley Johnson "
   "by name — she coordinates the event. If she says yes, Aug 21 is the single highest-value "
   "hour of the New Mexico tour. If she says no, fall back immediately to the Business & "
   "Accounting Career Fair on Sep 24 — a finance-major room you buy into rather than argue "
   "into. DO NOT, under any circumstances, ask a student club to reserve space on DGD's "
   "behalf: the CSO Booking Guidelines strip that club of its booking privileges for the "
   "year AND still charge the External Organizational Rate, so fronting is both punished and "
   "pointless here. The legitimate free move is UAP 2220 — 'scheduling to use University "
   "facilities for speech activities is not required' and 'the distribution of written "
   "materials' is expressly protected, so an ambassador may hand out literature on the open "
   "campus with no reservation at all, provided nothing is sold and no transaction is "
   "proposed. That line — leaflet freely, sell nothing — is the whole UNM strategy. Note "
   "the Lobo Hackathon is spring-only and already run, so the hackathon workaround is "
   "unavailable this term; make the Spring 2027 sponsorship call to Rainforest Innovations "
   "(505) 272-7900 while you are in town.",

 "gaps": [
   "⚠⚠ Whether a for-profit crypto project qualifies as a 'community agency' for Welcome "
   "Back Days, and what it costs — no fee published anywhere. SAC (505) 277-4706, ask for "
   "Haley Johnson. TIME-CRITICAL: registration closes Aug 17, 2026.",
   "⚠⚠ Full text of RPM 2.12 (Advertising, Sales and Solicitations) — the numbered "
   "subsections would not render on either the http or https URL; only the preamble is "
   "readable. This is the policy that actually governs whether DGD may solicit at UNM. "
   "Policy Office (505) 277-2069.",
   "⚠ UNM's External Organizational Rate card — no dollar figure is published anywhere on "
   "the web. Event Planning & Scheduling (505) 277-5498.",
   "⚠ Fall 2026 ADD/DROP DEADLINE, THANKSGIVING BREAK and FINALS WEEK — all three "
   "unretrievable. The detailed term calendar is a JavaScript widget at "
   "unmevents.unm.edu/site/academic/ that returns no dates to a fetcher, and the "
   "registrar's calendar directory (registrar.unm.edu/academic-calendar/) contains only the "
   "ten-year semester PDF; both /index.html and /fall-2026.html return 404. "
   "CALL THE REGISTRAR: (505) 277-8900.",
   "Full student-org roster — UNM Involve (unm.presence.io) is JavaScript-rendered and the "
   "SAC org page is two years stale (still shows a 'down until August 7th, 2024' banner). "
   "Only a partial list was recovered via the Presence API. Whether any blockchain, "
   "investment or FMA chapter exists is UNVERIFIED, not disproven. SAC (505) 277-4706.",
   "UNM CS department student organizations page — never loaded; likely home of any ACM "
   "chapter. https://www.cs.unm.edu/students/organizations.html",
   "Named faculty in blockchain / crypto / fintech / monetary economics — NONE confirmable "
   "on any live page. https://www.mgt.unm.edu/ and https://www.cs.unm.edu/",
   "Whether CS 444/544 Introduction to Cybersecurity actually runs in Fall 2026 — sourced "
   "from the 2021-22 catalog; current course pages 404. (505) 277-3112.",
   "Employer registration cost and deadline for all three career fairs — behind the "
   "Handshake employer login. Career Services (505) 277-2531.",
 ],
 "note": "UNM's Health Sciences Center (North Campus) is a separate population with its own "
         "welcome event (Aug 19, Domenici Center lawn). It is health-sciences only — no "
         "business or CS undergraduates. Do not spend the main-campus window there.",
},

# ══════════════════════════════════════════════════════════════════════════════
# 2. NEW MEXICO STATE UNIVERSITY
# ══════════════════════════════════════════════════════════════════════════════
{
 "state": "New Mexico",
 "name": "New Mexico State University",
 "city": "Las Cruces, NM",
 "type": "Public",
 "tier": "A — Named target",
 "access": 3,

 "start": "Wed Aug 19, 2026",
 "adddrop": "Last day to add WITHOUT instructor's signature: Aug 20, 2026. WITH signature: "
            "Aug 28, 2026. CENSUS (last day to cancel registration without a W): Sep 4, "
            "2026. Last day to withdraw from a single course with 'W': Oct 15, 2026.",
 "fallbreak": "⚠ NONE — there is NO October fall break at NMSU in Fall 2026. Indigenous "
              "People's Day (Oct 12) carries special programming but CLASSES CONTINUE.",
 "thanksgiving": "⚠ Nov 23-27, 2026 — THE FULL WEEK, offices closed. The longest "
                 "Thanksgiving closure of the six New Mexico campuses.",
 "lastclass": "Fri Dec 11, 2026",
 "finals": "Dec 7-11, 2026 — ⚠ note finals COINCIDE with the final instructional week "
           "rather than following it. Commencement Dec 11-12.",
 "cal_url": "https://records.nmsu.edu/academic-calendar/2026.html",
 "cal_status": "CONFIRMED",

 "fair": "Crimson Kickoff (welcome-week umbrella); Aggie Carnival is the org-fair analogue",
 "fair_date": "⚠ UNVERIFIED FOR FALL 2026 — crimsonkickoff.nmsu.edu publishes the schedule "
              "AS AN IMAGE FILE with no text alternative, and the page footer reads 2025. "
              "NOT ONE Fall 2026 Crimson Kickoff date could be confirmed. PATTERN (from the "
              "confirmed Fall 2025 cycle): runs roughly two weeks from move-in through the "
              "first week and a half of classes (Aug 15-30 in 2025); the org-fair analogue "
              "is the AGGIE CARNIVAL, 11am-2pm, International Mall (Aug 27 in 2025). Will "
              "post at crimsonkickoff.nmsu.edu and on Crimson Connection. "
              "ONE FALL 2026 DATE IS CONFIRMED: Student Employment Fair, Tue Aug 25, 2026, "
              "10am-1pm, Aggie Lounge, Corbett Center.",
 "fair_outside": "NOT ADDRESSED on any Crimson Kickoff page. Governed instead by ARP 14.92, "
                 "which DOES permit sponsored outside vendors — see policy_key. Tabling "
                 "requests are submitted as event forms through Crimson Connection and "
                 "administered by SILP.",
 "fair_cost": "UNVERIFIED — not published. SILP (575) 646-3200.",
 "fair_deadline": "UNVERIFIED — but ARP 14.92 requires departmental requests at least 2 "
                  "WEEKS prior, so budget a minimum two-week lead.",
 "fair_url": "https://crimsonkickoff.nmsu.edu/",

 "policy": "ARP 14.92 Sales and Solicitation (eff. 04-12-2019) · ARP 3.63 Freedom of "
           "Expression (revised 07-21-2015, replicated 10-21-2015)",
 "policy_url": "https://arp.nmsu.edu/chapter-14/14-92.html",
 "policy_key":
   "⚑ NMSU IS THE ONLY NEW MEXICO CAMPUS WHOSE WRITTEN POLICY EXPRESSLY AUTHORISES A "
   "SPONSORED OUTSIDE VENDOR. ARP 14.92 defines solicitation as 'THE ACT OF SELLING OR "
   "ENCOURAGING THE PURCHASE OF A PRODUCT EITHER DIRECTLY OR INDIRECTLY' — note 'or "
   "indirectly', which is broad enough to capture promotional crypto outreach even with no "
   "on-site transaction. Baseline: commercial advertising and solicitation are GENERALLY "
   "PROHIBITED, with narrow exceptions (media advertising, donated property bearing donor "
   "names, and in-person solicitation BY DIRECT INVITATION ONLY). THE CURE: outside vendors "
   "may conduct sales on campus ONLY WHEN 'SPONSORED BY A RECOGNIZED CAMPUS ORGANIZATION OR "
   "A UNIVERSITY DEPARTMENT', with PRIOR WRITTEN APPROVAL FROM THE DIRECTOR OF STUDENT "
   "INVOLVEMENT AND LEADERSHIP PROGRAMS. Process: student organisations file an ACTIVITY "
   "REGISTRATION FORM; departments submit written requests to the vice president for "
   "student enrollment and success AT LEAST 2 WEEKS PRIOR. "
   "ANTI-FRONTING — WEAK FORM ONLY, and it does not block this route: organisations "
   "'incorporated outside the university which raise funds for a University Department' "
   "must confer with the vice president for university advancement before fundraising. "
   "That is a FUNDRAISING provision; it is NOT a general bar on a student org hosting an "
   "outside entity. Contrast UNM, where fronting strips the club of its privileges. "
   "ARP 3.63 (Freedom of Expression) applies to 'ALL PEOPLE' across NMSU property — "
   "external parties receive the same protection as university members in designated "
   "forums — BUT IT EXPRESSLY CARVES OUT COMMERCIAL SPEECH: 'SPEECH THAT PROPOSES A "
   "COMMERCIAL TRANSACTION' is excluded from 3.63 and governed by 14.92 instead. So the "
   "expressive-activity shelter that works at UNM does NOT cover a sales pitch here. "
   "Forum taxonomy is three-tier (traditional public / limited public / non-public) — NMSU "
   "uses FORUM CLASSIFICATION RATHER THAN FENCED FREE-SPEECH ZONES. Thresholds: activities "
   "drawing 250+ participants require advance written notification; permits required for "
   "anything closing roads or parking. Amplification allowed '8:00 a.m. to 7:00 p.m., "
   "Sunday through Thursday; 8:00 a.m. to midnight Friday and Saturday'. Signage permitted "
   "24 hours pre/post event without permit. "
   "⚠ NO FEE SCHEDULE, NO INSURANCE REQUIREMENT, NO CREDIT-CARD OR PAYMENT-APP LANGUAGE AND "
   "NO ON-SITE-CONTRACT RESTRICTION appear in the retrieved text — all four are UNVERIFIED "
   "rather than absent. Confirm with SILP (575) 646-3200. "
   "⚠ NO NEW MEXICO CAMPUS FREE-SPEECH STATUTE EXISTS. ARP 3.63 grounds itself in the "
   "First Amendment and the NEW MEXICO CONSTITUTION — not in any state statute. A land-grant "
   "university writing a dedicated expression policy would cite a controlling statute if one "
   "existed. There is no FORUM-Act equivalent in New Mexico to invoke.",
 "sponsor_required": "⚠ YES — AND THIS IS GOOD NEWS, NOT A BARRIER. A recognised campus "
                     "organisation OR a university department must sponsor, plus prior "
                     "WRITTEN approval from the SILP director. Unlike UNM, this route is "
                     "expressly authorised rather than penalised. Best sponsor: the "
                     "Financial Management Association. Budget 2+ weeks.",

 "clubs": [
   ("⚠ DIRECTORY IS UNREADABLE — read this before trusting any negative below",
    "Crimson Connection (crimsonconnection.nmsu.edu) is a JavaScript-rendered application "
    "that returns only 'This application requires JavaScript to be enabled', and org pages "
    "are login-gated. THE DIRECTORY COULD NOT BE ENUMERATED. Do not let anyone claim a "
    "complete NMSU club list from the web.",
    "https://crimsonconnection.nmsu.edu/"),
   ("⚠ Financial Management Association",
    "THE ONLY FMA CHAPTER FOUND IN NEW MEXICO, and the single best sponsorship partner in "
    "the state under ARP 14.92. Org page confirmed to exist at a live URL via the public "
    "search index; ACTIVITY STATUS NOT VERIFIABLE because the page is JS-gated. Note the "
    "URL slug reads 'financestudentassociation' while the display name is 'Financial "
    "Management Association' — likely a renamed finance student association.",
    "https://crimsonconnection.nmsu.edu/organization/financestudentassociation"),
   ("(Blockchain / crypto / Web3 club)",
    "NONE CONFIRMED — but the directory is unreadable, not empty. UNVERIFIED, not "
    "established absence. Ask SILP to read out the org list by category: (575) 646-3200.",
    "https://crimsonconnection.nmsu.edu/"),
   ("(ACM chapter)",
    "NOT CONFIRMED — same directory limitation. NMSU offers CS specialisations in AI, "
    "cybersecurity and software development, so a chapter is plausible. Ask SILP.",
    "https://catalogs.nmsu.edu/nmsu/arts-sciences/computer-science/"),
 ],

 "faculty": [
   ("⚠ Carlos Cuesta",
    "PROGRAM DIRECTOR, NUSENDA FINTECH LAB at Arrowhead Center — THE HIGHEST-VALUE CONTACT "
    "IN NEW MEXICO. This is the ONLY unit in the entire NM higher-ed system that names "
    "'Digital Assets' as a published program focus area (alongside Payments, Alternative "
    "Lending, Capital Markets, Consumer Finance, RegTech, WealthTech). The lab offers "
    "mentorship and 'payment integration education'. No direct extension published — reach "
    "him by email or via the Arrowhead main line.",
    "Arrowhead Center — Nusenda FinTech Lab",
    "carlosic@nmsu.edu · (575) 646-7415 [Arrowhead Center main line — no direct extension "
    "published]",
    "https://arrowheadcenter.nmsu.edu/program/nusenda_fintech_lab/index.html"),
   ("Arrowhead Center",
    "NMSU's innovation/entrepreneurship arm, host of the Nusenda FinTech Lab. 3655 Research "
    "Rd, Las Cruces NM 88003. ⚠ Its EVENTS CALENDAR IS STALE — most recent entries are "
    "Feb/Mar 2024 with older 2019 items, and NO Fall 2026 events are posted. The program "
    "page is current; the calendar is not. Contact the director directly.",
    "Arrowhead Center",
    "arrowheadcenter@nmsu.edu · (575) 646-7415 [direct]",
    "https://arrowheadcenter.nmsu.edu/program/nusenda_fintech_lab/calendar_of_events/index.html"),
   ("⚠ Dr. Fred Martino",
    "Assistant Director, Student Activities / Student Media Advisor — THE PERSON WHO "
    "PROCESSES SPONSORED-OUTSIDE-VENDOR REQUESTS under ARP 14.92. Corbett Center Room 205.",
    "Student Involvement & Leadership Programs",
    "martinof@nmsu.edu · (575) 646-3200 [SILP main line]",
    "https://silp.nmsu.edu/contact-us.html"),
   ("Student Involvement & Leadership Programs (SILP)",
    "Administers tabling approvals, Activity Registration Forms, Crimson Kickoff and the "
    "org directory. THE call for both the fair date and the vendor route. Corbett Center "
    "Room 205.",
    "Student Affairs",
    "silp@nmsu.edu · (575) 646-3200 [main line, SILP]",
    "https://silp.nmsu.edu/contact-us.html"),
   ("Michelle Grandjean",
    "Interim Assistant Vice President of Student Life and Involvement — escalation above "
    "Martino.",
    "Student Life & Involvement",
    "m_rogers@nmsu.edu · (575) 646-3200 [SILP main line]",
    "https://studentlife.nmsu.edu/our-team.html"),
   ("Rose Carbajal",
    "SILP Administrative Assistant — the person who actually books time with Martino or "
    "Grandjean.",
    "Student Involvement & Leadership Programs",
    "rocarbaj@nmsu.edu · (575) 646-3200 [SILP main line]",
    "https://silp.nmsu.edu/contact-us.html"),
   ("Karo Ademilla",
    "Leadership, Engagement & Traditions Coordinator — owns Crimson Kickoff programming.",
    "Student Involvement & Leadership Programs",
    "karo3@nmsu.edu · (575) 646-3200 [SILP main line]",
    "https://silp.nmsu.edu/contact-us.html"),
   ("Dr. Sam Woorley",
    "ASNMSU Advisor — the student-government sponsorship route, an alternative to a club "
    "sponsor under ARP 14.92.",
    "Associated Students of NMSU",
    "sworley@nmsu.edu · (575) 646-4415 [direct]",
    "https://silp.nmsu.edu/contact-us.html"),
   ("Jessica Arroyos",
    "ASNMSU Administrative Assistant.",
    "Associated Students of NMSU",
    "jazz1@nmsu.edu · (575) 646-4415 [direct]",
    "https://silp.nmsu.edu/contact-us.html"),
   ("Dr. Ann Coombes Goodman",
    "DEAN OF STUDENTS — policy escalation if SILP declines. Corbett Center Suite 207.",
    "Office of the Dean of Students",
    "dos@nmsu.edu · (575) 646-1722 [direct]",
    "https://studentlife.nmsu.edu/our-team.html"),
   ("Nicki Halopka",
    "Sr. Associate Dean of Students.",
    "Office of the Dean of Students",
    "nhalopka@nmsu.edu · (575) 646-1722 [direct]",
    "https://studentlife.nmsu.edu/our-team.html"),
   ("Josh Taylor",
    "Associate Dean of Students / Student Conduct Officer — interprets what counts as a "
    "solicitation violation.",
    "Office of the Dean of Students",
    "joshjt@nmsu.edu · (575) 646-1722 [direct]",
    "https://studentlife.nmsu.edu/our-team.html"),
   ("Jana Williams",
    "Program Manager, Sr., Dean of Students office.",
    "Office of the Dean of Students",
    "janaw@nmsu.edu · (575) 646-1722 [direct]",
    "https://studentlife.nmsu.edu/our-team.html"),
   ("Will Waller",
    "Assistant Vice President of Student Health and Wellbeing.",
    "Student Affairs",
    "wwaller@nmsu.edu · (575) 646-1512 [direct]",
    "https://studentlife.nmsu.edu/our-team.html"),
   ("Xavier Dominguez",
    "Coordinator of Communications and Technology, Student Life.",
    "Student Life",
    "xavierd2@nmsu.edu · (575) 646-1233 [direct]",
    "https://studentlife.nmsu.edu/our-team.html"),
   ("NMSU Conference Services",
    "Corbett Center space reservations — the paid rental track, separate from the ARP 14.92 "
    "vendor route. ⚠ EXTERNAL RATE SCHEDULES ARE NOT PUBLISHED ANYWHERE ON THE WEB.",
    "Conference Services",
    "conference@nmsu.edu · (575) 646-4805 [direct]",
    "https://services.nmsu.edu/ccsu/meeting-events.html"),
   ("Corbett Center Student Union / Auxiliary Services",
    "Student union building authority. CCSU Third floor, Suite 317, Mon-Fri 8-5.",
    "Auxiliary Services",
    "auxservices@nmsu.edu · (575) 646-1839 [direct]",
    "https://services.nmsu.edu/ccsu/index.html"),
   ("NMSU Marketing & Communications",
    "University communications — useful only for press.",
    "University Communications",
    "ucomm@nmsu.edu · (575) 646-3221 [direct]",
    "https://newsroom.nmsu.edu/"),
   ("(Faculty — blockchain / crypto / monetary economics)",
    "⚠ NOT CONFIRMED. No individual NMSU faculty member researching blockchain or "
    "cryptocurrency could be verified on a live page. DO NOT GUESS — the Nusenda FinTech "
    "Lab is the confirmed institutional door instead. Look up at the Finance and CS "
    "department directories.",
    "College of Business / Arts & Sciences",
    "(575) 646-7415 [Arrowhead — start here instead]",
    "https://catalogs.nmsu.edu/nmsu/business/finance/"),
 ],

 "courses": [
   ("(Blockchain / crypto / fintech course)",
    "⚠ UNVERIFIED — COULD NOT BE CONFIRMED OR EXCLUDED. The BFIN (Business Finance) course "
    "listing and the Finance program page both returned navigation shells with no course "
    "descriptions; catalogs.nmsu.edu/nmsu/course-listings/cs/ returns 404; and THE NMSU "
    "CATALOG SEARCH ENDPOINT (catalogs.nmsu.edu/search/) IS DISALLOWED BY ROBOTS.TXT. "
    "Given the Nusenda FinTech Lab exists on this campus, a fintech course is plausible. "
    "Ask Carlos Cuesta, carlosic@nmsu.edu.",
    "https://catalogs.nmsu.edu/nmsu/course-listings/bfin/"),
   ("CS — AI / Cybersecurity / Software Development tracks",
    "CONFIRMED structurally: NMSU offers CS bachelor's specialisations in artificial "
    "intelligence, cybersecurity and software development. Individual course codes not "
    "retrieved.",
    "https://catalogs.nmsu.edu/nmsu/arts-sciences/computer-science/"),
 ],

 "events": [
   ("Student Employment Fair",
    "Tue Aug 25, 2026, 10am-1pm, Aggie Lounge, 1st Floor, Corbett Center. The one CONFIRMED "
    "Fall 2026 welcome-window date at NMSU.",
    "https://oel.nmsu.edu/career-events/career-fairs--future-dates.html"),
   ("⚠ Career Expo",
    "Tue-Wed Sep 15-16, 2026, 9am-2pm, 3rd Floor Ballrooms, Corbett Center. NMSU's largest "
    "employer event and the best audience-matched paid channel here.",
    "https://oel.nmsu.edu/career-events/career-fairs--future-dates.html"),
   ("Engineering, Science and Technology Fair",
    "Wed Sep 16, 2026, 9am-2pm, 3rd Floor Ballrooms, Corbett Center. Runs concurrent with "
    "day 2 of Career Expo.",
    "https://oel.nmsu.edu/career-events/career-fairs--future-dates.html"),
   ("Graduate and Professional School Fair",
    "Wed Oct 7, 2026, 10am-2pm, Aggie Lounge & 1st Floor, Corbett Center.",
    "https://oel.nmsu.edu/career-events/career-fairs--future-dates.html"),
   ("Health Professions Career Fair",
    "Wed Nov 4, 2026, 2-5pm, Aggie Lounge, Corbett Center. Low relevance — listed for "
    "calendar completeness only.",
    "https://oel.nmsu.edu/career-events/career-fairs--future-dates.html"),
   ("⚠ Nusenda FinTech Lab (Arrowhead Center)",
    "NOT AN EVENT — a standing accelerator, and the state's only digital-assets-adjacent "
    "academic program. Focus areas published as: Alternative Lending, Capital Markets, "
    "Consumer Finance, DIGITAL ASSETS, Financial Services IT, Payments, RegTech, WealthTech. "
    "⚠ Its events calendar is STALE to early 2024 and shows nothing for Fall 2026 — contact "
    "the director rather than relying on it.",
    "https://arrowheadcenter.nmsu.edu/program/nusenda_fintech_lab/index.html"),
   ("(Hackathon)",
    "NONE CONFIRMED for Fall 2026 at NMSU. NMSU teams have historically placed at a "
    "statewide hackathon but no NMSU-hosted Fall 2026 event was found. UNVERIFIED.",
    "https://arrowheadcenter.nmsu.edu/"),
 ],

 "play":
   "⚑ THIS IS THE BEST DOOR IN NEW MEXICO, and the access rating of 3 understates it — the "
   "gate is real but it is DOCUMENTED AND PASSABLE, which is more than any other campus in "
   "the state offers. ARP 14.92 expressly permits an outside vendor to operate on campus "
   "when 'sponsored by a recognized campus organization or a University Department' with "
   "prior written approval from the SILP director. Unlike UNM — where having a club front "
   "for you strips that club of its booking privileges — NMSU's policy contemplates exactly "
   "this arrangement and tells you how to file it. THE PLAY IS TWO CALLS, IN THIS ORDER. "
   "FIRST call Arrowhead Center (575) 646-7415 and ask for Carlos Cuesta, director of the "
   "Nusenda FinTech Lab — this is the only unit in New Mexico higher education that names "
   "DIGITAL ASSETS as a published program focus, and a warm relationship there is worth "
   "more than any table. Lead with the FinTech Lab, not with tabling. SECOND call SILP "
   "(575) 646-3200 and ask for Dr. Fred Martino, who processes sponsored-vendor requests; "
   "recruit the Financial Management Association (the only FMA chapter in the state) as "
   "sponsor, have them file an Activity Registration Form naming DGD, and budget a MINIMUM "
   "TWO WEEKS of lead time. Target the Career Expo window of Sep 15-16 or the Crimson "
   "Kickoff carnival, whose Fall 2026 date is not yet published. Two calendar warnings: "
   "NMSU has NO October fall break, so the whole of October is workable; and it closes the "
   "ENTIRE Thanksgiving week (Nov 23-27), the longest closure in the state.",

 "gaps": [
   "⚠⚠ Crimson Kickoff Fall 2026 dates — INCLUDING THE AGGIE CARNIVAL, the org-fair "
   "analogue. crimsonkickoff.nmsu.edu publishes its schedule as an IMAGE with no text "
   "alternative and the footer reads 2025. Not one Fall 2026 date confirmed. "
   "SILP (575) 646-3200.",
   "⚠ Fee schedule, insurance requirement, deposit and cancellation terms under ARP 14.92 — "
   "none appear in the retrieved policy text. UNVERIFIED rather than absent. "
   "SILP (575) 646-3200.",
   "⚠ Corbett Center external-organisation rate card — no rates published anywhere. "
   "Conference Services (575) 646-4805.",
   "Full student-org roster — Crimson Connection is JavaScript-rendered and login-gated; "
   "only the FMA chapter could be confirmed to exist, and even its ACTIVE STATUS is "
   "unverifiable. Whether NMSU has a blockchain, crypto or ACM club is UNVERIFIED, not "
   "disproven. Ask SILP (575) 646-3200 to read the list out by category.",
   "Whether NMSU offers any fintech/blockchain course — the BFIN listing returned a "
   "navigation shell and THE CATALOG SEARCH ENDPOINT IS ROBOTS-BLOCKED. "
   "Ask Carlos Cuesta, carlosic@nmsu.edu.",
   "Named faculty in blockchain / crypto / monetary economics — none confirmable. "
   "https://catalogs.nmsu.edu/nmsu/business/finance/",
   "Nusenda FinTech Lab Fall 2026 programming — the program page is current but its events "
   "calendar is stale to early 2024. carlosic@nmsu.edu · (575) 646-7415.",
   "Any Fall 2026 NMSU-hosted hackathon — none found. UNVERIFIED.",
   "Career fair employer registration cost and deadline — not published.",
 ],
},

# ══════════════════════════════════════════════════════════════════════════════
# 3. NEW MEXICO INSTITUTE OF MINING AND TECHNOLOGY
# ══════════════════════════════════════════════════════════════════════════════
{
 "state": "New Mexico",
 "name": "New Mexico Institute of Mining and Technology",
 "city": "Socorro, NM",
 "type": "Public",
 "tier": "B — Regional",
 "access": 3,

 "start": "Mon Aug 17, 2026",
 "adddrop": "Last day to add to waitlist: Aug 21, 2026. Last day to drop without "
            "permission: Aug 25, 2026.",
 "fallbreak": "None listed as a separate break",
 "thanksgiving": "Nov 23-27, 2026 (full week)",
 "lastclass": "Thu Dec 3, 2026",
 "finals": "Dec 7-11, 2026 — ⚠ the WIDEST last-class-to-finals gap of the six NM campuses "
           "(a genuine reading break Dec 4-6)",
 "cal_url": "https://docs.google.com/spreadsheets/d/11m7XFlZc77ZjqjDMsmVdtnUW3VpTgklC4CCw1taiOfc/edit",
 "cal_status": "PARTIAL",

 "fair": "None published",
 "fair_date": "⚠ NONE FOUND. No Fall 2026 involvement fair, club fair or welcome-week "
              "tabling event is published anywhere on nmt.edu or techConnect, AND NO "
              "RECURRING PATTERN IS DOCUMENTED EITHER — so there is not even a historical "
              "shape to plan against. The catalog's student-activities page says only 'A "
              "host of student clubs, organizations, and activities flourish at Tech.' "
              "Would post at techconnect.nmt.edu or nmt.edu/sga/clubs.php. "
              "Call Student Affairs (575) 835-5880.",
 "fair_outside": "UNVERIFIED — no fair, and no policy on outside participation either.",
 "fair_cost": "",
 "fair_deadline": "",
 "fair_url": "https://techconnect.nmt.edu/",

 "policy": "⚠ NONE EXISTS — no campus solicitation, facility-use, freedom-of-expression or "
           "space-reservation policy is published by New Mexico Tech",
 "policy_url": "https://www.nmt.edu/policies/index.php",
 "policy_key":
   "⚑ MAJOR FINDING — THERE IS NOTHING TO QUOTE, AND THAT IS THE FINDING. NEW MEXICO TECH "
   "PUBLISHES NO SOLICITATION POLICY, NO FACILITY-USE POLICY, NO FREEDOM-OF-EXPRESSION "
   "POLICY AND NO SPACE-RESERVATION POLICY. I read the complete institutional policy index, "
   "which enumerates policies across five offices (President, Administration & Finance, "
   "Academic Affairs, Student Affairs, Research). THE ENTIRE SET OF ADJACENT ITEMS IS: "
   "AF-02.1-2024 Purchasing Policy (INBOUND PROCUREMENT — does not govern outside entities "
   "on campus); Purchase Card Policy (10/31/2017); Gas Card Policy (02/10/2015); "
   "AF-01.1-2024 Alterations, Renovations and Modifications of Building and Space "
   "(CONSTRUCTION, not events); OP-05.1-2024 Web Policies and Standards; SA-03.1-2025 "
   "Student Code of Conduct; SA-06.1-2025 Hazing Discipline and Prevention. NONE of these "
   "reaches a non-university entity distributing materials, tabling or soliciting students. "
   "The catalog's policy landing page offers only aspirational language — policies exist to "
   "'ensure coordinated compliance with applicable laws and regulations, to promote "
   "operational efficiencies, to enhance the Institute mission' with emphasis on 'academic "
   "freedom, freedom of expression, shared governance' — and links onward without text. The "
   "Student Handbook page (nmt.edu/studentlife/handbook.php) RETURNS 404. "
   "⚠ THIS CUTS BOTH WAYS AND THE AMBASSADOR MUST UNDERSTAND BOTH SIDES. As a public "
   "institution NMT is bound by First Amendment public-forum doctrine whether or not it has "
   "written that down. With no published policy there is NO FEE SCHEDULE TO PAY, NO FORM TO "
   "FILE, NO INSURANCE LIMIT TO MEET AND NO ANTI-FRONTING RULE TO TRIP OVER — but equally "
   "NO DOCUMENTED RIGHT TO POINT AT WHEN TOLD NO. Access is a DISCRETIONARY PHONE DECISION "
   "by the Dean of Students / Student Affairs, and it is high-variance: a yes in one call, "
   "or an unappealable no. NOTHING can be quoted verbatim because nothing exists to quote. "
   "Absent, not merely unfound: free-speech-zone rules, insurance requirements, deposits, "
   "cancellation terms, commercial-solicitation bans, payment-credential language. "
   "⚠ NO NEW MEXICO CAMPUS FREE-SPEECH STATUTE EXISTS EITHER — so at NMT there is neither a "
   "state statute nor an institutional policy conferring any forum right. The First "
   "Amendment is literally the only thing an ambassador can cite here.",
 "sponsor_required": "UNKNOWN — no policy exists to require or excuse sponsorship. In "
                     "practice, route through a club (Cybersecurity Club is the strongest) "
                     "and let the club ask Student Affairs, (575) 835-5880.",

 "clubs": [
   ("⚠ DIRECTORY IS FULLY PUBLIC AND READABLE — the only one of the six",
    "techconnect.nmt.edu/club_signup?view=all returns all 120 groups in plain HTML, no "
    "JavaScript and no login. The clubs below are a genuine enumeration, unlike UNM, NMSU "
    "and NMHU where the directory is unreadable.",
    "https://techconnect.nmt.edu/club_signup?view=all"),
   ("⚠ NMT Cybersecurity Club",
    "STRONGEST PARTNER AT NMT. Confirmed active on BOTH techConnect AND the SGA clubs page "
    "— the only club with two independent confirmations. Crypto-literate audience, direct "
    "email published. Contact: cybersecurityclub@npe.nmt.edu",
    "https://www.nmt.edu/sga/clubs.php"),
   ("⚠ Association for Computing Machinery (ACM)",
    "DISCREPANCY — FLAG THIS. ACM appears on techConnect ('leading learned society for "
    "computing', focused on enhancing ACM visibility at NMT) but DOES NOT APPEAR on the "
    "SGA's own clubs page, which lists Cybersecurity Club, IEEE and Entrepreneurship Club. "
    "The SGA page carries its own warning: 'The websites listed may be out of date, so the "
    "emails listed are the most current.' Either ACM is DORMANT and lingering on "
    "techConnect, or the SGA page is incomplete. VERIFY BEFORE BUILDING A PLAN AROUND IT.",
    "https://techconnect.nmt.edu/club_signup?view=all"),
   ("Entrepreneurship Club",
    "Listed on BOTH techConnect and the SGA page. No email published. The closest "
    "business-adjacent group on campus — NMT has no finance or economics club at all.",
    "https://www.nmt.edu/sga/clubs.php"),
   ("NMT Inventors & Entrepreneurs",
    "Listed on techConnect. Second entrepreneurship-flavoured group.",
    "https://techconnect.nmt.edu/club_signup?view=all"),
   ("NMT Game Dev Club",
    "Listed on techConnect. Technical build-oriented audience.",
    "https://techconnect.nmt.edu/club_signup?view=all"),
   ("IEEE",
    "Active, confirmed on both lists. Contact: ieee@npe.nmt.edu",
    "https://www.nmt.edu/sga/clubs.php"),
   ("NM Cybersecurity Center for Excellence",
    "Listed on techConnect — an INSTITUTIONAL CENTER, not a student club. Potentially a "
    "research/speaking door rather than a tabling one.",
    "https://techconnect.nmt.edu/club_signup?view=all"),
   ("NMT Physics Club",
    "Active. physics.club@npe.nmt.edu. Quantitative audience.",
    "https://www.nmt.edu/sga/clubs.php"),
   ("QuASAR",
    "Listed on the SGA page. nmtquasar@npe.nmt.edu",
    "https://www.nmt.edu/sga/clubs.php"),
   ("Graduate Student Association",
    "Listed on techConnect.",
    "https://techconnect.nmt.edu/club_signup?view=all"),
   ("(Blockchain / crypto / finance / economics club)",
    "NONE — and here the negative is RELIABLE, because the full 120-group list is public "
    "and readable. NMT has no blockchain, crypto, Web3, finance, investment, economics, "
    "data-science or FMA group. The Entrepreneurship Club is the closest match.",
    "https://techconnect.nmt.edu/club_signup?view=all"),
 ],

 "faculty": [
   ("⚠ Division of Student Affairs / Student Life",
    "THE NUMBER THAT MATTERS AT NMT. Includes Student Leadership & Engagement AND the Dean "
    "of Students. WITH NO WRITTEN POLICY IN EXISTENCE, THIS OFFICE *IS* THE POLICY — the "
    "discretionary yes or no on outside-entity access is made here. Fidel Student Center, "
    "Suite 236. ⚠ Named Student Leadership & Engagement staff are NOT published anywhere "
    "and the Dean of Students page 404s — ask for people by role on this line, do not guess "
    "names.",
    "Student Affairs",
    "studentlife@npe.nmt.edu · (575) 835-5880 [main line, Student Affairs]",
    "https://www.nmt.edu/studentlife/"),
   ("Office of the Registrar",
    "Confirms the Fall 2026 calendar (sourced from a Google Sheet with at least one stray "
    "2025 row) and can answer whether cryptography coursework runs. Fidel Student Center, "
    "2nd floor Room 285, 801 Leroy Place, Socorro NM 87801. Fax (575) 835-6511.",
    "Office of the Registrar",
    "registrar@nmt.edu · (575) 835-5133 [main line] · 1-800-428-TECH ext. 6 [toll-free]",
    "https://www.nmt.edu/registrar/"),
   ("Heather Juarez",
    "INSTITUTION REGISTRAR — direct extension published, unusual for a campus this size.",
    "Office of the Registrar",
    "registrar@nmt.edu · (575) 835-5116 [direct]",
    "https://www.nmt.edu/registrar/"),
   ("Associate Registrar (POSITION VACANT)",
    "Listed as vacant on the live page — the line rings but nobody holds the role. Noted so "
    "nobody wastes a call.",
    "Office of the Registrar",
    "(575) 835-5830 [direct — POSITION VACANT]",
    "https://www.nmt.edu/registrar/"),
   ("Steph Moore",
    "Institutional Researcher.",
    "Office of the Registrar",
    "(575) 835-5128 [direct]",
    "https://www.nmt.edu/registrar/"),
   ("Alicia Romero",
    "Course Transfer Evaluator.",
    "Office of the Registrar",
    "(575) 835-5559 [direct]",
    "https://www.nmt.edu/registrar/"),
   ("Hezekiah Oxford",
    "Course Transfer Evaluator.",
    "Office of the Registrar",
    "(575) 835-5473 [direct]",
    "https://www.nmt.edu/registrar/"),
   ("Michael Jackson",
    "Academic Affairs contact — email only; NO PHONE IS PUBLISHED for Academic Affairs "
    "anywhere on nmt.edu.",
    "Office of Academic Affairs",
    "michael.jackson@nmt.edu · no phone published",
    "https://www.nmt.edu/academicaffairs/AA_Calendar.php"),
   ("(Faculty — cryptography / distributed systems / blockchain)",
    "⚠ NOT CONFIRMED. Every route into the CSE department FAILED: nmt.edu/cse/ 404s, "
    "nmt.edu/academics/cs/index.php 404s, and catalog.nmt.edu/departments/CSE/overview "
    "returned the catalog homepage shell rather than department content. The department "
    "IS confirmed to exist as 'CSE Computer Science & Engineering'. DO NOT GUESS NAMES — "
    "retry the department URL in a browser or call the registrar.",
    "Computer Science & Engineering",
    "(575) 835-5133 [Registrar main line — use to reach the CSE dept]",
    "https://catalog.nmt.edu/departments/CSE/overview"),
 ],

 "courses": [
   ("(Cryptography / distributed systems course)",
    "⚠ UNVERIFIED — A SPECIFIC TARGET OF THIS RESEARCH THAT COULD NOT BE CLOSED. NMT's "
    "catalog is a Coursedog instance whose course-listing routes 404 (/courses/cse, "
    "/coursesaz), and catalog.nmt.edu/scheduleofcourses merely redirects to a Banner search "
    "at banweb7.nmt.edu requiring a term+subject selection no fetcher can make. Given NMT "
    "runs a Cybersecurity degree program, applied-cryptography coursework is LIKELY TO "
    "EXIST. Absence here means unreadable catalog, NOT no course. "
    "Call the Registrar (575) 835-5133.",
    "https://catalog.nmt.edu/scheduleofcourses"),
   ("Cybersecurity (degree program)",
    "CONFIRMED to exist as a department/program in the catalog's department list. The "
    "strongest structural signal that cryptography is taught here.",
    "https://catalog.nmt.edu/departments"),
   ("Business and Technology Management (department)",
    "CONFIRMED to exist in the catalog's department list — NMT's only business-side "
    "academic unit and the plausible home of any fintech content.",
    "https://catalog.nmt.edu/departments"),
   ("Computer Science & Engineering (department)",
    "CONFIRMED to exist. Course list not retrievable.",
    "https://catalog.nmt.edu/departments/CSE/overview"),
 ],

 "events": [
   ("(All events)",
    "⚠ NONE FOUND for Fall 2026. No career fair, no hackathon, no speaker series and no "
    "entrepreneurship week is published on nmt.edu in retrievable form. A 'Career Services' "
    "group exists on techConnect but posts no event dates. This is a coverage gap as much "
    "as a finding — NMT publishes very little, and the search budget was exhausted before "
    "this could be pushed further. Call Student Affairs (575) 835-5880.",
    "https://techconnect.nmt.edu/"),
 ],

 "play":
   "⚑ BEST AUDIENCE IN THE STATE, THINNEST INSTITUTION — go, but go through a club and go "
   "by phone. NMT's ~2,000 students are the most quantitatively capable population in New "
   "Mexico and the natural audience for a cryptography-and-consensus conversation. But the "
   "institution publishes almost nothing: NO solicitation policy, NO facility-use policy, "
   "NO freedom-of-expression policy, NO involvement fair, NO events and NO retrievable "
   "course catalog. That absence is genuinely double-edged. There is no fee to pay, no form "
   "to file, no insurance limit and no anti-fronting rule to violate — but there is also no "
   "documented right to invoke if someone says no, and with New Mexico having no campus "
   "free-speech statute, the First Amendment is literally all you can cite. DO NOT PLAN A "
   "TABLE HERE. The play is a TALK, hosted by a club: email the NMT Cybersecurity Club at "
   "cybersecurityclub@npe.nmt.edu — it is the only club confirmed active on two independent "
   "lists, and its members are exactly the audience — and offer a technical session on "
   "consensus or cryptographic primitives, not a product pitch. This crowd will punish a "
   "sales pitch and reward substance. Back it with one call to Student Affairs at "
   "(575) 835-5880, which with no written policy IS the policy. Treat ACM with caution: it "
   "is listed on techConnect but absent from the SGA's own clubs page, so it may be "
   "dormant. Socorro is a 75-mile detour south of Albuquerque — pair it with the UNM leg "
   "rather than making a dedicated trip.",

 "gaps": [
   "⚠⚠ Whether outside-entity access is permitted AT ALL — no policy exists, so this is a "
   "purely discretionary decision and a single call determines whether the stop is viable. "
   "Student Affairs (575) 835-5880.",
   "⚠ Whether the ACM chapter is actually ACTIVE — listed on techConnect but ABSENT from "
   "the SGA clubs page, which warns its own data may be out of date. A specific target of "
   "this research. (575) 835-5880, or email cybersecurityclub@npe.nmt.edu who will know.",
   "⚠ Cryptography and distributed-systems coursework — a specific target that COULD NOT BE "
   "CLOSED. Every catalog route 404s and the schedule sits behind a Banner term/subject "
   "picker at banweb7.nmt.edu. Registrar (575) 835-5133.",
   "Fall 2026 dates need a 60-second phone confirmation — they come from the registrar's "
   "Google Sheet, which contains at least one row reading 11/23/2025 adjacent to 2026 "
   "entries. Both HTML calendar pages embed an unreadable Google Calendar iframe. "
   "Registrar (575) 835-5133 / Heather Juarez (575) 835-5116.",
   "Any Fall 2026 involvement fair, career fair, hackathon or speaker series — NONE found, "
   "and no recurring pattern documented either. (575) 835-5880.",
   "Named Student Leadership & Engagement staff — not published; the Dean of Students page "
   "404s. Ask by role at (575) 835-5880.",
   "Named CSE faculty in cryptography or distributed systems — every department URL 404s or "
   "returns a catalog shell. https://catalog.nmt.edu/departments/CSE/overview",
   "No phone is published for NMT Academic Affairs anywhere on the site.",
 ],
 "note": "NMT is small (~2,000 students) and science/engineering only — there is no "
         "traditional business school. Audience QUALITY is the highest in the state; "
         "audience SIZE is the lowest of the six. Do not judge this stop by headcount.",
},

# ══════════════════════════════════════════════════════════════════════════════
# 4. EASTERN NEW MEXICO UNIVERSITY
# ══════════════════════════════════════════════════════════════════════════════
{
 "state": "New Mexico",
 "name": "Eastern New Mexico University",
 "city": "Portales, NM",
 "type": "Public",
 "tier": "C — Opportunistic",
 "access": 3,

 "start": "Mon Aug 24, 2026 — ⚠ one week LATER than UNM, NM Tech and NMHU",
 "adddrop": "UNVERIFIED — the calendar table truncates before the deadline rows render. "
            "Student Affairs (575) 562-2221.",
 "fallbreak": "None listed",
 "thanksgiving": "Nov 23-27, 2026 (full week)",
 "lastclass": "Fri Dec 4, 2026",
 "finals": "⚠ UNVERIFIED AND AMBIGUOUS — classes end Dec 4 and WINTER BREAK BEGINS DEC 5, "
           "leaving NO GAP for a separate finals week. Either finals are embedded in the "
           "final instructional week or the calendar's finals rows did not render. ENMU "
           "maintains a separate 'Final Exam Schedule' document. DO NOT quote ENMU finals "
           "dates without confirming: (575) 562-2221.",
 "cal_url": "https://www.enmu.edu/academics/academic-resources-services/catalogs-schedules-calendars/academic-calendar",
 "cal_status": "PARTIAL",

 "fair": "'Dawg Days' New Student Orientation; Associated Students Activities Board (ASAB) "
         "programming",
 "fair_date": "UNVERIFIED — no Fall 2026 involvement fair date is published. The Student "
              "Involvement page names the recurring structures ('Dawg Days' orientation, "
              "ASAB, 60+ student organisations) but gives NO DATES and documents no "
              "pattern. Will post at enmu.edu/greyhound-life/student-involvement and on the "
              "MyENMU Campus Life Portal Community — ⚠ THE PORTAL IS LOGIN-GATED, so "
              "documents, applications and org materials sit behind authentication. "
              "Office of Campus Life (575) 562-2108.",
 "fair_outside": "UNVERIFIED — not addressed on any public page.",
 "fair_cost": "UNVERIFIED — not published.",
 "fair_deadline": "UNVERIFIED — not published.",
 "fair_url": "https://www.enmu.edu/greyhound-life/student-involvement",

 "policy": "⚠ UNVERIFIED — ENMU's solicitation, tabling and facility-use policy lives in "
           "the Student Handbook PDF, which is hosted on SharePoint and ROBOTS-BLOCKED",
 "policy_url": "https://www.enmu.edu/greyhound-life/student-handbook",
 "policy_key":
   "⚠ NOTHING CAN BE QUOTED FOR ENMU — THIS IS A HARD BLOCKER, NOT A SOFT GAP. ENMU's "
   "policies on solicitation, tabling, outside organisations, commercial activity, "
   "free-speech areas and facility use live in the STUDENT HANDBOOK PDF, which is hosted at "
   "liveenmu.sharepoint.com AND THAT URL IS DISALLOWED BY ROBOTS.TXT. The handbook landing "
   "page confirms the document contains the Student Code of Conduct and 'a lot of "
   "information about many different campus services and activities' but reproduces none of "
   "it. enmu.edu/about/consumer-information/policies-procedures RETURNS 404. "
   "NO POLICY NAME, NUMBER, EFFECTIVE DATE, FEE, INSURANCE LIMIT, DEPOSIT, CANCELLATION "
   "TERM, ANTI-FRONTING RULE OR SPONSORSHIP REQUIREMENT WAS OBTAINABLE. The access rating "
   "of 3 above is A PROVISIONAL PLACEHOLDER derived from peer institutions, NOT from "
   "ENMU's own text — treat it as unrated until someone reads the handbook. "
   "As a PUBLIC institution ENMU is bound by First Amendment public-forum doctrine, but its "
   "written rules are effectively unpublished to the open web. "
   "⚠ NO NEW MEXICO CAMPUS FREE-SPEECH STATUTE EXISTS — so there is no state-law backstop "
   "to fall back on while the institutional policy remains unreadable. "
   "CLOSE THIS BY PHONE: Student Affairs (575) 562-2221 — ask them to email the "
   "solicitation section or read the operative paragraph aloud.",
 "sponsor_required": "UNVERIFIED — policy unreadable. In practice the club-advisor route "
                     "below is far stronger than anything policy-based here.",

 "clubs": [
   ("⚑ BEST CLUB DIRECTORY IN NEW MEXICO — fully public, and it publishes STAFF ADVISORS "
    "WITH DIRECT PHONE NUMBERS",
    "Unlike UNM, NMSU and NMHU, ENMU's org directory is readable AND lists a named staff "
    "advisor with a direct line for each club. Advisors are STAFF, so unlike student "
    "officers they do not rotate annually — these are durable contacts. "
    "⚠ BUT EVERY EMAIL ON THE PAGE IS OBFUSCATED: addresses render as the literal "
    "placeholder '[email protected]' via client-side JavaScript. THE EMAILS ARE "
    "UNRECOVERABLE FROM THE PAGE; the phone numbers render in plain text. CALL, DO NOT "
    "EMAIL.",
    "https://www.enmu.edu/greyhound-life/student-involvement/student-organizations"),
   ("⚠ Accounting and Finance Club",
    "THE BEST FINANCE-AUDIENCE CONTACT AT ENMU. 'Provide the advance study of accounting "
    "and promote a closer affiliation.' Advisor Konni Wallace, (575) 562-2704 — a direct "
    "line to a staff member who convenes the finance students.",
    "https://www.enmu.edu/greyhound-life/student-involvement/student-organizations"),
   ("Computer Science Club",
    "'Promote members academic success and allow for members to establish networking.' "
    "Advisor Edgar Ceh Varela, (575) 562-2945.",
    "https://www.enmu.edu/greyhound-life/student-involvement/student-organizations"),
   ("Delta Mu Delta, Gamma Omega Chapter",
    "Business honor society — selective, high-quality business audience. Advisor Corey "
    "Cole, (575) 562-2361.",
    "https://www.enmu.edu/greyhound-life/student-involvement/student-organizations"),
   ("Greyhound Gaming",
    "Esports / competitive gaming. Advisor Josef Garcia, (575) 562-4352. Adjacent "
    "digital-native audience.",
    "https://www.enmu.edu/greyhound-life/student-involvement/student-organizations"),
   ("STEM Club",
    "'Fosters interest, collaboration, and professional development in Science, Technology, "
    "Engineering, and Mathematics.' Advisor Patricia Cabrales Arellano — no phone published.",
    "https://www.enmu.edu/greyhound-life/student-involvement/student-organizations"),
   ("Electronics Club",
    "'Promote an understanding and application of electronics technology.' Advisor Hamid "
    "Allamehzadeh — no phone published.",
    "https://www.enmu.edu/greyhound-life/student-involvement/student-organizations"),
   ("(Blockchain / crypto / investment / ACM club)",
    "NONE listed in a directory that IS readable — so this negative is reasonably reliable. "
    "No blockchain, cryptocurrency, Web3, investment, Financial Management Association, "
    "ACM, data-science or economics club. The Accounting and Finance Club is the closest "
    "match.",
    "https://www.enmu.edu/greyhound-life/student-involvement/student-organizations"),
 ],

 "faculty": [
   ("⚠ Konni Wallace",
    "ADVISOR, ACCOUNTING AND FINANCE CLUB — the single most useful contact at ENMU. A "
    "direct line to the staff member who convenes the finance-major audience. ⚠ Confirmed "
    "on a live page IN THAT CAPACITY ONLY — do NOT represent her as crypto faculty. Her "
    "email is obfuscated on the source page; the phone is not.",
    "College of Business",
    "email obfuscated on source page · (575) 562-2704 [direct]",
    "https://www.enmu.edu/greyhound-life/student-involvement/student-organizations"),
   ("Edgar Ceh Varela",
    "Advisor, Computer Science Club — the technical-audience door. Confirmed in that "
    "capacity only. Email obfuscated on the source page.",
    "Computer Science",
    "email obfuscated on source page · (575) 562-2945 [direct]",
    "https://www.enmu.edu/greyhound-life/student-involvement/student-organizations"),
   ("Corey Cole",
    "Advisor, Delta Mu Delta (business honor society). Confirmed in that capacity only. "
    "Email obfuscated on the source page.",
    "College of Business",
    "email obfuscated on source page · (575) 562-2361 [direct]",
    "https://www.enmu.edu/greyhound-life/student-involvement/student-organizations"),
   ("Josef Garcia",
    "Advisor, Greyhound Gaming. Confirmed in that capacity only. Email obfuscated.",
    "Student Affairs",
    "email obfuscated on source page · (575) 562-4352 [direct]",
    "https://www.enmu.edu/greyhound-life/student-involvement/student-organizations"),
   ("Office of Campus Life",
    "Student orgs, involvement, tabling. Campus Union Building (CUB) Room 104; ENMU Station "
    "39, 1500 S Ave K, Portales NM 88130. Fax (575) 562-4321.",
    "Student Affairs",
    "(575) 562-2108 [main line, Campus Life]",
    "https://www.enmu.edu/greyhound-life/student-involvement"),
   ("⚠ Student Affairs",
    "HOLDS THE UNRETRIEVABLE STUDENT HANDBOOK SOLICITATION POLICY — the only route to "
    "ENMU's written rules, which are robots-blocked on SharePoint.",
    "Student Affairs",
    "(575) 562-2221 [main line, Student Affairs]",
    "https://www.enmu.edu/greyhound-life/student-handbook"),
   ("ENMU University operator",
    "MAIN LINE. Useful mechanic for cold-calling: ENMU states 'All University extensions "
    "start with 575.562' and that additional numbers are available 'through the University "
    "operator at 575.562.1011'. The searchable directory back-end at ssb.enmu.edu returned "
    "no department numbers to a fetcher.",
    "—",
    "(575) 562-1011 [MAIN LINE / operator]",
    "https://www.enmu.edu/about/enmu-information-directories/university-directory"),
   ("(Faculty — blockchain / crypto / fintech / monetary economics)",
    "⚠ NOT CONFIRMED. No ENMU faculty member researching blockchain, cryptocurrency, "
    "fintech, digital assets, monetary economics or payments could be verified. The four "
    "named individuals above are CLUB ADVISORS ONLY. DO NOT GUESS. Look up via the "
    "university directory.",
    "—",
    "(575) 562-1011 [operator]",
    "https://www.enmu.edu/about/enmu-information-directories/university-directory"),
 ],

 "courses": [
   ("(All courses)",
    "⚠ NOT RESEARCHED — the web-search budget was exhausted before ENMU's catalog could be "
    "reached. No blockchain, crypto or fintech course is either confirmed OR excluded here. "
    "THIS IS A COVERAGE GAP, NOT A FINDING OF ABSENCE. "
    "Check https://www.enmu.edu/academics/academic-resources-services/catalogs-schedules-calendars/",
    "https://www.enmu.edu/academics/academic-resources-services/catalogs-schedules-calendars/"),
 ],

 "events": [
   ("(All events)",
    "⚠ NONE FOUND for Fall 2026 — no career fair, hackathon or speaker series dates were "
    "obtainable. Again a COVERAGE GAP (budget exhausted) as much as a finding. "
    "Office of Campus Life (575) 562-2108.",
    "https://www.enmu.edu/greyhound-life/student-involvement"),
 ],

 "play":
   "GO IN THROUGH A CLUB ADVISOR, NOT THROUGH THE INSTITUTION — because at ENMU the "
   "institution is unreadable and the advisors are not. ENMU's written policy is a hard "
   "blocker: the Student Handbook PDF that contains every solicitation, tabling and "
   "facility rule is hosted on SharePoint and ROBOTS-BLOCKED, and the policies-procedures "
   "page 404s, so NOTHING about ENMU's rules can be quoted. But ENMU has the best club "
   "directory in New Mexico — it publishes a named STAFF advisor with a DIRECT PHONE LINE "
   "for each organisation, and staff advisors do not rotate the way student officers do. "
   "THE SINGLE BEST DOOR IS KONNI WALLACE, ADVISOR TO THE ACCOUNTING AND FINANCE CLUB, AT "
   "(575) 562-2704 — one call reaches the person who convenes the entire finance-major "
   "audience on this campus. Back it with Edgar Ceh Varela at the Computer Science Club, "
   "(575) 562-2945. Note that EVERY EMAIL ADDRESS ON THAT DIRECTORY IS OBFUSCATED to the "
   "literal string '[email protected]' by client-side JavaScript, so the phone numbers "
   "are the only usable contact — call, do not email. Make one parallel call to Student "
   "Affairs (575) 562-2221 to get the handbook's solicitation section read out before "
   "committing to any tabling. Portales is remote — roughly 200 miles from Albuquerque with "
   "nothing else on the route — so this stop only justifies itself if the finance-club "
   "relationship lands first. Confirm by phone before driving.",

 "gaps": [
   "⚠⚠ ENMU'S ENTIRE SOLICITATION AND FACILITY POLICY — the Student Handbook PDF is "
   "ROBOTS-BLOCKED on SharePoint (liveenmu.sharepoint.com) and the policies-procedures page "
   "404s. Nothing about ENMU access is currently knowable, and the access rating of 3 is a "
   "PROVISIONAL PLACEHOLDER. Student Affairs (575) 562-2221.",
   "⚠ Fall 2026 FINALS WEEK — classes end Dec 4 and winter break starts Dec 5, leaving no "
   "gap. Ambiguous and must not be quoted as-is. Also the ADD/DROP deadline (calendar table "
   "truncated). (575) 562-2221.",
   "Fall 2026 involvement fair / Dawg Days dates — none published and no pattern "
   "documented. The MyENMU Campus Life Portal is LOGIN-GATED. "
   "Office of Campus Life (575) 562-2108.",
   "Whether outside organisations may table at all, and at what cost — not addressed on any "
   "public page. (575) 562-2108.",
   "ENMU courses — NOT RESEARCHED (search budget exhausted). No blockchain/fintech course "
   "confirmed or excluded.",
   "ENMU Fall 2026 events, career fairs and hackathons — NOT RESEARCHED (budget exhausted).",
   "Named faculty in blockchain / crypto / fintech — none confirmable. The four named "
   "contacts are club advisors only. https://www.enmu.edu/about/enmu-information-directories/university-directory",
   "Email addresses for all club advisors — obfuscated to '[email protected]' by "
   "client-side JavaScript. Use the published phone numbers instead.",
 ],
},

# ══════════════════════════════════════════════════════════════════════════════
# 5. NEW MEXICO HIGHLANDS UNIVERSITY
# ══════════════════════════════════════════════════════════════════════════════
{
 "state": "New Mexico",
 "name": "New Mexico Highlands University",
 "city": "Las Vegas, NM",
 "type": "Public",
 "tier": "C — Opportunistic",
 "access": 2,

 "start": "Mon Aug 17, 2026",
 "adddrop": "Last day to drop (full term): Fri Aug 28, 2026. Academic census: Fri Sep 4, "
            "2026.",
 "fallbreak": "⚠ Mon-Tue Oct 12-13, 2026 — THE ONLY DISCRETE OCTOBER FALL BREAK OF THE SIX "
              "NEW MEXICO CAMPUSES. Preceded immediately by MID-TERM EXAM WEEK, Oct 5-10 — "
              "so late Sept through mid-Oct is a DEAD ZONE for outreach here.",
 "thanksgiving": "⚠ Fall Recess Wed-Sat Nov 25-28, 2026 — the ONLY NM campus whose "
                 "Thanksgiving break starts on a WEDNESDAY. Students are on campus Mon-Tue "
                 "of Thanksgiving week, unlike NMSU, NM Tech and ENMU which close the whole "
                 "week.",
 "lastclass": "Fri Dec 11, 2026 (term ends)",
 "finals": "Dec 7-11, 2026",
 "cal_url": "https://www.nmhu.edu/academic-calendar/",
 "cal_status": "CONFIRMED",

 "fair": "None published",
 "fair_date": "⚠ NONE FOUND. No Fall 2026 involvement fair, club fair or welcome-week "
              "tabling event is published, AND NO RECURRING PATTERN IS DOCUMENTED. The "
              "student-life page is marketing copy with no dates, no staff and no fair. The "
              "Office of Campus Life is named as responsible but HAS NO WORKING WEB PAGE "
              "(nmhu.edu/office-of-campus-life/ returns 404). Would post at "
              "nmhu.edu/events-calendar or on NMHU Engage. "
              "Call the switchboard (505) 425-7511 and ask for Office of Campus Life.",
 "fair_outside": "UNVERIFIED — no fair and no participation policy published.",
 "fair_cost": "UNVERIFIED",
 "fair_deadline": "UNVERIFIED",
 "fair_url": "https://www.nmhu.edu/events-calendar",

 "policy": "Student Handbook — 'Policy for use of Campus Facilities'. No solicitation, "
           "tabling or freedom-of-expression policy exists on NMHU's public web.",
 "policy_url": "https://www.nmhu.edu/student-handbook/",
 "policy_key":
   "⚠ THE MOST UNCONSTRAINED DENIAL CLAUSE FOUND IN NEW MEXICO. The only retrievable "
   "governing text is the Student Handbook's 'Policy for use of Campus Facilities': "
   "'The University shall take all appropriate steps to reduce the risk to property and "
   "persons. Therefore, AT THE SOLE DISCRETION OF THE UNIVERSITY, THE UNIVERSITY MAY DENY "
   "THE USE OF UNIVERSITY FACILITIES FOR ANY REASON UP TO BUT NOT LIMITED TO the following "
   "reasons' — including events that 'May result in the violation of University policies, "
   "federal and state laws.' Read that literally: SOLE DISCRETION, FOR ANY REASON, UP TO "
   "BUT NOT LIMITED TO. As applied to expressive activity by a public institution this is "
   "constitutionally vulnerable, but as a practical matter it means an NMHU facilities "
   "officer can decline without stating a reason and without an appeal path. "
   "Facility requests are handled by the OFFICE OF UNIVERSITY RELATIONS — an unusual "
   "placement; most campuses route this through a student union or conference services. "
   "(505) 454-3387 · hurentals@nmhu.edu. "
   "⚠ NOT FOUND AND THEREFORE UNVERIFIED RATHER THAN ABSENT: no anti-fronting language, no "
   "sponsorship requirement, no fee schedule, no insurance limit, no deposit or cancellation "
   "terms, no free-speech-zone rules, no commercial-solicitation ban, no payment-credential "
   "or on-site-contract language. The handbook page rendered only partially, and NMHU's "
   "public 'policies' links go to Privacy/Terms and Title IX only. "
   "⚠ NO NEW MEXICO CAMPUS FREE-SPEECH STATUTE EXISTS — so against a sole-discretion denial "
   "clause there is no state statute to invoke, only First Amendment public-forum doctrine "
   "argued from first principles.",
 "sponsor_required": "UNVERIFIED — no sponsorship route is documented either way. The "
                     "practical route is a facility request to University Relations, "
                     "(505) 454-3387, which may be refused at sole discretion.",

 "clubs": [
   ("⚠ DIRECTORY IS COMPLETELY UNREACHABLE — ZERO NMHU CLUBS ARE KNOWN",
    "NMHU's org list runs on Anthology Engage at nmhu.campuslabs.com/engage/organizations. "
    "The page is JavaScript-rendered AND the Engage discovery API "
    "(/engage/api/discovery/search/organizations) IS DISALLOWED BY ROBOTS.TXT. Not one NMHU "
    "club could be enumerated. NO club — blockchain, crypto, finance, investment, "
    "economics, business, entrepreneurship, ACM, computer science, data science or FMA — is "
    "either CONFIRMED OR EXCLUDED at NMHU. This is a total blind spot, not a negative "
    "finding.",
    "https://nmhu.campuslabs.com/engage/organizations"),
   ("⚑ STRUCTURAL ODDITY WORTH KNOWING",
    "NMHU routes student clubs and organisations through the CENTER FOR PROFESSIONAL "
    "DEVELOPMENT AND CAREER READINESS — not through a student-activities or dean-of-students "
    "office. Club questions go to careerservices@nmhu.edu / (877) 850-9064. That atypical "
    "org chart means CAREER SERVICES, not student activities, is the gatekeeper for club "
    "introductions here. Most ambassadors will guess wrong.",
    "https://www.nmhu.edu/campus-clubs-and-organizations/"),
 ],

 "faculty": [
   ("⚠ Kimberly Blea",
    "VICE PRESIDENT FOR STUDENT AFFAIRS — the senior decision-maker for campus access, and "
    "with a sole-discretion denial clause in force, the person worth going to directly. "
    "⚠ Note her email prefix (kjvaldez@) does NOT match her displayed surname — this is "
    "confirmed as printed on the live page, not a transcription error.",
    "Student Affairs",
    "kjvaldez@nmhu.edu · (505) 454-3566 [direct]",
    "https://www.nmhu.edu/dean-of-students/"),
   ("Yvonne Duran",
    "Student Affairs Executive Administrative Assistant — THE GATEKEEPER; book time with "
    "Blea through her rather than cold-calling the VP line.",
    "Student Affairs",
    "ycduran@nmhu.edu · (505) 454-3020 [direct]",
    "https://www.nmhu.edu/dean-of-students/"),
   ("⚠ Office of University Relations",
    "HANDLES ALL CAMPUS FACILITY RENTALS — an unusual placement, and the office that "
    "exercises the sole-discretion denial. This is the number that decides whether DGD gets "
    "space.",
    "University Relations",
    "hurentals@nmhu.edu · (505) 454-3387 [direct]",
    "https://www.nmhu.edu/student-handbook/"),
   ("Center for Professional Development and Career Readiness",
    "OWNS STUDENT CLUBS at NMHU — the non-obvious gatekeeper for any club introduction.",
    "Career Services",
    "careerservices@nmhu.edu · (877) 850-9064 [main line, toll-free]",
    "https://www.nmhu.edu/campus-clubs-and-organizations/"),
   ("Office of Admissions",
    "Listed with a direct number in the campus directory.",
    "Admissions",
    "admissions@nmhu.edu · (505) 454-3394 [direct]",
    "https://its.nmhu.edu/www/directory"),
   ("NMHU Switchboard",
    "MAIN LINE — the route to the Office of Campus Life, which has no working web page and "
    "no published number of its own.",
    "—",
    "(505) 425-7511 [MAIN LINE, switchboard] · (877) 850-9064 [MAIN LINE, toll-free]",
    "https://its.nmhu.edu/www/directory"),
   ("(Faculty — blockchain / crypto / fintech / monetary economics)",
    "⚠ NOT CONFIRMED. The searchable employee directory sits behind a query form at "
    "its.nmhu.edu/www/directory that returns no department listings to a fetcher. DO NOT "
    "GUESS — look up in a browser or call the switchboard.",
    "—",
    "(505) 425-7511 [switchboard]",
    "https://its.nmhu.edu/www/directory"),
   ("(Office of Campus Life)",
    "NO PUBLISHED NUMBER AND NO WORKING PAGE — nmhu.edu/office-of-campus-life/ returns 404. "
    "Named as the office overseeing student activities but otherwise invisible. Reach it "
    "through the switchboard.",
    "Student Affairs",
    "no direct number published · (505) 425-7511 [switchboard]",
    "https://www.nmhu.edu/whats-college-life-like-on-campus/"),
 ],

 "courses": [
   ("(All courses)",
    "⚠ NOT RESEARCHED — search budget exhausted before NMHU's catalog could be reached. No "
    "blockchain, crypto or fintech course confirmed OR excluded. COVERAGE GAP, NOT A "
    "FINDING OF ABSENCE. Check https://www.nmhu.edu/academics/",
    "https://www.nmhu.edu/academics/"),
 ],

 "events": [
   ("(All events)",
    "⚠ NONE FOUND for Fall 2026. COVERAGE GAP (budget exhausted) as much as a finding. "
    "Check the events calendar.",
    "https://www.nmhu.edu/events-calendar"),
 ],

 "play":
   "LOWEST-PRIORITY STOP IN NEW MEXICO — do not drive to Las Vegas NM without a confirmed "
   "invitation in hand. NMHU is the smallest campus of the six (~3,000 students) and it "
   "ranks last on the written record: the only retrievable rule lets the university deny "
   "facilities 'AT THE SOLE DISCRETION OF THE UNIVERSITY... FOR ANY REASON UP TO BUT NOT "
   "LIMITED TO', with no published fees, no process and no appeal path. Compounding that, "
   "its club directory is a TOTAL BLIND SPOT — Engage is JavaScript-rendered and its API is "
   "robots-blocked, so ZERO NMHU clubs are known and nobody can tell you whether a finance "
   "or CS group exists. If the ambassador is in northern New Mexico anyway, the single best "
   "door is NOT student activities: NMHU uniquely routes clubs through the CENTER FOR "
   "PROFESSIONAL DEVELOPMENT AND CAREER READINESS, so call careerservices@nmhu.edu at "
   "(877) 850-9064, ask what clubs exist, and ask for an introduction. The institutional "
   "escalation is Yvonne Duran at (505) 454-3020, who books time with VP for Student "
   "Affairs Kimberly Blea (505) 454-3566. Facilities are a separate call to University "
   "Relations, (505) 454-3387. One scheduling note if you do go: NMHU runs MID-TERM EXAMS "
   "Oct 5-10 followed immediately by a FALL BREAK Oct 12-13, so the first half of October "
   "is dead — but unusually, students ARE on campus the Monday and Tuesday of Thanksgiving "
   "week, when every other NM campus has closed.",

 "gaps": [
   "⚠⚠ ZERO NMHU CLUBS ARE KNOWN — Engage is JavaScript-rendered and its discovery API is "
   "ROBOTS-BLOCKED. Whether NMHU has any finance, CS, business or crypto club is a total "
   "blind spot. Call Career Services (877) 850-9064, which owns clubs at this campus.",
   "⚠ Whether any solicitation or tabling policy exists at all — only a sole-discretion "
   "facility-denial clause could be retrieved. VP Student Affairs Kimberly Blea "
   "(505) 454-3566, or Yvonne Duran (505) 454-3020.",
   "⚠ Fees, insurance, deposits and cancellation terms for facility use — none published. "
   "Office of University Relations (505) 454-3387 · hurentals@nmhu.edu.",
   "Fall 2026 involvement fair — none published and no pattern documented. The Office of "
   "Campus Life has NO working web page (404) and no published number. "
   "Switchboard (505) 425-7511.",
   "NMHU courses — NOT RESEARCHED (search budget exhausted).",
   "NMHU Fall 2026 events — NOT RESEARCHED (search budget exhausted).",
   "Named faculty in blockchain / crypto / fintech — none confirmable; the employee "
   "directory is behind a query form. https://its.nmhu.edu/www/directory",
 ],
 "note": "Las Vegas, NEW MEXICO — not Las Vegas, Nevada. NMHU is routinely confused with "
         "UNLV in travel planning; it is a ~3,000-student campus 120 miles north-east of "
         "Albuquerque.",
},

# ══════════════════════════════════════════════════════════════════════════════
# 6. CENTRAL NEW MEXICO COMMUNITY COLLEGE
# ══════════════════════════════════════════════════════════════════════════════
{
 "state": "New Mexico",
 "name": "Central New Mexico Community College",
 "city": "Albuquerque, NM",
 "type": "Public (community college)",
 "tier": "C — Opportunistic",
 "access": 4,

 "start": "⚠⚠ Mon Aug 31, 2026 — LATEST START IN NEW MEXICO, TWO FULL WEEKS AFTER UNM IN "
          "THE SAME CITY. This creates a SECOND, NON-OVERLAPPING ALBUQUERQUE WELCOME "
          "WINDOW and is the single highest-leverage logistics fact in this state file.",
 "adddrop": "UNVERIFIED — not on the retrievable feed. Census date IS confirmed: Thu Sep 17, "
            "2026. Special registration request deadline Mon Sep 21, 2026. "
            "Ask CNM (505) 224-3000, press 0.",
 "fallbreak": "UNVERIFIED — not on the retrievable feed. Labor Day closure Mon Sep 7, 2026 "
              "IS confirmed.",
 "thanksgiving": "UNVERIFIED — not on the retrievable feed. Ask CNM (505) 224-3000.",
 "lastclass": "Term ends Sun Dec 13, 2026",
 "finals": "UNVERIFIED — not published on the retrievable feed.",
 "cal_url": "https://cnm.enterprise.localist.com/",
 "cal_status": "PARTIAL",

 "fair": "None published",
 "fair_date": "UNVERIFIED — no Fall 2026 involvement fair, club fair or welcome-week "
              "tabling event is published, and no recurring pattern is documented. The "
              "Student Activities Office page references 'Upcoming Student Events' and New "
              "Student Orientation but shows NO DATES. Would post at "
              "cnm.edu/depts/student-activities-office or cnm.enterprise.localist.com. "
              "Student Activities Office (505) 224-3238.",
 "fair_outside": "⚑ THE ONE REAL LEAD — CNM runs an explicit, published OUTSIDE-VENDOR "
                 "channel: 'CNM welcomes local food trucks to serve our campus community.' "
                 "It is a food-truck programme, not a tabling programme, BUT IT PROVES THE "
                 "PATHWAY EXISTS and identifies the exact person who administers outside "
                 "commercial presence on CNM ground: Val Gutierrez, Student Events Manager, "
                 "(505) 224-4000 ext. 54277. Application procedure, fees, insurance and "
                 "liability requirements are NOT DISCLOSED — that is the call to make.",
 "fair_cost": "UNVERIFIED for tabling. For SPACE RENTAL, rates ARE published: $400-$1,800 "
              "for full-day rentals depending on space type, with a 25% discount for "
              "nonprofit and government entities (DGD would NOT qualify).",
 "fair_deadline": "UNVERIFIED",
 "fair_url": "https://www.cnm.edu/depts/student-activities-office/food-trucks-at-cnm",

 "policy": "⚠ CNM's solicitation policy is REFERENCED BUT NOT PUBLISHED. The rentable-space "
           "track is governed by CNM SPACE Solutions terms (published rates).",
 "policy_url": "https://www.cnm.edu/depts/dean-of-students/the-student-handbook",
 "policy_key":
   "⚠ CNM MAKES SOLICITATION A PUNISHABLE OFFENCE WHILE NOT PUBLISHING THE RULE THAT "
   "DEFINES IT. The Student Handbook lists among General Violations: 'SOLICITING OR SELLING "
   "IN VIOLATION OF THE SOLICITATION POLICY.' THE SOLICITATION POLICY ITSELF APPEARS "
   "NOWHERE ON CNM.EDU. The governing-board policy manual could not be located — "
   "/depts/governing-board, /depts/governing-board/policies-and-procedures and "
   "/about-cnm/policies-procedures ALL RETURN 404. "
   "WHAT IS PUBLISHED — and CNM is the ONLY New Mexico campus with real numbers. Event "
   "Management states the routing rule explicitly: 'Employer events will be referred to CNM "
   "Workforce Community Services, student events will be directed to Student Services, "
   "outreach events will be directed to recruiting, and THIRD-PARTY EVENTS WILL BE DIRECTED "
   "TO SPACE SOLUTIONS.' CNM SPACE Solutions publishes RATES OF $400-$1,800 FOR FULL-DAY "
   "RENTALS with a 25% discount for nonprofit and government entities — THE ONLY PUBLISHED "
   "EXTERNAL-USER RATES FOUND ON ANY NEW MEXICO CAMPUS. "
   "⚠⚠ EXCLUSION THAT DIRECTLY THREATENS AN EDUCATION-FRAMED CRYPTO PITCH — renters may not "
   "offer 'TEACHING OR OFFERING TRAINING SERVICES WHICH COMPETE WITH THE INSTITUTE', and "
   "may not use space for 'nonbusiness functions such as wedding receptions, fraternal "
   "events, religious events.' CNM TEACHES IT AND BUSINESS SUBJECTS, so a DGD 'workshop', "
   "'training' or 'seminar' plausibly falls inside that exclusion. FRAME ANY CNM ENGAGEMENT "
   "AS SPONSORSHIP, OUTREACH OR A STUDENT-ORG PARTNERSHIP — NEVER AS TRAINING. "
   "NOT FOUND ANYWHERE AT CNM (unverified, not absent): anti-fronting language, sponsorship "
   "requirement, free-speech-zone rules, insurance requirements, deposit amounts, "
   "cancellation terms, payment-credential or on-site-contract language. "
   "⚠ NO NEW MEXICO CAMPUS FREE-SPEECH STATUTE EXISTS. CNM is a PUBLIC community college "
   "and so is bound by public-forum doctrine, but there is no state statute conferring "
   "campus forum rights to cite against an unpublished solicitation rule.",
 "sponsor_required": "No — pay the fee. Third-party events route to SPACE Solutions "
                     "(505) 224-3868 at $400-$1,800/day. No sponsorship requirement is "
                     "documented, though the solicitation policy that might impose one is "
                     "unpublished.",

 "clubs": [
   ("⚑ DIRECTORY IS FULLY PUBLIC AND COMPLETE — 18 organisations, all listed",
    "Unlike UNM, NMSU and NMHU, CNM's club list is readable in full. That makes the "
    "negative finding below RELIABLE rather than a gap. ⚠ But emails are OBFUSCATED to the "
    "literal placeholder '[email protected]' by client-side JavaScript — advisor names "
    "render in plain text, their emails do not. Reach advisors via the Student Activities "
    "Office, (505) 224-3238.",
    "https://www.cnm.edu/Plone/depts/student-support/student-activities-office/clubs-organizations/home"),
   ("⚠ Coffee Into Coders",
    "THE ONLY TECHNOLOGY CLUB AT CNM, and the entire technical-audience opportunity on this "
    "campus. Members 'network and collaborate on projects and goals'. Advisor: Neal "
    "Holtschulte (email obfuscated on source page).",
    "https://www.cnm.edu/Plone/depts/student-support/student-activities-office/clubs-organizations/home"),
   ("Executive Council of Students (ECOS)",
    "CNM's student government — the sponsorship path if one is ever required. Advisors: "
    "Sandra Vazquez, Tim Beaton.",
    "https://www.cnm.edu/Plone/depts/student-support/student-activities-office/clubs-organizations/home"),
   ("National Society of Leadership and Success (NSLS)",
    "Honor society, broad cross-disciplinary membership — the largest general-audience club "
    "on campus. Email obfuscated.",
    "https://www.cnm.edu/Plone/depts/student-support/student-activities-office/clubs-organizations/home"),
   ("Phi Theta Kappa",
    "Community-college honor society, broad membership. Email obfuscated.",
    "https://www.cnm.edu/Plone/depts/student-support/student-activities-office/clubs-organizations/home"),
   ("⚠ (Finance / business / crypto / entrepreneurship club)",
    "NONE — AND THIS NEGATIVE IS DEFINITIVE, not a gap. The complete public list runs to 18 "
    "organisations and NOT ONE is a finance, business, economics, investment, "
    "entrepreneurship, data-science, ACM or blockchain group. Full roster: American Sign "
    "Language, Artworks, Black Student Union, CNM Chronicle, CNM Dream Team, CNM Students "
    "Care, Coffee Into Coders, ECOS, NSLS, Phi Theta Kappa, Psychology Club, Radiology, "
    "SkillsUSA, Stitchers, Student Nurses Association, Student Veterans of CNM, Suncat "
    "Social Club, Vet Techs Unleashed.",
    "https://www.cnm.edu/Plone/depts/student-support/student-activities-office/clubs-organizations/home"),
 ],

 "faculty": [
   ("⚠ Val (Valerie) Gutierrez",
    "STUDENT EVENTS MANAGER — ADMINISTERS OUTSIDE COMMERCIAL VENDORS ON CNM GROUND. Named "
    "owner of the food-truck programme, which is the only documented mechanism by which a "
    "non-CNM commercial entity operates on this campus. THE call to make about tabling. "
    "Email obfuscated on the source page; the extension is not.",
    "Student Activities Office",
    "email obfuscated on source page · (505) 224-4000 ext. 54277 [direct extension]",
    "https://www.cnm.edu/depts/student-activities-office/food-trucks-at-cnm"),
   ("Student Activities Office",
    "Clubs, student events, advisor introductions. Student Resource Center (SRC) Room 201, "
    "835 Buena Vista SE, Albuquerque NM 87106. Mon-Fri 8am-5pm.",
    "Student Services",
    "(505) 224-3238 [main line, Student Activities]",
    "https://www.cnm.edu/depts/student-activities-office"),
   ("Peyton Williams",
    "Student Events Coordinator — works alongside Gutierrez. No direct extension published.",
    "Student Activities Office",
    "(505) 224-3238 [Student Activities main line — no direct extension published]",
    "https://www.cnm.edu/depts/student-activities-office"),
   ("⚠ Dean of Students",
    "HOLDS THE UNPUBLISHED SOLICITATION POLICY — the rule CNM punishes you for violating "
    "but does not print. 716 University Ave SE, KW Building Room 208, Mon-Fri 8-5. "
    "Fax (505) 224-4740. No individual staff names are published on the page.",
    "Dean of Students",
    "(505) 224-4342 [direct]",
    "https://www.cnm.edu/depts/dean-of-students"),
   ("⚠ CNM SPACE Solutions",
    "THIRD-PARTY SPACE RENTAL — the only published external rate card in New Mexico, "
    "$400-$1,800 per full day, 25% off for nonprofits and government. Also the office that "
    "would apply the 'competing training services' exclusion. No staff names published.",
    "Auxiliary / facilities",
    "(505) 224-3868 [direct]",
    "https://cnmspacesolutions.org/"),
   ("Event Management",
    "Institutional events; routes third parties to SPACE Solutions. 716 University Blvd SE. "
    "Event Planning Request form at form.jotform.com/200515137440039.",
    "Event Management",
    "(505) 224-3000 [main line]",
    "https://www.cnm.edu/depts/event-management"),
   ("Campus Security",
    "Listed in the Student Handbook for incident reporting — useful for day-of escalation.",
    "Security",
    "(505) 224-3002 [direct]",
    "https://www.cnm.edu/depts/dean-of-students/the-student-handbook"),
   ("Ask CNM Contact Center",
    "MAIN LINE — press 0. Also the route to unpublished calendar dates (add/drop, breaks, "
    "finals). 525 Buena Vista Dr. SE, Albuquerque NM 87106.",
    "—",
    "(505) 224-3000 [MAIN LINE, press 0]",
    "https://www.cnm.edu/about-cnm/directories"),
   ("CNM Faculty and Staff Directory",
    "⚠ A LIVE, WORKING PEOPLE-SEARCH — searchable by name or by department (~40 "
    "departments), returning Name / Phone / Email / Title / Department. It returns nothing "
    "to a fetcher without a query, but it is the RIGHT TOOL for an ambassador with a "
    "browser. LOOK UP INDIVIDUALS HERE.",
    "—",
    "(505) 224-3000 [main line]",
    "http://directory.cnm.edu/"),
   ("(Faculty — blockchain / crypto / fintech)",
    "⚠ NOT CONFIRMED. No CNM faculty in blockchain, crypto, fintech or digital assets could "
    "be verified. Neal Holtschulte is confirmed ONLY as the Coffee Into Coders advisor. DO "
    "NOT GUESS — use the working directory search.",
    "—",
    "(505) 224-3000 [main line]",
    "http://directory.cnm.edu/"),
 ],

 "courses": [
   ("(All courses)",
    "⚠ NOT RESEARCHED — search budget exhausted. Given CNM's two-year mission, expect IT "
    "and business CERTIFICATE and ASSOCIATE coursework rather than blockchain-specific "
    "offerings. Neither confirmed nor excluded. "
    "Check https://www.cnm.edu/programs-of-study",
    "https://www.cnm.edu/programs-of-study"),
 ],

 "events": [
   ("(All events)",
    "⚠ NONE FOUND for Fall 2026. COVERAGE GAP (budget exhausted) as much as a finding. "
    "Check the Localist calendar.",
    "https://cnm.enterprise.localist.com/"),
 ],

 "play":
   "⚠ AUDIENCE MISMATCH — READ THIS BEFORE ALLOCATING ANY EFFORT. CNM is a TWO-YEAR "
   "COMMUNITY COLLEGE. It awards associate degrees and certificates: there is NO "
   "undergraduate business school, NO bachelor's-level computer science cohort, NO finance "
   "or economics major and NO graduate population. The complete, fully public club list "
   "confirms it — 18 organisations and NOT ONE is a finance, business, economics or "
   "entrepreneurship group. The student body is predominantly commuter and part-time, "
   "spread across several Albuquerque campuses rather than one quad. THIS IS NOT A "
   "WORTHLESS STOP, BUT IT IS NOT A UNM-CALIBRE ONE — budget accordingly. What makes it "
   "worth an afternoon is pure logistics: CNM STARTS AUG 31, TWO FULL WEEKS AFTER UNM, IN "
   "THE SAME CITY, so it is a free second welcome window on a trip already being made. "
   "CNM is also the only New Mexico campus that publishes real external rates — SPACE "
   "Solutions rents at $400-$1,800 per full day, (505) 224-3868 — which makes access a "
   "budgeting question rather than a permission fight. ⚠ BUT MIND THE FRAMING: the rental "
   "terms bar 'teaching or offering training services which compete with the Institute', "
   "and CNM teaches IT and business, so pitch DGD as SPONSORSHIP OR OUTREACH AND NEVER AS "
   "A WORKSHOP OR TRAINING. THE SINGLE BEST DOOR IS VAL GUTIERREZ, STUDENT EVENTS MANAGER, "
   "AT (505) 224-4000 EXT. 54277 — she administers CNM's food-truck programme, which is the "
   "only documented route by which an outside commercial entity operates on this campus, so "
   "she is the person who actually knows whether a table is possible. Secondary door: "
   "Coffee Into Coders, the only technology club on campus, reachable through Student "
   "Activities at (505) 224-3238.",

 "gaps": [
   "⚠⚠ CNM's SOLICITATION POLICY — the Student Handbook makes 'soliciting or selling in "
   "violation of the solicitation policy' a punishable offence but THE POLICY ITSELF IS "
   "UNPUBLISHED, and three separate policy-manual URLs return 404. "
   "Dean of Students (505) 224-4342.",
   "⚠ Whether a DGD campus activity would trip the SPACE Solutions exclusion on 'teaching "
   "or offering training services which compete with the Institute' — decisive for framing. "
   "SPACE Solutions (505) 224-3868.",
   "⚠ Fall 2026 ADD/DROP, FALL BREAK, THANKSGIVING and FINALS — none on the retrievable "
   "feed. Three registrar URLs 404 and the student calendar 302-redirects off-host to a "
   "Localist feed that carries only term boundaries and payment dates. "
   "Ask CNM (505) 224-3000, press 0.",
   "Whether outside organisations may TABLE (as distinct from renting space or operating a "
   "food truck), the procedure, fee and insurance requirement — not disclosed. "
   "Val Gutierrez (505) 224-4000 ext. 54277.",
   "Insurance requirements, deposits and cancellation terms for SPACE Solutions rentals — "
   "not published alongside the rates. (505) 224-3868.",
   "Fall 2026 involvement fair or orientation tabling dates — none published, no pattern "
   "documented. Student Activities (505) 224-3238.",
   "CNM courses — NOT RESEARCHED (search budget exhausted).",
   "CNM Fall 2026 events — NOT RESEARCHED (search budget exhausted).",
   "Named faculty in blockchain / crypto / fintech — none confirmable, but "
   "directory.cnm.edu IS a working people-search; look up in a browser.",
   "Club advisor emails — obfuscated to '[email protected]' by client-side JavaScript. "
   "Route through Student Activities (505) 224-3238.",
 ],
 "note": "⚠ CNM is a COMMUNITY COLLEGE, not a branch of UNM, though both sit in "
         "Albuquerque and are routinely conflated. Different institution, different "
         "governing board, different (two-year, commuter, part-time) audience.",
},

]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; those sort last and never show a countdown.
DEADLINES = [

 # ── THE URGENT ONE ──────────────────────────────────────────────────────────
 ("2026-08-17", "Aug 17, 2026", "UNM",
  "⚠⚠ WELCOME BACK DAYS REGISTRATION CLOSES — THE STATE'S MOST URGENT ITEM",
  "General registration deadline per the UNM news release. The Friday Night Live tabling "
  "deadline (Aug 1) has ALREADY PASSED. Student Organization Day is Aug 20 and Campus "
  "Employment & Community Service Day — the off-campus-facing slot — is Aug 21. SAC says "
  "'Departments, student organizations, AND COMMUNITY AGENCIES may participate' but does "
  "not define 'community agency' and publishes NO FEE. One call decides whether the state's "
  "best tabling window is available: ask for Haley Johnson by name.",
  "https://sac.unm.edu/events/welcome-back-days.html",
  "Haley Johnson, Student Activities Center · hagjohnson44@unm.edu · (505) 277-4706"),

 # ── TERM STARTS ─────────────────────────────────────────────────────────────
 ("2026-08-14", "Aug 14-21, 2026", "UNM",
  "⚠⚠ UNM WELCOME BACK DAYS UNDERWAY — 350+ orgs, ~200 tabling",
  "Confirmed for Fall 2026 and every weekday verified against the 2026 calendar (page is "
  "current, not stale). Key days: Student Organization Day Thu Aug 20, 10am-2pm, Duck Pond; "
  "Campus Employment & Community Service Day Fri Aug 21, 10am-2pm, Duck Pond.",
  "https://sac.unm.edu/events/welcome-back-days.html",
  "Student Activities Center · sac@unm.edu · (505) 277-4706"),

 ("2026-08-17", "Aug 17, 2026", "UNM",
  "Fall 2026 classes begin",
  "Semesters. Fall break Oct 8-9. ⚠ Add/drop, Thanksgiving and finals are all UNRETRIEVABLE "
  "— the detailed calendar is a JavaScript widget. Call the registrar.",
  "https://registrar.unm.edu/academic-calendar/ten-year-semester-dates-calendar.html",
  "UNM Registrar · (505) 277-8900"),

 ("2026-08-17", "Aug 17, 2026", "NM Tech",
  "Fall 2026 classes begin",
  "Semesters. Last day to add to waitlist Aug 21; last day to drop without permission Aug "
  "25. ⚠ Dates come from the registrar's Google Sheet, which contains at least one stray "
  "2025 row — worth a 60-second confirmation.",
  "https://docs.google.com/spreadsheets/d/11m7XFlZc77ZjqjDMsmVdtnUW3VpTgklC4CCw1taiOfc/edit",
  "NMT Registrar · (575) 835-5133 · Heather Juarez (575) 835-5116"),

 ("2026-08-17", "Aug 17, 2026", "NM Highlands",
  "Fall 2026 classes begin",
  "Semesters. Fully confirmed calendar — the most complete of the six. Last day to drop "
  "Aug 28; census Sep 4.",
  "https://www.nmhu.edu/academic-calendar/",
  "NMHU switchboard · (505) 425-7511"),

 ("2026-08-19", "Aug 19, 2026", "NMSU",
  "Fall 2026 classes begin",
  "Semesters PLUS two 8-week mini-semesters — a second cohort starts mid-October and misses "
  "all August programming. ⚠ NO October fall break at NMSU.",
  "https://records.nmsu.edu/academic-calendar/2026.html",
  "NMSU SILP · silp@nmsu.edu · (575) 646-3200"),

 ("2026-08-20", "Aug 20, 2026", "UNM",
  "⚠ STUDENT ORGANIZATION DAY — 10am-2pm, Duck Pond",
  "~200 of UNM's 350+ registered student orgs table here. The best single day to meet "
  "student leaders on any New Mexico campus.",
  "https://sac.unm.edu/events/welcome-back-days.html",
  "Student Activities Center · (505) 277-4706"),

 ("2026-08-20", "Aug 20, 2026", "NMSU",
  "Last day to add a class WITHOUT instructor's signature",
  "With signature: Aug 28. Census (last day to cancel without a W): Sep 4.",
  "https://records.nmsu.edu/academic-calendar/2026.html",
  "NMSU Registrar / Records"),

 ("2026-08-21", "Aug 21, 2026", "UNM",
  "⚠⚠ CAMPUS EMPLOYMENT & COMMUNITY SERVICE DAY — 10am-2pm, Duck Pond",
  "THE SLOT STRUCTURALLY AIMED AT OFF-CAMPUS ENTITIES, and the most permissive documented "
  "on-campus tabling opportunity in New Mexico. Eligibility for a for-profit crypto project "
  "is UNCONFIRMED and no fee is published — call SAC before travelling.",
  "https://sac.unm.edu/events/welcome-back-days.html",
  "Haley Johnson · hagjohnson44@unm.edu · (505) 277-4706"),

 ("2026-08-24", "Aug 24, 2026", "ENMU",
  "Fall 2026 classes begin — ⚠ one week later than UNM/NMT/NMHU",
  "Semesters plus 8-week AND 4-week session overlays. ⚠ Finals week is AMBIGUOUS: classes "
  "end Dec 4 and winter break starts Dec 5, leaving no gap. Do not quote ENMU finals dates "
  "without confirming.",
  "https://www.enmu.edu/academics/academic-resources-services/catalogs-schedules-calendars/academic-calendar",
  "ENMU Student Affairs · (575) 562-2221"),

 ("2026-08-25", "Aug 25, 2026", "NMSU",
  "Student Employment Fair — 10am-1pm, Aggie Lounge, Corbett Center",
  "The ONE confirmed Fall 2026 date in NMSU's welcome window. Crimson Kickoff's own "
  "schedule is published as an image and no other Fall 2026 date could be read.",
  "https://oel.nmsu.edu/career-events/career-fairs--future-dates.html",
  "NMSU Office of Experiential Learning"),

 ("2026-08-28", "Aug 28, 2026", "CNM",
  "⚠⚠ Fall 2026 EARLY PAYMENT DEADLINE",
  "Hard money deadline for students; useful as a proxy for when CNM's enrolled population "
  "locks in. Late payment deadline Sep 4.",
  "https://cnm.enterprise.localist.com/",
  "Ask CNM · (505) 224-3000, press 0"),

 ("2026-08-28", "Aug 28, 2026", "NM Highlands",
  "Last day to drop (full term)",
  "Academic census Sep 4.",
  "https://www.nmhu.edu/academic-calendar/",
  "NMHU switchboard · (505) 425-7511"),

 ("2026-08-31", "Aug 31, 2026", "CNM",
  "⚠⚠ CNM FALL 2026 TERM BEGINS — THE SECOND ALBUQUERQUE WINDOW",
  "LATEST START IN NEW MEXICO, two full weeks after UNM IN THE SAME CITY. An ambassador who "
  "works UNM's Welcome Back Days (Aug 14-21) can work CNM's opening with ZERO calendar "
  "conflict. Highest-leverage logistics fact in the state. Term ends Dec 13.",
  "https://cnm.enterprise.localist.com/",
  "CNM Student Activities · (505) 224-3238"),

 ("2026-09-04", "Sep 4, 2026", "CNM",
  "⚠⚠ Fall 2026 LATE PAYMENT DEADLINE",
  "Second hard money deadline. NMSU census and NMHU census also fall on this date.",
  "https://cnm.enterprise.localist.com/",
  "Ask CNM · (505) 224-3000, press 0"),

 ("2026-09-07", "Sep 7, 2026", "Statewide",
  "Labor Day — no classes / campus closures",
  "Confirmed at NMSU, ENMU, NMHU and CNM. Do not schedule anything in New Mexico this day.",
  "https://records.nmsu.edu/academic-calendar/2026.html",
  ""),

 ("2026-09-09", "Sep 9, 2026", "UNM",
  "Engineering & Science Career Fair — 10am-2pm, SUB Ballrooms",
  "Handshake registration. ⚠ Employer cost and deadline are behind the employer login and "
  "UNPUBLISHED. ⚠ Note UNM's EMPLOYER-facing career fair page is TEN YEARS STALE (shows "
  "Fall 2016) — use the student-facing page, which is correct.",
  "https://career.unm.edu/students--alumni/career-fairs.html",
  "UNM Career Services · career4u@unm.edu · (505) 277-2531"),

 ("2026-09-15", "Sep 15-16, 2026", "NMSU",
  "⚠ CAREER EXPO — 9am-2pm, 3rd Floor Ballrooms, Corbett Center",
  "NMSU's largest employer event and its best audience-matched paid channel. Engineering, "
  "Science and Technology Fair runs concurrently on Sep 16. Employer cost UNVERIFIED.",
  "https://oel.nmsu.edu/career-events/career-fairs--future-dates.html",
  "NMSU Office of Experiential Learning"),

 ("2026-09-17", "Sep 17, 2026", "CNM",
  "Fall 2026 census date",
  "Special registration request deadline Sep 21.",
  "https://cnm.enterprise.localist.com/",
  "Ask CNM · (505) 224-3000"),

 ("2026-09-24", "Sep 24, 2026", "UNM",
  "⚠ BUSINESS & ACCOUNTING CAREER FAIR — 10am-2pm, SUB Ballrooms",
  "THE BEST AUDIENCE-MATCHED PAID CHANNEL AT UNM — a room full of finance and accounting "
  "majors you buy into rather than argue your way into, and the natural fallback if the "
  "Welcome Back Days answer is no. Handshake registration; cost UNVERIFIED.",
  "https://career.unm.edu/students--alumni/career-fairs.html",
  "UNM Career Services · career4u@unm.edu · (505) 277-2531"),

 ("2026-10-05", "Oct 5-10, 2026", "NM Highlands",
  "⚠ MID-TERM EXAM WEEK — dead zone",
  "Followed immediately by fall break Oct 12-13. The first half of October is unusable for "
  "outreach at NMHU.",
  "https://www.nmhu.edu/academic-calendar/",
  "NMHU switchboard · (505) 425-7511"),

 ("2026-10-07", "Oct 7, 2026", "NMSU",
  "Graduate and Professional School Fair — 10am-2pm, Aggie Lounge, Corbett Center",
  "",
  "https://oel.nmsu.edu/career-events/career-fairs--future-dates.html",
  "NMSU Office of Experiential Learning"),

 ("2026-10-08", "Oct 8-9, 2026", "UNM",
  "Fall break (Thu-Fri) — 4-day weekend",
  "The only UNM break confirmed on the ten-year calendar.",
  "https://registrar.unm.edu/academic-calendar/ten-year-semester-dates-calendar.html",
  "UNM Registrar · (505) 277-8900"),

 ("2026-10-12", "Oct 12-13, 2026", "NM Highlands",
  "Fall break (Mon-Tue) — no classes",
  "⚠ THE ONLY DISCRETE OCTOBER FALL BREAK OF THE SIX NEW MEXICO CAMPUSES.",
  "https://www.nmhu.edu/academic-calendar/",
  "NMHU switchboard · (505) 425-7511"),

 ("2026-10-12", "Oct 12, 2026", "NMSU",
  "Indigenous People's Day — special programming, CLASSES CONTINUE",
  "⚠ Not a break. NMSU has NO October fall break at all in Fall 2026.",
  "https://records.nmsu.edu/academic-calendar/2026.html",
  "NMSU Records"),

 ("2026-10-15", "Oct 15, 2026", "NMSU",
  "Last day to withdraw from a single course with a 'W'",
  "",
  "https://records.nmsu.edu/academic-calendar/2026.html",
  "NMSU Records"),

 ("2026-10-29", "Oct 29, 2026", "UNM",
  "Graduate & Professional School Fair — 10am-2pm, SUB Ballrooms",
  "",
  "https://career.unm.edu/students--alumni/career-fairs.html",
  "UNM Career Services · (505) 277-2531"),

 ("2026-11-04", "Nov 4, 2026", "NMSU",
  "Health Professions Career Fair — 2-5pm, Aggie Lounge, Corbett Center",
  "Low relevance to DGD; listed for calendar completeness.",
  "https://oel.nmsu.edu/career-events/career-fairs--future-dates.html",
  "NMSU Office of Experiential Learning"),

 ("2026-11-23", "Nov 23-28, 2026", "Statewide",
  "⚠ THANKSGIVING DEAD ZONE — schedule nothing in New Mexico",
  "NMSU, NM Tech and ENMU all close the FULL WEEK Nov 23-27. NMHU's Fall Recess runs Nov "
  "25-28, so NMHU students are on campus Mon-Tue only. UNM's Thanksgiving dates are "
  "UNRETRIEVABLE — confirm with the registrar.",
  "https://records.nmsu.edu/academic-calendar/2026.html",
  "UNM Registrar (505) 277-8900 for the UNM dates"),

 ("2026-12-03", "Dec 3, 2026", "NM Tech",
  "Last day of classes",
  "Finals Dec 7-11 — the widest last-class-to-finals gap of the six NM campuses (reading "
  "break Dec 4-6).",
  "https://docs.google.com/spreadsheets/d/11m7XFlZc77ZjqjDMsmVdtnUW3VpTgklC4CCw1taiOfc/edit",
  "NMT Registrar · (575) 835-5133"),

 ("2026-12-04", "Dec 4, 2026", "ENMU",
  "Classes end — ⚠ winter break begins Dec 5, leaving NO GAP for finals",
  "Either finals are embedded in the final instructional week or the calendar's finals rows "
  "did not render. DO NOT quote ENMU finals dates without confirming.",
  "https://www.enmu.edu/academics/academic-resources-services/catalogs-schedules-calendars/academic-calendar",
  "ENMU Student Affairs · (575) 562-2221"),

 ("2026-12-07", "Dec 7-11, 2026", "NMSU / NM Tech / NM Highlands",
  "Finals week at three campuses simultaneously",
  "NMSU finals COINCIDE with its final instructional week (last day of classes Dec 11); NM "
  "Tech and NMHU follow the conventional pattern. Term ends Dec 11 at NMSU and NMHU.",
  "https://records.nmsu.edu/academic-calendar/2026.html",
  ""),

 ("2026-12-13", "Dec 13, 2026", "CNM",
  "Fall 2026 term ends",
  "Latest term end in New Mexico, matching its latest start.",
  "https://cnm.enterprise.localist.com/",
  "Ask CNM · (505) 224-3000"),

 # ── MONITOR-ONLY (no date published) ────────────────────────────────────────
 ("", "Date not published", "NMSU",
  "⚠ MONITOR — Crimson Kickoff Fall 2026 schedule, including the AGGIE CARNIVAL",
  "crimsonkickoff.nmsu.edu publishes its schedule AS AN IMAGE with no text alternative and "
  "the footer reads 2025 — not one Fall 2026 date could be read. Pattern from the confirmed "
  "2025 cycle: roughly two weeks from move-in through the first week and a half of classes; "
  "the org-fair analogue is the Aggie Carnival, 11am-2pm, International Mall.",
  "https://crimsonkickoff.nmsu.edu/",
  "NMSU SILP · silp@nmsu.edu · (575) 646-3200"),

 ("", "Date not published", "NM Tech / ENMU / NM Highlands / CNM",
  "⚠ MONITOR — no involvement fair date published at FOUR of the six campuses",
  "None of these four publishes a Fall 2026 involvement fair, club fair or welcome-week "
  "tabling event, AND none documents a recurring pattern either — so there is not even a "
  "historical shape to plan against. Four calls close it.",
  "https://techconnect.nmt.edu/",
  "NMT (575) 835-5880 · ENMU (575) 562-2108 · NMHU (505) 425-7511 · CNM (505) 224-3238"),

 ("", "Spring 2027 — start the conversation this fall", "UNM",
  "⚠ MONITOR — Lobo Hackathon sponsorship for Spring 2027",
  "THE HACKATHON LEVER DOES NOT EXIST IN NEW MEXICO IN FALL 2026. The Lobo Hackathon is "
  "SPRING ONLY (Apr 9-10, 2026, already run and closed); no Fall 2026 hackathon was found "
  "at any of the six campuses. Open the Spring 2027 sponsorship conversation with Rainforest "
  "Innovations while in Albuquerque this fall.",
  "https://innovations.unm.edu/program-activities/lobo-hackathon/",
  "UNM Rainforest Innovations · Info@innovations.unm.edu · (505) 272-7900"),

 ("", "No date — call anytime", "NMSU",
  "⚠⚠ HIGHEST-VALUE UNDATED ACTION IN THE STATE — Nusenda FinTech Lab",
  "The ONLY unit in New Mexico higher education that names DIGITAL ASSETS as a published "
  "program focus area (with Payments, Alternative Lending, Capital Markets, Consumer "
  "Finance, RegTech, WealthTech). Ask for Carlos Cuesta, Program Director. ⚠ The lab's own "
  "events calendar is STALE to early 2024 — contact the director directly rather than "
  "waiting for a posted event.",
  "https://arrowheadcenter.nmsu.edu/program/nusenda_fintech_lab/index.html",
  "Carlos Cuesta · carlosic@nmsu.edu · Arrowhead Center (575) 646-7415"),

 ("", "No date — close before relying on any NM policy claim", "Statewide",
  "⚠ MONITOR — NEW MEXICO HAS NO CAMPUS FREE-SPEECH STATUTE (high confidence, formally "
  "unverified)",
  "UNM's own free-speech portal lists the state statutes it considers applicable and EVERY "
  "ONE IS A CRIMINAL-CODE PROVISION (§30-14-1 trespass, §30-20-1 disorderly conduct, "
  "§30-20-3 unlawful assembly, §30-14-4(2) wrongful use of public property). NMSU's ARP "
  "3.63 grounds itself in the First Amendment and the NM Constitution, not a statute. No "
  "enactment appeared in legislative or advocacy-tracker sources. ⚠ The web-search budget "
  "was exhausted before an exhaustive nmlegis.gov bill search could be completed — VERIFY "
  "BEFORE RELYING ON IT IN WRITING. Consequence: unlike Arizona, Colorado, Utah and "
  "Arkansas, there is NO statutory lever in New Mexico — only First Amendment public-forum "
  "doctrine and each institution's own policy.",
  "https://www.nmlegis.gov/Legislation/Bill_Finder",
  ""),

 ("", "No date — blocking for ENMU and CNM", "ENMU / CNM",
  "⚠⚠ MONITOR — two campuses' solicitation policies are UNREADABLE",
  "ENMU's entire solicitation and facility policy sits in a Student Handbook PDF hosted on "
  "SharePoint that is ROBOTS-BLOCKED, and its policies-procedures page 404s — ENMU's access "
  "rating is a PROVISIONAL PLACEHOLDER. CNM makes 'soliciting or selling in violation of "
  "the solicitation policy' a punishable offence while THE POLICY ITSELF IS UNPUBLISHED and "
  "three policy-manual URLs return 404. Neither campus can be assessed until someone reads "
  "the document aloud.",
  "https://www.enmu.edu/greyhound-life/student-handbook",
  "ENMU Student Affairs (575) 562-2221 · CNM Dean of Students (505) 224-4342"),

 ("", "No date — blocking for UNM", "UNM",
  "⚠⚠ MONITOR — full text of UNM RPM 2.12 (Advertising, Sales and Solicitations)",
  "The numbered operative subsections would not render on either the http or https URL; "
  "only the preamble is readable. THIS IS THE POLICY THAT ACTUALLY DECIDES whether DGD may "
  "solicit at UNM, and it is the single most important unretrieved document in New Mexico. "
  "Also ask for the unpublished External Organizational Rate card while on the phone.",
  "https://policy.unm.edu/regents-policies/section-2/2-12.html",
  "UNM Policy Office / University Counsel · (505) 277-2069"),
]
