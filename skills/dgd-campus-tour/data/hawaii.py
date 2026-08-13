"""Hawaii — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published / not retrievable at time of research — a gap to close by phone, not a
finding of absence. Schema: reference/data-schema.md

⚠⚠ READ FIRST — THE UH SYSTEMWIDE RULEBOOK WAS REPLACED ON 1 JULY 2026 AND IS STILL BEING
REWRITTEN. The University of Hawaiʻi replaced its systemwide TIME, PLACE AND MANNER (TPM)
policy on an INTERIM basis EFFECTIVE 1 JULY 2026, superseding a policy that had not been
substantially updated in over ten years, and UH has said it will hold community discussions
THROUGHOUT FALL 2026 BEFORE FINAL ADOPTION. Two consequences, both operational: (1) ANY UH
GUIDANCE, BLOG POST, HANDBOOK OR THIRD-HAND ADVICE PREDATING 1 JULY 2026 IS UNRELIABLE; and
(2) THE RULES CAN CHANGE MID-TOUR — what an office tells you by phone in September may not
hold in November, so GET EVERY PERMISSION IN WRITING BY EMAIL. ⚠ THE OPERATIVE TEXT OF THAT
POLICY COULD NOT BE RETRIEVED. Its landing page, https://www.hawaii.edu/tpm-policy/, and the
circulated draft, "DRAFT Administrative Procedure, AP 10.xxx Implementation of Time, Place,
and Manner Restrictions" dated 11.14.25
(https://www.hawaii.edu/wp/wp-content/uploads/2025/12/DRAFT_AP_10.XXX_Time_Place_Manner_Restrictions_11.14.25.pdf),
were both ROBOTS-BLOCKED (robots.txt fetch ConnectTimeout, roughly 4 attempts in 5 failing)
across ~12 retries over ten minutes. THE FINAL AP NUMBER IS UNVERIFIED — the "10.xxx"
placeholder was never resolved on any page that could be read. What IS confirmed, from two
readable press sources: "Peaceful protests, demonstrations, rallies, speeches, petitions and
other forms of constitutionally guaranteed expression remain fully protected," and the policy
"explicitly preserves the right" of STUDENTS, FACULTY AND STAFF to spontaneously assemble in
generally accessible outdoor areas WITHOUT PRIOR APPROVAL. ⚠ NOTE THE ENUMERATED CLASSES —
AFFILIATES ONLY. NEITHER SOURCE ADDRESSES NON-AFFILIATED PERSONS, OUTSIDE ENTITIES OR
COMMERCIAL ACTIVITY, WHICH IS EXACTLY DGD'S QUESTION. That is a confirmed gap, not a
permission.

GOVERNANCE STACK — the order to argue in: Hawaiʻi Administrative Rules → Board of Regents
Policy → Executive Policy → Administrative Procedure → campus policy. For facilities and
solicitation: HAR Title 20, Subtitle 1, Chapter 13, "Use of University-Owned Facilities,"
§§ 20-13-1 to 20-13-9 (confirmed to exist via
https://www.law.cornell.edu/regulations/hawaii/title-20/subtitle-1; SECTION TEXT NOT READ);
then the interim TPM policy above; then campus-level M10.300 (Mānoa) and the UH Hilo
Facilities Use Practices and Procedures — BOTH OF WHICH WERE ALSO ROBOTS-BLOCKED AND UNREAD.

NO HAWAIʻI CAMPUS FREE-SPEECH STATUTE WAS FOUND — no FORUM-Act-style law, no "free expression
on campus" chapter in HRS. Marked UNVERIFIED-NEGATIVE: the search budget ran out before a
targeted HRS query could be run. Confirm at https://www.capitol.hawaii.gov/. Either way the
operative constraint at UH is public-forum doctrine plus the interim TPM policy, not a statute
— and HPU and Chaminade are PRIVATE and bound by none of it.

⚠⚠ GEOGRAPHY — MĀNOA AND HILO ARE A FLIGHT APART, NOT A DRIVE APART. UH Mānoa is in Honolulu
on Oʻahu; UH Hilo is in Hilo on Hawaiʻi Island, ~200 miles southeast across open ocean. There
is NO ferry, NO bridge and NO road. Reaching Hilo means an interisland flight (HNL→ITO), a
half-day each direction, an airfare each direction and a rental car on arrival. Mānoa, Hawaiʻi
Pacific and Chaminade are ALL ON OʻAHU and 15–20 minutes apart by car (Mānoa valley, downtown
Honolulu at Aloha Tower, and Kaimukī) — those three are ONE TRIP. Hilo is a separate decision
with a separate budget line.

SCALE — DO NOT PLAN THIS AS FOUR MAINLAND STOPS. UH Mānoa is the only campus in the state with
a large undergraduate business and CS population. HPU is mid-sized with a real BSBA cohort. UH
Hilo is ~3,000 students and on another island. Chaminade is ~1,000 undergraduates and has
ZERO business, finance, computer science or entrepreneurship student organizations out of ten
recognized clubs total. This is one strong stop, one decent stop, and two that must justify
themselves.

⚠ THE BEST CHANNEL IN HAWAII IS NOT A CAMPUS AT ALL. The Hawaii Annual Innovation Challenge
(HAIC, formerly HACC) — State Office of Enterprise Technology Services IN PARTNERSHIP WITH THE
UNIVERSITY OF HAWAIʻI — publishes an open sponsorship rate card (Petabyte $7,000+, Terabyte
$5,000–6,999, Gigabyte $2,500–4,999, Megabyte $500–2,499), handled by the IMAG Foundation, a
501(c)(3), "making all contributions 100% tax deductible." It reaches UH Mānoa AND UH Hilo
students without a second flight, from $500, and it sidesteps every campus solicitation rule in
this file. Registration closes 27 Oct 2026. https://haic.hawaii.gov/sponsors/
"""

STATE = 'Hawaii'

