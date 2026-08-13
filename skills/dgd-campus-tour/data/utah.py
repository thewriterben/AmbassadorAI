"""Utah — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published at time of research — a gap to close by phone, not a finding of absence.
Schema: reference/data-schema.md
"""

STATE = 'Utah'

CAMPUSES = [{'state': 'Utah',
  'name': 'Brigham Young University',
  'city': 'Provo, UT',
  'type': 'Private (LDS Church-owned)',
  'tier': 'A — Named target',
  'access': 1,
  'start': 'Wed Sep 2, 2026',
  'adddrop': 'Sep 10, 2026',
  'fallbreak': 'NONE — Thanksgiving is the only mid-semester break',
  'thanksgiving': 'Nov 26–27, 2026',
  'lastclass': 'Thu Dec 10, 2026',
  'finals': 'Dec 12–17, 2026 (Exam Preparation Day Dec 11)',
  'cal_url': 'https://catalog26byu.catalog.prod.coursedog.com/policy/dates-and-deadlines',
  'cal_status': 'CONFIRMED',
  'fair': 'Clubs Night — recurring EVERY TUESDAY, two sessions (7:00–8:30pm and 8:30–10:00pm), Wilkinson Student '
          'Center',
  'fair_date': 'Weekly Tuesdays during semester (~50 clubs, ~1,000 students each week). Fall 2026 specific dates not '
               'published.',
  'fair_outside': 'NO indication that outside organizations can participate — framed as BYUSA clubs only',
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://sclcenter.byu.edu/clubs-night',
  'policy': 'Speakers and Events Policy; Clubs and Associations Policy; Campus Scheduling — Advertising',
  'policy_url': 'https://policy.byu.edu/view/speakers-and-events-policy',
  'policy_key': "STRICTEST CAMPUS IN THE ENTIRE DATASET. Speakers and Events Policy: 'Unless specifically approved "
                'in advance during the approval process, A SPEAKER MUST NOT MARKET OR PROMOTE ANY COMMERCIAL OR '
                "PERSONAL PRODUCT.' 'No invitations may be extended and no promotional materials may be distributed "
                "until all required approvals are obtained' — approvals escalate through department chairs/deans to "
                "VICE PRESIDENTS. Clubs and Associations Policy: BYUSA clubs 'ARE NOT AFFILIATED WITH ANY OFF-CAMPUS "
                "ORGANIZATION' and cannot maintain independent off-campus bank accounts. Campus Scheduling: digital "
                "signs must 'not promote any outside business, service, or product'; 'No selling at booth unless "
                "approved by Campus Scheduling'; 'The University prohibits any commercial banners or signs on "
                "campus.' Content standard: presentations must not 'seriously and adversely affect the university's "
                "mission or The Church of Jesus Christ of Latter-day Saints.'",
  'sponsor_required': 'NO SPONSORSHIP PATHWAY EXISTS for an outside commercial entity',
  'clubs': [('Club directory',
             'JavaScript-rendered; could not be enumerated. Requires manual browsing.',
             'https://clubs.byu.edu/link/Clubs/PLB'),
            ('BYU Blockchain Summit',
             'Hosted by the J. Reuben Clark Law School. ⚠ Live page shows 2019 as the most recent event — LIKELY '
             'DORMANT. Do not assume it is active.',
             'https://blockchain.byu.edu/'),
            ('No active BYU blockchain or fintech STUDENT CLUB confirmed',
             '',
             'https://stem.byu.edu/technology/clubs')],
  'faculty': [('No individual faculty confirmed',
               'Do not guess. No BYU faculty in blockchain/crypto/fintech confirmed on a live page.',
               '',
               '',
               ''),
              ('Campus Scheduling', 'Office', '', 'wscadvertising@byu.edu', 'https://scheduling.byu.edu/'),
              ('Student Leadership', 'Office (table tents, terrace/mezzanine)', '', '801-422-3901', ''),
              ('Student Connection and Leadership Center', 'Office', '', '', 'https://sclcenter.byu.edu/')],
  'courses': [('C S 466',
               "Blockchain Technologies (3cr) — 'Technical underpinnings of blockchain-based systems, including "
               "cryptocurrency, smart contracts, decentralized finance (De-Fi), and Web3.' ⚠ Typical offering term: "
               'WINTER. NOT indicated as offered Fall 2026.',
               'https://catalog.byu.edu/courses/L4M3LZdHS1ASklCQe82y'),
              ("'Blockchain and Cryptocurrency Law'",
               'Appears in BYU graduate studies listings but the page returned 403 — UNVERIFIED',
               'https://gradstudies.byu.edu/course/blockchain-and-cryptocurrency-law')],
  'events': [('Clubs Night', 'Weekly Tuesdays', 'https://sclcenter.byu.edu/clubs-night'),
             ('Marriott School speaker series', 'Fall 2026 lineup UNVERIFIED', 'https://marriott.byu.edu/series')],
  'play': 'TREAT AS CLOSED. Every route is independently blocked: clubs cannot affiliate with off-campus '
          'organizations, speakers cannot promote commercial products without VP-level approval, and outside '
          'businesses cannot advertise on any campus channel. There is no sponsorship workaround. The only realistic '
          'BYU engagement is academic — C S 466 exists and teaches DeFi and Web3 — but it typically runs in WINTER, '
          'not Fall. Recommend removing BYU Provo from the Fall 2026 tour and revisiting as a Winter 2027 academic '
          'conversation only.',
  'gaps': ['Whether any blockchain/fintech student club currently exists',
           'Named faculty for C S 466',
           'Confirmation that C S 466 is Winter-only']},
 {'state': 'Utah',
  'name': 'University of Utah',
  'city': 'Salt Lake City, UT',
  'type': 'Public',
  'tier': 'A — Added (confirmed Fall 2026 fintech curriculum)',
  'access': 4,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'Fri Sep 4, 2026',
  'fallbreak': 'Sat–Sun Oct 10–18, 2026',
  'thanksgiving': 'Thu–Sun Nov 26–29, 2026',
  'lastclass': 'Thu Dec 10, 2026',
  'finals': 'Dec 14–18, 2026 (Reading Day Dec 11)',
  'cal_url': 'https://registrar.utah.edu/academic-calendars/pdf-academic-calendars/main_and_online_2026_2027.pdf',
  'cal_status': 'CONFIRMED',
  'fair': 'PlazaFest — Union Plaza, during Welcome Week. Historically 200+ student groups and ~4,000 students.',
  'fair_date': 'UNVERIFIED — only the 2015 edition is retrievable. Pattern: late August, first week of classes.',
  'fair_outside': 'UNVERIFIED — contact studentorgs@utah.edu',
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://campusconnect.utah.edu/events',
  'policy': 'Policy 1-007 — University Speech Policy (Revision 6, eff. Aug 15, 2023); Rule R1-007A',
  'policy_url': 'https://regulations.utah.edu/general/1-007.php',
  'policy_key': '⚠ NOTABLE: THERE IS NO OUTRIGHT BAN ON COMMERCIAL SOLICITATION — the policy creates a '
                'PERMIT/FEE/DESIGNATED-AREA regime instead. This makes the U the most legally open Utah campus. '
                "§II.I defines commercial speech as 'all spoken, written and symbolic speech intended in whole or in "
                "part for the personal profit of the person, organization or institution engaged in the speech.' "
                "§IV.D: the Scheduling Office 'shall publish rules and regulations governing the use of University "
                "facilities for commercial and non-University related purposes.' §V.A.2.f: the Dean of Students "
                "publishes rules governing posting/distribution 'for commercial purposes.' §V.B.3: rules 'governing "
                "the distribution of commercial handbills,' with a possible 'schedule of fees and limitations upon "
                "the areas.' BUT Rule R1-007A: 'The use may not be allowed for the personal or private gain of "
                "individuals,' and community groups rank 6th in facility priority.",
  'sponsor_required': 'No — permit/fee regime',
  'clubs': [('Not enumerable',
             'Campus Connect (CampusGroups) requires sign-in for the full directory. No blockchain/crypto/fintech '
             'club could be confirmed.',
             'https://campusconnect.utah.edu/club_signup')],
  'faculty': [('Gene Levinzon',
               'Instructor of record, FINAN 2140 Intro to Global Fintech (sections 002, 003), Fall 2026',
               'Finance / Eccles School',
               'Email not on the schedule — look up in the Eccles directory',
               'https://class-schedule.app.utah.edu/main/1268/class_list.html?subject=FINAN'),
              ('Elena Asparouhova',
               'Instructor of record, FINAN 5140 Fintech Trading Lab, Fall 2026',
               'Finance / Eccles School',
               'Look up in the Eccles directory',
               ''),
              ('Vlas Lezin',
               'Instructor of record, FINAN 5530 Python for Finance, Fall 2026',
               'Finance / Eccles School',
               'Look up in the Eccles directory',
               ''),
              ('Robert Dubil',
               'Instructor of record, FINAN 4020 Adv Excel for Finance, Fall 2026',
               'Finance / Eccles School',
               'Look up in the Eccles directory',
               ''),
              ('Union Events & Scheduling',
               'Office',
               'A. Ray Olpin Union',
               '801-581-7251',
               'https://www.union.utah.edu/events-scheduling/onlinereservations/'),
              ('Student Organizations', 'Office', 'Olpin Union Suite 235', 'studentorgs@utah.edu', '')],
  'courses': [('FINAN 2140',
               'Intro to Global Fintech — ⚠ CONFIRMED OFFERED FALL 2026, sections 002 & 003, in person, 3 units',
               'https://class-schedule.app.utah.edu/main/1268/class_list.html?subject=FINAN'),
              ('FINAN 5140', 'Fintech Trading Lab — ⚠ CONFIRMED OFFERED FALL 2026, section 001, hybrid, 3 units', ''),
              ('FINAN 5530', 'Python for Finance — ⚠ CONFIRMED OFFERED FALL 2026, section 090 online, 3 units', ''),
              ('FINAN 4020',
               'Adv Excel for Finance — ⚠ CONFIRMED OFFERED FALL 2026, sections 001 & 090, 3 units',
               ''),
              ('(CS)',
               'NO CS courses on blockchain, cryptocurrency, cryptography or distributed systems in the Fall 2026 CS '
               'schedule.',
               'https://class-schedule.app.utah.edu/main/1268/class_list.html?subject=CS')],
  'events': [('PlazaFest', 'Late August — Fall 2026 date UNVERIFIED', 'https://campusconnect.utah.edu/events')],
  'play': '⚠ ONE OF ONLY TWO CAMPUSES WITH CONFIRMED FALL 2026 FINTECH TEACHING (the other is Wyoming). Four FINAN '
          'courses are scheduled with named instructors — that is a real, verifiable audience of fintech students '
          'meeting weekly. Lead with a guest-lecture offer to Gene Levinzon (FINAN 2140, the intro course, two '
          "sections) and Elena Asparouhova (FINAN 5140 Trading Lab). ACTION ITEM: request the Scheduling Office's "
          'published commercial-use rules referenced in Policy 1-007 §IV.D — that unlinked document is the operative '
          'gatekeeper for any tabling.',
  'gaps': ['⚠ Scheduling Office commercial-use rules (§IV.D) — the operative document, not linked',
           'PlazaFest Fall 2026 date and outside-org eligibility',
           'Union rooms & rates page (server error)',
           'Club directory (login-gated)']},
 {'state': 'Utah',
  'name': 'Utah State University',
  'city': 'Logan, UT',
  'type': 'Public',
  'tier': 'B — Regional (best paid tabling in UT)',
  'access': 5,
  'start': 'Mon Aug 31, 2026',
  'adddrop': 'See Fall 2026 Registration Calendar',
  'fallbreak': 'Fri Oct 9, 2026',
  'thanksgiving': 'Nov 25–27, 2026',
  'lastclass': 'Fri Dec 11, 2026',
  'finals': 'Dec 14–18, 2026',
  'cal_url': 'https://catalog.usu.edu/pages/BE3eydcZFJn50bDP0zEQ',
  'cal_status': 'CONFIRMED',
  'fair': 'Day on the Quad 2026',
  'fair_date': '⚠ Wed Sep 2, 2026, 10am–3pm (vendor setup from 8am), USU Logan campus quad — CONFIRMED on the live '
               '2026 page',
  'fair_outside': "YES — a dedicated 'Off-Campus Group Registration' path is OPEN",
  'fair_cost': "⚠ RE-VERIFIED AUG 11, 2026 on the live vendor-policy page: 'All off-Campus vendors are required to "
               "pay the $300.00 registration fee.' ALL FEES ARE NON-REFUNDABLE. Note the fee is NOT on the main "
               'event page — it lives only on the vendor policy sub-page. On-campus parking is NOT free to vendors '
               'for DOTQ 2026.',
  'fair_deadline': "⚠⚠ RE-VERIFIED AUG 11, 2026: 'Registration CLOSES on Friday, August 14, 2026' — THREE DAYS FROM "
                   'TODAY. Off-campus link: cvent.me/zdAW89?RefId=Off+Campus',
  'fair_url': 'https://www.usu.edu/involvement/day-on-the-quad/',
  'policy': 'TSC Table Request policy; USUSA Clubs & Organizations Handbook 2025-2026',
  'policy_url': 'https://www.usu.edu/tsc/request-forms/table',
  'policy_key': "'Tabling in the Taggart Student Center is LIMITED TO REGISTERED USUSA CLUBS AND UNIVERSITY "
                "DEPARTMENTS' — a categorical exclusion of outside entities from routine year-round tabling. ⚠ "
                "ANTI-FRONTING at Day on the Quad: 'On-Campus organizations/departments are NOT ALLOWED to reserve a "
                "space for an off-Campus business.' Beverage exclusivity: 'Only Coca-Cola beverages… may be sold, "
                "distributed, sampled, advertised.' Merchandise sales require a Special Event Permit tax form. Clubs "
                "'are not eligible to rent credit card machines from the university' and 'must use off-campus "
                "banking systems.'",
  'sponsor_required': 'No — pay the off-campus fee. Sponsorship is expressly prohibited.',
  'clubs': [('Not enumerable',
             'No blockchain, crypto, or fintech club could be confirmed on a live USU page.',
             'https://www.usu.edu/involvement/')],
  'faculty': [('Day on the Quad',
               'Office',
               '0105 Old Main Hill',
               'dotq@usu.edu · (435) 797-2912',
               'https://www.usu.edu/involvement/day-on-the-quad/'),
              ('TSC Operations',
               'Office',
               '650 North 800 East',
               'TSCOperations@usu.edu · (435) 797-1724',
               'https://www.usu.edu/tsc/request-forms/table'),
              ('Huntsman School of Business',
               'Office — no fintech/blockchain program advertised',
               '',
               'huntsman@usu.edu · 435.797.2272',
               'https://huntsman.usu.edu/directory/index.php')],
  'courses': [('—',
               'No blockchain/crypto/fintech courses confirmed. USU catalog search is robots-blocked.',
               'https://catalog.usu.edu/')],
  'events': [('Day on the Quad', '⚠ Wed Sep 2, 2026', 'https://www.usu.edu/involvement/day-on-the-quad/')],
  'play': '⚠⚠ MOST URGENT ITEM IN THE ENTIRE PACKET: registration closes FRIDAY, AUG 14 — three days from today. Day '
          'on the Quad explicitly sells booths to off-campus businesses at $300 and is the only Utah fair that does. '
          'Because TSC tabling is closed to outsiders year-round and the anti-fronting rule blocks the club '
          'workaround, this ONE DAY is effectively your only USU access for the entire academic year. If you '
          'register nothing else this week, register this.',
  'gaps': ['2026 fee figure (2025 doc says $300)', 'Add/drop deadlines', 'Club roster', 'Catalog course search']},
 {'state': 'Utah',
  'name': 'Utah Valley University',
  'city': 'Orem, UT',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 3,
  'start': 'Wed Aug 19, 2026 ⚠ anomalously early — cross-check',
  'adddrop': 'Wed Sep 9, 2026 (last day to drop with refund)',
  'fallbreak': 'Thu–Sun Oct 15–18, 2026',
  'thanksgiving': 'Mon–Sun Nov 23–29, 2026',
  'lastclass': 'Fri Dec 4, 2026',
  'finals': 'Dec 7–11, 2026',
  'cal_url': 'https://www.uvu.edu/schedule/fall/',
  'cal_status': 'CONFIRMED (with caution — page mixes in 2025 admission-cycle dates)',
  'fair': 'Club Rush',
  'fair_date': '⚠ September 15–16, 2026 — stated on the live UVU Clubs page',
  'fair_outside': 'NOT STATED — UNVERIFIED. Contact the Clubs Office.',
  'fair_cost': 'UNVERIFIED',
  'fair_deadline': 'UNVERIFIED',
  'fair_url': 'https://www.uvu.edu/clubs/',
  'policy': 'UVU Policy 425 — Event Scheduling and Authorizing the Use of University Facilities; Clubs Handbook',
  'policy_url': 'https://policy.uvu.edu/getDisplayFile/59a85b3b568009ec588136fe',
  'policy_key': "⚠ MOST PERMISSIVE UTAH CAMPUS ON PAPER. Policy 425 contains NO standalone section on 'solicitation' "
                "or 'commercial use.' §3.7.2 defines 'External entities'; §4.3.2 ranks them lowest in priority "
                '(university > co-sponsored > external); all requests go through Events Services. THE REAL OPENING '
                "is the Clubs Handbook, p.20, 'Partnering with an Off-Campus Group': the event/organization 'must "
                "fulfill the mission and purpose of the club,' the club must be 'heavily involved with all aspects "
                "of the planning, publicity, and day of event' and assume responsibility for costs. Separately, p.16 "
                "defines SPONSORSHIP as 'an exchange of services between the club and a business' — e.g. money for "
                'logo placement on club materials — requiring approval from the Student Affairs Development Officer.',
  'sponsor_required': 'Club-partnership route available, but the club must genuinely drive the event',
  'clubs': [('Not enumerable',
             'UVU CampusGroups. No blockchain, crypto, Web3, or fintech club could be confirmed. Browse the '
             "'Academic' category.",
             'https://uvu.campusgroups.com/')],
  'faculty': [('Bob Allen, Ph.D.',
               'Dean, Woodbury School of Business',
               'Woodbury School of Business',
               '801-863-8260 (email obfuscated on the live page)',
               'https://www.uvu.edu/woodbury/'),
              ('Polly Clauson', 'Director of Academic Advising', 'Woodbury School of Business', '801-863-8032', ''),
              ('Clubs Office',
               'Office',
               'Room SL-122',
               '(801) 863-5567 (email obfuscated on the live page)',
               'https://www.uvu.edu/clubs/')],
  'courses': [('—',
               'No blockchain/crypto/fintech courses confirmed. UVU catalog search is robots-blocked.',
               'https://catalog.uvu.edu/')],
  'events': [('Club Rush', '⚠ Sep 15–16, 2026', 'https://www.uvu.edu/clubs/')],
  'play': '⚠ PREMISE CORRECTION: the assumption that UVU has an active blockchain/fintech program is NOT SUPPORTED — '
          'no such program, center, or institute appears anywhere on the Woodbury School of Business site. What UVU '
          'does have is the clearest written club-partnership pathway in Utah (Handbook p.20) plus an explicit '
          'business-sponsorship mechanism (p.16). That means UVU is a place to BUILD a club relationship, not to '
          'find one. Also cross-check the Aug 19 start date — it is a week earlier than any other Utah campus.',
  'gaps': ['Aug 19 start date (anomalous — verify)',
           'Whether outside orgs may table at Club Rush, and at what cost',
           'Events Services contact',
           'Club roster']},
 {'state': 'Utah',
  'name': 'Weber State University',
  'city': 'Ogden, UT',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 4,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'Sep 6, 2026 (last day to add online); Sep 21 drop/cancellation',
  'fallbreak': 'Mon Oct 12, 2026',
  'thanksgiving': 'Nov 26–27, 2026',
  'lastclass': 'Fri Dec 11, 2026',
  'finals': 'Dec 14–17, 2026',
  'cal_url': 'https://www.weber.edu/wsuimages/registrar/AcademicCalendar/2026-2027%20Academic%20Calendar.pdf',
  'cal_status': 'CONFIRMED',
  'fair': 'Wildcat Block Party 2026',
  'fair_date': '⚠ Fri Aug 28, 2026, 8am–2pm, WSU Ogden campus — CONFIRMED on the live 2026 page',
  'fair_outside': "YES — a published 'For-Profit Vendors' category exists",
  'fair_cost': 'For-Profit Vendors: $375 (1 parking pass included). Non-profits free. WSU departments free.',
  'fair_deadline': '⚠ NO REGISTRATION DEADLINE IS PUBLISHED ANYWHERE — re-verified Aug 11, 2026 on both the main and '
                   'policy pages. The registration link is live. If a deadline matters, call 801-626-6349. Register '
                   'at saweb.weber.edu/stussex/blockparty/',
  'fair_url': 'https://www.weber.edu/blockparty/',
  'policy': "Wildcat Block Party vendor policy. ⚠ No dedicated WSU 'sales and solicitation' PPM policy was located.",
  'policy_url': 'https://www.weber.edu/blockparty/policy.html',
  'policy_key': '⚠ THE MOST DIRECTLY RELEVANT RESTRICTION IN THE DATASET, verbatim and re-verified Aug 11, 2026: '
                "'Vendors may not have students sign any kind of contract for services on site; THIS MUST TAKE PLACE "
                "AT THE VENDOR'S PLACE OF BUSINESS.' That language blocks on-the-spot account creation, wallet "
                "onboarding, or any terms-of-service acceptance at the booth. Also: the event prohibits 'retail "
                "selling' overall; vendors cannot 'actively solicit, use aggressive sales tactics or harass "
                "individuals'; 'Use of microphones or bullhorns for live announcements/broadcasting is prohibited'; "
                "canopies capped at 10'x10'. Off-campus groups MAY separately rent Shepherd Union space through "
                'Conference Services (unionscheduling@weber.edu, 801-626-7285), with a $100/hour after-hours charge; '
                'full commercial rate schedule not published.',
  'sponsor_required': 'No — pay the for-profit vendor fee',
  'clubs': [('Not enumerable',
             'No blockchain, crypto, fintech, or investment club confirmed on a live page.',
             'https://www.weber.edu/StudentInvolvement')],
  'faculty': [('Tara Peris',
               'Block Party policy contact (title not published)',
               '',
               'taraperis@weber.edu',
               'https://www.weber.edu/blockparty/'),
              ('Student Involvement and Leadership', 'Office', '', '801-626-6349', ''),
              ('Union Scheduling / Conference Services',
               'Office',
               '',
               'unionscheduling@weber.edu · 801-626-7285',
               'https://www.weber.edu/conferenceservices/union.html')],
  'courses': [('—',
               'No blockchain/crypto/fintech courses confirmed. Weber catalog search endpoint failed TLS '
               'verification.',
               'https://catalog.weber.edu/content.php?catoid=23&navoid=8163')],
  'events': [('Wildcat Block Party', '⚠ Fri Aug 28, 2026, 8am–2pm', 'https://www.weber.edu/blockparty/')],
  'play': "⚠ READ THE 'NO CONTRACTS ON SITE' RULE BEFORE BOOKING. Weber sells for-profit booths at $375, which is "
          'clean and unambiguous — but the policy explicitly forbids having students sign any contract for services '
          'at the booth. If your validation flow requires accepting terms of service on a phone at the table, that '
          'flow is non-compliant at Weber. Redesign the booth as lead-capture-only (collect an email, complete '
          "signup later off-campus) or don't book. Aug 28 also falls before a strict Sept–Dec window; flex four days "
          'to catch it.',
  'gaps': ['Block Party registration deadline',
           'Full commercial rate schedule for Shepherd Union',
           'Whether a WSU sales/solicitation PPM policy exists',
           'Club roster']}]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; sorts last.
