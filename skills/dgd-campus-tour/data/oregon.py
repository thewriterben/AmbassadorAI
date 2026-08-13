"""Oregon — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published at time of research — a gap to close by phone, not a finding of absence.
Schema: reference/data-schema.md
"""

STATE = 'Oregon'

CAMPUSES = [{'state': 'Oregon',
  'name': 'University of Oregon',
  'city': 'Eugene, OR',
  'type': 'Public',
  'tier': 'A — Added (strongest crypto club in the region)',
  'access': 5,
  'start': 'Mon Sep 28, 2026 (QUARTER)',
  'adddrop': 'Mon Oct 5, 2026 (last day to register/add)',
  'fallbreak': '—',
  'thanksgiving': 'Nov 26–27, 2026',
  'lastclass': 'Fri Dec 4, 2026',
  'finals': 'Dec 7–11, 2026',
  'cal_url': 'https://registrar.uoregon.edu/dates-deadlines/five-year-calendar',
  'cal_status': 'CONFIRMED',
  'fair': 'ASUO Street Faire — bi-annual outdoor faire; proceeds support UO student food-security initiatives',
  'fair_date': '⚠ Oct 14–16, 2026 — CONFIRMED. Wed/Thu 10am–6pm, Fri 10am–5pm. Along 13th Avenue, center of campus.',
  'fair_outside': 'YES — outside commercial businesses (with insurance), food vendors, craft/merchandise vendors, '
                  'nonprofits, and RSOs',
  'fair_cost': 'Booth fees vary by vendor type; reduced rates for nonprofits/affiliates; free for ASUO-recognized '
               'groups. Commercial rate UNVERIFIED — request the schedule. Nonrefundable $20 application fee covers '
               'both 2026 and 2027 faires.',
  'fair_deadline': '⚠ Applications RELEASE IN AUGUST 2026 — i.e. now. Requires proof of liability insurance and '
                   'product descriptions with photos.',
  'fair_url': 'https://sges.uoregon.edu/streetfaire',
  'policy': 'Scheduling and Event Services — Procedures and Practices',
  'policy_url': 'https://scheduling.uoregon.edu/procedures-practices',
  'policy_key': "'Unaffiliated Users' = organizations/individuals not recognized as Student Organizations or UO "
                "Departments. They 'must pay FULL RENTAL RATES… and must provide a signed Facilities Use Agreement, "
                "indemnification and PROOF OF INSURANCE.' ⚠ ANTI-FRONTING: 'Student Organizations and UO Departments "
                "MAY NOT RESERVE SPACE FOR OTHER ORGANIZATIONS for the purpose of securing lower rental rates.' "
                'Outside vendors: max 2 days/week, bookable 2 weeks at a time; PRODUCT VENDORS RESTRICTED TO THE '
                "UPPER AMPHITHEATER AREA ONLY; fees typically $20–330/day. 10'x10' space, one 6' table, two chairs. "
                "'Tablers/vendors must be present at the table during all hours reserved.' $100 non-refundable "
                'deposit on contract; cancellation within 1 week = 100% of fees. Insurance: $1M CGL / $2M aggregate, '
                "UO named as additional insured (TULIP available). Events over 300 attendees need 28 days' notice.",
  'sponsor_required': 'No — pay full rate; sponsorship route explicitly foreclosed',
  'clubs': [('Oregon Blockchain Group (OBG)',
             "⚠ THE STRONGEST CRYPTO CLUB IN THE NINE STATES. 'Community-oriented organization educating students "
             "about emergent technologies.' ACTIVE — 2025 travel to Consensus Toronto, Solana NYC, WebX Tokyo, ETH "
             "Cannes, UPenn Blockchain Hackathon. Claims '#1 Blockchain Research Institute in Pacific Northwest,' "
             "60K+ VC funds under management, 30+ company partnerships. Part of RIPPLE'S University Blockchain "
             'Research Initiative (UBRI). Contacts: uobg@uoregon.edu; uo.blockchain@gmail.com',
             'https://www.oregonblockchain.org/'),
            ('Oregon Quant Group',
             'Quantitative finance — oqg@uoregon.edu',
             'https://business.uoregon.edu/community/clubs-organizations'),
            ('UO Investment Group', 'Fundamental equity valuation, portfolio mgmt — uoig@uoregon.edu', ''),
            ('Financial Management Association', 'uofma@uoregon.edu', ''),
            ('Oregon Founders Club', 'Entrepreneurship — foundersclub@uoregon.edu', ''),
            ('AI Student Association', 'aisa@uoregon.edu', '')],
  'faculty': [('Scheduling and Event Services',
               'Office',
               '236 EMU',
               'scheduling@uoregon.edu · 541-346-6000',
               'https://scheduling.uoregon.edu/procedures-practices'),
              ('ASUO Street Faire',
               'Office',
               'EMU Suite 004',
               'asuostreetfaire@uoregon.edu · 541-346-0622',
               'https://sges.uoregon.edu/streetfaire'),
              ('(No named blockchain faculty)',
               "The UO 'Leading the Blockchain Revolution' article names NO faculty; Oregon Blockchain is 'a "
               "student-run initiative' formed April 2018. UO's only institutional tie is UBRI membership.",
               'Lundquist College',
               '',
               'https://business.uoregon.edu/faculty')],
  'courses': [('—',
               'UNVERIFIED — no blockchain/crypto course confirmed in the UO catalog. UO has run a non-credit '
               'Blockchain Boot Camp.',
               'https://catalog.uoregon.edu/')],
  'events': [('ASUO Street Faire',
              '⚠ Oct 14–16, 2026 — the main vendor-accessible event',
              'https://sges.uoregon.edu/streetfaire')],
  'play': '⚠ TOP-3 CAMPUS OVERALL, BUT APPROACH OBG WITH RESPECT. Two independent doors: (1) the ASUO Street Faire, '
          'Oct 14–16, an actual commercial vendor faire on 13th Avenue with applications opening now — get insurance '
          '($1M/$2M with UO as additional insured) lined up first; (2) Oregon Blockchain Group, which is '
          'Ripple-UBRI-affiliated, manages real VC funds, and travels internationally. OBG is a SOPHISTICATED '
          'AUDIENCE WITH EXISTING INDUSTRY RELATIONSHIPS, not a greenfield. Pitch them research collaboration or a '
          'technical talk. A $21-signup pitch will read as beneath them.',
  'gaps': ['Commercial booth rate for Street Faire',
           'UO fall org fair (separate from Street Faire)',
           'Catalog course search']},
 {'state': 'Oregon',
  'name': 'Oregon State University',
  'city': 'Corvallis, OR',
  'type': 'Public',
  'tier': 'A — Added (nearest deadline in the dataset)',
  'access': 5,
  'start': 'Wed Sep 23, 2026 (QUARTER)',
  'adddrop': 'UNVERIFIED',
  'fallbreak': '—',
  'thanksgiving': 'Nov 26–27, 2026',
  'lastclass': 'Fri Dec 4, 2026',
  'finals': 'Ends Fri Dec 11, 2026',
  'cal_url': 'https://registrar.oregonstate.edu/sites/registrar.oregonstate.edu/files/2024-03/osu-4-year-calendar-2026-2027.pdf',
  'cal_status': 'CONFIRMED',
  'fair': 'Beaver Community Fair 2026 (OSU Program Council / Experiential Learning & Activities)',
  'fair_date': '⚠ Fri Sep 25, 2026 — Memorial Quad & SEC Plaza. CONFIRMED.',
  'fair_outside': 'YES — EXPLICITLY. Three tiers: (1) RSOs/departments free; (2) external businesses and nonprofits '
                  'paid; (3) tax-exempt/government discounted.',
  'fair_cost': 'External business: $200. Tax-exempt organization or government agency: $150. Additional booth $200; '
               'additional table $35. ⚠ ALL RE-VERIFIED AUG 11, 2026.',
  'fair_deadline': '⚠⚠ 5:00 PM PST, AUG 27, 2026 — 16 DAYS OUT. Fees due Fri Sep 11, 2026, 5pm.',
  'fair_url': 'https://see.oregonstate.edu/ela/osu-program-council/events/beaver-community-fair',
  'policy': 'Memorial Union Policies (2025 ed.) — the primary governing document',
  'policy_url': 'https://mu.oregonstate.edu/policies',
  'policy_key': '⚠ GAP: the MU Policies PDF could not be parsed. Its detailed tabling, solicitation and fee '
                'provisions are UNVERIFIED — READ IT BEFORE COMMITTING. The RSO-sponsorship requirement and any '
                'financial-product marketing ban are inside that document. MU Reservations: '
                'reservations@oregonstate.edu · 541-737-0634.',
  'sponsor_required': 'UNVERIFIED — but the Beaver Community Fair sells directly to external businesses, no sponsor '
                      'needed',
  'clubs': [('Oregon State Investment Group (OSIG)',
             'ACTIVE. Actively manages a $1.5 MILLION equity portfolio for the OSU Foundation plus two additional '
             'funds; members analyze companies within assigned sectors. No contact email published on the directory '
             'page.',
             'https://clubs.oregonstate.edu/osig'),
            ('Hackathon Club at Oregon State', 'Runs BeaverHacks', 'https://beaverhacks.org/'),
            ('NO blockchain/crypto club at OSU',
             "⚠ 'Oregon Blockchain Group' is a UNIVERSITY OF OREGON org — do not conflate.",
             'https://clubs.oregonstate.edu/')],
  'faculty': [('MU Reservations',
               'Office',
               '',
               'reservations@oregonstate.edu · 541-737-0634',
               'https://mu.oregonstate.edu/policies'),
              ('Ella Tenido',
               '⚠ NEWLY VERIFIED — Beaver Community Fair registration contact',
               'Experiential Learning & Activities',
               'ella.tenido@oregonstate.edu',
               'https://see.oregonstate.edu/ela/osu-program-council/events/beaver-community-fair'),
              ('OSU Program Council',
               '⚠ NEWLY VERIFIED office email',
               'Student Experience Center 108',
               'osupc@oregonstate.edu · 541-737-1566',
               ''),
              ('Joshua Chilango',
               'BeaverHacks event contact',
               '',
               'chilangj@oregonstate.edu · 541-250-1435',
               'https://events.oregonstate.edu/event/beaverhacks-2026')],
  'courses': [('FIN 455',
               "FinTech and Applied AI in Finance (4cr) — 'Examines fintech and the application of AI and "
               "data-driven technologies in financial markets and financial services.' Covers data management, ML, "
               'NLP; ethics and regulatory challenges.',
               'https://catalog.oregonstate.edu/courses/fin/'),
              ('FIN 448',
               "International Financial Markets (4cr) — mentions 'CRYPTOCURRENCY MARKETS' alongside international "
               'equity, bond, FX and derivative markets',
               'https://catalog.oregonstate.edu/courses/fin/'),
              ('(non-credit)',
               "'Practical Blockchain and Cryptocurrency' — OSU Ecampus career hub, not a catalog course",
               'https://careers.ecampus.oregonstate.edu/classes/practical-blockchain-and-cryptocurrency/')],
  'events': [('Beaver Community Fair',
              '⚠ Fri Sep 25, 2026',
              'https://see.oregonstate.edu/ela/osu-program-council/events/beaver-community-fair'),
             ('BeaverHacks', '⚠ SPRING event (~May 2026) — NOT in the Fall window', 'https://beaverhacks.org/')],
  'play': '⚠⚠ THE SINGLE NEAREST DEADLINE IN THE ENTIRE DATASET: Aug 27, 5pm PST, 16 days out. The Beaver Community '
          'Fair is the best-documented, most explicitly business-open tabling opportunity anywhere in the nine '
          'states — $200, a published tier structure, and no sponsor required. Register FIRST, then read the MU '
          "Policies PDF to understand what you may actually do at the booth. OSIG's $1.5M OSU Foundation mandate "
          'makes it a serious secondary target.',
  'gaps': ['⚠ MU Policies PDF — the governing tabling/solicitation document, unparsed',
           'Add/drop deadlines',
           'OSIG contact email',
           'Whether FIN 455/448 run Fall 2026']},
 {'state': 'Oregon',
  'name': 'Portland State University',
  'city': 'Portland, OR',
  'type': 'Public',
  'tier': "A — Added (region's only blockchain credential)",
  'access': 4,
  'start': 'Mon Sep 28, 2026 (QUARTER)',
  'adddrop': 'UNVERIFIED',
  'fallbreak': '—',
  'thanksgiving': 'UNVERIFIED',
  'lastclass': 'Sun Dec 6, 2026',
  'finals': 'Ends Sat Dec 12, 2026',
  'cal_url': 'https://www.pdx.edu/registration/academic-calendar',
  'cal_status': 'PARTIAL',
  'fair': "Party in the Park (PSU's flagship fall involvement fair; part of Viking Days)",
  'fair_date': '⚠ Thu Oct 1, 2026, 11:00am–2:00pm — CONFIRMED. South Park Blocks at Smith Memorial Student Union.',
  'fair_outside': "YES — three categories including 'external organizations and businesses AS SPONSORS'",
  'fair_cost': 'NOT PUBLISHED — contact the SALP Executive Director',
  'fair_deadline': 'NOT PUBLISHED',
  'fair_url': 'https://www.pdx.edu/student-leadership/party-in-the-park',
  'policy': 'SALP Policy Manual (behind a CampusGroups shell — contents UNVERIFIED)',
  'policy_url': 'https://sites.google.com/pdx.edu/student-leader-resource-center/policy-manual',
  'policy_key': '⚠ GAP: The SALP Policy Manual did not render for automated retrieval. Sponsorship requirements, '
                'table fees, free-speech-zone rules and any financial-product marketing ban are ALL UNVERIFIED. Ask '
                'asksalp@pdx.edu directly. SMSU / Conference Services handles space rental for outside groups.',
  'sponsor_required': 'UNVERIFIED',
  'clubs': [('Not enumerable',
             'Portland State Connect / CampusGroups. ⚠ NO blockchain/crypto student club identified — notable given '
             "PSU has the region's only blockchain academic certificate. Worth checking the directory directly.",
             'https://pdx.campusgroups.com/')],
  'faculty': [('Aimee Shattuck',
               'Executive Director, Student Activities & Leadership Programs (SALP) — the EXTERNAL ORG/BUSINESS '
               'INTAKE POINT',
               'SALP',
               'shattuck@pdx.edu',
               'https://www.pdx.edu/student-leadership/party-in-the-park'),
              ('SALP general', 'Office', '', 'asksalp@pdx.edu', ''),
              ('Kristi Yuthas',
               '⚠ THE SINGLE MOST RELEVANT CONFIRMED FACULTY CONTACT IN THE ENTIRE DATASET. Professor, School of '
               "Business. 'Currently interested in the social, ethical, and economic impacts of BLOCKCHAIN and "
               "distributed ledger technologies.' FOUNDED the Business Blockchain Certificate Program (launched Fall "
               "2019); 'currently teaches blockchain conceptual and lab courses at the undergraduate and graduate "
               "levels.'",
               'School of Business',
               'kristi.yuthas@pdx.edu · (503) 725-5099',
               'https://www.pdx.edu/business/profile/kristi-yuthas')],
  'courses': [('Business Blockchain Certificate',
               "Undergraduate — the region's ONLY dedicated blockchain credential. Page 403'd to automated fetch; "
               'course codes UNVERIFIED.',
               'https://www.pdx.edu/academics/programs/undergraduate/business-blockchain'),
              ('Business Blockchain Graduate Certificate',
               'Graduate — same, 403',
               'https://www.pdx.edu/academics/programs/graduate/business-blockchain'),
              ("'Unlocking Blockchain for Business Leaders'",
               'Professional / non-credit',
               'https://www.pdx.edu/professional-education/unlocking-blockchain-for-business-leaders')],
  'events': [('Party in the Park',
              '⚠ Thu Oct 1, 2026, 11am–2pm, South Park Blocks',
              'https://www.pdx.edu/student-leadership/party-in-the-park'),
             ('Viking Days', "PSU's fall welcome program", 'https://www.pdx.edu/viking-days')],
  'play': '⚠ LOWEST-FRICTION FIRST CONTACT IN THE ENTIRE DATASET. PSU is the ONLY campus that publishes a NAMED '
          'INDIVIDUAL as the external-business intake point: Aimee Shattuck, shattuck@pdx.edu. External orgs must '
          'contact her directly, not through the portal. Second, and more important: Prof. Kristi Yuthas founded and '
          "teaches the region's only blockchain certificate program and lists blockchain's SOCIAL AND ETHICAL "
          'impacts as her active research interest. She is the highest-value academic conversation available to you '
          '— and she will ask hard questions about the referral mechanic. Have a real answer ready.',
  'gaps': ['Party in the Park external-org fee and deadline',
           '⚠ SALP Policy Manual contents',
           'Blockchain certificate course codes',
           'Whether any blockchain student club exists']}]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; sorts last.
