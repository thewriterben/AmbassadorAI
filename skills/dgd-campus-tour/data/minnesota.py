"""Minnesota — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published at time of research — a gap to close by phone, not a finding of absence.
Schema: reference/data-schema.md

STATEWIDE LEGAL CONTEXT — read before any ambassador cites a statute:

⚠ MINNESOTA HAS NO CAMPUS FREE-SPEECH STATUTE. Minn. Stat. ch. 135A (Postsecondary
Education) was read section by section; its full headnote list contains NO section on free
expression, free speech, expressive activity, public forums or student speech. Minnesota did
NOT enact a FORUM/Goldwater-style campus-speech act. At the four public campuses only direct
First Amendment forum doctrine applies; at the four private campuses there is no forum right
at all. DO NOT tell anyone Minnesota has a campus free-speech law.
https://www.revisor.mn.gov/statutes/cite/135A/full

⚠⚠ WHAT MINNESOTA DOES HAVE — Minn. Stat. s 135A.145, "SALE OF STUDENT INFORMATION;
MARKETING CREDIT CARDS." It reaches "a public or private postsecondary educational
institution, INCLUDING ITS AGENTS, EMPLOYEES, STUDENT OR ALUMNI ORGANIZATIONS, OR
AFFILIATES," and bars (a) transferring an undergraduate's contact information to any card
issuer without written permission and (b) entering "any agreement to market credit cards to
undergraduate students." TILA definitions (15 U.S.C. 1602); AG enforcement under s 8.31.
This is why St. Cloud State bans "credit card or debit card sign-ups" and Augsburg bans
"credit card promotions." Full text in the U of M Twin Cities policy_key below.

TWO SEPARATE SYSTEMS — DO NOT CONFLATE THEM.
(a) University of Minnesota system, Board of Regents: TWIN CITIES and DULUTH. Policy layer
    is policy.umn.edu plus the SUA Student Group Policies. Note UMD does NOT follow the Twin
    Cities calendar — they start EIGHT DAYS APART.
(b) Minnesota State, Board of Trustees, 33 colleges and universities: MANKATO, ST. CLOUD
    STATE, WINONA STATE, METROPOLITAN STATE. System layer is Board Policy 3.1 (students
    only) and System Procedure 6.7.2 (facilities as lessor). Both quoted in the Mankato
    policy_key, which is the anchor for the Minnesota State system note.

⚠ THE TWIN CITIES DENSITY FACT — the single most important planning fact in the state. FIVE
of these ten campuses sit inside the Minneapolis–St. Paul metro within roughly twenty minutes
of each other: U of M Twin Cities (300 Washington Ave SE, Mpls), Augsburg (2211 Riverside
Ave, Mpls — 1.5 miles from the U), St. Thomas (2115 Summit Ave, St. Paul), Macalester (1600
Grand Ave, St. Paul — one mile from St. Thomas, same street, ACTC cross-registration), and
Metro State (700 E 7th St, St. Paul). Build the tour as a Twin Cities base with three spokes
— Duluth 2.5 hrs north, Mankato 1.5 hrs southwest, Winona 2 hrs southeast, St. Cloud 1 hr
northwest, Northfield/Carleton 45 min south — NOT as a linear drive.

⚠ CALENDAR SPREAD IS THE WIDEST OF ANY STATE IN THIS PROJECT: seventeen days from Metro
State (Sat Aug 22) to Carleton (Mon Sep 14). NINE SEMESTER SCHOOLS, ONE TRIMESTER SCHOOL.
Carleton's fall term ENDS NOV 23 — there is no December window at Carleton at all.
"""

STATE = 'Minnesota'

