"""Wisconsin — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published at time of research — a gap to close by phone, not a finding of absence.
Schema: reference/data-schema.md

STATEWIDE LEGAL CONTEXT — read before any ambassador cites anything:
THERE IS NO WISCONSIN CAMPUS FREE-SPEECH STATUTE. 2025 Senate Bill 498 (Campus Free Speech
and Academic Freedom) was introduced Oct 21, 2025 and PASSED the legislature Feb 12, 2026,
53-45 on party lines; Governor Evers stated Jan 6, 2026 that he would veto it, and no
enactment could be found. AB 299 (2017), AB 444 (2019) and AB 553 (2023) all died earlier.
An ambassador who cites "Wisconsin's campus free speech law" is citing a vetoed bill.
Source: https://campus-speech.law.duke.edu/campus-speech-incidents/wisconsin-senate-bill-498-2025-campus-free-speech-and-academic-freedom/

The governing layer is Regent Policy Document 4-21, "Commitment to Academic Freedom and
Freedom of Expression," adopted October 6, 2017 (Resolution 10952). It reaches "students,
employees, and VISITORS" but contains NO commercial-speech provision and permits
"reasonable viewpoint-neutral and content-neutral restrictions on time, place, and manner."
Neutral for DGD. https://www.wisconsin.edu/regents/policies/commitment-to-academic-freedom-and-freedom-of-expression/

THE OPERATIVE RULE IS UWS 18.11(8), NOT UWS 21. Full text of both is in UW-Madison's
policy_key below, labelled as a STATE note. In short: ch. UWS 21 "Use of University
Facilities" (Register Dec 1986 No. 372, eff. 1-1-87) governs WHO may use facilities and
CONTAINS NO COMMERCIAL-ACTIVITY CLAUSE; UWS 18.11(8) "Selling, peddling and soliciting"
is the commercial ban and it carries two written exceptions that are DGD's only public-
campus doors. NOTE: docs.legis.wisconsin.gov subsection URLs and the whole of ch. UWS 18
are ROBOTS-BLOCKED to research tooling, and direct curl to that host returns a proxy 403;
the ch. 21 landing page fetched, and UWS 18.11 came from the Justia mirror.

STATE POSTURE ON DIGITAL ASSETS: the State of Wisconsin Investment Board bought $164
million of two spot bitcoin ETFs in early 2024, the first US state pension fund to do so.
UW-Whitewater's Paul Nylen was WPR's on-record expert on it. Verifiably true, and the best
conversational opener in the state.
https://www.wpr.org/news/wisconsin-invest-bitcoin-efts-uw-whitewater-professor

CALENDAR SHAPE: eight public campuses on SEMESTERS; LAWRENCE RUNS TRIMESTERS and its Fall
Term is over Nov 24. Marquette Aug 31; Madison/Milwaukee/Eau Claire/Whitewater/Stout Sep 2;
La Crosse Sep 8; Oshkosh Sep 9; Lawrence Sep 14. Nine campuses inside fifteen days, and
SIX OF THE NINE FAIRS FALL ON WEDNESDAY SEPTEMBER 9, 2026 in six different cities.

GEOGRAPHY: treat Wisconsin as THREE trips, not one. (1) Madison + Whitewater + Milwaukee
is a real two-day corridor — Whitewater sits between them, 45 min from Madison and 50 from
Milwaukee. (2) Oshkosh + Appleton (Lawrence) are 20 miles apart, ~90 min north of
Milwaukee. (3) Eau Claire + Menomonie (Stout) + La Crosse is a separate western trip —
Eau Claire to Menomonie 25 miles, Eau Claire to La Crosse 90 miles, La Crosse to Madison
3.5 hours.
"""

STATE = 'Wisconsin'

