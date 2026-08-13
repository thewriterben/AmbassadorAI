"""Washington — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published at time of research — a gap to close by phone, not a finding of absence.
Schema: reference/data-schema.md
"""

STATE = 'Washington'

CAMPUSES = [{'state': 'Washington',
  'name': 'Washington State University — Spokane',
  'city': 'Spokane, WA',
  'type': 'Public (health sciences campus)',
  'tier': 'A — Named target (but poor fit)',
  'access': 1,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'UNVERIFIED',
  'fallbreak': '—',
  'thanksgiving': 'UNVERIFIED',
  'lastclass': 'UNVERIFIED',
  'finals': 'UNVERIFIED',
  'cal_url': 'https://registrar.wsu.edu/academic-calendar-light/',
  'cal_status': 'Term start CONFIRMED; detail UNVERIFIED (registrar calendar is a JS form)',
  'fair': 'None published — WSU Spokane claims 75+ RSOs but publishes no Fall 2026 involvement fair',
  'fair_date': 'UNVERIFIED',
  'fair_outside': '',
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://spokane.wsu.edu/studentinvolvement/registered-student-organizations/',
  'policy': 'Same statewide rules as Pullman — Chapter 504-35 WAC. Plus a campus-specific Facilities Use Agreement.',
  'policy_url': 'https://app.leg.wa.gov/wac/default.aspx?cite=504-35&full=true',
  'policy_key': "WAC 504-35-050(1): 'University facilities may not be used for private or commercial gain including, "
                "but not limited to: Commercial advertising; solicitation and merchandising.' WAC 504-35-024(1): no "
                'facility use without a reservation AND an executed written facility use agreement.',
  'sponsor_required': 'n/a — commercial use barred by WAC',
  'clubs': [('Health-professions organizations only',
             'Medicine, nursing, pharmacy student groups. NO blockchain/fintech/investment club.',
             'https://spokane.wsu.edu/studentinvolvement/registered-student-organizations/')],
  'faculty': [('HUB / Student Leadership & Involvement',
               'Office',
               '',
               'spokane.elc@wsu.edu',
               'https://spokane.wsu.edu/studentinvolvement/registered-student-organizations/')],
  'courses': [('—', 'No blockchain/crypto/fintech courses. Health-sciences curriculum only.', '')],
  'events': [('—', 'None relevant to this audience', '')],
  'play': "⚠ AUDIENCE MISMATCH — CORRECT THE TARGET LIST. WSU Spokane is WSU's HEALTH SCIENCES campus: College of "
          'Medicine, Nursing, Pharmacy, Medical Sciences. There is NO undergraduate business or CS program here. The '
          'population is graduate/professional health-science students. The business and CS students you want are at '
          'WSU PULLMAN, 75 miles south. Redirect this stop to Pullman.',
  'gaps': ['Full Fall 2026 calendar detail']},
 {'state': 'Washington',
  'name': 'Washington State University — Pullman',
  'city': 'Pullman, WA',
  'type': 'Public',
  'tier': 'A — Substitute for WSU Spokane',
  'access': 4,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'UNVERIFIED',
  'fallbreak': '—',
  'thanksgiving': 'UNVERIFIED',
  'lastclass': 'UNVERIFIED',
  'finals': 'UNVERIFIED',
  'cal_url': 'https://registrar.wsu.edu/academic-calendar-light/',
  'cal_status': 'Term start CONFIRMED; detail UNVERIFIED',
  'fair': 'All-Campus Picnic & Resource Fair (part of Week of Welcome, Aug 15–23, 2026)',
  'fair_date': '⚠ Fri Aug 21, 2026, 11am–2pm — CONFIRMED. Glenn Terrell Mall + CUB. THIS IS 10 DAYS OUT.',
  'fair_outside': "YES — WSU's own pages say the fair includes 'student organizations, WSU departments, and LOCAL "
                  "BUSINESSES'",
  'fair_cost': "⚠ RE-VERIFIED AUG 11, 2026 on the LIVE 2026 registration form: 'Participation Sponsorship: $200 (WOW "
               "only)' — picnic access. A separate 'Cougar Sponsorship: $1,000' covers all New Coug Orientation "
               'sessions PLUS the WOW resource fair (summer 2026 NCO sessions are at capacity; the Aug 21 picnic and '
               'Spring 2027 remain open). $0 for student orgs and departments.',
  'fair_deadline': 'NOT PUBLISHED — call 509-335-6674. ⚠ DO NOT CITE wow.wsu.edu/basic-info: verification found it '
                   "STALE, showing the fair as 'Friday, August 16,' which contradicts the official event page. Use "
                   'the registration form.',
  'fair_url': 'https://universityevents.wsu.edu/all-campus-picnic/',
  'policy': 'Chapter 504-35 WAC — Use of University Facilities; WAC 504-34-140 — Signs, posters, handbills',
  'policy_url': 'https://app.leg.wa.gov/wac/default.aspx?cite=504-35&full=true',
  'policy_key': "WAC 504-35-050(1): facilities 'may not be used for private or commercial gain including… Commercial "
                "advertising; solicitation and merchandising.' WAC 504-35-024(1): reservation + executed written "
                "facility use agreement required. WAC 504-35-026(1): fees 'based upon the actual costs, direct and "
                "indirect.' WAC 504-34-140: 'Distribution by means of offering materials to passers-by who indicate "
                "a willingness to accept them is allowed'… 'Distribution by means of accosting, confronting, "
                "detaining, or waylaying individuals or by hawking is PROHIBITED.' RSOs may 'seek out local "
                "businesses… to collaborate, partner with, or sponsor their event'; RSO tabling is free but must be "
                'reserved 2 WEEKS in advance. The Student Organizations Manual contains NO explicit ban on '
                'financial-product marketing.',
  'sponsor_required': 'Not for the paid picnic booth; RSO partnership is a separate route',
  'clubs': [('Association for Computing Machinery (ACM)',
             'EECS; workshops, interview prep, industry talks. Advisor listed: Venera Arnaoudova.',
             'https://school.eecs.wsu.edu/academics/student-clubs/'),
            ('Software Development Club', '', ''),
            ('Cyber Security Group (CSG)', '', ''),
            ('LeetCode Club @ WSU', '', ''),
            ('Linux Users Group', '', ''),
            ('IEEE', '', ''),
            ('NO blockchain/crypto/Web3 club found',
             'Finance/investment/econ clubs UNVERIFIED',
             'https://wsu.presence.io/organizations')],
  'faculty': [('University Events (owns the Resource Fair)',
               'Office',
               'Office of the President, Info Tech Bldg Rm 2004',
               'university.events@wsu.edu · 509-335-6674',
               'https://universityevents.wsu.edu/all-campus-picnic/'),
              ('Center for Student Organizations & Leadership (CSOL)',
               'Office',
               'CUB 320',
               'getinvolved@wsu.edu · 509-335-9667',
               ''),
              ('Space/table reservations',
               'Office',
               '',
               'scheduling.wsu.edu',
               'https://scheduling.wsu.edu/campus-calendars/')],
  'courses': [('—',
               'No blockchain/cryptocurrency/fintech catalog course confirmed at WSU.',
               'https://catalog.wsu.edu/')],
  'events': [('Week of Welcome (WOW)', 'Aug 15–23, 2026', 'https://wow.wsu.edu/'),
             ('WoW Student Employment Fair',
              'Aug 18, 2026, 1pm, CUB',
              'https://events.wsu.edu/location/wsu-pullman/2026/08/'),
             ('All-Campus Picnic & Resource Fair',
              '⚠ Fri Aug 21, 2026, 11am–2pm, Glenn Terrell Mall — CONFIRMED on the official event page Aug 11, 2026',
              'https://universityevents.wsu.edu/all-campus-picnic/'),
             ('Table host registration form',
              'Live 2026 form — the authoritative source for the $200 figure',
              'https://futurecoug.wsu.edu/register/?id=085d4eb1-864f-4b38-ae89-d661dfaa4b8a')],
  'play': '⚠ ACT WITHIN 48 HOURS OR LOSE THIS. The All-Campus Picnic is Aug 21 — ten days out — and WSU explicitly '
          "admits local businesses at ~$200. No published deadline means call, don't email: 509-335-6674. WSU is "
          'also the ONLY campus in WA/OR on semesters, so its term is five weeks old before the quarter schools even '
          'start. Sequence Pullman first (late Aug), everywhere else second (late Sept).',
  'gaps': ['Fall 2026 add/drop, Thanksgiving, finals dates',
           'Picnic table signup deadline',
           'Confirmed 2026 booth fee',
           'Finance/investment club roster']},
 {'state': 'Washington',
  'name': 'Gonzaga University',
  'city': 'Spokane, WA',
  'type': 'Private (Jesuit)',
  'tier': 'A — Named target',
  'access': 1,
  'start': 'Tue Sep 1, 2026 (Monday-only classes meet Mon Aug 31)',
  'adddrop': 'Add Sep 9; Drop Sep 11, 2026',
  'fallbreak': '—',
  'thanksgiving': 'Nov 25–27, 2026',
  'lastclass': 'Reading/study days Dec 12–14, 2026',
  'finals': 'Dec 15–18, 2026',
  'cal_url': 'https://www.gonzaga.edu/academics/academic-resources/academic-calendar',
  'cal_status': 'CONFIRMED',
  'fair': 'GSBA Fall Club Fair',
  'fair_date': 'UNVERIFIED — pattern: early-to-mid September, in/around the Hemmingson Center. Format revamped in '
               '2024.',
  'fair_outside': 'NO — external commercial entities are not eligible under the solicitation policy',
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://gonzaga.campuslabs.com/engage/events',
  'policy': 'Solicitation Policy (Gonzaga University Policies, student conduct standards)',
  'policy_url': 'https://www.gonzaga.edu/student-life/student-services/resolution-center/student-code-of-conduct/standards-of-conduct-and-policies/university-policies/solicitation-policy',
  'policy_key': "THE HARDEST 'NO' IN THE PACIFIC NORTHWEST. Verbatim: 'In order to protect student's right to "
                'privacy, UNDER NO CIRCUMSTANCES ARE SOLICITORS (INTERNAL OR EXTERNAL) ALLOWED TO CANVAS THE '
                "CAMPUS.' And: 'The use of University facilities and resources to conduct commercial ventures not "
                "sanctioned by the University is prohibited.' Enforcement: 'Individuals engaged in these activities "
                'will be asked to leave the premises. Failure to do so will result in the staff contacting Campus '
                "Security & Public Safety.' The ONLY approval route is the Gonzaga University Event Service Team "
                '(GUEST) for a sanctioned vendor table. As a private institution Gonzaga is bound by neither the WAC '
                'chapters nor public-forum doctrine.',
  'sponsor_required': 'GUEST approval is the only route; no RSO-sponsorship carve-out',
  'clubs': [('Gonzaga University Investment Club (GUIC)',
             "ACTIVE. Manages a student-led portfolio 'exceeding $270,000.' Published contact: "
             'vcasella@zagmail.gonzaga.edu (officer emails rotate — re-verify).',
             'https://guic.org/'),
            ('Women in Business',
             '',
             'https://www.gonzaga.edu/student-life/student-affairs/our-departments-and-programs/center-for-student-involvement/clubs-and-student-organizations'),
            ('Alpha Kappa Psi', '', ''),
            ('Iota Rho', '', ''),
            ('NO blockchain/crypto/Web3 club found',
             'Gonzaga reports 130+ clubs — search the full directory',
             'https://gonzaga.campuslabs.com/engage')],
  'faculty': [('GUEST (Gonzaga University Event Service Team)',
               'The approval gate for any tabling — contact UNVERIFIED',
               '',
               '',
               'https://www.gonzaga.edu/student-life/student-affairs/our-departments-and-programs/center-for-student-involvement')],
  'courses': [('—',
               'NONE. The full BFIN catalog (BFIN 320, 322, 324, 325, 327, 367, 422, 423, 424, 426, 429A-C, 489, '
               "491) contains no blockchain/crypto/fintech course. BFIN 489 'Special Topic Seminar' is the only "
               'possible vehicle.',
               'https://catalog.gonzaga.edu/courses/bfin/')],
  'events': [('—',
              'Fall 2026 business speaker series / career fairs UNVERIFIED',
              'https://www.gonzaga.edu/school-of-business-administration/student-opportunities')],
  'play': 'Do not table. The policy bars canvassing outright and names Campus Security as the enforcement mechanism '
          '— a removal here would be documented and would follow you to other campuses. The ONLY credible path is an '
          'academic invitation: approach the Gonzaga University Investment Club (which runs a real $270K portfolio) '
          'and ask to be invited as a speaker on digital-asset market structure, then have GUEST clear it. Expect '
          'this to take 6–8 weeks and to fail if the pitch is promotional.',
  'gaps': ['GUEST contact details',
           'Fall 2026 Club Fair date',
           'Whether GUEST has ever approved a fintech/crypto vendor']},
 {'state': 'Washington',
  'name': 'University of Washington — Seattle',
  'city': 'Seattle, WA',
  'type': 'Public',
  'tier': 'A — Added (highest curriculum fit in WA)',
  'access': 3,
  'start': 'Wed Sep 30, 2026 (Autumn QUARTER)',
  'adddrop': 'Oct 6, 2026 (without fee)',
  'fallbreak': '—',
  'thanksgiving': 'Nov 26–27, 2026 (Thanksgiving + Native American Heritage Day)',
  'lastclass': 'Fri Dec 11, 2026',
  'finals': 'Dec 12–18, 2026',
  'cal_url': 'https://www.washington.edu/students/reg/2627cal.html',
  'cal_status': 'CONFIRMED',
  'fair': 'Student Activities Fair (part of Dawg Daze)',
  'fair_date': 'Dawg Daze has a live Fall 2026 event page for Sep 24, 2026 (robots-blocked; verify in a browser). '
               'Fair itself: 2 days, 10am–2pm, Red Square/Quad.',
  'fair_outside': "NO — 'open to all current RSOs' only; registration by RSO Group Administrators. Explicit rule: "
                  "'Giveaways only, no fundraising.'",
  'fair_cost': 'None (RSO-only)',
  'fair_deadline': 'Late August (RSO registration)',
  'fair_url': 'https://hub.washington.edu/whats-happening/hub-events/student-activities-fair/',
  'policy': 'Chapter 478-136 WAC — Use of University of Washington Facilities',
  'policy_url': 'https://app.leg.wa.gov/wac/default.aspx?cite=478-136&full=true',
  'policy_key': "WAC 478-136-030: 'University facilities may not be used for private or commercial purposes such as "
                "sales, advertising, or promotional activities UNLESS SUCH ACTIVITIES SERVE AN EDUCATIONAL PURPOSE.' "
                "'No solicitation of a commercial nature is permitted in university residence halls.' ⚠ CRITICAL: "
                "non-university organizations require 'sponsorship by a UNIVERSITY ACADEMIC OR ADMINISTRATIVE UNIT "
                "and approved by the appropriate chair' — this is a DEPARTMENT sponsor, NOT an RSO sponsor. The HUB "
                "lawn is UW's de facto free-speech area.",
  'sponsor_required': 'Yes — an academic or administrative UNIT (department), not a student club',
  'clubs': [('Blockchain Society at the University of Washington',
             "ACTIVE (site copyright 2026). Self-described: 'a student-led builder org focused on meaningful "
             "education, applied research, and shipping projects — NOT HYPE.' Faculty advisors from CSE and Foster. "
             'Contact: blockchn@uw.edu',
             'https://www.uwblockchain.org/'),
            ('(finance/FMA/ACM/data science)',
             'UNVERIFIED individually — search HuskyLink',
             'https://huskylink.washington.edu/')],
  'faculty': [('Student Activities Office (SAO)',
               'Office',
               'HUB 232',
               'sao@uw.edu · 206-543-2380',
               'https://hub.washington.edu/get-involved/sao/rso-directory/'),
              ('Career & Internship Center',
               'Office',
               '',
               'askcic@uw.edu · 206-543-0535',
               'https://careers.uw.edu/career-fairs/'),
              ('UW Blockchain Lab (ECE)',
               "Appears DORMANT — most recent news July 2022, '© Copyright 2021'",
               'ECE',
               '',
               'https://blockchain.ece.uw.edu/'),
              ('Cryptography Research @ UW',
               'Faculty roster — look up here',
               'Allen School',
               '',
               'https://crypto.cs.washington.edu/')],
  'courses': [('CFRM 426',
               "FinTech, Blockchains, and Cryptocurrencies (4cr) — 'blockchain applications in finance with emphasis "
               "on cryptocurrencies,' robo-advising, AI-driven trading. Prereq CFRM 415, 425.",
               'https://www.washington.edu/students/crscat/cfrm.html'),
              ('CFRM 526',
               'FinTech, Blockchains, and Cryptocurrencies (graduate, 4cr). Prereq CFRM 501; CFRM 506 or 507.',
               'https://www.washington.edu/students/crscat/cfrm.html'),
              ('CSE 490C',
               'Cryptography (topics course) — not cryptocurrency per se',
               'https://courses.cs.washington.edu/courses/cse490c/19au/'),
              ('(Foster FIN)',
               'The Foster School FIN catalog contains NO blockchain/crypto/fintech course — verified against the '
               'full listing.',
               'https://www.washington.edu/students/crscat/finance.html')],
  'events': [('DubHacks 2026',
              '⚠ Oct 17–18, 2026 — CONFIRMED. 1,000+ students, ~100 industry mentors/sponsors. Sponsorship: '
              "hello@dubhacks.co. Organizers state they are 'happy to work with sponsors to find ways to get "
              "involved that align with your budget.'",
              'https://dh26.dubhacks.co/'),
             ('UW Fall Job & Internship Fair', 'Oct 7, 2026, 11:00am', 'https://careers.uw.edu/career-fairs/')],
  'play': 'BEST NON-CAMPUS-POLICY PATH IN THE NORTHWEST: sponsor DubHacks (Oct 17–18). It is a private, student-run '
          "event with an open sponsor pipeline and an explicitly flexible budget — it sidesteps WAC 478-136-030's "
          "commercial bar in a way campus tabling cannot. ⚠ But read the UW Blockchain Society's own words first: "
          "they describe themselves as 'not hype.' This is a technical, research-oriented audience that will be "
          'actively hostile to a token-promotion pitch. Lead with protocol design, not with the $21.',
  'gaps': ['Fall 2026 Student Activities Fair exact date',
           'Whether CFRM 426/526 run Autumn 2026',
           'UW Blockchain Lab current status/lead']},
 {'state': 'Washington',
  'name': 'Eastern Washington University',
  'city': 'Cheney, WA',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 2,
  'start': 'UNVERIFIED — late September (QUARTER system, not semesters)',
  'adddrop': 'UNVERIFIED',
  'fallbreak': 'UNVERIFIED',
  'thanksgiving': 'UNVERIFIED',
  'lastclass': 'UNVERIFIED',
  'finals': 'UNVERIFIED',
  'cal_url': 'https://inside.ewu.edu/records-and-registration/calendar/calendar-quarter/',
  'cal_status': 'UNVERIFIED — registrar pages block automated fetching',
  'fair': 'Welcome Week (includes club/org tabling)',
  'fair_date': 'UNVERIFIED',
  'fair_outside': 'UNVERIFIED — but the WAC flatly bars commercial solicitation',
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://inside.ewu.edu/student-engagement/',
  'policy': 'Chapter 172-137 WAC — Use of University Facilities; Chapter 172-141 WAC — Use of outdoor areas for '
            'first amendment activities',
  'policy_url': 'https://apps.leg.wa.gov/wac/default.aspx?cite=172-137&full=true',
  'policy_key': "WAC 172-137-050: 'University facilities MAY NOT BE USED FOR COMMERCIAL GAIN, including: Commercial "
                "advertising; solicitation and merchandising of any food, goods, wares, service, or merchandise.' ⚠ "
                "CRITICAL: 'All requests for the use of university facilities by students, nonaffiliated groups, and "
                'outside community members, WHETHER SPONSORED OR NOT, must be approved by the VP for Business & '
                "Finance or designee' — RSO sponsorship does NOT bypass this at EWU. Reservations ≥48 hours in "
                'advance; fees at actual direct and indirect cost. WAC 172-141: non-affiliates MAY engage in first '
                'amendment activities outdoors, 6am–10pm, ≤8 hours/day, ≤5 days per two-week period when contested; '
                "activities likely to draw 100+ people require 3 days' notice to university police at 509-359-4021. "
                'But 172-137-060 permits distribution of NONCOMMERCIAL materials only.',
  'sponsor_required': 'Sponsorship is irrelevant — VP-BF approval required regardless',
  'clubs': [('Not enumerable',
             'EagleSync requires login. No blockchain/crypto club identified.',
             'https://eaglesync.ewu.edu/club_signup')],
  'faculty': [('University Police (required contact for 100+ person outdoor activities)',
               '',
               '',
               '509-359-4021',
               'https://apps.leg.wa.gov/wac/default.aspx?cite=172-141&full=true'),
              ('VP for Business & Finance (VP-BF)',
               'The approval authority for ALL outside-group facility use — name UNVERIFIED',
               '',
               '',
               'https://www.ewu.edu/')],
  'courses': [('—', 'UNVERIFIED — none found.', 'https://www.ewu.edu/cpp/business/')],
  'events': [('—', 'UNVERIFIED', 'https://www.ewu.edu/calendar')],
  'play': "⚠ CORRECTION TO THE BRIEF: EWU is a QUARTER school, not a semester school — 'four 10-week terms per "
          "year.' Access is hard: the commercial-gain ban applies and the VP-BF approval requirement explicitly "
          'survives sponsorship. The only open door is noncommercial outdoor literature distribution. Worth one stop '
          'only if you are already in Spokane (Cheney is ~20 min from Gonzaga).',
  'gaps': ['The ENTIRE Fall 2026 calendar (robots-blocked)',
           'Club roster',
           'VP-BF name and contact',
           'Any Fall 2026 fair date']},
 {'state': 'Washington',
  'name': 'Western Washington University',
  'city': 'Bellingham, WA',
  'type': 'Public',
  'tier': 'B — Regional (best-documented paid access in WA)',
  'access': 4,
  'start': 'Wed Sep 23, 2026 (QUARTER)',
  'adddrop': 'UNVERIFIED',
  'fallbreak': '—',
  'thanksgiving': 'UNVERIFIED',
  'lastclass': 'Dec 11, 2026 (term end)',
  'finals': 'UNVERIFIED',
  'cal_url': 'https://registrar.wwu.edu/term-dates',
  'cal_status': 'PARTIAL — start/end CONFIRMED',
  'fair': 'Fall Info Fair 2026',
  'fair_date': '⚠ Tue Sep 22, 2026, 11am–3pm — CONFIRMED on a live 2026 page. Red Square; Flag Plaza; PAC Plaza. '
               'Rain venue: Viking Union.',
  'fair_outside': "YES — but 'all off-campus groups by INVITATION ONLY.' Categories include local for-profit "
                  'businesses.',
  'fair_cost': 'For-profit business: $300 full table / $150 half table (non-profit $80/$40). Sponsorships '
               '$1,000–$7,500.',
  'fair_deadline': '⚠ MON AUG 31, 2026 — 20 days out. Off-campus orgs must REQUEST an invitation.',
  'fair_url': 'https://engage.wwu.edu/programs/community-service-center/fall-info-fair',
  'policy': 'Chapter 516-36 WAC — Use of University Property; POL-U1000.06 Scheduling of Facilities by Off-Campus '
            'Groups',
  'policy_url': 'https://app.leg.wa.gov/WAC/default.aspx?cite=516-36&full=true',
  'policy_key': "WAC 516-36-040: 'University property may not be used for private or commercial gain, including: "
                "Commercial advertising; solicitation and merchandising' — with limited exceptions requiring "
                'PRESIDENTIAL APPROVAL or formal agreements. The paid Info Fair booth operates under that exception '
                "hook. WAC 516-36-030: 'Handbills, leaflets, pamphlets, flyers, and similar materials may be "
                "distributed ONLY IN RELATION TO UNIVERSITY SANCTIONED ACTIVITIES.' POL-U1000.06: written request to "
                'the president or designee, evaluated on connection to university programs, mission compatibility, '
                "community-relationship impact, and 'the applicant's qualifications, experience, and FINANCIAL "
                "STABILITY.' The university may require an advance deposit, bond or insurance.",
  'sponsor_required': 'No — but invitation + presidential-exception route',
  'clubs': [('Not enumerable',
             'Western Involvement Network (WIN) directory. No blockchain/crypto club identified.',
             'https://win.wwu.edu/')],
  'faculty': [('Fall Info Fair Coordinator',
               'Office',
               '',
               'infofair.coordinator@wwu.edu · (360) 650-4190',
               'https://engage.wwu.edu/programs/community-service-center/fall-info-fair'),
              ('Associate Director (Info Fair)', 'Office', '', 'cookj22@wwu.edu · (360) 650-2390', ''),
              ('Viking Union Reservations',
               'Office',
               '',
               'VU.Reservations@wwu.edu · (360) 650-6131',
               'https://policy.wwu.edu/POL-U1000.06-Scheduling-of-Facilities-by-Off-Campus-Groups'),
              ('CBE accommodations contact',
               'College of Business & Economics',
               '',
               'renee.gayden@wwu.edu',
               'https://cbe.wwu.edu/upcoming-event-cbe-club-info-fair')],
  'courses': [('—', 'UNVERIFIED — none found.', 'https://catalog.wwu.edu/')],
  'events': [('Fall Info Fair', '⚠ Sep 22, 2026, 11am–3pm, Red Square', 'https://engage.wwu.edu/infofair'),
             ('CBE Club Info Fair',
              'Haskel Plaza, 1–4pm — published instance is historical; Fall 2026 date UNVERIFIED',
              'https://cbe.wwu.edu/upcoming-event-cbe-club-info-fair')],
  'play': '⚠ 20-DAY DEADLINE. The best-documented paid external access in Washington: $300 for a full table on Red '
          "Square the day before classes start. The catch is 'by invitation only' — you must email "
          'infofair.coordinator@wwu.edu to REQUEST an invitation, and that takes lead time you barely have. Do this '
          'in the same sitting as the OSU registration (Aug 27) and the WSU picnic call.',
  'gaps': ['Add/drop, Thanksgiving, finals dates',
           'Club roster',
           'Whether an invitation will actually be granted to a crypto project']},
 {'state': 'Washington',
  'name': 'Central Washington University',
  'city': 'Ellensburg, WA',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 2,
  'start': 'Wed Sep 23, 2026 (QUARTER)',
  'adddrop': 'Sep 29, 2026 (change of schedule/audit deadline)',
  'fallbreak': '—',
  'thanksgiving': 'Nov 25–27, 2026',
  'lastclass': 'Fri Dec 4, 2026',
  'finals': 'Dec 8–11, 2026 (study day Dec 7)',
  'cal_url': 'https://www.cwu.edu/about/offices/registrar/academic-information/2026-2027_university_academic_aalendar.pdf',
  'cal_status': 'CONFIRMED',
  'fair': 'Fall Involvement Fair (run by SLICE)',
  'fair_date': 'UNVERIFIED — pattern: first week of fall quarter, 3:00–5:00pm, SURC East Patio and Chestnut Mall',
  'fair_outside': "HISTORICALLY YES — the 2024 page invited students to meet 'student clubs and orgs, campus "
                  "departments AND COMMUNITY PARTNERS.' No fee schedule or application form published.",
  'fair_cost': 'UNVERIFIED',
  'fair_deadline': 'UNVERIFIED',
  'fair_url': 'https://www.cwu.edu/student-life/slice/clubs/index.php',
  'policy': 'Chapter 106-140 WAC — Use of Facilities; WAC 106-141-050 — Solicitation, Distribution, Posting',
  'policy_url': 'https://app.leg.wa.gov/wac/default.aspx?cite=106-140&full=true',
  'policy_key': "WAC 106-140-040: 'The soliciting, selling, exposing for sale, or offering to sell of ANY goods, "
                'services, articles, wares or merchandise of any nature whatsoever… IS PROHIBITED EXCEPT BY WRITTEN '
                "PERMISSION of the board of trustees, president, or designee.' WAC 106-140-011 adds a SECOND "
                "requirement: activities must 'serve the purposes and needs of the university AND ARE SPONSORED BY A "
                "UNIVERSITY DEPARTMENT, AGENCY, OR RECOGNIZED ORGANIZATION.' WAC 106-140-036: 'Publicity and "
                "literature—Commercial advertising prohibited.' WAC 106-141-050: 'Commercial solicitation generally "
                "is not permitted on university property'; campus BUILDINGS limited to campus groups; distributing "
                "materials on vehicle windshields 'is deemed to constitute littering.'",
  'sponsor_required': 'Yes — AND separate written permission from the board/president/designee',
  'clubs': [('Not enumerable',
             'CWU Engage. No blockchain/crypto/finance club identified.',
             'https://www.cwu.edu/student-life/slice/clubs/registered-student-organizations.php')],
  'faculty': [('SLICE (Student Life, Involvement & Campus Engagement)',
               'Office',
               'SURC 250',
               'slice@cwu.edu · 509-963-1850',
               'https://www.cwu.edu/student-life/slice/clubs/index.php'),
              ('Lola Gallagher', 'Director of Student Involvement', 'SLICE', 'via slice@cwu.edu', ''),
              ('Emilio Gonzalez', 'Assistant Director of Student Involvement', 'SLICE', 'via slice@cwu.edu', '')],
  'courses': [('—', 'UNVERIFIED — none found.', 'https://catalog.acalog.cwu.edu/')],
  'events': [('Fall Involvement Fair',
              'First week of fall quarter — Fall 2026 date TBC',
              'https://www.cwu.edu/student-life/slice/clubs/index.php')],
  'play': 'CWU requires BOTH written board/president permission AND departmental or RSO sponsorship — a double gate. '
          "The one encouraging signal is that the Involvement Fair has historically included 'community partners.' "
          'Call SLICE (509-963-1850) and ask specifically whether community partners pay a fee and what the Fall '
          '2026 date is. Ellensburg is a natural mid-point between Seattle and Spokane.',
  'gaps': ['Fall 2026 Involvement Fair date, fee, and application',
           'Club roster',
           'Whether community partners are for-profit-eligible']}]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; sorts last.
