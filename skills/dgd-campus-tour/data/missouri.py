"""Missouri — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published at time of research — a gap to close by phone, not a finding of absence.
Schema: reference/data-schema.md

STATEWIDE LEGAL CONTEXT — read before any ambassador cites a statute:
RSMo s 173.1550, the "Campus Free Expression Act," effective 28 August 2015 (L. 2015 S.B. 93),
deems "The outdoor areas of campuses of public institutions of higher education in this state...
traditional public forums" and creates a private right of action (AG or aggrieved person; not less
than $500 for the initial violation plus $50 for each day it continues; one-year limitation with
each day a new accrual). BUT s 173.1550(3) reads: "Any person who wishes to engage in NONCOMMERCIAL
expressive activity on campus shall be permitted to do so freely." DGD's tabling is commercial.
The statute is a tool for STUDENT ALLIES and a bar on banishing outdoor speech — it is NOT a right
to table and it defeats no fee or approval requirement in this file. It binds Mizzou, Missouri S&T,
UMKC, UMSL, Missouri State, Truman State and SEMO. It does NOT reach WashU or SLU, both private.
https://revisor.mo.gov/main/OneSection.aspx?section=173.1550

SYSTEMWIDE LAYER — UM System Collected Rules and Regulations 110.010 governs FOUR campuses at once
(Columbia, Kansas City, St. Louis, Rolla). Full quotes live in Mizzou's policy_key below. Short
version: outside entities are NOT banned; they need Chancellor-level WRITTEN approval and pay a
Chancellor-approved fee, with a ten-day floor when an RSO is the requester. CRR 110.010 itself
contains NO anti-fronting clause — that appears at campus level (Missouri S&T has one; Mizzou does
not). https://www.umsystem.edu/ums/rules/collected_rules/facilities/ch110/110.010_regulations

ALL NINE CAMPUSES ARE ON SEMESTERS. No quarter, trimester or true block school in this set. Truman
runs block courses inside the semester (first block ends Oct 6) and SEMO runs concurrent eight-week
sessions; neither reshapes the tour the way a quarter calendar would. Missouri splits into two start
waves one week apart: Missouri State and Truman Aug 17, SLU Aug 19, and Mizzou / WashU / S&T / UMSL /
SEMO Aug 24. UMKC unknown.

RESEARCH-TOOLING FINDINGS THAT ARE THEMSELVES DATA: every general search engine tested (Google, Bing,
DuckDuckGo, Mojeek) is ROBOTS-BLOCKED to research tooling, and direct curl is egress-blocked, so all
retrieval was by direct URL. SIX OF NINE org directories are JavaScript-rendered and could not be
enumerated. NO blockchain club was confirmed anywhere in Missouri — and none was ruled out either.
NO faculty member working on blockchain, crypto, digital assets or fintech was confirmed at ANY of the
nine campuses. That is the largest hole in this packet, because the academic door is the cheapest
route past every commercial rule below.
"""

STATE = 'Missouri'

