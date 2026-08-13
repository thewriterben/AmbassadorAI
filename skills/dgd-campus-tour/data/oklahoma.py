"""Oklahoma — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published at time of research — a gap to close by phone, not a finding of absence.
Schema: reference/data-schema.md

STATEWIDE LEGAL CONTEXT — read before any ambassador cites a statute:
Okla. Stat. tit. 70 s 2120 "Protected expressive activities on campus" (SB 361 / 2019,
Laws 2019 c. 212 s 1; amended HB 3543 / 2022, Laws 2022 c. 18 s 3; further amended
SB 1725 / 2026) bars free-speech zones and deems outdoor areas public forums — but
s 2120(D) protects only "NONCOMMERCIAL expressive activity," and the forum right runs to
the "campus community... AND THEIR INVITED GUESTS," defined as "students, administrators,
faculty and staff." DGD is neither noncommercial nor a member of the campus community.
The statute is a tool for student advocates, NOT a right to table. OU's $300/day fee,
OSU's $250 permit and $400/day table, and every approval requirement below are all lawful
under it. Statute text on OSCN is ROBOTS-BLOCKED to research tooling; Justia used instead:
https://law.justia.com/codes/oklahoma/title-70/section-70-2120/
Companion: 70 O.S. s 2119.1 (religious student association parity, Laws 2014 c. 350 s 2).
CORRECTION: the "Oklahoma Students' Religious Liberties Act" (2013, HB 1372) is a K-12
public-school-district statute and does NOT govern higher education. Its codified section
could not be confirmed. DO NOT CITE IT in campus outreach materials.
Statewide policy layer: OSRHE Freedom of Expression policy (Chicago-Statement style,
https://okhighered.org/wp-content/uploads/2024/03/freedom-of-expression-policy.pdf) —
contains NO commercial-speech provision and NO provision on non-affiliated persons.
Neutral for DGD.

ALL SIX CAMPUSES ARE ON SEMESTERS. No quarter, block, trimester or quad school in this
set. Oklahoma splits into two start waves one week apart: OSU and NSU Aug 17; OU, TU and
OCU Aug 24; UCO unknown.
"""

STATE = 'Oklahoma'