CAMPUSES = [

 # ------------------------------------------------- 1. U of M TWIN CITIES
 {'state': 'Minnesota',
  'name': 'University of Minnesota Twin Cities',
  'city': 'Minneapolis / St. Paul, MN',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 4,
  'start': 'Tue Sep 8, 2026 (the day after Labor Day, Mon Sep 7) ⚠ SECOND-LATEST START IN THE STATE — '
           'a full 17 days after Metro State and 15 days after Mankato/St. Cloud/Winona.',
  'adddrop': 'UNVERIFIED. UMN publishes drop/add deadlines on a separate filtered tool at '
             'https://onestop.umn.edu/calendar/dropadd-deadlines which is JavaScript-filtered and returned no '
             'Fall 2026 rows to research tooling; a parameterised academic-calendar URL was ROBOTS-BLOCKED. '
             'Deadlines are course-specific at UMN in any case.',
  'fallbreak': '⚠ NONE — UMN Twin Cities has NO October fall break. From Sep 8 to Nov 25 the campus runs at '
               'full density for eleven straight weeks — the longest uninterrupted window of any campus in '
               'this set.',
  'thanksgiving': '⚠ PARTIAL — Thu–Fri Nov 26–27, 2026 per the third-party aggregator acadcalendar.com; NOT '
                  'confirmed on any umn.edu page. The governance-approved ASR calendar as rendered did not '
                  'surface a Thanksgiving row. Treat as the historical pattern and confirm by phone before '
                  'scheduling the week of Nov 23.',
  'lastclass': 'Last day of instruction Wed Dec 16, 2026',
  'finals': 'Thu–Sat Dec 17–19 and Mon–Wed Dec 21–23, 2026. Study day Sun Dec 20. Term ends Wed Dec 23. '
            '70 class days in the term.',
  'cal_url': 'https://asr.umn.edu/2026-27-twin-cities-and-rochester-calendar',
  'cal_status': 'CONFIRMED — governance-approved calendar published by Academic Support Resources, approved by '
                'the Senate Committee on Educational Policy Jan 18, 2023 and the Faculty Senate Feb 23, 2023. '
                'The calendar-governing policy (https://policy.umn.edu/education/academiccalendar) requires '
                '"a minimum of 70 days of instruction, a maximum of 75 days of instruction, and approximately '
                'one week of final examinations." ⚠ onestop.umn.edu/calendar/academic-calendar and '
                'asr.umn.edu/dates-and-deadlines are JavaScript FILTER UIs that return NO dates to research '
                'tooling — do not send anyone there expecting an answer.',
  'fair': '⚠ EXPLORE U — the one paid door at the flagship, and outside businesses are EXPLICITLY admitted '
          'and priced. (Separately: the Fall Activities Fairs, which are student-groups-only and useless to DGD.)',
  'fair_date': '⚠⚠ Sat Sep 5, 2026, 1:00–4:30 p.m., HUNTINGTON BANK STADIUM — CONFIRMED on the University\'s '
               'own Orientation & Transition Experiences page. Over 4,000 new and current student leaders. '
               'Held "the Saturday before Labor Day" every year, i.e. THREE DAYS BEFORE CLASSES START, during '
               'move-in weekend. // SEPARATELY, student-groups-only and NOT available to DGD: Fall Activities '
               'Fair Minneapolis Tue Sep 22, 2026, 11:00 a.m.–2:00 p.m., Coffman Memorial Union; and St. Paul '
               'Wed Sep 23, 2026, 11:00 a.m.–1:00 p.m., St. Paul Student Center.',
  'fair_outside': '⚠ YES — AND IT IS THE ONLY "YES" AT THE FLAGSHIP. Verbatim: "EXPLORE U IS A GREAT '
                  'OPPORTUNITY FOR LOCAL BUSINESSES AND ORGANIZATIONS TO ACCESS INCOMING FIRST-YEAR AND '
                  'INCOMING TRANSFER STUDENTS." Only exclusion published: "The University of Minnesota is a '
                  'Drug-Free and Smoke-Free campus. Businesses and organizations promoting, selling, or '
                  'distributing items prohibited on campus... are not allowed to participate in Explore U." '
                  '// ⚠ DO NOT CONFUSE THE TWO EVENTS. The Activities Fairs are for "Any currently-registered '
                  'student group... in good standing" and the page states flatly: "EXPLORE U AND THE FALL AND '
                  'SPRING ACTIVITIES FAIRS ARE FOR REGISTERED STUDENT GROUPS ONLY" — that sentence governs the '
                  'Activities Fairs; the OTE page governs Explore U vendor booths. Confirm which is which on '
                  'the call.',
  'fair_cost': '$600 Maroon registration (basic booth package) · $1,150 Gold registration (adds logo on the '
               'jumbotron and an Explore U Passport feature) · $550 per additional booth (Gold level only). '
               'Partial payment via trade accepted up to 50% of fees in gift cards / new items. // SEPARATE '
               'AND LARGER DOOR: corporate sponsorship of Orientation, MINIMUM $6,000, reaching "15,000 '
               'participants through Orientation, Welcome Week, and first-year and second-year programming," '
               'with benefits listed as promotional item giveaways, meals AND TABLING OPPORTUNITIES. // The '
               'Activities Fairs are free and closed to DGD.',
  'fair_deadline': '⚠⚠ TIMING CONFLICT — CALL TODAY. The sponsors-and-partners overview states "TABLE SPACE '
                   'GOES ON SALE IN LATE SPRING, and the event takes place the Saturday before Labor Day." The '
                   'Explore U page, fetched Aug 11–12 2026, still says "REGISTRATION WILL OPEN IN THE COMING '
                   'WEEKS" for 2026. Those two statements cannot both be current — either the Explore U page is '
                   'stale and booths sold out in spring, or registration genuinely slipped. THE EVENT IS 24 '
                   'DAYS OUT. This is a phone call, not an email: (612) 624-1979.',
  'fair_url': 'https://ote.umn.edu/about-ote/sponsors-partners/explore-u-event',
  'policy': 'SUA Student Group Policies (the operative anti-fronting text) + SUA Fundraising page + SUA Event '
            'Services rates and reservation policies + Administrative Policy "Using and Leasing University '
            'Outdoor Space: Twin Cities" (effective August 2008) + Administrative Policy "Major Events" '
            '(effective September 2020)',
  'policy_url': 'https://sua.umn.edu/student-group-policies',
  'policy_key': "⚠⚠ STATE NOTE — MINNESOTA HAS NO CAMPUS FREE-SPEECH STATUTE. Minn. Stat. ch. 135A "
                "(Postsecondary Education) was read section by section; its full headnote list contains NO "
                "section on free expression, free speech, expressive activity, public forums or student "
                "speech (https://www.revisor.mn.gov/statutes/cite/135A/full). There is no FORUM/Goldwater-"
                "style act, no statutory ban on free-speech zones, no statutory outdoor-forum guarantee. At "
                "the four public campuses only direct First Amendment forum doctrine applies; at the four "
                "private campuses there is no forum right at all. DO NOT CLAIM A MINNESOTA CAMPUS SPEECH "
                "LAW. Argue fit and pay the fee; do not argue rights. "
                "⚠⚠ STATE NOTE — WHAT MINNESOTA DOES HAVE, AND IT IS AIMED STRAIGHT AT US: Minn. Stat. "
                "s 135A.145, 'SALE OF STUDENT INFORMATION; MARKETING CREDIT CARDS' "
                "(https://www.revisor.mn.gov/statutes/cite/135A.145). Scope, verbatim: it applies to a "
                "'PUBLIC OR PRIVATE POSTSECONDARY EDUCATIONAL INSTITUTION, INCLUDING ITS AGENTS, EMPLOYEES, "
                "STUDENT OR ALUMNI ORGANIZATIONS, OR AFFILIATES.' It prohibits (1) selling, giving or "
                "otherwise transferring TO ANY CARD ISSUER the name, address, telephone number or other "
                "contact information OF AN UNDERGRADUATE STUDENT without that student's written permission, "
                "and (2) entering into 'ANY AGREEMENT TO MARKET CREDIT CARDS TO UNDERGRADUATE STUDENTS.' "
                "'Credit,' 'credit card' and 'card issuer' take their federal Truth in Lending Act meanings, "
                "15 U.S.C. s 1602. Enforcement is by the Minnesota Attorney General under Minn. Stat. s 8.31. "
                "BECAUSE IT REACHES STUDENT ORGANIZATIONS AND AFFILIATES, NOT JUST THE INSTITUTION, it is "
                "almost certainly the origin of St. Cloud State's ban on 'credit card or debit card sign-ups' "
                "and Augsburg's ban on 'credit card promotions.' HAVE THE ANSWER READY, UNPROMPTED: DGD is "
                "not a card issuer under 15 U.S.C. s 1602 and runs no credit sign-ups. Do not collect card "
                "numbers. Do not run anything that looks like a card sign-up. "
                "⚠ STATE NOTE — MINNESOTA CONSUMER DATA PRIVACY ACT, Minn. Stat. ss 325M.10–.21, EFFECTIVE "
                "JULY 31, 2025. APPLICABILITY THRESHOLD, per the Minnesota Attorney General's own "
                "announcement, verbatim: 'BUSINESSES ARE SUBJECT TO THE MINNESOTA CONSUMER DATA PRIVACY ACT "
                "IF THEY CONTROL OR PROCESS THE PERSONAL DATA OF 100,000 OR MORE MINNESOTA RESIDENTS, OR IF "
                "THEY EARN OVER 25% OF THEIR REVENUE FROM THE SALE OF PERSONAL DATA AND PROCESS OR CONTROL "
                "PERSONAL DATA OF 25,000 CONSUMERS OR MORE.' Certain education-technology providers are "
                "separately covered. (https://www.ag.state.mn.us/Office/Communications/2025/07/28_MCDPA.asp; "
                "s 325M.10 is the citation section and s 325M.11 is definitions only — the numeric thresholds "
                "are not retrievable from either, the AG page is the source.) REALISTIC READ: a campus tour "
                "will not touch 100,000 Minnesotans. The exposure is the 25%-of-revenue + 25,000-consumer "
                "prong if DGD monetises data, plus the AG enforcement hook and consumer rights to know, "
                "delete and opt out. COLLECT THE MINIMUM AT A TABLE — an email address and nothing else. Do "
                "not collect phone number, wallet address and ID in one pass. "
                "⚠ STATE NOTE — FAVOURABLE LEGISLATIVE BACKDROP, USE IT AS AN OPENER: HF 3709 (2026), signed "
                "by Gov. Tim Walz, EFFECTIVE AUGUST 1, 2026 — eleven days before this tour window — "
                "authorises Minnesota STATE-CHARTERED BANKS AND CREDIT UNIONS to 'hold virtual currency and "
                "the cryptographic keys that control it on behalf of customers and members,' subject to "
                "written risk-management and cybersecurity policies, 60 days' advance written notice to the "
                "Minnesota Commissioner of Commerce, and strict segregation of client digital assets. "
                "Minnesota joins New York, Wyoming and Virginia "
                "(https://bitcoinmagazine.com/news/minnesota-law-opens-crypto-custody). Also pending, NOT "
                "enacted: the MINNESOTA BITCOIN ACT, SF 2661 / HF 2946, 94th Legislature 2025-26, authored by "
                "Sen. Jeremy Miller — would allow payment to the state in cryptocurrency and authorise the "
                "State Board of Investment to invest in it "
                "(https://www.revisor.mn.gov/bills/text.php?number=SF2661&version=0&session=ls94&session_year=2025&session_number=0). "
                "=== NOW THE CAMPUS RULE === "
                "⚠ THERE IS NO FREE-STANDING 'SOLICITATION' POLICY IN THE UMN POLICY LIBRARY. Searches "
                "returned nothing. The operative language lives in a STUDENT-UNION BYLAW, not a Regents "
                "policy — so if you are told 'it's against university policy,' ASK WHICH POLICY. The answer "
                "is SUA Student Group Policies (https://sua.umn.edu/student-group-policies). "
                "ARTICLE XI, SECTION 6, SUBD 17 — THE FLAT PROHIBITION, VERBATIM: 'UNIVERSITY POLICY "
                "PROHIBITS THE USE OF UNIVERSITY PROPERTY BY NON-UNIVERSITY ENTITIES FOR THE PURPOSE OF "
                "REVENUE GENERATION OR THE SALE, SOLICITATION, OR PROMOTION OF GOODS OR SERVICES.' "
                "ARTICLE XI, SECTION 6, SUBD 10 — THE NARROW EXCEPTION, VERBATIM: 'Off-campus agencies, "
                "nonprofit organizations, musicians, guest speakers, or performing artists SHALL NOT BE "
                "PERMITTED TO SOLICIT FUNDS ON CAMPUS UNLESS they have a contract with the University of "
                "Minnesota OR ARE SPONSORED BY A STUDENT GROUP.' "
                "ARTICLE XVI, SECTION 7, SUBD 2 — THE CONTACT-TABLE BAR, VERBATIM: 'STUDENT GROUPS ARE NOT "
                "PERMITTED TO RESERVE CONTACT TABLES ON BEHALF OF UNIVERSITY DEPARTMENTS OR EXTERNAL "
                "ORGANIZATIONS.' Same subdivision: 'Food and beverages or the sales of food and beverages are "
                "not permitted at any indoor contact tables.' "
                "⚠ ARTICLE III, SECTION 4 — ANTI-FRONTING, BY NAME. Student groups are prohibited from "
                "providing 'inappropriate access to student group resources' to non-registered groups, A "
                "PRACTICE THE POLICY ITSELF CALLS 'FRONTING.' Violations can bring disciplinary action and a "
                "change to the group's registered status. "
                "⚠ THE SHARPEST SENTENCE IF CHALLENGED AT A TABLE — SUA Fundraising page "
                "(https://sua.umn.edu/fundraising), VERBATIM: 'PERSONNEL FROM NON-UNIVERSITY VENDORS OR "
                "COMPANIES ARE NOT ALLOWED AT THE CONTACT TABLE, WHEN SALES OR SALES-RELATED, FUNDRAISING OR "
                "COMMERCIAL ACTIVITIES ARE BEING CONDUCTED.' Same page: student groups may conduct on-campus "
                "sales and fundraising 'up to 5 days per semester' and one bake sale per semester; 'Sales "
                "and/or fundraising activities shall not be conducted in classrooms, campus offices, "
                "residential facilities, and/or other University buildings, without written consent.' "
                "DOES SPONSORSHIP CURE IT? PARTIALLY, AND NOT FOR A TABLE. Subd 10 permits a sponsored "
                "off-campus agency to solicit — but Art. XVI s 7 Subd 2 forbids the student group from "
                "reserving the contact table for you, and the fundraising page forbids your personnel from "
                "standing at it. What the policy actually contemplates is a STUDENT-GROUP EVENT WITH A "
                "SPONSOR, subject to: 'THE PRIMARY PURPOSE OF THE EVENT CANNOT BE NON-UNIVERSITY SPONSOR "
                "PRESENCE, PROMOTION, OR SALES'; 'Insurance requirements and sponsorship agreements may be "
                "required'; and 'If promotional materials, including apparel, are created with sponsor logos, "
                "the sponsorship must be acknowledged via text as to not imply a University partnership.' "
                "MONEY TERMS FOR NON-UNIVERSITY BOOKINGS (SUA Event Services, "
                "https://reservesua.umn.edu/rates-payments): three client tiers — Registered Student Group / "
                "University Department / UNIVERSITY GUEST. Coffman Great Hall 0–8 hrs is $550 / $1,100 / "
                "$2,200 respectively. ⚠ NON-REFUNDABLE DEPOSIT, VERBATIM: 'A NON-REFUNDABLE DEPOSIT OF 50% OF "
                "THE ROOM RATE IS DUE AT THE TIME OF BOOKING. The remaining balance is due at least 30 days "
                "prior to the event date.' Non-University groups must sign a FACILITY USE AGREEMENT and "
                "provide 'PROOF OF INSURANCE' before reserving — ⚠ NO DOLLAR LIMIT IS PUBLISHED. Cancellation "
                "ladder (https://reservesua.umn.edu/reservation-policies): 25% of fee at 91–180 days out, "
                "rising to 100% OF FEE AT 0–5 DAYS. Contact-table terms: 'The reservation includes a maximum "
                "of one six-foot table and two chairs, no additional furniture is allowed'; 'A group is only "
                "permitted one contact table reservation, for a maximum of five hours, each day.' "
                "OUTDOORS — 'Using and Leasing University Outdoor Space: Twin Cities,' effective AUGUST 2008, "
                "responsible officers the VP for University Services and the VP for Student Affairs "
                "(https://policy.umn.edu/operations/outdoor). Assemblies under 100 participants need no permit "
                "at five designated plazas, BUT 'ANY GATHERING BY NON-UNIVERSITY PERSONS OR ENTITIES "
                "(REGARDLESS OF NUMBER OF PARTICIPANTS)' outside rallies and demonstrations must go through "
                "the Real Estate Office's Use and Lease of Real Estate protocol. Outdoor Events Office FAQ, "
                "verbatim: 'GUESTS OF THE UNIVERSITY OF MINNESOTA PAY A FLAT FEE AS A PART OF THE FACILITY "
                "USE AGREEMENT THEY COMPLETE WITH THE REAL ESTATE OFFICE' — ⚠ THE FLAT FEE AMOUNT IS NOT "
                "PUBLISHED ANYWHERE. Student groups and departments pay nothing. Permit lead times: 14 days "
                "standard, 30 days if security or traffic management is needed, 12 weeks for large events and "
                "concerts (https://outdoor.umn.edu/faq). "
                "MAJOR EVENTS POLICY, effective SEPTEMBER 2020 (https://policy.umn.edu/operations/majorevents): "
                "'This policy applies to ANYONE, be it an individual, a group, an academic department, "
                "college, or administrative unit, proposing to host a major event.' Major Event Proposal form "
                "to the Major Events Committee, review 'up to 14 business days'; the requester must 'Pay the "
                "University for all allocable costs' and is responsible for repair costs for any damage. "
                "PAYMENT CREDENTIALS / SIGNING CONTRACTS ON SITE: nothing in the UMN documents reaches "
                "payment apps or on-site contract signing. The reachable constraint is the STATE statute, "
                "s 135A.145 above, which binds the University AND its student organizations.",
  'sponsor_required': '⚠ NO — AND SPONSORSHIP DOES NOT GET YOU A TABLE. Art. XI s 6 Subd 10 allows a '
                      'student-group-sponsored off-campus agency to solicit, but Art. XVI s 7 Subd 2 forbids '
                      'the group from reserving a contact table on your behalf and the fundraising page bars '
                      'your personnel from standing at one during commercial activity — and Art. III s 4 calls '
                      'the workaround "fronting" and attaches disciplinary exposure for the students. THE ONLY '
                      'CLEAN ROUTE IS TO BUY A BOOTH AT EXPLORE U ($600/$1,150, Sat Sep 5) OR SPONSOR '
                      'ORIENTATION ($6,000 minimum). Do not spend three weeks courting the Blockchain Club for '
                      'table access it cannot legally give you — court it for a speaker slot instead, which no '
                      'rule here touches.',
  'clubs': [('⚠ UMN Blockchain Club (UMNBC) — ACTIVE, and the best student-side asset in Minnesota',
             'Registered on GopherLink as group #4465. The Minnesota Daily (Nov 13, 2025) describes it as '
             'drawing "primarily from computer science and business students" and running "lectures and '
             'discussions on blockchain fundamentals and programming," beginner-friendly and building knowledge '
             'progressively — i.e. exactly the audience DGD wants and a format that welcomes an outside '
             'speaker. ⚠ ACCESS PROBLEMS, ALL THREE OF THEM: gopherlink.umn.edu/4465/contact-us/ is '
             'LOGIN-GATED (fetch returned only a "Loading" shell and navigation); www.umnblockchain.org and '
             'www.umnbc.org are BOTH ROBOTS-BLOCKED to research tooling (robots.txt fetch failed / '
             'ConnectError), as is www.umnblockchain.org/events. The Daily article names a club president; '
             'that name is nearly a year old and rosters rotate — DO NOT USE IT. Route in through the '
             'Minnesota Blockchain Initiative (connect@mnblockchain.org), which the Daily names as a '
             'collaborator.',
             'https://gopherlink.umn.edu/4465/contact-us/'),
            ('⚠ ACM at UMN — the CS student chapter, and the owner of MinneHack',
             'Runs MinneHack, the 300+ participant regional hackathon. Club room Keller Hall 2-204, weekly '
             'open house, drop-ins welcome. acm@umn.edu is the published address for BOTH club business AND '
             'hackathon sponsorship — one email reaches both. This is the highest-leverage single contact at '
             'the flagship.',
             'https://acm.umn.edu/'),
            ('Carlson School Funds Enterprise (student-managed investment funds)',
             'Carlson runs student-managed funds under its Enterprise Programs umbrella with a public events '
             'page. Real money, real students. No officer contacts published.',
             'https://carlsonschool.umn.edu/enterprise-programs/funds-enterprise/events'),
            ('GopherLink directory generally',
             '⚠ JAVASCRIPT-RENDERED AND LOGIN-GATED. Group listings did not render to research tooling and '
             'individual group pages require authentication. No org list could be enumerated. Not a finding of '
             'absence — a finding that the directory is closed to outsiders.',
             'https://gopherlink.umn.edu')],
  'faculty': [('⚠⚠ Orientation & Transition Experiences — Explore U booth sales (315 Coffman Memorial Union)',
               'THE PAID DOOR AT THE FLAGSHIP AND THE MOST IMPORTANT NUMBER IN MINNESOTA. Sells the $600 / '
               '$1,150 Explore U booths and administers the $6,000-minimum Orientation corporate sponsorship. '
               'A sponsorship contact named Lizette Rebolledo appears on the page but HER EMAIL IS OBFUSCATED '
               'BY THE SITE\'S EMAIL-PROTECTION SCRIPT and could not be read — use the office phone. CALL '
               'ABOUT THE SEP 5 EVENT IMMEDIATELY; the registration-timing statements on the two OTE pages '
               'contradict each other.',
               'Orientation & Transition Experiences',
               'email obfuscated on page · (612) 624-1979',
               'https://ote.umn.edu/about-ote/sponsors-partners'),
              ('⚠ SUA Event Services (Coffman Memorial Union Room 309 / St. Paul Student Center Room 42)',
               'Books EVERY reservation in Coffman and the St. Paul Student Center, including contact tables '
               'and the "University Guest" non-university tier. This is the office that quotes the 50% '
               'non-refundable deposit and demands the Facility Use Agreement and proof of insurance — ask '
               'them for the insurance dollar limit, which is published nowhere.',
               'Student Unions & Activities — Event Services',
               'email obfuscated on page · (612) 624-9954',
               'https://reservesua.umn.edu/'),
              ('Student Unions & Activities — main line (as printed on the outdoor-space policy)',
               'Owns the Student Group Policies quoted above, including the anti-fronting rule and the '
               'contact-table bar. The number to call to argue about whether a sponsored event is compliant.',
               'Student Unions & Activities',
               '(612) 626-6919 (main line)',
               'https://policy.umn.edu/operations/outdoor'),
              ('SUA Welcome Desk (4-INFO)',
               'General union questions; staff "can answer questions about the unions, student groups, event '
               'locations." ⚠ Note the SUA contact page renders EVERY email address as a JavaScript-protected '
               'placeholder — research tooling reads them all as "[email protected]." PHONE, DO NOT EMAIL, '
               'ANYWHERE AT UMN.',
               'Student Unions & Activities',
               'all emails obfuscated on page · (612) 624-4636 (main line)',
               'https://sua.umn.edu/contact'),
              ('⚠ Outdoor Events Office',
               'Issues outdoor permits and is the office that routes non-University guests to the Real Estate '
               'Office for the Facility Use Agreement and the unpublished flat fee. If DGD wants a spot on the '
               'mall rather than inside a building, this call comes first. Email obfuscated on page.',
               'University Services',
               'email obfuscated on page · (612) 626-9307',
               'https://outdoor.umn.edu/faq'),
              ('⚠ Real Estate Office',
               'Executes the Facility Use Agreement and sets the FLAT FEE that non-University entities pay for '
               'outdoor space. THE FEE AMOUNT IS NOT PUBLISHED ANYWHERE — this number is the only way to learn '
               'it. Number printed on the outdoor-space policy page.',
               'University Services',
               '(612) 625-5345',
               'https://policy.umn.edu/operations/outdoor'),
              ('Landcare / Facilities Management',
               'Grounds impacts on outdoor events; printed on the outdoor-space policy page.',
               'Facilities Management',
               '(612) 625-7361',
               'https://policy.umn.edu/operations/outdoor'),
              ('⚠ Carlson School — Accounting Department (321 Nineteenth Avenue South, Suite 3-122)',
               '⚠⚠ CALL THIS NUMBER BEFORE YOU EMAIL ANYONE ABOUT CRYPTO AT CARLSON. Vivian Fang was the '
               'Carlson School\'s Honeywell Professor in Accounting and is the U of M\'s public voice on '
               'cryptocurrency and NFTs (twin-cities.umn.edu/news-events/talking-cryptocurrency-blockchain-'
               'and-nfts-u-m). HER LINKEDIN NOW LISTS HER AS RICHARD E. JACOBS CHAIR IN FINANCE AT INDIANA '
               'UNIVERSITY KELLEY SCHOOL OF BUSINESS — SHE IS VERY LIKELY NO LONGER AT MINNESOTA. Verify '
               'before using her name; a stale affiliation here would burn the best-known crypto voice at the '
               'flagship. Department staff listed: Tina Starnes (Department Administrator), Katy Berg '
               '(Executive Administrative Specialist). No chair is named on the page. Emails are protected.',
               'Carlson School of Management — Accounting',
               'emails protected on page · (612) 624-6506',
               'https://carlsonschool.umn.edu/departments/accounting/contact'),
              ('⚠ Carlson School — Finance Department (same suite)',
               'Owns FINA 5125 and FINA 6125, "Cryptocurrency, Blockchain, and Their Business Applications," '
               'which run EVERY SPRING and therefore NOT in Fall 2026. The syllabus already imports "industry '
               'expert guest lectures" — ask who teaches the Spring 2027 section and whether that slot is '
               'open. That is a genuine, non-commercial door no tabling rule touches.',
               'Carlson School of Management — Finance',
               'emails protected on page · (612) 624-6506',
               'https://carlsonschool.umn.edu/departments/finance/contact'),
              ('Irene Kawalec-Menasco, Associate Administrator, Finance Department',
               'Finance department administration — the person who can say whether a guest lecture is possible '
               'and route it.',
               'Carlson School of Management — Finance',
               'email protected on page · (612) 625-1252',
               'https://carlsonschool.umn.edu/departments/finance/contact'),
              ('Kelley Vanda, Executive Administrative Specialist, Finance Department',
               'Finance department administration.',
               'Carlson School of Management — Finance',
               'email protected on page · (612) 626-7108',
               'https://carlsonschool.umn.edu/departments/finance/contact'),
              ('University Conference & Event Services (Housing & Residential Life)',
               'Serves external organisations for conferences and events, hosting about 14,000 guests a year, '
               'with on-campus overnight housing in summer. A separate channel from SUA — worth a call if DGD '
               'ever wants a multi-day presence rather than a table. Email obfuscated on page.',
               'Housing & Residential Life',
               'email obfuscated on page · (612) 625-9090',
               'https://uces.umn.edu/'),
              ('Chris Vokracka, ARAMARK Concessions',
               'The only named individual with a published direct number on the SUA fundraising page; '
               'concessions at events. Carried across for completeness.',
               'ARAMARK / SUA',
               'email obfuscated on page · (612) 625-1022',
               'https://sua.umn.edu/fundraising'),
              ('St. Paul Student Center Post Office',
               'St. Paul campus; the Activities Fair second day is held at SPSC on Sep 23.',
               'Student Unions & Activities',
               '(612) 625-9794',
               'https://sua.umn.edu/contact'),
              ('Student Group Resource Center (Coffman Memorial Union, 2nd floor)',
               'Student group supplies and pick-up, with additional items at the St. Paul Student Center. '
               'NO NUMBER PUBLISHED — LOOK UP HERE. Email is sgrc@umn.edu (rendered as a protected link). '
               '⚠ Closed over summer break from May 15, 2026 through August 30, 2026 — it will not answer '
               'before Aug 31. No staff names published, only "SGRC Team" and "Student Group Resource Center '
               'Supervisor."',
               'Student Unions & Activities',
               'sgrc@umn.edu · no number published — look up here; use SUA (612) 626-6919',
               'https://sua.umn.edu/student-group-resource-center')],
  'courses': [('FINA 5125',
               '"Cryptocurrency, Blockchain, and Their Business Applications" — 2 credits, A-F, lecture, not '
               'repeatable, does not fulfil writing-intensive requirements. Begins with cryptography and '
               'consensus mechanisms, then enterprise blockchain implementations, smart contracts, and token '
               'offerings including ICOs and STOs; covers cryptoasset valuation and "blockchain-related '
               'investment strategies"; incorporates "industry expert guest lectures." Aims to give students '
               '"a basic set of skills to understand cryptocurrencies and blockchain and how businesses can '
               'use them." ⚠ OFFERED "EVERY SPRING" — DOES NOT RUN IN FALL 2026. The guest-lecture slot is a '
               'Spring 2027 play; call Finance at (612) 624-6506.',
               'https://umtc.catalog.prod.coursedog.com/courses/8194821'),
              ('FINA 6125',
               'Same title and content at MBA level, 2 credits. ⚠ ALSO "EVERY SPRING" — NOT FALL 2026.',
               'https://umtc.catalog.prod.coursedog.com/courses/8204401'),
              ('(Undergraduate CS)',
               'NO undergraduate blockchain, cryptocurrency or fintech course was confirmed at UMN Twin '
               'Cities. The CSCI course list did not surface one. Look up here. Contrast St. Thomas, which has '
               'a dedicated 2-credit UNDERGRADUATE crypto course (FINC 315) — the flagship does not.',
               'https://cse.umn.edu/cs/courses')],
  'events': [('⚠⚠ MinneHack — organised by ACM UMN, and the best non-tabling spend in Minnesota',
              'MinneHack 2026 ran Feb 14–15, 2026, in Coffman Memorial Union, Presidents Room and Mississippi '
              'Room — a 24-hour regional software-development competition, teams of up to four, historically '
              '300+ participants from around 100 schools globally. 2026 sponsors: Improving (Silver), Shipt '
              '(Bronze), Huntington Bank, Fyra Labs, RunAnywhere.ai. SPONSORSHIP LINE, VERBATIM: "If you are '
              'interested in sponsoring MinneHack in future years, contact us at acm@umn.edu." ⚠ THERE IS NO '
              'FALL 2026 MINNEHACK — IT IS A FEBRUARY EVENT. The Fall 2026 action is to buy into MinneHack '
              '2027 NOW, while the committee is forming and before tiers are set. This is a private '
              'student-run event and sits entirely outside the University\'s commercial-use rules in a way a '
              'table never can. ⚠ Tier PRICES are not published — the 2026 site names Silver and Bronze '
              'without numbers. A smaller sibling event, "uHack: minnehack, but smaller," exists on Devpost '
              '(https://uhack-umn.devpost.com/) with no confirmed dates.',
              'https://www.minnehack.com/sponsors/'),
             ('⚠ Minnesota Blockchain Initiative — the master key to the whole state scene',
              'Nonprofit founded 2018, "cultivat[ing] a dynamic community and industry hub supporting the '
              'blockchain and Web3 community and industry" across community-building, education and policy, '
              'and events. Runs MONTHLY SPOTLIGHT MEETUPS in the Twin Cities, a podcast, a Slack channel and '
              'an annual "Crypto Spring" conference; the next listed meetup at time of research was Jul 27, '
              '2026 in New Hope, MN. Annual sponsors: Quantum Lex, Fredrikson, Spencer Fane, Southwest '
              'Corporation, Dropchain — it actively seeks more. ⚠ IT IS NAMED AS A COLLABORATOR OF BOTH THE '
              'UMN BLOCKCHAIN CLUB AND THE ST. THOMAS SCHOOL OF LAW CONFERENCE. Given that the UMN club\'s own '
              'sites are robots-blocked and GopherLink is login-gated, connect@mnblockchain.org is the most '
              'reliable route to Minnesota student blockchain organisers that exists.',
              'https://www.mnblockchain.org/'),
             ('Fall 2026 career fairs — ⚠ LOGIN-GATED, DATES NOT OBTAINABLE',
              'UMN routes all employer registration through HANDSHAKE, which is login-gated to research '
              'tooling, and the Career Services fair calendar disclaims that fairs "are not guaranteed to '
              'occur until they are listed on Handshake." FALL 2026 TWIN CITIES FAIR DATES COULD NOT BE '
              'CONFIRMED. One cross-listed date WAS retrievable, via UMD\'s employer page: GOVERNMENT AND '
              'NONPROFIT CAREER FAIR, FRI OCT 23, 2026, 11:00 a.m.–3:00 p.m., AT UMN TWIN CITIES.',
              'https://career.umn.edu/channels/career-fair-calendar/'),
             ('Explore U + Welcome Week (the audience, in one place, once a year)',
              'Explore U Sat Sep 5, 2026, 1:00–4:30 p.m., Huntington Bank Stadium — over 4,000 new and current '
              'student leaders, three days before classes begin, on move-in weekend. The Orientation '
              'sponsorship package reaches "15,000 participants through Orientation, Welcome Week, and '
              'first-year and second-year programming" for a $6,000 minimum.',
              'https://ote.umn.edu/about-ote/sponsors-partners/explore-u-event')],
  'play': 'Buy the Explore U booth and stop trying to table. UMN is the largest audience in Minnesota and it '
          'has exactly one written door for a for-profit outsider: Explore U on Sat Sep 5, 2026, at Huntington '
          'Bank Stadium, where the University itself advertises "a great opportunity for local businesses and '
          'organizations to access incoming first-year and incoming transfer students" at $600 (Maroon) or '
          '$1,150 (Gold). Everything else is shut: a flat ban on non-University entities promoting goods or '
          'services on University property, a named anti-fronting rule with disciplinary exposure for the '
          'students who help you, an explicit bar on student groups reserving contact tables for external '
          'organizations, and a sentence forbidding your own personnel from standing at one. ⚠ CALL (612) '
          '624-1979 TODAY: the sponsors page says booths go on sale "in late spring" while the Explore U page '
          'still says registration "will open in the coming weeks" — both cannot be true, and the event is 24 '
          'days out. If the booth is gone, the fallback is not a table, it is the $6,000 Orientation '
          'sponsorship (which explicitly includes tabling) or, better and cheaper, MinneHack 2027 sponsorship '
          'via acm@umn.edu — a private student-run hackathon that no University commercial rule reaches. '
          'Court the UMN Blockchain Club for a SPEAKER SLOT, never for table access it cannot legally give '
          'you; reach it through connect@mnblockchain.org, because its own two websites are robots-blocked and '
          'GopherLink is login-gated. FINA 5125/6125 already runs industry guest lectures but is spring-only, '
          'so bank that for 2027. And do not email Vivian Fang before calling (612) 624-6506 to check whether '
          'she is still here — her LinkedIn says Indiana.',
  'gaps': ['⚠⚠ EXPLORE U REGISTRATION STATUS — the two OTE pages contradict each other on whether booths are '
           'still available for Sep 5, 2026. ☎ (612) 624-1979 TODAY. '
           'https://ote.umn.edu/about-ote/sponsors-partners/explore-u-event',
           '⚠ Explore U registration DEADLINE and whether a crypto project is excluded under the drug-free / '
           'smoke-free clause. ☎ (612) 624-1979',
           '⚠ Is Vivian Fang still at Carlson? Her LinkedIn lists Indiana Kelley. ☎ Carlson Accounting '
           '(612) 624-6506. https://carlsonschool.umn.edu/departments/accounting/contact',
           '⚠ The FLAT FEE non-University entities pay for outdoor space is published nowhere. ☎ Real Estate '
           'Office (612) 625-5345 or Outdoor Events (612) 626-9307. https://outdoor.umn.edu/faq',
           '⚠ The proof-of-insurance DOLLAR LIMIT for non-University bookings is not published. ☎ SUA Event '
           'Services (612) 624-9954. https://reservesua.umn.edu/rates-payments',
           'MinneHack 2027 sponsorship tiers and prices — not published; 2026 named Silver and Bronze without '
           'numbers. Email acm@umn.edu. https://www.minnehack.com/sponsors/',
           'Fall 2026 add/drop deadlines — onestop.umn.edu/calendar/dropadd-deadlines is a JavaScript filter '
           'that returned no rows; a parameterised academic-calendar URL was ROBOTS-BLOCKED.',
           '⚠ Thanksgiving break Nov 26–27, 2026 is confirmed ONLY on the third-party aggregator '
           'acadcalendar.com, not on any umn.edu page. Confirm before scheduling the week of Nov 23.',
           'Fall 2026 Twin Cities career-fair dates — all behind Handshake (login-gated); Career Services '
           'disclaims fairs are not guaranteed until listed there. https://career.umn.edu/channels/career-fair-calendar/',
           'UMN Blockchain Club current officers, meeting schedule and events — GopherLink #4465 LOGIN-GATED; '
           'umnblockchain.org and umnbc.org both ROBOTS-BLOCKED. Route via connect@mnblockchain.org.',
           'Spring 2027 instructor for FINA 5125/6125 and whether the existing industry-guest-lecture slot is '
           'open. ☎ (612) 624-6506'],
  'note': '⚠ EMAIL IS A DEAD END AT UMN. sua.umn.edu, reservesua.umn.edu, uces.umn.edu and carlsonschool.umn.edu '
          'all render addresses through a JavaScript email-protection script; research tooling reads every one '
          'as "[email protected]." Phone, do not email. Separately: onestop.umn.edu and asr.umn.edu/'
          'dates-and-deadlines are JavaScript FILTER UIs that return no dates at all — the only calendar page '
          'that actually yields Fall 2026 dates is asr.umn.edu/2026-27-twin-cities-and-rochester-calendar.',
 },

 # ------------------------------------------------- 2. MINNESOTA STATE MANKATO
 {'state': 'Minnesota',
  'name': 'Minnesota State University, Mankato',
  'city': 'Mankato, MN',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 3,
  'start': 'Mon Aug 24, 2026 — in the earliest wave with St. Cloud State and Winona State, fifteen days ahead '
           'of the U of M Twin Cities.',
  'adddrop': 'UNVERIFIED — ⚠ NEITHER the official fall term calendar NOR the 26-27 PDF publishes an add or drop '
             'date. The registrar holds them; the calendar pages do not. Look up here: '
             'https://admin.mnsu.edu/academic-affairs/university-calendars/academic-calendars/',
  'fallbreak': '⚠ NONE listed on the official fall term calendar. No October break at Mankato.',
  'thanksgiving': 'Nov 26–29, 2026',
  'lastclass': '⚠ PARTIAL — the calendar prints "semester ends Dec 11" and "finals Dec 7–11" but NO separate '
               '"last day of classes" row. The practical read is that regular instruction ends on or about '
               'FRI DEC 4, 2026. Confirm before booking an early-December visit; the useful Mankato window '
               'almost certainly closes around Dec 4.',
  'finals': 'Dec 7–11, 2026. Commencement Sat Dec 12, 2026.',
  'cal_url': 'https://admin.mnsu.edu/academic-affairs/university-calendars/academic-calendars/fall-term-calendar/',
  'cal_status': 'PARTIAL — start, Thanksgiving, finals and commencement CONFIRMED on the official fall term '
                'calendar. ⚠ The university ALSO publishes a 26-27 PDF that it marks "UNOFFICIAL" on its face '
                'and which itself recommends checking the official calendars '
                '(https://admin.mnsu.edu/globalassets/academic-calendars/26-27-academic-calendar.pdf). Add/drop '
                'and a distinct last-class date are absent from both.',
  'fair': 'CLUB MAVERICK (the student-organization event inside Welcome Week). ⚠ NOT to be confused with '
          'CHOOSE-A-PALOOZA, which is a scavenger hunt, not a fair.',
  'fair_date': 'Welcome Week 2026 runs THU AUG 20 – SUN AUG 23, 2026 (classes begin Mon Aug 24). The weekday '
               'pattern checks out — Aug 20, 2026 IS a Thursday — so the page is CURRENT, not stale. CLUB '
               'MAVERICK falls on THU AUG 20, 2026. ⚠ TIME, LOCATION AND OUTSIDE-ORG ELIGIBILITY ARE NOT '
               'PUBLISHED ANYWHERE. The Welcome Week landing page lists Club Maverick under Thursday with no '
               'detail; the per-day detail pages that still exist are for 2024 '
               '(/welcome-week/thursday-august-22/ — STALE), and a /thursday-august-20/ page 404s. // '
               'CHOOSE-A-PALOOZA is FRI AUG 21, 2026, 1:00 p.m. start with prizes at 3:00 p.m., OTTO REC '
               'CENTER GYM — but read what it actually is before budgeting for it: "a campus-wide scavenger '
               'hunt" in which students visit "participating offices across campus" to collect tickets and '
               'then deposit them in prize baskets in the gym (first 350 students at the CSU Administrative '
               'Office get balsa plane kits). IT IS NOT AN ORG FAIR. // No fall involvement fair appears on the '
               'Student Activities events page at all.',
  'fair_outside': '⚠ NO PUBLISHED ANSWER for Club Maverick. Nothing on any retrievable page says whether a '
                  'non-university organization may participate. What IS published, and is favourable, is the '
                  'general scheduling-policies statement that "Recognized Student Organizations, University '
                  'Departments, AND THE GENERAL PUBLIC are responsible for knowing and adhering to federal, '
                  'state, university, and student union policies" — the General Public is expressly '
                  'contemplated as a user class at Mankato. But the Lobby Space Usage policy limits lobby and '
                  'hallway tables to "Recognized Student Organizations and University departments," which does '
                  'not include you. CONFIRM BY PHONE: Gregory Wilkins (507) 389-6076.',
  'fair_cost': 'NOT PUBLISHED for Club Maverick, Choose-A-Palooza or any Welcome Week event. No outside-vendor '
               'rate card exists anywhere on mnsu.edu. ⚠ The real cost driver at Mankato is not a table fee, it '
               'is INSURANCE: $2,000,000 per person / $2,000,000 per occurrence for non-university clients '
               '(see policy_key).',
  'fair_deadline': 'NOT PUBLISHED. The only documented gate is the solicitation approval itself — "All '
                   'solicitation activities must receive prior approval from University Scheduling and '
                   'Conference Services (CSU 219)" — with no stated lead time. Ask for the lead time on the '
                   'call: Bill Tourville (507) 389-2223.',
  'fair_url': 'https://mankato.mnsu.edu/university-life/centennial-student-union/welcome-week/',
  'policy': 'Centennial Student Union Policies & Procedures — Solicitations; Lobby Space Usage; Insurance; '
            'Recognized Student Organizations (a set of 50+ individual policies) + University Scheduling '
            'Policies & Fees + Minnesota State System Procedure 6.7.2 and Board Policy 3.1',
  'policy_url': 'https://mankato.mnsu.edu/university-life/centennial-student-union/about-us/policies-and-procedures-update/solicitations/',
  'policy_key': "⚠ MINNESOTA STATE SYSTEM NOTE — THIS PARAGRAPH GOVERNS FOUR OF THE TEN CAMPUSES IN THIS FILE "
                "(Mankato, St. Cloud State, Winona State, Metropolitan State) AND IS REPORTED ONCE, HERE. "
                "Minnesota State is a 33-institution / 54-campus system with its OWN Board of Trustees, "
                "entirely separate from the University of Minnesota system and its Board of Regents. Different "
                "boards, different policy books. DO NOT CONFLATE THEM. "
                "(a) MINNESOTA STATE SYSTEM PROCEDURE 6.7.2, 'Use of College and University Facilities "
                "(College or University as Lessor)' — EFFECTIVE JULY 28, 1996, LAST REVISED JANUARY 22, 2026 "
                "(https://www.minnstate.edu/board/procedure/607p2.html). THIS IS THE DOCUMENT THAT GOVERNS "
                "EVERY OUTSIDE-ENTITY SPACE USE AT ALL FOUR MINNESOTA STATE CAMPUSES. Operative provisions, "
                "verbatim: 'USERS OF FACILITIES MUST HAVE A FULLY EXECUTED, WRITTEN AGREEMENT BEFORE OCCUPYING "
                "OR USING A COLLEGE OR UNIVERSITY FACILITY.' 'USERS OF A COLLEGE OR UNIVERSITY FACILITY SHALL "
                "PROVIDE EVIDENCE OF ADEQUATE LIABILITY INSURANCE COVERAGE... NAMING THE STATE OF MINNESOTA... "
                "AS AN ADDITIONAL INSURED, PRIOR TO USING OR OCCUPYING.' Institutions must 'CHARGE A USER A "
                "REASONABLE AMOUNT WHEN LEASING THEIR FACILITIES THAT COVERS ALL COSTS TYPICALLY INCLUDED IN A "
                "STANDARD MARKET LEASE including... utilities, parking, security, property management' — i.e. "
                "market-rate cost recovery is MANDATORY, not discretionary; nobody at a Minnesota State campus "
                "can give you space for free. And every agreement must include 'A CANCELLATION CLAUSE, WHICH "
                "CAN BE INVOKED AT THE COLLEGE'S OR UNIVERSITY'S SOLE AND ABSOLUTE DISCRETION' — you can be "
                "cancelled at will, with no stated cause and no stated notice. Approval thresholds: Vice "
                "Chancellor approval at $100,000+ or 5+ years including renewal options; $150,000+ for "
                "leasehold improvements; consult the Minnesota State Real Estate Manager before any Facilities "
                "Agreement involving General Obligation Bond-financed property. "
                "(b) MINNESOTA STATE BOARD POLICY 3.1, 'Student Rights and Responsibilities' — implementation "
                "date January 18, 1995, last reviewed March 18, 2026 "
                "(https://www.minnstate.edu/board/policy/301.html). Verbatim: 'Individual students and student "
                "organizations shall be free to examine and to discuss all questions of interest to them and "
                "to express opinions publicly and privately.' 'Students shall be free to organize and join "
                "organizations to promote their common and lawful interests, subject to college or university "
                "policies.' 'Students shall have the right to assemble, to select speakers, and to discuss "
                "issues of their choice.' ⚠ NOTE THE SUBJECT OF EVERY SENTENCE IS *STUDENTS*. POLICY 3.1 "
                "CONFERS NOTHING WHATSOEVER ON AN OUTSIDE FOR-PROFIT ENTITY. It is a tool for student allies, "
                "not a right to table. "
                "(c) THERE IS NO SYSTEM-WIDE MINNESOTA STATE SOLICITATION POLICY. Solicitation is delegated "
                "entirely to each campus (https://www.minnstate.edu/board/policy/index.html), which is why the "
                "four Minnesota State campuses below range from access 5 (St. Cloud, published rate card) to "
                "access 3 (Mankato, Winona, Metro State). "
                "=== NOW THE MANKATO CAMPUS RULE === "
                "CENTENNIAL STUDENT UNION 'SOLICITATIONS' POLICY — THIS IS THE ENTIRE TEXT, VERBATIM, ALL OF "
                "IT: 'ALL SOLICITATION ACTIVITIES MUST RECEIVE PRIOR APPROVAL FROM UNIVERSITY SCHEDULING AND "
                "CONFERENCE SERVICES (CSU 219). SOLICITATION IS NOT ALLOWED IN ACADEMIC BUILDINGS.' "
                "(https://mankato.mnsu.edu/university-life/centennial-student-union/about-us/policies-and-procedures-update/solicitations/) "
                "READ WHAT THAT DOES *NOT* SAY. It is a PERMISSION REGIME, NOT A BAN. It does not distinguish "
                "student from outside solicitors. It does not name commercial activity. It does not require "
                "sponsorship. It does not set a fee. IT DOES NOT PROHIBIT A FOR-PROFIT OUTSIDER FROM ASKING. "
                "CSU 219 IS THE WHOLE GAME AT MANKATO — one office, one approval, no published grounds for "
                "refusal. That is why this is a 3 and not a 2. "
                "THE CONSTRAINT IS THE LOBBY POLICY, VERBATIM: 'RECOGNIZED STUDENT ORGANIZATIONS AND "
                "UNIVERSITY DEPARTMENTS MAY REQUEST THE USE OF LOBBY SPACE (LOUNGES AND HALLWAYS) FOR PUBLIC "
                "EVENTS' — outside organizations are NOT among the listed eligible requesters. Approved events "
                "must allow free traffic flow, remain open to the public, and operate without 'admission fees "
                "or donations solicited'; users must 'be courteous of others by monitoring their noise level "
                "and responding promptly when asked to reduce noise levels.' Reservations run through "
                "University Scheduling and Conference Services, CSU 219. NO RATE CARD FOR OFF-CAMPUS GROUPS IS "
                "PUBLISHED ANYWHERE. "
                "(https://mankato.mnsu.edu/university-life/centennial-student-union/about-us/policies-and-procedures-update/lobby-space-usage/) "
                "⚠⚠ INSURANCE — HARD DOLLAR LIMITS, AND THEY ARE HIGH. VERBATIM: 'INSURANCE MUST BE PROVIDED "
                "FOR ANY UNIVERSITY EVENT WHERE ALCOHOL WILL BE SERVED AND FOR EVENTS HOSTED BY NON-UNIVERSITY "
                "CLIENTS.' On campus: 'the sponsor must show evidence of public liability and dram shop "
                "coverage NAMING THE UNIVERSITY AS AN ADDITIONAL INSURED FOR MINIMUM LIMITS OF $2,000,000 PER "
                "PERSON/$2,000,000 PER OCCURRENCE.' Off campus: 'the insurance coverage shall be at minimum "
                "$2,000,000 PER INDIVIDUAL/$2,000,000 PER INCIDENT and shall be provided by the off-campus "
                "site.' Two phone numbers are printed on the policy page itself for making the arrangements: "
                "Assistant Director, University Scheduling and Conference Services, 507-389-6785, and the "
                "Office of Finance and Administration, 507-389-6623. ASK WHETHER THE $2M/$2M REQUIREMENT "
                "ATTACHES TO A SIMPLE TABLE OR ONLY TO ALCOHOL EVENTS AND ROOM RENTALS — the sentence is "
                "ambiguous and the answer changes the economics completely. "
                "(https://mankato.mnsu.edu/university-life/centennial-student-union/about-us/policies-and-procedures-update/insurance/) "
                "GENERAL CONDUCT RULE, VERBATIM AND USEFUL: 'RECOGNIZED STUDENT ORGANIZATIONS, UNIVERSITY "
                "DEPARTMENTS, AND THE GENERAL PUBLIC are responsible for knowing and adhering to federal, "
                "state, university, and student union policies' — the General Public is an acknowledged user "
                "class here (https://mankato.mnsu.edu/university-scheduling/policies--fees). "
                "⚠ ANTI-FRONTING: NOT FOUND. No fronting language appears in the CSU policy set, the "
                "scheduling policies page, or the RSO policy. The RSO policy is purely definitional — an RSO "
                "'must be comprised of five or more student members and at least two-thirds of the membership "
                "must be enrolled at Minnesota State University, Mankato,' with a stated purpose, written "
                "constitution and advisor, and 'Minnesota State Mankato will not recognize a student "
                "organization as such until the registration process on Mav Central has been completed, and "
                "the Minnesota State Student Association (MSSA) has voted to recognize it.' NOTHING BARS A "
                "MANKATO RSO FROM RESERVING SPACE FOR AN OUTSIDE ENTITY — a striking contrast with UMN Twin "
                "Cities and St. Cloud State, both of which prohibit it by name. "
                "NO LANGUAGE REACHING PAYMENT CREDENTIALS OR ON-SITE CONTRACT SIGNING WAS FOUND AT MANKATO. "
                "The state-level constraint, Minn. Stat. s 135A.145 (credit-card marketing — see the U of M "
                "Twin Cities policy_key), still binds the university and its student organizations.",
  'sponsor_required': 'NO — approval, not sponsorship. The one operative sentence is "All solicitation '
                      'activities must receive prior approval from University Scheduling and Conference '
                      'Services (CSU 219)," and it neither requires a student-organization sponsor nor '
                      'forbids one. ⚠ AND UNLIKE UMN TWIN CITIES AND ST. CLOUD STATE, MANKATO HAS NO '
                      'ANTI-FRONTING RULE — an RSO reserving lobby space with DGD alongside is not prohibited '
                      'by anything published. That combination (approval regime + no fronting ban + a Business '
                      'Organization ecosystem via COSBO) makes the club route genuinely viable here in a way '
                      'it is not at the flagship. Two calls: Bill Tourville (507) 389-2223 for the approval, '
                      'Gregory Wilkins (507) 389-6076 for the club.',
  'clubs': [('⚠ NO BLOCKCHAIN / CRYPTO / WEB3 / BITCOIN RSO AT MANKATO',
             'Verified absent from the College of Business organizations page and the CSET student '
             'organizations page. No Financial Management Association chapter either (Winona State has the only '
             'FMA in this set). The full directory is Mav Central; the RSO landing page is '
             'https://mankato.mnsu.edu/university-life/activities-and-organizations/student-organizations-leadership/rso/',
             'https://cset.mnsu.edu/youbelong/student-organizations/'),
            ('⚠ COSBO — Council of Student Business Organizations',
             'THE HIGHEST-LEVERAGE CLUB CONTACT AT MANKATO AND NOBODY EVER FINDS IT. COSBO is comprised of '
             'representatives from EVERY College of Business student club. One meeting reaches Beta Alpha Psi, '
             'the Finance Club, the Maverick Entrepreneurship Club, Delta Sigma Pi, IBO, AMA, the Professional '
             'Sales Organization, SHRM and Women In Business simultaneously. ⚠ No advisor names, emails or '
             'phone numbers are published for ANY organization on the COB page.',
             'https://cob.mnsu.edu/real-world-experience/student-organizations/'),
            ('Beta Alpha Psi, Accounting and Finance Club',
             'Highest single-club fit at Mankato. Described as "an honor organization for financial '
             'information students and professionals." No contact published.',
             'https://cob.mnsu.edu/real-world-experience/student-organizations/'),
            ('Finance Club',
             'Has its own page under the College of Business. No officer or advisor contact published.',
             'https://cob.mnsu.edu/real-world-experience/student-organizations/finance-club/'),
            ('Maverick Entrepreneurship Club',
             '"An international non-profit organization dedicated to inspiring students to improve the world '
             'through entrepreneurial action." Second-best fit after Beta Alpha Psi. No contact published.',
             'https://cob.mnsu.edu/real-world-experience/student-organizations/'),
            ('Other College of Business organizations (listed, lower fit)',
             'AgToday; AMA Mankato (company tours and industry speaker events); Delta Sigma Pi (professional '
             'business fraternity); International Business Organization (IBO); Professional Sales '
             'Organization; Society for Human Resources Management (SHRM); Women In Business. No contacts '
             'published for any of them.',
             'https://cob.mnsu.edu/real-world-experience/student-organizations/')],
  'faculty': [('⚠ Bill Tourville — Assistant Director of Scheduling & Conference Services',
               'THE SINGLE MOST IMPORTANT PERSON AT MANKATO. He runs CSU 219, the office whose "prior '
               'approval" is the entire solicitation policy. Nothing happens at Mankato without this call. Ask '
               'him three things: (1) will you approve an outside for-profit information table, (2) what does '
               'it cost, and (3) does the $2,000,000/$2,000,000 insurance requirement attach to a table or '
               'only to alcohol events and room rentals.',
               'University Scheduling & Conference Services (CSU 219)',
               'william.tourville@mnsu.edu · (507) 389-2223',
               'https://mankato.mnsu.edu/university-life/centennial-student-union/staff/csu-staff/'),
              ('⚠ Kathryn Roche — Scheduling Coordinator',
               'Her direct line is the number printed on the CSU INSURANCE POLICY PAGE itself as the '
               '"Assistant Director, University Scheduling and Conference Services" contact for insurance '
               'arrangements. If Tourville does not pick up, she is the second call and she owns the insurance '
               'question.',
               'University Scheduling & Conference Services (CSU 219)',
               'kathryn.roche@mnsu.edu · (507) 389-6785',
               'https://mankato.mnsu.edu/university-life/centennial-student-union/about-us/policies-and-procedures-update/insurance/'),
              ('Lindsey Nelson — Scheduling Coordinator',
               'Third scheduling contact; books CSU space.',
               'University Scheduling & Conference Services',
               'lindsey.nelson@mnsu.edu · (507) 389-5868',
               'https://mankato.mnsu.edu/university-life/centennial-student-union/staff/csu-staff/'),
              ('Allie Jutton — Scheduling Graduate Assistant',
               'Shares Tourville\'s line; useful for a first pass at availability.',
               'University Scheduling & Conference Services',
               'allie.jutton@mnsu.edu · (507) 389-2223',
               'https://mankato.mnsu.edu/university-life/centennial-student-union/staff/csu-staff/'),
              ('⚠ Mark Constantine — Director of Centennial Student Union & Student Activities',
               'Runs the whole building and the whole student-activities operation. The escalation point if '
               'CSU 219 says no. Patrice Hundstad (patrice.hundstad@mnsu.edu) is his Executive Assistant on '
               'the same number.',
               'Centennial Student Union',
               'mark.constantine@mnsu.edu · (507) 389-2224',
               'https://mankato.mnsu.edu/university-life/centennial-student-union/staff/csu-staff/'),
              ('⚠ Gregory Wilkins — Associate Director, Student Activities',
               'Owns Club Maverick and the RSO relationship. THE call for the two things not published '
               'anywhere: what time and where Club Maverick is on Thu Aug 20, 2026, and whether an outside '
               'organization can be in the room.',
               'Student Activities (CSU 173)',
               'gregory.wilkins@mnsu.edu · (507) 389-6076',
               'https://mankato.mnsu.edu/university-life/centennial-student-union/staff/student-activities/'),
              ('⚠ Oluwaseun Adekeye — Assistant Director for RSOs, Leadership and Nontraditional Students',
               'RSO recognition and support — the person who would rule on an RSO co-hosting DGD. ⚠ DATA '
               'CONFLICT: the CSU staff page lists this seat as VACANT while the Student Activities staff page '
               'lists Adekeye in it. Both pages are live. Adekeye is the more recent listing; assume filled and '
               'confirm on the call.',
               'Student Activities (CSU 173)',
               'oluwaseun.adekeye@mnsu.edu · (507) 389-6076',
               'https://mankato.mnsu.edu/university-life/centennial-student-union/staff/student-activities/'),
              ('Lucy Bivins-Zheng — Assistant Director for Campus Programs',
               'Campus programming, including Welcome Week content.',
               'Student Activities (CSU 173)',
               'lucy.bivins-zheng@mnsu.edu · (507) 389-6076',
               'https://mankato.mnsu.edu/university-life/centennial-student-union/staff/csu-staff/'),
              ('Pam Guss — Business Manager, Student Activities',
               'Handles money on the student-activities side.',
               'Student Activities (CSU 173)',
               'pamela.guss@mnsu.edu · (507) 389-6076',
               'https://mankato.mnsu.edu/university-life/centennial-student-union/staff/csu-staff/'),
              ('Paul Lucas — CSU Business Manager',
               'Invoicing and billing for CSU space. Ask him what an outside table actually costs, since no '
               'rate card is published.',
               'Centennial Student Union',
               'paul.lucas@mnsu.edu · (507) 389-5225',
               'https://mankato.mnsu.edu/university-life/centennial-student-union/staff/csu-staff/'),
              ('⚠ Office of Finance and Administration',
               'PRINTED ON THE INSURANCE POLICY PAGE as a contact for insurance arrangements. This is where the '
               '$2,000,000/$2,000,000 certificate is actually vetted.',
               'Finance and Administration',
               '(507) 389-6623',
               'https://mankato.mnsu.edu/university-life/centennial-student-union/about-us/policies-and-procedures-update/insurance/'),
              ('James Ball — Associate Director, Operations',
               'Building operations. Brock Allore, Building Operations Coordinator (brock.allore@mnsu.edu, '
               '507-389-5997) and Nick Boone, Technical Services Coordinator (nicholas.boone.2@mnsu.edu, '
               '507-389-2060) report into this function.',
               'Centennial Student Union',
               'james.ball@mnsu.edu · (507) 389-5890',
               'https://mankato.mnsu.edu/university-life/centennial-student-union/staff/csu-staff/'),
              ('Lenny Koupal — Communications Coordinator',
               'CSU publicity; the route to getting an event listed. Grace Maloney, Maverick Bullpen Interim '
               'Program Coordinator (grace.maloney.2@mnsu.edu, 507-389-1221) runs the Bullpen space.',
               'Centennial Student Union',
               'leonard.koupal@mnsu.edu · (507) 389-6744',
               'https://mankato.mnsu.edu/university-life/centennial-student-union/staff/csu-staff/'),
              ('⚠ Dr. Puneet Jaiprakash — Associate Professor of Finance and FINANCE DEPARTMENT CHAIR',
               'The best academic call at Mankato: he decides whether a guest lecture happens and whether any '
               'special-topics FINA number could carry crypto content. ⚠ NOTE HONESTLY: no Mankato finance '
               'faculty page identifies fintech, blockchain or digital-asset research — DO NOT claim he has a '
               'crypto interest.',
               'College of Business — Finance',
               'puneet.jaiprakash@mnsu.edu · (507) 389-1826',
               'https://cob.mnsu.edu/about/faculty-and-staff/fin/'),
              ('Daniel Hiebert — Associate Professor of Financial Planning, Director of the Financial Planning '
               'Program',
               'Runs a named programme rather than just teaching a course, which makes him the second-best '
               'academic door — financial-planning students are a natural audience for a digital-asset talk.',
               'College of Business — Finance',
               'daniel.hiebert@mnsu.edu · (507) 389-5406',
               'https://cob.mnsu.edu/about/faculty-and-staff/fin/'),
              ('Finance faculty — remaining, all with direct lines',
               'Yilin (Leon) Chen, Professor — yilin.chen@mnsu.edu, (507) 389-5336. Yuhao Chen, Assistant '
               'Professor — yuhao.chen@mnsu.edu, (507) 389-6531. Ishuan Li Simonson, Professor — '
               'ishuan.li@mnsu.edu, (507) 389-5753. Nguyen Nguyen, Assistant Professor — '
               'nguyen.nguyen.2@mnsu.edu, (507) 389-5090. Joe Reising, Professor — joseph.reising@mnsu.edu, '
               '(507) 389-5344. None identifies crypto or fintech research.',
               'College of Business — Finance',
               'see notes · (507) 389-5336 / 6531 / 5753 / 5090 / 5344',
               'https://cob.mnsu.edu/about/faculty-and-staff/fin/'),
              ('Minnesota State University, Mankato — university main line',
               'Last resort. Two published main numbers.',
               'University',
               '(507) 389-1000 (main line) / (800) 722-0544 (main line)',
               'https://mankato.mnsu.edu/about-the-university/')],
  'courses': [('(No crypto/fintech course found)',
               'NO blockchain, cryptocurrency or fintech course was confirmed at Mankato. Catalog searches '
               'returned nothing. The active course list is at '
               'https://www.mnsu.edu/academic-catalog/active-course-list/ and the Finance program at '
               'https://www.mnsu.edu/programs/finance/. Ask Dr. Jaiprakash, (507) 389-1826, whether any '
               'special-topics FINA number carries crypto content in Fall 2026 — special-topics slots rotate '
               'and are not in the static catalog.',
               'https://www.mnsu.edu/programs/finance/')],
  'events': [('Welcome Week 2026',
              'THU AUG 20 – SUN AUG 23, 2026, immediately before classes begin Mon Aug 24. Published events: '
              'New Student & Family Dinner, New Student Rally and Arch March, CLUB MAVERICK (Thu Aug 20), '
              'Cosmic Bingo, Hypnotist, Backyard Bash, CHOOSE-A-PALOOZA (Fri Aug 21, 1:00 p.m., Otto Rec '
              'Center Gym), Prize Flight, Find Your Class Tours, Galactic Bingo (Sat Aug 22, "Minnesota\'s '
              'Biggest Bingo Showdown"), outdoor movie (Sun Aug 23). Weekdays check out against 2026 — the '
              'page is current.',
              'https://mankato.mnsu.edu/university-life/centennial-student-union/welcome-week/'),
             ('Homecoming week 2026',
              'CONFIRMED dates on the Student Activities events page: Homecoming Kick-Off Mon Sep 28, 2026, '
              '11:00 a.m., Centennial Student Union; Mavathon Blood Drive Wed Sep 30, 9:00 a.m., CSU Ballroom; '
              'Lip Sync and Coronation Thu Oct 1, 7:30 p.m., Bresnan Arena; Homecoming Carnival, football and '
              'volleyball Fri–Sat Oct 2–3. The Kick-Off is in the CSU, which is exactly where a CSU-219-'
              'approved table would sit.',
              'https://mankato.mnsu.edu/university-life/activities-and-organizations/student-activities-events/'),
             ('Family Weekend 2026',
              'Sat Oct 24, 2026 — Family Weekend Pancake Breakfast at 8:00 a.m. Parents on campus alongside '
              'students; a different and often more receptive audience for a financial product.',
              'https://mankato.mnsu.edu/university-life/activities-and-organizations/student-activities-events/'),
             ('(No hackathon or blockchain event)',
              'NO hackathon, blockchain conference, research centre or crypto-related legislative activity was '
              'found connected to Mankato.',
              'https://mankato.mnsu.edu/university-life/activities-and-organizations/')],
  'play': 'Mankato is the most winnable gated campus in Minnesota, and the reason is one sentence: the ENTIRE '
          'solicitation policy is "All solicitation activities must receive prior approval from University '
          'Scheduling and Conference Services (CSU 219). Solicitation is not allowed in academic buildings." '
          'That is a permission regime with no published grounds for refusal, no commercial ban, no sponsorship '
          'requirement — and, unusually, NO ANTI-FRONTING RULE, so unlike UMN Twin Cities and St. Cloud State '
          'nothing stops an RSO from reserving lobby space with DGD alongside. Call Bill Tourville at (507) '
          '389-2223 and ask him plainly whether he will approve an outside information table, what it costs '
          '(no rate card exists), and — the question that decides the economics — whether the $2,000,000 per '
          'person / $2,000,000 per occurrence insurance requirement attaches to a table or only to alcohol '
          'events and room rentals. If the insurance bites, Mankato becomes expensive fast; if it does not, '
          'this is a cheap approval. In parallel call Gregory Wilkins at (507) 389-6076 for the two Club '
          'Maverick facts nobody publishes (time, location, Thu Aug 20) and ask to be pointed at COSBO — the '
          'Council of Student Business Organizations, which has a representative from every business club and '
          'is the single highest-leverage student contact on this campus. ⚠ Do not budget for Choose-A-Palooza: '
          'it is a scavenger hunt of campus offices, not an org fair. And note the window closes early — '
          'instruction likely ends around Dec 4.',
  'gaps': ['⚠ CLUB MAVERICK (Thu Aug 20, 2026) — time, location and whether a non-university organization may '
           'participate are published NOWHERE. ☎ Gregory Wilkins (507) 389-6076. '
           'https://mankato.mnsu.edu/university-life/centennial-student-union/welcome-week/',
           '⚠ Will CSU 219 approve an outside for-profit information table, and what does it cost? No rate card '
           'for off-campus groups exists anywhere on mnsu.edu. ☎ Bill Tourville (507) 389-2223.',
           '⚠ Does the $2,000,000/$2,000,000 insurance requirement attach to a simple table, or only to alcohol '
           'events and room rentals? The policy sentence is ambiguous and the answer changes everything. '
           '☎ (507) 389-6785 or Finance and Administration (507) 389-6623.',
           'Add/drop deadline — absent from BOTH the official fall term calendar and the 26-27 PDF. Registrar '
           'has it. https://admin.mnsu.edu/academic-affairs/university-calendars/academic-calendars/',
           '⚠ Exact last day of regular classes — the calendar prints "semester ends Dec 11" and "finals Dec '
           '7–11" but no separate last-class row; instruction likely ends ~Fri Dec 4.',
           'Whether any special-topics FINA number carries crypto content in Fall 2026 — special-topics slots '
           'do not appear in the static catalog. ☎ Dr. Puneet Jaiprakash (507) 389-1826.',
           'Advisor and officer contacts for Beta Alpha Psi, the Finance Club and the Maverick Entrepreneurship '
           'Club — NONE are published on the COB organizations page. ☎ (507) 389-6076 or ask for COSBO.',
           'Whether the "Assistant Director for RSOs" seat is vacant (CSU staff page) or filled by Oluwaseun '
           'Adekeye (Student Activities staff page) — the two live pages disagree.'],
  'note': 'The CSU staff directory at Mankato publishes a DIRECT NUMBER for nearly every named person — 16 of '
          'them are carried above. This is the best-instrumented student-union staff page of any campus in this '
          'file and it makes Mankato the easiest campus in Minnesota to actually reach a human at. Use it.',
 },

 # ------------------------------------------------- 3. ST. CLOUD STATE
 {'state': 'Minnesota',
  'name': 'St. Cloud State University',
  'city': 'St. Cloud, MN',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 5,
  'start': 'Mon Aug 24, 2026 (day and evening classes begin) — earliest wave, with Mankato and Winona State.',
  'adddrop': 'UNVERIFIED — the registrar states "add/drop deadlines may vary depending upon the course" and '
             'pushes students to e-Services rather than publishing a single date. '
             'https://www.stcloudstate.edu/registrar/registration/default.aspx',
  'fallbreak': '⚠ NONE listed. No designated fall break period appears on the FY27 calendar.',
  'thanksgiving': 'Nov 25–27, 2026 — no classes; offices closed Nov 26–27.',
  'lastclass': '⚠⚠ FRI DEC 4, 2026 — THE EARLIEST CLASS END IN THE STATE, twelve days before UMN Twin Cities '
               'and a full week before Duluth. If the December leg of the tour runs west to east, ST. CLOUD '
               'MUST COME FIRST OR NOT AT ALL.',
  'finals': 'Mon–Thu Dec 7–10, 2026 — ⚠ exams end AT NOON on Dec 10. Commencement Dec 10 (graduate) and '
            'Dec 11 (undergraduate).',
  'cal_url': 'https://www.stcloudstate.edu/events/academic/academic-fy27.aspx',
  'cal_status': 'CONFIRMED — official FY27 list-view calendar. A calendar-view version exists at '
                'https://www.stcloudstate.edu/events/academic/academic-fy27-responsive-calendar.aspx and the '
                'hub at https://www.stcloudstate.edu/events/academic/default.aspx. Only add/drop is missing.',
  'fair': 'MAINSTREET INVOLVEMENT FAIR — and the page explicitly counts "community partners" among the '
          'participants',
  'fair_date': 'WED SEP 2, 2026, on the campus walkway near Atwood Memorial Center. ⚠ WEEKDAY CHECK PASSES — '
               'Sep 2, 2026 IS a Wednesday, so the date is a current listing, not a stale one. Time is NOT '
               'published. Registration via the "Mainstreet 2026 Sign-Up" form on HuskiesConnect. ⚠ '
               'PARTIAL-STALENESS WARNING: the page carries 2025 photography and 2025 copy alongside the 2026 '
               'date — treat the date as good and everything else as needing confirmation.',
  'fair_outside': '⚠ LIKELY YES, AND THE WORDING IS THE HOOK. The page describes Mainstreet as drawing "MORE '
                  'THAN 150 DEPARTMENTS, SERVICES, STUDENT ORGANIZATIONS, AND COMMUNITY PARTNERS." "Community '
                  'partners" is not "student organizations only," and it is consistent with SCSU\'s published '
                  'off-campus promotional rate card. But the fair page itself does not state eligibility or '
                  'cost. ASK ONE QUESTION ON THE CALL: is Mainstreet participation the same thing as an $85 '
                  'promotional-space booking, or a separate track? Carly Frederick or Lisa Johnson, '
                  '(320) 308-2074.',
  'fair_cost': 'NOT PUBLISHED for Mainstreet itself. ⚠ BUT THE STANDING RATE CARD IS PUBLISHED AND IS THE '
               'REAL ANSWER AT SCSU: Atwood kiosk $45 PER DAY; table in the Main Lounge $85 PER DAY; outside '
               'mall space $85 PER DAY, all available to off-campus vendors. SCSU organizations and '
               'departments pay nothing. Room rates for reference: Ballroom $600 minimum / $150 per hour; '
               'mid-size rooms (Glacier, Gallery, Theater) $150 minimum / $37.50 per hour; small rooms (Maple, '
               'Monarch) $50 minimum / $12.50 per hour; technical support $22/hour; after-hours room use '
               '$80/hour.',
  'fair_deadline': 'NOT PUBLISHED for Mainstreet — a sign-up form exists on HuskiesConnect with no stated '
                   'closing date. For the standing promotional space, there is no deadline: you book a kiosk, '
                   'table or mall space directly through the request forms or the Minnesota State EMS system. '
                   '⚠ The one money term to know: "The rental fee is NON-REFUNDABLE if the business or '
                   'organization does not arrive or use the space."',
  'fair_url': 'https://www.stcloudstate.edu/campusinvolvement/annual-events/mainstreet.aspx',
  'policy': 'Atwood Memorial Center — Promotional Areas and Advertising policy; Promotional Space reservation '
            'page and rates; Co-Sponsorship Policy (the anti-fronting rule); Event Space Usage policy. '
            'Governed above by Minnesota State System Procedure 6.7.2 (see the Mankato policy_key).',
  'policy_url': 'https://www.stcloudstate.edu/atwood/about/policies/advertising-promotion.aspx',
  'policy_key': "⚠⚠ ST. CLOUD STATE IS THE MOST OPEN CAMPUS IN MINNESOTA AND THE ONLY ONE IN THIS FILE WITH A "
                "PUBLIC, ITEMISED DAY-RATE FOR AN OUTSIDE BUSINESS TO STAND IN THE STUDENT UNION WITH A TABLE. "
                "THE RATE CARD (https://www.stcloudstate.edu/atwood/reservations/promotional-space.aspx, "
                "mirrored at https://www.stcloudstate.edu/atwood/reservations/rental-rates.aspx): ATWOOD KIOSK "
                "$45 PER DAY · TABLE IN THE MAIN LOUNGE $85 PER DAY · OUTSIDE MALL SPACE $85 PER DAY. SCSU "
                "organizations and departments reserve at no charge. "
                "THE ELIGIBILITY SENTENCE, VERBATIM (Promotional Areas and Advertising policy): 'SECONDARILY, "
                "AS POLICY, TIME, PLACE, AND MANNER PERMIT, OPPORTUNITIES MAY ALSO BE AVAILABLE FOR "
                "NON-UNIVERSITY ORGANIZATIONS AND BUSINESSES.' Off-campus groups submit through the "
                "promotional-space page rather than the EMS system used by student organizations. "
                "⚠⚠ THE DECISIVE PROHIBITION — IT REACHES PAYMENT CREDENTIALS BY NAME. VERBATIM: 'THE SALE OR "
                "DISTRIBUTION OF PRODUCTS/MESSAGES THAT PROMOTE VIOLATIONS OF UNIVERSITY POLICIES, CITY, STATE "
                "OR FEDERAL LAWS, AND/OR UNIVERSITY CONTRACTS IS PROHIBITED. SPECIFIC ITEMS THAT ARE "
                "PROHIBITED IN THE PROMOTIONAL SPACES INCLUDE: ACCESSORIES OR ITEMS THAT PROMOTE ALCOHOL, "
                "MARIJUANA, OR TOBACCO USE; CREDIT CARD OR DEBIT CARD SIGN-UPS; AND FOOD ITEMS IN CONFLICT "
                "WITH THE CONTRACTUAL AGREEMENT WITH THE CAMPUS DINING VENDOR.' READ THAT CLAUSE ALOUD IF "
                "CHALLENGED AND THEN GIVE THE ANSWER: DGD IS NOT RUNNING A CREDIT OR DEBIT CARD SIGN-UP AND IS "
                "NOT A CARD ISSUER UNDER 15 U.S.C. s 1602. This clause almost certainly derives from Minn. "
                "Stat. s 135A.145 (see the U of M Twin Cities policy_key) — which means it will not be waived "
                "and arguing about it is pointless. Design the table so no reasonable observer could call it a "
                "card sign-up: no card numbers, no payment capture, email only. "
                "ALSO PROHIBITED, VERBATIM: 'PER MINNESOTA STATE POLICY, ATWOOD DOES NOT PERMIT USERS TO HOLD "
                "A RAFFLE ON UNIVERSITY PROPERTY.' No prize draws. "
                "⚠⚠ ANTI-FRONTING — EXPLICIT, NAMED, AND ENFORCED WITH A TWO-STRIKE LADDER. Co-Sponsorship "
                "Policy, VERBATIM: 'STUDENT ORGANIZATIONS AND UNIVERSITY DEPARTMENTS SHALL NOT USE THEIR "
                "ACCESS TO CAMPUS, SPACE, AND SERVICES TO \"FRONT\" FOR A NON-UNIVERSITY GROUP OR COMMERCIAL "
                "VENDOR TO AVOID OR REDUCE EXPENSES OR TO PROVIDE ACCESS TO CAMPUS FOR THOSE ENTITIES.' A "
                "co-sponsoring student organization must 'BE THE PRIMARY RESERVATION CONTACT BEFORE, DURING, "
                "AND AFTER THE EVENT,' 'make the reservations and serve as the main contact for event "
                "planning,' have an authorised representative present at the event, be 'FINANCIALLY "
                "RESPONSIBLE FOR ALL BILLS AND INVOICES,' ensure the reservation aligns with its mission, and "
                "display all organization names clearly in promotional materials. ENFORCEMENT: warning on the "
                "first infraction; on the second, LOSS OF ATWOOD BOOKING PRIVILEGES FOR THE REMAINDER OF THE "
                "ACADEMIC YEAR PLUS PUBLIC-RATE CHARGES. "
                "(https://www.stcloudstate.edu/atwood/about/policies/cosponsorship.aspx) "
                "DOES SPONSORSHIP CURE IT? NO — AND IT IS COMPLETELY UNNECESSARY. The fronting rule closes the "
                "free club route while the published rate card opens a paid one for $85. PAY THE $85 AND SKIP "
                "THE CLUB ENTIRELY. That is the compliant, cheap, fast answer and it is the best "
                "outside-entity posture available anywhere in Minnesota. Courting a club here would expose the "
                "students to a booking ban for the rest of the year in exchange for saving $85. Do not do it. "
                "CONDUCT AND MONEY TERMS, VERBATIM: 'THE RENTAL FEE IS NON-REFUNDABLE IF THE BUSINESS OR "
                "ORGANIZATION DOES NOT ARRIVE OR USE THE SPACE.' Users must 'STAY BEHIND OR AT THE "
                "TABLE/KIOSK WHEN DISTRIBUTING MATERIAL OR RECRUITING.' 'Volume must not disturb others in "
                "adjacent areas.' Vendors violating campus policies 'may be denied future bookings.' FOOD: 'NO "
                "FOOD OR BEVERAGES WILL BE SOLD OR SERVED IN ATWOOD MEMORIAL CENTER OR ON THE ADJACENT MALLS "
                "UNLESS PURCHASED THROUGH OR PREPARED BY HUSKIES DINING.' "
                "EVENT SPACE USAGE POLICY "
                "(https://www.stcloudstate.edu/atwood/about/policies/event-space-usage.aspx), VERBATIM: "
                "'GROUPS OUTSIDE THE UNIVERSITY COMMUNITY WILL BE CHARGED RENTAL FOR SPACE USED IN THE "
                "BUILDING EVEN THOUGH SOME MEMBERS OF A GROUP MAY BE SCSU FACULTY OR STAFF' — the "
                "friend-on-the-inside workaround is pre-closed. 'As a general rule, space and facility "
                "scheduling will be done on a first-come, first-served basis.' CANCELLATION: 'Cancellations "
                "must be made at least SEVEN calendar days prior to the scheduled event, or the two-hour "
                "minimum tech fee will be charged'; room reservations cancelled fewer than two days in advance "
                "draw a warning first, then $25 per occurrence. The Conference and Scheduling Office arranges "
                "'contracts and billings' for off-campus groups. "
                "⚠ INSURANCE: NO INSURANCE REQUIREMENT AND NO DOLLAR LIMIT IS PUBLISHED ON ANY ATWOOD PAGE. "
                "Minnesota State System Procedure 6.7.2 supplies the underlying requirement — liability "
                "insurance naming the State of Minnesota as an additional insured, and a fully executed "
                "written agreement before occupancy — but no number. ASK ON THE BOOKING CALL. "
                "OFF-CAMPUS FLYERING: off-campus organizations may use designated tack-strip space in the "
                "NORTHEAST CORNER OF ATWOOD BY THE ELEVATOR for flyers no larger than 8.5\" x 11\", ONE FLYER "
                "PER EVENT. "
                "BOOKING ROUTES: kiosk, table and mall request forms at "
                "https://www.stcloudstate.edu/atwood/reservations/request-promotional.aspx (append "
                "?mail=kiosk, ?mail=table or ?mail=mall), or the Minnesota State EMS system at "
                "https://minnstate.bookitadmin.minnstate.edu/. "
                "NOTHING AT SCSU REACHES ON-SITE CONTRACT SIGNING.",
  'sponsor_required': '⚠ NO — AND DO NOT SEEK ONE. Sponsorship is not merely unnecessary at SCSU, it is '
                      'actively dangerous to the students who offer it: the Co-Sponsorship Policy names '
                      '"fronting" and punishes a second offence with loss of Atwood booking privileges for the '
                      'rest of the academic year plus public-rate charges. The published route is $85 for a '
                      'table in the Main Lounge (or $45 for a kiosk), booked directly with Lisa Johnson at '
                      '(320) 308-2074. Pay it.',
  'clubs': [('⚠ HuskiesConnect is LOGIN-GATED — the directory could not be read',
             '"Log into HuskiesConnect with StarID and password" is required to browse the organization '
             'directory, and a StarID is issued only to SCSU affiliates. The claimed count is "over 200 '
             'student clubs and organizations." NO BLOCKCHAIN, CRYPTO OR WEB3 ORGANIZATION WAS FOUND — but '
             'because the directory is gated, that is "not found," NOT "confirmed absent." Do not tell anyone '
             'SCSU has no crypto club; say you could not see the list.',
             'https://huskiesconnect.stcloudstate.edu/organizations'),
            ('Upsilon Pi Epsilon (UPE) — computing honour society',
             'Best-fit technical organization that IS publicly listed. "An international computer honors '
             'society which recognizes undergraduate and graduate students for their academic excellence in '
             'computing and information disciplines," endorsed by ACM and the IEEE Computer Society, with '
             'scholarships available to members. An honours society is a speaking audience, not a tabling '
             'partner — and at SCSU you do not need a tabling partner.',
             'https://www.stcloudstate.edu/cids/student/student-orgs.aspx'),
            ('Computing, Informatics and Data Science student organizations',
             'Publicly listed: Computer Science Club, Cloud Computing Club, GameDev Club, Cyber Competition '
             'Club, Cybersecurity–Information Assurance Club, Artificial Intelligence Research Society, '
             'Student Organization for Software Engineering (SOSE, '
             'https://huskiesconnect.stcloudstate.edu/organization/sose), National Society of Black Engineers, '
             'Society of Women Engineers. The two cybersecurity clubs are the closest cultural fit to a '
             'cryptography-literate audience. No contacts published for any of them.',
             'https://www.stcloudstate.edu/cids/student/student-orgs.aspx'),
            ('College of Liberal Arts student organizations',
             'Separate CLA list; economics and political-science orgs would sit here. Not enumerated to '
             'research tooling.',
             'https://www.stcloudstate.edu/cla/student/student-orgs.aspx')],
  'faculty': [('⚠⚠ Lisa Johnson — Scheduling Coordinator, Atwood Memorial Center',
               'THE SINGLE MOST USEFUL NUMBER AT ST. CLOUD AND ARGUABLY IN THE STATE. She books the $85 table '
               'in the Main Lounge and the $45 kiosk. There is no committee, no sponsor, no approval chain — '
               'one call, one date, one invoice. Ask her three things: (1) book the table, (2) what insurance '
               'certificate is required and at what limit (published nowhere), and (3) whether Mainstreet on '
               'Sep 2 is the same booking or a separate track.',
               'Atwood Memorial Center',
               'lajohnson@stcloudstate.edu · (320) 308-2074',
               'https://www.stcloudstate.edu/atwood/about/staff.aspx'),
              ('Atwood Memorial Center — facility and rates line',
               'The number printed on the rental-rates page itself. Second call if Lisa Johnson is out.',
               'Atwood Memorial Center',
               '(320) 308-2075',
               'https://www.stcloudstate.edu/atwood/reservations/rental-rates.aspx'),
              ('⚠ Reid (Douglas) Frederiksen — Assistant Director for Conference and Event Services',
               'Owns the Conference and Scheduling function that the Event Space Usage policy names as '
               'arranging "contracts and billings" for off-campus groups — i.e. the person who would write the '
               'Facilities Agreement required by Minnesota State Procedure 6.7.2. ⚠ NO DIRECT NUMBER IS '
               'PUBLISHED FOR HIM — look up here; reach him via the Atwood main line.',
               'Atwood Memorial Center — Conference and Event Services',
               'douglas.frederiksen@stcloudstate.edu · no number published — look up here; use (320) 308-2205',
               'https://www.stcloudstate.edu/atwood/about/staff.aspx'),
              ('Tommy Balicky — Executive Director of Atwood and the Department of Campus Involvement',
               'Runs both the building and the involvement operation — the escalation point, and the person '
               'who could waive or interpret the credit-card-sign-up clause if it were ever raised against a '
               'crypto table. The Associate Director seat is VACANT and shares this line '
               '(atwood@stcloudstate.edu).',
               'Atwood / Department of Campus Involvement',
               'tbbalicky@stcloudstate.edu · (320) 308-2205',
               'https://www.stcloudstate.edu/campusinvolvement/contact.aspx'),
              ('⚠ Carly Frederick — Assistant Director of Campus Involvement, Campus Programs',
               'OWNS MAINSTREET. The call for the two unpublished Mainstreet facts: what time it runs on Wed '
               'Sep 2, 2026, and what "community partners" actually means for a for-profit outsider.',
               'Department of Campus Involvement',
               'carly.frederick@stcloudstate.edu · (320) 308-2205',
               'https://www.stcloudstate.edu/campusinvolvement/contact.aspx'),
              ('Molly McCann — Director of Campus Involvement',
               'Directs involvement programming including Mainstreet; Carly Frederick reports into this '
               'function.',
               'Department of Campus Involvement',
               'mollyann.mccann@stcloudstate.edu · (320) 308-2205',
               'https://www.stcloudstate.edu/campusinvolvement/contact.aspx'),
              ('Anna Lehto — Assistant Director of Campus Involvement, Student Orgs and Greek Life',
               'Owns the student-organization relationship and the HuskiesConnect directory that outsiders '
               'cannot see. If DGD ever wants a speaker slot with the cybersecurity or CS clubs, she is the '
               'introduction — and a speaker slot is not "fronting," so it carries none of the co-sponsorship '
               'risk.',
               'Department of Campus Involvement',
               'anna.lehto@stcloudstate.edu · (320) 308-2205',
               'https://www.stcloudstate.edu/campusinvolvement/contact.aspx'),
              ('Campus Involvement — remaining staff on the shared line',
               'Lori Laudenbach, Accounting Technician (lalaudenbach@stcloudstate.edu) — she invoices. Arina '
               'Kisteneva, GA Huskies Events and Activities Team; Damien Ronk, GA Student Organizations; '
               'Claire Nelson, GA Civic Engagement. Heather VanWagner, Office Manager '
               '(heather.vanwagner@stcloudstate.edu) — NO NUMBER PUBLISHED, look up here. All others reachable '
               'on the departmental line.',
               'Department of Campus Involvement',
               'see notes · (320) 308-2205',
               'https://www.stcloudstate.edu/campusinvolvement/contact.aspx'),
              ('Joseph Koenig — Technology Coordinator, Atwood',
               'A/V and technical support; the $22/hour tech fee and the seven-day cancellation rule that '
               'triggers a two-hour minimum tech charge both run through this function.',
               'Atwood Memorial Center',
               'joseph.koenig@stcloudstate.edu · (320) 308-2021',
               'https://www.stcloudstate.edu/atwood/about/staff.aspx'),
              ('University Chronicle — advertising (Mass Communications and Film)',
               'The policy page names the Chronicle as the route to advertise OUTSIDE Atwood. A paid student-'
               'newspaper ad is a legitimate parallel channel that no solicitation policy touches.',
               'Mass Communications and Film',
               '(320) 308-3943',
               'https://www.stcloudstate.edu/atwood/about/policies/advertising-promotion.aspx'),
              ('Huskies Dining — catering (exclusive provider)',
               'Named as holding exclusive rights: no food or beverage may be sold or served in Atwood or on '
               'the adjacent malls unless purchased through or prepared by Huskies Dining. Relevant only if '
               'DGD wants to put anything edible on the table.',
               'Huskies Dining',
               '(320) 308-4295 · https://stcloud.catertrax.com/',
               'https://www.stcloudstate.edu/atwood/about/policies/advertising-promotion.aspx'),
              ('Troy VanWagner — Underground Bowling Center / Machinery Repair',
               'Atwood facilities. Carried across for completeness.',
               'Atwood Memorial Center',
               'tavanwagner@stcloudstate.edu · (320) 308-3774',
               'https://www.stcloudstate.edu/atwood/about/staff.aspx'),
              ('Intramurals and Sport Clubs Coordinator',
               'Printed on the student-organizations page; carried across for completeness.',
               'Department of Campus Involvement',
               '(320) 308-6691',
               'https://www.stcloudstate.edu/campusinvolvement/student-orgs/default.aspx'),
              ('(Herberger Business School faculty)',
               '⚠ NOT CONFIRMED — NO INDIVIDUAL FINANCE, FINTECH OR BLOCKCHAIN FACULTY MEMBER COULD BE '
               'CONFIRMED AT SCSU. The Herberger faculty page carries NO directory at all: it routes to a '
               '"SCSU EXPERT GUIDE" and a Digital Measures login, neither of which returned data. Look up '
               'here; the Finance program page is '
               'https://www.stcloudstate.edu/programs/finance/default.aspx and Information Systems faculty are '
               'at https://www.stcloudstate.edu/is/faculty-staff/default.aspx. No number published.',
               'Herberger Business School',
               'no number published — look up here',
               'https://www.stcloudstate.edu/hbs/faculty.aspx')],
  'courses': [('(No crypto/fintech course found)',
               'NO blockchain, cryptocurrency or fintech catalog course was confirmed at SCSU. The catalog is '
               'at https://future-catalog-stcloudstate.catalog.prod.coursedog.com/ and did not surface one to '
               'search. Given that the faculty directory is also unreadable, treat this as unconfirmed rather '
               'than absent.',
               'https://future-catalog-stcloudstate.catalog.prod.coursedog.com/')],
  'events': [('⚠ MAINSTREET INVOLVEMENT FAIR',
              'WED SEP 2, 2026, campus walkway near Atwood Memorial Center. "More than 150 departments, '
              'services, student organizations, and community partners." The single biggest concentration of '
              'students at SCSU all year, in week two of the semester. Time not published; sign-up via '
              'HuskiesConnect. The 2025 edition is archived at '
              'https://huskiesconnect.stcloudstate.edu/event/11406579.',
              'https://www.stcloudstate.edu/campusinvolvement/annual-events/mainstreet.aspx'),
             ('Atwood traditions and the HuskiesConnect events feed',
              'SCSU publishes an Atwood traditions calendar and a live events feed at '
              'https://huskiesconnect.stcloudstate.edu/events. Neither yielded Fall 2026 dates beyond '
              'Mainstreet to research tooling. Worth a check nearer the date for a second high-traffic day to '
              'book the $85 table against.',
              'https://www.stcloudstate.edu/atwood/events/traditions.aspx'),
             ('(No hackathon or blockchain event)',
              'NO hackathon, blockchain conference, research centre or crypto-related legislative activity was '
              'found connected to SCSU. The cybersecurity clubs are the nearest adjacent community.',
              'https://www.stcloudstate.edu/cids/student/student-orgs.aspx')],
  'play': 'This is the campus to run first and the template for the whole state. St. Cloud State publishes an '
          'off-campus rate card — $85 for a table in the Atwood Main Lounge, $85 for outside mall space, $45 '
          'for a kiosk, per day — and states in policy that "opportunities may also be available for '
          'non-university organizations and businesses." No sponsor, no committee, no approval chain: call '
          'Lisa Johnson at (320) 308-2074 and book a day. ⚠ TWO THINGS WILL GET YOU THROWN OUT, so design '
          'around them before you arrive. First, Atwood bans "credit card or debit card sign-ups" outright — '
          'almost certainly downstream of Minn. Stat. s 135A.145 — so run an email-only table, capture no '
          'payment credentials, and have the line ready: DGD is not a card issuer under 15 U.S.C. s 1602. '
          'Second, do NOT ask a student org to book for you: the Co-Sponsorship Policy names "fronting" and '
          'punishes a second offence with loss of Atwood booking privileges for the whole academic year plus '
          'public-rate charges — you would be risking their year to save $85. Book Wed Sep 2 if Mainstreet '
          'admits community partners (ask Carly Frederick on the same call), otherwise book any high-traffic '
          'Tuesday or Wednesday in September or October. ⚠ AND GO EARLY: classes end FRI DEC 4, the earliest '
          'in the state, so St. Cloud disappears twelve days before the flagship does.',
  'gaps': ['⚠ Is Mainstreet participation the same as an $85 promotional-space booking, or a separate track? '
           'And what time does it run on Wed Sep 2, 2026? ☎ Carly Frederick / Lisa Johnson (320) 308-2074. '
           'https://www.stcloudstate.edu/campusinvolvement/annual-events/mainstreet.aspx',
           '⚠ What insurance certificate and dollar limit are required for an off-campus vendor? NO Atwood page '
           'publishes one; Minnesota State Procedure 6.7.2 requires liability coverage naming the State of '
           'Minnesota as additional insured but sets no number. ☎ (320) 308-2074.',
           'Add/drop deadline — the registrar says deadlines "vary depending upon the course" and publishes '
           'none. https://www.stcloudstate.edu/registrar/registration/default.aspx',
           'Whether SCSU has any blockchain or crypto student organization — HuskiesConnect is LOGIN-GATED '
           '(StarID required) and could not be enumerated. ☎ Anna Lehto (320) 308-2205.',
           'Any SCSU finance/fintech/blockchain faculty member — the Herberger Business School faculty page '
           'has NO directory, routing instead to an "SCSU Expert Guide" and a Digital Measures login. '
           'https://www.stcloudstate.edu/hbs/faculty.aspx',
           'A direct number for Reid (Douglas) Frederiksen, Assistant Director for Conference and Event '
           'Services — none published. https://www.stcloudstate.edu/atwood/about/staff.aspx',
           'Whether any SCSU catalog course touches blockchain or fintech — catalog search returned nothing. '
           'https://future-catalog-stcloudstate.catalog.prod.coursedog.com/'],
  'note': '⚠ Do not let the small enrolment fool anyone into deprioritising St. Cloud. Access is what this '
          'file rates, and SCSU is the only 5 in Minnesota: a published price, a named booker with a direct '
          'line, and no sponsor requirement. It is also one hour from the Twin Cities base, making it the '
          'cheapest confirmed table in the state to actually execute.',
 },

 # ------------------------------------------------- 4. UNIVERSITY OF ST. THOMAS
 {'state': 'Minnesota',
  'name': 'University of St. Thomas',
  'city': 'St. Paul, MN',
  'type': 'Private (religious)',
  'tier': 'A — Named target',
  'access': 3,
  'start': 'Wed Sep 9, 2026 ⚠ THE LATEST SEMESTER START IN MINNESOTA — eighteen days after Metro State and '
           'sixteen after the Minnesota State wave. Only Carleton (trimester, Sep 14) starts later.',
  'adddrop': 'Tue Sep 22, 2026 — "Last day to drop a class without notation on record." One of only five clean '
             'add/drop dates published in this entire state file.',
  'fallbreak': 'Mid-term break Fri Oct 30 – Mon Nov 2, 2026 (a four-day break spanning a weekend).',
  'thanksgiving': 'Thanksgiving break begins Wed Nov 25, 2026; classes resume Mon Nov 30, 2026.',
  'lastclass': 'Tue Dec 15, 2026 — "Final day of classes."',
  'finals': 'Study day Wed Dec 16, 2026 — "Study Day. Final exams begin at 5:30 p.m." Final exams end Tue '
            'Dec 22, 2026. ⚠ St. Thomas runs the longest tail in the state: still examining on Dec 22.',
  'cal_url': 'https://www.stthomas.edu/academics/calendars/2026-2027-undergraduate/index.html',
  'cal_status': 'CONFIRMED — official 2026-2027 undergraduate academic calendar. Hub at '
                'https://www.stthomas.edu/academics/calendars/. ⚠ The law school keeps a SEPARATE calendar '
                '(https://law.stthomas.edu/) and OPUS graduate business runs its own '
                '(https://business.stthomas.edu/graduate/calendar/) — do not use either for undergraduates.',
  'fair': 'Fall Student Activities Fair (Department of Campus Life)',
  'fair_date': '⚠ UNVERIFIED — DATE COULD NOT BE READ. The event exists on Tommie Link '
               '(https://stthomas.campuslabs.com/engage/event/2309482) but THE PAGE IS JAVASCRIPT-RENDERED and '
               'returned no date, time or location to research tooling — only the meta description "Discover '
               'unique opportunities at!" and the notice "This application requires JavaScript to be enabled." '
               'The university newsroom confirms the fair runs each fall '
               '(https://news.stthomas.edu/activities-fair/) and each spring '
               '(https://news.stthomas.edu/check-out-spring-activities-fair-today/). PATTERN: early in the fall '
               'semester, run by the Department of Campus Life. With a Sep 9 start, expect mid-to-late '
               'September 2026. Will post to Tommie Link. ☎ Campus Life (651) 962-6130.',
  'fair_outside': '⚠ NOT PUBLISHED for the fair — but the ASC manual answers the broader question and the '
                  'answer is a qualified YES ON A DIFFERENT TRACK. Verbatim: "Solicitation or sale of any '
                  'products at the University of St. Thomas by any group or individual REQUIRES WRITTEN '
                  'PERMISSION," and "CAREER SERVICES WILL COORDINATE AND SPONSOR EXTERNAL VENDOR '
                  'RESERVATIONS." External vendors do not go through Student Activities at St. Thomas; they go '
                  'through Career Development. Ask Mary Beth Pickett, (651) 962-6777, not the fair organisers.',
  'fair_cost': 'NOT PUBLISHED for the fair. For external vendors generally the ASC manual says only: "The '
               'University may, if it chooses, impose an additional \'rental charge\' to cover overhead costs '
               'to the institution" — a discretionary, unquantified fee. Facility rental rates "can be found '
               'online at 25Live or by communicating with Marguerite [von Duerckheim]," (651) 962-6674.',
  'fair_deadline': 'NOT PUBLISHED. The documented lead times at St. Thomas are: two weeks for a club '
                   'fundraising report, and 48 hours for a student Notice of Intent to Demonstrate. Neither '
                   'governs a vendor table. Ask Career Development.',
  'fair_url': 'https://www.stthomas.edu/student-life/get-involved/clubs-organizations/',
  'policy': 'Anderson Student Center Policies & Procedures Manual + Undergraduate Club and Organization '
            'Handbook + Student Policy 602, "Expression, Demonstrations, Speakers and Sponsorship" (latest '
            'revision Aug 9, 2024; owner: Vice President for Student Affairs)',
  'policy_url': 'https://www.stthomas.edu/about/departments/general-counsel/policy-pdfs/anderson-student-center-policies-and-procedures-manual.pdf',
  'policy_key': "⚠ ST. THOMAS IS A PRIVATE CATHOLIC UNIVERSITY. IT HAS NO PUBLIC-FORUM OBLIGATION, NO FIRST "
                "AMENDMENT DUTY TOWARD OUTSIDE SPEAKERS, AND MINNESOTA HAS NO CAMPUS FREE-SPEECH STATUTE TO "
                "INVOKE (see the U of M Twin Cities policy_key). Everything here is contractual permission, "
                "granted or withheld at the university's discretion. DO NOT ARGUE RIGHTS AT ST. THOMAS — ARGUE "
                "FIT. "
                "ANDERSON STUDENT CENTER POLICIES & PROCEDURES MANUAL — THE OPERATIVE DOCUMENT, AND A PDF THAT "
                "PRINTS THREE DIRECT PHONE NUMBERS THAT APPEAR NOWHERE IN THE HTML SITE. VERBATIM: "
                "'SOLICITATION OR SALE OF ANY PRODUCTS AT THE UNIVERSITY OF ST. THOMAS BY ANY GROUP OR "
                "INDIVIDUAL REQUIRES WRITTEN PERMISSION.' 'THE DEPARTMENT OF CAMPUS LIFE IS THE UNIVERSITY "
                "OFFICIAL RESPONSIBLE FOR GRANTING SUCH PERMISSION.' 'THE BUSINESS OF ANY APPROVED SALE OR "
                "SOLICITATION MUST BE CONDUCTED IN THE CONFINEMENT OF THE AREA (OR SPACE) APPROVED BY THE "
                "DEPARTMENT OF CAMPUS LIFE.' 'THE UNIVERSITY MAY, IF IT CHOOSES, IMPOSE AN ADDITIONAL "
                "\"RENTAL CHARGE\" TO COVER OVERHEAD COSTS TO THE INSTITUTION.' "
                "⚠⚠ THE DOOR — VERBATIM, AND IT IS NOT WHERE ANYONE WOULD LOOK: 'AN INFORMATION TABLE, LOCATED "
                "ON THE 2ND FLOOR, MAY BE RESERVED THROUGH 25LIVE... TO SOLICIT FOR ON CAMPUS EVENTS. CAREER "
                "SERVICES WILL COORDINATE AND SPONSOR EXTERNAL VENDOR RESERVATIONS.' THAT SINGLE SENTENCE IS "
                "THE WHOLE PLAY AT ST. THOMAS. External vendors do not go through Student Activities and do "
                "not need a student club — THEY GO THROUGH CAREER DEVELOPMENT, WHICH THE UNIVERSITY'S OWN "
                "POLICY SAYS WILL 'COORDINATE AND SPONSOR' THEM. That is a documented, named route with a real "
                "office and published direct lines behind it. "
                "MONAHAN PLAZA: 'Vendor deliveries must be coordinated through Public Safety with the "
                "assistance of the Director.' PROHIBITED on the plaza: 'ANY NON-UNIVERSITY SPONSORED SALES OF "
                "FOOD, ALCOHOL OR MERCHANDISE.' EXTERNAL FACILITY RENTAL: 'EXTERNAL ENTITIES MAY CONTACT "
                "MARGUERITE VON DUERCKHEIM FOR INQUIRIES ABOUT RENTING SPACE'; rates 'can be found online at "
                "25Live or by communicating with Marguerite.' "
                "⚠ NOTE WHAT IS ABSENT AND TREAT IT AS FAVOURABLE: THE ASC MANUAL CONTAINS NO INSURANCE "
                "REQUIREMENT, NO DOLLAR LIMIT, NO DEPOSIT AND NO CANCELLATION TERMS. Compare Mankato's "
                "$2,000,000/$2,000,000 and UMN's 50% non-refundable deposit. "
                "UNDERGRADUATE CLUB AND ORGANIZATION HANDBOOK "
                "(https://www.stthomas.edu/about/departments/general-counsel/policy-pdfs/student-clubs-and-organizations-handbook.pdf) "
                "⚠ SIGNING CONTRACTS ON SITE — VERBATIM: 'STUDENTS ARE NOT ALLOWED TO ENTER INTO ANY "
                "AGREEMENTS OR SIGN ANY CONTRACTS ON BEHALF OF THE UNIVERSITY.' All vendor agreements require "
                "Campus Life and advisor review; clubs must use 'on-campus vendors or the preferred vendors "
                "list' for all purchases. ⚠ PAYMENT/FUNDING RAILS — VERBATIM: 'RECOGNIZED STUDENT CLUBS AND "
                "ORGANIZATIONS ARE NOT ALLOWED TO CREATE EXTERNAL GOFUND-ME TYPE EVENTS/ACCOUNTS.' Clubs "
                "cannot use social media to 'advertise or promote external groups or organizations.' All "
                "fundraising to support an external organization requires a fundraising report submitted a "
                "minimum of two weeks in advance; contributions must be payable directly to the charitable "
                "organization; clubs cannot imply university endorsement. Gambling, raffles and games of "
                "chance are not approved. On outsiders and student data: 'The University of St. Thomas "
                "recognizes and values the role of non-university and university volunteers who may work with "
                "student clubs,' BUT external groups seeking contact with student leaders must go through the "
                "general club email and THE DEPARTMENT WILL NOT RELEASE MEMBER NAMES OR CONTACT DETAILS TO "
                "EXTERNAL PARTIES. "
                "STUDENT POLICY 602, 'EXPRESSION, DEMONSTRATIONS, SPEAKERS AND SPONSORSHIP,' LATEST REVISION "
                "AUGUST 9, 2024, OWNER VICE PRESIDENT FOR STUDENT AFFAIRS "
                "(https://www.stthomas.edu/about/departments/general-counsel/policy-pdfs/student-policy-regarding-expression-demonstrations-speakers-and-sponsorship.pdf). "
                "VERBATIM: 'THIS POLICY DOES NOT AFFORD A VENUE FOR DEMONSTRATIONS BY INDIVIDUALS WHO ARE NOT "
                "ST. THOMAS STUDENTS.' Demonstrations may not 'HAVE A COMMERCIAL OR BUSINESS PURPOSE.' "
                "⚠ 'ST. THOMAS WILL NOT SPONSOR STUDENT GROUPS, ORGANIZATIONS OR ACTIVITIES THAT PROMOTE "
                "BELIEFS THAT ARE CONTRARY TO CATHOLIC TEACHING.' 'External speakers and performers who are "
                "sponsored or invited to campus by St. Thomas students or student organizations must agree to "
                "refrain from presenting and performing material that is defamatory, obscene, or CONTRAVENES "
                "THE ST. THOMAS CONVICTIONS STATEMENT.' Students must file a 'Notice of Intent to Demonstrate' "
                "at least 48 hours in advance with the Dean of Students Office. 'The allowance of student "
                "demonstrations does not imply sponsorship of the demonstration by St. Thomas.' "
                "ANTI-FRONTING: no clause by that name. The functional equivalent is the combination of the "
                "club handbook barring clubs from promoting external organizations and barring students from "
                "signing contracts, with the ASC manual routing external vendors to CAREER SERVICES rather "
                "than to clubs. The university has simply designated a different sponsor. "
                "DOES SPONSORSHIP CURE IT? YES — BUT THE SPONSOR IS CAREER SERVICES, NOT A STUDENT CLUB. "
                "Courting the Wall Street Club to host DGD is the slow, low-probability path and the handbook "
                "actively obstructs it. Calling Career Development's employer-partnerships line is the fast "
                "one and the policy explicitly contemplates it.",
  'sponsor_required': '⚠ YES — AND THE POLICY NAMES THE SPONSOR, WHICH IS THE UNUSUAL AND VALUABLE PART. '
                      '"Solicitation or sale of any products... by any group or individual requires written '
                      'permission," granted by the Department of Campus Life — but the operative routing '
                      'sentence is "CAREER SERVICES WILL COORDINATE AND SPONSOR EXTERNAL VENDOR RESERVATIONS." '
                      'Do not chase a student club: the club handbook forbids clubs from promoting external '
                      'organizations, forbids students from signing contracts, and forbids the department from '
                      'giving you member contact details. One call to Mary Beth Pickett, Employer '
                      'Partnerships, (651) 962-6777, replaces three weeks of club courtship.',
  'clubs': [('⚠ Tommie Link is JAVASCRIPT-RENDERED — no club could be read',
             'https://tommielink.stthomas.edu/ and EVERY stthomas.campuslabs.com/engage/organization/ URL '
             'returned only "This application requires JavaScript to be enabled" to research tooling. The '
             'organizations below are confirmed to EXIST because their URLs surfaced in search, but their '
             'descriptions, active status and officers COULD NOT BE READ and no contacts are published. NO '
             'BLOCKCHAIN OR CRYPTOCURRENCY CLUB WAS FOUND — treat as unconfirmed, not absent.',
             'https://tommielink.stthomas.edu/'),
            ('The Wall Street Club',
             'Highest-fit student organization at St. Thomas by name. Status, size, meeting schedule and '
             'contacts all unreadable (JavaScript-rendered). ⚠ Note the club handbook bars the department from '
             'releasing member names or contact details to external parties — so even a phone call will not '
             'produce a student contact. Go through Career Development instead.',
             'https://stthomas.campuslabs.com/engage/organization/stthomas-wall-street-club'),
            ('Computer Science Club',
             'The technical-audience club. Same JavaScript-rendering problem.',
             'https://stthomas.campuslabs.com/engage/organization/ComputerScience'),
            ('Sports Management Club',
             'Lower fit; listed for completeness. Same rendering problem.',
             'https://stthomas.campuslabs.com/engage/organization/SportsBusiness'),
            ('Anderson Student Center (department page on Tommie Link)',
             'The ASC maintains its own Tommie Link presence — useful only as a route to the department.',
             'https://stthomas.campuslabs.com/engage/organization/asc')],
  'faculty': [('⚠⚠ Mary Beth Pickett — Employer Partnerships, Career Development Center (MHC 123)',
               'THE DOOR AT ST. THOMAS, AND THE POLICY SAYS SO IN WRITING: "Career services will coordinate '
               'and sponsor external vendor reservations." She identifies partnerships and organises career '
               'fairs and networking events. One call here substitutes for the entire student-club route, '
               'which the club handbook actively obstructs. Ask her: will Career Development sponsor a DGD '
               'information table on the ASC 2nd floor, what does the discretionary "rental charge" come to, '
               'and what are the Fall 2026 career-fair dates.',
               'Career Development Center',
               'pick7529@stthomas.edu · (651) 962-6777',
               'https://career.stthomas.edu/staff/'),
              ('Career Development Center — main line (MHC 123, 2115 Summit Ave)',
               'Mon–Fri 8:00 a.m.–4:30 p.m.; drop-ins Mon–Fri 10:00 a.m.–3:00 p.m. during fall and spring '
               'semesters. Second call if Pickett is out.',
               'Career Development Center',
               '(651) 962-6761 (main line)',
               'https://career.stthomas.edu/'),
              ('Mary Graf — Career Coach',
               'Career Development staff with a published direct line; useful as an alternate entry to the '
               'department.',
               'Career Development Center',
               'graf3633@stthomas.edu · (651) 962-6435',
               'https://career.stthomas.edu/staff/'),
              ('Pa Jai Thao — Employer Engagement',
               'Secures internships and job opportunities for students; works alongside Pickett on the '
               'employer side. NO NUMBER PUBLISHED — look up here; reach via the Career Development main line.',
               'Career Development Center',
               'pthao@stthomas.edu · no number published — look up here; use (651) 962-6761',
               'https://career.stthomas.edu/staff/'),
              ('⚠ Kevin Manson — Director, Anderson Student Center',
               'PHONE NUMBER MINED FROM THE ASC POLICIES & PROCEDURES MANUAL PDF — it appears nowhere in the '
               'HTML site. He directs the building in which the 2nd-floor information table sits and is the '
               'escalation point above Campus Life on any solicitation question.',
               'Anderson Student Center',
               '(651) 962-7137',
               'https://www.stthomas.edu/about/departments/general-counsel/policy-pdfs/anderson-student-center-policies-and-procedures-manual.pdf'),
              ('⚠ Chris Yahnke — Assistant Director, Anderson Student Center',
               'Also mined from the ASC manual PDF. Day-to-day ASC operations — the person most likely to '
               'actually answer.',
               'Anderson Student Center',
               '(651) 962-6256',
               'https://www.stthomas.edu/about/departments/general-counsel/policy-pdfs/anderson-student-center-policies-and-procedures-manual.pdf'),
              ('⚠ Marguerite von Duerckheim — external facility rental',
               'NAMED IN THE ASC MANUAL AS THE CONTACT FOR EXTERNAL ENTITIES RENTING SPACE, with her direct '
               'line printed in the PDF and nowhere else. She holds the rental rates that are otherwise only '
               'visible inside 25Live. If DGD wants a room rather than a table, this is the call.',
               'Anderson Student Center / facility rental',
               '(651) 962-6674',
               'https://www.stthomas.edu/about/departments/general-counsel/policy-pdfs/anderson-student-center-policies-and-procedures-manual.pdf'),
              ('⚠ Department of Campus Life',
               'THE OFFICIAL WHO GRANTS WRITTEN PERMISSION TO SOLICIT — "The Department of Campus Life is the '
               'university official responsible for granting such permission." Number printed in the club '
               'handbook PDF. Also owns the Fall Student Activities Fair whose date Tommie Link will not '
               'render.',
               'Department of Campus Life',
               '(651) 962-6130',
               'https://www.stthomas.edu/about/departments/general-counsel/policy-pdfs/student-clubs-and-organizations-handbook.pdf'),
              ('Assistant Director, Campus Life (Clubs & Organizations)',
               'Direct line printed in the club handbook PDF; the club-side counterpart to Pickett. Note the '
               'handbook forbids releasing student member contacts to external parties, so use this line to '
               'ask about permission, not about students.',
               'Department of Campus Life',
               '(651) 962-6195',
               'https://www.stthomas.edu/about/departments/general-counsel/policy-pdfs/student-clubs-and-organizations-handbook.pdf'),
              ('Campus Scheduling Services',
               'Runs 25Live, through which the 2nd-floor information table is actually reserved. Number from '
               'the club handbook PDF.',
               'Campus Scheduling Services',
               '(651) 962-6670',
               'https://www.stthomas.edu/about/departments/general-counsel/policy-pdfs/student-clubs-and-organizations-handbook.pdf'),
              ('Dean of Students Office',
               'Owns Student Policy 602 and the Notice of Intent to Demonstrate. Relevant if DGD is ever '
               'accused of a "commercial or business purpose" demonstration.',
               'Dean of Students',
               'deanofstudents@stthomas.edu · (651) 962-6050',
               'https://stthomas.edu/student-affairs/departments/dean-of-students/policies/index.html'),
              ('⚠ Dr. Jiang (Will) Zhang — Assistant Professor of Finance; LEAD FACULTY, FINTECH CERTIFICATE',
               'THE BEST ACADEMIC DOOR AT ST. THOMAS AND ONE OF THE BEST IN THE STATE. He leads the '
               'undergraduate Financial Technology certificate and owns FINC 315 "Cryptocurrency and '
               'Blockchain" — a dedicated, required, UNDERGRADUATE crypto course, which the flagship does not '
               'have. ⚠ NO EMAIL OR PHONE IS PUBLISHED FOR HIM. The Opus faculty directory '
               '(https://business.stthomas.edu/faculty/directory/) is a search UI that returned no profile '
               'data to research tooling. DO NOT GUESS AN ADDRESS — reach him through the Opus main line.',
               'OPUS College of Business — Finance',
               'not published — reach via Opus College of Business (651) 962-4200',
               'https://www.stthomas.edu/academics/undergraduate/financial-technology-fintech-certificate/'),
              ('OPUS College of Business (1000 LaSalle Avenue, Minneapolis)',
               'Main line for the FinTech certificate, the Finance department and Dr. Zhang. Ask whether FINC '
               '315 runs in Fall 2026 — it is a 2-credit module and may run as a half-term, which would put it '
               'squarely in the October–December window.',
               'OPUS College of Business',
               '(651) 962-4200 (main line)',
               'https://business.stthomas.edu/faculty-research/faculty-bios/'),
              ('Vern Klobassa — branding and logo approvals',
               'Named in the club handbook as the contact for branding/logo creation. Relevant only if DGD '
               'produces co-branded material.',
               'University Communications',
               'klob6303@stthomas.edu · no number published — look up here',
               'https://www.stthomas.edu/about/departments/general-counsel/policy-pdfs/student-clubs-and-organizations-handbook.pdf'),
              ('University of St. Thomas — main line / Registrar; Disability Resources',
               'University main and registrar (651) 962-5000. Disability Resources (651) 962-6315 for event '
               'accommodations; Campus Life fax 651-962-6152. Carried across for completeness.',
               'University',
               '(651) 962-5000 (main line) · Disability Resources (651) 962-6315',
               'https://www.stthomas.edu/academics/calendars/')],
  'courses': [('⚠ FINC 315',
               '"Cryptocurrency and Blockchain" — 2 credits, a REQUIRED component of the undergraduate '
               'Financial Technology (FinTech) certificate. ⚠ THIS IS THE ONLY DEDICATED UNDERGRADUATE CRYPTO '
               'COURSE FOUND IN MINNESOTA — UMN\'s equivalent (FINA 5125/6125) is graduate-level and '
               'spring-only. Lead faculty Dr. Jiang (Will) Zhang. ⚠ FALL 2026 OFFERING UNVERIFIED: the catalog '
               'does not publish term rotation. A 2-credit course often runs as a half-term module, which '
               'would place it in the Oct–Dec window. The live class finder is '
               'https://classes.aws.stthomas.edu/ (term code 202630). ☎ (651) 962-4200.',
               'https://www.stthomas.edu/academics/undergraduate/financial-technology-fintech-certificate/'),
              ('FINC 314',
               '"Introduction to Financial Technology" — 4 credits, the anchor course of the 12-credit FinTech '
               'certificate. Fall 2026 offering UNVERIFIED.',
               'https://www.stthomas.edu/academics/undergraduate/financial-technology-fintech-certificate/'),
              ('FINC 316',
               '"Artificial Intelligence and Machine Learning in Finance" — 2 credits, the third required '
               'FinTech certificate course. Fall 2026 offering UNVERIFIED. Full finance catalog (FINC 310, '
               '311, 324, 325 Investments, 350 Finance on Wall Street, 351, 410 Derivatives, 430 Financial '
               'Intermediaries, 440, 442, 450, 475, 480, 490 Topics) at the URL.',
               'https://www.stthomas.edu/catalog/curricula/finance/')],
  'events': [('⚠⚠ "Web3 Impact on Law and Society" Conference — THE STATE\'S ONLY BLOCKCHAIN CONFERENCE, AND '
              'IT IS HOSTED HERE',
              'Hosted jointly by the MINNESOTA BLOCKCHAIN INITIATIVE, the UNIVERSITY OF ST. THOMAS SCHOOL OF '
              'LAW, and the ST. THOMAS LAW JOURNAL. ⚠ ITS OWN SITE, https://www.mnweb3lawconference.com, IS '
              'ROBOTS-BLOCKED AND DNS-UNRESOLVABLE to research tooling — date, venue, registration and '
              'sponsorship tiers are ALL UNVERIFIED. Its existence and the partnership are corroborated by the '
              'Minnesota Daily, which reports the law school "hosts large blockchain events in collaboration '
              'with the Minnesota Blockchain Initiative." GET THE DETAILS FROM connect@mnblockchain.org — this '
              'is a legitimate, non-commercial, sponsorship-friendly door into St. Thomas that no ASC or '
              'Campus Life rule touches.',
              'https://mndaily.com/city/minnesotas-emerging-blockchain-builders/11/13/2025/eicmndaily-com/'),
             ('Fall Student Activities Fair',
              'Run by the Department of Campus Life each fall. ⚠ Fall 2026 date UNVERIFIED — Tommie Link is '
              'JavaScript-rendered and returned nothing. Pattern: mid-to-late September given the Sep 9 start. '
              '☎ Campus Life (651) 962-6130.',
              'https://stthomas.campuslabs.com/engage/event/2309482'),
             ('Fall 2026 career fairs',
              'Organised by Career Development and coordinated by Mary Beth Pickett. ⚠ FALL 2026 DATES ARE NOT '
              'PUBLISHED on any retrievable page. Since Career Services is also the office that "coordinate[s] '
              'and sponsor[s] external vendor reservations," one call gets both the fair dates and the vendor '
              'route. ☎ (651) 962-6777.',
              'https://www.stthomas.edu/careerdevelopment/employers/employerservices/'),
             ('Minnesota Blockchain Initiative monthly Spotlight Meetups',
              'Twin Cities, monthly, plus an annual "Crypto Spring" conference. St. Thomas is a named academic '
              'partner. connect@mnblockchain.org.',
              'https://www.mnblockchain.org/')],
  'play': 'Ignore the Wall Street Club and call Career Development. St. Thomas buries the answer in a PDF: '
          '"Career services will coordinate and sponsor external vendor reservations" — the university has '
          'designated a specific office to sponsor outsiders, and that office publishes direct lines. Call Mary '
          'Beth Pickett, Employer Partnerships, at (651) 962-6777 and ask her to sponsor a DGD information '
          'table on the Anderson Student Center 2nd floor, reserved through 25Live. The club route is a trap '
          'here: the Undergraduate Club Handbook forbids clubs from promoting external organizations, forbids '
          'students from signing any contract, bars external GoFundMe-type accounts, and expressly prevents '
          'the department from giving you student contact details — three weeks of courtship would end in a '
          'no. ⚠ Two St. Thomas-specific cautions: it is Catholic and Policy 602 says it "will not sponsor '
          'student groups, organizations or activities that promote beliefs that are contrary to Catholic '
          'teaching," and demonstrations may not "have a commercial or business purpose" — so present DGD as '
          'financial education, never as a demonstration or a sale. The prize beyond the table is bigger: FINC '
          '315 "Cryptocurrency and Blockchain" is the ONLY dedicated undergraduate crypto course in Minnesota, '
          'and the St. Thomas School of Law co-hosts the state\'s only Web3 conference with the Minnesota '
          'Blockchain Initiative. Email connect@mnblockchain.org and call the Opus College of Business at '
          '(651) 962-4200 for Dr. Jiang (Will) Zhang. Also note the calendar: St. Thomas starts LAST among '
          'semester schools (Sep 9) and examines until Dec 22 — it is the best late-semester stop in the state.',
  'gaps': ['⚠ Will Career Development actually sponsor a vendor like DGD, and what does the discretionary '
           '"rental charge" come to? The ASC manual names the route but no fee. ☎ Mary Beth Pickett '
           '(651) 962-6777.',
           '⚠ Fall Student Activities Fair date — Tommie Link is JAVASCRIPT-RENDERED and returned no date, '
           'time or location. ☎ Campus Life (651) 962-6130. '
           'https://stthomas.campuslabs.com/engage/event/2309482',
           '⚠ Does FINC 315 "Cryptocurrency and Blockchain" run in Fall 2026? It is a 2-credit module and may '
           'run as a half-term. Who teaches it besides Dr. Zhang, and what is his direct contact? ☎ OPUS '
           'College of Business (651) 962-4200. https://classes.aws.stthomas.edu/',
           '⚠ "Web3 Impact on Law and Society" conference — date, venue, sponsorship tiers. Its site '
           'mnweb3lawconference.com is ROBOTS-BLOCKED and DNS-unresolvable. Email connect@mnblockchain.org.',
           'Whether any blockchain or crypto student club exists — Tommie Link and every campuslabs '
           'organization URL are JavaScript-rendered and unreadable. https://tommielink.stthomas.edu/',
           'Fall 2026 career-fair dates — not published on any retrievable page. ☎ (651) 962-6777.',
           'External facility rental rates — visible only inside 25Live or by asking. ☎ Marguerite von '
           'Duerckheim (651) 962-6674.',
           'A direct number or email for Dr. Jiang (Will) Zhang — the Opus faculty directory is a search UI '
           'that returned no profile data. https://business.stthomas.edu/faculty/directory/'],
  'note': '⚠⚠ NAME COLLISION — DO NOT USE stthom.edu. Searches for "University of St. Thomas academic calendar '
          '2026-2027" return stthom.edu, which is the UNIVERSITY OF ST. THOMAS IN HOUSTON, TEXAS — a different '
          'institution with a different calendar. The Minnesota school is stthomas.edu. Within it, the law '
          'school and OPUS graduate business keep SEPARATE calendars from the undergraduate one. Separately: '
          'the three most valuable phone numbers at St. Thomas (Manson, Yahnke, von Duerckheim) exist ONLY '
          'inside the Anderson Student Center PDF manual and appear nowhere in the HTML site — this is the '
          'clearest example in the file of why PDF handbooks are worth mining.',
 },

 # ------------------------------------------------- 5. U of M DULUTH
 {'state': 'Minnesota',
  'name': 'University of Minnesota Duluth',
  'city': 'Duluth, MN',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 4,
  'start': '⚠⚠ Mon Aug 31, 2026 — UMD DOES NOT FOLLOW THE TWIN CITIES CALENDAR. Same system, same Board of '
           'Regents, EIGHT DAYS APART. Anyone who assumes "the U of M starts Sep 8" will arrive in Duluth a '
           'week and a half late.',
  'adddrop': 'UNVERIFIED — not printed on the official 2026-2027 calendar. The Duluth One Stop calendar '
             '(https://onestop.d.umn.edu/calendar/academic-calendar) is a JavaScript filter UI that returned '
             'NO dates to research tooling. ☎ Kirby (218) 726-7163 or One Stop.',
  'fallbreak': '⚠ Thu–Fri Oct 29–30, 2026 — "Fall break: no class." UMD HAS A FALL BREAK; the Twin Cities does '
               'not. Do not schedule the last week of October in Duluth.',
  'thanksgiving': 'Thu Nov 26 and Fri Nov 27, 2026 (holiday / floating holiday).',
  'lastclass': 'Fri Dec 11, 2026 — "Last day of fall semester classes." 70 instructional days.',
  'finals': 'Mon–Fri Dec 14–18, 2026. No study day is listed. Commencement is spring only (May 8, 2027).',
  'cal_url': 'https://www.d.umn.edu/calendar/academic_cal.html',
  'cal_status': 'CONFIRMED — the official static 2026-2027 academic calendar on d.umn.edu. ⚠ THIS IS THE ONLY '
                'UMD CALENDAR PAGE THAT ACTUALLY YIELDS DATES: onestop.d.umn.edu/calendar/academic-calendar and '
                'calendar.d.umn.edu/all/categories/Academic%20Calendar are both JavaScript UIs that returned '
                'nothing. A tentative 2027-28 calendar exists at '
                'https://www.d.umn.edu/calendar/academic_cal_27-28.html.',
  'fair': '⚠ NO FALL INVOLVEMENT FAIR — and it does not matter, because Kirby sells tabling by the day all '
          'semester (which is better than a fair)',
  'fair_date': 'Bulldog Welcome Week 2026 runs AUG 26–30, 2026 — physical move-in Aug 26–27, official '
               'programming begins Aug 27, classes begin Mon Aug 31. ⚠ NO DISTINCT INVOLVEMENT OR ORGANIZATION '
               'FAIR WITH A PUBLISHED DATE WAS FOUND AT UMD. Kirby\'s answer to the fair question is its '
               'standing PAID DAILY TABLING PROGRAMME — which is strictly better for DGD: you can buy a '
               'Tuesday in October rather than compete for a booth on one day in August. ⚠ The Welcome Week '
               'FAQ contains a STALE LINE — "All new freshmen admitted for Fall 2025 are required to attend" — '
               'inside an otherwise-2026 page. Treat the dates as good and the copy as partly stale.',
  'fair_outside': '⚠ YES, BY A DEDICATED POLICY — but not at a fair, at a bought table. UMD is the only campus '
                  'in this file with a policy page TITLED for outside entities: "Policy: Tabling '
                  '(Non-University/External guest)." It covers "Non-UMD, external organizations and '
                  'businesses" seeking to engage UMD students "FOR COMMERCIAL, AWARENESS, OR RECRUITMENT '
                  'PURPOSES" — commercial purposes are named and admitted. ⚠ BUT SEE policy_key: at the table '
                  'itself, "revenue generation (sales or fundraising)" is a NON-PERMISSIBLE ACTIVITY. DGD may '
                  'inform; DGD may not sell or fundraise.',
  'fair_cost': '⚠ $160 PER TABLE PER DAY for non-UMD external guests, one table per day, Kirby Commons, '
               '9:00 a.m.–3:00 p.m., including one 6-foot strip table, two chairs and access to an outlet. '
               'Billing occurs in the first week following the reservation month. For reference: UMD student '
               'orgs and departments get the first 3 tables free, each additional $50, all 12 tables $450; '
               'non-UMD room rentals run $60–$1,200 depending on room and duration.',
  'fair_deadline': '⚠⚠ FALL RESERVATIONS OPEN AFTER AUGUST 15, 2026 (Spring opens after January 5). Submit '
                   '2–4 weeks in advance; confirmation arrives within 3 business days. REQUIRED PAPERWORK DUE '
                   'ONE WEEK BEFORE THE EVENT: a signed Facility Use Agreement AND liability insurance meeting '
                   'specified guidelines. ⚠ THE INSURANCE DOLLAR LIMIT IS NOT PUBLISHED — ask Jodi Nelson, '
                   '(218) 726-7169, when you book.',
  'fair_url': 'https://kirby.d.umn.edu/policy-tabling-non-universityexternal-guest',
  'policy': 'Kirby Student Center — "Policy: Tabling (Non-University/External guest)"; KSC Facilities & Rates; '
            '"Policy: Tabling: RSO & Campus Departments." UMN system layer: Board of Regents / policy.umn.edu.',
  'policy_url': 'https://kirby.d.umn.edu/policy-tabling-non-universityexternal-guest',
  'policy_key': "⚠ UMD IS THE ONLY CAMPUS IN THIS FILE WITH A POLICY PAGE *TITLED* FOR OUTSIDE ENTITIES: "
                "'POLICY: TABLING (NON-UNIVERSITY/EXTERNAL GUEST).' That framing matters — you are not an "
                "exception to a student policy here, you are a named user class with your own rules and your "
                "own price. "
                "WHO IT COVERS, VERBATIM: 'NON-UMD, EXTERNAL ORGANIZATIONS AND BUSINESSES' seeking to engage "
                "UMD students during the academic year 'FOR COMMERCIAL, AWARENESS, OR RECRUITMENT PURPOSES.' "
                "COMMERCIAL PURPOSES ARE NAMED AND ADMITTED. "
                "THE PRICE: '$160 PER TABLE.' 'ONE (1) TABLE PER DAY.' What you get: tabling space in KIRBY "
                "COMMONS, 9:00 A.M.–3:00 P.M., 'ONE (1) 6-FOOT STRIP TABLE AND TWO (2) CHAIRS; ACCESS TO "
                "OUTLET.' Billing in the first week following the reservation month. "
                "⚠⚠ THE BOOKING WINDOW — TIME-CRITICAL: 'FALL RESERVATIONS OPEN AFTER AUGUST 15' (Spring after "
                "January 5). Submit the Non-UMD Guests Space Request Form 2–4 WEEKS IN ADVANCE; confirmation "
                "within 3 business days. REQUIRED DOCUMENTATION DUE ONE WEEK BEFORE THE EVENT: a signed "
                "FACILITY USE AGREEMENT and LIABILITY INSURANCE MEETING SPECIFIED GUIDELINES. ⚠ THE DOLLAR "
                "LIMIT IS NOT PUBLISHED ON THE PAGE — ASK. "
                "⚠⚠ NON-PERMISSIBLE ACTIVITIES — READ THIS CAREFULLY AND DESIGN THE TABLE AROUND IT. VERBATIM: "
                "'NON-PERMISSIBLE ACTIVITIES INCLUDE: REVENUE GENERATION (SALES OR FUNDRAISING); ADULT "
                "ENTERTAINMENT; GAMBLING, RAFFLES, OR DRAWINGS; EMPLOYMENT INTERVIEWS; PROMOTION OF ALCOHOL, "
                "DRUGS, OR TOBACCO PRODUCTS.' Standing in hallways distributing materials is forbidden. WHAT "
                "THAT MEANS FOR DGD: you may PROMOTE and INFORM — the policy's own word is 'awareness' — but "
                "you may NOT sell, take money, fundraise, run a prize draw or giveaway drawing, or conduct "
                "interviews at the table. NO RAFFLES. NO 'ENTER TO WIN.' An awareness table with an email "
                "signup is compliant; a token giveaway drawing is not. "
                "SPONSORSHIP: required ONLY for political campaigns ('sponsorship by a Registered Student "
                "Organization with a member present at all times'). COMMERCIAL TABLING NEEDS NO SPONSOR — JUST "
                "THE $160. "
                "⚠ THE CLAUSE THAT BITES IF YOU GO VIA A CLUB INSTEAD — RSO Tabling Policy "
                "(https://kirby.d.umn.edu/tabling-policies), VERBATIM: 'AT LEAST ONE CURRENTLY ENROLLED UMD "
                "STUDENT REPRESENTATIVE OF THE ORGANIZATION MUST BE PRESENT AT THE TABLE AT ALL TIMES' — and "
                "the policy states this applies expressly 'INCLUDING WHEN COLLABORATING WITH EXTERNAL GUESTS.' "
                "Also: 'STANDING IN THE HALLWAY TO DISTRIBUTE LITERATURE OR SOLICIT IS STRICTLY PROHIBITED.' "
                "Personnel must remain behind the table and may not obstruct foot traffic; 'AGGRESSIVE SALES "
                "TECHNIQUES ARE NOT ALLOWED'; noise 'should be kept to a respectful level.' A CURRENTLY "
                "ENROLLED STUDENT must place the reservation in MAZEVO, and 'RESERVATIONS MUST BE PLACED BY "
                "4:00PM ON THE BUSINESS DAY PRIOR.' An identifying sign (8.5\" x 11\" minimum) or a tablecloth "
                "naming the organization must be visible throughout; tables cleared by 3:00 PM. THERE IS NO "
                "ANTI-FRONTING CLAUSE AT UMD — but the 'student present at all times' rule has the same "
                "practical effect on a club-hosted table, and it is simpler to pay $160. "
                "RATES BY CLIENT CATEGORY (2025-2026, "
                "https://kirby.d.umn.edu/ksc-event-conference-services/ksc-facilities-rates): UMD departments — "
                "waived. UMD student organizations — no charge unless admission or registration fees are "
                "collected (charges apply only to the Kirby Ballroom, Griggs Center, Lounge, Rafters and Kirby "
                "Terrace). Kirby Commons tabling weekdays 9–3 for internal groups: first 3 tables free, each "
                "additional $50, all 12 tables $450. NON-UMD GUESTS: room rentals $60–$1,200 depending on room "
                "and duration; SINGLE TABLE $160. ⚠ DEPOSIT REQUIREMENTS, CANCELLATION POLICIES AND THE "
                "INSURANCE DOLLAR LIMIT ARE NOT SPECIFIED ANYWHERE ON THE RATES PAGE. Reservation line: "
                "(218) 726-7163. "
                "NOTHING AT UMD REACHES PAYMENT CREDENTIALS OR ON-SITE CONTRACT SIGNING. The state statute "
                "Minn. Stat. s 135A.145 (credit-card marketing — see the U of M Twin Cities policy_key) binds "
                "UMD as a U of M campus. "
                "PUBLIC-FORUM POSTURE: UMD is public, so First Amendment forum doctrine applies to its "
                "traditional public fora — but Minnesota has NO campus free-speech statute to cite (see the "
                "U of M Twin Cities policy_key). The $160 fee and every condition above are lawful.",
  'sponsor_required': '⚠ NO — PAY THE $160. Sponsorship is required only for political campaigns. Commercial '
                      'and "awareness" tabling by a non-UMD business is its own named, priced category needing '
                      'no student partner. And going via a club is actively worse: the RSO tabling policy '
                      'requires "at least one currently enrolled UMD student representative... present at the '
                      'table at all times, including when collaborating with external guests," and a student '
                      'must place the booking in Mazévo by 4:00 p.m. the prior business day — you would be '
                      'renting a student\'s whole day to save $160.',
  'clubs': [('⚠ NO BLOCKCHAIN / CRYPTO / WEB3 CLUB AT UMD',
             'None found. UMD claims "over 260 student groups" on BULLDOG CONNECT '
             '(https://z.umn.edu/BulldogConnect / https://duluthumn.campusgroups.com) — ⚠ THE DIRECTORY DID '
             'NOT RENDER AN ORGANIZATION LIST to research tooling, so treat as not-found rather than '
             'confirmed-absent. ☎ Erin Olson, Student Organizations Coordinator, (218) 726-7163.',
             'https://kirby.d.umn.edu/student-organizations'),
            ('⚠ The Bulldog Fund — student-led investment fund, over $1 million under management',
             'THE SINGLE BEST STUDENT AUDIENCE AT UMD AND ONE OF THE TWO BEST IN MINNESOTA (with Macalester\'s '
             '$250,000 Investment Group). UMD publicly announced the fund "breach[ing] the $1 million mark." '
             'Real money, real students, real credibility for a digital-assets conversation — and unlike '
             'Macalester, UMD has no policy barring you from talking to them. Route in via Joe Artim, Director '
             'of the Financial Markets Program, (218) 726-8642.',
             'https://lsbe.d.umn.edu/lsbe614bulldogfund'),
            ('Investment Club / Finance Club (Labovitz School of Business and Economics)',
             'Highest-fit named club. ⚠ The LSBE clubs page publishes NO descriptions, advisor names or '
             'contacts for any organization — only names and CampusGroups links. Its CampusGroups page is '
             'https://duluthumn.campusgroups.com/FinanceClub/.',
             'https://lsbe.d.umn.edu/academics/undergraduate-programs/student-experience/clubs'),
            ('Financial Planning Club · Economics Club · Entrepreneurship Club',
             'The next three best-fit LSBE organizations. No contacts published for any of them; all route '
             'through CampusGroups.',
             'https://lsbe.d.umn.edu/academics/undergraduate-programs/student-experience/clubs'),
            ('Other LSBE student organizations (listed, lower fit)',
             'Accounting Club, American Marketing Association–Duluth, Beta Gamma Sigma (Duluth Chapter), '
             'Consumer Analytics Club, LSBE Sales Club, Management Club, Management Information Systems Club, '
             'Society for Human Resource Management, Student Healthcare Management Association, Women In '
             'Business. The Consumer Analytics and MIS clubs are the closest technical adjacencies. No '
             'contacts published. LSBE general: (218) 726-7281.',
             'https://lsbe.d.umn.edu/academics/undergraduate-programs/student-experience/clubs')],
  'faculty': [('⚠⚠ Jodi Nelson — KSC Office Manager, Kirby Student Center',
               'NAMED ON THE EXTERNAL-TABLING POLICY ITSELF as the contact. She takes the $160 booking. THE '
               'NUMBER TO CALL AT UMD. Ask her: (1) book a Kirby Commons table (fall bookings open after Aug '
               '15), (2) what liability-insurance limit the Facility Use Agreement requires — it is published '
               'nowhere, and (3) confirm that an email-capture awareness table does not count as "revenue '
               'generation." Her email renders as a protected placeholder on the page.',
               'Kirby Student Center',
               'email obfuscated on page · (218) 726-7169',
               'https://kirby.d.umn.edu/policy-tabling-non-universityexternal-guest'),
              ('⚠ Kirby Student Center — reservations and general line (1120 Kirby Drive)',
               'The line printed on the rates page: "For reservation questions, contact [email] or call '
               '218.726.7163." Also the number for career-fair employer questions and for Erin Olson. TTY/TDD '
               '(800) 627-3529.',
               'Kirby Student Center',
               'email obfuscated on page · (218) 726-7163',
               'https://kirby.d.umn.edu/ksc-event-conference-services/ksc-facilities-rates'),
              ('Erin Olson — Student Organizations Coordinator (office 115 Kirby, "on the porch behind the '
               'garage")',
               'Owns the relationship with all 260+ student groups and is the only route to a Bulldog Connect '
               'directory outsiders cannot read. Use her for a SPEAKER introduction to the Investment Club or '
               'the Bulldog Fund — not for table access, which you should simply buy. Email protected on page.',
               'Kirby Student Center — Student Activities',
               'email obfuscated on page · (218) 726-7163',
               'https://kirby.d.umn.edu/student-organizations'),
              ('⚠ Joe Artim — Instructor of Finance; DIRECTOR, FINANCIAL MARKETS PROGRAM (112A LSBE)',
               'THE BEST ACADEMIC DOOR AT UMD. He runs the trading-floor/Financial Markets Program and is the '
               'natural host for a markets guest lecture and the natural bridge to the $1M+ Bulldog Fund. A '
               'guest lecture is non-commercial and touches none of the Kirby tabling restrictions. ⚠ All LSBE '
               'emails render as protected placeholders — phone, do not email.',
               'Labovitz School of Business and Economics — Accounting and Finance',
               'email obfuscated on page · (218) 726-8642',
               'https://lsbe.d.umn.edu/acc-faculty-staff'),
              ('Neil Wilmot, Ph.D. — Professor of Economics; HEAD, Department of Accounting and Finance '
               '(360D LSBE)',
               'Department head — approves guest lectures and would know whether any course touches digital '
               'assets. ⚠ NO UMD FACULTY PAGE IDENTIFIES BLOCKCHAIN, CRYPTO OR DIGITAL-ASSET RESEARCH; do not '
               'claim otherwise.',
               'Labovitz School of Business and Economics — Accounting and Finance',
               'email obfuscated on page · (218) 726-7439',
               'https://lsbe.d.umn.edu/acc-faculty-staff'),
              ('Department of Accounting and Finance — main line (LSBE 360, 1318 Kirby Drive)',
               'Department main. Kristen Lesemann, Executive Office and Administrative Specialist (360B LSBE), '
               'sits on this number and is the person who actually schedules things.',
               'Labovitz School of Business and Economics',
               'email obfuscated on page · (218) 726-7966',
               'https://lsbe.d.umn.edu/acc-faculty-staff'),
              ('Finance faculty — remaining, every one with a direct line',
               'Wei Huang, Ph.D., Assistant Professor of Finance (360H) — (218) 726-6068. Valeriya Posylnaya, '
               'Ph.D., Assistant Professor of Finance (385L) — (218) 726-8506. Raluca Stan, Ph.D., Assistant '
               'Professor of Finance (360G) — (218) 726-7454. Timothy Peterson, M.B.A., A.B.V., Instructor of '
               'Finance (385F) — (218) 726-7531. Hugo Hietapelto, C.F.P., Ch.F.C., C.L.U., Instructor of '
               'Finance (360K) — (218) 726-8412. Hietapelto and Peterson teach the practitioner-facing '
               'courses and are the likeliest to welcome an outside speaker.',
               'Labovitz School of Business and Economics — Accounting and Finance',
               'emails obfuscated · (218) 726-6068 / 8506 / 7454 / 7531 / 8412',
               'https://lsbe.d.umn.edu/acc-faculty-staff'),
              ('Brian Lukasavitz, J.D. — Teaching Assistant Professor of Business Law (385J LSBE)',
               'Business law — the person to ask about Minnesota\'s new crypto-custody statute (HF 3709, '
               'effective Aug 1, 2026) as a teaching hook. A law-and-regulation angle is the easiest '
               'non-commercial framing on any campus.',
               'Labovitz School of Business and Economics — Accounting and Finance',
               'email obfuscated on page · (218) 726-8550',
               'https://lsbe.d.umn.edu/acc-faculty-staff'),
              ('Labovitz School of Business and Economics — school main line',
               'LSBE general. Economics and Health Care Management faculty are listed separately at '
               'https://lsbe.d.umn.edu/econ-hcm-faculty-staff.',
               'Labovitz School of Business and Economics',
               'email obfuscated on page · (218) 726-7281',
               'https://lsbe.d.umn.edu/academics'),
              ('Bulldog Beginnings / Bulldog Welcome Week',
               'Welcome Week programming Aug 26–30, 2026. Email bb-kirby@d.umn.edu — one of the few UMD '
               'addresses that renders in plain text. No dedicated phone; use the Kirby line.',
               'Kirby Student Center — Bulldog Beginnings',
               'bb-kirby@d.umn.edu · no direct number published — use (218) 726-7163',
               'https://kirby.d.umn.edu/student-activities/bulldog-beginnings/bulldog-welcome-week/faqs'),
              ('Career Center — Employer Engagement team',
               'Runs the five Fall 2026 career fairs listed in events. ⚠ EMPLOYER REGISTRATION COST AND '
               'DEADLINE ARE NOT PUBLISHED for any of them, and the team\'s email renders as a protected '
               'placeholder. Call the Kirby line and ask for Career Services.',
               'UMD Career Center',
               'email obfuscated on page · no direct number published — use (218) 726-7163',
               'https://career.d.umn.edu/employers/career-fairs')],
  'courses': [('(No crypto/fintech course found)',
               'NO blockchain, cryptocurrency or fintech catalog course was confirmed at UMD. LSBE academics '
               'at https://lsbe.d.umn.edu/academics. ⚠ But UMD has something better than a course: the '
               'FINANCIAL MARKETS PROGRAM and the $1M+ Bulldog Fund, both run by Joe Artim, (218) 726-8642. '
               'Ask him whether digital assets appear anywhere in the Financial Markets curriculum and whether '
               'a guest session is possible.',
               'https://lsbe.d.umn.edu/academics')],
  'events': [('⚠ STEM-Fest Career Fair — Thu Sep 17, 2026, 10:00 a.m.',
              'CONFIRMED on UMD\'s employer page and events calendar. "Engineering, science, math, data, and '
              'computer science positions." The technical audience, three weeks into the semester. ⚠ Employer '
              'registration cost and deadline NOT PUBLISHED. Registration link on the employer page; contact '
              'is the Employer Engagement team (email protected). '
              'https://calendar.d.umn.edu/event/105337-stem-fest-career-fair',
              'https://career.d.umn.edu/employers/career-fairs'),
             ('⚠ Business Career Fair — Thu Sep 24, 2026, 10:00 a.m.',
              'CONFIRMED. "Business positions including accounting & finance, economics & health care '
              'management, management studies, marketing & sales." ⚠ THIS IS THE BEST SINGLE DAY AT UMD — the '
              'finance audience, concentrated, with employers already paying to be in the room, one week after '
              'STEM-Fest. Cost and deadline NOT PUBLISHED. '
              'https://calendar.d.umn.edu/event/105367-business-career-fair',
              'https://career.d.umn.edu/employers/career-fairs'),
             ('Other Fall 2026 career fairs UMD students attend — all dates confirmed',
              'UW-Superior Career & Internship Fair, Thu Oct 1, 2026, all majors, at UW-Superior. GOVERNMENT '
              'AND NONPROFIT CAREER FAIR, FRI OCT 23, 2026, 11:00 a.m.–3:00 p.m., AT UMN TWIN CITIES (the only '
              'Twin Cities fair date retrievable anywhere in this research — the flagship\'s own calendar is '
              'behind Handshake). Saints Health & Human Services Career Fair, Wed Nov 4, 2026, at the College '
              'of St. Scholastica. Costs and deadlines not published for any.',
              'https://career.d.umn.edu/employers/career-fairs'),
             ('Bulldog Welcome Week 2026',
              'Aug 26–30, 2026 — move-in Aug 26–27, programming from Aug 27, classes Aug 31. Required for new '
              'freshmen, cost included in the confirmation/orientation fee. ⚠ No distinct involvement fair '
              'published, and the FAQ carries a stale "Fall 2025" line. Kirby external tabling reopens after '
              'Aug 15, so a bought table during Welcome Week is possible if booked immediately.',
              'https://kirby.d.umn.edu/student-activities/bulldog-beginnings/bulldog-welcome-week/faqs')],
  'play': 'Book the $160 table and time it to the Business Career Fair. UMD has the cleanest external policy in '
          'the state after St. Cloud: a page literally titled "Policy: Tabling (Non-University/External guest)" '
          'that admits "Non-UMD, external organizations and businesses" for "commercial, awareness, or '
          'recruitment purposes" at $160 per table per day in Kirby Commons, 9–3, no sponsor required. ⚠ ACT '
          'ON THE CALENDAR: fall reservations open AFTER AUGUST 15, 2026 — three days from now — and you need '
          'a signed Facility Use Agreement plus liability insurance filed one week before the date, with a '
          'limit that is published nowhere. Call Jodi Nelson at (218) 726-7169 the moment bookings open and '
          'ask for a day adjacent to the BUSINESS CAREER FAIR on Thu Sep 24, 2026 — that is the finance '
          'audience concentrated in one building. ⚠ DESIGN THE TABLE FOR THE PROHIBITIONS: "revenue generation '
          '(sales or fundraising)" and "gambling, raffles, or drawings" are non-permissible, so run an '
          'awareness table with email capture and absolutely no giveaway drawing. The second play is academic '
          'and free: Joe Artim, (218) 726-8642, directs the Financial Markets Program and the student-led '
          'Bulldog Fund that has passed $1 million — a guest session with him reaches the best finance '
          'audience in northern Minnesota and touches none of the Kirby rules. ⚠ And do not confuse Duluth '
          'with the flagship: UMD starts Aug 31, EIGHT DAYS before the Twin Cities, and has a fall break Oct '
          '29–30 that the Twin Cities does not.',
  'gaps': ['⚠⚠ FALL EXTERNAL TABLING RESERVATIONS OPEN AFTER AUG 15, 2026 — book immediately, 2–4 weeks lead '
           'time, $160/table. ☎ Jodi Nelson (218) 726-7169. '
           'https://kirby.d.umn.edu/policy-tabling-non-universityexternal-guest',
           '⚠ The LIABILITY INSURANCE DOLLAR LIMIT required by the Facility Use Agreement is not published on '
           'any Kirby page. ☎ (218) 726-7169.',
           '⚠ Confirm that an email-capture awareness table is not "revenue generation" under the '
           'non-permissible-activities clause. ☎ (218) 726-7169.',
           'Deposit requirements and cancellation terms for non-UMD bookings — not specified on the rates page. '
           'https://kirby.d.umn.edu/ksc-event-conference-services/ksc-facilities-rates',
           'Employer registration COST and DEADLINE for STEM-Fest (Sep 17) and the Business Career Fair '
           '(Sep 24) — not published for any UMD fair. ☎ (218) 726-7163. '
           'https://career.d.umn.edu/employers/career-fairs',
           'Add/drop deadline — not printed on the official calendar; the One Stop calendar is a JavaScript '
           'filter that returns no dates. https://www.d.umn.edu/calendar/academic_cal.html',
           'Whether UMD has any blockchain or crypto student organization — Bulldog Connect did not render an '
           'org list. ☎ Erin Olson (218) 726-7163.',
           'Whether any UMD course or the Financial Markets Program curriculum touches digital assets. '
           '☎ Joe Artim (218) 726-8642.'],
  'note': '⚠ TWO UMD-SPECIFIC TRAPS. (1) UMD IS ON A DIFFERENT CALENDAR FROM THE TWIN CITIES DESPITE BEING THE '
          'SAME UNIVERSITY AND THE SAME BOARD OF REGENTS — Aug 31 vs Sep 8, and UMD has an Oct 29–30 fall '
          'break the Twin Cities does not. (2) EVERY EMAIL ADDRESS ON kirby.d.umn.edu, lsbe.d.umn.edu and '
          'career.d.umn.edu renders through a JavaScript email-protection script and is unreadable — but '
          'almost every LSBE faculty member publishes a DIRECT PHONE NUMBER. Phone, do not email. Duluth is '
          '2.5 hours north of the Twin Cities base, so this stop needs an overnight; pair it with the Sep 17 '
          'and Sep 24 career fairs to justify the drive.',
 },

 # ------------------------------------------------- 6. WINONA STATE
 {'state': 'Minnesota',
  'name': 'Winona State University',
  'city': 'Winona, MN',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 3,
  'start': 'Mon Aug 24, 2026 — earliest wave, with Mankato and St. Cloud State.',
  'adddrop': '⚠ Fri Aug 28, 2026 — last day to add courses and to drop with a full refund. ONE OF ONLY FIVE '
             'CLEAN ADD/DROP DATES PUBLISHED ANYWHERE IN THIS STATE FILE, and the earliest of them.',
  'fallbreak': 'Student break day (no classes) Wed Nov 25, 2026 — Winona gives students the Wednesday before '
               'Thanksgiving, which most Minnesota campuses do not. No October fall break.',
  'thanksgiving': 'Thu–Fri Nov 26–27, 2026',
  'lastclass': '⚠ PARTIAL — the official PDF prints "last day of classes Thursday, December 10, 2026" AND '
               '"finals Mon–Thu December 7–10, 2026," which overlap. That is how the university published it. '
               'The practical read is that regular instruction ends around FRI DEC 4 and Dec 7–10 is finals. '
               'The usable Winona window closes in the first week of December.',
  'finals': 'Mon–Thu Dec 7–10, 2026. Commencement Fri Dec 11, 2026.',
  'cal_url': 'https://www.winona.edu/wp-content/uploads/2026/05/Fall-2026-Academic-Calendar.pdf',
  'cal_status': 'CONFIRMED — the official Fall 2026 Academic Calendar PDF, REVISED 04/21/2026 (a recent '
                'revision date, which is reassuring). Calendar hub at '
                'https://www.winona.edu/about/series/academic-calendar/. The only ambiguity is the overlapping '
                'last-class / finals rows noted above.',
  'fair': 'WSU CLUB FAIRS — multiple per year in the WSU Courtyard, and participation is MANDATORY for clubs',
  'fair_date': '⚠⚠ THE PAGE IS STALE — IT STILL SHOWS THE 2023 SCHEDULE. The "Promote a Club" page lists '
               'Welcome Weekend Aug 18; I LOVE WSU Day Sep 6; All-University Wellness Fair Sep 26, 1–4 p.m., '
               'register by Fri Sep 22; Homecoming Oct 13, 11 a.m.–1:30 p.m., register by Mon Oct 9. THOSE ARE '
               '2023 DATES. DO NOT PUT THEM IN A PLAN. // WHAT IS RELIABLE IS THE RECURRING PATTERN: FOUR '
               'FAIRS A YEAR — Welcome Weekend (late August), an early-September campus day, a late-September '
               'all-university wellness fair, and Homecoming (mid-October) — ALL IN THE WSU COURTYARD, all '
               'with registration roughly four days prior via WARRIORSPACE. // ⚠ The Welcome Week student page '
               'is WORSE: https://www.winona.edu/welcomeweek/students.asp still displays the "2018 '
               'All-University New Student Welcome and Picnic." The current schedule sits behind a STARID '
               'LOGIN ("Personalized Student Orientation Week Schedule"). The events calendar '
               'https://www.winona.edu/about/events/list/ returned HTTP 403 to research tooling. FALL 2026 '
               'FAIR DATES WILL NOT POST TO A PUBLIC PAGE IN USABLE FORM — GET THEM BY PHONE from Alex '
               'Thompson, (507) 457-5584.',
  'fair_outside': '⚠ NO for the club fairs themselves — they are a club-compliance mechanism, not a vendor '
                  'market. Verbatim: "ALL ACTIVE AND REGISTERED CLUBS MUST PARTICIPATE IN AT LEAST ONE FAIR TO '
                  'MAINTAIN THEIR ACTIVE STATUS," and "Each club/organization is allowed only one table, '
                  'although multiple clubs/organizations can share a table if desired." Registration is '
                  'through WarriorSpace, which requires a StarID. THE OUTSIDE ROUTE IS SEPARATE AND '
                  'DISCRETIONARY: "Third-party organizations requesting event or meeting space accommodations '
                  'SHOULD DISCUSS WITH THE STUDENT UNION & ACTIVITIES OFFICE." ☎ (507) 457-5310.',
  'fair_cost': '⚠ NO THIRD-PARTY RATE CARD IS PUBLISHED ANYWHERE AT WINONA STATE. The only fee language found '
               'is in the political-activity context: "Fees will be charged as posted for each space used by '
               'the third party" — and the posting is not public. This is the single biggest unknown at this '
               'campus. ☎ Phillip Steffes, Assistant Director – Event Services, (507) 457-5313.',
  'fair_deadline': 'Club fair registration runs roughly four days prior via WarriorSpace (2023 pattern: '
                   'register by the Friday before a Tuesday fair). For third-party space there is no published '
                   'deadline — a Minnesota State facility use agreement must be executed before occupancy, '
                   'which is the real lead-time driver.',
  'fair_url': 'https://www.winona.edu/student-life/clubs/student-senate/manage-a-club/promote-a-club/',
  'policy': 'Kryzsko Commons Student Union Policies (reservations, fundraising, third-party postings, food '
            'exclusivity) + Minnesota State System Procedure 6.7.2 and Board Policy 3.1 (see the Mankato '
            'policy_key for the system layer)',
  'policy_url': 'https://www.winona.edu/policies-student-conduct/student-union-policies/',
  'policy_key': "⚠ WINONA STATE'S REGIME IS 'COME AND DISCUSS IT WITH US' — DISCRETIONARY, UNDOCUMENTED, AND "
                "THEREFORE ENTIRELY DEPENDENT ON THE PHONE CALL. Nothing is priced, nothing is quantified, and "
                "there is nothing in the written rule to quote in your favour. Rated 3 because a route exists "
                "and is named; it is not a 4 because nothing about it is documented. "
                "KRYZSKO COMMONS STUDENT UNION POLICIES, VERBATIM: 'THIRD-PARTY ORGANIZATIONS REQUESTING EVENT "
                "OR MEETING SPACE ACCOMMODATIONS SHOULD DISCUSS WITH THE STUDENT UNION & ACTIVITIES OFFICE.' "
                "'A MINNESOTA STATE FACILITY USE AGREEMENT IS REQUIRED FOR ALL THIRD PARTY RESERVATIONS OF "
                "KRYZSKO COMMONS STUDENT UNION SPACES. INSURANCE PROVISIONS AS OUTLINED WITHIN THE FACILITY "
                "USE AGREEMENT ARE ALSO REQUIRED.' 'FEES WILL BE CHARGED AS POSTED FOR EACH SPACE USED BY THE "
                "THIRD PARTY' (stated in the political-activity context; the posting is not public). "
                "'A Minnesota State facility use agreement MAY BE REQUIRED pending the nature of the room "
                "usage and type of event. If required, insurance provisions will be outlined.' "
                "FUNDRAISING AND SOLICITATION, VERBATIM: 'FUNDRAISING AND SOLICITATIONS BY RECOGNIZED STUDENT "
                "ORGANIZATIONS AND ACADEMIC GROUPS IN KRYZSKO COMMONS STUDENT UNION AND ACROSS CAMPUS ARE "
                "SUBJECT TO A VARIETY OF REGULATIONS. ALL USES OF THE FACILITY FOR FUNDRAISING REQUIRE A "
                "RESERVATION. IT IS NOT PERMITTED IN THE DINING HALL, FOOD COURT, OUTSIDE THE BOOKSTORE OR "
                "OTHER COMMON AREAS WITHOUT PERMISSION FROM THE STUDENT UNION DIRECTOR.' ⚠ NOTE THE SUBJECT: "
                "that sentence governs RSOs and academic groups. It does not, on its face, address an outside "
                "for-profit at all — which is precisely why the third-party sentence sends you to the office "
                "instead. THE 'STUDENT UNION DIRECTOR' NAMED IN THAT CLAUSE IS GEORGE MICALONE, (507) "
                "457-5312. START THERE. "
                "THIRD-PARTY POSTINGS, VERBATIM: 'ONLY ONE BOARD IS AVAILABLE FOR THIRD PARTY POSTINGS (OFF "
                "CAMPUS RENTAL FLYERS, COMMUNITY EVENTS, ETC.) AND ONLY ONE FLYER WILL BE ACCEPTED.' One board, "
                "one flyer — that is the entire passive-advertising allowance for an outsider at Winona State. "
                "FOOD EXCLUSIVITY, VERBATIM: 'CHARTWELLS DINING SERVICES HAS EXCLUSIVE RIGHTS TO PROVIDE ALL "
                "FOOD SERVICE AND CATERING IN KRYZSKO COMMONS STUDENT UNION. UPON MUTUAL WRITTEN AGREEMENT "
                "WITH MINNESOTA STATE, CHARTWELLS MAY RELINQUISH ITS EXCLUSIVE RIGHTS FOR A SPECIFIC, "
                "PRE-IDENTIFIED EVENT.' Outside food only 'when the total amount is under $100 and the "
                "audience is WSU students for internal use only. Advertised events are considered catering and "
                "must go through Chartwells.' Put nothing edible on the table. "
                "CLUB FAIRS, VERBATIM: 'ALL ACTIVE AND REGISTERED CLUBS MUST PARTICIPATE IN AT LEAST ONE FAIR "
                "TO MAINTAIN THEIR ACTIVE STATUS.' 'EACH CLUB/ORGANIZATION IS ALLOWED ONLY ONE TABLE, ALTHOUGH "
                "MULTIPLE CLUBS/ORGANIZATIONS CAN SHARE A TABLE IF DESIRED.' Organizations may 'reserve a "
                "table in the Kryzsko Commons Student Union or the Courtyard/Gazebo area' using the online EMS "
                "system; indoor tabling requires compliance with all student union policies. NOTE THE "
                "TABLE-SHARING SENTENCE — it is the only published mechanism by which a second party could "
                "legitimately occupy a club's table, and nothing at Winona forbids it. "
                "⚠ WHAT IS *NOT* PUBLISHED AT WINONA STATE, AND EVERY ONE OF THESE IS A REAL GAP: NO "
                "third-party rate card. NO insurance dollar limit. NO deposit terms. NO cancellation schedule. "
                "NO ANTI-FRONTING CLAUSE. NO explicit ban on commercial solicitation. NO language reaching "
                "payment credentials or on-site contract signing. The absence of a fronting rule matters: "
                "unlike UMN Twin Cities and St. Cloud State, nothing at Winona prohibits a club from sharing "
                "its table with, or reserving space alongside, an outside entity. "
                "SYSTEM LAYER: Minnesota State System Procedure 6.7.2 supplies the written-agreement and "
                "additional-insured requirements and the market-rate cost-recovery mandate (quoted in full in "
                "the Mankato policy_key). Board Policy 3.1 protects STUDENT expression only. "
                "PUBLIC-FORUM POSTURE: Winona State is public, so First Amendment forum doctrine applies to "
                "its outdoor spaces — but Minnesota has NO campus free-speech statute (see the U of M Twin "
                "Cities policy_key). The Courtyard and Gazebo are the outdoor spaces named in policy.",
  'sponsor_required': '⚠ UNCLEAR — AND THAT AMBIGUITY IS AN OPPORTUNITY. The written rule sends third parties '
                      'to the Student Union & Activities Office ("should discuss with"), which is neither a '
                      'sponsorship requirement nor a refusal. Meanwhile the club-fair rule expressly allows '
                      'table sharing — "multiple clubs/organizations can share a table if desired" — and '
                      'WINONA HAS NO ANTI-FRONTING CLAUSE, unlike UMN Twin Cities and St. Cloud State. Two '
                      'live routes therefore exist: (a) a third-party facility use agreement negotiated with '
                      'George Micalone, (507) 457-5312, or (b) a Financial Management Association co-presence '
                      'via advisor Elizabeth Schwanke. Try (a) first; it is cleaner and does not put students '
                      'at risk.',
  'clubs': [('⚠ FINANCIAL MANAGEMENT ASSOCIATION (FMA) — THE ONLY FMA CHAPTER IN THIS ENTIRE STATE FILE',
             'Academic/Business category. Stated purpose, verbatim: "foster the next generation of financial '
             'professionals, build their network." This is the single highest-fit club at Winona State and one '
             'of the best in Minnesota. ADVISORS LISTED: Elizabeth Schwanke, Lawrence Schrenk, Yuqian Wang. '
             'Instagram @fma.wsu. ⚠ Student officer names ARE printed on the WSU clubs page but rosters rotate '
             'annually — REACH THE ADVISORS, NOT THE STUDENTS. No phone numbers are published for anyone on '
             'the clubs page.',
             'https://www.winona.edu/student-life/clubs/student-clubs/'),
            ('⚠ Elizabeth Schwanke advises essentially EVERY business club at WSU',
             'THE HIGHEST-LEVERAGE SINGLE FACT ABOUT WINONA STATE. Schwanke is listed as an advisor to the '
             'Financial Management Association, the Accounting Association, the Case Competition Club, the '
             'American Marketing Association AND the Sports Business Association. ONE CONVERSATION WITH HER '
             'REACHES ALL FIVE. ⚠ Her phone number is NOT published — the WSU campus directory requires '
             'sign-in to reveal individual contacts. Go through the College of Business or the Finance '
             'department line, (507) 457-5600.',
             'https://www.winona.edu/student-life/clubs/student-clubs/'),
            ('Accounting Association · Case Competition Club',
             'Accounting Association: connections with local employers and accounting firms; advisors '
             'Elizabeth Schwanke and YoungJin Kim. Case Competition Club: "strategic thinking, consulting, '
             'finance case competitions"; advisors Elizabeth Schwanke, Malgorzata Plecka and others. Both are '
             'strong secondary audiences.',
             'https://www.winona.edu/student-life/clubs/student-clubs/'),
            ('Computer Science Club · Women in Computer Science (WiCS)',
             'CS Club: "focuses on solving logic problems, expanding our knowledge of technology"; ADVISOR '
             'ERIC WRIGHT, who advises both. Site cs.winona.edu. WiCS Instagram @winonawics. The technical '
             'audience at Winona; Wright is a single point of contact for both clubs.',
             'https://www.winona.edu/scienceandeng/studentorgs.asp'),
            ('⚠ NO BLOCKCHAIN / CRYPTO / WEB3 CLUB AT WINONA STATE',
             'None found on the student clubs page, the science and engineering org page, or the Student '
             'Activities & Leadership list. The directory system is WarriorSpace, which requires a StarID. '
             'Other directory URLs: https://www.winona.edu/sal/clubs.asp and '
             'https://www.winona.edu/equity/clubs.asp.',
             'https://www.winona.edu/sal/clubs.asp')],
  'faculty': [('⚠⚠ George Micalone — DIRECTOR OF THE STUDENT UNION & ACTIVITIES',
               'START HERE. He is the "Student Union Director" whose permission the fundraising policy names '
               'by title, and his office is the one the third-party clause sends you to. Ask him the four '
               'things Winona publishes nowhere: (1) will you execute a Minnesota State facility use agreement '
               'for an outside information table, (2) what is the posted fee, (3) what insurance limit does '
               'the agreement require, and (4) what are the actual Fall 2026 Courtyard fair dates.',
               'Student Union & Activities (Kryzsko Commons 117)',
               'George.micalone@winona.edu · (507) 457-5312',
               'https://www2.winona.edu/studentunion/contact.asp'),
              ('⚠ Phillip Steffes — Assistant Director, Event Services',
               'HE BOOKS THE SPACE. The operational counterpart to Micalone and the person who will actually '
               'quote a fee for Courtyard or Kryzsko Commons space. Also the departmental main line.',
               'Student Union & Activities',
               'phillip.steffes@winona.edu · (507) 457-5313',
               'https://www2.winona.edu/studentunion/contact.asp'),
              ('⚠ Alex Thompson — Assistant Director of Student Activities',
               'OWNS THE CLUB FAIRS — the only person who can supply the Fall 2026 Courtyard fair dates, since '
               'the public page still shows 2023 and the current schedule sits behind a StarID login. ⚠ HER '
               'EMAIL IS NOT PUBLISHED on the contact page; the phone number is the only route.',
               'Student Union & Activities',
               'email not published — look up here · (507) 457-5584',
               'https://www2.winona.edu/studentunion/contact.asp'),
              ('James McGuire — Associate Director, Operations',
               'Building operations for Kryzsko Commons; third call in the department.',
               'Student Union & Activities',
               'james.mcguire@winona.edu · (507) 457-5314',
               'https://www2.winona.edu/studentunion/contact.asp'),
              ('Student Union and Activities — department main line (Kryzsko Commons 117)',
               'The departmental number from the campus directory. Ten staff are listed in the directory '
               'record (Steffes, Hovey, Barnes, Johnson, McDowell, Sims, Micalone, Thompson, Lupo, Bronk) but '
               '⚠ THE DIRECTORY DOES NOT PUBLISH TITLES OR INDIVIDUAL NUMBERS WITHOUT SIGN-IN — the four '
               'direct lines above came from the separate Student Union contact page.',
               'Student Union & Activities',
               'studentunion@winona.edu · (507) 457-5310',
               'https://w3.winona.edu/CampusDirectory/Home/DepartmentDetails/113M'),
              ('Student Senate',
               'Recognises clubs and owns the "Promote a Club" guidance that carries the stale fair schedule. '
               'Also the route to the ASO Director (aso@winona.edu, no number published).',
               'Student Senate',
               'studentsenate@winona.edu · (507) 457-5316',
               'https://www.winona.edu/student-life/clubs/student-senate/manage-a-club/promote-a-club/'),
              ('⚠ Finance Department (Somsen Hall 319) — and the sign-in wall behind it',
               'DEPARTMENT MAIN LINE. Faculty listed in the campus directory: Yuqian Wang, Carolyn Sinniger, '
               'Lawrence Schrenk, Robert Wolf, Randall Skalberg. ⚠ THE DIRECTORY REQUIRES SIGN-IN TO REVEAL '
               'INDIVIDUAL TITLES, EMAILS AND DIRECT PHONE NUMBERS — the page says "Sign in to see additional '
               'contact information." NO INDIVIDUAL NUMBER IS PUBLICLY AVAILABLE — look up here, or call the '
               'department line and ask for Schrenk or Wang, both of whom advise the FMA. NO WINONA FACULTY '
               'MEMBER COULD BE CONFIRMED AS WORKING ON BLOCKCHAIN, CRYPTO OR FINTECH.',
               'College of Business — Finance',
               'no individual numbers published — look up here · department (507) 457-5600',
               'https://w3.winona.edu/CampusDirectory/Home/DepartmentDetails/052M'),
              ('Elizabeth Schwanke — advisor to five business clubs',
               '⚠ NOT CONFIRMABLE BY DIRECT LINE. She is named as an advisor to the FMA, Accounting '
               'Association, Case Competition Club, AMA and Sports Business Association on the WSU clubs page, '
               'but NO email or phone is published for her anywhere and the campus directory hides individual '
               'contacts behind sign-in. Reach her through the College of Business directory or the Finance '
               'department line. DO NOT GUESS AN ADDRESS.',
               'College of Business',
               'no number published — look up here; use (507) 457-5600',
               'https://w3.winona.edu/CampusDirectory/Home/DepartmentDetails/083M'),
              ('Eric Wright — advisor, Computer Science Club and Women in Computer Science',
               'Single point of contact for both technical clubs at Winona. ⚠ No email or phone published on '
               'the clubs page; the CS department site is cs.winona.edu. Look up here.',
               'College of Science and Engineering — Computer Science',
               'no number published — look up here',
               'https://www.winona.edu/scienceandeng/studentorgs.asp'),
              ('WSU Tech Support',
               'Printed on the Welcome Week page as the route to StarID access for the "Personalized Student '
               'Orientation Week Schedule" — i.e. the login wall that hides the current Welcome Week calendar. '
               'Carried across because it is the only published number on that page.',
               'Information Technology',
               '(507) 457-5240',
               'https://www.winona.edu/welcomeweek/students.asp')],
  'courses': [('(No crypto/fintech course found)',
               'NO blockchain, cryptocurrency or fintech course was confirmed at Winona State. Catalog at '
               'https://catalog.winona.edu/ and the College of Business at '
               'https://www.winona.edu/academics/colleges/business/. Ask the Finance department, '
               '(507) 457-5600 — and note that the FMA chapter itself is the strongest signal of a '
               'finance-professional pipeline on this campus, course or no course.',
               'https://www.winona.edu/academics/colleges/business/finance-department/faculty/')],
  'events': [('⚠ WSU Courtyard club fairs — FOUR PER YEAR, DATES STALE ON THE PUBLIC PAGE',
              'Recurring pattern: Welcome Weekend (late August), an early-September campus day ("I LOVE WSU '
              'Day"), an All-University Wellness Fair (late September, historically 1–4 p.m. with registration '
              'four days prior), and HOMECOMING (mid-October, historically 11 a.m.–1:30 p.m.). All in the WSU '
              'Courtyard, all registered through WarriorSpace. ⚠ THE PAGE SHOWS 2023 DATES — Aug 18, Sep 6, '
              'Sep 26, Oct 13 — DO NOT USE THEM. ☎ Alex Thompson (507) 457-5584 for Fall 2026.',
              'https://www.winona.edu/student-life/clubs/student-senate/manage-a-club/promote-a-club/'),
             ('Warrior Game Day Experience',
              'Pre-football-game events at which clubs table; groups participating are entered into a drawing '
              'for $50 in club funding, season-long participants for $250. Requires at least three days\' '
              'advance notice. Relevant as a high-traffic recurring slot that a club ally could share a table '
              'at — note Winona has no anti-fronting rule.',
              'https://www.winona.edu/student-life/clubs/student-senate/manage-a-club/promote-a-club/'),
             ('⚠ Winona State events calendar — HTTP 403',
              'https://www.winona.edu/about/events/list/ returned HTTP 403 to research tooling and could not '
              'be read. The Welcome Week page shows 2018 content and the current schedule is behind a StarID '
              'login. NO FALL 2026 EVENT DATES COULD BE CONFIRMED FOR WINONA STATE BEYOND THE ACADEMIC '
              'CALENDAR. This campus must be planned by phone.',
              'https://www.winona.edu/welcomeweek/'),
             ('(No hackathon or blockchain event)',
              'NO hackathon, blockchain conference, research centre or crypto legislative activity was found '
              'connected to Winona State.',
              'https://www.winona.edu/about/events/category/student-life/clubs-activities/')],
  'play': 'Winona is a two-call campus and both calls are to the same office. Nothing here is priced or '
          'documented — no third-party rate card, no insurance limit, no deposit terms, no cancellation '
          'schedule — so the entire outcome depends on George Micalone, Director of the Student Union & '
          'Activities, (507) 457-5312. He is the "Student Union Director" the fundraising policy names, and '
          'the third-party clause ("should discuss with the Student Union & Activities Office") sends you '
          'straight to him. Ask for a Minnesota State facility use agreement for a Courtyard or Kryzsko '
          'Commons information table and get the fee and insurance limit in writing. Second call, same day: '
          'Alex Thompson, (507) 457-5584, for the Fall 2026 Courtyard fair dates — the public page still shows '
          '2023, the Welcome Week page still shows 2018, the events calendar 403s, and the real schedule is '
          'behind a StarID login, so the phone is the ONLY route. ⚠ The prize at Winona is the FINANCIAL '
          'MANAGEMENT ASSOCIATION — the only FMA chapter in this entire ten-campus set — and the fact that '
          'ELIZABETH SCHWANKE advises the FMA, the Accounting Association, the Case Competition Club, the AMA '
          'and the Sports Business Association, so one conversation reaches five clubs. Her number is not '
          'published; go through the Finance department at (507) 457-5600. Winona also has no anti-fronting '
          'rule and expressly permits table sharing, so a club co-presence is legitimate here in a way it is '
          'not at the flagship or St. Cloud. Two hours southeast of the Twin Cities — pair it with nothing, it '
          'is its own day.',
  'gaps': ['⚠⚠ NO THIRD-PARTY RATE CARD, NO INSURANCE DOLLAR LIMIT, NO DEPOSIT TERMS AND NO CANCELLATION '
           'SCHEDULE ARE PUBLISHED ANYWHERE AT WINONA STATE. ☎ George Micalone (507) 457-5312 / Phillip '
           'Steffes (507) 457-5313. https://www.winona.edu/policies-student-conduct/student-union-policies/',
           '⚠ FALL 2026 CLUB FAIR DATES — the "Promote a Club" page still shows the 2023 schedule and the '
           'Welcome Week page shows 2018 content; the current schedule is behind a StarID login. ☎ Alex '
           'Thompson (507) 457-5584.',
           '⚠ https://www.winona.edu/about/events/list/ returned HTTP 403 — no Winona State event calendar '
           'could be read at all.',
           'A direct phone number or email for ELIZABETH SCHWANKE, who advises five business clubs including '
           'the FMA — the campus directory hides individual contacts behind sign-in. ☎ (507) 457-5600. '
           'https://w3.winona.edu/CampusDirectory/Home/DepartmentDetails/083M',
           'Individual titles, emails and direct numbers for Finance faculty (Wang, Sinniger, Schrenk, Wolf, '
           'Skalberg) — "Sign in to see additional contact information." '
           'https://w3.winona.edu/CampusDirectory/Home/DepartmentDetails/052M',
           'An email address for Alex Thompson — not published on the Student Union contact page.',
           'Contact details for Eric Wright, advisor to both computer science clubs — none published.',
           'Whether the overlapping "last day of classes Dec 10" / "finals Dec 7–10" rows mean instruction '
           'actually ends around Dec 4. https://www.winona.edu/wp-content/uploads/2026/05/Fall-2026-Academic-Calendar.pdf',
           'Whether any Winona State course touches blockchain or fintech. https://catalog.winona.edu/'],
  'note': '⚠ WINONA STATE IS THE MOST STALE-PAGED CAMPUS IN THIS FILE. The club-fair page shows 2023, the '
          'Welcome Week page shows 2018, the events calendar returns HTTP 403, and the campus directory hides '
          'every individual\'s contact details behind a sign-in wall. Almost nothing about Fall 2026 at Winona '
          'can be learned from the web. The compensating fact is that the Student Union contact page publishes '
          'four direct lines — Micalone, McGuire, Steffes, Thompson — and those four people know everything '
          'the website does not.',
 },

 # ------------------------------------------------- 7. METROPOLITAN STATE
 {'state': 'Minnesota',
  'name': 'Metropolitan State University',
  'city': 'St. Paul, MN',
  'type': 'Public',
  'tier': 'C — Opportunistic',
  'access': 3,
  'start': '⚠⚠ Sat Aug 22, 2026 — THE EARLIEST START IN MINNESOTA, AND IT IS A SATURDAY. No other campus in '
           'the state begins on a weekend. That single fact tells you what Metro State is: working adults, '
           'evenings and weekends.',
  'adddrop': 'Fri Aug 28, 2026 — "last date to drop with a refund deadline" for initial courses. ⚠ Because '
             'Metro State runs two concurrent 8-week sessions alongside a full session, drop dates differ by '
             'session; this is the first-session/full-session date.',
  'fallbreak': '⚠ NO FALL BREAK. The only closures are Labor Day Sep 5–7, 2026 (no classes, buildings closed) '
               'and Veterans Day Wed Nov 11, 2026 (no classes, buildings closed). The Veterans Day closure is '
               'distinctive — most Minnesota campuses stay open.',
  'thanksgiving': 'Nov 25–29, 2026 — no evening classes Nov 25; FULL CLOSURE Nov 26–29.',
  'lastclass': '⚠ Sun Dec 13, 2026 — "Fall 2026 second session and full session semester courses end." THE '
               'SEMESTER ENDS ON A SUNDAY. Degree conferral Dec 13; grades due Wed Dec 16 at 11:59 p.m.; '
               'holiday closure Dec 21–31.',
  'finals': 'No separate finals week is published — finals sit inside the session end dates. ⚠ SESSION '
            'STRUCTURE IS THE THING TO UNDERSTAND: First Session Aug 22 – Oct 12, 2026; Second Session Oct 14 '
            '– Dec 13, 2026; Full Session Aug 22 – Dec 13, 2026. Students churn in and out mid-term, so the '
            'population on any given week is not stable.',
  'cal_url': 'https://www.metrostate.edu/academics/calendar/fall-2026',
  'cal_status': 'CONFIRMED — the official Fall 2026 calendar page. Hub at '
                'https://www.metrostate.edu/academics/calendar. This is the one part of Metro State\'s web '
                'presence that is complete and current.',
  'fair': '⚠ NONE FOUND — no involvement fair, org fair, welcome week or tabling event exists on any '
          'retrievable Metro State page',
  'fair_date': '⚠⚠ NONE. No involvement fair, organization fair, welcome week or student tabling event appears '
               'anywhere on metrostate.edu. THIS IS A REAL ABSENCE, NOT A SEARCH FAILURE — the university\'s '
               'student-life web presence is minimal: /student-life and /students/support/student-life BOTH '
               'RETURN 404, and the Student Life and Leadership Development office has NO retrievable web page '
               'at all. Its only public presence found anywhere was a Facebook page '
               '(https://www.facebook.com/MetroStateSLLD/) and a CampusLabs contact stub for the student '
               'association (https://metrostate.campuslabs.com/engage/organization/msusa/contact, '
               'JavaScript-rendered).',
  'fair_cost': 'N/A — no fair exists. No outside-vendor rate card of any kind is published for Metro State.',
  'fair_outside': '⚠ NO ANSWER AVAILABLE. Nothing is published about outside organizations, tabling, or fairs '
                  'at Metro State. ☎ 651.793.1300, option 5 (Gateway Student Services) is the only route to '
                  'an answer.',
  'fair_deadline': 'N/A — nothing published.',
  'fair_url': 'https://www.metrostate.edu/academics/calendar/fall-2026',
  'policy': '⚠ NOT RETRIEVED — no Metro State solicitation, tabling, facilities-use or outside-vendor policy '
            'could be found. Governing layer defaults to Minnesota State System Procedure 6.7.2 (eff. '
            '7/28/1996, last revised 1/22/2026) and Board Policy 3.1 (implementation 1/18/1995, last reviewed '
            '3/18/2026).',
  'policy_url': 'https://www.minnstate.edu/board/procedure/607p2.html',
  'policy_key': "⚠⚠ PROVISIONAL RATING — READ THIS BEFORE ACTING ON THE NUMBER 3. NO METRO STATE SOLICITATION, "
                "TABLING, FACILITIES-USE OR OUTSIDE-VENDOR POLICY COULD BE FOUND. Searches across "
                "metrostate.edu and general web searches returned nothing specific to this institution. This "
                "campus is rated 3 PER THE SCHEMA RULE FOR AN UNRETRIEVABLE GOVERNING POLICY — not because a "
                "gated route was found and documented. It could turn out to be a 5 (an unpublished rate card) "
                "or a 1 (a flat internal ban). DO NOT REPRESENT IT AS A KNOWN QUANTITY. THE NAMED GAP: get "
                "the Metro State facilities-use and solicitation policy by phone, 651.793.1300 option 5. "
                "WHAT DOES GOVERN, BY DEFAULT — THE MINNESOTA STATE SYSTEM LAYER (full text quoted in the "
                "Mankato policy_key, which is the anchor for this system note): "
                "MINNESOTA STATE SYSTEM PROCEDURE 6.7.2, 'Use of College and University Facilities (College or "
                "University as Lessor),' EFFECTIVE JULY 28, 1996, LAST REVISED JANUARY 22, 2026 "
                "(https://www.minnstate.edu/board/procedure/607p2.html). VERBATIM: 'USERS OF FACILITIES MUST "
                "HAVE A FULLY EXECUTED, WRITTEN AGREEMENT BEFORE OCCUPYING OR USING A COLLEGE OR UNIVERSITY "
                "FACILITY.' 'USERS OF A COLLEGE OR UNIVERSITY FACILITY SHALL PROVIDE EVIDENCE OF ADEQUATE "
                "LIABILITY INSURANCE COVERAGE... NAMING THE STATE OF MINNESOTA... AS AN ADDITIONAL INSURED, "
                "PRIOR TO USING OR OCCUPYING.' Institutions must 'CHARGE A USER A REASONABLE AMOUNT WHEN "
                "LEASING THEIR FACILITIES THAT COVERS ALL COSTS TYPICALLY INCLUDED IN A STANDARD MARKET LEASE' "
                "— market-rate cost recovery is mandatory. Every agreement must contain 'A CANCELLATION "
                "CLAUSE, WHICH CAN BE INVOKED AT THE COLLEGE'S OR UNIVERSITY'S SOLE AND ABSOLUTE DISCRETION.' "
                "MINNESOTA STATE BOARD POLICY 3.1, 'Student Rights and Responsibilities' "
                "(https://www.minnstate.edu/board/policy/301.html) protects STUDENT expression and assembly "
                "only — 'Individual students and student organizations shall be free to... express opinions "
                "publicly and privately'; 'Students shall have the right to assemble, to select speakers, and "
                "to discuss issues of their choice.' IT CONFERS NOTHING ON AN OUTSIDE FOR-PROFIT ENTITY. "
                "Metro State is PUBLIC, so First Amendment forum doctrine applies to any traditional public "
                "forum it maintains — but Minnesota has NO campus free-speech statute to cite (see the U of M "
                "Twin Cities policy_key), and Metro State's three scattered urban locations do not obviously "
                "contain a traditional quad-style forum at all. "
                "NO ANTI-FRONTING LANGUAGE, NO INSURANCE DOLLAR LIMIT, NO DEPOSIT TERMS, NO PAYMENT-CREDENTIAL "
                "OR CONTRACT-SIGNING LANGUAGE COULD BE FOUND — because no campus policy could be found at all.",
  'sponsor_required': '⚠ UNKNOWN — no policy could be retrieved. Under the Minnesota State system default, a '
                      'fully executed written Facilities Agreement and liability insurance naming the State of '
                      'Minnesota as additional insured are required before occupancy, and the institution must '
                      'charge market rate. Whether Metro State additionally requires a student-organization '
                      'sponsor is not published anywhere. ☎ 651.793.1300, option 5.',
  'clubs': [('⚠ NO CLUB DIRECTORY COULD BE RETRIEVED',
             'No finance, investment, economics, computer science, entrepreneurship or blockchain organization '
             'could be confirmed at Metro State. The Metropolitan State University Student Association appears '
             'on CampusLabs but the page is JAVASCRIPT-RENDERED. A Hmong Student Organization has a Facebook '
             'presence. This is the thinnest club picture of any campus in this file.',
             'https://metrostate.campuslabs.com/engage/organization/msusa/contact'),
            ('⚠ Student Life and Leadership Development — NO WEB PAGE EXISTS',
             'The office that would own student organizations has no retrievable page on metrostate.edu. '
             '/student-life and /students/support/student-life both return 404. Its only public presence found '
             'was a Facebook page. Record this: it is why no club information exists for this campus.',
             'https://www.facebook.com/MetroStateSLLD/')],
  'faculty': [('⚠ Metropolitan State University — MAIN LINE (700 East Seventh Street, Saint Paul)',
               'THIS IS THE ONLY NUMBER THERE IS. No named individual, no direct line and no departmental '
               'number could be confirmed for Student Life, Facilities, Events, Scheduling or the College of '
               'Management. The thinnest contact picture of any campus in this file. Everything must start '
               'here.',
               'University',
               '651.793.1300 (main line)',
               'https://www.metrostate.edu/about/contact'),
              ('⚠ Gateway Student Services — 651.793.1300, select option 5',
               'Described by the university as "the first stop for all students\' questions, including '
               'financial aid, registration, finding your advisor, locating university services, paying bills '
               'other than tuition, and more." Since no facilities or student-life office is reachable '
               'directly, THIS IS THE PRACTICAL ROUTE TO A HUMAN who can find the solicitation policy and say '
               'whether outside tabling exists at all.',
               'Gateway Student Services',
               '651.793.1300, option 5 (main line, menu option)',
               'https://www.metrostate.edu/about/contact'),
              ('Admissions',
               'Published direct number; carried across because so little else is. admissions@metrostate.edu.',
               'Admissions',
               'admissions@metrostate.edu · 651.793.1302',
               'https://www.metrostate.edu/about/contact'),
              ('(Faculty and staff directory)',
               'NOT CONFIRMED — no Metro State faculty member in finance, economics, computer science or any '
               'adjacent field could be confirmed on a live page, and no College of Management faculty '
               'directory was retrievable. A faculty and staff directory is said to exist at the URL. Look up '
               'here. No number published for any individual.',
               'Metropolitan State University',
               'no number published — look up here; use 651.793.1300',
               'https://www.metrostate.edu/about/directory')],
  'courses': [('(No crypto/fintech course found)',
               'NO blockchain, cryptocurrency or fintech course was confirmed at Metro State. No course '
               'catalog search returned anything for this institution.',
               'https://www.metrostate.edu/academics/calendar/fall-2026')],
  'events': [('⚠ NONE FOUND',
              'No involvement fair, welcome week, career fair, speaker series, hackathon, blockchain event or '
              'research centre could be found for Metropolitan State University. The academic calendar is the '
              'only complete piece of Metro State information that could be retrieved.',
              'https://www.metrostate.edu/academics/calendar/fall-2026')],
  'play': '⚠ SKIP THIS CAMPUS AS A TABLING STOP — and the reason is AUDIENCE, not policy. Metro State is not a '
          'traditional undergraduate campus and it behaves like nothing else in this file: fall classes begin '
          'on a SATURDAY (Aug 22), the term is built as two concurrent 8-week sessions so the population '
          'churns mid-semester, the semester ends on a SUNDAY (Dec 13), and the university is spread across '
          'three separate urban locations — Saint Paul (700 E 7th St), Minneapolis (1300 Harmon Pl) and the '
          'Public Safety and Police Science Center in Brooklyn Park. There is no single quad where the student '
          'body concentrates. No welcome week, no involvement fair and no organization fair exists on any page, '
          'the Student Life and Leadership Development office HAS NO WEBSITE AT ALL, and /student-life 404s. '
          'The adult student arrives at 6 p.m., goes to class and leaves — the foot traffic a table depends on '
          'is not there. THAT SAID, DO NOT DRIVE PAST IT FOR NOTHING: Metro State is ten minutes from '
          'Macalester and fifteen from the U of M, so if a Twin Cities week has a spare EVENING, one call to '
          '651.793.1300 option 5 costs almost nothing and would close the biggest single policy gap in this '
          'file — nobody has ever retrieved Metro State\'s solicitation policy. Rate it 3 provisionally, name '
          'the gap, and spend the day at Augsburg or St. Thomas instead.',
  'gaps': ['⚠⚠ THE METRO STATE SOLICITATION AND FACILITIES-USE POLICY COULD NOT BE FOUND AT ALL — this is what '
           'makes the access rating provisional. ☎ 651.793.1300 option 5. '
           'https://www.metrostate.edu/about/contact',
           '⚠ Whether ANY student-facing tabling, involvement fair or welcome-week event exists. ☎ 651.793.1300 '
           'option 5.',
           '⚠ Student Life and Leadership Development has NO WEB PAGE — /student-life and '
           '/students/support/student-life both return 404. No named staff, no direct line, no email.',
           'Any Metro State student organization in finance, business, computer science or blockchain — the '
           'CampusLabs directory is JavaScript-rendered. '
           'https://metrostate.campuslabs.com/engage/organization/msusa/contact',
           'Any Metro State faculty member in finance, economics or computing — no College of Management '
           'directory was retrievable. https://www.metrostate.edu/about/directory',
           'Whether the Saint Paul campus has any traditional public-forum outdoor space at all, given three '
           'scattered urban locations.',
           'Session-specific drop deadlines for the second 8-week session (Oct 14 – Dec 13). '
           'https://www.metrostate.edu/academics/calendar/fall-2026'],
  'note': '⚠⚠ AUDIENCE MISMATCH — FLAGGED LOUDLY. Metro State is a heavily commuter, heavily adult-learner, '
          'multi-location institution with Saturday and evening classes, two concurrent 8-week sessions, and '
          'no published student-life programming of any kind. It is the ONE campus in the Minnesota ten where '
          'the honest answer is "skip it," and the reason is that the undergraduate business-and-CS foot '
          'traffic a table depends on does not concentrate anywhere. Its access rating of 3 is PROVISIONAL and '
          'reflects an unretrievable policy, not a documented gated route.',
 },

 # ------------------------------------------------- 8. MACALESTER
 {'state': 'Minnesota',
  'name': 'Macalester College',
  'city': 'St. Paul, MN',
  'type': 'Private',
  'tier': 'C — Opportunistic',
  'access': 1,
  'start': 'Tue Sep 8, 2026 — same day as the U of M Twin Cities, and both are one mile and five miles '
           'respectively from St. Thomas.',
  'adddrop': 'Fri Sep 18, 2026 — "Last Day to Add/Drop a Class."',
  'fallbreak': 'Thu–Sun Oct 15–18, 2026 — a genuine four-day fall break.',
  'thanksgiving': 'Wed–Sun Nov 25–29, 2026 — a full five-day break beginning Wednesday.',
  'lastclass': 'Mon Dec 14, 2026',
  'finals': 'Study day Tue Dec 15, 2026; final examinations Wed–Sat Dec 16–19, 2026.',
  'cal_url': 'https://www.macalester.edu/registrar/academic-calendars/',
  'cal_status': 'CONFIRMED — official registrar academic calendar, all six dates published with weekdays. '
                'Semester system confirmed (distinct Fall and Spring semesters with separate registration, '
                'class schedules and examination periods).',
  'fair': '⚠ No fall student-organization fair with a published date. The only orientation fair is a Resource '
          'Fair, and it would not help.',
  'fair_date': 'Resource Fair, MON AUG 31, 2026, 10:00 a.m. — listed on the Center for Student Leadership & '
               'Engagement programming page alongside New Student Orientation (Aug 31) and a Library Open '
               'House (Aug 31, noon). ⚠ THIS IS AN ORIENTATION RESOURCE EVENT, NOT A STUDENT-ORGANIZATION '
               'FAIR, and it sits eight days before classes begin. No fall org fair date is published '
               'anywhere. The CSLE programming page lists Program Board traditions (Bingo for Books, Winter '
               'Ball, Pushball, Springfest, Food Festival, Drag @ Mac, Coffee House Jam, speaker events), '
               'Campus Center After Dark, Partners in Programming grants, Senior Week and the Adulting Series '
               '— but no involvement fair. UNVERIFIED, and see fair_outside: it would not matter.',
  'fair_outside': '⚠⚠ NO — AND THE BAN IS FLAT, WRITTEN AND UNAMBIGUOUS. Verbatim: "MACALESTER DOES NOT PERMIT '
                  'FUNDRAISING BY OUTSIDE ORGANIZATIONS ON ITS CAMPUS OR VIA COLLEGE AFFILIATED EVENTS OR '
                  'PROGRAMS." Private college, no public-forum obligation, no state statute, NO SPONSORSHIP '
                  'PATH. Whatever the fair date turns out to be is irrelevant to DGD.',
  'fair_cost': 'N/A — outside organizations are barred. Macalester does rent facilities as a conference '
               'business ("Our meeting facilities can host a group of any size from 10 to 500 in a variety of '
               'seating styles") but ⚠ RATES, INSURANCE REQUIREMENTS AND TERMS ARE NOT PUBLISHED; the page '
               'routes to eventservices@macalester.edu. That is room rental, not campus access.',
  'fair_deadline': 'N/A. For reference, a Macalester student org holding any fundraiser must submit a form AND '
                   'meet with CSLE "at least 14 calendar days prior" — the only published lead time.',
  'fair_url': 'https://www.macalester.edu/leadership-engagement/programming-involvement/',
  'policy': 'Center for Student Leadership & Engagement — Fundraising policy; Student Organization Code of '
            'Conduct; Purchasing policy; Conferences and Rentals',
  'policy_url': 'https://www.macalester.edu/leadership-engagement/student-organizations/fundraising/',
  'policy_key': "⚠⚠ THIS IS THE SHORTEST AND CLEAREST 'NO' IN MINNESOTA, AND IT IS A ONE-SENTENCE READ-ALOUD. "
                "CENTER FOR STUDENT LEADERSHIP & ENGAGEMENT, FUNDRAISING POLICY "
                "(https://www.macalester.edu/leadership-engagement/student-organizations/fundraising/), "
                "VERBATIM: 'MACALESTER DOES NOT PERMIT FUNDRAISING BY OUTSIDE ORGANIZATIONS ON ITS CAMPUS OR "
                "VIA COLLEGE AFFILIATED EVENTS OR PROGRAMS.' "
                "⚠⚠ PAYMENT CREDENTIALS — NAMED PLATFORMS, AND THE ONLY SUCH CLAUSE IN THIS ENTIRE STATE FILE. "
                "VERBATIM: 'STUDENT ORGANIZATIONS MAY ONLY CASH, CHECK, OR USE A BUSINESS SERVICES CREDIT CARD "
                "MACHINE TO COLLECT FUNDS. VENMO, PAYPAL, AND OTHER SIMILAR PLATFORMS ARE NOT ACCEPTED.' A "
                "crypto wallet is unambiguously an 'other similar platform.' A QR code on a Macalester table "
                "is a policy violation on its face. "
                "⚠ EXTERNAL FUNDING RAILS ALSO CLOSED, VERBATIM: 'STUDENT ORGANIZATIONS ARE PROHIBITED FROM "
                "HOLDING BANK ACCOUNTS EXTERNAL TO MACALESTER COLLEGE OR ACCEPT REGULAR FUNDING FROM EXTERNAL "
                "PARENT ORGANIZATIONS.' So a sponsored-club arrangement fails twice over: the club cannot take "
                "regular external funding and cannot bank outside the college. "
                "APPROVAL MACHINERY FOR STUDENTS, VERBATIM: 'ALL REGISTERED STUDENT ORGANIZATIONS WISHING TO "
                "SPONSOR A FUNDRAISING EVENT MUST HAVE APPROVAL FROM THE CENTER FOR STUDENT LEADERSHIP AND "
                "ENGAGEMENT FIRST.' 'THIS FORM MUST BE SUBMITTED AND YOU MUST MEET WITH THE CENTER FOR STUDENT "
                "LEADERSHIP AND ENGAGEMENT AT LEAST 14 CALENDAR DAYS PRIOR TO YOUR SCHEDULED EVENT.' "
                "'OFF-CAMPUS FUNDRAISING MAY BE APPROVED THROUGH THE EXECUTIVE DIRECTOR OF STUDENT LEADERSHIP "
                "AND ENGAGEMENT IN CONSULTATION WITH THE ADVANCEMENT OFFICE.' 'NO ALCOHOLIC BEVERAGES MAY BE "
                "SERVED, POSSESSED, OR CONSUMED AT ANY FUNDRAISING ACTIVITY.' "
                "READ THE THREE PROHIBITIONS TOGETHER AND THE PICTURE IS COMPLETE: an outside organization "
                "cannot raise funds on campus; a student org cannot bank outside Macalester or take regular "
                "funding from an external parent organization; and no student org may use a payment app. A "
                "crypto project handing out a wallet QR code at a Macalester table runs into the second and "
                "third of those before anyone even reaches the first. "
                "DOES SPONSORSHIP CURE IT? NO — THERE IS NO SPONSORSHIP PATH AT ALL. Unlike Carleton (where a "
                "department may reserve a table on your behalf, free) or St. Thomas (where Career Services is "
                "designated to sponsor external vendors), Macalester names no route by which an outside "
                "for-profit reaches students. THIS IS A 1. "
                "MACALESTER IS PRIVATE — NO PUBLIC-FORUM OBLIGATION, no First Amendment duty toward outside "
                "speakers, and Minnesota has NO campus free-speech statute (see the U of M Twin Cities "
                "policy_key). There is no appeal above the Executive Director. "
                "⚠ ANTI-FRONTING: no clause by that name — the outside-fundraising ban and the external-bank-"
                "account ban do the same work more comprehensively. "
                "FACILITY RENTAL DOES EXIST BUT IS A CONFERENCE BUSINESS, NOT CAMPUS ACCESS: 'Our meeting "
                "facilities can host a group of any size from 10 to 500 in a variety of seating styles' "
                "(https://www.macalester.edu/conferences/facilities/). ⚠ RATES, INSURANCE REQUIREMENTS AND "
                "TERMS ARE NOT PUBLISHED; inquiries route to eventservices@macalester.edu. Renting a room does "
                "not entitle you to solicit students in it. "
                "THE ONLY LAWFUL DOOR AT MACALESTER IS NON-COMMERCIAL SPEECH: Omicron Delta Epsilon, the "
                "economics honour society, 'holds speaker sessions pertaining to current topics' "
                "(https://www.macalester.edu/economics/clubsorganizations/). A speaker session is not "
                "fundraising, not solicitation and not a sale — it is the one thing the policy does not reach.",
  'sponsor_required': '⚠ NO ROUTE EXISTS. "Macalester does not permit fundraising by outside organizations on '
                      'its campus or via college affiliated events or programs" — and there is no sponsorship '
                      'provision anywhere to cure it, unlike Carleton (free sponsored table) or St. Thomas '
                      '(Career Services designated as sponsor). Do not spend a single hour courting a '
                      'Macalester club for table access. The only lawful presence is a NON-COMMERCIAL SPEAKER '
                      'SESSION, arranged through economics faculty — see Joyce Minor and Emily Richards below.',
  'clubs': [('⚠ Macalester Investment Group (MIG) — students manage a $250,000 portfolio',
             'ONE OF THE TWO BEST STUDENT-FINANCE AUDIENCES IN MINNESOTA (with UMD\'s $1M+ Bulldog Fund) — AND '
             'MACALESTER\'S POLICY WILL NOT LET DGD NEAR IT COMMERCIALLY. Students "manage a $250,000 '
             'portfolio, making investment recommendations through group discussion and voting"; members '
             'discuss finance careers, networking, interviews and personal money management. ⚠ THIS IS THE '
             'CLEAREST EXAMPLE IN THE FILE OF WHY ACCESS AND AUDIENCE ARE DIFFERENT NUMBERS: superb audience, '
             'access 1. Officer names are published on the department page but rotate annually — do not use '
             'them. LinkedIn: https://www.linkedin.com/company/macalester-investment-group/',
             'https://www.macalester.edu/economics/clubsorganizations/'),
            ('⚠ Omicron Delta Epsilon (ODE) — economics honour society, and THE ONLY DOOR',
             'ODE "holds speaker sessions pertaining to current topics" and hosts various annual events. A '
             'SPEAKER SESSION IS NOT FUNDRAISING, NOT SOLICITATION AND NOT A SALE — it is the single activity '
             'at Macalester that the outside-organization ban does not reach. This is the entire Macalester '
             'strategy in one line. Route in through economics faculty, not through student officers.',
             'https://www.macalester.edu/economics/clubsorganizations/'),
            ('Women in Economics (WIE)',
             'Strengthens networking among female economics students, faculty and alumni; "provides career '
             'support and networking opportunities"; biweekly meetings with 2–3 events per semester. Another '
             'speaker-session venue.',
             'https://www.macalester.edu/economics/clubsorganizations/'),
            ('Macalester Consulting Club · Macalester Entrepreneurship Club',
             'Consulting Club offers case-study analysis and interview practice across disciplines. '
             'Entrepreneurship Club is "a collaborative group developing business ideas through meetings with '
             'Twin Cities entrepreneurs" — note that phrase: the club already meets outside entrepreneurs, '
             'which is a speaking invitation waiting to happen and is not fundraising.',
             'https://www.macalester.edu/economics/clubsorganizations/'),
            ('⚠ NO BLOCKCHAIN / CRYPTO / WEB3 CLUB AT MACALESTER',
             'None found. Full student organization directories at '
             'https://www.macalester.edu/directory/studentorganizations/ and '
             'https://www.macalester.edu/life-at-mac/student-organizations/.',
             'https://www.macalester.edu/directory/studentorganizations/')],
  'faculty': [('⚠⚠ Joyce Minor — Karl Egge Professor of Economics',
               'THE SINGLE BEST DOOR AT MACALESTER. Her published field is INVESTMENT BANKING AND SECURITIES '
               'ANALYSIS — the closest thing to a digital-assets counterpart on this campus, and exactly the '
               'faculty member an ODE speaker session on cryptoassets would run through. A speaker invitation '
               'from her is non-commercial and touches none of the fundraising prohibitions. ⚠ Macalester '
               'emails render as JavaScript-protected placeholders — phone, do not email.',
               'Economics',
               'email obfuscated on page · (651) 696-6863',
               'https://www.macalester.edu/economics/facultystaff/'),
              ('⚠ Liang Ding — Professor of Economics',
               'Published field: INTERNATIONAL FINANCE AND FINANCIAL MARKETS. Second-best academic door and '
               'the most natural host for a markets-structure talk.',
               'Economics',
               'email obfuscated on page · (651) 696-6822',
               'https://www.macalester.edu/economics/facultystaff/'),
              ('Mario Solis-Garcia — Professor of Economics',
               'Published fields: "Macroeconomics, Growth and Development, FINANCIAL ECONOMICS." Third '
               'academic door; monetary-economics adjacent.',
               'Economics',
               'email obfuscated on page · (651) 696-6134',
               'https://www.macalester.edu/economics/facultystaff/'),
              ('Amy Damon — Professor and ECONOMICS DEPARTMENT CHAIR',
               'Chairs the department; approves department-hosted speakers. Fields are rural development and '
               'economic development, so she is the gatekeeper rather than the subject-matter host.',
               'Economics',
               'email obfuscated on page · (651) 696-6862',
               'https://www.macalester.edu/economics/facultystaff/'),
              ('⚠ Emily Richards — Economics Department Coordinator',
               'THE PERSON WHO ACTUALLY SCHEDULES A SPEAKER. Faculty agree to things; coordinators put them on '
               'a calendar and book the room. If Minor or Ding says yes, this is the follow-up call.',
               'Economics',
               'email obfuscated on page · (651) 696-6227',
               'https://www.macalester.edu/economics/facultystaff/'),
              ('Economics faculty — remaining, with published lines',
               'Sarah West, G. Theodore Mitau Professor (public finance, environmental economics) — '
               '(651) 696-6482. Felix Friedt, Associate Professor (international trade, industrial '
               'organization) — (651) 696-6779. Bridgit Jordan, Visiting Instructor — (651) 696-6740. ⚠ NO '
               'NUMBER PUBLISHED for Joe Anderson (Assistant Professor; "Macroeconomics, Monetary-Fiscal '
               'Interactions" — the closest monetary-economics fit on the faculty), Elizabeth Engle or Jessica '
               'Kiser — look up here.',
               'Economics',
               'emails obfuscated · (651) 696-6482 / 6779 / 6740; Anderson no number published — look up here',
               'https://www.macalester.edu/economics/facultystaff/'),
              ('⚠ Center for Student Leadership & Engagement (Weyerhaeuser Hall, Suite 103)',
               'APPROVES ALL FUNDRAISING AND ENFORCES THE OUTSIDE-ORGANIZATION BAN. The Executive Director of '
               'Student Leadership and Engagement is the named approver for off-campus fundraising, in '
               'consultation with the Advancement Office. ⚠ NO STAFF DIRECTORY EXISTS AS A PUBLIC PAGE — no '
               'individual staff names, titles or direct lines are published. A CSLE contact named EMI MENK '
               'appears on the fundraising page with a JavaScript-obfuscated email and no phone. This general '
               'line is the only route.',
               'Center for Student Leadership & Engagement',
               'email obfuscated on page · (651) 696-6569',
               'https://www.macalester.edu/leadership-engagement/'),
              ('Event Services — facility rental',
               'Handles external facility rentals and performance-space inquiries. ⚠ NO NUMBER PUBLISHED — '
               'look up here; the only published contact is eventservices@macalester.edu, and rates, insurance '
               'requirements and terms are all unpublished. Note that renting a room does not entitle you to '
               'solicit students in it.',
               'Conferences and Rentals',
               'eventservices@macalester.edu · no number published — look up here; use (651) 696-6000',
               'https://www.macalester.edu/conferences/facilities/'),
              ('Macalester College — main line (1600 Grand Avenue, Saint Paul, MN 55105)',
               'General switchboard; the number printed on the fundraising policy page itself. Offices '
               'directory at https://www.macalester.edu/directory/offices/.',
               'College',
               '(651) 696-6000 (main line)',
               'https://www.macalester.edu/leadership-engagement/student-organizations/fundraising/')],
  'courses': [('(No crypto/fintech course found)',
               'NO blockchain, cryptocurrency or fintech course was confirmed at Macalester. The Economics '
               'department is at https://www.macalester.edu/economics/. The relevant faculty fields are '
               'Investment Banking and Securities Analysis (Minor), International Finance and Financial '
               'Markets (Ding), Financial Economics (Solis-Garcia) and Monetary-Fiscal Interactions '
               '(Anderson) — a guest lecture into any of those is the realistic curricular play.',
               'https://www.macalester.edu/economics/')],
  'events': [('⚠ Omicron Delta Epsilon speaker sessions — THE ONLY LAWFUL DGD PRESENCE AT MACALESTER',
              'ODE "holds speaker sessions pertaining to current topics." A speaker session is not '
              'fundraising, not solicitation and not a sale, so it sits entirely outside the '
              'outside-organization ban. Arrange it through economics faculty — Joyce Minor (651) 696-6863 or '
              'Liang Ding (651) 696-6822 — and have Emily Richards (651) 696-6227 schedule it. No dates '
              'published.',
              'https://www.macalester.edu/economics/clubsorganizations/'),
             ('Business, Finance & Entrepreneurship Career Community',
              'A career-exploration programme grouping students by interest area — the natural institutional '
              'home for a non-commercial speaker slot outside the economics department. No Fall 2026 dates '
              'published.',
              'https://www.macalester.edu/career-exploration/business-finance-entrepreneurship/'),
             ('Orientation and CSLE programming, Fall 2026',
              'New Student Orientation Mon Aug 31, 2026; Resource Fair Aug 31, 10:00 a.m.; Library Open House '
              'Aug 31, noon. Recurring CSLE programming includes Program Board traditions (Bingo for Books, '
              'Winter Ball, Pushball, Springfest, Food Festival, Drag @ Mac, Coffee House Jam, speaker '
              'events), Campus Center After Dark, Partners in Programming grants of up to $500 for recognized '
              'student orgs to host events in the Campus Center, Senior Week and the Adulting Series. ⚠ Note '
              'the "Adulting Series" — "coordinated to help students prepare for their life after Macalester" '
              '— is the one programme whose stated purpose overlaps with personal finance education.',
              'https://www.macalester.edu/leadership-engagement/programming-involvement/'),
             ('(No hackathon or blockchain event)',
              'NO hackathon, blockchain conference, research centre or crypto legislative activity was found '
              'connected to Macalester.',
              'https://www.macalester.edu/life-at-mac/')],
  'play': 'Do not plan a table here — plan a talk, or skip it. Macalester is the only 1 in Minnesota and the '
          'sentence that makes it one is unambiguous: "Macalester does not permit fundraising by outside '
          'organizations on its campus or via college affiliated events or programs." There is no sponsorship '
          'provision to cure it, unlike Carleton or St. Thomas. Two further clauses close the crypto angle '
          'specifically: student organizations "may only cash, check, or use a Business Services credit card '
          'machine to collect funds — Venmo, PayPal, and other similar platforms are not accepted," and they '
          'are "prohibited from holding bank accounts external to Macalester College or accept regular funding '
          'from external parent organizations." A wallet QR code on a Macalester table is a violation on its '
          'face. ⚠ THE FRUSTRATION IS REAL AND WORTH NAMING: the Macalester Investment Group manages a '
          '$250,000 portfolio and is one of the two best student-finance audiences in the state — this is the '
          'clearest case in the file of a superb audience behind a closed door. THE ONE LAWFUL ROUTE IS '
          'NON-COMMERCIAL SPEECH. Omicron Delta Epsilon, the economics honour society, "holds speaker sessions '
          'pertaining to current topics"; a speaker session is not fundraising, not solicitation and not a '
          'sale. Call Joyce Minor, Karl Egge Professor, at (651) 696-6863 — her field is Investment Banking '
          'and Securities Analysis — or Liang Ding at (651) 696-6822 for International Finance and Financial '
          'Markets, and have Emily Richards at (651) 696-6227 put it on a calendar. Bring the Minnesota '
          'crypto-custody statute (HF 3709, effective Aug 1, 2026) as the hook; regulation is an academic '
          'topic, a wallet is not. Macalester is one mile from St. Thomas, so the visit costs an hour.',
  'gaps': ['⚠ Whether a purely educational, non-fundraising guest lecture is permitted despite the '
           'outside-organization ban. ☎ CSLE (651) 696-6569. '
           'https://www.macalester.edu/leadership-engagement/student-organizations/fundraising/',
           'No fall student-organization fair date is published anywhere — only an orientation Resource Fair '
           'on Aug 31. https://www.macalester.edu/leadership-engagement/programming-involvement/',
           'CSLE has NO public staff directory — no individual names, titles or direct lines. A contact named '
           'Emi Menk appears on the fundraising page with a JavaScript-obfuscated email and no phone. '
           '☎ (651) 696-6569.',
           'Facility rental rates, insurance requirements and terms are NOT published; only '
           'eventservices@macalester.edu, with no phone number. https://www.macalester.edu/conferences/facilities/',
           'A direct number for Joe Anderson (Macroeconomics, Monetary-Fiscal Interactions), the closest '
           'monetary-economics fit on the faculty — none published. '
           'https://www.macalester.edu/economics/facultystaff/',
           'Whether the Executive Director of Student Leadership and Engagement (the named approver for '
           'off-campus fundraising) would entertain any DGD presence — the person is unnamed on the site. '
           '☎ (651) 696-6569.'],
  'note': '⚠ ACCESS 1 IS ABOUT THE WRITTEN POLICY, NOT THE AUDIENCE. Macalester has the $250,000 Macalester '
          'Investment Group, an economics faculty with three published financial-markets specialists, and a '
          'consulting club and an entrepreneurship club that already meet Twin Cities entrepreneurs. It also '
          'has a flat ban on outside-organization fundraising, a named prohibition on payment apps, and no '
          'sponsorship path of any kind. Every Macalester email renders as a JavaScript-protected placeholder '
          '— phone, do not email. Located one mile from St. Thomas on Grand/Summit, with ACTC '
          'cross-registration between them.',
 },

 # ------------------------------------------------- 9. CARLETON COLLEGE
 {'state': 'Minnesota',
  'name': 'Carleton College',
  'city': 'Northfield, MN',
  'type': 'Private',
  'tier': 'C — Opportunistic',
  'access': 3,
  'start': '⚠⚠ Mon Sep 14, 2026, 8:30 a.m. — THE LATEST START IN MINNESOTA. Six days after the U of M Twin '
           'Cities, TWENTY-THREE DAYS after Metro State, and three weeks after Mankato, St. Cloud and Winona. '
           'New Student Week runs Tue–Sun Sep 8–13, 2026. ⚠ TRIMESTER SYSTEM — see finals.',
  'adddrop': 'Sun Sep 20, 2026, 11:59 p.m. for most courses — a six-day add/drop window, the shortest in the '
             'state, because a 10-week term leaves no slack.',
  'fallbreak': 'Midterm break Sat–Mon Oct 17–19, 2026 — a three-day break at the halfway point of a 10-week '
               'term.',
  'thanksgiving': '⚠⚠ NONE — THERE IS NO THANKSGIVING BREAK AT CARLETON BECAUSE THE TERM IS ALREADY OVER. Fall '
                  'term ends Mon Nov 23, 2026, two days before Thanksgiving.',
  'lastclass': '⚠⚠ Wed Nov 18, 2026. Reading days Thu–Fri Nov 19–20.',
  'finals': '⚠⚠ Sat–Mon Nov 21–23, 2026. Grades due Dec 2. TERM ENDS NOV 23 — THERE IS NO DECEMBER WINDOW AT '
            'CARLETON AT ALL. While every other Minnesota campus is running finals in mid-December, Carleton '
            'has been empty for three weeks. THE ENTIRE USABLE WINDOW IS MON SEP 14 – WED NOV 18, 2026, and '
            'realistically SEP 21 – NOV 13 once you exclude the first week and finals prep. Miss it and the '
            'next opportunity is Winter Term in January.',
  'cal_url': 'https://carleton-wp-production.s3.amazonaws.com/uploads/sites/740/2026/02/Academic-Calendar-26-27_detailed-1.pdf',
  'cal_status': 'CONFIRMED — the detailed 2026-27 academic calendar PDF. ⚠ TRIMESTER CONFIRMED SEPARATELY on '
                'the registrar\'s own page: "Carleton\'s academic year is comprised of THREE 10-WEEK-LONG '
                'TERMS," and "The standard course unit is six credits, and students normally carry THREE '
                'COURSES, or 18 credits, PER TERM" (https://www.carleton.edu/registrar/academic-term/). '
                'Students may carry 12–22 credits, or up to 24 with Academic Standing Committee permission. '
                'Multi-year approved calendar at '
                'https://carleton-wp-production.s3.amazonaws.com/uploads/sites/740/2025/02/Academic-Calendar-2026-2029_approved-by-CC-2.pdf; '
                'hub at https://www.carleton.edu/registrar/calendars/.',
  'fair': 'Carleton fall activities fair (Student Activities Office) — DATE NOT PUBLISHED',
  'fair_date': '⚠ UNVERIFIED — NO CARLETON FALL ACTIVITIES FAIR WITH A PUBLISHED DATE COULD BE FOUND. The '
               'Student Activities Office runs student-organization programming '
               '(https://www.carleton.edu/student-activities/guide/) but publishes no fair page and no date. '
               'PATTERN: New Student Week is Tue–Sun Sep 8–13, 2026, which is where such an event would sit, '
               'immediately before classes begin Mon Sep 14. ⚠ AND IT MAY NOT MATTER — Carleton\'s Sayles-Hill '
               'table policy lets a sponsoring department or club book a table FOR you on any weekday, free, '
               'with 24 hours\' notice, which is a better deal than any one-day fair. ☎ Student Activities '
               'Office, (507) 222-4462.',
  'fair_outside': '⚠ NO for a direct booking, YES via sponsorship — and Carleton is the ONLY campus in this '
                  'file where sponsorship is EXPLICITLY the cure and costs NOTHING. Verbatim: "WE DO NOT '
                  'ACCEPT RESERVATIONS FOR LOCAL BUSINESS OR OFF-CAMPUS ORGANIZATIONS. However, if you receive '
                  'sponsorship from a campus department or organization, THE DEPARTMENT/ORGANIZATION CAN MAKE '
                  'A TABLE RESERVATION ON YOUR BEHALF. THERE IS NO FEE IF YOU ARE SPONSORED."',
  'fair_cost': '⚠ $0 IF SPONSORED — "There is no fee if you are sponsored." No rate card exists because there '
               'is no unsponsored route to price. The cost at Carleton is not money, it is the time spent '
               'finding a department or chartered organization willing to make the booking in EMS with a '
               'Carleton login.',
  'fair_deadline': '⚠ "TABLES NEED TO BE RESERVED 24 HOURS IN ADVANCE." That is the only deadline — but the '
                   'sponsor must place the booking themselves through the EMS Web App using a Carleton ID and '
                   'password, so the real lead time is however long it takes to secure the sponsor. ⚠ AND THE '
                   'HARD DEADLINE IS THE TERM ITSELF: everything must happen between Sep 14 and Nov 18, 2026.',
  'fair_url': 'https://www.carleton.edu/student-activities/guide/event-promotion/table/',
  'policy': 'Sayles-Hill Tables policy (Student Activities Office) + Sayles-Hill Posting Policy + CSA Handbook '
            'for Student Organizations',
  'policy_url': 'https://www.carleton.edu/student-activities/guide/event-promotion/table/',
  'policy_key': "⚠⚠ CARLETON IS THE OPPOSITE OF EVERY ANTI-FRONTING CAMPUS IN THIS FILE. IT *INVITES* THE "
                "ARRANGEMENT THAT UMN TWIN CITIES AND ST. CLOUD STATE FORBID BY NAME AND PUNISH AS 'FRONTING' "
                "— AND IT CHARGES NOTHING FOR IT. "
                "SAYLES-HILL TABLES POLICY "
                "(https://www.carleton.edu/student-activities/guide/event-promotion/table/), VERBATIM: "
                "'A CARLETON COLLEGE DEPARTMENT OR STUDENT ORGANIZATION CAN RESERVE A TABLE LOCATION IN "
                "SAYLES-HILL GREAT SPACE MONDAY-FRIDAY FROM 9:00 A.M. – 6:00 P.M.' "
                "'WE DO NOT ACCEPT RESERVATIONS FOR LOCAL BUSINESS OR OFF-CAMPUS ORGANIZATIONS.' "
                "⚠⚠ AND THEN, IMMEDIATELY AFTER, THE SENTENCE THAT CHANGES EVERYTHING: 'HOWEVER, IF YOU "
                "RECEIVE SPONSORSHIP FROM A CAMPUS DEPARTMENT OR ORGANIZATION, THE DEPARTMENT/ORGANIZATION CAN "
                "MAKE A TABLE RESERVATION ON YOUR BEHALF. THERE IS NO FEE IF YOU ARE SPONSORED.' "
                "READ THAT SIDE BY SIDE WITH UMN TWIN CITIES ('Student groups are not permitted to reserve "
                "contact tables on behalf of University departments or external organizations') AND ST. CLOUD "
                "STATE ('Student organizations and university departments shall not use their access to "
                "campus, space, and services to \"front\" for a non-university group or commercial vendor'). "
                "SAME FACT PATTERN, OPPOSITE RULE. At Carleton the workaround IS the policy, it is written "
                "down, and an ambassador can read it aloud. "
                "OPERATIVE MECHANICS: 'TABLES NEED TO BE RESERVED 24 HOURS IN ADVANCE.' The reservation is "
                "made through the EMS WEB APP USING A CARLETON ID AND PASSWORD — so THE SPONSORING DEPARTMENT "
                "OR CHARTERED ORGANIZATION MUST PHYSICALLY MAKE THE BOOKING; DGD cannot self-serve. Signage "
                "must be 'placed behind your table using the tack strips' and 'NO TAPE SHOULD BE PLACED ON THE "
                "TABLES.' Hours are Monday–Friday 9:00 a.m.–6:00 p.m., which is a NINE-HOUR WINDOW — longer "
                "than UMD's 9–3 and Augsburg's 8–4:30. A separate Sayles-Hill Posting Policy governs flyers "
                "(https://www.carleton.edu/student-activities/guide/event-promotion/posting-policy/). "
                "⚠ WHAT IS *NOT* AT CARLETON, AND EVERY ABSENCE IS FAVOURABLE: NO rate card (there is no fee "
                "if sponsored). NO insurance requirement. NO deposit. NO cancellation terms. NO explicit "
                "commercial-solicitation ban beyond the reservation rule itself. NO language reaching payment "
                "credentials or on-site contract signing. The CSA Handbook for Student Organizations "
                "(https://www.carleton.edu/orgs/csa/administration/handbook/) contains none of these either — "
                "its only relevant restriction is that 'STUDENTS NOT CURRENTLY ENROLLED AND/OR \"ON LEAVE\" "
                "ARE NOT PERMITTED TO PARTICIPATE IN CSA CHARTERED STUDENTS ORGANIZATIONS, or student groups "
                "recognized or otherwise supported by the College.' "
                "CARLETON IS PRIVATE. No public-forum obligation, no First Amendment duty toward outside "
                "speakers, and Minnesota has NO campus free-speech statute (see the U of M Twin Cities "
                "policy_key). But unlike Macalester's discretionary flat ban, Carleton's rule is a PUBLISHED, "
                "QUOTABLE, PERMISSIVE SENTENCE — which is worth more than a forum right you would have to "
                "litigate. "
                "DOES SPONSORSHIP CURE IT? YES — EXPLICITLY, IN WRITING, AND FOR FREE. IT IS ALSO THE ONLY "
                "ROUTE. There is no paid alternative to buy your way past a reluctant sponsor. "
                "⚠⚠ THE REAL CONSTRAINT AT CARLETON IS NOT POLICY, IT IS THE CALENDAR. FALL TERM ENDS MONDAY "
                "NOVEMBER 23, 2026. There is no December window. See the calendar fields.",
  'sponsor_required': '⚠ YES — AND IT IS THE WHOLE STRATEGY, IT IS EXPLICITLY PERMITTED, AND IT IS FREE. '
                      '"If you receive sponsorship from a campus department or organization, the '
                      'department/organization can make a table reservation on your behalf. THERE IS NO FEE IF '
                      'YOU ARE SPONSORED." The sponsor must be a Carleton department or chartered student '
                      'organization and must place the booking themselves in the EMS Web App with a Carleton '
                      'login, 24 hours ahead. Best candidates: the Carleton Investment Group, the Economics '
                      'department, or the Career Center (which already runs Investment Banking/Finance and '
                      'Consulting resource programming). Start with the Student Activities Office, '
                      '(507) 222-4462, and ask them who sponsors outside speakers.',
  'clubs': [('⚠ Carleton Investment Group (CIG) — the obvious sponsor, and the page is bot-blocked',
             'The natural sponsoring organization for a DGD table under the Sayles-Hill rule. ⚠ THE PAGE IS '
             'BEHIND A CLOUDFLARE BOT CHECK — apps.carleton.edu returned only "Checking your browser before '
             'accessing apps.carleton.edu" and NO CONTENT to research tooling. Its existence is confirmed by '
             'the URL; its status, activities, size and contacts are NOT. ☎ Student Activities Office '
             '(507) 222-4462 and ask whether CIG is currently chartered and who advises it.',
             'https://apps.carleton.edu/student/orgs/cig/'),
            ('Carleton Student Association (CSA) — the chartering body',
             'CSA charters and administers student organizations and is the route to any chartered group. '
             'Published contact: csa-executives@carleton.edu. The Handbook for Student Organizations is at '
             'https://www.carleton.edu/orgs/csa/administration/handbook/ and the administration hub at '
             'https://www.carleton.edu/orgs/csa/administration/. ⚠ The "List of Student Organizations" link '
             'exists but the directory did not render a list to research tooling.',
             'https://www.carleton.edu/orgs/csa/'),
            ('⚠ NO BLOCKCHAIN / CRYPTO / WEB3 CLUB FOUND AT CARLETON',
             'None surfaced. ⚠ But the student-organization directory did not render, so this is not-found '
             'rather than confirmed-absent. What IS confirmed is a finance-interested student population: the '
             'Career Center maintains dedicated resource pages for INVESTMENT BANKING/FINANCE '
             '(https://www.carleton.edu/career/students/jobs/resources/banking/) and CONSULTING '
             '(https://www.carleton.edu/career/students/jobs/resources/consulting/), which colleges do not '
             'build without demand.',
             'https://www.carleton.edu/student-activities/guide/')],
  'faculty': [('⚠⚠ Student Activities Office (Sayles-Hill Suite 051, One North College Street, Northfield MN '
               '55057)',
               'THE ONLY NUMBER THAT MATTERS AT CARLETON. This is the office that must be persuaded to '
               'sponsor — or to name a department or chartered organization that will — and it owns the '
               'Sayles-Hill table reservation system. Hours 9:00 a.m.–5:00 p.m., Monday–Friday. Ask three '
               'things: (1) which departments or organizations sponsor outside speakers and tables, (2) is the '
               'Carleton Investment Group currently chartered and who advises it, and (3) when is the fall '
               'activities fair, which is published nowhere.',
               'Student Activities Office',
               'sao@carleton.edu · (507) 222-4462',
               'https://www.carleton.edu/student-activities/guide/event-promotion/table/'),
              ('Carleton Student Association (CSA) — executives',
               'The chartering body for student organizations; the route to CIG and to any chartered group '
               'willing to sponsor. ⚠ NO PHONE PUBLISHED — email only; use the Carleton main line or the '
               'Student Activities Office.',
               'Carleton Student Association',
               'csa-executives@carleton.edu · no number published — look up here; use (507) 222-4462',
               'https://www.carleton.edu/orgs/csa/administration/handbook/'),
              ('Carleton College — main line',
               'General switchboard, printed on the CSA handbook page. Lee Clark is named as maintaining the '
               'Student Activities pages but no direct contact is published for him.',
               'College',
               '(507) 222-4000 (main line)',
               'https://www.carleton.edu/orgs/csa/administration/handbook/'),
              ('(Student Activities staff — individuals)',
               'NOT CONFIRMED — no individual Student Activities staff member\'s name, title, email or direct '
               'line is published on any retrievable page. Only the office address, sao@carleton.edu and the '
               'main office number exist. Look up here.',
               'Student Activities Office',
               'sao@carleton.edu · no individual numbers published — look up here; use (507) 222-4462',
               'https://www.carleton.edu/student-activities/about/'),
              ('(Economics and Computer Science faculty)',
               'NOT CONFIRMED — NO Carleton economics or computer-science faculty member could be confirmed as '
               'working on blockchain, cryptocurrency, fintech or digital assets. Department catalogs: '
               'Economics https://www.carleton.edu/catalog/current/departments/econ/ and Computer Science '
               'https://www.carleton.edu/catalog/current/departments/cs/. Look up here. No numbers published.',
               'Economics / Computer Science',
               'no numbers published — look up here; use (507) 222-4000',
               'https://www.carleton.edu/catalog/current/departments/econ/')],
  'courses': [('(No crypto/fintech course found)',
               'NO blockchain, cryptocurrency or fintech course was confirmed at Carleton. Computer Science '
               'catalog at https://www.carleton.edu/catalog/current/departments/cs/ and course list at '
               'https://www.carleton.edu/computer-science/courses/; Economics at '
               'https://www.carleton.edu/catalog/current/departments/econ/. ⚠ Remember the structure: students '
               'take only THREE courses per 10-week term, so curricular breadth is narrower than at a semester '
               'school of comparable size.',
               'https://www.carleton.edu/computer-science/courses/')],
  'events': [('Carleton Career Summit',
              'A career-programming event run by the Career Center. ⚠ Date not published on a retrievable '
              'page. On-campus recruiting is administered at '
              'https://apps.carleton.edu/career/employers/oncampusrecruiting/. The Career Center is a '
              'plausible SPONSOR under the Sayles-Hill rule given it already maintains Investment '
              'Banking/Finance and Consulting resource pages.',
              'https://www.carleton.edu/career/programs/carletoncareersummit/'),
             ('New Student Week 2026',
              'Tue–Sun Sep 8–13, 2026, immediately before classes begin Mon Sep 14. The likeliest home for a '
              'fall activities fair, though no fair date is published.',
              'https://carleton-wp-production.s3.amazonaws.com/uploads/sites/740/2026/02/Academic-Calendar-26-27_detailed-1.pdf'),
             ('(No hackathon or blockchain event)',
              'NO hackathon, blockchain conference, research centre or crypto legislative activity was found '
              'connected to Carleton College. Campus calendar at https://www.carleton.edu/calendar/.',
              'https://www.carleton.edu/calendar/')],
  'play': 'Carleton is a sponsorship play on a stopwatch. The written rule is unusually generous and worth '
          'quoting aloud: "We do not accept reservations for local business or off-campus organizations. '
          'However, if you receive sponsorship from a campus department or organization, the '
          'department/organization can make a table reservation on your behalf. THERE IS NO FEE IF YOU ARE '
          'SPONSORED." That is the exact arrangement UMN Twin Cities and St. Cloud State forbid by name as '
          '"fronting" — at Carleton it is the policy, and it is free, in Sayles-Hill Great Space, weekdays '
          '9:00 a.m. to 6:00 p.m., a nine-hour window. The sponsor must place the booking themselves in the '
          'EMS Web App with a Carleton login, 24 hours ahead, so your entire job is finding one willing '
          'department or chartered organization. Call the Student Activities Office at (507) 222-4462 and ask '
          'who sponsors outside speakers; the obvious candidates are the Carleton Investment Group (whose page '
          'is behind a Cloudflare bot check and could not be read), the Economics department, and the Career '
          'Center, which already runs Investment Banking/Finance and Consulting resource programming. ⚠⚠ NOW '
          'THE STOPWATCH, AND IT IS THE MOST DANGEROUS CALENDAR FACT IN MINNESOTA: CARLETON IS ON TRIMESTERS. '
          'Fall term runs Sep 14 – Nov 23 only, classes end Nov 18, THERE IS NO THANKSGIVING BREAK BECAUSE THE '
          'TERM IS OVER, AND THERE IS NO DECEMBER WINDOW AT ALL. Anyone planning "hit Northfield in early '
          'December" will find an empty campus while every other Minnesota school is still in session. The '
          'real working window is roughly Sep 21 – Nov 13. Start the sponsor conversation in the first week of '
          'the term or do not bother until January. Northfield is 45 minutes south of the Twin Cities base.',
  'gaps': ['⚠⚠ WHICH department or chartered organization will sponsor the free Sayles-Hill table, and by '
           'when? The sponsor must book in EMS with a Carleton login, 24 hours ahead, and the window closes '
           'Nov 18. ☎ Student Activities Office (507) 222-4462. '
           'https://www.carleton.edu/student-activities/guide/event-promotion/table/',
           '⚠ Carleton Investment Group status, activities and advisor — apps.carleton.edu is behind a '
           'CLOUDFLARE BOT CHECK and returned no content. ☎ (507) 222-4462. '
           'https://apps.carleton.edu/student/orgs/cig/',
           'Fall activities fair date — none published anywhere; New Student Week Sep 8–13 is the likely '
           'window. ☎ (507) 222-4462.',
           'No individual Student Activities staff member is named or reachable directly — only sao@carleton.edu '
           'and the office line. https://www.carleton.edu/student-activities/about/',
           'The student organization directory did not render a list — whether any blockchain/crypto group '
           'exists is unknown. https://www.carleton.edu/orgs/csa/',
           'Any Carleton economics or CS faculty member working on blockchain or digital assets — none could '
           'be confirmed, and no faculty phone numbers are published. '
           'https://www.carleton.edu/catalog/current/departments/econ/',
           'Carleton Career Summit date — not published. '
           'https://www.carleton.edu/career/programs/carletoncareersummit/'],
  'note': '⚠⚠ TWO CARLETON TRAPS. (1) TRIMESTERS. Three 10-week terms, three courses per term. Fall Term 2026 '
          'is Sep 14 – Nov 23 and ENDS BEFORE THANKSGIVING — no December window exists, unlike every other '
          'campus in this file. It also starts LAST in the state, so a tour that opens in Northfield in late '
          'August will find an empty campus in the other direction. (2) NAME COLLISION: searches for '
          '"Carleton" clubs and calendars return CARLETON UNIVERSITY IN OTTAWA, ONTARIO (carleton.ca, CUSA, '
          'cusaclubs.ca, calendar.carleton.ca) — a completely different institution. Carleton College is '
          'carleton.edu, Northfield, Minnesota. Do not cite a Canadian policy at a Minnesota table.',
 },

 # ------------------------------------------------- 10. AUGSBURG UNIVERSITY
 {'state': 'Minnesota',
  'name': 'Augsburg University',
  'city': 'Minneapolis, MN',
  'type': 'Private (religious)',
  'tier': 'B — Regional',
  'access': 4,
  'start': 'Wed Sep 2, 2026 — six days before the U of M Twin Cities and one and a half miles from it.',
  'adddrop': 'Wed Sep 9, 2026 — "Last day to add or drop without notation."',
  'fallbreak': 'Midterm break Fri–Sun Oct 23–25, 2026.',
  'thanksgiving': 'Thu–Sun Nov 26–29, 2026.',
  'lastclass': '⚠ SPLIT — day classes end Fri Dec 11, 2026; FULL-SEMESTER classes end Fri Dec 18, 2026. '
               'Augsburg runs day and evening/weekend cohorts on different end dates, so the campus is still '
               'populated the week of Dec 14 even though day finals are running.',
  'finals': 'Final exams (day classes only) Mon–Thu Dec 14–17, 2026.',
  'cal_url': 'https://www.augsburg.edu/registrar/calendars/',
  'cal_status': 'CONFIRMED — dates extracted from Augsburg\'s official 2026-2027 academic calendar Google '
                'Sheet, linked from the registrar\'s calendars page '
                '(https://docs.google.com/spreadsheets/d/10niiR0NmnuD3Hk7D3VZGWTDssIOd72BwqK-Z3kU_vrI/edit). '
                '⚠ The Provost\'s calendars page (https://sites.augsburg.edu/academicaffairs/calendars/) is an '
                'EMBEDDED GOOGLE CALENDAR that returned no dates to research tooling, and the registrar '
                'landing page itself shows no dates — the linked spreadsheet is the only source that yields '
                'them.',
  'fair': 'Student Organizations Fall Involvement Fair (Campus Life) — ⚠ but the PAID VENDOR TABLE is the '
          'better route at Augsburg',
  'fair_date': '⚠ THE LIVE EVENT PAGE SHOWS AUGUST 29, 2024, 11:00 a.m.–12:30 p.m., Christensen Center Lobby — '
               'A TWO-YEAR-OLD LISTING. Verbatim description: "Each semester, Campus Life holds an Involvement '
               'Fair for all student organizations!" RECURRING PATTERN: every semester, Campus Life, '
               'Christensen Center Lobby, roughly 11:00 a.m.–12:30 p.m., in the days around the start of '
               'classes. With a Sep 2, 2026 start, expect late August or the first week of September 2026. '
               'FALL 2026 DATE UNVERIFIED — will post to https://calendar.augsburg.edu/ and to Auggie Life '
               '(https://augsburg.campuslabs.com/engage/). ⚠ BUT NOTE: at Augsburg the involvement fair is the '
               'WORSE option. The vendor policy lets DGD buy a table in the SAME LOBBY, any weekday, for $75 — '
               'no fair, no competition, no student-org gatekeeper.',
  'fair_outside': '⚠ YES — BY A PUBLISHED FLAT RATE, ON ANY WEEKDAY, NOT JUST AT A FAIR. Verbatim from the '
                  'Vendor/Tabling Policy: "EACH VENDOR WILL BE CHARGED A FLAT-RATE OF $75.00 PER DAY TO '
                  'DISPLAY ANYTIME BETWEEN 8 A.M. – 4:30 P.M. (ADDITIONAL TABLES ARE AVAILABLE FOR '
                  '$10.00/TABLE/DAY)." External groups may table in the Christensen Center Lobby, Monday–'
                  'Friday, maximum six tables; Saturday tabling is available by request. Oren Gateway Center '
                  '(11 a.m.–2 p.m., one table) is INTERNAL GROUPS ONLY. The involvement fair itself is for '
                  'student organizations.',
  'fair_cost': '⚠ $75.00 PER DAY FLAT RATE for external vendors, plus $10.00 per additional table per day. '
               'THAT IS THE CHEAPEST PUBLISHED OUTSIDE-VENDOR TABLE IN MINNESOTA — under half of UMD\'s $160 '
               'and below St. Cloud State\'s $85.',
  'fair_deadline': '⚠ MINIMUM 2 DAYS\' ADVANCE NOTICE FOR EXTERNAL VENDORS (internal groups use an online '
                   'form). That is the shortest lead time of any paid table in this file — Augsburg can be '
                   'booked almost on impulse. Saturday tabling by request. ☎ University Events, '
                   '(612) 330-1104.',
  'fair_url': 'https://sites.augsburg.edu/events/policies/vendor-tabling-policy/',
  'policy': 'University Events — Vendor/Tabling Policy; University Events General Information; Hosting '
            'External Events at Augsburg',
  'policy_url': 'https://sites.augsburg.edu/events/policies/vendor-tabling-policy/',
  'policy_key': "⚠ AUGSBURG PUBLISHES A PRICED INVITATION, NOT A BARRIER — AND AT $75 IT IS THE CHEAPEST "
                "OUTSIDE-VENDOR TABLE IN MINNESOTA. "
                "VENDOR/TABLING POLICY, University Events "
                "(https://sites.augsburg.edu/events/policies/vendor-tabling-policy/). THE RATE, VERBATIM: "
                "'EACH VENDOR WILL BE CHARGED A FLAT-RATE OF $75.00 PER DAY TO DISPLAY ANYTIME BETWEEN 8 A.M. "
                "– 4:30 P.M. (ADDITIONAL TABLES ARE AVAILABLE FOR $10.00/TABLE/DAY).' "
                "LOCATIONS AND HOURS: CHRISTENSEN CENTER LOBBY, 8:00 a.m.–4:30 p.m., Monday–Friday, MAXIMUM 6 "
                "TABLES. OREN GATEWAY CENTER, 11:00 a.m.–2:00 p.m., Monday–Friday, INTERNAL GROUPS ONLY, "
                "maximum 1 table. SATURDAY TABLING AVAILABLE BY REQUEST. ADVANCE NOTICE: MINIMUM 2 DAYS FOR "
                "EXTERNAL VENDORS (internal groups use an online form) — the shortest lead time of any paid "
                "table in this file. "
                "⚠⚠ PROHIBITED — AND NOTE THE FIRST ITEM, WHICH IS THE MINN. STAT. s 135A.145 SHADOW AGAIN: "
                "'NO CREDIT CARD PROMOTIONS.' Also prohibited: promotion of alcohol, drugs, tobacco or obscene "
                "material; food and beverage from anyone other than the on-campus provider (WRAPPED CANDY "
                "EXCEPTED — so a bowl of wrapped sweets on the table is fine); 'VENDORS MUST REMAIN AT TABLES; "
                "NO AGGRESSIVE SOLICITATION'; health-related vendors must coordinate through the Center for "
                "Wellness and Counseling. THE 'NO CREDIT CARD PROMOTIONS' CLAUSE IS THE ONE TO PREPARE FOR: it "
                "almost certainly derives from Minn. Stat. s 135A.145, which bars any postsecondary "
                "institution — including its student organizations — from agreements to market credit cards to "
                "undergraduates (full text in the U of M Twin Cities policy_key). DGD IS NOT A CARD ISSUER "
                "UNDER 15 U.S.C. s 1602 AND IS NOT PROMOTING A CREDIT CARD. Say it before they ask. "
                "SPONSORSHIP, VERBATIM: 'A MEMBER OF THE ORGANIZATION SPONSORING THE TABLE MUST BE PRESENT "
                "DURING ALL TABLING TIMES IN ORDER TO VALIDATE SPONSORSHIP.' ⚠ NOTE THE SCOPE: this governs "
                "SPONSORED tables. A straight PAID external vendor table does not require a student sponsor — "
                "you pay the $75 and stand there yourself. The sponsorship clause is the alternative route, "
                "not a condition on the paid one. Confirm this reading on the booking call. "
                "⚠ NO INSURANCE REQUIREMENT, NO DOLLAR LIMIT, NO DEPOSIT AND NO CANCELLATION TERMS APPEAR IN "
                "THE VENDOR/TABLING POLICY. The University Events general-information page "
                "(https://sites.augsburg.edu/events/policies/university-events-general-information/) routes "
                "external-event questions to a separate 'HOSTING EXTERNAL EVENTS AT AUGSBURG' section "
                "(https://sites.augsburg.edu/events/hosting-external-events-at-augsburg/) WHICH COULD NOT BE "
                "RETRIEVED — that is where any insurance requirement would live. ASK ON THE BOOKING CALL. "
                "Venues list at https://sites.augsburg.edu/events/planning-your-events/venues/; internal "
                "tabling form at https://sites.augsburg.edu/events/internal-event-requests/internal-tabling/. "
                "NO ANTI-FRONTING LANGUAGE AND NO ON-SITE-CONTRACT-SIGNING LANGUAGE WAS FOUND AT AUGSBURG. "
                "AUGSBURG IS PRIVATE (ELCA LUTHERAN). No public-forum duty, no First Amendment obligation "
                "toward outside speakers, and Minnesota has NO campus free-speech statute (see the U of M Twin "
                "Cities policy_key). But none of that matters here, because the written rule is an invitation "
                "with a price on it rather than a restriction to argue about. THE $75 IS THE ARGUMENT.",
  'sponsor_required': '⚠ NO FOR THE PAID ROUTE — PAY $75 AND STAND THERE. The sponsorship clause ("a member of '
                      'the organization sponsoring the table must be present during all tabling times in order '
                      'to validate sponsorship") governs SPONSORED tables, i.e. the free alternative where a '
                      'student organization hosts you. A straight external-vendor booking at the published '
                      'flat rate carries no sponsor requirement in the written policy. ⚠ CONFIRM THIS READING '
                      'WITH UNIVERSITY EVENTS, (612) 330-1104 — it is the single question that decides whether '
                      'Augsburg is a two-day turnaround or a three-week club courtship.',
  'clubs': [('⚠ Augsburg Business Organization (ABO) — advisor MARC ISAACSON, with a DIRECT LINE',
             'Commissioned Student Organization, chartered 2001-02. Verbatim purpose: "ABO promotes the study '
             'of business at Augsburg, as well as brings students together who have an interest in discussing '
             'and advocating for business." ⚠ THE BEST CLUB DOOR AT AUGSBURG PRECISELY BECAUSE THE ADVISOR IS '
             'NAMED WITH A PHONE NUMBER — Marc Isaacson, isaacson@augsburg.edu, 612-330-1194 — which is rare '
             'at any private college. Officer names are published on the department page but rotate annually; '
             'use the advisor.',
             'https://www.augsburg.edu/business/studentgroups/'),
            ('Augsburg Student Accounting Organization (ASAO) — advisor PHYLLIS KAPETANAKIS, with a direct line',
             'Chartered Student Organization, 2015-16. Provides opportunities for students to "enhance their '
             'accounting experience into a professional career, certification, or interest in the field beyond '
             'the classroom." Advisor Phyllis Kapetanakis, kapetanp@augsburg.edu, 612-330-1134. Second-best '
             'club door.',
             'https://www.augsburg.edu/business/studentgroups/'),
            ('⚠ "Augsburg University economics club" — listed with NO DETAILS AT ALL',
             'The Business Administration and Economics student-groups page lists an economics club by name '
             'but with no description, advisor, officers or status. Whether it is currently active is UNKNOWN. '
             '☎ Campus Life (612) 330-1418.',
             'https://www.augsburg.edu/business/studentgroups/'),
            ('⚠ NO BLOCKCHAIN / CRYPTO / WEB3 CLUB AT AUGSBURG',
             'None found. The full directory is AUGGIE LIFE (https://augsburg.campuslabs.com/engage/) which is '
             'JAVASCRIPT-RENDERED and did not enumerate to research tooling. Campus Life student '
             'organizations landing page: '
             'https://www.augsburg.edu/campuslife/campus-involvement/groups/. Starting a new organization: '
             'https://www.augsburg.edu/campuslife/campus-involvement/groups/start-new-student-organization/',
             'https://www.augsburg.edu/campuslife/campus-involvement/groups/'),
            ('Augsburg Entrepreneur Cup',
             'A business-plan competition run by the Business Administration and Economics department — not a '
             'club but a recurring programme, and the most natural venue for a fintech-flavoured sponsorship '
             'or judging role. No dates published.',
             'https://www.augsburg.edu/business/auggiecup/')],
  'faculty': [('⚠⚠ University Events — books the $75/day external vendor table',
               'THE NUMBER TO CALL AT AUGSBURG, AND THE CHEAPEST CONFIRMED TABLE IN MINNESOTA IS ON THE OTHER '
               'END OF IT. Two days\' notice, Christensen Center Lobby, 8:00 a.m.–4:30 p.m., $75 flat, +$10 '
               'per additional table. Ask three things: (1) book the table, (2) does a paid external vendor '
               'need a student sponsor present, or does that clause only govern sponsored tables, and (3) is '
               'any certificate of insurance required — the vendor policy is silent and the "Hosting External '
               'Events" page could not be retrieved.',
               'University Events',
               'events@augsburg.edu · (612) 330-1104',
               'https://sites.augsburg.edu/events/policies/vendor-tabling-policy/'),
              ('⚠ Campus Life — owns the Involvement Fair and Auggie Life',
               'The office that runs the Student Organizations Fall Involvement Fair each semester in the '
               'Christensen Center Lobby, and the only route to the Fall 2026 date since the live event page '
               'still shows August 2024. Also owns Auggie Life, the JavaScript-rendered org directory. ⚠ NO '
               'INDIVIDUAL CAMPUS LIFE STAFF MEMBER IS NAMED on any retrievable page — only this general line.',
               'Campus Life',
               'campuslife@augsburg.edu · (612) 330-1418',
               'https://www.augsburg.edu/campuslife/campus-involvement/'),
              ('⚠ Marc Isaacson — advisor, Augsburg Business Organization',
               'A NAMED FACULTY ADVISOR WITH A PUBLISHED DIRECT LINE — rare at a private college and the '
               'fastest route to Augsburg business students. ABO "promotes the study of business at Augsburg" '
               'and brings together students interested in "discussing and advocating for business," which is '
               'a speaking invitation waiting to be asked for.',
               'Business Administration and Economics',
               'isaacson@augsburg.edu · (612) 330-1194',
               'https://www.augsburg.edu/business/studentgroups/'),
              ('Phyllis Kapetanakis — advisor, Augsburg Student Accounting Organization',
               'Second named advisor with a direct line. ASAO students are pursuing professional certification '
               '— a receptive audience for a digital-assets accounting/regulatory talk, especially with '
               'Minnesota\'s new crypto-custody law in effect since Aug 1, 2026.',
               'Business Administration and Economics',
               'kapetanp@augsburg.edu · (612) 330-1134',
               'https://www.augsburg.edu/business/studentgroups/'),
              ('Augsburg University — main line (2211 Riverside Avenue, Minneapolis)',
               'General switchboard, cited on the University Events general-information page as the route to '
               'the Director of University Events. Also: university calendar management, '
               'universitycalendar-mgmt@augsburg.edu (no number published), and events@augsburg.edu for '
               'disability accommodations at events. A–Z directory at https://www.augsburg.edu/az/.',
               'University',
               '(612) 330-1000 (main line)',
               'https://sites.augsburg.edu/events/policies/university-events-general-information/'),
              ('(Director of University Events — individual)',
               'NOT CONFIRMED — the general-information page refers to "the Director of University Events" but '
               'names no one and gives no direct line. No individual University Events staff member is named '
               'on any retrievable page. Look up here; reach via (612) 330-1104.',
               'University Events',
               'events@augsburg.edu · no individual number published — look up here; use (612) 330-1104',
               'https://sites.augsburg.edu/events/policies/university-events-general-information/'),
              ('(Business/economics faculty on digital assets)',
               'NOT CONFIRMED — NO Augsburg faculty member could be confirmed as working on blockchain, '
               'cryptocurrency, fintech or digital assets. The Business Administration and Economics '
               'department is at https://www.augsburg.edu/business/. Isaacson and Kapetanakis are the two '
               'named, phone-reachable faculty at this campus; start with them. Look up here.',
               'Business Administration and Economics',
               'no number published — look up here; use (612) 330-1000',
               'https://www.augsburg.edu/business/')],
  'courses': [('(No crypto/fintech course found)',
               'NO blockchain, cryptocurrency or fintech course was confirmed at Augsburg. Business '
               'Administration and Economics: https://www.augsburg.edu/business/. The curricular hook here is '
               'not a course — it is the AUGSBURG ENTREPRENEUR CUP business-plan competition '
               '(https://www.augsburg.edu/business/auggiecup/) and the two named club advisors.',
               'https://www.augsburg.edu/business/')],
  'events': [('⚠ Student Organizations Fall Involvement Fair — PAGE SHOWS AUG 2024, DATE STALE',
              'Christensen Center Lobby, roughly 11:00 a.m.–12:30 p.m. Verbatim: "Each semester, Campus Life '
              'holds an Involvement Fair for all student organizations!" ⚠ THE LIVE EVENT PAGE STILL SHOWS '
              'AUGUST 29, 2024 — a two-year-old listing. Expect late August or the first week of September '
              '2026 given the Sep 2 start. Will post to https://calendar.augsburg.edu/ and Auggie Life. '
              '☎ Campus Life (612) 330-1418. Accommodations: events@augsburg.edu; calendar management: '
              'universitycalendar-mgmt@augsburg.edu.',
              'https://calendar.augsburg.edu/event/student-organizations-fall-involvement-fair/'),
             ('Augsburg Entrepreneur Cup',
              'Business-plan competition run by the Business Administration and Economics department. ⚠ Fall '
              '2026 dates not published. The most natural venue at Augsburg for a sponsorship, judging role or '
              'prize — a private-ish departmental competition rather than a campus tabling event, so it sits '
              'outside the vendor policy entirely.',
              'https://www.augsburg.edu/business/auggiecup/'),
             ('University calendar',
              'Where the Involvement Fair date and other Fall 2026 events will post. ⚠ Returned only an '
              'August 19 – September 2 event window to research tooling with no Fall 2026 fair listing.',
              'https://calendar.augsburg.edu/'),
             ('(No hackathon or blockchain event)',
              'NO hackathon, blockchain conference, research centre or crypto legislative activity was found '
              'connected to Augsburg University.',
              'https://www.augsburg.edu/studentlife/')],
  'play': 'Buy the $75 table and do it on two days\' notice. Augsburg publishes the cheapest and fastest '
          'outside-vendor route in Minnesota: "Each vendor will be charged a flat-rate of $75.00 per day to '
          'display anytime between 8 a.m. – 4:30 p.m.," Christensen Center Lobby, Monday–Friday, additional '
          'tables $10/day, minimum two days\' advance notice, Saturdays by request. That is under half UMD\'s '
          '$160 and below St. Cloud\'s $85, with the shortest lead time of any paid table in this file. Call '
          'University Events at (612) 330-1104. ⚠ ASK ONE CLARIFYING QUESTION ON THAT CALL: the policy says "a '
          'member of the organization sponsoring the table must be present during all tabling times in order '
          'to validate sponsorship" — confirm that this governs SPONSORED tables only and that a straight paid '
          'external vendor may staff its own table. Also ask whether any certificate of insurance is required, '
          'because the vendor policy is silent and the "Hosting External Events at Augsburg" page could not be '
          'retrieved. ⚠ DESIGN AROUND ONE PROHIBITION: "No credit card promotions" — almost certainly '
          'downstream of Minn. Stat. s 135A.145 — so run an education-and-email table, no card capture, and '
          'have the line ready that DGD is not a card issuer under 15 U.S.C. s 1602. Wrapped candy is '
          'expressly allowed, everything else edible is not. Skip the Involvement Fair: its page still shows '
          'August 2024, and a bought table in the same lobby on a day of your choosing beats competing with '
          'student groups for one morning. Two named advisors with direct lines make the club side easy too — '
          'Marc Isaacson (612) 330-1194 for the Augsburg Business Organization and Phyllis Kapetanakis '
          '(612) 330-1134 for the Student Accounting Organization. Augsburg is 1.5 miles from the U of M Twin '
          'Cities, so pair the two in a single Minneapolis day.',
  'gaps': ['⚠ Does a PAID external vendor need a student sponsor present, or does the "member of the '
           'organization sponsoring the table must be present" clause govern sponsored tables only? This '
           'decides whether Augsburg is a two-day turnaround or a three-week courtship. ☎ University Events '
           '(612) 330-1104. https://sites.augsburg.edu/events/policies/vendor-tabling-policy/',
           '⚠ Is a certificate of insurance required, and at what limit? The vendor policy is SILENT and the '
           '"Hosting External Events at Augsburg" page '
           '(https://sites.augsburg.edu/events/hosting-external-events-at-augsburg/) COULD NOT BE RETRIEVED. '
           '☎ (612) 330-1104.',
           '⚠ FALL 2026 INVOLVEMENT FAIR DATE — the live event page still shows AUGUST 29, 2024. ☎ Campus Life '
           '(612) 330-1418. https://calendar.augsburg.edu/event/student-organizations-fall-involvement-fair/',
           'Deposit and cancellation terms for the $75 table — not published. ☎ (612) 330-1104.',
           'Whether the "Augsburg University economics club" listed on the business student-groups page is '
           'currently active — it is listed with no details at all. '
           'https://www.augsburg.edu/business/studentgroups/',
           'Whether Augsburg has any blockchain or crypto student organization — Auggie Life '
           '(https://augsburg.campuslabs.com/engage/) is JAVASCRIPT-RENDERED and did not enumerate.',
           'The name and direct line of the Director of University Events — referenced but never named on any '
           'page. https://sites.augsburg.edu/events/policies/university-events-general-information/',
           'Augsburg Entrepreneur Cup Fall 2026 dates and whether outside sponsorship or judging is possible. '
           'https://www.augsburg.edu/business/auggiecup/'],
  'note': 'Augsburg is the best value-per-dollar stop in Minnesota: $75 a day, two days\' notice, in a lobby '
          '1.5 miles from the U of M Twin Cities campus, at a university whose written policy treats outside '
          'vendors as a normal category rather than an exception. ⚠ Note the split end dates — day classes '
          'finish Dec 11 but full-semester classes run to Dec 18, so evening and weekend cohorts are still on '
          'campus the week of Dec 14. Private, ELCA Lutheran, so no public-forum obligation — but the priced '
          'invitation makes that irrelevant.',
 },
]