CAMPUSES = [

 # ---------------------------------------------------------------- 1. MIZZOU
 {'state': 'Missouri',
  'name': 'University of Missouri–Columbia',
  'city': 'Columbia, MO',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 5,
  'start': 'Mon Aug 24, 2026',
  'adddrop': '⚠ NOT PRINTED on the 2026-2027 registrar calendar PDF. Last day any student may enroll is not '
             'given either. Call the Registrar or Get Involved, (573) 882-3780.',
  'fallbreak': '⚠ NONE — Mizzou has NO fall break in the 2026-27 calendar. Full density Aug 24 straight through '
               'Nov 21: THIRTEEN UNINTERRUPTED WEEKS, the best sustained access window in Missouri.',
  'thanksgiving': 'Thanksgiving recess begins at close of day Sat Nov 21, 2026; classwork resumes 8:00 a.m. '
                  'Mon Nov 30, 2026.',
  'lastclass': 'Classwork ends at close of day Thu Dec 10, 2026. Reading day Fri Dec 11.',
  'finals': 'Mon Dec 14 – Fri Dec 18, 2026. Commencement Dec 18, 19 and 20.',
  'cal_url': 'https://registrar.missouri.edu/wp-content/uploads/2024/12/2026-2027-Academic-Calendar-.pdf',
  'cal_status': 'CONFIRMED on the Registrar\'s published 2026-2027 Academic Calendar PDF. ⚠ CALENDAR CONFLICT: the '
                'registrar ALSO posted "2026-2027-Academic-Calendar-Revised-to-exclude-Reading-Day-1.docx" — two '
                'versions of the same calendar disagree about whether Fri Dec 11 is a reading day. Immaterial for '
                'tabling; confirm if a December stop is planned. Index: '
                'https://registrar.missouri.edu/academic-calendar/',
  'fair': 'Involvement Week — the "Get Involved Fair" (600+ student organizations)',
  'fair_date': '⚠ Aug 31, 11 a.m. – 2 p.m., Kuhlman Court, inside Involvement Week Aug 30 – Sept 5. NO YEAR IS '
               'PRINTED ANYWHERE ON THE PAGE (footer says "© 2026"). RESOLVED BY WEEKDAY: if 2025, the fair falls '
               'on a SUNDAY and the listed "Sept. 3 | 7 p.m. | Memorial Stadium — Mizzou Football" falls on a '
               'WEDNESDAY; if 2026, the fair is a MONDAY and the game a THURSDAY-night season opener. A Sunday fair '
               'and a Wednesday home game are both implausible. THE PAGE READS AS FALL 2026 — but it is unlabelled, '
               'so confirm at (573) 882-3780. Rest of the week as published: Volunteer Fair "Sept. 1 | 11 a.m. - 2 '
               'p.m. | Lowry Mall"; Meet Columbia Sept 1 5:30–7:30 p.m.; Power the Roar Pep Rally "Sept. 2 | '
               '7:30-9:30 p.m. | Traditions Plaza"; Part-Time Job Fair "Sept. 3 | 10 a.m. – 1 p.m. | Lowry Mall"; '
               'Fall Fest "Sept. 4 | 4 - 8 p.m."',
  'fair_outside': '⚠ NOT STATED — and the fair itself is a student-org fair. The one slot on the week that admits '
                  'outside entities by its own description is the VOLUNTEER FAIR, Sept 1, 11 a.m.–2 p.m., Lowry '
                  'Mall — "Connect with local organizations" — but that is a volunteering/nonprofit framing and a '
                  'for-profit crypto project is a poor fit for it. No cost, no deadline and no eligibility rule are '
                  'published for either. THE REAL ANSWER AT MIZZOU IS NOT THE FAIR: it is BPPM 6:053, which says '
                  'outright "Non-University Groups will be allowed to request a reservation to sell on campus," and '
                  'the $600 for-profit career-fair tier.',
  'fair_cost': 'Fair itself: not published. THE PUBLISHED FOR-PROFIT RATE IN MISSOURI is the career fair — $600 '
               'for-profit ($630 with the 5% credit-card fee); $250 non-profit/Mizzou-affiliated ($262.50) at the '
               'Mizzou Fall 2026 BUSINESS & ACCOUNTANCY Career Fair, Thu Sep 17, 2026, 10 a.m.–3 p.m., MizzouRec. '
               '⚠ The VENDOR TABLE rate under BPPM 6:053 is NOT PUBLISHED ANYWHERE — biggest money gap at Mizzou.',
  'fair_deadline': 'Fair: none published. Vendor reservation: "Reservations must be requested not later than '
                   'fifteen (15) business days in advance of the date requested," and the Facilities Use Agreement '
                   'plus full payment are due "not less than one week prior." Career fair: registration is open via '
                   'Handshake, NO DEADLINE PUBLISHED — call (573) 882-2565.',
  'fair_url': 'https://getinvolved.missouri.edu/involvement-week/',
  'policy': 'MU Business Policy and Procedure Manual 6:053, "Sales, Solicitations, Collections & Advertising" '
            '(revised 08/22/2017; 09/30/2022; 7/17/2025) — the operative campus document; above it, UM System '
            'Collected Rules and Regulations 110.010; alongside it, Missouri Student Unions Non-University '
            'Reservations and the Use of Outdoor Spaces guidance',
  'policy_url': 'https://bppm.missouri.edu/policy/sales-solicitations-collections-advertising/',
  'policy_key': "MU BPPM 6:053 'Sales, Solicitations, Collections & Advertising' (revised 7/17/2025, "
                "bppm.missouri.edu/policy/sales-solicitations-collections-advertising/): 'All sales, solicitations, "
                "and collections in University buildings or on University grounds... are prohibited without prior "
                "authorization' and 'THE UNIVERSITY SHALL NOT BE USED FOR COMMERCIAL OR PROMOTIONAL ADVERTISING "
                "PURPOSES.' BUT — and this is the sentence that makes Mizzou the most open campus in Missouri — "
                "'NON-UNIVERSITY GROUPS WILL BE ALLOWED TO REQUEST A RESERVATION TO SELL ON CAMPUS.' The route is "
                "priced in time rather than dollars: 'limited to conducting Sales or Solicitation activities for a "
                "MAXIMUM OF FIVE (5) DAYS DURING THE FALL SEMESTER, five (5) days during the spring semester'; "
                "'Reservations must be requested NOT LATER THAN FIFTEEN (15) BUSINESS DAYS IN ADVANCE of the date "
                "requested'; a maximum of THREE VENDOR RESERVATIONS PER DAY at approved locations, 10 a.m.–2 p.m. "
                "CST; applications are denied if inconsistent with the university mission or with existing "
                "contracts; gross sales above $5,000 require Vice Chancellor for Finance approval. RSOs separately "
                "'must get approval from the Division of Student Affairs' and follow BPPM 1:090, under which "
                "'fund-raising' means ANY income-producing activity, INCLUDING DONATIONS. ⚠ THE PRODUCT APPROVAL "
                "FORM IS THE REAL GATE (unions.missouri.edu/space-non-university): 'The off-campus vendor must fill "
                "out the University approved Facilities Use Agreement, and fulfill all requirements contained "
                "therein in its entirety,' and 'VENDORS MUST ALSO FILL OUT A PRODUCT APPROVAL FORM LISTING A "
                "DETAILED DESCRIPTION OF PRODUCTS AND/OR SERVICES THEY INTEND TO OFFER.' For a crypto project that "
                "form decides everything — fill it in honestly and early. MONEY TERMS: 'All reservations are "
                "tentative until approved. The Facilities Use Agreement and all other appropriate forms must be "
                "completed and returned WITH FULL PAYMENT NOT LESS THAN ONE WEEK PRIOR to the scheduled reservation "
                "date'; 'The reservation will be considered NULL AND VOID if no contract or payment or an "
                "incomplete contract is received after this deadline.' OUTDOORS (unions.missouri.edu/space-outdoor): "
                "'All outdoor spaces are traditional public forums subject to reasonable time, place, and manner "
                "regulations' — but activities may not 'INVOLVE SOLICITATIONS OR PROMOTION OF COMMERCIAL "
                "ENTERPRISES,' and the distribution permission is expressly limited: 'NON-COMMERCIAL pamphlets, "
                "handbills, circulars, newspapers, magazines and other written materials may be distributed on a "
                "person-to-person basis in open areas outside of buildings.' Kuhlman Court 'may be reserved and in "
                "which spontaneous events or activities may occur in the absence of a prior reservation' — "
                "reservable by 'officially recognized MU student organizations.' ⚠ SYSTEMWIDE LAYER — UM SYSTEM CRR "
                "110.010 (amended 11-18-21, 12-10-21, 6-29-23; umsystem.edu/ums/rules/collected_rules/facilities/"
                "ch110/110.010_regulations) GOVERNS MIZZOU, UMKC, UMSL AND MISSOURI S&T AT ONCE: 110.010.G.1 'THE "
                "SALE OF ANYTHING, THE SOLICITING OF SUBSCRIPTIONS OR THE COLLECTION OF DUES IS PROHIBITED... "
                "WITHOUT PRIOR AUTHORIZATION OF THE CHANCELLOR'; G.2 'Recognized student organizations may not "
                "solicit subscriptions or collect dues from prospective students or guests'; E.4 'Use of available "
                "University facilities may be granted to nonstudent groups for meetings, programs and activities' "
                "when (a) 'sponsored by or the group is invited by an instructional or administrative division,' "
                "(b) 'sponsored by a learned, educational, professional, or scientific society... when recommended "
                "by a dean,' or (c) 'OTHER NONAFFILIATED AND NONSPONSORED GROUPS MAY MAKE USE OF THE FACILITIES... "
                "UPON WRITTEN APPROVAL OF THE CHANCELLOR'; E.3 'Persons who are not current students or employees... "
                "without specific permission or authorization or without an appropriate purpose MAY BE DEEMED "
                "GUILTY OF TRESPASS'; D.2 'The organization file a written request for approval of the activity or "
                "program AT LEAST TEN DAYS PRIOR to the event' (Chancellor may except); E.6 'Nonaffiliated, "
                "nonsponsored groups... WILL BE CHARGED A FEE APPROVED BY THE CHANCELLOR.' ⚠ NOTABLE ABSENCES AT "
                "MIZZOU — verified-not-found, NOT verified-permitted: NO anti-fronting clause; NO clause barring an "
                "RSO from sponsoring an outside group; NO insurance requirement or dollar limit; NO deposit and NO "
                "cancellation schedule; NO language reaching credit cards, payment apps or on-site contracts; and "
                "NO DOLLAR RATE for a vendor table anywhere on any page. Get the rate at (573) 884-8793. ⚠ STATE "
                "NOTE — RSMo s 173.1550, the CAMPUS FREE EXPRESSION ACT, effective 28 Aug 2015 (S.B. 93): s 2 'The "
                "outdoor areas of campuses of public institutions of higher education in this state shall be deemed "
                "traditional public forums,' restrictions must 'employ clear, published, content, and "
                "viewpoint-neutral criteria, and provide for ample alternative means of expression'; s 5–6 create a "
                "private right of action for the attorney general or 'Persons whose expressive rights were "
                "violated,' with 'no less than five hundred dollars for the initial violation, plus fifty dollars "
                "for each day the violation remains ongoing'; s 7 makes each day a new accrual inside a one-year "
                "limitation. BUT s 3 PROTECTS ONLY 'NONCOMMERCIAL EXPRESSIVE ACTIVITY.' DGD IS COMMERCIAL. THE "
                "STATUTE IS A TOOL FOR STUDENT ALLIES, NOT A RIGHT TO TABLE, and it defeats none of the fees or "
                "approvals in this packet. It binds Mizzou, S&T, UMKC, UMSL, Missouri State, Truman and SEMO; it "
                "DOES NOT REACH WASHU OR SLU, both private. https://revisor.mo.gov/main/OneSection.aspx?"
                "section=173.1550",
  'sponsor_required': 'NO — Mizzou is one of the few campuses anywhere with a direct, published route for an '
                      'outside for-profit entity, and no rule was found barring an RSO from sponsoring one either. '
                      'BPPM 6:053: "Non-University Groups will be allowed to request a reservation to sell on '
                      'campus" (five days per semester, 15 business days ahead, three vendors a day, 10 a.m.–2 '
                      'p.m.). Above it CRR 110.010.E.4.c still requires "written approval of the Chancellor" for a '
                      'nonaffiliated, nonsponsored group and a "fee approved by the Chancellor" — so in practice '
                      'the campus process (Reservations & Events plus Finance & Business Services) IS the '
                      'Chancellor\'s delegated approval. Confirm that reading at (573) 882-2094 before relying on '
                      'it. No anti-fronting clause was found; absence of published text is not permission.',
  'clubs': [('⚠ NO BLOCKCHAIN / CRYPTO / BITCOIN / WEB3 ORGANIZATION FOUND AT MIZZOU',
             'Not confirmed present on any retrievable page — and NOT ruled out. The full MU Engage directory '
             '(engage.missouri.edu/club_signup?view=all) RETURNED HTTP 504 THROUGH THE PROXY and could not be '
             'enumerated at all. Absence is probable, not proven. Ask Get Involved directly, (573) 882-3780.',
             'https://engage.missouri.edu/club_signup?view=all'),
            ('⚠ Financial Management Association (FMA)',
             'Confirmed on the Trulaske College of Business student-organizations page. Faculty advisor DAVE '
             'JOHNSON — advisors are staff and stable, unlike student officers. NOTE: the Trulaske page publishes '
             'ADVISOR NAMES ONLY — no emails and no phone numbers for any club. Do not invent officer names; '
             'Trulaske publishes none and rosters rotate annually.',
             'https://business.missouri.edu/student-organization'),
            ('⚠ University of Missouri Investment Group',
             'SAME ADVISOR AS FMA — Dave Johnson. One approach reaches both the FMA chapter and the investment '
             'group, the two highest-fit audiences at Mizzou.',
             'https://business.missouri.edu/student-development/learning-doing/university-missouri-investment-group'),
            ('Association of Accountancy Students', 'Advisor Kari Gingrich.',
             'https://business.missouri.edu/student-organization'),
            ('National Association of Black Accountants (NABA)', 'Advisors Hayley Harned / Sijie Yao.',
             'https://business.missouri.edu/student-organization'),
            ('University of Missouri Insurance Association', 'Advisor Dave Fischer.',
             'https://business.missouri.edu/student-organization'),
            ('Other Trulaske organizations (listed, lower fit)',
             'Beta Alpha Psi; Trulaske Consulting Association; Collegiate DECA; Collegiate Future Business Leaders '
             'of America; Delta Sigma Pi; Alpha Kappa Psi; Mizzou Marketing Club; Pi Sigma Epsilon; Society for '
             'Human Resource Management; Student Center for the Public Trust; Association of Trulaske '
             'Businesswomen; Black Business Students Association; Association of Latino Professionals for America; '
             'Global Professionals; Health Sales Club; Diverse Student Organization; Business Week; Trulaske Study '
             'Abroad; Trulaske Student Council (STUCO); Alumni Mentor Program. No advisor listed for most; no '
             'emails or phones published for any.',
             'https://business.missouri.edu/student-organization')],
  'faculty': [('⚠ MU Reservations & Events — main line, S4 Memorial Union',
               'BOOKS THE NON-UNIVERSITY VENDOR RESERVATION UNDER BPPM 6:053. THE SINGLE MOST IMPORTANT NUMBER IN '
               'MISSOURI FOR THIS TOUR. Ask for the vendor table RATE (published nowhere), the Facilities Use '
               'Agreement and the PRODUCT APPROVAL FORM. Kate Fleming is the Director and sits on this same line.',
               'Reservations & Events',
               'reservations@missouri.edu · (573) 884-8793 (main line; also Director Kate Fleming, '
               'flemingkat@missouri.edu)',
               'https://reservations.missouri.edu/contact-us/'),
              ('Sam Cohen',
               'Reservations & Events Coordinator — one of the two people who actually books a table. Direct line.',
               'Reservations & Events', 'stcxc5@missouri.edu · (573) 882-0960',
               'https://reservations.missouri.edu/contact-us/'),
              ('Lauren Northern',
               'Reservations & Events Coordinator — the other booking coordinator. Direct line.',
               'Reservations & Events', 'lmtgw5@missouri.edu · (573) 884-8818',
               'https://reservations.missouri.edu/contact-us/'),
              ('Rachel Allen', 'Senior Event Support Specialist — event-day logistics.', 'Reservations & Events',
               'rallen@missouri.edu · (573) 884-1504', 'https://reservations.missouri.edu/contact-us/'),
              ('John Cattanach', 'Associate Director – Theaters. Venue escalation.', 'Reservations & Events',
               'cattanachj@missouri.edu · (573) 882-5998', 'https://reservations.missouri.edu/contact-us/'),
              ('Emily Stoker', 'Senior Event Coordinator and Student Development Specialist — the bridge between '
               'event booking and student programming.', 'Reservations & Events',
               'stokere@missouri.edu · (573) 882-2155', 'https://reservations.missouri.edu/contact-us/'),
              ('Josh Ramsey', 'EMS Reservation Software Project Coordinator and System Admin — runs the booking '
               'system itself.', 'Reservations & Events', '(573) 882-8935',
               'https://reservations.missouri.edu/contact-us/'),
              ('⚠ Division of Finance & Business Services (311 Jesse Hall)',
               'AUTHORIZES SALES AND SOLICITATION UNDER BPPM 6:053 — the office that says yes or no to a commercial '
               'reservation, and the number printed on the policy itself. Also the office to ask whether the campus '
               'process satisfies CRR 110.010\'s "written approval of the Chancellor."',
               'Finance & Business Services', '(573) 882-2094',
               'https://bppm.missouri.edu/policy/sales-solicitations-collections-advertising/'),
              ('MU Joint Office of Strategic Communications and Marketing',
               'The advertising contact printed on BPPM 6:053 — relevant to "The University shall not be used for '
               'commercial or promotional advertising purposes."',
               'Strategic Communications', '(573) 882-4523',
               'https://bppm.missouri.edu/policy/sales-solicitations-collections-advertising/'),
              ('Missouri Student Unions — administrative office (G210 MU Student Center, 911 E. Rollins St.)',
               'Second number printed on the Non-University Reservations page. NO INDIVIDUAL STAFF NAMES OR TITLES '
               'ARE PUBLISHED on the Unions contact page — department-level only.',
               'Missouri Student Unions', 'unions@missouri.edu · (573) 882-6310',
               'https://unions.missouri.edu/contact-info'),
              ('MU Student Center Information Desk', 'Building operations.', 'Missouri Student Unions',
               '(573) 882-1174', 'https://unions.missouri.edu/contact-info'),
              ('⚠ Get Involved / Student Activities & Engagement (2500 MU Student Center)',
               'OWNS THE INVOLVEMENT FAIR — and is the office that can settle whether the Involvement Week page is '
               'Fall 2025 or Fall 2026, since the page prints no year. Call this before booking travel.',
               'Student Affairs', 'engagement@missouri.edu · (573) 882-3780',
               'https://getinvolved.missouri.edu/events/'),
              ('Division of Student Affairs (2202 MU Student Center)',
               'Approves RSO sales and solicitation under BPPM 6:053 — the club-side gate.',
               'Student Affairs', 'studentaffairs@missouri.edu · (573) 882-0157',
               'https://studentaffairs.missouri.edu/contact-us/'),
              ('Dr. Michelle Froese', 'Dean of Students, 2202 MU Student Center — escalation above Student Affairs.',
               'Dean of Students', 'mudosdeanofstudents@missouri.edu · (573) 882-5397',
               'https://deanofstudents.missouri.edu/meet-the-dean'),
              ('⚠ Business Career Services (111 Cornell Hall)',
               'SELLS THE $600 FOR-PROFIT SLOT AT THE SEP 17 BUSINESS & ACCOUNTANCY CAREER FAIR — the only '
               'published for-profit rate in Missouri. Ask for the registration deadline; none is published.',
               'Trulaske College of Business', 'bcs@missouri.edu · (573) 882-2565',
               'https://business.missouri.edu/student-development/career-preparedness/business-career-services/career-fairs'),
              ('MU Career Center (201 Student Success Center)',
               'The other four confirmed Fall 2026 career fairs (Engineering Sep 10; Textile & Apparel Sep 16; '
               'CAFNR/Arts & Science Sep 30; Health & Wellness Sep 30). Drop-in hours Mon–Fri 9 a.m.–4 p.m.',
               'Career Services', 'career@missouri.edu · (573) 882-6801',
               'https://career.missouri.edu/jobs-and-internships/career-fairs/'),
              ('Campus Facilities', 'Tent stakes and utilities/irrigation clearance — required at least 3 working '
               'days before an outdoor event that stakes anything into the ground.',
               'Campus Facilities', '(573) 882-3094', 'https://unions.missouri.edu/space-outdoor'),
              ('Sound amplification approval (304 Jesse Hall)',
               'Amplified sound on outdoor space requires approval from this office.',
               'Campus Facilities', '(573) 882-7255', 'https://unions.missouri.edu/space-outdoor'),
              ('David Johnson',
               '⚠ FMA AND INVESTMENT GROUP FACULTY ADVISOR — one person reaches both clubs. Associate Teaching '
               'Professor of Finance, 339 Cornell Hall, 700 Tiger Avenue. ⚠ HIS PUBLISHED EXPERTISE IS REVERSE '
               'MORTGAGES AND FINANCIAL PLANNING, NOT DIGITAL ASSETS — do not represent him as a crypto '
               'researcher. HIS FACULTY PAGE PUBLISHES NO EMAIL AND NO PHONE.',
               'Trulaske College of Business — Finance',
               'no email or number published — look up here; reach via Trulaske',
               'https://business.missouri.edu/departments-faculty/people-directory/david-johnson'),
              ('(Blockchain / digital-assets faculty)',
               'NOT CONFIRMED — no Mizzou faculty member working on blockchain, cryptocurrency, digital assets, '
               'fintech or payments could be confirmed on any live page. The finance course-offerings URL '
               '(catalog.missouri.edu/courseofferings/finance/) 404s. Look up in the Trulaske faculty directory '
               'and the EECS directory.',
               'Trulaske College of Business / EECS',
               'no number published — look up here',
               'https://business.missouri.edu/directory?employee=faculty')],
  'courses': [('CMP_SC 4460',
               'Introduction to Cryptography — the closest Mizzou catalog course to the subject. Verbatim: '
               '"Cryptography is an important technique used to achieve security goals in an untrusted and possibly '
               'adversarial environment." Covers standard cryptographic algorithms and their correct use; NO '
               'mention of blockchain, distributed ledgers or digital currency. FALL 2026 OFFERING UNVERIFIED.',
               'https://catalog.missouri.edu/courseofferings/cmp_sc/'),
              ('(Blockchain / crypto / fintech)',
               '⚠ NONE FOUND. No blockchain, cryptocurrency or distributed-ledger course appears in the Computer '
               'Science course offerings. The Finance course list could not be checked — '
               'catalog.missouri.edu/courseofferings/finance/ returns 404. Gap.',
               'https://catalog.missouri.edu/')],
  'events': [('⚠⚠ Mizzou Fall 2026 BUSINESS & ACCOUNTANCY Career Fair',
              'Thu Sep 17, 2026, 10 a.m. – 3 p.m., MizzouRec. FOR-PROFIT $600 ($630 with the 5% credit-card fee); '
              'non-profit / Mizzou-affiliated $250 ($262.50). Registration via Handshake; NO DEADLINE PUBLISHED. '
              'Sep 17, 2026 IS a Thursday and the listing is explicitly labelled 2026 — not stale. THE CLEANEST '
              'PAID ROUTE TO MISSOURI STUDENTS THAT EXISTS ANYWHERE IN THE STATE.',
              'https://business.missouri.edu/student-development/career-preparedness/business-career-services/career-fairs'),
             ('Five confirmed Fall 2026 career fairs (all explicitly labelled 2026)',
              'Sep 10 Mizzou Engineering Career Fair · Sep 16 Textile and Apparel Management · Sep 17 Business & '
              'Accountancy · Sep 30 CAFNR/Arts & Science Career & Internship Expo · Sep 30 Health & Wellness Career '
              'and Graduate Fair. Times, locations and employer costs for the other four are NOT published on the '
              'index — each links through to Handshake. Call (573) 882-6801.',
              'https://career.missouri.edu/jobs-and-internships/career-fairs/'),
             ('⚠ TigerHacks — the sponsorship pipeline',
              'Mizzou\'s largest hackathon, Lafferre Hall, run by the College of Engineering. ⚠ THE LIVE SITE SHOWS '
              'NOV 7–9, 2025 (48 hours) — the "Major League Hacking 2026 Hackathon Season" badge is an MLH season '
              'label spanning 2025-26, NOT a 2026 date. FALL 2026 DATES NOT PUBLISHED; pattern is one weekend in '
              'early November. ⚠ THE SPONSORSHIP PROSPECTUS IS THE 2024 EDITION — a year and a half stale, treat '
              'amounts as indicative: Seed (Bronze) $1,700 — website/marketing/social logo, snack or meal '
              'sponsorship, project judging, NO dedicated table; Sprout (Silver) $3,000 — adds t-shirt logo, '
              '"Career Fair Participant," mentors/company reps on site, early participant data; Sapling (Gold) '
              '$5,000 — adds hosting a workshop, a custom prize category, "Present at Opening and Closing '
              'Ceremony," "Schedule On-Site Interviews," full participant data after the event. Custom packages '
              'available. 2024 attendance "over 300 students from across the Midwest." Past sponsors: Garmin, '
              'Veterans United, Enterprise Mobility, Shelter Insurance, H&R Block. A private student-run event — '
              'sponsoring it SIDESTEPS BPPM 6:053 entirely. Sponsor decks typically close 6–8 weeks out.',
              'https://tigerhacks.missouri.edu/prospectus.pdf'),
             ('Involvement Week Aug 30 – Sept 5, 2026 (year unlabelled — see fair_date)',
              'Get Involved Fair Aug 31 11–2 Kuhlman Court (600+ orgs); Volunteer Fair Sept 1 11–2 Lowry Mall '
              '("Connect with local organizations"); Meet Columbia Sept 1 5:30–7:30 p.m.; Yoga on Rothwell Lawn and '
              'MGC 101 Sept 2; Power the Roar Pep Rally Sept 2 7:30–9:30 p.m. Traditions Plaza; Gear Up for Game '
              'Day and Part-Time Job Fair Sept 3; Mizzou Football Sept 3 7 p.m. Memorial Stadium; Fall Fest Sept 4 '
              '4–8 p.m. Brewer Courts.',
              'https://getinvolved.missouri.edu/involvement-week/')],
  'play': 'Columbia is the whole trip. Mizzou is the only campus in Missouri that publishes a for-profit price, and '
          'it publishes two independent routes. Route one, and the one to buy first: the Mizzou Fall 2026 BUSINESS '
          '& ACCOUNTANCY Career Fair, Thu Sep 17, 10 a.m.–3 p.m. at MizzouRec — $600 for a for-profit ($630 paying '
          'by card), in front of the Trulaske finance cohort, no sponsorship, no club, no argument. Call Business '
          'Career Services at (573) 882-2565 and get the registration deadline, because none is published. Route '
          'two is BPPM 6:053, which states in terms that "Non-University Groups will be allowed to request a '
          'reservation to sell on campus" — five days a semester, three vendors a day, 10 a.m.–2 p.m., requested '
          'fifteen business days ahead, with the Facilities Use Agreement and FULL PAYMENT due a week before or the '
          'reservation is "null and void." The table rate is published NOWHERE; call MU Reservations & Events at '
          '(573) 884-8793 (ask for Sam Cohen or Lauren Northern) and expect to fill out a PRODUCT APPROVAL FORM '
          '"listing a detailed description of products and/or services they intend to offer" — for a crypto project '
          'that form is the whole decision, so answer it plainly rather than cleverly. Time the visit to the '
          'calendar: MIZZOU HAS NO FALL BREAK, thirteen uninterrupted weeks Aug 24 – Nov 21, the best sustained '
          'window in the state, and the last useful day is around Dec 8. ⚠ TIME-CRITICAL AND ALREADY PAST: the Get '
          'Involved Fair is listed for Aug 31, 11 a.m.–2 p.m. at Kuhlman Court — nineteen days ago if the page is '
          '2025, nineteen days FROM NOW if it is 2026, and THE PAGE PRINTS NO YEAR. Weekday analysis says 2026 (a '
          '2025 reading puts the fair on a Sunday and the listed home football game on a Wednesday), but call '
          '(573) 882-3780 this week and settle it. Do not chase a blockchain club here — none was found, though the '
          'MU Engage directory returned HTTP 504 and could not be enumerated, so that is probable rather than '
          'proven; the real audience is the Financial Management Association and the University of Missouri '
          'Investment Group, which share one faculty advisor, Dave Johnson, whose page publishes neither email nor '
          'phone. And keep TigerHacks warm: an early-November student-run hackathon with published sponsor tiers '
          '($1,700 / $3,000 / $5,000 in the 2024 deck) that sidesteps the solicitation policy completely — email '
          'muengrtigerhacks@umsystem.edu now, because decks close six to eight weeks out and the Fall 2026 date is '
          'not yet posted.',
  'gaps': ['⚠⚠ THE VENDOR TABLE RATE. BPPM 6:053 grants the right to request a selling reservation but NO DOLLAR '
           'FIGURE appears on any Mizzou page — not on the outdoor info-tables page, not on the indoor info-tables '
           'page, not on the non-university reservations page. (573) 884-8793 or (573) 882-2094. '
           'https://reservations.missouri.edu/event-spaces/outdoor-info-tables-1-3-rollins-4-6-kuhlman/',
           '⚠ WHICH YEAR THE INVOLVEMENT WEEK PAGE DESCRIBES. No year is printed; the footer says "© 2026"; weekday '
           'analysis points to Fall 2026 (Aug 31 = Monday, Sep 3 = Thursday) rather than 2025 (Sunday / Wednesday). '
           'Confirm at (573) 882-3780. https://getinvolved.missouri.edu/involvement-week/',
           '⚠ Whether an outside for-profit may table AT the Get Involved Fair or the Volunteer Fair — no '
           'eligibility rule, cost or deadline is published for either. (573) 882-3780.',
           '⚠ Whether the campus process (Reservations & Events + Finance & Business Services) satisfies CRR '
           '110.010.E.4.c\'s requirement of "written approval of the Chancellor" for a nonaffiliated, nonsponsored '
           'group, and what the "fee approved by the Chancellor" actually is. (573) 882-2094.',
           'Career fair registration deadlines — NONE published for any of the five Fall 2026 fairs. '
           '(573) 882-2565 for Business & Accountancy, (573) 882-6801 for the rest.',
           'TigerHacks Fall 2026 dates and current tier pricing — the live site still shows Nov 7–9, 2025 and the '
           'prospectus is the 2024 edition. muengrtigerhacks@umsystem.edu. https://tigerhacks.missouri.edu/',
           '⚠ The MU Engage club directory could not be enumerated — engage.missouri.edu/club_signup?view=all '
           'RETURNED HTTP 504 THROUGH THE PROXY. Whether any blockchain/crypto organization exists outside Trulaske '
           'is unconfirmed. (573) 882-3780.',
           'No blockchain/crypto/fintech FACULTY member could be confirmed at Mizzou, and no club email or phone is '
           'published for any Trulaske organization (advisor names only). '
           'https://business.missouri.edu/student-organization',
           'Add/drop deadlines are not printed on the 2026-2027 registrar calendar PDF, and two versions of that '
           'calendar exist (one "Revised to exclude Reading Day"). https://registrar.missouri.edu/academic-calendar/',
           'The Finance course list is unreachable — catalog.missouri.edu/courseofferings/finance/ returns 404. Any '
           'fintech or digital-assets course at Trulaske is unconfirmed.'],
  'note': 'CRR 110.010 is the systemwide rule and it governs Mizzou, UMKC, UMSL and Missouri S&T simultaneously — '
          'its full text is quoted in this campus\'s policy_key and is not repeated on the other three records. '
          'Each of those campuses layers a different procedure on top, and the four are materially different: '
          'Mizzou publishes a real vendor route, S&T publishes a financial-services vendor BAN, UMSL publishes '
          'free-speech guidelines that point straight back at 110.010, and UMKC publishes nothing retrievable at '
          'all. Chapter 110 also contains 110.020 Service and Use Fees — the likely home of any published rate '
          'card, not retrieved, and worth asking for by number. '
          'https://www.umsystem.edu/ums/rules/collected_rules/facilities/ch110'},

 # ---------------------------------------------------------------- 2. WASHU
 {'state': 'Missouri',
  'name': 'Washington University in St. Louis',
  'city': 'St. Louis, MO',
  'type': 'Private',
  'tier': 'A — Named target',
  'access': 2,
  'start': 'Mon Aug 24, 2026',
  'adddrop': '⚠ NOT PRINTED on the bulletin academic calendar for Fall 2026. Call Event Management or the '
             'registrar; the bulletin gives only term boundaries and breaks.',
  'fallbreak': 'Sat–Tue Oct 3–6, 2026 — the only genuine mid-semester fall break among the three St. Louis '
               'campuses, and it does not overlap the Oct 8–12 cluster the rest of the state takes.',
  'thanksgiving': 'Wed Nov 25 – Sun Nov 29, 2026',
  'lastclass': 'Mon Dec 7, 2026. Reading days Tue–Wed Dec 8–9.',
  'finals': 'Thu Dec 10 – Wed Dec 16, 2026. (Commencement for the Class of 2027 is May 21, 2027 — no December '
            'ceremony on the calendar.)',
  'cal_url': 'https://bulletin.wustl.edu/washu/calendar/',
  'cal_status': 'CONFIRMED on the WashU Bulletin 2026-27 academic calendar, which labels the term "Fall Semester '
                '2026" and dates every entry with a weekday. PDF: https://bulletin.wustl.edu/washu/calendar/'
                'calendar.pdf. SEMESTERS.',
  'fair': 'The annual Activities Fair (spelled "Activates Fair" on the Campus Life page — typo in the original)',
  'fair_date': '⚠ UNVERIFIED — Campus Life refers to "the annual Activates Fair" as a way to explore involvement '
               'but PUBLISHES NO DATE, TIME, LOCATION, ELIGIBILITY RULE OR COST anywhere. Confirmed First Week '
               'events only, all dated 2026 on the Campus Life homepage: "Aug24 First Week: Carnival 6:00 PM"; '
               '"Aug25 First Week: Customize your Crib 6:00 PM"; "Aug26 First Week: Pantry Bingo 6:00 PM". Will '
               'post at campuslife.washu.edu — call (314) 935-3443.',
  'fair_outside': '⚠⚠ NO — and not because of the fair. WashU bars external organizations from reserving ANY space '
                  'during the entire academic year: "External individuals and organizations not affiliated with the '
                  'university are NOT PERMITTED TO RESERVE UNIVERSITY SPACE during the academic year from August '
                  '1-May 31." DUC tabling is restricted to "university recognized student organizations and '
                  'departments." The only door is co-sponsorship.',
  'fair_cost': '⚠ NOT PUBLISHED — AND THE RATES PAGE IS AN IMAGE. eventmanagement.wustl.edu/rates names three tiers '
               '(Premier Level Spaces, Standard Level Spaces, Pooled Classrooms) and carries NO machine-readable '
               'dollar amounts at all. A sponsored academic-year external event pays "50% of the \'Non-University / '
               'External Events\' listed on the rates page" — 50% of a number nobody can read. Get the card by '
               'phone: (314) 935-3443.',
  'fair_deadline': 'General reservations "no less than two weeks prior"; DUC tables, DUC/Oak Walk banners and South '
                   '40 underpass panels "no less than five days prior"; changes "no less than three (3) business '
                   'days prior." EXTERNAL inquiries: "a minimum of 30 days in advance."',
  'fair_url': 'https://campuslife.washu.edu/get-involved',
  'policy': 'Danforth Campus Facilities Access Policy (last updated November 7, 2024) — the operative document; '
            'plus the Solicitation and Distribution Policy (Human Resources, updated January 2024) and the External '
            'Events page from Event Management',
  'policy_url': 'https://washu.edu/policies/danforth-campus-facilities-access-policy/',
  'policy_key': "Danforth Campus Facilities Access Policy, last updated 7 November 2024 (washu.edu/policies/"
                "danforth-campus-facilities-access-policy/): ⚠⚠ THE DECISIVE CLAUSE — 'Except as otherwise "
                "described herein, EXTERNAL INDIVIDUALS AND ORGANIZATIONS NOT AFFILIATED WITH THE UNIVERSITY ARE "
                "NOT PERMITTED TO RESERVE UNIVERSITY SPACE DURING THE ACADEMIC YEAR FROM AUGUST 1-MAY 31.' That "
                "window is the entire tour. The mirror image: 'External individuals and organizations not "
                "affiliated with the university MAY RESERVE CERTAIN SPACES DURING THE SUMMER MONTHS OF JUNE AND "
                "JULY and do not require sponsorship.' ⚠ WASHU STATES ITS OWN STATUS — DO NOT ARGUE PUBLIC-FORUM "
                "DOCTRINE OR RSMo s 173.1550 HERE, NEITHER APPLIES: 'THE UNIVERSITY IS A PRIVATE INSTITUTION AND "
                "RETAINS THE ABILITY TO PROHIBIT OR DENY USE OF ITS FACILITIES OR SPACES FOR ANY REASON AT THE SOLE "
                "DISCRETION OF THE UNIVERSITY.' SOLICITATION: 'Solicitation of funds on university property or at "
                "university events by persons not employed by the university or otherwise authorized by the "
                "university is prohibited'; 'Persons not employed or otherwise authorized by the university are "
                "prohibited from soliciting funds or signatures, distributing literature or gifts'; 'Solicitation "
                "of any kind in any university residential facility is prohibited.' ⚠ THE BROADER HR RULE IS "
                "BLUNTER STILL — Solicitation and Distribution Policy, updated January 2024, NO POLICY NUMBER "
                "ASSIGNED ON THE PAGE (hr.wustl.edu/items/solicitation-and-distribution-policy/): 'PERSONS NOT "
                "EMPLOYED OR OTHERWISE AUTHORIZED BY THE UNIVERSITY ARE PROHIBITED FROM SOLICITING FUNDS OR "
                "SIGNATURES, DISTRIBUTING LITERATURE OR GIFTS, OFFERING TO SELL MERCHANDISE OR SERVICES OR ENGAGING "
                "IN ANY OTHER SOLICITATIONS OR SIMILAR ACTIVITY ON UNIVERSITY PROPERTY.' Note 'distributing "
                "literature' — that reaches a flyer, not just a sale. ⚠ SPONSORSHIP DOES CURE IT — THIS IS THE ONE "
                "DOOR: 'Subject to certain restrictions around political activity, IF AN EVENT IS CO-SPONSORED BY A "
                "UNIVERSITY RECOGNIZED STUDENT ORGANIZATION OR DEPARTMENT, THE DEPARTMENT OR STUDENT ORGANIZATION "
                "MAY RESERVE THE SPACE AND INVITE THE EXTERNAL INDIVIDUAL OR ORGANIZATION TO PARTICIPATE.' ⚠ BUT "
                "THE TWO DOCUMENTS DISAGREE ON WHO MAY SPONSOR: Event Management's External Events page "
                "(eventmanagement.wustl.edu/special-events/) says academic-year 'non-university / external events "
                "REQUIRE SPONSORSHIP BY A WASHINGTON UNIVERSITY DEPARTMENT' — department, not student organization, "
                "a stricter reading than the Danforth policy's. ASK WHICH CONTROLS BEFORE SPENDING WEEKS COURTING A "
                "CLUB. Also: 'External inquiries must be placed A MINIMUM OF 30 DAYS IN ADVANCE, and are subject to "
                "availability, staffing, and resources,' and for a sponsored academic-year event the 'rental fee "
                "will be 50% of the \\'Non-University / External Events\\' listed on the rates page.' ⚠ THE RATES "
                "PAGE IS AN IMAGE — three tiers are named (Premier Level Spaces, Standard Level Spaces, Pooled "
                "Classrooms) and NO DOLLAR AMOUNT IS MACHINE-READABLE; 'Venue rates include furniture and some "
                "built-in technology associated with the room' but exclude 'housekeeping, some A/V additions, "
                "additional furniture not associated with the room, decor, parking, or catering.' RESERVATION "
                "TIMING: 'All requests to reserve facilities or campus spaces must be submitted no less than two "
                "weeks prior to the proposed event unless otherwise stated'; DUC tables, DUC/Oak Walk banners and "
                "South 40 underpass panels 'no less than five days prior'; changes 'no less than three (3) business "
                "days prior.' DUC TABLING (eventmanagement.wustl.edu/items/duc-tabling/): reservable only by "
                "'university recognized student organizations and departments'; 'Standard tabling hours are 11:00 "
                "AM to 2:00 PM,' forfeited if unstaffed past 11:15; 'EACH GROUP MAY ONLY TABLE 5 DAYS PER MONTH IN "
                "THE DUC'; no amplified sound; nothing attached to walls, floors or pillars; food must be "
                "pre-packaged, individually wrapped or catered. POSTINGS: 'Anonymous postings advertising events on "
                "or off campus without identification of a sponsoring registered student organization, department "
                "or university student or employee may be removed.' ⚠ ABSENCES — verified-not-found, NOT "
                "verified-permitted: NO anti-fronting clause was found; NO insurance requirement or dollar limit, "
                "NO deposit and NO cancellation schedule appear on any retrieved page; and NOTHING reaching credit "
                "cards, payment apps or signing contracts on site was found anywhere.",
  'sponsor_required': '⚠ YES — AND IT IS THE ONLY ROUTE, but the two governing documents disagree about who may '
                      'sponsor. The Danforth Campus Facilities Access Policy permits co-sponsorship by "a '
                      'university recognized student organization OR department." Event Management\'s External '
                      'Events page says academic-year external events "require sponsorship by a Washington '
                      'University DEPARTMENT." If the stricter reading governs, a student club cannot let DGD in at '
                      'all and only an Olin or CSE department invitation works. RESOLVE THIS ON THE FIRST CALL — '
                      '(314) 935-3443 or Indra Russell (314) 935-8264 — before investing in any club relationship. '
                      'Either way the external party pays 50% of unpublished external rates and must inquire at '
                      'least 30 days ahead.',
  'clubs': [('⚠ NO WASHU CLUB OF ANY KIND COULD BE CONFIRMED',
             'WUGO (Washington University Group Organizer) at wustl.presence.io is JAVASCRIPT-RENDERED — the fetch '
             'returned only page metadata and the title "Involve," with no directory content, no organization '
             'listings and no search results. Not confirmed login-gated, but not machine-readable. DO NOT ASSUME '
             'THERE IS NO BLOCKCHAIN CLUB AT WASHU — assume the directory was unreadable. Ask Campus Life, '
             '(314) 935-3443.',
             'https://wustl.presence.io/organizations')],
  'faculty': [('⚠ Event Management — main line, Danforth University Center Suite 270',
               'THE ONLY NUMBER THAT MATTERS AT WASHU. Controls every space reservation, the external-events '
               'process, DUC tabling and the unpublished rate card. Mon–Fri 8:30 a.m.–5 p.m. This is also the '
               'number Campus Life publishes for itself, so one call reaches both functions.',
               'Event Management',
               '(314) 935-3443 (main line)',
               'https://eventmanagement.wustl.edu/items/duc-tabling/'),
              ('⚠ Indra Russell',
               'EVENT MANAGER — THE NAMED HUMAN FOR EXTERNAL EVENTS, and the person to ask whether the Danforth '
               'policy (student org OR department may sponsor) or the External Events page (department only) '
               'controls. Direct line.',
               'Event Management',
               'irussell@wustl.edu · (314) 935-8264',
               'https://eventmanagement.wustl.edu/special-events/'),
              ('Office of Campus Life (DUC Suite 160, MSC 1068-226-270, 1 Brookings Drive)',
               'Student organizations, WUGO and the unpublished Activities Fair. Mon–Fri 8:30 a.m.–5 p.m. Shares '
               'the Event Management number. NO INDIVIDUAL STAFF NAMES ARE PUBLISHED on any Campus Life page.',
               'Campus Life',
               'campuslife@wustl.edu · (314) 935-3443 (main line)',
               'https://campuslife.washu.edu/get-involved'),
              ('(Olin Business School faculty)',
               '⚠ NOT CONFIRMED — THE OLIN FACULTY DIRECTORY IS JAVASCRIPT-RENDERED. The page presents filter '
               'controls by academic area and faculty type but returns an EMPTY RESULT SET to research tooling. No '
               'WashU faculty member could be confirmed on any topic, blockchain or otherwise. Olin publishes NO '
               'MAIN PHONE NUMBER on the directory page — only website@olin.wustl.edu and the postal address, One '
               'Brookings Drive, St. Louis MO 63130-4899. Look up here in a browser.',
               'Olin Business School',
               'website@olin.wustl.edu · no number published — look up here',
               'https://olin.washu.edu/faculty-and-research/faculty-directory/')],
  'courses': [('(All WashU courses)',
               '⚠ NOT CHECKABLE — THE WASHU BULLETIN COURSE SEARCH IS ROBOTS-BLOCKED. bulletin.wustl.edu/search/'
               '?P=blockchain returned ROBOTS_DISALLOWED to research tooling. No WashU course could be verified for '
               'blockchain, crypto or fintech content in either direction. Gap.',
               'https://bulletin.wustl.edu/')],
  'events': [('First Week 2026',
              'Aug 24 Carnival 6:00 PM; Aug 25 Customize your Crib 6:00 PM; Aug 26 Pantry Bingo 6:00 PM — all '
              'confirmed and dated 2026 on the Campus Life homepage. The Activities Fair is referenced but '
              'undated.',
              'https://campuslife.washu.edu/'),
             ('Hackathon — NONE CONFIRMED',
              'No WashU hackathon could be confirmed. Contrast Mizzou, which has TigerHacks with published sponsor '
              'tiers. Not a finding of absence — search engines were unavailable for this pass.',
              '')],
  'play': 'Skip WashU for tabling and treat it as a one-call reconnaissance stop, not a destination. The written '
          'policy closes the door for the whole tour window in a single sentence: "External individuals and '
          'organizations not affiliated with the university are not permitted to reserve university space during '
          'the academic year from August 1-May 31," and the HR rule separately bars non-employees from "distributing '
          'literature or gifts, offering to sell merchandise or services" anywhere on university property. WashU '
          'also states in terms that it "is a private institution and retains the ability to prohibit or deny use of '
          'its facilities or spaces for any reason at the sole discretion of the university" — so do not bring the '
          'Campus Free Expression Act into the room, it does not reach private schools and citing it will read as '
          'unserious. There is exactly one door and it is academic: co-sponsorship. The Danforth policy says a '
          'recognized student organization OR a department "may reserve the space and invite the external '
          'individual or organization to participate," but Event Management\'s own external-events page says '
          'academic-year external events "require sponsorship by a Washington University DEPARTMENT." Those two '
          'documents disagree, and which one governs decides whether a student club is any use to you at all. Make '
          'that the first question to Indra Russell, Event Manager, (314) 935-8264 — thirty days before you want '
          'anything, because "External inquiries must be placed a minimum of 30 days in advance." Ask for the rate '
          'card on the same call: the published rates page is AN IMAGE with no readable dollar figures, and a '
          'sponsored event pays 50% of a number you currently cannot see. Everything else at WashU is unreadable — '
          'WUGO is JavaScript-rendered so no club could be confirmed, the Olin faculty directory is '
          'JavaScript-rendered and returns nothing, and the course bulletin search is robots-blocked. Budget one '
          'phone call, not one trip. On calendar: Aug 24 start, a Sat–Tue fall break Oct 3–6 that no other Missouri '
          'campus shares, and classes ending Mon Dec 7.',
  'gaps': ['⚠⚠ WHETHER A STUDENT ORGANIZATION CAN SPONSOR AT ALL, or only a department. The Danforth Campus '
           'Facilities Access Policy says "a university recognized student organization or department"; the Event '
           'Management External Events page says "sponsorship by a Washington University department." These '
           'conflict and the answer determines the entire WashU strategy. (314) 935-8264.',
           '⚠⚠ THE EXTERNAL RATE CARD IS AN IMAGE. eventmanagement.wustl.edu/rates names Premier / Standard / '
           'Pooled Classroom tiers with NO machine-readable dollar amounts. A sponsored external event pays 50% of '
           'those numbers. (314) 935-3443. https://eventmanagement.wustl.edu/rates/',
           '⚠ Insurance requirements and limits, deposits and cancellation terms — NOT PUBLISHED on any retrieved '
           'WashU page. Confirm before signing anything. (314) 935-8264.',
           '⚠ The Activities Fair date, time, location, cost and eligibility — Campus Life names the event but '
           'publishes none of it. (314) 935-3443. https://campuslife.washu.edu/get-involved',
           '⚠ WUGO (wustl.presence.io) is JAVASCRIPT-RENDERED — NO WashU student organization could be enumerated. '
           'Whether a blockchain, crypto or fintech club exists is completely unknown.',
           '⚠ The Olin Business School faculty directory is JAVASCRIPT-RENDERED and returns an empty result set. No '
           'WashU faculty member could be confirmed. Olin publishes no main phone number. '
           'https://olin.washu.edu/faculty-and-research/faculty-directory/',
           '⚠ The WashU course bulletin search is ROBOTS-BLOCKED (bulletin.wustl.edu/search returned '
           'ROBOTS_DISALLOWED). No course could be checked.',
           'Fall 2026 add/drop deadlines are not printed on the bulletin academic calendar.',
           'DUC tabling pricing — the page publishes rules and hours but no cost, and in any case the tables are '
           'restricted to recognized student organizations and departments. '
           'https://eventmanagement.wustl.edu/items/duc-tabling/'],
  'note': 'WashU and SLU sit about fifteen minutes apart and UMSL about twenty minutes further — three campuses in '
          'one day is easy geographically. It is the ACCESS that makes the St. Louis cluster the weakest part of '
          'the state: two private institutions with no public-forum obligation and the thinnest of the four UM '
          'campuses. The money in Missouri is in Columbia, not St. Louis.'},

 # ---------------------------------------------------------------- 3. MISSOURI S&T
 {'state': 'Missouri',
  'name': 'Missouri University of Science and Technology',
  'city': 'Rolla, MO',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 2,
  'start': 'Mon Aug 24, 2026 (regular 16-week session)',
  'adddrop': 'Free add Mon Aug 24 — permission numbers required for the first two weeks. Free drop / 100% refund '
             'deadline Sun Aug 30, 2026. Last day to drop without "WD" on the transcript (regular session) '
             'Mon Oct 5, 2026.',
  'fallbreak': 'Begins 8:00 a.m. Thu Oct 8, 2026; ends 8:00 a.m. Mon Oct 12, 2026.',
  'thanksgiving': '⚠ Begins 8:00 a.m. Sun Nov 22, 2026; ends 8:00 a.m. Mon Nov 30, 2026 — NINE DAYS, THE LONGEST '
                  'THANKSGIVING SHUTDOWN OF ANY CAMPUS IN THIS SET. Rolla is empty for over a week.',
  'lastclass': 'Fri Dec 11, 2026',
  'finals': 'Begin 7:30 a.m. Mon Dec 14, 2026; end Fri Dec 18. Commencement Fri Dec 18 6:00 p.m. (PhD and '
            'Master\'s); Sat Dec 19 10:00 a.m. and 3:00 p.m. (undergraduate, by department).',
  'cal_url': 'https://registrar.mst.edu/media/administrative/registrar/documents/calendars/2026/FS2026%20Dates%20and%20Deadlines.pdf',
  'cal_status': 'CONFIRMED on the Registrar\'s official "FS2026 Dates and Deadlines" PDF, which dates every entry '
                'with a weekday. SEMESTERS (regular 16-week session, with shorter sessions running alongside). '
                'Calendar index: https://registrar.mst.edu/calendars/',
  'fair': 'Involvement fair — NOT PUBLISHED',
  'fair_date': '⚠ UNVERIFIED — no involvement fair, org fair or welcome-week tabling event is published on any '
               'retrievable Missouri S&T page. Student Involvement claims "more than 200 student organizations" '
               'spanning academic societies, cultural groups, service organizations, DESIGN TEAMS, club sports and '
               'special interest clubs, but publishes no fair. Call (573) 341-4025 or (573) 341-6771.',
  'fair_outside': '⚠⚠ IRRELEVANT AT S&T — THE CAMPUS-WIDE RULE ANSWERS IT FIRST. "Credit card, telephone card, or '
                  'other financial services vendors are not allowed at the Havener Center OR ON THE MISSOURI S&T '
                  'CAMPUS." Whatever the fair\'s own rules turn out to be, that sentence sits above them. Settle '
                  'the classification question before asking about a table: (573) 341-4399.',
  'fair_cost': '⚠ NO DOLLAR AMOUNTS ARE PUBLISHED ANYWHERE. Two table-space categories exist for non-affiliated '
               'groups — Informational and Commercial — and both carry a rental fee, but the policy says only '
               '"Please contact Events and Hospitality Management for pricing." What IS published: $50 '
               'administrative fee for late cancellation and for a no-show, decoration-violation fee "not less than '
               '$50," technician services "minimum $25 charge," overtime "minimum fee assessed is $50," and a 3% '
               'convenience fee on credit card payments. (573) 341-4399.',
  'fair_deadline': 'Table space of either category requires "two full business days prior to event." Cancellation '
                   'must also be at least two full business days ahead or a $50 fee attaches after the first '
                   'warning. Non-S&T users must additionally complete a usage agreement.',
  'fair_url': 'https://involvement.mst.edu/',
  'policy': 'Havener Center Policies (Events and Hospitality Management) — the operative campus document, no policy '
            'number or effective date printed; above it, UM System Collected Rules and Regulations 110.010',
  'policy_url': 'https://havener.mst.edu/policies/',
  'policy_key': "Havener Center Policies (havener.mst.edu/policies/ — NO POLICY NUMBER AND NO EFFECTIVE DATE ARE "
                "PRINTED ON THE PAGE). ⚠⚠ THE DECISIVE SENTENCE, AND THE ONLY ONE OF ITS KIND FOUND ANYWHERE IN "
                "MISSOURI: 'CREDIT CARD, TELEPHONE CARD, OR OTHER FINANCIAL SERVICES VENDORS ARE NOT ALLOWED AT THE "
                "HAVENER CENTER OR ON THE MISSOURI S&T CAMPUS.' That is a CAMPUS-WIDE prohibition naming a category "
                "of vendor by financial function, with NO exception process printed anywhere on the page. Whether a "
                "non-custodial protocol counts as an 'other financial services vendor' is genuinely open — but it "
                "is the question S&T will ask, and an ambassador must not be surprised by it. Second: 'DIRECT "
                "SOLICITATION OF MONEY, REGARDLESS OF THE INTENDED USE, IS NOT PERMITTED ON UNIVERSITY PROPERTY.' "
                "⚠ ANTI-FRONTING — THIS CLOSES THE CLUB WORKAROUND THAT WORKS ELSEWHERE: 'NON-UNIVERSITY GROUPS OR "
                "INDIVIDUALS MAY NOT RESERVE FACILITIES IN THE NAME OF A STUDENT GROUP OR UNIVERSITY DEPARTMENT TO "
                "AVOID PAYMENT OF USAGE FEES.' Related: 'Reservation requests will only be accepted in the name of "
                "the group or individual sponsoring the event.' NON-S&T USERS: 'Users of Havener Center who are not "
                "associated with Missouri S&T must complete an usage agreement in order to hosts events in the "
                "facility' (typos in the original). THE TABLE TIERS, verbatim — Informational: 'The organization "
                "distributes information to the campus community or gives away items at no charge.' Commercial: "
                "'The organization gathers information or sells goods and/or services for a profit.' Both require "
                "'two full business days prior to event' and both carry rental fees, but 'PLEASE CONTACT EVENTS AND "
                "HOSPITALITY MANAGEMENT FOR PRICING' — NO DOLLAR AMOUNT IS PUBLISHED FOR EITHER. Note the "
                "Informational definition is the one DGD could plausibly meet: distributing information and giving "
                "items away at no charge, selling nothing. That is the narrow exception worth asking about — but "
                "the financial-services sentence sits above it. MONEY TERMS THAT ARE PUBLISHED: 'Groups failing to "
                "cancel a reservation at least two full business days in advance of event... will receive a warning "
                "after the first infraction and a $50 ADMINISTRATIVE FEE for each time thereafter'; 'Groups who "
                "have a confirmed reservation that do not utilize meeting room(s) or space will be subject to a $50 "
                "ADMINISTRATIVE FEE'; decoration violations 'not less than $50'; technician services 'minimum $25 "
                "charge'; overtime 'minimum fee assessed is $50'; and A 3% CONVENIENCE FEE ON CREDIT CARD PAYMENTS "
                "— the one place S&T touches payment credentials, and it runs against the payer, not the vendor. "
                "INSURANCE: 'Proof of general liability insurance in the amount of ONE MILLION DOLLARS "
                "($1,000,000.00)' — as printed this attaches to events with ALCOHOLIC BEVERAGES; no general "
                "insurance requirement or limit for a table was found. PRIORITY OF USE (havener.mst.edu/"
                "reservations/): 'As a state and student fee-funded building, Havener Center offers its services to "
                "student organizations first and foremost'; 'Community members and non-university groups should "
                "contact reservations directly.' ABOVE IT ALL SITS UM SYSTEM CRR 110.010 — full text quoted in the "
                "Mizzou record; in short, 110.010.G.1 'The sale of anything, the soliciting of subscriptions or the "
                "collection of dues is prohibited... without prior authorization of the Chancellor,' 110.010.E.4.c "
                "'Other nonaffiliated and nonsponsored groups may make use of the facilities... upon written "
                "approval of the Chancellor,' and 110.010.E.6 'Nonaffiliated, nonsponsored groups... will be "
                "charged a fee approved by the Chancellor.' S&T is public and bound by RSMo s 173.1550, but "
                "s 173.1550(3) protects only NONCOMMERCIAL expressive activity — the statute does not reach DGD "
                "and does not touch the financial-services clause.",
  'sponsor_required': '⚠ NO — AND FRONTING IS EXPRESSLY PROHIBITED, SO A CLUB CANNOT CARRY YOU. "Non-university '
                      'groups or individuals may not reserve facilities in the name of a student group or '
                      'university department to avoid payment of usage fees," and "Reservation requests will only '
                      'be accepted in the name of the group or individual sponsoring the event." An outside group '
                      'books in its own name, completes a usage agreement and pays — and then runs straight into '
                      'the financial-services vendor ban. Do not spend weeks courting a design team or an ACM '
                      'chapter here expecting them to reserve on your behalf; that is precisely the arrangement the '
                      'policy names and forbids.',
  'clubs': [('⚠ MINERLINK COULD NOT BE ENUMERATED — 200+ ORGS, NONE READABLE',
             'The MinerLink directory (minerlink.mst.edu) is JAVASCRIPT-RENDERED — the fetch returned only '
             '{"title":"StudentsCommunityPlatform"} metadata with no organization listings at all. Not confirmed '
             'login-gated, but not machine-readable. NO S&T CLUB OF ANY KIND COULD BE CONFIRMED, and no blockchain '
             'or crypto club could be ruled out. Student Involvement describes the 200+ orgs as spanning academic '
             'societies, cultural groups, service organizations, DESIGN TEAMS, club sports and special interest '
             'clubs — at an engineering school the design teams are the likeliest technical audience. Ask by name '
             'at (573) 341-4025.',
             'https://minerlink.mst.edu/web_app?id=24040&menu_id=56483&if=0&')],
  'faculty': [('⚠ Events and Hospitality Management',
               'WRITES AND ENFORCES THE FINANCIAL-SERVICES VENDOR BAN, SETS TABLE PRICING (published nowhere), AND '
               'ISSUES THE USAGE AGREEMENT FOR NON-S&T USERS. THE SINGLE MOST IMPORTANT CALL AT S&T, and the call '
               'to make BEFORE booking travel: ask directly whether a non-custodial protocol that sells nothing and '
               'gives away materials at no charge falls inside "other financial services vendors," or whether it '
               'can book the Informational table tier. Get the answer from this office, not from a student.',
               'Events and Hospitality Management',
               '(573) 341-4399',
               'https://havener.mst.edu/policies/'),
              ('Havener Center — reservations desk (1346 North Bishop Avenue, Rolla MO 65401)',
               'Books the space once Events and Hospitality Management has cleared the classification. Building '
               'hours 7:00 a.m.–10:00 p.m. Mon–Fri, extended at weekends.',
               'Havener Center',
               'reserve@mst.edu · (573) 341-4564',
               'https://havener.mst.edu/reservations/'),
              ('⚠ Student Involvement (218 Havener Center, 1346 N. Bishop, Rolla MO 65409)',
               'Owns MinerLink and the 200+ organizations, including the design teams — the only route to a club '
               'list, since the directory is JavaScript-rendered. Also the office to ask whether any involvement '
               'fair exists at all; none is published. NO INDIVIDUAL STAFF NAMES ARE LISTED on any Student '
               'Involvement page.',
               'Student Involvement',
               'involvement@mst.edu · (573) 341-4025',
               'https://involvement.mst.edu/'),
              ('Student Involvement — second published number',
               'A different number for the same office appears on the student-organizations page. Try both.',
               'Student Involvement',
               'involvement@mst.edu · (573) 341-6771',
               'https://involvement.mst.edu/studentorganizations/'),
              ('⚠ Career Opportunities and Employer Relations',
               'THE REAL DOOR INTO S&T. Runs the Career Fair on Tue Sep 22, 2026, 9:00 a.m.–2:00 p.m. A career fair '
               'is an EMPLOYER-RECRUITING framework, not a vendor-solicitation framework — it is the one route that '
               'does not obviously run through the Havener financial-services clause. Employer registration cost is '
               'NOT PUBLISHED; get it here.',
               'Career Opportunities and Employer Relations',
               'career@mst.edu · (573) 341-4343',
               'https://career.mst.edu/'),
              ('Department of Computer Science (325 Computer Science Building, 500 West 15th Street)',
               '⚠ THE DEPARTMENT PUBLISHES ITS RESEARCH AREAS AND BLOCKCHAIN IS NOT AMONG THEM: Systems and '
               'Networking; Cyber Security; Artificial Intelligence and Data Science; Theory and Quantum '
               'Computation; High-Performance and Cloud Computing. No department chair is named on the landing '
               'page. Call to ask whether any faculty member works on distributed ledgers and whether any course '
               'touches the subject — catalog.mst.edu is robots-blocked, so this is the only route to the answer.',
               'Computer Science',
               'csdept@mst.edu · (573) 341-4492',
               'https://cs.mst.edu/'),
              ('Office of the Registrar',
               'Confirmed the Fall 2026 dates above. Calendar index at registrar.mst.edu/calendars/.',
               'Registrar',
               'registrar@mst.edu · (573) 341-4181',
               'https://registrar.mst.edu/'),
              ('S&T Dining Services',
               'Printed on the Havener policies page; relevant only if food is involved at an event.',
               'Dining Services',
               '(573) 341-7019',
               'https://havener.mst.edu/policies/'),
              ('Missouri S&T main line',
               'Printed on the Havener policies page. Operator, last resort.',
               'Missouri S&T',
               '(800) 522-0938 (main line)',
               'https://havener.mst.edu/policies/'),
              ('(Blockchain / digital-assets faculty)',
               'NOT CONFIRMED — no Missouri S&T faculty member working on blockchain, cryptocurrency, digital '
               'assets or fintech could be confirmed on any live page, and the CS department\'s own list of '
               'research areas omits the subject. Look up via the CS department, (573) 341-4492.',
               'Computer Science',
               'csdept@mst.edu · (573) 341-4492',
               'https://cs.mst.edu/'),
              ('(Business and Information Technology / economics faculty)',
               'NOT CONFIRMED — S&T\'s business department was not reached in this pass. No fintech or monetary '
               'economics researcher could be confirmed. Look up here; route via the campus operator.',
               'Missouri S&T',
               'no number published — look up here, or (800) 522-0938',
               'https://www.mst.edu/')],
  'courses': [('(All Missouri S&T courses)',
               '⚠ NOT CHECKABLE — catalog.mst.edu IS ROBOTS-BLOCKED to research tooling '
               '(catalog.mst.edu/search/?P=blockchain returned ROBOTS_DISALLOWED), and both '
               '/coursesofinstruction/comp_sci/ and /undergraduate/coursesofinstruction/comp_sci/ return 404. NO '
               'S&T COURSE COULD BE VERIFIED in either direction. What IS known: the CS department publishes its '
               'research areas as Systems and Networking, Cyber Security, AI and Data Science, Theory and Quantum '
               'Computation, and High-Performance and Cloud Computing — blockchain is not among them. Call '
               '(573) 341-4492.',
               'https://catalog.mst.edu/')],
  'events': [('⚠⚠ Missouri S&T Career Fair',
              'Tue Sep 22, 2026, 9:00 a.m. – 2:00 p.m. CONFIRMED on the career services landing page; Sep 22, 2026 '
              'IS a Tuesday, so the listing is internally consistent and not stale. EMPLOYER REGISTRATION COST IS '
              'NOT PUBLISHED — call (573) 341-4343. THIS IS THE ONE ROUTE INTO S&T THAT DOES NOT OBVIOUSLY RUN '
              'THROUGH THE HAVENER FINANCIAL-SERVICES CLAUSE, because a career fair is an employer-recruiting '
              'framework rather than a vendor-solicitation framework. At an engineering school with 200+ orgs '
              'including design teams, it is also the highest-quality technical audience in Missouri.',
              'https://career.mst.edu/'),
             ('Hackathon — NONE CONFIRMED',
              'No S&T hackathon could be confirmed. Given the engineering profile one very likely exists; search '
              'engines were unavailable for this pass. Ask Student Involvement, (573) 341-4025, and the CS '
              'department, (573) 341-4492. Contrast Mizzou, which has TigerHacks with published sponsor tiers.',
              '')],
  'play': 'Rolla is the best technical audience in Missouri sitting behind the worst-fitting sentence in Missouri, '
          'and an ambassador needs to know that sentence before getting in the car: "Credit card, telephone card, '
          'or other financial services vendors are not allowed at the Havener Center OR ON THE MISSOURI S&T '
          'CAMPUS." That is campus-wide, it names a category by financial function, and no exception process is '
          'printed. Alongside it: "Direct solicitation of money, regardless of the intended use, is not permitted '
          'on University property," and an explicit anti-fronting rule — "Non-university groups or individuals may '
          'not reserve facilities in the name of a student group or university department to avoid payment of usage '
          'fees" — which means courting a design team to book on your behalf is exactly the arrangement the policy '
          'forbids. So do NOT plan a table first. Make one call, to Events and Hospitality Management at '
          '(573) 341-4399, and ask the only question that matters: does a non-custodial protocol that sells nothing '
          'and gives away materials at no charge fall inside "other financial services vendors," or can it book the '
          'INFORMATIONAL table tier, which the policy itself defines as an organization that "distributes '
          'information to the campus community or gives away items at no charge"? That is the narrow exception and '
          'it is written into the same document. Get the answer in writing. Meanwhile, book the other door: the '
          'Missouri S&T Career Fair, Tue Sep 22, 2026, 9 a.m.–2 p.m., (573) 341-4343 — an employer-recruiting '
          'framework rather than a vendor-solicitation one, and the cleanest way to stand in front of exactly the '
          'right students. Cost is unpublished; ask. On calendar, note the trap: S&T shuts down for NINE DAYS at '
          'Thanksgiving, 8 a.m. Nov 22 to 8 a.m. Nov 30, the longest closure in the state, and there is also a fall '
          'break Oct 8–12. The usable windows are Aug 24 – Oct 7 and Oct 12 – Nov 20. Everything else here is dark: '
          'MinerLink is JavaScript-rendered so not one of the 200+ organizations could be read, catalog.mst.edu is '
          'robots-blocked so no course could be checked, and the CS department\'s published research areas do not '
          'include blockchain.',
  'gaps': ['⚠⚠ WHETHER DGD IS AN "OTHER FINANCIAL SERVICES VENDOR." The entire campus turns on this one '
           'classification, and the ban is campus-wide, not building-specific. Get it answered by Events and '
           'Hospitality Management, (573) 341-4399, and get it in writing. '
           'https://havener.mst.edu/policies/',
           '⚠⚠ TABLE PRICING — the Informational and Commercial tiers both carry rental fees but the policy says '
           'only "Please contact Events and Hospitality Management for pricing." NO DOLLAR AMOUNT IS PUBLISHED. '
           '(573) 341-4399.',
           '⚠ Missouri S&T Career Fair employer registration cost and deadline — the Sep 22 date is confirmed but '
           'no price appears on the page. (573) 341-4343. https://career.mst.edu/',
           '⚠ Whether ANY involvement fair or welcome-week tabling event exists at S&T — none is published '
           'anywhere. (573) 341-4025 or (573) 341-6771.',
           '⚠ MinerLink is JAVASCRIPT-RENDERED — 200+ organizations including design teams, and NOT ONE could be '
           'enumerated. Whether a blockchain, crypto or fintech club exists is completely unknown. (573) 341-4025.',
           '⚠ catalog.mst.edu is ROBOTS-BLOCKED and the course-of-instruction URLs 404 — no S&T course could be '
           'checked for blockchain content. (573) 341-4492.',
           'No blockchain or digital-assets faculty member could be confirmed; the CS department omits the subject '
           'from its published research areas. (573) 341-4492.',
           'Whether the campus reservation process satisfies CRR 110.010.E.4.c\'s "written approval of the '
           'Chancellor" for a nonaffiliated group, and what the Chancellor-approved fee is. (573) 341-4399.',
           'The Havener policies page carries NO POLICY NUMBER AND NO EFFECTIVE DATE — ask for the dated, numbered '
           'version, and for any Student Union / facility-use manual PDF that may print more.'],
  'note': 'Rolla is roughly 100 miles south-west of St. Louis on I-44, so it combines naturally with the St. Louis '
          'cluster rather than with Columbia. Missouri S&T is one of the four UM System campuses governed by CRR '
          '110.010 — the full systemwide text is quoted in the Mizzou record and is not repeated here.'},

 # ---------------------------------------------------------------- 4. SLU
 {'state': 'Missouri',
  'name': 'Saint Louis University',
  'city': 'St. Louis, MO',
  'type': 'Private (religious)',
  'tier': 'B — Regional',
  'access': 3,
  'start': '⚠ Wed Aug 19, 2026 — THE EARLIEST START IN MISSOURI, five days ahead of the Aug 24 wave and the only '
           'midweek start in the state.',
  'adddrop': '⚠ NOT PRINTED on the registrar\'s summary calendar page. The full 2026-2027 PDF was not retrieved — '
             'the registrar references slu.edu/registrar/pdfs/2026-2027-academic-calendar.pdf but the copy tested '
             'at slu.edu/pdfs/... returns 404. Call (314) 977-2269.',
  'fallbreak': 'Oct 22–23, 2026 — later in the term than any other Missouri campus, and NOT part of the Oct 8–12 '
               'cluster the rest of the state takes.',
  'thanksgiving': 'Nov 25–27, 2026',
  'lastclass': 'Fri Dec 4, 2026',
  'finals': 'Mon Dec 7 – Fri Dec 11, 2026. No study day is listed for Fall 2026 on the summary calendar.',
  'cal_url': 'https://www.slu.edu/registrar/calendars/index.php',
  'cal_status': 'PARTIAL — term boundaries, fall break, Thanksgiving, last class and finals are CONFIRMED on the '
                'registrar\'s Fall 2026 calendar table, which prints "Aug. 19 (Wed.)" for the first day. SEMESTERS, '
                'confirmed on the same page. Add/drop deadlines are NOT on the summary table and the full PDF was '
                'not retrieved.',
  'fair': 'Involvement fair — NOT FOUND',
  'fair_date': '⚠ UNVERIFIED — no fall involvement fair, org fair or welcome-week tabling event is published on any '
               'retrievable SLU page. The Student Involvement Center describes advising and mentoring and points to '
               'SLU Groups, but names no fair. Call (314) 977-2805.',
  'fair_outside': 'UNVERIFIED — no eligibility rule could be found because no fair could be found. SLU is PRIVATE '
                  'and CATHOLIC/JESUIT: it has no public-forum obligation and RSMo s 173.1550 does not reach it, so '
                  'the answer is whatever SLU decides it is.',
  'fair_cost': 'UNVERIFIED — not published.',
  'fair_deadline': 'UNVERIFIED — not published.',
  'fair_url': 'https://www.slu.edu/life-at-slu/student-involvement/index.php',
  'policy': '⚠ NOT RETRIEVED — SLU\'s governing solicitation and facility-use policy could not be reached on any '
            'tested URL. Rated PROVISIONAL.',
  'policy_url': 'https://www.slu.edu/life-at-slu/student-involvement/index.php',
  'policy_key': "⚠⚠ PROVISIONAL — THE GOVERNING POLICY COULD NOT BE RETRIEVED, AND THIS RATING IS A PLACEHOLDER, "
                "NOT A FINDING. Rated 3 under the standing rule for unretrievable policy: do not guess in either "
                "direction. Every candidate URL tested returned HTTP 404 — /about/catholic-jesuit-identity/policies/"
                "solicitation.php, /human-resources/pdfs/policies/solicitation-policy.pdf, /event-services/"
                "index.php, /scheduling/index.php, /life-at-slu/student-responsibility-and-community-standards/"
                "index.php. The Busch Student Center page carries NO reservation rules, NO tabling rules, NO rates "
                "and NO external-group terms, and directs all such questions to the Information Desk. The student-"
                "organization resources page carries NO handbook, NO PDF, NO policy text and NO phone number. "
                "catalog.slu.edu is ROBOTS-BLOCKED. Every general search engine is robots-blocked to this tooling, "
                "so the policy could not be located by search either. WHAT IS CERTAIN AND MATTERS MORE THAN THE "
                "MISSING TEXT: SLU IS A PRIVATE, CATHOLIC, JESUIT INSTITUTION. IT HAS NO PUBLIC-FORUM OBLIGATION, "
                "AND RSMo s 173.1550 — WHICH BY ITS TERMS REACHES ONLY 'PUBLIC INSTITUTIONS OF HIGHER EDUCATION IN "
                "THIS STATE' — DOES NOT APPLY. DO NOT CITE THE CAMPUS FREE EXPRESSION ACT AT SLU; it will read as "
                "unserious and it is simply wrong. A Jesuit mission-alignment argument is the register that works "
                "here — but a for-profit cryptocurrency project is a hard fit for it, and that should be conceded "
                "honestly rather than dressed up. ASK FOR, BY NAME, ON THE FIRST CALL: (1) the written solicitation "
                "policy and its number; (2) whether an outside for-profit entity may reserve space at all during "
                "term; (3) whether a recognized student organization may sponsor or reserve on behalf of an outside "
                "entity, or whether that is treated as fronting; (4) the Busch Student Center tabling rate for a "
                "non-university group; (5) insurance limits, deposits and cancellation terms; (6) whether anything "
                "in the policy reaches payment credentials or signing agreements on site. Two numbers cover all "
                "six: Student Involvement (314) 977-2805 and the Busch Student Center Information Desk "
                "(314) 977-2820, which the BSC page names explicitly as the contact for 'space reservations, "
                "tabling permissions, and applicable rules or fees.'",
  'sponsor_required': 'UNVERIFIED — no SLU policy on sponsorship, fronting or outside-entity access could be '
                      'retrieved. Ask explicitly whether a recognized student organization may reserve on behalf '
                      'of an outside entity, and whether SLU treats that as fronting. (314) 977-2805 / '
                      '(314) 977-2820.',
  'clubs': [('⚠ NO SLU CLUB OF ANY KIND COULD BE CONFIRMED — 200+ ORGS, NONE READABLE',
             'SLU Groups (groups.sluconnection.com), described by SLU as "the University\'s one-stop engagement '
             'platform," is JAVASCRIPT-RENDERED — the page returns the literal string "This application requires '
             'JavaScript to be enabled" and no organization listings, no search results and no club names. Not '
             'confirmed login-gated, but not machine-readable. Whether SLU has a blockchain, crypto, fintech, '
             'investment or ACM club is COMPLETELY UNKNOWN. Ask the Student Involvement Center by name at '
             '(314) 977-2805.',
             'https://groups.sluconnection.com/')],
  'faculty': [('⚠ Student Involvement Center (Busch Student Center Room 319, 20 N. Grand Blvd.)',
               'THE FIRST CALL AT SLU. Owns SLU Groups and the 200+ organizations, and is the office to ask for the '
               'written solicitation policy — which could not be retrieved from any live page. NO INDIVIDUAL STAFF '
               'NAMES ARE PUBLISHED; the page refers to "SIC staff" generically and points to a full staff '
               'directory page that was not reached.',
               'Student Involvement Center',
               'involvement@slu.edu · (314) 977-2805',
               'https://www.slu.edu/life-at-slu/student-involvement/index.php'),
              ('⚠ Busch Student Center — Information Desk',
               'THE SECOND CALL, AND POSSIBLY THE MORE USEFUL ONE. The BSC page names this number explicitly as the '
               'contact "to inquire about space reservations, tabling permissions, and applicable rules or fees" — '
               'the three things SLU publishes nowhere. The BSC holds the Wool Ballrooms, the Saint Louis Room and '
               'numerous conference and customizable meeting spaces.',
               'Busch Student Center',
               'BSC@slu.edu · (314) 977-2820',
               'https://www.slu.edu/life-at-slu/busch-student-center/index.php'),
              ('Office of the University Registrar (DuBourg Hall, Room 22, One North Grand Blvd.)',
               'Confirmed the Aug 19 start and the Fall 2026 boundaries. Ask for the add/drop deadlines, which are '
               'not on the summary calendar. Fax (314) 977-3447.',
               'Registrar',
               'registrar@slu.edu · (314) 977-2269',
               'https://www.slu.edu/registrar/contact-us.php'),
              ('Classroom Scheduling',
               'Separate from the BSC — books academic rooms. Relevant if a department or faculty member hosts a '
               'seminar rather than a table.',
               'Registrar',
               '(314) 977-3017',
               'https://www.slu.edu/registrar/contact-us.php'),
              ('(Chaifetz School of Business / computer science faculty)',
               'NOT CONFIRMED — no SLU faculty member could be confirmed on any relevant topic in this pass. No '
               'department directory was reached. Look up here, and route via Student Involvement or the operator.',
               'Saint Louis University',
               'no number published — look up here, or (314) 977-2805',
               'https://www.slu.edu/')],
  'courses': [('(All SLU courses)',
               '⚠ NOT CHECKABLE — catalog.slu.edu IS ROBOTS-BLOCKED to research tooling '
               '(catalog.slu.edu/search/?P=blockchain returned ROBOTS_DISALLOWED). No SLU course could be verified '
               'for blockchain, crypto or fintech content in either direction. Gap.',
               'https://catalog.slu.edu/')],
  'events': [('(All SLU events)',
              'NOT RETRIEVED — no career fair, entrepreneurship week, speaker series or hackathon could be '
              'confirmed at SLU in this pass. SLU has a well-known entrepreneurship reputation, so an '
              'entrepreneurship-week or startup-competition calendar very likely exists; it could not be reached. '
              'Ask Student Involvement, (314) 977-2805.',
              'https://www.slu.edu/life-at-slu/student-involvement/index.php')],
  'play': 'SLU is a one-hour phone problem, not a research problem, and it is worth the hour because of the '
          'calendar: SLU starts Wed Aug 19, 2026, the EARLIEST START IN MISSOURI, so it is in session and at full '
          'attention while the Aug 24 wave is still moving in — and it sits fifteen minutes from WashU and twenty '
          'from UMSL, so the St. Louis day is cheap to run. But nothing about SLU\'s access is knowable from the '
          'web. The governing solicitation and facility-use policy could NOT be retrieved: five candidate URLs '
          '404\'d, the Busch Student Center page carries no reservation rules or rates, the student-organization '
          'resources page carries no handbook and no phone number, catalog.slu.edu is robots-blocked, and SLU '
          'Groups is JavaScript-rendered so not one of the 200+ organizations could be read. It is rated 3 as a '
          'PLACEHOLDER under the rule for unretrievable policy — that number is not a finding and should not be '
          'quoted to anyone. Two calls close it. Ring the Busch Student Center Information Desk at (314) 977-2820 '
          '— the BSC page names that number specifically for "space reservations, tabling permissions, and '
          'applicable rules or fees" — and the Student Involvement Center at (314) 977-2805, and ask for the '
          'written solicitation policy by name, the non-university tabling rate, whether a student org may reserve '
          'on behalf of an outside entity, and the insurance and deposit terms. One thing to get right before '
          'dialling: SLU IS PRIVATE, CATHOLIC AND JESUIT. It has no public-forum obligation and the Campus Free '
          'Expression Act, which by its terms covers only "public institutions of higher education in this state," '
          'does not reach it. Do not cite the statute here. The register that works at a Jesuit institution is '
          'mission alignment, and a for-profit crypto project is a genuinely hard fit for it — say so plainly '
          'rather than stretching, because the people on that phone will hear the stretch.',
  'gaps': ['⚠⚠ THE ENTIRE WRITTEN POLICY. No solicitation, facility-use or outside-vendor policy could be reached. '
           'Five URLs tested returned 404 (/about/catholic-jesuit-identity/policies/solicitation.php, '
           '/human-resources/pdfs/policies/solicitation-policy.pdf, /event-services/index.php, /scheduling/'
           'index.php, /life-at-slu/student-responsibility-and-community-standards/index.php). Ask for it by name: '
           '(314) 977-2820 or (314) 977-2805.',
           '⚠⚠ The Busch Student Center tabling rate for a non-university group — no rate card exists on any SLU '
           'page. (314) 977-2820.',
           '⚠ Whether a recognized student organization may reserve or sponsor on behalf of an outside entity, or '
           'whether SLU treats that as fronting. (314) 977-2805.',
           '⚠ Insurance requirements and limits, deposits and cancellation terms — nothing published. '
           '(314) 977-2820.',
           '⚠ Whether SLU holds a fall involvement fair at all, and if so its date, cost and whether outside '
           'organizations may table. Nothing published. (314) 977-2805.',
           '⚠ SLU Groups (groups.sluconnection.com) is JAVASCRIPT-RENDERED — "This application requires JavaScript '
           'to be enabled." NOT ONE of the 200+ organizations could be enumerated.',
           '⚠ catalog.slu.edu is ROBOTS-BLOCKED — no SLU course could be checked for blockchain or fintech content.',
           'Fall 2026 add/drop deadlines — not on the registrar\'s summary calendar; the full 2026-2027 PDF was not '
           'retrieved (the copy at slu.edu/pdfs/2026-2027-academic-calendar.pdf returns 404). (314) 977-2269.',
           'No SLU faculty member could be confirmed on any topic. No department directory was reached.',
           'No SLU career fair, entrepreneurship week, speaker series or hackathon could be confirmed.'],
  'note': 'SLU, WashU and UMSL sit within about thirty minutes of each other — the tightest campus cluster in '
          'Missouri and the natural shape of a single St. Louis day. The cruelty of the geography is that this '
          'cluster is the LEAST open part of the state: two private institutions with no public-forum obligation '
          'and the thinnest of the four UM campuses. SLU\'s Aug 19 start is nonetheless the earliest opportunity in '
          'Missouri to stand in front of students at all.'},

 # ---------------------------------------------------------------- 5. MISSOURI STATE
 {'state': 'Missouri',
  'name': 'Missouri State University',
  'city': 'Springfield, MO',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 3,
  'start': '⚠ Mon Aug 17, 2026 — first wave, a full week ahead of Mizzou, WashU, S&T, UMSL and SEMO.',
  'adddrop': 'Late registration with full refund eligibility: Aug 24, 2026 – Aug 28, 2026. No other add/drop '
             'deadline is printed on the calendar page.',
  'fallbreak': 'Oct 8 – Oct 11, 2026 — no classes, offices open. Part of the Oct 8–12 cluster that takes five '
               'Missouri campuses dark in the same week.',
  'thanksgiving': '⚠ Nov 21 – Nov 29, 2026 (offices closed Nov 25–27) — a NINE-DAY student absence.',
  'lastclass': '⚠ Thu Dec 3, 2026 — MISSOURI STATE FINISHES FIRST IN THE STATE, a week before Mizzou, S&T, UMSL and '
               'SEMO. ANYTHING SCHEDULED IN SPRINGFIELD AFTER ABOUT NOV 18 IS WORTHLESS.',
  'finals': 'Dec 5 – Dec 10, 2026',
  'cal_url': 'https://www.missouristate.edu/registrar/academic-calendar.htm',
  'cal_status': 'CONFIRMED on the Registrar\'s academic calendar page, which prints explicit 2026 dates for every '
                'entry ("Oct. 8, 2026 - Oct. 11, 2026", "Nov. 21, 2026 - Nov. 29, 2026", "Dec. 5, 2026 - Dec. 10, '
                '2026"). SEMESTERS. Note the registrar\'s landing page still headlines the 2025-2026 calendar; the '
                'Fall 2026 dates above come from the calendar page itself, which is current.',
  'fair': 'Involvement fair — NOT PUBLISHED',
  'fair_date': '⚠ UNVERIFIED — no fall involvement fair, org fair or welcome-week tabling event is published on any '
               'retrievable Missouri State page. The Office of Student Engagement pages that were reached carry no '
               'events at all. Missouri State publishes NO DIRECT PHONE NUMBER for Student Engagement — go through '
               'the switchboard, (417) 836-5000, and ask for the Office of Student Engagement.',
  'fair_outside': 'UNVERIFIED — no eligibility rule could be found because no fair could be found and no '
                  'solicitation policy could be retrieved.',
  'fair_cost': 'UNVERIFIED — not published.',
  'fair_deadline': 'UNVERIFIED — not published.',
  'fair_url': 'https://www.missouristate.edu/StudentEngagement/student-organizations.htm',
  'policy': '⚠ NOT RETRIEVED — Missouri State\'s policy library is unreachable to research tooling. Rated '
            'PROVISIONAL.',
  'policy_url': 'https://www.missouristate.edu/registrar/academic-calendar.htm',
  'policy_key': "⚠⚠ PROVISIONAL — THE GOVERNING POLICY COULD NOT BE RETRIEVED, AND THIS RATING IS A PLACEHOLDER, "
                "NOT A FINDING. Rated 3 under the standing rule; do not guess in either direction. THE FAILURE MODE "
                "IS ITSELF THE FINDING, and it is unusually complete: (1) https://www.missouristate.edu/policy/ "
                "returns TOO MANY REDIRECTS — a redirect loop, not a 404; (2) https://policies.missouristate.edu/ "
                "DOES NOT RESOLVE AT ALL — DNS failure, 'Name or service not known'; (3) "
                "https://www.missouristate.edu/search/ 302-redirects to search.missouristate.edu, which is a "
                "JAVASCRIPT-RENDERED search shell returning no results to tooling; (4) every guessed Plaster "
                "Student Union and Event Services URL returns 404 (/PSU/, /PSU/reservations.htm, /psu/index.htm, "
                "/PlasterStudentUnion/, /eventservices/); (5) every guessed Student Engagement sub-page returns "
                "404; (6) FIRE's school page 302-redirects to a generic college index and yields nothing. Missouri "
                "State's solicitation policy, its Plaster Student Union tabling rates and its facility-use terms "
                "are ALL UNKNOWN. WHAT IS CERTAIN: Missouri State is a PUBLIC institution and IS bound by RSMo "
                "s 173.1550, so its outdoor areas are 'deemed traditional public forums' and any restriction must "
                "'employ clear, published, content, and viewpoint-neutral criteria' with 'ample alternative means "
                "of expression.' BUT s 173.1550(3) protects only 'NONCOMMERCIAL expressive activity,' so the "
                "statute does not carry DGD and will not defeat a solicitation rule or a tabling fee. ⚠ NOTE THE "
                "IRONY WORTH RAISING ON THE CALL: the statute requires restrictions to be CLEAR AND PUBLISHED, and "
                "Missouri State's are not reachable at all. That is a fair and polite reason to ask them to send "
                "the policy in writing. ASK FOR, BY NAME: the solicitation / sales policy and its number; the "
                "Plaster Student Union tabling rate for a non-university group; whether an outside for-profit may "
                "reserve at all during term; whether a recognized student organization may reserve on behalf of an "
                "outside entity; insurance limits, deposits and cancellation terms. ONE CALL CLOSES THIS ENTIRE "
                "CAMPUS: (417) 836-5000 — ask for the Office of Student Engagement and for Event/Facility "
                "Scheduling or the Plaster Student Union.",
  'sponsor_required': 'UNVERIFIED — no Missouri State policy on sponsorship, fronting or outside-entity access '
                      'could be retrieved. Ask explicitly. (417) 836-5000.',
  'clubs': [('⚠ NO MISSOURI STATE CLUB COULD BE CONFIRMED — 300+ ORGS, NONE READABLE',
             'The directory at missouristate.presence.io/organizations (branded "Real Bears Get Involved") is '
             'JAVASCRIPT-RENDERED — the fetch returned page metadata only, with no club listings and no search '
             'results. It is the same Presence platform that is also unreadable at SEMO. Missouri State claims '
             '"over 300 student organizations." Whether any blockchain, crypto, fintech, investment or ACM club '
             'exists is COMPLETELY UNKNOWN. Ask the Office of Student Engagement by name through the switchboard, '
             '(417) 836-5000.',
             'https://missouristate.presence.io/organizations')],
  'faculty': [('⚠ Missouri State University — main switchboard',
               'THE ONLY CONFIRMED NUMBER AT THIS CAMPUS, and that is itself the headline finding: Missouri State '
               'has the thinnest published contact picture in the set. Ask the operator for the Office of Student '
               'Engagement, for Event or Facility Scheduling, and for the Plaster Student Union — none of which '
               'publishes a direct number on any page reached.',
               'Missouri State University',
               'Info@MissouriState.edu · (417) 836-5000 (MAIN LINE)',
               'https://www.missouristate.edu/StudentEngagement/student-organizations.htm'),
              ('Office of Student Engagement',
               '⚠ NO DIRECT PHONE NUMBER IS PUBLISHED — the student-organizations page gives only the university '
               'switchboard and the general Info@MissouriState.edu inbox. The office oversees the 300+ student '
               'organizations and the Presence directory. No staff names are published either. Look up here; reach '
               'via the main line.',
               'Student Engagement',
               'Info@MissouriState.edu · no number published — look up here, or (417) 836-5000',
               'https://www.missouristate.edu/StudentEngagement/'),
              ('Office of the Registrar (Carrington Hall 320)',
               'Confirmed the Fall 2026 dates above. ⚠ NO DIRECT PHONE NUMBER IS PUBLISHED — email only. Office '
               'hours Monday–Friday 8 a.m. to 5 p.m., with Thursday mornings 8–9 a.m. unavailable.',
               'Registrar',
               'Registrar@MissouriState.edu · no number published — look up here, or (417) 836-5000',
               'https://www.missouristate.edu/registrar/'),
              ('(Plaster Student Union / Event Services)',
               'NOT CONFIRMED — every URL tested 404s (/PSU/, /PSU/reservations.htm, /psu/index.htm, '
               '/PlasterStudentUnion/, /eventservices/). The office that would sell a table cannot be reached on '
               'the web at all. Ask the switchboard for it by name.',
               'Plaster Student Union',
               'no number published — look up here, or (417) 836-5000',
               'https://www.missouristate.edu/'),
              ('(Blockchain / finance / fintech faculty)',
               'NOT CONFIRMED — no Missouri State faculty member could be confirmed on any relevant topic. No '
               'department directory was reached. Look up here; route via the switchboard.',
               'Missouri State University',
               'no number published — look up here, or (417) 836-5000',
               'https://www.missouristate.edu/')],
  'courses': [('(All Missouri State courses)',
               'NOT CHECKED — no Missouri State catalog or course-search page was reached in this pass. No course '
               'could be verified for blockchain, crypto or fintech content in either direction. Gap.',
               'https://www.missouristate.edu/')],
  'events': [('(All Missouri State events)',
              'NOT RETRIEVED — no career fair, involvement fair, speaker series or hackathon could be confirmed at '
              'Missouri State in this pass. Ask the Office of Student Engagement through the switchboard, '
              '(417) 836-5000.',
              'https://www.missouristate.edu/StudentEngagement/')],
  'play': 'Springfield is a blank page with a hard clock on it, and the clock is the reason to deal with it early '
          'rather than late. Missouri State started Mon Aug 17, 2026 — the term is already three and a half weeks '
          'old — and it FINISHES FIRST IN THE STATE, with the last day of classes on Thu Dec 3 and finals Dec 5–10. '
          'Subtract the Oct 8–11 fall break and the nine-day Thanksgiving absence Nov 21–29 and the usable window '
          'is essentially now to Nov 18. Against that, not one substantive fact about access is knowable from the '
          'web. Missouri State\'s policy library returns a REDIRECT LOOP at missouristate.edu/policy, '
          'policies.missouristate.edu DOES NOT RESOLVE AT ALL (DNS failure), the site search is JavaScript-only, '
          'every Plaster Student Union and Event Services URL 404s, and the 300+ organization directory is a '
          'JavaScript-rendered Presence app. There is exactly one confirmed phone number on this entire campus — '
          'the switchboard, (417) 836-5000 — because neither the Office of Student Engagement nor the Registrar '
          'publishes a direct line. So the play is a single deliberate call: ask the operator for the Office of '
          'Student Engagement and for the Plaster Student Union, and get four things in writing — the solicitation '
          'policy and its number, the non-university tabling rate, whether an outside for-profit may reserve during '
          'term, and whether a recognized student organization may reserve on its behalf. One useful lever on that '
          'call: Missouri State is public, so RSMo s 173.1550 binds it, and the statute requires time-place-manner '
          'restrictions to employ "clear, PUBLISHED, content, and viewpoint-neutral criteria." Missouri State\'s '
          'are not published anywhere reachable. That is a polite, accurate reason to ask them to send the policy. '
          'Do not overreach with the statute beyond that — s 173.1550(3) protects only NONCOMMERCIAL activity and '
          'gives DGD no right to table. Until that call happens, do not route an ambassador through Springfield; '
          'it is a four-hour drive from Columbia to a campus whose rules nobody can read.',
  'gaps': ['⚠⚠ THE ENTIRE WRITTEN POLICY AND EVERY RATE. missouristate.edu/policy returns TOO MANY REDIRECTS; '
           'policies.missouristate.edu FAILS DNS RESOLUTION; search.missouristate.edu is JavaScript-only. '
           '(417) 836-5000.',
           '⚠⚠ A DIRECT PHONE NUMBER FOR ANY MISSOURI STATE OFFICE. Neither the Office of Student Engagement nor '
           'the Registrar publishes one; the switchboard is the only confirmed number on the campus. This is the '
           'weakest contact coverage in the state.',
           '⚠ The Plaster Student Union tabling rate and reservation process — every PSU and Event Services URL '
           'tested returns 404. The office that would sell a table cannot be reached on the web.',
           '⚠ Whether a fall involvement fair exists at all, and its date, cost and outside-org eligibility. '
           '(417) 836-5000.',
           '⚠ The directory at missouristate.presence.io/organizations is JAVASCRIPT-RENDERED — NOT ONE of the 300+ '
           'organizations could be enumerated. Whether a blockchain or fintech club exists is unknown.',
           'No Missouri State faculty member could be confirmed on any topic; no department directory was reached.',
           'No Missouri State course catalog was reached — no course could be checked.',
           'No Missouri State career fair, speaker series or hackathon could be confirmed.',
           'Add/drop deadlines beyond the Aug 24–28 late-registration window are not printed on the calendar page.'],
  'note': 'Springfield is the south-west outlier — roughly three hours from Columbia and four from St. Louis — so '
          'it does not combine with any other stop in this packet. Given that it finishes first in the state and '
          'that nothing about its access is currently knowable, treat it as phone-first and travel-last.'},

 # ---------------------------------------------------------------- 6. UMKC
 {'state': 'Missouri',
  'name': 'University of Missouri–Kansas City',
  'city': 'Kansas City, MO',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 3,
  'start': '⚠⚠ UNVERIFIED — THE FALL 2026 CALENDAR COULD NOT BE RETRIEVED. For planning only, and explicitly NOT a '
           'finding: the three sibling UM System campuses whose calendars WERE confirmed — Mizzou, Missouri S&T and '
           'UMSL — ALL begin Mon Aug 24, 2026. UMKC very likely matches. DO NOT SCHEDULE ON THAT ASSUMPTION. '
           'Registrar (816) 235-1125.',
  'adddrop': 'UNVERIFIED — calendar not retrievable.',
  'fallbreak': 'UNVERIFIED — calendar not retrievable. The three confirmed sibling campuses all take Oct 8–12.',
  'thanksgiving': 'UNVERIFIED — calendar not retrievable. Mizzou and UMSL both run Nov 21–30; S&T runs Nov 22–30.',
  'lastclass': 'UNVERIFIED — calendar not retrievable.',
  'finals': 'UNVERIFIED — calendar not retrievable.',
  'cal_url': 'https://www.umkc.edu/registrar/academic-calendar.html',
  'cal_status': '⚠⚠ UNVERIFIED — https://www.umkc.edu/registrar/academic-calendar.html RETURNS AN EMPTY PAGE BODY. '
                'Confirmed twice on separate attempts: "The page body is empty. No content is displayed, and there '
                'are no dates, academic calendar information, or Fall 2026 scheduling details visible on this '
                'page." The content is either JavaScript-injected or the page is broken. The catalog route '
                '(catalog.umkc.edu/undergraduate-academic-regulations-information/academic-calendar/) returns '
                'navigation chrome only, with no calendar content. Every other URL variant tested returns 404 '
                '(/registrar/academic-calendar/, /registrar/academic-calendar/index.php, /registrar/academic-'
                'calendar/fall-2026.html, /registrar/calendars/index.html, catalog.umkc.edu/academic-calendar/). '
                'NOT ONE UMKC DATE IS CONFIRMED. Call (816) 235-1125.',
  'fair': 'Involvement fair — NOT PUBLISHED',
  'fair_date': '⚠ UNVERIFIED — no fall involvement fair is published on any retrievable UMKC page. The Office of '
               'Student Involvement page carries no events and no organization directory link. Call '
               '(816) 235-1407.',
  'fair_outside': 'UNVERIFIED — no eligibility rule could be found. The governing systemwide rule (CRR 110.010) '
                  'requires "prior authorization of the Chancellor" for any sale or solicitation, so the default '
                  'answer is "not without written approval."',
  'fair_cost': 'UNVERIFIED — no UMKC rate card of any kind was found. CRR 110.010.E.6 provides that '
               '"Nonaffiliated, nonsponsored groups... will be charged a fee approved by the Chancellor" — so a fee '
               'exists in principle and nobody has published its amount.',
  'fair_deadline': 'CRR 110.010.D.2 sets a floor where a student organization is the requester: "The organization '
                   'file a written request for approval of the activity or program at least ten days prior to the '
                   'event," with the Chancellor authorised to make exceptions "in special circumstances." No UMKC '
                   'campus deadline was found.',
  'fair_url': 'https://www.umkc.edu/student-affairs/offices/student-involvement.html',
  'policy': 'UM System Collected Rules and Regulations 110.010 (amended 11-18-21, 12-10-21, 6-29-23) — the '
            'operative document, because NO UMKC-specific solicitation, tabling or vendor page could be retrieved',
  'policy_url': 'https://www.umsystem.edu/ums/rules/collected_rules/facilities/ch110/110.010_regulations',
  'policy_key': "UM SYSTEM CRR 110.010 GOVERNS UMKC — and at UMKC it is ALL THERE IS, because no campus-level "
                "solicitation, tabling or vendor policy could be retrieved. Verbatim, with section numbers as "
                "printed (umsystem.edu/ums/rules/collected_rules/facilities/ch110/110.010_regulations; amendment "
                "history 12-10-49, 7-22-65, 9-26-69, 5-18-73, 11-19-82, 9-16-88, 11-18-21, 12-10-21, 6-29-23): "
                "110.010.G.1 — 'THE SALE OF ANYTHING, THE SOLICITING OF SUBSCRIPTIONS OR THE COLLECTION OF DUES IS "
                "PROHIBITED IN THE UNIVERSITY BUILDINGS AND UPON UNIVERSITY GROUNDS WITHOUT PRIOR AUTHORIZATION OF "
                "THE CHANCELLOR.' 110.010.G.2 — 'Recognized student organizations may not solicit subscriptions or "
                "collect dues from prospective students or guests.' 110.010.E.4 — 'Use of available University "
                "facilities may be granted to nonstudent groups for meetings, programs and activities' where "
                "(a) 'the meeting, program and activity is sponsored by or the group is invited by an instructional "
                "or administrative division'; (b) it is 'sponsored by a learned, educational, professional, or "
                "scientific society for organizational or educational purposes... when recommended by a dean'; or "
                "(c) 'OTHER NONAFFILIATED AND NONSPONSORED GROUPS MAY MAKE USE OF THE FACILITIES... UPON WRITTEN "
                "APPROVAL OF THE CHANCELLOR.' 110.010.E.3 — 'Persons who are not current students or employees... "
                "without specific permission or authorization or without an appropriate purpose MAY BE DEEMED "
                "GUILTY OF TRESPASS' — the sentence that makes an unapproved presence a trespass question rather "
                "than a policy question. 110.010.D.2 — 'The organization file a written request for approval of the "
                "activity or program AT LEAST TEN DAYS PRIOR to the event'; 'The Chancellor is authorized to make "
                "an exception to the ten day rule in special circumstances.' 110.010.D.4 — 'Such groups may do so "
                "only by written permission of the Chancellor.' FEES: E.5 'Affiliated groups... may be charged an "
                "approved fee'; E.6 'NONAFFILIATED, NONSPONSORED GROUPS... WILL BE CHARGED A FEE APPROVED BY THE "
                "CHANCELLOR.' ⚠ NOTE WHAT CRR 110.010 DOES NOT CONTAIN: there is NO ANTI-FRONTING CLAUSE in the "
                "systemwide rule. Anti-fronting appears at CAMPUS level and only at one campus in this set — "
                "Missouri S&T. Whether UMKC has adopted one locally is UNKNOWN, because no UMKC campus policy could "
                "be retrieved at all. ⚠ WHAT IS MISSING AT UMKC, AND IT IS ALMOST EVERYTHING: the Student Union "
                "page publishes a reservations EMAIL (umkcsureservations@umkc.edu) but NO RESERVATIONS PHONE "
                "NUMBER, NO RATES, NO TABLING RULES AND NO EXTERNAL-GROUP TERMS; info.umkc.edu/studentunion/ "
                "302-redirects to umkc.edu/campus, which carries none of it either; and the Student Affairs offices "
                "index lists eleven offices with URLs but NO individual phone numbers. UMKC is PUBLIC and bound by "
                "RSMo s 173.1550 — outdoor areas are traditional public forums — but s 173.1550(3) protects only "
                "'NONCOMMERCIAL expressive activity,' so the statute does not carry DGD past the Chancellor's "
                "authorization requirement.",
  'sponsor_required': 'PROBABLY YES, in the systemwide sense — CRR 110.010.E.4 grants facility use to nonstudent '
                      'groups where they are "sponsored by or... invited by an instructional or administrative '
                      'division," or sponsored by a learned society on a dean\'s recommendation; only otherwise '
                      'does it fall to E.4.c\'s "written approval of the Chancellor" plus a Chancellor-approved '
                      'fee. A departmental invitation is therefore the cleanest UMKC route on the retrievable text. '
                      '⚠ But NO UMKC campus procedure could be retrieved, so whether UMKC has a local '
                      'anti-fronting rule (as Missouri S&T does) is UNKNOWN. Ask explicitly: (816) 235-1407 or '
                      '(816) 235-5555.',
  'clubs': [('⚠ NO UMKC STUDENT ORGANIZATION DIRECTORY COULD BE LOCATED',
             'The Office of Student Involvement page carries no organization directory URL at all, and no UMKC org '
             'platform was reached in this pass. Whether UMKC has a blockchain, crypto, fintech, investment or ACM '
             'club is COMPLETELY UNKNOWN — not searched and not ruled out. Ask the office directly at '
             '(816) 235-1407.',
             'https://www.umkc.edu/student-affairs/offices/student-involvement.html')],
  'faculty': [('⚠ Office of the Registrar (Administrative Center, Room 115)',
               'CALL THIS FIRST — UMKC IS THE ONE CAMPUS IN MISSOURI WHOSE FALL 2026 CALENDAR IS COMPLETELY '
               'UNKNOWN. The academic-calendar page returns an empty body and the catalog route returns navigation '
               'only. Not one UMKC date is confirmed. Office hours Mon–Fri 8 a.m.–5 p.m.',
               'Registrar',
               'registrar@umkc.edu · (816) 235-1125',
               'https://www.umkc.edu/registrar/'),
              ('⚠ Office of Student Involvement (Student Union, 5100 Cherry Street, Suite 320)',
               'Owns student organizations and any involvement fair — neither of which is published. Also the '
               'office to ask whether UMKC has a local solicitation procedure on top of CRR 110.010, and whether it '
               'has an anti-fronting rule. NO STAFF NAMES ARE PUBLISHED on the page.',
               'Student Involvement',
               'getinvolved@umkc.edu · (816) 235-1407',
               'https://www.umkc.edu/student-affairs/offices/student-involvement.html'),
              ('⚠ Student Union (5100 Cherry St., Ste. 320, Kansas City MO 64110)',
               'The building that would host a table. Ask them to route the reservations question, since the '
               'reservations function publishes an email but NO PHONE NUMBER. Event and Conference Services offers '
               '"multipurpose rooms, theaters, conference rooms, and outdoor areas."',
               'Student Union',
               '(816) 235-5555',
               'https://www.umkc.edu/student-affairs/offices/student-union.html'),
              ('Student Union — Event and Conference Services / reservations',
               '⚠ NO PHONE NUMBER IS PUBLISHED for the reservations function anywhere on umkc.edu — only this '
               'email. No rates, no tabling rules and no external-group terms are published either. Look up here; '
               'reach via the Student Union line.',
               'Student Union',
               'umkcsureservations@umkc.edu · no number published — look up here, or (816) 235-5555',
               'https://www.umkc.edu/campus'),
              ('Division of Student Affairs (Volker Campus, 5100 Rockhill Road)',
               'Escalation above Student Involvement. ⚠ NOTE: the Student Affairs offices index lists ELEVEN '
               'offices — Student Involvement, Student Union, Campus Recreation, Counseling Services, Roo Wellness '
               'Accessibility Services, Multicultural Student Affairs, Residential Life, Student Conduct and '
               'Civility, Roo Wellness, and Student Veteran Support Services — with URLs but NO INDIVIDUAL PHONE '
               'NUMBERS, and it lists NO DEAN OF STUDENTS OFFICE at all.',
               'Student Affairs',
               'umkccares@umkc.edu · (816) 235-1141',
               'https://www.umkc.edu/student-affairs/offices/index.html'),
              ('UMKC main line',
               'Operator, last resort — printed on umkc.edu/campus.',
               'University of Missouri–Kansas City',
               '(816) 235-1000 (MAIN LINE)',
               'https://www.umkc.edu/campus'),
              ('(Bloch School of Management / computer science faculty)',
               'NOT CONFIRMED — no UMKC faculty member could be confirmed on any relevant topic in this pass. No '
               'department directory was reached. Look up here; route via Student Affairs or the operator.',
               'University of Missouri–Kansas City',
               'no number published — look up here, or (816) 235-1000',
               'https://www.umkc.edu/')],
  'courses': [('(All UMKC courses)',
               'NOT CHECKED — the UMKC catalog (catalog.umkc.edu) was reached only at the index level and its '
               'course listings were not retrieved. No UMKC course could be verified for blockchain, crypto or '
               'fintech content in either direction. Gap.',
               'https://catalog.umkc.edu/')],
  'events': [('(All UMKC events)',
              'NOT RETRIEVED — no career fair, involvement fair, speaker series or hackathon could be confirmed at '
              'UMKC in this pass. Ask Student Involvement, (816) 235-1407.',
              'https://www.umkc.edu/student-affairs/offices/student-involvement.html')],
  'play': 'Kansas City is the one metro in Missouri with a single university stop in it, which makes UMKC either a '
          'worthwhile anchor for a western swing or a wasted day — and right now nobody can tell which, because '
          'UMKC IS THE ONLY CAMPUS IN THIS PACKET WHOSE FALL 2026 CALENDAR IS COMPLETELY UNKNOWN. The registrar\'s '
          'academic-calendar page RETURNS AN EMPTY BODY (confirmed twice), the catalog route returns navigation '
          'chrome with no dates, and five other URL variants 404. Not one UMKC date is confirmed. The three sibling '
          'UM campuses whose calendars were confirmed all start Mon Aug 24, 2026, and UMKC very likely matches — '
          'but that is a pattern, not a fact, and booking travel on it would be exactly the kind of guess that '
          'wastes a week. So: call (816) 235-1125 before anything else. On access, the good news is that the '
          'answer is already known at system level and does not depend on UMKC publishing anything: CRR 110.010 '
          'governs, "the sale of anything, the soliciting of subscriptions or the collection of dues is prohibited '
          '... without prior authorization of the Chancellor," and a nonaffiliated, nonsponsored group "may make '
          'use of the facilities... upon written approval of the Chancellor" and "will be charged a fee approved by '
          'the Chancellor." The cleanest route on that text is not the Chancellor at all — it is E.4.a, facility '
          'use where the group "is sponsored by or... invited by an instructional or administrative division." A '
          'departmental invitation converts DGD from a vendor into an invited guest. Beyond that, UMKC publishes '
          'almost nothing: the Student Union names a reservations email but NO PHONE, NO RATES, NO TABLING RULES '
          'and NO external-group terms; the Student Affairs index lists eleven offices with no direct numbers and '
          'no Dean of Students at all; and no organization directory could even be located, so whether a blockchain '
          'club exists here is unknown rather than absent. Three numbers do all the work: Registrar '
          '(816) 235-1125 for the calendar, Student Involvement (816) 235-1407 for clubs and any fair, Student '
          'Union (816) 235-5555 to be routed to whoever actually books a table.',
  'gaps': ['⚠⚠ THE ENTIRE FALL 2026 CALENDAR. umkc.edu/registrar/academic-calendar.html RETURNS AN EMPTY PAGE BODY '
           '(confirmed twice); catalog.umkc.edu/undergraduate-academic-regulations-information/academic-calendar/ '
           'returns navigation only; five other URL variants 404. Not one date is confirmed. (816) 235-1125.',
           '⚠⚠ ANY UMKC-SPECIFIC SOLICITATION, TABLING OR VENDOR POLICY. None could be retrieved; CRR 110.010 is '
           'all that is known. Whether UMKC has a local anti-fronting rule (as Missouri S&T does) is UNKNOWN. '
           '(816) 235-1407.',
           '⚠ A PHONE NUMBER FOR THE STUDENT UNION RESERVATIONS FUNCTION — an email is published but no number. No '
           'rates, no tabling rules and no external-group terms appear anywhere. (816) 235-5555.',
           '⚠ The "fee approved by the Chancellor" under CRR 110.010.E.6 — a fee exists in principle and its amount '
           'is published nowhere.',
           '⚠ Whether UMKC holds a fall involvement fair at all. Nothing published. (816) 235-1407.',
           '⚠ No UMKC student organization directory could even be LOCATED — not JavaScript-blocked, simply not '
           'linked from the Student Involvement page. Whether a blockchain or fintech club exists is unknown.',
           'No UMKC faculty member could be confirmed on any topic; no department directory was reached.',
           'No UMKC course listing was retrieved — no course could be checked.',
           'The Student Affairs offices index lists NO DEAN OF STUDENTS OFFICE. Confirm who performs that function '
           'and get a direct number. (816) 235-1141.'],
  'note': 'UMKC is one of the four UM System campuses governed by CRR 110.010 — the full systemwide text is quoted '
          'in both the Mizzou and UMKC records because at UMKC it is the ONLY policy available. Kansas City holds '
          'no other campus in this packet, so a UMKC stop stands or falls on its own.'},

 # ---------------------------------------------------------------- 7. UMSL
 {'state': 'Missouri',
  'name': 'University of Missouri–St. Louis',
  'city': 'St. Louis, MO',
  'type': 'Public',
  'tier': 'C — Opportunistic',
  'access': 3,
  'start': 'Mon Aug 24, 2026 — classes begin 8:00 a.m.',
  'adddrop': 'Last day any student may enroll (enter a course for credit): Sun Aug 30, 2026.',
  'fallbreak': 'Begins 12:00 a.m. Thu Oct 8, 2026; classes resume Mon Oct 12, 2026.',
  'thanksgiving': 'Begins 5:00 p.m. Sat Nov 21, 2026; classes resume 8:00 a.m. Mon Nov 30, 2026 — a nine-day '
                  'absence, matching Mizzou\'s.',
  'lastclass': 'Classes end 5:00 p.m. Sat Dec 12, 2026 — the latest last-class date in Missouri.',
  'finals': 'Begin Mon Dec 14, 2026; the fall semester closes Sat Dec 19, 2026.',
  'cal_url': 'https://www.umsl.edu/registration/resources/students/semester-calendars-important-dates.html',
  'cal_status': 'CONFIRMED on UMSL\'s semester calendars page, which prints weekdays and times for every entry '
                '("August 24 … Monday … Classes begin 8:00 a.m."). SEMESTERS. The page displays Fall 2026 alongside '
                'Spring 2026 and Summer 2026.',
  'fair': 'Weeks of Welcome — no involvement fair is separately named or dated',
  'fair_date': '⚠ UNVERIFIED — the Office of Student Involvement page references "Weeks of Welcome" orientation '
               'activities for new students but names NO involvement fair and gives NO date, time, location, cost '
               'or eligibility rule. Call (314) 516-5291.',
  'fair_outside': 'UNVERIFIED for the fair itself. The campus-wide answer is clear and negative for commercial '
                  'actors: outdoor activities may not "Involve solicitations or promotion of commercial '
                  'enterprises," and the distribution permission is limited to "NON-COMMERCIAL pamphlets, '
                  'handbills, circulars, newspapers, magazines and other written materials."',
  'fair_cost': 'UNVERIFIED — no UMSL rate card was found. Under CRR 110.010.E.6, "Nonaffiliated, nonsponsored '
               'groups... will be charged a fee approved by the Chancellor"; the amount is published nowhere.',
  'fair_deadline': 'UNVERIFIED. CRR 110.010.D.2 sets a ten-day floor where a student organization is the requester. '
                   'The UMSL free-speech guidelines contain NO advance-notice or reservation requirement at all — a '
                   'notable absence on a page telling people how to exercise a right.',
  'fair_url': 'https://www.umsl.edu/studentinvolvement/index.html',
  'policy': 'UMSL Campus Free Speech Guidelines — which expressly defer to UM System Collected Rules and '
            'Regulations 110.010 for facilities, solicitation and sales',
  'policy_url': 'https://www.umsl.edu/free-speech.html',
  'policy_key': "UMSL Campus Free Speech Guidelines (umsl.edu/free-speech.html) — the cleanest single illustration "
                "in Missouri of how the state's structure actually works: the outdoor forum is genuinely open to "
                "the public, and COMMERCIAL SOLICITATION IS CARVED STRAIGHT OUT OF IT. Verbatim: 'THE OUTDOOR AREAS "
                "OF UMSL HAVE BEEN DEEMED A TRADITIONAL PUBLIC FORUM. THEREFORE, MEMBERS OF THE PUBLIC ARE FREE TO "
                "EXERCISE EXPRESSIVE ACTIVITIES OUTDOORS.' Then the carve-out — activities may not 'INVOLVE "
                "SOLICITATIONS OR PROMOTION OF COMMERCIAL ENTERPRISES.' And the distribution rule, whose adjective "
                "is the whole point: 'NON-COMMERCIAL pamphlets, handbills, circulars, newspapers, magazines and "
                "other written materials may be distributed on a person-to-person basis.' Placement: 'Remain 20 "
                "feet from entrances/exits.' And the referral that decides the question: 'POLICIES RELATED TO USE "
                "OF FACILITIES, INCLUDING FOR SOLICITATION OR SALES ARE OUTLINED IN THE COLLECTED RULES AND "
                "REGULATIONS (CRR 110.010).' So UMSL points straight back at the systemwide rule, whose operative "
                "terms are: 110.010.G.1 'The sale of anything, the soliciting of subscriptions or the collection of "
                "dues is prohibited in the University buildings and upon University grounds WITHOUT PRIOR "
                "AUTHORIZATION OF THE CHANCELLOR'; 110.010.E.4.c 'Other nonaffiliated and nonsponsored groups may "
                "make use of the facilities... UPON WRITTEN APPROVAL OF THE CHANCELLOR'; 110.010.E.4.a facility use "
                "where the activity 'is sponsored by or the group is invited by an instructional or administrative "
                "division'; 110.010.E.3 non-students present 'without specific permission or authorization or "
                "without an appropriate purpose MAY BE DEEMED GUILTY OF TRESPASS'; 110.010.E.6 'Nonaffiliated, "
                "nonsponsored groups... WILL BE CHARGED A FEE APPROVED BY THE CHANCELLOR.' Full CRR text is quoted "
                "in the Mizzou and UMKC records. ⚠ ABSENCES — verified-not-found, NOT verified-permitted: the UMSL "
                "guidelines contain NO ANTI-FRONTING CLAUSE, NO advance-notice or reservation requirement, NO "
                "insurance provision, NO deposit or cancellation terms, and NOTHING reaching payment credentials or "
                "on-site contracts. ⚠ AND A TELLING OMISSION WORTH NOTING: THE FREE-SPEECH PAGE PUBLISHES NO OFFICE "
                "NAME, NO EMAIL AND NO DIRECT PHONE NUMBER — only the campus switchboard (314) 516-5000 and the "
                "admissions toll-free line. A page explaining how to exercise a right names nobody to ask. UMSL is "
                "PUBLIC and bound by RSMo s 173.1550, and the guidelines plainly implement it — but s 173.1550(3) "
                "protects only 'NONCOMMERCIAL expressive activity,' which is precisely the line UMSL has drawn on "
                "its own page.",
  'sponsor_required': 'EFFECTIVELY YES. UMSL publishes no local procedure, so CRR 110.010 controls: a nonaffiliated '
                      'nonsponsored group needs "written approval of the Chancellor" plus a Chancellor-approved '
                      'fee, whereas a group "sponsored by or... invited by an instructional or administrative '
                      'division" (110.010.E.4.a) is admitted on the division\'s authority. A department or faculty '
                      'invitation is far the cheaper route. No anti-fronting clause was found at UMSL — but absence '
                      'of published text is not permission; confirm at (314) 516-5291.',
  'clubs': [('⚠ Triton Connect — PARTIALLY READABLE, 169 groups, only a fraction loaded',
             'The directory (tritonconnect.umsl.edu/club_signup) is JAVASCRIPT-RENDERED — the page shows "Loading…" '
             'indicators and a "Load all 169 groups" control — but unlike every other Missouri directory, a partial '
             'list did surface. NO BLOCKCHAIN, CRYPTO, BITCOIN OR WEB3 ORGANIZATION APPEARED, and no dedicated '
             'computer science, data science, ACM, economics, entrepreneurship or investment club appeared either. '
             '⚠ THIS IS PARTIAL, NOT EXHAUSTIVE — only a fraction of the 169 groups rendered. Treat as suggestive, '
             'not conclusive.',
             'https://tritonconnect.umsl.edu/club_signup'),
            ('Accounting Club',
             'Confirmed present in the partial Triton Connect listing. Closest business-side audience surfaced at '
             'UMSL. No officer names, emails or phone numbers are published; do not guess officers.',
             'https://tritonconnect.umsl.edu/club_signup'),
            ('Beta Alpha Psi – Gamma Psi',
             'Business and finance honour society — confirmed present in the partial listing. Honour societies '
             'have faculty advisors, which are more stable contacts than student officers; the advisor is not '
             'named on the directory. Ask Student Involvement, (314) 516-5291.',
             'https://tritonconnect.umsl.edu/club_signup'),
            ('Other confirmed UMSL organizations (lower fit)',
             'UMSL Esports; American Institute of Graphic Arts; Chess Club; Biological Society; Chemistry Club. '
             'All confirmed present in the partial Triton Connect listing. UMSL claims "90+ student organizations" '
             'on the Student Involvement page while the directory control says "Load all 169 groups" — a minor '
             'internal inconsistency, not material.',
             'https://www.umsl.edu/studentinvolvement/index.html')],
  'faculty': [('⚠ Office of Student Involvement (366 Millennium Student Center, 17 Arnold B. Grobman Dr.)',
               'THE ONLY SUBSTANTIVE NUMBER AT UMSL. Owns Triton Connect, the 90+ (or 169) organizations and Weeks '
               'of Welcome. Also the office to ask what the free-speech page conspicuously does not say: who '
               'approves an outside group, whether UMSL has any anti-fronting rule, and what the '
               'Chancellor-approved fee actually is. The page points to a "Meet Our Staff" directory but NAMES NO '
               'INDIVIDUAL STAFF.',
               'Student Involvement',
               'studentinvolvement@umsl.edu · (314) 516-5291',
               'https://www.umsl.edu/studentinvolvement/index.html'),
              ('Office of Registration',
               'Confirmed the Fall 2026 dates above. Also handles transcripts (onlinetranscript@umsl.edu).',
               'Registration',
               'registration@umsl.edu · (314) 516-5545',
               'https://www.umsl.edu/registration/'),
              ('⚠ UMSL Campus Free Speech Guidelines — NO OFFICE, NO EMAIL, NO DIRECT NUMBER',
               'The page that sets out who may speak outdoors and what commercial activity is excluded PUBLISHES NO '
               'RESPONSIBLE OFFICE, NO EMAIL AND NO DIRECT PHONE — only the campus switchboard and the admissions '
               'toll-free line ((888) GO-2-UMSL). That is a real gap: there is nobody named to ask. Start at '
               'Student Involvement instead.',
               'University of Missouri–St. Louis',
               'no office or number published — look up here; switchboard (314) 516-5000 (MAIN LINE)',
               'https://www.umsl.edu/free-speech.html'),
              ('UMSL main line',
               'Operator, last resort — the only number on the free-speech page.',
               'University of Missouri–St. Louis',
               '(314) 516-5000 (MAIN LINE)',
               'https://www.umsl.edu/free-speech.html'),
              ('(Blockchain / finance / fintech faculty)',
               'NOT CONFIRMED — no UMSL faculty member could be confirmed on any relevant topic in this pass. No '
               'College of Business Administration or computer science directory was reached. Look up here; route '
               'via Student Involvement.',
               'University of Missouri–St. Louis',
               'no number published — look up here, or (314) 516-5291',
               'https://www.umsl.edu/')],
  'courses': [('(All UMSL courses)',
               'NOT CHECKED — no UMSL catalog or course-search page was reached in this pass. No course could be '
               'verified for blockchain, crypto or fintech content in either direction. Gap.',
               'https://www.umsl.edu/')],
  'events': [('(All UMSL events)',
              'NOT RETRIEVED — beyond a reference to "Weeks of Welcome," no career fair, involvement fair, speaker '
              'series or hackathon could be confirmed at UMSL in this pass. Ask Student Involvement, '
              '(314) 516-5291.',
              'https://www.umsl.edu/studentinvolvement/index.html')],
  'play': 'UMSL is the cheapest stop in Missouri and the clearest statement of what the state actually permits, '
          'which makes it useful for calibration even though it is a thin destination on its own. It sits about '
          'twenty minutes from both WashU and SLU, so it costs an hour rather than a day, and it runs LATER THAN '
          'ANY OTHER MISSOURI CAMPUS — classes end 5:00 p.m. Sat Dec 12 with finals to Dec 19 — so it is the last '
          'usable stop in the state if a December window is needed. Read the free-speech page before going, because '
          'UMSL has written the answer down more plainly than anyone else: "The outdoor areas of UMSL have been '
          'deemed a traditional public forum. Therefore, members of the public are free to exercise expressive '
          'activities outdoors" — and in the next breath, activities may not "involve solicitations or promotion of '
          'commercial enterprises," with distribution limited to "NON-COMMERCIAL pamphlets, handbills, circulars, '
          'newspapers, magazines and other written materials." An ambassador can stand outdoors at UMSL and talk; '
          'he cannot pitch and cannot hand out DGD literature. For anything more the page defers explicitly to CRR '
          '110.010, which means Chancellor-level written approval and a Chancellor-approved fee — unless the visit '
          'comes in under 110.010.E.4.a, "sponsored by or... invited by an instructional or administrative '
          'division," which is by far the cheaper door and the one to pursue. One number does the work: Student '
          'Involvement, (314) 516-5291. Ask them who approves an outside group, what the fee is, whether UMSL has '
          'an anti-fronting rule, and whether Weeks of Welcome includes a fair at all — because the free-speech '
          'page itself names NO office, NO email and NO direct phone, which is a genuine gap on a page whose whole '
          'purpose is telling people how to exercise a right. On clubs, UMSL was the only Missouri directory that '
          'partially rendered: no blockchain or crypto club appeared, and the best fits surfaced are the Accounting '
          'Club and Beta Alpha Psi – Gamma Psi — but only a fraction of the 169 groups loaded, so treat that as '
          'suggestive rather than settled.',
  'gaps': ['⚠ WHO APPROVES AN OUTSIDE GROUP AT UMSL, AND WHAT THE FEE IS. The free-speech page defers to CRR '
           '110.010 without naming an office, and CRR 110.010.E.6\'s "fee approved by the Chancellor" is published '
           'nowhere. (314) 516-5291.',
           '⚠ THE FREE-SPEECH PAGE PUBLISHES NO OFFICE NAME, NO EMAIL AND NO DIRECT PHONE NUMBER — only the '
           'switchboard. There is nobody named to ask. https://www.umsl.edu/free-speech.html',
           '⚠ Whether UMSL has an anti-fronting rule or any local solicitation procedure on top of CRR 110.010 — '
           'none was found, and absence of published text is not permission. (314) 516-5291.',
           '⚠ Whether Weeks of Welcome includes an involvement fair, and its date, cost and eligibility. Nothing '
           'published. (314) 516-5291.',
           '⚠ Triton Connect is JAVASCRIPT-RENDERED and only a fraction of 169 groups loaded — the absence of a '
           'blockchain or fintech club is SUGGESTIVE, NOT PROVEN. Also note the internal inconsistency: the '
           'Student Involvement page says "90+ student organizations" while the directory offers to "Load all 169 '
           'groups."',
           'No UMSL faculty member could be confirmed on any topic; no business or CS department directory was '
           'reached.',
           'No UMSL course catalog was reached — no course could be checked.',
           'No UMSL career fair, speaker series or hackathon could be confirmed.',
           'No advance-notice or reservation requirement appears anywhere in the UMSL free-speech guidelines — an '
           'absence, not a permission. Confirm the actual lead time by phone.'],
  'note': 'UMSL is one of the four UM System campuses governed by CRR 110.010; the full systemwide text is quoted '
          'in the Mizzou and UMKC records. Of the three campuses in the St. Louis cluster UMSL is the only public '
          'one, so it is the only one where RSMo s 173.1550 applies at all — and even there the statute\'s '
          'noncommercial limiter means it changes nothing for DGD.'},

 # ---------------------------------------------------------------- 8. TRUMAN STATE
 {'state': 'Missouri',
  'name': 'Truman State University',
  'city': 'Kirksville, MO',
  'type': 'Public',
  'tier': 'C — Opportunistic',
  'access': 3,
  'start': '⚠ Mon Aug 17, 2026 — first wave, a week ahead of the Aug 24 group.',
  'adddrop': '⚠ NOT PRINTED on the 2026-27 academic calendar. The calendar gives term boundaries, breaks and '
             'block-course dates but no add/drop deadlines. Call (660) 785-4000.',
  'fallbreak': '⚠ Midterm break Thu–Fri Oct 8–9, 2026 — AND NOTE THE BLOCK BOUNDARY IMMEDIATELY BEFORE IT: FIRST '
               'BLOCK COURSES CONCLUDE TUE OCT 6, 2026. Truman is the one campus in this set where a sub-term '
               'boundary sits inside the tour window, and student attention resets there.',
  'thanksgiving': 'Mon–Fri Nov 23–27, 2026',
  'lastclass': 'Last day of instruction Fri Dec 4, 2026',
  'finals': 'Finals start Mon Dec 7, 2026; reading day Wed Dec 9; exams end Fri Dec 11. Commencement Sat Dec 12, '
            '11 a.m.',
  'cal_url': 'https://www.truman.edu/majors-programs/academic-resources/academic-calendar-schedules/academic-calendar/2026-27-academic-calendar/',
  'cal_status': 'CONFIRMED on Truman\'s published 2026-27 academic calendar, which prints weekdays for every entry '
                '("Monday, August 17", "Thursday-Friday, October 8-9", "Monday-Friday, November 23-27", "Finals '
                'Start Monday, December 7", "Reading Day Wednesday, December 9"). SEMESTERS, with BLOCK COURSES '
                'inside the term. The registrar page warns "Academic Calendars are subject to change."',
  'fair': 'Activities fair — NOT PUBLISHED',
  'fair_date': '⚠ UNVERIFIED — no fall activities fair, org fair or welcome-week tabling event is published on any '
               'retrievable Truman page. Union & Involvement Services describes itself as "the programmatic branch '
               'of the Student Union" but names no fair. Call (660) 785-4222 or email orgs@truman.edu.',
  'fair_outside': 'UNVERIFIED for the fair. The campus-level answer is unusually permissive on the retrievable '
                  'text: Board Chapter 12.010 provides that "Other persons and groups may use University '
                  'facilities on a space available basis" — with no solicitation or commercial ban found anywhere '
                  'in the Code.',
  'fair_cost': 'UNVERIFIED — no rate card exists on any retrievable page. Chapter 12.010 refers only to "possible '
               'rental fees, established by the President," with no schedule published. (660) 785-4222.',
  'fair_deadline': 'UNVERIFIED — no advance-notice requirement appears anywhere in Chapter 12 or in the Campus '
                   'Protests policy. That is an absence, not a permission; confirm the real lead time by phone.',
  'fair_url': 'https://involvement.truman.edu/',
  'policy': 'Truman State University Board of Governors Code of Policies, Chapter 12 — "Facilities – Uses and '
            'Priorities" (chapter revised August 2, 2014; facilities-use provisions carry a "1987 Compilation '
            '(Established practice)" citation); alongside it the Campus Protests policy',
  'policy_url': 'https://c3c5e312.delivery.rocketcdn.me/wp-content/uploads/2014/02/CHAPTER-12-REVISED-August-2-2014.pdf',
  'policy_key': "Truman State Board of Governors Code of Policies, CHAPTER 12 'FACILITIES – USES AND PRIORITIES' "
                "(chapter revised August 2, 2014; the facilities-use provisions cite '1987 Compilation (Established "
                "practice)'). Verbatim: 12.010 — 'University buildings and grounds are intended for use by faculty, "
                "staff, and students for educational, administrative, and recreational purposes, and SUCH USES HAVE "
                "THE HIGHEST PRIORITY.' 12.010 — ⚠ THE OPERATIVE SENTENCE, AND THE MOST PERMISSIVELY WORDED PUBLIC "
                "PROVISION IN THIS PACKET: 'OTHER PERSONS AND GROUPS MAY USE UNIVERSITY FACILITIES ON A SPACE "
                "AVAILABLE BASIS' — 'in accordance with the policies and procedures, INCLUDING POSSIBLE RENTAL "
                "FEES, established by the President.' 12.020.1(3) — outside speakers may come as 'Speakers invited "
                "by the faculty sponsor and president of a university-chartered organization.' 12.020.2 — 'Speakers "
                "invited by faculty sponsor and president of a chartered student organization SHALL ALSO BE THE "
                "RESPONSIBILITY OF THE MEMBERSHIP OF THAT CHARTERED ORGANIZATION' — note the invitation route "
                "requires BOTH the faculty sponsor AND the chapter president, and it puts the liability on the "
                "students, which is a reason to be scrupulous with them. ⚠⚠ NOTABLE ABSENCES — ALL "
                "VERIFIED-NOT-FOUND, NOT VERIFIED-PERMITTED, AND THE REASON THIS CAMPUS IS RATED 3 RATHER THAN 1: "
                "Chapter 12 CONTAINS NO SOLICITATION CLAUSE, NO SALES CLAUSE, NO COMMERCIAL-ACTIVITY BAN, NO "
                "ANTI-FRONTING CLAUSE, NO INSURANCE PROVISION AND NO DEPOSIT OR CANCELLATION TERMS that could be "
                "found. The companion Campus Protests policy (c3c5e312.delivery.rocketcdn.me/wp-content/uploads/"
                "2014/11/Campus-Protests.pdf) is a general First Amendment and civility statement — it 'discusses "
                "First Amendment rights generally but doesn't explicitly state who is permitted to protest on "
                "campus,' and contains NO commercial provision, NO advance-notice or permit procedure, NO "
                "designated-area rule and NO phone numbers. ⚠ AND TRUMAN SAYS SO ITSELF: its policy index carries "
                "the disclaimer 'This webpage does not contain an exhaustive list of university policies' and "
                "directs enquiries to the Institutional Compliance Office. SO THE RATE CARD AND THE OPERATING "
                "PROCEDURE UNDER 12.010 EXIST SOMEWHERE AND WERE NOT FOUND. Rated 3, not 4, purely because no rate, "
                "no form and no procedure could be produced — the WORDING would otherwise support 4. Truman is "
                "PUBLIC and bound by RSMo s 173.1550, whose s 2 deems outdoor areas traditional public forums; but "
                "s 173.1550(3) protects only 'NONCOMMERCIAL expressive activity,' so the statute adds nothing for "
                "DGD beyond what 12.010 already says more generously.",
  'sponsor_required': 'NO ON THE RETRIEVABLE TEXT — and that is what makes Truman unusual. Chapter 12.010 admits '
                      '"Other persons and groups... on a space available basis" in their own right, subject to '
                      '"possible rental fees," and NO anti-fronting clause and NO no-sponsorship clause could be '
                      'found anywhere in the Code. A second, cleaner route also exists under 12.020.1(3): a speaker '
                      '"invited by the faculty sponsor AND president of a university-chartered organization" — note '
                      'it requires both, and 12.020.2 places responsibility on the chapter\'s membership. Confirm '
                      'the absence of a solicitation rule explicitly at (660) 785-4222 before relying on it; '
                      'absence of published text is not permission.',
  'clubs': [('⚠ THE ONLY FULLY READABLE ORGANIZATION DIRECTORY IN MISSOURI',
             'Truman publishes a STATIC, NON-JAVASCRIPT organization list with faculty advisors and student '
             'contacts — the only one of the nine campuses where the directory could actually be read. Six other '
             'Missouri directories (MU Engage, WUGO, MinerLink, SLU Groups, Missouri State Presence, Engage SEMO) '
             'are JavaScript-rendered or errored out. ⚠ NO BLOCKCHAIN, CRYPTO, BITCOIN OR WEB3 ORGANIZATION IS '
             'LISTED — and at Truman that is a genuine verified absence rather than a tooling failure. ⚠ The '
             'directory also publishes STUDENT OFFICER NAMES AND EMAILS. They were read from a live page and are '
             'real, but ROSTERS ROTATE EVERY YEAR AND THEY WILL BE STALE BY SEPTEMBER — use the faculty advisors '
             'below, who are staff and stable. No phone number is published for any advisor or any club.',
             'https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/'),
            ('⚠ Bulldog Student Investment Fund (BSIF)',
             'THE HIGHEST-FIT STUDENT GROUP CONFIRMED ANYWHERE IN MISSOURI. Verbatim from the directory: it '
             '"manages $200,000 of the university\'s endowment funds, strategically investing in stocks and passive '
             'vehicles every semester." Real money, a real mandate and a named stable advisor. FACULTY ADVISOR: '
             'Sunghan Bae, sbae@truman.edu. No phone published for the advisor or the club.',
             'https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/'),
            ('Society of Actuaries at Truman State University (SATSU)',
             'Quantitative finance audience. Faculty advisor Steven Smith, sjsmith@truman.edu. The club runs its '
             'own site at satsu.truman.edu.',
             'https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/'),
            ('Beta Alpha Psi',
             '"Accounting and Business fraternity aimed at helping members develop their professional skillset." '
             'Faculty advisor Liz Diers, lizdiers@truman.edu.',
             'https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/'),
            ('Association for Computing Machinery (ACM)',
             'The technical audience at Truman. Faculty advisor Kafi Rahman, kafi@truman.edu.',
             'https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/'),
            ('Google Developer Group (GDG)',
             'Second technical club — a developer group is a natural fit for a protocol conversation. Faculty '
             'advisor Nazmul Shahadat, nshahadat@truman.edu.',
             'https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/'),
            ('Community of College Entrepreneurs (CCE)',
             'Entrepreneurship audience. Faculty advisor Yung-hwal Park, yhpark@truman.edu.',
             'https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/')],
  'faculty': [('⚠ Union & Involvement Services (Student Union Building, Room 2000, main level)',
               'THE ONE NUMBER THAT MATTERS AT TRUMAN. Described as "the programmatic branch of the Student Union," '
               'it owns the organizations, the building and whatever activities fair exists. It is also the office '
               'to ask for the two things Chapter 12 refers to but does not print: the RENTAL RATE and the '
               'OPERATING PROCEDURE "established by the President" under 12.010 — and to confirm explicitly that '
               'there is no solicitation rule, no anti-fronting rule and no insurance requirement, since none could '
               'be found. NO STAFF NAMES ARE PUBLISHED on the page.',
               'Union & Involvement Services',
               'orgs@truman.edu · (660) 785-4222',
               'https://involvement.truman.edu/'),
              ('Truman State University main line / Registrar',
               'The registrar publishes no direct number — the academic-calendar page gives only this switchboard, '
               'and so does the student-life index. Use it to reach the Registrar for add/drop deadlines and the '
               'Institutional Compliance Office for the policies Truman admits are not all on the web.',
               'Truman State University',
               '(660) 785-4000 (MAIN LINE)',
               'https://www.truman.edu/registrar/academic-calendar/'),
              ('⚠ Sunghan Bae',
               'FACULTY ADVISOR, BULLDOG STUDENT INVESTMENT FUND — the club that manages $200,000 of Truman\'s '
               'endowment. THE BEST SINGLE ACADEMIC/CLUB DOOR CONFIRMED IN MISSOURI, and a faculty sponsor is '
               'exactly what Chapter 12.020.1(3) requires for an invited speaker. Advisors are staff and stable, '
               'unlike student officers. NO PHONE IS PUBLISHED — email, or reach via (660) 785-4222.',
               'Bulldog Student Investment Fund',
               'sbae@truman.edu · no number published — look up here, or (660) 785-4222',
               'https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/'),
              ('Kafi Rahman',
               'Faculty advisor, Association for Computing Machinery — the technical door at Truman. No phone '
               'published.',
               'Association for Computing Machinery',
               'kafi@truman.edu · no number published — look up here, or (660) 785-4222',
               'https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/'),
              ('Nazmul Shahadat',
               'Faculty advisor, Google Developer Group — a developer audience already primed for a protocol talk. '
               'No phone published.',
               'Google Developer Group',
               'nshahadat@truman.edu · no number published — look up here, or (660) 785-4222',
               'https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/'),
              ('Steven Smith · Liz Diers · Yung-hwal Park',
               'Faculty advisors respectively to the Society of Actuaries (sjsmith@truman.edu), Beta Alpha Psi '
               '(lizdiers@truman.edu) and the Community of College Entrepreneurs (yhpark@truman.edu). NO PHONE IS '
               'PUBLISHED FOR ANY OF THEM — the directory prints emails only. Reach via Union & Involvement '
               'Services.',
               'Truman State University',
               'no numbers published — look up here, or (660) 785-4222',
               'https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/'),
              ('(Blockchain / fintech faculty)',
               'NOT CONFIRMED — no Truman faculty member working on blockchain, cryptocurrency or digital assets '
               'could be confirmed. The confirmed advisors above teach finance, actuarial science, accounting and '
               'computer science; DO NOT REPRESENT ANY OF THEM AS A CRYPTO RESEARCHER. Look up here.',
               'Truman State University',
               'no number published — look up here, or (660) 785-4000',
               'https://www.truman.edu/directory')],
  'courses': [('(All Truman State courses)',
               'NOT CHECKED — no Truman catalog or course-search page was reached in this pass. No course could be '
               'verified for blockchain, crypto or fintech content in either direction. Gap.',
               'https://www.truman.edu/')],
  'events': [('(All Truman State events)',
              'NOT RETRIEVED — no career fair, activities fair, speaker series or hackathon could be confirmed at '
              'Truman in this pass. Ask Union & Involvement Services, (660) 785-4222.',
              'https://involvement.truman.edu/'),
             ('⚠ Block-course boundary, Tue Oct 6, 2026',
              'Not an event but a scheduling fact worth treating as one: first block courses conclude Oct 6 and '
              'midterm break follows immediately, Thu–Fri Oct 8–9. Truman is the only campus in this set with a '
              'sub-term boundary inside the tour window. Schedule either side of it, not across it.',
              'https://www.truman.edu/majors-programs/academic-resources/academic-calendar-schedules/academic-calendar/2026-27-academic-calendar/')],
  'play': 'Kirksville is the most isolated stop in Missouri and the most promising one on paper, which is an '
          'uncomfortable combination — but the paper is genuinely good, so it is worth a phone call before it is '
          'written off. Two things make Truman different. First, the policy: the Board of Governors Code, Chapter '
          '12.010, says "Other persons and groups may use University facilities on a space available basis" subject '
          'to "possible rental fees, established by the President," and NO solicitation clause, NO sales clause, NO '
          'commercial-activity ban and NO anti-fronting clause could be found anywhere in the Code. That is the '
          'most permissively worded public provision in this entire packet. It is rated 3 rather than 4 only '
          'because no rate, no form and no procedure could be produced — and because Truman\'s own policy index '
          'admits "This webpage does not contain an exhaustive list of university policies," which means the '
          'missing procedure exists somewhere. Second, the clubs: Truman is THE ONLY CAMPUS IN MISSOURI whose '
          'organization directory is readable at all — static HTML, faculty advisors named — and it surfaces the '
          'best single target in the state, the BULLDOG STUDENT INVESTMENT FUND, which "manages $200,000 of the '
          'university\'s endowment funds, strategically investing in stocks and passive vehicles every semester," '
          'advised by Sunghan Bae (sbae@truman.edu). That matters doubly because Chapter 12.020.1(3) admits '
          'speakers "invited by the faculty sponsor AND president of a university-chartered organization" — a '
          'faculty-sponsored invitation from BSIF is a clean, cheap, non-commercial route in, and ACM (Kafi Rahman) '
          'and the Google Developer Group (Nazmul Shahadat) give two more. Note that 12.020.2 puts responsibility '
          'on the chapter\'s membership, so be scrupulous with the students who sign for you. One caution on the '
          'directory: it also prints student officer names and emails, and those rotate annually and will be stale '
          'by September — use advisors, not officers. Make one call to Union & Involvement Services, '
          '(660) 785-4222, ask for the rental rate and the President\'s operating procedure under 12.010, and '
          'confirm explicitly that no solicitation or anti-fronting rule exists. On calendar: Truman started Aug '
          '17, block courses end Oct 6 with midterm break right behind them Oct 8–9, and instruction ends Dec 4 — '
          'so aim at late September or the second half of October, not at the Oct 6–9 seam.',
  'gaps': ['⚠⚠ THE RENTAL RATE AND THE OPERATING PROCEDURE UNDER CHAPTER 12.010. The Code refers to "possible '
           'rental fees, established by the President" but publishes no schedule, no form and no procedure. '
           '(660) 785-4222.',
           '⚠ CONFIRM THE ABSENCES EXPLICITLY. No solicitation clause, no sales clause, no commercial-activity ban, '
           'no anti-fronting clause, no insurance provision and no deposit or cancellation terms could be found in '
           'Chapter 12 — but Truman\'s policy index states "This webpage does not contain an exhaustive list of '
           'university policies." Absence of published text is not permission. (660) 785-4222.',
           '⚠ Whether Truman holds a fall activities fair at all, and its date, cost and outside-org eligibility. '
           'Nothing published. (660) 785-4222 or orgs@truman.edu.',
           '⚠ NO PHONE NUMBER IS PUBLISHED FOR ANY TRUMAN FACULTY ADVISOR — the organization directory prints '
           'emails only, and the registrar publishes no direct line either. Only two numbers exist for this whole '
           'campus.',
           'Fall 2026 add/drop deadlines are not printed on the 2026-27 academic calendar. (660) 785-4000.',
           'No Truman course catalog was reached — no course could be checked for blockchain or fintech content.',
           'No Truman career fair, speaker series or hackathon could be confirmed.',
           'The Institutional Compliance Office (titleix.truman.edu) is named as the route to policies not on the '
           'web — worth a call if Union & Involvement Services cannot produce the 12.010 procedure.'],
  'note': 'Kirksville is roughly two hours north of Columbia and three and a half from St. Louis, with nothing else '
          'in this packet nearby — the most isolated stop in Missouri. It only justifies the drive if the BSIF or '
          'ACM invitation route lands first; do not go there speculatively. Truman is also the campus where the '
          'RESEARCH is strongest and the CONTACT DATA is weakest: the only readable club directory in the state, '
          'and only two phone numbers on the entire campus.'},

 # ---------------------------------------------------------------- 9. SEMO
 {'state': 'Missouri',
  'name': 'Southeast Missouri State University',
  'city': 'Cape Girardeau, MO',
  'type': 'Public',
  'tier': 'C — Opportunistic',
  'access': 3,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'Full-semester courses: last day to add Fri Aug 28, 2026; last day to drop Fri Nov 20, 2026. First '
             'Eight-Week session: add by Wed Aug 26, drop by Fri Sep 25. A Second Eight-Week session runs '
             'concurrently with its own deadlines.',
  'fallbreak': 'Thu–Fri Oct 8–9, 2026 — part of the Oct 8–12 cluster that takes five Missouri campuses dark in the '
               'same week.',
  'thanksgiving': 'Wed–Fri Nov 25–27, 2026 — the SHORTEST Thanksgiving break in the state, three days against '
                  'nine at Mizzou, S&T, UMSL and Missouri State.',
  'lastclass': 'Not separately printed; finals begin Mon Dec 14, 2026, so instruction runs to about Fri Dec 11.',
  'finals': 'Mon–Fri Dec 14–18, 2026 — SEMO is among the last three campuses in Missouri still in session in '
            'December, alongside Mizzou and UMSL.',
  'cal_url': 'https://semo.edu/student-support/academic-support/registrar/academic-calendar',
  'cal_status': 'CONFIRMED on SEMO\'s academic calendar, which prints weekdays for every entry ("Mon. Aug. 24", '
                '"Thu.-Fri. Oct. 08-09", "Wed.-Fri. Nov. 25-27", "Mon.-Fri. Dec. 14-18"). SEMESTERS, with '
                'concurrent FIRST EIGHT-WEEK and SECOND EIGHT-WEEK sessions carrying their own add/drop deadlines '
                'alongside full-semester courses. The last day of classes is not separately printed — confirm at '
                '(573) 651-2250.',
  'fair': 'Involvement fair — NOT PUBLISHED',
  'fair_date': '⚠ UNVERIFIED — no fall involvement fair, org fair or welcome-week tabling event is published on any '
               'retrievable SEMO page, despite "more than 275 social and special interest organizations." Call '
               'Campus Life & Event Services, (573) 651-2280.',
  'fair_outside': 'UNVERIFIED — no eligibility rule could be found because no fair could be found and the '
                  'governing Expression Policy could not be retrieved.',
  'fair_cost': 'UNVERIFIED — not published.',
  'fair_deadline': 'UNVERIFIED — not published.',
  'fair_url': 'https://semo.edu/life-at-semo/student-life/student-orgs/index',
  'policy': '⚠ NOT RETRIEVED — SEMO references an "Expression Policy" in its student handbook by name, but the '
            'document could not be reached on any tested URL. Rated PROVISIONAL.',
  'policy_url': 'https://semo.edu/campus-life/index.html',
  'policy_key': "⚠⚠ PROVISIONAL — THE GOVERNING POLICY COULD NOT BE RETRIEVED, AND THIS RATING IS A PLACEHOLDER, "
                "NOT A FINDING. Rated 3 under the standing rule; do not guess in either direction. ⚠ BUT NOTE WHAT "
                "IS KNOWN, BECAUSE IT IS MORE THAN AT SLU OR MISSOURI STATE: SEMO'S OWN CAMPUS LIFE PAGE "
                "EXPLICITLY REFERENCES 'a general \\'Expression Policy\\' handbook link related to exchange of "
                "ideas on campus.' THE DOCUMENT EXISTS AND IS NAMED — it simply could not be reached. Ask for it "
                "BY THAT NAME; Campus Life will know what you mean. RETRIEVAL FAILURES, all confirmed: "
                "semo.edu/policies/ and semo.edu/policies/index.html return 404; semo.edu/campus-life/student-"
                "conduct/student-handbook.html and /student-conduct/index.html return 404; semo.edu/campus-life/"
                "university-center/index.html and /campus-life/event-services/index.html return 404; semo.edu/pdf/ "
                "is ROBOTS-BLOCKED; and the site search (semo.edu/search/) is JAVASCRIPT-RENDERED, returning a "
                "search interface with no results and no policy content. SEMO's solicitation rules, its University "
                "Center tabling rates and its facility-use terms are ALL UNKNOWN. WHAT IS CERTAIN: SEMO is a PUBLIC "
                "institution and IS bound by RSMo s 173.1550, so its outdoor areas are 'deemed traditional public "
                "forums' and restrictions must 'employ clear, published, content, and viewpoint-neutral criteria' "
                "with 'ample alternative means of expression' — but s 173.1550(3) protects only 'NONCOMMERCIAL "
                "expressive activity,' so the statute gives DGD no right to table and will not defeat a "
                "solicitation rule or a fee. ASK FOR, BY NAME, ON ONE CALL TO (573) 651-2280: (1) the Expression "
                "Policy and the student handbook PDF; (2) the solicitation / sales policy and its number; (3) "
                "whether an outside for-profit may reserve space or a table during term, and at what rate; (4) "
                "whether a recognized student organization may reserve on behalf of an outside entity, or whether "
                "SEMO treats that as fronting; (5) insurance limits, deposits and cancellation terms; (6) whether "
                "any provision reaches payment credentials or signing agreements on site. SEMO is unusual in that "
                "ONE OFFICE — Campus Life & EVENT SERVICES — covers organizations, events AND space, so a single "
                "call can close the whole campus.",
  'sponsor_required': 'UNVERIFIED — no SEMO policy on sponsorship, fronting or outside-entity access could be '
                      'retrieved. Ask explicitly whether a recognized student organization may reserve on behalf '
                      'of an outside entity. (573) 651-2280.',
  'clubs': [('⚠ NO SEMO CLUB COULD BE CONFIRMED — 275+ ORGS, NONE READABLE',
             'The directory is Engage SEMO at semo.presence.io — the same Presence platform that is '
             'JAVASCRIPT-RENDERED and unreadable at Missouri State. No organization listings, no search results and '
             'no club names could be retrieved. SEMO claims "more than 275 social and special interest '
             'organizations." Whether any blockchain, crypto, fintech, investment or ACM club exists is COMPLETELY '
             'UNKNOWN. Ask Campus Life by name at (573) 651-2280.',
             'https://semo.presence.io')],
  'faculty': [('⚠ Campus Life & Event Services (University Center, Room 414, One University Plaza, MS 1200)',
               'THE ONE CALL THAT CLOSES SEMO. Unusually, a single office covers student organizations, events AND '
               'space — so the fair, the tabling rate, the solicitation rules and the Expression Policy are all '
               'reachable in one conversation. ASK FOR THE "EXPRESSION POLICY" BY THAT EXACT NAME: SEMO\'s own '
               'Campus Life page references it as a handbook link, so the document exists even though every URL to '
               'it 404s or is robots-blocked. NO INDIVIDUAL STAFF NAMES ARE PUBLISHED.',
               'Campus Life & Event Services',
               'campuslife@semo.edu · campredhawk@semo.edu · (573) 651-2280',
               'https://semo.edu/campus-life/index.html'),
              ('Office of the Registrar (Academic Hall 057, One University Plaza, MS 3760)',
               'Confirmed the Fall 2026 dates above. Ask for the last day of classes, which is not separately '
               'printed on the calendar, and for the Second Eight-Week session deadlines.',
               'Registrar',
               '(573) 651-2250',
               'https://semo.edu/registrar/academic-calendar.html'),
              ('SEMO main line',
               'Operator, last resort — printed on the student-organizations page alongside the Campus Life '
               'number.',
               'Southeast Missouri State University',
               '(573) 651-2000 (MAIN LINE)',
               'https://semo.edu/life-at-semo/student-life/student-orgs/index'),
              ('(Harrison College of Business / computer science faculty)',
               'NOT CONFIRMED — no SEMO faculty member could be confirmed on any relevant topic in this pass. No '
               'department directory was reached. Look up here; route via Campus Life or the operator.',
               'Southeast Missouri State University',
               'no number published — look up here, or (573) 651-2280',
               'https://semo.edu/')],
  'courses': [('(All SEMO courses)',
               'NOT CHECKED — no SEMO catalog or course-search page was reached, and semo.edu/search/ is '
               'JavaScript-rendered. No course could be verified for blockchain, crypto or fintech content in '
               'either direction. Gap.',
               'https://semo.edu/')],
  'events': [('(All SEMO events)',
              'NOT RETRIEVED — no career fair, involvement fair, speaker series or hackathon could be confirmed at '
              'SEMO in this pass. Ask Campus Life & Event Services, (573) 651-2280.',
              'https://semo.edu/campus-life/index.html')],
  'play': 'Cape Girardeau is the lowest-priority stop in Missouri and should be treated as a phone call rather than '
          'a trip — but it is the EASIEST phone call in the state, because SEMO is unusual in routing student '
          'organizations, events AND space through one office. Ring Campus Life & Event Services at '
          '(573) 651-2280 and ask for the "EXPRESSION POLICY" by that exact name: SEMO\'s own Campus Life page '
          'references it as a handbook link, so the document definitely exists, even though semo.edu/policies '
          '404s, the student-handbook URLs 404, semo.edu/pdf is robots-blocked and the site search is '
          'JavaScript-only. On the same call get the University Center tabling rate for a non-university group, '
          'whether an outside for-profit may reserve during term, and whether a student organization may reserve on '
          'its behalf. Until that call happens the access rating of 3 is a PLACEHOLDER and should not be quoted to '
          'anyone. What SEMO does have going for it is the calendar: it starts Aug 24, takes only a two-day fall '
          'break Oct 8–9, and has the SHORTEST THANKSGIVING BREAK IN THE STATE at three days (Nov 25–27) against '
          'nine at Mizzou, S&T, UMSL and Missouri State — so November is unusually intact here, and finals do not '
          'start until Dec 14, making SEMO one of only three Missouri campuses still in session in mid-December. '
          'If a late-season stop is ever needed, SEMO, Mizzou and UMSL are the only options. Watch the eight-week '
          'block structure: First Eight-Week courses close on Sep 25 and a second session begins, so late September '
          'is a churn point. Do not expect club intelligence — Engage SEMO runs on the same Presence platform that '
          'is unreadable at Missouri State, and not one of the 275+ organizations could be enumerated.',
  'gaps': ['⚠⚠ THE "EXPRESSION POLICY" AND THE STUDENT HANDBOOK. SEMO\'s Campus Life page references the Expression '
           'Policy BY NAME but every route to it fails: semo.edu/policies/ 404, /campus-life/student-conduct/'
           'student-handbook.html 404, /student-conduct/index.html 404, semo.edu/pdf/ ROBOTS-BLOCKED, site search '
           'JavaScript-only. Ask for it by name at (573) 651-2280.',
           '⚠⚠ THE SOLICITATION POLICY, THE UNIVERSITY CENTER TABLING RATE AND ALL FACILITY-USE TERMS. None could '
           'be retrieved; /campus-life/university-center/index.html and /campus-life/event-services/index.html both '
           '404. (573) 651-2280.',
           '⚠ Whether a recognized student organization may reserve on behalf of an outside entity, or whether SEMO '
           'treats that as fronting. (573) 651-2280.',
           '⚠ Insurance limits, deposits and cancellation terms — nothing published. (573) 651-2280.',
           '⚠ Whether SEMO holds a fall involvement fair at all, and its date, cost and outside-org eligibility. '
           'Nothing published despite 275+ organizations. (573) 651-2280.',
           '⚠ Engage SEMO (semo.presence.io) is JAVASCRIPT-RENDERED — NOT ONE of the 275+ organizations could be '
           'enumerated. Whether a blockchain or fintech club exists is unknown.',
           'The last day of classes is not separately printed on the SEMO academic calendar — only that finals run '
           'Dec 14–18. (573) 651-2250.',
           'Second Eight-Week session add/drop deadlines were not retrieved. (573) 651-2250.',
           'No SEMO faculty member could be confirmed on any topic; no department directory was reached.',
           'No SEMO course catalog was reached — no course could be checked.',
           'No SEMO career fair, speaker series or hackathon could be confirmed.'],
  'note': 'Cape Girardeau is roughly two hours south of St. Louis on I-55 — closer than Springfield or Kirksville, '
          'and the only campus in this packet that could be bolted onto a St. Louis day at a stretch. Its real '
          'value is timing rather than size: with a three-day Thanksgiving and finals starting Dec 14, SEMO holds '
          'students later in the term than almost anywhere else in Missouri.'},
]