CAMPUSES = [

 # ------------------------------------------------------------ 1. UH Mānoa
 {'state': 'Hawaii',
  'name': 'University of Hawaiʻi at Mānoa',
  'city': 'Honolulu, HI (Oʻahu)',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 3,
  'start': 'Mon Aug 24, 2026 — CONFIRMED on the university\'s own Fall 2026 registrar page (all weekdays check '
           'out against the dates, so this is a genuine Fall 2026 page, not a stale prior-year one).',
  'adddrop': 'Tue Sep 15, 2026, 11:59 p.m. HST — last day to add/drop without a W. ⚠ Three weeks after classes '
             'start, and two weeks looser than UH Hilo\'s Sep 1 add deadline: Mānoa schedules stay fluid longer.',
  'fallbreak': '⚠ NONE — no fall break appears anywhere on the Fall 2026 calendar. Good news for scheduling: an '
               'uninterrupted run from late August to early December. ⚠ BUT TWO HAWAII-ONLY CLOSURES MAINLAND '
               'PLANNERS MISS — Statehood Day Fri Aug 21, 2026 (harmless, it precedes classes) and ELECTION DAY '
               'TUE NOV 3, 2026, a Hawaii state holiday and a general-election day, so CAMPUS IS CLOSED. Veterans '
               'Day Wed Nov 11 also closed.',
  'thanksgiving': 'Thu Nov 26, 2026 (Thanksgiving) and Fri Nov 27, 2026 (observance) — no classes.',
  'lastclass': 'Thu Dec 10, 2026. Study period Dec 11–12.',
  'finals': 'Mon–Fri Dec 14–18, 2026. Semester ends and degrees confer Fri Dec 18; commencement Sat Dec 19.',
  'cal_url': 'https://manoa.hawaii.edu/registrar/academic-calendar/fall-2026/',
  'cal_status': 'CONFIRMED — read on the live Fall 2026 registrar page, weekday-checked.',
  'fair': 'Involvement Fair — run by Student Life & Development (SLD) at the Campus Center Complex, for and by '
          'Registered Independent Organizations (RIOs)',
  'fair_date': '⚠ FALL 2026 DATE IS NOT PUBLISHED ON ANY PAGE THAT COULD BE READ. Do not guess it. Recurring '
               'pattern: held at the Campus Center Complex EARLY IN THE FALL SEMESTER. A Fall 2025 event page '
               'exists at https://manoa.hawaii.edu/studentlife/eventlist/involvement-fair-fall-2025/ but was '
               'ROBOTS-BLOCKED on every attempt, so not even the prior year\'s date, time, eligibility or fee '
               'could be extracted. It will post at https://manoa.hawaii.edu/studentlife/ and at the permanent '
               'short link http://go.hawaii.edu/Um ("Student Involvement Fair at Campus Center"). ⚠ STALENESS '
               'WARNING: the Campus Center Complex landing page was still displaying FALL 2023 BUILDING HOURS when '
               'read in August 2026 — this site is not maintained aggressively, so do not trust a date found there '
               'without a phone confirmation. CALL (808) 956-8178.',
  'fair_outside': '⚠ UNVERIFIED — COULD NOT BE CONFIRMED EITHER WAY, AND ASSUME NO UNTIL SLD SAYS OTHERWISE. The '
                  'fair is run for and by RIOs (Registered Independent Organizations). Nothing on any readable '
                  'page says whether outside or community organizations may table. Given the blanket solicitation '
                  'language in the archived Mānoa facilities policy (see policy_key), the working assumption '
                  'should be that outside entities may not — but that is a working assumption, not a finding. '
                  'The one call that settles it: Student Life & Development, (808) 956-8178.',
  'fair_cost': 'UNVERIFIED — no fee, rate card or tier is published anywhere reachable. The Campus Center rate '
               'sheet at https://manoa.hawaii.edu/studentlife/campus-center-complex/meetings-events/planning-an-event/ '
               'was ROBOTS-BLOCKED on every attempt. Ask SLD, (808) 956-8178, for the rate sheet AND the deposit, '
               'cancellation and insurance terms in the same call.',
  'fair_deadline': 'UNVERIFIED — no registration deadline is published, because no Fall 2026 fair page could be '
                   'read at all. (808) 956-8178.',
  'fair_url': 'https://manoa.hawaii.edu/studentlife/',
  'policy': 'M10.300, "UH Mānoa Interim Guidelines on UH Mānoa Facilities Use Practices and Procedures" — THE '
            'OPERATIVE CAMPUS DOCUMENT, AND IT COULD NOT BE READ. Above it: the UH systemwide INTERIM Time, Place '
            'and Manner policy effective 1 Jul 2026, and HAR Title 20, Subtitle 1, Chapter 13 §§ 20-13-1 to '
            '20-13-9. Below/behind it: the ARCHIVED predecessor A1.200 (June 2002), which is readable in full and '
            'is quoted in policy_key as BACKGROUND ONLY.',
  'policy_url': 'https://manoa.hawaii.edu/policies/m10/m10-300/',
  'policy_key': "⚠⚠ THE ACCESS RATING OF 3 HERE IS PROVISIONAL AND ASSIGNED BECAUSE THE OPERATIVE TEXT COULD NOT "
                "BE READ — NOT BECAUSE MĀNOA IS KNOWN TO BE MODERATELY OPEN. Three layers govern and only one was "
                "readable. GAP 1 — THE CAMPUS LAYER: M10.300, 'UH Mānoa Interim Guidelines on UH Mānoa Facilities "
                "Use Practices and Procedures,' https://manoa.hawaii.edu/policies/m10/m10-300/ — ROBOTS-BLOCKED "
                "ACROSS ~12 ATTEMPTS OVER TEN MINUTES (robots.txt fetch ConnectTimeout, not a 403). THIS IS THE "
                "BIGGEST SINGLE GAP IN THE HAWAII PACKET. The word 'INTERIM' in its own title, alongside the "
                "systemwide interim TPM policy, strongly suggests Mānoa's facilities rules are ALSO MID-REVISION. "
                "SOMEONE MUST OPEN THIS URL IN A BROWSER or request the document from SLD, (808) 956-8178, and "
                "extract four things: whether outside entities may be sponsored, INSURANCE DOLLAR LIMITS, whether "
                "commercial solicitation has ANY exception, and any language on payment apps or on-site contracts. "
                "GAP 2 — THE SYSTEM LAYER: the UH systemwide TIME, PLACE AND MANNER POLICY WAS REPLACED ON AN "
                "INTERIM BASIS EFFECTIVE 1 JULY 2026 and is being rewritten through community discussions "
                "THROUGHOUT FALL 2026. ⚠⚠ ANY GUIDANCE PREDATING 1 JULY 2026 IS UNRELIABLE, AND THE RULES MAY "
                "CHANGE MID-TOUR. Landing page https://www.hawaii.edu/tpm-policy/ and the circulated draft 'DRAFT "
                "Administrative Procedure, AP 10.xxx Implementation of Time, Place, and Manner Restrictions' "
                "(11.14.25) WERE BOTH ROBOTS-BLOCKED AND THE OPERATIVE TEXT COULD NOT BE RETRIEVED DESPITE "
                "REPEATED ATTEMPTS; THE FINAL AP NUMBER IS UNVERIFIED. What two readable press sources confirm: "
                "'PEACEFUL PROTESTS, DEMONSTRATIONS, RALLIES, SPEECHES, PETITIONS AND OTHER FORMS OF "
                "CONSTITUTIONALLY GUARANTEED EXPRESSION REMAIN FULLY PROTECTED,' and the policy 'EXPLICITLY "
                "PRESERVES THE RIGHT' of STUDENTS, FACULTY AND STAFF to spontaneously assemble in generally "
                "accessible outdoor areas WITHOUT PRIOR APPROVAL. ⚠ READ THE ENUMERATED CLASSES: AFFILIATES ONLY. "
                "NEITHER SOURCE ADDRESSES NON-AFFILIATED PERSONS, OUTSIDE ENTITIES OR COMMERCIAL ACTIVITY — the "
                "exact question DGD needs answered. Standards do cover noise near classrooms and offices, "
                "DESIGNATED POSTING AREAS, and unobstructed building access. GAP 3 — THE RULE LAYER: HAR Title 20, "
                "Subtitle 1, Chapter 13, 'Use of University-Owned Facilities,' §§ 20-13-1 to 20-13-9, CONFIRMED TO "
                "EXIST (law.cornell.edu/regulations/hawaii/title-20/subtitle-1) BUT SECTION TEXT NOT READ. "
                "◆ WHAT COULD BE READ, VERBATIM — A1.200, 'University of Hawaii at Manoa Facilities Use Policy,' "
                "effective JUNE 2002, https://www.hawaii.edu/policy/archives/apm/a1200p/a1200.pdf. ⚠ THIS IS "
                "ARCHIVED. CITE IT AS BACKGROUND, NOT AS THE GOVERNING RULE — but it shows the drafting tradition "
                "M10.300 is built on: 'NO SOLICITATION SHALL BE CONDUCTED IN ANY BUILDING, STRUCTURE, FACILITY, OR "
                "ON ANY GROUNDS, SIDEWALKS, OR STREETS…' with enumerated exceptions for vending machines, the "
                "bookstore, and FUND-RAISING BY REGISTERED STUDENT ORGANIZATIONS WITH PRIOR WRITTEN APPROVAL. "
                "'THE UNIVERSITY OF HAWAI\\'I AT MANOA, AS A PUBLIC INSTITUTION, IS NOT IN COMPETITION WITH OTHER "
                "INSTITUTIONS OR COMMERCIAL ENTERPRISES…' 'UNIVERSITY-AFFILIATED ORGANIZATIONS MAY SPONSOR OTHER "
                "ORGANIZATIONS OR INDIVIDUALS AND THEREBY QUALIFY FOR USE OF CAMPUS FACILITIES…' 'ALL "
                "NON-AFFILIATED ORGANIZATIONS ARE REQUIRED TO PROVIDE EVIDENCE OF ADEQUATE INSURANCE PROTECTION' "
                "(waivable by the President). 'THE CAMPUS CENTER COURTYARD AREA IS DESIGNATED AS THE PUBLIC FORUM "
                "AREA FOR THE UNIVERSITY OF HAWAI\\'I AT MANOA WHERE INDIVIDUALS MAY ASSEMBLE AND ENGAGE IN PUBLIC "
                "SPEECH ACTIVITIES.' ◆ HOW TO READ THAT: (a) THE DEFAULT IS A BLANKET SOLICITATION BAN covering "
                "buildings, grounds, sidewalks AND streets — BROADER than most mainland policies, which ban only "
                "*commercial* solicitation. (b) ⚠ SPONSORSHIP APPEARS TO CURE THE *FACILITY-ACCESS* PROBLEM RATHER "
                "THAN BEING IRRELEVANT: an affiliated organization may sponsor an outside entity 'and thereby "
                "qualify for use of campus facilities,' and THERE IS NO ANTI-FRONTING PROHIBITION IN A1.200 — the "
                "drafters accepted fronting and handled it through LIABILITY TRANSFER instead, with the sponsoring "
                "group assuming responsibility for all damages and for the sponsored entity's compliance. "
                "PRACTICALLY: THE RIO OFFICER WHO SIGNS FOR DGD IS PERSONALLY EXPOSING THEIR ORGANIZATION. SAY SO "
                "OUT LOUD — it is the honest thing to do and it protects the relationship. (c) ⚠ BUT SPONSORSHIP "
                "DOES NOT OBVIOUSLY LIFT THE SOLICITATION BAN, which is a SEPARATE prohibition with its own narrow "
                "exception (RSO fund-raising with prior written approval). DISTRIBUTING DGD MATERIAL MAY BE FINE; "
                "ANYTHING TRANSACTIONAL PROBABLY IS NOT. (d) INSURANCE IS REQUIRED of all non-affiliated "
                "organizations but NO DOLLAR LIMITS ARE STATED — they live in M10.300 or the Campus Center rental "
                "agreement. UNVERIFIED. (e) FEES, DEPOSITS AND CANCELLATION TERMS: UNVERIFIED, rate sheet "
                "robots-blocked. (f) NOTHING FOUND REACHING PAYMENT CREDENTIALS (credit card, Venmo, payment apps) "
                "OR SIGNING CONTRACTS ON SITE — A1.200 predates all of that by two decades; whether M10.300 or the "
                "2026 TPM revision adds such language is UNVERIFIED and is exactly the clause a 2025–26 rewrite "
                "would add. ASK DIRECTLY. (g) PUBLIC FORUM: the CAMPUS CENTER COURTYARD is the designated "
                "public-forum area and UH is a public institution bound by public-forum doctrine there — DGD'S "
                "STRONGEST LEGAL FOOTING ANYWHERE IN THIS STATE. ⚠ But expressive activity in a public forum is "
                "NOT the same as commercial solicitation, and the solicitation ban is content-neutral on its face. "
                "Do not overload this argument. "
                "⚠⚠ STATE REGULATORY NOTE — HAWAII MONEY TRANSMISSION AND DIGITAL CURRENCY. RECORDED HERE BECAUSE "
                "THE PACKET HAS NO STATE-LEVEL FIELD, AND IT MATTERS WHETHER OR NOT ANYONE EVER TABLES IN "
                "HONOLULU. HAWAII WENT FROM HOSTILE TO DEREGULATED ON DIGITAL CURRENCY AND IS CURRENTLY IN A "
                "LEGISLATIVE VACUUM. (1) THE SANDBOX IS OVER: the DIGITAL CURRENCY INNOVATION LAB (DCIL), a "
                "DCCA/DFI + Hawaii Technology Development Corporation program that let digital currency companies "
                "operate WITHOUT a Hawaii money transmitter license, ran 2020 to 30 JUNE 2024 AND WAS ALLOWED TO "
                "SUNSET "
                "(cca.hawaii.gov/dfi/news-releases/release-hawaii-digital-currency-innovation-lab-to-conclude/). "
                "(2) THE CURRENT DFI POSITION — still the live FAQ, dated 9 FEB 2024: after the DCIL concluded, "
                "'DIGITAL CURRENCY COMPANIES WILL NO LONGER REQUIRE A HAWAIʻI-ISSUED MONEY TRANSMITTER LICENSE TO "
                "CONDUCT BUSINESS.' The FAQ lists activities that may be conducted WITHOUT a money transmitter "
                "license: 'TRADING OF DIGITAL CURRENCY OR ASSETS'; 'PROVIDING HOSTED DIGITAL CURRENCY WALLETS OR "
                "DIGITAL CURRENCY CUSTODIAL SERVICES'; 'ISSUING OR REDEEMING STABLE COINS'; 'TRANSFERRING DIGITAL "
                "ASSETS FROM ONE PERSON TO ANOTHER.' DFI also notes the list 'MAY CHANGE FROM TIME TO TIME.' "
                "(cca.hawaii.gov/dfi/dcil-faq-industry/ and /dcil-faq-consumers/). (3) ⚠⚠ THE HARD LINE IS FIAT — "
                "THE CARVE-BACK, VERBATIM: 'COMPANIES THAT CONDUCT ACTIVITY IN US$ OR OTHER FIAT CURRENCIES THAT "
                "MEETS THE DEFINITION OF MONEY TRANSMISSION…WILL LIKELY REQUIRE A MONEY TRANSMITTER LICENSE FOR "
                "THAT FIAT-DENOMINATED ACTIVITY IF AN EXCLUSION…DOES NOT APPLY.' THE MOMENT DGD TOUCHES DOLLARS — "
                "taking cash, on-ramping, anything resembling money transmission in USD — A HAWAII MONEY "
                "TRANSMITTER LICENSE LIKELY ATTACHES. BRIEF EVERY AMBASSADOR ON THIS BEFORE ANY EVENT WHERE A "
                "STUDENT MIGHT HAND OVER CASH OR USE A PAYMENT APP. (4) ⚠ PERMISSIVE IS NOT ENDORSED: DFI's "
                "consumer guidance warns that transactions involving digital currency 'ARE NOT GUARANTEED BY ANY "
                "GOVERNMENT AGENCY' and that there is 'NO GOVERNMENT AGENCY THAT WILL PROTECT CONSUMER FUNDS.' AN "
                "AMBASSADOR WHO IMPLIES HAWAII STATE OVERSIGHT OR APPROVAL IS MISREPRESENTING THE POSITION. "
                "(5) ⚠ THE WINDOW MAY CLOSE: SB 2757 SD1 (33rd Legislature, 2026), 'Relating to Digital Asset "
                "Charters,' would have created a Digital Asset Charter Program under DFI — mandatory charter, "
                "$9,000 application fee, $1,000 annual renewal, $2,500–$12,500 quarterly assessments, $500,000 "
                "minimum tangible net worth, $500,000 surety bond, AML and cybersecurity programs, civil penalties "
                "to $20,000 per violation, effective 1 Jan 2027. IT PASSED THE SENATE 10 MARCH 2026, WAS DEFERRED "
                "BY THE HOUSE CONSUMER PROTECTION & COMMERCE COMMITTEE ON 17 MARCH 2026, AND DIED IN COMMITTEE "
                "(https://legiscan.com/HI/bill/SB2757/2026). A charter bill will very likely return in the 2027 "
                "session — it cleared the whole Senate once. ANY MESSAGING BUILT ON 'NO LICENSE REQUIRED IN "
                "HAWAII' AGES BADLY. ⚠ CONFIRM ALL OF THIS DIRECTLY WITH THE HAWAII DIVISION OF FINANCIAL "
                "INSTITUTIONS (DFI), Department of Commerce and Consumer Affairs, https://cca.hawaii.gov/dfi/ , "
                "BEFORE ANY ON-SITE ACTIVITY THAT TOUCHES PAYMENTS, SIGN-UPS OR WALLET REGISTRATIONS — the FAQ "
                "relied on here is dated 9 Feb 2024 and DFI says the list may change.",
  'sponsor_required': '⚠ PROBABLY YES FOR FACILITY ACCESS, AND SPONSORSHIP PROBABLY DOES NOT CURE SOLICITATION — '
                      'but this rests on the ARCHIVED 2002 policy, not on M10.300, which could not be read. '
                      'A1.200 said "university-affiliated organizations may sponsor other organizations or '
                      'individuals and thereby qualify for use of campus facilities" and contained NO '
                      'ANTI-FRONTING CLAUSE — it transferred liability to the sponsor instead. So a RIO can '
                      'probably get DGD into a room, at the RIO\'s own risk. It probably cannot lift the separate '
                      'blanket solicitation ban, whose only narrow exception is RSO fund-raising with PRIOR '
                      'WRITTEN APPROVAL. ⚠ VERIFY AGAINST M10.300 BEFORE COURTING A CLUB — confirm with SLD, '
                      '(808) 956-8178, and get the answer in writing.',
  'clubs': [('⚠ NO BROWSABLE RIO DIRECTORY COULD BE RETRIEVED — UNCLOSED GAP, NOT A FINDING OF ABSENCE',
             'MORE THAN 150 RIOs (Registered Independent Organizations) operate at Mānoa — "student organizations, '
             'associations, or clubs that are formed to meet special interests of certain groups of students on '
             'campus." The RIO directory page itself was ROBOTS-BLOCKED and the involvement pages that could be '
             'read do not expose a roster. ASK SLD, (808) 956-8178, TO SEARCH THE RIO ROSTER for: blockchain, '
             'crypto, bitcoin, Web3, fintech, investment, FMA, ACM, data science.',
             'https://manoa.hawaii.edu/studentlife/involvement/registered-independent-organizations/'),
            ('⚠ NO BLOCKCHAIN / CRYPTOCURRENCY / BITCOIN / WEB3 / FINTECH CLUB IS CONFIRMED — AND NONE IS '
             'CONFIRMED ABSENT',
             'No evidence was found that one exists and none that one does not. DO NOT ASSERT EITHER WAY. No '
             'Financial Management Association chapter confirmed either. This is a directory-access limitation, '
             'not a verified absence — the directory was never read.',
             'https://manoa.hawaii.edu/studentlife/involvement/'),
            ('⚠ Student-run stock portfolio — UNVERIFIED LEAD, POTENTIALLY THE WARMEST AUDIENCE ON CAMPUS',
             'Honolulu Civil Beat, May 2026: "Student-Run Stock Portfolio Could Fund Scholarships." THE ARTICLE '
             'WAS NOT READ and it CANNOT BE CONFIRMED that it concerns a UH Mānoa student investment club. If it '
             'does, that is the single best sponsor candidate at Mānoa. VERIFY BEFORE ACTING — one browser tab '
             'settles it.',
             'https://www.civilbeat.org/2026/05/student-run-stock-portfolio-could-fund-scholarships/'),
            ('Chartered Student Organizations (CSOs) — the five BOR-recognized bodies',
             'ASUH (Associated Students of UH), CCB (Campus Center Board), GSO (Graduate Student Organization), '
             'SAPFB (Student Activity and Program Fee Board), SMB (Student Media Board). ⚠ TWO OF THESE MATTER: '
             'CCB GOVERNS THE CAMPUS CENTER — the venue — and SAPFB CONTROLS THE STUDENT ACTIVITY FEE THAT FUNDS '
             'RIO EVENTS. A club with SAPFB money can host a speaker without DGD paying a venue fee. NO PHONE '
             'NUMBERS ARE PUBLISHED on that page; route through SLD.',
             'https://manoa.hawaii.edu/studentlife/involvement/chartered-student-organizations/'),
            ('(Officer names)',
             'NONE REPORTED — none was confirmable on a live page and none is guessed here.',
             'https://manoa.hawaii.edu/studentlife/involvement/')],
  'faculty': [('⚠ Student Life & Development (SLD)',
               'THE SINGLE HIGHEST-VALUE CALL IN HAWAII. Runs the Campus Center, the RIO system and the Involvement '
               'Fair, and is the route to Meeting & Event Services. Ask it for: the Fall 2026 Involvement Fair '
               'date, whether OUTSIDE entities may table, the Campus Center rate sheet with deposit/cancellation '
               'terms, the INSURANCE DOLLAR LIMIT, and a copy of M10.300. Mon–Fri 8:00–4:30, closed state holidays '
               '(note Election Day Nov 3 is one).',
               'Student Life & Development',
               'sld@hawaii.edu · (808) 956-8178',
               'https://manoa.hawaii.edu/studentlife/'),
              ('⚠ Mānoa Career Center',
               'Owns the career fair — and the employer-facing page is EIGHTEEN MONTHS STALE, still showing a '
               'Spring 2025 event. Call for the Fall 2026 date, the employer registration cost and deadline, and '
               'specifically WHETHER A CRYPTO PROJECT IS AN ELIGIBLE EMPLOYER. 2600 Campus Road, QLCSS Room 212, '
               'Honolulu HI 96822.',
               'Career Center',
               'careers@hawaii.edu · (808) 956-7007',
               'https://manoa.hawaii.edu/careercenter/employers/career-fair/'),
              ('⚠ Qianqiu Liu',
               'CHAIR, DEPARTMENT OF FINANCE — START HERE ON THE ACADEMIC SIDE. Chairs are the people who can '
               'authorize a guest-lecture slot, and Finance is the department that owns FIN 311 Investments, the '
               'highest-enrollment finance course on campus. ⚠ NOT confirmed to research blockchain or digital '
               'assets — listed as the right door, not as a subject-matter match.',
               'Shidler College of Business — Finance',
               'qianqiu@hawaii.edu · (808) 956-8736',
               'https://shidler.hawaii.edu/directory'),
              ('⚠ Randall K. Minas, Jr.',
               'PROFESSOR AND MSIS DIRECTOR (Information Technology Management) — the second authorizing door. A '
               'program director can place a speaker in front of the MS in Information Systems cohort without any '
               'facilities process at all. ⚠ NOT confirmed to research blockchain or digital assets.',
               'Shidler College of Business — ITM',
               'rminas@hawaii.edu · (808) 956-7082',
               'https://shidler.hawaii.edu/directory'),
              ('Shidler College of Business — Information Technology Management department',
               'Departmental line for the ITM/MSIS side. Useful if Minas does not answer, and the right place to '
               'ask which ITM courses run in Fall 2026.',
               'Shidler College of Business — ITM',
               '(808) 956-7430',
               'https://shidler.hawaii.edu/itm/academics'),
              ('Jing Ai',
               'Interim Associate Dean for Academic Affairs — Shidler-level academic approvals, i.e. the '
               'escalation point above a department chair.',
               'Shidler College of Business',
               'jinga@hawaii.edu · (808) 956-9519',
               'https://shidler.hawaii.edu/directory'),
              ('Hua Chen',
               'Professor of Finance and Risk Management. Risk management is the nearest adjacent field to a '
               'digital-asset conversation among the confirmed Shidler finance faculty. ⚠ No crypto research '
               'interest confirmed.',
               'Shidler College of Business — Finance',
               'huachen@hawaii.edu · (808) 956-8063',
               'https://shidler.hawaii.edu/directory'),
              ('Jiakai Chen',
               'Associate Professor of Finance. ⚠ No crypto research interest confirmed — listed as finance '
               'faculty of record.',
               'Shidler College of Business — Finance',
               'jiakai.chen@hawaii.edu · (808) 956-7610',
               'https://shidler.hawaii.edu/directory'),
              ('Wei (Victor) Huang',
               'Professor of Finance. ⚠ No crypto research interest confirmed.',
               'Shidler College of Business — Finance',
               'weih@hawaii.edu · (808) 956-7679',
               'https://shidler.hawaii.edu/directory'),
              ('Rick Kazman',
               'Danny and Elsa Lui Distinguished Professor, Information Technology Management. Senior ITM name — '
               'a distinguished chair carries weight if the MSIS route needs escalating. ⚠ No crypto research '
               'interest confirmed.',
               'Shidler College of Business — ITM',
               'kazman@hawaii.edu · (808) 956-6948',
               'https://shidler.hawaii.edu/directory'),
              ('Campus Center — Meeting & Event Services / reservations',
               '⚠ NO DIRECT LINE COULD BE REACHED — the Campus Center event-planning page is ROBOTS-BLOCKED. This '
               'office holds the rate sheet, the deposit and cancellation terms and the insurance limit. ROUTE '
               'THROUGH SLD AND ASK FOR MEETING & EVENT SERVICES BY NAME.',
               'Campus Center Complex',
               'no direct number published — look up here; route via SLD (808) 956-8178',
               'https://manoa.hawaii.edu/studentlife/campus-center-complex/meetings-events/planning-an-event/'),
              ('Information & Computer Sciences (ICS) department',
               '⚠ NO NUMBER CONFIRMED — the ICS course listing was ROBOTS-BLOCKED, so an ICS cryptography or '
               'distributed-systems course may well exist and would be a natural fit. Worth one call to find out '
               'who teaches it. Look the number up in the UH directory.',
               'Information & Computer Sciences',
               'no number published — look up here',
               'https://www.ics.hawaii.edu/courses/'),
              ('(Chartered Student Organization contacts — ASUH, CCB, GSO, SAPFB, SMB)',
               'NO PHONE NUMBERS ARE PUBLISHED for any of the five CSOs on the page that lists them. CCB governs '
               'the Campus Center venue and SAPFB controls the student activity fee — both worth reaching. Route '
               'through SLD.',
               'Chartered Student Organizations',
               'no numbers published — look up here; route via SLD (808) 956-8178',
               'https://manoa.hawaii.edu/studentlife/involvement/chartered-student-organizations/')],
  'courses': [('⚠ FIN 311',
               'Investments (3 credits) — REQUIRED OF ALL BBA STUDENTS, therefore the HIGHEST-ENROLLMENT FINANCE '
               'COURSE ON CAMPUS and the best single classroom in the state. Fall 2026 offering not individually '
               'verified, but a required core course will run. Ask Qianqiu Liu, (808) 956-8736, who teaches it.',
               'https://shidler.hawaii.edu/courses/fin/311'),
              ('(Blockchain / crypto / digital assets / fintech)',
               '⚠ NONE FOUND in Shidler\'s Finance or ITM academics pages. The Finance department offers SIX '
               'specialization tracks — Asian Finance, Investment Management (CFA track), Corporate Finance, Real '
               'Estate Finance, Financial Services & Planning (CFP track), Insurance & Risk Management — AND NONE '
               'IS FINTECH OR DIGITAL ASSETS. ⚠ This is "not found in Shidler," NOT a whole-catalog absence.',
               'https://shidler.hawaii.edu/fin/academics'),
              ('(ICS — Information & Computer Sciences)',
               '⚠ NEVER CHECKED — https://www.ics.hawaii.edu/courses/ was ROBOTS-BLOCKED. An ICS CRYPTOGRAPHY or '
               'DISTRIBUTED-SYSTEMS course may exist and would be the most natural fit on this campus. UNCLOSED '
               'GAP — worth one call to ICS.',
               'https://www.ics.hawaii.edu/courses/'),
              ('Graduate programs that could host a talk',
               'MS in Finance (MSF), MS in Information Systems (MSIS — Randall Minas directs it), PhD in '
               'International Management. A graduate seminar is a lighter ask than a facilities booking and sits '
               'entirely outside the solicitation regime.',
               'https://shidler.hawaii.edu/itm/academics')],
  'events': [('⚠ Involvement Fair (Student Life & Development, Campus Center Complex)',
              'FALL 2026 DATE NOT PUBLISHED ANYWHERE READABLE. Pattern: early in the fall semester, at the Campus '
              'Center Complex, run for and by RIOs. Whether outside organizations may table is UNVERIFIED — assume '
              'no until SLD says otherwise. Will post at https://manoa.hawaii.edu/studentlife/ and '
              'http://go.hawaii.edu/Um. Call (808) 956-8178.',
              'https://manoa.hawaii.edu/studentlife/'),
             ('⚠ Mānoa Career Fair',
              'FALL 2026 DATE NOT PUBLISHED. ⚠ THE EMPLOYER PAGE IS EIGHTEEN MONTHS STALE — in August 2026 it was '
              'still displaying a SPRING 2025 event (5 March 2025, 10:00 a.m.–1:30 p.m., Campus Center Ballroom). '
              'Employer registration cost, deadline and eligibility are all unpublished. Call (808) 956-7007.',
              'https://manoa.hawaii.edu/careercenter/employers/career-fair/'),
             ('⚠ Hawaii Annual Innovation Challenge (HAIC, formerly HACC) — THE BEST OPPORTUNITY IN THE STATE',
              'Not a Mānoa event but UH IS A PARTNER and Mānoa students participate. Published Fall 2026 schedule: '
              'challenges announced 19 Oct; virtual kickoff 24 Oct; REGISTRATION DEADLINE 27 OCT; virtual interim '
              'workshops 31 Oct and 14 Nov. Published sponsorship tiers Petabyte $7,000+ / Terabyte $5,000–6,999 / '
              'Gigabyte $2,500–4,999 / MEGABYTE $500–2,499, handled by the IMAG Foundation, a 501(c)(3), "making '
              'all contributions 100% tax deductible." ⚠ Contact email is OBFUSCATED and NO PHONE IS PUBLISHED — '
              'use the site contact form or the HAIC Network Slack.',
              'https://haic.hawaii.gov/sponsors/'),
             ('HICSS (Hawaii International Conference on System Sciences)',
              '⚠ OUT OF WINDOW — convenes every JANUARY, so it falls outside the Sept–Dec 2026 tour entirely. Long '
              'standing UH ties. The site as fetched still surfaced HICSS-58, 7–10 January 2025, at the Hilton '
              'Waikoloa Village (stale page or stale subpage), and NO BLOCKCHAIN TRACK COULD BE CONFIRMED. Note it '
              'as a follow-on, not a tour stop.',
              'https://hicss.hawaii.edu/'),
             ('(Blockchain research centre)',
              'NONE FOUND at Mānoa.',
              'https://shidler.hawaii.edu/directory')],
  'play': 'This is the stop. If Hawaii gets one trip it is Oʻahu, and Mānoa is the reason — the only campus in the '
          'state with a large undergraduate business and CS population, 150+ RIOs to sponsor you, a required '
          'investments course every BBA student takes (FIN 311), and the one designated PUBLIC FORUM AREA anywhere '
          'in this file (the Campus Center Courtyard, at a public university bound by public-forum doctrine). ⚠ BUT '
          'DO NOT MISTAKE THE 3 FOR AN OPEN DOOR: IT IS PROVISIONAL, ASSIGNED BECAUSE THE OPERATIVE POLICY COULD '
          'NOT BE READ. M10.300 — the interim Mānoa facilities-use guidelines — was robots-blocked across ~12 '
          'attempts, and the systemwide Time, Place and Manner policy above it WAS REPLACED ON AN INTERIM BASIS ON '
          '1 JULY 2026 and is being rewritten through fall 2026. The archived 2002 predecessor that COULD be read '
          'opens with a BLANKET solicitation ban on "any building, structure, facility, or…any grounds, sidewalks, '
          'or streets" — broader than most mainland rules. THE SINGLE BEST DOOR IS ONE PHONE CALL: STUDENT LIFE & '
          'DEVELOPMENT, (808) 956-8178. Ask it for five things in one go: (1) a copy of M10.300; (2) the Fall 2026 '
          'Involvement Fair date and whether OUTSIDE entities may table — nothing is published, and the Campus '
          'Center page was still showing FALL 2023 building hours in August 2026; (3) the Campus Center rate sheet '
          'with deposits and cancellation terms; (4) the INSURANCE DOLLAR LIMIT required of non-affiliated '
          'organizations; (5) whether the new TPM policy says anything about non-affiliated persons, commercial '
          'activity, PAYMENT APPS or ON-SITE CONTRACTS. GET THE ANSWERS IN WRITING BY EMAIL — the rules are '
          'actively changing and what you are told in September may not hold in November. RUN THE ACADEMIC ROUTE '
          'IN PARALLEL AND PROBABLY PREFER IT: a guest lecture is free, non-commercial, and sits entirely outside '
          'the solicitation regime. Call QIANQIU LIU, Finance chair, (808) 956-8736, and RANDALL MINAS, MSIS '
          'director, (808) 956-7082 — chairs and program directors are the people who can authorize a slot. ⚠ IF '
          'YOU COURT A CLUB, SAY THE QUIET PART OUT LOUD: sponsorship transfers liability to the sponsor, so the '
          'RIO officer who signs for DGD is personally exposing their organization — and sponsorship probably does '
          'NOT lift the separate solicitation ban anyway. Handing out material may be fine; anything transactional '
          'probably is not. ⚠ AND BEFORE ANY OF IT, READ THE STATE REGULATORY NOTE IN policy_key: Hawaii currently '
          'requires NO money transmitter license for pure digital-asset activity, but the moment you touch US '
          'DOLLARS a license likely attaches.',
  'gaps': ['⚠⚠ M10.300, "UH Mānoa Interim Guidelines on UH Mānoa Facilities Use Practices and Procedures" — THE '
           'OPERATIVE POLICY, NEVER READ. ROBOTS-BLOCKED across ~12 attempts over ten minutes. The access rating '
           'of 3 is provisional because of this. Open it in a browser or request it from SLD, (808) 956-8178, and '
           'extract: whether outside entities may be sponsored, INSURANCE DOLLAR LIMITS, whether commercial '
           'solicitation has any exception, and any language on payment apps or on-site contracts. '
           'https://manoa.hawaii.edu/policies/m10/m10-300/',
           '⚠⚠ UH SYSTEMWIDE INTERIM TIME, PLACE AND MANNER POLICY — FULL TEXT NEVER RETRIEVED, and it REPLACED '
           'the previous policy EFFECTIVE 1 JULY 2026. Both the landing page and the circulated draft "AP 10.xxx" '
           '(11.14.25) were robots-blocked. Get the FINAL AP NUMBER, the sections on NON-AFFILIATED PERSONS and '
           'COMMERCIAL ACTIVITY, and — critically — WHEN THE FALL 2026 COMMUNITY-DISCUSSION REVISIONS LAND, '
           'because the rules may change mid-tour. https://www.hawaii.edu/tpm-policy/',
           '⚠ FALL 2026 INVOLVEMENT FAIR — date, whether OUTSIDE entities may table, and cost. NOTHING IS '
           'PUBLISHED. The Fall 2025 event page was robots-blocked and the Campus Center landing page was still '
           'showing FALL 2023 building hours in August 2026. Call (808) 956-8178. '
           'https://manoa.hawaii.edu/studentlife/',
           '⚠ CAMPUS CENTER RATE SHEET, DEPOSITS, CANCELLATION TERMS AND THE INSURANCE DOLLAR LIMIT — all '
           'unpublished; the planning page is robots-blocked. A1.200 requires "evidence of adequate insurance '
           'protection" from all non-affiliated organizations but states NO LIMITS. Ask SLD. '
           'https://manoa.hawaii.edu/studentlife/campus-center-complex/meetings-events/planning-an-event/',
           '⚠ DOES A BLOCKCHAIN / CRYPTO / FINTECH / INVESTMENT CLUB EXIST AT MĀNOA? UNRESOLVED — the RIO '
           'directory was robots-blocked and 150+ RIOs were never listed. Ask SLD to search the roster. Also '
           'verify whether the Civil Beat piece of May 2026 on a student-run stock portfolio concerns a Mānoa '
           'club — it would be the warmest audience on campus. '
           'https://www.civilbeat.org/2026/05/student-run-stock-portfolio-could-fund-scholarships/',
           '⚠ MĀNOA CAREER FAIR FALL 2026 — date, cost, and whether a crypto project is an ELIGIBLE EMPLOYER. The '
           'employer page is EIGHTEEN MONTHS STALE (still showing 5 March 2025). Call (808) 956-7007. '
           'https://manoa.hawaii.edu/careercenter/employers/career-fair/',
           'ICS (Information & Computer Sciences) COURSE LISTING — never read, robots-blocked. A cryptography or '
           'distributed-systems course would be the most natural academic fit on this campus and no ICS phone '
           'number was confirmed either. https://www.ics.hawaii.edu/courses/',
           'HAR TITLE 20, SUBTITLE 1, CHAPTER 13 §§ 20-13-1 to 20-13-9 "Use of University-Owned Facilities" — '
           'confirmed to EXIST but SECTION TEXT NEVER READ. It sits above every campus policy. '
           'https://www.law.cornell.edu/regulations/hawaii/title-20/subtitle-1',
           'Fall 2026 term offering for FIN 311 Investments and for the MSF/MSIS graduate seminars — catalog '
           'listing is not term offering. Qianqiu Liu (808) 956-8736 or Randall Minas (808) 956-7082.'],
  'note': '⚠ STALE PAGES ARE THE NORM AT MĀNOA, NOT THE EXCEPTION. The Campus Center Complex landing page was '
          'still showing FALL 2023 BUILDING HOURS in August 2026, and the Career Center employer page was still '
          'advertising a MARCH 2025 career fair. Treat any date found on manoa.hawaii.edu as unconfirmed until '
          'someone says it on the phone. Separately: MĀNOA, HAWAIʻI PACIFIC AND CHAMINADE ARE ALL ON OʻAHU AND '
          '15–20 MINUTES APART — they share a single trip. UH HILO DOES NOT; it is an interisland flight.'},

 # ------------------------------------------------------------ 2. Hawaiʻi Pacific University
 {'state': 'Hawaii',
  'name': 'Hawaiʻi Pacific University',
  'city': 'Honolulu, HI (Oʻahu)',
  'type': 'Private',
  'tier': 'B — Regional',
  'access': 3,
  'start': '⚠ Mon Aug 31, 2026 — THE LATEST START IN THE STATE. A full week after both UH campuses and TWO WEEKS '
           'after Chaminade. If the tour runs Chaminade → UH → HPU it is calendar-aligned; the reverse is not.',
  'adddrop': 'Tue Sep 8, 2026 — last day to register and last day for a 100% tuition refund. Then 50% refund Tue '
             'Sep 15, 25% refund Mon Sep 28.',
  'fallbreak': 'NONE listed. Labor Day (observed) Mon Sep 7, 2026. ⚠ HPU does NOT appear to close for Election '
               'Day, unlike the UH campuses — but that was not separately confirmed.',
  'thanksgiving': 'Not separately listed on the calendar as read. ⚠ UNVERIFIED — confirm with the Registrar.',
  'lastclass': '⚠ Sun Dec 20, 2026 — A SUNDAY. As published; unusual enough to verify with the Registrar if it '
               'matters.',
  'finals': '⚠ Mon Dec 14 – Sun Dec 20, 2026 — finals run THROUGH A SUNDAY, and commencement is on a MONDAY, Dec '
            '21. Both as published. HPU\'s term ends later than every other campus in this file.',
  'cal_url': 'https://www.hpu.edu/registrar/academic-calendar.html',
  'cal_status': 'CONFIRMED — weekday checks all pass, genuine Fall 2026 data. ⚠ BUT NOT CONVENTIONAL SEMESTERS, '
                'AND THIS IS THE MOST USEFUL CALENDAR FACT IN THE STATE: HPU runs 16-WEEK TERMS WITH CONCURRENT '
                '8-WEEK ACCELERATED SESSIONS (8A and 8B) INSIDE EACH TERM. THE 8B SESSION STARTING AROUND LATE '
                'OCTOBER MEANS A SECOND COHORT OF NEWLY-ENROLLED STUDENTS ARRIVES MID-TERM — a genuine second '
                'outreach window that no other Hawaii campus offers except Chaminade\'s October accelerated '
                'session. ⚠ The exact 8B start date was not published on any page read.',
  'fair': '⚠ NONE PUBLISHED — no club fair or involvement fair appears on any HPU page that could be read',
  'fair_date': '⚠ NOTHING PUBLISHED, AND NO RELIABLE RECURRING PATTERN EITHER — not on the Student Engagement '
               'page, not on the clubs page, not on the events calendar. This is unusual and worth saying plainly: '
               'HPU may hold one and simply not publish it, or may not hold one at all. ⚠ WHAT IS KNOWN AND IS '
               'ACTIONABLE: the Student Engagement page states the RSO listing for the academic year is finalized '
               '"BY SEPTEMBER 15, ONCE ALL REGISTRATIONS ARE COMPLETE." (That language referenced 2025–26 and may '
               'itself be stale.) SO HPU\'S CLUB ROSTER IS NOT SETTLED UNTIL MID-SEPTEMBER, AND A TABLING PUSH '
               'BEFORE ~15 SEPTEMBER IS AIMED AT CLUBS THAT MAY NOT YET BE RE-REGISTERED. Call (808) 544-0277 or '
               'email leadership@hpu.edu.',
  'fair_outside': 'UNKNOWN — nothing published either way, because no fair is published at all. At a private '
                  'university with no written policy on the subject, this is a person\'s decision on a phone call, '
                  'not a rule. (808) 544-0277.',
  'fair_cost': 'UNVERIFIED — no fee schedule, rate card or tier is published anywhere on hpu.edu.',
  'fair_deadline': 'UNVERIFIED. The one date that functions like a deadline is ~SEP 15, when the RSO roster is '
                   'finalized — before that, the clubs you would be pitching may not be registered yet.',
  'fair_url': 'https://www.hpu.edu/student-engagement/clubs/index.html',
  'policy': '⚠ NO WRITTEN SOLICITATION, VENDOR, TABLING OR FACILITIES-USE POLICY COULD BE LOCATED ANYWHERE AT HPU. '
            'HPU is PRIVATE: no public-forum doctrine, no state campus free-speech statute reaching it, no First '
            'Amendment claim. Access is entirely at HPU\'s discretion.',
  'policy_url': 'https://studenthandbook.hpu.edu/',
  'policy_key': "⚠⚠ THERE IS NOTHING TO QUOTE — AND THAT IS THE FINDING. NO SOLICITATION, VENDOR, TABLING, "
                "POSTING, FACILITIES-USE OR EVENT POLICY EXISTS ON ANY HPU PAGE THAT COULD BE READ. This was "
                "checked, not assumed. The online Student Handbook (https://studenthandbook.hpu.edu/) has three "
                "sections plus general information: Section One: Student Services, Departments and Programs (36+ "
                "offices); Section Two: Housing & Residence Life; Section Three: University Policies and "
                "Procedures. SECTION THREE COVERS ACADEMIC INTEGRITY, THE CODE OF STUDENT CONDUCT AND STUDENT "
                "RIGHTS — NOTHING ON OUTSIDE VENDORS. ⚠ AND THE USUAL HIDING PLACE IS CLOSED: the old PDF "
                "handbook (www.hpu.edu/student-life/files/student_handbook_webversion_2023_2024.pdf) NOW "
                "302-REDIRECTS TO THE HTML HANDBOOK. PDF handbooks are normally where these policies live; at HPU "
                "that avenue is gone. ⚠ THE ACCESS RATING OF 3 IS PROVISIONAL AND MEANS 'APPROVAL REQUIRED FROM A "
                "PERSON,' NOT 'DOCUMENTED ROUTE.' PRACTICAL READ, AND IT CUTS BOTH WAYS: THERE IS NO WRITTEN "
                "PROHIBITION TO OVERCOME — but there is ALSO NO WRITTEN ENTITLEMENT TO INVOKE AND NO APPEAL. "
                "ACCESS WILL BE DECIDED BY ONE PERSON IN THE STUDENT LIFE OFFICE ON A PHONE CALL. ⚠ GET ANY "
                "PERMISSION IN WRITING BY EMAIL — with nothing published, an email is the only record that will "
                "exist. ⚠ HPU IS PRIVATE: DO NOT REASON FROM UH'S RULES. The UH systemwide interim Time, Place "
                "and Manner policy effective 1 July 2026, HAR Title 20 Chapter 13, and public-forum doctrine ALL "
                "BIND UH AND NONE OF THEM BIND HPU. Citing them here will read as not having done the homework. "
                "⚠ UNVERIFIED BUT MUST BE ASKED ON THE FIRST CALL, BECAUSE NONE OF IT IS PUBLISHED: insurance "
                "requirements and dollar limits; space rental fees; deposits; cancellation terms; WHETHER AN RSO "
                "MUST SPONSOR AN OUTSIDE GROUP; and WHETHER FINANCIAL-PRODUCT MARKETING IS SPECIFICALLY "
                "RESTRICTED. ABSENCE OF PUBLISHED TEXT IS NOT PERMISSION — at a private institution these terms "
                "are CONTRACT TERMS, so their absence from the web is EXPECTED RATHER THAN INFORMATIVE. Read "
                "silence as 'the terms are in a document you have not seen yet.' ⚠ FUNDING ANGLE WORTH KNOWING "
                "BEFORE THE CALL: HPU has a STUDENT ACTIVITY FEE (SAF) FUND that RSOs apply to for event money "
                "(https://www.hpu.edu/student-engagement/student-activity-fee/index.html). A CLUB WITH SAF MONEY "
                "CAN HOST A SPEAKER WITHOUT DGD PAYING A VENUE FEE — which, with no published rate card, may be "
                "the cheapest route onto this campus. ⚠⚠ STATE REGULATORY: Hawaii's money-transmission and "
                "digital-currency position is recorded in full in the UH MĀNOA policy_key and APPLIES STATEWIDE, "
                "including here. Short version: NO Hawaii money transmitter license is currently required for "
                "pure digital-asset activity (DFI FAQ, 9 Feb 2024, after the Digital Currency Innovation Lab "
                "sunset on 30 June 2024), BUT ANY ACTIVITY IN US DOLLARS THAT MEETS THE DEFINITION OF MONEY "
                "TRANSMISSION 'WILL LIKELY REQUIRE A MONEY TRANSMITTER LICENSE.' Confirm with the Hawaii Division "
                "of Financial Institutions, https://cca.hawaii.gov/dfi/ .",
  'sponsor_required': '⚠ UNKNOWN — NOTHING IS PUBLISHED EITHER WAY, and this is one of the specific questions to '
                      'ask on the first call to (808) 544-0277. The likely-cheapest route is an RSO sponsor '
                      'funded by the STUDENT ACTIVITY FEE (SAF), which lets a club host a speaker without DGD '
                      'paying any venue fee. ⚠ BUT THE RSO ROSTER IS NOT FINALIZED UNTIL ~15 SEPTEMBER, so before '
                      'mid-September you may be courting clubs that are not yet re-registered.',
  'clubs': [('⚠ HPU PUBLISHES CATEGORIES, NOT A ROSTER — TREAT THE LIST AS UNPUBLISHED, NOT EMPTY',
             'The clubs page lists only categories: Academic/Professional, Film/Publications/Media Art, Fitness '
             'and Wellness, Games and Gaming, Lōkahi, Performing Arts, Service, Special Interests. ⚠ THE FULL '
             'ROSTER IS NOT PUBLISHED UNTIL ROUGHLY 15 SEPTEMBER, "once all registrations are complete." Call '
             '(808) 544-0277 AFTER THAT DATE and ask specifically for business, finance, economics, analytics and '
             'CS clubs.',
             'https://www.hpu.edu/student-engagement/clubs/index.html'),
            ('⚠ NO BUSINESS / FINANCE / ECONOMICS / INVESTMENT / ENTREPRENEURSHIP / CS / DATA SCIENCE / FINTECH / '
             'BLOCKCHAIN CLUB IS NAMED — BUT THIS IS A DIRECTORY LIMITATION, NOT A VERIFIED ABSENCE',
             'HPU has a BSBA with a FINANCE AND ECONOMICS concentration and an MS in Business Analytics, so one '
             'may well exist and simply not be listed. The public directory does not surface it and the roster is '
             'unpublished until mid-September. DO NOT ASSERT ABSENCE.',
             'https://www.hpu.edu/student-engagement/clubs/index.html'),
            ('Campus Activities Board (CAB)',
             '"A student-led, student-driven organization dedicated to enhancing the student experience through '
             'quality entertainment, creative programming, and community involvement." ⚠ THE BEST NAMED SPONSOR '
             'CANDIDATE AT HPU by function — it is the body that already programs events for the whole campus, so '
             'it does not need a subject-matter match to host something.',
             'https://www.hpu.edu/student-engagement/campus-activities-board/cab.html'),
            ('Student Government Association (SGA)',
             'The other campus-wide body, and the escalation route if CAB is unresponsive.',
             'https://www.hpu.edu/student-engagement/student-government/index.html'),
            ('Student Occupational Therapy Association (SOTA)',
             'Low relevance, listed because it is one of the few organizations actually NAMED on a live HPU page — '
             'a useful demonstration that the directory is thin rather than that the campus is. Advisors Dr. '
             'Emerson Hart (eehart@hpu.edu) and Dr. Julia Graham (jagraham@hpu.edu). Marine Science and Pre-Health '
             'clubs are also referenced under Academic/Professional.',
             'https://www.hpu.edu/student-engagement/clubs/index.html'),
            ('⚠ Student Activity Fee (SAF) fund — the funding mechanism, not a club',
             'RSOs apply to the SAF for event money. ⚠ A CLUB WITH SAF MONEY CAN HOST A SPEAKER WITHOUT DGD PAYING '
             'A VENUE FEE — with no published rate card anywhere at HPU, this may be the cheapest route onto the '
             'campus.',
             'https://www.hpu.edu/student-engagement/student-activity-fee/index.html')],
  'faculty': [('⚠ Office of Student Activities / Student Life',
               'THE OFFICE THAT DECIDES ACCESS AT HPU, AND (808) 544-0277 IS A GENUINE DIRECT LINE — not a '
               'switchboard. It runs RSOs and campus programming. Ask it, in one call: does any written '
               'solicitation or facility-use policy exist at all; may an outside organization table; must an RSO '
               'sponsor us; what are the insurance requirement and limit, rental fees, deposits and cancellation '
               'terms; is financial-product marketing restricted; and is there a club fair. ⚠ GET THE ANSWER BY '
               'EMAIL. Aloha Tower Marketplace, Suite 1400.',
               'Student Activities / Student Life',
               'studentlife@hpu.edu · (808) 544-0277 (direct)',
               'https://www.hpu.edu/student-activities/'),
              ('RSO inquiries',
               'The registered-student-organization inbox — the route to a club sponsor and to the roster that is '
               'not published until ~15 September. No separate phone number is published for it; use '
               '(808) 544-0277.',
               'Student Engagement',
               'leadership@hpu.edu · no direct number published — use (808) 544-0277',
               'https://www.hpu.edu/student-engagement/clubs/index.html'),
              ('HPU main line',
               'MAIN LINE / SWITCHBOARD — the fallback for every HPU office that publishes no direct number. Also '
               'reachable toll-free.',
               'Hawaiʻi Pacific University',
               '(808) 544-0200 (main line) · toll-free 1-866-CALL-HPU',
               'https://www.hpu.edu/'),
              ('Student Conduct Office',
               'Rules on what a sponsoring RSO may and may not do. ⚠ THE NUMBER PUBLISHED FOR IT IS THE HPU MAIN '
               'LINE, not a direct line — ask for the office by name. 1 Aloha Tower Drive, Honolulu HI 96813.',
               'Student Conduct',
               'cmorman@hpu.edu · (808) 544-0200 (HPU main line)',
               'https://studenthandbook.hpu.edu/sectionone/student-conduct-office'),
              ('Xin Fang, Ph.D.',
               'Professor, College of Business — a CONFIRMED direct office line, which is unusually good. ⚠ HIS '
               'SPECIFIC FIELD IS NOT CONFIRMED: do NOT describe him as a finance or crypto specialist. Listed '
               'because HPU\'s faculty directory publishes direct numbers and he is one of two business professors '
               'whose number was actually read.',
               'College of Business',
               'xfang@hpu.edu · (808) 544-0801 (direct)',
               'https://www.hpu.edu/faculty/index.html'),
              ('Joseph Ha, Ph.D.',
               'Professor, College of Business — second confirmed direct office line. ⚠ SPECIFIC FIELD NOT '
               'CONFIRMED.',
               'College of Business',
               'jha@hpu.edu · (808) 544-0826 (direct)',
               'https://www.hpu.edu/faculty/index.html'),
              ('Amy Nguyen-Chyung, Ph.D., MBA-MPA',
               'DEAN, COLLEGE OF BUSINESS — the school-level approval and the person who could place a speaker in '
               'front of the BSBA Finance and Economics cohort. ⚠ NO DIRECT NUMBER WAS FOUND; route through the '
               'main line or the faculty directory. College of Business, 1 Aloha Tower Drive, Honolulu HI 96813.',
               'College of Business',
               'no direct number found — look up here; or main line (808) 544-0200',
               'https://www.hpu.edu/cob/index.html'),
              ('⚠ HPU faculty directory — MINE THIS',
               'HPU PUBLISHES DIRECT OFFICE PHONE NUMBERS FOR FACULTY, which is unusually generous and is the '
               'fastest way to close the people gap here. It is an alphabetical A–Z table with photos, names, '
               'titles, departments, EMAIL AND PHONE, with a "VIEW ALL" option. Only a fragment was read. TO FIND '
               'THE FINANCE AND ECONOMICS FACULTY, PAGE THROUGH IT BY LETTER.',
               'Faculty directory',
               'directory publishes direct numbers — look up here; main line (808) 544-0200',
               'https://www.hpu.edu/faculty/index.html')],
  'courses': [('BS in Business Administration (BSBA) / BS in Global Business',
               'A 4-year BSBA and a 3-YEAR BS in Global Business, with concentrations including ⚠ FINANCE AND '
               'ECONOMICS, plus Accounting, Management, Marketing, Hospitality & Tourism Management and '
               'International Business Management. THIS IS A REAL UNDERGRADUATE BUSINESS POPULATION — HPU is not a '
               'health-sciences-only or graduate-only campus. NO INDIVIDUAL COURSE CODES WERE VERIFIED.',
               'https://www.hpu.edu/cob/index.html'),
              ('MS in Business Analytics; MBA; MS Construction Management; DBA',
               'Graduate programs. The MS in Business Analytics is the most quantitatively adjacent audience at '
               'HPU. The DBA is offered with Mandarin translation — consistent with a heavily international '
               'student body.',
               'https://www.hpu.edu/cob/index.html'),
              ('(Blockchain / crypto / digital assets / fintech)',
               '⚠ NONE CONFIRMED — AND THIS IS AN UNCLOSED GAP, NOT A VERIFIED ABSENCE. The catalog '
               'course-description pages were attempted (catalog.hpu.edu/coursedescriptions/fin and '
               '/courseinfo/e-j) and BOTH RETURNED 404. The catalog organizes courses in FOUR ALPHABETICAL BLOCKS '
               'BY SUBJECT PREFIX and the correct URL pattern was not discoverable without search. BROWSE '
               'MANUALLY FROM https://catalog.hpu.edu/ → Courses.',
               'https://catalog.hpu.edu/')],
  'events': [('⚠ NO FALL 2026 EVENT OF ANY KIND IS CONFIRMED AT HPU',
              'No career fair, speaker series, startup week or hackathon is published for Fall 2026 on any HPU '
              'page that could be read. UNCLOSED GAP, NOT AN EMPTY ONE. Events calendar: '
              'https://www.hpu.edu/calendar/index.html',
              'https://www.hpu.edu/calendar/index.html'),
             ('⚠ The 8B accelerated session — the one genuine timing advantage at HPU',
              'Not a dated event but the reason HPU is worth a second look: 8-WEEK SESSIONS RUN INSIDE THE 16-WEEK '
              'TERM, AND 8B STARTS AROUND LATE OCTOBER, BRINGING A SECOND COHORT OF NEWLY-ENROLLED STUDENTS ONTO '
              'CAMPUS MID-TERM. A SECOND BITE AT THE APPLE THAT UH MĀNOA AND UH HILO DO NOT OFFER. ⚠ The exact 8B '
              'start date was not published — ask the Registrar.',
              'https://www.hpu.edu/registrar/academic-calendar.html'),
             ('⚠ RSO roster finalized ~Sep 15',
              'Functionally a date-certain event: "by September 15, once all registrations are complete." Before '
              'it, the clubs you would be pitching may not be re-registered. After it, ask (808) 544-0277 for the '
              'business, finance, econ, analytics and CS clubs by name.',
              'https://www.hpu.edu/student-engagement/clubs/index.html')],
  'play': 'Worth the visit, and cheap to add — HPU is fifteen to twenty minutes from Mānoa at Aloha Tower '
          'Marketplace in downtown Honolulu, so it costs a taxi and half a day on a trip you are already taking. '
          'It has a genuine undergraduate business population with a FINANCE AND ECONOMICS concentration, an MS in '
          'Business Analytics, a heavily international student body, and — unusually — ONE SOLID DIRECT LINE TO '
          'THE OFFICE THAT ACTUALLY DECIDES: (808) 544-0277. ⚠ THE DEFINING FACT HERE IS THAT THERE IS NOTHING '
          'WRITTEN, IN EITHER DIRECTION. No solicitation policy, no vendor policy, no tabling rule, no '
          'facilities-use section — checked across the whole student handbook, and the old PDF handbook now '
          'redirects away. HPU IS PRIVATE, so there is no public-forum argument, no state statute, and no appeal; '
          'DO NOT REASON FROM UH\'S RULES, WHICH DO NOT BIND IT. That cuts both ways: nothing to overcome, nothing '
          'to invoke. ACCESS IS ONE PERSON\'S DECISION ON ONE PHONE CALL, SO MAKE THE CALL GOOD AND GET THE ANSWER '
          'IN WRITING BY EMAIL — an email will be the only record that exists. Ask on that call: does any written '
          'policy exist at all; may an outside organization table; must an RSO sponsor us; what are the insurance '
          'limit, fees, deposits and cancellation terms; is financial-product marketing restricted; and is there a '
          'club fair, because none is published anywhere. ⚠ TIME IT DELIBERATELY. HPU STARTS LATEST IN THE STATE, '
          'MON AUG 31 — a week after UH, two weeks after Chaminade — so it must come last in any sequenced trip. '
          'And its RSO ROSTER IS NOT FINALIZED UNTIL ~15 SEPTEMBER, so a club-sponsor conversation before then is '
          'aimed at organizations that may not yet be re-registered. The cheapest route in is an RSO funded by the '
          'STUDENT ACTIVITY FEE, which can host a speaker without DGD paying a venue fee — start with the CAMPUS '
          'ACTIVITIES BOARD, whose whole function is programming events. ⚠ THE ONE STRUCTURAL ADVANTAGE WORTH '
          'PLANNING AROUND: the 8-WEEK 8B SESSION STARTING LATE OCTOBER PUTS A SECOND COHORT OF NEW STUDENTS ON '
          'CAMPUS MID-TERM. If Oʻahu gets two visits, the second one should land in that window.',
  'gaps': ['⚠⚠ DOES ANY WRITTEN SOLICITATION OR FACILITY-USE POLICY EXIST AT HPU AT ALL? None could be found '
           'anywhere on hpu.edu or in the student handbook, and the old PDF handbook now 302-redirects to HTML. '
           'ASK STUDENT ACTIVITIES DIRECTLY WHETHER ONE EXISTS IN WRITING, and get any permission by email. '
           '(808) 544-0277. https://studenthandbook.hpu.edu/',
           '⚠⚠ INSURANCE REQUIREMENT AND LIMIT, SPACE RENTAL FEES, DEPOSITS, CANCELLATION TERMS, WHETHER AN RSO '
           'MUST SPONSOR AN OUTSIDE GROUP, AND WHETHER FINANCIAL-PRODUCT MARKETING IS RESTRICTED — NONE ARE '
           'PUBLISHED. At a private institution these are contract terms; absence from the web is expected. '
           '(808) 544-0277.',
           '⚠ DOES HPU HOLD A CLUB FAIR AT ALL? Nothing is published on the Student Engagement page, the clubs '
           'page or the events calendar, and no recurring pattern could be established. It is possible none '
           'exists. (808) 544-0277 or leadership@hpu.edu. https://www.hpu.edu/calendar/index.html',
           '⚠ HPU\'S FULL RSO ROSTER — not published until roughly 15 September, "once all registrations are '
           'complete." Call AFTER that date and ask specifically for business, finance, economics, analytics and '
           'CS clubs. No business, finance, CS or fintech club is currently named on any page — TREAT THE ROSTER '
           'AS UNPUBLISHED, NOT EMPTY. (808) 544-0277.',
           '⚠ HPU CATALOG COURSE LISTINGS — both attempted URL patterns returned 404 '
           '(catalog.hpu.edu/coursedescriptions/fin and /courseinfo/e-j). The catalog organizes courses in four '
           'alphabetical blocks by subject prefix. BROWSE MANUALLY from https://catalog.hpu.edu/ → Courses to '
           'check for any fintech or digital-asset course.',
           'THE EXACT 8B ACCELERATED-SESSION START DATE — "around late October" is the best that could be '
           'established, and it is the single most useful scheduling fact at HPU. Registrar. '
           'https://www.hpu.edu/registrar/academic-calendar.html',
           'HPU THANKSGIVING CLOSURE DATES were not listed on the calendar as read, and whether HPU closes for '
           'Election Day (Nov 3) was not confirmed. Registrar. '
           'https://www.hpu.edu/registrar/academic-calendar.html',
           'FINANCE AND ECONOMICS FACULTY NAMES — only two College of Business professors were confirmed (Xin '
           'Fang, Joseph Ha) and NEITHER\'S FIELD IS CONFIRMED. ⚠ The faculty directory PUBLISHES DIRECT OFFICE '
           'NUMBERS and has a "VIEW ALL" option — page through it by letter; this closes fast in a browser. '
           'https://www.hpu.edu/faculty/index.html'],
  'note': '⚠ HPU IS NOT A HEALTH-SCIENCES-ONLY OR GRADUATE-ONLY CAMPUS, which is a common misconception about it. '
          'It has a real undergraduate business population with a Finance and Economics concentration. It is also '
          'DOWNTOWN, at Aloha Tower Marketplace, 1 Aloha Tower Drive — not in Mānoa valley — but the two are 15–20 '
          'minutes apart and share a trip with Chaminade in Kaimukī.'},

 # ------------------------------------------------------------ 3. UH Hilo
 {'state': 'Hawaii',
  'name': 'University of Hawaiʻi at Hilo',
  'city': 'Hilo, HI (Hawaiʻi Island)',
  'type': 'Public',
  'tier': 'C — Opportunistic',
  'access': 2,
  'start': 'Mon Aug 24, 2026 — CONFIRMED on UH Hilo\'s own Fall 2026 registrar page, weekday-checked. Identical to '
           'Mānoa: same system, same term structure.',
  'adddrop': '⚠ Last day to ADD: Tue Sep 1, 2026 — TWO WEEKS TIGHTER THAN MĀNOA\'S Sep 15 erase deadline, so Hilo '
             'schedules lock earlier and the "students still shopping" window is much shorter. Last day to DROP '
             'WITH A W: Mon Nov 2, 2026.',
  'fallbreak': '⚠ NONE — the ONLY non-holiday non-instructional day all term is Fri Nov 27. Hawaii-specific '
               'closures apply as at Mānoa: Statehood Day Fri Aug 21, 2026 (before classes), ELECTION DAY TUE NOV '
               '3, 2026 (state holiday, campus closed), Veterans Day Wed Nov 11, Labor Day Mon Sep 7.',
  'thanksgiving': 'Thu Nov 26, 2026 (Thanksgiving Day) and Fri Nov 27, 2026 (non-instructional day).',
  'lastclass': 'Thu Dec 10, 2026.',
  'finals': 'Mon–Fri Dec 14–18, 2026. Semester ends Fri Dec 18; commencement Sat Dec 19.',
  'cal_url': 'https://hilo.hawaii.edu/registrar/Fall2026SemesterAcademicCalendar.php',
  'cal_status': 'CONFIRMED — read on UH Hilo\'s own Fall 2026 registrar page, weekday checks pass. ⚠ THE CALENDAR '
                'IS THE ONLY THING THAT COULD BE CONFIRMED AT THIS CAMPUS.',
  'fair': '⚠ NOT CONFIRMED — NO DATA. Whether UH Hilo holds an involvement or club fair at all could not be '
          'established.',
  'fair_date': '⚠ NO DATA AT ALL — NOT A FALL 2026 DATE, NOT A RECURRING PATTERN, NOT TABLING ELIGIBILITY, NOT A '
               'COST. The UH Hilo Campus Center and Student Life pages were ROBOTS-BLOCKED ON EVERY ATTEMPT. The '
               'Division of Student Affairs landing page states only that "Each office has an email and phone '
               'contact and of course always welcomes in person visits" — WITHOUT LISTING ANY OF THEM. Where to '
               'look: https://hilo.hawaii.edu/studentaffairs/campuscenter/',
  'fair_outside': 'UNKNOWN — no fair could be confirmed to exist, let alone its eligibility rules. ⚠ But read the '
                  'policy_key first: UH Hilo\'s ONE READABLE expressive-activity policy qualifies EVERY permission '
                  'it grants with the word "NON-COMMERCIAL," which is a clean written basis for refusing a '
                  'for-profit table.',
  'fair_cost': 'UNVERIFIED — no data.',
  'fair_deadline': 'UNVERIFIED — no data.',
  'fair_url': 'https://hilo.hawaii.edu/studentaffairs/campuscenter/',
  'policy': '"Free Expression on the UH Hilo Campus" — READ IN FULL ON THE LIVE PAGE, and it is the sharpest '
            'single restriction found at any campus in this state. Above it: the UH systemwide INTERIM Time, '
            'Place and Manner policy effective 1 Jul 2026 and HAR Title 20 Ch. 13. ⚠ THE DOCUMENT THAT ACTUALLY '
            'GOVERNS OUTSIDE GROUPS — the UH Hilo Facilities Use Practices and Procedures — WAS ROBOTS-BLOCKED '
            'ACROSS ~10 ATTEMPTS AND WAS NEVER READ.',
  'policy_url': 'https://hilo.hawaii.edu/studentaffairs/conduct/free-expression-on-campus.php',
  'policy_key': "◆ WHAT COULD BE READ, VERBATIM — 'Free Expression on the UH Hilo Campus' "
                "(hilo.hawaii.edu/studentaffairs/conduct/free-expression-on-campus.php): 'PERSONS SPEAKING, "
                "ASSEMBLING, AND/OR DISTRIBUTING **NON-COMMERCIAL** MATERIAL SHALL NOT PHYSICALLY IMPEDE THE "
                "PROGRESS OF PASSERSBY.' And students may 'DISTRIBUTE **NON-COMMERCIAL** LITERATURE SUCH AS "
                "PETITIONS, CIRCULARS, LEAFLETS, NEWSPAPERS IN ALL AREAS GENERALLY AVAILABLE TO STUDENTS AND THE "
                "COMMUNITY.' ⚠⚠ READ THE QUALIFIER: THE WORD 'NON-COMMERCIAL' APPEARS IN EVERY PERMISSION "
                "GRANTED. UH HILO'S PUBLISHED FREE-EXPRESSION PROTECTION IS DRAFTED SO THAT IT DOES NOT REACH "
                "COMMERCIAL DISTRIBUTION AT ALL. A DGD AMBASSADOR HANDING OUT PROJECT LITERATURE IS NOT OBVIOUSLY "
                "WITHIN THE PROTECTED CATEGORY, AND A UH HILO ADMINISTRATOR READING THIS PAGE LITERALLY WOULD BE "
                "ON SOLID GROUND REFUSING. THIS IS THE SHARPEST SINGLE RESTRICTION AT ANY OF THE FOUR HAWAII "
                "CAMPUSES, AND IT IS ON A PAGE A CAMPUS OFFICER WILL ACTUALLY HAVE READ. THE ACCESS RATING OF 2 "
                "RESTS ON THIS TEXT. The page is issued under CHANCELLOR BONNIE IRWIN and VICE CHANCELLOR FOR "
                "ADMINISTRATIVE AFFAIRS KALEIHIʻIIKAPOLI 'KALEI' RAPOZA. ⚠ NOTE WHAT IT DOES *NOT* ADDRESS: "
                "non-affiliated persons, reservation or permit requirements, commercial solicitation procedures, "
                "sale of goods, or tabling. Those live elsewhere. ⚠⚠ AND 'ELSEWHERE' WAS NEVER READ — THE 2 IS "
                "PROVISIONAL IN BOTH DIRECTIONS: UH HILO FACILITIES USE PRACTICES AND PROCEDURES, "
                "https://hilo.hawaii.edu/leadership/administrative/forms/facilities-use-practices-and-procedures.php, "
                "WAS ROBOTS-BLOCKED ACROSS ~10 ATTEMPTS (robots.txt fetch ConnectTimeout). THAT is the document "
                "containing outside-group rules, sponsorship requirements, insurance limits, fees, deposits and "
                "cancellation terms. COMPLETE GAP — MUST BE OPENED IN A BROWSER. If it turns out to contain a "
                "paid or documented outside-entity route, the rating rises; if it repeats the non-commercial "
                "qualifier, it falls. DO NOT GUESS EITHER WAY. ⚠ ANTI-FRONTING / SPONSORSHIP-CURE QUESTION: "
                "UNVERIFIED FOR HILO. The ARCHIVED Mānoa policy allowed an affiliated organization to sponsor an "
                "outside group 'and thereby qualify for use of campus facilities' — WHETHER HILO'S PROCEDURES DO "
                "THE SAME IS UNKNOWN, and Mānoa's rules do not bind Hilo. ⚠ SYSTEMWIDE LAYER APPLIES HERE EXACTLY "
                "AS AT MĀNOA AND IS EQUALLY UNREAD: THE UH SYSTEMWIDE TIME, PLACE AND MANNER POLICY WAS REPLACED "
                "ON AN INTERIM BASIS EFFECTIVE 1 JULY 2026 and is being rewritten through community discussion "
                "throughout fall 2026, so ANY GUIDANCE PREDATING 1 JULY 2026 IS UNRELIABLE AND THE RULES MAY "
                "CHANGE MID-TERM. Its landing page, https://www.hawaii.edu/tpm-policy/, AND the circulated draft "
                "'AP 10.xxx' (11.14.25) WERE BOTH ROBOTS-BLOCKED AND THE OPERATIVE TEXT COULD NOT BE RETRIEVED "
                "DESPITE ~12 REPEATED ATTEMPTS; THE FINAL AP NUMBER IS UNVERIFIED. What is confirmed from press "
                "sources is that the policy 'explicitly preserves the right' of STUDENTS, FACULTY AND STAFF — "
                "AFFILIATES — to assemble spontaneously without prior approval, and that NEITHER SOURCE ADDRESSES "
                "NON-AFFILIATED PERSONS, OUTSIDE ENTITIES OR COMMERCIAL ACTIVITY. Above that: HAR Title 20, "
                "Subtitle 1, Chapter 13 §§ 20-13-1 to 20-13-9, confirmed to exist, TEXT NOT READ. ⚠ UH HILO IS "
                "PUBLIC and is bound by public-forum doctrine — BUT UNLIKE MĀNOA'S CAMPUS CENTER COURTYARD, NO "
                "DESIGNATED PUBLIC-FORUM AREA WAS IDENTIFIED FOR HILO. ⚠⚠ STATE REGULATORY: Hawaii's money-"
                "transmission and digital-currency position is recorded in full in the UH MĀNOA policy_key and "
                "applies statewide. Short version: NO Hawaii money transmitter license is currently required for "
                "pure digital-asset activity after the Digital Currency Innovation Lab sunset on 30 June 2024 "
                "(DFI FAQ, 9 Feb 2024), BUT ANY US-DOLLAR ACTIVITY MEETING THE DEFINITION OF MONEY TRANSMISSION "
                "'WILL LIKELY REQUIRE A MONEY TRANSMITTER LICENSE.' Confirm with the Hawaii Division of Financial "
                "Institutions, https://cca.hawaii.gov/dfi/ .",
  'sponsor_required': '⚠ UNVERIFIED — the document that would say so was never read. Mānoa\'s archived policy '
                      'allowed sponsorship to qualify an outside group for facility use; WHETHER HILO DOES THE '
                      'SAME IS UNKNOWN, and Mānoa\'s rules do not bind Hilo. What IS readable cuts the other way: '
                      'every permission in the UH Hilo free-expression policy is qualified "non-commercial." '
                      'Resolve by opening the Facilities Use Practices and Procedures in a browser: '
                      'https://hilo.hawaii.edu/leadership/administrative/forms/facilities-use-practices-and-procedures.php',
  'clubs': [('⚠ NO DATA — DIRECTORY PAGES ROBOTS-BLOCKED. NOT A FINDING OF ABSENCE.',
             'The existence or absence of ANY blockchain, cryptocurrency, finance, business, CS or data science '
             'organization at UH Hilo could not be confirmed. DO NOT ASSUME EITHER WAY. Starting point: '
             'https://hilo.hawaii.edu/studentaffairs/campuscenter/ — open it in a real browser.',
             'https://hilo.hawaii.edu/studentaffairs/campuscenter/'),
            ('(Officer names)',
             'NONE — no student organization, officer or advisor could be named at UH Hilo, and none is guessed '
             'here.',
             'https://hilo.hawaii.edu/studentaffairs/')],
  'faculty': [('⚠⚠ NO UH HILO PHONE NUMBER COULD BE CONFIRMED — NOT ONE',
               'THIS IS THE SECOND MOST SERIOUS GAP IN THE HAWAII PACKET, after M10.300. Every staff-listing, '
               'Campus Center, Student Affairs and College of Business page attempted was ROBOTS-BLOCKED. ⚠⚠ DO '
               'NOT GUESS A UH HILO NUMBER: UH HILO USES THE 808-932-xxxx AND 808-974-xxxx RANGES, NOT MĀNOA\'S '
               '808-956-xxxx, so a Mānoa-pattern guess would be wrong. Call the campus and build the list: Campus '
               'Center, Student Life, Dean of Students, Administrative Affairs.',
               'University of Hawaiʻi at Hilo',
               'no number published — look up here; UH Hilo uses 808-932-xxxx / 808-974-xxxx',
               'https://hilo.hawaii.edu/studentaffairs/'),
              ('⚠ Kaleihiʻiikapoli "Kalei" Rapoza',
               'VICE CHANCELLOR FOR ADMINISTRATIVE AFFAIRS — SIGNATORY ON THE FREE-EXPRESSION POLICY, AND '
               'THEREFORE LIKELY THE ULTIMATE AUTHORITY ON FACILITIES USE AT THIS CAMPUS. THE SINGLE BEST DOOR AT '
               'UH HILO. ⚠ NO CONTACT DETAILS WERE PUBLISHED ON ANY PAGE THAT COULD BE READ — the name was '
               'confirmed on a live page, the number was not. Ask for this office by name and title.',
               'Administrative Affairs',
               'no number published — look up here',
               'https://hilo.hawaii.edu/leadership/administrative/forms/facilities-use-practices-and-procedures.php'),
              ('Bonnie Irwin',
               'CHANCELLOR — the free-expression policy is issued under her. Escalation point above '
               'Administrative Affairs. ⚠ Name confirmed on a live page; NO CONTACT DETAILS PUBLISHED.',
               'Office of the Chancellor',
               'no number published — look up here',
               'https://hilo.hawaii.edu/studentaffairs/conduct/free-expression-on-campus.php'),
              ('Division of Student Affairs',
               'The division that would run any involvement fair and hold the Campus Center. ⚠ Its landing page '
               'says "Each office has an email and phone contact and of course always welcomes in person visits" '
               '— AND THEN LISTS NONE OF THEM. Robots-blocked throughout.',
               'Student Affairs',
               'no number published — look up here',
               'https://hilo.hawaii.edu/studentaffairs/'),
              ('Campus Center',
               'The venue and the office that would know whether an involvement fair exists at all. '
               'ROBOTS-BLOCKED on every attempt; no number, no staff name, no hours.',
               'Campus Center',
               'no number published — look up here',
               'https://hilo.hawaii.edu/studentaffairs/campuscenter/'),
              ('College of Business and Economics',
               'UH Hilo DOES have a College of Business and Economics — the academic door, and the place to ask '
               'who teaches anything finance-adjacent. ⚠ ROBOTS-BLOCKED; no faculty member, course or number '
               'could be confirmed.',
               'College of Business and Economics',
               'no number published — look up here',
               'https://hilo.hawaii.edu/cob/')],
  'courses': [('⚠ NO DATA — COLLEGE OF BUSINESS AND ECONOMICS PAGES ROBOTS-BLOCKED',
               'UH Hilo has a College of Business and Economics, but NO COURSE COULD BE CONFIRMED. Specific '
               'courses on blockchain, crypto, fintech or digital money are UNVERIFIED IN BOTH DIRECTIONS. Check '
               'https://hilo.hawaii.edu/cob/ and the UH Hilo catalog in a browser.',
               'https://hilo.hawaii.edu/cob/'),
              ('(UH Hilo catalog)',
               'Never read. Registration and catalog information starts at '
               'https://hilo.hawaii.edu/catalog/registration — worth one browser pass if Hilo is ever seriously '
               'considered.',
               'https://hilo.hawaii.edu/catalog/registration')],
  'events': [('⚠ NONE CONFIRMED — NO DATA',
              'No involvement fair, career fair, hackathon or speaker series could be confirmed at UH Hilo. '
              'Everything that would carry them was robots-blocked. UNCLOSED GAP, NOT AN EMPTY ONE.',
              'https://hilo.hawaii.edu/studentaffairs/campuscenter/'),
             ('⚠ Hawaii Annual Innovation Challenge (HAIC) — REACHES HILO STUDENTS WITHOUT FLYING TO HILO',
              'THE MOST USEFUL FACT IN THIS RECORD. HAIC is STATEWIDE and UH-PARTNERED, so UH Hilo students are '
              'eligible. SPONSORING HAIC REACHES THIS AUDIENCE WITHOUT AN INTERISLAND FLIGHT, A RENTAL CAR OR TWO '
              'DAYS. Fall 2026: challenges announced 19 Oct, kickoff 24 Oct, REGISTRATION DEADLINE 27 OCT, '
              'workshops 31 Oct and 14 Nov. Entry sponsorship tier $500 (Megabyte). Contact email obfuscated, no '
              'phone published — use the site form or the HAIC Network Slack.',
              'https://haic.hawaii.gov/sponsors/')],
  'play': 'Skip it, unless the ambassador is already on Hawaiʻi Island — and say that plainly rather than hedging. '
          'THIS IS THE WEAKEST COST/BENEFIT STOP IN THE STATE. ⚠⚠ MĀNOA AND HILO ARE A FLIGHT APART, NOT A DRIVE '
          'APART: UH Hilo is ~200 miles southeast of Honolulu across open ocean, with NO ferry, NO bridge and NO '
          'road. Reaching it means an interisland flight (HNL→ITO), an airfare and a half-day each direction, plus '
          'a rental car on arrival — and what that buys is roughly 3,000 students, a modest business college, and '
          'a campus where NOT ONE relevant club, course, event or PHONE NUMBER could be confirmed. ⚠ THE ONE '
          'DOCUMENT THAT COULD BE READ IS ACTIVELY UNHELPFUL: UH Hilo\'s published free-expression page qualifies '
          'EVERY permission it grants with the word "NON-COMMERCIAL" — speaking, assembling and distributing '
          'literature are all protected only in their non-commercial form. An administrator reading that page '
          'literally would be on solid ground refusing a DGD table, and that page is one a campus officer will '
          'actually have read. The facilities-use procedures that govern outside groups were ROBOTS-BLOCKED across '
          '~10 attempts and are a complete gap, so the rating could move either way — but nothing readable '
          'currently argues for going. ⚠ THE RIGHT MOVE IS TO REACH HILO STUDENTS WITHOUT FLYING TO HILO: SPONSOR '
          'THE HAWAII ANNUAL INNOVATION CHALLENGE, which is statewide, UH-partnered, priced from $500 and closes '
          'registration 27 October. That reaches this audience for less than the airfare. If Hilo must be worked '
          'anyway, ONE CALL IS THE WHOLE CAMPUS: ask for KALEI RAPOZA, VICE CHANCELLOR FOR ADMINISTRATIVE AFFAIRS '
          '— he signs the free-expression policy and is therefore the likeliest authority on facilities use. ⚠⚠ '
          'AND YOU WILL HAVE TO FIND THE NUMBER YOURSELF: NOT ONE UH HILO PHONE NUMBER COULD BE CONFIRMED, AND DO '
          'NOT GUESS ONE — HILO USES THE 808-932-xxxx AND 808-974-xxxx RANGES, NOT MĀNOA\'S 808-956-xxxx.',
  'gaps': ['⚠⚠ UH HILO FACILITIES USE PRACTICES AND PROCEDURES — NEVER READ, ROBOTS-BLOCKED ACROSS ~10 ATTEMPTS. '
           'This is the document containing outside-group rules, sponsorship requirements, insurance limits, '
           'fees, deposits and cancellation terms. COMPLETE GAP — the access rating of 2 rests only on the '
           'free-expression page and could move in either direction once this is read. MUST BE OPENED IN A '
           'BROWSER. '
           'https://hilo.hawaii.edu/leadership/administrative/forms/facilities-use-practices-and-procedures.php',
           '⚠⚠ NOT ONE UH HILO PHONE NUMBER COULD BE CONFIRMED. Every staff-listing, Campus Center, Student '
           'Affairs and College of Business page was robots-blocked. Call the campus and build the list from '
           'scratch: Campus Center, Student Life, Dean of Students, and Administrative Affairs (VC Kalei '
           'Rapoza\'s office). ⚠ DO NOT GUESS — UH Hilo uses 808-932-xxxx / 808-974-xxxx, not 808-956-xxxx. '
           'https://hilo.hawaii.edu/studentaffairs/',
           '⚠ DOES UH HILO HOLD AN INVOLVEMENT FAIR AT ALL? No date, no recurring pattern, no tabling '
           'eligibility, no cost — the Campus Center and Student Life pages were robots-blocked on every attempt. '
           'https://hilo.hawaii.edu/studentaffairs/campuscenter/',
           '⚠ NO DESIGNATED PUBLIC-FORUM AREA WAS IDENTIFIED AT UH HILO, unlike Mānoa\'s Campus Center '
           'Courtyard. UH Hilo is public and bound by public-forum doctrine regardless, but there is no named '
           'space to point to. Ask Administrative Affairs.',
           'UH HILO CLUBS — the existence or absence of any blockchain, finance, business, CS or data science '
           'organization is completely unknown; directory pages robots-blocked. Do not assume either way. '
           'https://hilo.hawaii.edu/studentaffairs/campuscenter/',
           'UH HILO COURSES — College of Business and Economics pages robots-blocked; no course confirmed and no '
           'crypto/fintech course verified in either direction. https://hilo.hawaii.edu/cob/',
           '⚠ THE UH SYSTEMWIDE INTERIM TPM POLICY applies at Hilo exactly as at Mānoa and is EQUALLY UNREAD — '
           'replaced on an interim basis EFFECTIVE 1 JULY 2026, being rewritten through fall 2026, full text '
           'never retrieved despite ~12 attempts, final AP number unverified. https://www.hawaii.edu/tpm-policy/'],
  'note': '⚠⚠ HILO IS NOT A DRIVE FROM HONOLULU. UH Hilo is on HAWAIʻI ISLAND, ~200 miles southeast of Oʻahu '
          'across open ocean — interisland flight only (HNL→ITO), no ferry, no bridge, no road. Budget a half-day '
          'and an airfare EACH DIRECTION plus a rental car in Hilo. It shares no trip with any other campus in '
          'this file: Mānoa, HPU and Chaminade are all on Oʻahu and all within 15–20 minutes of each other.'},

 # ------------------------------------------------------------ 4. Chaminade
 {'state': 'Hawaii',
  'name': 'Chaminade University of Honolulu',
  'city': 'Honolulu, HI (Kaimukī, Oʻahu)',
  'type': 'Private (religious)',
  'tier': 'C — Opportunistic',
  'access': 2,
  'start': '⚠ Mon Aug 17, 2026 — THE EARLIEST START IN THE STATE, and unusually early nationally. A WEEK before '
           'both UH campuses and TWO WEEKS before HPU.',
  'adddrop': 'Mon Aug 17 – Tue Aug 25, 2026.',
  'fallbreak': '⚠ NONE listed. Labor Day Mon Sep 7, 2026. ⚠ CHAMINADE OBSERVES INDIGENOUS PEOPLE\'S DAY, MON OCT '
               '12, 2026 — UH DOES NOT. And CHAMINADE DOES *NOT* CLOSE FOR ELECTION DAY NOV 3 — UH DOES. The two '
               'systems close on different days; check before booking either.',
  'thanksgiving': 'Thu–Fri Nov 26–27, 2026 — no classes, offices closed.',
  'lastclass': '⚠⚠ Fri Dec 4, 2026 — THE EARLIEST TERM END IN THE STATE. Mānoa is still teaching until Dec 10 and '
               'examining until Dec 18. THE ACTIONABLE CHAMINADE WINDOW CLOSES ROUGHLY TWO WEEKS BEFORE EVERYONE '
               'ELSE\'S — anything here must be scheduled before late November.',
  'finals': 'Mon–Thu Dec 7–10, 2026. Chaminade is done examining before Mānoa and Hilo even begin finals.',
  'cal_url': 'https://catalog.chaminade.edu/academiccalendar/semester',
  'cal_status': 'CONFIRMED — weekday checks pass. ⚠ SEMESTERS (16 WEEKS) PLUS A PARALLEL ACCELERATED SYSTEM. Per '
                'the catalog: "The semester calendar consists of a Spring and a Fall term, each approximately 16 '
                'weeks in length as well as three summer sessions of varying lengths. THE FOUR ACCELERATED '
                'SESSIONS BEGIN IN JANUARY, APRIL, JULY AND OCTOBER." ⚠ THE OCTOBER ACCELERATED SESSION IS A '
                'MODEST SECOND ENTRY POINT — but it mostly serves ADULT AND WORKING STUDENTS rather than '
                'traditional undergraduates, so do not overrate it. Exact October start date not published on the '
                'pages read.',
  'fair': '⚠ NO FALL 2026 CLUB FAIR OR INVOLVEMENT FAIR IS PUBLISHED. The Office of Student Engagement (formerly '
          'the Office of Student Activities and Leadership, OSAL) would run any such event.',
  'fair_date': '⚠ NOTHING PUBLISHED FOR FALL 2026. ⚠ AND CALIBRATE EXPECTATIONS BEFORE SPENDING A CALL ON IT: '
               'WITH TEN RECOGNIZED STUDENT ORGANIZATIONS CAMPUS-WIDE, A "CLUB FAIR" AT CHAMINADE IS A SMALL '
               'AFFAIR. Where it would post: https://chaminade.edu/student-engagement/ . Call (808) 739-8556.',
  'fair_outside': 'UNKNOWN — no fair is published, so no eligibility rule exists to read. ⚠ But the governing '
                  'handbook is unambiguous about the general case: "ONLY REGISTERED STUDENT CLUBS/ORGANIZATIONS, '
                  'UNIVERSITY DEPARTMENTS, OR AGENCIES MAY HOST UNAFFILIATED SPEAKERS OR ACTS ON CAMPUS," and '
                  'partnering with an unregistered entity requires the DIRECTOR\'S WRITTEN APPROVAL. Assume the '
                  'same gate applies to any table.',
  'fair_cost': 'UNVERIFIED for a fair. ⚠ WHAT IS PUBLISHED AND WILL BITE: A FACILITIES REQUEST SUBMITTED WITH '
               'LESS THAN 10 BUSINESS DAYS\' NOTICE INCURS A $200 LATE FEE. Room requests require 10 business '
               'days; car washes 15 business days; vans 7 business days with a 90-mile round-trip cap and $2/mile '
               'overage. Rental rates, deposits and insurance requirements are NOT PUBLISHED — ask Facilities, '
               '(808) 735-4869.',
  'fair_deadline': '⚠ THE BINDING CONSTRAINT IS NOT THE ROOM BOOKING — IT IS ADVANCEMENT APPROVAL. Room requests: '
                   '10 BUSINESS DAYS (below that, a $200 LATE FEE). But off-campus fundraising requiring vendor '
                   'contact needs OFFICE OF ADVANCEMENT APPROVAL 6 WEEKS PRIOR, and ALL corporate sponsorship '
                   'must be cleared by the Director AND the VP of Advancement BEFORE SOLICITATION. BUILD IN SIX '
                   'WEEKS, NOT TEN BUSINESS DAYS.',
  'fair_url': 'https://chaminade.edu/student-engagement/',
  'policy': '"Handbook for Student Clubs & Organizations," Chaminade Office of Student Activities and Leadership, '
            'UPDATED OCTOBER 2022 — a PDF, and the governing document. ⚠ The Campus Community Policies index '
            'contains NO solicitation, vendor, facility-use, posting or freedom-of-expression policy at all. '
            'Chaminade is PRIVATE and CATHOLIC (Marianist): no public-forum obligation, no state statute reach, '
            'and — uniquely among these four campuses — AN EXPLICIT VALUES-BASED DISCRETIONARY VETO.',
  'policy_url': 'https://assets.chaminade.edu/wp-content/uploads/2022/10/04094553/Handbook-for-Student-Clubs-Organizations-Chaminade-Office-of-Student-Activities-and-Leadership.pdf',
  'policy_key': "◆ THE MOST RESTRICTIVE REGIME OF THE FOUR HAWAII CAMPUSES, AND THE MOST EXPLICIT — WHICH AT "
                "LEAST MEANS YOU CAN READ IT. Governing document: 'HANDBOOK FOR STUDENT CLUBS & ORGANIZATIONS,' "
                "Chaminade Office of Student Activities and Leadership, UPDATED OCTOBER 2022 (PDF). VERBATIM: "
                "'ONLY REGISTERED STUDENT CLUBS/ORGANIZATIONS, UNIVERSITY DEPARTMENTS, OR AGENCIES MAY HOST "
                "UNAFFILIATED SPEAKERS OR ACTS ON CAMPUS.' Groups CANNOT PARTNER WITH UNREGISTERED ENTITIES "
                "WITHOUT WRITTEN APPROVAL OF THE DIRECTOR. 'THE DIRECTOR OF STUDENT ACTIVITIES & LEADERSHIP AND "
                "THE OFFICE OF ADVANCEMENT MUST APPROVE ALL ON-CAMPUS FUNDRAISING.' 'CORPORATE SPONSORSHIP OF "
                "EVENTS ON CAMPUS IS PERMISSIBLE TO THE EXTENT THAT IT DOES NOT PROMOTE VALUES COUNTER TO THOSE "
                "OF THE UNIVERSITY.' The DIRECTOR AND THE VP OF ADVANCEMENT MUST CLEAR ALL SPONSORSHIPS *BEFORE* "
                "SOLICITATION. Off-campus fundraising requiring vendor contact needs Office of Advancement "
                "approval 6 WEEKS PRIOR. SPACE RESERVATION: room requests require 10 BUSINESS DAYS advance "
                "notice; a facilities request submitted with LESS THAN 10 BUSINESS DAYS NOTICE INCURS A $200 LATE "
                "FEE. (Car washes 15 business days; vans 7 business days, 90-mile round-trip cap, $2/mile "
                "overage.) ◆ HOW TO READ IT FOR DGD: (a) ⚠ SPONSORSHIP DOES *NOT* SIMPLY CURE THE PROBLEM HERE. A "
                "club may host you, but THE PARTNERSHIP ITSELF NEEDS THE DIRECTOR'S **WRITTEN** APPROVAL, and any "
                "corporate sponsorship needs DIRECTOR + VP OF ADVANCEMENT clearance BEFORE YOU EVEN SOLICIT. THAT "
                "IS A TWO-SIGNATURE PRIOR-RESTRAINT CHAIN WITH A FUNDRAISING OFFICE IN IT — and Advancement's job "
                "is to protect the university's donor relationships, so a crypto project is EXACTLY THE KIND OF "
                "COUNTERPARTY IT EXISTS TO SCREEN. (b) ⚠⚠ THE 'VALUES COUNTER TO THOSE OF THE UNIVERSITY' CLAUSE "
                "IS A DISCRETIONARY VETO AT A CATHOLIC INSTITUTION. THERE IS NO APPEAL AND NO NEUTRALITY "
                "REQUIREMENT. ASSUME IT WILL BE INVOKED IF ANYONE OBJECTS. This is the reason the access rating "
                "is 2 rather than 3: a documented route exists, but it is narrow, discretionary and "
                "double-gated. (c) ⚠ THIS IS FUNCTIONALLY AN ANTI-FRONTING RULE, though not phrased that way: A "
                "CLUB CANNOT SIMPLY RESERVE SPACE AND HAND IT TO DGD, because the PARTNERSHIP WITH AN "
                "UNREGISTERED ENTITY is separately gated on Director approval. (d) ⚠ BUILD IN SIX WEEKS OF LEAD "
                "TIME, NOT TEN BUSINESS DAYS — THE ADVANCEMENT APPROVAL, NOT THE ROOM BOOKING, IS THE BINDING "
                "CONSTRAINT. (e) NO LANGUAGE FOUND REACHING PAYMENT CREDENTIALS OR ON-SITE CONTRACT SIGNING — not "
                "addressed in a 2022 document. (f) INSURANCE REQUIREMENTS, RENTAL RATES, DEPOSITS AND "
                "CANCELLATION TERMS: NOT FOUND — not in the handbook, not in the policy index. Ask Facilities, "
                "(808) 735-4869. (g) ⚠ CAVEAT ON THE WHOLE DOCUMENT: IT IS DATED OCTOBER 2022. The office has "
                "since been RENAMED from 'Office of Student Activities and Leadership' to 'OFFICE OF STUDENT "
                "ENGAGEMENT' and THE DIRECTOR HAS CHANGED. VERIFY THE HANDBOOK IS STILL CURRENT WHEN YOU CALL, "
                "(808) 739-8556. ◆ WHAT DOES *NOT* APPLY HERE: Chaminade is PRIVATE AND CATHOLIC (MARIANIST). NO "
                "public-forum doctrine, NO state campus free-speech statute reach, NO First Amendment claim. The "
                "UH systemwide interim Time, Place and Manner policy (replaced effective 1 JULY 2026, still being "
                "rewritten through fall 2026, full text never retrieved) and HAR Title 20 Ch. 13 BIND UH AND DO "
                "NOT BIND CHAMINADE. DO NOT REASON FROM PUBLIC-UNIVERSITY NORMS HERE — it will read as not having "
                "done the homework. ⚠ ALSO NOTE: the Campus Community Policies index contains NO solicitation, "
                "vendor, facility-use, posting or freedom-of-expression policy at all — it covers parking, golf "
                "carts, alcohol/drugs/smoking, hazardous materials, surveillance, acceptable technology use, van "
                "drivers, business office procedures, grants and SSN protection "
                "(chaminade.edu/compliance-office/campus-community-policies/). The rules live in the clubs "
                "handbook PDF, which is exactly where they usually hide. ⚠⚠ STATE REGULATORY: Hawaii's money-"
                "transmission and digital-currency position is recorded in full in the UH MĀNOA policy_key and "
                "applies statewide, private campuses included. Short version: NO Hawaii money transmitter license "
                "is currently required for pure digital-asset activity following the sunset of the Digital "
                "Currency Innovation Lab on 30 June 2024 (DFI FAQ, 9 Feb 2024), BUT ANY US-DOLLAR ACTIVITY "
                "MEETING THE DEFINITION OF MONEY TRANSMISSION 'WILL LIKELY REQUIRE A MONEY TRANSMITTER LICENSE.' "
                "A 2026 re-regulation bill (SB 2757 SD1) passed the Senate and died in House committee and will "
                "likely return in 2027. Confirm with the Hawaii Division of Financial Institutions, "
                "https://cca.hawaii.gov/dfi/ .",
  'sponsor_required': '⚠⚠ YES — AND SPONSORSHIP IS NOT ENOUGH ON ITS OWN. "Only registered Student '
                      'Clubs/Organizations, University Departments, or agencies may host unaffiliated speakers or '
                      'acts on campus," AND groups cannot partner with unregistered entities without the '
                      'DIRECTOR\'S WRITTEN APPROVAL, AND any corporate sponsorship needs DIRECTOR + VP OF '
                      'ADVANCEMENT clearance BEFORE SOLICITATION, AND the whole thing sits under a "values '
                      'counter to those of the University" veto with no appeal. ⚠ AND THERE IS NO CLUB TO '
                      'SPONSOR YOU ANYWAY: ZERO of the ten recognized organizations is business, finance, CS or '
                      'entrepreneurship. THE ONLY VIABLE ROUTE IS FACULTY OR THE HOGAN PROGRAM — pitch a TALK in '
                      'an existing lecture series, which does not trip the corporate-sponsorship clause at all.',
  'clubs': [('⚠⚠ TEN RECOGNIZED STUDENT ORGANIZATIONS CAMPUS-WIDE, AND ZERO ARE RELEVANT — THIS IS A VERIFIED '
             'ABSENCE, NOT A DIRECTORY LIMITATION',
             'The full recognized list for 2025–26 is published and it is TEN ITEMS LONG: 1. Chaminade Drama Club; '
             '2. Chaminade Student Nurses\' Association; 3. Ka Ipu Kukui Me Ka ʻieʻie (Hawaiian) Club; 4. Lumanaʻi '
             'O Samoa; 5. Pride Alliance for Queers (PAQ); 6. Psi Chi, International Honor Society in Psychology; '
             '7. Student Athlete Advisory Committee (SAAC); 8. Taotao Marianas Club; 9. The Filipino Club (TFC); '
             '10. United Nations Association of Chaminade University (UNAC). ⚠ NO BUSINESS, FINANCE, ECONOMICS, '
             'INVESTMENT, ENTREPRENEURSHIP, COMPUTER SCIENCE, DATA SCIENCE, FINTECH OR BLOCKCHAIN ORGANIZATION. '
             'NO FINANCIAL MANAGEMENT ASSOCIATION CHAPTER. ⚠ IMPLICATION: THERE IS NO STUDENT-ORGANIZATION '
             'SPONSOR AVAILABLE AT CHAMINADE FOR A CRYPTO/FINTECH PITCH — the only route is faculty or Hogan.',
             'https://chaminade.edu/student-engagement/student-organizations/'),
            ('Governing bodies — CSGA, CSAB, CSPB, HOR',
             'Confirmed in the clubs handbook as separate governing bodies. CSGA (Chaminade Student Government '
             'Association) is the one with a published number, (808) 739-8378, and is the only student-side body '
             'that could plausibly sponsor anything at this campus.',
             'https://chaminade.edu/student-engagement/csga/'),
            ('⚠ Directory is public but emails are Cloudflare-obfuscated — CALL, DO NOT EMAIL',
             'The student-organizations directory is PUBLICLY ACCESSIBLE AND NOT LOGIN-GATED, which is unusually '
             'good — but individual org emails are rendered through Cloudflare protection and CANNOT BE SCRAPED. '
             'The org-management platform is SILVER SOURCE; deeper org detail there may require authentication. '
             'Use the phone.',
             'https://chaminade.edu/student-engagement/student-organizations/')],
  'faculty': [('⚠⚠ Guanlin Gao, Ph.D.',
               'DIRECTOR, ECONOMIC EDUCATION CENTER; ASSOCIATE PROFESSOR OF ECONOMICS. ⚠ OF EVERY NAMED '
               'INDIVIDUAL ACROSS ALL FOUR HAWAII CAMPUSES, THIS IS THE MOST NATURAL COUNTERPART FOR A MONETARY / '
               'DIGITAL-CURRENCY CONVERSATION — and directing an outreach centre means she has a STANDING REASON '
               'TO HOST SPEAKERS. ⚠ NOT confirmed to research blockchain or cryptocurrency; listed by field and '
               'role.',
               'School of Business and Communication — Economics',
               'guanlin.gao@chaminade.edu · (808) 739-4609',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('⚠⚠ Roy Panzarella',
               'DIRECTOR, HOGAN ENTREPRENEURIAL LEADERSHIP PROGRAM — AND THE HOGAN PROGRAM RUNS A BI-WEEKLY '
               'LECTURE SERIES FEATURING OUTSIDE SPEAKERS. THAT IS A STANDING SLOT THAT ALREADY EXISTS AND '
               'ALREADY IMPORTS OUTSIDE SPEAKERS — the single best access route at Chaminade and possibly the '
               'best faculty-side route in the state. ⚠ PITCH IT AS A TALK, NOT A SPONSORSHIP: a speaking slot '
               'does not trip the corporate-sponsorship clause and its approval chain is far shorter. Kieffer '
               'Hall, Room 12.',
               'Hogan Entrepreneurial Leadership Program',
               'roy.panzarella@chaminade.edu · hogan@chaminade.edu · (808) 440-4280',
               'https://chaminade.edu/hogan/'),
              ('⚠ Office of Student Engagement (formerly OSAL) — Director Andrew Peter Ancheta II',
               'THE OFFICE THAT GRANTS PERMISSION. Runs organization registration, policies, facility '
               'reservations, bulletin boards and the Silver Source platform. ⚠ ANDREW PETER ANCHETA II IS THE '
               '"DIRECTOR" WHOSE **WRITTEN** APPROVAL THE HANDBOOK REQUIRES to partner with an unregistered '
               'entity — no direct line is published, reach him on the office number. ⚠ ALSO ASK FOR THE '
               'ASSISTANT DIRECTOR: that role handles FACILITY RESERVATIONS AND BULLETIN-BOARD POSTINGS and IS '
               'NOT NAMED on the web page. Programming Specialist and Marketing Specialist posts were listed as '
               'OPEN. The office email is JavaScript/Cloudflare-obfuscated — USE THE PHONE. Clarence T.C. Ching '
               'Hall Room 106; Mon–Thu 8:00–20:00, Fri 8:00–17:00.',
               'Office of Student Engagement',
               'OSAL@chaminade.edu · (808) 739-8556',
               'https://chaminade.edu/student-engagement/visit-our-office/'),
              ('Facilities',
               'Space and setup requests — and the office to ask for INSURANCE REQUIREMENTS AND RENTAL RATES, '
               'which are published nowhere. ⚠ $200 LATE FEE for a facilities request under 10 business days\' '
               'notice. (Number from the OCTOBER 2022 handbook PDF — spot-check it on the call.)',
               'Facilities',
               '(808) 735-4869',
               'https://assets.chaminade.edu/wp-content/uploads/2022/10/04094553/Handbook-for-Student-Clubs-Organizations-Chaminade-Office-of-Student-Activities-and-Leadership.pdf'),
              ('Registrar / Classrooms',
               'Classroom bookings specifically, as distinct from Facilities. (Number from the October 2022 '
               'handbook PDF — spot-check.)',
               'Registrar',
               '(808) 735-4722',
               'https://catalog.chaminade.edu/'),
              ('CSGA — Chaminade Student Government Association',
               'Student government, and the only student-side body at Chaminade with a published number. With '
               'zero business or finance clubs on campus, this is the only plausible student sponsor. (Number '
               'from the October 2022 handbook PDF — spot-check.)',
               'Chaminade Student Government Association',
               'CSGA@chaminade.edu · (808) 739-8378',
               'https://chaminade.edu/student-engagement/csga/'),
              ('School of Business and Communication',
               'Departmental line — the front door to the business faculty below. Kieffer Hall, Room 12.',
               'School of Business and Communication',
               '(808) 739-8369',
               'https://chaminade.edu/business/'),
              ('Caryn Callahan, Ph.D.',
               'PROFESSOR, FINANCE & INTERNATIONAL BUSINESS — the finance faculty of record at Chaminade and the '
               'third-best academic target here. ⚠ NOT confirmed to research blockchain or cryptocurrency.',
               'School of Business and Communication — Finance',
               'caryn.callahan@chaminade.edu · (808) 739-4615',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('Maria Brownlow, Ph.D.',
               'ASSOCIATE PROFESSOR, COMPUTER INFORMATION SYSTEMS — the technical door on a campus with no CS '
               'club and no CS organization. ⚠ NOT confirmed to research blockchain or cryptocurrency.',
               'School of Business and Communication — CIS',
               'maria.brownlow@chaminade.edu · (808) 739-8337',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('Annette Taijeron Santos, D.B.A.',
               'INTERIM DEAN, School of Business and Communication — school-level approval and the escalation '
               'point above any individual faculty member.',
               'School of Business and Communication',
               'annette.santos@chaminade.edu · (808) 739-4611',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('Ann Lujan Kishi',
               'ASSOCIATE DIRECTOR, HOGAN PROGRAM — Hogan scheduling. The practical follow-up once Panzarella '
               'says yes to a lecture-series slot.',
               'Hogan Entrepreneurial Leadership Program',
               'ann.kishi@chaminade.edu · (808) 739-4673',
               'https://chaminade.edu/hogan/'),
              ('Masahisa Yamaguchi, Ph.D.',
               'INTERIM MBA DIRECTOR; Assistant Professor, Strategic Management — the graduate audience, and a '
               'program director who can place a speaker without a facilities process.',
               'School of Business and Communication — MBA',
               'masahisa.yamaguchi@chaminade.edu · (808) 739-4602',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('Richard Kido, M.B.A.',
               'Associate Professor, Accounting.',
               'School of Business and Communication — Accounting',
               'richard.kido@chaminade.edu · (808) 440-4245',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('Aaron Williamson, Jr., CPA',
               'Professor; Accounting Coordinator.',
               'School of Business and Communication — Accounting',
               'aaron.williamson@chaminade.edu · (808) 739-8592',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('Pamela Estell, Ph.D.',
               'Assistant Professor; Curriculum Chair, Management — the curriculum chair, i.e. the person who '
               'knows which courses actually run in Fall 2026.',
               'School of Business and Communication — Management',
               'pamela.estell@chaminade.edu · (808) 440-4225',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('Wendy Lam, Ph.D.',
               'Associate Professor; Sport & Event Management coordinator.',
               'School of Business and Communication — Sport & Event Management',
               'wendy.lam@chaminade.edu · (808) 739-4606',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('Wera Panow-Loui, M.B.A.',
               'Senior Lecturer, Marketing.',
               'School of Business and Communication — Marketing',
               'wera.loui@chaminade.edu · (808) 739-4608',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('Scott Schroeder, Ph.D.',
               'Professor in Residence, Management. ⚠ NOTE THE NUMBER IS AN OFF-CAMPUS OFFICE WITH AN EXTENSION, '
               'not a campus extension — dial it as listed.',
               'School of Business and Communication — Management',
               'scott.schroeder@chaminade.edu · (808) 734-5058 x226',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('George S. Vozikis, Ph.D.',
               'Professor in Residence, Management. ⚠ NOTE THE NUMBER IS AN OFF-CAMPUS OFFICE (808-946-xxxx), not '
               'a Chaminade campus extension.',
               'School of Business and Communication — Management',
               'george.vozikis@chaminade.edu · (808) 946-3366',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('Brian Fila, MA, MS',
               'Adjunct Senior Lecturer, Leadership. ⚠ OUT-OF-STATE NUMBER — (650) is the San Francisco '
               'Peninsula, not Hawaii. Dial accordingly and mind the time difference.',
               'School of Business and Communication — Leadership',
               'brian.fila@chaminade.edu · (650) 503-3452',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('Residence Life',
               'Carried across for completeness. (Number from the October 2022 handbook PDF — spot-check.)',
               'Residence Life',
               '(808) 739-4868',
               'https://assets.chaminade.edu/wp-content/uploads/2022/10/04094553/Handbook-for-Student-Clubs-Organizations-Chaminade-Office-of-Student-Activities-and-Leadership.pdf'),
              ('Dining Services',
               'Catering, if food is ever promised at an event. (Number from the October 2022 handbook PDF — '
               'spot-check.)',
               'Dining Services',
               '(808) 739-4621',
               'https://assets.chaminade.edu/wp-content/uploads/2022/10/04094553/Handbook-for-Student-Clubs-Organizations-Chaminade-Office-of-Student-Activities-and-Leadership.pdf')],
  'courses': [('⚠ NO BLOCKCHAIN / CRYPTO / DIGITAL-ASSET / FINTECH COURSE CONFIRMED',
               'The School of Business and Communication is IACBE-ACCREDITED, but the business faculty page does '
               'not enumerate courses and the catalog course listings were not retrievable within budget. '
               'UNCLOSED GAP, NOT A VERIFIED ABSENCE. Check https://catalog.chaminade.edu/ .',
               'https://catalog.chaminade.edu/'),
              ('⚠ Economic Education Center',
               'THE RELEVANT ACADEMIC INFRASTRUCTURE THAT DOES EXIST — directed by GUANLIN GAO, (808) 739-4609. '
               'An outreach centre with a standing reason to host speakers is a better venue than any classroom '
               'at this campus.',
               'https://chaminade.edu/business-and-communication/business-faculty/'),
              ('MBA program',
               'Interim director Masahisa Yamaguchi, (808) 739-4602. The graduate audience at Chaminade and a '
               'lighter ask than any facilities booking.',
               'https://chaminade.edu/business/')],
  'events': [('⚠⚠ Hogan Entrepreneurial Leadership Program — BI-WEEKLY LECTURE SERIES FEATURING OUTSIDE SPEAKERS',
              'THE BEST ACCESS ROUTE AT CHAMINADE AND POSSIBLY THE BEST FACULTY-SIDE ROUTE IN THE STATE. A one- '
              'or two-year certificate program open to full-time Chaminade students ACROSS ALL MAJORS — so it '
              'reaches beyond the (nonexistent) business-club population. Students "learn first-hand from '
              'experienced Hawaiʻi business leaders and entrepreneurs about the business of getting a new idea up '
              'and running." Components: a BI-WEEKLY LECTURE SERIES FEATURING OUTSIDE SPEAKERS (← this is the '
              'ask, a standing slot that already imports outside speakers); mentorships and internships; a 2026 '
              'NONPROFIT BUSINESS PLAN COMPETITION; international study trips; community service. ⚠ FALL 2026 '
              'PROGRAMMING DATES ARE NOT PUBLISHED — call (808) 440-4280 or email hogan@chaminade.edu. ⚠⚠ '
              'CAUTION: HOGAN IS PHILANTHROPICALLY FUNDED (the California-based Hogan Family Foundation) AND THE '
              'SPONSORSHIP APPROVAL CHAIN RUNS THROUGH THE VP OF ADVANCEMENT. A SPEAKING SLOT IN AN EXISTING '
              'LECTURE SERIES IS A MUCH LIGHTER ASK THAN SPONSORSHIP AND DOES NOT TRIP THE CORPORATE-SPONSORSHIP '
              'CLAUSE. PITCH IT AS A TALK, NOT A SPONSORSHIP.',
              'https://chaminade.edu/hogan/'),
             ('⚠ October accelerated session — a modest second entry point',
              'Chaminade runs FOUR ACCELERATED SESSIONS beginning in January, April, July and OCTOBER alongside '
              'the 16-week semester. The October session brings a second cohort mid-term — but it MOSTLY SERVES '
              'ADULT AND WORKING STUDENTS rather than traditional undergraduates, so do not overrate it. Exact '
              'start date not published.',
              'https://catalog.chaminade.edu/academiccalendar/accelerated'),
             ('No career fair, hackathon or blockchain conference — NONE FOUND',
              'Nothing of the kind is published for Fall 2026 at Chaminade, and no club fair either. With ten '
              'recognized student organizations campus-wide, expect little. Call (808) 739-8556.',
              'https://chaminade.edu/student-engagement/')],
  'play': 'Go for the Hogan lecture series and nothing else — and go early, because Chaminade\'s term ends first. '
          'This is the BEST-DOCUMENTED campus in the state for phone numbers and THE WORST FOR AUDIENCE FIT: '
          '~1,000 undergraduates in Kaimukī, fifteen minutes from downtown Honolulu, with TEN recognized student '
          'organizations campus-wide of which ZERO are business, finance, economics, investment, entrepreneurship, '
          'computer science, data science or blockchain. THAT IS A PUBLISHED, VERIFIED LIST, NOT A DIRECTORY '
          'LIMITATION — so THERE IS NO CLUB TO SPONSOR YOU HERE, and the club route simply does not exist. ⚠⚠ AND '
          'THE WRITTEN REGIME IS THE MOST RESTRICTIVE OF THE FOUR: only registered clubs, departments or agencies '
          'may host unaffiliated speakers; partnering with an unregistered entity needs the DIRECTOR\'S WRITTEN '
          'APPROVAL; ALL corporate sponsorship needs DIRECTOR + VP OF ADVANCEMENT clearance BEFORE YOU EVEN '
          'SOLICIT; and it all sits under a "values counter to those of the University" veto at a Catholic '
          'institution with NO APPEAL AND NO NEUTRALITY REQUIREMENT. Assume that veto gets invoked if anyone '
          'objects. ⚠ THE ONE GENUINE OPENING IS ROY PANZARELLA, (808) 440-4280, DIRECTOR OF THE HOGAN '
          'ENTREPRENEURIAL LEADERSHIP PROGRAM, WHICH RUNS A BI-WEEKLY LECTURE SERIES THAT ALREADY IMPORTS OUTSIDE '
          'SPEAKERS AND IS OPEN TO STUDENTS ACROSS ALL MAJORS. PITCH A TALK, NOT A SPONSORSHIP — a speaking slot '
          'does not trip the corporate-sponsorship clause and its approval chain is far shorter. SECOND CALL: '
          'GUANLIN GAO, (808) 739-4609, DIRECTOR OF THE ECONOMIC EDUCATION CENTER AND AN ECONOMIST — of every '
          'named individual across all four Hawaii campuses, the most natural counterpart for a monetary and '
          'digital-currency conversation, and someone whose job includes hosting speakers. ⚠⚠ TIMING IS '
          'UNFORGIVING HERE: CHAMINADE STARTS MON AUG 17 (EARLIEST IN THE STATE) AND ITS TERM ENDS FRI DEC 4 '
          '(EARLIEST IN THE STATE), so the actionable window CLOSES ROUGHLY TWO WEEKS BEFORE EVERYONE ELSE\'S — '
          'anything here must land before late November. Combine that with SIX WEEKS OF ADVANCEMENT LEAD TIME if '
          'money is ever involved and the real deadline is late September. Note also Chaminade closes for '
          'INDIGENOUS PEOPLE\'S DAY OCT 12 (UH does not) and does NOT close for ELECTION DAY NOV 3 (UH does). ⚠ '
          'AND VERIFY THE RULEBOOK: the governing clubs handbook is dated OCTOBER 2022, the office has been '
          'renamed and the Director has changed — confirm it is still current at (808) 739-8556.',
  'gaps': ['⚠⚠ IS THE OCTOBER 2022 CLUBS HANDBOOK STILL CURRENT? It is the governing document for everything in '
           'this record, and since it was written the office has been RENAMED (Office of Student Activities and '
           'Leadership → Office of Student Engagement) and THE DIRECTOR HAS CHANGED. Also get the ASSISTANT '
           'DIRECTOR\'S NAME — that role handles facility reservations and bulletin-board postings and is NOT '
           'named on the web page. Call (808) 739-8556.',
           '⚠⚠ INSURANCE REQUIREMENTS, FACILITY RENTAL RATES, DEPOSITS AND CANCELLATION TERMS — NOT FOUND '
           'ANYWHERE: not in the handbook, not in the Campus Community Policies index. The only published figure '
           'is the $200 LATE FEE for a facilities request under 10 business days. Call Facilities, '
           '(808) 735-4869.',
           '⚠ HOGAN PROGRAM FALL 2026 LECTURE-SERIES DATES — not published. This is the single best access route '
           'at Chaminade and its schedule is unknown. Call (808) 440-4280 or email hogan@chaminade.edu.',
           '⚠ NO FALL 2026 CLUB FAIR OR INVOLVEMENT FAIR IS PUBLISHED, and with ten recognized organizations it '
           'may be a very small affair or may not exist. https://chaminade.edu/student-engagement/',
           'CHAMINADE COURSE LISTINGS — the catalog course descriptions were not retrievable within budget, so '
           'the "no blockchain/fintech course" call is an UNCLOSED GAP rather than a verified absence. '
           'https://catalog.chaminade.edu/',
           'THE EXACT OCTOBER ACCELERATED-SESSION START DATE — the catalog confirms four accelerated sessions '
           'begin in January, April, July and October, but not the day. '
           'https://catalog.chaminade.edu/academiccalendar/accelerated',
           'ADMINISTRATIVE NUMBERS SOURCED FROM THE OCTOBER 2022 HANDBOOK PDF (Facilities 735-4869, Registrar '
           '735-4722, CSGA 739-8378, Residence Life 739-4868, Dining 739-4621) SHOULD BE SPOT-CHECKED on the '
           'call. Faculty numbers come from the CURRENT live directory and are more reliable. '
           'https://chaminade.edu/business-and-communication/business-faculty/',
           'ORG EMAILS ARE CLOUDFLARE-OBFUSCATED on both the student-organizations page and the Office of Student '
           'Engagement page, and the org platform (Silver Source) may require authentication. There is no way to '
           'email a club directly without a browser — USE THE PHONE. '
           'https://chaminade.edu/student-engagement/student-organizations/'],
  'note': '⚠ CHAMINADE IS PRIVATE AND CATHOLIC (MARIANIST) and is bound by NONE of the UH policy layer — not the '
          'systemwide interim Time, Place and Manner policy, not HAR Title 20 Ch. 13, not public-forum doctrine. '
          'Citing any of them here will read as not having done the homework. ⚠ It is 15–20 minutes from downtown '
          'Honolulu (HPU at Aloha Tower) and from Mānoa, so all three Oʻahu campuses share one trip — but '
          'Chaminade\'s calendar runs two weeks ahead of the others at both ends, so it should be worked FIRST on '
          'any sequenced visit.'},
]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; those sort last and never show a countdown.
DEADLINES = [

 ('2026-08-17', 'Aug 17, 2026', 'Chaminade',
  '⚠ CLASSES BEGIN — THE EARLIEST START IN THE STATE',
  'A week before both UH campuses and TWO WEEKS before HPU, and unusually early nationally. Add/drop runs Aug '
  '17–25. ⚠ Pair this with the other end of the term: Chaminade\'s last day of classes is FRI DEC 4, so its whole '
  'usable window is Aug 17 – late Nov, about two weeks ahead of everyone else at both ends. On any sequenced '
  'Oʻahu trip, Chaminade goes FIRST.',
  'https://catalog.chaminade.edu/academiccalendar/semester',
  'Office of Student Engagement (808) 739-8556'),

 ('2026-08-21', 'Aug 21, 2026', 'UH Mānoa / UH Hilo',
  'Statehood Day — state holiday, UH campuses closed',
  'A Hawaii-only closure mainland planners miss (third Friday in August). Harmless this year at UH because it '
  'precedes the Aug 24 term start — but note Chaminade is already in its first week.',
  'https://manoa.hawaii.edu/registrar/academic-calendar/fall-2026/',
  'UH Mānoa SLD (808) 956-8178'),

 ('2026-08-24', 'Aug 24, 2026', 'UH Mānoa',
  'CLASSES BEGIN — confirmed on the Fall 2026 registrar page',
  'Add/drop without a W runs to Sep 15. NO FALL BREAK all term, so an uninterrupted run to Thanksgiving. Last day '
  'of instruction Dec 10, study period Dec 11–12, finals Dec 14–18, commencement Dec 19. ⚠ The Involvement Fair '
  'is held "early in the fall semester" but NO FALL 2026 DATE IS PUBLISHED — call SLD now, not in September.',
  'https://manoa.hawaii.edu/registrar/academic-calendar/fall-2026/',
  'Student Life & Development · sld@hawaii.edu · (808) 956-8178'),

 ('2026-08-24', 'Aug 24, 2026', 'UH Hilo',
  'CLASSES BEGIN — same date as Mānoa (same system, same term structure)',
  '⚠ But the deadlines are tighter: last day to ADD is Sep 1, two weeks ahead of Mānoa\'s Sep 15, so Hilo '
  'schedules lock earlier. ⚠⚠ AND REMEMBER HILO IS A FLIGHT, NOT A DRIVE — ~200 miles across open ocean, '
  'interisland only. Sponsoring HAIC reaches these students without the airfare.',
  'https://hilo.hawaii.edu/registrar/Fall2026SemesterAcademicCalendar.php',
  'No UH Hilo number confirmed — build the list; Hilo uses 808-932-xxxx / 808-974-xxxx'),

 ('2026-08-25', 'Aug 25, 2026', 'Chaminade',
  'Add/drop period ends',
  'Chaminade schedules are locked from today — the earliest lock-in of any campus in the state.',
  'https://catalog.chaminade.edu/academiccalendar/semester',
  'Office of Student Engagement (808) 739-8556'),

 ('2026-08-31', 'Aug 31, 2026', 'Hawaiʻi Pacific',
  '⚠ TERM BEGINS (16-week) — THE LATEST START IN THE STATE',
  'A full week after both UH campuses and TWO WEEKS after Chaminade, so HPU must come LAST in any sequenced trip. '
  '⚠ NOT CONVENTIONAL SEMESTERS: HPU runs concurrent 8-week accelerated sessions (8A/8B) inside the 16-week term, '
  'and the 8B session starting around LATE OCTOBER brings a SECOND COHORT OF NEWLY-ENROLLED STUDENTS mid-term — '
  'the only such second window on Oʻahu besides Chaminade\'s October accelerated session.',
  'https://www.hpu.edu/registrar/academic-calendar.html',
  'Student Activities · studentlife@hpu.edu · (808) 544-0277'),

 ('2026-09-01', 'Sep 1, 2026', 'UH Hilo',
  'Last day to ADD — two weeks tighter than Mānoa',
  'Hilo schedules lock on Sep 1; Mānoa\'s erase deadline is not until Sep 15. The "students still shopping" '
  'window is correspondingly shorter here. Last day to drop with a W is Nov 2.',
  'https://hilo.hawaii.edu/registrar/Fall2026SemesterAcademicCalendar.php',
  'No UH Hilo number confirmed — see gaps'),

 ('2026-09-07', 'Sep 7, 2026', 'All Hawaii campuses',
  'Labor Day — holiday at all four campuses',
  'The one closure every campus in this file shares.',
  'https://manoa.hawaii.edu/registrar/academic-calendar/fall-2026/',
  'UH Mānoa SLD (808) 956-8178 · HPU (808) 544-0277 · Chaminade (808) 739-8556'),

 ('2026-09-08', 'Sep 8, 2026', 'Hawaiʻi Pacific',
  'Last day to register; 100% tuition refund deadline',
  'Then 50% refund Sep 15 and 25% refund Sep 28. HPU\'s enrolment is still moving well into September.',
  'https://www.hpu.edu/registrar/academic-calendar.html',
  'HPU Registrar · main line (808) 544-0200'),

 ('2026-09-15', 'Sep 15, 2026', 'UH Mānoa',
  'Last day to add/drop without a W — 11:59 p.m. HST',
  'Mānoa schedules stay fluid three full weeks into the term, two weeks longer than Hilo. The best window for '
  'reaching students while course loads are still being decided closes today.',
  'https://manoa.hawaii.edu/registrar/academic-calendar/fall-2026/',
  'Student Life & Development (808) 956-8178'),

 ('2026-09-15', 'Sep 15, 2026', 'Hawaiʻi Pacific',
  '⚠ RSO ROSTER FINALIZED — "by September 15, once all registrations are complete" (also the 50% refund deadline)',
  '⚠ THIS IS THE DATE THAT MATTERS AT HPU. The full club roster is NOT PUBLISHED until now, so any club-sponsor '
  'conversation before today is aimed at organizations that may not yet be re-registered. CALL AFTER TODAY and '
  'ask specifically for business, finance, economics, analytics and CS clubs by name — none is currently named on '
  'any public HPU page, but the roster is UNPUBLISHED, NOT EMPTY. (The quoted language referenced 2025–26 and may '
  'itself be stale — confirm.)',
  'https://www.hpu.edu/student-engagement/clubs/index.html',
  'leadership@hpu.edu · Student Activities (808) 544-0277'),

 ('2026-09-28', 'Sep 28, 2026', 'Hawaiʻi Pacific',
  '25% tuition refund deadline',
  'Last of HPU\'s three refund tiers (100% Sep 8, 50% Sep 15, 25% Sep 28).',
  'https://www.hpu.edu/registrar/academic-calendar.html',
  'HPU main line (808) 544-0200'),

 ('2026-10-12', 'Oct 12, 2026', 'Chaminade',
  'Indigenous People\'s Day — Chaminade closed; ⚠ UH DOES NOT OBSERVE IT',
  'The two systems close on different days. Chaminade closes today and UH does not; three weeks later UH closes '
  'for Election Day and Chaminade does not. Check both calendars before booking anything on Oʻahu in this '
  'stretch.',
  'https://catalog.chaminade.edu/academiccalendar/semester',
  'Office of Student Engagement (808) 739-8556'),

 ('2026-10-19', 'Oct 19, 2026', 'Statewide — HAIC',
  'Hawaii Annual Innovation Challenge — challenges announced',
  'Opening of the HAIC cycle. State Office of Enterprise Technology Services IN PARTNERSHIP WITH THE UNIVERSITY '
  'OF HAWAIʻI; participants are university students statewide, so it reaches UH Mānoa AND UH Hilo without a '
  'second flight.',
  'https://haic.hawaii.gov/',
  'No phone published; contact email obfuscated — use the site form or HAIC Network Slack'),

 ('2026-10-24', 'Oct 24, 2026', 'Statewide — HAIC',
  'HAIC virtual kickoff',
  'Three days before the registration deadline. Virtual interim workshops follow on Oct 31 and Nov 14.',
  'https://haic.hawaii.gov/',
  'No phone published — site contact form or HAIC Network Slack'),

 ('2026-10-27', 'Oct 27, 2026', 'Statewide — HAIC',
  '⚠⚠ HAIC REGISTRATION DEADLINE — THE ONE HARD DATE ON THE BEST CHANNEL IN THE STATE',
  'THE BEST OPPORTUNITY IN HAWAII IS NOT A CAMPUS. HAIC publishes an OPEN, PRICED SPONSORSHIP RATE CARD: '
  'PETABYTE $7,000+, TERABYTE $5,000–6,999, GIGABYTE $2,500–4,999, MEGABYTE $500–2,499. Funds are received and '
  'handled by the IMAG FOUNDATION, A 501(c)(3) — "making all contributions 100% tax deductible." ⚠ WHY IT RANKS '
  'FIRST: it is an open published pipeline into a UH-PARTNERED student event administered by a private foundation '
  'rather than a university procurement office, it reaches UH Mānoa AND UH Hilo students at an entry price of '
  '$500, and IT SIDESTEPS EVERY CAMPUS SOLICITATION RULE IN THIS PACKET. ⚠ NO PHONE IS PUBLISHED AND THE CONTACT '
  'EMAIL IS OBFUSCATED on both the main and sponsors pages — pursue via the site contact form or the HAIC Network '
  'Slack workspace, and START THE CONVERSATION BY LATE SEPTEMBER.',
  'https://haic.hawaii.gov/sponsors/',
  'No phone published — site contact form or HAIC Network Slack'),

 ('2026-10-31', 'Oct 31, 2026', 'Statewide — HAIC',
  'HAIC virtual interim workshop',
  'First of two published interim workshops (the second is Nov 14). Sponsor visibility, if any, would attach '
  'here.',
  'https://haic.hawaii.gov/',
  'No phone published — site contact form or HAIC Network Slack'),

 ('2026-11-02', 'Nov 2, 2026', 'UH Hilo',
  'Last day to drop with a W',
  'Confirmed on the UH Hilo Fall 2026 registrar page.',
  'https://hilo.hawaii.edu/registrar/Fall2026SemesterAcademicCalendar.php',
  'No UH Hilo number confirmed — see gaps'),

 ('2026-11-03', 'Nov 3, 2026', 'UH Mānoa / UH Hilo',
  '⚠ ELECTION DAY — HAWAII STATE HOLIDAY, BOTH UH CAMPUSES CLOSED (Chaminade is NOT)',
  'A general-election day AND a state holiday in Hawaii, so UH campuses close — a closure mainland planners '
  'routinely miss. ⚠ CHAMINADE DOES NOT CLOSE FOR IT, and HPU\'s closure was not confirmed either way. Note UH '
  'offices including Student Life & Development are closed on state holidays, so do not plan a call for today.',
  'https://manoa.hawaii.edu/registrar/academic-calendar/fall-2026/',
  'UH Mānoa SLD (808) 956-8178 (closed today)'),

 ('2026-11-11', 'Nov 11, 2026', 'UH Mānoa / UH Hilo',
  'Veterans Day — UH campuses closed',
  'Second November closure at both UH campuses.',
  'https://manoa.hawaii.edu/registrar/academic-calendar/fall-2026/',
  'UH Mānoa SLD (808) 956-8178'),

 ('2026-11-14', 'Nov 14, 2026', 'Statewide — HAIC',
  'HAIC virtual interim workshop (second)',
  'Final published HAIC touchpoint of the fall.',
  'https://haic.hawaii.gov/',
  'No phone published — site contact form or HAIC Network Slack'),

 ('2026-11-26', 'Nov 26–27, 2026', 'All Hawaii campuses',
  'Thanksgiving — no classes at any campus',
  'UH Mānoa and UH Hilo: Thanksgiving Nov 26 plus an observance / non-instructional day Nov 27. Chaminade: Nov '
  '26–27, offices closed. ⚠ NO CAMPUS IN THIS SET HAS A FALL BREAK, so the run from Labor Day to Thanksgiving is '
  'uninterrupted — but after this week Chaminade has only one teaching week left.',
  'https://manoa.hawaii.edu/registrar/academic-calendar/fall-2026/',
  'UH Mānoa SLD (808) 956-8178 · Chaminade (808) 739-8556'),

 ('2026-12-04', 'Dec 4, 2026', 'Chaminade',
  '⚠ LAST DAY OF CLASSES — THE EARLIEST TERM END IN THE STATE',
  'Mānoa and Hilo are still teaching until Dec 10 and examining until Dec 18; HPU runs to Dec 20. THE ACTIONABLE '
  'CHAMINADE WINDOW CLOSED ROUGHLY TWO WEEKS AGO — anything here had to be scheduled before late November, and '
  'with six weeks of Advancement lead time for anything involving money, the real planning deadline was late '
  'September.',
  'https://catalog.chaminade.edu/academiccalendar/semester',
  'Office of Student Engagement (808) 739-8556'),

 ('2026-12-07', 'Dec 7–10, 2026', 'Chaminade',
  'Finals — Chaminade is finished before UH begins examining',
  'Chaminade closes out its term a full week before Mānoa and Hilo start finals on Dec 14.',
  'https://catalog.chaminade.edu/academiccalendar/semester',
  'Office of Student Engagement (808) 739-8556'),

 ('2026-12-10', 'Dec 10, 2026', 'UH Mānoa / UH Hilo',
  'Last day of instruction at both UH campuses',
  'Mānoa study period Dec 11–12. Nothing worth doing on a UH campus after about Nov 25.',
  'https://manoa.hawaii.edu/registrar/academic-calendar/fall-2026/',
  'UH Mānoa SLD (808) 956-8178'),

 ('2026-12-14', 'Dec 14–18, 2026', 'UH Mānoa / UH Hilo',
  'Finals at both UH campuses',
  'Semester ends and degrees confer Fri Dec 18; commencement Sat Dec 19 at both. HPU is examining across the same '
  'week but runs through Sunday Dec 20.',
  'https://manoa.hawaii.edu/registrar/academic-calendar/fall-2026/',
  'UH Mānoa SLD (808) 956-8178'),

 ('2026-12-14', 'Dec 14–20, 2026', 'Hawaiʻi Pacific',
  '⚠ Finals — running THROUGH A SUNDAY',
  'Unusual and as published. Verify with the Registrar if it matters.',
  'https://www.hpu.edu/registrar/academic-calendar.html',
  'HPU main line (808) 544-0200'),

 ('2026-12-18', 'Dec 18, 2026', 'UH Mānoa / UH Hilo',
  'Semester ends / degree conferral at both UH campuses',
  'Commencement follows Sat Dec 19.',
  'https://manoa.hawaii.edu/registrar/academic-calendar/fall-2026/',
  'UH Mānoa SLD (808) 956-8178'),

 ('2026-12-20', 'Dec 20, 2026', 'Hawaiʻi Pacific',
  '⚠ Last day of classes — A SUNDAY, and the latest term end in the state',
  'Commencement follows on MONDAY DEC 21. Both are as published and both are unusual; verify with the Registrar '
  'if either matters.',
  'https://www.hpu.edu/registrar/academic-calendar.html',
  'HPU main line (808) 544-0200'),

 ('2026-12-21', 'Dec 21, 2026', 'Hawaiʻi Pacific',
  'Commencement — the Hawaii fall window fully closes',
  'The last date on the Hawaii calendar. Everything else in the state finished on or before Dec 19.',
  'https://www.hpu.edu/registrar/academic-calendar.html',
  'HPU main line (808) 544-0200'),

 ('', 'By late Sep 2026 — ahead of the Oct 27 HAIC deadline', 'Statewide — HAIC',
  '⚠⚠ OPEN THE HAIC SPONSORSHIP CONVERSATION — THE BEST CHANNEL IN HAWAII AND THE ONLY PUBLISHED PRICE',
  'Registration closes 27 OCTOBER, so sponsorship conversations should START BY LATE SEPTEMBER. Published tiers: '
  'PETABYTE $7,000+, TERABYTE $5,000–6,999, GIGABYTE $2,500–4,999, MEGABYTE $500–2,499, handled by the IMAG '
  'FOUNDATION, a 501(c)(3), "making all contributions 100% tax deductible." State Office of Enterprise Technology '
  'Services IN PARTNERSHIP WITH THE UNIVERSITY OF HAWAIʻI, participants statewide — SO IT REACHES UH MĀNOA AND UH '
  'HILO STUDENTS WITHOUT A SECOND FLIGHT AND SIDESTEPS EVERY CAMPUS SOLICITATION RULE IN THIS PACKET. ⚠ NO PHONE '
  'IS PUBLISHED AND THE CONTACT EMAIL IS OBFUSCATED on both the main and sponsors pages — use the site contact '
  'form or join the HAIC Network Slack workspace. Budget for the lead time that implies.',
  'https://haic.hawaii.gov/sponsors/',
  'No phone published — site contact form or HAIC Network Slack'),

 ('', 'BLOCKING — before any Mānoa commitment', 'UH Mānoa',
  '⚠⚠ GET M10.300 — THE OPERATIVE MĀNOA FACILITIES POLICY WAS NEVER READ, AND THE ACCESS RATING OF 3 IS '
  'PROVISIONAL BECAUSE OF IT',
  '"UH Mānoa Interim Guidelines on UH Mānoa Facilities Use Practices and Procedures," '
  'https://manoa.hawaii.edu/policies/m10/m10-300/ — ROBOTS-BLOCKED ACROSS ~12 ATTEMPTS OVER TEN MINUTES '
  '(robots.txt fetch ConnectTimeout, not a 403). THIS IS THE BIGGEST SINGLE GAP IN THE HAWAII PACKET. The word '
  '"INTERIM" in its own title, alongside the systemwide interim TPM policy, suggests Mānoa\'s facilities rules '
  'are ALSO MID-REVISION. OPEN IT IN A BROWSER or request it from SLD, and extract four things specifically: '
  '(1) whether OUTSIDE ENTITIES MAY BE SPONSORED; (2) INSURANCE DOLLAR LIMITS (the archived policy requires '
  '"evidence of adequate insurance protection" but states no figures); (3) whether COMMERCIAL SOLICITATION HAS '
  'ANY EXCEPTION; (4) any language on PAYMENT APPS OR ON-SITE CONTRACTS — exactly the clause a 2025–26 rewrite '
  'would add.',
  'https://manoa.hawaii.edu/policies/m10/m10-300/',
  'Student Life & Development · sld@hawaii.edu · (808) 956-8178'),

 ('', 'BLOCKING — read before quoting ANY UH rule', 'UH Mānoa / UH Hilo',
  '⚠⚠ THE UH SYSTEMWIDE TIME, PLACE AND MANNER POLICY WAS REPLACED ON AN INTERIM BASIS EFFECTIVE 1 JULY 2026 — '
  'ANY GUIDANCE PREDATING THAT DATE IS UNRELIABLE',
  'UH replaced a TPM policy that had not been substantially updated in over ten years. Per UH President Wendy '
  'Hensel the revision targets "inconsistent interpretation and enforcement" and makes standards "more precise, '
  'transparent and workable." ⚠⚠ AND UH PLANS COMMUNITY DISCUSSIONS THROUGHOUT FALL 2026 BEFORE FINAL ADOPTION — '
  'SO THE RULES A DGD AMBASSADOR OPERATES UNDER IN SEPT–DEC 2026 ARE INTERIM AND ACTIVELY BEING REWRITTEN. WHAT '
  'AN OFFICE TELLS YOU BY PHONE IN SEPTEMBER MAY NOT HOLD IN NOVEMBER — GET IT IN WRITING. ⚠ THE OPERATIVE TEXT '
  'COULD NOT BE RETRIEVED DESPITE REPEATED ATTEMPTS: the landing page https://www.hawaii.edu/tpm-policy/ AND the '
  'circulated draft "DRAFT Administrative Procedure, AP 10.xxx Implementation of Time, Place, and Manner '
  'Restrictions" dated 11.14.25 were BOTH ROBOTS-BLOCKED, and THE FINAL AP NUMBER IS UNVERIFIED — the "10.xxx" '
  'placeholder was never resolved on any readable page. WHAT IS CONFIRMED, from two readable press sources: '
  '"Peaceful protests, demonstrations, rallies, speeches, petitions and other forms of constitutionally '
  'guaranteed expression remain fully protected," and the policy "explicitly preserves the right" of STUDENTS, '
  'FACULTY AND STAFF to spontaneously assemble in generally accessible outdoor areas WITHOUT PRIOR APPROVAL. '
  '⚠ NOTE THE ENUMERATED CLASSES — AFFILIATES ONLY. NEITHER SOURCE ADDRESSES NON-AFFILIATED PERSONS, OUTSIDE '
  'ENTITIES OR COMMERCIAL ACTIVITY, WHICH IS EXACTLY DGD\'S QUESTION — A CONFIRMED GAP, NOT A PERMISSION. Get the '
  'final AP number, the sections on non-affiliated persons and commercial activity, AND ASK WHEN THE FALL 2026 '
  'REVISIONS LAND.',
  'https://www.hawaii.edu/tpm-policy/',
  'UH Mānoa SLD (808) 956-8178 — ask for the current AP number and text'),

 ('', 'BLOCKING — before any Hilo commitment', 'UH Hilo',
  '⚠⚠ UH HILO FACILITIES USE PRACTICES AND PROCEDURES — NEVER READ, AND IT IS THE DOCUMENT THAT GOVERNS OUTSIDE '
  'GROUPS',
  'https://hilo.hawaii.edu/leadership/administrative/forms/facilities-use-practices-and-procedures.php — '
  'ROBOTS-BLOCKED ACROSS ~10 ATTEMPTS. It contains the outside-group rules, sponsorship requirements, insurance '
  'limits, fees, deposits and cancellation terms. COMPLETE GAP; MUST BE OPENED IN A BROWSER. ⚠ THE ACCESS RATING '
  'OF 2 AT HILO RESTS ENTIRELY ON THE ONE DOCUMENT THAT COULD BE READ — the "Free Expression on the UH Hilo '
  'Campus" page, which qualifies EVERY permission it grants with the word "NON-COMMERCIAL": "persons speaking, '
  'assembling, and/or distributing NON-COMMERCIAL material shall not physically impede the progress of '
  'passersby," and students may "distribute NON-COMMERCIAL literature such as petitions, circulars, leaflets, '
  'newspapers in all areas generally available to students and the community." AN ADMINISTRATOR READING THAT '
  'LITERALLY WOULD BE ON SOLID GROUND REFUSING A DGD TABLE. If the unread facilities document turns out to '
  'contain a paid or documented outside-entity route the rating rises; if it repeats the non-commercial '
  'qualifier it falls. DO NOT GUESS EITHER WAY. Ask for VC KALEI RAPOZA, who signs the free-expression policy.',
  'https://hilo.hawaii.edu/leadership/administrative/forms/facilities-use-practices-and-procedures.php',
  'No UH Hilo number confirmed — ask for VC Administrative Affairs, Kalei Rapoza'),

 ('', 'BEFORE ANY ON-SITE ACTIVITY THAT TOUCHES MONEY', 'All Hawaii campuses',
  '⚠⚠ HAWAII IS CURRENTLY PERMISSIVE ON PURE DIGITAL-ASSET ACTIVITY — BUT THE MOMENT YOU TOUCH US DOLLARS A '
  'MONEY TRANSMITTER LICENSE LIKELY ATTACHES',
  'THE MOST TRANSFERABLE FINDING IN THIS FILE, AND IT MATTERS WHETHER OR NOT ANYONE EVER TABLES IN HONOLULU. '
  'HAWAII WENT FROM HOSTILE TO DEREGULATED ON DIGITAL CURRENCY AND IS IN A LEGISLATIVE VACUUM. (1) THE SANDBOX IS '
  'OVER: the DIGITAL CURRENCY INNOVATION LAB (DCIL), a DCCA/DFI + Hawaii Technology Development Corporation '
  'program that let digital currency companies operate WITHOUT a Hawaii money transmitter license, ran 2020 to '
  '30 JUNE 2024 AND WAS ALLOWED TO SUNSET. (2) CURRENT DFI POSITION — still the live FAQ, dated 9 FEB 2024: '
  'after the DCIL concluded, "DIGITAL CURRENCY COMPANIES WILL NO LONGER REQUIRE A HAWAIʻI-ISSUED MONEY '
  'TRANSMITTER LICENSE TO CONDUCT BUSINESS." Activities listed as permissible WITHOUT a license: "trading of '
  'digital currency or assets"; "providing hosted digital currency wallets or digital currency custodial '
  'services"; "issuing or redeeming stable coins"; "transferring digital assets from one person to another." DFI '
  'notes the list "may change from time to time." (3) ⚠⚠ THE HARD LINE IS FIAT, VERBATIM: "COMPANIES THAT CONDUCT '
  'ACTIVITY IN US$ OR OTHER FIAT CURRENCIES THAT MEETS THE DEFINITION OF MONEY TRANSMISSION…WILL LIKELY REQUIRE A '
  'MONEY TRANSMITTER LICENSE FOR THAT FIAT-DENOMINATED ACTIVITY IF AN EXCLUSION…DOES NOT APPLY." BRIEF EVERY '
  'AMBASSADOR BEFORE ANY EVENT WHERE A STUDENT MIGHT HAND OVER CASH OR USE A PAYMENT APP. (4) ⚠ PERMISSIVE IS '
  'NOT ENDORSED: DFI warns that digital-currency transactions "are not guaranteed by any government agency" and '
  'that there is "no government agency that will protect consumer funds." AN AMBASSADOR WHO IMPLIES HAWAII STATE '
  'OVERSIGHT OR APPROVAL IS MISREPRESENTING THE POSITION. (5) ⚠ THE WINDOW MAY CLOSE — SEE THE 2027 MONITOR ROW. '
  '⚠ CONFIRM WITH THE HAWAII DIVISION OF FINANCIAL INSTITUTIONS (DFI), Department of Commerce and Consumer '
  'Affairs, BEFORE ANY ACTIVITY TOUCHING PAYMENTS, SIGN-UPS OR WALLET REGISTRATIONS — the FAQ relied on here is '
  'dated 9 Feb 2024.',
  'https://cca.hawaii.gov/dfi/dcil-faq-industry/',
  'Hawaii Division of Financial Institutions (DFI) — https://cca.hawaii.gov/dfi/'),

 ('', 'Monitor — 2027 legislative session', 'All Hawaii campuses',
  '⚠⚠ A DIGITAL-ASSET CHARTER BILL WILL VERY LIKELY RETURN IN 2027 — ANY MESSAGING BUILT ON "NO LICENSE REQUIRED '
  'IN HAWAII" AGES BADLY',
  'SB 2757 SD1 (33rd Legislature, 2026), "Relating to Digital Asset Charters," would have created a Digital Asset '
  'Charter Program under DFI: MANDATORY CHARTER for digital asset business activity, $9,000 application fee, '
  '$1,000 annual renewal, $2,500–$12,500 quarterly assessments, $500,000 MINIMUM TANGIBLE NET WORTH, $500,000 '
  'SURETY BOND, AML and cybersecurity programs, civil penalties to $20,000 per violation, effective 1 Jan 2027. '
  'IT PASSED THE SENATE 10 MARCH 2026, WAS DEFERRED BY THE HOUSE CONSUMER PROTECTION & COMMERCE COMMITTEE ON 17 '
  'MARCH 2026, AND DIED IN COMMITTEE. ⚠ IT CLEARED THE ENTIRE SENATE ONCE — the deregulated window is NOT '
  'guaranteed to persist. If a version passes in 2027 with a 1 Jan 2028 effective date, Hawaii\'s current '
  'permissive posture ends. Bill text: https://data.capitol.hawaii.gov/sessions/session2026/bills/SB2757_SD1_.PDF',
  'https://legiscan.com/HI/bill/SB2757/2026',
  'Hawaii DFI — https://cca.hawaii.gov/dfi/'),

 ('', 'BEFORE BOOKING ANY HAWAII TRAVEL', 'All Hawaii campuses',
  '⚠⚠ MĀNOA AND HILO ARE A FLIGHT APART, NOT A DRIVE APART — MAKE THE ROUTING DECISION FIRST',
  'UH MĀNOA IS IN HONOLULU ON OʻAHU. UH HILO IS ON HAWAIʻI ISLAND, ~200 MILES SOUTHEAST ACROSS OPEN OCEAN. THERE '
  'IS NO FERRY, NO BRIDGE AND NO ROAD — getting between them requires an interisland flight (HNL→ITO). BUDGET A '
  'HALF-DAY AND AN AIRFARE PER DIRECTION PLUS A RENTAL CAR IN HILO. ⚠ WHAT HAWAII ACTUALLY SUPPORTS IS ONE OʻAHU '
  'TRIP: MĀNOA, HAWAIʻI PACIFIC (downtown, Aloha Tower) AND CHAMINADE (Kaimukī) ARE ALL 15–20 MINUTES APART BY '
  'CAR AND SHARE A SINGLE VISIT. Hilo is a separate decision with a separate budget line, and the honest read is '
  'that it does not justify one: ~3,000 students, a modest business college, and NOT ONE relevant club, course, '
  'event or phone number confirmed. ⚠ SPONSOR HAIC INSTEAD — it is statewide and UH-partnered and reaches Hilo '
  'students for less than the airfare. ⚠ AND SEQUENCE THE OʻAHU TRIP BY CALENDAR: CHAMINADE STARTS AUG 17 AND '
  'ENDS DEC 4; UH STARTS AUG 24; HPU STARTS AUG 31 AND RUNS TO DEC 20. The one stretch where all four are in '
  'session and none is in finals is roughly 31 AUG – 26 NOV 2026.',
  'https://manoa.hawaii.edu/registrar/academic-calendar/fall-2026/',
  'UH Mānoa SLD (808) 956-8178 · HPU (808) 544-0277 · Chaminade (808) 739-8556'),

 ('', 'Call this week — highest-value call in the state', 'UH Mānoa',
  '⚠ CONFIRM THE FALL 2026 INVOLVEMENT FAIR: DATE, WHETHER OUTSIDE ENTITIES MAY TABLE, AND COST — NOTHING IS '
  'PUBLISHED',
  'ONE CALL TO STUDENT LIFE & DEVELOPMENT, (808) 956-8178, CLOSES MOST OF MĀNOA. Ask for: (1) the FALL 2026 '
  'INVOLVEMENT FAIR DATE — not published anywhere, and the Fall 2025 event page was robots-blocked, so not even '
  'the prior year\'s date could be extracted; the pattern is "early in the fall semester" at the Campus Center '
  'Complex, run for and by RIOs; (2) WHETHER OUTSIDE OR COMMUNITY ORGANIZATIONS MAY TABLE — UNVERIFIED in both '
  'directions, and given the blanket solicitation language in UH policy the working assumption should be NO until '
  'SLD says otherwise; (3) the CAMPUS CENTER RATE SHEET with DEPOSITS AND CANCELLATION TERMS (the planning page '
  'is robots-blocked); (4) the INSURANCE DOLLAR LIMIT required of non-affiliated organizations; (5) a copy of '
  'M10.300. ⚠ STALENESS WARNING: the Campus Center Complex landing page was STILL DISPLAYING FALL 2023 BUILDING '
  'HOURS in August 2026 — DO NOT TRUST A DATE FOUND THERE WITHOUT A PHONE CONFIRMATION. It will post at '
  'https://manoa.hawaii.edu/studentlife/ and at the permanent short link http://go.hawaii.edu/Um.',
  'https://manoa.hawaii.edu/studentlife/',
  'Student Life & Development · sld@hawaii.edu · (808) 956-8178'),

 ('', 'Before any Hilo outreach', 'UH Hilo',
  '⚠⚠ NOT ONE UH HILO PHONE NUMBER COULD BE CONFIRMED — BUILD THE LIST FROM SCRATCH, AND DO NOT GUESS',
  'Every staff-listing, Campus Center, Student Affairs and College of Business page attempted was ROBOTS-BLOCKED. '
  'This is the second most serious gap in the Hawaii packet after M10.300. ⚠⚠ DO NOT GUESS A NUMBER: UH HILO USES '
  'THE 808-932-xxxx AND 808-974-xxxx RANGES, NOT MĀNOA\'S 808-956-xxxx, so a Mānoa-pattern guess would be wrong. '
  'Call the campus and build the list: Campus Center, Student Life, Dean of Students, and ADMINISTRATIVE AFFAIRS '
  '(VC KALEI RAPOZA\'S OFFICE — he signs the free-expression policy and is likely the ultimate authority on '
  'facilities use). Two names are confirmed WITHOUT contact details: CHANCELLOR BONNIE IRWIN and VICE CHANCELLOR '
  'KALEIHIʻIIKAPOLI "KALEI" RAPOZA. ⚠ Also unknown: whether UH Hilo holds an involvement fair AT ALL, and whether '
  'any relevant club exists — do not assume either way. And note NO DESIGNATED PUBLIC-FORUM AREA was identified '
  'at Hilo, unlike Mānoa\'s Campus Center Courtyard.',
  'https://hilo.hawaii.edu/studentaffairs/',
  'No number confirmed — ask for VC Administrative Affairs (Kalei Rapoza) and the Campus Center'),

 ('', 'First call at HPU — and get it in writing', 'Hawaiʻi Pacific',
  '⚠⚠ DOES ANY WRITTEN SOLICITATION OR FACILITY-USE POLICY EXIST AT HPU AT ALL? NONE COULD BE FOUND',
  'NO solicitation, vendor, tabling, posting, facilities-use or event policy exists on any HPU page that could be '
  'read — checked across the whole online Student Handbook, whose Section Three covers academic integrity, the '
  'Code of Student Conduct and student rights and NOTHING on outside vendors. ⚠ AND THE USUAL HIDING PLACE IS '
  'CLOSED: the old PDF handbook now 302-REDIRECTS to the HTML version. HPU IS PRIVATE — no public-forum doctrine, '
  'no state statute reach, no First Amendment claim, NO APPEAL. ⚠ ACCESS WILL BE DECIDED BY ONE PERSON IN THE '
  'STUDENT LIFE OFFICE ON A PHONE CALL, so ask everything at once: does a written policy exist; may an outside '
  'organization table; MUST AN RSO SPONSOR US; INSURANCE REQUIREMENT AND LIMIT; SPACE RENTAL FEES; DEPOSITS; '
  'CANCELLATION TERMS; IS FINANCIAL-PRODUCT MARKETING SPECIFICALLY RESTRICTED; and is there a club fair at all — '
  'none is published on the Student Engagement page, the clubs page or the events calendar, and no recurring '
  'pattern could be established. ⚠⚠ GET ANY PERMISSION IN WRITING BY EMAIL — with nothing published, that email '
  'is the only record that will exist. ⚠ DO NOT REASON FROM UH\'S RULES; none of them bind HPU. Cheapest route '
  'in: an RSO funded by the STUDENT ACTIVITY FEE, which can host a speaker with no venue fee — start with the '
  'CAMPUS ACTIVITIES BOARD.',
  'https://studenthandbook.hpu.edu/',
  'Student Activities · studentlife@hpu.edu · leadership@hpu.edu · (808) 544-0277'),

 ('', 'Before any Chaminade ask — build in 6 weeks', 'Chaminade',
  '⚠⚠ VERIFY THE OCTOBER 2022 CLUBS HANDBOOK IS STILL CURRENT, AND PITCH THE HOGAN LECTURE SERIES AS A TALK, NOT '
  'A SPONSORSHIP',
  'The governing document — "Handbook for Student Clubs & Organizations" — IS DATED OCTOBER 2022, and since then '
  'THE OFFICE HAS BEEN RENAMED (Office of Student Activities and Leadership → OFFICE OF STUDENT ENGAGEMENT) AND '
  'THE DIRECTOR HAS CHANGED. Confirm it still governs, and get the ASSISTANT DIRECTOR\'S NAME — that role handles '
  'facility reservations and bulletin-board postings and IS NOT NAMED on the web page. ⚠ THE APPROVAL CHAIN IS '
  'THE BINDING CONSTRAINT, NOT THE ROOM: "Only registered Student Clubs/Organizations, University Departments, or '
  'agencies may host unaffiliated speakers or acts on campus"; partnering with an unregistered entity needs the '
  'DIRECTOR\'S WRITTEN APPROVAL; "The Director of Student Activities & Leadership and the Office of Advancement '
  'must approve all on-campus fundraising"; corporate sponsorship needs DIRECTOR + VP OF ADVANCEMENT clearance '
  'BEFORE SOLICITATION; off-campus fundraising requiring vendor contact needs Advancement approval 6 WEEKS PRIOR; '
  'rooms need 10 BUSINESS DAYS or a $200 LATE FEE applies. AND IT ALL SITS UNDER A "VALUES COUNTER TO THOSE OF '
  'THE UNIVERSITY" VETO AT A CATHOLIC INSTITUTION, WITH NO APPEAL. ⚠ THERE IS ALSO NO CLUB TO SPONSOR YOU: ZERO '
  'of the TEN recognized student organizations is business, finance, CS or entrepreneurship, and that list is '
  'published in full. ⚠ THE ONE GENUINE OPENING: ROY PANZARELLA, (808) 440-4280, HOGAN ENTREPRENEURIAL '
  'LEADERSHIP PROGRAM, WHICH RUNS A BI-WEEKLY LECTURE SERIES ALREADY IMPORTING OUTSIDE SPEAKERS AND OPEN ACROSS '
  'ALL MAJORS — a speaking slot does not trip the corporate-sponsorship clause. Second: GUANLIN GAO, '
  '(808) 739-4609, Director of the Economic Education Center. ⚠ INSURANCE, RENTAL RATES, DEPOSITS AND '
  'CANCELLATION TERMS ARE PUBLISHED NOWHERE — ask Facilities, (808) 735-4869.',
  'https://chaminade.edu/hogan/',
  'Student Engagement (808) 739-8556 · Hogan (808) 440-4280 · Facilities (808) 735-4869'),

 ('', 'Academic door — anytime, and cheaper than a table', 'UH Mānoa',
  '⚠ CALL THE FINANCE CHAIR AND THE MSIS DIRECTOR — A GUEST LECTURE IS FREE, NON-COMMERCIAL AND SITS OUTSIDE THE '
  'SOLICITATION REGIME ENTIRELY',
  'QIANQIU LIU, CHAIR OF THE DEPARTMENT OF FINANCE, (808) 956-8736, qianqiu@hawaii.edu — Finance owns FIN 311 '
  'INVESTMENTS, which is REQUIRED OF ALL BBA STUDENTS and is therefore the highest-enrollment finance course on '
  'campus and the best single classroom in the state. RANDALL K. MINAS, JR., MSIS DIRECTOR, (808) 956-7082, '
  'rminas@hawaii.edu — a program director can place a speaker in front of the MS in Information Systems cohort '
  'with no facilities process at all. Chairs and program directors are the people who can authorize a slot. ⚠ NO '
  'SHIDLER FACULTY MEMBER IS CONFIRMED TO RESEARCH BLOCKCHAIN, CRYPTOCURRENCY OR DIGITAL ASSETS — they are the '
  'right doors, not subject-matter matches, and NO blockchain/crypto/fintech course was found in Shidler\'s '
  'Finance or ITM academics pages (the six Finance specialization tracks are Asian Finance, Investment Management '
  '(CFA), Corporate Finance, Real Estate Finance, Financial Services & Planning (CFP), Insurance & Risk '
  'Management — none is fintech). ⚠ ONE UNCHECKED LEAD WORTH A CALL: ICS (Information & Computer Sciences) course '
  'listings were ROBOTS-BLOCKED, and a cryptography or distributed-systems course there would be the most natural '
  'fit on this campus.',
  'https://shidler.hawaii.edu/directory',
  'Qianqiu Liu (808) 956-8736 · Randall Minas (808) 956-7082 · Shidler ITM (808) 956-7430'),

 ('', 'Monitor — stale pages and unresolved leads', 'All Hawaii campuses',
  '⚠ PAGES AND LEADS AN AMBASSADOR WITH A BROWSER CAN CLOSE THAT RESEARCH TOOLING COULD NOT',
  '(1) ⚠ STALE PAGES ARE THE NORM, NOT THE EXCEPTION: the UH MĀNOA CAMPUS CENTER COMPLEX page was still showing '
  'FALL 2023 BUILDING HOURS in August 2026, and the MĀNOA CAREER CENTER employer page was still advertising a '
  'MARCH 2025 CAREER FAIR — eighteen months stale. Treat any date found on manoa.hawaii.edu as unconfirmed until '
  'someone says it on the phone; for the career fair call (808) 956-7007 and ask the date, the employer '
  'registration cost and deadline, and WHETHER A CRYPTO PROJECT IS AN ELIGIBLE EMPLOYER. (2) THE MĀNOA RIO '
  'DIRECTORY was robots-blocked and 150+ RIOs were never listed — ASK SLD TO SEARCH THE ROSTER for blockchain, '
  'crypto, bitcoin, Web3, fintech, investment, FMA, ACM and data science; NO such club is confirmed to exist AND '
  'NONE IS CONFIRMED ABSENT. (3) ⚠ UNVERIFIED LEAD WORTH ONE CLICK: Honolulu Civil Beat, May 2026, "Student-Run '
  'Stock Portfolio Could Fund Scholarships" — the article was never read and it CANNOT be confirmed that it '
  'concerns a UH Mānoa club. If it does, that is the warmest audience on the campus. '
  'https://www.civilbeat.org/2026/05/student-run-stock-portfolio-could-fund-scholarships/ (4) HPU\'S FACULTY '
  'DIRECTORY PUBLISHES DIRECT OFFICE PHONE NUMBERS and has a "VIEW ALL" option — page through it by letter to '
  'find the FINANCE AND ECONOMICS faculty; only two College of Business professors were confirmed and NEITHER\'S '
  'FIELD IS KNOWN. https://www.hpu.edu/faculty/index.html (5) HPU CATALOG COURSE LISTINGS — both attempted URL '
  'patterns 404\'d; browse from https://catalog.hpu.edu/ → Courses. (6) CHAMINADE ORG EMAILS ARE '
  'CLOUDFLARE-OBFUSCATED on both the student-organizations and Student Engagement pages and the Silver Source '
  'platform may require login — USE THE PHONE. (7) HAIC publishes NO phone and obfuscates its email — use the '
  'site form or the HAIC Network Slack. (8) NO HAWAIʻI CAMPUS FREE-SPEECH STATUTE WAS FOUND (no FORUM-Act-style '
  'law, no HRS free-expression-on-campus chapter) — marked UNVERIFIED-NEGATIVE because the search budget ran out; '
  'confirm at https://www.capitol.hawaii.gov/ and DO NOT ASSERT ONE EXISTS. (9) HAR TITLE 20, SUBTITLE 1, CHAPTER '
  '13 §§ 20-13-1 to 20-13-9 "Use of University-Owned Facilities" is CONFIRMED TO EXIST but its SECTION TEXT WAS '
  'NEVER READ, and it sits above every UH campus policy.',
  'https://manoa.hawaii.edu/careercenter/employers/career-fair/',
  'Mānoa Career Center · careers@hawaii.edu · (808) 956-7007 · SLD (808) 956-8178'),
]