DEADLINES = [('2026-08-27',
  'Aug 27, 2026',
  'Oregon State',
  '⚠⚠ BEAVER COMMUNITY FAIR VENDOR REGISTRATION CLOSES, 5:00pm PST',
  'External business $200; tax-exempt/government $150. Event Sep 25. Best-documented business-open fair in the '
  'dataset. Fees due Sep 11, 5pm. Contact: Ella Tenido, ella.tenido@oregonstate.edu; osupc@oregonstate.edu.',
  'https://see.oregonstate.edu/ela/osu-program-council/events/beaver-community-fair',
  'ella.tenido@oregonstate.edu · 541-737-1566'),
 ('2026-09-25',
  'Sep 25, 2026',
  'Oregon State',
  '⚠ BEAVER COMMUNITY FAIR, Memorial Quad & SEC Plaza',
  'Register by Aug 27, 5pm PST.',
  'https://see.oregonstate.edu/ela/osu-program-council/events/beaver-community-fair',
  '541-737-1566'),
 ('2026-10-01',
  'Oct 1, 2026',
  'Portland State',
  '⚠ PARTY IN THE PARK, 11am–2pm, South Park Blocks',
  'External orgs admitted AS SPONSORS. Fee and deadline unpublished — contact Aimee Shattuck directly, not the '
  'portal.',
  'https://www.pdx.edu/student-leadership/party-in-the-park',
  'shattuck@pdx.edu'),
 ('2026-10-14',
  'Oct 14–16, 2026',
  'U of Oregon',
  '⚠ ASUO STREET FAIRE, 13th Avenue',
  'Commercial vendors admitted with insurance ($1M/$2M, UO as additional insured). $20 nonrefundable application '
  'fee. APPLICATIONS RELEASE AUGUST 2026 — apply now.',
  'https://sges.uoregon.edu/streetfaire',
  'asuostreetfaire@uoregon.edu · 541-346-0622')]