DEADLINES = [

 # ---- term starts, in order ----
 ('2026-08-17', 'Aug 17, 2026', 'Missouri State / Truman',
  'CLASSES BEGIN — first wave, a week ahead of the Aug 24 group',
  'Missouri State: fall break Oct 8–11, Thanksgiving Nov 21–29, LAST DAY OF CLASSES THU DEC 3 — the state\'s '
  'earliest finish. Truman: block courses end Oct 6, midterm break Oct 8–9, instruction ends Dec 4.',
  'https://www.missouristate.edu/registrar/academic-calendar.htm',
  'Missouri State (417) 836-5000 (main line) · Truman (660) 785-4222'),

 ('2026-08-19', 'Aug 19, 2026', 'Saint Louis University',
  '⚠ CLASSES BEGIN — THE EARLIEST START IN MISSOURI, and the only midweek start',
  'Wed Aug 19, five days ahead of the Aug 24 wave. Fall break Oct 22–23 (later than anyone else in the state), '
  'Thanksgiving Nov 25–27, last class Fri Dec 4, finals Dec 7–11.',
  'https://www.slu.edu/registrar/calendars/index.php',
  'Student Involvement (314) 977-2805 · Busch Student Center (314) 977-2820'),

 ('2026-08-24', 'Aug 24, 2026', 'Mizzou / WashU / S&T / UMSL / SEMO',
  'CLASSES BEGIN at five campuses — the main wave',
  'Mizzou has NO FALL BREAK: 13 uninterrupted weeks Aug 24 – Nov 21, the best sustained window in Missouri. '
  'WashU takes Oct 3–6. S&T, UMSL and SEMO all fall into the Oct 8–12 break cluster. ⚠ UMKC\'s Fall 2026 start is '
  'UNVERIFIED — its registrar calendar page returns an empty body.',
  'https://registrar.missouri.edu/wp-content/uploads/2024/12/2026-2027-Academic-Calendar-.pdf',
  'Mizzou (573) 882-3780 · WashU (314) 935-3443 · S&T (573) 341-4025 · UMSL (314) 516-5291 · SEMO (573) 651-2280'),

 ('2026-08-30', 'Aug 30, 2026', 'Missouri S&T / UMSL',
  'Free-drop and enrollment deadlines — the roster settles',
  'S&T: free drop / 100% refund Sun Aug 30 (drop with W deadline Mon Oct 5). UMSL: "Last day any student may '
  'enroll (enter a course for credit)" Sun Aug 30.',
  'https://registrar.mst.edu/media/administrative/registrar/documents/calendars/2026/FS2026%20Dates%20and%20Deadlines.pdf',
  'S&T (573) 341-4181 · UMSL (314) 516-5545'),

 ('2026-08-31', 'Aug 31, 2026', 'U of Missouri–Columbia',
  '⚠ GET INVOLVED FAIR, 11 a.m. – 2 p.m., Kuhlman Court, 600+ organizations — YEAR UNCONFIRMED',
  '⚠ THE PAGE PRINTS NO YEAR (footer says "© 2026"). Resolved by weekday: a 2025 reading puts the fair on a SUNDAY '
  'and the listed "Sept. 3 | 7 p.m. | Memorial Stadium — Mizzou Football" on a WEDNESDAY; a 2026 reading gives a '
  'Monday fair and a Thursday-night opener. THE PAGE READS AS FALL 2026. Part of Involvement Week Aug 30 – Sept 5. '
  'Outside-org eligibility, cost and deadline are NOT published for the fair. The one slot that names outside '
  'entities is the VOLUNTEER FAIR, Sept 1, 11–2, Lowry Mall — "Connect with local organizations" — but that is a '
  'nonprofit framing. CALL AND SETTLE THE YEAR BEFORE BOOKING TRAVEL.',
  'https://getinvolved.missouri.edu/involvement-week/',
  'engagement@missouri.edu · (573) 882-3780'),

 ('2026-09-01', 'Sept 1, 2026', 'U of Missouri–Columbia',
  'Volunteer Fair, 11 a.m. – 2 p.m., Lowry Mall — "Connect with local organizations"',
  'The only Involvement Week event whose own description admits outside entities. Nonprofit/volunteering framing, '
  'so a poor fit for a for-profit crypto project — but worth one question on the call. Same year caveat as the '
  'Get Involved Fair: no year is printed on the page.',
  'https://getinvolved.missouri.edu/involvement-week/',
  '(573) 882-3780'),

 ('2026-09-10', 'Sept 10, 2026', 'U of Missouri–Columbia',
  'Fall 2026 MIZZOU ENGINEERING Career Fair',
  'Explicitly labelled 2026 on the MU Career Center fair index. Time, location and employer cost are NOT on the '
  'index — each fair links through to Handshake. The engineering audience is the closest technical cohort at '
  'Mizzou. Call for the rate and the deadline.',
  'https://career.missouri.edu/jobs-and-internships/career-fairs/',
  'career@missouri.edu · (573) 882-6801'),

 ('2026-09-16', 'Sept 16, 2026', 'U of Missouri–Columbia',
  'Mizzou Textile and Apparel Management Fall 2026 Career Fair',
  'Explicitly labelled 2026. Low fit for DGD; listed for completeness so the September calendar is not misread.',
  'https://career.missouri.edu/jobs-and-internships/career-fairs/',
  'career@missouri.edu · (573) 882-6801'),

 ('2026-09-17', 'Sept 17, 2026', 'U of Missouri–Columbia',
  '⚠⚠ MIZZOU FALL 2026 BUSINESS & ACCOUNTANCY CAREER FAIR — $600 FOR-PROFIT. THE BEST PAID DOOR IN MISSOURI.',
  'Thu Sep 17, 10 a.m. – 3 p.m., MizzouRec. FOR-PROFIT ORGANIZATIONS $600 ($630 with the 5% credit-card fee); '
  'non-profit / Mizzou-affiliated $250 ($262.50). Registration via Handshake. ⚠ NO DEADLINE IS PUBLISHED — call '
  'and get one. Sep 17, 2026 IS a Thursday and the listing is explicitly labelled 2026, so it is not stale. This '
  'is the ONLY published for-profit rate found anywhere in Missouri, it puts DGD in front of the Trulaske finance '
  'cohort, and it requires no club, no sponsorship and no argument.',
  'https://business.missouri.edu/student-development/career-preparedness/business-career-services/career-fairs',
  'bcs@missouri.edu · (573) 882-2565'),

 ('2026-09-22', 'Sept 22, 2026', 'Missouri S&T',
  '⚠⚠ MISSOURI S&T CAREER FAIR, 9:00 a.m. – 2:00 p.m. — THE ONLY ROUTE INTO ROLLA',
  'Tue Sep 22, 2026 — confirmed, and Sep 22 IS a Tuesday, so the listing is internally consistent. EMPLOYER '
  'REGISTRATION COST IS NOT PUBLISHED; call for it. WHY THIS MATTERS: a career fair is an EMPLOYER-RECRUITING '
  'framework, not a vendor-solicitation framework, so it is the one route into S&T that does not obviously run '
  'through the Havener rule that "Credit card, telephone card, or other financial services vendors are not allowed '
  'at the Havener Center or on the Missouri S&T campus." Best technical audience in the state.',
  'https://career.mst.edu/',
  'career@mst.edu · (573) 341-4343'),

 ('2026-09-25', 'Sept 25, 2026', 'Southeast Missouri State',
  'First Eight-Week session drop deadline — a churn point at SEMO',
  'SEMO runs concurrent eight-week sessions alongside full-semester courses. First Eight-Week closes and a second '
  'session begins, so late September is unusually unsettled here. Full-semester drop deadline is Fri Nov 20.',
  'https://semo.edu/student-support/academic-support/registrar/academic-calendar',
  '(573) 651-2250'),

 ('2026-09-30', 'Sept 30, 2026', 'U of Missouri–Columbia',
  'TWO Mizzou career fairs on one day — CAFNR/Arts & Science Career & Internship Expo, and Health & Wellness',
  'Both explicitly labelled 2026 on the MU Career Center index. The Arts & Science half of the CAFNR/A&S expo is '
  'the broader undergraduate audience of the two. Times, locations and employer costs are not on the index.',
  'https://career.missouri.edu/jobs-and-internships/career-fairs/',
  'career@missouri.edu · (573) 882-6801'),

 ('2026-10-03', 'Oct 3–6, 2026', 'Washington University',
  'FALL BREAK — WashU goes dark alone',
  'Sat–Tue Oct 3–6. WashU is the only Missouri campus that does NOT fall into the Oct 8–12 cluster, so a St. Louis '
  'day in that week can still work SLU and UMSL.',
  'https://bulletin.wustl.edu/washu/calendar/',
  '(314) 935-3443'),

 ('2026-10-06', 'Oct 6, 2026', 'Truman State',
  '⚠ FIRST BLOCK COURSES CONCLUDE — the only sub-term boundary in the state',
  'Truman runs block courses inside the semester. Attention resets here, and midterm break follows immediately '
  '(Thu–Fri Oct 8–9). Schedule either side of the Oct 6–9 seam, not across it.',
  'https://www.truman.edu/majors-programs/academic-resources/academic-calendar-schedules/academic-calendar/2026-27-academic-calendar/',
  'orgs@truman.edu · (660) 785-4222'),

 ('2026-10-08', 'Oct 8–12, 2026', 'FIVE CAMPUSES',
  '⚠ FALL BREAK CLUSTER — Missouri State, Missouri S&T, UMSL, Truman and SEMO all dark in the same week',
  'Missouri State Oct 8–11; S&T 8 a.m. Thu Oct 8 – 8 a.m. Mon Oct 12; UMSL 12 a.m. Thu Oct 8 – Mon Oct 12; Truman '
  'midterm break Thu–Fri Oct 8–9; SEMO Thu–Fri Oct 8–9. Mizzou has NO fall break at all and WashU took its Oct '
  '3–6, so Columbia and St. Louis are the only useful destinations that week.',
  'https://registrar.mst.edu/media/administrative/registrar/documents/calendars/2026/FS2026%20Dates%20and%20Deadlines.pdf',
  'Mizzou (573) 882-3780 — the one campus still at full density'),

 ('2026-10-22', 'Oct 22–23, 2026', 'Saint Louis University',
  'Fall break — SLU\'s is later than anyone else\'s in Missouri',
  'Two weeks after the Oct 8–12 cluster. If a St. Louis day is planned for that week, WashU and UMSL are in '
  'session and SLU is not.',
  'https://www.slu.edu/registrar/calendars/index.php',
  '(314) 977-2805'),

 ('2026-11-20', 'Nov 20, 2026', 'Missouri State',
  '⚠ LAST USEFUL DAY IN SPRINGFIELD — Thanksgiving begins Nov 21 and classes end Dec 3',
  'Missouri State takes a NINE-DAY Thanksgiving absence Nov 21–29 and then finishes first in the state on Thu Dec '
  '3. Practically, anything scheduled in Springfield after about Nov 18 is worthless.',
  'https://www.missouristate.edu/registrar/academic-calendar.htm',
  '(417) 836-5000 (main line — the only confirmed number at this campus)'),

 ('2026-11-21', 'Nov 21, 2026', 'Mizzou / UMSL / Missouri State',
  '⚠ LAST FULL-DENSITY DAY before the long Thanksgiving absences',
  'Mizzou: recess begins close of day Sat Nov 21, classwork resumes 8 a.m. Mon Nov 30 — that closes the 13-week '
  'uninterrupted run that began Aug 24. UMSL: 5 p.m. Sat Nov 21 to 8 a.m. Mon Nov 30. Missouri State: Nov 21–29.',
  'https://registrar.missouri.edu/wp-content/uploads/2024/12/2026-2027-Academic-Calendar-.pdf',
  'Mizzou (573) 882-3780 · UMSL (314) 516-5291'),

 ('2026-11-22', 'Nov 22–30, 2026', 'Missouri S&T',
  '⚠ NINE-DAY SHUTDOWN — THE LONGEST THANKSGIVING CLOSURE IN THE STATE',
  '8:00 a.m. Sun Nov 22 to 8:00 a.m. Mon Nov 30. Rolla is empty for over a week, and classes then run only to Dec '
  '11. The usable S&T windows are Aug 24 – Oct 7 and Oct 12 – Nov 20.',
  'https://registrar.mst.edu/media/administrative/registrar/documents/calendars/2026/FS2026%20Dates%20and%20Deadlines.pdf',
  '(573) 341-4025'),

 ('2026-12-03', 'Dec 3, 2026', 'Missouri State',
  'LAST DAY OF CLASSES — MISSOURI STATE IS DONE FIRST',
  'A full week before Mizzou, S&T, UMSL and SEMO. Finals Dec 5–10.',
  'https://www.missouristate.edu/registrar/academic-calendar.htm',
  '(417) 836-5000 (main line)'),

 ('2026-12-04', 'Dec 4, 2026', 'Truman State / Saint Louis University',
  'Last day of instruction at two campuses',
  'Truman: instruction ends Fri Dec 4, finals Dec 7–11, reading day Dec 9, commencement Sat Dec 12 at 11 a.m. '
  'SLU: last class Fri Dec 4, finals Dec 7–11.',
  'https://www.slu.edu/registrar/calendars/index.php',
  'Truman (660) 785-4222 · SLU (314) 977-2269'),

 ('2026-12-07', 'Dec 7, 2026', 'Washington University',
  'Last day of classes at WashU',
  'Reading days Dec 8–9; finals Thu Dec 10 – Wed Dec 16. No December commencement — the Class of 2027 ceremony is '
  'May 21, 2027.',
  'https://bulletin.wustl.edu/washu/calendar/',
  '(314) 935-3443'),

 ('2026-12-12', 'Dec 12–19, 2026', 'UMSL / SEMO / Mizzou',
  '⚠ THE ONLY DECEMBER WINDOW LEFT IN MISSOURI',
  'UMSL classes end 5 p.m. Sat Dec 12 with finals Dec 14–19 — the latest last-class date in the state. SEMO finals '
  'Dec 14–18. Mizzou finals Dec 14–18. Every other Missouri campus has finished. If a December stop is required, '
  'these three are the only options, and UMSL and SEMO are both reachable from St. Louis.',
  'https://www.umsl.edu/registration/resources/students/semester-calendars-important-dates.html',
  'UMSL (314) 516-5291 · SEMO (573) 651-2280 · Mizzou (573) 882-3780'),

 # ---- undated / monitor-only action items ----
 ('', 'ASAP — before anything at Mizzou', 'U of Missouri–Columbia',
  '⚠⚠ GET THE MIZZOU VENDOR TABLE RATE — THE POLICY GRANTS THE RIGHT, NOBODY PUBLISHES THE PRICE',
  'BPPM 6:053 states outright "Non-University Groups will be allowed to request a reservation to sell on campus," '
  'capped at "a maximum of five (5) days during the fall semester," three vendors a day, 10 a.m.–2 p.m., requested '
  '"not later than fifteen (15) business days in advance." But NO DOLLAR FIGURE appears on the outdoor info-tables '
  'page, the indoor info-tables page or the non-university reservations page. On the same call: get the Facilities '
  'Use Agreement and the PRODUCT APPROVAL FORM — "Vendors must also fill out a product approval form listing a '
  'detailed description of products and/or services they intend to offer," which for a crypto project is the whole '
  'decision. Money terms: full payment "not less than one week prior" or "The reservation will be considered null '
  'and void." Ask for Sam Cohen or Lauren Northern.',
  'https://bppm.missouri.edu/policy/sales-solicitations-collections-advertising/',
  'reservations@missouri.edu · (573) 884-8793 · authorising office (573) 882-2094'),

 ('', 'ASAP — no later than mid-September 2026', 'U of Missouri–Columbia',
  '⚠⚠ TIGERHACKS SPONSORSHIP — EMAIL NOW. THE BEST SPONSORSHIP PIPELINE IN MISSOURI.',
  'A private, student-run hackathon run out of the College of Engineering: sponsoring it SIDESTEPS BPPM 6:053 and '
  'the whole solicitation regime. ⚠ THE LIVE SITE IS A YEAR STALE — it still shows Nov 7–9, 2025 (the "Major '
  'League Hacking 2026 Hackathon Season" badge is an MLH season label spanning 2025-26, NOT a 2026 date), and the '
  'PROSPECTUS IS THE 2024 EDITION. Treat amounts as indicative: Seed $1,700 (logo, marketing, meal sponsorship, '
  'judging — NO table); Sprout $3,000 (adds t-shirt logo, "Career Fair Participant," mentors/reps on site, early '
  'participant data); Sapling $5,000 (adds hosting a workshop, a custom prize category, "Present at Opening and '
  'Closing Ceremony," "Schedule On-Site Interviews," full participant data). Custom packages available. 2024 '
  'attendance "over 300 students from across the Midwest"; past sponsors Garmin, Veterans United, Enterprise '
  'Mobility, Shelter Insurance, H&R Block. Pattern: one weekend in early November, Lafferre Hall. Sponsor decks '
  'typically close 6–8 WEEKS OUT — get the Fall 2026 date and current pricing now.',
  'https://tigerhacks.missouri.edu/prospectus.pdf',
  'muengrtigerhacks@umsystem.edu'),

 ('', 'BEFORE driving to Rolla', 'Missouri S&T',
  '⚠⚠ SETTLE THE "FINANCIAL SERVICES VENDOR" QUESTION — THE WHOLE CAMPUS TURNS ON ONE SENTENCE',
  'Havener Center Policies: "CREDIT CARD, TELEPHONE CARD, OR OTHER FINANCIAL SERVICES VENDORS ARE NOT ALLOWED AT '
  'THE HAVENER CENTER OR ON THE MISSOURI S&T CAMPUS." Campus-wide, named by financial function, no exception '
  'process printed. Alongside it: "Direct solicitation of money, regardless of the intended use, is not permitted '
  'on University property," and an explicit ANTI-FRONTING rule — "Non-university groups or individuals may not '
  'reserve facilities in the name of a student group or university department to avoid payment of usage fees" — '
  'which closes the club workaround. ASK THE ONE QUESTION THAT MATTERS: does a non-custodial protocol that sells '
  'nothing and gives away materials at no charge fall inside "other financial services vendors," or can it book '
  'the INFORMATIONAL tier, which the same policy defines as an organization that "distributes information to the '
  'campus community or gives away items at no charge"? Get the answer in writing. Also get table pricing — both '
  'tiers carry fees and the policy says only "Please contact Events and Hospitality Management for pricing." '
  'Published money terms: $50 late-cancellation fee, $50 no-show fee, $25 technician minimum, $50 overtime '
  'minimum, 3% credit-card convenience fee, $1,000,000 general liability for alcohol events.',
  'https://havener.mst.edu/policies/',
  '(573) 341-4399 · reservations reserve@mst.edu (573) 341-4564'),

 ('', 'First call at WashU — 30 days before anything', 'Washington University',
  '⚠⚠ RESOLVE THE SPONSORSHIP CONTRADICTION, AND GET A RATE CARD THAT IS CURRENTLY AN IMAGE',
  'The Danforth Campus Facilities Access Policy (updated 7 Nov 2024) bars outsiders outright for the whole tour '
  'window — "External individuals and organizations not affiliated with the university are NOT PERMITTED TO '
  'RESERVE UNIVERSITY SPACE DURING THE ACADEMIC YEAR FROM AUGUST 1-MAY 31" — with one exception: co-sponsorship, '
  'where "a university recognized student organization OR department... may reserve the space and invite the '
  'external individual or organization to participate." BUT Event Management\'s own External Events page says '
  'academic-year external events "require sponsorship by a Washington University DEPARTMENT." THOSE CONFLICT, and '
  'the answer decides whether a student club is any use to you at all. Also: "External inquiries must be placed a '
  'minimum of 30 days in advance," a sponsored event pays "50% of the \'Non-University / External Events\' listed '
  'on the rates page," and ⚠ THE RATES PAGE IS AN IMAGE with no readable dollar amounts. Do NOT cite RSMo '
  's 173.1550 here — WashU states it "is a private institution and retains the ability to prohibit or deny use of '
  'its facilities or spaces for any reason at the sole discretion of the university."',
  'https://washu.edu/policies/danforth-campus-facilities-access-policy/',
  'Indra Russell, Event Manager · irussell@wustl.edu · (314) 935-8264 · office (314) 935-3443'),

 ('', 'Before routing anyone to Kansas City', 'U of Missouri–Kansas City',
  '⚠⚠ UMKC\'S ENTIRE FALL 2026 CALENDAR IS UNKNOWN — THE REGISTRAR PAGE RETURNS AN EMPTY BODY',
  'umkc.edu/registrar/academic-calendar.html returns an EMPTY PAGE BODY (confirmed on two separate attempts); '
  'catalog.umkc.edu/undergraduate-academic-regulations-information/academic-calendar/ returns navigation chrome '
  'with no dates; five other URL variants 404. NOT ONE UMKC DATE IS CONFIRMED. The three sibling UM System '
  'campuses whose calendars WERE confirmed all begin Mon Aug 24, 2026 — that is a PATTERN, NOT A FACT, and booking '
  'travel on it would waste a week. Also get: whether UMKC has any campus solicitation procedure on top of CRR '
  '110.010, whether it has a local anti-fronting rule, and A PHONE NUMBER FOR THE STUDENT UNION RESERVATIONS '
  'FUNCTION — an email is published but no number, no rates, no tabling rules and no external-group terms exist '
  'anywhere on umkc.edu. Note the Student Affairs offices index lists NO DEAN OF STUDENTS OFFICE.',
  'https://www.umkc.edu/registrar/academic-calendar.html',
  'Registrar (816) 235-1125 · Student Involvement (816) 235-1407 · Student Union (816) 235-5555'),

 ('', 'One call closes the campus', 'Missouri State',
  '⚠⚠ MISSOURI STATE IS A BLANK PAGE — AND ITS POLICY LIBRARY IS UNREACHABLE THREE DIFFERENT WAYS',
  'missouristate.edu/policy returns TOO MANY REDIRECTS (a redirect loop); policies.missouristate.edu FAILS DNS '
  'RESOLUTION entirely ("Name or service not known"); search.missouristate.edu is a JavaScript-rendered shell; '
  'every Plaster Student Union and Event Services URL 404s; the 300+ organization directory is a '
  'JavaScript-rendered Presence app; and NEITHER the Office of Student Engagement NOR the Registrar publishes a '
  'direct phone number. THE SWITCHBOARD IS THE ONLY CONFIRMED NUMBER ON THE CAMPUS. Ask the operator for Student '
  'Engagement and for the Plaster Student Union, and get in writing: the solicitation policy and its number, the '
  'non-university tabling rate, whether an outside for-profit may reserve during term, and whether a student '
  'organization may reserve on its behalf. ⚠ USEFUL LEVER: Missouri State is public, so RSMo s 173.1550 binds it, '
  'and the statute requires restrictions to employ "clear, PUBLISHED, content, and viewpoint-neutral criteria." '
  'Missouri State\'s are not published anywhere reachable — a polite and accurate reason to ask them to send it.',
  'https://www.missouristate.edu/StudentEngagement/student-organizations.htm',
  '(417) 836-5000 (MAIN LINE — the only confirmed number at this campus)'),

 ('', 'Two calls close the campus', 'Saint Louis University',
  '⚠⚠ SLU\'S WRITTEN POLICY COULD NOT BE RETRIEVED — AND DO NOT CITE THE STATE STATUTE THERE',
  'Five candidate policy URLs returned 404, the Busch Student Center page carries no reservation rules or rates, '
  'the student-organization resources page carries no handbook and no phone number, catalog.slu.edu is '
  'robots-blocked, and SLU Groups is JavaScript-rendered so not one of the 200+ organizations could be read. The '
  'access rating of 3 is a PLACEHOLDER and must not be quoted to anyone. Ring the Busch Student Center Information '
  'Desk — the BSC page names that number specifically for "space reservations, tabling permissions, and applicable '
  'rules or fees" — and the Student Involvement Center. Ask for the solicitation policy by name, the '
  'non-university tabling rate, whether a student org may reserve on behalf of an outside entity, and the '
  'insurance and deposit terms. ⚠ SLU IS PRIVATE, CATHOLIC AND JESUIT: it has no public-forum obligation and RSMo '
  's 173.1550, which by its terms covers only "public institutions of higher education in this state," DOES NOT '
  'REACH IT. Citing the statute at SLU will read as unserious.',
  'https://www.slu.edu/life-at-slu/busch-student-center/index.php',
  'BSC (314) 977-2820 · Student Involvement (314) 977-2805'),

 ('', 'Ask for it by name', 'Southeast Missouri State',
  '⚠ ASK SEMO FOR THE "EXPRESSION POLICY" — THE DOCUMENT EXISTS AND IS NAMED, BUT EVERY URL TO IT FAILS',
  'SEMO\'s own Campus Life page references "a general \'Expression Policy\' handbook link related to exchange of '
  'ideas on campus," so the document definitely exists. It could not be reached: semo.edu/policies/ 404, '
  '/campus-life/student-conduct/student-handbook.html 404, /student-conduct/index.html 404, '
  '/campus-life/university-center/index.html 404, /campus-life/event-services/index.html 404, semo.edu/pdf/ '
  'ROBOTS-BLOCKED, and the site search is JavaScript-only. SEMO is unusual in routing organizations, events AND '
  'space through ONE office, so a single call can close the whole campus: get the Expression Policy, the '
  'solicitation policy, the University Center tabling rate for a non-university group, whether an outside '
  'for-profit may reserve during term, whether a student org may reserve on its behalf, and the insurance and '
  'deposit terms. The access rating of 3 is a PLACEHOLDER until this call happens.',
  'https://semo.edu/campus-life/index.html',
  'campuslife@semo.edu · (573) 651-2280'),

 ('', 'Best club door in the state', 'Truman State',
  '⚠ THE BULLDOG STUDENT INVESTMENT FUND — $200,000 OF REAL ENDOWMENT MONEY, AND A NAMED STABLE ADVISOR',
  'Truman is THE ONLY CAMPUS IN MISSOURI whose organization directory is readable at all (static HTML; the other '
  'six are JavaScript-rendered or errored out), and it surfaces the best single target in the state: BSIF '
  '"manages $200,000 of the university\'s endowment funds, strategically investing in stocks and passive vehicles '
  'every semester," advised by Sunghan Bae (sbae@truman.edu). This matters doubly because Board Chapter 12.020.1(3) '
  'admits speakers "invited by the faculty sponsor AND president of a university-chartered organization" — note it '
  'requires BOTH, and 12.020.2 places responsibility on the chapter\'s membership, so be scrupulous with the '
  'students who sign for you. ACM (Kafi Rahman, kafi@truman.edu) and Google Developer Group (Nazmul Shahadat, '
  'nshahadat@truman.edu) are two more. ⚠ NO PHONE IS PUBLISHED FOR ANY TRUMAN ADVISOR — emails only. ⚠ The '
  'directory also prints STUDENT OFFICER names and emails; those rotate annually and will be stale by September — '
  'use advisors, not officers.',
  'https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/',
  'Union & Involvement Services · orgs@truman.edu · (660) 785-4222'),

 ('', 'Confirm the absences before relying on them', 'Truman State',
  '⚠ GET TRUMAN\'S RENTAL RATE AND THE PRESIDENT\'S PROCEDURE UNDER CHAPTER 12.010',
  'Board of Governors Code Chapter 12.010 (revised Aug 2, 2014): "OTHER PERSONS AND GROUPS MAY USE UNIVERSITY '
  'FACILITIES ON A SPACE AVAILABLE BASIS" — "in accordance with the policies and procedures, INCLUDING POSSIBLE '
  'RENTAL FEES, established by the President." That is the most permissively worded public provision in this '
  'packet, and NO solicitation clause, NO sales clause, NO commercial-activity ban, NO anti-fronting clause, NO '
  'insurance provision and NO deposit or cancellation terms could be found anywhere in the Code. But Truman\'s own '
  'policy index warns "This webpage does not contain an exhaustive list of university policies," so the missing '
  'procedure exists somewhere. ABSENCE OF PUBLISHED TEXT IS NOT PERMISSION — confirm explicitly, and ask the '
  'Institutional Compliance Office if Union & Involvement Services cannot produce it.',
  'https://c3c5e312.delivery.rocketcdn.me/wp-content/uploads/2014/02/CHAPTER-12-REVISED-August-2-2014.pdf',
  '(660) 785-4222 · main line (660) 785-4000'),

 ('', 'Monitor — statewide', 'All Missouri campuses',
  '⚠ DO NOT LET AN AMBASSADOR CITE RSMo s 173.1550 AS A RIGHT TO TABLE',
  'The Campus Free Expression Act (effective 28 Aug 2015, L. 2015 S.B. 93) deems "The outdoor areas of campuses of '
  'public institutions of higher education in this state... traditional public forums," requires restrictions to '
  'employ "clear, published, content, and viewpoint-neutral criteria" with "ample alternative means of '
  'expression," and creates a private right of action for the attorney general or "Persons whose expressive rights '
  'were violated" worth "no less than five hundred dollars for the initial violation, plus fifty dollars for each '
  'day the violation remains ongoing," with each day a new accrual inside a one-year limitation. BUT s 173.1550(3) '
  'PROTECTS ONLY "NONCOMMERCIAL EXPRESSIVE ACTIVITY." DGD is commercial. The statute is a tool for STUDENT ALLIES '
  'and a bar on banishing outdoor speech — it is NOT a right to table, and it defeats no fee or approval '
  'requirement in this packet. UMSL has written the line into its own guidelines: outdoor areas are a public '
  'forum, yet activities may not "involve solicitations or promotion of commercial enterprises" and only '
  '"NON-COMMERCIAL" written material may be distributed person-to-person. ⚠ THE STATUTE BINDS Mizzou, Missouri '
  'S&T, UMKC, UMSL, Missouri State, Truman and SEMO — IT DOES NOT REACH WASHU OR SLU, BOTH PRIVATE. WashU says so '
  'itself: it "is a private institution and retains the ability to prohibit or deny use of its facilities or '
  'spaces for any reason at the sole discretion of the university."',
  'https://revisor.mo.gov/main/OneSection.aspx?section=173.1550',
  'UMSL free-speech page names NO office — start at Student Involvement (314) 516-5291'),

 ('', 'Monitor — four campuses at once', 'UM System (Mizzou, S&T, UMKC, UMSL)',
  '⚠ ONE SYSTEMWIDE RULE ANSWERS THE THRESHOLD QUESTION AT FOUR CAMPUSES — CRR 110.010',
  'UM System Collected Rules and Regulations 110.010 (amended 11-18-21, 12-10-21, 6-29-23) governs Columbia, '
  'Rolla, Kansas City and St. Louis simultaneously. 110.010.G.1: "The sale of anything, the soliciting of '
  'subscriptions or the collection of dues is prohibited in the University buildings and upon University grounds '
  'WITHOUT PRIOR AUTHORIZATION OF THE CHANCELLOR." 110.010.E.4.c: "Other nonaffiliated and nonsponsored groups may '
  'make use of the facilities... UPON WRITTEN APPROVAL OF THE CHANCELLOR." 110.010.E.6: such groups "WILL BE '
  'CHARGED A FEE APPROVED BY THE CHANCELLOR." 110.010.E.3: non-students present "without specific permission or '
  'authorization or without an appropriate purpose MAY BE DEEMED GUILTY OF TRESPASS." 110.010.D.2: an RSO must '
  'file "a written request for approval... AT LEAST TEN DAYS PRIOR to the event." ⚠ THE CHEAPEST ROUTE IS '
  '110.010.E.4.a — facility use where the activity "is sponsored by or the group is invited by an instructional or '
  'administrative division." A DEPARTMENTAL INVITATION CONVERTS DGD FROM A VENDOR INTO AN INVITED GUEST at all '
  'four campuses. ⚠ NOTE: CRR 110.010 CONTAINS NO ANTI-FRONTING CLAUSE — that appears only at campus level, and '
  'only at Missouri S&T in this set. Chapter 110 also contains 110.020 "Service and Use Fees," the likely home of '
  'any published rate card; it was NOT retrieved. Ask for it by number.',
  'https://www.umsystem.edu/ums/rules/collected_rules/facilities/ch110/110.010_regulations',
  'Mizzou (573) 882-2094 · S&T (573) 341-4399 · UMKC (816) 235-1407 · UMSL (314) 516-5291'),

 ('', 'Monitor — statewide gap', 'All Missouri campuses',
  '⚠ NO BLOCKCHAIN FACULTY AND NO BLOCKCHAIN CLUB WAS CONFIRMED ANYWHERE IN MISSOURI — AND NONE WAS RULED OUT',
  'This is the largest hole in the packet, because the academic door is the cheapest route past every commercial '
  'rule above. NOT ONE faculty member working on blockchain, cryptocurrency, digital assets, fintech or payments '
  'could be confirmed at any of the nine campuses. SIX OF NINE organization directories are JavaScript-rendered '
  'and could not be enumerated — MU Engage (which also returned HTTP 504), WUGO at WashU, MinerLink at S&T, SLU '
  'Groups, Missouri State Presence and Engage SEMO — while UMKC publishes no directory link at all and UMSL\'s '
  'rendered only partially. Truman is the sole exception and its readable directory shows NO crypto club. Two '
  'faculty directories (Olin Business School, and Mizzou\'s finance course list) were JavaScript-rendered or 404. '
  'Every general search engine tested is ROBOTS-BLOCKED to research tooling. CLOSE THIS BY PHONE, campus by '
  'campus — ask each involvement office directly whether a blockchain, crypto or fintech organization exists, and '
  'ask each CS and finance department whether anyone researches distributed ledgers.',
  'https://involvement.truman.edu/index-5/student-organizations-2/student-organizations-list/',
  'Mizzou (573) 882-3780 · WashU (314) 935-3443 · S&T (573) 341-4025 · SLU (314) 977-2805 · '
  'Missouri State (417) 836-5000 · UMKC (816) 235-1407 · UMSL (314) 516-5291 · Truman (660) 785-4222 · '
  'SEMO (573) 651-2280'),
]