CAMPUSES = [

 # ---------------------------------------------------------------- 1. UW-MADISON
 {'state': 'Wisconsin',
  'name': 'University of Wisconsin–Madison',
  'city': 'Madison, WI',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 3,
  'start': 'Wed Sep 2, 2026 (Labor Day holiday Mon Sep 7 — five days AFTER classes begin)',
  'adddrop': 'Not published on the Secretary of the Faculty calendar — the SecFac page gives instruction, '
             'recess, exam and commencement dates only. Get add/drop from the Registrar, '
             'https://registrar.wisc.edu/dates/',
  'fallbreak': '⚠ NONE — UW-Madison has NO fall break in the 2026-27 calendar. Full density Sep 2 straight '
               'through Nov 25. Best sustained access window at the flagship.',
  'thanksgiving': 'Thanksgiving recess Nov 26–29, 2026',
  'lastclass': 'Wed Dec 9, 2026. Study Day Thu Dec 10.',
  'finals': 'Fri Dec 11 – Thu Dec 17, 2026. Commencement Sun Dec 13.',
  'cal_url': 'https://secfac.wisc.edu/academic-calendar/',
  'cal_status': 'CONFIRMED on the Office of the Secretary of the Faculty 2026-2027 calendar, cross-confirmed '
                'against the Universities of Wisconsin systemwide calendar (Sep 2 – Dec 17), '
                'https://www.wisconsin.edu/academic-calendars/academic-year-2026-27/',
  'fair': 'Student Organization Fair (two nights)',
  'fair_date': 'Wed Sep 9 AND Thu Sep 10, 2026, 5:00–8:00 p.m., Kohl Center. Both weekdays check out against '
               '2026 (Sep 9 = Wednesday, Sep 10 = Thursday) — page is CURRENT, not stale.',
  'fair_outside': '⚠ NO — RSO-ONLY, AND THERE IS AN EXPLICIT ANTI-FRONTING SENTENCE: "YOUR ORGANIZATION MAY '
                  'NOT ALLOW A CORPORATE SPONSOR TO USE YOUR TABLE FOR PROMOTION." Table requests are open '
                  'only to "active registered student organizations (RSOs) whose primary contact has no policy '
                  'violations in the past two semesters," and the org must be searchable in the Wisconsin '
                  'Involvement Network. Courting a club to get a table here does not work by design.',
  'fair_cost': 'Not published for RSOs. The compliant paid alternative at UW-Madison is the All-Campus Career '
               '& Internship Fair — $900 for a for-profit table (see events).',
  'fair_deadline': 'Table requests ran May 8–22, 2026 — CLOSED. Cancellation deadline Aug 26, 2026. RSOs only.',
  'fair_url': 'https://soli.wisc.edu/attending-the-student-organization-fair/',
  'policy': 'UW-6000 Use of Facilities and Land; UW-6013 Expressive Activity; UW-2058 Wisconsin Union Conduct '
            'and Use; above all three, Wis. Admin. Code ch. UWS 21 and UWS 18.11(8)',
  'policy_url': 'https://policy.wisc.edu/library/UW-6000',
  'policy_key': "⚠ STATE NOTE — THE TWO PROVISIONS THAT GOVERN EVERY PUBLIC CAMPUS IN WISCONSIN. "
                "Wis. Admin. Code ch. UWS 21 'Use of University Facilities' (created Register, December 1986, "
                "No. 372, effective 1-1-87, https://docs.legis.wisconsin.gov/code/admin_code/uws/21). "
                "UWS 21.01: 'It is the policy of the Board of Regents that the facilities of the university are "
                "to be used primarily for purposes of fulfilling the university's missions of teaching, research "
                "and public service.' UWS 21.04(1): 'The chancellor of each institution, or his or her designee, "
                "MAY permit persons, or organizations not associated with that institution, to use university "
                "facilities' if (a) 'THE PROPOSED USE IS UNDER THE SPONSORSHIP OR AT THE INVITATION OF AN "
                "ORGANIZATION ASSOCIATED WITH THE INSTITUTION'; (b) it 'will not interfere with or detract from "
                "the teaching, research and public service missions of the institution, or the use of the "
                "facilities by organizations associated with the institution'; (c) 'The institution has "
                "appropriate facilities available for the proposed use'; (d) the person or organization 'has "
                "complied with institutional procedures adopted under s. UWS 21.06.' UWS 21.04(2): 'Persons or "
                "organizations using university facilities under this section MUST REIMBURSE THE INSTITUTIONS "
                "FOR THE COSTS, if any, incident to the use of the facilities.' UWS 21.06 requires each "
                "chancellor to publish procedures, 'A schedule of the costs and rental fees, if any,' and time "
                "and manner limits. ⚠ UWS 21 CONTAINS NO COMMERCIAL-ACTIVITY CLAUSE. The commercial ban lives in "
                "a different chapter and it is the sentence you will be quoted: Wis. Admin. Code UWS 18.11(8) "
                "'SELLING, PEDDLING AND SOLICITING' — 'NO PERSON MAY SELL, PEDDLE OR SOLICIT FOR THE SALE OF "
                "GOODS, SERVICES, OR CONTRIBUTIONS ON ANY UNIVERSITY LANDS EXCEPT IN THE CASE OF: (a) SPECIFIC "
                "PERMISSION IN ADVANCE FROM A SPECIFIC UNIVERSITY OFFICE or the occupant of a university house, "
                "apartment, or residence hall; (b) Sales by an individual of personal property owned or acquired "
                "by the seller primarily for his/her own use pursuant to an allocation; (c) Sales of newspapers "
                "and similar printed matter outside university buildings; (d) SUBSCRIPTION, MEMBERSHIP, TICKET "
                "SALES SOLICITATION, FUND-RAISING, SELLING, AND SOLICITING ACTIVITIES BY OR UNDER THE "
                "SPONSORSHIP OF A UNIVERSITY OR REGISTERED STUDENT ORGANIZATION; (e) Admission events in a "
                "university building pursuant to contract with the university, and food, beverage or other "
                "concessions conducted pursuant to a contract; (f) Solicitation of political contributions under "
                "ch. 11, Stats.' ⚠ UNLIKE OKLAHOMA, THE WISCONSIN CODE EXPRESSLY BLESSES THE SPONSORSHIP ROUTE "
                "at 18.11(8)(d). Nowhere in the public system is sponsorship forbidden outright; campus rules "
                "narrow it. Text retrieved from the Justia mirror because the Legislature's own ch. 18 page is "
                "ROBOTS-BLOCKED: https://regulations.justia.com/states/wisconsin/uws/chapter-uws-18/section-uws-18-11/ "
                "⚠ ALSO STATE-LEVEL: there is NO Wisconsin campus free-speech statute — 2025 SB 498 passed the "
                "legislature Feb 12, 2026 and Evers had said on Jan 6, 2026 he would veto it. DO NOT CITE ONE. "
                "=== MADISON-SPECIFIC === UW-6000 Use of Facilities and Land (eff. 09-01-2003, revised "
                "08-27-2024 and 06-10-2025, Facilities Planning & Management): 'THE USE OF UNIVERSITY FACILITIES "
                "BY OR FOR COMMERCIAL OR COMMERCIALLY-RELATED INTERESTS IS ALLOWED AS LONG AS THE USE IS "
                "CONSISTENT WITH THESE AND OTHER APPLICABLE POLICIES AND RULES' — commercial use requires 'a "
                "contract with the appropriate contracting department or building manager,' and 'Approval of "
                "commercial use does not constitute university endorsement of the using entity, its products, "
                "views, objectives, or program content.' ⚠ THE SPONSOR MUST BE A UNIVERSITY UNIT, NOT A CLUB, "
                "AND MUST ATTEND: non-university use requires sponsorship by a university department/office or "
                "invitation from the chancellor, provost, a vice chancellor, dean or director, and 'THE HEAD OF "
                "THE SPONSORING UNIT OR THEIR DESIGNEE MUST BE PRESENT FOR THE DURATION OF A SPONSORED EVENT'; "
                "the written commitment is due 'no later than two weeks prior to the event.' Users 'assume "
                "responsibility for all administrative, financial, and insurance responsibilities associated "
                "with the use of space.' 'RSOs are limited to THREE separate reservations for fundraising "
                "purposes during an academic year.' INSURANCE: 'Persons or organizations not covered under the "
                "[State Self-Funded Liability Program], including RSOs, MAY BE REQUIRED to obtain and submit "
                "necessary evidence of insurance coverage' — NO DOLLAR LIMIT IS PUBLISHED. UW-6013 Expressive "
                "Activity (eff. 08-27-2024, Office of the VC for Legal Affairs, policy.wisc.edu/library/UW-6013) "
                "looks friendly — 'University community members AS WELL AS VISITORS may use outdoor public "
                "university areas for expressive activity' — but ⚠ THE CARVE-OUT IS DECISIVE: 'COMMERCIAL "
                "ACTIVITY (RELATED TO A COMMERCIAL TRANSACTION OR AN ADVERTISEMENT TO PROMOTE THE SALE OF GOODS "
                "OR SERVICES) IS EXCLUDED and governed by [state administrative code] and separate university "
                "policy.' The visitor-friendly regime does not reach DGD at all. Also: no protest/chant/speech "
                "aimed beyond direct conversation 'within 25 feet of entrances to university owned or controlled "
                "buildings and facilities'; amplification only 12:00–1:30 p.m. and 5:00–7:00 p.m. and 'expressly "
                "prohibited' from Study Day through the day after the last exam. UW-2058 Wisconsin Union Conduct "
                "and Use (eff. 04-18-2017, revised 06-03-2025): ⚠ A HARD AFFILIATION GATE — 'GROUPS OR "
                "INDIVIDUALS ENGAGED IN FREE EXPRESSION ACTIVITIES (E.G., LEAFLETTING, SURVEYING, PETITIONING) "
                "MUST BE UW-MADISON STUDENTS, STAFF, OR FACULTY.' Free publications on the first-floor racks "
                "must be 'NON-COMMERCIAL', dated, 30-day limit. 'only Union members, university faculty and "
                "staff, invited guests, and university-sponsored conference groups, may use Wisconsin Union "
                "facilities.' Wisconsin Union event policy: outside parties can buy corporate membership, but "
                "outside members 'may only reserve spaces for INVITATION-ONLY, PERSONAL, PRIVATE EVENTS WITH NO "
                "BUSINESS OR ORGANIZATION CONNECTIONS OR PURPOSES.' NO rate card, insurance terms, deposits or "
                "cancellation terms are published on that page. NOTE: UW-6145 Vendor Permits is RETIRED "
                "(eff. 03-01-2000), superseded by UW-6140 Service/Vendor Permits.",
  'sponsor_required': 'YES — and it must be a UNIVERSITY UNIT, not a student club. UW-6000 routes non-university '
                      'use through a sponsoring department/office (or a chancellor/provost/VC/dean/director '
                      'invitation), the sponsoring unit head "must be present for the duration of a sponsored '
                      'event," and the written commitment is due two weeks out. Separately, the Student '
                      'Organization Fair bars a corporate sponsor from using an RSO table, and UW-2058 bars '
                      'non-affiliates from leafletting in the Union. The state code\'s RSO-sponsorship door '
                      '(UWS 18.11(8)(d)) is technically open at Madison but every campus implementation '
                      'narrows it. The clean route is the priced career fair.',
  'clubs': [('⚠ Badger Blockchain',
             'THE BLOCKCHAIN CLUB AT THE FLAGSHIP. Listed under "Interest Related" on the Wisconsin School of '
             'Business undergraduate student-organizations page. Own site badgerblockchain.com; active on GitHub '
             '(badgerblockchain/Deblocracy — "Badger Blockchain\'s democratic voting system for UW Madison ASM"), '
             'Medium, LinkedIn and Facebook. NO OFFICER NAMES OR CLUB EMAIL ARE PUBLISHED on any retrievable UW '
             'page — do not guess officers. WSB student-org questions go to Danae Dorsey, danae.dorsey@wisc.edu.',
             'https://www.badgerblockchain.com/'),
            ('Finance and investment cluster (Wisconsin School of Business)',
             'Capital Management Club (cmc-uwmadison.com); Cardinal Trading Group (win.wisc.edu/organization/ctg); '
             'Corporate Finance Club (wisconsincfc.com); Finance and Investment Society (fiswisconsin.com); '
             'Investment Banking Club (wisconsinibc.com); Prospera Financial Club; Sales & Trading and Asset '
             'Management Society (stamwisconsin.com); Scholars of Finance; Wealth Management Group '
             '(badgerwmg.org); Women in Finance and Accounting (wisconsinwifa.com). Deep, well-organised, and '
             'reachable only as guests of a university-sponsored event.',
             'https://business.wisc.edu/undergraduate/student-organizations/'),
            ('Entrepreneurship and tech cluster',
             'Badger Future Founders; Invent (inventuw.com); Women in Entrepreneurship; Engineering, Business & '
             'Entrepreneurship; AI Hub; Association of Business Leaders in Technology; Information Systems '
             'Society; Women in Business Technology.',
             'https://business.wisc.edu/undergraduate/student-organizations/'),
            ('⚠ WIN (Wisconsin Involvement Network) — NOT ENUMERABLE',
             'The campus-wide org directory at win.wisc.edu returns a landing shell with a "Discover your groups" '
             'link and no organization listing; individual org URLs '
             '(win.wisc.edu/organization/badgerblockchain) also returned no content. NOT confirmed login-gated, '
             'but not machine-readable. Whether any second crypto/Web3 org exists outside WSB is UNCONFIRMED — '
             'ask SOLI, (608) 263-0365.',
             'https://win.wisc.edu/organizations/')],
  'faculty': [('⚠ Brad Chandler',
               'THE BEST ACADEMIC DOOR AT MADISON. Teaching Faculty III, Finance, Investment & Banking; TEACHES '
               'FINANCE 765/615 CRYPTOCURRENCIES, BLOCKCHAIN AND DIGITAL ASSETS, and in Spring 2024 "partnered '
               'with Layer 3, a crypto educational platform, to provide students with hands-on experience" with '
               'DeFi protocols through customised quests. A guest lecture or seminar invitation from him is a '
               'non-commercial door that UW-6013 does not touch. ⚠ NO DIRECT PHONE IS PUBLISHED — the entire WSB '
               'Finance directory lists emails and no numbers. Reach him through the Nicholas Center.',
               'Wisconsin School of Business — Finance, Investment & Banking',
               'brad.chandler@wisc.edu · no direct number published — reach via Nicholas Center (608) 262-1550',
               'https://business.wisc.edu/faculty-research/finance-investment-banking/faculty/'),
              ('⚠ Randall Wright',
               'Professor of Finance, WARF named professorship — one of the world\'s monetary economists '
               '(Kiyotaki-Wright search-theoretic monetary economics), Minneapolis Fed and CEPR affiliations. '
               'The person on this campus who thinks professionally about what money IS. Not a crypto '
               'researcher — do not represent him as one — but the right room for a sound-money argument. '
               'NO PHONE PUBLISHED on the WSB directory.',
               'Wisconsin School of Business — Finance, Investment & Banking',
               'randall.wright@wisc.edu · no number published — look up here',
               'https://business.wisc.edu/faculty-research/finance-investment-banking/faculty/'),
              ('Nicholas Center for Corporate Finance & Investment Banking',
               'Grainger Hall, 975 University Avenue. Published the "Top Student Perspectives on Blockchain & '
               'Cryptocurrencies" volume from the inaugural 2018 crypto course (~50 students from finance, CS, '
               'economics, engineering, journalism, accounting, risk management and marketing). The route to '
               'Brad Chandler and the answer to whether FINANCE 615 runs in Fall 2026.',
               'Wisconsin School of Business',
               '(608) 262-1550',
               'https://business.wisc.edu/centers/nicholas/contact/'),
              ('⚠ Brandon Spoon',
               'Director of Marketing & Employer Engagement, SuccessWorks. CONTROLS THE ONE CLEAN PRICED '
               'COMMERCIAL DOOR AT UW-MADISON: the All-Campus Career & Internship Fair, Sep 16, 2026, $900 for a '
               'for-profit table, REGISTRATION AND PAYMENT DUE FRIDAY AUGUST 28, 2026. Call this number first.',
               'SuccessWorks at the College of Letters & Science',
               'brandon.spoon@wisc.edu · (608) 262-3921',
               'https://careerfair.wisc.edu/employers/'),
              ('Seng Thao',
               'Contact for the SuccessWorks Inclusive Community Career & Internship Fair Sponsor package, '
               '$1,200 — two tables, up to four representatives, "prime high-traffic table location at the fair '
               'with electrical provided," logo in promotional materials, signage, emails and online listings. '
               'No industry restriction is stated. No phone published — reach via (608) 262-3921.',
               'SuccessWorks',
               'seng.thao@wisc.edu · no number published — look up here, or (608) 262-3921',
               'https://successworks.wisc.edu/employers/employer-sponsorship-opportunities/'),
              ('⚠ SOLI — Office for Student Organizations, Leadership & Involvement',
               'Runs the Sep 9–10 Student Organization Fair and RSO recognition. 333 East Campus Mall, 3rd Floor, '
               'Student Activity Center. Ask them whether a second crypto RSO exists outside WSB — WIN is not '
               'machine-readable. Event-specific questions go to rsoevents@union.wisc.edu.',
               'Wisconsin Union / Student Affairs',
               'soli@union.wisc.edu · (608) 263-0365',
               'https://soli.wisc.edu/'),
              ('Wisconsin Union — Campus Event Services',
               'Books Union space and sells corporate membership. Mon–Fri 8:30 a.m.–4:30 p.m. Ask them what an '
               'outside corporate member can and cannot do, given that outside members may only book '
               '"invitation-only, personal, private events with no business or organization connections."',
               'Wisconsin Union',
               'events@union.wisc.edu · (608) 262-2511',
               'https://union.wisc.edu/host-your-event/policies-and-frequently-asked-questions'),
              ('Paul Broadhead',
               'Assistant Director for Facilities Management, Wisconsin Union — the named contact on UW-2058, the '
               'policy that restricts leafletting and petitioning in the Union to UW-Madison students, staff and '
               'faculty. Direct line.',
               'Wisconsin Union',
               'paul.broadhead@wisc.edu · (608) 263-4588',
               'https://policy.wisc.edu/library/UW-2058'),
              ('Jesse Luckey Winters',
               'Director, Space Management — the named contact on UW-6000, the facilities policy itself. The '
               'person who can tell you what "a contract with the appropriate contracting department" actually '
               'means for an outside for-profit. Direct line.',
               'Facilities Planning & Management',
               'jesse.winters@wisc.edu · (608) 556-7741',
               'https://policy.wisc.edu/library/UW-6000'),
              ('Nancy Lynch',
               'Office of the Vice Chancellor for Legal Affairs — named contact on UW-6013 Expressive Activity, '
               'including the commercial-activity carve-out. The authority on whether anything DGD does counts '
               'as expressive activity rather than commercial activity. Direct line.',
               'Office of the VC for Legal Affairs',
               'nancy.lynch@wisc.edu · (608) 263-7400',
               'https://policy.wisc.edu/library/UW-6013'),
              ('Office of Student Assistance and Support / Dean of Students',
               '70 Bascom Hall, 500 Lincoln Drive. Drop-in M–F 8:30–4. Escalation above SOLI.',
               'Student Affairs',
               'osas@studentaffairs.wisc.edu · (608) 263-5700',
               'https://osas.wisc.edu/'),
              ('Caryn Walline',
               'Director of Parking Operations — named contact on UW-6145 Vendor Permits. ⚠ UW-6145 IS RETIRED '
               '(eff. 03-01-2000); the live policy is UW-6140 Service/Vendor Permits. Carried across because a '
               'vendor permit may still be the mechanism for anything on wheels.',
               'Transportation Services',
               'cwalline@wisc.edu · (608) 263-6667',
               'https://policy.wisc.edu/library/UW-6145'),
              ('MadHacks — student organisers',
               'THE NON-COMMERCIAL-RULES BYPASS AT MADISON. "The largest hackathon in Wisconsin," 400+ '
               'participants in 2025 (largest in its history), 24 hours at Morgridge Hall. Student-run, so campus '
               'commercial-use rules do not reach the sponsorship pipeline. Past sponsors: American Family '
               'Insurance, Capital One, Epic, Google, MG&E, TDS, Fish Audio, Mastra; partners Red Bull, poppi, '
               'gener8tor, interviewing.io. NO PHONE — email only.',
               'School of Computer, Data & Information Science (student-run)',
               'team@madhacks.io · no number published — email only',
               'https://www.madhacks.io/'),
              ('(Wisconsin School of Business Finance department)',
               'NO PHONE NUMBERS AT ALL are published on the WSB Finance faculty directory — 28 faculty, 28 '
               'emails, zero numbers. Hengjie Ai chairs (hengjie.ai@wisc.edu); Jim Johannes is deputy chair; '
               'Dean Corbae is Academic Director; Mark Fedenia is Academic Executive Director; Susannah Gustafson '
               'is Finance Program Director. Look up here or route through the Nicholas Center.',
               'Wisconsin School of Business',
               'no numbers published — look up here, or (608) 262-1550',
               'https://business.wisc.edu/faculty-research/finance-investment-banking/faculty/')],
  'courses': [('FINANCE 615',
               'Cryptocurrencies, Blockchain and Digital Assets, 3 credits — "Delving into the experimental and '
               'evolving landscape of cryptocurrencies, blockchain and digital assets, technologies that have '
               'impacted the financial world," with focus on decentralized finance applications. Instructor Brad '
               'Chandler. ⚠ FALL 2026 OFFERING UNVERIFIED: the catalog entry reads "Last Taught: Spring 2026" and '
               'prints NO "Typically Offered" line. Confirm with the Nicholas Center, (608) 262-1550.',
               'https://guide.wisc.edu/courses/finance/'),
              ('FINANCE 765',
               'The graduate number for the same course — a Nicholas Center MBA elective. In Spring 2024 Chandler '
               '"partnered with Layer 3, a crypto educational platform" to give students hands-on DeFi '
               'experience through customised quests. FINANCE 365 was the original one-credit 2018 version.',
               'https://business.wisc.edu/centers/nicholas/blog/uw-crypto-course-gives-students-hand-on-experience-with-defi-by-partnering-with-layer-3/'),
              ('Nicholas Center student-research volume',
               '"Top Student Perspectives on Blockchain & Cryptocurrencies" — the best papers from the inaugural '
               '2018 course, whose ~50 students came from finance, computer science, economics, engineering, '
               'journalism, accounting, risk management and marketing. Useful evidence that the audience is '
               'cross-disciplinary, not just business.',
               'https://business.wisc.edu/wp-content/uploads/2020/03/Nicholas-Center-Cryptocurrencies-Papers-December-2018.pdf')],
  'events': [('⚠⚠ All-Campus Career & Internship Fair',
              'Wed Sep 16, 2026, Kohl Center. FOR-PROFIT $900 · GOVERNMENT $400 · START-UP/SMALL BUSINESS $300 · '
              'NON-PROFIT $150. One 8-foot table and two chairs. "Organizations must register and submit payment '
              'no later than FRIDAY, AUGUST 28, 2026" to appear in printed guides. THE CLEANEST FULLY-PRICED '
              'COMMERCIAL DOOR IN WISCONSIN AND THE MOST URGENT ITEM IN THIS PACKET. Brandon Spoon, '
              '(608) 262-3921.',
              'https://careerfair.wisc.edu/employers/'),
             ('SuccessWorks Inclusive Community Career & Internship Fair — sponsorship',
              '$1,200 sponsor package: two tables, seating for up to four representatives, "Prime high-traffic '
              'table location at the fair with electrical provided," logo recognition in promotional materials, '
              'signage, emails and online listings. The fair is "open to students of all majors, with interest in '
              'every industry" and NO industry restriction on sponsors is stated. Contact Seng Thao.',
              'https://successworks.wisc.edu/employers/employer-sponsorship-opportunities/'),
             ('⚠ MadHacks — the hackathon route',
              '"The largest hackathon in Wisconsin." 400+ participants in 2025, the biggest turnout in its '
              'history; 24 hours overnight at Morgridge Hall, School of Computer, Data & Information Science. '
              '2025 dates Nov 22–23. ⚠ FALL 2026 DATES NOT YET PUBLISHED — the pattern is the weekend before '
              'Thanksgiving, which in 2026 would be Nov 21–22. Student-run and privately sponsored, so campus '
              'commercial rules do not touch it. Email team@madhacks.io.',
              'https://cai.wisc.edu/2026/01/21/inside-madhacks-the-midwests-premier-hackathon/')],
  'play': 'Madison is the biggest audience in Wisconsin, it has the state\'s only flagship blockchain club '
          '(Badger Blockchain) and a professor who literally teaches the crypto course — and it also has the '
          'tightest expressive-activity carve-out in the state. Do NOT plan to table. UW-6013 says in terms that '
          '"commercial activity... is EXCLUDED" from the visitor-friendly outdoor regime; UW-2058 says free '
          'expression in the Union is limited to "UW-Madison students, staff, or faculty"; UW-6000 routes '
          'non-university use through a sponsoring university DEPARTMENT whose head must physically attend the '
          'whole event; and the Student Organization Fair states flatly that "your organization may not allow a '
          'corporate sponsor to use your table for promotion." There are exactly two doors and both are good. '
          '⚠⚠ THE URGENT ONE: the All-Campus Career & Internship Fair, Wed Sep 16, 2026, Kohl Center — $900 for '
          'a for-profit table, and REGISTRATION AND PAYMENT ARE DUE FRIDAY AUGUST 28, 2026, sixteen days from '
          'today. Call Brandon Spoon at (608) 262-3921 this week; there is no second chance, and it is the only '
          'place in Wisconsin where DGD can stand in front of Madison students entirely lawfully for a published '
          'price. THE BETTER ONE, and the single best door at Madison: Brad Chandler, who teaches FINANCE '
          '615/765 Cryptocurrencies, Blockchain and Digital Assets and who has already run a course in '
          'partnership with a crypto platform (Layer 3) — no phone is published for him, so go through the '
          'Nicholas Center at (608) 262-1550. A guest lecture is non-commercial, free, and puts DGD in front of '
          'exactly the right fifty students. Third, in November, sponsor MadHacks (team@madhacks.io) — 400+ '
          'developers, student-run, entirely outside the campus commercial regime. Skip the Student Org Fair '
          'and skip the Union.',
  'gaps': ['⚠⚠ ALL-CAMPUS CAREER FAIR PAYMENT DEADLINE IS FRI AUG 28, 2026 — sixteen days out, $900 for-profit '
           'tier. Call Brandon Spoon, (608) 262-3921, before anything else in this packet.',
           'Whether FINANCE 615/765 Cryptocurrencies, Blockchain and Digital Assets runs in FALL 2026 — the '
           'catalog says only "Last Taught: Spring 2026" and prints no "Typically Offered" line. Nicholas '
           'Center, (608) 262-1550.',
           '⚠ No direct phone is published for ANY Wisconsin School of Business Finance faculty member, '
           'including Brad Chandler and Randall Wright — 28 faculty, 28 emails, zero numbers. Route through the '
           'Nicholas Center. https://business.wisc.edu/faculty-research/finance-investment-banking/faculty/',
           'The Wisconsin Involvement Network (win.wisc.edu) could NOT be enumerated — the organizations index '
           'returns a landing shell and individual org URLs returned nothing. Whether a second crypto or Web3 '
           'RSO exists outside the Wisconsin School of Business is unconfirmed. SOLI, (608) 263-0365.',
           'Badger Blockchain publishes NO officer names, club email or advisor on any retrievable UW page. Ask '
           'SOLI or Danae Dorsey (danae.dorsey@wisc.edu) who currently runs it. Do not guess.',
           'MadHacks Fall 2026 dates and sponsorship tiers — nothing is published for 2026; madhacks.io still '
           'shows Nov 22–23, 2025. team@madhacks.io.',
           'What "a contract with the appropriate contracting department or building manager" costs for an '
           'outside for-profit under UW-6000 — no rate card exists anywhere on policy.wisc.edu. Jesse Luckey '
           'Winters, (608) 556-7741.',
           'The insurance dollar limit for non-SSLP users — UW-6000 says coverage "may be required" and never '
           'says how much. (608) 556-7741.',
           'Add/drop deadlines for Fall 2026 — the Secretary of the Faculty calendar carries instruction, '
           'recess, exam and commencement dates only. https://registrar.wisc.edu/dates/',
           '⚠ docs.legis.wisconsin.gov SUBSECTION URLs (uws/21/04, uws/21/03) and the ENTIRE ch. UWS 18 landing '
           'page are ROBOTS-BLOCKED, and direct curl to that host returns a proxy 403. UWS 21 came from the '
           'chapter landing page; UWS 18.11(8) came from the Justia mirror. If a campus official disputes the '
           'wording, cite Justia: '
           'https://regulations.justia.com/states/wisconsin/uws/chapter-uws-18/section-uws-18-11/'],
  'note': 'UW-6145 Vendor Permits is a RETIRED policy (eff. 03-01-2000) — the page explicitly directs users to '
          'UW-6140 Service/Vendor Permits instead. Do not cite UW-6145. Also note that the UW-Madison Policy '
          'Library is unusually good: UW-6000 lists nineteen related policies including UW-3030 Revenue '
          'Producing Activities, UW-202 Filming and Commercial Production, UW-2014 Temporary Food Service and '
          'UW-205 Use of Institutional Names, Logos, Symbols — any of which can be turned against a table.'},
 # ---------------------------------------------------------------- 2. UW-MILWAUKEE
 {'state': 'Wisconsin',
  'name': 'University of Wisconsin–Milwaukee',
  'city': 'Milwaukee, WI',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 2,
  'start': 'Wed Sep 2, 2026 ("Instruction Begins September 2, 2026")',
  'adddrop': 'NOT PUBLISHED on the 2026-27 academic year calendar — the Senate calendar carries instruction, '
             'recess, study day, exam and graduation dates only. Get from the Registrar.',
  'fallbreak': 'None separate from Thanksgiving.',
  'thanksgiving': 'Fall Recess Nov 25–29, 2026',
  'lastclass': 'Mon Dec 14, 2026 ("Last Day of Semester Classes"). Study Day Tue Dec 15.',
  'finals': '⚠ Dec 16–19 and Dec 21–23, 2026 (Dec 20 is graduation) — THE LONGEST FALL TERM IN WISCONSIN, '
            'running six days past Madison. Graduation Sun Dec 20. 70 class days total.',
  'cal_url': 'https://uwm.edu/secu/resources/calendars-schedules/academic-year-calendar-2026-27/',
  'cal_status': 'CONFIRMED on the UWM Secretary of the University 2026-27 calendar, cross-confirmed against the '
                'systemwide calendar (Sep 2 – Dec 23). ⚠ The page carries its own caveat: "Dates are subject to '
                'change upon approval of the Senate."',
  'fair': 'UWM Involvement Fair',
  'fair_date': '⚠ FALL 2026 DATE NOT PUBLISHED — AND THE OFFICIAL PAGE IS FIVE YEARS STALE. '
               'uwm.edu/welcome/event/involvement-fair/ still renders "September 14, 2021 @ 11:00 am – 2:00 pm, '
               'Spaights Plaza, 2200 E Kenwood Blvd." That is a 2021 listing, not a 2026 one. The Student '
               'Involvement events feed lists twelve events through Sep 8, 2026 with NO fair among them. '
               'RECURRING PATTERN: Spaights Plaza, roughly 11 a.m.–2 p.m., mid-September. It will post at '
               'uwm.edu/studentinvolvement/ and uwm.edu/welcome/. CALL 414-229-5780.',
  'fair_outside': '⚠ NO PUBLISHED ANSWER for the fair itself, and the campus answer is a flat no: "Outside '
                  'clients may only use an Atrium Booth for the purposes of employment recruitment, with proper '
                  'sponsorship and payment. NO COMMERCIAL SOLICITATION IS PERMITTED." Do not expect a fair table.',
  'fair_cost': 'Not published. Union space costs "vary depending on the event\'s nature, size, scope and other '
               'details" — NO RATE CARD EXISTS ANYWHERE ON THE UWM SITE. Quote by phone only, 414-229-4828.',
  'fair_deadline': 'Not published. Note the Union booth rule that "Lobby booth space may be requested a maximum '
                   'of one month in advance" — so there is a ceiling as well as a floor on how early you can act.',
  'fair_url': 'https://uwm.edu/welcome/event/involvement-fair/',
  'policy': 'UWM Student Union Event Services reservation rules + UWM Student Involvement "Planning an Event" '
            'guidelines; above both, Wis. Admin. Code UWS 18.11(8) and ch. UWS 21',
  'policy_url': 'https://uwm.edu/union/event-services/faqs/',
  'policy_key': "UWM Student Union Event Services (uwm.edu/union/event-services/faqs/): 'To obtain space within "
                "the Student Union you must be an active UWM student organization, UWM department, or you may be "
                "AN OUTSIDE ORGANIZATION THAT HAS BEEN SPONSORED BY A UWM ORGANIZATION.' And: 'You must obtain "
                "sponsorship through a recognized UWM student organization or campus department before you are "
                "allowed to reserve space.' ⚠⚠ THE DECISIVE SENTENCE, VERBATIM: 'OUTSIDE CLIENTS MAY ONLY USE AN "
                "ATRIUM BOOTH FOR THE PURPOSES OF EMPLOYMENT RECRUITMENT, WITH PROPER SPONSORSHIP AND PAYMENT. NO "
                "COMMERCIAL SOLICITATION IS PERMITTED.' An outside entity may buy exactly one thing at UWM: a "
                "recruiting booth. Not a marketing booth. ⚠ ANTI-FRONTING, WITH ONE EXCEPTION THAT CLOSES THE "
                "LOOP (uwm.edu/studentinvolvement/organizations/manage-an-organization/planning-an-event/): "
                "registered student organizations in good standing 'are eligible to use campus space' but CANNOT "
                "'SPONSOR NON-UNIVERSITY GROUPS OR UNQUALIFIED GROUPS FOR THE USE OF UNIVERSITY SPACE, EXCEPT IN "
                "THE UNION BUILDING.' Read the two rules together: the ONLY place an RSO may front for DGD is the "
                "Union, and inside the Union commercial solicitation is precisely what is banned. That is why "
                "UWM ranks last in the state. The state code's sponsorship door at UWS 18.11(8)(d) is open in "
                "law and shut by campus rule. ALSO: 'ONLY STUDENT ORGANIZATIONS are allowed to hold food sale "
                "fundraisers on campus. These fundraisers are not allowed inside any campus buildings and are "
                "only allowed outside' — food sales capped at 5 per semester, one per day, form due 10 days "
                "prior and no more than 6 weeks in advance; outside caterers need Catering Manager approval two "
                "weeks prior. BOOTH MECHANICS: 'An atrium booth is often used by UWM student organization and "
                "departments for information distribution, fundraising, or recruitment'; first-floor booths are "
                "limited to information and bake sales only; a maximum of 4 half-day or 2 full-day reservations "
                "per week; 'LOBBY BOOTH SPACE MAY BE REQUESTED A MAXIMUM OF ONE MONTH IN ADVANCE'; booths must be "
                "staffed by at least one student member; and 'Organizations are required to notify Union "
                "Reservations & Event Planning of any cancellations TWO BUSINESS DAYS IN ADVANCE.' CONTRACTS AND "
                "LEAD TIME — this is the number that kills a September plan made in September: a PAID guest "
                "speaker requires a planning meeting FIVE TO SIX WEEKS AHEAD and a contract A MINIMUM OF 30 DAYS "
                "before the event; even an UNPAID speaker needs a contract 14 days prior. ⚠ NOTABLE ABSENCES — "
                "verified-not-found, NOT verified-permitted: NO RATE CARD, NO INSURANCE REQUIREMENT, NO DEPOSIT "
                "AND NO CANCELLATION-FEE TERMS appear on the FAQ, and no language reaching credit cards, payment "
                "apps or on-site contracts was found. Get the Union rate sheet by phone: 414-229-4828.",
  'sponsor_required': '⚠ YES — AND IT DOES NOT CURE THE PROBLEM. Sponsorship by a UWM student organization or '
                      'department is mandatory before an outside organization may reserve any space. But an RSO '
                      'may only sponsor a non-University group "in the Union Building," and in the Union "no '
                      'commercial solicitation is permitted" and outside clients may use a booth only for '
                      '"employment recruitment." Sponsorship buys you a recruiting booth, nothing more. Do not '
                      'spend three weeks courting a UWM club expecting it to open a marketing table — it cannot.',
  'clubs': [('⚠ NO BLOCKCHAIN / CRYPTO / WEB3 ORGANISATION AT UWM',
             'None found. The Lubar College of Business publishes its full undergraduate org list and there is no '
             'crypto group on it. The campus-wide PantherSync / UWM Presence directory could NOT be enumerated. '
             'Contrast UW-Whitewater, 50 miles west, which has a 110-member blockchain club.',
             'https://uwm.edu/business/students/current/undergraduate/organizations/'),
            ('Student Investment Club (SIC)',
             'Highest-fit club at UWM. "Provides financial markets education and mock investment experience." '
             '⚠ NO EMAIL OR PHONE IS PUBLISHED for this or any other Lubar organisation — the whole page is '
             'names and one-line descriptions. Route through Student Involvement, 414-229-5780.',
             'https://uwm.edu/business/students/current/undergraduate/organizations/'),
            ('Collegiate Entrepreneurs Organization (CEO)',
             'Supports entrepreneurship "with access to successful business founders and competitions." Second '
             'best fit. No contact published.',
             'https://uwm.edu/business/students/current/undergraduate/organizations/'),
            ('Other Lubar College of Business organisations',
             'AIESEC; American Marketing Association; Beta Alpha Psi (Eta Theta Chapter); Beta Gamma Sigma (Delta '
             'Chapter); Delta Sigma Pi; Future Healthcare Executives; Supply Chain Management Association; '
             'Society for Human Resource Management; Women in Business. No emails or phone numbers published for '
             'any of them.',
             'https://uwm.edu/business/students/current/undergraduate/organizations/')],
  'faculty': [('⚠ UWM Student Union — Event Services',
               'BOOKS THE ATRIUM BOOTHS AND HOLDS THE UNPUBLISHED RATE CARD. Student Union Room 300A, 3rd floor. '
               'The office that will tell you, out loud, that no commercial solicitation is permitted — ask them '
               'exactly where the line between "employment recruitment" and "commercial solicitation" sits, '
               'because that line is the entire question at UWM.',
               'UWM Student Union',
               'reservat@uwm.edu · 414-229-4828',
               'https://uwm.edu/union/event-services/faqs/'),
              ('⚠ UWM Student Involvement',
               'Student Union Room 351/355, 2200 East Kenwood Blvd. Owns RSO recognition, the anti-fronting rule, '
               'and the UNPUBLISHED Fall 2026 Involvement Fair date. Summer hours from May 18 are Mon–Fri '
               '10:00 a.m.–3:00 p.m. "Until Fall 2026 Semester." CALL THIS NUMBER TO GET THE FAIR DATE — the '
               'official fair page still shows September 2021.',
               'Division of Student Affairs',
               'activities@uwm.edu · 414-229-5780',
               'https://uwm.edu/studentinvolvement/'),
              ('UWM Dean of Students Office',
               'UWM Student Union Room 345, PO Box 413. Mon–Fri 8:00 a.m.–4:30 p.m. Escalation above Student '
               'Involvement; the dean\'s name is NOT published on the office page.',
               'Division of Student Affairs',
               'dos@uwm.edu · 414-229-4632',
               'https://uwm.edu/deanofstudents/'),
              ('Division of Student Affairs',
               'Above the Dean of Students; also the route to career-fair dates and employer fees, neither of '
               'which UWM publishes.',
               'Division of Student Affairs',
               '414-229-4058 (main line)',
               'https://uwm.edu/studentaffairs/'),
              ('⚠ G. Kevin Spellman',
               'Professor of Practice, Finance; DAVID O. NICHOLAS DIRECTOR OF INVESTMENT MANAGEMENT — runs the '
               'investment-management programme and reaches the students who actually manage money. Note the '
               'MADISON area code on his line: he is reachable outside Milwaukee. ⚠ NOT a crypto researcher; do '
               'not represent him as one.',
               'Lubar College of Business — Finance',
               'spellman@uwm.edu · 608-334-2110',
               'https://uwm.edu/business/people-category/faculty/finance/'),
              ('Lori Craig',
               'Executive in Residence, Finance; DREAM EXCHANGE DIRECTOR — the closest thing at UWM to a '
               'market-structure and capital-formation contact. Direct line.',
               'Lubar College of Business — Finance',
               'craigl@uwm.edu · 414-251-6545',
               'https://uwm.edu/business/people-category/faculty/finance/'),
              ('Lora Reinholz',
               'Teaching Assistant Professor, Finance; Director of the Financial Planning Certificate Program — '
               'reaches the personal-finance cohort, the most receptive audience on this campus for a '
               'sound-money argument. Direct line.',
               'Lubar College of Business — Finance',
               'reinholl@uwm.edu · 414-251-6303',
               'https://uwm.edu/business/people-category/faculty/finance/'),
              ('Lubar College of Business — Finance department',
               'Department main line. Individual direct lines, all confirmed on the staff directory: Carlos Acuna '
               'Silva 414-251-8032 (acunasil@uwm.edu); Michael Farrell 414-251-7372 (farrell1@uwm.edu); Ioannis '
               '(Yianni) Floros, Hans G. Storr Associate Professor, 414-229-4369 (ivfloros@uwm.edu); Xiaoting '
               'Hao 414-229-3662 (haox@uwm.edu); Valeriy Sibilkov 414-229-4369 (sibilkov@uwm.edu); Chad Venne, '
               'Director of the Real Estate Program, 414-251-6654 (cmvenne@uwm.edu); Jiadi Xu 414-251-5871 '
               '(jiadixu@uwm.edu). ⚠ NO UWM FACULTY MEMBER RESEARCHING CRYPTOCURRENCY, BLOCKCHAIN, FINTECH OR '
               'DIGITAL ASSETS COULD BE CONFIRMED — the directory publishes no research interests. DO NOT '
               'REPRESENT ANY OF THEM AS A CRYPTO RESEARCHER.',
               'Lubar College of Business — Finance',
               '414-229-4235 (main line)',
               'https://uwm.edu/business/people-category/faculty/finance/'),
              ('UWM Media Services',
               'Printed on the fall career-fair announcement. Not a decision-maker, but a live number if every '
               'other line fails.',
               'University Relations',
               'media-services-team@uwm.edu · 414-229-7490',
               'https://uwm.edu/news/save-the-dates-fall-internship-and-career-fairs/')],
  'courses': [('(Blockchain / crypto / fintech)',
               'NONE CONFIRMED. No UWM course on cryptocurrency, blockchain, digital assets or fintech could be '
               'found. The Lubar finance faculty directory publishes no research interests, so nothing could be '
               'inferred either. Look up in the UWM academic catalog.',
               'https://catalog.uwm.edu/business/')],
  'events': [('⚠ Fall career fairs — FIVE separate fairs, FALL 2026 DATES NOT PUBLISHED',
              'UWM runs five distinct fairs across three days, all 1:00–4:00 p.m.: Architecture, Engineering, '
              'Conservation & Sciences (Union Wisconsin Room); Software, Data Analytics and IT (Union Wisconsin '
              'Room); Public Impact (Union Ballroom); Global Works (Fireside and MLK Lounges); Business and '
              'Communications (Union Wisconsin Room). ⚠ THE ONLY SOURCE IS AN ARTICLE DATED AUGUST 26, 2025 '
              'GIVING 2025 DATES (Sep 30 – Oct 2, 2025). DO NOT READ THOSE AS 2026 DATES. Employer registration '
              'fees are not published anywhere. Call 414-229-4058.',
              'https://uwm.edu/news/save-the-dates-fall-internship-and-career-fairs/'),
             ('Hackathon — NONE FOUND',
              'No UWM hackathon could be confirmed. Contrast Madison (MadHacks, 400+ participants) 80 miles west.',
              ''),
             ('Winter Involvement Fair',
              'A second, spring-semester fair exists (uwm.edu/studentaffairs/event/winter-involvement-fair/) — '
              'irrelevant to a Fall 2026 tour but worth knowing if the fall window is missed.',
              'https://uwm.edu/studentaffairs/event/winter-involvement-fair/')],
  'play': 'Milwaukee is the second-biggest audience in Wisconsin and it is the HARDEST public campus in the state '
          'to enter lawfully — a 2, and the rating is driven by one sentence: "Outside clients may only use an '
          'Atrium Booth for the purposes of EMPLOYMENT RECRUITMENT, with proper sponsorship and payment. NO '
          'COMMERCIAL SOLICITATION IS PERMITTED." Sponsorship does not fix it: a UWM student organisation "cannot '
          'sponsor non-University groups... EXCEPT IN THE UNION BUILDING," and the Union is exactly where '
          'commercial solicitation is banned. The two rules close the loop, and there is no blockchain or crypto '
          'club here to work around them. Be honest about what this means: DGD cannot market to UWM students on '
          'campus. What DGD CAN lawfully do is recruit — and if DGD has any hiring, internship or ambassador '
          'programme at all, that is the door, because a recruiting booth is expressly permitted. Start with '
          'Union Event Services at 414-229-4828 and ask them to draw the line between "employment recruitment" '
          'and "commercial solicitation" for you, in their words, before you spend money. ⚠ TIME-CRITICAL AND '
          'EASY TO MISS: the Fall 2026 Involvement Fair date is NOT PUBLISHED and the official page still shows '
          'SEPTEMBER 14, 2021 — five years stale. Call Student Involvement at 414-229-5780 to get the real date '
          'before assuming it has passed. Also note the lead times, which are the longest in the state: a paid '
          'speaker needs a planning meeting five to six weeks out and a contract thirty days out; even an unpaid '
          'speaker needs a contract fourteen days out. A plan made in September cannot execute in September at '
          'UWM. If the trip is tight, Milwaukee is the stop to trade for Whitewater, fifty miles west, where the '
          'audience is better and the policy is friendlier.',
  'gaps': ['⚠ FALL 2026 INVOLVEMENT FAIR DATE IS UNPUBLISHED AND THE OFFICIAL PAGE IS FIVE YEARS STALE — '
           'uwm.edu/welcome/event/involvement-fair/ still renders "September 14, 2021 @ 11:00 am - 2:00 pm, '
           'Spaights Plaza." Call Student Involvement, 414-229-5780.',
           '⚠ Where UWM draws the line between "employment recruitment" (permitted for outside clients) and '
           '"commercial solicitation" (not permitted). This single question decides whether Milwaukee is worth a '
           'stop. Union Event Services, 414-229-4828.',
           'The Union rate card — "Costs vary depending on the event\'s nature, size, scope and other details. To '
           'obtain a quote please contact Event Services." NO published rates for atrium booths or rooms. '
           '414-229-4828.',
           'Whether UWM requires insurance, a deposit or cancellation fees from outside clients — NONE of the '
           'three appears anywhere in the FAQ. Absence of published text is not permission. 414-229-4828.',
           'Fall 2026 career-fair dates and employer registration fees — the only source is an article dated '
           'August 26, 2025 carrying 2025 dates. 414-229-4058.',
           'Add/drop deadlines for Fall 2026 — not on the Senate academic-year calendar, which also warns that '
           '"Dates are subject to change upon approval of the Senate." '
           'https://uwm.edu/secu/resources/calendars-schedules/academic-year-calendar-2026-27/',
           'The PantherSync / UWM Presence student-organisation directory could not be enumerated, so the absence '
           'of a crypto club is confirmed only for the Lubar College list. Ask Student Involvement, 414-229-5780.',
           'The UWM Dean of Students name is not published on the office page. 414-229-4632.'],
  'note': 'UWM has the LONGEST fall term in Wisconsin — final exams run to December 23, six days past Madison and '
          'a full month past Lawrence. If a late-semester activity is ever worth doing in this state, Milwaukee '
          'is the only campus where December still has students in it.'},

 # ---------------------------------------------------------------- 3. MARQUETTE
 {'state': 'Wisconsin',
  'name': 'Marquette University',
  'city': 'Milwaukee, WI',
  'type': 'Private (religious)',
  'tier': 'B — Regional',
  'access': 3,
  'start': '⚠ Mon Aug 31, 2026 — THE EARLIEST START IN WISCONSIN, two days ahead of the entire UW system and '
           'fifteen days ahead of Lawrence.',
  'adddrop': '09/08/2026 for most undergraduate sessions — varies by program (Undergraduate, Graduate, Health '
             'Science, Dental, Law all run different tables).',
  'fallbreak': 'Oct 1–2 AND Oct 22–23, 2026 — two separate short breaks, varying by program (Dental School '
               'midterm break Oct 23). Marquette is the only Wisconsin campus with two fall breaks.',
  'thanksgiving': '11/25/2026 – 11/29/2026',
  'lastclass': 'Sat Dec 12, 2026 for most sessions (some run to Dec 19).',
  'finals': 'Dec 14–19, 2026 for most programs; Law School exams Dec 7–18. Winter break 12/20/2026 – 1/18/2027. '
            'Mid-year degree conferral 01/08/2027 — no fall commencement ceremony date is published.',
  'cal_url': 'https://www.marquette.edu/central/registrar/2026-fall-academic-calendar.php',
  'cal_status': 'CONFIRMED on the Marquette Central registrar\'s own 2026 Fall Academic Calendar. Note that dates '
                'genuinely differ by school — the calendar is a set of parallel tables, not one calendar.',
  'fair': 'O-Fest 2026 (Organization Fest)',
  'fair_date': 'Thu Sep 10, 2026, 4:00–7:00 p.m., Central Mall. Registration opened April 2026.',
  'fair_outside': '⚠ NO — "Student organizations and campus departments," ONE TABLE EACH. Two separate '
                  'registration forms exist (marquette.presence.io/form/o-fest-2026-student-org-registration and '
                  '.../o-fest-2026-university-department-registration) and there is no third form for anyone '
                  'else. The article adds: "Organizations interested in participating should read the form '
                  'description, as minor changes will be made to table placements next year."',
  'fair_cost': 'Not mentioned for O-Fest. The paid external alternative is an AMU Space Agreement — billed for '
               'room, equipment and labour with a 75% deposit, and NO RATE CARD IS PUBLISHED.',
  'fair_deadline': 'Not specified in the announcement. Registration opened April 2026 via marquette.presence.io. '
                   'Call AMU Student Engagement Services, (414) 288-7250.',
  'fair_url': 'https://today.marquette.edu/2026/04/o-fest-2026-registration-open/',
  'policy': 'AMU Event Services Reservations Policy and AMU Space Reservation Policy; plus the AMU student-'
            'organization fundraising policy',
  'policy_url': 'https://www.marquette.edu/event-services/amu-space-reservation-policy.php',
  'policy_key': "⚠ MARQUETTE IS PRIVATE AND JESUIT. Wis. Admin. Code chs. UWS 18 and 21 and Regent Policy "
                "Document 4-21 DO NOT BIND IT. It has NO public-forum obligation of any kind and can exclude DGD "
                "for any reason or none. Do not assume it resembles the UW campuses; in places it is stricter. "
                "AMU Event Services Reservations Policy / AMU Space Reservation Policy "
                "(marquette.edu/event-services/): ⚠⚠ ANTI-FRONTING, VERBATIM — 'UNIVERSITY DEPARTMENTS AND "
                "STUDENT ORGANIZATIONS MAY NOT RESERVE SPACE OR EQUIPMENT FOR, OR ON THE BEHALF OF, AN OUTSIDE "
                "ORGANIZATION, PERSON OR FOR A PERSONAL EVENT except in the case of a hosted event.' Enforcement: "
                "'IF FRONTING IS DISCOVERED, NON-UNIVERSITY RENTAL RATES WILL APPLY.' ⚠ COMMERCIAL SOLICITATION "
                "BAN, AND NOTE HOW BROAD IT IS — prohibited activities include 'COMMERCIAL SOLICITATIONS "
                "(INCLUDING DISTRIBUTING ANY KIND OF WRITTEN OR PRINTED MATERIALS, SALES OF GOODS OR SERVICES, "
                "INCLUDING FOODS, ETC.) ON UNIVERSITY PROPERTY UNLESS PRIOR APPROVAL HAS BEEN PROVIDED.' Handing "
                "a student a flyer is commercial solicitation at Marquette. Solicitations promoting alcohol or "
                "tobacco are barred outright. ⚠⚠ PAYMENT CREDENTIALS — THE MOST DIRECTLY RELEVANT SENTENCE FOUND "
                "ANYWHERE IN WISCONSIN, from the AMU student-organization fundraising policy "
                "(marquette.edu/alumni-memorial-union/student-organizations/policies-fundraising.php): "
                "'FUNDRAISERS INVOLVING CREDIT CARDS (E.G., CREDIT CARD APPLICATIONS) WILL NOT BE APPROVED.' "
                "Marquette has written a rule about handing students financial-product signups on campus. Read "
                "narrowly it covers credit cards; read as Marquette will read it, it covers an on-the-spot wallet "
                "install, an exchange referral or any account opening. ASSUME IT REACHES DGD. Also: 'NO RAFFLES, "
                "LOTTERIES OR SWEEPSTAKES MAY BE HELD' — which kills the airdrop-style giveaway. 'Only recognized "
                "and registered student organizations may sponsor a fundraising activity'; 'AMU Student "
                "Engagement Services must approve all fundraising activities... through completion and acceptance "
                "of an Event Registration Form'; and 'Solicitation of a student organization's own members does "
                "not require approval from AMU Student Engagement Services. SOLICITATIONS OF ANY PERSON OR ENTITY "
                "OTHER THAN A STUDENT ORGANIZATION MEMBER... REQUIRE REVIEW AND APPROVAL.' THE PAID EXTERNAL "
                "ROUTE DOES EXIST AND IS DOCUMENTED: Non-University Groups may request space 'up to twelve (12) "
                "months in advance'; a Marquette University Space Agreement must be executed on confirmation; "
                "such groups 'WILL BE BILLED FOR ROOM, EQUIPMENT AND LABOR' with no complimentary services; and "
                "⚠⚠ THE MONEY TERM: 'A DEPOSIT OF 75% OF THE ESTIMATED CHARGES WILL BE DUE UPON RECEIPT. BALANCE "
                "PAYMENT WILL BE DUE TEN (10) BUSINESS DAYS PRIOR TO THE EVENT.' Priority order is explicit: "
                "'University Departments and Student Organizations requests will have priority over "
                "Non-University Group requests.' University departments may book annual events five years ahead "
                "and hold two tentative dates for 14 days; student organizations may book one year ahead. "
                "⚠ NOTABLE ABSENCES — verified-not-found, NOT verified-permitted: NO INSURANCE REQUIREMENT OR "
                "DOLLAR LIMIT is published, NO RATE CARD is published, and no cancellation-penalty schedule was "
                "found. Get all three in writing from AMU Event Services, (414) 288-7202, before signing a Space "
                "Agreement with a 75% up-front deposit.",
  'sponsor_required': '⚠ NO — AND THE CLUB ROUTE IS AFFIRMATIVELY BLOCKED. "University departments and student '
                      'organizations may not reserve space or equipment for, or on the behalf of, an outside '
                      'organization, person or for a personal event," and fronting, if discovered, re-prices the '
                      'booking at non-university rates. The only compliant channel is a direct Marquette '
                      'University Space Agreement as a Non-University Group, at the lowest scheduling priority, '
                      'with 75% of estimated charges due on receipt — plus separate prior approval from AMU '
                      'Student Engagement Services for anything resembling solicitation.',
  'clubs': [('⚠ Marquette Blockchain Lab — EXISTENCE CONFIRMED, ROSTER ALMOST CERTAINLY STALE',
             '"A student-run initiative" and "virtual, interdisciplinary laboratory" to "facilitate education and '
             'innovation in the blockchain space," working toward "implementation of distributed ledger '
             'solutions" to reduce waste and fraud. ⚠ THE LAB\'S OWN SITE, marquetteblockchain.com, IS '
             'ROBOTS-BLOCKED to research tooling and its DNS did not resolve for robots.txt. The only retrievable '
             'source is a Marquette Innovation PDF naming President Clayton Boehm and Director of Events '
             'Gabriella Suliga at clayton@marquetteblockchain.com — STUDENT ROSTERS ROTATE ANNUALLY AND THIS ONE '
             'IS OLD. DO NOT COLD-CALL THOSE NAMES. Confirm the Lab still exists via marquette.presence.io or AMU '
             'Student Engagement Services, (414) 288-7250.',
             'https://www.marquette.edu/innovation/documents/ec2010_blockchain_lab.pdf'),
            ('⚠ Marquette Investment Club',
             'THE BEST-FIT LIVE CLUB AT MARQUETTE. Focuses on investment methods and strategies, particularly '
             'ETFs, and manages a real portfolio — "approximately $25,000 net worth across ~20 ETF positions." '
             'Students who already hold ETFs are the right room for a bitcoin-ETF conversation, and Wisconsin\'s '
             'own pension fund owns $164 million of them. No email or advisor published.',
             'https://www.marquette.edu/business/finance/student-organizations.php'),
            ('Financial Management Association (FMA)',
             'Speakers and professionals on finance topics and ethical decision-making; hosts "The Ins and Outs '
             'of Wall Street" seminar for interview preparation. No email or advisor published.',
             'https://www.marquette.edu/business/finance/student-organizations.php'),
            ('Commercial Banking Club',
             '"Explore and discover the vast opportunities in the Commercial Banking industry" — networking with '
             'professional bankers, internship placement. Published contact is an Instagram handle only, '
             '@marquette_commercialbanking.',
             'https://www.marquette.edu/business/finance/student-organizations.php'),
            ('Real Estate Club of Marquette (RECM); Marquette Economics Association',
             'RECM runs weekly speakers, property site visits and shadowing. The Economics Association is the '
             'department\'s student organisation. Neither publishes an email.',
             'https://www.marquette.edu/business/economics/student-organization.php')],
  'faculty': [('⚠ AMU Event Services',
               'AMU Room 245. BOOKS NON-UNIVERSITY SPACE AND WROTE THE ANTI-FRONTING RULE. The office to ask for '
               'the rate card, the insurance requirement and the cancellation schedule — none of which Marquette '
               'publishes — before committing to a 75%-deposit Space Agreement. NO EMAIL ADDRESS IS LISTED for '
               'this office anywhere in the policy documents; phone or in person only.',
               'Alumni Memorial Union',
               '(414) 288-7202 · no email published — phone or AMU 245 in person',
               'https://www.marquette.edu/event-services/amu-space-reservation-policy.php'),
              ('⚠ AMU Student Engagement Services',
               '1442 W. Wisconsin Avenue. APPROVES ALL FUNDRAISING AND ALL SOLICITATION, and enforces the rule '
               'that "fundraisers involving credit cards will not be approved." The person who decides whether a '
               'wallet signup counts. Coordinator: Stephanie Dooge. Also the office to ask whether the Marquette '
               'Blockchain Lab is still a live registered organisation.',
               'Alumni Memorial Union',
               '(414) 288-7250',
               'https://www.marquette.edu/alumni-memorial-union/student-organizations/policies-fundraising.php'),
              ('Marquette Career Center',
               'Runs the Fall Career & Internship Fair, "the largest on-campus recruiting event of the year," '
               'split into a Non-Technical Day and a Technical Day. ⚠ DATES AND EMPLOYER FEES ARE HANDSHAKE-ONLY '
               'AND NOT PUBLISHED ON THE OPEN WEB — this number is the only way to get them.',
               'Career Center',
               'recruiting@marquette.edu · (414) 288-7423',
               'https://www.marquette.edu/career-center/employers/career-fairs.php'),
              ('Department of Finance',
               'Reaches the Investment Club, FMA, Commercial Banking Club and Real Estate Club cluster — none of '
               'which publishes its own contact. Department main line.',
               'College of Business Administration',
               '(414) 288-7142 (main line)',
               'https://www.marquette.edu/business/finance/student-organizations.php'),
              ('O-Fest organisers (Office of Engagement and Inclusion)',
               'Named contact for O-Fest 2026 registration, Thu Sep 10, 4–7 p.m., Central Mall. NO PHONE IS '
               'PUBLISHED for this address — email only; use AMU Student Engagement Services, (414) 288-7250, if '
               'the email goes unanswered.',
               'Office of Engagement and Inclusion',
               'engaged@marquette.edu · no number published — look up here, or (414) 288-7250',
               'https://today.marquette.edu/2026/04/o-fest-2026-registration-open/'),
              ('(Blockchain / crypto / fintech faculty)',
               'NOT CONFIRMED — no Marquette faculty member working on blockchain, cryptocurrency, digital assets '
               'or fintech could be confirmed on a live page, and the Blockchain Lab document names no faculty '
               'instructor or advisor at all. Look up in the College of Business Administration directory.',
               'College of Business Administration',
               'no individual confirmed — look up here, or Finance dept (414) 288-7142',
               'https://www.marquette.edu/business/')],
  'courses': [('(Blockchain / crypto / fintech)',
               'NONE CONFIRMED. No Marquette course on blockchain or cryptocurrency could be found in '
               'bulletin.marquette.edu/course-descriptions/. The blockchain activity at Marquette is a student '
               'initiative, not a curriculum.',
               'https://bulletin.marquette.edu/course-descriptions/')],
  'events': [('⚠ Fall Career & Internship Fair — DATES AND FEES NOT PUBLISHED',
              '"Held annually in September," "the largest on-campus recruiting event of the year," run over two '
              'days: a Non-Technical Day (business, communications, government, non-profit, healthcare, social '
              'services, post-grad/year of service) and a Technical Day (engineering, IT and technical fields). '
              '⚠ "Details and registration will be available in Handshake each year" — nothing is on the open '
              'web. Call (414) 288-7423.',
              'https://www.marquette.edu/career-center/employers/career-fairs.php'),
             ('Discovery World Hackathon — UNVERIFIED',
              '$10,000 in prizes, promoted through Marquette Today in January 2026. Hosted at Discovery World in '
              'Milwaukee, not run by Marquette. ⚠ DETAILS UNVERIFIED — the article 302-redirects HTTPS to HTTP '
              'and was not fully retrieved. Hackathons are the one route that sidesteps Marquette\'s '
              'commercial-solicitation and credit-card rules entirely, so this is worth a phone call.',
              'https://today.marquette.edu/2026/01/compete-for-10000-in-the-discovery-world-hackathon/'),
             ('O-Fest 2026',
              'Thu Sep 10, 2026, 4:00–7:00 p.m., Central Mall. Student organizations and campus departments only, '
              'one table each. Useful as a scouting visit to see which clubs are actually alive — walking the '
              'mall is not solicitation — but not as a tabling opportunity.',
              'https://today.marquette.edu/2026/04/o-fest-2026-registration-open/')],
  'play': 'Marquette starts Aug 31 — the earliest campus in Wisconsin, already in session as you read this — and '
          'it is private, which cuts both ways: no public-forum obligation protects DGD, but no state '
          'administrative code constrains Marquette either, so everything is negotiable with the right office. '
          'The written rules are the harshest in the state on exactly the things DGD does. Commercial '
          'solicitation is defined to include "distributing any kind of written or printed materials," so a '
          'flyer is a violation without prior approval; "fundraisers involving credit cards (e.g., credit card '
          'applications) will not be approved," which is the closest thing to a payment-credentials rule found '
          'anywhere in Wisconsin and should be read as reaching on-the-spot wallet installs; and raffles, '
          'lotteries and sweepstakes are banned outright, which kills a giveaway. The club route is closed by an '
          'explicit anti-fronting clause with an enforcement penalty. THE ONE COMPLIANT DOOR is a direct '
          'Marquette University Space Agreement as a Non-University Group — call AMU Event Services at '
          '(414) 288-7202 — but go in knowing that 75% of the estimated charges is due on receipt, that no rate '
          'card, insurance requirement or cancellation schedule is published anywhere, and that you will have '
          'the lowest scheduling priority on campus. GET ALL THREE IN WRITING BEFORE PAYING ANYTHING. The '
          'genuinely interesting lead here is the Marquette Blockchain Lab, a student-run interdisciplinary '
          'group — but its website is robots-blocked, the only roster available is years old, and cold-calling '
          'those names would burn the introduction. Ask AMU Student Engagement Services at (414) 288-7250 '
          'whether the Lab is still registered and who runs it now. Second-best live club is the Marquette '
          'Investment Club, which manages a real ~$25,000 portfolio across roughly twenty ETF positions — '
          'students who already hold ETFs, in a state whose pension fund holds $164 million of bitcoin ETFs. '
          'That is the conversation. Milwaukee gets you Marquette and UWM in one day; Marquette is the better '
          'of the two.',
  'gaps': ['⚠ Whether the Marquette Blockchain Lab still exists and who leads it. marquetteblockchain.com is '
           'ROBOTS-BLOCKED and did not resolve; the only roster (Clayton Boehm, Gabriella Suliga) comes from an '
           'undated Marquette Innovation PDF and is almost certainly stale. AMU Student Engagement Services, '
           '(414) 288-7250, or marquette.presence.io.',
           '⚠ Whether "fundraisers involving credit cards (e.g., credit card applications) will not be approved" '
           'reaches crypto wallet installs, exchange referrals or on-site account openings. This is the single '
           'most important question at Marquette and only AMU Student Engagement Services can answer it: '
           '(414) 288-7250.',
           '⚠⚠ THE AMU RATE CARD DOES NOT EXIST ON THE OPEN WEB. Non-University Groups are "billed for room, '
           'equipment and labor" and owe a 75% DEPOSIT ON RECEIPT against an estimate nobody can see in advance. '
           'Get the rate sheet before signing. (414) 288-7202.',
           'Insurance requirements and dollar limits for Non-University Groups — not published in either AMU '
           'policy document. (414) 288-7202.',
           'The cancellation-penalty schedule for a Non-University Group Space Agreement — not published. '
           '(414) 288-7202.',
           'Fall Career & Internship Fair dates and employer registration fees — "available in Handshake each '
           'year" and nowhere else. (414) 288-7423.',
           'O-Fest registration deadline — not stated in the announcement. engaged@marquette.edu or '
           '(414) 288-7250.',
           'Discovery World Hackathon details — the Marquette Today article 302-redirects HTTPS to HTTP and was '
           'not retrieved. Hackathons are the cleanest bypass of Marquette\'s rules, so close this gap.',
           'No Marquette blockchain, crypto or fintech FACULTY member could be confirmed, and no such course '
           'exists in the bulletin. https://www.marquette.edu/business/'],
  'note': 'Marquette runs genuinely different calendars per school — Undergraduate, Graduate, Health Science, '
          'Dental and Law each have their own add/drop, break and exam dates, and Law exams start a full week '
          'earlier (Dec 7). Confirm which population you are targeting before fixing a date. Also note the two '
          'separate fall breaks (Oct 1–2 and Oct 22–23), unique in Wisconsin — both are dead days on campus.'},
 # ---------------------------------------------------------------- 4. UW-EAU CLAIRE
 {'state': 'Wisconsin',
  'name': 'University of Wisconsin–Eau Claire',
  'city': 'Eau Claire, WI',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 4,
  'start': 'Wed Sep 2, 2026',
  'adddrop': 'NOT PUBLISHED on the detailed 2026-2027 academic calendar PDF, which carries instructional-day '
             'counts, recess, exam and commencement dates only. Get from Blugold Central, '
             'https://www.uwec.edu/offices-services/blugold-central/academic-planning/academic-and-registration-calendars',
  'fallbreak': 'Fall Recess Nov 25–27, 2026, verbatim from the calendar: "25 - Fall Recess begins-No classes / '
               '26 - Thanksgiving Day Holiday-University closed / 27 - No classes / 30 - Classes Resume." No '
               'separate October break.',
  'thanksgiving': 'Thu Nov 26, 2026 — university closed; contiguous with Fall Recess Nov 25–27.',
  'lastclass': 'Mon Dec 14, 2026. No formal study day is designated between the last class day and finals.',
  'finals': 'Dec 15–21, 2026. Commencement Sat Dec 19; degree confer date Dec 21.',
  'cal_url': 'https://www.uwec.edu/sites/default/files/2024-07/2026-2027_Academic_Calendar.pdf',
  'cal_status': 'CONFIRMED on the UWEC Detailed Academic Calendar 2026-2027 PDF, cross-confirmed against the '
                'systemwide calendar (Sep 2 – Dec 21).',
  'fair': "Blu's Organizations Bash (\"BOB\")",
  'fair_date': 'Wed Sep 9, 2026, 11:00 a.m. – 1:00 p.m., Central Campus Mall (rain backup: Ojibwe & Dakota '
               'Ballrooms, Davies Center 3rd floor). Sep 9, 2026 IS a Wednesday and the page metadata shows a '
               'July 13, 2026 update — CURRENT, not stale.',
  'fair_outside': '⚠ NO — VERBATIM: "ONLY OFFICIALLY REGISTERED UWEC STUDENT ORGANIZATIONS ARE ELIGIBLE TO '
                  'PARTICIPATE IN THE BOB EVENT." Outside and community organisations are not permitted. The '
                  'answer is unambiguous and there is no vendor tier for this event.',
  'fair_cost': 'Not published for BOB. Separately, the campus solicitation policy states that "non-student '
               'individuals/groups and unaffiliated students WILL BE CHARGED A FEE for use of any University '
               'structure and/or grounds" — the fee exists, the amount is not published anywhere. Ask Jake '
               'Serwe, 715-836-4150.',
  'fair_deadline': 'Registration for student organisations opened April 1, 2026. Irrelevant to DGD, which is '
                   'ineligible. The deadline that matters is the solicitation permission itself — no lead time '
                   'is published; ask the Director of University Centers.',
  'fair_url': 'https://www.uwec.edu/offices-services/activities-involvement-leadership/student-organizations-uwec/blus-organizations',
  'policy': 'UW-Eau Claire "Policies: Solicitation on University Premises" (Knowledge Base), plus the Risk '
            'Management Facility Use & Insurance requirements; above both, Wis. Admin. Code UWS 18.11(8)',
  'policy_url': 'https://kb.uwec.edu/articles/policies-solicitation-on-university-premises',
  'policy_key': "UW-Eau Claire, 'Policies: Solicitation on University Premises' "
                "(kb.uwec.edu/articles/policies-solicitation-on-university-premises) — LAST UPDATED TUESDAY, "
                "MARCH 31, 2026, a live current document, not a legacy one. NO POLICY NUMBER IS PRINTED. ⚠ THE "
                "DEFINITION IS THE WIDEST IN WISCONSIN: solicitation means 'SELLING, PEDDLING, AND/OR "
                "DISTRIBUTION OF MATERIAL, FREE OR OTHERWISE.' Handing out a free sticker is solicitation at "
                "UWEC. THE OPERATIVE RESTRICTION: 'NO SUCH USE OF UNIVERSITY STRUCTURES AND/OR GROUNDS WILL BE "
                "PERMITTED WITHOUT REGISTRATION AND PERMISSION OF THE APPROPRIATE OFFICE.' The approval routing "
                "is unusually specific and worth knowing before you call the wrong person: requests go to the "
                "DIRECTOR OF UNIVERSITY CENTERS (residence halls are the exception and go to the Student "
                "Programs Coordinator); ACADEMIC BUILDINGS require VICE CHANCELLOR approval; GROUNDS require "
                "ASSISTANT CHANCELLOR approval. THE FEE: 'NON-STUDENT INDIVIDUALS/GROUPS AND UNAFFILIATED "
                "STUDENTS WILL BE CHARGED A FEE FOR USE OF ANY UNIVERSITY STRUCTURE AND/OR GROUNDS' — the fee is "
                "mandatory and the amount is NOT PUBLISHED. ⚠ STUDENT-DATA CLAUSE, DIRECTLY RELEVANT TO WALLET "
                "SIGN-UPS AND EMAIL CAPTURE: 'LISTS OF NAMES, ADDRESSES, OFFICIAL UNIVERSITY RECORDS, OR ANY "
                "OTHER INFORMATION ABOUT UNIVERSITY STUDENTS WILL NOT BE MADE AVAILABLE TO NON-UNIVERSITY "
                "INDIVIDUALS OR ORGANIZATIONS WITHOUT APPROVAL OF THE CHANCELLOR.' That governs what the "
                "university will hand you; ask explicitly whether it also governs what you may collect at a "
                "table. INSURANCE — UWEC PUBLISHES ACTUAL NUMBERS, WHICH ALMOST NO ONE ELSE IN THIS PACKET DOES "
                "(uwec.edu/risk-management-safety/facility-use/, non-sponsored events, via the TULIP program): "
                "COMMERCIAL GENERAL LIABILITY 'EACH OCCURRENCE $1,000,000' and 'GEN. AGGR. INCL. PRDTS/CO "
                "$2,000,000'; Sexual Abuse/Misconduct $1,000,000 (when applicable); Professional Liability "
                "$1,000,000 (when applicable); Fire Legal $100,000; Liquor Liability $1,000,000; Automobile "
                "Combined Single Limit $1,000,000. ADDITIONAL INSURED WORDING, use it verbatim on the "
                "certificate: 'BOARD OF REGENTS OF THE UNIVERSITY OF WISCONSIN SYSTEM, ITS OFFICERS, EMPLOYEES, "
                "AND AGENTS.' 'A Certificate of Insurance will be emailed to both you and UW-Eau Claire Risk "
                "Management' when purchased through TULIP. ⚠ NOTABLE ABSENCES — verified-not-found, NOT "
                "verified-permitted: NO ANTI-FRONTING CLAUSE was found; NO CLAUSE FORBIDDING RSOs FROM "
                "SPONSORING OUTSIDE GROUPS was found; NO DEPOSIT OR CANCELLATION TERMS were found; and NO "
                "LANGUAGE REACHING CREDIT CARDS, PAYMENT APPS OR ON-SITE CONTRACTS was found. THE COUNTERWEIGHT "
                "THAT LIFTS UWEC TO A 4: University Centers separately advertises 'CUSTOMIZABLE PARTNERSHIP "
                "OPPORTUNITIES INCLUDING NAMING RIGHTS, EVENT SPONSORSHIP, DIGITAL DISPLAYS, ELEVATOR WRAPS AND "
                "TABLE TENTS' against a building with 'over 1 million annual visits', with a NAMED CONTACT — "
                "that is a commercial-access menu in everything but name. https://www.uwec.edu/offices-services/university-centers",
  'sponsor_required': 'NO — permission, not sponsorship. The policy requires "registration and permission of the '
                      'appropriate office," names which officer approves which kind of space, and says a fee '
                      'will be charged to non-students. No anti-fronting clause and no bar on RSOs sponsoring '
                      'outside groups could be found, so the UWS 18.11(8)(d) club route is also available in '
                      'principle — but the direct paid route is cleaner and UWEC has a named person selling it. '
                      'Confirm the absence of a fronting rule explicitly at 715-836-4150 before relying on it.',
  'clubs': [('⚠ NO BLOCKCHAIN OR CRYPTOCURRENCY CLUB AT UW-EAU CLAIRE',
             'Verified absent from the College of Business student-organizations page, which lists eighteen '
             'groups and no crypto group among them. The Blugold Connect campus-wide directory '
             '(blugoldconnect.uwec.edu) was not enumerable, so absence is confirmed for the business college '
             'only. Activities, Involvement and Leadership oversees 200+ organisations — ask them at '
             '715-836-4833.',
             'https://www.uwec.edu/activities-involvement-leadership/student-clubs-organizations/'),
            ('Financial Management Association (FMA)',
             'Highest-fit club at UWEC. ⚠ NO ADVISOR NAME, ORGANISATION EMAIL OR PHONE IS PUBLISHED for this or '
             'any other College of Business organisation — the page is names only, with a Google Sheets link to '
             'meeting times that was not retrievable. College of Business main line 715-836-5509.',
             'https://www.uwec.edu/academics/colleges/college-business/student-organizations-business'),
            ("Blu's Gold Financial Management",
             'A student-managed fund group — the second-best fit. No advisor or contact published.',
             'https://www.uwec.edu/academics/colleges/college-business/student-organizations-business'),
            ('Student Economics Association (SEA)',
             'The economics-department student organisation — the right room for a monetary argument. No advisor '
             'or contact published.',
             'https://www.uwec.edu/academics/colleges/college-business/student-organizations-business'),
            ('Blugold Innovation',
             'The entrepreneurship organisation. No advisor or contact published.',
             'https://www.uwec.edu/academics/colleges/college-business/student-organizations-business'),
            ('Other College of Business organisations (lower fit)',
             'Beta Alpha Psi Honorary; Student Accounting Society; Beta Gamma Sigma Honorary; Business '
             'Association of Multicultural Students; College of Business Student Advisory Council; Collegiate '
             'DECA; American College of Health Care Administrators; Leadership & Technology; International '
             'Business Student Professionals; SHRM; Blugold Student Leadership and Management; American '
             'Marketing Association; Pi Sigma Epsilon Sales and Marketing; APICS. None publishes a contact.',
             'https://www.uwec.edu/academics/colleges/college-business/student-organizations-business')],
  'faculty': [('⚠ Jake Serwe',
               'THE SINGLE MOST USEFUL NUMBER AT UW-EAU CLAIRE. Named contact for NON-UNIVERSITY GROUP SPACE '
               'RESERVATIONS, TABLING, AND UNIVERSITY CENTERS PARTNERSHIPS — the person who sells the "naming '
               'rights, event sponsorship, digital displays, elevator wraps and table tents" menu against a '
               'building with over a million visits a year. Ask him for the tabling fee, which the policy '
               'mandates and never quantifies. Direct line.',
               'University Centers',
               'serwej@uwec.edu · 715-836-4150',
               'https://www.uwec.edu/offices-services/university-centers'),
              ('University Centers / Davies Student Center',
               '77 Roosevelt Avenue. The DIRECTOR OF UNIVERSITY CENTERS is the officer the solicitation policy '
               'names as the approver for most campus solicitation requests — but the director is not named on '
               'the page. Houses Activities & Leadership, Blugold Card Services, Dining, Event Services, Student '
               'Senate, University Activities Commission and the Bookstore. Summer building hours through Aug 28, '
               '2026 are Mon–Fri 7 a.m.–5 p.m.',
               'University Centers',
               'campusinfo@uwec.edu · 715-836-4636 (main line)',
               'https://www.uwec.edu/offices-services/university-centers'),
              ('Activities, Involvement and Leadership',
               'Davies Student Center 222. Runs Blu\'s Organizations Bash and oversees 200+ student '
               'organisations. The office to ask whether any crypto or blockchain club exists outside the '
               'business college — the campus-wide directory is not machine-readable. ⚠ NO INDIVIDUAL STAFF '
               'NAMES OR DIRECT PHONES ARE PUBLISHED on the office page.',
               'Division of Student Affairs',
               'activities@uwec.edu · 715-836-4833 (main line)',
               'https://www.uwec.edu/offices-services/activities-involvement-leadership/'),
              ('College of Business',
               'Schneider Social Science Hall 119, 1702 Park Avenue. Reaches FMA, Blu\'s Gold Financial '
               'Management, the Student Economics Association and Blugold Innovation — none of which publishes a '
               'contact of its own. Department main line.',
               'College of Business',
               'cob@uwec.edu · 715-836-5509 (main line)',
               'https://www.uwec.edu/academics/colleges/college-business/student-organizations-business'),
              ('Career Services / Advising, Retention & Career Center (ARCC)',
               'Vicki Lord Larson Hall 2100, 105 Garfield Ave. Runs five Fall 2026 fairs including the '
               'Actuarial, Accounting and Finance Career Fair on Sep 23 — the highest-fit audience at UWEC. '
               '⚠ EMPLOYER REGISTRATION COSTS ARE NOT PUBLISHED FOR ANY OF THE FIVE. NO named staff with direct '
               'phones are listed; a separate staff directory page is referenced but was not retrieved.',
               'Career Services',
               'arcc@uwec.edu · 715-836-3487 (main line)',
               'https://www.uwec.edu/offices-services/advising-retention-career-center/career-services'),
              ('Risk Management, Safety & Sustainability',
               'Owns the TULIP insurance requirement and receives the certificate of insurance. NO PHONE NUMBER '
               'AND NO STAFF NAMES ARE PUBLISHED on the facility-use page — look up here, or route through '
               'University Centers at 715-836-4636.',
               'Risk Management, Safety & Sustainability',
               'no number published — look up here, or 715-836-4636',
               'https://www.uwec.edu/risk-management-safety/facility-use/'),
              ('(Blockchain / crypto / fintech / monetary economics faculty)',
               'NOT CONFIRMED — no UW-Eau Claire faculty member working on digital assets, blockchain, fintech or '
               'monetary economics could be confirmed on a live page. Consistent with the curriculum, which has '
               'no such course. Look up in the College of Business and Economics directories.',
               'College of Business',
               'cob@uwec.edu · no individual confirmed — 715-836-5509',
               'https://www.uwec.edu/academics/colleges/college-business')],
  'courses': [('(Blockchain / crypto / fintech)',
               '⚠ VERIFIED ABSENT, not merely unfound. The full UW-Eau Claire Finance (FIN) course catalog was '
               'reviewed and contains NO course on cryptocurrency, blockchain, digital assets or fintech. The '
               'catalog runs Principles of Finance, Financial Markets and Institutions, Investments, '
               'International Financial Management, Derivative Securities and Portfolio Management. This is a '
               'campus with finance students and no digital-asset curriculum at all — an opening for a guest '
               'lecture, not a barrier.',
               'https://catalog.uwec.edu/courses/fin/')],
  'events': [('⚠ Actuarial, Accounting and Finance Career Fair',
              'Wed Sep 23, 2026 — THE HIGHEST-FIT AUDIENCE AT UWEC, and the fair most worth paying for if the '
              'fee turns out to be reasonable. ⚠ EMPLOYER REGISTRATION COST NOT PUBLISHED. Call 715-836-3487.',
              'https://www.uwec.edu/offices-services/advising-retention-career-center/career-services'),
             ('All Majors Career Fair + Science and Tech Breakfast',
              'BOTH on Wed Sep 30, 2026 — the same day, so choose. Also Part-Time Job Fair Fri Sep 11, 2026 and '
              'Health Career, Professional & Graduate School Fair Wed Oct 21, 2026. ⚠ EMPLOYER FEES NOT '
              'PUBLISHED FOR ANY OF THEM.',
              'https://www.uwec.edu/offices-services/advising-retention-career-center/career-services'),
             ('Hackathon — NONE FOUND',
              'No UW-Eau Claire hackathon could be confirmed.',
              '')],
  'play': 'Eau Claire is the most quietly workable regional campus in Wisconsin and almost nobody would guess '
          'it. The solicitation policy is the broadest in the state — it defines solicitation as "selling, '
          'peddling, and/or distribution of material, FREE OR OTHERWISE," so even free swag needs permission — '
          'but it is also the most honest: it names exactly which officer approves which kind of space, it says '
          'plainly that non-students "will be charged a fee," and it was last updated March 31, 2026, so it is '
          'live and someone maintains it. Better still, University Centers openly sells commercial access: '
          '"customizable partnership opportunities including naming rights, event sponsorship, digital displays, '
          'elevator wraps and table tents" against a building with over a million visits a year. CALL JAKE '
          'SERWE AT 715-836-4150. He is the named contact for non-university space, tabling and partnerships, '
          'and he is the person who can tell you the tabling fee that the policy mandates and never quantifies. '
          'Budget for insurance: UWEC is one of the few campuses that publishes actual limits, $1,000,000 per '
          'occurrence and $2,000,000 aggregate through TULIP, with the Board of Regents named as additional '
          'insured — get the certificate before you call, not after. Do NOT chase Blu\'s Organizations Bash '
          '(Wed Sep 9, 11 a.m.–1 p.m., Central Campus Mall): "only officially registered UWEC student '
          'organizations are eligible," full stop. The academic angle is thin — there is verifiably NO '
          'cryptocurrency, blockchain or fintech course in the Finance catalog and no confirmable digital-assets '
          'faculty member — but that cuts in DGD\'s favour for a guest lecture to the Financial Management '
          'Association or the Student Economics Association, neither of which publishes a contact, so go through '
          'the College of Business at 715-836-5509. Pair Eau Claire with Stout, twenty-five miles away, on the '
          'same day; both fairs are Wed Sep 9.',
  'gaps': ['⚠ THE TABLING FEE. The policy says non-students "will be charged a fee for use of any University '
           'structure and/or grounds" and never says how much. This is the number that decides whether Eau '
           'Claire is worth the drive. Jake Serwe, 715-836-4150.',
           '⚠ The price list for the University Centers partnership menu (naming rights, event sponsorship, '
           'digital displays, elevator wraps, table tents) — advertised with no rates. 715-836-4150.',
           'Whether the student-data clause ("lists of names, addresses... will not be made available to '
           'non-University individuals or organizations without approval of the Chancellor") also restricts what '
           'an outside group may COLLECT at a table. Ask specifically; it matters for wallet signups. '
           '715-836-4150.',
           'The name of the Director of University Centers — the officer the solicitation policy designates as '
           'the approver, and the page does not name them. 715-836-4636.',
           'Required lead time for a solicitation request — the policy requires "registration and permission" '
           'and gives no notice period. 715-836-4636.',
           'Employer registration costs for all five Fall 2026 career fairs, including the Sep 23 Actuarial, '
           'Accounting and Finance fair. 715-836-3487.',
           'Add/drop deadlines for Fall 2026 — not on the detailed academic calendar PDF. '
           'https://www.uwec.edu/offices-services/blugold-central/academic-planning/academic-and-registration-calendars',
           'No advisor names, organisation emails or phones are published for ANY UWEC College of Business '
           'student organisation, including FMA. 715-836-5509.',
           'The Blugold Connect campus-wide org directory could not be enumerated, so the absence of a crypto '
           'club is confirmed only for the business college. Activities, Involvement and Leadership oversees '
           '200+ orgs — 715-836-4833.',
           'No phone number or staff name is published for UWEC Risk Management, which receives the certificate '
           'of insurance. https://www.uwec.edu/risk-management-safety/facility-use/'],
  'note': 'UWEC also operates a branch campus, UW-Eau Claire – Barron County (barron.uwec.edu), with its own '
          'academic calendar. It is a small two-year campus in Rice Lake with no business or CS population worth '
          'a stop — do not confuse the two calendars.'},

 # ---------------------------------------------------------------- 5. UW-LA CROSSE
 {'state': 'Wisconsin',
  'name': 'University of Wisconsin–La Crosse',
  'city': 'La Crosse, WI',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 4,
  'start': 'Tue Sep 8, 2026 — the day after Labor Day; six days behind Madison.',
  'adddrop': 'Last day to ADD without permission: Sep 14 (full-semester), Sep 10 (first half-term), Oct 29 '
             '(second half-term). Last day to DROP without a W: Sep 21 (full-semester), Sep 14 (first half), '
             'Nov 2 (second half). Last day to drop WITH a W: Nov 9 (full-semester), Oct 6 (first half), Nov 24 '
             '(second half). The most completely published add/drop table in the state.',
  'fallbreak': 'None separate from Thanksgiving.',
  'thanksgiving': 'Verbatim: "Break begins Wednesday November 25 at 5:30pm. Classes resume Monday, November 30, '
                  '2026." Note the 5:30 p.m. cutoff — Nov 25 is a full teaching day until evening.',
  'lastclass': 'Wed Dec 16, 2026',
  'finals': 'Dec 17–22, 2026. Commencement Sun Dec 20, 2026.',
  'cal_url': 'https://www.uwlax.edu/records/dates-and-deadlines/',
  'cal_status': 'CONFIRMED on the Records & Registration Dates & Deadlines page, cross-confirmed against the '
                'systemwide calendar (Sep 8 – Dec 22). The undergraduate catalog describes Semester I as '
                '"September through mid-December... 14 weeks of instruction plus one week of final exams."',
  'fair': '⚠ "Sample the City & Volunteer Fair" — plus a separate, undated "Fall Involvement Fair"',
  'fair_date': '⚠⚠ SAMPLE THE CITY: Wed Sep 9, 2026, 10:00 a.m. – 1:00 p.m. Sep 9, 2026 is a Wednesday and the '
               'term starts Sep 8 — internally consistent, page is current. SEPARATELY, a "Fall Involvement '
               'Fair" is listed at orgs.uwlax.edu/event/10176010 — THAT PAGE IS JAVASCRIPT-RENDERED and returned '
               'only "This application requires JavaScript to be enabled." No date, time, location or '
               'eligibility could be retrieved for it. Call the LIC at 608-785-8866 to find out whether these '
               'are one event or two.',
  'fair_outside': '⚠⚠ YES — AND IT IS THE ONLY UNAMBIGUOUS YES IN WISCONSIN. Verbatim from the Leadership & '
                  'Involvement Center page: "LOCAL BUSINESSES AND NON-PROFITS CAN REGISTER HERE." The event '
                  'exists to bring "La Crosse area businesses and volunteer opportunities to campus for '
                  'students" to sample food, learn about local organisations, discover volunteer opportunities '
                  'and win prizes. REGISTRATION FORM IS LIVE: '
                  'https://uwlax.iad1.qualtrics.com/jfe/form/SV_8ppQc49Lby5Fh5A — ⚠ the open question is whether '
                  '"LOCAL" is enforced against an out-of-area company. Ask Amanda Krafft directly.',
  'fair_cost': '⚠ NOT PUBLISHED for Sample the City — the page carries a registration link and no price. Ask '
               'Amanda Krafft, 608-785-8902. Separately, the Fall Career & Internship Fair on Oct 14 is FREE for '
               'employers, which is the cheapest confirmed commercial access in the state.',
  'fair_deadline': '⚠ NOT PUBLISHED for Sample the City. The registration form is open now — register early '
                   'rather than waiting for a deadline that may never be announced. For any separate space '
                   'booking, the Facility Use Waiver must be signed and returned "at least two weeks before the '
                   'event."',
  'fair_url': 'https://www.uwlax.edu/university-centers/orgs/lic/',
  'policy': 'UW-La Crosse University Reservations policies (which cite UWS 18.11(8) directly) plus the Facility '
            'Use Waiver',
  'policy_url': 'https://www.uwlax.edu/reservations/policies/',
  'policy_key': "UW-La Crosse University Reservations (uwlax.edu/reservations/policies/) cites the state code to "
                "your face and then sells you the exception: 'NO PERSON MAY SELL, PEDDLE OR SOLICIT FOR THE SALE "
                "OF GOODS, SERVICES, OR CONTRIBUTIONS' per UWS 18.11(8) — but 'SPECIFIC DESIGNATED SPACES ARE "
                "AVAILABLE FOR A FEE' through University Reservations. ⚠⚠ THE DECISIVE FINDING, AND IT IS UNIQUE "
                "IN WISCONSIN: FRONTING IS NOT BANNED HERE, IT IS PRICED AT A DISCOUNT. The published tier "
                "structure is (1) FIRST PRIORITY, NO FEES — UWL departments and recognised student organisations, "
                "for events targeting the campus community without revenue generation; (2) SECOND PRIORITY, 50% "
                "OF THE UNIVERSITY RATE — 'EVENTS PRIMARILY DEVELOPED BY EXTERNAL GROUPS WHERE A UWL "
                "DEPARTMENT/RSO REQUESTS SPACE ON THEIR BEHALF'; (3) EXTERNAL CUSTOMERS, STANDARD RATE — private "
                "companies, nonprofits or individuals initiating events. Every other campus in this packet either "
                "forbids that middle arrangement or is silent about it; UWL writes it down and halves the price. "
                "THE FOUR-PART SPONSORSHIP TEST, all of which must hold for a booking to count as 'University "
                "sponsored': a UWL representative requests the space; a UWL representative serves as primary "
                "contact and planner; a UWL department pays the fees from a departmental account; and UWL "
                "department representative(s) are ACTIVE AT THE EVENT. 'IF ANY OF THESE CONDITIONS ARE NOT MET, "
                "THE RESERVATION WILL FALL INTO THE EXTERNAL CUSTOMER CATEGORY.' THE WAIVER: 'BEFORE A "
                "CONFIRMATION CAN BE FINALIZED FOR EXTERNAL CUSTOMERS, THEY MUST AGREE TO THE CONDITIONS IN THE "
                "FACILITY USE WAIVER BY SIGNING THE FORM AND RETURNING IT TO THE UNIVERSITY RESERVATIONS OFFICE "
                "AT LEAST TWO WEEKS BEFORE THE EVENT.' ⚠ ONE SPECIFIC EXCLUSION: 'EXTERNAL GROUPS CANNOT RESERVE "
                "TABLING AT THE CLOCKTOWER' — the highest-traffic outdoor spot on campus is off limits to "
                "outsiders. Also 'Fundraising for political purposes is not allowed per WI State Statute, Chapter "
                "11.36.' INSURANCE: 'Depending on the nature of the event, appropriate insurance coverage, AS "
                "DETERMINED BY THE UNIVERSITY RISK MANAGEMENT OFFICE, may need to be purchased. PROOF OF THE "
                "REQUIRED COVERAGE NAMING UW-LA CROSSE AS AN INSURED PARTY MUST BE PROVIDED' — NO DOLLAR LIMIT "
                "IS PUBLISHED; it is discretionary and set case by case. CANCELLATION: late cancellation within "
                "one business day leaves second-priority and external groups 'responsible for all fees'; a "
                "NO-SHOW costs external groups '100% OF FEES'; and a third no-show means 'RESERVATION PRIVILEGES "
                "SUSPENDED FOR THE REMAINING OF THE SEMESTER.' NO DEPOSITS are mentioned anywhere. ⚠ NOTABLE "
                "ABSENCES — verified-not-found, NOT verified-permitted: NO RATE CARD EXISTS ANYWHERE (the 50% "
                "and standard tiers are defined against a 'University Rate' that is never printed), and NO "
                "LANGUAGE REACHING CREDIT CARDS, PAYMENT APPS OR ON-SITE CONTRACTS was found. Get the rate sheet "
                "by phone: University Reservations, 608-785-8895, or Hayley Harnden, 608-785-6600.",
  'sponsor_required': 'NO — but sponsorship is worth HALF THE PRICE, and UWL is the one campus in Wisconsin that '
                      'says so in writing. An external group can book directly at the standard rate. But if a '
                      'UWL department or recognised student organisation requests the space on DGD\'s behalf — '
                      'an arrangement other campuses call fronting and prohibit — UWL charges 50% of the '
                      'University Rate. Note the ceiling: to get all the way to the free first-priority tier a '
                      'UWL department must request, plan, PAY from a departmental account, and staff the event, '
                      'and failing any one of those four drops the booking straight to external rates.',
  'clubs': [('⚠ NO BLOCKCHAIN OR CRYPTOCURRENCY CLUB AT UW-LA CROSSE',
             'Verified absent from the College of Business Administration organisation list (twelve groups, no '
             'crypto group) and from the Finance department\'s own student-organizations page. Note the irony: '
             'UWL is the only campus in Wisconsin that TEACHES a dedicated blockchain course (FNT 735) and it has '
             'no student club — but the course is an online graduate certificate, so the two populations never '
             'meet. That gap is an opening.',
             'https://www.uwlax.edu/university-centers/orgs/organization-directory/'),
            ('Financial Management Association (FMA)',
             'Highest-fit club at UWL — "facilitates the development of knowledge regarding economic and '
             'financial-based careers." ⚠ NO ADVISOR NAME, EMAIL OR PHONE IS PUBLISHED for this or any other CBA '
             'organisation, on either the CBA page or the Finance department page. Finance department main line '
             '608-785-8115.',
             'https://orgs.uwlax.edu/organization/fma'),
            ('UWL Investment Club',
             '"Provides opportunity to learn about various topics in investing," personal investment strategies '
             'and finance careers. Active on Instagram and LinkedIn. No advisor or email published.',
             'https://orgs.uwlax.edu/organization/investmentclub'),
            ('UWL Financial Planning Association',
             '"Dedicated to educating and empowering future financial professionals." No contact published.',
             'https://orgs.uwlax.edu/organization/uwlfpa'),
            ('DATA — Data & Analytics in Technology Association',
             'The technical-audience club at UWL: "develops skills in data, analytics, and technology." The right '
             'room for a protocol conversation rather than an asset conversation. No contact published.',
             'https://orgs.uwlax.edu/organization/data'),
            ('Other CBA organisations (lower fit)',
             'UWL Real Estate Club; Beta Alpha Psi (accountancy, finance and information systems); Beta Gamma '
             'Sigma (top 10% of undergraduates); Delta Sigma Pi; Eagle Sales Club; American Marketing '
             'Association; SHRM; Women in Business Club; It Make$ Cents! (the financial-literacy programme, '
             'uwlax.edu/it-makes-cents/). None publishes a contact.',
             'https://www.uwlax.edu/cba/resources-for-students/cba-student-organizations/')],
  'faculty': [('⚠ Amanda Krafft',
               'THE SINGLE BEST NUMBER IN WISCONSIN FOR AN OUTSIDE ORGANISATION. Program Coordinator for '
               'Community Engagement and Belonging, 2208 Student Union. RUNS "SAMPLE THE CITY & VOLUNTEER FAIR," '
               'Wed Sep 9, 2026, 10 a.m.–1 p.m. — the one campus event in this entire state whose own page says '
               '"local businesses and non-profits can register here." Ask her two things: what it costs, and '
               'whether "local" is enforced against an out-of-area company. Direct line.',
               'Leadership & Involvement Center, University Centers',
               'akrafft@uwlax.edu · 608-785-8902',
               'https://www.uwlax.edu/university-centers/orgs/lic/'),
              ('⚠ Hayley Harnden',
               'Associate Director of Events and Operations, 3232 Student Union — THE DECISION-MAKER ON EXTERNAL '
               'BOOKINGS AND THE 50% SECOND-PRIORITY TIER. The person who holds the unpublished rate card and '
               'who can confirm whether a UWL department requesting space on DGD\'s behalf really does halve the '
               'price. Direct line.',
               'University Centers — Events & Operations',
               'hharnden@uwlax.edu · 608-785-6600',
               'https://www.uwlax.edu/reservations/external/event-services/'),
              ('Jacob Hall',
               'Event Manager, Student Union — the working-level contact for off-campus group reservations. The '
               'external event services page recommends "at least two weeks" of advance planning. Direct line.',
               'University Centers — Events & Operations',
               'jhall@uwlax.edu · 608-785-8892',
               'https://www.uwlax.edu/reservations/external/event-services/'),
              ('University Reservations',
               '3200 Student Union. Receives the signed Facility Use Waiver (due at least two weeks before the '
               'event) and administers the priority tiers, the no-show penalties and the Clocktower exclusion. '
               'Office main line.',
               'University Centers — University Reservations',
               'reservations@uwlax.edu · 608-785-8895',
               'https://www.uwlax.edu/reservations/policies/'),
              ('Leadership & Involvement Center (LIC) — "The COVE"',
               '2200 Student Union. Ask them whether the JavaScript-rendered "Fall Involvement Fair" at '
               'orgs.uwlax.edu is the same event as Sample the City or a second one, and whether outside groups '
               'may table at it. Also Paytyn Wilson, Program Coordinator for Student Leadership, '
               'pwilson@uwlax.edu, extension 6601 off this line.',
               'University Centers',
               'LIC@uwlax.edu · 608-785-8866',
               'https://www.uwlax.edu/university-centers/orgs/lic/'),
              ('⚠ Rebecca Lee',
               'Runs the Fall Career & Internship Fair — Wed Oct 14, 2026, 10 a.m.–2 p.m., Student Union, and it '
               'is FREE FOR EMPLOYERS. Registration through Handshake, opened May 1, 2026. She is also the person '
               'who adds names to the invitation lists for the three invitation-only fairs. Direct line.',
               'Academic Advising Center & Career Services',
               'rlee@uwlax.edu · 608-785-8362',
               'https://www.uwlax.edu/aaccs/employers/recruit-at-uwl/'),
              ('Department of Finance',
               'Reaches FMA, the Investment Club, the Financial Planning Association and the Real Estate Club — '
               'none of which publishes a contact. Also the route to whoever teaches FNT 735 Blockchain '
               'Technologies, since no instructor is named anywhere. Department main line.',
               'College of Business Administration — Finance',
               '608-785-8115 (main line)',
               'https://www.uwlax.edu/academics/department/finance/student-organizations/'),
              ('UW-La Crosse campus operator',
               'Main university line — last resort, clearly labelled.',
               'University',
               '608-785-8000 (main line)',
               'https://www.uwlax.edu/'),
              ('(Blockchain / crypto faculty)',
               'NOT CONFIRMED — no named UWL faculty member on blockchain or cryptocurrency could be found, '
               'despite UWL owning the only dedicated blockchain course in Wisconsin. FNT 735 is taught online '
               'through UW Extended Campus and no instructor is named on any retrievable page. Ask the Finance '
               'department, 608-785-8115.',
               'College of Business Administration',
               'no individual confirmed — 608-785-8115',
               'https://www.uwlax.edu/academics/grad/financial-technology/')],
  'courses': [('⚠ FNT 735',
               'BLOCKCHAIN TECHNOLOGIES, 3 credits — THE ONLY DEDICATED BLOCKCHAIN COURSE IN WISCONSIN. Verbatim: '
               '"Covers Bitcoin, Ethereum and other blockchain technologies, cryptocurrencies vs blockchain, '
               'smart contracts, dApps, DeFi applications, CRYPTO WALLETS, blockchain test nets & transactions, '
               'REGULATORY LANDSCAPE, crypto trading and implications on accounting." ⚠⚠ TWO CRITICAL CAVEATS: '
               '(1) the course is FULLY ONLINE and graduate-level — these are working professionals, not '
               'undergraduates on a quad; (2) UWL\'s own page states the programme "has been suspended" and is '
               '"no longer accepting new applications," directing enquiries to learn@uwex.wisconsin.edu. '
               'DO NOT BUILD A CAMPUS VISIT AROUND IT. It is a credible conversation-opener, not an audience.',
               'https://catalog.uwlax.edu/graduate/programrequirements/financialtechnology/'),
              ('FNT 700 / 705 / 710 / 730 / 740',
               'The rest of the graduate FinTech suite: FNT 700 FinTech Essentials; FNT 705 FinTech Analytics; '
               'FNT 710 Managing FinTech Innovation; FNT 730 Technologies in FinTech (cloud, AI, machine '
               'learning, cybersecurity in financial services); FNT 740 Artificial Intelligence and Machine '
               'Learning in FinTech (credit evaluation, fraud detection, algorithmic trading). Certificates are '
               'three courses / nine credits, one year, fully online.',
               'https://catalog.uwlax.edu/graduate/programrequirements/financialtechnology/'),
              ('Graduate Certificate in Emerging Technologies in Fintech',
               'FNT 730 + FNT 735 + FNT 740, offered jointly by UW-LA CROSSE AND UW-PARKSIDE through UW Extended '
               'Campus. Worth knowing that Wisconsin built a two-campus blockchain teaching partnership and then '
               'suspended admissions to it — that is a story, and stories open doors.',
               'https://uwex.wisconsin.edu/certificates/emerging-technologies-in-fintech/')],
  'events': [('⚠⚠ Fall Career & Internship Fair — FREE FOR EMPLOYERS',
              'Wed Oct 14, 2026, 10:00 a.m. – 2:00 p.m., Student Union. COST: FREE. Registration through '
              'Handshake, opened May 1, 2026 at 8:00 a.m. THE CHEAPEST CONFIRMED COMMERCIAL ACCESS TO STUDENTS '
              'IN WISCONSIN — a university-run event, no fee, no invitation required. Rebecca Lee, 608-785-8362.',
              'https://www.uwlax.edu/aaccs/employers/recruit-at-uwl/'),
             ('⚠⚠ Sample the City & Volunteer Fair',
              'Wed Sep 9, 2026, 10:00 a.m. – 1:00 p.m. "Local businesses and non-profits can register here." '
              'Registration form live at uwlax.iad1.qualtrics.com/jfe/form/SV_8ppQc49Lby5Fh5A. Cost and deadline '
              'NOT PUBLISHED. Amanda Krafft, 608-785-8902.',
              'https://www.uwlax.edu/university-centers/orgs/lic/'),
             ('Invitation-only career events',
              'Part-Time Job Fair Sep 9, 2026 (open); Accounting Career Fair Sep 28, 2026 (INVITATION ONLY); '
              'Science & Math Career Forum Nov 6, 2026 (INVITATION ONLY); REXPO: Exploring Leisure, Recreation & '
              'Well-Being Nov 11, 2026 (INVITATION ONLY). "Employers – Please contact Rebecca Lee... to have your '
              'name added to the invitation list." That email should go out now, not in September.',
              'https://www.uwlax.edu/aaccs/employers/recruit-at-uwl/')],
  'play': 'La Crosse is the most open campus in Wisconsin on paper and the one nobody would think to visit. Three '
          'things make it worth the three-and-a-half-hour drive from Madison. First, "SAMPLE THE CITY & VOLUNTEER '
          'FAIR," Wed Sep 9, 2026, 10 a.m.–1 p.m. — the only campus event in this entire state whose own page '
          'says "LOCAL BUSINESSES AND NON-PROFITS CAN REGISTER HERE," with a live Qualtrics registration form and '
          'no published price. Call Amanda Krafft at 608-785-8902 and ask two questions: what does it cost, and '
          'is "local" enforced? Second, the Fall Career & Internship Fair on Wed Oct 14 is FREE FOR EMPLOYERS — '
          'a university-run event, no fee, no invitation, register through Handshake. Nowhere else in Wisconsin '
          'is a table free. Third, and this is the structural finding: UWL is the only campus in the state that '
          'PRICES FRONTING RATHER THAN BANNING IT. Its published second-priority tier is "events primarily '
          'developed by external groups where a UWL department/RSO requests space on their behalf" at FIFTY '
          'PERCENT OF THE UNIVERSITY RATE. Every other campus either forbids that arrangement or is silent; UWL '
          'writes it down and halves the price. Watch three things: external groups CANNOT reserve tabling at '
          'the Clocktower, the Facility Use Waiver must be signed and returned at least two weeks ahead, and a '
          'no-show costs an external group 100% of fees with a third no-show suspending privileges for the '
          'semester. The academic hook is real but must be handled honestly — UWL owns FNT 735 Blockchain '
          'Technologies, the only dedicated blockchain course in Wisconsin, covering crypto wallets, DeFi and the '
          'regulatory landscape — but it is a FULLY ONLINE GRADUATE certificate and UWL has SUSPENDED admissions '
          'to it. Do not build a visit around it; use it as an opener with the Finance department at '
          '608-785-8115, which is also the only way to reach FMA, the Investment Club and the Financial Planning '
          'Association, none of which publishes a contact.',
  'gaps': ['⚠⚠ SAMPLE THE CITY: cost, deadline, and whether "local businesses" is enforced against an '
           'out-of-area company. This is the highest-value unanswered question in Wisconsin. Amanda Krafft, '
           '608-785-8902. Form is live: https://uwlax.iad1.qualtrics.com/jfe/form/SV_8ppQc49Lby5Fh5A',
           '⚠ THE RATE CARD DOES NOT EXIST ON THE OPEN WEB. The 50% second-priority tier and the standard '
           'external rate are both defined against a "University Rate" that is never printed anywhere. '
           'University Reservations 608-785-8895, or Hayley Harnden 608-785-6600.',
           'The insurance dollar limit — coverage is "as determined by the University Risk Management Office" '
           'with no published amount, set case by case. 608-785-8895.',
           '⚠ The separate "Fall Involvement Fair" at orgs.uwlax.edu/event/10176010 is JAVASCRIPT-RENDERED and '
           'returned nothing — no date, time, location or eligibility. Whether it is the same event as Sample '
           'the City or a second one is unknown. LIC, 608-785-8866.',
           'Who teaches FNT 735 Blockchain Technologies, and whether the suspended FinTech certificate is coming '
           'back. Finance department, 608-785-8115, or learn@uwex.wisconsin.edu.',
           'No advisor names, emails or phones are published for ANY UWL College of Business student '
           'organisation, on either the CBA page or the Finance department page. 608-785-8115.',
           'Getting onto the invitation lists for the Accounting Career Fair (Sep 28), Science & Math Career '
           'Forum (Nov 6) and REXPO (Nov 11) — all three are invitation-only. Rebecca Lee, 608-785-8362.',
           'Whether the Clocktower exclusion ("external groups cannot reserve tabling at the Clocktower") has '
           'an equivalent high-traffic alternative that IS available to external groups. 608-785-8895.'],
  'note': 'La Crosse is 3.5 hours from Madison and 90 miles from Eau Claire — it belongs on the western trip '
          'with Eau Claire and Stout, not on the Madison–Whitewater–Milwaukee corridor. Note also the collision: '
          'Sample the City is Wed Sep 9, the same day as the Eau Claire fair, the Whitewater fair, the Madison '
          'fair and Meet Menomonie at Stout. Six of the state\'s nine fairs are on that one Wednesday.'},
 # ---------------------------------------------------------------- 6. UW OSHKOSH
 {'state': 'Wisconsin',
  'name': 'University of Wisconsin Oshkosh',
  'city': 'Oshkosh, WI',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 5,
  'start': '⚠ Wed Sep 9, 2026 — THE LATEST START OF ANY PUBLIC CAMPUS IN WISCONSIN, a full week behind Madison. '
           'Calendar note: "Begin 1st 7-week; 14-week session."',
  'adddrop': '⚠ NOT PUBLISHED on the 2026-27 academic calendar PDF, which gives session boundaries, recess and '
             'commencement only. Note the unusual structure: two 7-week sessions run inside the 14-week '
             'semester, so there are multiple add/drop tables. Get them from Academic Affairs.',
  'fallbreak': 'None separate from Thanksgiving.',
  'thanksgiving': 'Thanksgiving recess Wed Nov 25 – Sun Nov 29, 2026. ⚠ Note the precise cutoff: "Recess begins '
                  'after EVENING classes on November 24," so Nov 24 is a full day including evening sessions. '
                  'Classes resume Mon Nov 30.',
  'lastclass': 'Fri Dec 18, 2026 ("End 2nd 7-week, 14-week session & semester")',
  'finals': '⚠ FINAL EXAM DATES ARE NOT ON THE ACADEMIC CALENDAR PDF and could not be retrieved. The semester '
            'ends Dec 18 and commencement is Sat Dec 19, which leaves no separate exam week — exams are likely '
            'inside the final teaching weeks. CONFIRM before scheduling anything in December.',
  'cal_url': 'https://www.uwosh.edu/academic-affairs/wp-content/uploads/sites/196/2024/06/2026-27-Academic-Calendar-1.pdf',
  'cal_status': 'PARTIAL — start, recess, semester end and commencement CONFIRMED on the UWO Academic Affairs '
                '2026-27 calendar PDF and cross-confirmed against the systemwide calendar (Sep 9 – Dec 18). '
                'Add/drop deadlines, study days and final exam dates are NOT on the document.',
  'fair': 'Titan Fest (inside Titan Welcome)',
  'fair_date': 'Tue Sep 8, 2026, 11:00 a.m. – 1:30 p.m., "Across Campus." Sep 8, 2026 IS a Tuesday — consistent. '
               '⚠ NOTE THE FAIR IS THE DAY BEFORE CLASSES START. Description: "Explore opportunities to get '
               'involved at UWO during our annual Titan Fest! Connect with student organizations, learn about '
               'on-campus employment, and discover volunteer opportunities that match your interests."',
  'fair_outside': '⚠ NOT STATED on the Titan Welcome page — but UW Oshkosh is the ONE campus in Wisconsin that '
                  'has already priced the answer for tabling generally. Reeve Union publishes a Category C rate '
                  'for "OTHER INDIVIDUALS/GROUPS": CONCOURSE TABLES $75 (free for RSOs and departments). Whether '
                  'that $75 table can be bought AT TITAN FEST SPECIFICALLY is the single call to make — Reeve '
                  'reservations, (920) 424-2435.',
  'fair_cost': '⚠ $75.00 PER CONCOURSE TABLE for Category C ("Other individuals/groups") at Reeve Memorial '
               'Union — THE ONLY PUBLISHED FOR-PROFIT TABLE RATE IN WISCONSIN, and roughly one-twelfth of what '
               'Madison charges. Category A (RSOs) and Category B (departments/faculty/staff) pay $0. Titan Fest '
               'itself carries no published price.',
  'fair_deadline': 'Not published for Titan Fest. THE OPERATIVE LEAD TIME IS THE SOLICITATION APPROVAL: the '
                   'Reeve Union Building & Event Policy requires approved requests to be "submitted AT LEAST 7 '
                   'DAYS PRIOR." Non-University groups must also have a signed University Facility Use Agreement '
                   'on file. Cancellation with less than two business days\' notice may incur accrued expenses.',
  'fair_url': 'https://www.uwosh.edu/newstudents/welcome/',
  'policy': 'Reeve Union Building & Event Policy (PDF) plus the published Reeve Memorial Union rate card; above '
            'both, Wis. Admin. Code UWS 18.11(8), which the Reeve policy reproduces verbatim',
  'policy_url': 'https://www.uwosh.edu/reeve/event-planning/rates/',
  'policy_key': "⚠⚠ UW OSHKOSH IS THE ONLY CAMPUS IN WISCONSIN THAT PUBLISHES A FOR-PROFIT TABLE RATE. Reeve "
                "Memorial Union rate card (uwosh.edu/reeve/event-planning/rates/) defines three categories "
                "verbatim: 'CATEGORY A: UNIVERSITY RECOGNIZED STUDENT ORGANIZATIONS/CLUBS (RSOs)'; 'CATEGORY B: "
                "DEPARTMENTS, FACULTY, AND STAFF'; 'CATEGORY C: OTHER INDIVIDUALS/GROUPS.' DGD is Category C, "
                "and Category C has a price list: CONCOURSE TABLES $75 (A and B: $0) · Upper Marketplace $300 · "
                "Titan Underground $600 · Lower Marketplace $600 · Blackhawk Commons, no food, $700 · Room 227 "
                "ABC whole $1,000. Labor outside normal operating hours $75/hr for C versus $50/hr for A and B; "
                "A/V technicians $25/hr for C versus $20/hr; equipment free for A and B, $5–$150 per item for C. "
                "THE GOVERNING POLICY ABOVE THE RATE CARD — Reeve Union Building & Event Policy "
                "(uwosh.edu/reeve/wp-content/uploads/sites/56/2023/11/Reeve-Union-Building-Event-Policy.pdf): "
                "'THE UNION IS A PUBLIC FACILITY OPEN TO STUDENTS, FACULTY, STAFF, ALUMNI, AND GUESTS OF THE "
                "UNIVERSITY.' It then reproduces the state code — 'NO PERSON MAY SELL, PEDDLE OR SOLICIT FOR THE "
                "SALE OF GOODS, SERVICES, OR CONTRIBUTIONS ON ANY UNIVERSITY LANDS' — 'EXCEPT THROUGH APPROVED "
                "REQUESTS SUBMITTED AT LEAST 7 DAYS PRIOR.' That seven-day window is the operative deadline at "
                "Oshkosh. 'NON-UNIVERSITY GROUPS ARE REQUIRED TO HAVE A SIGNED UNIVERSITY FACILITY USE AGREEMENT "
                "ON FILE' for potential charges. TABLING CONDUCT, VERBATIM: 'INDIVIDUALS STAFFING THE TABLE MUST "
                "STAY DIRECTLY IN FRONT OF/BEHIND THE ASSIGNED TABLE. TABLE STAFF ARE NOT PERMITTED TO ROAM THE "
                "AREA OR BUILDING.' No walking the concourse handing out flyers. CANCELLATION: 'Events canceled "
                "with less than two business days' notice may be responsible for expenses already accrued'; "
                "three no-shows in an academic year may restrict future reservations. ⚠ NOTABLE ABSENCES — ALL "
                "VERIFIED-NOT-FOUND, NOT VERIFIED-PERMITTED, and together they are what makes Oshkosh rank "
                "first: NO ANTI-FRONTING CLAUSE was found; NO CLAUSE FORBIDDING RSOs FROM SPONSORING OUTSIDE "
                "GROUPS was found; NO INSURANCE REQUIREMENT AND NO DOLLAR LIMIT appear in the retrievable "
                "policy; NO DEPOSIT TERMS were found; and NO LANGUAGE REACHING CREDIT CARDS, PAYMENT APPS OR "
                "ON-SITE CONTRACTS was found anywhere. ⚠ ABSENCE OF PUBLISHED TEXT IS NOT PERMISSION — and note "
                "that NO PHONE NUMBERS ARE PRINTED IN THE POLICY PDF AT ALL. Confirm the insurance and "
                "fronting position explicitly before relying on it: Reeve reservations, (920) 424-2435.",
  'sponsor_required': 'NO — and uniquely with UW-La Crosse, no rule bars a club from hosting DGD either. UW '
                      'Oshkosh sells direct commercial access at a published price ($75 per concourse table for '
                      '"other individuals/groups") and no anti-fronting clause or no-sponsorship clause could be '
                      'found in the Reeve policy. Buy the table; you do not need a student proxy. File the '
                      'solicitation request seven days ahead and get the University Facility Use Agreement '
                      'signed. Confirm the absence of an insurance requirement explicitly at (920) 424-2435 '
                      'before relying on it.',
  'clubs': [('⚠ NO BLOCKCHAIN OR CRYPTOCURRENCY CLUB AT UW OSHKOSH',
             'Verified absent from the School of Business student-organizations page, which is unusually '
             'detailed — it names faculty advisors AND student presidents for most groups — and lists no crypto '
             'group. The campus-wide directory runs on Involve (uwosh.presence.io); its access level could not '
             'be determined. Note the contrast with the access rating: Oshkosh is the EASIEST campus in the '
             'state to buy a table at and has no crypto club to greet you. That is the opening.',
             'https://www.uwosh.edu/reeve/involvement/clubs-orgs/'),
            ('⚠ Finance Club',
             'Highest-fit club at UWO — "Affiliated with the Financial Management Association, the UW Oshkosh '
             'Finance Club provides opportunities for its members to interact with business professionals." '
             'FACULTY ADVISOR: WILL MORRISON — advisors are staff and stable, use that name. ⚠ The page also '
             'publishes the current student president and email; STUDENT ROSTERS ROTATE ANNUALLY, so go through '
             'the advisor or the School of Business at (920) 424-0297 instead.',
             'https://www.uwosh.edu/cob/current-students/student-organizations/'),
            ('Economics Student Association (ESA)',
             'Brings economics students together with faculty and professionals for educational and networking '
             'opportunities — the right room for a monetary argument. No advisor named on the page.',
             'https://www.uwosh.edu/cob/current-students/student-organizations/'),
            ('Titan Spark! Entrepreneurship Club',
             '"Dedicated to inspiring students to think creatively, take initiative, and explore entrepreneurial '
             'opportunities," and explicitly OPEN TO ALL MAJORS — the widest door on campus. Faculty advisor '
             'Dr. John Muraski, muraskij@uwosh.edu.',
             'https://www.uwosh.edu/cob/current-students/student-organizations/'),
            ('Tech Titans and the AI Club',
             'Tech Titans covers Information Systems, IWM, AI and Computer Science — faculty advisor Kim Iversen, '
             'iversenk@uwosh.edu. The AI Club shares Titan Spark\'s advisor, Dr. John Muraski '
             '(muraskij@uwosh.edu). These are the technical audiences at Oshkosh; pitch the protocol, not the '
             'asset.',
             'https://www.uwosh.edu/cob/current-students/student-organizations/'),
            ('Other School of Business organisations (lower fit)',
             'Beta Alpha Psi (accounting) — bap@uwosh.edu, advisor Cynthia Dederich; Beta Gamma Sigma — advisor '
             'Debbie Gray Patton; SHRM — advisor Barbara Rau; Supply Chain Club — advisor Jay Woldt, winner of '
             '17 Platinum Awards; Marketing & Sales Club; Titans of Risk (insurance); Women in Business.',
             'https://www.uwosh.edu/cob/current-students/student-organizations/')],
  'faculty': [('⚠ Reeve Union Reservations',
               'SELLS THE $75 CATEGORY C CONCOURSE TABLE. THE SINGLE MOST IMPORTANT NUMBER IN WISCONSIN FOR THIS '
               'TOUR — the only published for-profit table rate in the state, and the office that sells it. Also '
               'the office to ask for the University Facility Use Agreement, to file the seven-day solicitation '
               'request, and to confirm that no insurance requirement, deposit or anti-fronting clause exists.',
               'Reeve Memorial Union — Student Engagement & Campus Life',
               'reevereserve@uwosh.edu · (920) 424-2435',
               'https://www.uwosh.edu/reeve/event-planning/rates/'),
              ('Student Engagement & Campus Life at Reeve Union',
               '748 Algoma Blvd, Oshkosh WI 54901. Owns the Building & Event Policy quoted above — the document '
               'reproducing UWS 18.11(8) and the seven-day approval requirement. ⚠ NO PHONE NUMBERS ARE PRINTED '
               'IN THE POLICY PDF ITSELF; this number comes from the Reeve resources page.',
               'Reeve Memorial Union',
               'secl@uwosh.edu · (920) 424-0847',
               'https://www.uwosh.edu/reeve/resources/'),
              ('New Student and Retention Programs',
               'Student Success Center, Suite 125, 750 Elmwood Ave. Runs Titan Welcome and TITAN FEST, Tue Sep 8, '
               '2026, 11 a.m.–1:30 p.m. Ask whether an outside group can buy a spot at Titan Fest specifically, '
               'or whether the $75 concourse table is the only Category C option.',
               'New Student and Retention Programs',
               'orientation@uwosh.edu · (920) 424-2909',
               'https://www.uwosh.edu/newstudents/welcome/'),
              ('⚠ Chrissy Lambie',
               'Career & Professional Development — runs the UWO Fall 2026 Internship & Career Fair, Wed Sep 30, '
               '2026, Kolf Sports Center: up to 200 employers and 800+ job seekers, with FULLY PUBLISHED TIERED '
               'PRICING ($375 early bird through $475) and a hard Sep 4 cancellation cutoff. Direct line.',
               'Career & Professional Development',
               'lambiec@uwosh.edu · (920) 424-2181',
               'https://www.uwosh.edu/career/employers/events/'),
              ('School of Business',
               'Reaches the Finance Club, Economics Student Association, Titan Spark!, Tech Titans and the AI '
               'Club — and the faculty advisors behind them, who are the stable contacts. Department main line.',
               'School of Business',
               'business@uwosh.edu · (920) 424-0297 (main line)',
               'https://www.uwosh.edu/cob/current-students/student-organizations/'),
              ('Dr. John Muraski',
               'Faculty advisor to BOTH the Titan Spark! Entrepreneurship Club AND the AI Club — one email '
               'reaches the two widest-open audiences at Oshkosh. NO DIRECT PHONE PUBLISHED; reach via the '
               'School of Business, (920) 424-0297.',
               'School of Business',
               'muraskij@uwosh.edu · no number published — look up here, or (920) 424-0297',
               'https://www.uwosh.edu/cob/current-students/student-organizations/'),
              ('Kim Iversen',
               'Faculty advisor to Tech Titans (Information Systems, IWM, AI, Computer Science) — the technical '
               'audience. NO DIRECT PHONE PUBLISHED.',
               'School of Business',
               'iversenk@uwosh.edu · no number published — look up here, or (920) 424-0297',
               'https://www.uwosh.edu/cob/current-students/student-organizations/'),
              ('Center for Entrepreneurship and Economic Development / Wisconsin SBDC at UW Oshkosh',
               'A small-business development centre hosted on campus — a second, non-student audience and a '
               'potential co-host that is used to working with outside businesses. NO PHONE CONFIRMED on the '
               'centre page — look up here, or via the School of Business.',
               'Center for Entrepreneurship and Economic Development',
               'no number published — look up here, or (920) 424-0297',
               'https://www.uwosh.edu/cei/'),
              ('(Blockchain / crypto / fintech faculty)',
               'NOT CONFIRMED — no UW Oshkosh faculty member working on blockchain, cryptocurrency, digital '
               'assets or fintech could be confirmed on a live page. Look up in the School of Business directory.',
               'School of Business',
               'business@uwosh.edu · no individual confirmed — (920) 424-0297',
               'https://www.uwosh.edu/business/')],
  'courses': [('(Blockchain / crypto / fintech)',
               'NONE CONFIRMED. No UW Oshkosh course on cryptocurrency, blockchain, digital assets or fintech '
               'could be found. Look up in the UWO bulletins.',
               'https://www.uwosh.edu/bulletins/')],
  'events': [('⚠⚠ UWO Fall 2026 Internship & Career Fair',
              'Wed Sep 30, 2026, 11:30 a.m. – 3:30 p.m., Kolf Sports Center, 785 High Ave. Up to 200 employers '
              'and universities, 800+ job seekers. TIERED PRICING, FULLY PUBLISHED: EARLY BIRD $375 (20 '
              'available) · $425 (20 available) · $450 (20 available) · $475 (unlimited). Educational '
              'institutions (K-12) $150; Government/Social Assistance $250; ELECTRIC BOOTHS +$75. "PAYMENT MUST '
              'BE RECEIVED WITHIN 48 HOURS." ⚠⚠ CANCELLATION CUTOFF SEP 4, 2026 — refund minus a $50 processing '
              'fee before that date, NO REFUNDS AFTER. Chrissy Lambie, (920) 424-2181.',
              'https://www.uwosh.edu/career/employers/events/'),
             ('Titan Fest',
              'Tue Sep 8, 2026, 11:00 a.m. – 1:30 p.m., across campus, inside Titan Welcome. The day before '
              'classes start. Eligibility for outside groups is not stated — call (920) 424-2435.',
              'https://www.uwosh.edu/newstudents/welcome/'),
             ('Hackathon — NONE FOUND',
              'No UW Oshkosh hackathon could be confirmed.',
              '')],
  'play': 'Oshkosh is the answer to the question "where can DGD legally put a table in front of Wisconsin '
          'students for the least money," and the answer is $75. Reeve Memorial Union publishes a three-category '
          'rate card, DGD is Category C ("Other individuals/groups"), and a CONCOURSE TABLE IS $75 — against $900 '
          'for a for-profit table at Madison. No anti-fronting clause, no no-sponsorship clause, no insurance '
          'requirement and no deposit terms appear anywhere in the retrievable Reeve policy. CALL REEVE '
          'RESERVATIONS AT (920) 424-2435. Do three things on that call: buy the concourse table, file the '
          'solicitation request (the policy requires approved requests "at least 7 days prior"), and get the '
          'University Facility Use Agreement, which non-university groups must have on file. Then confirm out '
          'loud that no insurance certificate is required — absence of published text is not permission. Know '
          'the tabling conduct rule before you arrive: "individuals staffing the table must stay directly in '
          'front of/behind the assigned table. Table staff are not permitted to roam the area or building." No '
          'working the concourse. Two timing facts shape the visit. Oshkosh has the LATEST public-campus start '
          'in Wisconsin, Wed Sep 9 — so if the first week of September is oversubscribed elsewhere, Oshkosh is '
          'still ahead of you. And TITAN FEST IS TUE SEP 8, the day BEFORE classes start; ask whether the $75 '
          'Category C table can be bought at Titan Fest specifically or only on the concourse. The paid '
          'alternative is the Sep 30 career fair, where pricing is fully published ($375 early bird rising to '
          '$475, +$75 for electricity, payment within 48 hours, NO REFUNDS AFTER SEP 4) — call Chrissy Lambie at '
          '(920) 424-2181. There is no crypto club here and no crypto course; the audience is the Finance Club '
          '(advisor Will Morrison), the Economics Student Association, and Titan Spark! plus the AI Club, both '
          'advised by Dr. John Muraski, whose one email reaches the two widest-open groups on campus. Pair '
          'Oshkosh with Lawrence, twenty miles up the road in Appleton.',
  'gaps': ['⚠ Whether the $75 Category C concourse table can be bought AT TITAN FEST (Tue Sep 8) specifically, '
           'or only on the Reeve concourse on ordinary days. (920) 424-2435.',
           '⚠ Whether UW Oshkosh requires insurance from Category C users — NO insurance requirement and no '
           'dollar limit appear anywhere in the retrievable Reeve Union Building & Event Policy. Absence of '
           'published text is not permission. (920) 424-2435.',
           '⚠ Whether an anti-fronting rule exists that is simply not published — none was found, which is the '
           'main reason Oshkosh ranks first in the state. Confirm explicitly before relying on it. '
           '(920) 424-2435.',
           'The University Facility Use Agreement itself — required for non-university groups, not published '
           'online. Ask for a copy. (920) 424-2435.',
           '⚠ FINAL EXAM DATES for Fall 2026 are NOT on the UWO academic calendar PDF, and neither are add/drop '
           'deadlines. The semester ends Dec 18 with commencement Dec 19, leaving no obvious exam week. '
           'Academic Affairs, https://www.uwosh.edu/academic-affairs/calendars/',
           'Whether the campus-wide Involve directory (uwosh.presence.io) is publicly enumerable — the absence '
           'of a crypto club is confirmed only for the School of Business list. Reeve SECL, (920) 424-0847.',
           'No direct phone is published for Dr. John Muraski or Kim Iversen, the advisors to the three '
           'best-fit clubs. School of Business, (920) 424-0297.',
           'No phone confirmed for the Center for Entrepreneurship and Economic Development or the Wisconsin '
           'SBDC at UW Oshkosh. https://www.uwosh.edu/cei/'],
  'note': 'The UWO School of Business page publishes CURRENT STUDENT PRESIDENT names and emails for most clubs. '
          'Those rotate every May. This packet deliberately records only the FACULTY ADVISORS, who are staff and '
          'stable — if an ambassador wants a student contact, pull it fresh from the page on the day, do not '
          'reuse a name from a briefing document.'},

 # ---------------------------------------------------------------- 7. UW-WHITEWATER
 {'state': 'Wisconsin',
  'name': 'University of Wisconsin–Whitewater',
  'city': 'Whitewater, WI',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 3,
  'start': 'Wed Sep 2, 2026 at 8:00 a.m.',
  'adddrop': 'Last day to ADD a first half-term course Sep 3; last day to ADD a full-semester course Sep 10; '
             'last day to DROP a full-semester course Sep 16 (also the financial-aid enrollment lock date); last '
             'day to withdraw or change grading basis for a first half-term course Oct 23.',
  'fallbreak': 'None separate from Thanksgiving. ⚠ STALE-SOURCE WARNING: the FYE Family Calendar PDF renders '
               '"November 4: Fall break begins at 9 p.m." — the Registrar\'s own 2026-27 calendar says NOVEMBER '
               '24. Trust the Registrar PDF; the Family Calendar line is a parsing or typesetting error.',
  'thanksgiving': 'Thanksgiving break begins 9:00 p.m. Tue Nov 24, 2026 and ends 8:00 a.m. Mon Nov 30, 2026.',
  'lastclass': 'Sat Dec 12, 2026 (Whitewater runs Saturday classes — the term genuinely ends on a Saturday).',
  'finals': 'Exam period begins 7:45 a.m. Mon Dec 14 and runs to 9:00 p.m. Fri Dec 18, 2026; makeup exams Dec 18, '
            '12:15–9:00 p.m. Commencement Sat Dec 19, 2026.',
  'cal_url': 'https://www.uww.edu/documents/registrar/Calendars/2026-2027/2026-27%20CALENDAR-%20Final.pdf',
  'cal_status': 'CONFIRMED on the Registrar\'s 2026-2027 calendar PDF, cross-confirmed against the systemwide '
                'calendar (Sep 2 – Dec 18). ⚠ The FYE Family Calendar PDF conflicts on the Thanksgiving date '
                '(Nov 4 vs Nov 24) — the Registrar governs.',
  'fair': 'Involvement Fair',
  'fair_date': 'Wed Sep 9, 2026, with a RAIN DATE of Thu Sep 10 — confirmed on the 2026-2027 UW-Whitewater '
               'Family Calendar. ⚠ TIME, LOCATION, ELIGIBILITY AND COST ARE NOT PUBLISHED ANYWHERE RETRIEVABLE. '
               'The University Center "Engage and Connect" page carries no fair details and directs enquiries to '
               '"Involvement Interns" at involvement@uww.edu. Prior-year listings exist at '
               'events.uww.edu/university-center/ (2024 Fall Involvement Fair; Spring 2025 Involvement Fair) but '
               'no Fall 2026 listing was retrievable.',
  'fair_outside': '⚠ UNPUBLISHED for the fair — but the campus sales-and-solicitation policy answers the general '
                  'question and the answer is workable: all sales must be "SPONSORED BY A RECOGNIZED UNIVERSITY '
                  'DEPARTMENT OR ORGANIZATION, OR STUDENT ORGANIZATION," registered with the Office for '
                  'Leadership Development at least five days in advance. There is NO anti-fronting language in '
                  'the policy. Whitewater is the campus where the sponsorship route is genuinely open — and it '
                  'is the campus with a 110-member blockchain club to sponsor you.',
  'fair_cost': 'NOT PUBLISHED — the sales-and-solicitation policy contains no fee or penalty schedule at all. '
               'Call the University Center or Compliance and Risk Management at 262-472-1234.',
  'fair_deadline': 'The operative deadline is the five-day registration: "Student organizations... shall register '
                   'for the activity with the Office for Leadership Development AT LEAST FIVE DAYS IN ADVANCE." '
                   'Building Supervisor approval is separately required for the specific location.',
  'fair_url': 'https://www.uww.edu/documents/fye/Family%20Programs/Final%202026.%202027%20Family%20Calendar.pdf',
  'policy': 'UW-Whitewater "Policy for Campus Sales and Solicitation" (Office of Compliance and Risk '
            'Management); above it, Wis. Admin. Code UWS 18.11(8)',
  'policy_url': 'https://www.uww.edu/policies/policies-by-category/general-policies/sales-and-solicitation',
  'policy_key': "UW-Whitewater, 'Policy for Campus Sales and Solicitation' "
                "(uww.edu/policies/policies-by-category/general-policies/sales-and-solicitation) — 'AS AMENDED "
                "OCTOBER 2005. LAST REVIEWED: OCTOBER 2015.' ⚠ NO POLICY NUMBER IS PRINTED, and the document is "
                "over a decade past its last review — ask whether a newer version exists before relying on it. "
                "⚠⚠ THE DECISIVE PROVISION, AND IT IS A DOOR RATHER THAN A WALL: ALL SALES MUST BE 'SPONSORED BY "
                "A RECOGNIZED UNIVERSITY DEPARTMENT OR ORGANIZATION, OR STUDENT ORGANIZATION.' Sponsorship is "
                "MANDATORY and it is EXPRESSLY PERMITTED. ⚠ THERE IS NO ANTI-FRONTING LANGUAGE ANYWHERE IN THE "
                "POLICY — nothing forbids a recognised student organisation from reserving or hosting on behalf "
                "of an outside entity, which is exactly what OU, Marquette and UWM each forbid. Whitewater is "
                "where the state code's own exception at UWS 18.11(8)(d) — 'selling, and soliciting activities "
                "BY OR UNDER THE SPONSORSHIP OF a university or REGISTERED STUDENT ORGANIZATION' — is widest "
                "open, and it is the campus with the club to walk you through it. THE REGISTRATION REQUIREMENT: "
                "'STUDENT ORGANIZATIONS... SHALL REGISTER FOR THE ACTIVITY WITH THE OFFICE FOR LEADERSHIP "
                "DEVELOPMENT AT LEAST FIVE DAYS IN ADVANCE.' Separately, 'Building Supervisor approval [is] "
                "required for the specific location.' PRODUCT RESTRICTIONS: 'ITEMS SOLD OR TO BE OFFERED FOR "
                "SALE MAY NOT BE IN VIOLATION OF EXISTING UNIVERSITY CONTRACTS' or duplicate bookstore items — "
                "the exclusivity-contract trap that catches merchandise. 'With the exception of the sale of "
                "baked goods and candy, no other food preparation/sales is permitted.' Activities must comply "
                "with 'applicable state, local and federal laws.' LOCATION RESTRICTIONS: sales are generally "
                "limited to 'THE UNIVERSITY CENTER, RESIDENCE HALLS, ESKER HALL AND DRUMLIN HALL.' ⚠ NOTABLE "
                "ABSENCES — verified-not-found, NOT verified-permitted: NO FEE SCHEDULE, NO PENALTY SCHEDULE, NO "
                "INSURANCE REQUIREMENT, NO DEPOSIT OR CANCELLATION TERMS, and NO LANGUAGE REACHING CREDIT CARDS, "
                "PAYMENT APPS OR ON-SITE CONTRACTS appear anywhere in the policy. Contact for the policy itself: "
                "Office of Compliance and Risk Management, policies@uww.edu, 262-472-1234.",
  'sponsor_required': '⚠ YES — AND HERE, UNIQUELY, SPONSORSHIP ACTUALLY CURES THE PROBLEM. "All sales must be '
                      'sponsored by a recognized university department or organization, or student '
                      'organization," registered with the Office for Leadership Development at least five days '
                      'in advance, with Building Supervisor approval for the location. There is NO anti-fronting '
                      'clause and NO bar on student organisations hosting outside entities. And Whitewater has '
                      'the one club in Wisconsin that would obviously want to: a 110-member Blockchain and '
                      'Cryptocurrency Student Organization advised by Paul Nylen, operating under an FMA that '
                      'already advertises a corporate-partners programme.',
  'clubs': [('⚠⚠ Blockchain and Cryptocurrency Student Organization',
             'THE SINGLE MOST VALUABLE STUDENT ORGANISATION IN WISCONSIN AND THE REASON WHITEWATER IS AN A-TIER '
             'TARGET. 110 MEMBERS, 9 OFFICERS. Dedicated to Bitcoin and cryptocurrency education through '
             'expert-led events and peer discussion; runs "MAJOR EVENTS (2-3 PER SEMESTER): INDUSTRY PANELS, '
             'GUEST SPEAKERS, HANDS-ON WORKSHOPS" plus "DISCUSSION GROUPS (EVERY OTHER WEDNESDAY): INFORMAL '
             'CONVERSATIONS ABOUT BITCOIN, MARKETS, AND NEWS." OPERATES UNDER THE FMA UMBRELLA. The page is '
             'PUBLICLY READABLE, not login-gated. ⚠ ADVISOR: PAUL NYLEN, nylenp@uww.edu, (262) 472-5453 — use '
             'the advisor, who is staff and stable, NOT the student officers, whose roster rotates every year. '
             'An "industry panel" or "guest speaker" slot is a non-commercial door that the sales-and-'
             'solicitation policy does not touch at all.',
             'https://uww.campusgroups.com/blockchaincrypto/home/'),
            ('⚠ Financial Management Association (FMA) — WITH AN OPEN CORPORATE-SPONSORSHIP PIPELINE',
             'The parent organisation of the blockchain club and the strongest finance club in Wisconsin. Meets '
             'TUESDAYS 5:30 P.M., HH2203, BAKER TILLY HALL. Sister clubs: Capital Markets Club, Real Estate Club, '
             'and a CRYPTO CLUB. Runs an Applied Investments Program — "Apply your skills in real-world '
             'scenarios, and compete for cash prizes." ⚠⚠ PUBLISHES A "CORPORATE PARTNERS" PAGE — "Meet the '
             'firms behind the mission," "Enabling the next generation of finance professionals." A STUDENT-RUN, '
             'PUBLICLY ADVERTISED CORPORATE SPONSORSHIP PROGRAMME THAT SITS OUTSIDE THE CAMPUS SALES POLICY '
             'ENTIRELY. Contact fma@uww.edu; also on LinkedIn as "UWW Financial Management Association." '
             'Contact page: https://uww.campusgroups.com/fma/contact-us/',
             'https://uwwfma.org/'),
            ('Capital Markets Club; Real Estate Club; Crypto Club',
             'The three named FMA sister clubs. The "Crypto Club" is listed separately from the Blockchain and '
             'Cryptocurrency Student Organization on the FMA site — whether they are the same body under two '
             'names or two distinct groups is UNCONFIRMED. Ask Paul Nylen, (262) 472-5453.',
             'https://uwwfma.org/')],
  'faculty': [('⚠⚠ Paul Nylen',
               'THE BEST DOOR IN WISCONSIN, FULL STOP. Associate Professor of Accounting AND advisor to the '
               '110-member Blockchain and Cryptocurrency Student Organization. WPR (May 24, 2024) identified him '
               'as "a University of Wisconsin-Whitewater professor and FACULTY DIRECTOR OF UW-WHITEWATER\'S '
               'BLOCKCHAIN AND CRYPTOCURRENCY INSTITUTE," commenting on the State of Wisconsin Investment '
               'Board\'s $164 million bitcoin ETF position — he called the state "a little under-invested," '
               'saying 1–3% would be more appropriate than the under-1% actually held. ⚠ THE INSTITUTE HAS NO '
               'RETRIEVABLE PAGE ON uww.edu; its existence is confirmed only in WPR and a LinkedIn company page, '
               'so treat the Institute as UNVERIFIED — but THE PERSON, THE ADVISOR ROLE AND THE DIRECT PHONE ARE '
               'ALL CONFIRMED. One call reaches the club, the Institute question and a media-experienced '
               'academic who already argues publicly that Wisconsin should hold more bitcoin. CALL HIM FIRST.',
               'College of Business and Economics — Accounting',
               'nylenp@uww.edu · (262) 472-5453',
               'https://www.uww.edu/cobe/cobe-directory'),
              ('Career & Leadership Development',
               '⚠ CONTROLS THE INVITATION LIST FOR THE FALL WARHAWK INTERNSHIP & CAREER FAIR, WHICH IS '
               'INVITATION-ONLY. "Organizations without previous attendance must request an invitation by '
               'emailing career@uww.edu with company name, primary contact details, opportunity types, and '
               'target majors." That email must go out well before the Sep 17 registration close. $400 standard, '
               '$175 non-profit, free for Career Services sponsor partners.',
               'Career & Leadership Development',
               'career@uww.edu · (262) 472-1471',
               'https://www.uww.edu/career/employer-resources/employer-career-fairs'),
              ('Office of Compliance and Risk Management',
               'Owns the Policy for Campus Sales and Solicitation — the document that makes sponsorship '
               'mandatory and contains no anti-fronting clause. Ask them two things: whether a newer version '
               'exists (this one was last reviewed October 2015), and what the fee is, since the policy names '
               'none. This number is the UW-Whitewater main line and also reaches the COBE Dean\'s Office.',
               'Office of Compliance and Risk Management',
               'policies@uww.edu · 262-472-1234 (main line)',
               'https://www.uww.edu/policies/policies-by-category/general-policies/sales-and-solicitation'),
              ('University Center — Student Engagement / Involvement Interns',
               '190 Hamilton Green Way. The route to the Involvement Fair (Wed Sep 9, 2026, rain date Sep 10) '
               'whose time, location, eligibility and cost are all unpublished, and to the Office for Leadership '
               'Development, which receives the five-day sales registration. ⚠ NO DIRECT PHONE IS PUBLISHED for '
               'this office — the page gives only the campus main line.',
               'University Center — Student Engagement',
               'involvement@uww.edu · no direct number published — look up here, or 262-472-1234',
               'https://www.uww.edu/uc/get-involved'),
              ('First Year Experience',
               'Publishes the Family Calendar that carries the Sep 9 Involvement Fair date. Also runs Warhawk '
               'Welcome, which begins Aug 30, 2026. Direct line.',
               'First Year Experience',
               'fye@uww.edu · 262-472-3205',
               'https://www.uww.edu/fye/students/warhawk-welcome'),
              ('Rashiqa Kamal',
               'Professor, Department of Finance and Business Law — the senior finance academic at Whitewater. '
               '⚠ NOT a confirmed digital-assets researcher; do not represent her as one. Direct line.',
               'College of Business and Economics — Finance and Business Law',
               'kamalr@uww.edu · 262-472-5446',
               'https://www.uww.edu/cobe/cobe-directory'),
              ('Pascal Letourneau',
               'Associate Professor, Finance and Business Law — quantitative finance. Plausible instructor for '
               'FNBSLW 377 Introduction to FinTech, but that is INFERENCE, not confirmation. Direct line.',
               'College of Business and Economics — Finance and Business Law',
               'letournp@uww.edu · 262-472-3209',
               'https://www.uww.edu/cobe/cobe-directory'),
              ('Department of Finance and Business Law — full direct-line list',
               'Every one confirmed on the COBE directory, all @uww.edu: Neal Dihora, Lecturer — dihoran, '
               '262-472-5445; Dennis Elverman, Senior Lecturer — elvermad, 262-472-2191; Mohammad Jafarinejad, '
               'Associate Professor — jafarinm, 262-472-1845; He Li, Associate Professor — lih, 262-472-1326; '
               'Md Showaib Rahman Sarker, Assistant Professor — sarkerm, 262-472-1029; Bakhtear Talukdar, '
               'Associate Professor — talukdam, 262-472-7036; Gene Toboyek, Distinguished Lecturer — toboyekg, '
               '262-472-3950; Pengyu Qian, Assistant Professor — qianp, 262-472-1229; Yanhui Zhao, Associate '
               'Professor — zhaoya, 262-472-1299; Yuan Yuan, Professor — yuany, 262-472-5458. ⚠ NONE IS A '
               'CONFIRMED DIGITAL-ASSETS RESEARCHER — the crypto expertise at Whitewater sits in ACCOUNTING with '
               'Paul Nylen, not in Finance.',
               'College of Business and Economics — Finance and Business Law',
               'see individual numbers above · COBE Dean\'s Office 262-472-1234',
               'https://www.uww.edu/cobe/cobe-directory')],
  'courses': [('FNBSLW 377',
               'INTRODUCTION TO FINTECH, 3 units — "Financial technology innovations, including '
               'disintermediation, the evolution of product and service creation, and addressing challenges '
               'related to privacy, regulation, and law enforcement." Prerequisites: FNBSLW 344 and either COBE '
               'major status with a 2.50 GPA, or 60 credits with a 2.00 GPA for non-COBE majors and minors. '
               '⚠ FALL 2026 OFFERING UNVERIFIED — no "typically offered" line is published. Instructor not named.',
               'https://uww-public.courseleaf.com/undergraduate/course-inventory/fnbslw/'),
              ('(Dedicated blockchain / cryptocurrency course)',
               '⚠ NONE — verified absent from the Finance and Business Law (FNBSLW) course inventory. This is the '
               'most striking finding at Whitewater: the campus has a 110-member blockchain club, an FMA crypto '
               'sister club and a professor described as director of a blockchain institute, AND NO BLOCKCHAIN '
               'COURSE IN THE CATALOG. The teaching happens in the student organisation, not the curriculum — '
               'which is precisely why the club runs 2-3 industry panels and guest-speaker events a semester and '
               'why a speaking slot is available to someone who asks.',
               'https://uww-public.courseleaf.com/undergraduate/course-inventory/itscm/')],
  'events': [('⚠⚠ Fall Warhawk Internship & Career Fair — INVITATION ONLY',
              'Wed Sep 30, 2026, 11:00 a.m. – 3:30 p.m., DLK Kachel Fieldhouse at the Williams Center. '
              'STANDARD EMPLOYERS $400 · NON-PROFIT $175 (501(c)(3), government agencies, public school '
              'districts) · CAREER SERVICES SPONSOR PARTNERS FREE. Additional fees for extra representatives and '
              'electrical access. REGISTRATION CLOSES THU SEP 17, 2026 AT 6:00 P.M. OR AT CAPACITY. ⚠⚠ THE FAIR '
              'IS BY INVITATION ONLY — "Organizations without previous attendance must request an invitation by '
              'emailing career@uww.edu with company name, primary contact details, opportunity types, and target '
              'majors." SEND THAT EMAIL NOW; the invitation has to arrive before the registration window closes.',
              'https://www.uww.edu/career/employer-resources/employer-career-fairs'),
             ('⚠ Blockchain club industry panels and guest speakers',
              'Not a dated event but the real prize: the Blockchain and Cryptocurrency Student Organization runs '
              '"Major Events (2-3 per semester): Industry panels, guest speakers, hands-on workshops" and '
              'biweekly Wednesday discussion groups on Bitcoin, markets and news. A speaking slot is '
              'non-commercial, free, in front of 110 self-selected students, and completely outside the campus '
              'sales-and-solicitation policy. Route through Paul Nylen, (262) 472-5453.',
              'https://uww.campusgroups.com/blockchaincrypto/home/'),
             ('Involvement Fair, Family Fest and Homecoming',
              'Involvement Fair Wed Sep 9, 2026 (rain date Thu Sep 10) — time and location unpublished. Warhawk '
              'Welcome begins Aug 30 (residence halls open 9 a.m.). Family Fest weekend Oct 2–3, 2026 with a '
              'football game. Homecoming Week Oct 19–24, 2026. Homecoming and Family Fest are high-traffic days '
              'when a sponsored club table would be at its most valuable.',
              'https://www.uww.edu/documents/fye/Family%20Programs/Final%202026.%202027%20Family%20Calendar.pdf')],
  'play': 'WHITEWATER IS THE MOST IMPORTANT STOP IN WISCONSIN AND IT IS NOT CLOSE. It has the only dedicated '
          'blockchain student organisation in the state — 110 members, 9 officers, running two to three industry '
          'panels and guest-speaker events per semester plus biweekly Wednesday discussion groups about Bitcoin '
          'and markets — sitting under a Financial Management Association that publicly advertises a corporate-'
          'partners programme, on a campus whose sales-and-solicitation policy REQUIRES sponsorship by a '
          'recognised student organisation and contains NO ANTI-FRONTING LANGUAGE WHATSOEVER. Every other campus '
          'in this packet either forbids the club route or has no club. Here the policy demands the club route '
          'and the club exists. CALL PAUL NYLEN AT (262) 472-5453. He is an Associate Professor of Accounting, '
          'the club\'s advisor, and was WPR\'s on-record expert when Wisconsin\'s pension fund bought $164 '
          'million of bitcoin ETFs — he said publicly the state was "a little under-invested." One call gets you '
          'a guest-speaker slot in front of 110 self-selected students at zero cost and entirely outside the '
          'commercial regime, plus an answer on whether the Blockchain and Cryptocurrency Institute (reported by '
          'WPR, with no page on uww.edu) still exists. If he says yes to a panel, that is the single best '
          'outcome available anywhere in Wisconsin. Second, work the FMA directly at fma@uww.edu — it meets '
          'Tuesdays at 5:30 p.m. in HH2203, Baker Tilly Hall, and it is openly soliciting corporate partners. '
          '⚠⚠ TIME-CRITICAL AND EASY TO MISS: the Fall Warhawk Internship & Career Fair on Wed Sep 30 IS '
          'INVITATION ONLY — an organisation with no attendance history must email career@uww.edu with company '
          'name, contact, opportunity types and target majors to REQUEST an invitation, and registration closes '
          'Sep 17 at 6 p.m. or at capacity. That email should go this week, not in September. If a table is '
          'wanted, note the mechanics: sales must be sponsored, registered with the Office for Leadership '
          'Development five days ahead, approved by the Building Supervisor for the location, confined to the '
          'University Center, Residence Halls, Esker Hall or Drumlin Hall, and must not conflict with existing '
          'university contracts or duplicate bookstore merchandise. And Whitewater sits between Madison and '
          'Milwaukee — 45 minutes from one, 50 from the other — so it costs almost nothing to add.',
  'gaps': ['⚠⚠ THE WARHAWK CAREER FAIR IS INVITATION-ONLY and registration closes Sep 17, 2026 at 6:00 p.m. '
           'Email career@uww.edu NOW with company name, primary contact, opportunity types and target majors to '
           'request an invitation. (262) 472-1471.',
           '⚠ Whether the UW-Whitewater Blockchain and Cryptocurrency Institute still exists — Paul Nylen\'s '
           'directorship is confirmed only in a May 2024 WPR story and a LinkedIn company page; there is NO '
           'PAGE ON uww.edu. Paul Nylen, (262) 472-5453.',
           'Whether the FMA "Crypto Club" and the Blockchain and Cryptocurrency Student Organization are the '
           'same body under two names or two separate groups. (262) 472-5453 or fma@uww.edu.',
           '⚠ Involvement Fair TIME, LOCATION, ELIGIBILITY AND COST — only the date (Wed Sep 9, rain date '
           'Sep 10) is confirmed, from the FYE Family Calendar. No Fall 2026 listing exists on events.uww.edu. '
           'involvement@uww.edu or 262-472-1234.',
           'The fee for a sponsored sales activity — the Policy for Campus Sales and Solicitation contains NO '
           'fee schedule and NO penalty schedule at all. Compliance and Risk Management, policies@uww.edu, '
           '262-472-1234.',
           '⚠ Whether a newer version of the sales-and-solicitation policy exists — the published one is "as '
           'amended October 2005" and "last reviewed October 2015," over a decade stale. 262-472-1234.',
           'Whether "items sold... may not be in violation of existing University contracts" reaches branded '
           'merchandise or giveaways. 262-472-1234.',
           'Whether FNBSLW 377 Introduction to FinTech runs in Fall 2026 and who teaches it — no instructor is '
           'named and no "typically offered" line is published. COBE, 262-472-1234.',
           'No direct phone is published for the University Center Student Engagement office or the Office for '
           'Leadership Development, which receives the five-day sales registration. 262-472-1234.',
           '⚠ STALE-SOURCE WARNING to preserve: the FYE Family Calendar PDF renders "November 4: Fall break '
           'begins at 9 p.m." while the Registrar\'s calendar says November 24. Use the Registrar PDF.'],
  'note': 'Whitewater\'s College of Business and Economics is unusually strong for a regional campus — it '
          'sustains an FMA with four sister clubs, an Applied Investments Program with cash prizes, and an '
          'advertised corporate-partners programme. Treat it as a business school, not a regional. Geographically '
          'it is the cheapest stop in the state to add: 45 minutes from Madison, 50 from Milwaukee, on the way '
          'between them.'},
 # ---------------------------------------------------------------- 8. UW-STOUT
 {'state': 'Wisconsin',
  'name': 'University of Wisconsin–Stout',
  'city': 'Menomonie, WI',
  'type': 'Public',
  'tier': 'C — Opportunistic',
  'access': 3,
  'start': 'Wed Sep 2, 2026 (systemwide calendar)',
  'adddrop': '⚠ NOT RETRIEVABLE. Three UW-Stout Registration & Records pages were tried — '
             '/important-dates-times, /academic-registration-calendars and /fall-2026-registration-information — '
             'and ALL THREE render their calendar content dynamically and returned no dates to research tooling. '
             'One page carried a mislabeled "Evaluation Dates: Fall 2024" link. Get by phone.',
  'fallbreak': '⚠ UNVERIFIED — not retrievable (see adddrop).',
  'thanksgiving': '⚠ UNVERIFIED — not retrievable. Assume the systemwide pattern (roughly Nov 25–29) but DO NOT '
                  'schedule against that assumption; confirm first.',
  'lastclass': '⚠ UNVERIFIED. The systemwide calendar gives a fall term end of Dec 18, 2026, which may be the '
               'end of exams rather than the last class day.',
  'finals': '⚠ UNVERIFIED — not retrievable.',
  'cal_url': 'https://www.uwstout.edu/academics/academic-services/registration-records-office/important-dates-times',
  'cal_status': '⚠ PARTIAL — ONLY the term boundaries (Sep 2 – Dec 18, 2026) are confirmed, and only from the '
                'Universities of Wisconsin systemwide calendar, https://www.wisconsin.edu/academic-calendars/academic-year-2026-27/ '
                'NO UW-Stout registrar page would yield a single Fall 2026 date. THIS IS THE WORST CALENDAR GAP '
                'IN THE STATE — call Registration & Records before scheduling anything at Stout.',
  'fair': '⚠⚠ MEET MENOMONIE (chamber-run, on campus) — plus Backyard Bash (the student org fair)',
  'fair_date': 'MEET MENOMONIE: Wed Sep 9, 2026, 4:00 – 7:00 p.m., at University of Wisconsin-Stout. Sep 9, 2026 '
               'is a Wednesday — consistent. BACKYARD BASH: ⚠ FALL 2026 DATE NOT PUBLISHED. Recurring pattern is '
               'early in Week One, roughly 5:00–7:30 p.m., on the lawn south of the student center, with student '
               'organisation booths, music, food and inflatables — the 2022 instance was Tue Sep 6. ⚠ THAT '
               'PATTERN COMES FROM AN ARTICLE DATED AUGUST 29, 2022, four years old; treat it as a pattern, not '
               'a schedule.',
  'fair_outside': '⚠⚠ YES FOR MEET MENOMONIE — AND IT IS THE MOST STRUCTURALLY INTERESTING FINDING IN WISCONSIN. '
                  'Meet Menomonie is run by the MENOMONIE AREA CHAMBER OF COMMERCE, not by the university, and '
                  'its own pitch to businesses reads: "Streamline your recruiting and maximize your reach at '
                  'Meet Menomonie, an EXCLUSIVE OPPORTUNITY TO CONNECT WITH UW-STOUT STUDENTS." Businesses '
                  '"showcase products, highlight employment opportunities, and build relationships with '
                  'potential customers, volunteers, and future employees." PLATINUM AND GOLD SPONSORSHIP LEVELS '
                  'ARE NAMED. A for-profit-friendly tabling event, on campus, in front of the students, whose '
                  'guest list is controlled by a chamber of commerce with no sales-and-solicitation policy — it '
                  'sidesteps UWS 18.11(8) the same way a student-run hackathon does. BACKYARD BASH: student '
                  'organisations only, as far as can be told.',
  'fair_cost': '⚠ NOT PUBLISHED for Meet Menomonie — the chamber page names Platinum and Gold sponsorship levels '
               'and prints no booth price or sponsorship price at all. CALL (715) 235-9087. Backyard Bash: no '
               'cost published, and DGD is likely ineligible anyway.',
  'fair_deadline': '⚠ NOT PUBLISHED for either event. Meet Menomonie has a general registration link and no '
                   'stated deadline. Given the Sep 9 date, treat late August as the practical cutoff and call '
                   'the chamber now.',
  'fair_url': 'https://www.menomoniechamber.org/meetmenomonie/',
  'policy': '⚠ NO UW-STOUT CAMPUS SOLICITATION OR FACILITY-USE POLICY COULD BE RETRIEVED. Wis. Admin. Code '
            'UWS 18.11(8) and ch. UWS 21 govern by default.',
  'policy_url': 'https://regulations.justia.com/states/wisconsin/uws/chapter-uws-18/section-uws-18-11/',
  'policy_key': "⚠⚠ PROVISIONAL — THE GOVERNING CAMPUS POLICY COULD NOT BE RETRIEVED, AND THAT GAP IS THE "
                "FINDING. No UW-Stout solicitation, sales or facility-use policy exists at any retrievable URL. "
                "The connect.uwstout.edu CampusGroups pages (/involvement/reserve-space/, /involvement/staff/, "
                "/msc/staff/) return ONLY navigation chrome and footer with no substantive content, and the "
                "university's own Venues page under Outreach & Engagement returns menu structure without any "
                "rental details, eligibility criteria or rates. RATED 3 BECAUSE THE POLICY IS UNKNOWN, NOT "
                "BECAUSE IT IS RESTRICTIVE — do not guess in either direction. IN THE ABSENCE OF A CAMPUS "
                "POLICY, THE STATE CODE GOVERNS AND AN AMBASSADOR SHOULD BE ABLE TO RECITE IT: Wis. Admin. Code "
                "UWS 18.11(8), 'NO PERSON MAY SELL, PEDDLE OR SOLICIT FOR THE SALE OF GOODS, SERVICES, OR "
                "CONTRIBUTIONS ON ANY UNIVERSITY LANDS EXCEPT IN THE CASE OF: (a) SPECIFIC PERMISSION IN ADVANCE "
                "FROM A SPECIFIC UNIVERSITY OFFICE... (d) SUBSCRIPTION, MEMBERSHIP, TICKET SALES SOLICITATION, "
                "FUND-RAISING, SELLING, AND SOLICITING ACTIVITIES BY OR UNDER THE SPONSORSHIP OF A UNIVERSITY OR "
                "REGISTERED STUDENT ORGANIZATION.' Plus UWS 21.04(1)(a), which permits non-associated "
                "organisations to use facilities where 'THE PROPOSED USE IS UNDER THE SPONSORSHIP OR AT THE "
                "INVITATION OF AN ORGANIZATION ASSOCIATED WITH THE INSTITUTION', and UWS 21.04(2), 'PERSONS OR "
                "ORGANIZATIONS USING UNIVERSITY FACILITIES UNDER THIS SECTION MUST REIMBURSE THE INSTITUTIONS "
                "FOR THE COSTS.' ⚠ THE PRACTICAL POINT THAT MATTERS MORE THAN THE POLICY GAP: MEET MENOMONIE "
                "ROUTES AROUND ALL OF IT. It is run by the Menomonie Area Chamber of Commerce, whose own page "
                "sells businesses 'an EXCLUSIVE OPPORTUNITY TO CONNECT WITH UW-STOUT STUDENTS' with Platinum and "
                "Gold sponsorship levels. A private organiser's guest list is not a university solicitation "
                "permit, and the chamber has no commercial-use rule to apply. Same structural logic as a "
                "student-run hackathon. On paper Stout is a 3; in practice, through the chamber, it behaves "
                "like a 5. GET THE WRITTEN CAMPUS POLICY ANYWAY before doing anything university-side: Career "
                "Services, (715) 232-1122.",
  'sponsor_required': 'UNKNOWN — no campus policy could be retrieved. Under the state code that governs by '
                      'default, either route is available in principle: advance permission from a specific '
                      'university office (UWS 18.11(8)(a)) or activity under the sponsorship of a registered '
                      'student organisation (UWS 18.11(8)(d)). ⚠ But note there is no finance, investment or '
                      'crypto club at UW-Stout to sponsor anything — the club route has no obvious partner here. '
                      'The chamber-run Meet Menomonie needs no university sponsorship at all.',
  'clubs': [('⚠ NO BLOCKCHAIN, CRYPTO, INVESTMENT, FINANCE OR ECONOMICS ORGANISATION AT UW-STOUT',
             'VERIFIED ABSENT, and the absence is meaningful because the UW-Stout CONNECT directory '
             '(connect.uwstout.edu/club_signup) IS SERVER-RENDERED AND READABLE — unlike Madison\'s WIN, '
             'UWM\'s PantherSync and Lawrence\'s Presence, all of which defeated retrieval. UW-Stout has roughly '
             '150 student organisations and not one of them is finance- or crypto-adjacent.',
             'https://connect.uwstout.edu/club_signup'),
            ('Artificial Intelligence Club',
             'THE BEST-FIT CLUB AT STOUT, which tells you what kind of campus this is. "Foster a community of '
             'learners and enthusiasts passionate about artificial intelligence." Pitch the protocol and the '
             'cryptography, not the asset. No contact published.',
             'https://connect.uwstout.edu/club_signup'),
            ('AWS Cloud Club',
             'Second-best technical fit — "Help students... understand cloud" with "hands-on ways for students to '
             'apply their skills." A distributed-systems audience. Note that AWS Cloud Clubs are themselves a '
             'corporate-sponsored student programme, which means this group is already accustomed to industry '
             'involvement. No contact published.',
             'https://connect.uwstout.edu/club_signup'),
            ('American Marketing Association; APICS; Stout Student Association',
             'AMA — "Strives to give members the opportunity to gain professional development, networking '
             'skills, and practical business experience." APICS — supply chain and operations management. Stout '
             'Student Association is the student government. These are the closest things to a business audience '
             'on campus.',
             'https://www.uwstout.edu/life-stout/campus-connect/student-organizations')],
  'faculty': [('⚠⚠ Menomonie Area Chamber of Commerce — Meet Menomonie',
               'THE MOST IMPORTANT NUMBER AT UW-STOUT, AND IT IS NOT A UNIVERSITY NUMBER. Runs Meet Menomonie, '
               'Wed Sep 9, 2026, 4:00–7:00 p.m., ON THE UW-STOUT CAMPUS — a commercial exhibitor event whose own '
               'pitch is "an exclusive opportunity to connect with UW-Stout students," with named Platinum and '
               'Gold sponsorship levels. NO BOOTH PRICE OR DEADLINE IS PUBLISHED. 1125 North Broadway Street, '
               'Suite 3, Menomonie WI 54751.',
               'Menomonie Area Chamber of Commerce (NOT the university)',
               'info@menomoniechamber.org · (715) 235-9087',
               'https://www.menomoniechamber.org/meetmenomonie/'),
              ('⚠ UW-Stout Career Services',
               '712 South Broadway Street, Menomonie WI 54751. THE ONLY CONFIRMED UNIVERSITY PHONE NUMBER AT '
               'UW-STOUT. Runs Career Conference Week (300–400+ employers over four days in late September) and '
               'the Career Services Partnership Program, whose tiers and prices are not published. Also, by '
               'default, the route to the Fall 2026 academic calendar and to whoever owns the campus '
               'solicitation policy — because no other UW-Stout office publishes a number.',
               'Career Services',
               'careerservices@uwstout.edu · (715) 232-1122',
               'https://www.uwstout.edu/academics/career-services/career-professional-events/career-conference-week'),
              ('UW-Stout Involvement Center',
               '⚠ NO PHONE NUMBER, NO STAFF NAMES AND NO EMAIL COULD BE CONFIRMED. The staff page at '
               'connect.uwstout.edu/involvement/staff/ returns only navigation chrome; the space-reservation page '
               'at /involvement/reserve-space/ returns nothing substantive. This is the office that would own '
               'tabling and student-organisation sponsorship, and it is invisible to research tooling. LOOK UP '
               'HERE, or route through Career Services at (715) 232-1122.',
               'Involvement Center',
               'no number published — look up here, or (715) 232-1122',
               'https://connect.uwstout.edu/involvement/home/'),
              ('Memorial Student Center — reservations',
               '⚠ NO PHONE NUMBER OR STAFF NAMES COULD BE CONFIRMED — connect.uwstout.edu/msc/staff/ returned '
               'only chrome, and the Student Centers landing page carries no contact details. The MSC and Merle '
               'Price Commons are the two student-centre buildings. LOOK UP HERE.',
               'Memorial Student Center',
               'no number published — look up here, or (715) 232-1122',
               'https://www.uwstout.edu/life-stout/student-centers'),
              ('Registration & Records Office',
               '⚠ THE OFFICE THAT HOLDS THE ONE THING NOBODY COULD RETRIEVE: the Fall 2026 add/drop, '
               'Thanksgiving and final exam dates. Three separate registrar pages render dynamically and yielded '
               'nothing. NO DIRECT PHONE IS PUBLISHED on any of them. Look up here.',
               'Registration & Records',
               'no number published — look up here, or (715) 232-1122',
               'https://www.uwstout.edu/academics/academic-services/registration-records-office'),
              ('(Blockchain / crypto / fintech / finance faculty)',
               'NOT CONFIRMED — no UW-Stout faculty member on blockchain, cryptocurrency, digital assets or '
               'fintech could be confirmed, consistent with a campus that has no finance club and no such '
               'course. Look up in the UW-Stout directory.',
               'University of Wisconsin–Stout',
               'no individual confirmed — look up here',
               'https://www.uwstout.edu/directory')],
  'courses': [('(Blockchain / crypto / fintech)',
               'NONE CONFIRMED. No UW-Stout course on cryptocurrency, blockchain, digital assets or fintech could '
               'be found. Consistent with the polytechnic programme mix — packaging, manufacturing engineering, '
               'game design and development, hospitality, apparel design, HCI, engineering technology, business '
               'administration and applied economics.',
               'https://www.uwstout.edu/programs')],
  'events': [('⚠⚠ Meet Menomonie',
              'Wed Sep 9, 2026, 4:00 – 7:00 p.m., at UW-Stout. Run by the Menomonie Area Chamber of Commerce. '
              '"Streamline your recruiting and maximize your reach at Meet Menomonie, an exclusive opportunity to '
              'connect with UW-Stout students." Businesses showcase products, highlight employment opportunities '
              'and build relationships with "potential customers, volunteers, and future employees." Platinum and '
              'Gold sponsorship levels named; NO PRICES OR DEADLINE PUBLISHED. (715) 235-9087. THE CLEANEST '
              'COMMERCIAL-ACCESS STRUCTURE IN WISCONSIN — a private organiser controlling the guest list to a '
              'campus event.',
              'https://www.menomoniechamber.org/meetmenomonie/'),
             ('⚠ Career Conference Week',
              '"One of the largest conferences in the Midwest, preparing Blue Devils to be career ready on day '
              'one" — historically 300 to 400+ employers over four days in late September (the 2024 pattern was '
              'Mon Sep 22 – Thu Sep 25). ⚠ FALL 2026 DATES AND EMPLOYER REGISTRATION FEES ARE NOT PUBLISHED. '
              'Call (715) 232-1122.',
              'https://www.uwstout.edu/academics/career-services/career-professional-events/career-conference-week'),
             ('Career Services Partnership Program — the documented sponsorship route',
              '"Identify your strategic focus for recruitment & build deep connections on campus," with a live '
              '"Register for 2026-2027" link. ⚠ TIERS AND PRICES ARE NOT PUBLISHED and the page does not say '
              'whether it is open to all employers. This is the sponsorship channel at Stout and its price is '
              'one phone call away: (715) 232-1122.',
              'https://www.uwstout.edu/academics/career-services/employer-resources/career-services-partnership-program')],
  'play': 'The polytechnic focus DOES change the audience, and honestly: UW-Stout has no finance club, no '
          'investment club, no economics society and no blockchain club — and unlike Madison, Milwaukee and '
          'Lawrence, whose directories defeated retrieval, STOUT\'S DIRECTORY IS READABLE, so that absence is '
          'verified rather than merely unfound. The programme mix is packaging, manufacturing engineering, game '
          'design, hospitality, apparel, HCI and business administration. This is not a worthless stop — there '
          'is a real undergraduate population, an Artificial Intelligence Club and an AWS Cloud Club — but the '
          'pitch that works at Whitewater\'s FMA will not work here. Pitch the technology, not the asset. AND '
          'YET Stout offers the cleanest commercial-access STRUCTURE in Wisconsin, because of an accident of who '
          'runs the event: MEET MENOMONIE, Wed Sep 9, 2026, 4–7 p.m., ON THE UW-STOUT CAMPUS, is run by the '
          'MENOMONIE AREA CHAMBER OF COMMERCE and sold to businesses as "an exclusive opportunity to connect '
          'with UW-Stout students," with Platinum and Gold sponsorship tiers. A private organiser\'s guest list '
          'is not a university solicitation permit — the chamber has no commercial-use rule to apply, exactly '
          'like a student-run hackathon. CALL (715) 235-9087 AND ASK WHAT A BOOTH COSTS; neither the price nor '
          'the deadline is published and the event is four weeks out. Everything on the university side of Stout '
          'is a blank: NO campus solicitation or facility-use policy could be retrieved at any URL; NO phone '
          'number exists for the Involvement Center, the Memorial Student Center or Registration & Records; and '
          'NOT ONE Fall 2026 date beyond the term boundaries could be obtained, because three separate registrar '
          'pages render dynamically. The only confirmed university number on this campus is Career Services, '
          '(715) 232-1122 — use it to get the calendar, the written solicitation policy, the Career Conference '
          'Week dates and the unpublished Partnership Program tiers, all in one call. Pair Stout with Eau '
          'Claire, twenty-five miles away — but note both fairs are Wed Sep 9, so you can only work one.',
  'gaps': ['⚠⚠ MEET MENOMONIE BOOTH COST AND REGISTRATION DEADLINE — Wed Sep 9, 2026, four weeks out, Platinum '
           'and Gold tiers named with no prices. This is the single best commercial structure in Wisconsin and '
           'nobody publishes what it costs. Menomonie Area Chamber of Commerce, (715) 235-9087.',
           '⚠⚠ UW-STOUT HAS NO RETRIEVABLE SOLICITATION OR FACILITY-USE POLICY AT ALL. Ask for it in writing '
           'before committing to anything university-side. (715) 232-1122.',
           '⚠⚠ NOT ONE FALL 2026 DATE beyond the Sep 2 – Dec 18 term boundaries could be retrieved — no '
           'add/drop, no Thanksgiving recess, no finals. Three registrar pages '
           '(/important-dates-times, /academic-registration-calendars, /fall-2026-registration-information) all '
           'render dynamically and returned nothing; one carried a mislabeled "Evaluation Dates: Fall 2024" '
           'link. GET THE CALENDAR BY PHONE BEFORE SCHEDULING.',
           '⚠ NO PHONE NUMBER exists for the UW-Stout Involvement Center, the Memorial Student Center or '
           'Registration & Records — every connect.uwstout.edu staff page returned empty chrome. Career '
           'Services, (715) 232-1122, is the only confirmed university line on this campus.',
           'Backyard Bash Fall 2026 date, time and eligibility — the only source is an article dated August 29, '
           '2022 giving a Tue Sep 6 pattern. Four years stale. (715) 232-1122.',
           'Career Conference Week Fall 2026 dates and employer registration fees — nothing published for 2026; '
           'the 2024 pattern was Sep 22–25. (715) 232-1122.',
           'Career Services Partnership Program tiers, prices and whether it is open to any employer — the '
           '"Register for 2026-2027" link is live and the terms are not published. (715) 232-1122.',
           'Whether an anti-fronting rule or insurance requirement exists at UW-Stout — unknown, because no '
           'policy could be read at all. Absence of retrievable text is not permission.'],
  'note': '⚠ AUDIENCE MISMATCH, STATED PLAINLY: UW-Stout is Wisconsin\'s polytechnic. It is NOT health-sciences-'
          'only, law-only or graduate-only, and it does have a substantial undergraduate population — so it is '
          'not a worthless stop. But its verified club directory contains no finance, investment, economics, '
          'crypto or blockchain organisation of any kind, and no such course exists. The technical clubs (AI '
          'Club, AWS Cloud Club) are the audience and they want the engineering story. If the trip is tight, '
          'Stout is worth exactly one thing: a Meet Menomonie booth on Sep 9, bought from the chamber.'},

 # ---------------------------------------------------------------- 9. LAWRENCE
 {'state': 'Wisconsin',
  'name': 'Lawrence University',
  'city': 'Appleton, WI',
  'type': 'Private',
  'tier': 'C — Opportunistic',
  'access': 3,
  'start': '⚠⚠ Mon Sep 14, 2026 — THE LATEST START IN WISCONSIN, twelve days after the UW pack and fifteen after '
           'Marquette. TRIMESTER SYSTEM: three 10-week terms (Fall, Winter, Spring), students taking THREE '
           'courses per term rather than five.',
  'adddrop': '⚠ Fri Sep 18, 2026 — FOUR DAYS after classes begin. A brutally short window, and a marker of how '
             'compressed a 10-week trimester is.',
  'fallbreak': 'Mid-term reading period Oct 22–25, 2026 — a four-day break at the midpoint of the term, the '
               'trimester equivalent of a fall break.',
  'thanksgiving': '⚠⚠ NOT SEPARATELY LABELLED — THE TERM SIMPLY ENDS INTO IT. Final exams finish Nov 24 and '
                  'residence halls close Nov 25. Lawrence students go home for Thanksgiving and DO NOT COME '
                  'BACK until January.',
  'lastclass': '⚠⚠ Thu Nov 19, 2026. Reading period Nov 20–21.',
  'finals': '⚠⚠ Nov 22–24, 2026. THE FALL TERM IS OVER ON NOVEMBER 24 — three-and-a-half weeks before every '
            'other campus in Wisconsin. ANYTHING SCHEDULED AT LAWRENCE AFTER ROUGHLY NOV 12 IS WORTHLESS, AND '
            'THERE IS NO DECEMBER WINDOW AT ALL. The entire fall is a nine-week strip, Sep 14 to Nov 19, that '
            'opens after everyone else and closes before them.',
  'cal_url': 'https://www.lawrence.edu/academics/trimester-schedule',
  'cal_status': 'CONFIRMED on Lawrence\'s own trimester-schedule page. ⚠ NOTE: www7.lawrence.edu/s/registrar/'
                'calendar 302-redirects to this page, and a large share of Lawrence policy content on '
                'www7.lawrence.edu is ROBOTS-BLOCKED while /offices/ URLs redirect to inside.lawrence.edu.',
  'fair': '⚠ NOT FOUND',
  'fair_date': '⚠ NO LAWRENCE INVOLVEMENT FAIR, ORG FAIR OR ACTIVITIES FAIR COULD BE CONFIRMED for Fall 2026 or '
               'for any year. lawrence.presence.io/organizations is JAVASCRIPT-RENDERED and returned only meta '
               'tags and the title "Involve" — no organisation list and no events. A SEAL "Annual Student Events" '
               'page exists (lawrence.edu/offices/student-engagement-activities-and-leadership/activities-events/'
               'annual-events) but no fair was retrievable from it. If a fair exists it would fall in the week of '
               'Sep 14, given the Sep 14 start. CALL SEAL AT (920) 832-6772.',
  'fair_outside': 'UNKNOWN — no fair could be identified, so no eligibility rule could be read. Lawrence is '
                  'PRIVATE and has no public-forum obligation whatsoever; it may exclude DGD for any reason or '
                  'none.',
  'fair_cost': 'UNKNOWN. Separately, Conference & Event Services advertises spaces "available for rent by '
               'community organizations" with NO published rates of any kind.',
  'fair_deadline': 'UNKNOWN.',
  'fair_url': 'https://www.lawrence.edu/offices/student-engagement-activities-and-leadership',
  'policy': '⚠ NOT RETRIEVED — the current student handbook is not published at a retrievable URL and the '
            'archived one truncated before the relevant section.',
  'policy_url': 'https://www.lawrence.edu/our-neighbors/conference-event-services',
  'policy_key': "⚠⚠ PROVISIONAL — LAWRENCE'S SOLICITATION POLICY COULD NOT BE READ, AND THAT GAP IS THE FINDING. "
                "FIRST, THE THING AN AMBASSADOR MUST KNOW: LAWRENCE IS PRIVATE. Wis. Admin. Code chs. UWS 18 and "
                "21 and Regent Policy Document 4-21 DO NOT TOUCH IT. It has NO public-forum obligation of any "
                "kind and may exclude DGD for any reason or none. Do not walk in citing state law; there is none "
                "that applies. WHAT COULD BE CONFIRMED: the archived 2022-23 student handbook PDF "
                "(blogs.lawrence.edu/lucc/files/2023/08/V2-Student-HandbookCURRENT.pdf) HAS A SECTION TITLED "
                "'SOLICITATION ON CAMPUS' AT PAGE 102, a 'Facility and Room Reservation Procedure' at page 51 "
                "and 'Billboards and Posted Notices' at page 35 — ⚠ BUT THE FETCH TRUNCATED MID-PAGE-32 AND THE "
                "ACTUAL POLICY TEXT COULD NOT BE READ. The current handbook is not published at a retrievable "
                "URL; www7.lawrence.edu/students/activities/student-organization-handbook is ROBOTS-BLOCKED. The "
                "only phone number in the retrievable portion of the handbook is the Title IX Coordinator, "
                "920-832-7490, Room 93 Brokaw Hall. FROM SEAL'S STUDENT-ORGANISATION RESOURCES PAGE, verbatim "
                "and directly relevant to signing anything on site: 'A CONTRACT IS REQUIRED FOR ANY PAID "
                "PERFORMER, SPEAKER, OR ACT. DESIGNATED UNIVERSITY STAFF MAY ENTER INTO CONTRACTS: NO DEPOSITS "
                "OR VERBAL AGREEMENTS SHOULD BE MADE BY A STUDENT.' A Lawrence student CANNOT commit to anything "
                "on DGD's behalf — that authority is reserved to designated staff. Also: 'American Dining "
                "Company contract does not allow student orgs to bring outside catering into Warch Campus Center "
                "with prior approval' — an exclusivity contract that would catch food or drink giveaways. FROM "
                "CONFERENCE & EVENT SERVICES: 'LAWRENCE FEATURES A WIDE VARIETY OF SPACES AVAILABLE FOR RENT BY "
                "COMMUNITY ORGANIZATIONS for public and private functions, meetings, conferences, concerts and "
                "performances, summer camps, and more.' ⚠ NO RATES, NO ELIGIBILITY CRITERIA, NO INSURANCE "
                "REQUIREMENTS, NO DEPOSITS, NO CANCELLATION TERMS AND NO COMMERCIAL RESTRICTIONS ARE PUBLISHED — "
                "a community-rental route is advertised and nothing about it is documented. Tours by appointment "
                "only, Mon-Fri 9 a.m.-3 p.m.; office hours Mon-Fri 8 a.m.-4:30 p.m. RATED 3 BECAUSE THE POLICY "
                "IS UNKNOWN, NOT BECAUSE IT IS RESTRICTIVE OR PERMISSIVE. Close the gap with Dakota McKee, "
                "920-832-6698, or Conference & Event Services, (920) 832-6839.",
  'sponsor_required': 'UNKNOWN — the solicitation policy could not be read. What IS known: a Lawrence student '
                      'cannot bind Lawrence, because "designated university staff may enter into contracts: no '
                      'deposits or verbal agreements should be made by a student." So even a willing student '
                      'club cannot commit to anything on DGD\'s behalf; a staff member must sign. Conference & '
                      'Event Services advertises rentals to "community organizations" with no eligibility '
                      'criteria published, which suggests a direct route exists — get its terms in writing.',
  'clubs': [('Lawrence University Investment Club',
             'THE ONLY RELEVANT CLUB THAT COULD BE CONFIRMED. Aims to "teach members about investing in various '
             'securities" and "analyze and carry out securities transactions based on research," fostering '
             'connections with industry professionals and "fulfilling fiduciary duties to Lawrence University '
             'through prudent investment selection" — that last phrase means they manage a real slice of the '
             'endowment, not a paper portfolio. ⚠ NO CONTACT EMAIL AND NO ADVISOR ARE PUBLISHED. Reach through '
             'Aaron Wojciechowski, 920-832-7676.',
             'https://lawrence.presence.io/organization/lawrence-university-investment-club'),
            ('⚠ NO BLOCKCHAIN OR CRYPTOCURRENCY CLUB FOUND — BUT THE DIRECTORY IS NOT ENUMERABLE',
             'lawrence.presence.io/organizations is JAVASCRIPT-RENDERED and returned only meta tags and the '
             'title "Involve" — no organisation list at all. ⚠ ABSENCE HERE IS UNCONFIRMED, NOT VERIFIED, unlike '
             'UW-Stout where the directory is readable. Ask Aaron Wojciechowski, Assistant Director of Student '
             'Activities and Support for Student Organizations, who is the person who actually knows which clubs '
             'are alive: 920-832-7676.',
             'https://lawrence.presence.io/organizations'),
            ('⚠ SCALE NOTE',
             'Lawrence enrols roughly 1,500 students total and has a music conservatory attached, so a large '
             'share of the student body is conservatory rather than economics or computer science. The '
             'finance-adjacent population is small in absolute terms — perhaps a few dozen students. Judge the '
             'stop on that, not on the quality of the Investment Club.',
             'https://www.lawrence.edu/life-lawrence/get-involved')],
  'faculty': [('⚠ Dakota McKee',
               'Director of Student Engagement, Activities & Leadership — THE DECISION-MAKER AT LAWRENCE and the '
               'person to ask for the current student handbook\'s "Solicitation on Campus" section, which could '
               'not be read anywhere online. Direct line.',
               'Student Engagement, Activities, and Leadership (SEAL)',
               'dakota.mckee@lawrence.edu · 920-832-6698',
               'https://inside.lawrence.edu/offices/student-engagement-activities-and-leadership/staff'),
              ('⚠ Aaron Wojciechowski',
               'Assistant Director of Student Activities and Support for Student Organizations — THE PERSON WHO '
               'KNOWS WHICH CLUBS ARE ACTUALLY ALIVE, which matters more than usual here because the Presence '
               'directory is JavaScript-rendered and returned nothing. Ask him whether any crypto, blockchain, '
               'economics or entrepreneurship group exists, and how to reach the Investment Club. Direct line.',
               'Student Engagement, Activities, and Leadership (SEAL)',
               'aaron.wojciechowski@lawrence.edu · 920-832-7676',
               'https://inside.lawrence.edu/offices/student-engagement-activities-and-leadership/staff'),
              ('Hannah Osborne',
               'Student Events & Viking Room Fellow — programming and student events. Direct line.',
               'Student Engagement, Activities, and Leadership (SEAL)',
               'hannah.osborne@lawrence.edu · 920-832-6514',
               'https://inside.lawrence.edu/offices/student-engagement-activities-and-leadership/staff'),
              ('SEAL office',
               '4th floor, Warch Campus Center, 711 East Boldt Way, Appleton WI 54911. Mon–Fri 9:00 a.m.–5:00 '
               'p.m. Owns the rule that "designated university staff may enter into contracts: no deposits or '
               'verbal agreements should be made by a student," and the room reservation request form. Office '
               'main line.',
               'Student Engagement, Activities, and Leadership (SEAL)',
               'student.activities@lawrence.edu · (920) 832-6772 (main line)',
               'https://inside.lawrence.edu/offices/student-engagement-activities-and-leadership/student-organization-resources'),
              ('⚠ Conference & Event Services',
               'RENTS CAMPUS SPACE TO "COMMUNITY ORGANIZATIONS" — the only documented external route at '
               'Lawrence, and NOTHING about it is published: no rates, no eligibility criteria, no insurance '
               'terms, no deposits, no cancellation terms, no commercial restrictions. Office hours Mon–Fri '
               '8:00 a.m.–4:30 p.m.; tours by appointment only, Mon–Fri 9 a.m.–3 p.m. NO STAFF NAMES ARE LISTED. '
               'SPC 30, 711 East Boldt Way.',
               'Conference & Event Services / Office of Auxiliary Services',
               'events@lawrence.edu · (920) 832-6839',
               'https://www.lawrence.edu/our-neighbors/conference-event-services'),
              ('Title IX Coordinator',
               'Room 93, Brokaw Hall. Not relevant to tabling — carried across because it is THE ONLY PHONE '
               'NUMBER printed in the retrievable portion of the Lawrence student handbook PDF, and the handbook '
               'is otherwise the document that would answer the solicitation question.',
               'Lawrence University',
               '920-832-7490',
               'https://blogs.lawrence.edu/lucc/files/2023/08/V2-Student-HandbookCURRENT.pdf'),
              ('(Blockchain / crypto / fintech / monetary economics faculty)',
               'NOT CONFIRMED — no Lawrence faculty member on blockchain, cryptocurrency, fintech or monetary '
               'economics could be confirmed on a live page. Look up in the Economics department directory.',
               'Lawrence University',
               'no individual confirmed — look up here, or SEAL (920) 832-6772',
               'https://www.lawrence.edu/offices')],
  'courses': [('(Blockchain / crypto / fintech)',
               'NONE CONFIRMED. No Lawrence course on cryptocurrency, blockchain, digital assets or fintech could '
               'be found. ⚠ Note that under the trimester system students take only THREE courses per term, so '
               'the catalog is narrower than a semester school of comparable size and a specialist elective is '
               'less likely to exist.',
               'https://www.lawrence.edu/academics')],
  'events': [('⚠ NO LAWRENCE EVENTS COULD BE CONFIRMED',
              'No involvement fair, career fair, hackathon, speaker series or entrepreneurship week could be '
              'retrieved for Fall 2026. lawrence.presence.io is JavaScript-rendered; www7.lawrence.edu paths are '
              'robots-blocked; /offices/ URLs 302-redirect to inside.lawrence.edu. A SEAL "Annual Student '
              'Events" page exists but yielded nothing. Call SEAL, (920) 832-6772.',
              'https://www.lawrence.edu/offices/student-engagement-activities-and-leadership/activities-events/annual-events'),
             ('⚠ THE CALENDAR IS THE EVENT CONSTRAINT',
              'Fall Term runs Mon Sep 14 – Thu Nov 19, 2026, with exams Nov 22–24 and residence halls closing '
              'Nov 25. Any Lawrence activity must land between about Sep 21 (after the Sep 18 add/drop scramble) '
              'and Nov 12. That is a seven-week window that opens twelve days after every other Wisconsin '
              'campus and shuts three-and-a-half weeks before them.',
              'https://www.lawrence.edu/academics/trimester-schedule'),
             ('Hackathon — NONE FOUND',
              'No Lawrence hackathon could be confirmed.',
              '')],
  'play': 'The honest answer is SKIP LAWRENCE unless you are already in Appleton for Oshkosh, twenty miles away '
          '— and even then, treat it as a one-hour call rather than a day. Three reasons, in order. First, THE '
          'CALENDAR DOES NOT FIT ANYTHING ELSE IN WISCONSIN. Lawrence runs TRIMESTERS — three 10-week terms, '
          'three courses at a time — and Fall Term is Mon Sep 14 to Thu Nov 19, with exams Nov 22–24 and '
          'residence halls closing Nov 25. It STARTS TWELVE DAYS AFTER the rest of the state and is COMPLETELY '
          'OVER BY NOVEMBER 24, three-and-a-half weeks before everyone else. There is no December window at all, '
          'and the add/drop deadline is Sep 18, four days after classes begin, so the first week is chaos. The '
          'usable strip is roughly Sep 21 to Nov 12. Second, THE SCALE. Lawrence enrols about 1,500 students '
          'with a conservatory attached; the finance-adjacent population is perhaps a few dozen. The only '
          'relevant club that could be confirmed is the Lawrence University Investment Club, which does manage a '
          'real slice of the endowment — genuinely interesting, and it publishes no contact. Third, NOTHING IS '
          'READABLE. Lawrence is private, so no state law helps; its Presence directory is JavaScript-rendered '
          'and yielded no club list; its www7 policy paths are robots-blocked; its /offices/ URLs redirect to a '
          'separate host; and the "Solicitation on Campus" section of the student handbook sits at page 102 of a '
          'PDF that truncated at page 32. We do not know what the rules are. IF YOU DO GO: one call to Aaron '
          'Wojciechowski at 920-832-7676 answers the club question, and one to Dakota McKee at 920-832-6698 gets '
          'the handbook\'s solicitation section. If a paid route matters, Conference & Event Services at '
          '(920) 832-6839 rents to "community organizations" and publishes literally nothing about terms. And '
          'know before anyone shakes hands: at Lawrence a student cannot commit to anything — "designated '
          'university staff may enter into contracts: no deposits or verbal agreements should be made by a '
          'student."',
  'gaps': ['⚠⚠ THE SOLICITATION POLICY. The student handbook has a "Solicitation on Campus" section at PAGE 102; '
           'the archived PDF truncated at page 32 and the current handbook URL '
           '(www7.lawrence.edu/students/activities/student-organization-handbook) is ROBOTS-BLOCKED. We do not '
           'know Lawrence\'s rules. Dakota McKee, 920-832-6698.',
           '⚠ Whether ANY Lawrence involvement fair, org fair or activities fair exists — none could be '
           'confirmed for Fall 2026 or any year, because lawrence.presence.io is JavaScript-rendered. SEAL, '
           '(920) 832-6772.',
           '⚠ Whether any blockchain, crypto, economics or entrepreneurship club exists — the Presence directory '
           'returned no organisation list at all, so the absence is UNCONFIRMED rather than verified. Aaron '
           'Wojciechowski, 920-832-7676.',
           'Conference & Event Services terms for community organisations — rates, eligibility, insurance, '
           'deposits, cancellation and commercial restrictions are ALL unpublished. (920) 832-6839.',
           'A contact for the Lawrence University Investment Club — no email and no advisor are published. '
           'Aaron Wojciechowski, 920-832-7676.',
           'Whether Lawrence runs any career fair, speaker series or hackathon in Fall 2026 — nothing could be '
           'retrieved. (920) 832-6772.',
           'Whether the mid-term reading period (Oct 22–25) empties the campus the way a fall break does. '
           '(920) 832-6772.',
           '⚠ ROBOTS/REDIRECT NOTE to preserve: www7.lawrence.edu paths are ROBOTS-BLOCKED; www.lawrence.edu '
           '/offices/ URLs 302-REDIRECT to inside.lawrence.edu; and www7.lawrence.edu/s/registrar/calendar '
           'redirects to the trimester-schedule page. A large share of Lawrence content is simply unreadable to '
           'research tooling.'],
  'note': '⚠⚠ THE TRIMESTER IS THE HEADLINE. Nothing about Lawrence\'s calendar lines up with any other campus '
          'in this packet: it starts Sep 14, twelve days late, and finishes Nov 24, three-and-a-half weeks '
          'early. If a statewide Wisconsin activity is planned for late November or December, LAWRENCE WILL BE '
          'CLOSED. Appleton is 20 miles from Oshkosh and about 90 minutes north of Milwaukee, so the two north-'
          'eastern campuses pair naturally — but Oshkosh does not start until Sep 9 and Lawrence not until '
          'Sep 14, making that pair the LAST stop of any Wisconsin tour, not the first.'},
]

