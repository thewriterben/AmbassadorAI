"""Wyoming — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published at time of research — a gap to close by phone, not a finding of absence.
Schema: reference/data-schema.md
"""

STATE = 'Wyoming'

CAMPUSES = [{'state': 'Wyoming',
  'name': 'University of Wyoming',
  'city': 'Laramie, WY',
  'type': 'Public',
  'tier': 'A — ANCHOR CAMPUS',
  'access': 3,
  'start': 'Mon Aug 31, 2026',
  'adddrop': 'NOT in the AY calendar PDF — check the registrar',
  'fallbreak': 'Mon Oct 12, 2026 (Mid-Semester Break)',
  'thanksgiving': 'Nov 25–27, 2026',
  'lastclass': 'Fri Dec 11, 2026 (UW Casper: Dec 13)',
  'finals': 'Dec 14–18, 2026',
  'cal_url': 'https://www.uwyo.edu/acadaffairs/_files/docs/ay-calendar-26-27.pdf',
  'cal_status': 'CONFIRMED',
  'fair': 'Involvement Fest',
  'fair_date': 'UNVERIFIED — Fall 2026 date not published. Pattern: early-to-mid September.',
  'fair_outside': "NO — registration requires a UWYO email address: 'Please register using your UWYO Email Address "
                  "ONLY.'",
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://www.uwyo.edu/csil/student-orgs/index.html',
  'policy': 'UW Regulation 11-4; UW Regulation 3-690; PD 2-1992 (facilities use with commercial entities)',
  'policy_url': 'https://www.uwyo.edu/csil/_files/student-organizations/studentorghandbook2023.pdf',
  'policy_key': "Reg 11-4: 'the Student Organization must be non-profit in nature. IT MAY NOT USE ITS POSITION TO "
                "SOLICIT OR ADVERTISE FOR COMMERCIAL PURPOSES.' Reg 3-690: 'it is not permissible to post a "
                'third-party business name on posters or via online resources when the Student Organization is '
                "collaborating with the third-party business for financial gain.' ⚠ ANTI-FRONTING: 'Fronting is "
                'permitting a non-University individual, organization, or University entity to use University '
                'property… in order to avoid fees or take advantage of benefits specific to Student Organizations '
                "and IS PROHIBITED.' Breezeway tabling: 'There is a STRICT NO SOLICITATION POLICY IN THE UNION. All "
                'the members of your group must stay behind the table and are asked to refrain from aggressive '
                "salesmanship.' Outdoor loud events only 11:45am–1:00pm and 5:00–6:00pm.",
  'sponsor_required': 'No sponsorship route — a student org cannot host DGD as a proxy. Route through PD 2-1992 as a '
                      'paying external renter.',
  'clubs': [('Blockchain Club at the University of Wyoming',
             'Listed on Presence. JS-rendered — description, officers, active status and contact UNVERIFIED.',
             'https://uwyo.presence.io/organization/university-of-wyoming-blockchain-club'),
            ('Blockchain Law and Innovation Club',
             'Appeared in a 2023 UW Giving Day page. Current status UNVERIFIED.',
             'https://give.uwyo.edu/schools/UniversityofWyoming/giving-day-2023/pages/blockchain-club')],
  'faculty': [('Center for Blockchain and Digital Innovation (CBDI)',
               'Interdisciplinary center spanning Business, Engineering, Agriculture, School of Energy Resources and '
               "Wyoming's community colleges",
               'College of Business Dept 3275',
               'blockchain@uwyo.edu · (307) 766-6847',
               'https://www.uwyo.edu/acct-fin/cbdi/index.html'),
              ('⚠ Steven Charles Lupien',
               'Ada Lovelace Director of the CBDI — DIED JULY 5, 2026. Founded the CBDI and created the '
               'first-in-the-nation interdisciplinary blockchain minor. NO SUCCESSOR NAMED ON ANY LIVE UW PAGE.',
               'College of Business',
               '—',
               'https://www.uwyo.edu/news/2026/07/a-message-from-the-president-death-of-uw-faculty-member-steve-lupien.html'),
              ('Candace Ryder',
               'Instructional Designer, Blockchain',
               'CBDI',
               'cryder2@uwyo.edu',
               'https://www.uwyo.edu/acct-fin/cbdi/directory/index.html'),
              ('⚠ CBDI directorship status',
               'RE-CHECKED AUG 11, 2026: the live CBDI site still names NO current or interim director and carries a '
               "memorial — 'Steven Charles Lupien, 1964-2026, Ada Lovelace Director.' Whether a successor has been "
               'named elsewhere COULD NOT BE VERIFIED.',
               'CBDI',
               'blockchain@uwyo.edu',
               'https://www.uwyo.edu/acct-fin/cbdi/directory/index.html'),
              ('Dr. Bradley Rettler',
               "Professor of Philosophy; DIRECTOR, BITCOIN RESEARCH INSTITUTE. Author of 'Resistance Money: A "
               "Philosophical Case for Bitcoin' (Routledge). Runs an annual summer workshop, weekly reading group, "
               'and Student Research Prizes (deadline Sept 30 annually).',
               'Philosophy and Religious Studies',
               'bitcoin@uwyo.edu',
               'https://www.uwyo.edu/philrelig/bitcoin.html'),
              ('Blockchain minor faculty',
               'Dr. Corey Billington, Dr. Danial Conway, Dr. Ali Nejadmalayeri, Dr. Soheil Sarachi — named as '
               'assisting. Individual emails not published.',
               'College of Business',
               '',
               'https://www.uwyo.edu/business/about-us/directory/'),
              ('Student Organizations', 'Office', 'Wyoming Union Room 033', 'stuorgs@uwyo.edu · (307) 766-6340', ''),
              ('Union Events Office',
               'Office',
               'Wyoming Union Room 210',
               'UnionRes@uwyo.edu · (307) 766-3161',
               'https://www.uwyo.edu/union/reservations/index.html')],
  'courses': [('BKCH 3021',
               'Fundamentals of Blockchain (3cr, required for the minor) — prereq junior standing',
               'https://www.uwyo.edu/acct-fin/cbdi/curriculum/index.html'),
              ('BKCH 4021', 'Business Applications of Blockchain (3cr, required) — prereq BKCH 3021', ''),
              ('BKCH 4121', 'Case Studies in Blockchain (3cr, elective)', ''),
              ('BKCH 4910', 'Topics in Blockchain (3cr, elective)', ''),
              ('FIN 4221', 'Blockchain & Digital Financial Services (3cr, elective)', ''),
              ('COSC 4010', 'Blockchain Design/Programming (3cr, elective)', ''),
              ('WyoBEE',
               'Wyoming Blockchain Education for Everyone — 12 teaching modules for high school juniors/seniors and '
               'community college students; NFT certification on completion',
               'https://www.uwyo.edu/acct-fin/cbdi/wyobee/index.html')],
  'events': [('⚠ WYOMING BLOCKCHAIN STAMPEDE 2026',
              'Sep 28–30, 2026, Laramie (Wyoming Union + College of Business). FREE, annual, hosted by CBDI. Sep '
              "28–29: Wyoming Legislature's SELECT COMMITTEE ON BLOCKCHAIN meets, 8:30am, Room 212. Sep 29: industry "
              'networking dinner HONORING THE LATE STEVE LUPIEN, 4pm, College of Business Atrium. Sep 30: public '
              'sessions from 9am. Registration: luma.com/8vubx2wd. ⚠ ALL RE-VERIFIED AUG 11, 2026. Minor page error: '
              "UW writes 'Tuesday, Sept. 28 and Monday, Sept. 29' — the WEEKDAY LABELS ARE SWAPPED (Sep 28, 2026 is "
              'a Monday). The dates themselves are consistent everywhere else.',
              'https://www.uwyo.edu/acct-fin/cbdi/stampede/index.html')],
  'play': '⚠⚠ THIS IS THE ANCHOR OF THE ENTIRE TOUR. The Wyoming Blockchain Stampede (Sep 28–30) is a free, public, '
          'blockchain-specific conference held ON CAMPUS, inside your window, with STATE LEGISLATORS PRESENT — the '
          "Legislature's Select Committee on Blockchain meets there Sept 28–29. Nothing else in nine states comes "
          'close. Wyoming also has the most crypto-friendly statutory environment in the US (WY-DUNA for DAOs, SPDI '
          'bank charters, and a virtual-currency exemption from money-transmitter licensing at W.S. '
          '§40-22-104(a)(vi)). ⚠ TONE WARNING: CBDI founder Steve Lupien died July 5, 2026, there is no named '
          'successor, and the Sept 29 dinner is a MEMORIAL. Attend as a participant and a mourner, not as a '
          "promoter. Do not table, do not pitch the $21 at that dinner. Separately: UW's campus rules are hostile — "
          'strict no-solicitation in the Union, Reg 11-4 bars clubs from commercial solicitation, and anti-fronting '
          'blocks the proxy route. The Stampede is the door; campus tabling is not.',
  'gaps': ['Add/drop deadlines',
           'Involvement Fest Fall 2026 date',
           'Blockchain Club active status and officers',
           'Whether BKCH sections actually run Fall 2026 given the director vacancy',
           'Wyoming Advanced Blockchain Lab status (robots-blocked)',
           'WyoHackathon 2026 status']}]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; sorts last.
DEADLINES = [('2026-09-28',
  'Sep 28–30, 2026',
  'U of Wyoming',
  '⚠⚠ WYOMING BLOCKCHAIN STAMPEDE 2026 — THE TOUR ANCHOR',
  "FREE, on campus, blockchain-specific — all re-verified Aug 11. Sep 28–29: Wyoming Legislature's Select Committee "
  'on Blockchain meets, 8:30am, Room 212 (Wyoming Union). Sep 29: networking dinner HONORING THE LATE STEVE LUPIEN, '
  '4pm. Sep 30: public sessions from 9am. ⚠ TONE: attend as a participant and a mourner, not a promoter.',
  'https://www.uwyo.edu/acct-fin/cbdi/stampede/index.html',
  'blockchain@uwyo.edu · (307) 766-6847'),
 ('2026-09-30',
  'Sep 30, 2026',
  'U of Wyoming',
  'Bitcoin Research Institute Student Research Prizes deadline (annual)',
  'Dr. Bradley Rettler, bitcoin@uwyo.edu',
  'https://www.uwyo.edu/philrelig/bitcoin.html',
  'bitcoin@uwyo.edu')]