DEADLINES = [('2026-08-21',
  'Aug 21, 2026',
  'WSU Pullman',
  '⚠ ALL-CAMPUS PICNIC & RESOURCE FAIR, 11am–2pm, Glenn Terrell Mall',
  "$200 'Participation Sponsorship' — re-verified Aug 11 on the live 2026 registration form (NOT on wow.wsu.edu, "
  "which is stale). A $1,000 'Cougar Sponsorship' tier also covers New Coug Orientation. No published signup "
  "deadline — CALL, don't email.",
  'https://universityevents.wsu.edu/all-campus-picnic/',
  'university.events@wsu.edu · 509-335-6674'),
 ('2026-08-31',
  'Aug 31, 2026',
  'Western Washington',
  '⚠⚠ FALL INFO FAIR REGISTRATION DEADLINE',
  'For-profit $300 full / $150 half. Event Sep 22. ⚠ OFF-CAMPUS GROUPS BY INVITATION ONLY — you must request an '
  'invitation first.',
  'https://engage.wwu.edu/programs/community-service-center/fall-info-fair',
  'infofair.coordinator@wwu.edu · (360) 650-4190'),
 ('2026-09-01',
  'Sep 1, 2026',
  'Gonzaga',
  'Fall classes begin',
  '',
  'https://www.gonzaga.edu/academics/academic-resources/academic-calendar',
  ''),
 ('2026-09-22',
  'Sep 22, 2026',
  'Western Washington',
  '⚠ FALL INFO FAIR, 11am–3pm, Red Square',
  'Register by Aug 31, invitation required.',
  'https://engage.wwu.edu/infofair',
  'infofair.coordinator@wwu.edu'),
 ('2026-09-30',
  'Sep 30, 2026',
  'U of Washington',
  'Autumn quarter instruction begins',
  '',
  'https://www.washington.edu/students/reg/2627cal.html',
  ''),
 ('2026-10-07',
  'Oct 7, 2026',
  'U of Washington',
  'Fall Job & Internship Fair, 11:00am',
  'Handshake registration.',
  'https://careers.uw.edu/career-fairs/',
  ''),
 ('2026-10-17',
  'Oct 17–18, 2026',
  'U of Washington',
  '⚠ DUBHACKS 2026',
  "1,000+ students, ~100 industry mentors/sponsors. Open sponsor pipeline; organizers 'happy to work with sponsors "
  "to find ways to get involved that align with your budget.' Sidesteps WAC 478-136-030's commercial bar.",
  'https://dh26.dubhacks.co/',
  'hello@dubhacks.co')]