DEADLINES = [

 # ---- HARD MONEY DEADLINES ------------------------------------------------
 ('2026-08-28', 'Aug 28, 2026', 'UW–Madison',
  '⚠⚠ ALL-CAMPUS CAREER FAIR REGISTRATION AND PAYMENT CLOSE — $900 FOR-PROFIT TABLE',
  'The single most time-critical item in Wisconsin. "Organizations must register and submit payment no later '
  'than Friday, August 28, 2026" to appear in printed guides. Fair is Wed Sep 16, 2026 at the Kohl Center. '
  'For-Profit $900 · Government $400 · Start-Up/Small Business $300 · Non-Profit $150; includes one 8-foot '
  'table and two chairs. This is the ONLY fully-priced, no-sponsorship-required commercial access to '
  'UW-Madison students that exists — every other Madison door requires a university unit to sponsor and attend.',
  'https://careerfair.wisc.edu/employers/',
  'Brandon Spoon · brandon.spoon@wisc.edu · (608) 262-3921'),

 ('2026-09-04', 'Sep 4, 2026', 'UW Oshkosh',
  '⚠⚠ UWO CAREER FAIR CANCELLATION CUTOFF — NO REFUNDS AFTER THIS DATE',
  'Fair is Wed Sep 30, 2026, 11:30am–3:30pm, Kolf Sports Center. Cancel by Sep 4 for a refund minus a $50 '
  'processing fee; NO REFUNDS AFTER. Tiered pricing: Early bird $375 (20 available) · $425 (20) · $450 (20) · '
  '$475 (unlimited); K-12 $150; Government/Social Assistance $250; electric booth +$75. "Payment must be '
  'received within 48 hours" of registering. Up to 200 employers, 800+ job seekers.',
  'https://www.uwosh.edu/career/employers/events/',
  'Chrissy Lambie · lambiec@uwosh.edu · (920) 424-2181'),

 ('2026-09-17', 'Sep 17, 2026', 'UW–Whitewater',
  '⚠⚠ WARHAWK CAREER FAIR REGISTRATION CLOSES 6:00 P.M. — AND IT IS INVITATION-ONLY',
  'Two gates, not one. Registration closes Thu Sep 17 at 6:00pm OR at capacity, whichever comes first — but '
  'first you must be invited: "Organizations without previous attendance must request an invitation by emailing '
  'career@uww.edu with company name, primary contact details, opportunity types, and target majors." SEND THAT '
  'EMAIL WEEKS EARLY. Fair is Wed Sep 30, 2026, 11:00am–3:30pm, DLK Kachel Fieldhouse, Williams Center. '
  'Standard $400 · Non-profit $175 · Career Services sponsor partners FREE. Extra fees for additional '
  'representatives and electrical access.',
  'https://www.uww.edu/career/employer-resources/employer-career-fairs',
  'career@uww.edu · (262) 472-1471'),

 # ---- THE SEPTEMBER 9 COLLISION -------------------------------------------
 ('2026-09-09', 'Sep 9, 2026', 'All Wisconsin campuses',
  '⚠⚠ SIX OF THE STATE\'S NINE FAIRS FALL ON THIS ONE WEDNESDAY, IN SIX DIFFERENT CITIES',
  'You cannot cover them; you must choose. Madison Student Organization Fair (Sep 9 AND 10, 5–8pm, Kohl Center '
  '— RSO ONLY) · UW-Eau Claire Blu\'s Organizations Bash (11am–1pm, Central Campus Mall — RSO ONLY) · '
  'UW-La Crosse Sample the City & Volunteer Fair (10am–1pm — LOCAL BUSINESSES WELCOME) · UW-Whitewater '
  'Involvement Fair (rain date Sep 10, time/location unpublished) · UW-Stout Meet Menomonie (4–7pm — '
  'CHAMBER-RUN, BUSINESSES WELCOME) · UW-La Crosse Part-Time Job Fair. Only TWO of the six admit outside '
  'businesses, and they are 190 miles apart: La Crosse and Menomonie. Oshkosh\'s Titan Fest is the day before '
  '(Tue Sep 8) and Marquette\'s O-Fest the day after (Thu Sep 10).',
  'https://www.uwlax.edu/university-centers/orgs/lic/',
  'La Crosse: Amanda Krafft 608-785-8902 · Stout/Menomonie: chamber (715) 235-9087'),

 ('2026-09-09', 'Sep 9, 2026', 'UW–Stout',
  '⚠⚠ MEET MENOMONIE — THE CLEANEST COMMERCIAL STRUCTURE IN WISCONSIN, PRICE UNPUBLISHED',
  'Wed Sep 9, 2026, 4:00–7:00pm, ON THE UW-STOUT CAMPUS but run by the MENOMONIE AREA CHAMBER OF COMMERCE, not '
  'the university. Sold to businesses as "an exclusive opportunity to connect with UW-Stout students"; '
  'exhibitors "showcase products, highlight employment opportunities, and build relationships with potential '
  'customers, volunteers, and future employees." Platinum and Gold sponsorship levels are named and NO PRICE OR '
  'DEADLINE IS PUBLISHED. A private organiser\'s guest list is not a university solicitation permit — the '
  'chamber has no commercial-use rule to apply. CALL NOW; the event is four weeks out.',
  'https://www.menomoniechamber.org/meetmenomonie/',
  'Menomonie Area Chamber of Commerce · info@menomoniechamber.org · (715) 235-9087'),

 ('2026-09-09', 'Sep 9, 2026', 'UW–La Crosse',
  '⚠⚠ SAMPLE THE CITY & VOLUNTEER FAIR — "LOCAL BUSINESSES AND NON-PROFITS CAN REGISTER HERE"',
  'Wed Sep 9, 2026, 10:00am–1:00pm. The ONLY campus event in Wisconsin whose own page invites businesses to '
  'register. Registration form is LIVE: https://uwlax.iad1.qualtrics.com/jfe/form/SV_8ppQc49Lby5Fh5A — cost and '
  'deadline are NOT PUBLISHED. Two questions for the call: what does it cost, and is "local" enforced against '
  'an out-of-area company? Register early rather than waiting for a deadline that may never be announced.',
  'https://www.uwlax.edu/university-centers/orgs/lic/',
  'Amanda Krafft · akrafft@uwlax.edu · 608-785-8902'),

 # ---- TERM STARTS ---------------------------------------------------------
 ('2026-08-31', 'Aug 31, 2026', 'Marquette',
  '⚠ CLASSES BEGIN — EARLIEST START IN WISCONSIN',
  'Two days ahead of the entire UW system and fifteen ahead of Lawrence. Marquette is already in session. Add/'
  'drop Sep 8. Two fall breaks (Oct 1–2 and Oct 22–23), Thanksgiving Nov 25–29, last classes Sat Dec 12, exams '
  'Dec 14–19. ⚠ Dates genuinely differ by school — Undergraduate, Graduate, Health Science, Dental and Law each '
  'run their own table, and Law exams start a week earlier (Dec 7).',
  'https://www.marquette.edu/central/registrar/2026-fall-academic-calendar.php',
  'AMU Student Engagement Services (414) 288-7250'),

 ('2026-09-02', 'Sep 2, 2026', 'Five UW campuses',
  'CLASSES BEGIN — MADISON, MILWAUKEE, EAU CLAIRE, WHITEWATER AND STOUT ALL ON THE SAME DAY',
  'Madison has NO FALL BREAK — full density Sep 2 through Nov 25, the best sustained window at the flagship. '
  'Milwaukee has the LONGEST term in the state, exams running to Dec 23. Whitewater starts at 8:00 a.m. sharp '
  'and its term ends on a SATURDAY, Dec 12. ⚠ UW-Stout\'s add/drop, Thanksgiving and finals dates could NOT be '
  'retrieved from any registrar page — only the Sep 2 – Dec 18 term boundary is confirmed, from the systemwide '
  'calendar.',
  'https://www.wisconsin.edu/academic-calendars/academic-year-2026-27/',
  'UW-Stout Career Services (715) 232-1122 — the only confirmed number on that campus'),

 ('2026-09-08', 'Sep 8, 2026', 'UW–La Crosse / UW Oshkosh',
  'UW-LA CROSSE CLASSES BEGIN; UW OSHKOSH TITAN FEST (the day before Oshkosh classes)',
  'La Crosse starts Tue Sep 8, the day after Labor Day. Oshkosh\'s Titan Fest runs Tue Sep 8, 11:00am–1:30pm '
  'across campus — the day BEFORE Oshkosh classes begin Sep 9. Titan Fest eligibility for outside groups is not '
  'stated; ask whether the $75 Category C concourse table can be bought at the fair specifically.',
  'https://www.uwosh.edu/newstudents/welcome/',
  'Reeve Union reservations (920) 424-2435 · New Student Programs (920) 424-2909'),

 ('2026-09-09', 'Sep 9, 2026', 'UW Oshkosh',
  'CLASSES BEGIN — LATEST START OF ANY PUBLIC CAMPUS IN WISCONSIN',
  'A full week behind Madison. If the first week of September is oversubscribed elsewhere, Oshkosh is still '
  'ahead of you. ⚠ Add/drop deadlines and FINAL EXAM DATES are NOT on the academic calendar PDF; the semester '
  'ends Dec 18 with commencement Dec 19, leaving no obvious exam week. Confirm before scheduling in December.',
  'https://www.uwosh.edu/academic-affairs/calendars/',
  'Reeve Union reservations (920) 424-2435'),

 ('2026-09-14', 'Sep 14, 2026', 'Lawrence University',
  '⚠⚠ FALL TRIMESTER BEGINS — LATEST START IN WISCONSIN, AND THE TERM IS OVER NOV 24',
  'Lawrence runs THREE 10-WEEK TERMS, three courses at a time. Fall Term Mon Sep 14 – Thu Nov 19; reading period '
  'Nov 20–21; exams Nov 22–24; residence halls close Nov 25. ⚠⚠ THERE IS NO DECEMBER WINDOW AT LAWRENCE AT ALL '
  '— it opens twelve days after the rest of Wisconsin and shuts three-and-a-half weeks before. Add/drop is '
  'Fri Sep 18, FOUR DAYS after classes begin. The usable strip is roughly Sep 21 – Nov 12.',
  'https://www.lawrence.edu/academics/trimester-schedule',
  'Dakota McKee, Director of SEAL · dakota.mckee@lawrence.edu · 920-832-6698'),

 # ---- FAIRS AND EVENTS ----------------------------------------------------
 ('2026-09-10', 'Sep 10, 2026', 'Marquette',
  'O-FEST 2026 — STUDENT ORGS AND CAMPUS DEPARTMENTS ONLY, ONE TABLE EACH',
  'Thu Sep 10, 2026, 4:00–7:00pm, Central Mall. Two registration forms exist (student org, university '
  'department) and there is no third form for anyone else. Useful as a SCOUTING visit — walking the mall to see '
  'which clubs are alive is not solicitation — but not as a tabling opportunity. Registration opened April 2026 '
  'via marquette.presence.io; deadline not stated.',
  'https://today.marquette.edu/2026/04/o-fest-2026-registration-open/',
  'engaged@marquette.edu · AMU Student Engagement Services (414) 288-7250'),

 ('2026-09-16', 'Sep 16, 2026', 'UW–Madison',
  '⚠ ALL-CAMPUS CAREER & INTERNSHIP FAIR — THE EVENT ITSELF',
  'Wed Sep 16, 2026, Kohl Center. Registration and payment closed Aug 28. $900 for-profit tier. If the Aug 28 '
  'deadline is missed there is no other priced, sponsorship-free route to Madison students all semester — the '
  'fallback is a guest lecture through Brad Chandler or sponsoring MadHacks in November.',
  'https://careerfair.wisc.edu/employers/',
  'Brandon Spoon · (608) 262-3921'),

 ('2026-09-23', 'Sep 23, 2026', 'UW–Eau Claire',
  '⚠ ACTUARIAL, ACCOUNTING AND FINANCE CAREER FAIR — HIGHEST-FIT AUDIENCE AT UWEC',
  'Wed Sep 23, 2026. The most targeted finance audience of UWEC\'s five fall fairs. ⚠ EMPLOYER REGISTRATION '
  'COST IS NOT PUBLISHED for this or any other UWEC fair. Also Part-Time Job Fair Fri Sep 11; Science and Tech '
  'Breakfast AND All Majors Career Fair both Wed Sep 30 (same day, choose one); Health Career, Professional & '
  'Graduate School Fair Wed Oct 21.',
  'https://www.uwec.edu/offices-services/advising-retention-career-center/career-services',
  'Career Services (ARCC) · arcc@uwec.edu · 715-836-3487'),

 ('2026-09-30', 'Sep 30, 2026', 'UW Oshkosh / UW–Whitewater',
  '⚠⚠ TWO PRICED CAREER FAIRS ON THE SAME DAY, 130 MILES APART — CHOOSE',
  'UW Oshkosh Internship & Career Fair, 11:30am–3:30pm, Kolf Sports Center — $375–$475 tiers, +$75 for '
  'electricity, up to 200 employers and 800+ job seekers, Chrissy Lambie (920) 424-2181. UW-Whitewater Fall '
  'Warhawk Internship & Career Fair, 11:00am–3:30pm, DLK Kachel Fieldhouse — $400 standard / $175 non-profit, '
  'INVITATION ONLY, registration closed Sep 17, career@uww.edu (262) 472-1471. Whitewater has the blockchain '
  'club; Oshkosh has the cheaper table and no invitation gate.',
  'https://www.uwosh.edu/career/employers/events/',
  'Oshkosh (920) 424-2181 · Whitewater (262) 472-1471'),

 ('2026-10-14', 'Oct 14, 2026', 'UW–La Crosse',
  '⚠ FALL CAREER & INTERNSHIP FAIR — FREE FOR EMPLOYERS',
  'Wed Oct 14, 2026, 10:00am–2:00pm, Student Union. COST: FREE. Registration through Handshake, opened May 1, '
  '2026 at 8:00am. THE CHEAPEST CONFIRMED COMMERCIAL ACCESS TO STUDENTS IN WISCONSIN — a university-run event, '
  'no fee, no invitation required. Also worth asking Rebecca Lee to add DGD to the invitation lists for the '
  'Accounting Career Fair (Sep 28), Science & Math Career Forum (Nov 6) and REXPO (Nov 11), all three of which '
  'are invitation-only.',
  'https://www.uwlax.edu/aaccs/employers/recruit-at-uwl/',
  'Rebecca Lee · rlee@uwlax.edu · 608-785-8362'),

 ('2026-11-19', 'Nov 19, 2026', 'Lawrence University',
  '⚠⚠ LAST DAY OF LAWRENCE FALL TERM — THE CAMPUS EMPTIES',
  'Classes end Thu Nov 19; reading period Nov 20–21; exams Nov 22–24; residence halls close Nov 25. Lawrence '
  'students do not return until January. ANYTHING SCHEDULED AT LAWRENCE AFTER ROUGHLY NOV 12 IS WORTHLESS. If a '
  'statewide Wisconsin push is planned for late November or December, Lawrence will be closed while every other '
  'campus is still running.',
  'https://www.lawrence.edu/academics/trimester-schedule',
  'SEAL (920) 832-6772'),

 ('2026-11-25', 'Nov 25, 2026', 'All Wisconsin campuses',
  '⚠ THANKSGIVING RECESS BEGINS ACROSS THE STATE — NOTE THE STAGGERED CUTOFFS',
  'Whitewater breaks EARLIEST, 9:00pm Tue Nov 24, and Oshkosh\'s recess "begins after EVENING classes on '
  'November 24." La Crosse breaks Wed Nov 25 at 5:30pm — Nov 25 is a full teaching day there until evening. '
  'Madison Nov 26–29; Milwaukee Nov 25–29; Eau Claire Nov 25–27 with Thanksgiving Day closure Nov 26; Marquette '
  'Nov 25–29. Everyone resumes Mon Nov 30. Lawrence is already finished. ⚠ UW-Stout\'s Thanksgiving dates could '
  'NOT be retrieved.',
  'https://www.wisconsin.edu/academic-calendars/academic-year-2026-27/',
  'UW-Stout Career Services (715) 232-1122 to close the Stout calendar gap'),

 # ---- MONITOR / UNDATED ---------------------------------------------------
 ('', 'Weekend before Thanksgiving — MONITOR', 'UW–Madison',
  '⚠ MADHACKS FALL 2026 DATES NOT YET PUBLISHED — THE BEST HACKATHON SPONSORSHIP IN THE STATE',
  '"The largest hackathon in Wisconsin": 400+ participants in 2025, the biggest turnout in its history, 24 hours '
  'overnight at Morgridge Hall. 2025 dates were Nov 22–23; the pattern is the weekend before Thanksgiving, which '
  'in 2026 would be Nov 21–22. STUDENT-RUN AND PRIVATELY SPONSORED, so UW-Madison\'s commercial-activity '
  'carve-out does not reach it at all. Past sponsors: American Family Insurance, Capital One, Epic, Google, '
  'MG&E, TDS, Fish Audio, Mastra. Email now to get on the 2026 sponsor list.',
  'https://www.madhacks.io/',
  'team@madhacks.io · no phone published — email only'),

 ('', 'Anytime — the best door in Wisconsin', 'UW–Whitewater',
  '⚠⚠ CALL PAUL NYLEN — ADVISOR TO THE ONLY BLOCKCHAIN CLUB IN THE STATE',
  'Associate Professor of Accounting, (262) 472-5453, nylenp@uww.edu. Advisor to the Blockchain and '
  'Cryptocurrency Student Organization — 110 MEMBERS, 9 OFFICERS, running "Major Events (2-3 per semester): '
  'industry panels, guest speakers, hands-on workshops" plus biweekly Wednesday discussion groups about Bitcoin '
  'and markets. WPR named him "faculty director of UW-Whitewater\'s Blockchain and Cryptocurrency Institute" '
  'when Wisconsin\'s pension fund bought $164M of bitcoin ETFs; he said the state was "a little under-invested." '
  'A guest-speaker slot is non-commercial, free, in front of 110 self-selected students, and entirely outside '
  'the campus sales-and-solicitation policy. ⚠ Also ask whether the Institute still exists — it has NO PAGE ON '
  'uww.edu and is confirmed only in WPR and LinkedIn.',
  'https://uww.campusgroups.com/blockchaincrypto/home/',
  'Paul Nylen · nylenp@uww.edu · (262) 472-5453'),

 ('', 'Anytime — second-best door', 'UW–Whitewater',
  '⚠ THE UWW FMA PUBLICLY ADVERTISES A CORPORATE-PARTNERS PROGRAMME',
  'The Financial Management Association is the blockchain club\'s parent body and runs sister clubs including a '
  'Crypto Club, plus an Applied Investments Program with cash prizes. Meets TUESDAYS 5:30 P.M., HH2203, BAKER '
  'TILLY HALL. Its site carries a "Corporate Partners" page — "Meet the firms behind the mission," "Enabling the '
  'next generation of finance professionals." A student-run, publicly advertised sponsorship channel that sits '
  'outside the campus sales policy entirely. Ask also whether the "Crypto Club" and the Blockchain and '
  'Cryptocurrency Student Organization are the same body under two names.',
  'https://uwwfma.org/',
  'fma@uww.edu · via Paul Nylen (262) 472-5453'),

 ('', 'Before any Oshkosh visit — cheapest table in the state', 'UW Oshkosh',
  '⚠⚠ BUY THE $75 CATEGORY C CONCOURSE TABLE — THE ONLY PUBLISHED FOR-PROFIT RATE IN WISCONSIN',
  'Reeve Memorial Union publishes three categories: A = "University Recognized Student Organizations/Clubs '
  '(RSOs)", B = "Departments, Faculty, and Staff", C = "OTHER INDIVIDUALS/GROUPS". DGD is C, and a CONCOURSE '
  'TABLE IS $75 (A and B pay $0) — against $900 for a for-profit table at Madison. Other Category C rates: Upper '
  'Marketplace $300, Titan Underground $600, Lower Marketplace $600, Blackhawk Commons $700, Room 227ABC $1,000; '
  'labour $75/hr, A/V tech $25/hr, equipment $5–$150. THREE THINGS ON THE CALL: buy the table; file the '
  'solicitation request (the policy requires approved requests "AT LEAST 7 DAYS PRIOR"); get the University '
  'Facility Use Agreement, which non-university groups must have on file. Then confirm out loud that no '
  'insurance certificate is required — none is published, and absence of text is not permission. Conduct rule to '
  'know in advance: "Individuals staffing the table must stay directly in front of/behind the assigned table. '
  'Table staff are not permitted to roam the area or building."',
  'https://www.uwosh.edu/reeve/event-planning/rates/',
  'Reeve Union reservations · reevereserve@uwosh.edu · (920) 424-2435'),

 ('', 'Before any La Crosse booking — fronting is DISCOUNTED here', 'UW–La Crosse',
  '⚠ UWL PRICES FRONTING AT 50% INSTEAD OF BANNING IT — UNIQUE IN WISCONSIN',
  'Published tiers: FIRST PRIORITY, NO FEES — UWL departments and RSOs for campus-community events without '
  'revenue generation. SECOND PRIORITY, 50% OF THE UNIVERSITY RATE — "events primarily developed by EXTERNAL '
  'GROUPS where a UWL department/RSO requests space ON THEIR BEHALF." EXTERNAL CUSTOMERS, standard rate. Every '
  'other campus in this packet forbids that middle arrangement or is silent; UWL writes it down and halves the '
  'price. ⚠ NO RATE CARD IS PUBLISHED — the tiers are defined against a "University Rate" that appears nowhere. '
  'Also: the Facility Use Waiver must be signed and returned AT LEAST TWO WEEKS before the event; "EXTERNAL '
  'GROUPS CANNOT RESERVE TABLING AT THE CLOCKTOWER"; a no-show costs an external group 100% of fees and a third '
  'no-show suspends privileges for the semester; insurance is set case by case by Risk Management with no '
  'published limit.',
  'https://www.uwlax.edu/reservations/policies/',
  'Hayley Harnden · hharnden@uwlax.edu · 608-785-6600 · Reservations 608-785-8895'),

 ('', 'Before any Madison plan — read this first', 'UW–Madison',
  '⚠ THE COMMERCIAL CARVE-OUT THAT CLOSES MADISON\'S FRIENDLY-LOOKING DOOR',
  'UW-6013 Expressive Activity (eff. 08-27-2024) reads generously — "University community members AS WELL AS '
  'VISITORS may use outdoor public university areas for expressive activity" — and then removes DGD from it: '
  '"COMMERCIAL ACTIVITY (RELATED TO A COMMERCIAL TRANSACTION OR AN ADVERTISEMENT TO PROMOTE THE SALE OF GOODS OR '
  'SERVICES) IS EXCLUDED." Reinforced by UW-2058: "Groups or individuals engaged in free expression activities '
  '(e.g., leafletting, surveying, petitioning) MUST BE UW-MADISON STUDENTS, STAFF, OR FACULTY." And by UW-6000, '
  'which routes non-university use through a sponsoring university DEPARTMENT whose head "must be present for '
  'the duration of a sponsored event." And by the Student Organization Fair rules: "Your organization may not '
  'allow a corporate sponsor to use your table for promotion." Do not plan to table at Madison.',
  'https://policy.wisc.edu/library/UW-6013',
  'Nancy Lynch, VC Legal Affairs (608) 263-7400 · Space Mgmt (608) 556-7741'),

 ('', 'Before any Marquette handshake', 'Marquette',
  '⚠⚠ MARQUETTE MONEY AND PAYMENT-CREDENTIAL TERMS — 75% DEPOSIT, AND CREDIT-CARD FUNDRAISERS BARRED',
  'Non-University Groups: "A DEPOSIT OF 75% OF THE ESTIMATED CHARGES WILL BE DUE UPON RECEIPT. Balance payment '
  'will be due ten (10) business days prior to the event" — against an estimate nobody can see in advance, '
  'because NO RATE CARD, NO INSURANCE REQUIREMENT AND NO CANCELLATION SCHEDULE ARE PUBLISHED ANYWHERE. Get all '
  'three in writing before paying. ⚠ ANTI-FRONTING: "University departments and student organizations may not '
  'reserve space or equipment for, or on the behalf of, an outside organization"; if discovered, non-university '
  'rates apply. ⚠ COMMERCIAL SOLICITATION is defined to include "distributing any kind of written or printed '
  'materials" and needs prior approval. ⚠⚠ PAYMENT CREDENTIALS — the most relevant sentence in Wisconsin: '
  '"FUNDRAISERS INVOLVING CREDIT CARDS (E.G., CREDIT CARD APPLICATIONS) WILL NOT BE APPROVED." Ask AMU Student '
  'Engagement Services whether that reaches wallet installs, exchange referrals or on-site account openings. '
  'Also "no raffles, lotteries or sweepstakes may be held" — which kills a giveaway.',
  'https://www.marquette.edu/event-services/amu-space-reservation-policy.php',
  'AMU Event Services (414) 288-7202 · Student Engagement Services (414) 288-7250'),

 ('', 'Before routing anything through Menomonie', 'UW–Stout',
  '⚠⚠ UW-STOUT IS A BLANK PAGE ON THE UNIVERSITY SIDE — ONE HOUR ON THE PHONE FIRST',
  'NOT ONE Fall 2026 date beyond the Sep 2 – Dec 18 term boundary is confirmed: three registrar pages '
  '(/important-dates-times, /academic-registration-calendars, /fall-2026-registration-information) all render '
  'dynamically and returned nothing, one carrying a mislabeled "Evaluation Dates: Fall 2024" link. NO campus '
  'solicitation or facility-use policy exists at any retrievable URL. NO phone number could be confirmed for the '
  'Involvement Center, the Memorial Student Center or Registration & Records — every connect.uwstout.edu staff '
  'page returned empty chrome. GET: the Fall 2026 add/drop, Thanksgiving and finals dates; the written '
  'solicitation policy; Career Conference Week dates and fees; and the unpublished Career Services Partnership '
  'Program tiers. Career Services, (715) 232-1122, is the ONLY confirmed university number on this campus. '
  '⚠ AUDIENCE NOTE: Stout\'s club directory IS readable and contains NO finance, investment, economics or crypto '
  'organisation at all — the AI Club and AWS Cloud Club are the audience, and they want the engineering story.',
  'https://www.uwstout.edu/academics/academic-services/registration-records-office/important-dates-times',
  'UW-Stout Career Services · careerservices@uwstout.edu · (715) 232-1122'),

 ('', 'Before deciding whether Lawrence is worth a stop', 'Lawrence University',
  '⚠ LAWRENCE IS UNREADABLE AND ITS TERM ENDS NOV 24 — TWO CALLS, NOT A DAY TRIP',
  'The "Solicitation on Campus" section sits at PAGE 102 of a student handbook whose archived PDF truncated at '
  'page 32 and whose current URL is ROBOTS-BLOCKED; lawrence.presence.io is JAVASCRIPT-RENDERED and returned no '
  'club list at all; www7.lawrence.edu paths are robots-blocked and /offices/ URLs redirect to '
  'inside.lawrence.edu. We do not know Lawrence\'s rules and cannot confirm what clubs exist. Lawrence is '
  'PRIVATE — no state law helps. Two calls settle it: Aaron Wojciechowski, 920-832-7676, for whether any crypto, '
  'economics or entrepreneurship club exists; Dakota McKee, 920-832-6698, for the handbook\'s solicitation '
  'section. Know before anyone shakes hands: "DESIGNATED UNIVERSITY STAFF MAY ENTER INTO CONTRACTS: NO DEPOSITS '
  'OR VERBAL AGREEMENTS SHOULD BE MADE BY A STUDENT." Scale check: ~1,500 students with a conservatory attached.',
  'https://inside.lawrence.edu/offices/student-engagement-activities-and-leadership/staff',
  'Aaron Wojciechowski 920-832-7676 · Dakota McKee 920-832-6698 · SEAL (920) 832-6772'),

 ('', 'Before any UWM plan', 'UW–Milwaukee',
  '⚠ UWM ADMITS OUTSIDE GROUPS FOR RECRUITMENT ONLY — AND THE FAIR PAGE IS FIVE YEARS STALE',
  'Verbatim: "OUTSIDE CLIENTS MAY ONLY USE AN ATRIUM BOOTH FOR THE PURPOSES OF EMPLOYMENT RECRUITMENT, WITH '
  'PROPER SPONSORSHIP AND PAYMENT. NO COMMERCIAL SOLICITATION IS PERMITTED." Sponsorship does not cure it: an '
  'RSO "cannot sponsor non-University groups... EXCEPT IN THE UNION BUILDING," and the Union is exactly where '
  'commercial solicitation is banned. If DGD has any hiring, internship or ambassador programme, recruitment is '
  'the lawful door — ask Union Event Services to draw the line for you in their words before spending money. '
  '⚠ ALSO: the Fall 2026 Involvement Fair date is UNPUBLISHED and uwm.edu/welcome/event/involvement-fair/ still '
  'renders "September 14, 2021" — five years out of date. Call 414-229-5780 for the real date. ⚠ LEAD TIMES ARE '
  'THE LONGEST IN THE STATE: a paid speaker needs a planning meeting 5–6 weeks out and a contract 30 days out; '
  'even an unpaid speaker needs a contract 14 days prior.',
  'https://uwm.edu/union/event-services/faqs/',
  'Union Event Services 414-229-4828 · Student Involvement 414-229-5780'),

 ('', 'Before any UWEC visit', 'UW–Eau Claire',
  '⚠ UWEC CHARGES A FEE IT NEVER QUANTIFIES — AND DEFINES SOLICITATION TO INCLUDE FREE HANDOUTS',
  'The policy (last updated Tue Mar 31, 2026) defines solicitation as "SELLING, PEDDLING, AND/OR DISTRIBUTION OF '
  'MATERIAL, FREE OR OTHERWISE" — free swag counts. "No such use of University structures and/or grounds will be '
  'permitted without registration and permission of the appropriate office," routed to the Director of '
  'University Centers (grounds: Assistant Chancellor; academic buildings: Vice Chancellor). "NON-STUDENT '
  'INDIVIDUALS/GROUPS... WILL BE CHARGED A FEE" and the amount is nowhere. INSURANCE IS PUBLISHED, unusually: '
  'CGL $1,000,000 each occurrence / $2,000,000 aggregate, plus $1M sexual abuse, $1M professional, $100K fire '
  'legal, $1M liquor, $1M auto, via TULIP, naming "Board of Regents of the University of Wisconsin System, its '
  'officers, employees, and agents" as additional insured. Buy the certificate before you call. Ask Jake Serwe '
  'for the tabling fee AND the price list for the advertised partnership menu (naming rights, event '
  'sponsorship, digital displays, elevator wraps, table tents).',
  'https://kb.uwec.edu/articles/policies-solicitation-on-university-premises',
  'Jake Serwe · serwej@uwec.edu · 715-836-4150 · University Centers 715-836-4636'),

 ('', 'Monitor — statewide', 'All Wisconsin campuses',
  '⚠⚠ THERE IS NO WISCONSIN CAMPUS FREE-SPEECH STATUTE — DO NOT LET AN AMBASSADOR CITE ONE',
  '2025 Senate Bill 498 passed the legislature Feb 12, 2026, 53-45 on party lines, after Governor Evers had '
  'already said on Jan 6, 2026 that he would veto it. AB 299 (2017), AB 444 (2019) and AB 553 (2023) all died '
  'earlier. Citing "Wisconsin\'s campus free speech law" means citing a vetoed bill and being corrected on the '
  'spot. THE REAL LAW IS Wis. Admin. Code UWS 18.11(8): "No person may sell, peddle or solicit for the sale of '
  'goods, services, or contributions on any university lands EXCEPT in the case of: (a) SPECIFIC PERMISSION IN '
  'ADVANCE FROM A SPECIFIC UNIVERSITY OFFICE... (d) ...selling, and soliciting activities BY OR UNDER THE '
  'SPONSORSHIP OF a university or REGISTERED STUDENT ORGANIZATION." Those two exceptions are DGD\'s only public-'
  'campus doors — and unlike Oklahoma, the Wisconsin code EXPRESSLY BLESSES the club-sponsorship route. Note '
  'also Regent Policy Document 4-21 (adopted Oct 6, 2017), which reaches "visitors" but contains NO commercial-'
  'speech provision. ⚠ Marquette and Lawrence are PRIVATE and bound by none of it. ⚠ docs.legis.wisconsin.gov '
  'is ROBOTS-BLOCKED at subsection level and returns a proxy 403 to direct fetches — cite the Justia mirror.',
  'https://regulations.justia.com/states/wisconsin/uws/chapter-uws-18/section-uws-18-11/',
  'No single office — see each campus\'s policy contact'),

 ('', 'Conversational opener — statewide', 'All Wisconsin campuses',
  'WISCONSIN\'S OWN PENSION FUND BOUGHT $164 MILLION OF BITCOIN ETFs — AND IT IS VERIFIABLY TRUE',
  'The State of Wisconsin Investment Board purchased $164 million of shares in two spot bitcoin ETFs in early '
  '2024, the first US state pension fund to do so. UW-Whitewater\'s Paul Nylen was WPR\'s on-record expert, '
  'calling the state "a little under-invested" — under 1% allocated where he thought 1–3% appropriate. This is '
  'the best opener in the state, it flatters a local institution, and it hands an ambassador a Wisconsin '
  'professor\'s name to cite. Article dated May 24, 2024 (updated May 29).',
  'https://www.wpr.org/news/wisconsin-invest-bitcoin-efts-uw-whitewater-professor',
  'Paul Nylen · nylenp@uww.edu · (262) 472-5453'),
]
