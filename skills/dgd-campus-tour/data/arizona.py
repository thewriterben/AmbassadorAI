"""Arizona — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published at time of research — a gap to close by phone, not a finding of absence.
Schema: reference/data-schema.md
"""

STATE = 'Arizona'

CAMPUSES = [{'state': 'Arizona',
  'name': 'Arizona State University',
  'city': 'Tempe, AZ',
  'type': 'Public (ABOR)',
  'tier': 'A — Added (high priority)',
  'access': 3,
  'start': 'Thu Aug 20, 2026',
  'adddrop': 'Wed Aug 26, 2026 (Session A/C, no W); Tue Oct 20 (Session B)',
  'fallbreak': 'Oct 10–13, 2026 (classes excused, university open)',
  'thanksgiving': 'Nov 26–27, 2026',
  'lastclass': 'Fri Dec 4, 2026 (Sessions B & C); Session A ends Fri Oct 9',
  'finals': 'Dec 7–12, 2026 (Session C)',
  'cal_url': 'https://registrar.asu.edu/academic-calendar',
  'cal_status': 'CONFIRMED',
  'fair': "Passport to ASU — ASU's flagship club fair, 500+ student organizations",
  'fair_date': 'UNVERIFIED — Fall 2026 date not published anywhere reachable. Pattern: the Wednesday of Welcome Week '
               'in August, evening, spanning the Sun Devil Fitness Complex, Memorial Union, Student Pavilion and '
               'Hayden Library.',
  'fair_outside': 'NO — framed entirely around student organizations; outside-vendor participation is not advertised '
                  'and is inconsistent with SSM 802-01',
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://eoss.asu.edu/clubs/passport',
  'policy': 'SSM 802-01 Scheduling Outdoor Campus Activities Areas; SSM 802-02 Sales and Promotion (on Campus)',
  'policy_url': 'https://public.powerdms.com/ASU/documents/1560623',
  'policy_key': "SSM 802-01: 'ASU DOES NOT MAKE SPACE AVAILABLE TO INDIVIDUALS OR NON-ASU ORGANIZATIONS FOR PRIVATE "
                "USE.' External orgs may access outdoor areas ONLY if 'sponsored by an ASU-registered student "
                "organization or ASU department.' ⚠ CRITICAL LIMIT: student groups sponsoring outside vendors for "
                "sales get FIVE DAYS EACH SEMESTER, and the proceeds must 'raise money for the sponsoring student "
                "organization.' Vendors must complete a Sales/Promotion Agreement; 'DIRECT PRIVATE SALES TO "
                "INDIVIDUALS ARE NOT PERMITTED.' Bans 'fixed or immobile signage of any kind.' SSM 802-02: external "
                "vendors may participate only 'as part of an ASU-sponsored event'; individuals seeking personal gain "
                'are prohibited; outdoor event/sales requests ≥3 full working days ahead, and events involving '
                'non-university individuals ≥2 WEEKS ahead due to added approvals, insurance and fees. ASU '
                'departments CANNOT conduct raffles (per Arizona AG determination). Available outdoor sales spaces '
                'for non-university orgs: portions of Cady Mall, Orange Mall, Student Services Lawn.',
  'sponsor_required': 'Yes — ASU-registered student org or department, capped at 5 days/semester, proceeds must '
                      'benefit the sponsor',
  'clubs': [('⚠ Blockchain at ASU',
             "CONFIRMED on an ASU-hosted page. 'Serves to educate students about the underpinning cryptography and "
             "computer science of blockchain technology'; covers finance, healthcare, supply chain. PARTNERS WITH "
             'THE ASU BLOCKCHAIN RESEARCH LAB. Reachable via Discord, Twitter, Instagram (@blockchain.at.asu), '
             "SunDevilSync, LinkedIn ('blockchainasu'). The page lists five officers by name — rosters turn over "
             'annually; VERIFY BEFORE USING ANY NAME.',
             'https://blockchain.asu.edu/blockchainclub'),
            ('⚠ Blockchain, FinTech & Cryptography Club at ASU (BFC)',
             'Independent site thebfc.club. Focus: education, research, community. Email: bfcasu@protonmail.com. '
             'Discord: discord.gg/vxdf3fRPC4. ADVISOR: DR. DRAGAN BOSCOVIC. Listed events carry no year and are '
             'likely stale.',
             'https://thebfc.club/'),
            ('(Sun Devil Central directory)',
             'JS-rendered — look up fintech / investment / FMA / ACM / data science orgs',
             'https://sundevilcentral.eoss.asu.edu/')],
  'faculty': [('⚠⚠ Dr. Dragan Boscovic',
               'Clinical Professor, Dept. of Information Systems; DIRECTOR, ASU BLOCKCHAIN RESEARCH LAB; Associate '
               'Director, Center for AI and Data Analytics; Research Director, AZ Blockchain Applied Research '
               'Center; CEO, VizLore LLC. Research: distributed ledger technology in circular-economy models, '
               'generative AI for automated smart-contract creation. Prior: ~20 years at Motorola and Google, 24 '
               'patents. ⚠ BOTH a lab director AND the BFC club advisor — THE SINGLE HIGHEST-LEVERAGE CONTACT ACROSS '
               'ALL 30 CAMPUSES.',
               'Information Systems / W. P. Carey',
               'dragan.boscovic@asu.edu · (480) 965-2770 (lab) · 480-965-5368 (directory)',
               'https://blockchain.asu.edu/team/contact-us'),
              ('Student org offices',
               'Tempe: Student Pavilion 2nd Floor #221E-H. Downtown Phoenix: Student Center @ The Post Office #221, '
               '602-496-2013. Polytechnic: 480-727-1098. West Valley: University Center Bldg #110, 602-543-8200.',
               '',
               '',
               'https://eoss.asu.edu/clubs')],
  'courses': [('CSE 598',
               'Engineering Blockchain Applications — referenced via third-party only, NOT confirmed on an ASU '
               'catalog page. UNVERIFIED.',
               'https://catalog.apps.asu.edu/catalog/classes'),
              ("'Intro to Web3'", 'ASU Blockchain Research Lab offering', 'https://blockchain.asu.edu/web3'),
              ('(Law)',
               'ASU College of Law maintains a blockchain research guide',
               'https://libguides.law.asu.edu/lawandscience/blockchain')],
  'events': [('Fall Welcome / InfernoFest / Echo from the Buttes',
              'Recur annually; Fall 2026 dates UNVERIFIED',
              'https://eoss.asu.edu/welcome/events/signature')],
  'play': '⚠ START HERE FOR THE SOUTHWEST LEG — but start with a person, not a booth. Dr. Dragan Boscovic directs '
          'the ASU Blockchain Research Lab AND advises the BFC club: one email reaches both the institutional '
          'research capacity and a student organization. ASU also has TWO distinct, confirmable blockchain clubs, '
          "which no other campus in the dataset does. The tabling path is genuinely hard (ASU 'does not make space "
          "available to non-ASU organizations,' sponsorship is capped at 5 days/semester, and proceeds must benefit "
          'the sponsoring club) — so treat ASU as a relationship and speaking opportunity, not a booth. Note also: '
          'ASU bans raffles per an Arizona AG determination, which rules out any token giveaway structured as a '
          'raffle.',
  'gaps': ['Passport to ASU Fall 2026 date',
           'Whether CSE 598 exists and runs Fall 2026',
           'Current officer rosters for both clubs',
           'SSM 1001-04/1001-05 fee amounts']},
 {'state': 'Arizona',
  'name': 'University of Arizona',
  'city': 'Tucson, AZ',
  'type': 'Public (ABOR)',
  'tier': 'A — Added (cleanest paid access in the dataset)',
  'access': 5,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'UNVERIFIED',
  'fallbreak': 'UNVERIFIED (typically a 2-day break in mid-October)',
  'thanksgiving': 'UNVERIFIED (typically Nov 26–27)',
  'lastclass': 'UNVERIFIED',
  'finals': 'UNVERIFIED (semester ends Thu Dec 17, 2026)',
  'cal_url': 'https://catalog.arizona.edu/calendar',
  'cal_status': 'Term span CONFIRMED (Aug 24 – Dec 17); intra-semester dates UNVERIFIED (JS-rendered tables)',
  'fair': '⚠ ASUA VENDOR FAIR — a purpose-built, PAID, outside-business tabling event on the UA Mall',
  'fair_date': '⚠ RE-VERIFIED AUG 11, 2026: THE PAGE IS STALE. It still displays the 2025–26 cycle (Fall 2025 Sept '
               '3; Spring 2026 Jan 28) and has NOT been updated for Fall 2026. Its own deadline text is internally '
               "inconsistent — the timeline says 'Registration Closes: August 15th' while the forms deadline says "
               "'Saturday, August 16th at 5:00 PM.' Aug 16, 2026 is a SUNDAY, confirming those are 2025 leftovers.",
  'fair_outside': "⚠ YES — EXPLICITLY. 'Businesses and organizations to showcase their products and services to "
                  "students, families, and our University of Arizona community.' BOTH for-profit and nonprofit "
                  'organizations. Past vendors include retailers, entertainment venues, food establishments.',
  'fair_cost': 'For-profit: $500 single event / $800 school-year package (both fairs). Nonprofit: $100 single / $200 '
               'school year. Booth includes one table, two chairs, and parking for one vehicle. Tents not provided. '
               '(Fees RE-VERIFIED Aug 11, 2026 — the fee tiers are current even though the dates are not.)',
  'fair_deadline': '⚠ UNKNOWN — TREAT AS UNSCHEDULABLE UNTIL THE PAGE REFRESHES. The Aug 16 date recorded earlier '
                   'belongs to the 2025 cycle, not 2026. First-come, first-served when it opens. PHONE 520-621-2782; '
                   'DO NOT EMAIL. Ask when Fall 2026 dates post and whether registration is open.',
  'fair_url': 'https://www.asuatoday.arizona.edu/vendor-fair',
  'policy': 'Campus Use Policy (Interim), policy no. SA-200; Campus Use Scheduling (Arizona Student Unions); Clubs '
            'Handbook 2026-2027',
  'policy_url': 'https://policy.arizona.edu/ethics-and-conduct/campus-use-policy-interim',
  'policy_key': "SA-200 defines 'Commercial Activity' as '(a) all advertising, sales, purchases, or agreements for "
                'the sale or purchase of goods or services; (b) all giving, demonstration, or solicitation for the '
                "purchase or sale of goods or services.' 'COMMERCIAL ACTIVITY IS GENERALLY PROHIBITED ON UNIVERSITY "
                "PROPERTY' — the Vendor Fair and club-sponsored fundraising are the carve-outs. The Mall splits into "
                'Reserved Areas (advance scheduling) and Unreserved Areas (no reservation for petitions, literature '
                "distribution, picketing) — but 'literature distribution' ≠ commercial promotion; the "
                'commercial-activity ban still governs content. Outdoor space requests: 10 business days ahead. '
                "Campus Use Scheduling: 'COMMERCIAL ACTIVITIES REQUIRE EXPLICIT APPROVAL TO PROTECT CONSUMERS. "
                "UNAPPROVED VENDORS ARE PROHIBITED ON CAMPUS.' Verify approval status by calling (520) 626-2630. "
                "Vendors must hold city and state licensing. Approval takes 'a minimum of two calendar weeks.' "
                'Amplification M–F 12–1pm & 5–7pm; 85 dB max. ⚠ CLUBS HANDBOOK: recognized clubs in good standing '
                "have the 'ABILITY TO SPONSOR FUNDRAISING EVENTS (INCLUDING THE SPONSORSHIP OF COMMERCIAL VENDORS ON "
                "THE UA MALL)' — the clearest written club-sponsorship route in the dataset. ⚠ RAFFLES PROHIBITED: "
                "'UA, departments, administrative units, and student organizations are NOT permitted to conduct "
                "raffles.'",
  'sponsor_required': 'No for the Vendor Fair; a club-sponsorship route also exists and is explicitly documented',
  'clubs': [('NOT ENUMERATED',
             "The ASUA club directory fetch was robots-blocked. UA uses Campus Groups as 'the hub for all student "
             "organizations.' Search: blockchain, crypto, bitcoin, Web3, fintech, investment, finance, economics, "
             'entrepreneurship, ACM, data science, FMA. Eller College of Management is the likely home for finance '
             'orgs. ⚠ COULD NOT CONFIRM a blockchain club at UArizona — do not assume one exists.',
             'https://asua.arizona.edu/clubs')],
  'faculty': [('ASUA Vendor Fair',
               'Office',
               '',
               'asua-vendorfair@arizona.edu · 520-621-2782',
               'https://www.asuatoday.arizona.edu/vendor-fair'),
              ('Campus Use Scheduling / Dean of Students',
               'Office',
               '',
               'DOS-UACampususe@arizona.edu · (520) 626-2630',
               'https://union.arizona.edu/services/campus-use-scheduling'),
              ('(Faculty)',
               'NOT CONFIRMED. Look up at Eller College Finance dept and Computer Science.',
               '',
               '',
               'https://eller.arizona.edu/departments/finance')],
  'courses': [('—',
               'UNVERIFIED. The College of Law maintains a blockchain research guide, but no catalog course was '
               'confirmed.',
               'https://catalog.arizona.edu/')],
  'events': [('ASUA Vendor Fair',
              '⚠ Fall 2026 date TBC — prior cycle was Sept 3',
              'https://www.asuatoday.arizona.edu/vendor-fair'),
             ('ASUA Club Fair',
              'Student orgs only; Fall 2026 date UNVERIFIED',
              'https://welcome.arizona.edu/events/asua-club-fair-0')],
  'play': '⚠ CALL 520-621-2782 — BUT THIS IS NOT A 5-DAY EMERGENCY. A verification pass on Aug 11, 2026 found the '
          "ASUA Vendor Fair page STILL SHOWING THE 2025–26 CYCLE; the 'Aug 16 deadline' is a 2025 leftover (Aug 16, "
          '2026 is a Sunday). Nothing can be registered until the page refreshes. That said, this remains the '
          'cleanest, most purpose-built commercial access point found anywhere in the nine states: an explicit '
          'for-profit tier at $500/event or $800 for the year, a published booth spec, no sponsor required, and no '
          'insurance certificate needed unless you serve food or display a vehicle. Call, ask when Fall 2026 dates '
          'post, and get on the list. UA ALSO has the clearest written club-sponsorship pathway anywhere '
          "('sponsorship of commercial vendors on the UA Mall' is an enumerated club privilege), giving you a second "
          'independent route. Note: raffles are prohibited university-wide, so no raffle-structured giveaways.',
  'gaps': ['⚠ Fall 2026 Vendor Fair dates and registration deadline — the page is STALE (2025–26 cycle still '
           'displayed). CALL 520-621-2782.',
           'Add/drop, fall break, Thanksgiving, finals dates',
           'Whether any blockchain club exists',
           'Faculty in blockchain/fintech',
           'Mall Fees document']},
 {'state': 'Arizona',
  'name': 'Northern Arizona University',
  'city': 'Flagstaff, AZ',
  'type': 'Public (ABOR)',
  'tier': 'C — Opportunistic',
  'access': 2,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'UNVERIFIED',
  'fallbreak': 'UNVERIFIED',
  'thanksgiving': 'UNVERIFIED',
  'lastclass': 'UNVERIFIED',
  'finals': 'UNVERIFIED (term ends Fri Dec 11, 2026)',
  'cal_url': 'https://in.nau.edu/registrar/important-dates/',
  'cal_status': 'Term span CONFIRMED (Aug 24 – Dec 11); detail UNVERIFIED (JS-rendered)',
  'fair': 'NOT FOUND — NAU runs student org activity through TRUE BLUE Connects (CampusLabs)',
  'fair_date': 'UNVERIFIED',
  'fair_outside': 'UNVERIFIED',
  'fair_cost': '',
  'fair_deadline': '',
  'fair_url': 'https://nau.campuslabs.com/engage',
  'policy': 'NOT RETRIEVED — UNVERIFIED',
  'policy_url': 'https://in.nau.edu/campusevents/event-information-form/',
  'policy_key': '⚠ NAU is governed by the Arizona Board of Regents, the same system as ASU and UArizona, so '
                'ABOR-level policy on commercial activity and campus use is LIKELY to parallel those campuses — BUT '
                'THIS IS INFERENCE, NOT A CONFIRMED NAU POLICY CITATION. DO NOT RELY ON IT. Start with the Event '
                'Information Form and the Dean of Students organization pages.',
  'sponsor_required': 'UNVERIFIED',
  'clubs': [('NOT ENUMERATED',
             "Directory is JS-rendered ('This application requires JavaScript to be enabled').",
             'https://nau.campuslabs.com/engage/organizations')],
  'faculty': [('Office of the Registrar',
               'Office',
               '',
               'registrar@nau.edu · 928-523-5490 (M–Tu 8–5, W 9:15–5, Th 8–5)',
               'https://in.nau.edu/registrar/important-dates/'),
              ('University Advising', 'Office', '', 'UniversityAdvising@nau.edu · (928) 523-4772', ''),
              ('(Faculty)',
               'NOT CONFIRMED. Look up at the W. A. Franke College of Business and the School of Informatics, '
               'Computing & Cyber Systems.',
               '',
               '',
               'https://nau.edu/franke-college-business/')],
  'courses': [('—', 'UNVERIFIED.', 'https://catalog.nau.edu/')],
  'events': [('—', 'UNVERIFIED', 'https://nau.edu/events/')],
  'play': 'Lowest information in Arizona and a 2.5-hour drive north of Phoenix. Nothing is confirmed except term '
          'start and end. Only worth a stop if you are already driving between Phoenix and Utah, and only after '
          'someone retrieves the actual NAU policy — do not extrapolate from ASU or UArizona.',
  'gaps': ['ALL policy (nothing retrieved)',
           'Any student-org fair',
           'Add/drop, breaks, finals',
           'Club roster',
           'Faculty',
           'Catalog courses']}]

# (iso_date, display_date, campus, action, detail, url, contact)
# iso_date "" = undated / monitor-only; sorts last.
DEADLINES = [('2026-08-20',
  'Aug 20, 2026',
  'ASU / CU Boulder',
  'Fall classes begin (earliest in the dataset)',
  '',
  'https://registrar.asu.edu/academic-calendar',
  ''),
 ('',
  'Monitor',
  'U of Arizona',
  'ASUA Vendor Fair — ⚠ PAGE IS STALE, NOT A DEADLINE',
  "Re-verified Aug 11: the page still shows the 2025–26 cycle. The 'Aug 16' deadline is a 2025 leftover (Aug 16, "
  '2026 is a Sunday). Fees confirmed current: $500/event, $800/year for-profit. Call to ask when Fall 2026 dates '
  'post — phone, do not email.',
  'https://www.asuatoday.arizona.edu/vendor-fair',
  'asua-vendorfair@arizona.edu · 520-621-2782')]