# (iso_date, display_date, campus, action, detail, url, contact)
DEADLINES = [

 ('2026-08-12', 'Aug 12, 2026', 'U of Minnesota Twin Cities',
  '⚠⚠ CALL TODAY — EXPLORE U BOOTH STATUS UNRESOLVED, EVENT IS 24 DAYS OUT',
  'The ONLY paid door at the flagship. Explore U is Sat Sep 5, 1:00–4:30pm, Huntington Bank Stadium: Maroon '
  '$600, Gold $1,150, additional booths $550. ⚠ THE TWO OTE PAGES CONTRADICT EACH OTHER — the sponsors page '
  'says "Table space goes on sale in LATE SPRING," the Explore U page still says registration "will open in '
  'the coming weeks." One of them is stale. If booths are gone, ask immediately about the $6,000-minimum '
  'Orientation corporate sponsorship, which explicitly includes tabling and reaches 15,000 participants.',
  'https://ote.umn.edu/about-ote/sponsors-partners/explore-u-event',
  'Orientation & Transition Experiences · (612) 624-1979'),

 ('2026-08-15', 'Aug 15, 2026', 'U of Minnesota Duluth',
  '⚠⚠ KIRBY EXTERNAL TABLING RESERVATIONS OPEN — $160/table, 3 DAYS OUT',
  '"Fall reservations open after August 15." $160 per table per day, one table per day, Kirby Commons '
  '9am–3pm, 6-foot table + 2 chairs + outlet. Submit the Non-UMD Guests Space Request Form 2–4 weeks ahead; '
  'confirmation in 3 business days. ⚠ A signed Facility Use Agreement AND liability insurance are due ONE WEEK '
  'BEFORE the date — the insurance dollar limit is published nowhere, so ask when you book. Target a day '
  'adjacent to the Business Career Fair on Sep 24.',
  'https://kirby.d.umn.edu/policy-tabling-non-universityexternal-guest',
  'Jodi Nelson, KSC Office Manager · (218) 726-7169 | reservations (218) 726-7163'),

 ('2026-08-20', 'Aug 20, 2026', 'Minnesota State Mankato',
  '⚠ CLUB MAVERICK (Welcome Week Aug 20–23) — TIME, LOCATION AND ELIGIBILITY ALL UNPUBLISHED',
  'The student-organization event of MNSU Welcome Week, four days before classes begin Aug 24. Nothing on any '
  'retrievable page gives a time, a location, or whether an outside organization may participate; the per-day '
  'detail pages that exist are for 2024 and a /thursday-august-20/ page 404s. ⚠ Do NOT budget for '
  'Choose-A-Palooza (Fri Aug 21, 1pm, Otto Rec Center Gym) as a substitute — it is a scavenger hunt of campus '
  'offices, not an org fair. Ask the same call whether CSU 219 will approve an outside table and at what cost.',
  'https://mankato.mnsu.edu/university-life/centennial-student-union/welcome-week/',
  'Gregory Wilkins · gregory.wilkins@mnsu.edu · (507) 389-6076 | Bill Tourville (CSU 219) · (507) 389-2223'),

 ('2026-08-22', 'Aug 22, 2026', 'Metropolitan State',
  '⚠ CLASSES BEGIN — ON A SATURDAY. EARLIEST START IN MINNESOTA.',
  'First session and full session courses begin Sat Aug 22. No other Minnesota campus starts on a weekend, and '
  'the reason is the audience: heavily commuter, heavily adult-learner, three scattered locations (St. Paul, '
  'Minneapolis, Brooklyn Park), two concurrent 8-week sessions. ⚠ AUDIENCE MISMATCH — no welcome week, no '
  'involvement fair, and no Student Life web page exists at all. Treat as a phone call, not a visit.',
  'https://www.metrostate.edu/academics/calendar/fall-2026',
  '651.793.1300 option 5 (Gateway Student Services)'),

 ('2026-08-24', 'Aug 24, 2026', 'Minnesota State Mankato',
  'Classes begin — earliest wave, 15 days ahead of the U of M Twin Cities',
  'No fall break at Mankato. Thanksgiving Nov 26–29; finals Dec 7–11; semester ends Dec 11 (regular '
  'instruction likely ends ~Dec 4). Add/drop date is NOT published on either official calendar.',
  'https://admin.mnsu.edu/academic-affairs/university-calendars/academic-calendars/fall-term-calendar/',
  '(507) 389-1000 (main line)'),

 ('2026-08-24', 'Aug 24, 2026', 'St. Cloud State',
  'Classes begin (day and evening) — ⚠ SHORTEST USABLE TERM IN THE STATE',
  'St. Cloud runs Aug 24 to Dec 4 only — classes end twelve days before the U of M Twin Cities and a week '
  'before Duluth. No fall break. Thanksgiving Nov 25–27. Finals Dec 7–10, ending at NOON Dec 10. If the '
  'December leg runs west to east, St. Cloud must come first or not at all.',
  'https://www.stcloudstate.edu/events/academic/academic-fy27.aspx',
  'Lisa Johnson, Scheduling Coordinator · (320) 308-2074'),

 ('2026-08-24', 'Aug 24, 2026', 'Winona State',
  'Classes begin',
  'Student break day Wed Nov 25; Thanksgiving Nov 26–27; finals Dec 7–10; commencement Dec 11. Calendar '
  'revised 04/21/2026. ⚠ The PDF prints overlapping "last day of classes Dec 10" and "finals Dec 7–10" rows — '
  'regular instruction likely ends ~Dec 4.',
  'https://www.winona.edu/wp-content/uploads/2026/05/Fall-2026-Academic-Calendar.pdf',
  'George Micalone, Director Student Union & Activities · (507) 457-5312'),

 ('2026-08-26', 'Aug 26, 2026', 'U of Minnesota Duluth',
  'Bulldog Welcome Week begins (Aug 26–30) — move-in Aug 26–27, programming from Aug 27',
  'Required for new freshmen; cost included in the confirmation/orientation fee. ⚠ NO distinct involvement or '
  'organization fair with a published date exists at UMD — Kirby sells tabling by the day instead, which is '
  'better. ⚠ The FAQ page carries a stale "Fall 2025" line inside otherwise-2026 copy. Since external '
  'bookings reopen Aug 15, a paid table during Welcome Week is possible if booked immediately.',
  'https://kirby.d.umn.edu/student-activities/bulldog-beginnings/bulldog-welcome-week/faqs',
  'bb-kirby@d.umn.edu · Kirby (218) 726-7163'),

 ('2026-08-28', 'Aug 28, 2026', 'Winona State',
  '⚠ ADD/DROP DEADLINE — last day to add and to drop with full refund',
  'The earliest and cleanest add/drop date in the state; only five Minnesota campuses in this set publish one '
  'at all. Same day: Metro State\'s last date to drop first-session and full-session courses with a refund.',
  'https://www.winona.edu/wp-content/uploads/2026/05/Fall-2026-Academic-Calendar.pdf',
  '(507) 457-5310 (Student Union & Activities)'),

 ('2026-08-31', 'Aug 31, 2026', 'U of Minnesota Duluth',
  '⚠ CLASSES BEGIN — EIGHT DAYS BEFORE THE TWIN CITIES, SAME UNIVERSITY',
  'UMD does NOT follow the Twin Cities calendar despite sharing the Board of Regents. Anyone assuming "the '
  'U of M starts Sep 8" arrives in Duluth a week and a half late. ⚠ UMD also has a FALL BREAK the Twin Cities '
  'does not: Oct 29–30. Thanksgiving Nov 26–27; classes end Dec 11; finals Dec 14–18. 70 instructional days.',
  'https://www.d.umn.edu/calendar/academic_cal.html',
  'Kirby Student Center · (218) 726-7163'),

 ('2026-08-31', 'Aug 31, 2026', 'Macalester',
  'New Student Orientation + Resource Fair, 10:00am (Library Open House noon)',
  '⚠ This is an ORIENTATION RESOURCE EVENT, not a student-organization fair, and it sits eight days before '
  'classes begin Sep 8. No fall org fair date is published anywhere at Macalester — and it would not matter: '
  '"Macalester does not permit fundraising by outside organizations on its campus or via college affiliated '
  'events or programs."',
  'https://www.macalester.edu/leadership-engagement/programming-involvement/',
  'Center for Student Leadership & Engagement · (651) 696-6569'),

 ('2026-09-02', 'Sep 2, 2026', 'St. Cloud State',
  '⚠⚠ MAINSTREET INVOLVEMENT FAIR — and the page counts "COMMUNITY PARTNERS"',
  '"More than 150 departments, services, student organizations, and community partners," on the campus walkway '
  'near Atwood. Weekday check PASSES — Sep 2, 2026 is a Wednesday — so the date is current, though the page '
  'carries 2025 photography. Time and cost NOT published. ⚠ ASK ONE QUESTION: is Mainstreet the same as an $85 '
  'promotional-space booking, or a separate track? Sign-up via HuskiesConnect.',
  'https://www.stcloudstate.edu/campusinvolvement/annual-events/mainstreet.aspx',
  'Carly Frederick · (320) 308-2205 | Lisa Johnson · (320) 308-2074'),

 ('2026-09-02', 'Sep 2, 2026', 'Augsburg',
  'Classes begin — 1.5 miles from the U of M Twin Cities campus',
  'Add/drop without notation Sep 9; midterm break Oct 23–25; Thanksgiving Nov 26–29. ⚠ SPLIT END DATES: day '
  'classes end Dec 11 with finals Dec 14–17, but FULL-SEMESTER classes run to Dec 18 — evening and weekend '
  'cohorts are still on campus the week of Dec 14.',
  'https://www.augsburg.edu/registrar/calendars/',
  'University Events · events@augsburg.edu · (612) 330-1104'),

 ('2026-09-05', 'Sep 5, 2026', 'U of Minnesota Twin Cities',
  '⚠⚠ EXPLORE U — THE ONLY PAID DOOR AT THE FLAGSHIP. 1:00–4:30pm, Huntington Bank Stadium.',
  'Over 4,000 new and current student leaders, three days before classes start, on move-in weekend. The '
  'University\'s own words: "Explore U is a great opportunity for LOCAL BUSINESSES AND ORGANIZATIONS to access '
  'incoming first-year and incoming transfer students." Maroon $600 · Gold $1,150 · additional booths $550 '
  '(Gold only) · partial payment via trade up to 50%. Every other route at UMN is closed by a flat ban on '
  'non-University entities promoting goods or services, a named anti-fronting rule, and a bar on student '
  'groups reserving contact tables for external organizations.',
  'https://ote.umn.edu/about-ote/sponsors-partners/explore-u-event',
  '(612) 624-1979'),

 ('2026-09-08', 'Sep 8, 2026', 'U of Minnesota Twin Cities',
  'Classes begin (day after Labor Day) — ⚠ NO FALL BREAK, eleven straight weeks of full density',
  'Sep 8 to Nov 25 with no October break — the longest uninterrupted access window of any campus in this set. '
  'Last day of instruction Dec 16; study day Dec 20; finals Dec 17–19 and Dec 21–23; term ends Dec 23. '
  '⚠ Thanksgiving Nov 26–27 is confirmed only on a third-party aggregator, not on any umn.edu page.',
  'https://asr.umn.edu/2026-27-twin-cities-and-rochester-calendar',
  'Student Unions & Activities · (612) 626-6919'),

 ('2026-09-08', 'Sep 8, 2026', 'Macalester',
  'Classes begin — same day as the U of M, one mile from St. Thomas',
  'Add/drop Sep 18; fall break Oct 15–18; Thanksgiving Nov 25–29; classes end Dec 14; finals Dec 16–19. '
  '⚠ ACCESS 1 — the only flat "no" in Minnesota. Plan a non-commercial ODE speaker session or skip.',
  'https://www.macalester.edu/registrar/academic-calendars/',
  'Joyce Minor (Investment Banking & Securities Analysis) · (651) 696-6863'),

 ('2026-09-08', 'Sep 8, 2026', 'Carleton College',
  'New Student Week begins (Sep 8–13) — the likeliest home for the unpublished activities fair',
  'Classes begin Mon Sep 14. No Carleton fall activities fair date is published anywhere; the Student '
  'Activities Office runs organization programming but publishes no fair page. ☎ (507) 222-4462.',
  'https://www.carleton.edu/student-activities/guide/',
  'Student Activities Office · sao@carleton.edu · (507) 222-4462'),

 ('2026-09-09', 'Sep 9, 2026', 'University of St. Thomas',
  '⚠ CLASSES BEGIN — LATEST SEMESTER START IN MINNESOTA',
  'Sixteen days after the Minnesota State wave. Add/drop Sep 22; mid-term break Oct 30 – Nov 2; Thanksgiving '
  'break begins Nov 25 with classes resuming Nov 30; classes end Dec 15; study day Dec 16 with finals starting '
  '5:30pm; finals end Dec 22 — the longest tail in the state. ⚠ Same day: Augsburg add/drop deadline.',
  'https://www.stthomas.edu/academics/calendars/2026-2027-undergraduate/index.html',
  'Mary Beth Pickett, Employer Partnerships · (651) 962-6777'),

 ('2026-09-14', 'Sep 14, 2026', 'Carleton College',
  '⚠⚠ CLASSES BEGIN 8:30am — LATEST START IN THE STATE, AND THE CLOCK STARTS NOW',
  'TRIMESTER SYSTEM: three 10-week terms, three courses per term. Fall term is Sep 14 – Nov 23 ONLY. Add/drop '
  'Sun Sep 20 11:59pm — a six-day window. Midterm break Oct 17–19. ⚠ The sponsorship conversation must start '
  'in week one: a Carleton department or chartered organization must book the Sayles-Hill table for you in EMS '
  'with a Carleton login, 24 hours ahead — "There is no fee if you are sponsored."',
  'https://www.carleton.edu/student-activities/guide/event-promotion/table/',
  'Student Activities Office · sao@carleton.edu · (507) 222-4462'),

 ('2026-09-17', 'Sep 17, 2026', 'U of Minnesota Duluth',
  'STEM-Fest Career Fair, 10:00am — the technical audience',
  '"Engineering, science, math, data, and computer science positions." ⚠ Employer registration COST and '
  'DEADLINE are NOT published for any UMD fair. Pair with a $160 Kirby Commons table booked the same week.',
  'https://calendar.d.umn.edu/event/105337-stem-fest-career-fair',
  'Kirby / Career Services · (218) 726-7163'),

 ('2026-09-22', 'Sep 22, 2026', 'U of Minnesota Twin Cities',
  '⚠ FALL ACTIVITIES FAIR (Minneapolis), 11:00am–2:00pm, Coffman Memorial Union — STUDENT GROUPS ONLY',
  'Registration open now at https://z.umn.edu/activitiesfairsregistration, closes when full. Verbatim: '
  '"Explore U and the Fall and Spring Activities Fairs are for REGISTERED STUDENT GROUPS ONLY." Free. ⚠ NOT '
  'AVAILABLE TO DGD — and a student group may not reserve a contact table on your behalf (Art. XVI s 7 Subd 2) '
  'nor may your personnel stand at one during commercial activity. Listed so nobody wastes a day on it. '
  'St. Paul edition Wed Sep 23, 11:00am–1:00pm, St. Paul Student Center. Same day: St. Thomas add/drop.',
  'https://sua.umn.edu/student-group-opportunities',
  'SUA · (612) 626-6919'),

 ('2026-09-24', 'Sep 24, 2026', 'U of Minnesota Duluth',
  '⚠ BUSINESS CAREER FAIR, 10:00am — THE BEST SINGLE DAY AT UMD',
  '"Accounting & finance, economics & health care management, management studies, marketing & sales." The '
  'finance audience concentrated in one building, with employers already paying to be there, one week after '
  'STEM-Fest. Book the $160 Kirby Commons table for the same day or the day after. ⚠ Cost and deadline not '
  'published.',
  'https://calendar.d.umn.edu/event/105367-business-career-fair',
  'Jodi Nelson · (218) 726-7169 | Career Services (218) 726-7163'),

 ('2026-09-28', 'Sep 28, 2026', 'Minnesota State Mankato',
  'Homecoming week begins — Kick-Off 11:00am at the Centennial Student Union',
  'Mavathon Blood Drive Sep 30, 9:00am, CSU Ballroom; Lip Sync and Coronation Oct 1, 7:30pm, Bresnan Arena; '
  'Homecoming Carnival, football and volleyball Oct 2–3. The Kick-Off is in the CSU — exactly where a '
  'CSU-219-approved table would sit.',
  'https://mankato.mnsu.edu/university-life/activities-and-organizations/student-activities-events/',
  'Gregory Wilkins · (507) 389-6076'),

 ('2026-10-12', 'Oct 12, 2026', 'Metropolitan State',
  'First 8-week session ENDS — population churns before the second session starts Oct 14',
  'Metro State runs two concurrent 8-week sessions alongside a full session, so the student body on any given '
  'week is not stable. Second Session runs Oct 14 – Dec 13.',
  'https://www.metrostate.edu/academics/calendar/fall-2026',
  '651.793.1300 option 5'),

 ('2026-10-23', 'Oct 23, 2026', 'U of Minnesota Twin Cities',
  'Government and Nonprofit Career Fair, 11:00am–3:00pm, at UMN Twin Cities',
  '⚠ THE ONLY TWIN CITIES CAREER-FAIR DATE RETRIEVABLE ANYWHERE IN THIS RESEARCH — and it was found on UMD\'s '
  'employer page, not the flagship\'s, because UMN routes all employer registration through Handshake '
  '(login-gated) and disclaims that fairs "are not guaranteed to occur until they are listed on Handshake." '
  'Same weekend: Augsburg midterm break Oct 23–25.',
  'https://career.d.umn.edu/employers/career-fairs',
  'UMD Career Services · (218) 726-7163'),

 ('2026-10-29', 'Oct 29, 2026', 'U of Minnesota Duluth',
  '⚠ FALL BREAK Oct 29–30 — the Twin Cities does NOT have one',
  'Do not schedule the last week of October in Duluth. Macalester\'s fall break is Oct 15–18 and Carleton\'s '
  'midterm break is Oct 17–19; St. Thomas breaks Oct 30 – Nov 2.',
  'https://www.d.umn.edu/calendar/academic_cal.html',
  '(218) 726-7163'),

 ('2026-11-11', 'Nov 11, 2026', 'Metropolitan State',
  'Veterans Day — no classes, buildings CLOSED',
  'Distinctive: most Minnesota campuses stay open on Veterans Day. Metro State closes entirely.',
  'https://www.metrostate.edu/academics/calendar/fall-2026',
  '651.793.1300'),

 ('2026-11-18', 'Nov 18, 2026', 'Carleton College',
  '⚠⚠ LAST DAY OF CLASSES — CARLETON\'S ENTIRE WINDOW CLOSES HERE',
  'Reading days Nov 19–20; finals Nov 21–23; TERM ENDS MON NOV 23. There is NO Thanksgiving break because the '
  'term is already over, and THERE IS NO DECEMBER WINDOW AT CARLETON AT ALL. While every other Minnesota '
  'campus runs finals in mid-December, Carleton has been empty for three weeks. Anyone planning "hit '
  'Northfield in early December" will find nobody there.',
  'https://carleton-wp-production.s3.amazonaws.com/uploads/sites/740/2026/02/Academic-Calendar-26-27_detailed-1.pdf',
  'Student Activities Office · (507) 222-4462'),

 ('2026-12-04', 'Dec 4, 2026', 'St. Cloud State',
  '⚠ LAST DAY OF CLASSES — EARLIEST CLASS END IN MINNESOTA',
  'Twelve days before the U of M Twin Cities and a week before Duluth. Finals Dec 7–10, ending at NOON Dec 10; '
  'commencement Dec 10 (graduate) and Dec 11 (undergraduate). Mankato and Winona close in the same week.',
  'https://www.stcloudstate.edu/events/academic/academic-fy27.aspx',
  'Lisa Johnson · (320) 308-2074'),

 ('2026-12-11', 'Dec 11, 2026', 'U of Minnesota Duluth',
  'Last day of fall semester classes (finals Dec 14–18)',
  'Same day: Mankato semester ends and commencement is Dec 12; Winona commencement; Augsburg DAY classes end '
  '(full-semester classes run to Dec 18).',
  'https://www.d.umn.edu/calendar/academic_cal.html',
  '(218) 726-7163'),

 ('2026-12-13', 'Dec 13, 2026', 'Metropolitan State',
  'Semester ends — on a SUNDAY',
  'Second session and full session courses end Sun Dec 13; degree conferral the same day; grades due Wed '
  'Dec 16 at 11:59pm; holiday closure Dec 21–31.',
  'https://www.metrostate.edu/academics/calendar/fall-2026',
  '651.793.1300'),

 ('2026-12-16', 'Dec 16, 2026', 'U of Minnesota Twin Cities',
  'Last day of instruction — the latest-running campus in the state alongside St. Thomas',
  'Finals Dec 17–19 and Dec 21–23; study day Dec 20; term ends Dec 23. St. Thomas classes end Dec 15 with '
  'finals to Dec 22; Macalester finals end Dec 19; Augsburg full-semester classes end Dec 18.',
  'https://asr.umn.edu/2026-27-twin-cities-and-rochester-calendar',
  '(612) 626-6919'),

 ('', 'Monitor', 'U of Minnesota Twin Cities',
  '⚠ MINNEHACK 2027 SPONSORSHIP — buy in NOW, while the committee forms',
  'MinneHack is a February event (2026 edition ran Feb 14–15 in Coffman, Presidents and Mississippi Rooms), so '
  'there is NO Fall 2026 hackathon at UMN. But it is a PRIVATE STUDENT-RUN EVENT that sits entirely outside '
  'the University\'s commercial-use rules in a way tabling never can — 300+ participants from ~100 schools. '
  'Verbatim: "If you are interested in sponsoring MinneHack in future years, contact us at acm@umn.edu." '
  '⚠ Tier PRICES are not published; 2026 named Silver and Bronze without numbers. Highest-leverage '
  'non-tabling spend in Minnesota.',
  'https://www.minnehack.com/sponsors/',
  'ACM at UMN · acm@umn.edu'),

 ('', 'Monitor', 'University of St. Thomas',
  '⚠ "WEB3 IMPACT ON LAW AND SOCIETY" CONFERENCE — the state\'s only blockchain conference, date unknown',
  'Hosted jointly by the Minnesota Blockchain Initiative, the UST School of Law and the St. Thomas Law '
  'Journal. ⚠ Its own site, mnweb3lawconference.com, is ROBOTS-BLOCKED AND DNS-UNRESOLVABLE to research '
  'tooling — date, venue, registration and sponsorship tiers are ALL UNVERIFIED. Get them from the Minnesota '
  'Blockchain Initiative, which also runs monthly Twin Cities Spotlight Meetups and is named as a '
  'collaborator of the UMN Blockchain Club. This is the best non-campus entry point into the entire Minnesota '
  'student blockchain scene.',
  'https://www.mnblockchain.org/',
  'connect@mnblockchain.org'),

 ('', 'Monitor', 'Metropolitan State',
  '⚠ CLOSE THE BIGGEST POLICY GAP IN THE FILE — Metro State\'s solicitation policy could not be found at all',
  'No Metro State solicitation, tabling, facilities-use or outside-vendor policy exists on any retrievable '
  'page; /student-life and /students/support/student-life both 404 and the Student Life and Leadership '
  'Development office has NO website. The access rating of 3 is PROVISIONAL for that reason — it could be a 5 '
  'or a 1. Ten minutes from Macalester, fifteen from the U of M: one phone call closes it.',
  'https://www.metrostate.edu/about/contact',
  '651.793.1300 option 5 (Gateway Student Services)'),

 ('', 'Monitor', 'Winona State',
  '⚠ THE MOST STALE-PAGED CAMPUS IN THE FILE — every Fall 2026 fair date must come by phone',
  'The "Promote a Club" page still shows the 2023 schedule (Welcome Weekend Aug 18, I LOVE WSU Day Sep 6, '
  'Wellness Fair Sep 26, Homecoming Oct 13 — DO NOT USE THESE). The Welcome Week page shows 2018 content. The '
  'events calendar returns HTTP 403. The current schedule sits behind a StarID login. Recurring pattern: four '
  'Courtyard fairs a year, registration ~4 days prior via WarriorSpace. Also unpublished: third-party rate '
  'card, insurance limit, deposit and cancellation terms.',
  'https://www.winona.edu/student-life/clubs/student-senate/manage-a-club/promote-a-club/',
  'Alex Thompson (fairs) · (507) 457-5584 | George Micalone (policy) · (507) 457-5312'),

 ('', 'Monitor', 'Augsburg',
  '⚠ FALL 2026 INVOLVEMENT FAIR DATE — the live page still shows AUGUST 29, 2024',
  'Christensen Center Lobby, ~11:00am–12:30pm, every semester per Campus Life. Expect late August or the first '
  'week of September 2026. ⚠ BUT THE FAIR IS THE WORSE OPTION: the vendor policy lets DGD buy a table in the '
  'SAME LOBBY on any weekday for $75 flat with two days\' notice — the cheapest and fastest paid table in '
  'Minnesota. Ask on the same call whether a paid vendor needs a student sponsor present, and whether any '
  'certificate of insurance is required (the policy is silent and the External Events page could not be '
  'retrieved).',
  'https://sites.augsburg.edu/events/policies/vendor-tabling-policy/',
  'University Events · events@augsburg.edu · (612) 330-1104 | Campus Life (612) 330-1418'),

 ('', 'Monitor', 'U of Minnesota Twin Cities',
  '⚠ VERIFY VIVIAN FANG IS STILL AT CARLSON BEFORE USING HER NAME',
  'Vivian Fang was Carlson\'s Honeywell Professor in Accounting and is the U of M\'s public voice on '
  'cryptocurrency and NFTs. Her LinkedIn now lists her as Richard E. Jacobs Chair in Finance at INDIANA '
  'UNIVERSITY KELLEY SCHOOL OF BUSINESS. Using a stale affiliation would burn the best-known crypto voice at '
  'the flagship. Also ask the same call about FINA 5125/6125 "Cryptocurrency, Blockchain, and Their Business '
  'Applications" — offered EVERY SPRING (not Fall 2026), and its syllabus already imports "industry expert '
  'guest lectures."',
  'https://carlsonschool.umn.edu/departments/accounting/contact',
  'Carlson Accounting · (612) 624-6506 | Carlson Finance · (612) 624-6506'),

 ('', 'Monitor', 'University of St. Thomas',
  '⚠ DOES FINC 315 "CRYPTOCURRENCY AND BLOCKCHAIN" RUN IN FALL 2026?',
  'The ONLY dedicated undergraduate crypto course in Minnesota — 2 credits, required for the FinTech '
  'certificate alongside FINC 314 and FINC 316, lead faculty Dr. Jiang (Will) Zhang. A 2-credit course often '
  'runs as a half-term module, which would put it in the Oct–Dec window. ⚠ No email or phone is published for '
  'Dr. Zhang and the Opus faculty directory is a search UI that returned no profile data — DO NOT GUESS AN '
  'ADDRESS. Live class finder: https://classes.aws.stthomas.edu/ (term code 202630).',
  'https://www.stthomas.edu/academics/undergraduate/financial-technology-fintech-certificate/',
  'OPUS College of Business · (651) 962-4200'),

 ('', 'Monitor', 'U of Minnesota Twin Cities',
  '⚠ REACH THE UMN BLOCKCHAIN CLUB — all three of its own channels are closed to outsiders',
  'The club is ACTIVE (GopherLink group #4465) and is the best student-side asset in Minnesota, drawing '
  '"primarily from computer science and business students" and running beginner-friendly lectures — an '
  'ideal speaker venue. ⚠ BUT: GopherLink is LOGIN-GATED, and umnblockchain.org AND umnbc.org are BOTH '
  'ROBOTS-BLOCKED. A club president is named in a Nov 2025 Minnesota Daily article; that name is nearly a '
  'year old and rosters rotate — DO NOT USE IT. Route in through the Minnesota Blockchain Initiative, named '
  'in the same article as a collaborator.',
  'https://mndaily.com/city/minnesotas-emerging-blockchain-builders/11/13/2025/eicmndaily-com/',
  'connect@mnblockchain.org | ACM at UMN · acm@umn.edu'),

 ('', 'Monitor', 'Minnesota State Mankato',
  '⚠ DOES THE $2,000,000/$2,000,000 INSURANCE REQUIREMENT ATTACH TO A TABLE?',
  'The CSU insurance policy says "Insurance must be provided for any University event where alcohol will be '
  'served AND FOR EVENTS HOSTED BY NON-UNIVERSITY CLIENTS," at minimum limits of $2,000,000 per person / '
  '$2,000,000 per occurrence naming the University as additional insured. The sentence is ambiguous and the '
  'answer decides Mankato\'s economics completely — a $2M certificate for a folding table is a different '
  'proposition from a CSU 219 approval. Ask alongside: will CSU 219 approve an outside for-profit table, and '
  'at what fee? No rate card exists anywhere on mnsu.edu.',
  'https://mankato.mnsu.edu/university-life/centennial-student-union/about-us/policies-and-procedures-update/insurance/',
  'Bill Tourville (CSU 219) · (507) 389-2223 | Finance & Administration · (507) 389-6623'),

 ('', 'Monitor', 'Carleton College',
  '⚠ FIND THE SPONSOR — it is free, it is explicitly permitted, and the window is Sep 14 – Nov 18 only',
  'Verbatim: "We do not accept reservations for local business or off-campus organizations. However, if you '
  'receive sponsorship from a campus department or organization, the department/organization can make a table '
  'reservation on your behalf. THERE IS NO FEE IF YOU ARE SPONSORED." This is the exact arrangement UMN Twin '
  'Cities and St. Cloud State forbid by name as "fronting." The sponsor must book in EMS with a Carleton '
  'login, 24 hours ahead, Sayles-Hill Great Space, weekdays 9am–6pm. Candidates: Carleton Investment Group '
  '(its page is behind a CLOUDFLARE BOT CHECK and unreadable), the Economics department, the Career Center.',
  'https://www.carleton.edu/student-activities/guide/event-promotion/table/',
  'Student Activities Office · sao@carleton.edu · (507) 222-4462'),

 ('', 'Monitor', 'St. Cloud State',
  '⚠ BOOK THE $85 TABLE — no sponsor, no committee, no approval chain',
  'Atwood kiosk $45/day, table in the Main Lounge $85/day, outside mall $85/day, all available to '
  'non-university organizations and businesses. ⚠ Two design constraints: Atwood bans "CREDIT CARD OR DEBIT '
  'CARD SIGN-UPS" outright (almost certainly downstream of Minn. Stat. s 135A.145) and bans raffles per '
  'Minnesota State policy — so run an email-only table with no prize draw. ⚠ And do NOT ask a student org to '
  'book for you: the Co-Sponsorship Policy names "fronting" and punishes a second offence with loss of Atwood '
  'booking privileges for the whole academic year plus public-rate charges. The fee is non-refundable if you '
  'do not show. Insurance limit not published — ask.',
  'https://www.stcloudstate.edu/atwood/reservations/promotional-space.aspx',
  'Lisa Johnson, Scheduling Coordinator · lajohnson@stcloudstate.edu · (320) 308-2074'),

 ('', 'Monitor', 'U of Minnesota Twin Cities',
  '⚠ STATE-LEVEL COMPLIANCE PREP — read before any Minnesota table',
  'MINNESOTA HAS NO CAMPUS FREE-SPEECH STATUTE (Minn. Stat. ch. 135A contains no free-expression section) — '
  'do not claim one. What it DOES have is Minn. Stat. s 135A.145, which bars any "public or private '
  'postsecondary educational institution, INCLUDING ITS AGENTS, EMPLOYEES, STUDENT OR ALUMNI ORGANIZATIONS, '
  'OR AFFILIATES" from "any agreement to market credit cards to undergraduate students" — the source of St. '
  'Cloud\'s and Augsburg\'s credit-card bans. Prepare the answer: DGD is not a card issuer under 15 U.S.C. '
  's 1602. Also: MCDPA (Minn. Stat. ss 325M.10–.21, effective Jul 31, 2025) covers businesses controlling or '
  'processing data on 100,000+ Minnesotans, or earning 25%+ of revenue from data sales while handling 25,000+ '
  '— collect an email and nothing else. Favourable opener: HF 3709, effective Aug 1, 2026, lets Minnesota '
  'state-chartered banks and credit unions custody virtual currency.',
  'https://www.revisor.mn.gov/statutes/cite/135A.145',
  'Minnesota AG MCDPA page · https://www.ag.state.mn.us/Office/Communications/2025/07/28_MCDPA.asp'),
]
