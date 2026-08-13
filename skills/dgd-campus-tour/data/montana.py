"""Montana — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published at time of research — a gap to close by phone, not a finding of absence.
Schema: reference/data-schema.md
"""

STATE = 'Montana'

CAMPUSES = [{'state': 'Montana',
  'name': 'University of Montana',
  'city': 'Missoula, MT',
  'type': 'Public',
  'tier': 'C — Opportunistic',
  'access': 2,
  'start': 'Mon Aug 24, 2026',
  'adddrop': "NOT PUBLISHED — registrar page says 'Coming Soon: Autumn Semester 2026'",
  'fallbreak': "Mon Oct 12 (Indigenous People's Day) + Wed Nov 11 (Veterans Day) — three separate no-class days",
  'thanksgiving': 'Nov 25–27, 2026',
  'lastclass': 'Fri Dec 4, 2026',
  'finals': 'Dec 7–11, 2026',
  'cal_url': 'https://www.umt.edu/provost/academiccalendar/',
  'cal_status': "CONFIRMED (calendar carries a 'subject to change' caveat)",
  'fair': 'Griz Welcome (no dedicated clubs/involvement fair is listed; UC After Dark is the closest analogue)',
  'fair_date': 'UNVERIFIED — Fall 2026 schedule not published. Pattern: ~Aug 18 to early Sept, culminating in '
               'WelcomeFeast in the first week of September.',
  'fair_outside': 'UNVERIFIED',
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://www.umt.edu/griz-welcome/schedule.php',
  'policy': '⚠ NOT RETRIEVABLE — the weakest-documented campus in the dataset',
  'policy_url': 'https://www.umt.edu/policies/',
  'policy_key': "⚠ ACTION REQUIRED: UM's solicitation and vendor policy MUST be obtained manually or by phone. Four "
                'separate UM policy and facility pages are blocked to automated fetch by robots.txt: /policies/, '
                '/policies/browse/facilities-administration/, /student-involvement/, and /uc/uc-event-services/. The '
                "University Center main page confirms only building hours. DO NOT assume UM's rules resemble MSU's — "
                'they are separate institutions under the Montana University System with distinct policy manuals.',
  'sponsor_required': 'UNKNOWN',
  'clubs': [('Not enumerable',
             'Griz Hub is JavaScript-rendered. No blockchain, crypto, fintech, finance or investment club confirmed.',
             'https://grizhub.umt.edu/organizations')],
  'faculty': [('No individual names confirmed',
               'Do not guess. Offices to look up: Registrar, University Center, Student Involvement, Provost.',
               '',
               '',
               'https://www.umt.edu/uc/')],
  'courses': [('—', 'No blockchain/crypto/fintech courses confirmed.', '')],
  'events': [('Griz Welcome', 'Fall 2026 dates UNVERIFIED', 'https://www.umt.edu/griz-welcome/schedule.php')],
  'play': 'Do not commit travel here until someone phones UM and obtains the solicitation policy in writing. '
          'Everything about outside-entity access at Missoula is currently unknown — that is a research gap, not a '
          'green light. UM also has the earliest finish in Montana (finals end Dec 11) and three separate no-class '
          'days that fragment the fall.',
  'gaps': ['⚠ The ENTIRE solicitation/vendor policy set (robots-blocked) — HIGHEST-PRIORITY MANUAL RESEARCH ITEM',
           'Add/drop deadlines',
           'Griz Welcome Fall 2026 schedule',
           'Club roster',
           'All named staff contacts']},
 {'state': 'Montana',
  'name': 'Montana State University',
  'city': 'Bozeman, MT',
  'type': 'Public',
  'tier': 'B — Regional (best-documented policy in the dataset)',
  'access': 4,
  'start': 'Wed Aug 26, 2026',
  'adddrop': 'NOT specified in the calendar PDF',
  'fallbreak': 'Wed Nov 11 (Veterans Day)',
  'thanksgiving': 'Nov 23–27, 2026 — a FULL WEEK, the most generous in the dataset',
  'lastclass': "⚠ PARTIALLY GARBLED IN SOURCE ('ursday, December 17') — UNVERIFIED",
  'finals': 'UNVERIFIED',
  'cal_url': 'https://catalog.montana.edu/academiccalendar/academiccalendar.pdf',
  'cal_status': "PARTIAL — registrar page 404'd",
  'fair': 'Catapalooza 2026',
  'fair_date': '⚠ Fri Aug 28, 2026, 10am–3pm — CONFIRMED. MSU Centennial Mall, South Campus District, and Romney '
               'Oval.',
  'fair_outside': "YES — 'We invite all community and campus organizations, BUSINESSES and student organizations to "
                  "register.' Described as an opportunity to interact with 'Bozeman community organizations and "
                  "local businesses.'",
  'fair_cost': "'Catapalooza is free for student organizations. We ask for an event fee from MSU offices and "
               "off-campus organizations.' ⚠ RE-CHECKED AUG 11, 2026 — the base off-campus fee is STILL NOT "
               'PUBLISHED: it is rendered dynamically inside the ecommerce payment form and is not exposed in the '
               'page source. To get the number, start the form at ecommerce.montana.edu/ose_catapalooza/ or call OSE '
               'at 406-994-2933. Sponsorship tiers ARE published: Bobcat $1,500 (11x10 premiere booth, logo on '
               'website + all posters); Champ $3,000 (22x10 booth in location of choice, logo on all publicity, OSE '
               'social media).',
  'fair_deadline': 'Registration opened June 17, 2026. ⚠ NO CLOSING DATE PUBLISHED (re-checked Aug 11, 2026). '
                   'Student-org signup is now CLOSED, but the off-campus link remains live.',
  'fair_url': 'https://www.montana.edu/catapalooza/',
  'policy': 'MSU Policy 400.00 — Facilities Use for Sales/Promotions and Commercial Activities (adopted Jun 1994; '
            'revised Feb 2009)',
  'policy_url': 'https://www.montana.edu/policy/facility_use/facuse400.html',
  'policy_key': 'THE CLEAREST WRITTEN ROUTE FOR AN OUTSIDE ENTITY IN THE DATASET. Non-affiliated groups may conduct '
                "commercial activity ONLY if: (1) they have contracted to rent a facility AND 'the activity is noted "
                "and approved in the contract'; (2) they have a SPONSORSHIP CONTRACT exchanging goods/services "
                'promotion for program support; or (3) activities occur in the Strand Union Building as authorized. '
                "Blanket rule: 'No state facilities, equipment and/or employees may be used for any commercial "
                "purpose.' ⚠ BUT CATAPALOOZA ITSELF IS STRICTER: 'Vendors are PROHIBITED from seeking a MONETARY "
                "EXCHANGE for products, services, or donations at Catapalooza.' 'Vendors DO NOT sell goods or "
                "services (no exchange of money).' ✓ EXPRESSLY PERMITTED: distributing 'informational items, "
                "coupons, hand-outs, freebies, company contact information' and COLLECTING CONTACT INFO to follow up "
                "post-event. ⚠ BUT WITH TWO BINDING CONDITIONS re-verified Aug 11, 2026: (1) 'If you collect contact "
                'information from potential customers interested in purchasing goods or services, you MUST CONTACT '
                'THE POTENTIAL CUSTOMER AFTER CATAPALOOZA RE-CONFIRMING THEIR INTEREST BEFORE ANY TRANSACTIONS TAKE '
                "PLACE'; (2) 'DO NOT use any contact information you collect at Catapalooza for purposes other than "
                'to contact those individuals about this specific interaction or transaction, and please do not add '
                "a potential customer to any mailing list without their specific consent.' NO LIST-BUILDING. "
                'Raffle-style and controlled-substance booths banned.',
  'sponsor_required': 'No — but a rental or sponsorship contract with the commercial activity expressly noted',
  'clubs': [('Not enumerable',
             'CatsConnect (Campus Labs). No blockchain, crypto, fintech or investment club confirmed.',
             'https://www.montana.edu/engagement/')],
  'faculty': [('Office of Student Engagement',
               '⚠ NEWLY VERIFIED office email',
               'SUB 222, PO Box 174200, Bozeman MT 59717',
               'catapalooza@montana.edu · (406) 994-2933',
               'https://www.montana.edu/catapalooza/'),
              ('Christopher Pruden',
               '⚠ NEWLY VERIFIED — Catapalooza ecommerce / registration contact',
               'Office of Student Engagement',
               'christopher.pruden@montana.edu · 406-994-5821',
               ''),
              ('Office of Legal Counsel',
               'Owner of the Freedom of Expression policy',
               '',
               '',
               'https://www.montana.edu/policy/freedom_expression/')],
  'courses': [('—', 'No blockchain/crypto/fintech courses confirmed.', 'https://catalog.montana.edu/')],
  'events': [('Catapalooza', '⚠ Fri Aug 28, 2026, 10am–3pm', 'https://www.montana.edu/catapalooza/')],
  'play': '⚠ MSU IS THE PERFECT FIT FOR A NON-TRANSACTIONAL BOOTH — and a terrible one for a transactional booth. '
          'Catapalooza bans ANY monetary exchange outright, but EXPRESSLY PERMITS handing out informational '
          'materials and collecting contact information for post-event follow-up. That is exactly the compliant '
          'shape your program should take everywhere: educate at the table, capture an email, complete validation '
          "off-campus and off-clock. Book Catapalooza and use it as the pilot for that model. MSU's Policy 400.00 is "
          'also the best-written outside-entity pathway anywhere in the nine states — a rental or sponsorship '
          'contract with the commercial activity expressly noted and approved.',
  'gaps': ['⚠ Last day of classes / finals week (source PDF garbled, registrar 404)',
           'Catapalooza off-campus fee amount and registration close date',
           'Add/drop deadlines',
           'Club roster',
           'OSE staff names']}]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; sorts last.
DEADLINES = [('2026-08-26',
  'Aug 26, 2026',
  'Montana State',
  'Fall classes begin',
  '',
  'https://catalog.montana.edu/academiccalendar/academiccalendar.pdf',
  ''),
 ('2026-08-28',
  'Aug 28, 2026',
  'Montana State',
  '⚠ CATAPALOOZA, 10am–3pm, Centennial Mall',
  'Businesses explicitly invited. Base fee still unpublished (rendered inside the ecommerce form) — call '
  '406-994-2933 or email catapalooza@montana.edu. Sponsorships ARE published: Bobcat $1,500 / Champ $3,000. ⚠ NO '
  'monetary exchange; and contacts collected must be re-confirmed after the event before any transaction, with NO '
  'list-building. This is the model booth.',
  'https://www.montana.edu/catapalooza/',
  'catapalooza@montana.edu · (406) 994-2933')]
