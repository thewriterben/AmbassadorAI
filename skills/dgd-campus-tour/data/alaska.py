"""Alaska — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published / not retrievable at time of research — a gap to close by phone, not a
finding of absence. Schema: reference/data-schema.md

STATEWIDE STRUCTURE — read before any ambassador argues policy in Alaska:
The University of Alaska is ONE system with THREE separately-accredited universities
(UAA, UAF, UAS). Board of Regents policy sits above campus policy, but on facility use and
solicitation BOR POLICY IS DELIBERATELY THIN AND DELEGATES EVERYTHING DOWNWARD. That is the
single most important structural fact here. Regents' Policy P05.12.100 "Public Use of
Facilities" (eff. 06-20-97): "Facilities of the university will be open to the public for
educational, recreational, cultural activities, and other use IN ACCORDANCE WITH USE
PRIORITIES AND OTHER REQUIREMENTS AS MAY BE SET FORTH IN UNIVERSITY REGULATION AND CAMPUS
PROCEDURES." Regents' Policy P05.12.101 "Campus Solicitation" (eff. 06-20-97): "All
canvassing, peddling, or solicitation on university grounds or in university buildings will
be SUBJECT TO UNIVERSITY REGULATION AND CAMPUS PROCEDURES AS TO TIME, MANNER, AND PLACE."
(https://www.alaska.edu/bor/policy-regulations/chapter-05-12-capital-planning-facilities-management.php)
There is NO systemwide ban on commercial solicitation, NO systemwide fee schedule, NO
systemwide insurance limit and NO systemwide free-speech-zone rule. Every operative
restriction DGD will face is written at the CAMPUS level. If anyone says "it's a system
rule," ask which campus procedure. The full BOR text is reproduced in UAA's policy_key.

GEOGRAPHY — ALASKA IS NOT A TOUR. Anchorage to Fairbanks is ~358 road miles, 6–7 hours on
the Parks Highway in Sept–Dec weather that runs rain to ice — a full travel day each way.
JUNEAU HAS NO ROAD from anywhere: UAS is reachable only by air or the Alaska Marine Highway
ferry. APU is the only campus co-located with another — 4101 University Drive, walking
distance from UAA at 3211 Providence Drive. What Alaska supports is ONE ANCHORAGE TRIP
(UAA + APU on foot), a separate yes/no on a Fairbanks flight, and Juneau by phone.

ALL FOUR CAMPUSES START Mon Aug 24, 2026 — the three UA campuses because they share the UA
Common Calendar, APU by coincidence. No quarter school in Alaska. APU is the one calendar
oddity: a Block/Module hybrid where Block courses END SEPT 18 and Module II students do not
ARRIVE UNTIL OCT 21.
"""

STATE = 'Alaska'

