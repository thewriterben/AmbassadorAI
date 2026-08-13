"""Colorado — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published at time of research — a gap to close by phone, not a finding of absence.
Schema: reference/data-schema.md
"""

STATE = 'Colorado'

CAMPUSES = [{'state': 'Colorado',
  'name': 'University of Colorado Boulder',
  'city': 'Boulder, CO',
  'type': 'Public',
  'tier': 'A — Added (high priority)',
  'access': 4,
  'start': 'Thu Aug 20, 2026',
  'adddrop': 'Add/swap Fri Aug 28; drop without penalty Fri Sep 4, 2026',
  'fallbreak': 'Midsemester reading day Thu Oct 8, 2026',
  'thanksgiving': 'Nov 23–27, 2026 (full fall break; closed Nov 26–27)',
  'lastclass': 'Fri Dec 4, 2026',
  'finals': 'Dec 7–11, 2026 (reading days Dec 5–6)',
  'cal_url': 'https://www.colorado.edu/today/2026/06/12/know-key-academic-dates-fall-2026',
  'cal_status': 'CONFIRMED',
  'fair': 'Be Involved Fair',
  'fair_date': 'Wed Aug 26, 2026, 2–6pm, Farrand Field (year inferred but near-certain — Aug 26 is a Wednesday in '
               '2026)',
  'fair_outside': "⚠ NO — limited to 'Recognized student organizations, recognized social Greek organizations and "
                  "university student-run programs and sport clubs.' Application deadline was MAY 31 — already "
                  'passed.',
  'fair_cost': '',
  'fair_deadline': 'PASSED (May 31)',
  'fair_url': 'https://bulletin.colorado.edu/node/9047',
  'policy': 'Campus Use of University Facilities (CUUF) Procedures',
  'policy_url': 'https://www.colorado.edu/compliance/policies/campus-use-university-facilities-cuuf-procedures',
  'policy_key': "§XI.2: 'Commercial Solicitation is permitted ONLY as provided elsewhere in the CUUF Procedures' — "
                'non-affiliates may solicit only via UMC table rentals, designated spaces, or contractually-approved '
                "arrangements. §V.9: facilities 'may not be used for commercial, personal, or private financial gain "
                "except as approved by the University.' §V.7: ALL non-university organizations, 'including "
                "non-profit entities,' will be charged a rental fee. §V.8.2: 'If a Student Organization and/or "
                "University Department sponsors an outside entity, a UNIVERSITY CONTRACT… must be in place.' "
                '§VII.7.1: Dalton Trumbo Fountain Court is an unscheduled free-expression space, 9am–5pm. §XI.1.1: '
                "unscheduled canvassing on sidewalks must keep 'a 25-FOOT DISTANCE from building entrances.' No "
                'explicit credit-card-marketing ban found. ⚠ LITIGATION: CU Boulder students sued the university on '
                'Aug 5, 2026 alleging campus policies impermissibly restrict free speech — POLICIES MAY CHANGE '
                'MID-TOUR.',
  'sponsor_required': 'Yes — non-university clients must secure sponsorship from a recognized student org (or select '
                      "'Program Council'), with a University Contract in place",
  'clubs': [('⚠ CU Blockchain',
             "CONFIRMED ACTIVE RSO on BuffConnect. Category: Engineering & Technology. 'A hub for students to meet "
             "and talk about everything blockchain-related' — development, staking, mining, security, governance; "
             "'no experience is needed.' MEETS MONDAYS 6PM, ECCR 200. Also on LinkedIn, Meetup, X (@CU_blockchain), "
             'Facebook (@boulderblockchain). No officer names published — do not guess.',
             'https://campusgroups.colorado.edu/club_signup'),
            ('Alternative Asset Club', '', 'https://campusgroups.colorado.edu/club_signup'),
            ('Alternative Investment Club', '', ''),
            ('AI Club at CU Boulder', '', ''),
            ('Alpha Kappa Psi', 'Professional business fraternity', '')],
  'faculty': [('⚠ Eric C. Alston',
               'Scholar-In-Residence, Finance Division, Leeds School of Business; Director, Hernando de Soto Capital '
               "Markets Program. Research EXPLICITLY covers 'cryptocurrency and blockchain network governance,' "
               'blockchain network design, and a Templeton World Charity Foundation project on digital currency '
               'market development. Instructor of record for FNCE 4080. HIGHEST-VALUE ACADEMIC CONTACT AT THIS '
               'CAMPUS.',
               'Leeds School of Business',
               'Eric.Alston@colorado.edu · 303-735-6874 · Koelbel Bldg Rm 425J',
               'https://www.colorado.edu/business/eric-c-alston'),
              ('Bo Waggoner',
               'Taught CYBR 5240 / CSCI 5240 Introduction to Blockchain (Spring 2022 per CU Experts). Contact not '
               'confirmed on a live page.',
               'Computer Science',
               'Look up here',
               'https://www.colorado.edu/cs/'),
              ('Center for Student Involvement (CSI)',
               'Office',
               'UMC Room 330, 207 UCB',
               '303-492-6366',
               'https://www.colorado.edu/involvement/'),
              ('CU Events Planning & Catering',
               'Office (UMC tabling contracts)',
               '',
               'cueventsplanning@colorado.edu · 303-492-8833',
               'https://www.colorado.edu/umc/umc-tabling-contract-non-university-vendors')],
  'courses': [('FNCE 4080',
               'Blockchain and Cryptocurrencies: Speculation or Innovation? — crypto business models, ICOs, '
               'regulatory perspectives, business uses of blockchain. Instructor: Eric Alston. ⚠ Terms offered per '
               'CU Experts: Fall 2020, Spring 2022, Spring 2023, Spring 2024 — the pattern suggests a SPRING course '
               'that may be dormant. Fall 2026: UNVERIFIED.',
               'https://experts.colorado.edu/display/coursename_FNCE-4080'),
              ('CYBR 5240 / CSCI 5240 / CSCI 4240',
               'Introduction to Blockchain — policy/governance, technology, application. Fall 2026: UNVERIFIED.',
               'https://experts.colorado.edu/display/coursename_CYBR-5240')],
  'events': [('Be Involved Fair',
              'Wed Aug 26, 2026 — closed to outside orgs',
              'https://calendar.colorado.edu/event/be-involved-fair')],
  'play': "⚠ PREMISE CORRECTION: CU Boulder's Media Archaeology Lab has NO blockchain research footprint — it is a "
          'historical-computing hardware archive under English/Intermedia. The real CU blockchain presence is (1) '
          'Eric Alston at Leeds and (2) the CU Blockchain RSO, which meets MONDAYS AT 6PM IN ECCR 200 and is '
          'confirmed active. That standing weekly meeting is the single most actionable club touchpoint in the '
          'dataset — you know the day, time and room. Pair it with UMC tabling at $250–350/day (informational) which '
          'requires RSO sponsorship plus a University Contract — CU Blockchain could be that sponsor. ⚠ Watch the '
          'Aug 5, 2026 free-speech lawsuit; tabling rules may shift mid-tour.',
  'gaps': ['Whether FNCE 4080 or CYBR 5240 run Fall 2026',
           'CU Blockchain officer contacts',
           'Outcome/status of the Aug 5 lawsuit',
           'Fall 2026 events calendar']},
 {'state': 'Colorado',
  'name': 'Colorado State University',
  'city': 'Fort Collins, CO',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 1,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'Wed Sep 9, 2026 (registration closes; last day to add/drop without record)',
  'fallbreak': 'Fall recess begins Sat Nov 21, 2026',
  'thanksgiving': 'Nov 26–27, 2026 (classes resume Nov 30)',
  'lastclass': 'Fri Dec 11, 2026',
  'finals': 'Dec 14–17, 2026',
  'cal_url': 'https://registrar.colostate.edu/wp-content/uploads/sites/23/2023/12/Faculty-Council-Approved-26-28-calendar.pdf',
  'cal_status': 'CONFIRMED',
  'fair': 'RamFest (RamEvents, Lory Student Center)',
  'fair_date': "UNVERIFIED — a 'RamFest 2026' listing exists but the detail page was not retrievable",
  'fair_outside': 'UNVERIFIED',
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://lsc.colostate.edu/ramevents/ramfest/',
  'policy': 'CSU Policy: Sales and Solicitations on University Property (Policy ID 539); Lory Student Center (LSC) '
            'Policies',
  'policy_url': 'https://policylibrary.colostate.edu/policy.aspx?id=539',
  'policy_key': "⚠⚠ THE MOST RESTRICTIVE CAMPUS FOR THIS SPECIFIC USE CASE IN ALL NINE STATES. Policy 539: 'Sales "
                "and solicitations are GENERALLY PROHIBITED in university facilities.' 'All sales and solicitations "
                'of merchandise or services for commercial purposes are permitted ONLY IN THE LORY STUDENT CENTER '
                "(LSC) FLEA MARKET and must be approved, in advance.' ⚠ AND: 'Solicitations that are permitted under "
                'this policy MAY NOT INCLUDE COMMERCIAL TRANSACTIONS, SUCH AS COLLECTING CASH OR CREDIT CARD '
                "INFORMATION.' LSC Policies go further: 'NO FINANCIAL TRANSACTIONS (INCLUDING REQUESTING CREDIT CARD "
                "INFORMATION, VENMO OR SIMILAR APP INFO, ETC) ARE PERMITTED ON THE PLAZA.' 'Credit card applications "
                'and similar commercial solicitations are explicitly prohibited; staff remove these postings WITHOUT '
                "EXCEPTION.' ⚠ ANTI-FRONTING: the co-sponsorship policy 'prohibits fronting, where on-campus groups "
                "represent off-campus interests.' RSOs may reserve space 'only for events that they directly "
                "sponsor, are integrally involved in, and will be present at.'",
  'sponsor_required': 'Sponsorship route expressly foreclosed by the anti-fronting rule',
  'clubs': [('NOT ENUMERATED',
             'RamLink redirects to a JS-rendered CampusLabs app.',
             'https://ramlink.campuslabs.com/engage')],
  'faculty': [('(Not confirmed)',
               'Look up at College of Business and Computer Science directories.',
               '',
               '',
               'https://biz.colostate.edu/')],
  'courses': [('—', 'UNVERIFIED.', 'https://catalog.colostate.edu/')],
  'events': [('RamFest',
              'Fall 2026 date and tabling terms UNVERIFIED',
              'https://lsc.colostate.edu/ramevents/ramfest/'),
             ('LSC Market',
              'A commercial vendor space; the Career Center references it for employers — the most likely paid '
              'access route. Terms UNVERIFIED.',
              'https://career.colostate.edu/employer-resources/lory-student-center-market/')],
  'play': "⚠ SKIP CSU. This is the campus most likely to generate a compliance incident. CSU's rules do three things "
          'simultaneously that no other campus does: they confine commercial solicitation to a single venue (the LSC '
          'Flea Market), they bar collecting payment credentials at ANY permitted solicitation — with language '
          "explicitly extending beyond credit cards to 'Venmo or similar app info,' which reads directly onto crypto "
          'wallet onboarding — and they foreclose the club-sponsorship workaround by name. If you go anywhere in '
          'Colorado, go to Boulder.',
  'gaps': ['RamFest Fall 2026 date and terms',
           'LSC Market terms and fees',
           'Club roster',
           'Faculty',
           'Catalog courses']},
 {'state': 'Colorado',
  'name': 'Colorado School of Mines',
  'city': 'Golden, CO',
  'type': 'Public',
  'tier': 'C — Opportunistic',
  'access': 3,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'Wed Sep 2, 2026 (last day to add / drop with full refund)',
  'fallbreak': 'Oct 12–13, 2026',
  'thanksgiving': 'Nov 25–27, 2026',
  'lastclass': 'Wed Dec 9, 2026',
  'finals': 'Dec 11–12 and Dec 14–16, 2026 (semester ends Dec 18)',
  'cal_url': 'https://www.mines.edu/registrar/wp-content/uploads/sites/51/2026/04/2026-2027-Academic-Calendar-4-8-26.pdf',
  'cal_status': 'CONFIRMED',
  'fair': 'Celebration of Mines',
  'fair_date': "⚠ Fri Aug 28, 2026, 5:00–7:00pm, North IM Field — CONFIRMED. 'Free and open to all.' Rain or shine; "
               'lightning may postpone.',
  'fair_outside': 'NOT SPECIFIED — UNVERIFIED. Framing is student organizations and departments.',
  'fair_cost': 'UNVERIFIED',
  'fair_deadline': 'UNVERIFIED',
  'fair_url': 'https://student-activities.mines.edu/celebration-of-mines',
  'policy': "⚠ No dedicated Mines solicitation policy located. Notably, the Mines RSO Handbook is itself 'Adapted "
            "from the Colorado State University RSO Handbook' — so CSU-style restrictions may be mirrored.",
  'policy_url': 'https://www.mines.edu/student-activities/wp-content/uploads/sites/69/2023/08/RSO-Handbook-2023-2024.pdf',
  'policy_key': "⚠ READ THE RSO HANDBOOK — it is adapted from CSU's, and CSU's is the most restrictive in the "
                'dataset for this use case. Conference & Event Services (External) confirms non-Mines organizations '
                'MAY rent campus facilities: requests must be submitted AT LEAST 6 WEEKS prior via a Request for '
                'Proposal Form. Venues: Ben Parker Student Center ballrooms/meeting rooms, Green Center, classrooms, '
                'gymnasium. Insurance: $1M per accident bodily injury; $3M per accident property damage (URMIA-TULIP '
                'available). Sodexo is the exclusive caterer.',
  'sponsor_required': 'UNVERIFIED',
  'clubs': [('NOT ENUMERATED',
             'Mines is an engineering/mining school; ACM, CS and quantitative-finance orgs are the likeliest fits.',
             'https://idig.mines.edu/s/840/dg23/project.aspx?sid=840&gid=1&pgid=8981')],
  'faculty': [('Audrey Weber',
               'Student Activities — Celebration of Mines coordinator; the table sign-up contact',
               'Student Activities',
               'audrey.weber@mines.edu',
               'https://student-activities.mines.edu/celebration-of-mines'),
              ('Student Activities (SAIL)', 'Office', '', 'sail@mines.edu · 303-273-3234', ''),
              ('Conference & Event Services',
               'Office',
               '',
               'rentals@mines.edu · 303-273-3460',
               'https://ces.mines.edu/external/')],
  'courses': [('—', 'UNVERIFIED.', 'https://catalog.mines.edu/')],
  'events': [('Celebration of Mines',
              '⚠ Fri Aug 28, 2026, 5–7pm, North IM Field',
              'https://student-activities.mines.edu/celebration-of-mines')],
  'play': 'A named coordinator with a published email (audrey.weber@mines.edu) and a confirmed Aug 28 date make this '
          'a cheap phone call. Mines students are quantitatively strong and the school has a real hard-tech culture '
          '— a good audience for a protocol conversation. But the 6-week lead time on external facility rentals '
          'means the Celebration of Mines table is your only near-term option, and outside-org eligibility there is '
          'unconfirmed. Golden is 25 minutes from Boulder; bundle them.',
  'gaps': ['Whether outside orgs may table at Celebration of Mines, and at what cost',
           "⚠ The RSO Handbook's solicitation provisions (CSU-derived)",
           'Club roster',
           'Faculty']},
 {'state': 'Colorado',
  'name': 'University of Denver',
  'city': 'Denver, CO',
  'type': 'Private',
  'tier': 'C — Opportunistic',
  'access': 2,
  'start': '⚠ Tue Sep 8, 2026 (QUARTER system — latest start in the dataset)',
  'adddrop': 'UNVERIFIED',
  'fallbreak': '—',
  'thanksgiving': 'Nov 26–27, 2026',
  'lastclass': '⚠ Mon Nov 16, 2026 — instruction ends',
  'finals': 'Nov 17–20, 2026',
  'cal_url': 'https://bulletin.du.edu/graduate/aboutdu/academiccalendar/quartercalendar/',
  'cal_status': 'CONFIRMED',
  'fair': 'NOT FOUND — DU runs student-org fairs through the Office of Student Engagement on CrimsonConnect',
  'fair_date': 'UNVERIFIED',
  'fair_outside': 'UNVERIFIED',
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://crimsonconnect.du.edu/',
  'policy': 'NOT RETRIEVED — UNVERIFIED',
  'policy_url': 'https://crimsonconnect.du.edu/ose/event-planning-resources/',
  'policy_key': 'DU is a PRIVATE university, so the Colorado open-forum constraints that bind CU, CSU and Mines do '
                'NOT apply. DU has broad latitude to exclude outside entities outright, and private institutions '
                'commonly do. Assume access is discretionary and contract-based. Call the Office of Student '
                'Engagement directly — the event-planning page is a JS navigation shell.',
  'sponsor_required': 'Assume yes — discretionary',
  'clubs': [('NOT ENUMERATED',
             'Daniels College of Business is the likely home for finance/fintech orgs.',
             'https://crimsonconnect.du.edu/')],
  'faculty': [('(Not confirmed)',
               'Look up at Daniels College of Business and the Ritchie School of Engineering & Computer Science.',
               '',
               '',
               'https://daniels.du.edu/')],
  'courses': [('—', 'UNVERIFIED.', 'https://bulletin.du.edu/')],
  'events': [('—', 'UNVERIFIED', '')],
  'play': "⚠ CRITICAL SCHEDULING CONSTRAINT: DU's autumn quarter ENDS NOV 20, 2026. Students are gone from campus "
          'for the entire December window, and the term does not start until Sept 8. Any DU activity must land '
          'between roughly Sept 8 and Nov 13 — a narrow band that conflicts with the Wyoming Stampede and the '
          'Portland/Eugene leg. Combined with zero retrievable policy and no confirmed fair, DU is the '
          'lowest-information campus in Colorado. Deprioritize unless a Daniels College contact opens a door.',
  'gaps': ['ALL policy', 'Any student-org fair', 'Add/drop deadlines', 'Club roster', 'Faculty', 'Catalog courses'],
  'note': '⚠ Several search results conflate DU with CU DENVER (ucdenver.edu), a separate public institution. If CU '
          'Denver is of interest it should be scoped as a separate campus.'}]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; sorts last.
DEADLINES = [('2026-08-26',
  'Aug 26, 2026',
  'CU Boulder',
  'Be Involved Fair, 2–6pm, Farrand Field',
  '⚠ CLOSED to outside orgs; application deadline was May 31.',
  'https://bulletin.colorado.edu/node/9047',
  ''),
 ('2026-08-28',
  'Aug 28, 2026',
  'Colorado Mines',
  '⚠ CELEBRATION OF MINES, 5–7pm, North IM Field',
  'Outside-org eligibility UNVERIFIED — email the coordinator.',
  'https://student-activities.mines.edu/celebration-of-mines',
  'audrey.weber@mines.edu · 303-273-3234'),
 ('2026-09-08',
  'Sep 8, 2026',
  'U of Denver',
  'Autumn QUARTER begins',
  '⚠ Term ENDS Nov 20 — no December window at DU.',
  'https://bulletin.du.edu/graduate/aboutdu/academiccalendar/quartercalendar/',
  ''),
 ('2026-11-20',
  'Nov 20, 2026',
  'U of Denver',
  'Autumn quarter ENDS',
  '⚠ DU students are gone for the entire December window.',
  '',
  '')]