CAMPUSES = [

 # ---------------------------------------------------------------- 1. OU
 {'state': 'Oklahoma',
  'name': 'University of Oklahoma',
  'city': 'Norman, OK',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 4,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'Final day to register/add without instructor permission Fri Aug 28, 2026. '
             '100% charge-reduction window Aug 24 – Sep 8. Automatic W grades begin Sep 9.',
  'fallbreak': '⚠ NONE — OU has NO fall break in the 2026-27 calendar. Norman is at full '
               'density Aug 24 straight through Nov 24. Best sustained access in the state.',
  'thanksgiving': 'Wed Nov 25 – Sun Nov 29, 2026',
  'lastclass': 'Fri Dec 11, 2026 (pre-finals / exam-prep period Dec 6–13)',
  'finals': 'Mon–Fri Dec 14–18, 2026. Commencement Sat Dec 19; grades due Dec 22.',
  'cal_url': 'https://www.ou.edu/registrar/academic-records/academic-calendars/fall-2026-academic-calendar',
  'cal_status': 'CONFIRMED — registrar page last updated 6/30/2026, cross-confirmed against the 2026-2027 PDF '
                'calendar (https://ou.edu/content/dam/registrar/docs/2026-2027-academic-calendar.pdf). The HTML '
                'page renders "August 24" with no weekday; Aug 24, 2026 is a MONDAY per the PDF chronological '
                'calendar. Full-semester term Aug 24 – Dec 18 (16 weeks).',
  'fair': 'SovalPalooza (Involvement Fair) — plus a separately titled "Fall Involvement Fair" that may or may not '
          'be the same event',
  'fair_date': '⚠ Sat Aug 22, 2026, 7–9 p.m., The South Oval — CONFIRMED on OU\'s own Welcome Week schedule: '
               '"Come joint us and Camp Crimson for an Involvement Fair, a silent disco, and more!" (typo in the '
               'original). NOTE THIS IS TWO DAYS BEFORE CLASSES START. Separately, "Fall Involvement Fair '
               '(Presented by Howdy Week & Camp Crimson – ALL STUDENTS WELCOME)" is listed on OU Engage '
               '(ou.campuslabs.com/ENGAGE/event/10183606) and calendar.ou.edu/wtd/event/106791 — BOTH ARE '
               'JAVASCRIPT-RENDERED and returned no date, time or location to research tooling; the OU Daily '
               'mirror returned HTTP 429 on repeated attempts. DATE UNVERIFIED — call (405) 325-5471 or '
               '(405) 325-3163 to confirm whether this is the same fair or a second one.',
  'fair_outside': '⚠ NO PUBLISHED ANSWER — and the realistic answer is no. The Welcome Week page says "All events '
                  'are free and open to all. There is no registration required, and all guests are welcome" — that '
                  'is an ATTENDANCE statement, NOT a tabling-eligibility statement. Do not read it as permission to '
                  'table. OU policy separately bars RSOs and departments from sponsoring non-university groups '
                  'outright, so the compliant path is the paid $300/day OMU Info Tabling route. CONFIRM BY PHONE.',
  'fair_cost': 'Fair itself: not published. The compliant paid alternative is $300 PER DAY for non-university '
               'groups at Oklahoma Memorial Union Info Tabling (RSOs and university departments: free).',
  'fair_deadline': 'Not published for the fair. For OMU Info Tabling: booking via the Union Business Office; '
                   'Special Events Request Form required 15 days in advance for third parties; insurance '
                   'certificate to Risk Management at least 5 working days prior; payment due 72 working hours '
                   'prior to the event.',
  'fair_url': 'https://ou.edu/sga/cac/welcome-week/schedule',
  'policy': 'OU Facility Use Policies (Campus Scheduling) — the operative document; plus Oklahoma Memorial Union '
            'Info Tabling rates, the Special Events Request Form, the RSO Risk Management Policy and the Open '
            'Social Event Policy',
  'policy_url': 'https://www.ou.edu/scheduling/policies',
  'policy_key': "OU Facility Use Policies (Campus Scheduling, www.ou.edu/scheduling/policies): 'UNSOLICITED SALES "
                "DOOR-TO-DOOR, OFFICE-TO-OFFICE, OR IN OPEN AREAS, BY COMMERCIAL GROUPS OR INDIVIDUALS FOR "
                "COMMERCIAL OR FINANCIAL GAIN IS NOT ALLOWED.' And: 'Solicitation shall be prohibited on campus "
                "except for solicitation by university departments, RSOs or branches of the SGA which may occur in "
                "conjunction with regular student activities and campus events.' (RSOs file a Solicitation Request "
                "three (3) working days prior and pay solicitation fees.) ⚠ ANTI-FRONTING — THE DECISIVE CLAUSE: "
                "'Fronting is defined as permitting a non-University individual or organization to use University "
                "space/facilities and services under the guise that the activity is a University-sponsored program "
                "in order to receive a discounted rate or avoid payment. FRONTING IS PROHIBITED BY UNIVERSITY "
                "POLICY.' If discovered, non-university rental rates apply and the RSO/students MAY BE REFERRED TO "
                "THE OFFICE OF STUDENT CONDUCT. ⚠ SPONSORSHIP DOES NOT CURE IT — SPONSORSHIP IS ITSELF BARRED: "
                "'STUDENT ORGANIZATIONS AND UNIVERSITY DEPARTMENTS MAY NOT SPONSOR NON-UNIVERSITY GROUPS, "
                "CONTRACTORS, VENDORS, OR ORGANIZATIONS.' Co-sponsorship is the only channel and it is narrow: "
                "'The event or meeting must be planned and managed by a university department and/or RSOs' — plus a "
                "majority of attendees must be OU-affiliated and 'the mission of the outside group relates to the "
                "on-campus group.' INSURANCE: 'Third party groups are outside entities not affiliated with the "
                "University that have been hired and/or contracted to provide a service or to conduct business on "
                "campus. THESE GROUPS DO NOT FALL UNDER ANY INSURANCE COVERAGE OR SELF-INSURANCE PROVISIONS "
                "MAINTAINED BY THE UNIVERSITY OR THE STATE OF OKLAHOMA AND THEREFORE MUST ACQUIRE THEIR OWN "
                "LIABILITY COVERAGE' — proof to Risk Management at least 5 working days prior; NO DOLLAR LIMIT IS "
                "PUBLISHED on this page. ⚠ PAYMENT CREDENTIALS: 'For your protection, THE UNIVERSITY OF OKLAHOMA "
                "DOES NOT ACCEPT AND WILL NOT PROCESS CREDIT CARD INFORMATION PROVIDED VIA EMAIL OR TEXT MESSAGES. "
                "Please pay online via the payment link sent to you or contact the Campus Scheduling office via "
                "phone or in person.' Payment due 72 working hours prior; billing within 45 days of invoice, 1.5% "
                "DAILY LATE FEE thereafter. CONTRACT DISCLAIMER: 'NOTHING HEREIN CREATES ANY CONTRACTUAL, "
                "CONSTITUTIONAL OR OTHER LEGAL RIGHTS ON BEHALF OF THE RESERVING PARTY regarding the use of "
                "University property/facilities.' THE PAID ROUTE (www.ou.edu/union/host-your-event): RSOs and "
                "university departments get 7-foot tables at NO COST; 'NON-UNIVERSITY GROUPS: $300 PER DAY,' booked "
                "through the Union Business Office. Tabling conduct, verbatim: 'persons distributing flyers must "
                "remain within three feet of their tabling space'; materials must stay on the table; 'tape, nails, "
                "staples or tacks is strictly prohibited'; products 'cannot conflict with current university "
                "contracts and/or Oklahoma Memorial Union contracts or lease agreements'; groups distributing "
                "flyers without reserved space 'WILL BE ASKED TO DESIST AND REPORTED TO OUPD.' COUNTERWEIGHT for "
                "student allies only: 'The outdoor areas of campus that are generally accessible to the public are "
                "available to be used for expressive activity on a first-come, first-served basis' and OU 'does not "
                "limit demonstration activity taking place along its public roads and sidewalks, including "
                "leafleting and the dissemination of information' — the distinction OU draws is NON-COMMERCIAL "
                "EXPRESSION vs. SALES, and DGD sits on the sales side.",
  'sponsor_required': '⚠ NO — AND SPONSORSHIP IS AFFIRMATIVELY PROHIBITED. "Student organizations and University '
                      'departments may not sponsor Non-University groups, contractors, vendors, or organizations." '
                      'Do not spend three weeks courting a club: at OU that route is not merely unavailable, it '
                      'exposes the students to a conduct referral under the fronting rule. The only channels are '
                      '(a) pay $300/day for OMU Info Tabling, or (b) genuine co-sponsorship where an OU department '
                      'or RSO plans and manages the event, the audience is OU-majority, and missions align.',
  'clubs': [('⚠ NO BLOCKCHAIN / CRYPTO / WEB3 / BITCOIN RSO AT OU',
             'Verified absent — neither the Price College student-organizations page nor OU Engage surfaces one. '
             'No Financial Management Association chapter either (FMA exists at OSU). The Engage directory '
             '(500+ orgs claimed) is JAVASCRIPT-RENDERED and returned no organization list to research tooling; '
             'not login-gated as far as could be told, but not machine-readable.',
             'https://ou.campuslabs.com/engage/organizations'),
            ('Investment Club', 'Highest-fit club at OU. Confirmed on the Price College of Business student-'
             'organizations page. NO OFFICER NAMES OR CLUB EMAILS ARE PUBLISHED — do not guess officers; general '
             'inbox pricecollege@ou.edu.',
             'https://ou.campuslabs.com/engage/organization/investmentclub'),
            ('Wall Street Sooners', 'Confirmed on the Price College page.',
             'https://ou.campuslabs.com/engage/organization/wall-street-sooners'),
            ('Finance Student Association', 'Confirmed on the Price College page.',
             'https://ou.campuslabs.com/engage/organization/finance-student-association'),
            ('Wealth Management Club', 'Confirmed on the Price College page.',
             'https://ou.campuslabs.com/engage/organization/wmc'),
            ('Entrepreneurship Club', 'Confirmed on the Price College page.',
             'https://ou.campuslabs.com/engage/organization/ouentrepreneurshipclub'),
            ('Women in Finance; MISSA (Management Information Systems Student Association)',
             'Listed on the Price College page, no Engage URL captured.',
             'https://www.ou.edu/price/student-resources/student-organizations'),
            ('Other Price College orgs (listed, lower fit)',
             'Real Estate Club, Supply Chain Club, Energy Management Student Association, American Marketing '
             'Association, Beta Alpha Psi, Delta Sigma Pi, Beta Gamma Sigma, Women in Business Association, Sports '
             'Business Association, Healthcare Business Club, Pre-Law@Price, Price Professional Sales Club, '
             'Multicultural Business Program, Asian Americans in Business Association, Management & International '
             'Business Association, WISE, JCPenney Leadership Program, Graduate Business Association, Phi Beta Delta.',
             'https://www.ou.edu/price/student-resources/student-organizations')],
  'faculty': [('⚠ Dr. Anindya Maiti',
               'THE BEST ACADEMIC DOOR IN OKLAHOMA. Assistant Professor of Computer Science & Data Science '
               'Analytics; holds an ETHEREUM FOUNDATION ACADEMIC GRANT to study Ethereum network security '
               '(so does his doctoral student Scott Seidenberger). Authored the CS 5970 Blockchains & '
               'Cryptocurrencies syllabus. A guest lecture or research-seminar invitation from Maiti makes DGD an '
               '"invited guest" of the campus community under 70 O.S. s 2120 — a non-commercial door that the '
               'tabling rules do not touch. Office Devon Energy Hall 460 (the Spring 2023 syllabus lists DEH 235 / '
               'DEH 210G — STALE, use 460).',
               'Gallogly College of Engineering — Computer Science',
               'am@ou.edu · (405) 325-4951',
               'https://www.ou.edu/coe/cs/people/faculty/anindya-maiti'),
              ('Scott Seidenberger',
               'Doctoral candidate, Gallogly College of Engineering; co-holder of the Ethereum Foundation Academic '
               'Grant with Maiti. Quoted: "The Ethereum Foundation grants that Dr. Maiti and I received focus on '
               'quantitatively measuring risk to these networks and working to improve them." No phone or email '
               'published — reach via Maiti or the CS office (405) 325-4042.',
               'Gallogly College of Engineering',
               'not published — reach via (405) 325-4951 or CS office (405) 325-4042',
               'https://www.ou.edu/news/articles/2024/december/ou-showcases-blockchain-security-research'),
              ('⚠ Oklahoma Memorial Union — Union Business Office',
               'BOOKS THE $300/DAY NON-UNIVERSITY INFO TABLING. THE SINGLE MOST IMPORTANT NUMBER AT OU. '
               'Mon–Fri 8 a.m.–4 p.m. Ask for Carolyn Carter (Reservations Specialist) or Sherry Paxton '
               '(Reservations & Catering Coordinator) — the right people for a table. Same number serves OMU '
               'catering.',
               'Oklahoma Memorial Union',
               'union@ou.edu · (405) 325-2121 (main line)',
               'https://www.ou.edu/union/host-your-event'),
              ('OMU staff — names confirmed, NO DIRECT PHONES PUBLISHED',
               'Laura Tontz, Director (ltontz@ou.edu); Carolyn Carter, Reservations Specialist (cbcarter@ou.edu) — '
               'the right person for a table; Sherry Paxton, Reservations & Catering Coordinator '
               '(spaxton@ou.edu); Kim Standefer, Administrative Assistant (kstandefer@ou.edu); Bud Ille, Building '
               'Manager (ille@ou.edu). No number published for any individual — look up here; reach all via the '
               'main line.',
               'Oklahoma Memorial Union',
               'no number published — look up here; reach all via (405) 325-2121',
               'https://www.ou.edu/union/contact'),
              ('OMU building staff, after 4 p.m.',
               'After-hours building access.',
               'Oklahoma Memorial Union',
               '(405) 255-1294',
               'https://www.ou.edu/union/contact'),
              ('OMU after-hours line (per the Campus Scheduling policy page)',
               'Second after-hours number printed on the scheduling policy page.',
               'Oklahoma Memorial Union',
               '(405) 325-6894',
               'https://www.ou.edu/scheduling/policies'),
              ('⚠ K. George Ahmadi',
               'Assistant Dean of Students, Student Government & Organization Services. Controls RSO recognition, '
               'RSO SPONSORSHIP APPROVALS and solicitation requests — the person who rules on whether any '
               'club-based route exists. Direct line.',
               'Student Government & Organization Services',
               'kga@ou.edu · (405) 325-5471',
               'https://www.ou.edu/rso/contact.html'),
              ('Kyla Lewis',
               'Student Organization Support Coordinator — RSO support. No number published — look up here; reach '
               'via Student Government & Organization Services.',
               'Student Government & Organization Services',
               'kyla.lewis-1@ou.edu · no number published — look up here, or (405) 325-5471',
               'https://www.ou.edu/rso/contact.html'),
              ('Mary Hacker',
               'Administrative Support Specialist. No number published — look up here.',
               'Student Government & Organization Services',
               'mary@ou.edu · no number published — look up here, or (405) 325-5471',
               'https://www.ou.edu/rso/contact.html'),
              ('Office of Student Life (OMU Suite 428)',
               'Welcome Week, campus programs, and the open-event exemptions for non-OU attendees. Mon–Fri 9–5 CST. '
               'This number is also printed on the Open Social Event Policy PDF.',
               'Student Affairs',
               'studentlife@ou.edu · (405) 325-3163 (main line)',
               'https://www.ou.edu/studentlife/contact'),
              ('Student Life staff — names confirmed, NO DIRECT PHONES',
               'Quy Nguyen, Director of Student Life & Assistant Dean of Students (Qnguyen@ou.edu); Hannah '
               'Phillips, Associate Director, Campus Programs (hannahpphillips@ou.edu) — named on the Welcome Week '
               'page as the contact for general questions; plus 12 more coordinators. No number published for any '
               'individual — look up here; reach all via the Student Life main line.',
               'Student Affairs',
               'no number published — look up here; reach all via (405) 325-3163',
               'https://www.ou.edu/studentlife/contact'),
              ('Campus Scheduling (900 Asp Ave, Rm 207)',
               'Space reservations and Special Events approval — writes the policy quoted above. NO PHONE IS '
               'PUBLISHED ON THE PAGE — look up here; use the Union line instead.',
               'Campus Scheduling',
               'scheduling@ou.edu · no number published — look up here; use OMU (405) 325-2121',
               'https://www.ou.edu/scheduling/policies'),
              ('OU Career Center (900 Asp Ave, Suite 320)',
               'Career fairs and employer access. ⚠ EVERY OU CAREER-FAIR URL TESTED 404ed and the Handshake fair '
               'list is robots-blocked — the employer page confirms only that "the Career Center hosts or co-hosts '
               'a variety of career fairs." Dates must be obtained by phone.',
               'Career Services',
               'careercenter@ou.edu · (405) 325-1974',
               'https://www.ou.edu/career/employers'),
              ('School of Computer Science (Devon Energy Hall, 110 W. Boyd St.)',
               'Ask whether CS 5970 Blockchains & Cryptocurrencies runs in Fall 2026 and who teaches it — the '
               'CourseLeaf search endpoint is robots-blocked, so this is the only route to the answer.',
               'Gallogly College of Engineering',
               'cs@ou.edu · (405) 325-4042',
               'https://www.ou.edu/coe/cs'),
              ('Coordinator of Trademark Licensing',
               'Merchandise and branding clearance — relevant if DGD hands out branded goods.',
               'OU Operations',
               '(405) 325-8203',
               'https://www.ou.edu/operations/resources/policies'),
              ('Conference Services / ADA accommodations',
               'Accessibility accommodations for events.',
               'Conference Services',
               '(405) 325-4318',
               'https://www.ou.edu/scheduling/policies'),
              ('University Lost & Found',
               'Printed on the scheduling policy page; carried across for completeness.',
               'OU Operations',
               '(405) 325-3060',
               'https://www.ou.edu/scheduling/policies'),
              ('(Price College finance / monetary-economics faculty)',
               'NOT CONFIRMED — no individual OU Price faculty member working on digital assets, fintech or '
               'monetary economics could be confirmed on a live page. Price College main phone is NOT PUBLISHED '
               '(address 307 West Brooks, Norman OK 73019-4004). No number published — look up here, in the '
               'Finance and Economics department directories.',
               'Michael F. Price College of Business',
               'pricecollege@ou.edu · no number published — look up here',
               'https://www.ou.edu/price')],
  'courses': [('CS 5970',
               'Blockchains & Cryptocurrencies — graduate special-topics number, instructor Anindya Maiti. '
               'Syllabus PDF confirms the course RAN SPRING 2023. ⚠ FALL 2026 OFFERING UNVERIFIED: 5970 is a '
               'rotating special-topics slot, so it may or may not run. The CourseLeaf search endpoint is '
               'ROBOTS-BLOCKED (ou-public.courseleaf.com/search/?P=blockchain returned ROBOTS_DISALLOWED and '
               '/courses-az/cs/ 404ed). Confirm with the CS office, (405) 325-4042.',
               'https://www.ou.edu/content/dam/CoE/CS/Syllabi/spring-2023/CS%205970%20Syllabus%20Spr%2023%20Maiti.pdf'),
              ('(Undergraduate)',
               'NO undergraduate blockchain / crypto / fintech catalog course confirmed at OU. Class search is '
               'robots-blocked to research tooling — look up here.',
               'https://ou-public.courseleaf.com/')],
  'events': [('Welcome Week 2026',
              'Aug 22–29, 2026, all CONFIRMED: SovalPalooza + Involvement Fair, Sat Aug 22, 7–9 p.m., South Oval; '
              'Crimson Bash, South Oval, Mon Aug 24, 5–6:30 p.m.; movie night, South Oval, Tue Aug 25, 8–10 p.m.; '
              'crafts + late-night breakfast, Wed Aug 26, Jim Thorpe Multicultural Center; pickleball/bingo/soccer '
              'Thu Aug 27; CAC & Greek showcases + dance, Oklahoma Memorial Union, Fri Aug 28, 8–10 p.m.; Yardshow, '
              'South Oval, Sat Aug 29, 7 p.m.',
              'https://ou.edu/sga/cac/welcome-week/schedule'),
             ('⚠ Ethereum Foundation blockchain-security research (Maiti / Seidenberger)',
              'Not an event but the real hook: a legitimate, NON-COMMERCIAL door into OU that the tabling rules do '
              'not touch. An invitation from Maiti to speak at a research seminar makes DGD an "invited guest" of '
              'the campus community under 70 O.S. s 2120.',
              'https://www.ou.edu/news/articles/2024/december/ou-showcases-blockchain-security-research'),
             ('Career fairs — UNVERIFIED',
              '⚠ Every OU career-fair URL tested 404ed (/career/career-fairs, /career/students/career-fairs, '
              '/career/students/careerfairs, /career/about/contact) and the Handshake fair list '
              '(ou.joinhandshake.com/career_fairs) is ROBOTS-BLOCKED. No dates obtainable from the web. '
              'Call (405) 325-1974.',
              'https://www.ou.edu/career/employers'),
             ('Hackathon — NONE FOUND',
              'No OU hackathon confirmed. Contrast OSU, which has one (Hack OKState).',
              '')],
  'play': 'Norman is the state\'s biggest audience and OU has NO FALL BREAK — full density from Aug 24 straight '
          'through Nov 24, the best sustained access window in Oklahoma. But do NOT plan to work it through a club: '
          'OU is the one campus that affirmatively prohibits sponsorship ("Student organizations and University '
          'departments may not sponsor Non-University groups, contractors, vendors, or organizations") AND has an '
          'explicit anti-fronting rule that refers the students to the Office of Student Conduct. Courting an RSO '
          'here does not just fail, it endangers the people who help you. There are exactly two doors. The '
          'transactional one: pay $300/day for Oklahoma Memorial Union Info Tabling, booked at the Union Business '
          'Office, (405) 325-2121 — ask for Carolyn Carter — with the Special Events Request Form 15 days ahead, '
          'insurance certificate to Risk Management 5 working days ahead, and payment 72 working hours ahead. '
          'The better one, and the single best door at OU: Dr. Anindya Maiti, (405) 325-4951, an Ethereum '
          'Foundation Academic Grantee doing Ethereum network-security research and the author of the CS 5970 '
          'Blockchains & Cryptocurrencies syllabus. An invitation from him to a research seminar makes DGD an '
          '"invited guest" of the campus community under 70 O.S. s 2120 — outside the commercial-solicitation '
          'regime entirely, at zero cost, in front of exactly the right students. Call him first and Campus '
          'Scheduling second. ⚠ TIME-CRITICAL: SovalPalooza — OU\'s confirmed Involvement Fair — is Sat Aug 22, '
          '7–9 p.m. on the South Oval, TEN DAYS OUT, two days before classes start; and there is a second, '
          'separately titled "Fall Involvement Fair" whose date nobody could retrieve because both listings are '
          'JavaScript-rendered. Call (405) 325-5471 or (405) 325-3163 this week to find out whether that is one '
          'event or two. Also note there is no blockchain or crypto RSO at OU at all, and no FMA chapter — the '
          'finance-club cluster at Price College (Investment Club, Wall Street Sooners, Finance Student '
          'Association, Wealth Management Club) is the audience, reachable only as guests of a co-sponsored, '
          'OU-planned event.',
  'gaps': ['⚠ Which Involvement Fair is which — SovalPalooza (Sat Aug 22, 7–9pm, South Oval, CONFIRMED) vs. the '
           'separately titled "Fall Involvement Fair (Presented by Howdy Week & Camp Crimson)" on OU Engage and '
           'calendar.ou.edu, both JavaScript-rendered with no retrievable date; the OU Daily mirror returned HTTP '
           '429 repeatedly. Call (405) 325-5471 or (405) 325-3163.',
           '⚠ Whether a paid outside table is possible at either involvement fair — no published answer. '
           '(405) 325-2121.',
           'OU room and table rate card — the $300/day Info Tabling rate is confirmed, but the Equipment & Service '
           'Rates PDF has "UNIVERSITY/RSO RATE" and "NON-UNIVERSITY RATE" columns with NO room rental or tabling '
           'rates in the retrievable portion (only A/V tech $40/hr, projectors $100–$200). Union Business Office, '
           '(405) 325-2121 — ask for Carolyn Carter or Sherry Paxton. '
           'https://www.ou.edu/content/dam/union/docs/equipmentandservicerates.pdf',
           'Insurance dollar limit for third parties — the requirement is published, the amount is not. Risk '
           'Management via (405) 325-2121.',
           'Whether CS 5970 Blockchains & Cryptocurrencies runs in Fall 2026 and who teaches it — the CourseLeaf '
           'search endpoint is ROBOTS-BLOCKED. CS office, (405) 325-4042.',
           'OU career-fair dates — all four URL variants 404ed and the Handshake list is robots-blocked. '
           '(405) 325-1974.',
           'OU Engage club directory could not be enumerated (JavaScript-rendered, 500+ orgs claimed). Whether any '
           'blockchain/crypto RSO exists outside Price College is unconfirmed — ask (405) 325-5471.',
           'Price College main phone and any digital-assets/fintech faculty — not published. '
           'https://www.ou.edu/price',
           'FIRE\'s mirror of "Facility Use and Solicitation Policy for RSOs and Individual OU Students" 404s — '
           'DEAD LINK, do not rely on it. The RSO Policy on PolicyStat requires a session token in the URL and may '
           'not load cleanly: https://oupolicy.policystat.com/v2/policy/18173323/latest/'],
  'note': 'The Open Social Event Policy (unticketed parties 11 p.m.–8 a.m.) is not relevant to daytime tabling but '
          'matters if DGD ever sponsors an evening student event: it requires 2 CLEET-certified guards plus 1 OUPD '
          'officer on university property, and non-OU attendees need a "written exemption... granted by the '
          'director of Student Life. Only one exemption per organization will be permitted each semester." '
          'https://www.ou.edu/content/dam/scheduling/docs/Open%20Event%20Policy%20Revised%200715.pdf'},

 # ---------------------------------------------------------------- 2. OSU
 {'state': 'Oklahoma',
  'name': 'Oklahoma State University',
  'city': 'Stillwater, OK',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 5,
  'start': '⚠ Mon Aug 17, 2026 — EARLIEST START IN THE STATE, a full week ahead of OU, TU and OCU',
  'adddrop': '100% refund / nonrestrictive drop-add deadline Mon Aug 24; partial refund / restrictive drop-add '
             'deadline Fri Aug 28. W drop/withdrawal deadline Fri Nov 6; assigned W or F deadline Mon Nov 30.',
  'fallbreak': '⚠ Mon–Wed Nov 23–25, 2026 — merged with Thanksgiving into ONE FIVE-DAY DEAD ZONE Nov 23–27.',
  'thanksgiving': 'Thu–Fri Nov 26–27, 2026 (contiguous with fall break — campus closed Nov 23–27)',
  'lastclass': '⚠ Fri Dec 4, 2026 — a full week before OU/NSU/OCU. ANYTHING SCHEDULED AT OSU AFTER ~NOV 20 IS '
               'WORTHLESS.',
  'finals': 'Mon–Fri Dec 7–11, 2026. Graduate commencement Fri Dec 11; undergraduate Sat Dec 12; grades on '
            'transcripts Fri Dec 18.',
  'cal_url': 'https://registrar.okstate.edu/academic_calendar/academic-calendar-fall-2026',
  'cal_status': 'CONFIRMED on the Registrar\'s Fall 2026 page.',
  'fair': 'Fall 2026 Involvement Fair (inside Cowboy Welcome) — BEST-DOCUMENTED FAIR IN THE STATE',
  'fair_date': '⚠⚠ Thu Aug 13, 2026, 3:30–5:30 p.m. CDT, Student Union 2nd Floor, 110 S Hester Street, Stillwater '
               'OK 74078 — CONFIRMED on two OSU pages, page is current, not stale. Aug 13, 2026 IS a Thursday. '
               'Billed as "500+ student organizations" on the events page and "400+" on the Cowboy Welcome page — '
               'minor internal inconsistency, not material. NOTE THE FAIR IS FOUR DAYS BEFORE CLASSES START '
               '(Aug 13 vs Aug 17). Registration via cowboycentral.okstate.edu.',
  'fair_outside': 'NOT STATED on the fair page — but OSU is the ONE campus in this set with a published, '
                  'purchasable outside-vendor route, so the question is answerable and priced: "All off-campus '
                  'vendors that would like to vend within the OSU campus must contact Meeting & Conference '
                  'Services to obtain a solicitation permit." Whether that permit can be used AT THE INVOLVEMENT '
                  'FAIR SPECIFICALLY is the call to make. Meeting & Conference Services (405) 744-5232 and Alex '
                  'Comer (405) 744-5785.',
  'fair_cost': '$250.00 solicitation permit per semester (Fall, Spring, Summer) PLUS $400.00 per standard table '
               'space per day for off-campus vendors. Clothed tables $5.00 each. On-campus RSOs and faculty/staff '
               'departments table free, 8 a.m.–5 p.m. Mon–Fri. Budget: $250 once for Fall 2026 + $400 per '
               'table-day.',
  'fair_deadline': 'Not published. Booking through the EMS portal (bookings.okstate.edu/EMSWebApp/) and the permit '
                   'through Meeting & Conference Services, (405) 744-5232. ⚠ THE FAIR IS AUG 13 — a permit bought '
                   'after that date still covers the whole Fall semester, so buying it is worth doing regardless.',
  'fair_url': 'https://events.okstate.edu/event/fall-2026-involvement-fair',
  'policy': 'OSU Meeting & Conference Services — Tabling (the operative document, and the only published '
            'for-profit vendor tier in Oklahoma); above it, OSU/A&M Board of Regents Policy 3.13 "Extracurricular '
            'Use of Institutional Facilities, Areas or Media for the Purpose of Expression"',
  'policy_url': 'https://meetings.okstate.edu/tabling',
  'policy_key': "OSU Meeting & Conference Services — Tabling (meetings.okstate.edu/tabling): 'ALL OFF-CAMPUS "
                "VENDORS THAT WOULD LIKE TO VEND WITHIN THE OSU CAMPUS MUST CONTACT MEETING & CONFERENCE SERVICES "
                "TO OBTAIN A SOLICITATION PERMIT. All reservations for off-campus vendors or those selling "
                "merchandise of any kind will incur a cost of $400.00 PER STANDARD TABLE SPACE PER DAY as well as "
                "a SOLICITATION PERMIT FEE OF $250.00 PER SEMESTER (Fall, Spring, Summer).' This is the cleanest "
                "commercial-access path in Oklahoma: a permit exists, it has a price, and a named office sells it. "
                "Fee-free tabling is limited to 'On-Campus Recognized Student Organizations and Faculty/Staff "
                "Departments', available 8:00 a.m.–5:00 p.m., Monday through Friday. CONDUCT: 'SOLICITATION MUST "
                "OCCUR FROM BEHIND THE TABLE AND MUST NOT BLOCK EGRESS. No structures can be built on the "
                "solicitation site and/or table top. Amplified sound is not allowed inside the Student Union' — "
                "outdoor amplified sound must stay 'at or below 70 decibels.' INDOOR: 'One 6-foot table and two "
                "chairs will be set up at your reserved tabling location. Clothed tables are $5.00 each.' OUTDOOR: "
                "'Organizations and departments may check-in at the Information Desk located on the first floor of "
                "the Student Union across from The University Store... A VALID OSU ID IS REQUIRED AT TIME OF "
                "CHECK-IN. You will be required to set up your own table and chairs at your approved tabling "
                "location; once your tabling reservation is over you will need to return your table and chairs and "
                "sign out at the Information Desk. Fees may apply if equipment is not returned or stolen.' ⚠ The "
                "OSU-ID check-in means an unaffiliated vendor needs an escort or a different arrangement outdoors "
                "— ask about this specifically. GOVERNING POLICY ABOVE MCS — OSU/A&M Board of Regents Policy 3.13, "
                "'Extracurricular Use of Institutional Facilities, Areas or Media for the Purpose of Expression' "
                "(amended June 22, 2018 and September 13, 2019, regents.okstate.edu/node/287): 'This Policy shall "
                "be applicable only to the Extracurricular use of any institutional-controlled facility, area or "
                "medium used as a forum generally open to members of the institutional community AND OTHERS for "
                "the purpose of Expression.' Reservation requests must include 'the name of the requestor and how "
                "he/she can be contacted; the proposed date, time and location for the contemplated activity; the "
                "expected size of the audience; and any other information that may be necessary to accommodate the "
                "needs associated with the activity.' THE RETRIEVABLE REGENTS TEXT CONTAINS NO COMMERCIAL-ACTIVITY "
                "OR SOLICITATION CLAUSE — commercial control lives in the MCS tabling policy and the permit fee. "
                "⚠ NOTABLE ABSENCES — all verified-not-found, NOT verified-permitted: NO ANTI-FRONTING CLAUSE "
                "was found (nothing forbids an RSO reserving on behalf of an outside entity); NO CLAUSE FORBIDDING "
                "RSOs FROM SPONSORING OUTSIDE GROUPS was found; NO INSURANCE REQUIREMENT appears on the tabling "
                "page; NO DEPOSIT OR CANCELLATION TERMS were found; and NO LANGUAGE REACHING CREDIT CARDS, PAYMENT "
                "APPS OR ON-SITE CONTRACTS was found anywhere. That combination is what makes OSU rank first — but "
                "ABSENCE OF PUBLISHED TEXT IS NOT PERMISSION. The policy hub at meetings.okstate.edu/guidelines "
                "lists eight request forms and six policy documents but CONTAINS NO POLICY TEXT, NO RATE TABLE, NO "
                "INSURANCE TERMS AND NO DEPOSIT OR CANCELLATION TERMS, and the substantive PDFs behind it did not "
                "resolve to research tooling. GET THE STUDENT UNION USE GUIDELINES PDF BY PHONE: (405) 744-5232.",
  'sponsor_required': 'NO — and uniquely in Oklahoma, no rule bars a club from hosting DGD either. OSU sells '
                      'direct commercial access ($250 permit + $400/table/day) and no anti-fronting or '
                      'no-sponsorship clause could be found. Buy the permit; you do not need a student proxy. '
                      'But confirm the absence explicitly at (405) 744-5232 before relying on it.',
  'clubs': [('⚠ NO BLOCKCHAIN / CRYPTO / WEB3 RSO AT OSU',
             'Verified absent — and note the contrast: OSU runs a substantial NON-CREDIT blockchain certificate '
             'program (13 courses, 5 certifications) with no student club to match it. The demand exists, the club '
             'does not. That is an opening. The Cowboy Central directory is JAVASCRIPT-RENDERED (stuck on '
             '"Loading") and returned nothing to research tooling; not confirmed login-gated. Cowboy Central is '
             'new as of 2026.',
             'https://cowboycentral.okstate.edu/organizations/'),
            ('⚠ Financial Management Association (FMA)',
             'Best club target in the state. FMA International chapter — "Superior Chapter" for 20 consecutive '
             'years, Ambassador Chapter since 2021. PUBLISHED FACULTY ADVISORS with direct phones: Jun Zhang '
             '(jun.zhang@okstate.edu, (405) 744-8628) and Amit Bansal (amit.bansal@okstate.edu, (405) 612-5681). '
             'Advisors are staff, not students — these names are stable and safe to use.',
             'https://business.okstate.edu/undergraduate/student_organizations'),
            ('Spearhead Scholars Investment Banking Program',
             'Advisor Eric Sisneros — eric.sisneros@okstate.edu, (405) 744-1798. The investment-banking cohort.',
             'https://business.okstate.edu/undergraduate/student_organizations'),
            ('Free Enterprise Society',
             'Free-markets speaker series — STRONG IDEOLOGICAL FIT FOR A SOUND-MONEY PITCH, and a speaker series '
             'is a non-commercial door. Advisor Per Bylund — per.bylund@okstate.edu.',
             'https://business.okstate.edu/undergraduate/student_organizations'),
            ('Economics Society',
             'Advisor Sunny (Qinghe) Su — qinghe.su@okstate.edu.',
             'https://business.okstate.edu/undergraduate/student_organizations'),
            ('OSU Consulting Club', 'Advisor Stephanie Royce — ssroyce@okstate.edu.',
             'https://business.okstate.edu/undergraduate/student_organizations'),
            ('Data Analytics Club', 'Advisors Kim Strom and Jerry Rackley — emails not listed.',
             'https://business.okstate.edu/undergraduate/student_organizations'),
            ('Beta Alpha Psi (accounting)', 'Advisor Craig Sisneros — craig.sisneros@okstate.edu.',
             'https://business.okstate.edu/undergraduate/student_organizations'),
            ('Entrepreneurship Club', 'Listed on the Spears page; no advisor listed.',
             'https://business.okstate.edu/undergraduate/student_organizations'),
            ('⚠ STALE-SOURCE WARNING — archived Spears PDF',
             'An archived PDF at business.okstate.edu/site-files/archive/docs/undergraduate/student_organizations.'
             'pdf lists a DIFFERENT advisor set (FMA to Tom Johansen, 311 Business; Economics Society to Karen '
             'Maguire, 327 Business; Entrepreneurship Club to Bruce Barringer, 104B Business) plus "Students in '
             'Free Enterprise," a name retired industry-wide in 2012. IT IS OUT OF DATE — DO NOT USE ITS NAMES. '
             'The one useful thing in it is a Career Services number, 405.744.2772. Advisor assignments rotate; '
             'cross-check the live page against directory.okstate.edu before calling.',
             'https://business.okstate.edu/site-files/archive/docs/undergraduate/student_organizations.pdf')],
  'faculty': [('⚠ Meeting & Conference Services (179 Student Union)',
               'SELLS THE $250/SEMESTER SOLICITATION PERMIT AND THE $400/DAY TABLE. THE SINGLE MOST IMPORTANT '
               'NUMBER IN OKLAHOMA FOR THIS TOUR. Also the office to ask for the Student Union Use Guidelines PDF, '
               'the outdoor OSU-ID check-in workaround, and confirmation that no insurance/deposit/anti-fronting '
               'terms exist.',
               'Meeting & Conference Services',
               'meetings@okstate.edu · (405) 744-5232',
               'https://meetings.okstate.edu/tabling'),
              ('Meeting & Conference Services (207 Wes Watkins Center)',
               'Second MCS office — same function, different building.',
               'Meeting & Conference Services',
               'meetings@okstate.edu · (405) 744-9359',
               'https://meetings.okstate.edu/contact-us'),
              ('⚠ Alex Comer',
               'Coordinator, Campus Life — THE NAMED CONTACT ON THE FALL 2026 INVOLVEMENT FAIR LISTING. Call this '
               'number first about the Aug 13 fair; call (405) 744-5232 for the permit.',
               'Campus Life',
               'roo.comer@okstate.edu · (405) 744-5785',
               'https://events.okstate.edu/event/fall-2026-involvement-fair'),
              ('Campus Life (232 Student Union, Mon–Fri 8–5)',
               'Involvement Fair, RSO recognition, Cowboy Welcome — the office behind Comer.',
               'Campus Life',
               'campuslife@okstate.edu · (405) 744-5488',
               'https://campuslife.okstate.edu/aboutus'),
              ('Amy Gazaway', 'Director, Campus Life — leadership escalation.', 'Campus Life',
               'amy.gazaway@okstate.edu · (405) 744-5815',
               'https://directory.okstate.edu/index.php/module/Default/action/ViewDepartment?id=1568'),
              ('Johnny Robinson', 'Director, Campus Life.', 'Campus Life',
               'johnny.robinson@okstate.edu · (405) 744-9885',
               'https://directory.okstate.edu/index.php/module/Default/action/ViewDepartment?id=1568'),
              ('Aleigha Mariott', 'Assistant VP, Campus Life — escalation above Campus Life.', 'Campus Life',
               'aleigha.mariott@okstate.edu · (405) 744-9885',
               'https://directory.okstate.edu/index.php/module/Default/action/ViewDepartment?id=1568'),
              ('Fran Gragg', 'Assistant Director, Campus Life.', 'Campus Life',
               'fran.gragg@okstate.edu · (405) 744-5406',
               'https://directory.okstate.edu/index.php/module/Default/action/ViewDepartment?id=1568'),
              ('Melisa Echols', 'Coordinator, Campus Life.', 'Campus Life',
               'mechols@okstate.edu · (405) 744-0370',
               'https://directory.okstate.edu/index.php/module/Default/action/ViewDepartment?id=1568'),
              ('Garrett Hargrove', 'Coordinator, Campus Life.', 'Campus Life',
               'gahargr@okstate.edu · (405) 744-7332',
               'https://directory.okstate.edu/index.php/module/Default/action/ViewDepartment?id=1568'),
              ('Kristen Hill', 'Coordinator, Campus Life.', 'Campus Life',
               'kristen.hill10@okstate.edu · (405) 744-7264',
               'https://directory.okstate.edu/index.php/module/Default/action/ViewDepartment?id=1568'),
              ('Haley Osiek', 'Coordinator, Campus Life.', 'Campus Life',
               'haley.osiek@okstate.edu · (405) 744-7158',
               'https://directory.okstate.edu/index.php/module/Default/action/ViewDepartment?id=1568'),
              ('Mckinley Paratore', 'Coordinator, Campus Life.', 'Campus Life',
               'mckinley.paratore@okstate.edu · (405) 744-1055',
               'https://directory.okstate.edu/index.php/module/Default/action/ViewDepartment?id=1568'),
              ('Darius Wingfield', 'Coordinator, Campus Life.', 'Campus Life',
               'darius.wingfield@okstate.edu · (405) 744-5490',
               'https://directory.okstate.edu/index.php/module/Default/action/ViewDepartment?id=1568'),
              ('Elizabeth Greythorne', 'Administrative Support Specialist II, Campus Life.', 'Campus Life',
               'elizabeth.greythorne@okstate.edu · (405) 744-5490',
               'https://directory.okstate.edu/index.php/module/Default/action/ViewDepartment?id=1568'),
              ('Casey Domnick', 'Assistant Director, Fraternity & Sorority Affairs.', 'Campus Life',
               'casey.domnick@okstate.edu · (405) 744-6403',
               'https://directory.okstate.edu/index.php/module/Default/action/ViewDepartment?id=1568'),
              ('Student Union main office', 'Building operations.', 'Student Union',
               'osuunion@okstate.edu · (405) 744-5231', 'https://union.okstate.edu/directory.html'),
              ('Office of the VP for Student Affairs (201 Whitehurst)',
               'Free-speech complaints, appeals and policy escalation. OSU\'s free-speech hub cites 70 O.S. s 2120 '
               'and SB 361 and publishes a violation complaint form and an annual report.',
               'Student Affairs', '(405) 744-5328', 'https://studentaffairs.okstate.edu/free-speech/'),
              ('Career Services (360 Student Union)',
               'All six confirmed Fall 2026 career fairs and employer registration. Employer registration is open '
               'with early-bird pricing offered, but SPECIFIC FEES AND DEADLINES ARE NOT PUBLISHED — call.',
               'Career Services', 'careers@okstate.edu · (405) 744-5253', 'https://careerservices.okstate.edu/'),
              ('Career Services (number from the ARCHIVED Spears PDF)',
               '⚠ This number comes from an archived, out-of-date document — treat as secondary to '
               '(405) 744-5253.',
               'Career Services', '405.744.2772',
               'https://business.okstate.edu/site-files/archive/docs/undergraduate/student_organizations.pdf'),
              ('David Carter',
               'Head, Department of Finance; OBA Chair of Commercial Bank Management — the finance department '
               'gatekeeper. ⚠ The OSU finance directory publishes NO research interests, so no one here is a '
               'confirmed digital-assets researcher. Carter (commercial banking), Piccotti (market '
               'microstructure), Lee (quant finance) and Bansal (financial health + FMA) are the most plausible '
               'starting calls, but that is INFERENCE. DO NOT REPRESENT ANY OF THEM AS A CRYPTO RESEARCHER.',
               'Department of Finance, 461 Business Building',
               'david.carter@okstate.edu · (405) 744-5104',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Department of Finance (461 Business Building)',
               'Department main line — also the listed number for Brian Roseman and Jake Walters.',
               'Department of Finance', '(405) 744-5199 (main line)',
               'https://business.okstate.edu/departments_programs/finance'),
              ('⚠ Amit Bansal',
               'Instructor of Professional Practice; DIRECTOR, CENTER FOR FINANCIAL HEALTH AND WELLNESS; FMA '
               'co-advisor. One call reaches both a financial-literacy programming budget and the FMA chapter.',
               'Department of Finance', 'amit.bansal@okstate.edu · (405) 612-5681',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('⚠ Jun Zhang',
               'Associate Professor, Spears Professorship; FMA ADVISOR — the faculty door to the strongest finance '
               'club in the state.',
               'Department of Finance', 'jun.zhang@okstate.edu · (405) 744-8628',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('⚠ Eric Sisneros',
               'Assistant Head, Department of Finance; SPEARHEAD SCHOLARS INVESTMENT BANKING ADVISOR — reaches the '
               'IB cohort and carries departmental authority.',
               'Department of Finance', 'eric.sisneros@okstate.edu · (405) 744-1798',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Betty Simkins', 'Regents Professor; Williams Companies Chair — senior finance faculty.',
               'Department of Finance', 'betty.simkins@okstate.edu · (405) 744-8625',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Louis Piccotti', 'Associate Professor; William S. Spears Chair — market microstructure.',
               'Department of Finance', 'louis.r.piccotti@okstate.edu · (405) 744-8666',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Brian Roseman', 'Associate Professor; Watson Family Chair in Financial Risk Management.',
               'Department of Finance', 'brian.roseman@okstate.edu · (405) 744-5199',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Allissa Lee', 'Assoc. Prof. of Professional Practice; DIRECTOR, MS QUANTITATIVE FINANCE — reaches '
               'the quant-finance graduate cohort.',
               'Department of Finance', 'allissa.lee@okstate.edu · (405) 744-3260',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Shu Yan', 'Associate Professor; ONEOK Chair; Ph.D. Coordinator.', 'Department of Finance',
               'yanshu@okstate.edu · (405) 744-5089',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('William Grieser', 'Associate Professor.', 'Department of Finance',
               'william.grieser@okstate.edu · (405) 744-5104',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Aaron Burt', 'Assistant Professor.', 'Department of Finance',
               'aaron.burt@okstate.edu · (405) 744-1692',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Joe Byers', 'Assistant Professor of Professional Practice.', 'Department of Finance',
               'joe.w.byers@okstate.edu · (405) 744-8636',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Ken Petrashek', 'Lecturer.', 'Department of Finance',
               'ken.petrashek@okstate.edu · (405) 744-9892',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Emma Qin Wang', 'Associate Professor; Spears Chair — Tulsa-based number.', 'Department of Finance',
               'qin.wang@okstate.edu · (918) 594-8394',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Josh Herlan', 'Lecturer.', 'Department of Finance',
               'joshua.herlan@okstate.edu · (918) 812-2682',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Jared Pawelka', 'Lecturer.', 'Department of Finance',
               'jared.pawelka@okstate.edu · (918) 720-2996',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Jake Walters', 'Lecturer.', 'Department of Finance',
               'jacob.r.walters@okstate.edu · (405) 744-5199',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Anshuang Fu', 'Assistant Professor. No number published — look up here.', 'Department of Finance',
               'anshuang.fu@okstate.edu · no number published — look up here',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('Beth Peterson', 'Lecturer. Neither phone nor email published — look up here.',
               'Department of Finance', 'no number published — look up here',
               'https://business.okstate.edu/departments_programs/finance/meet_the_department.html'),
              ('⚠ Lindsey Ray',
               'Program Manager for the OSU + The Blockchain Academy non-credit program (13 courses, 5 '
               'certification programs), Center for Executive and Professional Development, Spears Business. '
               'Dean at launch was Dr. Ken Eastman; external partner Ryan Williams, Executive Director of The '
               'Blockchain Academy. ⚠ ANNOUNCED 2021 AND THE REGISTRATION SITE (blockchainhub360.com/okstate) '
               'TIMED OUT ON robots.txt — CONFIRM THE PROGRAM STILL RUNS BEFORE BUILDING A PITCH AROUND IT. Note '
               'this is a PROFESSIONAL-EDUCATION audience, not undergraduates — different buyer, different pitch.',
               'Center for Executive and Professional Development',
               'lindssk@okstate.edu · (405) 744-8650',
               'https://news.okstate.edu/articles/business/2021/cepd_blockchain_academy.html'),
              ('Center for Executive and Professional Development',
               'The office behind the blockchain certificate suite.',
               'Spears School of Business', '(405) 744-5208',
               'https://news.okstate.edu/articles/business/2021/cepd_blockchain_academy.html'),
              ('OSU main operator',
               'MAIN LINE — last resort. OSU publishes a full staff directory with direct numbers at '
               'directory.okstate.edu; use that for anyone not listed here.',
               'Oklahoma State University', '(405) 744-5000 (main line)', 'https://directory.okstate.edu')],
  'courses': [('(For-credit)',
               'NO for-credit blockchain / crypto / fintech course confirmed at OSU. '
               'catalog.okstate.edu/search/?P=blockchain is ROBOTS-BLOCKED; catalog.okstate.edu/courses/fin/ '
               'returned a program index with no course descriptions; /course-descriptions/fin/ 404ed. Look up '
               'here, and in the live schedule at '
               'https://studentregistrationssb.okstate.edu/StudentRegistrationSsb/ssb/term/termSelection'
               '?mode=search&mepCode=OSU',
               'http://catalog.okstate.edu/'),
              ('OSU + The Blockchain Academy (non-credit)',
               'CONFIRMED: 13 non-credit courses and 5 certification programs through the Center for Executive and '
               'Professional Development. Professional-education audience, not undergraduates. Program Manager '
               'Lindsey Ray, (405) 744-8650. ⚠ Registration site blockchainhub360.com/okstate was not retrievable '
               '(robots.txt timeout); announced 2021, current status unconfirmed.',
               'https://news.okstate.edu/articles/business/2021/cepd_blockchain_academy.html'),
              ('Blockchain Fundamentals (ed2go) — NOT A STILLWATER COURSE',
               'Offered by OSU-OKC, a SEPARATE INSTITUTION. Self-paced, non-credit, online. Do not confuse it with '
               'a Stillwater offering.',
               'https://www.ed2go.com/osuokc/online-courses/blockchain-fundamentals/')],
  'events': [('⚠⚠ Fall 2026 Involvement Fair',
              'Thu Aug 13, 2026, 3:30–5:30 p.m., Student Union 2nd Floor. 400–500+ student organizations. Named '
              'contact Alex Comer, roo.comer@okstate.edu, (405) 744-5785. Four days before classes begin.',
              'https://events.okstate.edu/event/fall-2026-involvement-fair'),
             ('Cowboy Welcome, Aug 12–22, 2026 — full confirmed schedule',
              'SUAB Night, Wed Aug 12, 6–9 p.m., Student Union; STUDENT INVOLVEMENT FAIR, Thu Aug 13, 3:30–5:30 '
              'p.m., Student Union 2nd floor; Library House Party, Thu Aug 13, 7–9 p.m., Edmon Low Library; Rock '
              'the Block, Fri Aug 14, 5–7 p.m., Colvin Recreation Center; Xposed, Sat Aug 15, 6–9 p.m., Student '
              'Union North Plaza; Late Night Cafe, Sat Aug 15, 8:30–10:30 p.m., Student Union Food Court; Cowboy '
              'Kickoff, Sun Aug 16, 6:30–7:30 p.m., Gallagher-Iba Arena; Class Photo, Sun Aug 16, gates 7:30 p.m., '
              'Boone Pickens Stadium.',
              'https://campuslife.okstate.edu/cowboy-welcome'),
             ('⚠⚠ HACK OKSTATE — the single best sponsorship-pipeline target in Oklahoma',
              'A PRIVATE, STUDENT-RUN EVENT: sponsoring it sidesteps the $250 permit and the '
              'commercial-solicitation rules entirely. ⚠ THE LIVE SITE IS STALE — it still shows "Hack OKState '
              '\'25," Nov 1–2, 2025, Engineering South, Stillwater, which as of August 2026 is LAST YEAR\'S CYCLE. '
              '(It also carries a "Major League Hacking 2026 Hackathon Season" badge — that is the MLH season '
              'label spanning 2025-26, NOT a 2026 event date.) Recurring pattern: one weekend, early November, '
              'Engineering South, 24 hours, 100+ participants from any university, $1,000+ in prizes, OPEN '
              'SPONSORSHIP (2025 sponsors included MLH and Pure Buttons). FALL 2026 DATES UNVERIFIED — email '
              'hackokstate@okstate.edu NOW; sponsor decks typically close 6–8 weeks out, i.e. SEPTEMBER 2026. '
              'Discord: discord.gg/NkrYgaUnAN',
              'https://hackokstate.com/'),
             ('Fall 2026 career fairs — ALL SIX CONFIRMED WITH DATES',
              'Part-Time Job Fair, Tue Aug 25, 11 a.m.–2 p.m., Student Union Ballroom (2nd floor Rm 265); CEAT '
              '(Engineering/Architecture/Tech) Career Fair, Tue Sep 15, 9 a.m.–3:30 p.m.; BUSINESS CAREER FAIR, '
              'Wed Sep 16, 11:30 a.m.–4 p.m. (best fit); Ag, Food & Natural Resources Career Fair, Thu Sep 17, '
              '11:30 a.m.–4:30 p.m.; OSU-Tulsa Career Fair, Wed Sep 30, 1:30–3:30 p.m., Main Hall Commons; '
              'Construction Industry Career Fair, Tue Oct 6, 9:30 a.m.–12 p.m. ⚠ Employer registration fees and '
              'deadlines are NOT PUBLISHED — call (405) 744-5253.',
              'https://careerservices.okstate.edu/'),
             ('Oklahoma Bitcoin Association — off-campus, possible co-host',
              'A state-level community group, NOT campus-affiliated, but a plausible co-host for a Stillwater or '
              'OKC event.',
              'https://www.oklahomabitcoin.org/')],
  'play': '⚠⚠ THIS IS THE ANCHOR OF THE OKLAHOMA TOUR, AND IT IS ON FIRE RIGHT NOW. OSU is the only campus in the '
          'state that sells commercial access outright: a $250 solicitation permit per semester plus $400 per '
          'table per day, from a named office at a known number — Meeting & Conference Services, (405) 744-5232. '
          'No anti-fronting clause, no ban on RSO sponsorship, no insurance requirement and no deposit terms could '
          'be found anywhere in OSU\'s published policy, which is why it ranks first; treat those absences as '
          'questions to confirm on that call, not as permissions. ⚠⚠ THE FALL 2026 INVOLVEMENT FAIR IS TOMORROW — '
          'Thu Aug 13, 3:30–5:30 p.m., Student Union 2nd floor, 400–500+ organizations, four days before classes '
          'start. If there is any chance of making it, call Alex Comer at (405) 744-5785 and Meeting & Conference '
          'Services at (405) 744-5232 TODAY and ask whether an off-campus vendor can buy in at the fair itself; '
          'note the outdoor check-in requires "a valid OSU ID," so ask how a non-affiliated vendor checks in. If '
          'tomorrow is impossible, buy the permit anyway — it covers the whole Fall semester — and aim at the '
          'Business Career Fair on Wed Sep 16. The other half of the play is free: Hack OKState is a private, '
          'student-run hackathon that sidesteps the solicitation regime entirely, its site is a year stale, and '
          'sponsor decks typically close 6–8 weeks before an early-November weekend — email hackokstate@okstate.edu '
          'this week, September at the very latest. Warmest human doors: Jun Zhang (405) 744-8628 and Amit Bansal '
          '(405) 612-5681, the two FMA advisors, and Per Bylund\'s Free Enterprise Society speaker series, which '
          'is an ideological match for a sound-money talk and a non-commercial format. ⚠ TIMING TRAP: OSU starts a '
          'week early and DIES FIRST — fall break and Thanksgiving merge into a five-day closure Nov 23–27 and the '
          'last day of classes is Dec 4. Nothing scheduled in Stillwater after about Nov 20 is worth the drive.',
  'gaps': ['⚠⚠ Whether an off-campus vendor may purchase a table AT THE AUG 13 INVOLVEMENT FAIR SPECIFICALLY — not '
           'stated anywhere. (405) 744-5232 and (405) 744-5785.',
           '⚠ How a non-affiliated vendor satisfies the outdoor check-in rule ("A valid OSU ID is required at time '
           'of check-in"). (405) 744-5232.',
           '⚠ The Student Union Use Guidelines PDF — meetings.okstate.edu/guidelines lists eight forms and six '
           'policy documents but contains NO policy text, NO rate table, NO insurance terms and NO deposit or '
           'cancellation terms, and the PDFs behind it did not resolve. Get it by phone: (405) 744-5232.',
           '⚠ Confirm the $250 permit and $400/day table are current for Fall 2026. (405) 744-5232.',
           '⚠ OSU\'s missing restrictions — no anti-fronting clause, no RSO-sponsorship ban, no insurance '
           'requirement, no deposit/cancellation terms and no payment-credential language were found. ABSENCE OF '
           'PUBLISHED TEXT IS NOT PERMISSION. Confirm each explicitly at (405) 744-5232.',
           '⚠⚠ Hack OKState Fall 2026 dates and sponsorship deck — the live site is a year stale (shows Nov 1–2, '
           '2025). hackokstate@okstate.edu.',
           'Career-fair employer registration fees and deadlines — dates confirmed, prices not published. '
           '(405) 744-5253.',
           'Whether the OSU + Blockchain Academy non-credit program still operates — announced 2021, registration '
           'site blockchainhub360.com/okstate not retrievable (robots.txt timeout). Lindsey Ray, (405) 744-8650.',
           'Cowboy Central org directory could not be enumerated (JavaScript-rendered, stuck on "Loading"). '
           'Whether any blockchain/crypto RSO exists — ask Campus Life, (405) 744-5488.',
           'Which finance faculty actually work on digital assets — the OSU finance directory publishes NO research '
           'interests, so 19 faculty are unsorted. Do not represent any of them as a crypto researcher.'],
  'note': '⚠ DO NOT CONFUSE THIS CAMPUS WITH OSU-OKC, OSU-IT OR OSU-TULSA. Each publishes its own calendar '
          '(osuokc.edu, osuit.edu) and NONE of the Stillwater dates above apply to them. The ed2go "Blockchain '
          'Fundamentals" course belongs to OSU-OKC, not Stillwater.'},

 # ---------------------------------------------------------------- 3. TU
 {'state': 'Oklahoma',
  'name': 'University of Tulsa',
  'city': 'Tulsa, OK',
  'type': 'Private',
  'tier': 'B — Regional',
  'access': 3,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'Last day to add via Self-Service Fri Aug 28; last day to add through advising Tue Sep 1; last day to '
             'drop without a W Fri Sep 11.',
  'fallbreak': 'Thu–Fri Oct 15–16, 2026 — ⚠ IDENTICAL TO NSU\'S. Do not route Tulsa and Tahlequah in that week; '
               'both are closed.',
  'thanksgiving': '⚠ Mon–Fri Nov 23–27, 2026 — a FULL FIVE-DAY WEEK, longer than any other campus in the set.',
  'lastclass': 'Tue Dec 8, 2026',
  'finals': '⚠ Fri Dec 11, then Mon–Fri Dec 14–18, 2026 — an unusual split: one Friday exam day, a weekend, then '
            'the block.',
  'cal_url': 'https://utulsa.edu/academics/academic-calendar/',
  'cal_status': 'CONFIRMED — 16-week traditional terms; online programs run 8-week sessions. Bulletin mirrors: '
                'https://utulsa.catalog.acalog.com/content.php?catoid=53&navoid=2884 and '
                'https://bulletin.utulsa.edu/content.php?catoid=48&navoid=2582',
  'fair': 'Activity & Resource Fair (Office of Student Activities)',
  'fair_date': '⚠ FALL 2026 DATE NOT PUBLISHED. What IS confirmed, verbatim: "On the first Thursday of each '
               'semester, SA sponsors an Activity & Resource Fair." Classes begin Mon Aug 24, 2026, so the first '
               'Thursday of the semester is THU AUG 27, 2026 — THIS IS INFERRED, NOT CONFIRMED. A separate TU news '
               'piece confirms only "an activities fair held each year at the beginning of the fall semester" and '
               'that TU has "more than 180 student organizations." It will post at calendar.utulsa.edu (⚠ the '
               'default view surfaced only Aug 11–15, 2026 — USE MONTH VIEW for September onward) and in the SA '
               'Student Hub at univoftulsa.sharepoint.com/sites/sa-hub, which is SHAREPOINT AND LOGIN-GATED. '
               'Confirm at 918-631-3211.',
  'fair_outside': '⚠ NO PUBLISHED ANSWER — assume NO by default. TU is PRIVATE: neither First Amendment '
                  'public-forum doctrine nor 70 O.S. s 2120 binds it, and the Student Union rules say "Events at '
                  'which non-TU participants may be in attendance MAY REQUIRE PRIOR APPROVAL FROM THE DIRECTOR." '
                  'Call 918-631-3211.',
  'fair_cost': 'Not published. TU publishes NO DOLLAR RATE CARD anywhere. Recognized university groups and campus '
               'departments get space at no charge; TU faculty, staff, students and alumni get 10% off rack rate '
               'for non-TU functions; DGD as an outside entity pays FULL PUBLISHED RACK RATE, amount unknown. Get '
               'the rate sheet by phone: 918-631-3211.',
  'fair_deadline': 'Not published for the fair. For rentals: deposits and insurance certificates due 10–14 '
                   'business days prior; cancellation free only 20+ days out.',
  'fair_url': 'https://utulsa.edu/about/offices/student-activities/',
  'policy': 'Allen Chapman Student Union Reservation Policies Guide (the operative document); plus Student '
            'Policies & Procedures (governs students, not outside entities)',
  'policy_url': 'https://utulsa.edu/about/offices/event-planning/reservation-policies-guide/',
  'policy_key': "⚠ TU IS PRIVATE. NEITHER THE FIRST AMENDMENT PUBLIC-FORUM DOCTRINE NOR 70 O.S. s 2120 BINDS IT — "
                "s 2120 applies only to 'public institution[s] of higher education.' TU CAN REFUSE DGD FOR ANY "
                "REASON, AT ANY TIME, WITH NO APPEAL. Everything below is contractual, not constitutional. "
                "Allen Chapman Student Union Reservation Policies Guide "
                "(utulsa.edu/about/offices/event-planning/reservation-policies-guide/): OUTSIDE PARTICIPANTS — "
                "'Events at which non-TU participants may be in attendance MAY REQUIRE PRIOR APPROVAL FROM THE "
                "DIRECTOR.' SALES AND SOLICITATION IN LOBBY SPACE — 'All uses of lobby space that involve the SALE "
                "OF GOODS OR SERVICES (especially food/beverages) OR TAKING OF ORDERS OR SUBSCRIPTION, etc. MUST "
                "BE APPROVED BY THE ADMINISTRATIVE OFFICE, and in some cases, Director of Dining Services.' ⚠ Note "
                "'TAKING OF ORDERS OR SUBSCRIPTION' — that language plausibly reaches sign-ups, waitlists and "
                "wallet registrations. RAISE IT EXPLICITLY WHEN YOU CALL. MERCHANDISE EXCLUSIVITY — 'The Allen "
                "Chapman Student Union... RESERVES THE RIGHT TO SELL ALL NOVELTIES OR ANY RELATED MERCHANDISE that "
                "are in conjunction with any event.' RATES — 'Recognized University groups and campus departments "
                "are provided space at no charge'; 'University members, including faculty, staff, student and "
                "alumni, can rent facilities for non-UTulsa functions at a 10 percent discount off of the room "
                "rental rates (discount does not apply to staffing and equipment charges).' THE DOLLAR RATE CARD "
                "IS NOT PUBLISHED; DGD pays full rack rate. INSURANCE — 'You may be required to purchase a general "
                "liability and property damage insurance certificate FOR UP TO $500,000.00. The certificate must "
                "also state, THE UNIVERSITY OF TULSA IS NAMED AS ADDITIONAL INSURED.' Off-campus clients 'must "
                "secure the insurance' and submit deposits and certificates 10–14 BUSINESS DAYS PRIOR. DEPOSITS "
                "AND CANCELLATION (off-campus clients) — 'Room reservation cancellations are allowed, without "
                "charge, if canceled TWENTY (20) DAYS IN ADVANCE'; 'Within twenty (20) days prior to the start of "
                "the event will be charged 50% OF APPLICABLE ROOM FEES'; 'Within five (5) business days prior to "
                "the start of the event will be charged 100% OF APPLICABLE ROOM FEES.' Deposits due 10 business "
                "days prior. (University groups: cancel by 9:00 a.m. the prior business day; 'After three (3) no "
                "shows without notification, per semester, scheduling privileges... may be suspended for 12 "
                "calendar months.') FOR STUDENT ALLIES ONLY — Student Policies & Procedures is comparatively "
                "permissive on NON-COMMERCIAL distribution: 'Leaflets and printed materials may be distributed at "
                "gatherings, in common areas, and also in classrooms with the permission of the instructor,' and "
                "facility regulations 'cannot be used for censorship' — but THAT SECTION GOVERNS STUDENTS, NOT "
                "OUTSIDE ENTITIES. ⚠ GAPS THAT ARE NOT PERMISSIONS: NO ANTI-FRONTING CLAUSE FOUND; NO EXPLICIT "
                "RSO-SPONSORSHIP REQUIREMENT FOUND; NO EXPLICIT BAN ON COMMERCIAL SOLICITATION OR FINANCIAL-"
                "PRODUCT MARKETING FOUND; NO LANGUAGE REACHING CREDIT CARDS, PAYMENT APPS OR ON-SITE CONTRACTS "
                "FOUND. AT A PRIVATE INSTITUTION THE ABSENCE OF A WRITTEN RULE MEANS DISCRETION, NOT PERMISSION.",
  'sponsor_required': 'Unclear — no RSO-sponsorship requirement and no anti-fronting rule are published, but '
                      '"Events at which non-TU participants may be in attendance may require prior approval from '
                      'the Director," so the Student Union Director is the gate regardless of who invites you. '
                      'A student org route is not foreclosed on paper; it is simply undefined, and TU can say no '
                      'without a reason. Ask Event Planning (918-631-3211) and Student Engagement (918-631-2067).',
  'clubs': [('⚠ NO BLOCKCHAIN / CRYPTO / WEB3 CLUB AT TU',
             'Not found on the public org page. ~180 orgs total; the FULL ROSTER LIVES IN THE SA STUDENT HUB ON '
             'SHAREPOINT AND IS LOGIN-GATED — unreadable to research tooling. Every club on the public page lists '
             'the same shared contact, sga.ssc@utulsa.edu, with NO OFFICER NAMES. DO NOT INVENT OFFICER NAMES.',
             'https://utulsa.edu/student-life/student-organizations/'),
            ('⚠ NO FINANCE, INVESTMENT, ECONOMICS OR FMA CHAPTER ON THE PUBLIC PAGE — but one almost certainly '
             'exists',
             'TU runs a $9 MILLION STUDENT-MANAGED INVESTMENT FUND (ranked Top 25 in the U.S.) and 12 Bloomberg '
             'terminals. A fund that size implies a finance club; it is simply behind the SharePoint wall. THOSE '
             'STUDENTS ARE THE SINGLE BEST-QUALIFIED AUDIENCE IN THE STATE. Ask Student Engagement, 918-631-2067.',
             'https://utulsa.edu/programs/finance/'),
            ('Association for Computing Machinery (ACM)', 'Strongest CS-side target on the public page.',
             'https://utulsa.edu/student-life/student-organizations/'),
            ('Capture the Flag', 'Cybersecurity competition club — competes in international CTFs. CLOSEST '
             'CULTURAL ADJACENCY TO CRYPTO at TU. Contact sga.ssc@utulsa.edu.',
             'https://utulsa.edu/student-life/student-organizations/'),
            ('Marketing Club', 'The only business-side club named on the public page.',
             'https://utulsa.edu/student-life/student-organizations/'),
            ('Artificial Intelligence / Machine Learning Club', 'Listed on the public page.',
             'https://utulsa.edu/student-life/student-organizations/'),
            ('Quantum Computing Club; International Game Developers Association', 'Listed on the public page.',
             'https://utulsa.edu/student-life/student-organizations/'),
            ('Student Government Association', 'Shared inbox sga.ssc@utulsa.edu is the ONLY published club contact '
             'at TU.',
             'https://utulsa.edu/student-life/student-organizations/student-government-association/')],
  'faculty': [('⚠ Allen Chapman Student Union — Administrative Office / Event Planning',
               'ALL SPACE RESERVATIONS, LOBBY-SALES APPROVAL, INSURANCE AND DEPOSITS. THE NUMBER TO CALL AT TU. '
               'Also the number for the Office of Student Activities, which runs the Activity & Resource Fair and '
               'publishes no direct line of its own.',
               'Allen Chapman Student Union',
               'eventhelp@utulsa.edu · 918-631-3211',
               'https://utulsa.edu/about/offices/event-planning/reservation-policies-guide/'),
              ('⚠ Office of Student Engagement / Dean of Students',
               'Student orgs, the SharePoint org roster, and policy interpretation — the office that can tell you '
               'whether a finance club exists behind the login. 2nd floor, Hardesty Hall–Holmes Student Center. '
               '⚠ THE PAGE LISTS ROLES, NOT NAMES ("Dean of Students or Associate Dean of Students," "Director of '
               'New Student Programs") — NO INDIVIDUAL COULD BE CONFIRMED. Ask by role.',
               'Student Engagement',
               'dean-of-students@utulsa.edu · 918-631-2067',
               'https://utulsa.edu/about/offices/student-engagement/'),
              ('Director of New Student Programs',
               'Welcome week and orientation programming — name not published, ask by role.',
               'Student Engagement', '918-631-3590',
               'https://utulsa.edu/about/offices/student-engagement/'),
              ('Office of Civic Engagement', 'Community partnerships.', 'Civic Engagement', '918-631-3303',
               'https://utulsa.edu/about/offices/student-engagement/'),
              ('Sorority & Fraternity Life', 'Greek programming.', 'Student Engagement',
               'greeklife@utulsa.edu · 918-631-3057', 'https://utulsa.edu/about/offices/student-engagement/'),
              ('1894 Catering (Sodexo)', 'REQUIRED CATERER for any TU event with food.', 'Dining Services',
               '1894catering.usa@sodexo.com · 918-697-9286',
               'https://utulsa.edu/about/offices/event-planning/reservation-policies-guide/'),
              ('Office of Student Activities (Student Union 2nd floor, 800 S. Tucker Dr.)',
               'Runs the Activity & Resource Fair. NO DIRECT PHONE PUBLISHED — look up here; use Event Planning.',
               'Student Activities', 'no number published — look up here; use 918-631-3211',
               'https://utulsa.edu/about/offices/student-activities/'),
              ('Wen-Chyuan Chiang',
               'Department Chair, Finance & Operations Management (2nd floor Helmerich Hall, 3102 E. Fifth Street). '
               'NO DEPARTMENT PHONE IS PUBLISHED on the page and no direct number for the chair — look up here.',
               'Finance & Operations Management',
               'wen-chyuan-chiang@utulsa.edu · no number published — look up here',
               'https://utulsa.edu/academics/business/academics/departments/finance-operations-management/'),
              ('Ismail Abdulrashid; Anila Madhan (CPA); Thomas Kim',
               'Named finance faculty from the program page. NO PHONES OR EMAILS PUBLISHED FOR ANY OF THEM. ⚠ NO TU '
               'FACULTY MEMBER WORKING ON BLOCKCHAIN, CRYPTO, FINTECH, DIGITAL ASSETS OR MONETARY ECONOMICS COULD '
               'BE CONFIRMED. Look up here.',
               'Finance & Operations Management', 'no number published — look up here',
               'https://utulsa.edu/programs/finance/'),
              ('⚠ School of Cyber Studies / Cyber Corps',
               'THE REAL INSTITUTIONAL ASSET AT TU: an NSF-funded Cyber Corps program ($6.3M NSF award) and a cyber '
               'innovation institute with a projected $75M investment — the deepest applied-security faculty '
               'concentration in Oklahoma and the natural home for a distributed-systems/security conversation. '
               'NO INDIVIDUAL FACULTY PHONE NUMBERS CONFIRMED — look up here.',
               'College of Engineering & Computer Science',
               'no number published — look up here',
               'https://utulsa.edu/academics/engineering-computer-science/academics/departments/school-cyber-studies/')],
  'courses': [('(Finance curriculum)',
               'NO fintech, blockchain, cryptocurrency or digital-assets course is listed on the TU finance program '
               'page. Program areas are corporate finance, banking, investment planning and real estate. Degrees: '
               'Finance B.S.B.A., Finance minor, Finance MBA (online).',
               'https://utulsa.edu/programs/finance/'),
              ('(Infrastructure, not curriculum)',
               '12 BLOOMBERG TERMINALS, a $9 MILLION STUDENT-MANAGED INVESTMENT FUND (Top 25 in the U.S.), and a '
               'risk-management center with live financial databases and stock-ticker boards. A student fund of '
               'that size is a serious, sophisticated audience and a natural venue for a digital-assets guest '
               'session.',
               'https://utulsa.edu/programs/finance/'),
              ('(Full catalog search)',
               'NOT PERFORMED — research search budget exhausted. Look up here and at '
               'https://utulsa.edu/academics/academic-calendar/schedule-of-courses/',
               'https://utulsa.catalog.acalog.com/')],
  'events': [('⚠ Activity & Resource Fair — INFERRED Thu Aug 27, 2026',
              'UNCONFIRMED. Policy text says only "On the first Thursday of each semester, SA sponsors an Activity '
              '& Resource Fair." First Thursday after the Aug 24 start is Aug 27. Confirm at 918-631-3211.',
              'https://utulsa.edu/about/offices/student-activities/'),
             ('Career fairs — UNVERIFIED',
              'Not found on any reachable page. If DGD ever positions as an EMPLOYER, a separate and stricter '
              'recruiting regime applies: '
              'https://utulsa.edu/student-life/canecareers/employers/recruiting-policies-guidelines/',
              'https://utulsa.edu/student-life/canecareers/employers/recruiting-policies-guidelines/'),
             ('Hackathon — NONE FOUND',
              'None found at TU. Given the Cyber Corps / CTF culture a CTF competition likely exists — ask the '
              'Capture the Flag club via sga.ssc@utulsa.edu.',
              ''),
             ('⚠ Cyber innovation institute build-out (~$75M)',
              'The most fundable technical environment in the state. SPONSORSHIP AND SPEAKER ACCESS THERE ARE WORTH '
              'MORE THAN A TABLE.',
              'https://utulsa.edu/news/tu-launches-cyber-research-commercialization-institute/'),
             ('Events calendar — use month view',
              '⚠ The default view surfaced only Aug 11–15, 2026 to research tooling. Use month/list view for Fall.',
              'https://calendar.utulsa.edu/')],
  'play': 'Do not table at TU — rent, or better, get invited. TU is private, so there is no forum right, no '
          'statute and no appeal; the Student Union Director can refuse you without a reason, lobby sales '
          'including "taking of orders or subscription" need Administrative Office approval, the Union reserves '
          'the right to sell all merchandise at any event, insurance runs to $500,000 naming TU as additional '
          'insured, and the cancellation ladder charges 50% inside 20 days and 100% inside 5 business days — '
          'against a rate card that is not published anywhere. Enrollment is only ~4,000, so the economics of a '
          'paid table are poor. The reason to come to Tulsa is that TU has the single best-qualified audience in '
          'the state and it is invisible from the web: a $9 MILLION student-managed investment fund ranked Top 25 '
          'nationally, 12 Bloomberg terminals, and — on the other side of campus — the NSF-funded Cyber Corps and '
          'a cyber innovation institute with ~$75M behind it. There is no finance club on the public org page '
          'because the full roster sits behind a SharePoint login. So the single best door is one phone call: '
          '918-631-2067, Office of Student Engagement, asking who advises the student-managed fund and whether a '
          'finance or investment club exists. A guest session with that fund, or a talk to the Capture the Flag '
          'club, is worth more than any table TU would sell you. ⚠ TIME-CRITICAL: the Activity & Resource Fair is '
          'INFERRED for Thu Aug 27 (policy says first Thursday of the semester; classes start Aug 24) — that is '
          'fifteen days out and unconfirmed, so call 918-631-3211 this week. ⚠ ROUTING: TU\'s fall break, Oct '
          '15–16, is identical to NSU\'s, and TU takes a full five-day Thanksgiving week Nov 23–27 — do not route '
          'Tulsa and Tahlequah together in mid-October.',
  'gaps': ['⚠ Activity & Resource Fair Fall 2026 date — INFERRED as Thu Aug 27 from "first Thursday of each '
           'semester." Confirm at 918-631-3211.',
           '⚠ TU rate card — NO dollar rental rates are published anywhere. The $500,000 insurance figure, the '
           '20-day/5-day cancellation ladder and the 10-day deposit rule ARE confirmed; the prices are not. '
           '918-631-3211.',
           '⚠ Whether "taking of orders or subscription" reaches sign-ups, waitlists and wallet registrations — '
           'raise it explicitly. 918-631-3211.',
           '⚠ TU\'s finance club and the advisor of the $9M student-managed fund — the full org roster is behind a '
           'SharePoint login (univoftulsa.sharepoint.com/sites/sa-hub). 918-631-2067.',
           'Whether outside organizations may table at the Activity & Resource Fair at all — no published answer.',
           'Individual names in the Office of Student Engagement — the page lists ROLES ONLY. Ask by role at '
           '918-631-2067.',
           'Any TU faculty member in blockchain, crypto, fintech, digital assets or monetary economics — none '
           'could be confirmed. Finance & Operations Management directory: '
           'https://utulsa.edu/academics/business/academics/departments/finance-operations-management/',
           'Finance department phone — not published on the department page.',
           'TU career fairs — none found on any reachable page.',
           'Full catalog course search was not performed (search budget exhausted): '
           'https://utulsa.catalog.acalog.com/'],
  'note': 'PRIVATE UNIVERSITY, ~4,000 students, heavy engineering/cyber and petroleum focus with a real business '
          'school (Collins College of Business). 70 O.S. s 2120 does not apply. Absence of a written rule here '
          'means discretion, not permission.'},

 # ---------------------------------------------------------------- 4. UCO
 {'state': 'Oklahoma',
  'name': 'University of Central Oklahoma',
  'city': 'Edmond, OK',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 3,
  'start': '⚠ UNVERIFIED — NO UCO DATE OF ANY KIND COULD BE CONFIRMED. UCO is a SEMESTER institution (structural, '
           'not date-specific). Regional Oklahoma publics (NSU, and UCO historically) tend to start the same week '
           'as OSU — i.e. ~Aug 17, 2026, a week earlier than OU/TU/OCU. THIS IS A PATTERN INFERENCE ONLY. DO NOT '
           'SCHEDULE AGAINST IT.',
  'adddrop': 'UNVERIFIED',
  'fallbreak': 'UNVERIFIED',
  'thanksgiving': 'UNVERIFIED',
  'lastclass': 'UNVERIFIED',
  'finals': 'UNVERIFIED',
  'cal_url': 'https://www.uco.edu/academic-calendar',
  'cal_status': '⚠ UNVERIFIED — the academic-calendar URL returns HTTP 403 to research tooling. Also try '
                'https://catalog.uco.edu/content.php?catoid=11&navoid=384 (SSL CERTIFICATE_VERIFY_FAILED), '
                'https://calendar.uco.edu/academics/all (JavaScript-rendered; exposes only a link back to the '
                '403 page), and the priority-enrollment page, which sometimes carries term dates: '
                'https://www.uco.edu/admissions-aid/enrollment-services/priority-enrollment-dates',
  'fair': 'UNVERIFIED',
  'fair_date': '⚠ UNVERIFIED — no fair name, date, time, location, cost tier or application deadline could be '
               'confirmed. UCO welcome-week programming is branded around "Stampede Week" in some years, but THAT '
               'COULD NOT BE CONFIRMED AND SHOULD NOT BE PRINTED. Where it would post: '
               'https://www.uco.edu/students/involvement/ (403), https://ucore.uco.edu/studentorgs/home/ '
               '(JavaScript single-page app), https://calendar.uco.edu/',
  'fair_outside': 'UNVERIFIED — no answer either way. UCO IS PUBLIC, so 70 O.S. s 2120 binds it: outdoor areas are '
                  'public forums FOR THE CAMPUS COMMUNITY, free-speech zones are prohibited, and the NONCOMMERCIAL '
                  'carve-out in subsection D applies against DGD exactly as it does at OU and OSU.',
  'fair_cost': 'UNVERIFIED — no tabling rate is published anywhere reachable. The only retrievable rates are Nigh '
               'University Center ROOM rentals (see policy_key), and that page does not say whether external '
               'commercial entities may book them or at what tier.',
  'fair_deadline': 'UNVERIFIED',
  'fair_url': 'https://www.uco.edu/students/involvement/',
  'policy': '⚠ NOT RETRIEVED — no policy text, no policy number, no effective date, no fees, no insurance terms, '
            'no anti-fronting language and no sponsorship rule could be obtained. Known policy landing pages to '
            'try: uco.edu/policy/ · uco.edu/students/dss/campus-events-access · '
            'uco.edu/fin-ops/financial-services/purchasing/ (vendor/procurement side) · '
            'uco.edu/fin-ops/financial-services/policies',
  'policy_url': 'https://www.uco.edu/offices/events/spaces',
  'policy_key': "⚠⚠ ACCESS RATING IS PROVISIONAL — RATED 3 BY DEFAULT BECAUSE THE GOVERNING POLICY COULD NOT BE "
                "RETRIEVED, NOT BECAUSE A GATE WAS FOUND. THE NAMED GAP: uco.edu is largely unreachable from "
                "research tooling. curl to any uco.edu URL returns CONNECT TUNNEL FAILED, 403 at the proxy — the "
                "domain appears blocked at the network layer for direct fetches. WebFetch returns HTTP 403 on "
                "/students/involvement/, /students/involvement/student-orgs/, /students/, /offices/events, "
                "/offices/events/, /policy/, /academic-calendar, /students/dss/campus-events-access, and on "
                "uco.edu without www. catalog.uco.edu fails robots.txt fetch with SSL: CERTIFICATE_VERIFY_FAILED — "
                "an unresolvable certificate-chain problem on UCO's catalog host, NOT a robots exclusion. "
                "calendar.uco.edu/academics/all is JAVASCRIPT-RENDERED. ucore.uco.edu/studentorgs/home/ is a "
                "JAVASCRIPT SINGLE-PAGE APP ('StudentsCommunityPlatform') with no server-rendered content. "
                "eventscentralok.com (UCO's external event-rental brand) returns 403. EXACTLY ONE PAGE LOADED: "
                "https://www.uco.edu/offices/events/spaces, which carries ZERO CONTACT INFORMATION and says only "
                "'Contact our team and let them find one of the hidden gems on campus.' WHAT THAT ONE PAGE DOES "
                "GIVE — Nigh University Center rental rates, published, but with NO statement of whether external "
                "commercial entities may book them or at what tier: Grand Ballroom (9,000 sq ft, 525 banquet / 600 "
                "theatre / 450 classroom) $2,055 FULL, $685 PER SECTION, incl. mic, screen and house sound; "
                "Constitution Hall (5,500 sq ft auditorium, 510 theatre) $575 HALF-DAY, $1,155 FULL-DAY, incl. "
                "mics, projector, screen, Blu-ray and house sound; Executive Conference Room 112 (14 people) $210; "
                "Executive Conference Room 423 (14 people) $240; The Blue Tent at Broncho Lake (50 theatre) $130 "
                "FULL-DAY; The Terrace overlooking Broncho Lake (30 theatre) $130 FULL-DAY. Premium Rooms (floors "
                "2–4, 664–1,910 sq ft), Standard Rooms (floors 1–3, 192–915 sq ft), the Y-Chapel of Song, Plunkett "
                "Park and Chickasaw Plaza amphitheater are listed with NO PUBLISHED RATE. Page note: 'Rates below "
                "do not apply to wedding ceremonies or receptions.' NO TABLING RATE, NO EXTERNAL-CLIENT POLICY, NO "
                "ANTI-FRONTING LANGUAGE, NO SPONSORSHIP RULE, NO INSURANCE TERMS AND NO PAYMENT-CREDENTIAL "
                "LANGUAGE ARE PUBLISHED ANYWHERE REACHABLE. THE ONLY BINDING TEXT CONFIRMED FOR UCO IS THE STATUTE "
                "ITSELF: 70 O.S. s 2120(D) protects only 'NONCOMMERCIAL expressive activity,' and the public-forum "
                "right in s 2120(C) runs to the 'campus community... and their invited guests.' THIS CAMPUS MUST "
                "BE WORKED ENTIRELY BY PHONE. Third-party aggregators (academicjobs.com, semestertimeline.com, "
                "ZoomInfo, Yelp) surfaced UCO calendar and phone data in search results and were DELIBERATELY NOT "
                "USED — publishing a scraped number that turns out wrong burns the relationship; a labelled gap "
                "does not.",
  'sponsor_required': 'UNVERIFIED — no sponsorship rule of any kind could be retrieved. Do not assume a club route '
                      'exists and do not assume it is barred. Establish it on the first call.',
  'clubs': [('⚠ UNVERIFIED — NO UCO CLUB OF ANY KIND IS CONFIRMED',
             'Including whether a blockchain, crypto, finance, investment, economics, entrepreneurship, ACM or '
             'data-science club exists. The org directory is the UCORE "StudentsCommunityPlatform" JavaScript app '
             'and it RENDERS NOTHING SERVER-SIDE — not confirmed login-gated, confirmed unreadable. Also try '
             'https://www.uco.edu/students/involvement/student-orgs/ (403). DO NOT INVENT NAMES.',
             'https://ucore.uco.edu/studentorgs/home/')],
  'faculty': [('⚠⚠ ZERO UCO PHONE NUMBERS CONFIRMED — THE SINGLE LARGEST GAP IN THE OKLAHOMA DATASET',
               'No Student Involvement, Dean of Students, Events Management, Conference Services or Nigh '
               'University Center scheduling number could be confirmed on any live page. UCO does not appear to '
               'expose a directory.uco.edu people-search reachable by research tooling. UCO main campus address: '
               '100 N. University Drive, Edmond, OK 73034. The main switchboard number was NOT confirmed on a UCO '
               'page and is deliberately NOT PRINTED HERE rather than guessed.',
               'University of Central Oklahoma',
               'no number published — look up here',
               'https://www.uco.edu/offices/events'),
              ('Events Management',
               'Controls the Nigh University Center spaces whose rates are the only UCO data that loaded. FIRST '
               'CALL — start here. No number published — look up here.',
               'Events Management',
               'no number published — look up here',
               'https://www.uco.edu/offices/events'),
              ('Student Involvement',
               'Second call — org directory, involvement fair, any club route. No number published — look up here '
               '(page returns 403 to automated tooling; may load in a normal browser).',
               'Student Affairs',
               'no number published — look up here',
               'https://www.uco.edu/students/involvement/'),
              ('Student Affairs index',
               'Third call. No number published — look up here.',
               'Student Affairs',
               'no number published — look up here',
               'https://www.uco.edu/students/'),
              ('(Faculty)',
               'NOT CONFIRMED — no UCO faculty member in blockchain, crypto, fintech, digital assets, monetary '
               'economics or payments could be confirmed. Look up in the College of Business (Economics, Finance) '
               'and Computer Science listings once the catalog host\'s SSL problem is worked around.',
               'College of Business / Computer Science',
               'no number published — look up here',
               'https://catalog.uco.edu/')],
  'courses': [('(Catalog)',
               'UNVERIFIED — no UCO catalog course on blockchain, crypto, fintech or digital money confirmed. The '
               'catalog host has an SSL CERTIFICATE-CHAIN FAILURE that blocked all access. Look up here (expect '
               'certificate warnings) — College of Business (Economics, Finance) and Computer Science listings.',
               'https://catalog.uco.edu/')],
  'events': [('(All events)',
              'UNVERIFIED — no career fair, startup week, speaker series or hackathon confirmed. Look up here.',
              'https://calendar.uco.edu/')],
  'play': 'UCO cannot be planned from a desk, and that is the whole finding: uco.edu returns 403 to automated '
          'fetches at nearly every path, the catalog host has an SSL certificate-chain failure, the org directory '
          'is an unreadable JavaScript app, and the external event-rental brand (eventscentralok.com) also 403s. '
          'Exactly one page loaded — the Nigh University Center room-rate list — and it carries no contact '
          'information at all. NOT ONE UCO DATE, POLICY QUOTE, CLUB, FACULTY MEMBER OR PHONE NUMBER IS CONFIRMED, '
          'and no number is printed here because a scraped one that turns out wrong burns the relationship. Do '
          'NOT skip this campus on that basis, though: UCO is ~14,000 students in the OKC metro, the third-largest '
          'audience in the state, and as a public institution it sits under the same statute as OU and OSU with no '
          'published gate found either way — the access rating of 3 is a PROVISIONAL default reflecting the '
          'retrieval failure, not a finding of restriction. The play is one hour on the phone before any routing '
          'decision: start at Events Management via https://www.uco.edu/offices/events (they own the Nigh '
          'University Center spaces, so they will know the external-client tier), then Student Involvement, then '
          'the campus operator. Get four things: Fall 2026 start and finals dates; the solicitation policy; the '
          'Nigh UC tabling rate for external entities; and one working number each for Student Involvement and '
          'Events Management. ⚠ Do not build a route on the inference that UCO starts ~Aug 17 with OSU and NSU — '
          'that is a regional pattern, not a confirmed date, and if it is right the term has ALREADY STARTED.',
  'gaps': ['⚠⚠ EVERYTHING. UCO is presented as verified gaps, not findings. No date, policy, club, faculty member '
           'or phone number was verifiable.',
           '⚠⚠ Fall 2026 start and finals dates — https://www.uco.edu/academic-calendar (403), '
           'https://catalog.uco.edu/content.php?catoid=11&navoid=384 (SSL failure), '
           'https://calendar.uco.edu/academics/all (JavaScript), '
           'https://www.uco.edu/admissions-aid/enrollment-services/priority-enrollment-dates',
           '⚠⚠ The solicitation / outside-vendor policy — https://www.uco.edu/policy/ (403), '
           'https://www.uco.edu/students/dss/campus-events-access (403), '
           'https://www.uco.edu/fin-ops/financial-services/policies',
           '⚠⚠ The Nigh University Center TABLING rate for external entities, and whether external commercial '
           'entities may book the rooms whose rates ARE published — https://www.uco.edu/offices/events/spaces',
           '⚠⚠ One working phone number for Student Involvement and one for Events Management — start at '
           'https://www.uco.edu/offices/events, then the campus operator.',
           '⚠ Involvement fair name, date and outside-org eligibility — "Stampede Week" branding could NOT be '
           'confirmed and must not be printed. https://www.uco.edu/students/involvement/',
           'Whether any blockchain, crypto, finance or CS club exists — UCORE is a JavaScript single-page app. '
           'https://ucore.uco.edu/studentorgs/home/',
           'Any UCO faculty member in blockchain, crypto, fintech, digital assets or monetary economics.',
           'Career fairs, speaker series, hackathons — nothing confirmed. https://calendar.uco.edu/'],
  'note': '⚠ This campus was SEVERELY UNDER-RESEARCHED because of a network/access failure, not because it is '
          'unimportant — ~14,000 students in the OKC metro makes it the third-largest audience in the set. Rank it '
          'only after a phone call.'},

 # ---------------------------------------------------------------- 5. OCU
 {'state': 'Oklahoma',
  'name': 'Oklahoma City University',
  'city': 'Oklahoma City, OK',
  'type': 'Private (religious)',
  'tier': 'C — Opportunistic',
  'access': 2,
  'start': 'Mon Aug 24, 2026 (16-week AND 1st 8-week terms, NON-LAW calendar)',
  'adddrop': 'Final day to add without professor\'s signature, and full tuition-adjustment deadline: Fri Sep 4, '
             '2026. Signature required to drop, 2nd 8-week term: Nov 6.',
  'fallbreak': 'NONE FOUND on the calendar.',
  'thanksgiving': 'Wed–Fri Nov 25–27, 2026 — University closed.',
  'lastclass': 'Fri Dec 11, 2026 (also the final day to drop, 16-week). "Inquiry Day" reading day Mon Dec 14. '
               '2nd 8-week term runs to Dec 18.',
  'finals': '⚠ Dec 15–18, 2026 — THE LATEST FINALS IN THE STATE. OCU is the LAST CAMPUS STILL IN SESSION, which '
            'makes it the only usable late-semester stop. Fall conferral Dec 18; grades due Dec 21; winter break '
            'Dec 22 – Jan 1.',
  'cal_url': 'https://www.okcu.edu/calendar/calendars/academicCalendar',
  'cal_status': 'CONFIRMED (Non-Law, 16-week term). Finals cross-confirmed against the Fall 2026 final exam '
                'schedule PDF: https://okc-university.files.svdcdn.com/production/Academics/Acad-Affairs/'
                '2026-Fall-Final-Exam-Schedule.pdf ⚠ LAW-SCHOOL DATES DIFFER AND ARE NOT COVERED HERE.',
  'fair': 'UNVERIFIED — none found',
  'fair_date': '⚠ UNVERIFIED — no Fall 2026 involvement fair, org fair or welcome-week tabling event was found on '
               'any reachable OCU page, and NO RECURRING PATTERN COULD BE ESTABLISHED. The student handbook '
               'describes the OCU Involved Center as the org hub but names no fair. Where it would post: '
               'https://www.okcu.edu/calendar/ and the Engage portal referenced in the handbook (OCU registers '
               'events through Engage). Call the Office of Student Engagement, (405) 208-5221.',
  'fair_outside': '⚠ NO — effectively barred as a standalone. Per the handbook, a non-university vendor may appear '
                  'ONLY where an OCU department or organization "reserves a room for official OCU use and THE '
                  'SELLING IS SUPPLEMENTAL TO THE EVENT, NOT THE PRIMARY USE," and "THE DEAN OF STUDENTS MUST '
                  'APPROVE ALL NON-UNIVERSITY VENDORS AND CONTRACTORS."',
  'fair_cost': 'Rental rate card NOT PUBLISHED. What IS confirmed: a REFUNDABLE $1,000 DAMAGE DEPOSIT due 15 '
               'business days prior; "a deposit of 1/3 the total rental fee is due upon reserving space"; and a '
               '$50 rental fee for cancellation within 48 hours. University departments and registered student '
               'organizations reserve University Center space at NO CHARGE. Call (405) 208-5000 and ask for the '
               'Dean of Students, Room 257.',
  'fair_deadline': 'Damage deposit due 15 business days prior. External speakers need Dean of Students approval AT '
                   'LEAST ONE WEEK before the speaker is on campus. Demonstrations must be scheduled with the Dean '
                   'at least three school days in advance.',
  'fair_url': 'https://www.okcu.edu/calendar/',
  'policy': 'OCU Student Handbook §X (University Center & Reservations), §IV (University Policies & Procedures) '
            'and §IX (Student Organizations) — MOST RESTRICTIVE REGIME IN THE STATE',
  'policy_url': 'https://www.okcu.edu/current/student-policies/student-handbook/x-university-center-reservations',
  'policy_key': "OCU Student Handbook §X, University Center & Reservations: 'University departments and registered "
                "student organizations may reserve space at the University Center at no charge.' ⚠ THE CLAUSE THAT "
                "CLOSES THE DOOR ON OUTSIDE COMMERCIAL TABLING: 'SOLICITING OR DISTRIBUTING INFORMATION IS ONLY "
                "PERMITTED BY RESERVING A BOOTH OR ROOM AND IS NOT PERMITTED ELSEWHERE.' Non-university vendors "
                "are permitted ONLY when 'the organization or department reserves a room for official OCU use and "
                "THE SELLING IS SUPPLEMENTAL TO THE EVENT, NOT THE PRIMARY USE.' And: 'THE DEAN OF STUDENTS MUST "
                "APPROVE ALL NON-UNIVERSITY VENDORS AND CONTRACTORS.' TABLING CONDUCT: 'Only use the table "
                "assigned to your organization. Only use the table during your requested time period'; 'No "
                "adhesive material is allowed on the walls, pillars, or glass'; 'Posters and/or other "
                "materials... must be confined to the booth area and may not be attached to the wall.' MONEY: a "
                "REFUNDABLE DAMAGE DEPOSIT OF $1,000 due 15 business days prior; 'A DEPOSIT OF 1/3 THE TOTAL "
                "RENTAL FEE IS DUE UPON RESERVING SPACE'; cancellation within 48 hours costs a $50 rental fee; "
                "food/beverage sales require 'Special permission from the Dean of Students.' THE RENTAL RATE CARD "
                "IS NOT PUBLISHED AND NO INSURANCE REQUIREMENT WAS FOUND. §IV, Solicitations & Advertising: "
                "'ON-CAMPUS SOLICITATION IS ONLY ALLOWED WITH THE EXPRESS PERMISSION OF THE DEAN OF STUDENT'S "
                "OFFICE, Room 257 of the McDaniel University Center.' Employment-related solicitation routes to "
                "Career Services (Room 200, Meinders School of Business); religious solicitation to the Director "
                "of Religious Life (Chapel L111). ALL PRINTED MATERIAL MUST BE PRE-APPROVED: 'THE OCU INVOLVED "
                "CENTER, room 114 of the Tom and Brenda McDaniel University Center MUST APPROVE ALL PRINTED "
                "MATERIALS before being posted on campus' — flyers require the Involved Center's APPROVAL STAMP; "
                "nothing on painted, wood, metal or glass surfaces; violators pay for damages. ⚠ THE ANTI-FRONTING "
                "EQUIVALENT AT OCU — SPONSORSHIP DOES NOT CURE IT: 'All students or student organizations inviting "
                "external speakers to appear on-campus with an invitation to the entire campus community or to the "
                "general public MUST OBTAIN PRIOR APPROVAL OF THE DEAN OF STUDENTS or designee AT LEAST ONE WEEK "
                "before the speaker is expected to be at the University.' A student org cannot simply invite DGD "
                "in; Dean of Students approval is required WHETHER THE ORG SPONSORS IT OR NOT. Demonstrations: "
                "'All public demonstrations and rallies must be scheduled with the Dean of Students AT LEAST THREE "
                "SCHOOL DAYS IN ADVANCE.' §IX, Student Organizations, contains only religious-org solicitation "
                "language ('General solicitation of students is limited to specific areas and times that must be "
                "preapproved by the Director of University Church Relations and Religious Life and the Dean of "
                "Students Office'; 'They may not canvass, approach, or visit an entire residence hall or floor') — "
                "NO general fundraising, commercial-activity or outside-group-sponsorship rule for secular orgs is "
                "published, but §IV's Dean-of-Students approval requirement covers it in practice. ⚠ GAPS THAT ARE "
                "NOT PERMISSIONS: NO INSURANCE REQUIREMENT OR LIMIT FOUND; NO EXPLICIT BAN ON FINANCIAL-PRODUCT "
                "MARKETING FOUND; NO LANGUAGE REACHING CREDIT CARDS, PAYMENT APPS OR ON-SITE CONTRACTS FOUND; NO "
                "RENTAL RATE CARD FOUND. OCU IS PRIVATE AND UNITED METHODIST-AFFILIATED — 70 O.S. s 2120 DOES NOT "
                "APPLY AND THERE IS NO FORUM RIGHT AND NO APPEAL.",
  'sponsor_required': '⚠ YES — AND SPONSORSHIP DOES NOT CURE THE PROBLEM. A department or registered org must hold '
                      'the reservation and the selling must be "supplemental to the event, not the primary use"; '
                      'on top of that, "The Dean of Students must approve all non-university vendors and '
                      'contractors," and any external speaker invited by any student or org needs Dean of Students '
                      'approval at least one week out REGARDLESS of who invites them. Two gates, both held by the '
                      'same person: Dr. Levi Harrel, Room 257, reachable only through the main switchboard.',
  'clubs': [('⚠ UNVERIFIED — NO OCU CLUB ROSTER RETRIEVED',
             'No blockchain, crypto, finance, investment, economics, entrepreneurship, ACM or data-science club at '
             'OCU is confirmed. The directory is the Engage portal referenced throughout the handbook and no '
             'enumerable listing could be reached. Orgs must be "registered with the Division of Student Affairs" '
             'and register events through Engage. Look up via the handbook\'s Engage link and call the Involved '
             'Center, (405) 208-5221. DO NOT INVENT NAMES.',
             'https://www.okcu.edu/current/student-policies/student-handbook/ix-student-organizations')],
  'faculty': [('⚠ Office of Student Engagement / OCU Involved Center (Room 114, Tom and Brenda McDaniel '
               'University Center)',
               'BEST DIRECT NUMBER AT OCU. Controls student orgs, the Engage portal, and the REQUIRED PRINTED-'
               'MATERIAL APPROVAL STAMP — no flyer goes up on this campus without them. Start here.',
               'Student Affairs',
               '(405) 208-5221',
               'https://www.okcu.edu/current/student-policies/student-handbook/iv-university-policies-procedures'),
              ('⚠ Dean of Students — Dr. Levi Harrel (Room 257, Tom and Brenda McDaniel University Center)',
               'THE DECISION-MAKER: approves ALL non-university vendors and contractors, ALL on-campus '
               'solicitation, ALL external speakers and ALL demonstrations. ⚠ THE NUMBER BELOW IS THE MAIN '
               'UNIVERSITY LINE, NOT A DIRECT LINE — you must go through the switchboard and ask for the Dean of '
               'Students, Room 257. ⚠ His email is unreadable: OCU handbook pages render staff emails as '
               '[email protected] via Cloudflare JavaScript email protection. USE THE PHONE.',
               'Student Affairs',
               '(405) 208-5000 (MAIN LINE, not direct — ask for Dean of Students, Room 257)',
               'https://www.okcu.edu/current/student-policies/student-handbook/iv-university-policies-procedures'),
              ('Career Services (Room 200, Meinders School of Business)',
               'Employment-related solicitation routes here rather than to the Dean. Reached on the main line.',
               'Career Services',
               '(405) 208-5000 (main line)',
               'https://www.okcu.edu/current/student-policies/student-handbook/iv-university-policies-procedures'),
              ('Director of University Church Relations & Religious Life (Chapel L111)',
               'Religious solicitation gate — not DGD\'s route, but the person who co-approves any solicitation '
               'touching religious orgs. NO NUMBER PUBLISHED — look up here.',
               'Religious Life',
               'no number published — look up here; use (405) 208-5000',
               'https://www.okcu.edu/current/student-policies/student-handbook/ix-student-organizations'),
              ('Registrar',
               'Academic calendar questions, including the separate LAW calendar. Reached on the main line.',
               'Registrar', '405-208-5000 (main line)', 'https://www.okcu.edu/calendar/calendars/academicCalendar'),
              ('Chief Human Resources Officer',
               'One of only two direct extensions confirmed at OCU; carried across for completeness.',
               'Human Resources', '405-208-5075', 'https://www.okcu.edu/'),
              ('OCU main switchboard',
               'MAIN LINE. Almost everything at OCU routes through it — the Dean of Students, Career Services and '
               'the Registrar all publish this number rather than a direct extension.',
               'Oklahoma City University', '(405) 208-5000 (main line)', 'https://www.okcu.edu/'),
              ('(Faculty)',
               'NOT CONFIRMED — no OCU faculty member in blockchain, crypto, fintech, digital assets, monetary '
               'economics or payments could be confirmed. Look up in the Meinders School of Business directory.',
               'Meinders School of Business',
               'no number published — look up here; use (405) 208-5000',
               'https://www.okcu.edu/')],
  'courses': [('(Catalog)',
               'UNVERIFIED — no OCU catalog course on blockchain, crypto, fintech or digital money confirmed. '
               'Look up here.',
               'https://www.okcu.edu/academics/course-schedule')],
  'events': [('(All events)',
              'UNVERIFIED — no career fair, entrepreneurship week, speaker series or hackathon confirmed at OCU. '
              'Look up here.',
              'https://www.okcu.edu/calendar/'),
             ('⚠ PDF student handbooks — the likeliest source of direct extensions',
              'The AY25-26 handbook PDF download was BLOCKED AT THE PROXY (CONNECT tunnel failed, 403). These PDFs '
              'are the most likely place OCU prints direct extensions — retrieve manually. AY24-25 mirror: '
              'https://okc-university.files.svdcdn.com/production/Campus-Life/OCU-Student-Handbook-24-25.pdf',
              'https://okc-university.files.svdcdn.com/production/Campus-Life/Student-Handbook-AY25-26.pdf')],
  'play': 'Skip OCU unless you are already in Oklahoma City for something else — and if you go, go in December. '
          'This is the most restrictive regime in the state attached to the smallest audience in it: ~2,600 '
          'students, heavily weighted to performing arts, with a law school on a separate calendar and a small '
          'undergraduate business and CS population. The written rule is flat — "Soliciting or distributing '
          'information is only permitted by reserving a booth or room and is not permitted elsewhere" — a '
          'non-university vendor may appear only where an OCU department already holds the room and the selling is '
          '"supplemental to the event, not the primary use," and the Dean of Students must personally approve all '
          'non-university vendors, all solicitation, all external speakers (one week out, no matter who invites '
          'them) and all demonstrations. Even a flyer needs the Involved Center\'s approval stamp. Add a $1,000 '
          'refundable damage deposit and a third of the rental up front against a rate card nobody publishes, and '
          'the cost-per-conversation is the worst in Oklahoma. There is exactly one reason to keep it on the list: '
          'OCU runs LATEST — classes through Dec 11, finals Dec 15–18 — so it is the only campus still in session '
          'when everyone else has gone home, and OSU has been shut since Nov 23. If you use it, do not try to '
          'table. Call the Office of Student Engagement at (405) 208-5221 first (they are also the printed-material '
          'gate), then ask the switchboard, (405) 208-5000, for Dr. Levi Harrel, Dean of Students, Room 257, and '
          'ask for one thing: to be an invited speaker at an event a department already owns. Note both offices '
          'publish only the main line, and every staff email on the handbook pages is Cloudflare-obfuscated — this '
          'is a phone campus.',
  'gaps': ['⚠ Any involvement fair at all — none found, no recurring pattern established. (405) 208-5221.',
           '⚠ OCU rental rate card — the $1,000 damage deposit, the 1/3-rental deposit and the $50 '
           'late-cancellation fee are confirmed; THE BASE RENTAL RATES ARE NOT PUBLISHED. (405) 208-5000, ask for '
           'the Dean of Students, Room 257.',
           'No insurance requirement or limit found; no explicit ban on financial-product marketing found; no '
           'language reaching credit cards, payment apps or on-site contracts found. Absence is not permission at '
           'a private religious institution.',
           'Club roster — the Engage portal could not be enumerated. No blockchain, crypto, finance, investment, '
           'economics, entrepreneurship, ACM or data-science club is confirmed. (405) 208-5221.',
           'Any OCU faculty member in blockchain, crypto, fintech, digital assets or monetary economics.',
           'Career fairs, speaker series, hackathons — nothing confirmed. https://www.okcu.edu/calendar/',
           '⚠ Direct phone extensions — the AY25-26 handbook PDF, the likeliest source, was BLOCKED AT THE PROXY '
           '(403). Retrieve manually: '
           'https://okc-university.files.svdcdn.com/production/Campus-Life/Student-Handbook-AY25-26.pdf',
           'Staff emails are Cloudflare-obfuscated ([email protected]) across the handbook, including Dr. Levi '
           'Harrel\'s and the Student Engagement inbox. Use the phone numbers.',
           'Catalog courses — https://www.okcu.edu/academics/course-schedule'],
  'note': '⚠ PRIVATE, UNITED METHODIST-AFFILIATED, ~2,600 students — the smallest campus in the set, with strong '
          'performing arts (Bass School of Music) and a law school. LAW STUDENTS RUN ON A SEPARATE "LAW" CALENDAR; '
          'every date in this record is the NON-LAW calendar. Weight the small undergraduate business/CS '
          'population accordingly.'},

 # ---------------------------------------------------------------- 6. NSU
 {'state': 'Oklahoma',
  'name': 'Northeastern State University',
  'city': 'Tahlequah, OK',
  'type': 'Public',
  'tier': 'C — Opportunistic',
  'access': 4,
  'start': '⚠ Mon Aug 17, 2026 (all formats) — same week as OSU, a week ahead of OU/TU/OCU.',
  'adddrop': '⚠ DIFFERS BY TRACK — NSU runs 16-week, two 8-week and two 7-week formats concurrently, the only '
             'multi-track structure in the set. Last day to add: 16-week and 1st 8-week Fri Aug 21; 1st 7-week '
             'Tue Aug 18. End of 1st 7-week Oct 2; end of 1st 8-week Oct 9; end of 2nd 7-week Dec 4.',
  'fallbreak': 'Thu–Fri Oct 15–16, 2026 — CAMPUSES CLOSED. ⚠ Identical to TU\'s fall break; that week knocks out '
               'Tulsa and Tahlequah simultaneously.',
  'thanksgiving': 'Wed–Fri Nov 25–27, 2026 — campuses closed.',
  'lastclass': 'Fri Dec 11, 2026 (end of 16-week format). Usable Tahlequah window: Aug 17 – Nov 24.',
  'finals': '⚠ Dec 7–11, 2026 (16-week) — INTERNAL INCONSISTENCY: NSU\'s own page gives finals as Dec 7–11 AND the '
            '16-week format ending Dec 11, i.e. finals week appears to overlap or immediately follow the last '
            'teaching week with no gap. CONFIRM WITH THE REGISTRAR which days are instruction and which are exams '
            'before scheduling Dec 7–11.',
  'cal_url': 'https://nsuok.edu/academics/CourseSchedules/Fall/AcademicCalendar.aspx',
  'cal_status': 'CONFIRMED on NSU\'s Fall 2026 semester-dates page, with the Dec 7–11 overlap flagged above as an '
                'internal inconsistency to verify.',
  'fair': 'UNVERIFIED — none found',
  'fair_date': '⚠ UNVERIFIED — no Fall 2026 involvement fair, org fair or welcome-week tabling event was found on '
               'any NSU page, and NO RECURRING PATTERN COULD BE ESTABLISHED. The Office of Student Engagement and '
               'Transitions describes itself as "a one stop shop to a wide variety of involvement and leadership '
               'opportunities" coordinating "over 100 student organizations" but publishes no fair. Where it would '
               'post: https://offices.nsuok.edu/engagement/StudentEngagement/default.aspx and the HawkLife portal. '
               'Call Student Engagement, Tahlequah: 918-444-2526.',
  'fair_outside': 'LIKELY YES ON PAPER, TERMS UNDEFINED — NSU\'s written posture is the most even-handed in the '
                  'state: "NON-UNIVERSITY PERSONNEL AND ORGANIZATIONS MUST MAKE THEIR REQUESTS IN THE SAME MANNER '
                  'AS UNIVERSITY STUDENTS, PERSONNEL OR ORGANIZATIONS." But advance reservation with the Student '
                  'Affairs AVP is required 5 business days out for anything promoted, org-sponsored or expected to '
                  'draw 25+, and NO tabling fee is published. Openness is real but undocumented — 918-444-2526.',
  'fair_cost': 'NO PUBLISHED TABLING FEE — a genuine gap, not a finding of "free." The $1,000,000/$2,000,000 '
               'insurance requirement and the half-the-fee deposit belong to the CONFERENCE RENTAL regime, not '
               'necessarily to a table. Confirm at 918-444-2526 and 918-444-2500.',
  'fair_deadline': 'Expressive-activity reservation requests "must be made at least FIVE BUSINESS DAYS in advance '
                   'of the event," by email to the Student Affairs Assistant Vice President (selfsj@nsuok.edu). '
                   'Poster/flier approval from Student Affairs is required BEFORE anything is posted. For '
                   'conference rentals: half the fee on contract signing, full balance 30 days before the event.',
  'fair_url': 'https://offices.nsuok.edu/engagement/StudentEngagement/default.aspx',
  'policy': 'NSU Student Handbook — Student Administrative Services; Campus Space Reservations for Student '
            'Organizations; Conferences and Events Policies (the paid-rental regime)',
  'policy_url': 'https://offices.nsuok.edu/studentaffairs/StudentServices/ConductandDevelopment/Handbook/'
                'AdministrativeServices.aspx',
  'policy_key': "NSU Campus Space Reservations for Student Organizations — THE MOST OUTSIDE-FRIENDLY SENTENCE IN "
                "THE OKLAHOMA DATASET, verbatim: 'NON-UNIVERSITY PERSONNEL AND ORGANIZATIONS MUST MAKE THEIR "
                "REQUESTS IN THE SAME MANNER AS UNIVERSITY STUDENTS, PERSONNEL OR ORGANIZATIONS.' NSU reserves "
                "authority to 'designate places for non-university persons to conduct activities so that it does "
                "not interfere with normal campus business.' ⚠ BUT APPROVAL IS REQUIRED WHETHER SPONSORED OR NOT — "
                "Student Handbook, Student Administrative Services: 'ADVANCE RESERVATION FOR EXPRESSIVE ACTIVITY "
                "IS REQUIRED (in the form of an email to the Student Affairs Assistant Vice President, "
                "<selfsj@nsuok.edu>) for events or activities that are PROMOTED IN ADVANCE, AND/OR SPONSORED BY "
                "STUDENT ORGANIZATIONS, AND/OR EXPECTED TO DRAW A CROWD OF MORE THAN 25 PEOPLE'; 'requests must be "
                "made at least FIVE BUSINESS DAYS IN ADVANCE of the event.' READ THAT TRIGGER CAREFULLY: IT IS "
                "DISJUNCTIVE. A promoted DGD table trips clause (a) regardless of sponsorship, and student-org "
                "sponsorship independently trips clause (b). SPONSORSHIP DOES NOT CURE THE REQUIREMENT — IT "
                "TRIGGERS IT. Scheduling offices: University Center (Tahlequah); Administration Building (Broken "
                "Arrow); Administration Building (Muskogee). POSTING: 'ALL POSTERS, INCLUDING SIGNS, FLIERS, "
                "HANDOUTS, ETC., MUST HAVE PRIOR APPROVAL FROM STUDENT AFFAIRS before they are placed on or about "
                "the campus of Northeastern State University.' ORG CONSEQUENCES: 'Any recognized student "
                "organization conducting activities that are not properly registered with the Division of Student "
                "Affairs is considered to be in violation' — consequences 'may include RELINQUISHING RECOGNITION "
                "STATUS ON CAMPUS.' CONFERENCES AND EVENTS POLICIES (the paid-rental regime for non-university "
                "events, offices.nsuok.edu/conferences/Policies.aspx) — INSURANCE: 'Comprehensive general "
                "liability insurance in the amounts of $1,000,000 PER OCCURRENCE / $2,000,000 AGGREGATE for "
                "non-University events,' with NSU named ADDITIONAL INSURED and certificate holder at Northeastern "
                "State University, 601 N. Grand Avenue, Tahlequah, OK 74464; ⚠ IF MINORS UNDER 18 ATTEND, A "
                "SEXUAL-MOLESTATION COVERAGE ENDORSEMENT IS REQUIRED (relevant if DGD sponsors anything touching "
                "high-school outreach). DEPOSITS AND CANCELLATION: HALF THE RENTAL FEE IS THE DEPOSIT, due on "
                "contract signing; FULL BALANCE DUE 30 DAYS BEFORE THE EVENT; cancellation more than 30 days out "
                "= full refund, WITHIN 30 DAYS = DEPOSIT FORFEITED, and must be in writing. VENDOR EXCLUSIVITY: "
                "'SODEXO CAMPUS DINING MUST SUPPLY ALL FOOD SERVICE'; alcohol only in the Banquet Hall through "
                "Sodexo; no outside caterers, security or equipment vendors without prior approval and cost "
                "authorization. ⚠ GAPS THAT ARE NOT PERMISSIONS: NO PUBLISHED TABLING FEE, NO INSURANCE "
                "REQUIREMENT FOR A TABLE (the $1M/$2M figure attaches to conference rentals), NO ANTI-FRONTING "
                "CLAUSE ANYWHERE AT NSU, NO SPONSORSHIP REQUIREMENT, AND NO LANGUAGE REACHING CREDIT CARDS, "
                "PAYMENT APPS OR ON-SITE CONTRACTS. The Student Engagement handbook section contains NO rules on "
                "outside groups, sponsorship, solicitation, fundraising or commercial activity at all — only "
                "'University recognition in no way implies that Northeastern State University condones or supports "
                "any or all activities of a registered student organization.' NSU IS PUBLIC, so 70 O.S. s 2120 "
                "binds it — and its NONCOMMERCIAL carve-out applies against DGD exactly as at OU and OSU.",
  'sponsor_required': '⚠ NO — AND SPONSORSHIP MAKES IT WORSE, NOT BETTER. The reservation trigger is disjunctive: '
                      'advance promotion OR student-org sponsorship OR an expected crowd over 25 each '
                      'independently requires an email to the Student Affairs AVP five business days out. Routing '
                      'through a club buys nothing and adds a trigger. Go direct: email selfsj@nsuok.edu and call '
                      '918-444-2120. No anti-fronting clause exists at NSU, but there is nothing to front around.',
  'clubs': [('⚠ UNVERIFIED — NO NSU CLUB IS CONFIRMED',
             'No blockchain, crypto, finance, investment, economics, entrepreneurship, ACM or data-science club at '
             'NSU is confirmed. The directory is HawkLife, a third-party Suitable-platform portal, NOT ENUMERABLE '
             'by research tooling. ~80–100 orgs claimed (NSU\'s two pages say "over 80" and "over 100" — '
             'inconsistent). Student government: nsga@nsuok.edu. Activities board: nab@nsuok.edu. DO NOT INVENT '
             'OFFICER NAMES. Call 918-444-2526.',
             'https://app.suitable.co/orgs/JjKz28CjYygB'),
            ('College of Education organizations',
             'Separately listed and NOT RELEVANT to DGD — noted only so an ambassador does not mistake this list '
             'for the general org roster.',
             'https://coe.nsuok.edu/studentresources/StudentOrganizations.aspx')],
  'faculty': [('⚠ Office of Student Engagement and Transitions (University Center, B01, Tahlequah)',
               'BEST FIRST CALL AT NSU. Student orgs, HawkLife, involvement programming — and the office that can '
               'say whether an involvement fair exists at all. Same number serves the Student Activities office.',
               'Student Engagement',
               'engagement@nsuok.edu · 918-444-2526',
               'https://offices.nsuok.edu/engagement/StudentEngagement/default.aspx'),
              ('⚠ Student Affairs (2nd floor Administration Building, 701 N. Grand Ave., Tahlequah OK 74464-2300)',
               'POSTER APPROVAL and EXPRESSIVE-ACTIVITY RESERVATIONS — this office houses the Assistant Vice '
               'President who must receive every reservation request five business days out. Fax 918-458-2340.',
               'Student Affairs',
               'studentaffairs@nsuok.edu · 918-444-2120',
               'https://offices.nsuok.edu/studentaffairs/ContactUs.aspx'),
              ('⚠ Student Affairs Assistant Vice President',
               'RECEIVES ALL EXPRESSIVE-ACTIVITY RESERVATION REQUESTS — the single decision-maker for a DGD table. '
               '⚠ THE PERSON\'S NAME IS NOT PUBLISHED ANYWHERE ON THE HANDBOOK PAGE. Call Student Affairs and ask '
               'for the AVP by role. No direct number published — look up here.',
               'Student Affairs',
               'selfsj@nsuok.edu · no number published — look up here; ask by role at 918-444-2120',
               'https://offices.nsuok.edu/studentaffairs/StudentServices/ConductandDevelopment/Handbook/'
               'AdministrativeServices.aspx'),
              ('Student Affairs / Student Engagement — Broken Arrow (3100 E. New Orleans, Broken Arrow OK '
               '74014-3501, 2nd floor Administration Building / Administrative Services Bldg 211)',
               'The Broken Arrow campus is largely COMMUTER / UPPER-DIVISION — Tahlequah is the only residential '
               'campus worth a stop. Fax 918-449-6190.',
               'Student Affairs',
               'studentaffairsba@nsuok.edu · 918-449-6136',
               'https://offices.nsuok.edu/studentaffairs/ContactUs.aspx'),
              ('⚠ Auxiliary Services',
               'CONFERENCE AND EVENT RENTALS — the paid route, and the office behind the $1M/$2M insurance '
               'requirement, the half-fee deposit and the 30-day cancellation rule.',
               'Auxiliary Services', '918-444-2500',
               'https://offices.nsuok.edu/studentaffairs/auxiliaryservices.aspx'),
              ('Kirsti Cook',
               'Conferences and events, TAHLEQUAH — University Center, 612 North Grand Avenue, Tahlequah OK 74464. '
               'NO DIRECT PHONE PUBLISHED — look up here; use Auxiliary Services or Student Affairs.',
               'Conferences and Events',
               'cookk@nsuok.edu · no number published — look up here; use 918-444-2500',
               'https://offices.nsuok.edu/conferences/Policies.aspx'),
              ('Jacki Adair',
               'Conferences and events, BROKEN ARROW — Administrative Services Building, 3100 E. New Orleans, '
               'Broken Arrow OK 74014. NO DIRECT PHONE PUBLISHED — look up here.',
               'Conferences and Events',
               'adairsmi@nsuok.edu · no number published — look up here; use 918-444-2500',
               'https://offices.nsuok.edu/conferences/Policies.aspx'),
              ('Academic Affairs', 'Departmental main line.', 'Academic Affairs', '918-444-2060',
               'https://offices.nsuok.edu/studentaffairs/ContactUs.aspx'),
              ('College of Liberal Arts', 'Departmental main line.', 'College of Liberal Arts', '918-444-3600',
               'https://offices.nsuok.edu/studentaffairs/ContactUs.aspx'),
              ('Housing Office', 'Departmental main line.', 'Housing', '918-444-4700',
               'https://offices.nsuok.edu/studentaffairs/ContactUs.aspx'),
              ('Athletics', 'Departmental main line.', 'Athletics', '918-444-3900',
               'https://offices.nsuok.edu/studentaffairs/ContactUs.aspx'),
              ('Fitness Center', 'Departmental main line.', 'Fitness Center', '918-444-3980',
               'https://offices.nsuok.edu/studentaffairs/ContactUs.aspx'),
              ('Sodexo Catering — Tahlequah', 'REQUIRED CATERER: "Sodexo Campus dining must supply all food '
               'service." Alcohol only in the Banquet Hall through Sodexo.', 'Dining Services', '918-444-2550',
               'https://offices.nsuok.edu/conferences/Policies.aspx'),
              ('Sodexo Catering — Broken Arrow', 'Required caterer, BA campus.', 'Dining Services', '918-449-6293',
               'https://offices.nsuok.edu/conferences/Policies.aspx'),
              ('(Faculty)',
               'NOT CONFIRMED — no NSU faculty member working on blockchain, crypto, fintech, digital assets, '
               'monetary economics or payments could be confirmed. ⚠ directory.nsuok.edu DOES NOT RESOLVE (DNS '
               'failure) — there is no reachable people-search, and NSU publishes department numbers freely but '
               'almost no individual direct lines. Look up in the College of Business and Technology directory.',
               'College of Business and Technology',
               'no number published — look up here; use 918-444-2060',
               'https://nsuok.edu/')],
  'courses': [('(For-credit)',
               'NO for-credit blockchain / crypto / fintech course confirmed at NSU. Look up here.',
               'https://nsuok.edu/academics/CourseSchedules/Fall/default.aspx'),
              ('A Manager\'s Guide to Blockchain (non-credit) — ⚠ DEAD',
               'NSU Continuing Education: online, open enrollment, 90 days, ~3 hours, 0.3 CEUs, $99.00. THE PAGE '
               'STATES: "This course is no longer being offered." Do not pitch against it. Continuing Ed contact '
               'page (no phone published on the course page): '
               'https://academics.nsuok.edu/continuingeducation/ContactUs.aspx',
               'https://academics.nsuok.edu/continuingeducation/Courses/AManagersGuidetoBlockchain.aspx')],
  'events': [('(All events)',
              'UNVERIFIED — no career fair, startup week, speaker series or hackathon confirmed at NSU. '
              'Call 918-444-2526.',
              'https://offices.nsuok.edu/engagement/StudentEngagement/default.aspx')],
  'play': 'If the tour has to cut one Oklahoma stop, cut this one — NSU is priority six for a reason. It is a '
          'regional teaching university of ~6,500 spread across three sites, with an optometry college and a large '
          'education and health-professions population; the business and CS cohorts are small relative to OU and '
          'OSU, Broken Arrow is largely commuter and upper-division, and Tahlequah is the only residential campus '
          'worth a visit. Nothing is confirmed on the ground: no involvement fair, no club of any kind, no career '
          'fair, no faculty match, and the one blockchain offering NSU ever had — a $99 non-credit Continuing Ed '
          'course — is marked "no longer being offered." What makes it worth a phone call rather than a drive is '
          'that NSU has the most permissive written text in the state: "non-university personnel and organizations '
          'must make their requests in the same manner as university students, personnel or organizations," with '
          'no anti-fronting clause, no sponsorship requirement, and no published tabling fee anywhere. That is '
          'real openness, entirely undocumented — which is exactly why it needs a call before it needs a visit. '
          'Two numbers: 918-444-2526 (Student Engagement — ask whether an involvement fair exists and what a table '
          'costs) and 918-444-2120 (Student Affairs — ask for the Assistant Vice President by role, because the '
          'name behind selfsj@nsuok.edu is not published, and that person must receive your reservation request '
          'FIVE BUSINESS DAYS out). Do not route through a student org: the reservation trigger is disjunctive, so '
          'org sponsorship independently triggers the approval it was supposed to avoid. ⚠ TIMING: NSU already '
          'started (Aug 17), the usable window is Aug 17 – Nov 24, and fall break Oct 15–16 is identical to TU\'s '
          '— do not plan a Tulsa/Tahlequah swing that week. ⚠ Also confirm the finals dates with the Registrar: '
          'NSU\'s own page shows finals Dec 7–11 AND the 16-week term ending Dec 11.',
  'gaps': ['⚠ Whether an involvement fair exists at all, and its date — nothing found, no pattern establishable. '
           '918-444-2526.',
           '⚠ NSU tabling terms — the parity clause is confirmed, but NO tabling fee, NO insurance requirement for '
           'a table (the $1M/$2M figure applies to conference rentals) and NO sponsorship requirement are '
           'published. 918-444-2526 and 918-444-2500.',
           '⚠ The name behind selfsj@nsuok.edu — the Student Affairs Assistant Vice President who must approve all '
           'expressive activity. Ask by role at 918-444-2120.',
           '⚠ Finals-week inconsistency — NSU\'s page gives finals Dec 7–11 AND the 16-week format ending Dec 11. '
           'Confirm with the Registrar which days are instruction and which are exams.',
           'Club roster — HawkLife (app.suitable.co/orgs/JjKz28CjYygB) is a third-party Suitable portal and was '
           'not enumerable. No blockchain, crypto, finance, investment, economics, entrepreneurship, ACM or '
           'data-science club is confirmed. 918-444-2526.',
           'Any NSU faculty member in blockchain, crypto, fintech, digital assets or monetary economics — '
           'directory.nsuok.edu DOES NOT RESOLVE (DNS failure), so there is no people-search.',
           'Direct phone numbers for Kirsti Cook and Jacki Adair (conferences/events) — email only.',
           'Career fairs, speaker series, hackathons — nothing confirmed.',
           'For-credit course offerings — https://nsuok.edu/academics/CourseSchedules/Fall/default.aspx'],
  'note': '⚠ THREE CAMPUSES: Tahlequah (main, residential — the only one worth a stop), Broken Arrow (largely '
          'commuter / upper-division) and Muskogee. ~6,500 students total. AUDIENCE MISMATCH TO WATCH: a regional '
          'teaching university with an optometry college and a large education / health-professions population; '
          'the business and CS cohorts are small. Also the ONLY multi-track campus in the set — 16-week, two '
          '8-week and two 7-week formats run concurrently and add/drop dates differ by track.'},
]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; sorts last.
DEADLINES = [

 ('2026-08-12', 'Aug 12, 2026', 'Oklahoma State',
  'Cowboy Welcome opens (Aug 12–22) — SUAB Night, 6–9pm, Student Union',
  'The Involvement Fair sits inside this window on Aug 13. Rock the Block Aug 14, 5–7pm, Colvin Recreation '
  'Center; Xposed Aug 15, 6–9pm, Student Union North Plaza; Late Night Cafe Aug 15, 8:30–10:30pm; Cowboy Kickoff '
  'Aug 16, 6:30–7:30pm, Gallagher-Iba Arena; Class Photo Aug 16, gates 7:30pm, Boone Pickens Stadium.',
  'https://campuslife.okstate.edu/cowboy-welcome',
  'campuslife@okstate.edu · (405) 744-5488'),

 ('2026-08-13', 'Aug 13, 2026', 'Oklahoma State',
  '⚠⚠ FALL 2026 INVOLVEMENT FAIR — 3:30–5:30pm, Student Union 2nd Floor. TOMORROW.',
  '400–500+ student organizations, 110 S Hester Street, Stillwater. Four days before classes begin. Outside-vendor '
  'eligibility AT THIS FAIR is not published — the purchasable route is a $250/semester solicitation permit plus '
  '$400 per table per day from Meeting & Conference Services. Ask both offices TODAY, and ask how a '
  'non-affiliated vendor satisfies the outdoor "valid OSU ID" check-in rule.',
  'https://events.okstate.edu/event/fall-2026-involvement-fair',
  'Alex Comer · roo.comer@okstate.edu · (405) 744-5785 | permit: meetings@okstate.edu · (405) 744-5232'),

 ('2026-08-17', 'Aug 17, 2026', 'Oklahoma State',
  'Classes begin — EARLIEST START IN THE STATE',
  'A full week ahead of OU, TU and OCU. OSU also ends first: last class Dec 4.',
  'https://registrar.okstate.edu/academic_calendar/academic-calendar-fall-2026',
  '(405) 744-5000'),

 ('2026-08-17', 'Aug 17, 2026', 'Northeastern State',
  'Classes begin (all formats — 16-week, two 8-week, two 7-week)',
  'Usable Tahlequah window is Aug 17 – Nov 24. Last day to add: 16-week and 1st 8-week Aug 21; 1st 7-week Aug 18.',
  'https://nsuok.edu/academics/CourseSchedules/Fall/AcademicCalendar.aspx',
  'engagement@nsuok.edu · 918-444-2526'),

 ('2026-08-21', 'Aug 21, 2026', 'Northeastern State',
  'Last day to add — 16-week and 1st 8-week formats',
  'Add/drop dates differ by track at NSU; the 1st 7-week deadline was Aug 18.',
  'https://nsuok.edu/academics/CourseSchedules/Fall/AcademicCalendar.aspx',
  '918-444-2120'),

 ('2026-08-22', 'Aug 22, 2026', 'U of Oklahoma',
  '⚠ SOVALPALOOZA INVOLVEMENT FAIR — 7–9pm, The South Oval',
  'OU\'s only CONFIRMED involvement fair, two days before classes start, inside Welcome Week (Aug 22–29). The page '
  'says "all guests are welcome" — that is an ATTENDANCE statement, NOT tabling permission. A separately titled '
  '"Fall Involvement Fair (Presented by Howdy Week & Camp Crimson)" exists on OU Engage and calendar.ou.edu with '
  'NO retrievable date (both JavaScript-rendered; the OU Daily mirror returned HTTP 429). Call to find out whether '
  'that is one event or two, and whether a paid outside table is possible at either.',
  'https://ou.edu/sga/cac/welcome-week/schedule',
  'K. George Ahmadi · kga@ou.edu · (405) 325-5471 | Student Life · (405) 325-3163'),

 ('2026-08-24', 'Aug 24, 2026', 'U of Oklahoma',
  'Classes begin — ⚠ OU HAS NO FALL BREAK AT ALL',
  'Norman runs at full density from Aug 24 straight through Nov 24 — the best sustained access window in the '
  'state. Thanksgiving Nov 25–29; last class Dec 11; finals Dec 14–18.',
  'https://www.ou.edu/registrar/academic-records/academic-calendars/fall-2026-academic-calendar',
  '(405) 325-3163'),

 ('2026-08-24', 'Aug 24, 2026', 'U of Tulsa',
  'Classes begin',
  'Private university — no forum right, no statute, no appeal. Fall break Oct 15–16; a FULL five-day Thanksgiving '
  'week Nov 23–27; last class Dec 8; finals Dec 11 then Dec 14–18.',
  'https://utulsa.edu/academics/academic-calendar/',
  'eventhelp@utulsa.edu · 918-631-3211'),

 ('2026-08-24', 'Aug 24, 2026', 'Oklahoma City U',
  'Classes begin (16-week and 1st 8-week, NON-LAW calendar)',
  'Law students run on a separate calendar not covered here. No fall break found.',
  'https://www.okcu.edu/calendar/calendars/academicCalendar',
  '(405) 208-5000'),

 ('2026-08-25', 'Aug 25, 2026', 'Oklahoma State',
  'Part-Time Job Fair — 11am–2pm, Student Union Ballroom, 2nd floor Rm 265',
  'First of six confirmed Fall 2026 OSU career fairs. Employer registration is open with early-bird pricing, but '
  'SPECIFIC FEES AND DEADLINES ARE NOT PUBLISHED — call Career Services.',
  'https://events.okstate.edu/event/part-time-job-fair-1107',
  'careers@okstate.edu · (405) 744-5253'),

 ('2026-08-27', 'Aug 27, 2026', 'U of Tulsa',
  '⚠ ACTIVITY & RESOURCE FAIR — INFERRED, NOT CONFIRMED',
  'TU publishes only: "On the first Thursday of each semester, SA sponsors an Activity & Resource Fair." Classes '
  'begin Aug 24, so the first Thursday is Aug 27. THIS IS AN INFERENCE. It will post at calendar.utulsa.edu (use '
  'MONTH view — the default view surfaced only Aug 11–15) and in the SA Student Hub, which is SharePoint and '
  'login-gated. Confirm by phone before driving.',
  'https://utulsa.edu/about/offices/student-activities/',
  'eventhelp@utulsa.edu · 918-631-3211'),

 ('2026-08-28', 'Aug 28, 2026', 'U of Oklahoma',
  'Final day to register/add without instructor permission',
  '100% charge-reduction window runs Aug 24 – Sep 8; automatic W grades begin Sep 9.',
  'https://www.ou.edu/registrar/academic-records/academic-calendars/fall-2026-academic-calendar',
  '(405) 325-3163'),

 ('2026-09-04', 'Sep 4, 2026', 'Oklahoma City U',
  'Final day to add without professor\'s signature; full tuition-adjustment deadline',
  'Non-Law calendar.',
  'https://www.okcu.edu/calendar/calendars/academicCalendar',
  '(405) 208-5000'),

 ('2026-09-11', 'Sep 11, 2026', 'U of Tulsa',
  'Last day to drop without a W',
  'Last day to add via Self-Service was Aug 28; through advising, Sep 1.',
  'https://utulsa.edu/academics/academic-calendar/',
  '918-631-3211'),

 ('2026-09-15', 'Sep 15, 2026', 'Oklahoma State',
  'CEAT (Engineering / Architecture / Technology) Career Fair — 9am–3:30pm',
  'The engineering-side audience; Hack OKState students overlap heavily with it. Registration fees and deadlines '
  'not published.',
  'https://careerservices.okstate.edu/',
  'careers@okstate.edu · (405) 744-5253'),

 ('2026-09-16', 'Sep 16, 2026', 'Oklahoma State',
  '⚠ BUSINESS CAREER FAIR — 11:30am–4pm. BEST-FIT OSU FAIR.',
  'The Spears School audience — FMA, Spearhead Scholars, Economics Society and the Free Enterprise Society all sit '
  'here. Registration fees and deadlines are NOT published; call for both.',
  'https://careerservices.okstate.edu/',
  'careers@okstate.edu · (405) 744-5253'),

 ('2026-09-17', 'Sep 17, 2026', 'Oklahoma State',
  'Ag, Food & Natural Resources Career Fair — 11:30am–4:30pm',
  'Third of three consecutive fair days at OSU (Sep 15, 16, 17).',
  'https://careerservices.okstate.edu/',
  'careers@okstate.edu · (405) 744-5253'),

 ('2026-09-30', 'Sep 30, 2026', 'Oklahoma State',
  'OSU-Tulsa Career Fair — 1:30–3:30pm, Main Hall Commons',
  '⚠ OSU-Tulsa is a separate site from Stillwater; do not apply Stillwater dates to it. Pairs naturally with a TU '
  'visit the same week.',
  'https://events.okstate.edu/event/osu-tulsa-career-fair-3422',
  'careers@okstate.edu · (405) 744-5253'),

 ('2026-10-06', 'Oct 6, 2026', 'Oklahoma State',
  'Construction Industry Career Fair — 9:30am–12pm',
  'Last of the six confirmed OSU fall career fairs.',
  'https://careerservices.okstate.edu/',
  'careers@okstate.edu · (405) 744-5253'),

 ('2026-10-15', 'Oct 15–16, 2026', 'Tulsa / Northeastern State',
  '⚠ FALL BREAK AT BOTH CAMPUSES — DO NOT ROUTE TULSA/TAHLEQUAH THIS WEEK',
  'TU and NSU take identical Oct 15–16 breaks; NSU campuses are CLOSED. OU has no fall break at all, and OSU\'s is '
  'in November — Norman and Stillwater are live this week.',
  'https://utulsa.edu/academics/academic-calendar/',
  'TU 918-631-3211 · NSU 918-444-2526'),

 ('2026-11-06', 'Nov 6, 2026', 'Oklahoma State',
  'W drop/withdrawal deadline',
  'Assigned W or F drop/withdrawal deadline follows Nov 30 — after the campus has effectively emptied.',
  'https://registrar.okstate.edu/academic_calendar/academic-calendar-fall-2026',
  '(405) 744-5000'),

 ('2026-11-20', 'Nov 20, 2026', 'Oklahoma State',
  '⚠ LAST USABLE DAY IN STILLWATER',
  'Fall break and Thanksgiving merge into a five-day closure Nov 23–27, and the last day of classes is Dec 4. '
  'ANYTHING SCHEDULED AT OSU AFTER ABOUT NOV 20 IS WORTHLESS.',
  'https://registrar.okstate.edu/academic_calendar/academic-calendar-fall-2026',
  '(405) 744-5488'),

 ('2026-11-23', 'Nov 23–27, 2026', 'Oklahoma State',
  'Fall Break (Nov 23–25) + Thanksgiving (Nov 26–27) — ONE FIVE-DAY DEAD ZONE',
  'The only campus in the set that merges the two.',
  'https://registrar.okstate.edu/academic_calendar/academic-calendar-fall-2026',
  '(405) 744-5000'),

 ('2026-11-24', 'Nov 24, 2026', 'U of Oklahoma',
  'Last full-density day in Norman before Thanksgiving (Nov 25–29)',
  'With no fall break, OU delivers 13 uninterrupted weeks Aug 24 – Nov 24. Classes resume Nov 30 and run to '
  'Dec 11.',
  'https://www.ou.edu/registrar/academic-records/academic-calendars/fall-2026-academic-calendar',
  '(405) 325-3163'),

 ('2026-12-04', 'Dec 4, 2026', 'Oklahoma State',
  'Last day of classes — OSU IS DONE FIRST',
  'A full week before OU, NSU and OCU. Finals Dec 7–11; graduate commencement Dec 11, undergraduate Dec 12.',
  'https://registrar.okstate.edu/academic_calendar/academic-calendar-fall-2026',
  '(405) 744-5000'),

 ('2026-12-11', 'Dec 11, 2026', 'OU / NSU / OCU',
  'Last day of classes at three campuses',
  'OU finals Dec 14–18 (commencement Dec 19). NSU 16-week format ends Dec 11 — ⚠ but NSU\'s page ALSO gives finals '
  'as Dec 7–11; confirm with the Registrar which days are instruction. OCU classes end Dec 11 with "Inquiry Day" '
  'reading day Dec 14.',
  'https://www.ou.edu/registrar/academic-records/academic-calendars/fall-2026-academic-calendar',
  'OU (405) 325-3163 · NSU 918-444-2120 · OCU (405) 208-5000'),

 ('2026-12-15', 'Dec 15–18, 2026', 'Oklahoma City U',
  '⚠ FINALS — THE LAST CAMPUS IN THE STATE STILL IN SESSION',
  'OCU runs latest by a week. If a December stop is needed, this is the only one available — OSU has been shut '
  'since Nov 23. Fall conferral Dec 18; grades due Dec 21; university closed Dec 22 – Jan 1.',
  'https://okc-university.files.svdcdn.com/production/Academics/Acad-Affairs/2026-Fall-Final-Exam-Schedule.pdf',
  '(405) 208-5221'),

 ('', 'ASAP — no later than September 2026', 'Oklahoma State',
  '⚠⚠ HACK OKSTATE SPONSORSHIP — EMAIL NOW. THE BEST SPONSORSHIP PIPELINE IN OKLAHOMA.',
  'A private, student-run hackathon: sponsoring it SIDESTEPS the $250 permit and the commercial-solicitation rules '
  'entirely. ⚠ THE LIVE SITE IS A YEAR STALE — it still shows "Hack OKState \'25," Nov 1–2, 2025, Engineering '
  'South. (The "Major League Hacking 2026 Hackathon Season" badge is the MLH season label spanning 2025-26, NOT a '
  '2026 date.) Pattern: one weekend, early November, Engineering South, 24 hours, 100+ participants from any '
  'university, $1,000+ in prizes, open sponsorship (2025 sponsors included MLH and Pure Buttons). Sponsor decks '
  'typically close 6–8 WEEKS OUT.',
  'https://hackokstate.com/',
  'hackokstate@okstate.edu · Discord discord.gg/NkrYgaUnAN'),

 ('', 'Before any OSU table', 'Oklahoma State',
  '⚠⚠ BUY THE SOLICITATION PERMIT — $250 PER SEMESTER, PLUS $400 PER TABLE PER DAY',
  'The only published for-profit vendor tier in Oklahoma. "All off-campus vendors that would like to vend within '
  'the OSU campus must contact Meeting & Conference Services to obtain a solicitation permit." Clothed tables $5 '
  'each. On the same call: get the Student Union Use Guidelines PDF (the guidelines page lists documents but '
  'carries no rate table, insurance, deposit or cancellation terms and the PDFs did not resolve), confirm the '
  'rates are current for Fall 2026, ask how a non-affiliated vendor satisfies the outdoor "valid OSU ID" check-in, '
  'and confirm explicitly that there is no anti-fronting rule, no RSO-sponsorship ban, no insurance requirement '
  'and no deposit terms — absence of published text is not permission.',
  'https://meetings.okstate.edu/tabling',
  'meetings@okstate.edu · (405) 744-5232'),

 ('', 'Lead times before any OU table', 'U of Oklahoma',
  '⚠⚠ OU INFO TABLING — $300 PER DAY, WITH THREE STACKED LEAD TIMES',
  'Non-university groups pay $300/day for Oklahoma Memorial Union Info Tabling (RSOs and departments: free). '
  'Special Events Request Form required 15 DAYS in advance for third parties; liability insurance certificate to '
  'Risk Management at least 5 WORKING DAYS prior (no dollar limit published); payment due 72 WORKING HOURS prior, '
  'then 1.5% DAILY late fee after 45 days. ⚠ OU WILL NOT PROCESS CREDIT CARD DETAILS SENT BY EMAIL OR TEXT — pay '
  'via the payment link or by phone. Do NOT attempt a club route: sponsorship of non-university groups is '
  'expressly prohibited and fronting is referred to Student Conduct.',
  'https://www.ou.edu/union/host-your-event',
  'union@ou.edu · (405) 325-2121 — ask for Carolyn Carter or Sherry Paxton'),

 ('', 'Anytime — best door at OU', 'U of Oklahoma',
  '⚠ CALL DR. ANINDYA MAITI — ETHEREUM FOUNDATION GRANTEE, THE BEST ACADEMIC DOOR IN OKLAHOMA',
  'Assistant Professor of CS & Data Science Analytics; holds an Ethereum Foundation Academic Grant on Ethereum '
  'network security with doctoral student Scott Seidenberger; wrote the CS 5970 Blockchains & Cryptocurrencies '
  'syllabus (confirmed only for Spring 2023 — it is a rotating special-topics slot; ask CS at (405) 325-4042 '
  'whether it runs in Fall 2026). A seminar invitation from him makes DGD an "invited guest" of the campus '
  'community under 70 O.S. s 2120 — outside the commercial regime, at no cost.',
  'https://www.ou.edu/coe/cs/people/faculty/anindya-maiti',
  'am@ou.edu · (405) 325-4951'),

 ('', 'Five business days before anything at NSU', 'Northeastern State',
  '⚠ EMAIL THE STUDENT AFFAIRS AVP — REQUIRED WHETHER SPONSORED OR NOT',
  '"Advance reservation for expressive activity is required (in the form of an email to the Student Affairs '
  'Assistant Vice President) for events or activities that are PROMOTED IN ADVANCE, AND/OR SPONSORED BY STUDENT '
  'ORGANIZATIONS, AND/OR EXPECTED TO DRAW A CROWD OF MORE THAN 25 PEOPLE... at least five business days in '
  'advance." The trigger is DISJUNCTIVE — org sponsorship does not cure it, it triggers it. ⚠ The AVP\'s NAME IS '
  'NOT PUBLISHED; call Student Affairs and ask by role. All posters and fliers also need prior Student Affairs '
  'approval.',
  'https://offices.nsuok.edu/studentaffairs/StudentServices/ConductandDevelopment/Handbook/AdministrativeServices.aspx',
  'selfsj@nsuok.edu · Student Affairs 918-444-2120 · Student Engagement 918-444-2526'),

 ('', 'Deposit and cancellation ladder — TU', 'U of Tulsa',
  '⚠⚠ TU MONEY TERMS — 50% INSIDE 20 DAYS, 100% INSIDE 5 BUSINESS DAYS',
  'Off-campus clients: cancellation free only if 20+ days in advance; "within twenty (20) days... 50% of '
  'applicable room fees"; "within five (5) business days... 100% of applicable room fees." Deposits due 10 '
  'business days prior; insurance certificate 10–14 business days prior, general liability and property damage '
  'UP TO $500,000 naming "The University of Tulsa... as additional insured." ⚠ THE DOLLAR RATE CARD IS NOT '
  'PUBLISHED ANYWHERE — get it before committing. Also ask whether "taking of orders or subscription" reaches '
  'sign-ups and wallet registrations.',
  'https://utulsa.edu/about/offices/event-planning/reservation-policies-guide/',
  'eventhelp@utulsa.edu · 918-631-3211'),

 ('', 'Deposits and approvals — OCU', 'Oklahoma City U',
  '⚠⚠ OCU MONEY AND APPROVAL GATES — $1,000 DAMAGE DEPOSIT, 1/3 RENTAL UP FRONT',
  'Refundable $1,000 damage deposit due 15 business days prior; "a deposit of 1/3 the total rental fee is due upon '
  'reserving space"; cancellation within 48 hours costs $50. THE BASE RENTAL RATES ARE NOT PUBLISHED. On top of '
  'the money: "The Dean of Students must approve all non-university vendors and contractors," and any external '
  'speaker needs Dean approval AT LEAST ONE WEEK out no matter who invites them; demonstrations need three school '
  'days. Every flyer needs the Involved Center\'s approval stamp.',
  'https://www.okcu.edu/current/student-policies/student-handbook/x-university-center-reservations',
  'Involved Center (405) 208-5221 · Dean of Students Dr. Levi Harrel via (405) 208-5000, Room 257'),

 ('', 'Before routing anything through Edmond', 'U of Central Oklahoma',
  '⚠⚠ UCO IS A BLANK PAGE — ONE HOUR ON THE PHONE BEFORE ANY ROUTING DECISION',
  'NOT ONE UCO date, policy quote, club, faculty member or phone number is confirmed: uco.edu returns 403 to '
  'automated fetches at nearly every path, catalog.uco.edu fails with SSL CERTIFICATE_VERIFY_FAILED, the org '
  'directory (UCORE) is a JavaScript single-page app, and eventscentralok.com 403s. Exactly one page loaded — the '
  'Nigh University Center room rates (Grand Ballroom $2,055 full / $685 per section; Constitution Hall $575 '
  'half-day / $1,155 full-day; conference rooms $210 and $240; Blue Tent and Terrace $130 full-day) — and it '
  'carries NO contact information and does not say whether external commercial entities may book at all. GET: '
  'Fall 2026 start and finals dates, the solicitation policy, the external tabling rate, and one working number '
  'each for Student Involvement and Events Management. ⚠ Do not assume the ~Aug 17 regional start pattern; if it '
  'holds, the term has already begun.',
  'https://www.uco.edu/offices/events',
  'NO UCO NUMBER IS CONFIRMED — start at uco.edu/offices/events, then the campus operator'),

 ('', 'Monitor — statewide', 'All Oklahoma campuses',
  '⚠ DO NOT LET AN AMBASSADOR CITE 70 O.S. s 2120 AS A RIGHT TO TABLE',
  'The campus free-speech statute (SB 361/2019, amended HB 3543/2022 and SB 1725/2026) bars free-speech zones and '
  'deems outdoor areas public forums — but s 2120(D) protects only "NONCOMMERCIAL expressive activity," and the '
  'forum right runs to the "campus community... AND THEIR INVITED GUESTS," defined as students, administrators, '
  'faculty and staff. DGD is neither. OU\'s $300/day fee, OSU\'s $250 permit and $400/day table and every approval '
  'requirement in this packet are all lawful under it. It binds OU, OSU, UCO and NSU only — NOT TU or OCU, which '
  'are private. ⚠ ALSO: the "Oklahoma Students\' Religious Liberties Act" is a K-12 statute and MUST NOT appear in '
  'DGD materials.',
  'https://law.justia.com/codes/oklahoma/title-70/section-70-2120/',
  'OSU free-speech office (405) 744-5328'),
]