CAMPUSES = [

 # ---------------------------------------------------------------- 1. UAA
 {'state': 'Alaska',
  'name': 'University of Alaska Anchorage',
  'city': 'Anchorage, AK',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 5,
  'start': 'Mon Aug 24, 2026 ⚠ UNVERIFIED FOR UAA SPECIFICALLY — inferred from the UA Common Calendar, which UAF '
           'and UAS both independently confirm. Never read on a UAA page: the registrar calendar URL failed '
           'repeatedly with robots.txt fetch errors. Confirm with the Provost, (907) 786-1050.',
  'adddrop': 'Fri Sep 4, 2026 (inferred from the UA Common Calendar — UNVERIFIED at UAA)',
  'fallbreak': 'No separate October fall break. UA folds fall break into Thanksgiving as a single Thu–Sun block.',
  'thanksgiving': 'Thu–Sun Nov 26–29, 2026 — no classes, most offices closed (inferred, UNVERIFIED at UAA)',
  'lastclass': 'Sat Dec 5, 2026 (inferred)',
  'finals': 'Mon–Sat Dec 7–12, 2026 (inferred). ⚠ UA campuses genuinely examine on SATURDAY.',
  'cal_url': 'https://www.uaa.alaska.edu/academics/faculty-services/dates/academic.cshtml',
  'cal_status': 'UNVERIFIED — the UAA calendar page is ROBOTS-BLOCKED to research tooling (the robots fetch itself '
                'times out; not a 403). UAA\'s Office of Academic Affairs states its calendars are "set in '
                'coordination with the UA Common Calendar" '
                '(https://www.uaa.alaska.edu/academics/office-of-academic-affairs/calendarsanddeadlines.cshtml), '
                'and UAF and UAS Fall 2026 dates — independently confirmed — are identical to each other. The '
                'inference is strong but it is an inference. Provost\'s Office (907) 786-1050.',
  'fair': 'Campus Kickoff / Kickoff Festival (the commercial door) — plus a separate, club-only Student '
          'Involvement Fair run by Club Council',
  'fair_date': '⚠ Sat Aug 22, 2026 — UNVERIFIED. This date comes from a THIRD-PARTY AGGREGATOR '
               '(https://frostboard.com/events/alaska/anchorage/uaa-campus-kickoff-2026), not from UAA. Aug 22, '
               '2026 is in fact a Saturday and a Saturday two days before an Aug 24 term start fits UAA\'s '
               'historical pattern — but UAA student press separately reports that "Campus Kickoff is moving" '
               '(thenorthernlight.org), so venue and possibly date may have changed. CONFIRM BY PHONE BEFORE '
               'BOOKING TRAVEL: (907) 786-1800, ask for Student Life & Leadership / Student Engagement. '
               'The Fall 2026 Student Involvement Fair date is NOT PUBLISHED — the pattern is one per semester '
               'in the Student Union (the most recent confirmed instance was Wed Jan 28, 2026, 10am–2pm, Student '
               'Union upper hallway, 2921 Spirit Dr). It will post at https://uaa.campusgroups.com/events — a '
               'JAVASCRIPT-RENDERED page that shows only template placeholders ([eventName], [date_text]) to '
               'non-browser tooling. Open it in a real browser.',
  'fair_outside': 'YES — EXPLICITLY, AS A PAYING "BUSINESS." UAA sells Campus Kickoff booth space directly to '
                  'businesses on a published rate card, and its own activities page describes Kickoff as featuring '
                  '"over 150 student clubs, departments, AND BUSINESSES." This is the only published for-profit '
                  'vendor tier in Alaska. ⚠ BUT NOT AT THE OTHER FAIR: the Student Involvement Fair is hosted by '
                  'Club Council for STUDENT ORGANIZATIONS and has no published outside-business tier. Kickoff is '
                  'the commercial door; the Involvement Fair is not.',
  'fair_cost': '$150.00 Business / Green tier; $225.00 Business / Gold tier. (Student Organization FREE / $50; UAA '
               'Department FREE / $100; Non-Profit $110 / $160.) Each tier includes an "Approx. 10\' x 10\' space '
               '(canopies not provided)" plus a table and chairs; Gold adds sponsor recognition and newspaper '
               'advertising. Extra tables and chairs are allowed but are "REQUIRED to fit within in the 10\' x 10\' '
               'space provided."',
  'fair_deadline': '⚠ NOT PUBLISHED. The registration page carries NO deadline, NO phone number, NO email and NO '
                   'named contact, and says nothing about whether vendors may sell, solicit, collect contact '
                   'information or run giveaways at the booth — which for a crypto project is the entire question. '
                   'The one procedural rule it does state: "sign-up once," duplicate registrations are deleted. '
                   'Call (907) 786-1800.',
  'fair_url': 'https://www.uaa.alaska.edu/students/traditions/kickoff-registration.cshtml',
  'policy': '"Use of University Facilities & Property for Non-Academic Purposes," UAA Student Handbook section of '
            'the Academic Catalog (no effective date stated on the page; cites no Board of Regents policy '
            'numbers). Above it: Regents\' Policy P05.12.100 and P05.12.101 (eff. 06-20-97) and Regents\' Policy '
            'Chapter 09.07 (Student Organizations).',
  'policy_url': 'https://catalog.uaa.alaska.edu/handbook/student-freedoms-rights-and-responsibilities/use-of-university-facilities-and-property-for-non-academic-purposes/',
  'policy_key': "UAA Student Handbook, 'Use of University Facilities & Property for Non-Academic Purposes': "
                "'DIRECT ADVERTISING, SALES AND COMMERCIAL SOLICITATION ARE NOT PERMITTED ON UNIVERSITY PROPERTY "
                "OR IN UNIVERSITY FACILITIES UNLESS UNDER CONTRACT WITH A UNIVERSITY COLLEGE, SCHOOL, DEPARTMENT, "
                "BUILDING MANAGER, OR ADMINISTRATIVE UNIT.' ⚠ THE BAN IS NOT ABSOLUTE — IT NAMES ITS OWN "
                "EXCEPTION, AND PAYING THE $150/$225 BUSINESS BOOTH FEE AT CAMPUS KICKOFF IS THAT CONTRACT. This "
                "is not a loophole; it is the mechanism the policy itself supplies. SPONSORSHIP, SEPARATELY: "
                "unaffiliated persons 'MUST BE SPONSORED BY A STUDENT GROUP/ORGANIZATION OR A UNIVERSITY SCHOOL OR "
                "DEPARTMENT IN ORDER TO USE UNIVERSITY FACILITIES.' That is PERMISSIVE sponsorship language — not "
                "the 'approval required whether sponsored or not' construction of stricter systems — so "
                "⚠ SPONSORSHIP GENUINELY CURES THE *FACILITY-ACCESS* PROBLEM AT UAA. ⚠ BUT SPONSORSHIP DOES NOT "
                "CURE THE *COMMERCIAL* RESTRICTION: read the two clauses together — sponsorship gets an outside "
                "entity into a facility; the commercial-solicitation ban is separately gated on a CONTRACT. A club "
                "hosting DGD does not by itself authorize 'direct advertising, sales and commercial solicitation.' "
                "Do not conflate them. PRIORITY: 'events by University schools or departments and student "
                "groups/organizations shall have priority over events and activities conducted by unaffiliated "
                "persons.' FUNDRAISING requires advance approval wherever 'monies (directly or indirectly) are "
                "exchanged for merchandise, service, entertainment or a chance at winning a prize' — read that on "
                "any giveaway or raffle. OUTDOOR SPEAKING AREAS (non-commercial channel only): unaffiliated groups "
                "must 'CONTACT THE UAA POLICE DEPARTMENT (UPD) AT LEAST TEN BUSINESS DAYS IN ADVANCE BUT NO MORE "
                "THAN TWELVE MONTHS IN ADVANCE.' Useful for expressive activity, NOT for marketing a financial "
                "product. ⚠ SYSTEMWIDE LAYER — UA BOARD OF REGENTS, which sits above all three UA campuses and "
                "DECIDES ALMOST NOTHING: P05.12.100 Public Use of Facilities (eff. 06-20-97) — 'Facilities of the "
                "university will be open to the public for educational, recreational, cultural activities, and "
                "other use IN ACCORDANCE WITH USE PRIORITIES AND OTHER REQUIREMENTS AS MAY BE SET FORTH IN "
                "UNIVERSITY REGULATION AND CAMPUS PROCEDURES'; P05.12.101 Campus Solicitation (eff. 06-20-97) — "
                "'All canvassing, peddling, or solicitation on university grounds or in university buildings will "
                "be SUBJECT TO UNIVERSITY REGULATION AND CAMPUS PROCEDURES AS TO TIME, MANNER, AND PLACE' "
                "(alaska.edu/bor/policy-regulations/chapter-05-12-capital-planning-facilities-management.php). "
                "Both PUNT to campus procedure. STUDENT-ORG LAYER — Regents' Chapter 09.07 "
                "(alaska.edu/bor/policy-regulations/chapter-09-07-student-organizations.php): P09.07.030 "
                "(04-23-99) 'NO STUDENT ORGANIZATION WILL BE DENIED REGISTRATION...ON THE BASIS OF THE VIEWS "
                "ESPOUSED BY ITS MEMBERS' — viewpoint neutrality; a crypto club cannot be refused recognition for "
                "being crypto. P09.07.040.C (04-23-99) organizations must 'AVOID ANY UNAUTHORIZED REPRESENTATION "
                "THAT THEY ARE AGENTS OF THE UNIVERSITY or that their views or actions are attributable to or "
                "endorsed' by it, must assume 'SOLE RESPONSIBILITY FOR THEIR DEBTS AND CONTRACTS,' and must 'USE "
                "UNIVERSITY BUSINESS OFFICES AND PRACTICES FOR FINANCIAL TRANSACTIONS.' ⚠ THAT LAST CLAUSE IS THE "
                "ONLY PAYMENT-CREDENTIAL-ADJACENT LANGUAGE IN UA POLICY: a sponsoring club CANNOT cleanly act as a "
                "payment conduit for DGD — money moving through a club must move through university business "
                "offices. R09.07.040 (06-21-99): 'STUDENT ORGANIZATIONS MUST SIGN A LICENSE AGREEMENT WITH THE "
                "UNIVERSITY IN ORDER TO USE A UNIVERSITY LOGO, TRADEMARK, OR SERVICEMARK' — relevant to any "
                "co-branded flyer. ⚠ NOTABLE ABSENCES, ALL 'NOT FOUND' RATHER THAN 'CONFIRMED ABSENT': NO "
                "ANTI-FRONTING LANGUAGE anywhere at the system level or at UAA (many state systems have it; this "
                "one appears not to); NO insurance requirement or coverage limit; NO deposit or cancellation "
                "terms; NO explicit ban on marketing financial products; and NO language reaching credit cards, "
                "payment apps by name, or signing contracts on site. These terms almost certainly exist in the "
                "EVENT SPACE USE AGREEMENT — the Event Services contact page and the Student Union reservations "
                "detail page were both robots-blocked, and the reservations page that did load says only "
                "'competitive rates' with no figures. GET THE AGREEMENT BY PHONE. "
                "⚠⚠ STATE REGULATORY NOTE — ALASKA, recorded here because the packet has no state-level field: "
                "THE RESEARCH FOUND NOTHING on Alaska's money-transmission or consumer-protection posture, and "
                "nothing was searched to exhaustion — treat that as an OPEN QUESTION, NOT as a finding that "
                "Alaska tracks the mainland. Do not represent Alaska's money-transmitter licensing, virtual-"
                "currency or consumer-protection regime as equivalent to any other state without checking the "
                "Alaska Division of Banking & Securities directly. Related and equally open: A CAMPUS FREE-"
                "EXPRESSION STATUTE (FORUM Act-style) COULD NOT BE CONFIRMED TO EXIST IN ALASKA — do not assert "
                "one does. Check Alaska Statutes Title 14 (Education) and confirm with UA General Counsel. And "
                "note that even the confirmed protections above (P09.07.030; the UAS catalog's protest right) are "
                "INSTITUTIONAL POLICY, NOT STATUTE, and NEITHER REACHES COMMERCIAL SPEECH BY AN OUTSIDE ENTITY, "
                "which is exactly what DGD is. DO NOT BUILD AN ACCESS ARGUMENT ON FREE-SPEECH GROUNDS IN ALASKA — "
                "the commercial-contract route is far stronger and needs no legal theory at all.",
  'sponsor_required': 'NO for the commercial route — pay the fee. The $150/$225 Business booth at Campus Kickoff '
                      'IS the "contract with a University... administrative unit" the policy names, and it needs '
                      'no student proxy. Sponsorship is a genuine SECOND route for facility access ("must be '
                      'sponsored by a student group/organization or a University school or department in order to '
                      'use University facilities" — permissive language, and no anti-fronting rule was found) — '
                      'but ⚠ a sponsor does NOT lift the separate ban on "direct advertising, sales and commercial '
                      'solicitation." For anything commercial, buy the contract.',
  'clubs': [('⚠ NO BLOCKCHAIN / CRYPTOCURRENCY / BITCOIN / WEB3 CLUB AT UAA',
             'Verified absent on the CampusGroups directory as read. No Financial Management Association chapter '
             'found either, and no dedicated investment club on the directory. ⚠ The directory is '
             'JAVASCRIPT-RENDERED (loading spinners, dynamic sections) and individual group pages may require '
             'login — read it in a real browser before treating any absence as final.',
             'https://uaa.campusgroups.com/club_signup'),
            ('⚠ Finance & Investments Club — UNVERIFIED LEAD, BEST SPONSOR CANDIDATE IN THE STATE',
             'Operates an Instagram account at @uaa_fnic but did NOT appear on the CampusGroups directory listing '
             'that could be read. It may be defunct, newly formed, or simply not rendered. Worth exactly one check '
             '— a finance/investments club is the single best sponsor candidate on this campus.',
             'https://www.instagram.com/uaa_fnic/'),
            ('Accounting Club at UAA',
             'Active. "To support students as they pursue a degree and build a career in the field of accounting." '
             'Also on Instagram @uaa_acctclub and Facebook @uaaacctclub. The best CONFIRMED club fit at UAA. No '
             'officer names published — none were found on a live page and none are guessed here.',
             'https://uaa.campusgroups.com/club_signup'),
            ('Computer Science Club at UAA',
             'Encourages CS involvement and professional connections.',
             'https://uaa.campusgroups.com/club_signup'),
            ('AI Club', '"No technical skills required, just curiosity." Low barrier, curious audience.',
             'https://uaa.campusgroups.com/club_signup'),
            ('Artificial Intelligence and Robotics Club',
             '"Enhance AI education and research capabilities at UAA."',
             'https://uaa.campusgroups.com/club_signup'),
            ('American Society of Civil Engineers at UAA; ASHRAE UAA Student Club',
             'Engineering, low relevance — listed for completeness.',
             'https://uaa.campusgroups.com/club_signup')],
  'faculty': [('⚠ Student Engagement, Community & Belonging / Student Life & Leadership',
               'RUNS BOTH CAMPUS KICKOFF AND THE STUDENT INVOLVEMENT FAIR — the office that decides whether DGD '
               'gets a booth, and the highest-value missing number in Alaska. Its pages '
               '(/students/student-life-leadership/, /students/engage/, /students/organizations/) ALL failed with '
               'robots.txt fetch errors across repeated attempts, so no number published — look up here, or reach '
               'it through the switchboard. The ONLY confirmed contact is the email.',
               'Student Affairs',
               'uaa.sos@alaska.edu · no number published — look up here; reach via switchboard (907) 786-1800',
               'https://uaa.campusgroups.com/web/rsvp_boot?id=377011'),
              ('⚠ College of Business and Public Policy',
               'THE RIGHT FIRST ACADEMIC CALL AT UAA. Owns the twelve-course finance sequence including BA A491A '
               'Student Managed Portfolio (a real-money student fund) and ECON A350 Money and Banking. ⚠ The CBPP '
               'faculty and staff directory is ROBOTS-BLOCKED, so NO UAA FACULTY MEMBER IS NAMED IN THIS PACKET — '
               'none was confirmed on a live page and none is guessed. Ask this line who teaches BA A491A and '
               'ECON A350 in Fall 2026.',
               'College of Business and Public Policy',
               '(907) 786-4100',
               'https://catalog.uaa.alaska.edu/coursedescriptions/ba/'),
              ('⚠ Ben Morton',
               'Dean of Students. Sits ABOVE student organizations and is the escalation point if Student '
               'Engagement stalls. One of the two people worth calling at UAA. Number is the Dean of Students '
               'main line.',
               'Dean of Students Office, Rasmuson Hall 122',
               'bmorton4@alaska.edu · (907) 786-1214',
               'https://www.uaa.alaska.edu/students/dean-of-students/contact-us.cshtml'),
              ('⚠ Michael Votava',
               'Assistant Dean of Students & Director of Student Conduct and Ethical Development. The second of '
               'the two worth calling — rules on org compliance and on what a sponsoring club may and may not do.',
               'Dean of Students Office',
               'mvotava@alaska.edu · (907) 786-6129',
               'https://www.uaa.alaska.edu/students/dean-of-students/contact-us.cshtml'),
              ('Dean of Students Office (main line)',
               'Rasmuson Hall 122, 3211 Providence Drive, Anchorage AK 99508. General inbox and main line for the '
               'office above.',
               'Dean of Students Office',
               'uaa_deanofstudents@alaska.edu · (907) 786-1214 (main line)',
               'https://www.uaa.alaska.edu/students/dean-of-students/contact-us.cshtml'),
              ('Denise Eggers',
               'Fiscal Coordinator, Dean of Students — money and fees inside the Dean of Students office.',
               'Dean of Students Office',
               'deggers1@alaska.edu · (907) 786-6152',
               'https://www.uaa.alaska.edu/students/dean-of-students/contact-us.cshtml'),
              ('Trevor Gillespie',
               'Assistant Director of Clery Compliance / Student Conduct Administrator.',
               'Dean of Students Office',
               'tlgillespie@alaska.edu · (907) 786-6151',
               'https://www.uaa.alaska.edu/students/dean-of-students/contact-us.cshtml'),
              ('Zoe Dohring',
               'Assistant Director of Student Conduct and Ethical Development.',
               'Dean of Students Office',
               'zdohring@alaska.edu · (907) 786-6065',
               'https://www.uaa.alaska.edu/students/dean-of-students/contact-us.cshtml'),
              ('Provost\'s Office (Office of Academic Affairs)',
               'THE AUTHORITATIVE SOURCE ON THE FALL 2026 CALENDAR, which could not be read on any UAA page. Call '
               'before booking travel.',
               'Academic Affairs',
               '(907) 786-1050',
               'https://www.uaa.alaska.edu/academics/office-of-academic-affairs/calendarsanddeadlines.cshtml'),
              ('UAA main campus switchboard',
               'The workaround for every UAA office whose page is robots-blocked. Use it to reach Student Life & '
               'Leadership, Student Engagement, Event Services and Student Activities.',
               'University Relations',
               '(907) 786-1800 (main line)',
               'https://www.uaa.alaska.edu/contact.cshtml'),
              ('Admissions / Enrollment / Registration',
               'Front door if the switchboard routing fails.',
               'Enrollment Services',
               '(907) 786-1480',
               'https://www.uaa.alaska.edu/contact.cshtml'),
              ('Graduate School',
               'Graduate cohort — relevant to BA A603 / BA A636 finance students.',
               'Graduate School',
               '(907) 786-1098',
               'https://www.uaa.alaska.edu/contact.cshtml'),
              ('Consortium Library',
               'Carried across for completeness — a possible non-commercial venue for a talk.',
               'Consortium Library',
               '(907) 786-1871',
               'https://www.uaa.alaska.edu/contact.cshtml'),
              ('Hugh McPeck Gallery',
               'Student Union gallery space. Carried across for completeness.',
               'Student Union',
               '(907) 786-1052',
               'https://www.uaa.alaska.edu/contact.cshtml'),
              ('Event Services',
               'Holds the Event Space Use Agreement and the actual rate card — the document with the insurance, '
               'deposit and cancellation terms that are published nowhere. Its contact page was ROBOTS-BLOCKED on '
               'every attempt: no number published — look up here in the UAA department directory.',
               'Event Services',
               'no number published — look up here; or switchboard (907) 786-1800',
               'https://directory.uaa.alaska.edu/Department/Detail/dir_UAA_ANC_Event_Services'),
              ('Student Activities',
               'Exists as a department in the UAA directory; no number reached. No number published — look up here.',
               'Student Union — Student Activities',
               'no number published — look up here; or switchboard (907) 786-1800',
               'https://directory.uaa.alaska.edu/Department/Detail/dir_UAA_SU_Student_Activities'),
              ('(UAA finance / economics faculty)',
               'NOT CONFIRMED — the CBPP faculty and staff directory is robots-blocked and NO UAA FACULTY MEMBER '
               'IS NAMED HERE. UAA has a substantial finance faculty by inference from twelve catalog finance '
               'courses (derivatives, bond markets, a student-managed portfolio), but naming anyone would be a '
               'guess. ⚠ Also note: directory.uaa.alaska.edu and directory.alaska.edu are real campus-wide '
               'people-search systems that were UNREACHABLE from the research environment (robots timeouts plus a '
               '403 from the egress proxy). An ambassador on a normal connection should hit them first — they '
               'will resolve most missing individual numbers in minutes.',
               'College of Business and Public Policy',
               'no number published — look up here; start at CBPP (907) 786-4100',
               'https://directory.alaska.edu/')],
  'courses': [('⚠ BA A491A',
               'Student Managed Portfolio — HIGHEST-VALUE TARGET IN ALASKA. A real-money student fund is the most '
               'crypto-curious audience on any campus in the state. ⚠ Fall 2026 offering UNVERIFIED: catalog '
               'listing is not term offering. Check UAOnline or ask CBPP, (907) 786-4100.',
               'https://catalog.uaa.alaska.edu/coursedescriptions/ba/'),
              ('⚠ ECON A350',
               'Money and Banking — the single most topically adjacent course in Alaska. "Examines how financial '
               'markets and financial institutions affect the macroeconomic state of the economy, HOW MONEY IS '
               'CREATED, the role of central banks in financial regulation, and the implementation of monetary '
               'policy." A guest lecture here is the natural non-commercial door. Fall 2026 offering UNVERIFIED.',
               'https://catalog.uaa.alaska.edu/coursedescriptions/econ/'),
              ('BA A452 / BA A453 / BA A451',
               'Financial Derivatives; Bond Market Analysis; Advanced Investment Strategies — the upper-division '
               'quantitative cluster. Fall 2026 offering UNVERIFIED for all.',
               'https://catalog.uaa.alaska.edu/coursedescriptions/ba/'),
              ('BA A233 / A325 / A380 / A385 / A426 / A427',
               'Survey of Finance; Corporate Finance; Investment Management; Intermediate Financial Management; '
               'Financial Institutions; International Finance — the rest of a twelve-course finance sequence, the '
               'deepest finance curriculum in Alaska. Graduate: BA A603 Fundamentals of Finance, BA A636 '
               'Financial Decision Making.',
               'https://catalog.uaa.alaska.edu/coursedescriptions/ba/'),
              ('(Blockchain / crypto / fintech)',
               '⚠ NONE — no blockchain, cryptocurrency, fintech or digital-asset course exists in the UAA catalog. '
               'Confirmed by reading both relevant subject listings in full (Business Administration and '
               'Economics). This is a verified absence, not a gap.',
               'https://catalog.uaa.alaska.edu/coursedescriptions/')],
  'events': [('⚠ Campus Kickoff / Kickoff Festival',
              'Sat Aug 22, 2026 per a third-party aggregator only — UNVERIFIED, and UAA student press reports '
              'Kickoff "is moving." "Over 150 student clubs, departments, and businesses." $150/$225 Business '
              'booth. THE ONE EVENT IN ALASKA THAT SELLS SPACE TO A FOR-PROFIT ON A PUBLISHED RATE CARD.',
              'https://www.uaa.alaska.edu/students/traditions/kickoff-registration.cshtml'),
             ('Student Involvement Fair (Club Council)',
              'Indoor, club-focused, Student Union upper hallway, one per semester. Most recent confirmed '
              'instance: Wed Jan 28, 2026, 10am–2pm, 2921 Spirit Dr — that was the SPRING edition and has passed. '
              'FALL 2026 DATE NOT PUBLISHED. No outside-business tier. Contact uaa.sos@alaska.edu.',
              'https://uaa.campusgroups.com/web/rsvp_boot?id=377011'),
             ('Bartlett Lecture Series',
              'An established UAA speaker series bringing speakers on national and international topics — the '
              'obvious non-commercial door if a talk beats a table. ⚠ No Fall 2026 schedule published, and the '
              'page it appears on is STALE (still references Spring 2020 COVID closures and Fall 2021 planning).',
              'https://www.uaa.alaska.edu/students/engage/activities-programs.cshtml'),
             ('Homecoming Week',
              'Annual, Fall. No Fall 2026 date published.',
              'https://www.uaa.alaska.edu/students/engage/activities-programs.cshtml'),
             ('Hackathon / career fair — NONE FOUND',
              '⚠ No hackathon at UAA, no career fair date confirmed, no blockchain conference or research centre, '
              'and no Alaska legislative blockchain activity connected to a campus. Given the research budget was '
              'exhausted, treat this as UNCLOSED rather than empty — hackathons are the one channel that '
              'sidesteps campus commercial rules entirely, so it is worth one more pass (MLH Alaska listings, '
              'UAA/UAF CS department pages).',
              '')],
  'play': 'This is the stop. If Alaska gets one trip, it is Anchorage, and UAA is why. It is the only campus in '
          'the state — and one of very few anywhere — whose written policy bans commercial solicitation and then '
          'names its own cure in the same sentence: "unless under contract with a University College, School, '
          'Department, Building Manager, or administrative unit." Paying the $150 (Green) or $225 (Gold) BUSINESS '
          'booth fee at Campus Kickoff IS that contract. You are not asking for an exception; you are buying the '
          'product UAA advertises to businesses on its own rate card, alongside "over 150 student clubs, '
          'departments, and businesses." Do that, and you are on the largest quad in Alaska, in front of the '
          'deepest finance curriculum in the state — twelve finance courses, a real-money Student Managed '
          'Portfolio (BA A491A) and ECON A350 Money and Banking. ⚠ BUT THE SINGLE BEST DOOR IS A PHONE CALL, NOT '
          'A FORM: call (907) 786-1800 and ask for Student Life & Leadership / Student Engagement, Community & '
          'Belonging — the office that runs Kickoff, whose direct number is published nowhere and whose pages are '
          'all robots-blocked (only confirmed contact: uaa.sos@alaska.edu). Ask three things on that call: (1) is '
          'Kickoff still Sat Aug 22, and where — the date comes from a THIRD-PARTY AGGREGATOR and the student '
          'paper says Kickoff "is moving"; (2) what is the registration deadline — the rate card publishes prices '
          'but no deadline; (3) may a business booth SELL, SOLICIT, COLLECT CONTACT INFORMATION OR RUN A GIVEAWAY '
          '— the page is silent, and for a crypto project that is the whole question (note fundraising rules bite '
          'wherever "monies (directly or indirectly) are exchanged for merchandise, service, entertainment or a '
          'chance at winning a prize"). Second call: CBPP at (907) 786-4100, to find who teaches BA A491A and '
          'ECON A350 — a guest lecture is free, non-commercial and reaches exactly the right twenty students. Do '
          'NOT chase the Student Involvement Fair: it is Club Council\'s, student-orgs only, no business tier. Do '
          'NOT lean on sponsorship to do commercial work: a club can get you into a facility, but it cannot lift '
          'the sales ban, and under Regents\' P09.07.040.C a club cannot act as your payment conduit either. And '
          'do NOT argue free speech — no Alaska campus-expression statute could be confirmed to exist, and the '
          'protections that do exist are policy, not statute, and do not reach commercial speech.',
  'gaps': ['⚠⚠ CAMPUS KICKOFF 2026 DATE AND VENUE — Sat Aug 22 comes from a third-party aggregator '
           '(frostboard.com), never from UAA, and UAA student press reports Kickoff "is moving." Blocking for '
           'travel. Call (907) 786-1800, ask for Student Life & Leadership. '
           'https://www.thenorthernlight.org/stories/usuaa-meeting-5-31-campus-kickoff-is-moving-students-like-free-ice-cream-and-adopt-a-road-cleaning-dates-set',
           '⚠⚠ KICKOFF BOOTH REGISTRATION DEADLINE AND BOOTH CONDUCT RULES — the registration page publishes '
           'prices but NO deadline, NO contact, and says nothing about whether vendors may sell, solicit, collect '
           'contact information or run giveaways. (907) 786-1800. '
           'https://www.uaa.alaska.edu/students/traditions/kickoff-registration.cshtml',
           '⚠ UAA FALL 2026 CALENDAR — every date in this record is INFERRED from the UA Common Calendar and was '
           'never read on a UAA page (registrar calendar robots-blocked). Provost\'s Office (907) 786-1050. '
           'https://www.uaa.alaska.edu/academics/faculty-services/dates/academic.cshtml',
           '⚠ UAA STUDENT LIFE & LEADERSHIP / STUDENT ENGAGEMENT DIRECT NUMBER — the office that runs both fairs, '
           'and no phone could be confirmed. Only confirmed contact: uaa.sos@alaska.edu. Every relevant page '
           '(/students/student-life-leadership/, /students/engage/, /students/organizations/) failed with '
           'robots.txt fetch errors.',
           'UAA EVENT SERVICES NUMBER and the EVENT SPACE USE AGREEMENT — insurance requirement and limit, '
           'deposit, and cancellation terms are published NOWHERE at UAA; they will be in that agreement. Contact '
           'page robots-blocked throughout. '
           'https://directory.uaa.alaska.edu/Department/Detail/dir_UAA_ANC_Event_Services',
           'Does the "Finance & Investments Club" (@uaa_fnic on Instagram) exist and is it registered? It did not '
           'appear on the CampusGroups directory listing that could be read. It would be the best sponsor in the '
           'state. https://uaa.campusgroups.com/club_signup',
           'Fall 2026 Student Involvement Fair date — not published. Will post at '
           'https://uaa.campusgroups.com/events, which is JAVASCRIPT-RENDERED and shows only template '
           'placeholders to non-browser tooling. Open in a real browser. uaa.sos@alaska.edu',
           'UAA faculty — NO ONE IS NAMED in this record. The CBPP faculty/staff directory is robots-blocked and '
           'directory.uaa.alaska.edu / directory.alaska.edu were unreachable (robots timeouts + 403 from the '
           'egress proxy). Both work fine on a normal connection. Start at CBPP (907) 786-4100.',
           'Whether BA A491A Student Managed Portfolio and ECON A350 Money and Banking actually run in Fall 2026 '
           '— catalog listing is not term offering. UAOnline or CBPP (907) 786-4100.',
           'Fall 2026 events at UAA — no hackathon, career fair date, or Bartlett Lecture schedule was '
           'obtainable, and the activities page carrying them is STALE (Spring 2020 / Fall 2021 content). '
           'Unclosed, not empty. https://www.uaa.alaska.edu/students/engage/activities-programs.cshtml'],
  'note': '⚠ STALE PAGE: https://www.uaa.alaska.edu/students/engage/activities-programs.cshtml still references '
          'Spring 2020 COVID closures and Fall 2021 planning. It is the source for the Bartlett Lecture Series, '
          'Homecoming and the "over 150 student clubs, departments, and businesses" line — treat nothing on it as '
          'current. Separately, UAA and APU are WALKING DISTANCE APART (3211 Providence Drive vs 4101 University '
          'Drive) — they are the only pairing in Alaska that shares a trip.'},

 # ---------------------------------------------------------------- 2. UAF
 {'state': 'Alaska',
  'name': 'University of Alaska Fairbanks',
  'city': 'Fairbanks, AK',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 4,
  'start': 'Mon Aug 24, 2026 — CONFIRMED on UAF\'s own catalog calendar PDF',
  'adddrop': 'Fri Sep 4, 2026 — 5:00 p.m. in person, 11:59 p.m. at UAOnline',
  'fallbreak': '⚠ NO SEPARATE OCTOBER FALL BREAK — UAF folds fall break and Thanksgiving into ONE Thu–Sun block, '
               'Nov 26–29. Fairbanks runs at full density Aug 24 through Nov 25.',
  'thanksgiving': 'Thu–Sun Nov 26–29, 2026 — no classes, most offices closed',
  'lastclass': 'Sat Dec 5, 2026',
  'finals': '⚠ Mon–Sat Dec 7–12, 2026 — UAF genuinely examines THROUGH SATURDAY DEC 12.',
  'cal_url': 'https://catalog.uaf.edu/calendar/calendar.pdf',
  'cal_status': 'CONFIRMED on the UAF catalog calendar PDF. (The registrar mirror at '
                'https://www.uaf.edu/reg/calendar/fall-26.php is robots-blocked and could not be cross-checked.)',
  'fair': 'Party in the Park (fall involvement fair) — and, more usefully, STANDING COMMERCIAL BOOTH SPACE in the '
          'Wood Center, bookable Tuesday–Thursday all year',
  'fair_date': '⚠ NOT PUBLISHED for Fall 2026. Pattern, from a 2017 UAF news article: the TUESDAY OF THE FIRST '
               'WEEK OF CLASSES, noon–2 p.m., setup from 11 a.m., Constitution Park (by the bookstore), moving '
               'indoors to Wood Center in poor weather. Applied to the Fall 2026 calendar that would be about '
               'TUE SEP 1, 2026 — ⚠ THAT IS ARITHMETIC, NOT UAF\'S ANNOUNCEMENT. DO NOT RELY ON IT. It will post '
               'at https://www.uaf.edu/sli/. ⚠ The date risk is largely moot: Wood Center commercial booth space '
               'is a standing, bookable product available Tuesday–Thursday throughout the academic year, so UAF '
               'does not require hitting a single date.',
  'fair_outside': 'YES for Party in the Park — verbatim from UAF: "This is a great way for new and returning '
                  'students to connect with student clubs, UAF departments AND FAIRBANKS COMMUNITY '
                  'ORGANIZATIONS," and there is a dedicated non-university registration path: "IF YOU ARE A '
                  'COMMUNITY ORGANIZATION WITHOUT A UA EMAIL, PLEASE REGISTER HERE." ⚠ Source is a 2017 article — '
                  'nine years stale, internally consistent (Aug 29, 2017 was a Tuesday) but must be re-confirmed. '
                  'YES for Wood Center too, by a different mechanism: the scheduling system carries a dedicated '
                  'request type, "BOOTHS SPACE: FOR AN INFORMATION OR FUNDRAISING BOOTH," and commercial booth '
                  'space is sold Tuesday–Thursday during the academic year.',
  'fair_cost': '⚠ NOT PUBLISHED — no commercial or non-university rate appears anywhere. The published fee page '
               'lists ONLY: setup/teardown for UAF departments $20.00/hr; setup/teardown for student clubs and '
               'organizations $15.00/hr; AV equipment $10 flat in addition to setup/teardown; additional building '
               'hours $75.00/hr with a 3-hour minimum for unannounced openings (ten working days\' notice '
               'required). Some rooms have standard setups at no charge. Party in the Park community-organization '
               'cost tiers are not published either. GET THE COMMERCIAL RATE BY PHONE: (907) 474-6023.',
  'fair_deadline': 'Standard scheduling processing is 48 HOURS (2 business days). Additional building hours '
                   'require TEN WORKING DAYS notice; an alcohol waiver (if ever relevant) ten days prior. '
                   'Scheduling office hours Mon–Fri 7:30 a.m.–4:30 p.m. No registration deadline is published for '
                   'Party in the Park.',
  'fair_url': 'https://www.uaf.edu/woodcenter/services/room-scheduling/',
  'policy': 'UAF Wood Center Solicitation Policy (no effective date shown) — plus the Wood Center room- and '
            'event-scheduling procedures, the Event Space Use Agreement and the Events Committee approval list. '
            'Above them: Regents\' P05.12.100 / P05.12.101 (see the UAA record for the full systemwide text).',
  'policy_url': 'https://www.uaf.edu/woodcenter/about/policies/solicitation-policy.php',
  'policy_key': "UAF Wood Center Solicitation Policy "
                "(www.uaf.edu/woodcenter/about/policies/solicitation-policy.php): 'PRIVATE INDIVIDUALS OR "
                "ORGANIZATIONS DESIRING CAMPUS ACCESS FOR NON-COMMERCIAL SOLICITATION ACTIVITIES...MUST REGISTER "
                "IN PERSON WITH THE UAF SCHEDULING OFFICE.' And: 'IN-PERSON SOLICITATION ACTIVITIES...IS LIMITED "
                "TO EXTERIOR AREAS AS APPROVED BY UAF.' And: 'HANDBILLS, LEAFLETS, PAMPHLETS AND OTHER SIMILAR "
                "MATERIALS SHALL NOT BE PLACED ON VEHICLES PARKED ON UAF PROPERTY.' Residence-hall door-to-door "
                "solicitation requires prior consent of the Resident Director and must meet three criteria, "
                "including that it serve NON-COMMERCIAL interests in UAF-affiliated programs. ⚠ CRITICAL READ — "
                "THIS POLICY GOVERNS NON-COMMERCIAL SOLICITATION ONLY. IT SAYS NOTHING ABOUT COMMERCIAL VENDORS. "
                "AT UAF, COMMERCIAL ACTIVITY IS NOT HANDLED AS 'SOLICITATION' AT ALL — IT IS HANDLED AS A "
                "FACILITIES TRANSACTION through Wood Center Scheduling's commercial booth product, available "
                "Tuesday–Thursday during the academic year, with 'BOOTHS SPACE: FOR AN INFORMATION OR FUNDRAISING "
                "BOOTH' as a named request type. That is a materially different posture from UAA and it is good "
                "news: DGD is a paying customer, not a supplicant. ⚠ BUT NOTE 'MUST REGISTER IN PERSON' — UAF "
                "expects a physical appearance at the Scheduling Office for the non-commercial route. For a "
                "fly-in ambassador that is real friction; resolve it by phone in advance. PROCESS "
                "(www.uaf.edu/woodcenter/services/room-scheduling/): (1) submit a space request through 25LIVE; "
                "(2) complete an EVENT SPACE USE AGREEMENT where required; (3) obtain EVENTS COMMITTEE approval "
                "where needed. ⚠ DGD TRIGGERS THE FIRST APPROVAL CATEGORY AUTOMATICALLY — events requiring "
                "approval are: 'PUBLIC EVENTS OR THOSE WITH NON-UNIVERSITY ATTENDEES'; events expecting 50+ "
                "participants; events featuring anyone under 18; events requiring campus publicity. Events NOT "
                "requiring further approval: closed meetings under 50 attendees, and — importantly — 'TABLING AT "
                "WOOD CENTER,' WHICH IS PRE-CLEARED. Outside groups may reserve space but 'REQUIRE A 25 LIVE "
                "SPACE/EVENT REQUEST AND THE COMPLETION OF THE EVENT SPACE USE AGREEMENT.' PUBLISHED FEES "
                "(uaf.edu/woodcenter/services/event-scheduling/event-planning-resources/): setup/teardown UAF "
                "departments $20.00/hr; student clubs and organizations $15.00/hr; AV equipment $10 flat in "
                "addition; additional building hours $75.00/hr, 3-HOUR MINIMUM, for unannounced openings, TEN "
                "WORKING DAYS notice; all food must go through UAF Dining Services; alcohol waiver ten days "
                "prior. ⚠ NO COMMERCIAL / NON-UNIVERSITY RATE IS PUBLISHED ANYWHERE — the fee page lists only "
                "department and student-club rates. ⚠ NOTABLE ABSENCES, ALL 'NOT FOUND' RATHER THAN 'CONFIRMED "
                "ABSENT' (campus procedures could not all be read): NO ANTI-FRONTING LANGUAGE; NO clause barring "
                "a club from hosting an outside entity; NO insurance requirement or coverage limit; NO deposit or "
                "cancellation terms; NO free-speech-zone designation; NO language reaching credit cards, payment "
                "apps or on-site contract signing. THESE TERMS WILL LIVE IN THE EVENT SPACE USE AGREEMENT — "
                "REQUEST A COPY OF THE ACTUAL DOCUMENT AT (907) 474-6023 BEFORE COMMITTING. ABSENCE OF PUBLISHED "
                "TEXT IS NOT PERMISSION. CLUB-SIDE CONSTRAINT worth knowing before any club-mediated giveaway "
                "(www.uaf.edu/sli/clubs/about/faq.php): prohibited club purchases are 'drugs, alcohol, tobacco, "
                "or firearms,' and GIFT CARDS ARE CAPPED AT $25. Clubs start with zero funding; 'SLI will offer "
                "club funding when budget permits' and 'ASUAF also offers funding to clubs on an application "
                "basis though Club Council'; each club gets a '$75 credit per semester with Wood Center Graphics' "
                "for promotional materials, non-carryover. SYSTEMWIDE LAYER: see the UAA record — Regents' "
                "P05.12.100 and P05.12.101 delegate all of this to campus procedure, and P09.07.040.C requires "
                "student organizations to 'use university business offices and practices for financial "
                "transactions,' which blocks any club from acting as DGD's payment conduit.",
  'sponsor_required': 'NO — buy the booth. UAF treats commercial access as a facilities purchase, not as '
                      'solicitation, and Wood Center tabling is expressly pre-cleared from further approval. You '
                      'need a 25Live request and an Event Space Use Agreement, not a student proxy. No '
                      'anti-fronting or no-sponsorship clause was found — but that is "not found," not '
                      '"confirmed absent." Confirm at (907) 474-6023.',
  'clubs': [('⚠ UAF CLUB DIRECTORY — NEVER READ. UNCLOSED GAP, NOT A FINDING OF ABSENCE.',
             'UAF states it has "over 100 active student organizations." The directory platform is NANOOK ENGAGE. '
             'The SLI clubs pages that could be reached carry no roster and no directory link that resolved, so '
             'NOTHING can be said about whether a blockchain, crypto, fintech or investment club exists at UAF. '
             'An ambassador should search Nanook Engage directly for: blockchain, crypto, bitcoin, Web3, fintech, '
             'investment, FMA, ACM, data science.',
             'https://www.uaf.edu/sli/clubs/'),
            ('Club funding and giveaway constraints (from the SLI clubs FAQ)',
             'Useful sponsor-side context if a club route is attempted: clubs start with ZERO funding; "SLI will '
             'offer club funding when budget permits"; "ASUAF also offers funding to clubs on an application '
             'basis though Club Council"; each club gets a "$75 credit per semester with Wood Center Graphics" '
             '(non-carryover); "Student Organizations can also reserve space in the Wood Center to table for '
             'different events." ⚠ GIFT CARDS ARE CAPPED AT $25 and drugs/alcohol/tobacco/firearms are prohibited '
             'purchases — relevant to any club-mediated giveaway.',
             'https://www.uaf.edu/sli/clubs/about/faq.php'),
            ('(Officer names)',
             'NONE REPORTED — none was found on a live page and none is guessed.',
             'https://www.uaf.edu/sli/clubs/')],
  'faculty': [('⚠ UAF Event Scheduling Office',
               'THE DECISION-MAKER AT UAF AND THE SINGLE MOST IMPORTANT NUMBER IN FAIRBANKS. Controls booth '
               'space, 25Live requests and the Event Space Use Agreement. Ask it for: the COMMERCIAL booth rate '
               '(published nowhere), a copy of the Event Space Use Agreement, the insurance/deposit/cancellation '
               'terms, and how a fly-in ambassador satisfies the "must register in person" requirement. Office '
               'hours Mon–Fri 7:30 a.m.–4:30 p.m.; standard processing 48 hours.',
               'Wood Center — Event Scheduling',
               'uaf-event-schedule@alaska.edu · (907) 474-6023',
               'https://www.uaf.edu/woodcenter/services/event-scheduling/'),
              ('⚠ Wood Center (student union)',
               'THE BUILDING — and the workaround for two offices that publish no phone at all. Student Leadership '
               'and Involvement (SLI) is physically located here, and Student Activities runs Nanook Traditions '
               'from here. 1731 S. Chandalar Drive, P.O. Box 750126, Fairbanks, AK 99775-0126.',
               'Wood Center',
               'uaf-woodcenter@alaska.edu · (907) 474-7034',
               'https://catalog.uaf.edu/resources/wood-center/'),
              ('Student Leadership and Involvement (SLI)',
               'Runs Party in the Park and the club system, and is where the Fall 2026 date will post. ⚠ NEITHER '
               'https://www.uaf.edu/sli/ NOR /sli/about/index.php carries a phone, email, room or staff name — a '
               'genuinely under-documented office. No number published — look up here; reach it via Wood Center, '
               '(907) 474-7034, since SLI sits inside that building.',
               'Student Leadership and Involvement',
               'no number published — look up here; reach via Wood Center (907) 474-7034',
               'https://www.uaf.edu/sli/'),
              ('Dean of Students',
               'Escalation point above student organizations. ⚠ The page describes the office\'s functions but '
               'publishes NO phone, email, location or staff names. No number published — look up here; route via '
               'Wood Center or the UA directory at https://directory.alaska.edu/.',
               'Dean of Students',
               'no number published — look up here; route via Wood Center (907) 474-7034',
               'https://www.uaf.edu/deanofstudents/'),
              ('"r.keele@alaska.edu"',
               '⚠ An email that appears on the Wood Center scheduling page for form updates. A SURNAME AND AN '
               'INSTITUTIONAL EMAIL ONLY — no confirmed full name, title or direct line. DO NOT ADDRESS THIS '
               'PERSON BY A GUESSED FIRST NAME. No number published — look up here or via Event Scheduling.',
               'Wood Center — Event Scheduling',
               'r.keele@alaska.edu · no number published — look up here; or (907) 474-6023',
               'https://www.uaf.edu/woodcenter/services/event-scheduling/'),
              ('UAF Dining Services',
               'MANDATORY for any food at any event — "all food must go through UAF Dining Services." Budget for '
               'this before promising snacks at a table.',
               'Dining Services',
               '(907) 474-6820',
               'https://uaf.edu/woodcenter/services/event-scheduling/event-planning-resources/'),
              ('UAF Dining Services (alternate line)',
               'Second number given on the Wood Center pricing page.',
               'Dining Services',
               '(907) 474-6661',
               'https://uaf.edu/woodcenter/services/event-scheduling/event-planning-resources/'),
              ('BP Design Theatre',
               'Venue-specific scheduling — an option if a talk beats a table.',
               'Venue scheduling',
               '(907) 474-5402',
               'https://www.uaf.edu/woodcenter/services/room-scheduling/'),
              ('Murie Building',
               'Venue-specific scheduling.',
               'Venue scheduling',
               '(907) 474-6294',
               'https://www.uaf.edu/woodcenter/services/room-scheduling/'),
              ('UAF Theater & Film',
               'Venue-specific scheduling.',
               'Venue scheduling',
               '(907) 474-7231',
               'https://www.uaf.edu/woodcenter/services/room-scheduling/'),
              ('(UAF faculty)',
               'NOT CONFIRMED — no UAF blockchain, crypto or fintech faculty member was identified and NO ONE IS '
               'NAMED HERE. The relevant department for ECON F350 Money and Banking is Economics within the '
               'School of Management. Look up at the UA people directory. No number published — look up here.',
               'School of Management — Economics',
               'no number published — look up here',
               'https://directory.alaska.edu/')],
  'courses': [('⚠ ECON F350',
               'Money and Banking — THE ONLY RELEVANT COURSE AT UAF. "Examines... the liquid wealth system in the '
               'United States, including the commercial banking system, the Federal Reserve System and nonbank '
               'financial institutions." Confirmed by reading the full 29-course ECON listing. ⚠ Fall 2026 '
               'offering UNVERIFIED — it is a standard rotation course at most institutions but the term was not '
               'confirmed.',
               'https://catalog.uaf.edu/courses/econ/'),
              ('(Blockchain / crypto / fintech)',
               '⚠ NONE in the ECON listing, which was read in full. ⚠ The BA / School of Management and Computer '
               'Science course listings were NOT READ — unclosed gap, so this is not a whole-catalog absence.',
               'https://catalog.uaf.edu/courses/')],
  'events': [('⚠ Party in the Park',
              'UAF\'s fall involvement fair. Pattern (from a 2017 article — NINE YEARS STALE): Tuesday of the '
              'first week of classes, noon–2 p.m., setup 11 a.m., Constitution Park by the bookstore, indoors to '
              'Wood Center in poor weather. Explicitly welcomes "Fairbanks community organizations" with a '
              'dedicated non-UA-email registration path. FALL 2026 DATE NOT PUBLISHED; arithmetic suggests about '
              'Tue Sep 1, 2026 but that is not UAF\'s announcement. Will post at https://www.uaf.edu/sli/.',
              'https://news.uaf.edu/party-in-the-park-aug-29/'),
             ('⚠ Wood Center commercial booth space — the year-round channel',
              'Not a dated event but the reason UAF works: commercial booth space is sold Tuesday–Thursday '
              'THROUGHOUT the academic year, with "Booths Space: for an information or fundraising booth" as a '
              'named request type, and Wood Center tabling pre-cleared from further approval. DGD does not have '
              'to hit a single date at UAF. Rate unpublished — (907) 474-6023.',
              'https://www.uaf.edu/woodcenter/services/room-scheduling/'),
             ('Nanook Traditions',
              'UAF\'s traditions programming, run out of the Student Activities Office in Wood Center. No Fall '
              '2026 dates confirmed.',
              'https://catalog.uaf.edu/resources/wood-center/'),
             ('Hackathon / career fair / speaker series — NONE CONFIRMED',
              '⚠ No Fall 2026 event of any kind was confirmed at UAF. The Wood Center events calendar '
              '(https://www.uaf.edu/woodcenter/about/calendar.php) could not be read. Unclosed gap, not an empty '
              'one.',
              'https://www.uaf.edu/woodcenter/about/calendar.php')],
  'play': 'Fairbanks is a real option but a conditional one, and the condition is money and daylight, not policy. '
          'The policy read is genuinely good: UAF\'s written solicitation policy governs NON-COMMERCIAL activity '
          'only and says nothing about commercial vendors, because at UAF commercial access is not a permission '
          'question at all — it is a facilities purchase. Wood Center sells commercial booth space Tuesday '
          'through Thursday all year, the scheduling system has a dedicated "Booths Space" request type, and '
          '"Tabling at Wood Center" is expressly pre-cleared from further approval. That removes the single '
          'biggest risk at every other campus: you are not chasing one fair date. The one door to knock on is the '
          'UAF EVENT SCHEDULING OFFICE, (907) 474-6023 — it controls booth space, 25Live and the Event Space Use '
          'Agreement, and it is the only office in Fairbanks that can answer the three unpublished questions: '
          'what does a COMMERCIAL booth actually cost (the fee page lists only $20/hr departments and $15/hr '
          'student clubs), what does the Event Space Use Agreement require on insurance, deposit and '
          'cancellation, and how does a fly-in ambassador satisfy the policy\'s "must register in person" '
          'language. ⚠ Now the honest part: UAF is 358 road miles and 6–7 hours from Anchorage on the Parks '
          'Highway in weather that runs rain to ice from September on, or a separate flight. The audience is '
          'smaller than UAA\'s, the ECON F350 Money and Banking course is the only topically relevant class, the '
          'club directory (Nanook Engage) could not be read at all so no crypto club is either confirmed or '
          'ruled out, and DECEMBER IN FAIRBANKS IS A GENUINE OPERATIONAL CONSTRAINT — a few hours of usable light '
          'and deep cold, against a term whose last class is Dec 5 anyway. If Fairbanks happens, do it in '
          'September, aim at Party in the Park in the first week (about Tue Sep 1 by arithmetic — NOT UAF\'s '
          'announcement), and back it with a Wood Center booth so the trip does not hinge on one date. If the '
          'budget is one trip, spend it in Anchorage instead and work Fairbanks by phone.',
  'gaps': ['⚠⚠ UAF COMMERCIAL BOOTH RATE — no commercial or non-university rate is published ANYWHERE; the fee '
           'page lists only department ($20/hr) and student-club ($15/hr) setup rates. Blocking for budget. '
           'Event Scheduling, (907) 474-6023. '
           'https://uaf.edu/woodcenter/services/event-scheduling/event-planning-resources/',
           '⚠⚠ UAF EVENT SPACE USE AGREEMENT — request the ACTUAL DOCUMENT. Insurance requirement and limit, '
           'deposit and cancellation terms are published nowhere; they live in this agreement. (907) 474-6023.',
           '⚠ PARTY IN THE PARK FALL 2026 DATE AND COMMUNITY-ORGANIZATION FEE — the entire pattern comes from a '
           '2017 news article. Neither date nor cost tier is published. Posts at https://www.uaf.edu/sli/; reach '
           'SLI through Wood Center, (907) 474-7034.',
           '⚠ UAF CLUB DIRECTORY (Nanook Engage) — NEVER READ. Whether a blockchain, crypto, fintech or '
           'investment club exists at UAF is completely unknown. Search Nanook Engage for blockchain, crypto, '
           'bitcoin, Web3, fintech, investment, FMA, ACM, data science. https://www.uaf.edu/sli/clubs/',
           'SLI and Dean of Students phone numbers — neither office publishes a phone, email, room or staff name '
           'on any page reached. Route both through Wood Center, (907) 474-7034, or the UA directory at '
           'https://directory.alaska.edu/.',
           'How a fly-in ambassador satisfies "must register in person with the UAF Scheduling Office" for the '
           'non-commercial route — a real friction point for a visiting org. (907) 474-6023.',
           'Whether ECON F350 Money and Banking runs in Fall 2026, and who teaches it. No UAF faculty member is '
           'named in this packet. https://catalog.uaf.edu/courses/econ/',
           'UAF BA / School of Management and Computer Science course listings were NOT READ — the "no blockchain '
           'course" finding covers ECON only. https://catalog.uaf.edu/courses/',
           'Fall 2026 UAF events — the Wood Center events calendar could not be read. '
           'https://www.uaf.edu/woodcenter/about/calendar.php'],
  'note': '⚠ DECEMBER IN FAIRBANKS. Interior Alaska in December means a few hours of usable daylight and severe '
          'cold, and UAF\'s last day of instruction is Sat Dec 5 with finals running through Sat Dec 12 anyway. '
          'There is no December window in Fairbanks worth flying for. Plan September or do not plan Fairbanks. '
          'Also note the Parks Highway drive from Anchorage — ~358 miles, 6–7 hours each way — is a FULL TRAVEL '
          'DAY in each direction from September on.'},

 # ---------------------------------------------------------------- 3. UAS
 {'state': 'Alaska',
  'name': 'University of Alaska Southeast — Juneau',
  'city': 'Juneau, AK',
  'type': 'Public',
  'tier': 'C — Opportunistic',
  'access': 3,
  'start': 'Mon Aug 24, 2026 — CONFIRMED on the UAS catalog calendar',
  'adddrop': 'Fri Sep 4, 2026 — deadline to drop with 100% tuition/fee refund, full-term courses. Deadline to '
             'withdraw, full-term: Fri Oct 30, 2026.',
  'fallbreak': 'Wed Nov 25, 2026 is a non-teaching day; campus CLOSED Nov 26–29. No separate October break.',
  'thanksgiving': 'Thu–Sun Nov 26–29, 2026 — campus closed',
  'lastclass': 'Sat Dec 5, 2026 — ⚠ UNVERIFIED. The UAS calendar page does not state it plainly; UAF\'s identical '
               'common-calendar term ends Sat Dec 5, so the inference is strong but unconfirmed.',
  'finals': 'Mon–Sat Dec 7–12, 2026. Grades due Wed Dec 16, noon.',
  'cal_url': 'https://catalog.uas.alaska.edu/calendar/',
  'cal_status': 'PARTIAL — start, add/drop, withdrawal, break, finals and grades-due dates all CONFIRMED on the '
                'UAS catalog; LAST DAY OF INSTRUCTION is not stated and is inferred from UAF. ⚠ The calendar '
                'carries its own caveat: "specific courses or programs may start or end on different dates" — '
                'UAS runs a lot of non-standard-length and distance courses.',
  'fair': 'UNKNOWN — no involvement fair could be confirmed, and the recurring pattern could not even be '
          'established',
  'fair_date': '⚠ NOTHING FOUND, AND THE PAGES THAT WOULD CARRY IT COULD NOT BE OPENED. Every UAS '
               'student-activities and campus-life URL attempted failed with robots.txt fetch errors: '
               '/student-activities/index.html, /juneau/campus-life/index.html, /juneau/student-activities/'
               'index.html, /juneau/activities/index.html, /juneau/campus-life/student-activities.html. No Fall '
               '2026 fair is confirmed and no pattern is established. Start at https://uas.alaska.edu/ and the '
               'directory at https://uas.alaska.edu/contacts/index.html, or just call (907) 796-6100.',
  'fair_outside': 'UNKNOWN — no published answer either way.',
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://uas.alaska.edu/',
  'policy': '⚠ NO UAS-SPECIFIC FACILITY-USE OR SOLICITATION POLICY COULD BE FOUND. The catalog\'s Student Rights '
            'and Responsibilities section is general rights language only and itself notes that the operative '
            'rules live in a student handbook that could not be located. In its absence UAS defaults to Regents\' '
            'P05.12.100 and P05.12.101 — which delegate rather than decide.',
  'policy_url': 'https://catalog.uas.alaska.edu/student-rights-responsibilities/',
  'policy_key': "⚠⚠ THE ACCESS RATING OF 3 HERE IS PROVISIONAL AND ASSIGNED BY DEFAULT, NOT BY EVIDENCE: THE "
                "GOVERNING CAMPUS POLICY COULD NOT BE RETRIEVED. No UAS facility-use or solicitation procedure, "
                "no fee schedule, no insurance terms, no anti-fronting language, no free-speech-zone designation "
                "and no payment-credential language could be found on any page — and every student-activities "
                "and campus-life URL attempted failed with robots.txt fetch errors. THERE IS NO PUBLISHED RULE AT "
                "UAS EITHER PERMITTING OR FORBIDDING AN OUTSIDE VENDOR. That ambiguity must be resolved BY A "
                "PHONE CALL, NOT BY READING. What the catalog does say, verbatim, is only general student-rights "
                "language (catalog.uas.alaska.edu/student-rights-responsibilities/): students have the right 'TO "
                "BE ABLE TO PROTEST ON UNIVERSITY PREMISES IN A MANNER WHICH DOES NOT OBSTRUCT OR DISRUPT "
                "TEACHING, RESEARCH, ADMINISTRATION, OR OTHER ACTIVITIES AUTHORIZED BY THE UNIVERSITY' and 'TO "
                "ORGANIZE AND JOIN ASSOCIATIONS TO PROMOTE THEIR COMMON AND LAWFUL INTERESTS.' The same page "
                "states that 'INFORMATION REGARDING STUDENT RIGHTS AND RESPONSIBILITIES WILL BE SET FORTH IN "
                "STUDENT HANDBOOKS' — so the operative rules are in a handbook that could not be located. Note "
                "neither right reaches COMMERCIAL speech by an outside entity, which is what DGD is. IN THE "
                "ABSENCE OF A CAMPUS PROCEDURE, UAS DEFAULTS TO THE SYSTEMWIDE LAYER, WHICH DECIDES NOTHING: "
                "Regents' P05.12.100 (eff. 06-20-97) — facilities open to the public 'IN ACCORDANCE WITH USE "
                "PRIORITIES AND OTHER REQUIREMENTS AS MAY BE SET FORTH IN UNIVERSITY REGULATION AND CAMPUS "
                "PROCEDURES' — and P05.12.101 (eff. 06-20-97) — 'All canvassing, peddling, or solicitation on "
                "university grounds or in university buildings will be SUBJECT TO UNIVERSITY REGULATION AND "
                "CAMPUS PROCEDURES AS TO TIME, MANNER, AND PLACE.' Both punt to a campus procedure that, at UAS, "
                "nobody has been able to find. Also live here: P09.07.030 viewpoint neutrality for student "
                "organizations, and P09.07.040.C's requirement that student organizations 'use university "
                "business offices and practices for financial transactions' — which would block a UAS club from "
                "acting as a payment conduit for DGD exactly as it does at UAA and UAF. THE GAP: ask Damian "
                "Medina, Dean of Students, at (907) 796-6100 for the UAS student handbook and any facility-use "
                "or solicitation procedure. At a campus this small he will know the answer personally.",
  'sponsor_required': 'UNKNOWN — no published rule was found either requiring or excusing sponsorship. Assume '
                      'approval is needed until Damian Medina says otherwise. (907) 796-6100.',
  'clubs': [('⚠ UNCLOSED GAP — NO UAS CLUB DIRECTORY WAS REACHED',
             'Nothing can be said about UAS clubs. Given UAS Juneau\'s size and program mix — NO computer science '
             'and NO engineering school — the prior probability of a blockchain, fintech or investment club is '
             'low, but it was NOT verified either way. Ask the Dean of Students.',
             'https://uas.alaska.edu/')],
  'faculty': [('⚠ Damian Medina',
               'DEAN OF STUDENTS, JUNEAU CAMPUS — THE CORRECT SINGLE POINT OF CONTACT FOR ALL OF UAS. At a campus '
               'this small the Dean of Students will personally know the outside-vendor answer; there is no '
               'separate events bureaucracy to route through. One call to him can close the involvement fair, '
               'clubs, courses, solicitation policy and every missing individual number at once. ⚠ His direct '
               'number is NOT extractable: the Dean of Students page renders each person\'s contact behind a '
               '"View profile and contact info" link that did not expand — the details ARE on the site but could '
               'not be read. No number published — look up here; reach him on the UAS main line.',
               'Dean of Students, Juneau',
               'no number published — look up here; reach via UAS main line (907) 796-6100',
               'https://uas.alaska.edu/dean-of-students/index.html'),
              ('UAS main / Admissions line',
               'THE ONLY CONFIRMED NUMBER AT UAS, cited on two catalog pages. Ask for Damian Medina, Dean of '
               'Students.',
               'UAS Juneau',
               '(907) 796-6100 (main line)',
               'https://catalog.uas.alaska.edu/student-services/'),
              ('Sean McCarthy (he/him)',
               'Director of Residence Life, Juneau. Contact hidden behind the same "View profile and contact '
               'info" link. No number published — look up here.',
               'Residence Life, Juneau',
               'no number published — look up here; or (907) 796-6100',
               'https://uas.alaska.edu/dean-of-students/index.html'),
              ('Randy Nutting',
               'Records and Registration Manager — SITKA campus, not Juneau. Carried across because he is one of '
               'only three named UAS staff confirmed on a live page. No number published — look up here.',
               'Records and Registration, Sitka',
               'no number published — look up here; or (907) 796-6100',
               'https://uas.alaska.edu/dean-of-students/index.html'),
              ('(UAS faculty)',
               'NONE IDENTIFIED AND NONE NAMED. The UAS directory at https://uas.alaska.edu/contacts/index.html '
               'was robots-blocked on every attempt but is a working people-search on a normal connection. No '
               'number published — look up here.',
               'UAS',
               'no number published — look up here; or (907) 796-6100',
               'https://uas.alaska.edu/contacts/index.html')],
  'courses': [('(UAS course catalog)',
               '⚠ NOT CHECKED — UNCLOSED GAP. Course descriptions are at '
               'https://catalog.uas.alaska.edu/course-descriptions/ and the full catalog PDF at '
               '"https://catalog.uas.alaska.edu/pdf/Final UAS 2026-2027 Catalog.pdf". With no computer science '
               'and no finance school, expect little — but nothing was verified either way.',
               'https://catalog.uas.alaska.edu/course-descriptions/')],
  'events': [('(UAS events)',
              '⚠ UNCLOSED GAP — nothing found. No involvement fair, career fair, hackathon or speaker series '
              'could be confirmed, and the pages that would carry them were all robots-blocked.',
              'https://uas.alaska.edu/')],
  'play': 'Skip it — and say so plainly rather than hedging. UAS Juneau is the smallest campus in the UA system, '
          'its enrollment mix is heavily distance and online, it has NO computer science and NO engineering '
          'school, and it is NOT REACHABLE BY ROAD FROM ANYWHERE — not from Anchorage, not from Fairbanks, not '
          'from the Lower 48. Getting there means a flight or the Alaska Marine Highway ferry, for the weakest '
          'confirmed audience in the state at a campus where no solicitation policy, no fee schedule, no club '
          'directory and no involvement fair could be found at all. JUNEAU DOES NOT JUSTIFY A PLANE TICKET. Work '
          'it entirely by phone: one call to (907) 796-6100, ask for DAMIAN MEDINA, DEAN OF STUDENTS. That is the '
          'single best door and probably the only one — at a campus this small he will personally know whether an '
          'outside organization can table, what the handbook says, whether an involvement fair exists, and who '
          'teaches anything finance-adjacent. Ask him for the UAS student handbook and any facility-use '
          'procedure, since neither is findable online. If he says yes and someone is already in Juneau, it is '
          'cheap to act on; if not, spend the travel budget on a SECOND Anchorage visit timed to APU\'s Module II '
          'start on Oct 21 instead. Note the access rating of 3 here is a DEFAULT ASSIGNED FOR MISSING POLICY, '
          'not a judgement that UAS is moderately open — nobody knows what UAS permits.',
  'gaps': ['⚠⚠ THE ENTIRE UAS PICTURE — involvement fair, clubs, courses, solicitation policy, facility-use '
           'procedure, fees, and every individual phone number. ONE CALL CLOSES MOST OF IT: (907) 796-6100, ask '
           'for Damian Medina, Dean of Students.',
           '⚠ NO UAS SOLICITATION OR FACILITY-USE POLICY EXISTS ON THE WEB THAT COULD BE FOUND — the access '
           'rating of 3 is provisional and assigned by default. The catalog says the operative rules are in a '
           'student handbook that could not be located. Ask the Dean of Students for it. '
           'https://catalog.uas.alaska.edu/student-rights-responsibilities/',
           '⚠ ROBOTS-BLOCKED THROUGHOUT: https://uas.alaska.edu/contacts/index.html, '
           'https://uas.alaska.edu/student-activities/, https://uas.alaska.edu/juneau/campus-life/index.html, '
           '/juneau/student-activities/index.html, /juneau/activities/index.html, '
           '/juneau/campus-life/student-activities.html. All work on a normal browser connection.',
           'Direct phone numbers for Damian Medina, Sean McCarthy and Randy Nutting — present on the Dean of '
           'Students page behind a "View profile and contact info" link that did not expand to research tooling. '
           'https://uas.alaska.edu/dean-of-students/index.html',
           'UAS last day of instruction — the calendar does not state it; Sat Dec 5 is inferred from UAF\'s '
           'identical common-calendar term. https://catalog.uas.alaska.edu/calendar/',
           'UAS course catalog was never checked. https://catalog.uas.alaska.edu/course-descriptions/'],
  'note': '⚠ NO ROAD TO JUNEAU. There is no highway to Juneau from Anchorage, Fairbanks or the Lower 48 — access '
          'is by air or the Alaska Marine Highway ferry only. A driving tour cannot include this campus under any '
          'routing. Note also that UAS is one of THREE SEPARATELY-ACCREDITED UNIVERSITIES in the University of '
          'Alaska system (with UAA and UAF) — it is not a branch campus of either, and UAA/UAF staff cannot '
          'authorize anything here.'},

 # ---------------------------------------------------------------- 4. APU
 {'state': 'Alaska',
  'name': 'Alaska Pacific University',
  'city': 'Anchorage, AK',
  'type': 'Private',
  'tier': 'C — Opportunistic',
  'access': 3,
  'start': '⚠ Mon Aug 24, 2026 for Full semester, Block AND Module I — but MODULE II STUDENTS DO NOT ARRIVE UNTIL '
           'WED OCT 21, 2026. A single September visit reaches only part of APU\'s student body.',
  'adddrop': '⚠ Full semester: Fri Aug 28, 2026, 5 p.m. — A FULL WEEK EARLIER THAN THE UA CAMPUSES\' Sep 4, so '
             'the settling-in window is shorter. Block: Tue Aug 25. Module II: Fri Oct 23.',
  'fallbreak': 'None listed. Labor Day Mon Sep 7, 2026 — college closed.',
  'thanksgiving': 'Wed–Fri Nov 25–27, 2026 (⚠ note this differs from the UA campuses\' Nov 26–29)',
  'lastclass': '⚠ SPLIT BY FORMAT: Block classes END FRI SEP 18, 2026. Full semester and Module II end Fri Dec 11, '
               '2026. Last day to withdraw: Block Sep 14; Full semester Nov 20; Module II Dec 2.',
  'finals': '⚠ NO DISTINCT FINALS WEEK IS LISTED on the APU calendar — exams appear to sit inside the final week '
            'of instruction. Grades due Fri Dec 18, 2026, 8:00 a.m.',
  'cal_url': 'https://www.alaskapacific.edu/academics/academic-calendar/',
  'cal_status': 'CONFIRMED — ⚠ DISTINCTIVE SYSTEM, FLAG THIS: APU does NOT run conventional semesters. It runs '
                'FULL SEMESTER, BLOCK and MODULE formats SIMULTANEOUSLY with staggered start dates. Block '
                'compresses an entire course into roughly Aug 24 – Sep 18; Module I starts Aug 24 and Module II '
                'starts Oct 21. It is the only calendar oddity in Alaska and the only campus where one visit '
                'misses a large share of students.',
  'fair': 'NONE FOUND — no involvement fair, org fair or welcome-week tabling event is published anywhere '
          'reachable',
  'fair_date': '⚠ NOTHING PUBLISHED. https://www.alaskapacific.edu/student-life/ describes recreation facilities '
               'and outdoor programs and lists NO clubs, NO events, NO staff and NO contacts. No cost tiers, no '
               'application process, and no URL where a fair would post. Given APU\'s size it is entirely '
               'possible NO FORMAL FAIR EXISTS. Ask ASAPU student government directly at (907) 564-8283.',
  'fair_outside': 'UNKNOWN — nothing published. The commercial route at APU is not a fair at all: it is '
                  'Conferencing Services, (907) 564-8078, which exists precisely to rent APU space to outside '
                  'parties.',
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://www.alaskapacific.edu/student-life/',
  'policy': '⚠ NO PUBLISHED APU SOLICITATION OR FACILITY-USE POLICY COULD BE FOUND. APU is a PRIVATE institution '
            'and is NOT part of the University of Alaska system — no Regents\' policy applies to it at all. '
            'Access is purely contractual, through Conferencing Services.',
  'policy_url': 'https://www.alaskapacific.edu/directory/',
  'policy_key': "⚠⚠ THE ACCESS RATING OF 3 HERE IS PROVISIONAL: THE GOVERNING POLICY COULD NOT BE RETRIEVED "
                "BECAUSE NO PUBLISHED APU SOLICITATION OR FACILITY-USE POLICY WAS FINDABLE, and "
                "https://www.alaskapacific.edu/contact-us/ RETURNED A 403. ⚠ CAPTURE THIS HONESTLY: APU IS A "
                "PRIVATE INSTITUTION. PUBLIC-FORUM DOCTRINE DOES NOT APPLY. REGENTS' POLICY DOES NOT APPLY — APU "
                "IS NOT PART OF THE UNIVERSITY OF ALASKA SYSTEM, and nothing in P05.12.100, P05.12.101 or Chapter "
                "09.07 binds it. Whatever campus free-expression statute Alaska may or may not have (see the UAA "
                "record — IT COULD NOT BE CONFIRMED TO EXIST) would, in the typical drafting, reach PUBLIC "
                "institutions only. CONSEQUENCE: APU MAY EXCLUDE DGD FOR ANY REASON OR NO REASON, INCLUDING THE "
                "SUBJECT MATTER OF THE PRODUCT. THERE IS NO APPEAL, NO FORUM ARGUMENT, AND NO 'BUT THE POLICY "
                "SAYS.' Access here is purely discretionary and purely contractual. THE PRACTICAL ROUTE IS "
                "COMMERCIAL: CONFERENCING SERVICES, (907) 564-8078, Carr-Gottstein Academic Center Rm 225, which "
                "exists to rent APU space to outside parties. ASK THEM FOR: the facility-use agreement, rates, "
                "the insurance requirement and limit, and deposit and cancellation terms — NONE of which are "
                "published. ⚠ NO ANTI-FRONTING LANGUAGE, NO FREE-SPEECH ZONE, AND NO PAYMENT-CREDENTIAL OR "
                "ON-SITE-CONTRACT LANGUAGE WAS FOUND — but at a private institution these would be CONTRACT "
                "TERMS, NOT PUBLISHED POLICY, so their absence from the web is EXPECTED RATHER THAN INFORMATIVE. "
                "Do not read silence as permission here; read it as 'the terms are in a document you have not "
                "seen yet.' ONE MORE STRUCTURAL NOTE: APU'S DIRECTORY PUBLISHES DEPARTMENTAL PHONE NUMBERS BUT NO "
                "INDIVIDUAL NAMES, TITLES OR EMAILS. At APU you will be calling OFFICES, NOT PEOPLE — write the "
                "script accordingly.",
  'sponsor_required': 'UNKNOWN — nothing is published. The realistic route is not sponsorship at all but a '
                      'commercial rental through Conferencing Services, (907) 564-8078. A student-side sponsor '
                      'route would run through ASAPU, (907) 564-8283, which is the only confirmed student body '
                      'on campus.',
  'clubs': [('⚠ ASAPU (Associated Students of Alaska Pacific University)',
             'THE ONLY CONFIRMED STUDENT BODY AT APU — student government, Atwood Center First Floor. The student '
             'sponsor route and the office most likely to know what events actually exist on this campus. '
             '(907) 564-8283.',
             'https://www.alaskapacific.edu/directory/'),
            ('⚠ NO CLUB DIRECTORY FOUND',
             'No blockchain, crypto, fintech, investment, ACM or data science club is confirmed at APU, and no '
             'club directory exists on the public site. With NO computer science program and NO finance major, '
             'expect none.',
             'https://www.alaskapacific.edu/student-life/')],
  'faculty': [('⚠ Conferencing Services',
               'RENTS APU SPACE TO OUTSIDE ENTITIES — THE DECISION-MAKER AT APU AND THE ONLY REAL COMMERCIAL '
               'CHANNEL ON THIS CAMPUS. Carr-Gottstein Academic Center, Rm 225. Ask for the facility-use '
               'agreement, rates, insurance requirement and limit, and deposit/cancellation terms — none of which '
               'are published anywhere.',
               'Conferencing Services',
               '(907) 564-8078',
               'https://www.alaskapacific.edu/directory/'),
              ('⚠ ASAPU Student Government',
               'Atwood Center, 1st Floor. The student sponsor route, and the people who will know whether APU '
               'holds any involvement fair at all — nothing is published either way.',
               'Associated Students of Alaska Pacific University',
               '(907) 564-8283',
               'https://www.alaskapacific.edu/directory/'),
              ('Facilities Management',
               'Physical setup, tables and power — the practical follow-up call once Conferencing Services says '
               'yes. Atwood Center, Basement.',
               'Facilities Management',
               '(907) 564-8320',
               'https://www.alaskapacific.edu/directory/'),
              ('Admissions',
               'Front door if all else fails. Carr Gottstein Academic Center, Ste 106.',
               'Admissions',
               '(907) 564-8248',
               'https://www.alaskapacific.edu/directory/'),
              ('Academic Support Center',
               'Atwood Center, 2nd Floor. Carried across for completeness.',
               'Academic Support',
               '(907) 564-8280',
               'https://www.alaskapacific.edu/directory/'),
              ('Chaplain',
               'Atwood Center, 1st Floor. Carried across for completeness.',
               'Chaplain',
               '(907) 564-8355',
               'https://www.alaskapacific.edu/directory/'),
              ('Alumni Association',
               'Carr Gottstein, 2nd Floor. Carried across for completeness.',
               'Alumni Association',
               '(907) 564-8282',
               'https://www.alaskapacific.edu/directory/'),
              ('Nordic Ski Center',
               'Atwood Center, Basement. Carried across for completeness — it is a fair indicator of what this '
               'campus is actually about.',
               'Nordic Ski Center',
               '(907) 564-8906',
               'https://www.alaskapacific.edu/directory/'),
              ('Campus Safety',
               '⚠ AFTER-HOURS EMERGENCIES ONLY — DO NOT USE FOR SCHEDULING.',
               'Campus Safety',
               '(907) 564-8888',
               'https://www.alaskapacific.edu/directory/'),
              ('(APU individuals)',
               '⚠ NO FACULTY OR STAFF MEMBER IS NAMED HERE AND NONE COULD BE — APU\'s directory publishes '
               'DEPARTMENTAL phone numbers but NO individual names, titles or emails. This is unusual and worth '
               'knowing before you write an outreach script: at APU you call offices, not people. Campus address '
               '4101 University Drive, Anchorage, AK 99508.',
               'Alaska Pacific University',
               'no individual contacts published — look up here; call the office lines above',
               'https://www.alaskapacific.edu/directory/')],
  'courses': [('Business Administration (major)',
               '⚠ APU\'s only finance-adjacent program, and note what it is NOT. The description emphasises '
               '"leadership, communication, organizational change and development, financial statements, and '
               'accounting" — a general-management and accounting program, NOT a finance or quantitative one. No '
               'investments course, no derivatives, no monetary economics is visible.',
               'https://www.alaskapacific.edu/academics/'),
              ('(Blockchain / crypto / fintech / CS / finance / economics)',
               '⚠ NONE. APU HAS NO FINANCE, ECONOMICS, COMPUTER SCIENCE OR TECHNOLOGY MAJOR. The full program '
               'list is: Alaska Native Governance, Business Administration, Community & Place-Based Education, '
               'Counseling Psychology, Creative & Professional Writing, Environmental Public Health, Health '
               'Sciences, Liberal Studies, Marine & Environmental Sciences, Nursing, Outdoor Studies, '
               'Environmental & Sustainability Studies. The course catalog was not read line by line, but with no '
               'CS and no finance major the probability of a digital-money course is very low.',
               'https://www.alaskapacific.edu/academics/')],
  'events': [('(APU events)',
              '⚠ UNCLOSED GAP — nothing found. No career fair, hackathon, startup week or speaker series, and no '
              'blockchain conference or research centre. APU\'s public web presence is thin. Ask ASAPU, '
              '(907) 564-8283.',
              'https://www.alaskapacific.edu/student-life/')],
  'play': 'Treat APU as a bolt-on, never a destination — and be clear-eyed that the audience fit is the weakest '
          'of the four campuses. Its one real advantage is geographic: 4101 University Drive is WALKING DISTANCE '
          'from UAA at 3211 Providence Drive, so adding it to an Anchorage trip costs almost nothing. Everything '
          'else argues down. APU is tiny; it has NO computer science, NO finance, NO economics and NO technology '
          'major; its institutional identity is Alaska Native governance, outdoor studies, environmental science '
          'and health; and as a PRIVATE institution it owes DGD nothing — no public-forum doctrine, no Regents\' '
          'policy, no appeal if it says no. The single best door is CONFERENCING SERVICES, (907) 564-8078, which '
          'exists specifically to rent APU space to outside parties; ask for the facility-use agreement, rates, '
          'insurance requirement and deposit/cancellation terms, because none of it is published. Second call: '
          'ASAPU student government, (907) 564-8283, the only confirmed student body on campus and the only '
          'people who can say whether any involvement fair exists at all. ⚠ TIMING IS THE ONE GENUINELY USEFUL '
          'INSIGHT HERE: APU runs Full semester, Block and Module formats simultaneously. BLOCK COURSES END SEP '
          '18 and MODULE II STUDENTS DO NOT ARRIVE UNTIL OCT 21 — so an August or early-September visit misses a '
          'whole second cohort. If APU matters at all, LATE OCTOBER IS THE MORE INTERESTING WINDOW THAN AUGUST, '
          'and that is the strongest argument for a second Anchorage trip rather than a Juneau flight.',
  'gaps': ['⚠⚠ APU FACILITY-USE AGREEMENT, RATES, INSURANCE REQUIREMENT AND DEPOSIT/CANCELLATION TERMS — NONE '
           'published; at a private institution these are contract terms, so absence from the web is expected. '
           'Conferencing Services, (907) 564-8078.',
           '⚠ DOES APU HOLD AN INVOLVEMENT FAIR AT ALL? Nothing is published anywhere reachable — no fair, no '
           'cost tier, no application process, and no URL where one would post. It is entirely possible none '
           'exists. ASAPU, (907) 564-8283.',
           'https://www.alaskapacific.edu/contact-us/ RETURNED A 403 — the general contact route is unreadable. '
           'Use the departmental numbers from the directory instead.',
           'APU publishes NO individual names, titles or emails anywhere — only departmental phone numbers. '
           'There is no way to address a named person before the first call. '
           'https://www.alaskapacific.edu/directory/',
           'APU course catalog was not read line by line — the "no crypto course" call is inference from the '
           'program list, not a full catalog read. https://www.alaskapacific.edu/academics/'],
  'note': '⚠ APU IS NOT PART OF THE UNIVERSITY OF ALASKA SYSTEM. It is commonly confused with UAA because the two '
          'sit adjacent in Anchorage and share the "Alaska" name — but APU is private, independently governed, '
          'and bound by no Regents\' policy. Do not cite P05.12.100, P05.12.101 or Chapter 09.07 to anyone at '
          'APU; it will read as not having done the homework.'},
]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; those sort last and never show a countdown.
DEADLINES = [

 ('2026-01-28', 'Jan 28, 2026', 'UA Anchorage',
  'PAST — Student Involvement Fair (spring edition), 10am–2pm, Student Union upper hallway',
  'Recorded because it establishes the pattern and the only confirmed contact: one fair per semester in the '
  'Student Union, 2921 Spirit Dr, Anchorage AK 99508, run by Club Council with Student Engagement, Community & '
  'Belonging. THE FALL 2026 DATE IS NOT PUBLISHED. Note this fair is for STUDENT ORGANIZATIONS — no '
  'outside-business tier exists, unlike Campus Kickoff. It will post at https://uaa.campusgroups.com/events, a '
  'JavaScript-rendered page that shows only template placeholders to non-browser tooling.',
  'https://uaa.campusgroups.com/web/rsvp_boot?id=377011',
  'uaa.sos@alaska.edu'),

 ('2026-08-22', 'Aug 22, 2026', 'UA Anchorage',
  '⚠⚠ CAMPUS KICKOFF — THE ONLY PUBLISHED FOR-PROFIT BOOTH IN ALASKA. $150 GREEN / $225 GOLD. DATE UNVERIFIED.',
  'Business tier $150 (Green) / $225 (Gold) for an approx. 10\' x 10\' space with table and chairs; Gold adds '
  'sponsor recognition and newspaper advertising. Student orgs FREE/$50, UAA departments FREE/$100, non-profits '
  '$110/$160. "Over 150 student clubs, departments, and businesses." ⚠ THE SAT AUG 22 DATE COMES FROM A '
  'THIRD-PARTY AGGREGATOR (frostboard.com), NOT FROM UAA, and UAA student press reports Kickoff "is moving" — '
  'confirm date AND venue before booking travel. ⚠ NO REGISTRATION DEADLINE, NO CONTACT AND NO BOOTH CONDUCT '
  'RULES ARE PUBLISHED: ask specifically whether a business booth may sell, solicit, collect contact information '
  'or run a giveaway, since fundraising approval is required wherever "monies (directly or indirectly) are '
  'exchanged for merchandise, service, entertainment or a chance at winning a prize."',
  'https://www.uaa.alaska.edu/students/traditions/kickoff-registration.cshtml',
  'uaa.sos@alaska.edu · switchboard (907) 786-1800 — ask for Student Life & Leadership'),

 ('2026-08-24', 'Aug 24, 2026', 'UA Fairbanks',
  'Classes begin — CONFIRMED on the UAF catalog calendar',
  'Usable Fairbanks window is Aug 24 – Nov 25. No separate October fall break; add/drop Sep 4; break Nov 26–29; '
  'last class Sat Dec 5; finals through Sat Dec 12. ⚠ December in Fairbanks is a few hours of daylight and deep '
  'cold — plan September or do not plan Fairbanks.',
  'https://catalog.uaf.edu/calendar/calendar.pdf',
  'Wood Center · uaf-woodcenter@alaska.edu · (907) 474-7034'),

 ('2026-08-24', 'Aug 24, 2026', 'UA Anchorage',
  '⚠ Classes begin — INFERRED FROM THE UA COMMON CALENDAR, NEVER READ ON A UAA PAGE',
  'Every UAA date in this packet is an inference from the UA Common Calendar, which UAF and UAS independently '
  'confirm. The UAA registrar calendar page is robots-blocked. Confirm before booking travel.',
  'https://www.uaa.alaska.edu/academics/office-of-academic-affairs/calendarsanddeadlines.cshtml',
  'Provost\'s Office (907) 786-1050'),

 ('2026-08-24', 'Aug 24, 2026', 'UA Southeast — Juneau',
  'Classes begin — CONFIRMED on the UAS catalog calendar',
  'Withdrawal deadline Oct 30; non-teaching day Nov 25; campus closed Nov 26–29; finals Dec 7–12; grades due '
  'Dec 16 noon. ⚠ The calendar warns "specific courses or programs may start or end on different dates" — UAS '
  'runs many non-standard-length and distance courses.',
  'https://catalog.uas.alaska.edu/calendar/',
  '(907) 796-6100 — ask for Damian Medina, Dean of Students'),

 ('2026-08-24', 'Aug 24, 2026', 'Alaska Pacific',
  '⚠ Classes begin — FULL SEMESTER, BLOCK AND MODULE I ALL START TODAY',
  'APU runs three formats simultaneously. Block compresses a whole course into Aug 24 – Sep 18. Module II does '
  'NOT begin until Oct 21. A single visit here reaches only part of the student body.',
  'https://www.alaskapacific.edu/academics/academic-calendar/',
  'ASAPU (907) 564-8283'),

 ('2026-08-25', 'Aug 25, 2026', 'Alaska Pacific',
  'Block format add/drop deadline',
  'The Block cohort is locked in from today and gone by Sep 18.',
  'https://www.alaskapacific.edu/academics/academic-calendar/',
  'ASAPU (907) 564-8283'),

 ('2026-08-28', 'Aug 28, 2026', 'Alaska Pacific',
  '⚠ Full-semester add/drop deadline, 5:00 p.m. — A FULL WEEK EARLIER THAN THE UA CAMPUSES',
  'APU settles a week before UAA/UAF/UAS (Sep 4). The window for reaching students while schedules are still '
  'fluid is correspondingly shorter here.',
  'https://www.alaskapacific.edu/academics/academic-calendar/',
  'ASAPU (907) 564-8283'),

 ('2026-09-01', 'about Tue Sep 1, 2026', 'UA Fairbanks',
  '⚠ PARTY IN THE PARK — INFERRED, NOT ANNOUNCED. UAF\'S FALL INVOLVEMENT FAIR.',
  'Pattern from a 2017 UAF news article (nine years stale, internally consistent): the TUESDAY OF THE FIRST WEEK '
  'OF CLASSES, noon–2 p.m., setup 11 a.m., Constitution Park by the bookstore, moving indoors to Wood Center in '
  'poor weather. ⚠ OUTSIDE ORGANIZATIONS ARE EXPLICITLY WELCOME: "a great way for new and returning students to '
  'connect with student clubs, UAF departments and FAIRBANKS COMMUNITY ORGANIZATIONS," with a dedicated path — '
  '"if you are a community organization without a UA email, please register here." COST TIERS FOR COMMUNITY '
  'ORGANIZATIONS ARE NOT PUBLISHED. The Fall 2026 date will post at https://www.uaf.edu/sli/. DO NOT BOOK TRAVEL '
  'ON THIS ARITHMETIC.',
  'https://news.uaf.edu/party-in-the-park-aug-29/',
  'SLI publishes no phone — reach via Wood Center (907) 474-7034'),

 ('2026-09-04', 'Sep 4, 2026', 'UA Fairbanks',
  'Add/drop deadline — 5:00 p.m. in person, 11:59 p.m. at UAOnline',
  'Same date at UAA and UAS under the shared UA Common Calendar (confirmed at UAF and UAS, inferred at UAA).',
  'https://catalog.uaf.edu/calendar/calendar.pdf',
  'UAF Event Scheduling (907) 474-6023'),

 ('2026-09-04', 'Sep 4, 2026', 'UA Southeast — Juneau',
  'Deadline to drop with 100% tuition/fee refund, full-term courses',
  'Confirmed on the UAS catalog calendar.',
  'https://catalog.uas.alaska.edu/calendar/',
  '(907) 796-6100'),

 ('2026-09-07', 'Sep 7, 2026', 'Alaska Pacific',
  'Labor Day — college closed',
  'Note APU closes; the UA campuses\' calendar does not list this.',
  'https://www.alaskapacific.edu/academics/academic-calendar/',
  'ASAPU (907) 564-8283'),

 ('2026-09-14', 'Sep 14, 2026', 'Alaska Pacific',
  'Block format — last day to withdraw',
  'The Block course ends four days later.',
  'https://www.alaskapacific.edu/academics/academic-calendar/',
  'ASAPU (907) 564-8283'),

 ('2026-09-18', 'Sep 18, 2026', 'Alaska Pacific',
  '⚠ BLOCK CLASSES END — A WHOLE APU COHORT IS GONE FROM CAMPUS AFTER TODAY',
  'Anything aimed at APU Block students must land between Aug 24 and Sep 18. The next arrival is Module II on '
  'Oct 21.',
  'https://www.alaskapacific.edu/academics/academic-calendar/',
  'ASAPU (907) 564-8283'),

 ('2026-10-21', 'Oct 21, 2026', 'Alaska Pacific',
  '⚠ MODULE II BEGINS — A SECOND, SEPARATE APU COHORT ARRIVES TWO MONTHS INTO THE TERM',
  'This is the strongest argument for a SECOND Anchorage trip in late October rather than a Juneau flight: a '
  'cohort of APU students who were not on campus in August starts today, and UAA is walking distance away.',
  'https://www.alaskapacific.edu/academics/academic-calendar/',
  'ASAPU (907) 564-8283 · Conferencing Services (907) 564-8078'),

 ('2026-10-23', 'Oct 23, 2026', 'Alaska Pacific',
  'Module II add/drop deadline',
  'Two days after the Module II cohort arrives.',
  'https://www.alaskapacific.edu/academics/academic-calendar/',
  'ASAPU (907) 564-8283'),

 ('2026-10-30', 'Oct 30, 2026', 'UA Southeast — Juneau',
  'Deadline to withdraw, full-term courses',
  'Confirmed on the UAS catalog calendar.',
  'https://catalog.uas.alaska.edu/calendar/',
  '(907) 796-6100'),

 ('2026-11-20', 'Nov 20, 2026', 'Alaska Pacific',
  'Full semester — last day to withdraw',
  'Confirmed on the APU academic calendar.',
  'https://www.alaskapacific.edu/academics/academic-calendar/',
  'ASAPU (907) 564-8283'),

 ('2026-11-25', 'Nov 25, 2026', 'Alaska Pacific / UA Southeast',
  'APU Thanksgiving break begins (Nov 25–27); UAS non-teaching day',
  '⚠ APU and the UA campuses break on DIFFERENT DAYS: APU Nov 25–27, the three UA campuses Nov 26–29. Nothing '
  'usable in Anchorage across that whole stretch.',
  'https://www.alaskapacific.edu/academics/academic-calendar/',
  'ASAPU (907) 564-8283'),

 ('2026-11-26', 'Nov 26–29, 2026', 'All three UA campuses',
  'Fall break / Thanksgiving — no classes, most offices closed',
  'UA folds fall break and Thanksgiving into one Thu–Sun block; there is no separate October fall break at any '
  'UA campus. Confirmed at UAF and UAS, inferred at UAA.',
  'https://catalog.uaf.edu/calendar/calendar.pdf',
  'UAF Wood Center (907) 474-7034 · UAS (907) 796-6100'),

 ('2026-12-02', 'Dec 2, 2026', 'Alaska Pacific',
  'Module II — last day to withdraw',
  'Confirmed on the APU academic calendar.',
  'https://www.alaskapacific.edu/academics/academic-calendar/',
  'ASAPU (907) 564-8283'),

 ('2026-12-05', 'Dec 5, 2026', 'UA Fairbanks',
  'Last day of instruction (a SATURDAY)',
  'Confirmed at UAF; the same date is inferred for UAA and UAS, whose calendars do not state it plainly.',
  'https://catalog.uaf.edu/calendar/calendar.pdf',
  '(907) 474-7034'),

 ('2026-12-07', 'Dec 7–12, 2026', 'All three UA campuses',
  '⚠ FINALS — UA EXAMINES THROUGH SATURDAY DEC 12',
  'Confirmed at UAF and UAS, inferred at UAA. Nothing worth doing on a UA campus after about Nov 25.',
  'https://catalog.uaf.edu/calendar/calendar.pdf',
  'UAF (907) 474-7034 · UAS (907) 796-6100 · UAA Provost (907) 786-1050'),

 ('2026-12-11', 'Dec 11, 2026', 'Alaska Pacific',
  'Full semester and Module II classes end — ⚠ NO DISTINCT FINALS WEEK IS LISTED',
  'Exams appear to sit inside the final week of instruction. Grades due Dec 18, 8:00 a.m.',
  'https://www.alaskapacific.edu/academics/academic-calendar/',
  'ASAPU (907) 564-8283'),

 ('2026-12-16', 'Dec 16, 2026', 'UA Southeast — Juneau',
  'Grades due, noon — UAS term fully closed',
  'End of the Alaska fall window.',
  'https://catalog.uas.alaska.edu/calendar/',
  '(907) 796-6100'),

 ('', 'BEFORE BOOKING ANY ALASKA TRAVEL', 'All Alaska campuses',
  '⚠⚠ ALASKA IS NOT A TOUR — MAKE THE ROUTING DECISION FIRST',
  'Anchorage to Fairbanks is ~358 road miles, 6–7 hours on the Parks Highway, in Sept–Dec weather running rain to '
  'ice — A FULL TRAVEL DAY EACH WAY, or a separate flight. THERE IS NO ROAD TO JUNEAU from anywhere: UAS is '
  'reachable only by air or the Alaska Marine Highway ferry. APU is the ONLY campus co-located with another — '
  '4101 University Drive, walking distance from UAA at 3211 Providence Drive. What Alaska supports is ONE '
  'ANCHORAGE TRIP covering UAA and APU on foot, a separate yes/no on a Fairbanks flight, and Juneau handled '
  'entirely by phone. If the budget is one trip, it is Anchorage — and the better second trip is a return to '
  'Anchorage timed to APU\'s Module II start on Oct 21, not a plane ticket to Juneau.',
  'https://www.uaa.alaska.edu/contact.cshtml',
  'UAA switchboard (907) 786-1800'),

 ('', 'Before any UAA booth — call this week', 'UA Anchorage',
  '⚠⚠ CONFIRM CAMPUS KICKOFF: DATE, VENUE, REGISTRATION DEADLINE AND BOOTH CONDUCT RULES',
  'Three blocking unknowns on one call. (1) DATE AND VENUE: Sat Aug 22 comes from a third-party aggregator and '
  'UAA student press reports Kickoff "is moving." (2) REGISTRATION DEADLINE: the rate card publishes $150/$225 '
  'Business pricing but NO deadline, NO phone, NO email and NO named contact. (3) BOOTH CONDUCT: the page says '
  'nothing about whether a vendor may sell, solicit, collect contact information or run a giveaway — for a crypto '
  'project that is the whole question, and fundraising approval is separately required wherever "monies '
  '(directly or indirectly) are exchanged for merchandise, service, entertainment or a chance at winning a '
  'prize." The office that runs Kickoff publishes NO phone at all (its pages are robots-blocked); go through the '
  'switchboard.',
  'https://www.uaa.alaska.edu/students/traditions/kickoff-registration.cshtml',
  'uaa.sos@alaska.edu · switchboard (907) 786-1800 — ask for Student Life & Leadership'),

 ('', 'Before booking UAA travel', 'UA Anchorage',
  '⚠ CONFIRM THE UAA FALL 2026 CALENDAR — EVERY UAA DATE IN THIS PACKET IS INFERRED',
  'The UAA registrar calendar page is ROBOTS-BLOCKED (the robots fetch itself times out; not a 403). UAA states '
  'its calendars are "set in coordination with the UA Common Calendar," and UAF and UAS Fall 2026 dates — both '
  'independently confirmed — are identical to each other. The inference is strong. It is still an inference.',
  'https://www.uaa.alaska.edu/academics/faculty-services/dates/academic.cshtml',
  'Provost\'s Office (907) 786-1050'),

 ('', 'Before any UAF table', 'UA Fairbanks',
  '⚠⚠ GET THE UAF COMMERCIAL BOOTH RATE AND THE EVENT SPACE USE AGREEMENT',
  'NO commercial or non-university rate is published anywhere at UAF — the fee page lists only department '
  '($20.00/hr) and student-club ($15.00/hr) setup/teardown rates, AV $10 flat, and additional building hours '
  '$75.00/hr with a 3-hour minimum and ten working days\' notice. Request the ACTUAL Event Space Use Agreement: '
  'the insurance requirement and limit, deposit and cancellation terms exist nowhere on the public site and will '
  'live in that document. On the same call: confirm that Wood Center commercial booth space is bookable '
  'Tuesday–Thursday for Fall 2026, that "Tabling at Wood Center" remains pre-cleared from Events Committee '
  'approval, and HOW A FLY-IN AMBASSADOR SATISFIES THE POLICY\'S "MUST REGISTER IN PERSON" LANGUAGE. Standard '
  'processing is 48 hours. ABSENCE OF PUBLISHED TEXT IS NOT PERMISSION — also ask explicitly whether any '
  'anti-fronting rule exists, since none was found.',
  'https://www.uaf.edu/woodcenter/services/event-scheduling/',
  'uaf-event-schedule@alaska.edu · (907) 474-6023'),

 ('', 'Ahead of the first week at UAF', 'UA Fairbanks',
  '⚠ GET THE PARTY IN THE PARK FALL 2026 DATE AND THE COMMUNITY-ORGANIZATION FEE',
  'The entire pattern for UAF\'s fall involvement fair comes from a 2017 news article — NINE YEARS STALE. '
  'Outside organizations ARE explicitly welcome ("if you are a community organization without a UA email, please '
  'register here"), but no Fall 2026 date and no cost tier is published. It will post at https://www.uaf.edu/sli/. '
  '⚠ SLI publishes NO phone, email, room or staff name on any page — reach it through Wood Center, where it is '
  'physically located.',
  'https://www.uaf.edu/sli/',
  'Wood Center · uaf-woodcenter@alaska.edu · (907) 474-7034'),

 ('', 'One call closes most of UAS', 'UA Southeast — Juneau',
  '⚠⚠ CALL THE UAS DEAN OF STUDENTS — THE WHOLE CAMPUS IS AN UNCLOSED GAP',
  'No UAS solicitation policy, facility-use procedure, fee schedule, club directory or involvement fair could be '
  'found, and every student-activities and campus-life URL was robots-blocked. The access rating of 3 is a '
  'DEFAULT ASSIGNED FOR MISSING POLICY, not a judgement. Ask DAMIAN MEDINA, Dean of Students, Juneau, for: the '
  'UAS student handbook (the catalog says the operative rules live there), any facility-use or solicitation '
  'procedure, whether an outside for-profit may table, whether an involvement fair exists, and any finance-'
  'adjacent faculty. At a campus this small he will know all of it personally. ⚠ AND REMEMBER JUNEAU HAS NO ROAD '
  '— do not turn a yes into a plane ticket without a second reason to fly.',
  'https://uas.alaska.edu/dean-of-students/index.html',
  '(907) 796-6100 — ask for Damian Medina, Dean of Students'),

 ('', 'Before any APU commitment', 'Alaska Pacific',
  '⚠⚠ APU IS PRIVATE — GET THE CONTRACT, BECAUSE THERE IS NO POLICY TO APPEAL TO',
  'APU is NOT part of the University of Alaska system: no Regents\' policy applies, no public-forum doctrine '
  'applies, and APU may exclude DGD for any reason or no reason including the subject matter of the product. No '
  'published solicitation or facility-use policy exists and the contact page returns a 403. Access is purely '
  'contractual. Call CONFERENCING SERVICES — the office that exists to rent APU space to outside parties — and '
  'ask for the facility-use agreement, rates, insurance requirement and limit, and deposit/cancellation terms, '
  'none of which are published. Separately ask ASAPU, (907) 564-8283, whether APU holds any involvement fair at '
  'all; nothing is published either way and it is possible none exists. ⚠ APU publishes DEPARTMENTAL numbers '
  'only, NO individual names or emails — you will be calling offices, not people.',
  'https://www.alaskapacific.edu/directory/',
  'Conferencing Services (907) 564-8078 · ASAPU (907) 564-8283'),

 ('', 'Academic door — anytime', 'UA Anchorage',
  '⚠ CALL CBPP ABOUT BA A491A STUDENT MANAGED PORTFOLIO AND ECON A350 MONEY AND BANKING',
  'The deepest finance curriculum in Alaska sits in one college: twelve finance courses including Financial '
  'Derivatives, Bond Market Analysis and a REAL-MONEY STUDENT MANAGED PORTFOLIO (BA A491A) — the most '
  'crypto-curious audience in the state — plus ECON A350 Money and Banking, which "examines... HOW MONEY IS '
  'CREATED, the role of central banks in financial regulation, and the implementation of monetary policy." A '
  'guest lecture is free, non-commercial, and sits entirely outside the solicitation regime. ⚠ NO UAA FACULTY '
  'MEMBER IS NAMED IN THIS PACKET — the CBPP faculty directory is robots-blocked and nobody was confirmed on a '
  'live page. Ask this line who teaches both courses in Fall 2026, and whether they run at all (catalog listing '
  'is not term offering).',
  'https://catalog.uaa.alaska.edu/coursedescriptions/econ/',
  'CBPP (907) 786-4100'),

 ('', 'Monitor — one browser session closes several gaps', 'All Alaska campuses',
  '⚠ JAVASCRIPT-RENDERED AND ROBOTS-BLOCKED PAGES AN AMBASSADOR CAN OPEN THAT RESEARCH TOOLING COULD NOT',
  'None of these are broken sites — they are limitations of automated fetching, and a normal browser resolves '
  'them in minutes. (1) directory.uaa.alaska.edu and directory.alaska.edu — real campus-wide people-and-'
  'department search; will resolve most missing UAA/UAF/UAS individual numbers, including UAA Event Services, '
  'UAA Student Activities, UAF SLI and the UAF Dean of Students. (2) uas.alaska.edu/contacts/index.html and the '
  'UAS Dean of Students page, where contacts hide behind a "View profile and contact info" link. (3) '
  'uaa.campusgroups.com/events and /club_signup — JavaScript-rendered; the events page shows only [eventName] '
  'and [date_text] placeholders to non-browser tooling, and this is where the Fall 2026 Involvement Fair date '
  'will appear. (4) NANOOK ENGAGE, UAF\'s club directory, which was never read at all — search it for '
  'blockchain, crypto, bitcoin, Web3, fintech, investment, FMA, ACM, data science. (5) Instagram @uaa_fnic, a '
  'possible UAA "Finance & Investments Club" that did not appear on the CampusGroups listing — it would be the '
  'best sponsor in the state.',
  'https://directory.alaska.edu/',
  'UAA switchboard (907) 786-1800 · UAF Wood Center (907) 474-7034'),

 ('', 'Monitor — statewide legal posture', 'All Alaska campuses',
  '⚠⚠ DO NOT ARGUE FREE SPEECH IN ALASKA, AND DO NOT ASSUME MAINLAND FINANCIAL-REGULATORY PARITY',
  'NO ALASKA CAMPUS FREE-EXPRESSION STATUTE COULD BE CONFIRMED TO EXIST — do not assert one does; absence of '
  'evidence here is a search limitation, not a finding. Check Alaska Statutes Title 14 (Education) and confirm '
  'with UA General Counsel before relying on any free-speech argument. What IS confirmed is weaker and purely '
  'internal: Regents\' P09.07.030, "No student organization will be denied registration...on the basis of the '
  'views espoused by its members," and the UAS catalog\'s student right "to be able to protest on university '
  'premises in a manner which does not obstruct or disrupt teaching, research, administration, or other '
  'activities." Both are INSTITUTIONAL POLICY, NOT STATUTE, and NEITHER REACHES COMMERCIAL SPEECH BY AN OUTSIDE '
  'ENTITY — which is exactly what DGD is. The commercial-contract route at UAA and UAF is far stronger and needs '
  'no legal theory at all. ⚠⚠ STATE REGULATORY: the research found NOTHING on Alaska\'s money-transmission or '
  'consumer-protection posture and did not search it to exhaustion — treat it as an OPEN QUESTION, not as parity '
  'with the mainland. Verify with the Alaska Division of Banking & Securities before any on-site activity that '
  'touches payments, sign-ups or wallet registrations. ⚠ Also note APU is PRIVATE and outside the UA system '
  'entirely — none of the Regents\' policy layer binds it.',
  'https://www.alaska.edu/bor/policy-regulations/chapter-09-07-student-organizations.php',
  'UA System / General Counsel — via UAA switchboard (907) 786-1800'),

 ('', 'Monitor — the channel nobody found', 'All Alaska campuses',
  '⚠ NO HACKATHON WAS FOUND ANYWHERE IN ALASKA — WORTH ONE MORE TARGETED PASS',
  'No hackathon, career fair date, startup week or Fall 2026 speaker series could be confirmed at ANY of the four '
  'campuses. That matters more than it looks: a student-run hackathon is the one channel that sidesteps campus '
  'commercial rules entirely, with no booth fee and no solicitation policy in the way. Given the research budget '
  'was exhausted, treat this as UNCLOSED rather than empty — check MLH\'s Alaska listings and the UAA and UAF '
  'computer-science department pages directly. UAA\'s Bartlett Lecture Series is the nearest confirmed '
  'speaker-series equivalent, but its page is STALE (Spring 2020 / Fall 2021 content) and no Fall 2026 schedule '
  'is published.',
  'https://www.uaa.alaska.edu/students/engage/activities-programs.cshtml',
  'UAA CBPP (907) 786-4100 · UAF Wood Center (907) 474-7034'),
]