DEADLINES = [('2026-08-14',
  'Aug 14, 2026',
  'Utah State',
  '⚠⚠ Day on the Quad OFF-CAMPUS REGISTRATION CLOSES',
  "$300, NON-REFUNDABLE — re-verified Aug 11 on the live vendor-policy page. Event Sep 2. This is USU's only outside "
  'access all year — TSC tabling is closed to non-USU entities and fronting is banned. Parking is not free to '
  'vendors.',
  'https://www.usu.edu/involvement/day-on-the-quad/',
  'dotq@usu.edu · (435) 797-2912'),
 ('2026-08-19',
  'Aug 19, 2026',
  'UVU',
  'Fall classes begin (anomalously early — verify)',
  '',
  'https://www.uvu.edu/schedule/fall/',
  ''),
 ('2026-08-28',
  'Aug 28, 2026',
  'Weber State',
  '⚠ WILDCAT BLOCK PARTY, 8am–2pm',
  "For-profit vendors $375 (incl. 1 parking pass). ⚠ Verbatim: 'Vendors may not have students sign any kind of "
  "contract for services on site; this must take place at the Vendor's place of business.' Redesign the booth as "
  'lead-capture only. NO registration deadline is published — call 801-626-6349.',
  'https://www.weber.edu/blockparty/',
  'taraperis@weber.edu · 801-626-6349'),
 ('2026-09-02',
  'Sep 2, 2026',
  'Utah State',
  '⚠ DAY ON THE QUAD, 10am–3pm (setup 8am)',
  'Register by Aug 14.',
  'https://www.usu.edu/involvement/day-on-the-quad/',
  'dotq@usu.edu'),
 ('2026-09-02',
  'Sep 2, 2026',
  'BYU Provo',
  'Fall classes begin',
  '',
  'https://catalog26byu.catalog.prod.coursedog.com/policy/dates-and-deadlines',
  ''),
 ('2026-09-15',
  'Sep 15–16, 2026',
  'UVU',
  'Club Rush',
  'Outside-org eligibility UNVERIFIED.',
  'https://www.uvu.edu/clubs/',
  '(801) 863-5567')]
