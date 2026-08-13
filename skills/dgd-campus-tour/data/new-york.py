"""New York — campus records and dated action items for the DGD Campus Tour skill.

Every field traces to a live university URL. Empty string or "UNVERIFIED" means
not published at time of research — a gap to close by phone, not a finding of absence.
Schema: reference/data-schema.md

STATEWIDE LEGAL CONTEXT — READ BEFORE ANY NEW YORK TRAVEL IS BOOKED:

⚠⚠ NEW YORK'S BITLICENSE (23 NYCRR Part 200, NY DFS) OUTRANKS EVERY CAMPUS POLICY IN
THIS FILE. It is carried in full in NYU's policy_key, labelled STATE REGULATORY note —
HIGHEST PRIORITY. Short version: s 200.3(a) "No Person shall, without a license obtained
from the superintendent as provided in this Part, engage in any Virtual Currency Business
Activity," and s 200.2(q)(5) puts "controlling, administering, or issuing a Virtual
Currency" inside that definition whenever the activity involves "New York or a New York
Resident." A student sign-up on a Manhattan quad is enough to trigger it. Neither s 200.3(c)
exemption reaches an issuer. Get counsel before collecting a single New York sign-up.

⚠ NEW YORK HAS NO CAMPUS FREE-SPEECH STATUTE. Unlike Oklahoma, Wisconsin, Arizona and
~20 other states, no SUNY/CUNY free-expression statute was enacted. SUNY's own 2021
legislative survey catalogues 17+ other states and discusses no New York bill
(https://system.suny.edu/sci/news/10-7-21-free-expression-legislation/index.html).
What exists is Article 129-A of the Education Law (the Henderson Act), which REQUIRES every
NY college, public and private, to adopt rules for the maintenance of public order — a
restriction mandate, not a speech grant. It is the statute used to eject people.
DO NOT LET AN AMBASSADOR CITE A NEW YORK CAMPUS FREE-SPEECH STATUTE.

SUNY AND CUNY ARE TWO SEPARATE SYSTEMS with separate Boards of Trustees. Do not conflate.
  SUNY (64 campuses; here: Stony Brook, Buffalo, Binghamton, Albany) — systemwide layer is
  Policy 5607 Commercial Use (eff. 3/28/2012, https://www.suny.edu/sunypp/documents.cfm?doc_id=704),
  Policy 5603 Use of Facilities by NON-Commercial Organizations (eff. 6/22/2020,
  https://www.suny.edu/sunypp/documents.cfm?doc_id=374 — the WRONG door for DGD), and the
  Rules for the Maintenance of Public Order, Doc 3653 (eff. 6/10/2009,
  https://www.suny.edu/sunypp/documents.cfm?doc_id=351). 5607 DEVOLVES the real rules to
  each campus, so SUNY does not resolve four campuses at a stroke. Full quotes in Stony
  Brook's policy_key.
  CUNY (25 campuses; here: Baruch, Hunter, City College) — systemwide layer is Policy 4.02
  Facilities Use (BOT 12/04/2017). It is the only NY systemwide document that NAMES
  commercial users as a category. Full quotes in Baruch's policy_key.

ALL TWELVE CAMPUSES ARE ON SEMESTERS. No quarter, trimester, block or quad school in this
set. ⚠ RIT IS THE TRAP — it used to be a quarter school and is now on semesters; anyone
planning from stale knowledge will be five weeks wrong on Rochester.
Start spread is 21 days: Binghamton Aug 18 → Columbia Sep 8.

⚠ THE MANHATTAN CLUSTER: NYU, Columbia, Baruch, Hunter and City College sit within subway
distance of each other — the densest concentration of target audience in the United States.
Columbia to City College is THREE STOPS on the 1 train. Baruch to Hunter is eight stops on
the 6. One ambassador can physically stand on all five in a single day. Nothing else in the
fifty-state tour comes close.
"""

STATE = 'New York'

CAMPUSES = [

 # ---------------------------------------------------------------- 1. NYU
 {'state': 'New York',
  'name': 'New York University',
  'city': 'New York, NY (Washington Square, Manhattan)',
  'type': 'Private',
  'tier': 'A — Named target',
  'access': 3,
  'start': 'Wed Sep 2, 2026 (Stern Langone evening/weekend classes begin Mon Sep 14). '
           'Labor Day holiday Mon Sep 7 — five days AFTER classes start.',
  'adddrop': '⚠ NOT PUBLISHED on the CAS calendar PDF; the Stern registration calendar defers to '
             'linked sub-pages. Gap — the term is already underway by the time of this packet.',
  'fallbreak': 'Fall Break Mon Oct 12, 2026. "Legislative Day" Wed Oct 14 — a Wednesday on which '
               'MONDAY classes meet; it is a scheduling artefact, NOT a break. Campus is at full '
               'density that day.',
  'thanksgiving': 'Thu–Fri Nov 26–27, 2026 (Stern shows Nov 25–29)',
  'lastclass': 'Mon Dec 14, 2026',
  'finals': 'Dec 16–22, 2026 (Stern day classes Dec 15–22). ⚠ LATEST-RUNNING TERM IN THE STATE '
            'after Columbia — NYU is still in session two days before Christmas Eve.',
  'cal_url': 'https://bulletins.nyu.edu/undergraduate/arts-science/academic-calendar/academic-calendar.pdf',
  'cal_status': 'CONFIRMED — CAS/undergraduate calendar PDF, cross-confirmed against the Stern Fall 2026 '
                'registration calendar (https://www.stern.nyu.edu/portal-partners/registrar/calendars-and-'
                'important-dates/registration-calendars/fall-2026-calendar). Second-latest start in New York.',
  'fair': 'Club Fest (Center for Student Life) — "some 300 NYU student organizations under one roof"',
  'fair_date': '⚠ UNVERIFIED — the Fall 2026 Club Fest page EXISTS at nyu.edu/life/events-traditions/clubfest/'
               'Fall-2026-club-fest.html but EVERY PAGE ON www.nyu.edu RETURNS HTTP 405 TO RESEARCH TOOLING '
               'and the date could not be read. Pattern, confirmed from the Fall 2025 instance: Tuesday '
               'Sep 9, 2025 at 1:00 PM, second week of September. With a Sep 2, 2026 start, expect the week '
               'of Sep 8–11, 2026. NYU Engage (engage.nyu.edu) is a JavaScript single-page app and returned '
               '"This application requires JavaScript to be enabled" with no event data. CALL TO CONFIRM.',
  'fair_outside': '⚠ NO PUBLISHED ANSWER — and assume no. Every description says "NYU student organizations." '
                  'No external-vendor tier appears anywhere. The one indexed NYU non-solicitation policy is an '
                  'EMPLOYMENT policy about soliciting employees, not a campus-access policy, so it neither '
                  'permits nor forbids tabling. Confirm by phone before travelling.',
  'fair_cost': 'Not published. No NYU vendor rate card of any kind could be located.',
  'fair_deadline': 'Not published.',
  'fair_url': 'https://www.nyu.edu/life/events-traditions/clubfest/Fall-2026-club-fest.html',
  'policy': '⚠ THE GOVERNING DOCUMENT COULD NOT BE RETRIEVED. Kimmel Center Policies is the operative '
            'document and it is unreadable. The only indexed policy is the Non-Solicitation Policy — '
            'New York, District of Columbia, Oklahoma, and California, which is an employment policy.',
  'policy_url': 'https://www.nyu.edu/life/campus-resources/kimmel-center/policies.html',
  'policy_key': "⚠⚠⚠ STATE REGULATORY note — HIGHEST PRIORITY — NEW YORK'S BITLICENSE, 23 NYCRR Part 200, "
                "administered by NY DFS. THIS OUTRANKS EVERY CAMPUS POLICY IN THIS PACKET AND MAY DETERMINE "
                "WHETHER NEW YORK IS VIABLE AT ALL. 23 NYCRR s 200.3(a): 'NO PERSON SHALL, WITHOUT A LICENSE "
                "OBTAINED FROM THE SUPERINTENDENT AS PROVIDED IN THIS PART, ENGAGE IN ANY VIRTUAL CURRENCY "
                "BUSINESS ACTIVITY.' s 200.2(q): 'Virtual Currency Business Activity means the conduct of any "
                "one of the following types of activities INVOLVING NEW YORK OR A NEW YORK RESIDENT:' (1) "
                "'receiving Virtual Currency for Transmission or Transmitting Virtual Currency, except where "
                "the transaction is undertaken for non-financial purposes and does not involve the transfer of "
                "more than a nominal amount'; (2) 'storing, holding, or maintaining custody or control of "
                "Virtual Currency on behalf of others'; (3) 'buying and selling Virtual Currency as a customer "
                "business'; (4) 'performing Exchange Services as a customer business'; (5) '⚠ CONTROLLING, "
                "ADMINISTERING, OR ISSUING A VIRTUAL CURRENCY.' Prong (5) is the one that bites DGD. There is "
                "NO small-volume, student, or promotional carve-out anywhere in Part 200 — the trigger is "
                "involvement of a single New York Resident. s 200.2(p): 'Virtual Currency means any type of "
                "digital unit that is used as a medium of exchange or a form of digitally stored value.' "
                "THE ONLY ARGUMENT WORTH PUTTING TO COUNSEL is the s 200.2(p)(2) affinity-program exclusion — "
                "digital units 'redeemable only for goods/services within customer affinity programs, NOT "
                "CONVERTIBLE TO FIAT OR VIRTUAL CURRENCY' — and it FAILS ON ITS OWN TERMS if the redeemed "
                "asset is convertible, which is the premise of the model. NEITHER EXEMPTION SAVES IT: "
                "s 200.3(c) exempts only (1) 'Persons that are chartered under the New York Banking Law and "
                "are approved by the superintendent' and (2) 'MERCHANTS AND CONSUMERS that utilize Virtual "
                "Currency SOLELY for the purchase or sale of goods or services or for investment purposes' — "
                "DGD is on the ISSUER side, not the merchant/consumer side. ⚠ THE AMBASSADOR CLAUSE: s 200.3 "
                "also provides 'Each Licensee is prohibited from conducting any Virtual Currency Business "
                "Activity THROUGH AN AGENT OR AGENCY ARRANGEMENT WHEN THE AGENT IS NOT A LICENSEE' — read that "
                "as a direct warning about campus ambassador and affiliate structures. MONEY: BitLicense "
                "application fee $5,000; S.8008C (signed 4/9/2022, eff. 6/8/2022) lets DFS assess licensees "
                "annually in amounts the Superintendent deems 'just and reasonable.' 'The development and "
                "dissemination of software in and of itself does not constitute Virtual Currency Business "
                "Activity' — not helpful here. OPERATIONAL READ: an INFORMATION-ONLY presence (literature, "
                "education, a club talk, NO wallet creation, NO credit issuance, NO referral accrual) is a "
                "materially different legal posture from a sign-up table and is THE ONLY POSTURE THAT SHOULD "
                "BE CONTEMPLATED before written clearance from New York counsel. Cites: "
                "law.cornell.edu/regulations/new-york/23-NYCRR-200.2 · .../23-NYCRR-200.3 · "
                "dfs.ny.gov/apps_and_licensing/virtual_currency_businesses (DFS publishes NO PHONE for the "
                "virtual currency unit and obfuscates its email). THIS IS RESEARCH, NOT LEGAL ADVICE. "
                "⚠ STATE note 2 — THERE IS NO NEW YORK CAMPUS FREE-SPEECH STATUTE. SUNY's own 2021 survey "
                "catalogues 17+ other states and discusses no New York bill "
                "(system.suny.edu/sci/news/10-7-21-free-expression-legislation/index.html). A2309 (2023) was "
                "introduced, not enacted. What exists is ARTICLE 129-A of the Education Law (the Henderson "
                "Act), which REQUIRES every NY college — public AND private — to adopt rules for the "
                "maintenance of public order. It is a RESTRICTION mandate and it is the statute used to eject "
                "people. DO NOT CITE A NEW YORK CAMPUS FREE-SPEECH STATUTE; THERE ISN'T ONE. "
                "=== NOW NYU ITSELF === ⚠ THE GOVERNING DOCUMENT COULD NOT BE RETRIEVED. EVERY PAGE ON "
                "www.nyu.edu RETURNS HTTP 405 to automated fetching, including the operative Kimmel Center "
                "Policies page (nyu.edu/life/campus-resources/kimmel-center/policies.html); the "
                "web.home.syr.nyu.edu mirror TIMES OUT on robots.txt. The ONLY NYU solicitation policy that is "
                "publicly indexed is the 'Non-Solicitation Policy — New York, District of Columbia, Oklahoma, "
                "and California' (revisions 2/13/2019, 7/17/2017, 4/1/2000) and IT IS AN EMPLOYMENT POLICY: "
                "'This Policy covers NYU employees and non-NYU employees.' 'NYU EMPLOYEES AND NON-NYU "
                "EMPLOYEES MAY NOT SOLICIT NYU EMPLOYEES, BY ANY MEANS, IN UNIVERSITY WORK AREAS DURING WORK "
                "TIME FOR ANY NON-WORK-RELATED PURPOSE.' 'Violation of this policy may result in disciplinary "
                "action.' Read literally that bars soliciting EMPLOYEES, not students, and it does not resolve "
                "tabling either way. ACCESS RATED 3 PROVISIONAL — rated 3 because the document is UNREADABLE, "
                "not because a route was found. DO NOT TREAT THIS 3 AS A FINDING. NYU is PRIVATE and owes no "
                "public-forum duty. ⚠ ONE GENUINELY DIFFERENT FACT: NYU's campus is interleaved with New York "
                "City public streets and Washington Square Park (NYC Parks jurisdiction) — the SIDEWALK "
                "outside an NYU building is not NYU's to control. Raise that with counsel separately; do not "
                "improvise it at a table.",
  'sponsor_required': 'UNKNOWN — the Kimmel Center policy that would answer this returns HTTP 405. Assume yes '
                      'and confirm by phone.',
  'clubs': [
    ('⚠ NYU Blockchain & Fintech (BNF)',
     'Active. Ran the INAUGURAL NYU Blockchain Conference (Nov 1) jointly with NYU Blockchain Society. '
     'Linktree/Instagram-fronted; no institutional email published. A student-run conference is a PRIVATE '
     'event with its own sponsorship pipeline and engages NONE of NYU\'s tabling rules — this is the door.',
     'https://www.nyubnf.com/'),
    ('NYU Blockchain Society',
     'Active. Co-host of the NYU Blockchain Conference. An ALUMNI special-interest club of the same name also '
     'exists at nyu.edu/alumni/get-involved/alumni-clubs/special-interest-clubs/nyu-blockchain-society.html — '
     'do not confuse the two.',
     'https://www.nyublockchain.com/'),
    ('NYU Stern Blockchain & Fintech',
     'Listed as an affiliated student group of the NYU Blockchain Lab. Status otherwise unconfirmed.',
     'https://blockchain.stern.nyu.edu/'),
    ('NYU Tandon student organizations (40+)',
     '⚠ DIRECTORY NOT ENUMERABLE — the landing page lists no club names and NYU Engage is JavaScript-rendered. '
     'Tandon (Brooklyn) is the engineering campus and the likeliest home of a technical crypto club.',
     'https://engineering.nyu.edu/life-tandon/student-life/student-organizations'),
  ],
  'faculty': [
    ('⚠ David L. Yermack',
     'Albert Fingerhut Professor of Finance and Business Transformation, NYU Stern — THE most prominent crypto '
     'academic in New York and the founder of Stern\'s cryptocurrency curriculum. Teaches "Bitcoin and '
     'Cryptocurrencies" and co-teaches the digital-currency course with NYU Law. At Stern since 1994. '
     'Kaufman Management Center, 44 West Fourth St, room 9-70. ⚠ NO PHONE PUBLISHED on the faculty bio.',
     'Finance, NYU Stern',
     'dy1@stern.nyu.edu · no phone published',
     'https://www.stern.nyu.edu/faculty/bio/david-yermack'),
    ('Hanna Halaburda',
     'NYU Stern; leading professor associated with the NYU BLOCKCHAIN LAB — "a research lab committed to '
     'pushing our frontier of knowledge in the blockchain and Web 3.0 space." The Lab runs research talks on '
     'stablecoins, MEV, DeFi and CBDCs and co-hosts the CBER Conference. ⚠ The Lab site publishes NO email and '
     'NO phone — it says only "If you are interested in chatting, please feel free to reach out."',
     'NYU Stern / NYU Blockchain Lab',
     'no email or phone published — contact via the Lab site',
     'https://blockchain.stern.nyu.edu/'),
    ('Geoffrey Miller and Max Raskin',
     'NYU School of Law; co-teach FINC-GB.3324 / LAW-LW.12371 "Digital Currency, Blockchains, and the Future '
     'of the Financial Services Industry" with Yermack. ⚠ That course is SPRING, not Fall.',
     'NYU School of Law',
     'no phone published — look up in the law faculty directory',
     'https://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.overview&personid=20547'),
    ('⚠ NYU Tandon Student Life / Engagement',
     'THE ONLY WORKING NYU OFFICE NUMBER confirmable on a live, fetchable page — every www.nyu.edu page 405s. '
     'Call this and ask for a transfer to the Center for Student Life on Kimmel 7.',
     'NYU Tandon, Brooklyn',
     'engagement.tandonstudentlife@nyu.edu · (646) 997-3600',
     'https://engineering.nyu.edu/life-tandon/student-life/student-organizations'),
    ('Center for Student Life',
     'Runs "over 300 student-run clubs & organizations" and owns Club Fest. Located Kimmel Center for '
     'University Life, 7TH FLOOR, 60 Washington Square South (location confirmed via meet.nyu.edu). '
     '⚠ NO NUMBER PUBLISHED THAT COULD BE CONFIRMED — the CSL organization-directory page returns HTTP 405. '
     'Look up here, or route through Tandon on (646) 997-3600.',
     'NYU Student Affairs',
     'no number published — look up here',
     'https://www.nyu.edu/about/leadership-university-administration/organization-directory/center-for-student-life.html'),
  ],
  'courses': [
    ('FINC-GB.3324 / LAW-LW.12371',
     '"Digital Currency, Blockchains, and the Future of the Financial Services Industry" (Miller, Raskin & '
     'Yermack). ⚠⚠ SPRING TERM, NOT FALL — the confirmed syllabus is Spring 2026, Mon & Wed 10:30–11:50 AM, '
     'KMC 1-70. A joint Stern/Law offering. Do NOT plan a Fall visit around this course.',
     'https://pages.stern.nyu.edu/~dyermack/courses/Miller%20Raskin%20Yermack%20-%20Spring%202026.pdf'),
    ('Bitcoin and Cryptocurrencies',
     'Yermack, NYU Stern. Listed on his faculty bio. ⚠ TERM NOT CONFIRMED — no Fall 2026 section verified.',
     'https://www.stern.nyu.edu/faculty/bio/david-yermack'),
    ('Stern executive-education digital currency course',
     'Yermack with Assistant Dean Roy Lee. Professional education, not undergraduate catalog — a paying '
     'audience of practitioners rather than students.',
     'https://www.stern.nyu.edu/experience-stern/news/professor-david-yermack-and-assistant-dean-roy-lee-are-interviewed-about-stern-s-new-executive'),
  ],
  'events': [
    ('⚠ NYU Blockchain Conference',
     'Student-run, inaugural edition Nov 1, co-run by NYU Blockchain & Fintech and NYU Blockchain Society. '
     'A STUDENT-RUN CONFERENCE IS A PRIVATE EVENT WITH ITS OWN SPONSORSHIP PIPELINE AND SIDESTEPS NYU\'S '
     'TABLING RULES ENTIRELY. This is the single best door at NYU and it does not require solving the 405 '
     'problem. Fall 2026 edition unconfirmed — ask the clubs directly.',
     'https://x.com/nyubnf/status/1850307801119170954'),
    ('NYU Blockchain Lab research talks',
     'Recurring seminar series on stablecoins, MEV, DeFi protocols and CBDCs, featuring faculty and external '
     'researchers. Co-hosts the multi-university CBER Conference.',
     'https://blockchain.stern.nyu.edu/'),
    ('Club Fest, Fall 2026',
     '⚠ Date UNVERIFIED (page 405s). Pattern: second week of September, ~300 orgs. Expect Sep 8–11, 2026.',
     'https://www.nyu.edu/life/events-traditions/clubfest/Fall-2026-club-fest.html'),
  ],
  'play': 'DO NOT SET FOOT ON THIS CAMPUS — OR ANY NEW YORK CAMPUS — UNTIL COUNSEL HAS CLEARED 23 NYCRR '
          's 200.2(q)(5) IN WRITING. NYU carries the state\'s BitLicense note because it is the anchor campus, '
          'and that question determines whether New York is viable at all. Assuming it clears: NYU is a '
          'documentation blackout — every page on www.nyu.edu returns HTTP 405 and the Kimmel tabling policy '
          'cannot be read, so the access 3 is provisional and means nothing. THE SINGLE BEST DOOR IS THE '
          'STUDENT-RUN NYU BLOCKCHAIN CONFERENCE, co-run by NYU Blockchain & Fintech and NYU Blockchain '
          'Society. It is a private event with its own sponsorship pipeline; it engages no NYU facility '
          'policy; and it reaches exactly the audience DGD wants without anyone having to interpret an '
          'unreadable page. Approach the clubs, not the university. The second door is David Yermack — the '
          'most prominent crypto academic in New York, who has built Stern\'s entire cryptocurrency '
          'curriculum and has an obvious professional interest in the space; email dy1@stern.nyu.edu. Note '
          'his flagship course runs in SPRING, so a Fall classroom slot is not available. For the '
          'institutional route, the only NYU number that works is Tandon\'s (646) 997-3600 — call it, ask for '
          'a transfer to the Center for Student Life on Kimmel 7, and get three things: the Fall 2026 Club '
          'Fest date, whether outside organisations may table, and the Kimmel tabling rate. NYU starts Sep 2 '
          'and runs to Dec 22, the longest tail in the state, so the visit window is late but generous. '
          'Finally: NYU has no walls. The sidewalks and Washington Square Park around it are New York City '
          'jurisdiction, not NYU\'s — a genuinely different fact pattern worth raising with counsel, and one '
          'no ambassador should improvise at street level.',
  'gaps': [
    '⚠⚠ BLOCKING — the BitLicense question. Does DGD\'s issuance of USD credit redeemable for a digital asset, '
    'with referral accrual, constitute "controlling, administering, or issuing a Virtual Currency" under '
    '23 NYCRR s 200.2(q)(5)? Does the s 200.2(p)(2) affinity-program exclusion save it if the redeemed asset '
    'is convertible? NEW YORK COUNSEL, NOT A PHONE CALL. App fee $5,000 if a licence is required.',
    '⚠⚠ BLOCKING — s 200.3 bars a licensee from operating "through an agent or agency arrangement when the '
    'agent is not a Licensee." Get counsel\'s read on whether a campus ambassador is an agent.',
    '⚠ EVERY PAGE ON www.nyu.edu RETURNS HTTP 405 to automated fetching. Unreadable: the Kimmel Center '
    'policies (the operative tabling document), the Center for Student Life directory, and the Fall 2026 Club '
    'Fest page. A human with a browser sees all three instantly — https://www.nyu.edu/life/campus-resources/'
    'kimmel-center/policies.html',
    '⚠ Fall 2026 Club Fest date, time, location and whether outside organisations may table — all unknown. '
    'Start at Tandon (646) 997-3600.',
    '⚠ No Center for Student Life phone number could be confirmed anywhere.',
    'Add/drop deadline not published on the CAS calendar PDF.',
    'Kimmel Center tabling rate card — does one exist at all? Not indexed anywhere.',
    'NYU Engage (engage.nyu.edu) is a JavaScript single-page app — the org directory cannot be read; club '
    'rosters and contacts are unavailable to tooling.',
    'Fall 2026 edition of the NYU Blockchain Conference — date and sponsorship tiers unconfirmed. Ask BNF.',
  ],
  },

 # ---------------------------------------------------------------- 2. Columbia
 {'state': 'New York',
  'name': 'Columbia University',
  'city': 'New York, NY (Morningside Heights, Manhattan)',
  'type': 'Private',
  'tier': 'A — Named target',
  'access': 2,
  'start': '⚠ Tue Sep 8, 2026 — LATEST START IN THE STATE, three weeks after Binghamton. '
           'The registrar phrases it "Classes begin for the 273rd academic year."',
  'adddrop': 'Change of Program (add/drop) ends Fri Sep 18, 2026. A "Post Change of Program Add/Drop" '
             'period then runs through Tue Oct 13.',
  'fallbreak': '⚠ NONE. Columbia has NO October fall break. The only autumn holiday is ELECTION DAY, '
               'Tue Nov 3, 2026 (University holiday). Columbia runs at FULL DENSITY from Sep 8 straight '
               'through Nov 24 — the best sustained access window in New York, it just opens very late.',
  'thanksgiving': 'Thu–Fri Nov 26–27, 2026 (University holidays)',
  'lastclass': 'Mon Dec 14, 2026. Study days Tue–Wed Dec 15–16.',
  'finals': 'Thu Dec 17 – Wed Dec 23, 2026. ⚠ The longest tail in the state — Columbia is still examining '
            'the day before Christmas Eve.',
  'cal_url': 'https://bulletin.columbia.edu/columbia-college/academic-calendar/academic-calendar.pdf',
  'cal_status': 'CONFIRMED — Columbia College academic calendar PDF, every date carrying an explicit weekday '
                'in the source ("September 8 Tuesday", "December 14 Monday").',
  'fair': 'Activities Day (Columbia Club Fair) — "300+ of Columbia\'s undergraduate-wide student groups '
          'and organizations"',
  'fair_date': '⚠ UNVERIFIED for Fall 2026. Recurring pattern CONFIRMED from the Fall 2025 instance: '
               'Friday Sep 5, 2025, 12:00–4:00 PM, on LOW PLAZA (535 W. 116th St), plus Butler Plaza and '
               'College Walk. That page is now flagged "Past Event." With a Tuesday Sep 8, 2026 start, the '
               'pattern (Friday of week one) points to FRI SEP 11, 2026 — INFERRED, NOT CONFIRMED. '
               '⚠ The Columbia College events mirror (college.columbia.edu/events/event/activities-day-2) '
               'RETURNS HTTP 403 to research tooling. Confirm with GS Student Life.',
  'fair_outside': '⚠ NOT ADDRESSED — and the realistic answer is no. Every description is of Columbia\'s own '
                  'undergraduate student groups. Separately, the University Event Policy names a mandatory '
                  'sponsor office for nonprofit, civic, political and governmental non-affiliates and names '
                  'NO OFFICE AT ALL for a commercial one. That silence is not permission.',
  'fair_cost': 'Not published.',
  'fair_deadline': 'Not published.',
  'fair_url': 'https://www.gs.columbia.edu/events/activities-day-columbia-club-fair',
  'policy': 'University Event Policy (primary); plus Use of University Name, Facilities and Equipment '
            '(eff. 1/1/1993, rev. 5/12/2017) and the Columbia Housing Commercial Activities policy',
  'policy_url': 'https://universitypolicies.columbia.edu/content/university-event-policy',
  'policy_key': "UNIVERSITY EVENT POLICY (universitypolicies.columbia.edu/content/university-event-policy) — "
                "scope covers 'University departments, offices, groups, and student organizations AND "
                "NON-AFFILIATES requesting to reserve campus facilities.' Operative: '⚠ ALL EVENTS REQUIRE A "
                "RESERVATION AND ADVANCE APPROVAL.' Special events generally need 'TEN WORKING DAYS ADVANCE "
                "NOTICE,' exceptions case-by-case. ⚠ SPONSORSHIP IS MANDATORY FOR NON-AFFILIATES, AND THE "
                "SPONSOR CHANNEL IS PRESCRIBED BY CATEGORY: 'NONPROFIT COMMUNITY ORGANIZATIONS, PUBLIC AND "
                "CIVIC ORGANIZATIONS, POLITICAL ORGANIZATIONS, AND GOVERNMENTAL ORGANIZATIONS MUST USE THE "
                "UNIVERSITY'S OFFICE OF GOVERNMENT RELATIONS AND COMMUNITY AFFAIRS AS THEIR CAMPUS CONTACT AND "
                "SPONSOR.' ⚠⚠ READ THE GAP: THE POLICY NAMES A MANDATORY SPONSOR OFFICE FOR EVERY CATEGORY OF "
                "NON-AFFILIATE EXCEPT A FOR-PROFIT COMMERCIAL ENTITY, FOR WHICH IT NAMES NONE. That silence is "
                "not permission — ask Event Management on (212) 853-1479 which office sponsors a commercial "
                "third party and expect the answer 'none.' Columbia also reserves: it may 'regulate the time, "
                "place and manner' and '⚠ LIMIT ANY EVENT TO UNIVERSITY ID HOLDERS.' ⚠ THE DISCLAIMER "
                "REQUIREMENT — Columbia's closest thing to an anti-fronting rule: non-affiliates must include "
                "on ALL materials, in comparable font size, 'THIS EVENT IS NOT AFFILIATED WITH, ENDORSED BY, "
                "OR SPONSORED BY COLUMBIA UNIVERSITY.' Student organisations must follow the student event "
                "approval process and have 'a faculty or other academic sponsor' for special events. "
                "USE OF UNIVERSITY NAME, FACILITIES AND EQUIPMENT (eff. Jan 1 1993, last revised May 12 2017; "
                "Responsible Office: HUMAN RESOURCES — universitypolicies.columbia.edu/content/"
                "use-university-name-facilities-and-equipment): 'UNDER NO CIRCUMSTANCES SHALL AN EMPLOYEE USE "
                "UNIVERSITY PROPERTY AND RESOURCES INCLUDING BUT NOT LIMITED TO THE UNIVERSITY NAME, ITS "
                "OFFICES, ITS FACILITIES, LOCAL MAIL SERVICE AND TELEPHONES, TO SOLICIT IN ANY MANNER WITHOUT "
                "THE PRIOR PERMISSION OF THE VICE PRESIDENT, HUMAN RESOURCES.' And, decisively for a "
                "third party: '⚠ INDIVIDUALS WHO ARE NOT EMPLOYEES CANNOT DISTRIBUTE MATERIALS OR SOLICIT "
                "STAFF ON CAMPUS PROPERTY AT ANY TIME.' Staff are separately barred from distributing "
                "'religious, charitable, COMMERCIAL, or other solicitations' in work areas. "
                "COMMERCIAL ACTIVITIES — HOUSING (housing.columbia.edu/content/commercial-activities): "
                "'NO COMMERCIAL ACTIVITIES MAY BE CONDUCTED IN OR FROM ANY OF THE RESIDENCE HALLS OR "
                "BROWNSTONES, including but not limited to in or from any student bedrooms, suite rooms or "
                "common areas' — explicitly naming 'running a business and solicitation, including soliciting "
                "in-person, door-to-door, by voicemail, email, US Mail, etc.' So the dorm-based student "
                "ambassador model is barred in terms. COLUMBIA IS PRIVATE — no public-forum obligation, and "
                "New York has no campus free-speech statute to fall back on. NO FEE SCHEDULE, INSURANCE LIMIT "
                "OR DEPOSIT TERM IS PUBLISHED anywhere in the retrieved policies.",
  'sponsor_required': '⚠ YES — MANDATORY. Non-affiliates must have a University department sponsor. But the '
                      'policy prescribes a sponsor office ONLY for nonprofit, civic, political and '
                      'governmental groups; for a commercial entity it names none, which in practice means '
                      'there is no sponsor to find. Confirm on (212) 853-1479.',
  'clubs': [
    ('Blockchain @ Columbia',
     'Listed as a student club by Columbia Entrepreneurship. Undergraduate-facing. Status current as of the '
     'Entrepreneurship directory; no officer contact published (rosters rotate — do not guess).',
     'https://entrepreneurship.columbia.edu/resources/blockchain-columbia-student-club/'),
    ('⚠ Columbia Blockchain Alliance',
     '⚠ SITE IS LIVE BUT RETURNED NO RENDERED CONTENT to research tooling — only a viewport meta tag. '
     'Status genuinely UNCONFIRMED in either direction. Check in a browser before relying on it.',
     'https://columbiablockchainalliance.com/'),
    ('Columbia FinTech and Blockchain Club (CBS, graduate)',
     'Active — Columbia Business School admissions runs recruiting sessions titled "The CBS Experience: '
     'Student Chat with FinTech and Blockchain Club," which means the school itself treats it as a live, '
     'front-of-house organisation. MBA audience: older, better capitalised, professionally motivated.',
     'https://groups.gsb.columbia.edu/fintech/home'),
  ],
  'faculty': [
    ('⚠ Assistant Vice President, Event Management',
     'THE OFFICE THAT GRANTS OR REFUSES PERMISSION FOR EVERY EVENT ON CAMPUS, and the contact printed on the '
     'University Event Policy itself. This is the single most valuable number at Columbia. Ask them directly '
     'which office sponsors a commercial non-affiliate, since the policy names one for every other category.',
     'Columbia Event Management',
     'sm4534@columbia.edu · (212) 853-1479',
     'https://universitypolicies.columbia.edu/content/university-event-policy'),
    ('⚠ Omid Malekan',
     'Adjunct Assistant Professor of Business, Finance Division, Columbia Business School. AN EIGHT-YEAR '
     'CRYPTOCURRENCY INDUSTRY VETERAN, not a pure academic — author of "Re-Architecting Trust" and "The Story '
     'of the Blockchain," quoted in the NYT, WSJ and FT. Teaches B7462 and B8462 "Blockchain & '
     'Cryptocurrencies," and B8462 RUNS IN FALL 2026 WITH INDUSTRY GUEST SPEAKERS BUILT INTO THE SYLLABUS. '
     'Office 570 Kravis. ⚠ His email is OBFUSCATED on the CBS profile page (renders as a placeholder) and no '
     'phone is published.',
     'Finance Division, Columbia Business School',
     'email obfuscated on the page · no phone published',
     'https://business.columbia.edu/faculty/people/omid-malekan'),
    ('Gur Huberman',
     'Finance, Columbia Business School; co-instructor of B8462 "Blockchain & Cryptocurrencies" with Malekan. '
     'The senior academic name on the course.',
     'Finance Division, Columbia Business School',
     'no phone published — look up in the CBS faculty directory',
     'https://courses.business.columbia.edu/B8462'),
    ('Office of Government Relations and Community Affairs',
     'Named in the University Event Policy as the MANDATORY campus contact and sponsor for nonprofit, civic, '
     'political and governmental non-affiliates. Not the right door for DGD, but Event Management will send '
     'you here first, so know the name. ⚠ No number captured.',
     'Columbia University',
     'no number published — look up here',
     'https://universitypolicies.columbia.edu/content/university-event-policy'),
    ('HR Compliance',
     'Owns the Use of University Name, Facilities and Equipment policy — the one containing "individuals who '
     'are not employees cannot distribute materials or solicit staff on campus property at any time." '
     '⚠ Email only, no phone published.',
     'Columbia Human Resources',
     'no phone published — look up here',
     'https://universitypolicies.columbia.edu/content/use-university-name-facilities-and-equipment'),
  ],
  'courses': [
    ('B8462',
     '"Blockchain & Cryptocurrencies" — MBA elective, Finance Division; Gur Huberman and Omid Malekan. '
     '⚠⚠ CONFIRMED RUNNING FALL 2026: Sep 8 – Dec 11, 2026, THURSDAYS 9:00 AM–12:15 PM, KRAVIS 840. Covers '
     'cryptography and distributed systems foundations, Bitcoin history, consensus models, ICOs and smart '
     'contracts — AND GUEST SPEAKERS FROM INDUSTRY ARE BUILT INTO THE SYLLABUS. Prerequisite B8306 Capital '
     'Markets & Investments. THIS IS THE ONLY COURSE IN THE ENTIRE NEW YORK PACKET CONFIRMED TO RUN IN FALL '
     '2026, and its guest slot is the lowest-friction, highest-quality room in the state.',
     'https://courses.business.columbia.edu/B8462'),
    ('B7462',
     '"Blockchain & Cryptocurrencies" — Malekan. The companion section listed on his faculty bio. Term not '
     'separately confirmed.',
     'https://business.columbia.edu/faculty/people/omid-malekan'),
    ('B8210',
     '"Regulatory and Legal Matters on Blockchain, Cryptocurrencies and Digital Assets." ⚠ TERM NOT '
     'CONFIRMED. Given the BitLicense problem, this is the course whose students already understand exactly '
     'why New York is hard.',
     'https://courses.business.columbia.edu/B8210'),
  ],
  'events': [
    ('⚠ B8462 industry guest-speaker slot, Thursdays 9:00 AM, Kravis 840, Sep 8 – Dec 11 2026',
     'THE BEST-DOCUMENTED DOOR IN NEW YORK. It is a classroom, not a tabling permit — it engages NO facility '
     'policy, requires NO sponsor, costs nothing, and the instructor is an industry veteran who books outside '
     'speakers as a matter of routine. Fourteen Thursday mornings of confirmed access to an MBA finance '
     'audience. Approach Malekan.',
     'https://courses.business.columbia.edu/B8462'),
    ('Columbia FinTech and Blockchain Club event stream (CBS)',
     'Standing event feed for the graduate fintech/blockchain club. Dates roll; check the feed for Fall 2026.',
     'https://events.business.columbia.edu/taxonomy/term/72'),
    ('Columbia Business School Cryptocurrency topic hub',
     'CBS maintains a standing editorial hub on cryptocurrency — evidence the school is comfortable being '
     'publicly associated with the subject, which matters for the mission-alignment screen.',
     'https://business.columbia.edu/insights/topics/cryptocurrency'),
  ],
  'play': 'FORGET TABLING AT COLUMBIA AND GO STRAIGHT TO THE CLASSROOM. The University Event Policy requires '
          'every non-affiliate to have a University department sponsor, prescribes a mandatory sponsor office '
          'for nonprofit, civic, political and governmental groups, and names NO OFFICE AT ALL for a '
          'commercial entity — which in practice means there is no sponsor for DGD to find, and Columbia can '
          'additionally limit any event to ID holders. THE SINGLE BEST DOOR IS B8462 "Blockchain & '
          'Cryptocurrencies," confirmed running Fall 2026 on Thursdays 9:00 AM–12:15 PM in Kravis 840 from '
          'Sep 8 to Dec 11, co-taught by Omid Malekan — an eight-year crypto industry veteran, not a career '
          'academic — with INDUSTRY GUEST SPEAKERS ALREADY BUILT INTO THE SYLLABUS. That is fourteen '
          'confirmed Thursday mornings in front of an MBA finance audience, costing nothing, requiring no '
          'permit, and engaging no facility policy whatsoever. It is the best-documented access route in the '
          'state. Approach Malekan (his email is obfuscated on the CBS page — go through the Business School '
          'faculty office or the Columbia FinTech and Blockchain Club, which CBS admissions itself puts '
          'front-of-house). Second door: Blockchain @ Columbia on the undergraduate side. Only if you must go '
          'institutional, call Event Management on (212) 853-1479 — the most useful question is not "may we '
          'table" but "which office sponsors a commercial non-affiliate," and the answer will tell you '
          'everything. Timing: Columbia starts Sep 8, the latest in New York, but has NO October break — only '
          'Election Day, Nov 3 — so it runs at full density Sep 8 to Nov 24. Activities Day is probably Fri '
          'Sep 11, 2026 (inferred from the Sep 5, 2025 pattern; the College mirror 403s), and City College is '
          'three stops away on the 1 train.',
  'gaps': [
    '⚠ Which office, if any, sponsors a FOR-PROFIT commercial non-affiliate? The Event Policy names one for '
    'every other category and none for this one. Call (212) 853-1479.',
    '⚠ Activities Day Fall 2026 date — inferred as Fri Sep 11, 2026 from the confirmed Sep 5, 2025 instance. '
    'Confirm with GS Student Life.',
    '⚠ The Columbia College Activities Day page returns HTTP 403 to research tooling — '
    'https://www.college.columbia.edu/events/event/activities-day-2',
    '⚠ Columbia Blockchain Alliance returned NO rendered content (viewport meta only). Active or defunct is '
    'genuinely unknown — https://columbiablockchainalliance.com/',
    'No fee schedule, insurance limit, security cost or deposit term is published in ANY retrieved Columbia '
    'policy. If an institutional route is ever pursued, all of it must come by phone.',
    'Omid Malekan\'s email is obfuscated on his CBS profile and no phone is published for him or Huberman.',
    'No phone number for the Office of Government Relations and Community Affairs (the named sponsor office).',
    'B8210 term of offering not confirmed.',
  ],
  },

 # ---------------------------------------------------------------- 3. Baruch (CUNY)
 {'state': 'New York',
  'name': 'CUNY Baruch College',
  'city': 'New York, NY (25th & Lexington, Manhattan)',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 2,
  'start': 'Fri Aug 28, 2026 — CUNY COMMON CALENDAR (identical at Hunter and City College; one date '
           'covers all three Manhattan CUNYs).',
  'adddrop': 'Last day to add a course / drop for 75% refund Thu Sep 3, 2026. Last day to drop without a '
             '"W" Fri Sep 4, 2026.',
  'fallbreak': '⚠⚠ THE SEPTEMBER NO-CLASS CLUSTER IS THE MOST IMPORTANT CALENDAR FACT IN NEW YORK. '
               'CUNY loses Mon Sep 7 (Labor Day), Fri–Sun Sep 11–13 (Rosh Hashanah) AND Mon Sep 21 '
               '(Yom Kippur). September at CUNY is Swiss cheese. THE CLEAN WINDOWS ARE Aug 31 – Sep 4 AND '
               'EVERYTHING FROM SEP 22 ONWARD. A tour planner who books mid-September in Manhattan CUNY '
               'will find empty buildings.',
  'thanksgiving': 'College CLOSED Thu–Fri Nov 26–27, 2026; no classes Wed Nov 25 and Sat Nov 28.',
  'lastclass': 'Fall term ends Mon Dec 21, 2026 (seven-week sessions end Dec 20).',
  'finals': 'Tue Dec 15 – Mon Dec 21, 2026',
  'cal_url': 'https://enrollmentmanagement.baruch.cuny.edu/registrar/academic-calendar/',
  'cal_status': 'CONFIRMED — Baruch registrar, cross-confirmed against the CUNY central 2026-27 calendar at '
                'https://our.catalog.cuny.edu/pages/6v5vCLMZ3vBKXnNNscUh which shows the identical common '
                'calendar for CUNY senior colleges.',
  'fair': '⚠ NO NAMED BARUCH INVOLVEMENT FAIR COULD BE LOCATED. Club activity concentrates in CLUB HOURS '
          'rather than a single annual fair.',
  'fair_date': '⚠⚠ THE SINGLE MOST ACTIONABLE SCHEDULING FACT AT BARUCH — CLUB HOURS: "Most undergraduate '
               'clubs meet on THURSDAYS, 12:40 to 2:20 PM (Club Hours)." Graduate clubs meet Fridays 6–9 PM. '
               'That is a recurring, guaranteed, twice-weekly concentration of every club on campus, and it '
               'beats any one-day fair. Tabling in the 2nd Floor Lobby of the Newman Vertical Campus is a '
               'STANDING facility, not an annual event. No Fall 2026 fair date is published — call '
               '(646) 312-4550 and ask directly.',
  'fair_outside': '⚠ NO — and the binding number is 15%. The student-org handbook: "ONLY 15% OF EVENT '
                  'PARTICIPANTS MAY BE OUTSIDE GUESTS. ALUMNI ARE CONSIDERED OUTSIDE GUESTS." A DGD-heavy '
                  'event breaches that on its face. Exceptions exist for ticketed shows and case-by-case '
                  'through the Office of Student Life.',
  'fair_cost': 'Not published. No Baruch external-vendor rate card exists. The only formal door for DGD as an '
               'entity is CUNY Policy 4.02 category 6 ("All other users, including commercial users"), which '
               'colleges MAY permit and are never required to.',
  'fair_deadline': 'Fundraiser Request Form 3 weeks ahead; off-campus events 8 weeks; contracts 2 weeks '
                   'before a CUNYBuy PO request that is itself due 6–8 weeks before the event.',
  'fair_url': 'https://studentaffairs.baruch.cuny.edu/studentlife/student-activities/student-clubs-organizations/',
  'policy': 'The Informer 2025-2026 (Baruch student-organization handbook) — the operative document; above it '
            'sits CUNY Policy 4.02 Facilities Use (BOT 12/04/2017)',
  'policy_url': 'https://studentaffairs.baruch.cuny.edu/wp-content/uploads/sites/6/2025/08/The-Informer-2025-2026.pdf',
  'policy_key': "⚠ CUNY SYSTEMWIDE LAYER — POLICY 4.02 FACILITIES USE, approved by the CUNY Board of Trustees "
                "December 4, 2017 (amending 2/28/2005), policy.cuny.edu/wp-content/uploads/sites/6/page-assets/"
                "general-policy/Policy-4.02-Facilities-Use-approved-by-BOT-120417.pdf. REPORTED ONCE HERE FOR "
                "ALL THREE CUNY CAMPUSES IN THIS PACKET (Baruch, Hunter, City College) — CUNY AND SUNY ARE "
                "SEPARATE SYSTEMS WITH SEPARATE BOARDS; DO NOT CONFLATE THEM. 4.02 is the only NY systemwide "
                "document that NAMES commercial users. Six priority categories: '(1) Host college "
                "departments... (2) Users affiliated with the host college... (3) Other CUNY colleges... "
                "(4) Government agencies and non-profit organizations... (5) Union organizations... "
                "(6) ALL OTHER USERS, INCLUDING COMMERCIAL USERS.' THE OPERATIVE DISCRETION CLAUSE: 'COLLEGES "
                "SHALL PERMIT USE UNDER CATEGORIES 1 THROUGH 5 AND MAY PERMIT USE UNDER CATEGORY 6' — "
                "commercial use is DISCRETIONARY, never mandatory, at every CUNY campus. Fees: 'Fair market "
                "value must be charged for partisan political use'; commercial users are charged direct costs "
                "at standard rates; affiliated users pay no Use Fee. Insurance: non-affiliated users must "
                "'provide evidence of appropriate and adequate insurance protection.' ⚠ SPONSORSHIP IS "
                "CONTEMPLATED, NOT FORBIDDEN — CUNY HAS NO SYSTEMWIDE ANTI-FRONTING RULE: 'if an affiliated "
                "user co-sponsors with outside organizations, the host college may charge a Use Fee... "
                "APPORTIONED TO THE OUTSIDE ORGANIZATION(S).' CUNY INSURANCE DOLLAR TIERS, from John Jay's "
                "Best Practices for Use of Campus Facilities by Student Organizations (July 2024): low-risk "
                "'$500,000 may be sufficient'; standard lectures/dance/music '$1,000,000 (one million "
                "dollars) per occurrence and $2,000,000 (two million dollars) aggregate is usually adequate'; "
                "high-risk outdoor '$2,000,000... to $5,000,000... range may be appropriate.' Broker named in "
                "that document: 'InterCity Agency, Inc. (718-279-7705).' That same document states plainly it "
                "is 'NOT intended to address facility use by external groups, such as community groups, "
                "not-for-profit organizations, and COMMERCIAL ENTITIES' — so it governs the CLUB, not DGD. "
                "⚠ TWO CUNY SYSTEMWIDE DOCUMENTS ARE ROBOTS-BLOCKED to research tooling and a human should "
                "read them before any CUNY commitment: the primary Facility Use Policy PDF at cuny.edu/"
                "wp-content/.../Facility-Use-Policy.pdf, and CUNY Bylaws Article XV at "
                "policy.cuny.edu/bylaws/article-xv/. === NOW BARUCH ITSELF — THE INFORMER 2025-2026, the "
                "richest single policy document in the New York packet === TABLING, VERBATIM: 'YOUR "
                "ORGANIZATION MAY RESERVE A TABLE IN THE 2ND FLOOR LOBBY OF THE NEWMAN VERTICAL CAMPUS for "
                "promotional activities such as the distribution of literature, recruitment drives, ticket "
                "sales, etc.' Amplified sound only on Thursdays during club hours via Bluetooth speakers; "
                "microphones and bullhorns prohibited. ⚠⚠ THE PAYMENT-CREDENTIAL CLAUSE — THE MOST DIRECTLY "
                "RELEVANT SENTENCE FOUND ANYWHERE IN FIFTY STATES: 'STUDENTS ARE NOT PERMITTED TO UTILIZE "
                "ONLINE TICKETING SYSTEMS OR MONEY TRANSFER SERVICES WHEN SELLING TICKETS. PROHIBITED SERVICES "
                "INCLUDE, BUT ARE NOT LIMITED TO, EVENTBRITE, VENMO, ZELLE, CASHAPP, CHIME, AND OTHER "
                "ELECTRONIC SOURCES OF CROWDFUNDING OR ONLINE MONEY DONATION PLATFORMS.' It is written about "
                "ticket sales, but the operative words are 'MONEY TRANSFER SERVICES' and 'OTHER ELECTRONIC "
                "SOURCES' — a wallet-funding or credit-purchase flow run at a Baruch table sits squarely "
                "inside the mischief. RAISE IT BEFORE, NOT AFTER. ⚠ THE OUTSIDE-GUEST CAP: 'ONLY 15% OF EVENT "
                "PARTICIPANTS MAY BE OUTSIDE GUESTS. ALUMNI ARE CONSIDERED OUTSIDE GUESTS.' ⚠ CONTRACTS — "
                "NOBODY SIGNS ANYTHING AT A TABLE: 'All expenditures for personnel services (speakers, "
                "musicians, DJs, performers, etc.) require a written contract'; STUDENTS MUST NEVER SIGN "
                "CONTRACTS — all agreements route through Student Life Advisors via MyBaruch; 'CONTRACTS ARE "
                "ALWAYS SIGNED BY THE VENDOR OR PERFORMER FIRST AND THEN BY BARUCH, NEVER THE OTHER WAY "
                "AROUND'; contracts submitted after performance WILL NOT BE HONORED; honorarium cap $2,000. "
                "CORPORATE SOLICITATION: 'ONLY STUDENT MEMBERS IN A REGISTERED ORGANIZATION CAN SOLICIT FUNDS "
                "FROM CORPORATIONS OR OTHER ORGANIZATIONS on behalf of a student organization' — and clubs "
                "need Office of Student Life approval before approaching an external company PLUS Office of "
                "College Advancement approval. TWO internal approvals before a club may even ask DGD for "
                "money. FUNDRAISING: 'The Office of Student Life must approve ALL fundraising activities/"
                "events (INCLUDING EVENTS THAT UTILIZE SUGGESTED DONATIONS) in advance'; Fundraiser Request "
                "Form 3 weeks ahead; proceeds to the Bursar within one week; money never into personal "
                "accounts. GIVEAWAYS: 'RAFFLE PRIZES AND GIVEAWAYS COST SHOULD NOT EXCEED $299'; winners must "
                "give an EMPL number and Baruch ID; members cannot win their own giveaways; approval must "
                "PRECEDE purchase. OFF-CAMPUS: an org event may be held off campus 'regardless of whether "
                "student activity fees are being used, ONLY with the permission and prior approval of the "
                "Office of Student Life AND the Dean of Students Office' — 8 weeks' notice, 6 months "
                "international, venue insurance naming Baruch as additional insured. NATIONAL AFFILIATION: "
                "'The Office of Student Life reserves the right to request a LETTER OF SUPPORT from any "
                "national or international organization that desires to have a chapter on the Baruch campus.'",
  'sponsor_required': '⚠ YES in practice, and it is not enough. A registered club must reserve the table; only '
                      'student members may solicit corporate funds; the club needs BOTH Student Life and '
                      'College Advancement approval to approach DGD; and the 15% outside-guest cap limits how '
                      'many DGD people can be present once they get there.',
  'clubs': [
    ('⚠ Blockchain Club',
     'Founded fall 2022 by Syed Samir with 2023 graduate Cristian Guerrero; relaunched and recruiting. Roughly '
     '100 people in one WhatsApp group, 10–12 active. Was seeking a board marketer and executive secretary, '
     'freshmen welcome. Aims to "help them build niche knowledge, writing opinion pieces on Blockchain, '
     'recognizing possible career choices" with guest speakers from financial sectors — A CLUB THAT BOOKS '
     'GUEST SPEAKERS IS A CLUB THAT WILL TAKE A CALL. ⚠ Contact is by Instagram DM or a LinkTree form; NO '
     'institutional email is published. Officer names deliberately not carried forward — rosters rotate and '
     'the source is a student-newspaper article.',
     'https://theticker.org/11901/business/baruchs-blockchain-club-starts-fresh/'),
    ('The CUNY Crypto Club at Baruch College',
     'Has a Medium publication (medium.com/@cunycrypto) and a LinkedIn company page. ⚠ Status on Baruch\'s own '
     'systems UNCONFIRMED — it may or may not be a currently registered organisation.',
     'https://medium.com/@cunycrypto'),
    ('⚠ 120+ clubs total — directory is LOGIN-GATED',
     'The public Student Clubs page lists NO club names; the full directory sits behind MyBaruch and is not '
     'publicly enumerable. Club Hours: Thursdays 12:40–2:20 PM (undergrad), Fridays 6–9 PM (graduate). Call '
     '(646) 312-4550 for room locations.',
     'https://studentaffairs.baruch.cuny.edu/studentlife/student-activities/student-clubs-organizations/'),
  ],
  'faculty': [
    ('⚠ Dr. Damali Smith Tolson',
     'DIRECTOR OF STUDENT LIFE — the decision-maker for every club activity, tabling reservation, fundraising '
     'approval and outside-guest exception at Baruch. Direct dial printed in The Informer PDF and confirmed on '
     'the staff page. START HERE.',
     'Office of Student Life, NVC 2-210',
     'damali.tolson@baruch.cuny.edu · (646) 312-4553',
     'https://studentaffairs.baruch.cuny.edu/studentlife/office-of-student-life-staff/'),
    ('Dr. Richard Suarez',
     'Associate Director of Operations — the space-and-operations gatekeeper. If Tolson says yes in principle, '
     'Suarez is who makes the 2nd-floor lobby table actually happen.',
     'Office of Student Life',
     'richard.suarez@baruch.cuny.edu · (646) 312-4552',
     'https://studentaffairs.baruch.cuny.edu/studentlife/office-of-student-life-staff/'),
    ('Stephen Palencia · Dinetta Curtis · Margaret Van-Ess Holman · Jan Martinez',
     'Assistant Director of Student Activities (Palencia — day-to-day club liaison, the most likely person to '
     'know which clubs are actually alive); Deputy Director (Curtis); Asst Dir Leadership Development '
     '(Van-Ess Holman); Asst Dir DEI (Martinez). All direct dials, all printed in The Informer.',
     'Office of Student Life',
     'stephen.palencia@ (646) 312-4566 · dinetta.curtis@ (646) 312-4569 · margaret.van-ess@ (646) 312-4554 · '
     'jan.martinez@ (646) 312-4564 — all @baruch.cuny.edu',
     'https://studentaffairs.baruch.cuny.edu/studentlife/office-of-student-life-staff/'),
    ('Office of Student Life — main line, plus operations and press',
     'MAIN LINE (646) 312-4550, NVC Room 2-210, student.life@baruch.cuny.edu. Operations: Natalie Otero '
     '(646) 312-3134, Yianice Nieves (646) 312-4555, Julia Skarzynska (646) 312-4599, Evelyn Almonte '
     '(646) 312-4560, Traci Espinet-Marquez (646) 312-4556. ⚠ THE TICKER, the student newspaper that already '
     'covered the Blockchain Club, is (646) 312-4710 in NVC 3-290 — a low-friction way in that requires no '
     'permit at all. WBMB Radio (646) 312-4720, NVC 3-280. Alumni Relations (646) 660-6097.',
     'Baruch College',
     'main line (646) 312-4550 · The Ticker (646) 312-4710 · WBMB (646) 312-4720',
     'https://studentaffairs.baruch.cuny.edu/studentlife/office-of-student-life-staff/'),
    ('(Faculty)',
     '⚠⚠ NOT CONFIRMED — NO BARUCH FACULTY MEMBER IS NAMED IN THIS PACKET. The Bert W. Wasserman Department of '
     'Economics and Finance directory FAILS SSL VERIFICATION to research tooling: "[SSL: '
     'CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate." A normal '
     'browser will load it fine. Zicklin is CUNY\'s business school with the strongest finance audience in '
     'New York — there is almost certainly someone here. Look up here.',
     'Bert W. Wasserman Dept of Economics and Finance, Zicklin School of Business',
     'no number published — look up here (site fails SSL to tooling)',
     'https://zicklin.baruch.cuny.edu/Department/economics-and-finance-faculty/'),
  ],
  'courses': [
    ('(Courses)',
     '⚠ NOT CONFIRMED. The Zicklin catalog could not be searched because zicklin.baruch.cuny.edu fails SSL '
     'verification. WARNING: the Baruch Confluence bulletin instances that ARE indexed are ARCHIVED editions '
     'from Fall 2016, Fall 2019 and Fall 2022 — DO NOT CITE THEM AS CURRENT. Gap to close in a browser.',
     'https://baruch-archived-graduate-2023-2024.catalog.cuny.edu/departments/ECOFIN-BAR/overview'),
    ('Zicklin public programming — "Blockchain to the Future: Understanding the Digital Economy"',
     'Evidence Zicklin runs public blockchain speaker events. Not a catalog course. Date not current.',
     'https://zicklin.baruch.cuny.edu/event/blockchain-to-the-future-understanding-the-digital-economy/'),
    ('(Fall 2026 offerings)',
     '⚠ NO BARUCH COURSE CONFIRMED FOR FALL 2026. Given the finance-heavy student body this is a real gap, '
     'not an absence — close it via the department directory once SSL is not a problem.',
     'https://zicklin.baruch.cuny.edu/Department/economics-and-finance-faculty/'),
  ],
  'events': [
    ('⚠ CLUB HOURS — Thursdays 12:40–2:20 PM, every week of term',
     'THE RECURRING EVENT THAT BEATS ANY FAIR. Every undergraduate club on campus meets in the same two-hour '
     'block, every Thursday. Graduate clubs Fridays 6–9 PM. Combined with the standing 2nd-floor NVC lobby '
     'table, this is the highest-density repeatable access at Baruch. Call (646) 312-4550 for room locations.',
     'https://studentaffairs.baruch.cuny.edu/studentlife/student-activities/student-clubs-organizations/'),
    ('The Ticker — student newspaper coverage',
     'Already covered the Blockchain Club\'s relaunch. A campus-press story requires NO facility permit, no '
     'sponsor and no 15% guest cap. (646) 312-4710, NVC 3-290.',
     'https://theticker.org/11901/business/baruchs-blockchain-club-starts-fresh/'),
    ('(Fall 2026 dated events)',
     '⚠ NONE CONFIRMED. No Baruch involvement fair, career fair or speaker series date could be verified for '
     'Fall 2026. Call the Office of Student Life.',
     'https://studentaffairs.baruch.cuny.edu/studentlife/about/'),
  ],
  'play': 'BARUCH HAS THE BEST FINANCE AUDIENCE IN NEW YORK AND THE MOST HOSTILE PAPERWORK. Zicklin is CUNY\'s '
          'business school, the student body is heavily finance and accounting, there is an active Blockchain '
          'Club that books guest speakers — and the student-org handbook contains the single most damaging '
          'sentence in the entire fifty-state packet: students may not use "MONEY TRANSFER SERVICES... '
          'EventBrite, Venmo, Zelle, CashApp, Chime, and other electronic sources of crowdfunding." A wallet '
          'or credit-purchase flow at a Baruch table walks straight into it. On top of that, only 15% of event '
          'participants may be outside guests, students may NEVER sign contracts, and there is no published '
          'route for a non-Baruch entity at all — CUNY Policy 4.02 category 6 says colleges "MAY permit" '
          'commercial users and Baruch publishes nothing about doing so. SO GO IN AS AN EDUCATOR, NOT A '
          'VENDOR. The single best door is the Blockchain Club, which explicitly brings in speakers from '
          'financial sectors; reach it through Stephen Palencia, Assistant Director of Student Activities, on '
          '(646) 312-4566, or start at the top with Director of Student Life Dr. Damali Smith Tolson on '
          '(646) 312-4553. Aim at CLUB HOURS — Thursdays 12:40–2:20 PM, every week, when every undergraduate '
          'club on campus is meeting at once. Second, cheapest door: The Ticker at (646) 312-4710 already '
          'covered the club\'s relaunch and a press story needs no permit, no sponsor and no guest cap. '
          'CALENDAR TRAP: CUNY loses Sep 7, Sep 11–13 and Sep 21 to holidays — mid-September Manhattan CUNY '
          'is dead. Hit Aug 31–Sep 4 or anything from Sep 22. And Baruch is fifteen minutes from NYU and '
          'twelve from Hunter on the 6 train, so it should never be a standalone trip.',
  'gaps': [
    '⚠⚠ Does the Informer\'s ban on "money transfer services... and other electronic sources of crowdfunding" '
    'reach a wallet sign-up or credit purchase at a table? Ask Dr. Suarez (646) 312-4552 BEFORE anything is '
    'set up, not after.',
    '⚠ zicklin.baruch.cuny.edu FAILS SSL VERIFICATION to tooling (CERTIFICATE_VERIFY_FAILED) — NO Baruch '
    'faculty member and NO Baruch course is confirmed in this packet as a result. Load it in a browser.',
    '⚠ The 120+ club directory is behind MyBaruch and is NOT publicly enumerable. Whether the CUNY Crypto Club '
    'is currently registered is unknown.',
    '⚠ No Baruch involvement fair exists or could be found for Fall 2026 — call (646) 312-4550.',
    'Will Baruch permit a category-6 commercial user under CUNY Policy 4.02 at all, and at what rate? Nothing '
    'is published.',
    'The Blockchain Club has no institutional email — contact is Instagram DM or a LinkTree form only.',
    '⚠ CUNY\'s primary Facility Use Policy PDF and CUNY Bylaws Article XV are BOTH ROBOTS-BLOCKED to tooling. '
    'A human should read both before any CUNY commitment.',
  ],
  },

 # ---------------------------------------------------------------- 4. Hunter (CUNY)
 {'state': 'New York',
  'name': 'CUNY Hunter College',
  'city': 'New York, NY (68th & Lexington, Manhattan)',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 3,
  'start': 'Fri Aug 28, 2026 — CUNY COMMON CALENDAR, same as Baruch and City College.',
  'adddrop': 'Last day to add Thu Sep 3, 2026 (CUNY common calendar).',
  'fallbreak': '⚠ Same CUNY September cluster: no classes Mon Sep 7 (Labor Day), Fri–Sun Sep 11–13 '
               '(Rosh Hashanah), Mon Sep 21 (Yom Kippur). Clean windows: Aug 31 – Sep 4, and Sep 22 onward.',
  'thanksgiving': 'College closed Thu–Fri Nov 26–27, 2026; no classes Nov 25 and Nov 28.',
  'lastclass': 'Fall term ends Mon Dec 21, 2026.',
  'finals': 'Tue Dec 15 – Mon Dec 21, 2026',
  'cal_url': 'https://our.catalog.cuny.edu/pages/6v5vCLMZ3vBKXnNNscUh',
  'cal_status': '⚠ PARTIAL — dates taken from the CUNY CENTRAL 2026-27 calendar, not from Hunter. '
                'HUNTER\'S OWN REGISTRAR CALENDAR PAGE RETURNS HTTP 403 to research tooling '
                '(hunter.cuny.edu/students/registration/academic-calendar/). Confirm Hunter-specific '
                'deviations by phone before relying on these.',
  'fair': 'Welcome Week — Club Fair & Carnival (plus a separate Graduate Student Association Club Fair)',
  'fair_date': '⚠ UNVERIFIED for Fall 2026. Recurring pattern CONFIRMED from a prior instance: held OUTDOORS '
               'ON 69TH STREET BETWEEN LEXINGTON AND 3RD AVENUES, 12:00–4:00 PM, in the last days of August '
               '(the confirmed instance was Aug 31). Rain plan: student clubs move to the 3rd-floor '
               'cafeteria, carnival activities to the West Lobby, food stays on 69th Street. Attractions '
               'include popcorn, cotton candy, caricatures and airbrush t-shirts — it is a carnival, not a '
               'quiet org fair. Fall 2026 date will post at hunter.cuny.edu/series/welcome-week/.',
  'fair_outside': '⚠ NOT ADDRESSED on any event page — the fair is student-club focused. BUT NOTE THE '
                  'JURISDICTIONAL WRINKLE: 69th Street between Lexington and 3rd is a NEW YORK CITY STREET, '
                  'and the fair happens on it under a City permit. That is a different legal fact from an '
                  'interior lobby. Raise it with counsel; do not improvise it.',
  'fair_cost': 'Not published for the fair. Known campus cost: AV tech support "50/hr. with a 5-hour minimum" '
               '— A $250 FLOOR on any AV-assisted event. Equipment borrowing itself is free. "There may be '
               'additional charges for Public Safety, Cleaning/Facilities, and Event Host."',
  'fair_deadline': '⚠ THE SHORTEST OUTSIDE-ENTITY LEAD TIME IN NEW YORK: vendor/visitor requests to the '
                   'Visitors Center "at least 48 hours prior to arriving on campus." Compare Columbia\'s ten '
                   'working days and Binghamton\'s fifteen business days.',
  'fair_url': 'https://hunter.cuny.edu/series/welcome-week/',
  'policy': 'Central Reservations — Student Organizations (operative for space and vendors); Solicitation of '
            'Funds (text not retrievable); above both, CUNY Policy 4.02 Facilities Use',
  'policy_url': 'https://www.hunter.cuny.edu/central-reservations-and-events/reservation-information/student-organizations/',
  'policy_key': "CENTRAL RESERVATIONS — STUDENT ORGANIZATIONS (hunter.cuny.edu/central-reservations-and-events/"
                "reservation-information/student-organizations/): 'STUDENT CLUBS MUST BE OFFICIALLY REGISTERED "
                "WITH THE OFFICE OF STUDENT ACTIVITIES TO REQUEST A SPACE RESERVATION.' 'ONLY CLUB OFFICERS "
                "(PRESIDENT, VICE PRESIDENT, TREASURER, OR SECRETARY) ARE AUTHORIZED TO SUBMIT RESERVATION "
                "REQUESTS' — a quiet anti-fronting provision: an ordinary member cannot book for you, and "
                "neither can an adviser. 'Once your space reservation is confirmed, you must submit a STUDENT "
                "EVENT INFORMATION FORM (SEIF) to finalize your event details.' '⚠ ALL EVENT SPACES — "
                "INCLUDING CLASSROOMS AND AUDITORIUMS — ARE PRIMARILY DESIGNATED FOR ACADEMIC USE, AND "
                "AVAILABILITY IS SUBJECT TO LIMITATIONS.' ⚠⚠ THE OUTSIDE-VENDOR ROUTE, VERBATIM AND "
                "REFRESHINGLY SHORT: 'REQUEST FOR VENDOR SERVICES OR VISITORS SHOULD BE SENT TO THE VISITOR'S "
                "CENTER (visitors@hunter.cuny.edu) AT LEAST 48 HOURS PRIOR TO ARRIVING ON CAMPUS.' That is a "
                "VISITOR CLEARANCE, NOT A COMMERCIAL-TABLING PERMIT — the underlying authority is still CUNY "
                "Policy 4.02 category 6, under which colleges 'MAY permit' commercial users and are never "
                "required to (full 4.02 text is carried in Baruch's policy_key; SUNY and CUNY are SEPARATE "
                "SYSTEMS). Community hours: 'Fridays after 4:00 PM' and weekends by request. MONEY: "
                "'Borrowing available equipment from Audio Visual Department is free of charge. IF YOU NEED A "
                "TECH FOR YOUR EVENT AND EXTENSIVE SET-UP, IT IS 50/HR. WITH A 5-HOUR MINIMUM' — a $250 floor "
                "— plus 'There may be additional charges for Public Safety, Cleaning/Facilities, and Event "
                "Host.' ⚠ HUNTER'S SOLICITATION OF FUNDS POLICY COULD NOT BE READ: the page "
                "(hunter.cuny.edu/students/campus-life/student-clubs/fundraising/) says only 'Below is the "
                "link to information, policies and procedures for solicitation of funds' and the actual text "
                "sits behind a link that did not resolve. THAT IS THE ONE DOCUMENT MOST LIKELY TO CONTAIN A "
                "COMMERCIAL PROHIBITION — get it in a browser before committing. ⚠ AND NOTE: the Welcome Week "
                "Club Fair happens ON 69TH STREET, a New York City street under a City permit, not on Hunter "
                "property — a genuinely different jurisdictional fact worth raising with counsel.",
  'sponsor_required': '⚠ YES for space — only a registered club\'s named officers may reserve. For a visitor '
                      'or vendor, the club or department emails the Visitors Center 48 hours ahead. Whether '
                      'that clearance extends to commercial tabling is NOT stated anywhere.',
  'clubs': [
    ('Investment and Trading Society of Hunter College',
     'Has a LinkedIn presence. The closest thing to a finance audience found at Hunter. Status on Hunter\'s '
     'own systems unconfirmed. No officer names carried forward.',
     'https://www.linkedin.com/in/hunterits/'),
    ('⚠ Club directory — HTTP 403, NOT ENUMERABLE',
     'The undergraduate student government clubs directory RETURNS HTTP 403 to research tooling. NO club list '
     'could be read and NO blockchain or crypto club at Hunter is confirmed either way. Call Student '
     'Activities on (212) 772-4908 and ask.',
     'https://www.hunter.cuny.edu/students/undergraduate-student-government/clubs/students/'),
    ('(Audience note)',
     'Hunter is a liberal-arts-and-sciences college with NO business school — the relevant populations sit in '
     'Economics and Computer Science, not a Zicklin-equivalent. Expect a thinner finance audience than '
     'Baruch, twelve minutes away on the same 6 train.',
     'https://www.hunter.cuny.edu/students/campus-life/office-of-student-activities/'),
  ],
  'faculty': [
    ('⚠ Office of Student Activities',
     'THE DIRECT LINE — and it does NOT appear on the office\'s own landing page. It was recovered from a '
     'Welcome Week event listing, which is exactly the sort of place these numbers hide. This office owns the '
     'Club Fair, club registration and club reservations.',
     'Hunter College Student Affairs',
     'student.activities@hunter.cuny.edu · (212) 772-4908 (direct)',
     'https://hunter.cuny.edu/event/club-fair-carnival-2/'),
    ('Central Reservations · Club Reservations · Visitors Center',
     'The three email doors: central7@hunter.cuny.edu (all space), clubrese@hunter.cuny.edu (club space), and '
     'visitors@hunter.cuny.edu — THE LAST ONE IS THE OUTSIDE-VENDOR CHANNEL, 48 hours\' notice. ⚠ NO DIRECT '
     'PHONE IS PUBLISHED FOR ANY OF THE THREE.',
     'Hunter College Central Reservations and Events',
     'no direct numbers published — route via the main line (212) 772-4000',
     'https://www.hunter.cuny.edu/central-reservations-and-events/reservation-information/student-organizations/'),
    ('Hunter College — main line',
     'MAIN LINE. Use it to reach Central Reservations or the Visitors Center, neither of which publishes a '
     'direct number.',
     'Hunter College',
     '(212) 772-4000 (main line)',
     'https://www.hunter.cuny.edu/central-reservations-and-events/reservation-information/student-organizations/'),
    ('Office of Student Activities landing page',
     '⚠ The office\'s own page renders its contact details behind a "View our contact information and business '
     'hours" link that did not resolve — THE PAGE ITSELF CARRIES NO NUMBER. Use the (212) 772-4908 direct line '
     'above, which came from an event page instead.',
     'Hunter College',
     'no number published on this page — look up here',
     'https://www.hunter.cuny.edu/students/campus-life/office-of-student-activities/'),
    ('(Faculty)',
     '⚠ NOT CONFIRMED — no Hunter faculty member working on blockchain, cryptocurrency, fintech or digital '
     'assets could be found on a live page. Hunter has no business school; look in Economics and Computer '
     'Science. Look up at the Hunter directory.',
     'Hunter College',
     'no number published — look up here',
     'https://www.hunter.cuny.edu/students/campus-life/office-of-student-activities/'),
  ],
  'courses': [
    ('(Courses)',
     '⚠ NOT CONFIRMED. No Hunter catalog course on blockchain, cryptocurrency or digital money could be '
     'located. With no business school, expect any relevant offering to sit in Economics or Computer Science. '
     'Genuine gap — not a finding of absence.',
     'https://www.hunter.cuny.edu/students/campus-life/office-of-student-activities/'),
    ('(CUNY-wide alternative)',
     'If a Hunter course is needed for credibility, the nearest confirmed CUNY finance curriculum is at '
     'Baruch, twelve minutes south on the 6 train — though Baruch\'s catalog is itself blocked by an SSL '
     'failure. See the Baruch record.',
     'https://our.catalog.cuny.edu/pages/6v5vCLMZ3vBKXnNNscUh'),
    ('(Fall 2026 offerings)',
     '⚠ NONE CONFIRMED at Hunter.',
     'https://our.catalog.cuny.edu/pages/6v5vCLMZ3vBKXnNNscUh'),
  ],
  'events': [
    ('Welcome Week — Club Fair & Carnival',
     '⚠ Fall 2026 date UNVERIFIED. Pattern: outdoors on 69th Street between Lex and 3rd, 12:00–4:00 PM, last '
     'days of August. The Fall 2026 date posts to the Welcome Week series page.',
     'https://hunter.cuny.edu/series/welcome-week/'),
    ('Graduate Student Association Club Fair',
     'A SEPARATE Welcome Week fair for graduate students — an older, better-capitalised audience than the '
     'undergraduate carnival, and a distinct booking.',
     'https://www.hunter.cuny.edu/event/graduate-student-association-club-fair-welcome-week/'),
    ('(Blockchain-specific events)',
     '⚠ NONE CONFIRMED at Hunter.',
     'https://www.hunter.cuny.edu/students/campus-life/student-events-and-programs/'),
  ],
  'play': 'HUNTER IS THE EASIEST DOOR IN CUNY AND THE THINNEST AUDIENCE. The mechanism is unusually simple: a '
          'registered club\'s named officer reserves the space, and vendor or visitor clearance goes to the '
          'Visitors Center on 48 HOURS\' NOTICE — the shortest outside-entity lead time anywhere in New York, '
          'against Columbia\'s ten working days and Binghamton\'s fifteen. But that is a visitor clearance, '
          'not a commercial-tabling permit, and the one document that would settle it — Hunter\'s Solicitation '
          'of Funds policy — could not be read; get it in a browser first. Set against that ease: Hunter has '
          'NO BUSINESS SCHOOL. The only finance-adjacent group found is the Investment and Trading Society, '
          'and the club directory returns HTTP 403 so no blockchain club is confirmed either way. THE SINGLE '
          'BEST DOOR IS THE OFFICE OF STUDENT ACTIVITIES ON (212) 772-4908 — a direct line that does not '
          'appear on the office\'s own page and had to be dug out of a Welcome Week event listing. Call it and '
          'ask three things: is there a blockchain, crypto or investment club currently registered; what is '
          'the Fall 2026 Club Fair date; and does 48-hour Visitors Center clearance cover a commercial table. '
          'Budget for the AV tech floor of $250 (50/hr, 5-hour minimum) if you need anything more than a '
          'folding table. Realistically Hunter is a HALF-DAY ADD-ON, not a destination: it sits eight stops '
          'from Baruch and one crosstown hop from Columbia, so fold it into a Manhattan cluster day rather '
          'than spending a trip on it. One thing genuinely worth knowing: the Club Fair happens on 69th '
          'Street, a New York City street under a City permit — not Hunter property.',
  'gaps': [
    '⚠ Hunter\'s Solicitation of Funds policy text COULD NOT BE RETRIEVED — the page links to it but the link '
    'did not resolve. This is the document most likely to carry a commercial prohibition. '
    'https://www.hunter.cuny.edu/students/campus-life/student-clubs/fundraising/',
    '⚠ Hunter\'s registrar academic calendar page RETURNS HTTP 403 — all dates here come from the CUNY central '
    'calendar. Confirm Hunter-specific deviations.',
    '⚠ The undergraduate student government club directory RETURNS HTTP 403 — no club list could be read and '
    'no blockchain or crypto club is confirmed either way.',
    '⚠ Fall 2026 Club Fair & Carnival date not published. Call (212) 772-4908.',
    'Does 48-hour Visitors Center clearance actually cover a commercial entity at a table, or only a guest '
    'speaker? Nothing on the page distinguishes them.',
    'No direct phone for Central Reservations or the Visitors Center — both are email-only.',
    'No Hunter faculty member on blockchain/fintech confirmed.',
  ],
  },

 # ---------------------------------------------------------------- 5. City College (CUNY)
 {'state': 'New York',
  'name': 'CUNY City College of New York',
  'city': 'New York, NY (Harlem, 138th & Convent)',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 3,
  'start': 'Fri Aug 28, 2026 — CUNY COMMON CALENDAR, same as Baruch and Hunter.',
  'adddrop': 'Last day to add Thu Sep 3, 2026 (CUNY common calendar).',
  'fallbreak': '⚠ Same CUNY September cluster — no classes Sep 7, Sep 11–13, Sep 21. Clean windows: '
               'Aug 31 – Sep 4, and Sep 22 onward.',
  'thanksgiving': 'College closed Thu–Fri Nov 26–27, 2026; no classes Nov 25 and Nov 28.',
  'lastclass': 'Fall term ends Mon Dec 21, 2026.',
  'finals': 'Tue Dec 15 – Mon Dec 21, 2026',
  'cal_url': 'https://www.ccny.cuny.edu/registrar/fall-2026-academic-calendar',
  'cal_status': '⚠ PARTIAL — dates taken from the CUNY CENTRAL 2026-27 calendar. CCNY publishes its own Fall '
                '2026 calendar ONLY as a downloadable PDF behind a "Click here to download" link; the HTML '
                'page carries NO dates at all.',
  'fair': '⚠ NO NAMED CCNY INVOLVEMENT FAIR COULD BE LOCATED. Tabling is a standing, request-based facility '
          'administered from NAC 1/210 rather than a single annual event.',
  'fair_date': '⚠ UNVERIFIED — no Fall 2026 CCNY fair date exists in any indexed page. Club Relations & '
               'Reservations operates from NAC 1/210 with published office hours and invites students to '
               '"stop by NAC 1/210." Call and ask.',
  'fair_outside': '⚠ YES, WITH A VETTING PROCESS — AND THIS IS THE FINDING. The Beaver Handbook: for tabling '
                  'requests involving EXTERNAL ORGANIZATIONS, clubs must submit within 15 BUSINESS DAYS and '
                  'the department will "request additional information on the external organization TO VET '
                  'THEM AND TO ENSURE THEIR AUTHENTICITY AND ITS APPROVAL BY THE COLLEGE." A named, written, '
                  'documented pathway for an outside organisation to appear at a CCNY table — more than NYU, '
                  'Columbia, Hunter, Cornell or Fordham offer. ⚠ BUT NO MONEY MAY CHANGE HANDS (see policy).',
  'fair_cost': 'No table fee published. ⚠ Real costs sit elsewhere: staffing fees "cannot be reduced or '
               'cancelled within 72 hours" of an event and departments are billed the FULL original amount '
               'for changes inside that window; NYC-FDNY-certified Fire Guards are required in designated '
               'Public Assembly Spaces; and metal detectors may be mandated by Public Safety AT THE '
               'ORGANISER\'S EXPENSE.',
  'fair_deadline': '⚠ 15 BUSINESS DAYS for a tabling request involving an external organisation; 10 BUSINESS '
                   'DAYS for an ordinary club table, first-come first-served.',
  'fair_url': 'https://groups.ccny.cuny.edu/clubreg/home/',
  'policy': 'The Beaver Handbook — A Guide for Club Leaders, 2025-2026 (operative); plus the CCNY Event Policy '
            '(external groups, insurance, security); above both, CUNY Policy 4.02 Facilities Use',
  'policy_url': 'https://www.ccny.cuny.edu/sites/default/files/2026-01/2025%20-%202026%20CCNY%20Student%20Club%20handbook.pdf',
  'policy_key': "THE BEAVER HANDBOOK 2025-2026 — ⚠ THE EXTERNAL-ORGANISATION TABLING ROUTE, WHICH IS THE "
                "CLEAREST IN CUNY: for tabling requests involving external organizations, clubs must submit "
                "requests within 15 BUSINESS DAYS and the department will 'REQUEST ADDITIONAL INFORMATION ON "
                "THE EXTERNAL ORGANIZATION TO VET THEM AND TO ENSURE THEIR AUTHENTICITY AND ITS APPROVAL BY "
                "THE COLLEGE.' For outside-organisation fundraising the SOAR Form requires the club to "
                "'properly write the name of the organization,' 'describe what said organization does and why "
                "you are fundraising for this charity,' and 'add organization's/institution's donation link'; "
                "these organisations 'WILL BE PROPERLY VETTED TO ENSURE THEIR AUTHENTICITY AND APPROVAL BY THE "
                "COLLEGE.' ⚠⚠ AND THEN THE MONEY BAN KILLS THE TRANSACTION: 'AS OF FALL 2023, FUNDRAISING TO "
                "INCREASE CLUB FUNDING IS PROHIBITED.' Clubs CANNOT collect funds on behalf of the "
                "organisation, CANNOT ACCEPT ANY FORM OF PAYMENTS, and cannot charge event admission fees, "
                "host bake sales, or sell items. Food must be 'pre-packaged or catered'; clubs are 'not "
                "permitted to sell food.' TABLING MECHANICS: requests 10 business days in advance, "
                "first-come first-served; clubs must 'arrange to ALWAYS HAVE A CLUB MEMBER PRESENT.' "
                "PROCUREMENT: all purchase requests must 'follow the University's established procurement "
                "process'; no purchases without prior Purchasing Department approval; 'REIMBURSEMENTS FOR "
                "EXPENSES WILL NOT BE ALLOWED.' ⚠ THE HANDBOOK PRINTS NO PHONE NUMBERS AT ALL — unusual, and "
                "recorded here deliberately; it gives names and room numbers only. "
                "CCNY EVENT POLICY (ccny.cuny.edu/gca/ccny-event-policy): external groups must provide "
                "insurance documentation meeting CCNY requirements; must demonstrate '⚠ SIGNIFICANT CCNY "
                "INTEREST' and alignment with the college's 'MISSION, GOALS, AND IDEALS'; must comply with all "
                "CCNY rules; and must have marketing materials approved by the Office of Events Management. "
                "'TICKETS AND MARKETING MATERIALS MUST CLEARLY IDENTIFY THE SPONSORING GROUP, ORGANIZATION OR "
                "DEPARTMENT ALONG WITH CONTACT INFORMATION.' ⚠ 'NO COMMERCIAL OR SALES ADVERTISING IS "
                "PERMITTED ON CAMPUS BULLETIN BOARDS.' ⚠⚠ 'CASH TRANSACTIONS ARE PROHIBITED; ONLY NON-CASH "
                "PAYMENT IS ALLOWED.' Staffing fees cannot be reduced or cancelled within 72 HOURS; metal "
                "detectors at the organiser's expense; NYC-FDNY-certified Fire Guards in Public Assembly "
                "Spaces. No insurance dollar limits are stated — use the CUNY tiers carried in Baruch's "
                "policy_key ($500k low-risk / $1M per occurrence and $2M aggregate standard / $2M–$5M "
                "high-risk, broker InterCity Agency 718-279-7705). ⚠⚠ READ THE TWO DOCUMENTS TOGETHER: AN "
                "OUTSIDE ORG CAN BE VETTED ONTO A CCNY TABLE IN 15 BUSINESS DAYS PROVIDED IT DOES NO SELLING, "
                "TAKES NO PAYMENTS AND PASSES THE 'SIGNIFICANT CCNY INTEREST' TEST. THAT IS AN "
                "EDUCATION-AND-LITERATURE POSTURE — WHICH, GIVEN THE BITLICENSE PROBLEM CARRIED IN NYU'S "
                "policy_key, IS THE ONLY POSTURE DGD SHOULD WANT IN NEW YORK ANYWAY. CCNY IS THE CLEANEST FIT "
                "IN THE STATE BETWEEN WHAT THE POLICY PERMITS AND WHAT DGD CAN SAFELY DO.",
  'sponsor_required': '⚠ YES — a registered CCNY club must submit the tabling request and a club member must '
                      'be present at the table throughout. The college then vets the external organisation '
                      'for "authenticity" and applies a "significant CCNY interest" test.',
  'clubs': [
    ('⚠ 100+ clubs — roster NOT publicly enumerated',
     'Club Relations & Reservations administers 100+ undergraduate and graduate clubs from NAC 1/210, but the '
     'site is a services and registration portal, not a directory. NO club names are published. NO blockchain '
     'or crypto club at CCNY is confirmed either way — email clubreg@ccny.cuny.edu and ask.',
     'https://groups.ccny.cuny.edu/clubreg/home/'),
    ('(Where a crypto club would live)',
     'CCNY\'s Grove School of Engineering and its Computer Science department are the likeliest home. The '
     'Colin Powell School covers economics and public affairs. Ask Club Relations for both.',
     'https://groups.ccny.cuny.edu/clubreg/club-registration-steps/'),
    ('Undergraduate Student Government / Graduate Student Council',
     'usg@ccny.cuny.edu and gsc@ccny.cuny.edu. The student governments charter clubs and are the fastest route '
     'to finding out which technical clubs are actually active this year.',
     'https://groups.ccny.cuny.edu/clubreg/student-organization-club-space-(socs)/'),
  ],
  'faculty': [
    ('⚠ Department of Student Life and Leadership Development — NAC 1/210',
     'THE OFFICE THAT VETS EXTERNAL ORGANISATIONS AND APPROVES TABLES. It runs the 15-business-day external-'
     'org process. ⚠ THE BEAVER HANDBOOK PRINTS NO PHONE NUMBERS AT ALL — I read it specifically for that and '
     'there are none. Email clubreg@ccny.cuny.edu or route through the main line.',
     'CCNY Student Affairs',
     'clubreg@ccny.cuny.edu · no direct number published — main line (212) 650-7000',
     'https://groups.ccny.cuny.edu/clubreg/home/'),
    ('Ramón De Los Santos, Ed.D.',
     'Assistant Vice President of Student Affairs — the senior name printed in the Beaver Handbook and the '
     'escalation point if Club Relations stalls. ⚠ No direct contact published in the handbook.',
     'CCNY Division of Student Affairs',
     'no number published — look up here',
     'https://www.ccny.cuny.edu/studentaffairs'),
    ('CCNY Office of Events Management',
     'Approves marketing materials for external groups and applies the "significant CCNY interest" test under '
     'the CCNY Event Policy. Reachable at ccnyevents@ccny.cuny.edu; the only number on the policy page is the '
     'campus main line.',
     'CCNY',
     'ccnyevents@ccny.cuny.edu · (212) 650-7000 (main line)',
     'https://www.ccny.cuny.edu/gca/ccny-event-policy'),
    ('Sandy Lee',
     'SSC Business Office — named in the Beaver Handbook for club financial matters. Relevant because CCNY '
     'clubs may not accept payments of any kind, so anything involving money routes here. No phone published.',
     'CCNY Student Services Corporation',
     'slee2@ccny.cuny.edu · no number published',
     'https://www.ccny.cuny.edu/sites/default/files/2026-01/2025%20-%202026%20CCNY%20Student%20Club%20handbook.pdf'),
    ('(Faculty)',
     '⚠ NOT CONFIRMED — no CCNY faculty member working on blockchain, cryptocurrency or digital assets could '
     'be found on a live page. Look in the Grove School of Engineering (CS) and the Colin Powell School '
     '(economics). Look up here.',
     'CCNY',
     'no number published — look up here',
     'https://www.ccny.cuny.edu/studentaffairs'),
  ],
  'courses': [
    ('(Courses)',
     '⚠ NOT CONFIRMED. No CCNY catalog course on blockchain, cryptocurrency or digital money could be located. '
     'Check the Grove School of Engineering (computer science) and the Colin Powell School catalogs. Genuine '
     'gap.',
     'https://www.ccny.cuny.edu/registrar/academic-calendar'),
    ('(CUNY-wide note)',
     'CCNY is CUNY\'s engineering and sciences flagship — the audience is technical rather than financial, '
     'which suits an education-first posture better than a finance pitch.',
     'https://www.ccny.cuny.edu/activities/services'),
    ('(Fall 2026 offerings)',
     '⚠ NONE CONFIRMED at CCNY.',
     'https://www.ccny.cuny.edu/registrar/fall-2026-academic-calendar'),
  ],
  'events': [
    ('(Involvement fair)',
     '⚠ NO NAMED CCNY FAIR COULD BE FOUND for Fall 2026 or any year. Tabling is a standing request-based '
     'facility instead — arguably better, because it is available all term rather than one afternoon.',
     'https://groups.ccny.cuny.edu/clubreg/home/'),
    ('(Blockchain-specific events)',
     '⚠ NONE CONFIRMED at CCNY.',
     'https://www.ccny.cuny.edu/activities/services'),
    ('Three stops from Columbia on the 1 train',
     'CCNY (138th & Convent) is roughly six minutes from Columbia (116th & Broadway). Whatever is booked at '
     'Columbia should have a CCNY half-day attached to it — the two campuses are functionally the same trip.',
     'https://www.ccny.cuny.edu/studentaffairs'),
  ],
  'play': 'CCNY IS THE BEST POLICY FIT IN NEW YORK AND ALMOST NOBODY WOULD GUESS IT. The Beaver Handbook '
          'contains something no other campus in this packet has in writing: a named, documented process by '
          'which a club submits a tabling request involving an EXTERNAL ORGANISATION on 15 business days\' '
          'notice, after which the college vets that organisation for "authenticity." That is a real door. '
          'The catch is that CCNY has simultaneously banned every form of money movement — "as of Fall 2023, '
          'fundraising to increase club funding is prohibited," clubs "cannot accept any form of payments," '
          'and campus-wide "cash transactions are prohibited." So the ONLY posture available at CCNY is '
          'education and literature with no transaction — WHICH IS EXACTLY THE POSTURE THE BITLICENSE '
          'PROBLEM FORCES ON DGD EVERYWHERE IN NEW YORK ANYWAY. CCNY is the one campus where the policy '
          'constraint and the legal constraint point the same direction, so nothing is lost by complying. '
          'THE SINGLE BEST DOOR IS THE DEPARTMENT OF STUDENT LIFE AND LEADERSHIP DEVELOPMENT IN NAC 1/210 — '
          'email clubreg@ccny.cuny.edu, because the Beaver Handbook prints no phone numbers whatsoever and '
          'the only number on campus is the main line (212) 650-7000. Start the 15-business-day clock early '
          'and prepare for the "significant CCNY interest" test: lead with the Grove School of Engineering '
          'audience and an educational framing, not a product pitch. Practically, never make CCNY a '
          'standalone trip — it is three stops up the 1 train from Columbia, six minutes, so it attaches to '
          'whatever is booked in Morningside Heights. Watch the CUNY September holes: Sep 7, 11–13 and 21 are '
          'all dead.',
  'gaps': [
    '⚠ THE BEAVER HANDBOOK PRINTS NO PHONE NUMBERS AT ALL. The only confirmed CCNY number in this packet is '
    'the campus main line (212) 650-7000. Get a direct line for NAC 1/210.',
    '⚠ Is a crypto project capable of passing the "significant CCNY interest" test and the "mission, goals, '
    'and ideals" screen? Ask Events Management at ccnyevents@ccny.cuny.edu before spending 15 business days.',
    '⚠ The 100+ club roster is NOT publicly enumerated — no blockchain, crypto, fintech or investment club at '
    'CCNY is confirmed either way.',
    '⚠ CCNY publishes its Fall 2026 calendar ONLY as a PDF download; the HTML page carries no dates. Dates '
    'here come from the CUNY central calendar.',
    'No CCNY faculty member on blockchain/digital assets confirmed.',
    'No CCNY course on blockchain/crypto confirmed.',
    'Insurance dollar limits for an external group at CCNY are not stated on the Event Policy page — only the '
    'requirement. Use the CUNY tiers and confirm.',
  ],
  },

 # ---------------------------------------------------------------- 6. Stony Brook (SUNY)
 {'state': 'New York',
  'name': 'Stony Brook University',
  'city': 'Stony Brook, NY (Long Island)',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 4,
  'start': 'Mon Aug 24, 2026 (M–F classes). Saturday classes begin Sat Aug 29.',
  'adddrop': '⚠ NOT PUBLISHED on the fetched Fall 2026 calendar. Gap — call the registrar.',
  'fallbreak': 'Mon–Tue Oct 12–13, 2026 — a two-day break, the standard SUNY pattern shared with Buffalo, '
               'Albany and RIT.',
  'thanksgiving': 'Wed Nov 25 – Sun Nov 29, 2026',
  'lastclass': 'Last day of M–F classes Mon Dec 7, 2026 (last Saturday classes Sat Dec 5). Reading days '
               'Dec 6, Dec 8, Dec 12 and Dec 13.',
  'finals': 'Dec 9–17, 2026, split between M–F and Saturday classes.',
  'cal_url': 'https://www.stonybrook.edu/registrar/academic-calendar/fall2026-summer2027.html',
  'cal_status': 'CONFIRMED — registrar Fall 2026–Summer 2027 calendar, dates carrying explicit weekdays. '
                'NOTE the separate undergraduate Fall 2026 page (registrar/academic-calendar/future-terms/'
                'undergrad-calendar-fall-2026.html) returned HTTP 404; the combined page above is the '
                'working one.',
  'fair': 'Seawolves Block Party (the Involvement Fair) — "Seawolves\' Street"',
  'fair_date': '⚠ CONFIRMED FOR FALL 2026 — THE BEST-DOCUMENTED FAIR DATE IN THE STATE: Friday August 28, '
               '2026, 1:00–5:00 PM, on the ACADEMIC MALL. Two club tabling shifts: 1:00–2:30 PM for '
               'Academic/Honor Society, Activism/Advocacy, Fraternity & Sorority, Media and Sport clubs; '
               '3:30–5:00 PM for Community Awareness/Service, Cultural, Graduate, Religious/Spiritual, '
               'Leisure and Performance organisations. DEPARTMENT TABLING RUNS CONTINUOUSLY 1:00–5:00 PM. '
               '⚠⚠ HARD CONFLICT: Aug 28, 2026 is ALSO the first day of classes at all three Manhattan CUNY '
               'campuses. Long Island and Manhattan cannot both be covered that day.',
  'fair_outside': '⚠ NO — the fair is for Stony Brook student organisations and departments only. '
                  'Participation requires "re-registration approval for the 26-27 Academic Year" and category '
                  'verification; organisations receive an RSVP form by email to secure a spot. THE PAID '
                  'THIRD-PARTY ROUTE IS SEPARATE — a revocable permit through Conference Services, '
                  '(631) 632-1930. Use that, not the fair.',
  'fair_cost': 'No cost published for the fair. For the third-party permit route: "The University must be '
               'reimbursed for ALL COSTS INCURRED" including Direct Costs — ⚠ NO DOLLAR RATE CARD IS '
               'PUBLISHED ANYWHERE. Get a written quote from Conference Services before committing.',
  'fair_deadline': 'Fair: RSVP form issued to eligible organisations by email, deadline not published. '
                   'Third-party permit: no published lead time — ask Conference Services on (631) 632-1930.',
  'fair_url': 'https://www.stonybrook.edu/commcms/studentaffairs/sac/Get_Involved/Clubs_and_Organizations/involvement_fairs.php',
  'policy': 'Use of Campus Facilities Policy (eff. 07/26/2024) — the operative third-party document; plus the '
            'Fundraising and Solicitation on Campus Policy (eff. 11/18/2022), the Sponsorship and Advertising '
            'Policy and the Public Assembly Policy',
  'policy_url': 'https://www.stonybrook.edu/policy/policies/use_of_campus_facilities_policy.php',
  'policy_key': "⚠ SUNY SYSTEMWIDE LAYER — REPORTED ONCE HERE FOR ALL FOUR SUNY CAMPUSES IN THIS PACKET "
                "(Stony Brook, Buffalo, Binghamton, Albany). SUNY AND CUNY ARE SEPARATE SYSTEMS WITH SEPARATE "
                "BOARDS OF TRUSTEES — the CUNY layer is in Baruch's policy_key; DO NOT CONFLATE THEM. "
                "SUNY POLICY 5607, 'COMMERCIAL USE POLICY (Use of University Facilities for Commercial "
                "Purposes),' EFFECTIVE MARCH 28, 2012 (suny.edu/sunypp/documents.cfm?doc_id=704): 'Use of "
                "University facilities for instruction, research and public service TAKE PRIORITY OVER THE "
                "COMMERCIAL USE of University facilities.' Commercial activity 'shall not be in conflict with, "
                "and shall advance the mission of, the campus'; 'shall not infringe upon, delay or conflict "
                "with the normal operation of the campus'; '⚠ SHALL NOT HAVE A SIGNIFICANT POTENTIAL FOR "
                "MATERIAL ADVERSE EFFECT ON THE REPUTATION OF THE CAMPUS FOR ACADEMIC INTEGRITY AND "
                "INDEPENDENCE' — THAT IS THE CLAUSE A RISK-AVERSE ADMINISTRATOR WILL REACH FOR WHEN A CRYPTO "
                "PROJECT ASKS TO TABLE, SO HAVE AN ANSWER READY; 'Commercial use shall not compete with or "
                "replicate activities of the campus auxiliary services corporation, campus foundation, or "
                "other campus-related entities'; 'shall not violate existing agreements between the campus... "
                "and vendors providing goods or services on campus'; 'shall conform to federal tax law "
                "restrictions on private use of facilities financed by tax-exempt bonds.' ⚠ 5607 DEVOLVES THE "
                "REAL RULES — each campus must adopt local policies specifying authorisation procedures, "
                "eligible facilities, cost structures and fair-market appraisal standards. SUNY DOES NOT "
                "RESOLVE FOUR CAMPUSES AT A STROKE; it sets a reputational-risk screen and sends you to the "
                "campus. SUNY POLICY 5603, 'USE OF FACILITIES BY NON-COMMERCIAL ORGANIZATIONS,' EFFECTIVE "
                "JUNE 22, 2020 (doc_id=374): covers not-for-profit, governmental, charitable, civic and "
                "religious groups; excludes auxiliary services corporations, recognised student government "
                "organisations and alumni organisations. 'The University intends NOT TO COMPETE WITH PRIVATE "
                "BUSINESS ENTERPRISES having similar facilities'; 'Auxiliary services, such as food, legal "
                "beverages, vending machines and bookstore, SHALL NOT BE PROVIDED' except incidentally; "
                "organisations 'may charge an admission fee or accept donations subject to pertinent state and "
                "local laws and approval of the campus president.' ⚠⚠ DGD IS NOT A NON-COMMERCIAL "
                "ORGANISATION. 5603 IS THE WRONG DOOR AND IT MATTERS NOT TO WALK THROUGH IT BY ACCIDENT — "
                "several SUNY campuses point third-party free-speech applicants at 5603, which quietly "
                "confirms that the third-party forum route is for NON-COMMERCIAL expression only. "
                "SUNY RULES FOR THE MAINTENANCE OF PUBLIC ORDER, DOCUMENT 3653, EFFECTIVE JUNE 10, 2009 "
                "(doc_id=351), adopted under ARTICLE 129-A of the Education Law (the Henderson Act): the "
                "president must 'INFORM ANY LICENSEE OR INVITEE WHO SHALL VIOLATE ANY PROVISIONS OF THESE "
                "RULES THAT HIS OR HER LICENSE OR INVITATION IS WITHDRAWN' and direct them to leave; for "
                "non-affiliated violators, must 'inform the violator that they are NOT AUTHORIZED TO REMAIN ON "
                "THE PROPERTY of the campus and direct them to leave the premises,' with ejection and TRESPASS "
                "OR LOITERING PROSECUTION to follow. THIS IS THE ENFORCEMENT BACKSTOP — it is how a SUNY "
                "campus removes an unpermitted table. === NOW STONY BROOK ITSELF === USE OF CAMPUS FACILITIES "
                "POLICY, EFFECTIVE 07/26/2024, next review 07/26/2027. Two user categories: 'Students, "
                "faculty, and staff may reserve available space on campus to hold events' related to their "
                "University role; and THIRD-PARTY USE by external organisations and individuals, WHICH "
                "REQUIRES A REVOCABLE PERMIT THROUGH CONFERENCE SERVICES. Third parties must submit through "
                "Conference Services, comply with all University policies, be responsible for 'ALL RELATED "
                "CHARGES INCURRED for use of University facilities,' and not interfere with scheduled academic "
                "classes. INSURANCE: 'Permit applicants must SECURE APPROPRIATE LIABILITY INSURANCE NAMING THE "
                "STATE OF NEW YORK, THE STATE UNIVERSITY OF NEW YORK' as additional insureds — ⚠ NO DOLLAR "
                "LIMIT IS PUBLISHED; get it in writing before budgeting. COST RECOVERY: 'The University must "
                "be reimbursed for all costs incurred' including Direct Costs, with waivers possible for "
                "'significant public benefit.' ⚠⚠ ANTI-FRONTING — THE CLEANEST SUCH CLAUSE IN NEW YORK: 'IF "
                "ANY REVENUE GENERATED FROM THE USE OF FACILITIES IS RECEIVED BY AN EXTERNAL ORGANIZATION OR "
                "INDIVIDUAL FOR ITS OWN BENEFIT, THE USE OF CAMPUS FACILITIES IS NOT A UNIVERSITY USE.' It "
                "does not merely say a club may not front for you — IT SAYS THE MOMENT DGD BENEFITS FROM THE "
                "REVENUE, THE RESERVATION IS RECLASSIFIED AS THIRD-PARTY REGARDLESS OF WHOSE NAME IS ON IT. A "
                "club booking a room for a DGD sign-up drive converts, by operation of the policy, into a paid "
                "third-party permit. QUOTE IT BEFORE SOMEONE ELSE DOES. FUNDRAISING AND SOLICITATION ON CAMPUS "
                "POLICY, EFFECTIVE 11/18/2022 — ⚠ NEXT REVIEW DATE 11/18/2025 HAS PASSED; CONFIRM IT IS STILL "
                "CURRENT: 'RAFFLES AND OTHER GAMES OF CHANCE ARE NOT PERMITTED'; unapproved use of campus mail "
                "for solicitation prohibited; fundraising must benefit the University unless authorised by the "
                "President; 'UNIVERSITY ADVANCEMENT STAFF EXCLUSIVELY HANDLES ALL FUNDRAISING'; student "
                "activities may solicit only WITH WRITTEN AUTHORIZATION FROM THE VICE PRESIDENT FOR STUDENT "
                "AFFAIRS; activities projecting OVER $1,000 in revenue require coordination through the Office "
                "of the Vice President for Advancement; pre-approved activities needing facilities must submit "
                "a Facilities Use Request form.",
  'sponsor_required': '⚠ NO — AND SPONSORSHIP IS THE WRONG STRATEGY HERE. Third parties get their own revocable '
                      'permit through Conference Services. The anti-fronting clause reclassifies any '
                      'club-hosted event from which DGD derives revenue as third-party use anyway, so routing '
                      'through a club buys nothing and risks the club. PAY THE PERMIT.',
  'clubs': [
    ('⚠ VIP team "Blockchain, Crypto, and Web3 in Business and Finance"',
     '⚠⚠ THE TEAM NAME IS REAL BUT THE PAGE IS AN UNFILLED TEMPLATE — Goals, Faculty and Contact all render '
     'as "." with no content. A Vertically Integrated Projects team is a multi-year faculty-led undergraduate '
     'research group, which would be an excellent door IF it exists. NOTHING BEHIND THE NAME IS VERIFIED. '
     'Call the VIP Program before assuming it is live.',
     'https://www.stonybrook.edu/commcms/vertically-integrated-projects/teams/_team_page/team_page.php?team=Blockchain,+Crypto,+and+Web3+in+Business+and+Finance'),
    ('Computer Science student organizations',
     'The CS department maintains its own organisations page. No blockchain or crypto club is named on it. '
     'CS is the likeliest home of a technical crypto group at Stony Brook.',
     'https://www.cs.stonybrook.edu/students/organizations'),
    ('⚠ SB Engaged (CampusLabs) — JAVASCRIPT-RENDERED, NOT READABLE',
     'Stony Brook\'s org directory runs on CampusLabs and returned no data to tooling. NO named blockchain or '
     'crypto student club at Stony Brook could be confirmed. Call Student Engagement on (631) 632-9392 and '
     'ask which clubs exist.',
     'https://stonybrook.campuslabs.com/engage/event/11346536'),
  ],
  'faculty': [
    ('⚠ Conference & Event Services',
     'THE THIRD-PARTY PERMIT. This is the number that actually buys DGD access to Stony Brook — the Use of '
     'Campus Facilities Policy names this office as the sole route for external organisations. Ask for the '
     'revocable permit process, the Direct Cost quote (no rate card is published) and the insurance dollar '
     'limit (also not published).',
     'Stony Brook University',
     '(631) 632-1930',
     'https://www.stonybrook.edu/policy/policies/use_of_campus_facilities_policy.php'),
    ('Student Engagement & Activities',
     'Owns the Seawolves Block Party (Fri Aug 28, 2026, 1–5 PM, Academic Mall) and all club tabling. Stony '
     'Brook Union Suite 205. This is who knows which clubs exist, since SB Engaged is unreadable.',
     'Stony Brook University',
     'studentengagement@stonybrook.edu · (631) 632-9392',
     'https://www.stonybrook.edu/commcms/studentaffairs/sac/Get_Involved/Clubs_and_Organizations/involvement_fairs.php'),
    ('Enterprise Risk Management',
     'Sets the insurance certificate requirements. The policy requires naming the State of New York and SUNY '
     'as additional insureds but PUBLISHES NO DOLLAR LIMIT — this office is where that number comes from.',
     'Stony Brook University',
     '(631) 632-9500',
     'https://www.stonybrook.edu/policy/policies/use_of_campus_facilities_policy.php'),
    ('University Advancement · Office of the VP for Student Affairs · Procurement',
     'Advancement "exclusively handles all fundraising" and must be involved above $1,000 of projected '
     'revenue; the VP for Student Affairs issues the written authorisation without which no student activity '
     'may solicit at all; Procurement handles vendor contracting.',
     'Stony Brook University',
     'Advancement (631) 632-6300 · VP Student Affairs (631) 632-6700 · Procurement (631) 632-6010',
     'https://www.stonybrook.edu/policy/policies/fundraising_and_solicitation_on_campus_policy.php'),
    ('(Faculty)',
     '⚠ NOT CONFIRMED — no Stony Brook faculty member working on blockchain, cryptocurrency or digital assets '
     'could be found on a live page. The College of Business and its MS in Finance are where to look, and the '
     'empty VIP team page suggests someone was at least assigned to the subject. Look up here.',
     'Stony Brook College of Business',
     'no number published — look up here',
     'https://www.stonybrook.edu/commcms/business/'),
  ],
  'courses': [
    ('(Courses)',
     '⚠ NOT CONFIRMED. No Stony Brook catalog course on blockchain, cryptocurrency or fintech could be '
     'located. The College of Business MS in Finance is the likeliest home.',
     'https://www.stonybrook.edu/commcms/business/graduates/ms-finance-new.php'),
    ('VIP — "Blockchain, Crypto, and Web3 in Business and Finance"',
     '⚠ The only blockchain-LABELLED academic activity found at Stony Brook, and ITS PAGE IS AN EMPTY '
     'TEMPLATE. VIP teams carry course credit, so if this is real it is effectively a multi-semester course '
     'with a captive audience. VERIFY BEFORE RELYING ON IT.',
     'https://www.stonybrook.edu/commcms/vertically-integrated-projects/teams/_team_page/team_page.php?team=Blockchain,+Crypto,+and+Web3+in+Business+and+Finance'),
    ('(Fall 2026 offerings)',
     '⚠ NONE CONFIRMED at Stony Brook.',
     'https://www.stonybrook.edu/commcms/business/'),
  ],
  'events': [
    ('⚠⚠ Seawolves Block Party — Fri Aug 28, 2026, 1:00–5:00 PM, Academic Mall',
     'THE BEST-DOCUMENTED FAIR IN NEW YORK, confirmed on Stony Brook\'s own Fall 2026 page with shift times '
     'and categories. Clubs table in two shifts; departments run continuously 1–5 PM. OUTSIDE ORGS ARE NOT '
     'ADMITTED — but knowing the date matters because it is the one afternoon every club on campus is in one '
     'place. ⚠ SAME DAY as the CUNY first day of classes in Manhattan.',
     'https://www.stonybrook.edu/commcms/studentaffairs/sac/Get_Involved/Clubs_and_Organizations/involvement_fairs.php'),
    ('Third-party permitted event via Conference Services',
     'Not an event so much as the mechanism: a revocable permit, cost-recovered, insured naming the State of '
     'New York and SUNY. This is the only compliant way DGD itself appears on this campus. (631) 632-1930.',
     'https://www.stonybrook.edu/policy/policies/use_of_campus_facilities_policy.php'),
    ('(Blockchain-specific events)',
     '⚠ NONE CONFIRMED at Stony Brook.',
     'https://www.cs.stonybrook.edu/students/organizations'),
  ],
  'play': 'STONY BROOK IS THE MOST PROCEDURALLY OPEN PUBLIC CAMPUS IN NEW YORK AND THE ONE WHERE YOU MUST NOT '
          'ROUTE THROUGH A CLUB. Its Use of Campus Facilities Policy names a real third-party route — a '
          'revocable permit through Conference & Event Services on (631) 632-1930 — with a named office, '
          'published phone numbers and cost recovery. It also carries the sharpest anti-fronting clause in the '
          'state: "IF ANY REVENUE GENERATED FROM THE USE OF FACILITIES IS RECEIVED BY AN EXTERNAL ORGANIZATION '
          'OR INDIVIDUAL FOR ITS OWN BENEFIT, THE USE OF CAMPUS FACILITIES IS NOT A UNIVERSITY USE." That '
          'sentence reclassifies any club-hosted DGD event as paid third-party use automatically, so '
          'sponsorship buys nothing and puts the club at risk. PAY THE PERMIT. Call (631) 632-1930 first and '
          'get two numbers nobody publishes: the Direct Cost quote and the insurance dollar limit (Enterprise '
          'Risk Management on (631) 632-9500 sets the latter; the policy requires naming the State of New York '
          'and SUNY as additional insureds but names no figure). SECOND CALL: Student Engagement on '
          '(631) 632-9392, because SB Engaged is JavaScript-only and nobody outside that office knows which '
          'clubs actually exist — including whether the "Blockchain, Crypto, and Web3 in Business and Finance" '
          'VIP team is real, since its page is a literally empty template. TIMING: the Seawolves Block Party '
          'is CONFIRMED for Friday August 28, 2026, 1–5 PM on the Academic Mall — outside orgs cannot table, '
          'but it is the one afternoon every club is in one place, so it is worth walking. ⚠ That is the same '
          'day CUNY starts classes in Manhattan; you cannot do both.',
  'gaps': [
    '⚠ NO DOLLAR RATE CARD for third-party facility use is published anywhere. Get a written quote from '
    'Conference Services (631) 632-1930 before committing.',
    '⚠ NO INSURANCE DOLLAR LIMIT is published — only the requirement to name the State of New York and SUNY as '
    'additional insureds. Enterprise Risk Management (631) 632-9500.',
    '⚠ The Fundraising and Solicitation policy shows next review 11/18/2025, WHICH HAS PASSED. Confirm the '
    'version quoted here is still operative.',
    '⚠ The VIP team "Blockchain, Crypto, and Web3 in Business and Finance" has an UNFILLED TEMPLATE page — '
    'Goals, Faculty and Contact all render as ".". Real or vapour is unknown.',
    '⚠ SB Engaged is JavaScript-rendered — no Stony Brook club roster could be read and no blockchain or '
    'crypto club is confirmed either way. (631) 632-9392.',
    'Add/drop deadline not published on the Fall 2026 calendar.',
    'No lead time is published for a third-party permit application — ask.',
    'No Stony Brook faculty member on blockchain/digital assets confirmed.',
  ],
  },

 # ---------------------------------------------------------------- 7. Buffalo (SUNY)
 {'state': 'New York',
  'name': 'University at Buffalo',
  'city': 'Buffalo, NY',
  'type': 'Public',
  'tier': 'A — Named target',
  'access': 3,
  'start': 'Mon Aug 24, 2026 (15-week session). Two concurrent 7-week sessions: Session 1 Aug 24 – Oct 14, '
           'Session 2 Oct 15 – Dec 7.',
  'adddrop': 'Mon Aug 31, 2026. Last day to resign a course Wed Nov 11. Maximum 19 credit hours in fall. '
             'Note: "Additional charges will be applied to a student\'s bill if they do not register for '
             'courses by the published billing dates."',
  'fallbreak': 'Mon–Tue Oct 12–13, 2026 — the standard SUNY two-day break, same days as Stony Brook, Albany '
               'and RIT.',
  'thanksgiving': 'Wed Nov 25 – Sat Nov 28, 2026',
  'lastclass': 'Session ends Wed Dec 16, 2026 (7-week Session 2 classes end Dec 7).',
  'finals': 'Dec 9–16, 2026',
  'cal_url': 'https://www.buffalo.edu/registrar/registration/important-dates-and-enrollment-appointments/fall.html',
  'cal_status': 'CONFIRMED — registrar Fall 2026 important-dates page. ⚠ NAVIGATION TRAP: the "Future Academic '
                'Calendars" page (buffalo.edu/registrar/calendars/future-academic-calendars.html) BEGINS AT '
                '2027-28 and contains NO Fall 2026 dates at all. Registrar main line 716-645-5698.',
  'fair': '⚠ NO UB INVOLVEMENT FAIR OR ORG FAIR COULD BE CONFIRMED FOR FALL 2026.',
  'fair_date': '⚠⚠ GENUINE GAP — NOT A FINDING OF ABSENCE. "Fall Fest" at UB is a Student Association CONCERT '
               'SERIES, not an org fair, and SA CANCELLED the 2023 Fall Fest citing space availability '
               '(ubspectrum.com/article/2023/09/sa-cancels-2023-fall-fest). The SA events system '
               '(sa.buffalo.edu, a Joomla/JEvents install) returned only archived 2022 items to tooling. '
               'CALL STUDENT UNIONS ON (716) 645-2055 AND ASK WHETHER AN ORG FAIR EXISTS AT ALL.',
  'fair_outside': '⚠ NO AT THE UNION — the decisive sentence is "NON-UNIVERSITY GROUPS MAY NOT RESERVE '
                  'CLASSROOM AND GENERAL CAMPUS SPACE THROUGH THE STUDENT UNIONS." Those interested are '
                  'directed to contact UNIVERSITY EVENTS instead, which is a full-service office with six '
                  'named staff on published direct lines. UB is bifurcated: free for clubs, closed at the '
                  'Union for outsiders, routed to University Events.',
  'fair_cost': 'Recognised student clubs typically reserve at NO CHARGE. ⚠ For non-University groups, NO RATE '
               'CARD IS PUBLISHED — the Union page points to a "View current fee information" link and the '
               'University Events route is quoted bespoke. Known money terms: $30 PER SPACE cancellation fee '
               'if not cancelled two business days out.',
  'fair_deadline': '⚠ FOURTEEN BUSINESS DAYS in advance for a Union reservation, and "only completed requests, '
                   'which include a signature from the requesting individual, will be accepted." Corporate '
                   'sponsorship requires a Corporate Sponsorship Request Form BEFORE any sponsor is '
                   'approached.',
  'fair_url': 'https://www.buffalo.edu/studentlife/who-we-are/departments/student-unions/non-academic-event-reservations.html',
  'policy': 'Non-Academic Event Reservations — Student Unions (the operative exclusion); Sponsorship and '
            'Advertising Policy (issued 10/4/2019, updated 9/3/2020); VPSL Event Policy; Student Club and '
            'Organization University-Wide Recognition Policy. SUNY systemwide layer in Stony Brook\'s '
            'policy_key.',
  'policy_url': 'https://www.buffalo.edu/studentlife/who-we-are/departments/student-unions/non-academic-event-reservations.html',
  'policy_key': "NON-ACADEMIC EVENT RESERVATIONS — STUDENT UNIONS (buffalo.edu/studentlife/who-we-are/"
                "departments/student-unions/non-academic-event-reservations.html). ⚠⚠ THE DECISIVE SENTENCE: "
                "'NON-UNIVERSITY GROUPS MAY NOT RESERVE CLASSROOM AND GENERAL CAMPUS SPACE THROUGH THE STUDENT "
                "UNIONS.' Those interested are told to CONTACT UNIVERSITY EVENTS INSTEAD — (716) 645-6147, "
                "501 Capen Hall, ub-events@buffalo.edu. Recognised student clubs and organisations receive "
                "FIRST PRIORITY and 'can typically reserve space at no charge.' University departments may "
                "also submit. Requests must be submitted 'AT LEAST FOURTEEN BUSINESS DAYS IN ADVANCE.' 'ONLY "
                "COMPLETED REQUESTS, WHICH INCLUDE A SIGNATURE FROM THE REQUESTING INDIVIDUAL, WILL BE "
                "ACCEPTED.' CANCELLATION: organisations must notify Student Unions 'NO LATER THAN TWO BUSINESS "
                "DAYS PRIOR TO THE SCHEDULED EVENT' or face a '$30 PER SPACE CANCELLATION FEE.' Groups must "
                "read and comply with the Rental Agreement Policy before submitting. ⚠ SPECIFIC DOLLAR RATES "
                "SIT BEHIND A 'View current fee information' LINK AND ARE NOT PRINTED ON THE PAGE. "
                "SPONSORSHIP AND ADVERTISING POLICY, ISSUED OCTOBER 4, 2019, LAST UPDATED SEPTEMBER 3, 2020 "
                "(buffalo.edu/administrative-services/policy-compliance-and-internal-controls/policy/"
                "ub-policy-lib/sponsorship-advertising.html). DEFINITIONS MATTER HERE BECAUSE THEY DETERMINE "
                "TAX TREATMENT: 'SPONSORSHIP' is a 'Relationship with an entity where that entity provides "
                "money, goods, or services to the university and in return, THE ENTITY RECEIVES "
                "ACKNOWLEDGEMENT'; 'ADVERTISING' is a 'Paid service purchased by a non-university entity that "
                "includes messages that contain QUALITATIVE OR COMPARATIVE LANGUAGE, PRICE INFORMATION.' The "
                "policy distinguishes QUALIFIED sponsorship ('not taxable income to the university under UBIT "
                "provisions') from NON-QUALIFIED ('considered income to the university under the Unrelated "
                "Business Income Tax provisions') — ⚠ WHICH IS OFTEN WHAT A UNIVERSITY IS ACTUALLY OBJECTING "
                "TO WHEN IT REFUSES: a sponsorship that names a product with price information becomes "
                "advertising, and advertising is taxable income to UB. KEEP THE MESSAGE ACKNOWLEDGEMENT-SHAPED "
                "AND THE TAX PROBLEM GOES AWAY. Sponsorship and advertising must 'ALIGN WITH THE UNIVERSITY'S "
                "MISSION AND CORE VALUES' and 'be free of obscene, indecent, or profane material.' PROHIBITED: "
                "materials promoting 'FIREARMS, TOBACCO, OR ILLEGAL GOODS OR SERVICES' and those that "
                "'ridicule, exploit, demean, or marginalize persons' on protected characteristics; the "
                "university 'DOES NOT PARTNER WITH SPONSORS WHO ARE ENGAGED IN, OR HAVE A DOCUMENTED HISTORY "
                "OF, DISCRIMINATION.' ⚠ NOTE WHAT IS NOT ON THE PROHIBITED LIST: NOTHING ABOUT CRYPTOCURRENCY, "
                "FINANCIAL PRODUCTS, GAMBLING OR INVESTMENT SCHEMES. That is a small but genuine positive and "
                "it is worth quoting back. ⚠ APPROVAL LADDER — MONEY DETERMINES WHO SIGNS: under $25,000 = "
                "unit authorisation; $25,000–$50,000 = Vice President for University Advancement; OVER $50,000 "
                "= Sponsorship Advisory Committee final approval. All entities must complete the CORPORATE "
                "SPONSORSHIP REQUEST FORM BEFORE SOLICITING SPONSORS. Related: VPSL Event Policy "
                "(buffalo.edu/vpsl/policies/event-policy.html) and the Student Club and Organization "
                "University-Wide Recognition Policy. SUNY SYSTEMWIDE LAYER — Policies 5607, 5603 and the "
                "Rules for the Maintenance of Public Order (Doc 3653) — IS CARRIED IN FULL IN STONY BROOK'S "
                "policy_key; SUNY and CUNY are separate systems, do not conflate.",
  'sponsor_required': '⚠ SPONSORSHIP DOES NOT HELP AT THE UNION — non-University groups simply may not reserve '
                      'there, sponsored or not. The route is University Events, which deals with third parties '
                      'directly. Separately, a CORPORATE SPONSORSHIP arrangement (DGD giving UB money) runs '
                      'through the $25k/$50k approval ladder and requires the Corporate Sponsorship Request '
                      'Form before anyone is approached.',
  'clubs': [
    ('⚠ UB Blockchain ThinkLab — A UNIVERSITY INITIATIVE, NOT A STUDENT CLUB',
     'Do not mistake it for one. The ThinkLab "collaborates with industry and the community in shaping our '
     'future" and aims to make Buffalo "a premier blockchain education and research hub." It runs a Blockchain '
     'Buildathon and free Coursera blockchain/DeFi MOOCs. ⚠ THE SITE NAMES NO DIRECTOR AND PUBLISHES NO EMAIL '
     'OR PHONE — only a contact form. Its "Meet faculty and industry advocates" page named nobody in the '
     'fetched content. This is nonetheless the most crypto-forward institutional structure at any SUNY.',
     'https://www.buffalo.edu/ubblockchain.html'),
    ('(Student blockchain club)',
     '⚠ NONE CONFIRMED. No student blockchain or crypto organisation at UB could be found; the general clubs '
     'page does not enumerate. Given the ThinkLab exists, a student group probably does too — ask Student '
     'Unions on (716) 645-2055.',
     'https://www.buffalo.edu/news/key-issues/student-clubs-and-organizations.html'),
    ('Student Association (SA)',
     'UB\'s undergraduate student government, which charters clubs and runs Fall Fest (a concert series, not '
     'an org fair — SA cancelled the 2023 edition over space). Its events system returned only 2022 archive '
     'items to tooling.',
     'https://www.sa.buffalo.edu/component/jevents/eventdetail/11615/-/fall-fest-2022?Itemid=1047'),
  ],
  'faculty': [
    ('⚠ Amy Veiders',
     'ASSOCIATE DIRECTOR OF UNIVERSITY EVENTS — the likeliest owner of an external booking, in the office that '
     'non-University groups are explicitly directed to when the Student Unions turn them away. START HERE.',
     'UB Office of University Events, 501 Capen Hall',
     'amybeard@buffalo.edu · (716) 645-3414',
     'https://www.buffalo.edu/events/contact-us.html'),
    ('Office of University Events — main line and full staff',
     'MAIN LINE (716) 645-6147, ub-events@buffalo.edu, 501 Capen Hall. Full desk, all direct dials: Jocelyn '
     'Jakubus, Director of University and Presidential Events, (716) 645-2908 jocelynj@; Allison Giunta, '
     'Assoc. Dir. Presidential Events, (716) 645-4660 atkorta@; Emma Halstead, Asst Dir Events, '
     '(716) 645-3705 emmahals@; Sonia Marinaccio, Asst Dir Events, (716) 645-3662 smarin@; Allison '
     'Rhinebarger, Asst Dir Events, (716) 645-6843 arhineba@ — all @buffalo.edu.',
     'UB Office of University Events',
     'main line (716) 645-6147 · six direct dials listed',
     'https://www.buffalo.edu/events/contact-us.html'),
    ('⚠ N. Geoffrey Bartlett',
     'ASSISTANT VICE PRESIDENT, CORPORATE & FOUNDATION RELATIONS — THE PERSON WHO FIELDS A CORPORATE '
     'SPONSORSHIP APPROACH AT UB. If the play is money-to-the-university rather than a table, this is the '
     'first call, and note the approval ladder: under $25k is a unit decision.',
     'UB University Advancement',
     'gbartlet@buffalo.edu · (716) 881-8203',
     'https://www.buffalo.edu/administrative-services/policy-compliance-and-internal-controls/policy/ub-policy-lib/sponsorship-advertising.html'),
    ('Kathleen Heckman',
     'Vice President, University Advancement — signs off sponsorships in the $25,000–$50,000 band; above '
     '$50,000 it goes to the Sponsorship Advisory Committee.',
     'UB University Advancement',
     'kheckman@buffalo.edu · (716) 645-3725',
     'https://www.buffalo.edu/administrative-services/policy-compliance-and-internal-controls/policy/ub-policy-lib/sponsorship-advertising.html'),
    ('Student Unions · Registrar',
     'STUDENT UNIONS (716) 645-2055, 228 Student Union, North Campus — controls all club space and is the '
     'office that confirms the non-University exclusion; also the place to ask whether an org fair exists at '
     'all in Fall 2026. REGISTRAR (716) 645-5698 for the calendar. ⚠ No UB faculty member working on '
     'blockchain could be confirmed by name — the ThinkLab names nobody.',
     'University at Buffalo',
     'Student Unions (716) 645-2055 · Registrar (716) 645-5698',
     'https://www.buffalo.edu/studentlife/who-we-are/departments/student-unions/non-academic-event-reservations.html'),
  ],
  'courses': [
    ('UB Blockchain ThinkLab — Coursera blockchain and DeFi MOOCs',
     'The ThinkLab offers FREE online blockchain and decentralized-finance courses through Coursera. Not a '
     'catalog course, but it means UB has publicly committed institutional effort to blockchain education — '
     'useful framing when asking for access.',
     'https://www.buffalo.edu/ubblockchain/services/learning-opportunities/coursera_blockchain.html'),
    ('(Catalog courses)',
     '⚠ NOT CONFIRMED. No UB catalog course on blockchain, cryptocurrency or fintech could be located. Gap.',
     'https://www.buffalo.edu/ubblockchain/services/learning-opportunities.html'),
    ('(Fall 2026 offerings)',
     '⚠ NONE CONFIRMED at UB.',
     'https://www.buffalo.edu/ubblockchain.html'),
  ],
  'events': [
    ('⚠ Blockchain Buildathon (UB Blockchain ThinkLab) — LIKELY DORMANT',
     'A student build event run by the ThinkLab. ⚠ THE PAGE\'S MOST RECENT DATED INSTANCE IS JUNE 28, 2019 — '
     'treat the event as DORMANT unless confirmed otherwise. If it were revived it would be exactly the kind '
     'of student-run technical event with an open sponsorship pipeline that sidesteps campus commercial rules. '
     'Worth one email to the ThinkLab contact form to ask.',
     'https://www.buffalo.edu/ubblockchain/blockchain-buildathon.html'),
    ('(Involvement fair)',
     '⚠ NO FALL 2026 UB ORG FAIR CONFIRMED. "Fall Fest" is a concert series and SA cancelled the 2023 edition '
     'over space availability. Call (716) 645-2055.',
     'https://www.ubspectrum.com/article/2023/09/sa-cancels-2023-fall-fest'),
    ('(Corporate sponsorship route)',
     'Not an event: the Corporate Sponsorship Request Form must be completed BEFORE any sponsor is approached, '
     'and approvals ladder at $25k and $50k. Geoffrey Bartlett (716) 881-8203 is the entry point.',
     'https://www.buffalo.edu/administrative-services/policy-compliance-and-internal-controls/policy/ub-policy-lib/sponsorship-advertising.html'),
  ],
  'play': 'BUFFALO IS THE LARGEST SUNY AND THE ONLY ONE WITH A UNIVERSITY-BADGED BLOCKCHAIN INITIATIVE, WHICH '
          'MAKES IT MORE INTERESTING THAN ITS ACCESS RATING SUGGESTS. The Student Unions door is shut in '
          'terms — "non-University groups may not reserve classroom and general campus space through the '
          'Student Unions" — but the same sentence hands you the alternative, and UB\'s Office of University '
          'Events is unusually well staffed: a main line on (716) 645-6147 and six named people with direct '
          'dials. CALL AMY VEIDERS ON (716) 645-3414 FIRST; she is the Associate Director most likely to own '
          'an external booking, and no rate card is published anywhere so a quote has to be asked for. THE '
          'SECOND, POSSIBLY BETTER PLAY IS SPONSORSHIP RATHER THAN A TABLE: UB\'s Sponsorship and Advertising '
          'Policy prohibits firearms, tobacco and illegal goods and says NOTHING about cryptocurrency or '
          'financial products, and anything under $25,000 is a unit-level decision. Geoffrey Bartlett, AVP '
          'Corporate & Foundation Relations, (716) 881-8203, is the person who fields that. Keep the message '
          'ACKNOWLEDGEMENT-SHAPED rather than comparative or price-bearing — the moment it carries "qualitative '
          'or comparative language, price information" it becomes advertising and therefore taxable UBIT income '
          'to UB, which is usually the real reason a university says no. The natural partner is the UB '
          'BLOCKCHAIN THINKLAB, whose stated goal is making Buffalo "a premier blockchain education and '
          'research hub" — but it names no director and publishes no phone, and its Buildathon page has not '
          'been dated since 2019, so establish whether it is alive before building a plan on it. ⚠ Genuine '
          'gap: no Fall 2026 org fair could be confirmed to exist at UB at all. Ask Student Unions on '
          '(716) 645-2055.',
  'gaps': [
    '⚠⚠ NO UB ORG FAIR CONFIRMED FOR FALL 2026 — "Fall Fest" is a concert series, SA cancelled the 2023 '
    'edition, and the SA events system returned only 2022 archive items. Call (716) 645-2055.',
    '⚠ NO RATE CARD for non-University groups is published — the Union hides fees behind a link and University '
    'Events quotes bespoke. Get a written quote from (716) 645-3414.',
    '⚠ Is the UB Blockchain ThinkLab still active? It names NO director, publishes NO email or phone (contact '
    'form only), and its Buildathon page has no instance more recent than June 28, 2019.',
    '⚠ No student blockchain or crypto club at UB confirmed either way.',
    'No UB faculty member working on blockchain confirmed by name.',
    'No insurance requirement or dollar limit appears on the Student Unions reservation page — ask University '
    'Events what applies to a third party.',
    'The registrar\'s "Future Academic Calendars" page begins at 2027-28 and omits Fall 2026 — a navigation '
    'trap for anyone checking dates.',
  ],
  },

 # ---------------------------------------------------------------- 8. Binghamton (SUNY)
 {'state': 'New York',
  'name': 'Binghamton University',
  'city': 'Binghamton/Vestal, NY',
  'type': 'Public',
  'tier': 'B — Regional',
  'access': 3,
  'start': '⚠⚠ Tue Aug 18, 2026 — EARLIEST START IN NEW YORK, six days ahead of the next SUNY and THREE WEEKS '
           'ahead of Columbia. If a tour is planned from a September mental model, Binghamton is already '
           'weeks into term.',
  'adddrop': 'Course add/drop deadline Mon Aug 31, 2026 at 11:59 p.m.',
  'fallbreak': '⚠⚠ Sat Oct 10 – Sun Oct 18, 2026 — A FULL NINE-DAY FALL BREAK WITH THE RESIDENCE HALLS '
               'PHYSICALLY CLOSED (halls close 10 a.m. Oct 10, reopen 2 p.m. Oct 18). THE CAMPUS EMPTIES. '
               'This is not a two-day SUNY breather like Stony Brook or Buffalo — DO NOT SCHEDULE INTO '
               'OCT 10–18.',
  'thanksgiving': 'Wed Nov 25 – Sun Nov 29, 2026 (halls close 10 a.m. Nov 25, reopen 2 p.m. Nov 29)',
  'lastclass': 'Tue Dec 8, 2026. Reading day Wed Dec 9.',
  'finals': 'Thu–Fri Dec 10–11 and Mon–Wed Dec 14–16, 2026. Halls close 10 a.m. Thu Dec 17 (late stays to '
            'Dec 19).',
  'cal_url': 'https://www.binghamton.edu/academics/academic-calendar.html',
  'cal_status': 'CONFIRMED — university academic calendar with residence-hall open/close times attached to '
                'every break, which is how the nine-day fall break was verified as a genuine emptying rather '
                'than a no-class period. The registrar\'s own calendar page rendered only four August items '
                'to tooling.',
  'fair': 'University Fest (U-Fest) — 250+ recognised student organisations, 40 fraternities and sororities, '
          'campus recreation, athletics, university departments AND EXTERNAL VENDORS',
  'fair_date': '⚠⚠ STALE-PAGE WARNING — DATE UNVERIFIED. The page says "August 22, 11 a.m. – 3 p.m., Peace '
               'Quad" WITH NO YEAR. AUGUST 22, 2026 IS A SATURDAY; August 22, 2025 was a Friday. Binghamton\'s '
               'Fall 2026 term begins Tuesday August 18, which would put a Saturday-of-week-one fair at an odd '
               'remove from move-in. TREAT AS CARRIED OVER FROM 2025 AND CONFIRM BEFORE TRAVELLING — email '
               'evp@binghamtonsa.org. Student-organisation slots were described as FULL WITH A WAITLIST.',
  'fair_outside': '⚠ YES — ONE OF ONLY TWO CONFIRMED "YES" ANSWERS IN NEW YORK, WITH A CAVEAT. Verbatim: '
                  '"VENDORS FROM ALL OVER THE BINGHAMTON, VESTAL AND JOHNSON CITY AREA WILL BE ON CAMPUS." '
                  '⚠ NOTE THE GEOGRAPHIC LIMITER — that reads as a LOCAL-BUSINESS tier, not a general '
                  'commercial one, and a national crypto issuer is not obviously what the sentence '
                  'contemplates. ASK EXPLICITLY.',
  'fair_cost': 'U-Fest cost not published. ⚠ The known figure is the Union\'s: "External organizations must be '
               'sponsored by a University recognized department or student organization and MAY BE SUBJECT TO '
               'A $75 VENDOR FEE." That $75 is the cheapest published outside-entity figure in New York after '
               'RIT\'s $60 table.',
  'fair_deadline': 'U-Fest deadline not published (slots already full with a waitlist). Union deadlines: '
                   'OUTDOOR TABLING AT LEAST 15 BUSINESS DAYS PRIOR; outdoor logistics 10 business days, or 20 '
                   'business days where extra campus support is needed; large events require meeting Catherine '
                   'Faughnan at least THREE WEEKS prior; catering two weeks.',
  'fair_url': 'https://www.binghamton.edu/campus-activities/events/ufest/index.html',
  'policy': 'Policy 203 "Business and Commercial Activities on Campus" (last revised 10/20/2025) — the '
            'campus-wide prohibition; plus The Union Reservation Guidelines — the narrow priced exception',
  'policy_url': 'https://www.binghamton.edu/operations/policies/policy-203.html',
  'policy_key': "⚠ TWO BINGHAMTON DOCUMENTS POINT OPPOSITE DIRECTIONS AND AN AMBASSADOR NEEDS BOTH. "
                "(1) POLICY 203, 'BUSINESS AND COMMERCIAL ACTIVITIES ON CAMPUS,' LAST REVISED 10/20/2025 "
                "(binghamton.edu/operations/policies/policy-203.html) — THE PROHIBITION: '⚠⚠ IT IS THE POLICY "
                "OF THE STATE UNIVERSITY OF NEW YORK (UNIVERSITY) THAT NO AUTHORIZATION WILL BE GIVEN TO "
                "PRIVATE COMMERCIAL ENTERPRISES TO OPERATE ON UNIVERSITY CAMPUSES' — except for specific "
                "authorised services: food, beverages, bookstore, vending, banking and cultural events. "
                "Written advance approval is required from the DIRECTOR OF PROCUREMENT for business activities "
                "on campus, or from the DIRECTOR OF THE UNIVERSITY UNION for University Union facilities. "
                "'DOOR-TO-DOOR SOLICITATION IS PROHIBITED.' 'UNADDRESSED HANDBILLS PROMOTING GOODS OR SERVICES "
                "CANNOT BE DISTRIBUTED.' 'COMMERCIAL VENDORS CANNOT PARTICIPATE IN CRAFT FAIRS OR FLEA "
                "MARKETS.' Permitted advertising channels are only: University publications and event "
                "programs; University bulletin boards (via the Director of the University Union); and campus "
                "mail service, UNADDRESSED advertising only. NO PHONE NUMBERS ARE PRINTED IN THE POLICY. "
                "⚠ SOURCING NOTE: that opening sentence attributes itself to SUNY, but the exact string "
                "returns ONLY Binghamton in search — I COULD NOT LOCATE ITS SOURCE DOCUMENT ON suny.edu. TREAT "
                "IT AS AUTHORITATIVE AT BINGHAMTON AND AS A STRONG INDICATOR OF SUNY POSTURE ELSEWHERE, BUT DO "
                "NOT CITE IT AS 'SUNY POLICY' TO ANOTHER SUNY CAMPUS — make them name their own document. "
                "(2) THE UNION — RESERVATION GUIDELINES (binghamton.edu/services/union/events-and-reservations/"
                "reservation-guidelines.html) — THE EXCEPTION: 'S.A. chartered organizations, "
                "University-recognized Greek groups, department recognized student groups, faculty and staff "
                "are permitted to make room reservations' via the B There system, and the same list applies to "
                "TABLING reservations. ⚠ THE ROUTE, VERBATIM: 'EXTERNAL ORGANIZATIONS MUST BE SPONSORED BY A "
                "UNIVERSITY RECOGNIZED DEPARTMENT OR STUDENT ORGANIZATION AND MAY BE SUBJECT TO A $75 VENDOR "
                "FEE.' ⚠⚠ ANTI-FRONTING — EXPLICIT AND WITH A PENALTY ON THE SPONSOR: 'GROUPS MAY NOT HOLD "
                "RESERVATIONS FOR OTHER GROUPS. IF YOU ARE FOUND TO BE HOLDING A RESERVATION FOR ANOTHER "
                "GROUP, BOTH GROUPS WILL RISK LOSING B THERE REQUEST ACCESS.' The sponsoring club must "
                "genuinely be running the event — a club that books a room and hands it to DGD loses its "
                "booking privileges, which is a real cost to a real student group. DEADLINES: meet CATHERINE "
                "FAUGHNAN at least THREE WEEKS prior for large events; outdoor logistics AT LEAST TEN BUSINESS "
                "DAYS, or TWENTY BUSINESS DAYS where additional campus support is needed; OUTDOOR TABLING AT "
                "LEAST 15 BUSINESS DAYS PRIOR; Dining Services two weeks for catering. ⚠ NO INSURANCE "
                "REQUIREMENT IS STATED ON THIS PAGE — verify rather than assume. THE UNION FAQ NARROWS IT "
                "FURTHER (binghamton.edu/services/union/events-and-reservations/faq.html): 'EXTERNAL VENDORS "
                "MAY BE APPROVED TO PARTICIPATE IN THE FACILITATION OF EVENTS, BUT ATTENDEES ARE LIMITED TO "
                "ON-CAMPUS PARTICIPANTS ONLY.' ⚠⚠ HOW TO READ THE CONFLICT: Policy 203 bars private commercial "
                "enterprises from OPERATING on campus; the Union creates a narrow, priced, sponsored exception "
                "for vendor PARTICIPATION IN A SPONSORED EVENT, confined to on-campus attendees. THE HONEST "
                "READ IS THAT A SPONSORED $75 VENDOR TABLE AT A CLUB-RUN EVENT IS AVAILABLE AND AN INDEPENDENT "
                "DGD COMMERCIAL PRESENCE IS NOT. SUNY systemwide layer (Policies 5607, 5603, Doc 3653) is "
                "carried in full in STONY BROOK'S policy_key.",
  'sponsor_required': '⚠ YES — MANDATORY AND POLICED. "External organizations must be sponsored by a '
                      'University recognized department or student organization and may be subject to a $75 '
                      'vendor fee." And the sponsor cannot be a shell: "Groups may not hold reservations for '
                      'other groups... BOTH GROUPS WILL RISK LOSING B THERE REQUEST ACCESS." The club must '
                      'genuinely run the event.',
  'clubs': [
    ('⚠ 250+ S.A.-chartered organisations — directory NOT enumerable',
     'Binghamton runs its org directory on CampusGroups (referenced by U-Fest for giveaways and raffles) and '
     'it was not readable to tooling. NO blockchain, crypto or fintech club at Binghamton could be confirmed '
     'either way. The School of Management is the likeliest home. Ask the Student Association at '
     'evp@binghamtonsa.org.',
     'https://www.binghamton.edu/campus-activities/events/ufest/index.html'),
    ('Student Association (SA)',
     'Charters all 250+ organisations and RUNS U-FEST, including its external-vendor tier. The Executive Vice '
     'President is the named U-Fest contact — evp@binghamtonsa.org. This is the office to ask both "is there a '
     'blockchain club" and "does the vendor tier admit a non-local company."',
     'https://www.binghamton.edu/campus-activities/plan/'),
    ('(Where to look next)',
     'The School of Management and the computer science department are the two places a crypto group would '
     'sit. Campus Activities handles event planning for all of them.',
     'https://www.binghamton.edu/campus-activities/plan/reservations.html'),
  ],
  'faculty': [
    ('⚠ Catherine Faughnan',
     'ASSISTANT DIRECTOR, THE UNION — the named person you MUST meet at least three weeks before any large '
     'event, and therefore the gatekeeper for the $75 sponsored-vendor route. ⚠ NO DIRECT PHONE IS PUBLISHED '
     'ANYWHERE; email only. Start with her, then ask her for the Director of the University Union by name.',
     'The Union, Binghamton University',
     'cfaughn@binghamton.edu · no phone published',
     'https://www.binghamton.edu/services/union/events-and-reservations/reservation-guidelines.html'),
    ('Union Catering',
     '⚠ THE ONLY PHONE NUMBER PRINTED ANYWHERE ON THE UNION\'S RESERVATION GUIDELINES PAGE. Not the right '
     'office, but it is a live line into the building and can transfer you. Recorded here because Binghamton '
     'publishes almost no numbers.',
     'Binghamton University Dining Services',
     '(607) 777-2925',
     'https://www.binghamton.edu/services/union/events-and-reservations/reservation-guidelines.html'),
    ('Director of Procurement · Director of the University Union',
     '⚠ THE TWO APPROVAL AUTHORITIES NAMED IN POLICY 203 — Procurement for business activities anywhere on '
     'campus, the Union Director for Union facilities. ⚠⚠ NEITHER IS NAMED BY PERSON AND NEITHER HAS A '
     'PUBLISHED PHONE. ASK FOR THEM BY TITLE. Without one of these two signatures, Policy 203 says no '
     'authorisation exists at all.',
     'Binghamton University',
     'no numbers published — ask for them by title',
     'https://www.binghamton.edu/operations/policies/policy-203.html'),
    ('Student Association Executive Vice President',
     'Owns U-Fest and its external-vendor tier. The person to ask whether "vendors from all over the '
     'Binghamton, Vestal and Johnson City area" is a geographic restriction or just a description, and '
     'whether the August 22 date is 2025 carryover.',
     'Binghamton University Student Association',
     'evp@binghamtonsa.org · no phone published',
     'https://www.binghamton.edu/campus-activities/events/ufest/index.html'),
    ('The Union — general enquiries',
     'bengaged@binghamton.edu for anything the FAQ does not cover; the Union contact page is where a direct '
     'number should be obtainable. ⚠ No Binghamton faculty member working on blockchain or digital assets '
     'could be confirmed — the School of Management is where to look.',
     'The Union, Binghamton University',
     'bengaged@binghamton.edu · no number published — look up here',
     'https://www.binghamton.edu/services/union/'),
  ],
  'courses': [
    ('(Courses)',
     '⚠ NOT CONFIRMED. No Binghamton catalog course on blockchain, cryptocurrency or fintech could be located. '
     'The School of Management is the likeliest home. Gap.',
     'https://www.binghamton.edu/academics/academic-calendar.html'),
    ('(Fall 2026 offerings)',
     '⚠ NONE CONFIRMED at Binghamton.',
     'https://www.binghamton.edu/academics/academic-calendar.html'),
    ('(Audience note)',
     'Binghamton is the most academically selective SUNY and its School of Management places heavily into New '
     'York finance — a strong audience on paper, entirely unverified in this packet.',
     'https://www.binghamton.edu/campus-activities/plan/'),
  ],
  'events': [
    ('⚠ University Fest (U-Fest) — Peace Quad, 11 a.m.–3 p.m.',
     '⚠⚠ DATE SUSPECT: the page says "August 22" with NO YEAR and Aug 22, 2026 is a SATURDAY (term starts Tue '
     'Aug 18). Probably carried over from 2025. But the substance is real and rare: 250+ student '
     'organisations, 40 Greek chapters, campus rec, athletics, departments AND EXTERNAL VENDORS — "vendors '
     'from all over the Binghamton, Vestal and Johnson City area will be on campus." Student performances, '
     'inflatables, free food, giveaways and raffles via CampusGroups. CONFIRM THE DATE AND THE VENDOR '
     'ELIGIBILITY AT evp@binghamtonsa.org.',
     'https://www.binghamton.edu/campus-activities/events/ufest/index.html'),
    ('Sponsored $75 vendor table at a club-run Union event',
     'The compliant year-round mechanism rather than a dated event. Requires a genuine sponsoring department '
     'or student org (fronting costs BOTH groups their booking access), 15 business days for outdoor tabling, '
     'and a meeting with Catherine Faughnan three weeks out for anything large.',
     'https://www.binghamton.edu/services/union/events-and-reservations/reservation-guidelines.html'),
    ('(Blockchain-specific events)',
     '⚠ NONE CONFIRMED at Binghamton.',
     'https://www.binghamton.edu/campus-activities/plan/'),
  ],
  'play': 'BINGHAMTON IS THE CALENDAR OUTLIER OF NEW YORK AND THE TWO DATES ARE THE WHOLE STORY. It starts '
          'TUESDAY AUGUST 18 — six days before any other SUNY and three weeks before Columbia — and then it '
          'CLOSES ITS RESIDENCE HALLS FOR NINE DAYS from October 10 to 18, so the campus physically empties '
          'mid-term. Get there in the last week of August or the last week of September; October 10–18 is '
          'worthless. On access, Binghamton contradicts itself and you need both halves. Policy 203 declares '
          'that "NO AUTHORIZATION WILL BE GIVEN TO PRIVATE COMMERCIAL ENTERPRISES TO OPERATE ON UNIVERSITY '
          'CAMPUSES" and bans door-to-door solicitation and unaddressed handbills outright. But the Union\'s '
          'own reservation guidelines create a narrow, priced exception: "External organizations must be '
          'sponsored by a University recognized department or student organization and may be subject to a $75 '
          'VENDOR FEE" — the cheapest published outside-entity figure in New York after RIT. THE SPONSOR MUST '
          'BE REAL: "Groups may not hold reservations for other groups... BOTH GROUPS WILL RISK LOSING B THERE '
          'REQUEST ACCESS," so a club that fronts for DGD loses its own booking privileges, which is a real '
          'cost you should not ask a student group to bear. THE SINGLE BEST DOOR IS CATHERINE FAUGHNAN, '
          'Assistant Director of the Union — cfaughn@binghamton.edu, no phone published, meet her three weeks '
          'before anything large. Ask her for the Director of the University Union by title, because Policy '
          '203 makes that person one of only two people who can authorise a commercial activity at all. '
          'Separately, email evp@binghamtonsa.org about U-Fest: it genuinely admits external vendors, which '
          'almost no fair in New York does, but the page says "vendors from all over the Binghamton, Vestal '
          'and Johnson City area" — find out whether that is a geographic restriction — and the printed date '
          '"August 22" carries no year and falls on a Saturday in 2026, so it is probably 2025 carryover.',
  'gaps': [
    '⚠⚠ U-FEST DATE IS PROBABLY STALE. The page prints "August 22" with no year; Aug 22, 2026 is a SATURDAY '
    'and term starts Tue Aug 18. Confirm at evp@binghamtonsa.org before travelling.',
    '⚠ Does U-Fest\'s external-vendor tier admit a NON-LOCAL company? The page says "vendors from all over the '
    'Binghamton, Vestal and Johnson City area."',
    '⚠ NO PHONE NUMBER for the Union, Campus Activities, Catherine Faughnan, the Director of Procurement or '
    'the Director of the University Union. The ONLY number printed on the reservation guidelines page is '
    'Catering (607) 777-2925. Get a real one at binghamton.edu/services/union/contact.html',
    '⚠ Policy 203\'s opening sentence attributes itself to SUNY but its source document COULD NOT BE LOCATED '
    'on suny.edu. Do not cite it as SUNY policy to another SUNY campus.',
    '⚠ Is the $75 vendor fee actually charged, and does it cover a table at U-Fest or only a Union event? '
    '"May be subject to" is doing a lot of work in that sentence.',
    'No insurance requirement or limit is stated on the Union reservation page — verify.',
    'The 250+ club directory (CampusGroups) is not enumerable — no blockchain or crypto club confirmed.',
    'No Binghamton faculty member or catalog course on blockchain confirmed.',
  ],
  },

 # ---------------------------------------------------------------- 9. Albany (SUNY)
 {'state': 'New York',
  'name': 'University at Albany',
  'city': 'Albany, NY',
  'type': 'Public',
  'tier': 'C — Opportunistic',
  'access': 3,
  'start': 'Mon Aug 24, 2026',
  'adddrop': 'Last day to add semester-length classes without permission Mon Aug 31, 2026. Last day to drop '
             'without a "W" Fri Sep 4, 2026.',
  'fallbreak': 'Mon–Tue Oct 12–13, 2026 — standard SUNY two-day break.',
  'thanksgiving': 'Wed Nov 25 – Sun Nov 29, 2026',
  'lastclass': 'Mon Dec 7, 2026. Reading day Tue Dec 8.',
  'finals': 'Wed Dec 9 – Tue Dec 15, 2026. Degree conferral Sat Dec 19.',
  'cal_url': 'https://www.albany.edu/registrar/academic-calendar',
  'cal_status': 'CONFIRMED — registrar academic calendar. ⚠ NAVIGATION TRAP: the "Future Academic Calendars" '
                'page (albany.edu/registrar/academic-calendar/future-calendars) BEGINS AT FALL 2027 and '
                'contains no Fall 2026 dates. Registrar / main line (518) 442-3300.',
  'fair': '⚠ NO UALBANY INVOLVEMENT FAIR COULD BE CONFIRMED FOR FALL 2026. Tabling at UAlbany is a standing '
          'facility rather than a single annual event.',
  'fair_date': '⚠ UNVERIFIED — no Fall 2026 UAlbany org fair date exists in any indexed page. Three standing '
               'tabling locations exist instead: the GREAT HALL (ground level), the CAMPUS CENTER LOBBY '
               '(Podium level), and the AREA AROUND THE SMALL FOUNTAIN (weather permitting). Call Student '
               'Engagement & Belonging via (518) 442-3300.',
  'fair_outside': '⚠⚠ NO — THE EXCLUSION IS EXPLICIT AND IT IS THE DECISIVE FACT AT UALBANY. The three '
                  'tabling spaces are "RESTRICTED TO RECOGNIZED STUDENT ORGANIZATIONS, UNIVERSITY DEPARTMENTS '
                  'OR OFFICES." Non-affiliated entities "MUST OBTAIN A REVOCABLE PERMIT FROM THE OFFICE OF '
                  'THE CONTROLLER." Separately, Policy 1.6 gives third parties a FREE designated public forum '
                  '— but it is cross-referenced to SUNY\'s NON-COMMERCIAL facilities policy, so it is not for '
                  'DGD. See policy_key.',
  'fair_cost': '⚠ TWO DIFFERENT ANSWERS. Policy 1.6 public forum: the institution "CANNOT CHARGE APPLICATION '
               'FEES, USAGE FEES, INSURANCE REQUIREMENTS, OR SECURITY COSTS to third-party speakers" — the '
               'only fee-free, insurance-free third-party route found anywhere in New York, and it is for '
               'non-commercial expression. Campus Center commercial route: revocable permit from the Office of '
               'the Controller, NO RATE PUBLISHED. Ballroom cancellation inside 10 business days incurs a fee, '
               'amount not published.',
  'fair_deadline': '⚠ THREE BUSINESS DAYS for the Policy 1.6 public forum — applications to the Office of '
                   'Facilities Management, and the university "shall review the application and respond to '
                   'the applicant no later than the close of business on the third business day prior."',
  'fair_url': 'https://www.albany.edu/student-engagement-belonging/campus-center/reserve-our-facilities',
  'policy': 'Policy 1.6 "Public Forum: Time, Manner and Place Rules" (adopted 7/11/2019, amended 8/17/2023); '
            'Campus Center Reserve Our Facilities; Freedom of Speech and Expressive Activities. SUNY '
            'systemwide layer in Stony Brook\'s policy_key.',
  'policy_url': 'https://www.albany.edu/risk-management-compliance/policy/public-forum-time-manner-and-place-rules',
  'policy_key': "⚠ UALBANY IS THE MOST INTERESTING BIFURCATION IN NEW YORK: IT GIVES THIRD PARTIES A FREE "
                "PUBLIC FORUM AND SHUTS THEM OUT OF TABLING. "
                "CAMPUS CENTER — RESERVE OUR FACILITIES (albany.edu/student-engagement-belonging/campus-center/"
                "reserve-our-facilities): 'RECOGNIZED STUDENT ORGANIZATIONS AND UNIVERSITY DEPARTMENTS OR "
                "OFFICES can reserve Campus Center facilities and/or tabling space using the University's "
                "Event Management System (EMS).' ⚠⚠ THE EXCLUSION: three information-table locations exist — "
                "the Great Hall (ground level), the Campus Center lobby (Podium level), and the area around "
                "the small fountain (weather permitting) — and these spaces are 'RESTRICTED TO RECOGNIZED "
                "STUDENT ORGANIZATIONS, UNIVERSITY DEPARTMENTS OR OFFICES.' ⚠ THE EXTERNAL ROUTE: "
                "'NON-AFFILIATED ENTITIES MUST OBTAIN A REVOCABLE PERMIT FROM THE OFFICE OF THE CONTROLLER.' "
                "⚠ QUIET ANTI-FRONTING: student groups may designate up to two reservation coordinators, and "
                "'FACULTY ADVISORS CANNOT REQUEST SPACE ON BEHALF OF ORGANIZATIONS' — the person booking must "
                "be a student officer, not a proxy. MONEY: 'IF YOU CANCEL A BALLROOM RESERVATION LESS THAN 10 "
                "BUSINESS DAYS FROM THE DATE OF YOUR EVENT, YOU WILL BE CHARGED A CANCELLATION FEE' — amount "
                "not published. "
                "POLICY 1.6, 'PUBLIC FORUM: TIME, MANNER AND PLACE RULES,' ADOPTED JULY 11, 2019, AMENDED "
                "AUGUST 17, 2023 (albany.edu/risk-management-compliance/policy/public-forum-time-manner-and-"
                "place-rules): third parties apply to the OFFICE OF FACILITIES MANAGEMENT AT LEAST THREE "
                "BUSINESS DAYS before the intended date, and the university 'SHALL REVIEW THE APPLICATION AND "
                "RESPOND TO THE APPLICANT NO LATER THAN THE CLOSE OF BUSINESS ON THE THIRD BUSINESS DAY PRIOR' "
                "to the requested date. ⚠⚠ THE STANDOUT PROVISION — THE ONLY ONE OF ITS KIND IN THIS PACKET: "
                "THE INSTITUTION CANNOT CHARGE APPLICATION FEES, USAGE FEES, INSURANCE REQUIREMENTS, OR "
                "SECURITY COSTS TO THIRD-PARTY SPEAKERS USING THE FORUM. Third parties must remove their own "
                "materials; MEGAPHONE AMPLIFICATION IS PROHIBITED but the university will provide a microphone "
                "and sound system on written request. ⚠ BLACKOUT PERIODS: 'the forum closes during OPENING "
                "WEEKEND, EXAM PERIODS, GRADUATION ACTIVITIES, AND MAJOR CAMPUS CELEBRATIONS LIKE HOMECOMING' "
                "— for Fall 2026 that removes roughly Aug 21–23 and Dec 9–15 at minimum. "
                "FREEDOM OF SPEECH AND EXPRESSIVE ACTIVITIES (albany.edu/about-ualbany/freedom-of-speech): "
                "'As a public entity partially funded by NYS tax dollars the University will' provide A "
                "DESIGNATED PUBLIC FORUM TO NON-UALBANY COMMUNITY MEMBERS. ⚠⚠ THE CATCH, AND IT IS THE WHOLE "
                "BALLGAME: third parties must follow Policy 1.6 PLUS the policies on camping, chalking, "
                "prohibited items at events, exterior posting, photography/filming, AND 'SUNY FACILITY USE BY "
                "NON-COMMERCIAL ORGANIZATIONS' — i.e. SUNY POLICY 5603, WHICH BY ITS TERMS COVERS "
                "NOT-FOR-PROFIT, GOVERNMENTAL, CHARITABLE, CIVIC AND RELIGIOUS GROUPS. UALBANY'S FREE "
                "THIRD-PARTY FORUM IS FOR NON-COMMERCIAL EXPRESSION. DGD DOES NOT QUALIFY FOR IT, AND THE "
                "HONEST POSTURE IS THE REVOCABLE PERMIT FROM THE CONTROLLER. ⚠ BUT KNOW 1.6 VERBATIM ANYWAY, "
                "BECAUSE A STUDENT ADVOCATE DISTRIBUTING DGD LITERATURE AS PERSONAL EXPRESSION IS A MATERIALLY "
                "DIFFERENT ACTOR FROM DGD-THE-ISSUER, AND 1.6 IS GENEROUS TO THAT STUDENT. Also on file: "
                "Freedom of Expression policy (albany.edu/risk-management-compliance/policy/freedom-expression) "
                "and the student-organisation policies at albany.edu/involvement/policies.shtml. ⚠ THE "
                "PREVIOUSLY INDEXED CAMPUS CENTER TABLING PAGE (albany.edu/events/campus_center_tabling.php) "
                "NOW RETURNS HTTP 404. SUNY systemwide layer is carried in STONY BROOK'S policy_key.",
  'sponsor_required': '⚠ EFFECTIVELY YES FOR TABLING — the three table locations are restricted to recognised '
                      'student organisations and university departments, and a faculty adviser cannot even '
                      'book on a club\'s behalf. For DGD as an entity the answer is a revocable permit from '
                      'the Office of the Controller, not sponsorship.',
  'clubs': [
    ('(Blockchain / crypto / fintech club)',
     '⚠ NONE CONFIRMED. No UAlbany blockchain, cryptocurrency or fintech student organisation could be found '
     'on any indexed page. UAlbany has a School of Business and a strong public-administration profile; the '
     'student-organisation policies page is the entry point. Genuine gap.',
     'https://albany.edu/involvement/policies.shtml'),
    ('Student Engagement & Belonging',
     'The office that administers recognised student organisations and the EMS reservation system. Registration '
     'questions go here. This is who can tell you whether any relevant club exists.',
     'https://www.albany.edu/student-engagement-belonging/campus-center/reserve-our-facilities'),
    ('(Audience note)',
     'UAlbany is the smallest-upside campus in this packet on current evidence — no confirmed club, no '
     'confirmed faculty, no confirmed course, and a tabling regime that excludes outsiders by name. Treat as '
     'opportunistic only.',
     'https://www.albany.edu/registrar/academic-calendar'),
  ],
  'faculty': [
    ('⚠ Stacy Stern, Office of Facilities Management',
     'THE NAMED HUMAN WHO PROCESSES THE THIRD-PARTY PUBLIC-FORUM APPLICATION, and the number is printed on '
     'Policy 1.6 itself. Even though the free forum is for non-commercial expression, this is the office that '
     'will tell you precisely where the line sits and who at the Controller\'s office issues a commercial '
     'permit. 1400 Washington Avenue, SBA. ⚠ The email on the page is obfuscated/placeholder.',
     'UAlbany Office of Facilities Management',
     '(518) 442-3400 · email obfuscated on the page',
     'https://www.albany.edu/risk-management-compliance/policy/public-forum-time-manner-and-place-rules'),
    ('Office of the Controller',
     '⚠ THE OFFICE THAT ISSUES REVOCABLE PERMITS TO NON-AFFILIATED ENTITIES — i.e. THE ONLY LAWFUL ROUTE FOR '
     'DGD AT UALBANY — AND NO PHONE NUMBER IS PUBLISHED FOR IT ANYWHERE. The Campus Center page names it '
     'without contact details. Route via the main line and ask by title. This is the single most important '
     'gap at this campus.',
     'University at Albany',
     'no number published — look up here, or route via (518) 442-3300',
     'https://www.albany.edu/student-engagement-belonging/campus-center/reserve-our-facilities'),
    ('University at Albany — main line',
     'MAIN LINE, and also the Registrar\'s published number. Use it to reach the Office of the Controller and '
     'Student Engagement & Belonging, neither of which publishes a direct line. 1400 Washington Avenue.',
     'University at Albany',
     '(518) 442-3300 (main line)',
     'https://www.albany.edu/about-ualbany/freedom-of-speech'),
    ('UAlbany Community Led Expressive Activity form',
     'The notification form referenced by the freedom-of-speech policy for campus-community expressive '
     'activity. Relevant only to a STUDENT advocate, not to DGD as an entity — but that distinction is exactly '
     'where UAlbany\'s generous Policy 1.6 becomes usable.',
     'University at Albany',
     'web form — no phone',
     'https://forms.office.com/r/JXH6zw3pj0'),
    ('(Faculty)',
     '⚠ NOT CONFIRMED — no UAlbany faculty member working on blockchain, cryptocurrency, fintech or digital '
     'assets could be found on a live page. Look up in the School of Business and Economics directories.',
     'University at Albany',
     'no number published — look up here',
     'https://www.albany.edu/registrar/academic-calendar'),
  ],
  'courses': [
    ('(Courses)',
     '⚠ NOT CONFIRMED. No UAlbany catalog course on blockchain, cryptocurrency or fintech could be located. '
     'Gap.',
     'https://www.albany.edu/registrar/academic-calendar'),
    ('(Fall 2026 offerings)',
     '⚠ NONE CONFIRMED at UAlbany.',
     'https://www.albany.edu/registrar/academic-calendar'),
    ('(Where to look)',
     'UAlbany\'s School of Business and its Economics department are the two plausible homes. Nothing verified.',
     'https://albany.edu/involvement/policies.shtml'),
  ],
  'events': [
    ('Policy 1.6 designated public forum — 3 business days, no fee, no insurance',
     '⚠ THE MECHANISM, NOT AN EVENT, AND IT IS FOR NON-COMMERCIAL SPEECH. Genuinely remarkable terms: no '
     'application fee, no usage fee, no insurance requirement, no security cost, three business days\' notice, '
     'microphone provided on written request. BLACKOUTS: opening weekend, exam periods, graduation, '
     'Homecoming. Apply to Stacy Stern (518) 442-3400.',
     'https://www.albany.edu/risk-management-compliance/policy/public-forum-time-manner-and-place-rules'),
    ('(Involvement fair)',
     '⚠ NO UALBANY FALL 2026 ORG FAIR CONFIRMED. Standing tabling in the Great Hall, Campus Center lobby and '
     'the fountain area is the alternative — but all three are closed to non-affiliates.',
     'https://www.albany.edu/student-engagement-belonging/campus-center/reserve-our-facilities'),
    ('(Blockchain-specific events)',
     '⚠ NONE CONFIRMED at UAlbany.',
     'https://www.albany.edu/about-ualbany/freedom-of-speech'),
  ],
  'play': 'ALBANY IS A ONE-PHONE-CALL CAMPUS AND PROBABLY A SKIP UNLESS SOMETHING ELSE BRINGS YOU TO THE '
          'CAPITAL REGION. Nothing is confirmed here — no blockchain club, no faculty member, no course, no '
          'involvement fair — and the tabling regime excludes outsiders by name: the Great Hall, the Campus '
          'Center lobby and the fountain area are "RESTRICTED TO RECOGNIZED STUDENT ORGANIZATIONS, UNIVERSITY '
          'DEPARTMENTS OR OFFICES," while "non-affiliated entities must obtain a revocable permit from the '
          'OFFICE OF THE CONTROLLER" — an office for which UAlbany publishes no phone number at all. THE ONE '
          'GENUINELY VALUABLE THING HERE IS POLICY 1.6, and it is worth reading even though DGD cannot use it '
          'directly. UAlbany gives third-party speakers a designated public forum on three business days\' '
          'notice with NO application fee, NO usage fee, NO insurance requirement and NO security cost — the '
          'only terms like that anywhere in New York — and it will supply a microphone on written request. '
          'The catch is that the freedom-of-speech page cross-references it to SUNY\'s NON-COMMERCIAL '
          'facilities policy (5603), so DGD-the-issuer does not qualify. BUT A STUDENT ADVOCATE HANDING OUT '
          'DGD LITERATURE AS PERSONAL EXPRESSION IS A DIFFERENT ACTOR ENTIRELY, and 1.6 is generous to that '
          'student. So the play, if there is one, is to recruit a student and stay out of it. Make one call: '
          'Stacy Stern at the Office of Facilities Management, (518) 442-3400, printed on Policy 1.6 itself. '
          'Ask her exactly where the commercial line falls and who at the Controller\'s office issues a '
          'permit. If the answer is unpromising, spend the day at Binghamton or on Long Island instead. Avoid '
          'the forum blackout periods: opening weekend and Dec 9–15.',
  'gaps': [
    '⚠⚠ NO PHONE NUMBER for the OFFICE OF THE CONTROLLER — the only office that can issue DGD a permit at '
    'UAlbany. Route via (518) 442-3300 and ask by title. This is the blocking gap here.',
    '⚠ Does Policy 1.6\'s fee-free public forum exclude commercial speakers outright, or only condition them? '
    'The cross-reference to SUNY 5603 (non-commercial organisations) implies exclusion. Confirm with Stacy '
    'Stern (518) 442-3400.',
    '⚠ NO Fall 2026 UAlbany involvement fair confirmed to exist.',
    '⚠ NO UAlbany blockchain, crypto or fintech club confirmed.',
    '⚠ NO UAlbany faculty member or catalog course on blockchain/digital assets confirmed.',
    'Ballroom cancellation fee amount not published (charged inside 10 business days).',
    'The previously indexed Campus Center tabling page now returns HTTP 404 — '
    'https://www.albany.edu/events/campus_center_tabling.php',
    'The registrar\'s "Future Academic Calendars" page begins at Fall 2027 and omits Fall 2026.',
  ],
  },

 # ---------------------------------------------------------------- 10. Cornell
 {'state': 'New York',
  'name': 'Cornell University',
  'city': 'Ithaca, NY',
  'type': 'Private',
  'tier': 'A — Named target',
  'access': 2,
  'start': 'Mon Aug 24, 2026 — first-year writing seminar, project session, full, regular and 7-week-1 '
           'instruction all begin. Add/drop OPENS earlier, staggered Aug 17–21 by class level.',
  'adddrop': 'Fri Sep 8, 2026 for regular session and first-year writing seminars.',
  'fallbreak': 'Sat Oct 10 – Tue Oct 13, 2026 — no classes. A four-day break, longer than the SUNY two-day '
               'norm but nothing like Binghamton\'s nine-day hall closure.',
  'thanksgiving': 'Wed Nov 25 – Sun Nov 29, 2026 — no classes',
  'lastclass': 'Mon Dec 7, 2026 (regular session, first-year writing, project sessions). Study days '
               'Dec 8–10.',
  'finals': 'Fri Dec 11 – Sat Dec 19, 2026. Term ends Dec 19.',
  'cal_url': 'https://registrar.cornell.edu/calendars-exams/academic-calendar',
  'cal_status': 'CONFIRMED — Cornell registrar 2026-2027 academic calendar.',
  'fair': 'ClubFest — "registered undergraduate student organizations"',
  'fair_date': '⚠ CONFIRMED FOR FALL 2026: SATURDAY SEPTEMBER 5, 2026, on the ARTS QUAD (Barton Hall is the '
               'rain venue). SESSION ONE 12:00–1:30 PM, SESSION TWO 2:00–4:00 PM — organisations '
               'self-identify their category and are assigned to one session, so the population turns over '
               'halfway through. ⚠ ClubFest runs BOTH semesters and is weather-sensitive: the January 2026 '
               'spring edition was moved forward a day for a winter storm warning.',
  'fair_outside': '⚠⚠ NO — AND IT IS THE FLATTEST BAN IN NEW YORK. The event admits "registered undergraduate '
                  'student organizations." Separately and decisively, Cornell\'s tabling policy states: '
                  '"OUTSIDE ORGANIZATIONS/VENDORS/BUSINESSES ARE NOT PERMITTED TO CONDUCT BUSINESS ON CAMPUS, '
                  'INCLUDING TABLING." There is no sponsorship cure and no fee tier. Do not plan a table here.',
  'fair_cost': 'No cost published — and irrelevant, since outside organisations may not table at all.',
  'fair_deadline': '⚠ NOT PRINTED. The page warns only that "if your organization fails to complete the '
                   'registration form by the posted deadline, you will not be guaranteed a table" WITHOUT '
                   'GIVING THE DATE. Email studentunion@cornell.edu.',
  'fair_url': 'https://scl.cornell.edu/clubfest',
  'policy': 'Student & Campus Life — Tabling on Campus (the operative flat ban); plus University Policy 4.3 '
            '"Sales Activities on Campus" (last updated August 6, 2021)',
  'policy_url': 'https://scl.cornell.edu/sub/sub/get-involved/event-planning/tabling-campus',
  'policy_key': "STUDENT & CAMPUS LIFE — TABLING ON CAMPUS (scl.cornell.edu/sub/sub/get-involved/event-"
                "planning/tabling-campus): 'Tables must be reserved using the 25LIVE SCHEDULING SYSTEM, and "
                "MAY BE RESERVED FOR USE ONLY BY REGISTERED STUDENT ORGANIZATIONS, REGISTERED SORORITIES OR "
                "FRATERNITIES, OR UNIVERSITY DEPARTMENTS.' ⚠⚠ THE DECISIVE SENTENCE, AND THE FLATTEST "
                "PROHIBITION IN NEW YORK: 'OUTSIDE ORGANIZATIONS/VENDORS/BUSINESSES ARE NOT PERMITTED TO "
                "CONDUCT BUSINESS ON CAMPUS, INCLUDING TABLING.' ⚠ SPONSORSHIP DOES NOT CURE IT — the "
                "companion clause, 'A REPRESENTATIVE OF THE SPONSORING ORGANIZATION MUST BE PHYSICALLY ON SITE "
                "AT THE TABLE FOR THE DURATION OF THE RESERVATION,' is a PRESENCE REQUIREMENT FOR THE CLUB'S "
                "OWN TABLE, NOT AN ADMISSION TICKET FOR A VENDOR. Do not read it as a workaround. Contact: "
                "Student & Campus Life, 311 Day Hall, Ithaca NY 14853, SCLComms@cornell.edu. Cornell's central "
                "scheduling tabling page (scheduling.cornell.edu/planning-guide-and-policies/event-planning-"
                "guide/tablings-donation-boxes) adds only mechanics — enter '2' for Expected Head Count — and "
                "PUBLISHES NO ELIGIBILITY RULES, FEES, DEADLINES OR PHONE NUMBERS. "
                "UNIVERSITY POLICY 4.3, 'SALES ACTIVITIES ON CAMPUS,' LAST UPDATED AUGUST 6, 2021 "
                "(policy.cornell.edu/sites/default/files/policy/vol4_3.pdf): 'Cornell University allows LIMITED "
                "SALES to be conducted on its campus in ways that are consistent with the university's "
                "mission, TAKE ACCOUNT OF OFF-CAMPUS BUSINESSES, and comply with applicable laws and "
                "regulations.' 'On-campus sales units must not take advantage of the university's TAX-EXEMPT "
                "STATUS TO COMPETE UNFAIRLY WITH THE PRIVATE RETAIL SECTOR.' The only aperture for a "
                "non-affiliate: 'Registered campus organizations, campus units, and individuals may conduct "
                "fundraising activities' and 'VENDORS NOT AFFILIATED WITH THE UNIVERSITY... MAY PARTICIPATE IN "
                "LIMITED SEASONAL OR THEMATIC SALES.' ⚠ THAT IS A CRAFT-FAIR APERTURE, NOT A FINTECH-"
                "RECRUITING ONE. All sales-related activity on campus OR VIA INTERNET SITES is reviewed and "
                "approved through the CORNELL COMMUNITY COORDINATION COMMITTEE (4C), advised by University "
                "Relations. Named contacts printed in the policy: Director of University Licensing, University "
                "Relations, (607) 255-6074, prodlicenseoffice@cornell.edu; and for fundraising and "
                "course-related sales, the OFFICE OF STUDENT ACTIVITIES, (607) 255-4169, "
                "activities@cornell.edu. "
                "⚠⚠ THE STATUTORY-COLLEGE QUESTION — ASKED AND ANSWERED, AND THE ANSWER IS 'DO NOT ACT ON IT.' "
                "Cornell contains FOUR STATUTORY (CONTRACT) COLLEGES — Agriculture and Life Sciences, Human "
                "Ecology, Industrial and Labor Relations, and Veterinary Medicine — which are State University "
                "of New York units administered by a private university. The obvious question is whether they "
                "are STATE ACTORS bound by the First Amendment, and therefore whether the tabling ban is "
                "unenforceable inside them. FINDING: NO DIFFERENTIAL POLICY EXISTS ON PAPER. The SCL tabling "
                "policy, Policy 4.3 and the 25Live scheduling system are written UNIVERSITY-WIDE with NO "
                "STATUTORY/ENDOWED DISTINCTION ANYWHERE IN THE RETRIEVED TEXT. Cornell operates one facilities "
                "regime across both. THE STATE-ACTION ARGUMENT IS A LIVE LEGAL QUESTION NOT RESOLVED BY ANY "
                "PUBLISHED CORNELL DOCUMENT, AND IT IS NOT ONE AN AMBASSADOR SHOULD ATTEMPT AT A TABLE. Flag "
                "it to counsel alongside the BitLicense question in NYU's policy_key. Note also that New York "
                "has NO campus free-speech statute to invoke even if the state-action point were won.",
  'sponsor_required': '⚠ IRRELEVANT — SPONSORSHIP IS NOT A ROUTE HERE. Only registered student organisations, '
                      'registered Greek chapters and university departments may reserve a table, and outside '
                      'businesses "are not permitted to conduct business on campus, including tabling." The '
                      '"sponsoring organization must be physically on site" clause governs the club\'s own '
                      'table, not a vendor\'s.',
  'clubs': [
    ('⚠⚠ Cornell Blockchain — THE BEST STUDENT BLOCKCHAIN ORGANISATION IN NEW YORK',
     'Founded 2017; "a registered student organization of Cornell University"; mission to "democratize Web3 '
     'awareness and help catalyze real-world use cases of Blockchain technology." IT TEACHES ITS OWN COURSES: '
     'CS-1998, an introductory blockchain course that "has educated over 300 undergraduates" covering '
     'fundamentals through DEXs and NFTs, and CS-4998, a development course on Solidity, Hardhat and '
     'Metamask. It runs the NYC BLOCKCHAIN BOOTCAMP — a 6-week summer programme, three years running, for '
     '50+ inner-city high-school students in Brooklyn — an ANNUAL CONFERENCE SINCE 2019, and an ACCELERATOR '
     'COHORT. Named partners include the Joe and Clara Tsai Foundation and the New York Department of '
     'Education. CONTACT: cornellblockchain@gmail.com · @CUBlockchain on X and YouTube · CornellBlockchain on '
     'GitHub. Officer names deliberately not carried forward — rosters rotate annually.',
     'https://www.cornellblockchain.org/'),
    ('IC3 — the Initiative for CryptoCurrencies and Contracts',
     'Cornell\'s blockchain RESEARCH CENTRE, co-founded and co-directed by Ari Juels. Runs its own events '
     'programme. This is faculty infrastructure, not a student club, and it is the most serious academic '
     'blockchain operation on any campus in this packet.',
     'https://initc3.org/'),
    ('Blockchain @ Cornell Tech',
     'The New York City arm — Cornell Tech on Roosevelt Island runs its own blockchain programming, including '
     'the AI Blockchain Conference. A Manhattan-adjacent audience without the four-hour drive to Ithaca.',
     'https://cornelltechblockchain.com/'),
  ],
  'faculty': [
    ('⚠ Office of Student Activities',
     'NAMED IN POLICY 4.3 as the contact for fundraising and course-related sales — the office to call about '
     'anything club-sponsored, and the one that can tell you what a registered student organisation is and is '
     'not permitted to do with an outside partner. The most useful institutional number at Cornell.',
     'Cornell Student & Campus Life',
     'activities@cornell.edu · (607) 255-4169',
     'https://policy.cornell.edu/sites/default/files/policy/vol4_3.pdf'),
    ('Director of University Licensing, University Relations',
     'Named in Policy 4.3 for policy clarification, and advises the CORNELL COMMUNITY COORDINATION COMMITTEE '
     '(4C) which reviews and approves ALL sales-related activity on campus or via internet sites. If anyone '
     'can tell you whether a crypto sign-up counts as a "sale," it is this office.',
     'Cornell University Relations',
     'prodlicenseoffice@cornell.edu · (607) 255-6074',
     'https://policy.cornell.edu/sites/default/files/policy/vol4_3.pdf'),
    ('Ari Juels',
     'Professor, Cornell Tech; CO-DIRECTOR OF IC3, the Initiative for CryptoCurrencies and Contracts — the '
     'most prominent blockchain research centre at any campus in this packet. Widely quoted on smart-contract '
     'security. ⚠ NO PHONE CONFIRMED on a live page — look up in the Cornell directory.',
     'Cornell Tech / IC3',
     'no phone published — look up in the Cornell directory',
     'https://www.initc3.org/people'),
    ('Student & Campus Life · Cornell Student Union',
     '⚠ NEITHER PUBLISHES A PHONE NUMBER. SCL is email-only at SCLComms@cornell.edu, 311 Day Hall; ClubFest '
     'questions go to studentunion@cornell.edu. Cornell\'s central scheduling site publishes no number either. '
     'Use the Office of Student Activities number above instead.',
     'Cornell University',
     'SCLComms@cornell.edu · studentunion@cornell.edu · no numbers published — look up here',
     'https://scl.cornell.edu/sub/sub/get-involved/event-planning/tabling-campus'),
    ('Cornell Blockchain (student org) — the actual best contact at this campus',
     'Not staff, but this is who an ambassador should email first. The club teaches two credit-bearing '
     'blockchain courses, runs an annual conference with an existing sponsor roster, and operates an '
     'accelerator. It has every reason to want a sponsor and none of the university\'s facility constraints.',
     'Cornell Blockchain',
     'cornellblockchain@gmail.com · no phone published',
     'https://www.cornellblockchain.org/'),
  ],
  'courses': [
    ('CS-1998',
     '⚠ "Introduction to Blockchain" — TAUGHT BY THE STUDENT CLUB, NOT BY FACULTY, and it "has educated over '
     '300 undergraduates" on fundamentals through DEXs and NFTs. A student-taught course is UNUSUALLY '
     'ACCESSIBLE TO AN OUTSIDE GUEST SPEAKER because the people setting the syllabus are the same people who '
     'want industry contact. Fall 2026 offering NOT CONFIRMED — ask the club.',
     'https://www.cornellblockchain.org/'),
    ('CS-4998',
     '⚠ Blockchain DEVELOPMENT course teaching Solidity, Hardhat and Metamask — described as "upcoming," also '
     'run by Cornell Blockchain. Fall 2026 offering NOT CONFIRMED.',
     'https://www.cornellblockchain.org/'),
    ('eCornell FinTech certificate',
     'Professional/executive education, not the undergraduate catalog. A paying practitioner audience rather '
     'than students. Included for completeness.',
     'https://ecornell.cornell.edu/certificates/financial-management/fintech/'),
  ],
  'events': [
    ('⚠⚠ Cornell Blockchain Conference — annual since 2019, STUDENT-RUN, WITH AN EXISTING SPONSOR ROSTER',
     'THE SINGLE HIGHEST-VALUE TARGET IN NEW YORK. A student-run conference is a PRIVATE EVENT with its own '
     'sponsorship pipeline — it engages NONE of Cornell\'s tabling ban or Policy 4.3 sales review. It brings '
     'together "academic, Web3-native, corporate, and institutional leaders." ⚠ THE 2026 HOMEPAGE RETURNED '
     'HTTP 404; the 2025 SPONSORS PAGE IS INDEXED and lists prior sponsors, which is the evidence the pipeline '
     'exists. Email cornellblockchain@gmail.com.',
     'https://www.cornellblockchainconference.com/sponsors'),
    ('AI Blockchain Conference — "The Programmable Economy: AI & Blockchain Redefining Markets"',
     '⚠ April 24, 2026, Cornell Tech, NEW YORK CITY — across the Verizon Executive Education Center '
     '(9am–5pm) and the Tata Innovation Center (from 12pm), closing reception 5:30–7:00 PM. Sessions on '
     'blockchain infrastructure, digital assets, payments, stablecoins, institutional crypto adoption, wealth '
     'management and securities markets. ⚠ THAT DATE IS IN THE PAST relative to a Fall 2026 tour — WATCH FOR '
     'THE 2027 EDITION and get on the sponsor list early.',
     'https://www.aiblockchaincornelltech.org/agenda'),
    ('ClubFest — Sat Sep 5, 2026, Arts Quad, sessions 12:00–1:30 and 2:00–4:00 PM',
     'CONFIRMED date, but outside organisations may not table. Worth walking to identify which clubs are alive '
     'and to meet Cornell Blockchain in person — the two sessions carry different org categories, so check '
     'which one Cornell Blockchain is assigned to before choosing a slot. Also: IC3 runs its own events '
     'programme at ic3research.org/events/.',
     'https://scl.cornell.edu/clubfest'),
  ],
  'play': 'CORNELL HAS THE BEST AUDIENCE IN NEW YORK AND THE FLATTEST BAN — AND THAT COMBINATION HAS EXACTLY '
          'ONE ANSWER: GO THROUGH THE STUDENTS, NEVER THROUGH THE UNIVERSITY. Cornell\'s tabling policy says '
          '"OUTSIDE ORGANIZATIONS/VENDORS/BUSINESSES ARE NOT PERMITTED TO CONDUCT BUSINESS ON CAMPUS, '
          'INCLUDING TABLING," and there is no fee tier and no sponsorship cure — the "sponsoring organization '
          'must be physically on site" clause governs a club\'s own table, not a vendor\'s. Policy 4.3\'s only '
          'aperture, "limited seasonal or thematic sales" reviewed by the 4C committee, is a craft-fair door. '
          'So do not attempt a table. THE SINGLE BEST DOOR IN THE ENTIRE STATE IS CORNELL BLOCKCHAIN AT '
          'cornellblockchain@gmail.com. It is a registered student organisation founded in 2017 that TEACHES '
          'TWO OF ITS OWN BLOCKCHAIN COURSES (CS-1998 has educated 300+ undergraduates; CS-4998 covers '
          'Solidity and Hardhat), runs a summer bootcamp for Brooklyn high-schoolers, operates an accelerator, '
          'and has hosted an ANNUAL CONFERENCE SINCE 2019 WITH AN EXISTING SPONSOR ROSTER. A student-run '
          'conference is a private event with its own sponsorship pipeline — it engages none of the tabling '
          'ban, none of the 4C sales review, and none of Cornell\'s facility policy. Sponsor the conference '
          'and guest-lecture in CS-1998. Second target: Cornell Tech in New York City, which runs the AI '
          'Blockchain Conference — the April 24, 2026 edition has passed, so get on the 2027 sponsor list '
          'early, and note it is a subway ride from the Manhattan cluster rather than four hours to Ithaca. '
          'Only institutional call worth making: Office of Student Activities, (607) 255-4169, to confirm what '
          'a registered org may accept from an outside partner. ⚠ ONE THING TO LEAVE ALONE: Cornell\'s four '
          'STATUTORY COLLEGES (Agriculture, Human Ecology, ILR, Vet) are SUNY units inside a private '
          'university, which raises a real state-action question — but NO CORNELL DOCUMENT DRAWS ANY '
          'STATUTORY/ENDOWED DISTINCTION and one facilities regime covers both. That argument belongs with '
          'counsel, not at a table.',
  'gaps': [
    '⚠ The Cornell Blockchain Conference 2026 HOMEPAGE RETURNS HTTP 404 — only the 2025 sponsors page is '
    'indexed. Get current dates and sponsorship tiers from cornellblockchain@gmail.com.',
    '⚠ ClubFest registration deadline is NOT PRINTED — the page warns that missing it forfeits a guaranteed '
    'table without giving the date. studentunion@cornell.edu.',
    '⚠ Are CS-1998 and CS-4998 running in Fall 2026, and who sets their guest-speaker slate? Ask the club.',
    '⚠ THE STATUTORY-COLLEGE STATE-ACTION QUESTION IS UNRESOLVED and no Cornell document addresses it. '
    'Counsel only — do not act on it.',
    'No phone number for Student & Campus Life, the Cornell Student Union, or Ari Juels/IC3. SCL and the '
    'Student Union are email-only; Cornell\'s central scheduling site publishes no number at all.',
    'Cornell\'s central scheduling tabling page publishes NO eligibility rules, fees or deadlines — only '
    'mechanics.',
    'Whether the 4C committee would treat a crypto sign-up as a "sale" at all is unknown. (607) 255-6074.',
  ],
  },

 # ---------------------------------------------------------------- 11. RIT
 {'state': 'New York',
  'name': 'Rochester Institute of Technology',
  'city': 'Rochester, NY',
  'type': 'Private',
  'tier': 'A — Named target',
  'access': 4,
  'start': 'Mon Aug 24, 2026. ⚠⚠ RIT IS ON SEMESTERS, NOT QUARTERS — it converted years ago and anyone '
           'planning from stale knowledge will be FIVE WEEKS WRONG on Rochester. The calendar labels the '
           'year Fall / Spring / Summer.',
  'adddrop': 'Mon Aug 31, 2026',
  'fallbreak': 'Mon–Tue Oct 12–13, 2026 — same two days as Stony Brook, Buffalo and Albany.',
  'thanksgiving': 'Wed–Fri Nov 25–27, 2026 — ⚠ the university closes at 2:00 p.m. on Wed Nov 25, so Nov 25 is '
                  'a half day, not a full one.',
  'lastclass': 'Mon Dec 7, 2026. Study day Tue Dec 8.',
  'finals': 'Wed Dec 9 – Wed Dec 16, 2026',
  'cal_url': 'https://www.rit.edu/calendar',
  'cal_status': 'CONFIRMED — RIT 2026-2027 academic calendar. Future-year chart at rit.edu/calendar/'
                'future-chart.',
  'fair': 'Tiger Activity Fair (general) and the FirstByte Club Fair (computing organisations)',
  'fair_date': '⚠ NO FALL 2026 DATE PUBLISHED. Pattern: "towards the beginning of the Fall semester," annual, '
               'welcoming new students; features "every official group on campus. Everything from sports '
               'teams to fraternities"; attendance skews heavily freshman — "the majority of the attendees '
               'are going to be freshmen, hunting for people to talk to." LOCATION NOT SPECIFIED on the '
               'source page. ⚠ THE BETTER ROOM IS THE FIRSTBYTE CLUB FAIR, which focuses specifically on '
               'COMPUTING student organisations — a narrower and far better-targeted audience for DGD than '
               'the general fair.',
  'fair_outside': '⚠ NOT MENTIONED at the fair — but IT DOES NOT MATTER, because RIT does not make you use '
                  'the fair. It runs a STANDING PAID VENDOR PROGRAMME with a published external rate card, '
                  'available all term. That is the route. See fair_cost.',
  'fair_cost': '⚠⚠ THE ONLY PUBLISHED EXTERNAL-VENDOR RATE CARD IN NEW YORK, verbatim from the Campus Life '
               'Vendor Agreement: "ONE (1) TABLE — $60.00" · "TWO (2) TABLES — $80.00" · "THREE (3) TABLES — '
               '$100.00." No deposit and NO INSURANCE REQUIREMENT are specified in the agreement — genuinely '
               'unusual, and worth verifying rather than assuming.',
  'fair_deadline': '⚠⚠ "ALL VENDING CONTRACTS RECEIVED BY JULY 18TH WILL RECEIVE THE SAME PRIORITY. ALL '
                   'CONTRACTS RECEIVED AFTER JULY 18TH WILL BE REVIEWED AND ASSIGNED FIRST COME." THAT DATE '
                   'HAS PASSED FOR FALL 2026 — RIT IS NOW FIRST-COME, SO MOVE IMMEDIATELY. Cancellation: '
                   'at least 24 HOURS prior or NO REFUND.',
  'fair_url': 'https://www.rit.edu/campuslife/vending-agreement',
  'policy': 'Campus Life Vendor Agreement (the operative document, with the rate card); RIT Policy C20.0 '
            'Vending Policy (approved 11/4/1998; decommissioned as a governance policy and reclassified as '
            'administrative 5/6/2020); Campus Life Posting Procedures (revised August 2024)',
  'policy_url': 'https://www.rit.edu/campuslife/vending-agreement',
  'policy_key': "⚠⚠ RIT IS THE MOST OPEN CAMPUS IN NEW YORK BY A LARGE MARGIN AND THE ONLY ONE THAT PUBLISHES "
                "A PRICE. CAMPUS LIFE VENDOR AGREEMENT (rit.edu/campuslife/vending-agreement) — THE OPERATIVE "
                "DOCUMENT. THE GATE: 'TO BE SPONSORED BY AN OFFICIALLY RECOGNIZED RIT DEPARTMENT, "
                "ORGANIZATION, OR CLUB.' THE PUBLISHED EXTERNAL VENDOR RATE CARD — THE ONLY ONE IN THE STATE: "
                "'ONE (1) TABLE- $60.00' · 'TWO (2) TABLES- $80.00' · 'THREE (3) TABLES- $100.00.' "
                "⚠⚠ PRIORITY DEADLINE: 'ALL VENDING CONTRACTS RECEIVED BY JULY 18TH WILL RECEIVE THE SAME "
                "PRIORITY. ALL CONTRACTS RECEIVED AFTER JULY 18TH WILL BE REVIEWED AND ASSIGNED FIRST COME.' "
                "THAT DATE HAS PASSED FOR FALL 2026 — RIT IS NOW FIRST-COME AND EVERY DAY COSTS SLOTS. "
                "CANCELLATION AND FORFEITURE: 'INFORM THE VENDING GRADUATE ASSISTANT OF ALL CANCELLATIONS AT "
                "LEAST 24 HOURS PRIOR TO CONFIRMED DATES. FAILURE TO DO SO WILL RESULT IN NO RETURN OF "
                "PAYMENT.' PROHIBITED GOODS: 'No selling of candles or other open flame devices, incense and "
                "potpourri, health/energy drinks, cosmetics, CBD OIL... fog machines' and 'No selling of "
                "tapestries and/or other fabric wall hangings.' ⚠ NOTE WHAT IS *NOT* ON THAT LIST: NOTHING "
                "ABOUT FINANCIAL PRODUCTS, DIGITAL GOODS, SUBSCRIPTIONS, SIGN-UPS, INVESTMENT SCHEMES OR "
                "CRYPTOCURRENCY. The prohibitions are PHYSICAL-GOODS prohibitions written against a "
                "craft-vendor problem, and they simply do not contemplate DGD's activity. That silence is the "
                "most favourable fact in the New York packet — but confirm it rather than exploit it, because "
                "an unanticipated category is exactly the thing an administrator adds to the list after you "
                "leave. ⚠ NO INSURANCE REQUIREMENT AND NO DEPOSIT ARE SPECIFIED IN THE AGREEMENT. That is "
                "genuinely unusual against every other campus in this file and should be VERIFIED, NOT "
                "ASSUMED. CONTACTS PRINTED IN THE AGREEMENT: Jackie Zysk, Assistant Director, (585) 475-2952; "
                "Vending Graduate Assistant, gaccl@rit.edu. "
                "RIT POLICY C20.0, VENDING POLICY, APPROVED NOVEMBER 4, 1998 (rit.edu/academicaffairs/"
                "policiesmanual/c200), responsible office Center for Campus Life / Dining Services — ⚠ "
                "'DECOMMISSIONED AS A GOVERNANCE POLICY AND RECLASSIFIED AS AN ADMINISTRATIVE POLICY MAY 6, "
                "2020.' THE POLICY MANUAL PAGE CARRIES THE HEADER ONLY; THE OPERATIVE TEXT IS NOT ON IT. It "
                "redirects to the Campus Life Vendor Agreement for Campus Center, SAU and Monroe Hall, and for "
                "other buildings to 'the division/college/department that controls the space you wish to vend "
                "in' — i.e. RIT IS DECENTRALISED BEYOND THOSE THREE BUILDINGS, so a college-specific approach "
                "(Golisano, for computing) is a separate and possibly easier conversation. Also: Campus Life "
                "Posting Procedures, revised August 2024 (rit.edu/studentlife/sites/rit.edu.studentlife/files/"
                "2024-08/Campus%20Life%20Posting%20Procedures%20FINAL.pdf). RIT IS PRIVATE — no public-forum "
                "obligation, and New York has no campus free-speech statute — AND IT DOES NOT NEED ONE, "
                "BECAUSE IT SELLS ACCESS AT A PUBLISHED PRICE. ⚠ STRATEGIC CONTEXT: FOUNDRY, one of the "
                "largest bitcoin mining and staking operations in North America (a Digital Currency Group "
                "company), IS HEADQUARTERED IN ROCHESTER AND ALREADY HAS A FORMAL TEACHING RELATIONSHIP WITH "
                "RIT. Rochester is a functioning crypto-industry town with a technical university in it.",
  'sponsor_required': '⚠ YES — "to be sponsored by an officially recognized RIT department, organization, or '
                      'club" is the first line of the vendor agreement. BUT UNLIKE EVERY OTHER SPONSORSHIP '
                      'GATE IN THIS FILE, IT SITS ON TOP OF A PUBLISHED PRICE RATHER THAN INSTEAD OF ONE — '
                      'RIT tells you exactly what it costs once you have a sponsor. The Blockchain Technology '
                      'Club is the obvious sponsor.',
  'clubs': [
    ('⚠⚠ Blockchain Technology Club (BTC RIT)',
     'ACTIVE, WEEKLY MEETINGS, TECHNICAL, AND THE OBVIOUS SPONSOR FOR THE $60 VENDOR TABLE. Focused on '
     '"decentralized systems and their use cases" including cryptocurrencies, blockchain, DeFi, NFTs and DAOs. '
     'Meets in GOL 2690 and on Discord, runs a Discord server and a weekly member email, and maintains its own '
     'wiki at wiki.btcrit.com. Executive board listed at btcrit.com/eboard — names deliberately not carried '
     'forward, rosters rotate. ⚠ The club\'s own site carries a dated meeting listing; CONFIRM THE CURRENT '
     'TIME via Discord or CampusGroups before travelling.',
     'https://btcrit.com/'),
    ('BTC RIT on CampusGroups — a directory that actually works',
     '⚠ UNUSUALLY, RIT\'s CampusGroups install (campusgroups.rit.edu) RESOLVED TO READABLE CONTENT, unlike '
     'almost every other CampusLabs/CampusGroups directory in this packet. Club forum and events calendar are '
     'both browsable. That makes RIT the easiest campus in New York to verify club activity before you travel.',
     'https://campusgroups.rit.edu/BTC/'),
    ('FirstByte and the computing organisations',
     'RIT runs a FirstByte Club Fair specifically for computing student organisations — a narrower, more '
     'technical room than the general Tiger Activity Fair and a better fit for DGD.',
     'https://www.rit.edu/admissions/blog/rits-tiger-activity-fair-great-place-go'),
  ],
  'faculty': [
    ('⚠⚠ Jackie Zysk',
     'ASSISTANT DIRECTOR, CENTER FOR CAMPUS LIFE — SHE CONTROLS THE $60 VENDOR TABLE. THIS IS THE SINGLE MOST '
     'VALUABLE PHONE NUMBER IN THE NEW YORK PACKET, because it is the only one anywhere in the state attached '
     'to a published price for outside access. The July 18 priority deadline has passed, so RIT is now '
     'first-come — call before anything else in New York.',
     'RIT Center for Campus Life',
     '(585) 475-2952',
     'https://www.rit.edu/campuslife/vending-agreement'),
    ('Vending Graduate Assistant',
     'Handles vendor scheduling and, critically, CANCELLATIONS — "at least 24 hours prior to confirmed dates. '
     'Failure to do so will result in no return of payment." ⚠ Email only, no phone published.',
     'RIT Center for Campus Life',
     'gaccl@rit.edu · no phone published',
     'https://www.rit.edu/campuslife/vending-agreement'),
    ('Jonathan S. Weissman',
     'PRINCIPAL LECTURER, Department of Cybersecurity, Golisano College of Computing and Information Sciences '
     '— TAUGHT THE RIT CERTIFIED x FOUNDRY CRYPTOCURRENCY AND BLOCKCHAIN COURSE, which means he has already '
     'built and delivered crypto curriculum in partnership with a major industry player. Multiple teaching '
     'awards; developed coursework for the edX RITx Cybersecurity MicroMasters. Office 100 Lomb Memorial '
     'Drive. ⚠ THE RIT DIRECTORY PAGE PUBLISHES NEITHER EMAIL NOR PHONE.',
     'Department of Cybersecurity, Golisano College, RIT',
     'no email or phone published — look up here',
     'https://www.rit.edu/directory/jswics-jonathan-weissman'),
    ('Dennis Di Lorenzo',
     'Chief Business Officer, RIT CERTIFIED — the unit that partnered with Foundry to build and deliver the '
     'cryptocurrency course. If the play is a co-branded educational programme rather than a table, RIT '
     'Certified is the counterparty that has already done exactly that deal once. ⚠ No contact published in '
     'the article.',
     'RIT Certified',
     'no number published — look up here',
     'https://www.rit.edu/news/rit-certified-and-foundry-collaborate-cryptocurrency-course'),
    ('Center for Campus Life — Building Operations & Vending',
     'The services page behind the vendor programme, covering Campus Center, SAU and Monroe Hall. Note that '
     'C20.0 sends you elsewhere for other buildings: "the division/college/department that controls the space '
     'you wish to vend in" — so Golisano College is a separate, possibly easier conversation for a computing '
     'audience.',
     'RIT Center for Campus Life',
     'route via Jackie Zysk (585) 475-2952',
     'https://campusgroups.rit.edu/cclbuildingops/services/'),
  ],
  'courses': [
    ('RIT Certified x Foundry cryptocurrency and blockchain course',
     '⚠ A "weeklong course on cryptocurrency and blockchain technology," taught by Jonathan S. Weissman and '
     'developed with FOUNDRY, the Rochester-based digital-asset company. The programme served underserved '
     'Rochester students. Article dated August 8, 2022. NO OFFICIAL COURSE TITLE IS PRINTED and the Fall 2026 '
     'offering is NOT CONFIRMED — but the precedent is the point: RIT has already co-built crypto curriculum '
     'with an industry partner.',
     'https://www.rit.edu/news/rit-certified-and-foundry-collaborate-cryptocurrency-course'),
    ('"Giving students interdisciplinary perspectives on the evolving cryptocurrency industry"',
     'RIT\'s own news coverage of its cryptocurrency teaching. Useful as evidence of institutional comfort '
     'with the subject when asking for access — RIT publicises this work rather than hiding it.',
     'https://www.rit.edu/news/giving-students-interdisciplinary-perspectives-evolving-cryptocurrency-industry'),
    ('(Catalog courses)',
     '⚠ NO STANDING RIT CATALOG COURSE on blockchain or cryptocurrency was confirmed for Fall 2026. The '
     'Foundry collaboration was a short course through RIT Certified, which is professional education. Gap.',
     'https://www.rit.edu/calendar'),
  ],
  'events': [
    ('⚠⚠ Standing paid vendor table — $60 / $80 / $100, available all term',
     'NOT AN EVENT, AND THAT IS WHY IT IS BETTER THAN ONE. RIT sells table access at a published price for as '
     'many days as you want, all term long, rather than confining outside organisations to one afternoon in '
     'August. Requires an RIT department, organisation or club sponsor (BTC RIT is the obvious one). July 18 '
     'priority deadline has passed — first-come now. Jackie Zysk (585) 475-2952.',
     'https://www.rit.edu/campuslife/vending-agreement'),
    ('Tiger Activity Fair and FirstByte Club Fair',
     '⚠ NO FALL 2026 DATES PUBLISHED. Tiger Activity Fair is early-semester, all official groups, heavily '
     'freshman. FirstByte is computing-specific and the better room. Location not specified for either.',
     'https://www.rit.edu/admissions/blog/rits-tiger-activity-fair-great-place-go'),
    ('BTC RIT weekly meetings — GOL 2690 and Discord',
     'A weekly, technical, self-selecting audience of exactly the right students, requiring no vendor fee at '
     'all. ⚠ Confirm the current meeting time via the club\'s Discord or CampusGroups — the website listing is '
     'dated. Events calendar: campusgroups.rit.edu/btc/events/calendar',
     'https://campusgroups.rit.edu/BTC/'),
  ],
  'play': 'START THE ENTIRE NEW YORK TOUR HERE, AND CALL (585) 475-2952 BEFORE ANY OTHER NUMBER IN THIS FILE. '
          'RIT is the only campus in New York that publishes a price for outside access: "ONE (1) TABLE- '
          '$60.00, TWO (2) TABLES- $80.00, THREE (3) TABLES- $100.00," with no deposit and no insurance '
          'requirement stated in the agreement, and a prohibited-goods list that bans candles, incense, energy '
          'drinks, cosmetics, CBD oil and fog machines while saying NOTHING about financial products, digital '
          'goods, subscriptions or sign-ups. Jackie Zysk, Assistant Director of the Center for Campus Life, '
          'controls it. ⚠ THE JULY 18 PRIORITY DEADLINE HAS ALREADY PASSED FOR FALL 2026, so RIT is now '
          'first-come and every day of delay costs slots — this is the most time-critical item in the state. '
          'You need an RIT department, organisation or club to sponsor you, and the obvious one is the '
          'BLOCKCHAIN TECHNOLOGY CLUB, which is active, meets weekly in GOL 2690 and on Discord, and is one of '
          'the few clubs in this packet whose activity can actually be VERIFIED before you travel, because '
          'RIT\'s CampusGroups directory is readable. And the strategic case is the strongest anywhere: '
          'FOUNDRY, one of North America\'s largest bitcoin mining and staking operations, is headquartered in '
          'Rochester and has ALREADY co-built and delivered a cryptocurrency course with RIT Certified, taught '
          'by Jonathan Weissman of Golisano College. Rochester is a working crypto town with a technical '
          'university in it and the loosest access rules in New York. If the BitLicense question clears, this '
          'is the best stop on the tour. ⚠ AND REMEMBER: RIT IS ON SEMESTERS, NOT QUARTERS — it starts Aug 24 '
          'like the rest of upstate, not five weeks later.',
  'gaps': [
    '⚠⚠ TIME-CRITICAL — the July 18 vendor-contract priority deadline has PASSED. RIT is first-come for Fall '
    '2026. Call Jackie Zysk (585) 475-2952 immediately.',
    '⚠ Does RIT treat a crypto sign-up or wallet creation as "selling"? The prohibited list is entirely '
    'physical goods and does not contemplate it. ASK BEFORE ASSUMING — an unanticipated category is exactly '
    'what gets added to the list afterwards.',
    '⚠ The vendor agreement specifies NO INSURANCE REQUIREMENT AND NO DEPOSIT, which is unusual against every '
    'other campus in this file. VERIFY rather than assume.',
    '⚠ Which RIT department, organisation or club will sponsor? BTC RIT is the obvious candidate but has not '
    'been asked.',
    '⚠ No Fall 2026 date or location for the Tiger Activity Fair or the FirstByte Club Fair.',
    'No email or phone published for Jonathan Weissman on the RIT directory page.',
    'No contact published for Dennis Di Lorenzo / RIT Certified.',
    'BTC RIT\'s published meeting time is dated — confirm via Discord or CampusGroups.',
    'C20.0 sends non-Campus-Center buildings to "the division/college/department that controls the space" — '
    'get the Golisano College contact if a computing-specific location is wanted.',
  ],
  },

 # ---------------------------------------------------------------- 12. Fordham
 {'state': 'New York',
  'name': 'Fordham University',
  'city': 'Bronx, NY (Rose Hill) and Manhattan (Lincoln Center)',
  'type': 'Private (religious)',
  'tier': 'C — Opportunistic',
  'access': 2,
  'start': '⚠ Wed Aug 26, 2026 — UNVERIFIED. THIS DATE COMES FROM A THIRD-PARTY AGGREGATOR '
           '(acadcalendar.com), NOT FROM FORDHAM. Do not print it in an ambassador packet without a phone '
           'confirmation.',
  'adddrop': '⚠ Thu Sep 3, 2026 — "Add/drop ends and the last day for program changes." UNVERIFIED, '
             'third-party aggregator only.',
  'fallbreak': '⚠ NONE LISTED for Fall 2026 — UNVERIFIED. Fordham has historically run a Family Weekend in '
               'early October rather than a break. Confirm.',
  'thanksgiving': '⚠ Wed Nov 25 – Sun Nov 29, 2026, university closed — UNVERIFIED, third-party aggregator.',
  'lastclass': '⚠ Tue Dec 8, 2026 — UNVERIFIED, third-party aggregator.',
  'finals': '⚠ Dec 11–18, 2026, with Modern Languages exams Dec 10 — UNVERIFIED, third-party aggregator.',
  'cal_url': 'https://go.activecalendar.com/FordhamUniversity/site/academic/',
  'cal_status': '⚠⚠ UNVERIFIED — EVERY DATE ABOVE COMES FROM acadcalendar.com, A THIRD-PARTY AGGREGATOR. '
                'Fordham\'s official calendar runs on an ActiveCalendar JavaScript grid that renders NO event '
                'data to tooling. AND WORSE: Fordham\'s own "Important Dates for Parents and Families" page — '
                'one of the very few fordham.edu pages that DID load — STILL DISPLAYS THE 2024-25 ACADEMIC '
                'YEAR ("First Day of Classes: Wednesday, August 28th, 2024"; "Last Day of Fall Classes: '
                'Friday, December 10th, 2024"; "Spring Semester Classes Begin: Monday, January 13th, 2025"). '
                'THAT PAGE HAS NOT BEEN UPDATED IN TWO YEARS AND WILL HAND A 2024 CALENDAR TO ANYONE READING '
                'IT IN AUGUST 2026. Note also that the Law School publishes its own separate Fall 2026 page — '
                'LAW SCHOOL DATES DO NOT GOVERN THE UNDERGRADUATE COLLEGES.',
  'fair': 'Fall Club Fair — run by USG Rose Hill; Fordham runs SEPARATE club fairs at Rose Hill and Lincoln '
          'Center',
  'fair_date': '⚠ UNVERIFIED AND UNREADABLE. The USG Rose Hill Fall Club Fair page (usgrh.fordham.edu/'
               'fall-club-fair/) is ROBOTS_DISALLOWED — its robots.txt fetch TIMED OUT — so no date, time or '
               'location could be read. A student-organisation event page for a prior Club Fair is dated '
               'AUGUST 28 (2024), i.e. the pattern is THE FIRST DAYS OF TERM, traditionally on EDWARDS PARADE '
               'at Rose Hill. Two campuses means two fairs and two bookings.',
  'fair_outside': '⚠ NO PUBLISHED ANSWER — and assume no. The Student Handbook limits distribution of '
                  'literature to registered student organisations and to individual students "sponsored by a '
                  'University club, office, or department." NO CATEGORY EXISTS FOR AN OUTSIDE ENTITY in any '
                  'Fordham document that could be reached.',
  'fair_cost': '⚠ NOT PUBLISHED. No Fordham fee schedule, vendor tier or rate card exists in any reachable '
               'document — and the pages that would carry one are behind a login gateway.',
  'fair_deadline': '⚠ NOT PUBLISHED.',
  'fair_url': 'https://usgrh.fordham.edu/fall-club-fair/',
  'policy': 'Fordham Student Handbook — "Distribution of Literature" (recovered via FIRE\'s policy archive; '
            'Fordham\'s own copy is login-gated). FIRE rating: YELLOW, last reviewed May 1, 2026.',
  'policy_url': 'https://www.fire.org/colleges/fordham-university/student-handbook-distribution-literature',
  'policy_key': "⚠⚠ FORDHAM IS THE MOST OPAQUE CAMPUS IN THIS PACKET. www.fordham.edu IS EFFECTIVELY "
                "UNREADABLE TO RESEARCH TOOLING: SIX SEPARATE URLS ALL RETURNED A 302 REDIRECT TO "
                "https://loginp.fordham.edu/cas/login?gateway=true — the registration-information page, the "
                "Distribution of Literature policy, the McGinley Center reservations FAQ, the McGinley Center "
                "page, the Office for Student Involvement at Rose Hill page, and its staff page. THIS IS NOT A "
                "ROBOTS BLOCK AND NOT A 403 — IT IS A CAS SINGLE-SIGN-ON AUTHENTICATION WALL IN FRONT OF "
                "PUBLIC MARKETING PAGES. The consequence is that NO FORDHAM PHONE NUMBER, STAFF NAME, FEE, OR "
                "EVENT DATE IN THIS RECORD COULD BE CONFIRMED FROM A FORDHAM-HOSTED PAGE. A human with a "
                "normal browser will see all of it instantly. THIS ENTIRE CAMPUS NEEDS ONE HOUR OF MANUAL "
                "BROWSING BEFORE ANYONE TRAVELS TO THE BRONX. "
                "THE OPERATIVE POLICY TEXT WAS RECOVERED FROM FIRE'S ARCHIVE (fire.org/colleges/"
                "fordham-university/student-handbook-distribution-literature), which rates the policy YELLOW, "
                "last reviewed May 1, 2026. FORDHAM STUDENT HANDBOOK — DISTRIBUTION OF LITERATURE. SECTION 2: "
                "registered student organisations distributing materials must 'COORDINAT[E] WITH THE OFFICE "
                "FOR STUDENT INVOLVEMENT' and ensure 'THE SOURCE OF THE MATERIAL AND THE NAME OF THE "
                "ORGANIZATION MUST BE STATED'; organisations and participants remain 'responsible for ensuring "
                "that NO UNIVERSITY POLICY IS VIOLATED' and that there are 'NO JUSTIFIED COMPLAINT[S] ON THE "
                "GROUNDS OF OBSCENITY OR LIBEL.' SECTION 3: individual students may distribute materials only "
                "when 'SPONSORED BY A UNIVERSITY CLUB, OFFICE, OR DEPARTMENT,' with identical responsibilities "
                "and coordination requirements. FIRE's analysis: rated yellow for vagueness — compliance with "
                "unspecified 'University Regulations' and undefined 'obscenity or libel' create room for "
                "subjective enforcement. ⚠⚠ READ WHAT THE POLICY DOES NOT CONTAIN: ANY CATEGORY FOR A "
                "NON-FORDHAM ENTITY. Distribution is available to (a) registered student organisations and "
                "(b) individual students sponsored by a University club, office or department. A COMMERCIAL "
                "THIRD PARTY IS NOT ON THE LIST. There is no fee schedule, no vendor tier and no external-user "
                "route in any Fordham document that could be reached. CONFIRMING THE GAP FROM ANOTHER "
                "DIRECTION: Fordham's Bulletin 'University Policies' section (bulletin.fordham.edu/pcs-grad/"
                "policies-procedures/university-policies/) DOES LOAD, and it contains NO POLICY WHATSOEVER on "
                "solicitation, commercial activity, outside organisations, use of facilities or distribution "
                "of literature — it covers campus safety, FERPA, Clery, workplace equity, transcripts and the "
                "Code of Conduct. Those policies live only in the GATED Student Handbook. FORDHAM IS A "
                "PRIVATE, JESUIT INSTITUTION — no public-forum obligation, New York has no campus free-speech "
                "statute, and A MISSION-ALIGNMENT SCREEN SHOULD BE EXPECTED from a Catholic university being "
                "asked to host a cryptocurrency issuer. ⚠ ONE MORE DOCUMENTATION FAILURE WORTH RECORDING: "
                "411.fordham.edu, which looks like a campus directory, IS ACTUALLY AN INTERNAL "
                "EXTENSION-DIALLING INSTRUCTION PAGE — 'Extension dialing between campuses at Fordham "
                "University is accomplished by dialing a steering digit + a four digit extension' — AND "
                "CONTAINS NO NUMBERS AT ALL.",
  'sponsor_required': '⚠ YES, AND THERE IS NO CATEGORY FOR YOU. Distribution runs through registered student '
                      'organisations coordinating with the Office for Student Involvement, or individual '
                      'students "sponsored by a University club, office, or department." No Fordham document '
                      'that could be reached contemplates an outside commercial entity at all.',
  'clubs': [
    ('⚠ Rose Hill and Lincoln Center student organisations — BOTH DIRECTORIES LOGIN-GATED',
     'Both student-organisation directories sit behind the CAS gateway and COULD NOT BE ENUMERATED. NO '
     'blockchain, crypto or fintech club at Fordham is confirmed EITHER WAY. Fordham has a Gabelli School of '
     'Business with a substantial finance population, so the prior probability of a finance or investment club '
     'is high — but NOTHING IS VERIFIED. Browse fordham.edu/student-life/student-organizations/ manually.',
     'https://www.fordham.edu/student-life/student-organizations/rose-hill-student-organizations/'),
    ('USG Rose Hill (undergraduate student government)',
     'Runs the Fall Club Fair. ⚠ Its site (usgrh.fordham.edu) is ROBOTS_DISALLOWED to tooling — the robots.txt '
     'fetch timed out — so nothing on it could be read. This is the body to email once a human has found a '
     'working address on it.',
     'https://usgrh.fordham.edu/fall-club-fair/'),
    ('(Two campuses, two club ecosystems)',
     'Fordham runs SEPARATE club fairs and separate student-involvement offices at Rose Hill (Bronx) and '
     'Lincoln Center (Manhattan). Lincoln Center is inside the Manhattan cluster; Rose Hill is a separate '
     'trip to the Bronx. Treat them as two campuses, because Fordham does.',
     'https://now.fordham.edu/university-news/diving-into-campus-life-at-fordham-club-fairs/'),
  ],
  'faculty': [
    ('⚠⚠ NO FORDHAM PHONE NUMBER COULD BE CONFIRMED — THE ONLY CAMPUS IN NEW YORK WITH ZERO',
     'Six separate fordham.edu URLs all 302-redirect to loginp.fordham.edu/cas/login: the Office for Student '
     'Involvement page and its staff page, the Dean of Students pages, the McShane/McGinley Campus Center '
     'pages, and the registration-information page. The Public Safety emergency-numbers page is gated too. '
     '⚠ DO NOT GUESS FORDHAM\'S MAIN LINE — widely circulated numbers for Rose Hill and Lincoln Center exist '
     'in secondary sources but NONE COULD BE VERIFIED ON A FORDHAM PAGE, and a wrong number in an ambassador '
     'packet is exactly the failure mode to avoid. Look them up here in a normal browser.',
     'Fordham University',
     'NO NUMBER CONFIRMED — look up here',
     'https://www.fordham.edu/about/maps-and-directions/'),
    ('Office for Student Involvement (Rose Hill)',
     'THE OFFICE NAMED IN THE POLICY: registered student organisations distributing materials must "coordinate '
     'with the Office for Student Involvement." It is therefore the single most important office at Fordham '
     'for DGD — and its page AND its staff page are both behind the CAS gateway. There is a separate Office '
     'for Student Involvement at Lincoln Center.',
     'Fordham Rose Hill, Bronx',
     'no number published to tooling (page 302s to CAS login) — look up here',
     'https://www.fordham.edu/student-life/student-involvement/office-for-student-involvement-at-rose-hill/'),
    ('Dean of Students (Rose Hill and Lincoln Center)',
     'Fordham maintains separate Deans of Students by campus. The escalation point above Student Involvement, '
     'and at a Jesuit university the person most likely to apply a mission-alignment judgement to a '
     'cryptocurrency approach. ⚠ Pages gated.',
     'Fordham University',
     'no number published to tooling — look up here',
     'https://www.fordham.edu/student-life/deans-of-students-and-student-life/'),
    ('McShane Campus Center (formerly McGinley)',
     'The Rose Hill campus centre and the reservations office for it. ⚠ Both the McGinley reservations FAQ and '
     'the campus centre page 302-redirect to CAS login. Renamed McShane — searching for "McGinley" still '
     'surfaces live URLs, so use both names.',
     'Fordham Rose Hill',
     'no number published to tooling — look up here',
     'https://www.fordham.edu/mcginley/'),
    ('(Faculty)',
     '⚠ NOT CONFIRMED — no Fordham faculty member working on blockchain, cryptocurrency, fintech or digital '
     'assets could be found. The GABELLI SCHOOL OF BUSINESS is where to look and it has a real finance '
     'faculty. Nothing verified because the site is gated.',
     'Gabelli School of Business, Fordham',
     'no number published — look up here',
     'https://bulletin.fordham.edu/pcs-grad/policies-procedures/university-policies/'),
  ],
  'courses': [
    ('(Courses)',
     '⚠ NOT CONFIRMED. The undergraduate bulletin is partially reachable but no blockchain, cryptocurrency or '
     'fintech course was located. The Gabelli School of Business is the likeliest home. Gap.',
     'https://bulletin.fordham.edu/pcs-grad/policies-procedures/university-policies/'),
    ('(Fall 2026 offerings)',
     '⚠ NONE CONFIRMED at Fordham.',
     'https://go.activecalendar.com/FordhamUniversity/site/academic/'),
    ('⚠ Note on the Law School',
     'Fordham Law publishes its own separate Fall 2026 academic calendar at fordham.edu/school-of-law/'
     'academics/academic-calendar/fall-2026/. LAW SCHOOL DATES DO NOT GOVERN THE UNDERGRADUATE COLLEGES — do '
     'not substitute one for the other when the undergraduate calendar cannot be read.',
     'https://www.fordham.edu/school-of-law/academics/academic-calendar/fall-2026/'),
  ],
  'events': [
    ('Fall Club Fair — Rose Hill (Edwards Parade) and a separate one at Lincoln Center',
     '⚠ DATE UNVERIFIED AND THE PAGE IS UNREADABLE (usgrh.fordham.edu robots.txt times out). Pattern from a '
     'prior instance: AUGUST 28 (2024), i.e. the first days of term. Two campuses, two fairs, two bookings.',
     'https://now.fordham.edu/university-news/diving-into-campus-life-at-fordham-club-fairs/'),
    ('(Blockchain-specific events)',
     '⚠ NONE CONFIRMED at Fordham. Nothing could be verified in either direction because the site is gated.',
     'https://bulletin.fordham.edu/pcs-grad/policies-procedures/university-policies/'),
    ('⚠ Family Weekend / Important Dates page — CONFIRMED STALE',
     'Fordham\'s own Important Dates for Parents and Families page still shows the 2024-25 year: "First Day of '
     'Classes: Wednesday, August 28th, 2024," "Family Weekend: Friday, October 4th - Sunday, October 6th, '
     '2024," "Last Day of Fall Classes: Friday, December 10th, 2024." TWO YEARS OUT OF DATE AND STILL LIVE. '
     'Anyone reading it in August 2026 gets a 2024 calendar.',
     'https://www.fordham.edu/families/important-dates/'),
  ],
  'play': 'DROP FORDHAM TO LAST AND DO NOT TRAVEL TO THE BRONX UNTIL SOMEONE HAS SPENT AN HOUR IN A BROWSER. '
          'This is the only campus in New York where NOT ONE PHONE NUMBER COULD BE VERIFIED, because '
          'www.fordham.edu puts a CAS single-sign-on wall in front of its public marketing pages — six '
          'separate URLs all 302-redirected to loginp.fordham.edu/cas/login, including the Office for Student '
          'Involvement, its staff page, the Dean of Students, the McShane Campus Center reservations FAQ and '
          'the registration-information page. Every Fall 2026 date in this record rests on a THIRD-PARTY '
          'AGGREGATOR, and Fordham\'s own Important Dates page is TWO YEARS STALE and still serving 2024 '
          'dates to anyone who finds it. On substance the picture is not encouraging either: the Student '
          'Handbook (recovered via FIRE, which rates it yellow) permits distribution of literature only by '
          'registered student organisations coordinating with the Office for Student Involvement, or by '
          'individual students "sponsored by a University club, office, or department" — THERE IS NO CATEGORY '
          'FOR AN OUTSIDE ENTITY AT ALL, no fee schedule and no vendor tier anywhere. Fordham is private and '
          'Jesuit, owes no public-forum duty, and will apply a mission screen to a cryptocurrency issuer. '
          'IF YOU GO ANYWAY, the one real asset is the GABELLI SCHOOL OF BUSINESS finance population, and the '
          'only viable door is a student club at LINCOLN CENTER — which sits inside the Manhattan cluster and '
          'costs you nothing extra to try, unlike Rose Hill in the Bronx. So: assign someone thirty minutes '
          'to browse fordham.edu manually, get the Rose Hill and Lincoln Center main lines and the Office for '
          'Student Involvement number, confirm the six Fall 2026 dates by phone, and find out whether any '
          'finance or blockchain club exists. If that returns nothing, skip Fordham — with eleven better '
          'campuses in this state, it does not earn a day.',
  'gaps': [
    '⚠⚠ ZERO FORDHAM PHONE NUMBERS CONFIRMED. Six URLs 302-redirect to loginp.fordham.edu/cas/login. Get the '
    'Rose Hill and Lincoln Center main lines from fordham.edu/about/maps-and-directions/ IN A BROWSER. DO NOT '
    'GUESS THEM.',
    '⚠⚠ ALL SIX FALL 2026 DATES COME FROM A THIRD-PARTY AGGREGATOR (acadcalendar.com), NOT FROM FORDHAM. '
    'Confirm every one by phone before printing them.',
    '⚠⚠ Fordham\'s own "Important Dates for Parents and Families" page IS TWO YEARS STALE and still shows '
    '2024-25 dates. https://www.fordham.edu/families/important-dates/',
    '⚠ The USG Rose Hill Fall Club Fair page is ROBOTS_DISALLOWED (robots.txt fetch timed out) — no date, time '
    'or location readable.',
    '⚠ Both student-organisation directories are login-gated. NO blockchain, crypto, fintech or investment '
    'club at Fordham is confirmed either way, despite the Gabelli School finance population.',
    '⚠ 411.fordham.edu is NOT a people directory — it is an internal extension-dialling instruction page with '
    'no numbers on it.',
    'Fordham\'s official academic calendar runs on an ActiveCalendar JavaScript grid that renders no data.',
    'No Fordham faculty member or course on blockchain/fintech confirmed.',
    'Is there ANY route at all for an outside commercial entity? No Fordham document that could be reached '
    'contemplates one. Ask the Office for Student Involvement directly.',
  ],
  },
]

DEADLINES = [

 # ---- The one that outranks everything ----
 ('', 'BEFORE ANY NEW YORK TRAVEL IS BOOKED', 'All New York campuses',
  '⚠⚠ GET WRITTEN COUNSEL ON THE BITLICENSE — THIS DECIDES WHETHER NEW YORK EXISTS AS A MARKET',
  '23 NYCRR s 200.3(a): "No Person shall, without a license obtained from the superintendent as provided in '
  'this Part, engage in any Virtual Currency Business Activity." s 200.2(q)(5) puts "CONTROLLING, '
  'ADMINISTERING, OR ISSUING A VIRTUAL CURRENCY" inside that definition whenever the activity involves "New '
  'York or a New York Resident" — one student sign-up on a Manhattan quad is enough, and there is no '
  'small-volume or promotional carve-out anywhere in Part 200. Neither s 200.3(c) exemption reaches an issuer: '
  'the merchant/consumer exemption covers people who USE virtual currency, not people who issue it. The only '
  'argument worth putting is the s 200.2(p)(2) affinity-program exclusion, and it fails on its own terms if '
  'the redeemed asset is convertible. ALSO GET A READ ON THE AGENT CLAUSE: licensees may not operate "through '
  'an agent or agency arrangement when the agent is not a Licensee" — that is a direct warning about campus '
  'ambassadors. Application fee $5,000. Until this clears, INFORMATION-ONLY is the only defensible posture: '
  'no wallet creation, no credit issuance, no referral accrual.',
  'https://www.law.cornell.edu/regulations/new-york/23-NYCRR-200.2',
  'NY DFS publishes NO phone for its virtual currency unit and obfuscates its email — this is a lawyer, not '
  'a phone call'),

 # ---- Time-critical, money attached ----
 ('', 'IMMEDIATELY — the deadline has already passed', 'Rochester Institute of Technology',
  '⚠⚠ RIT VENDOR PRIORITY DEADLINE WAS JULY 18 — YOU ARE NOW FIRST-COME',
  '"ALL VENDING CONTRACTS RECEIVED BY JULY 18TH WILL RECEIVE THE SAME PRIORITY. ALL CONTRACTS RECEIVED AFTER '
  'JULY 18TH WILL BE REVIEWED AND ASSIGNED FIRST COME." RIT is the ONLY campus in New York with a published '
  'external-vendor rate card: one table $60, two tables $80, three tables $100. No deposit and no insurance '
  'requirement are stated in the agreement. Cancellation must be at least 24 hours prior or there is NO '
  'RETURN OF PAYMENT. You must be "sponsored by an officially recognized RIT department, organization, or '
  'club" — the Blockchain Technology Club (active, weekly, GOL 2690 + Discord) is the obvious one. Every day '
  'of delay costs slots.',
  'https://www.rit.edu/campuslife/vending-agreement',
  'Jackie Zysk, Assistant Director, Center for Campus Life · (585) 475-2952 · gaccl@rit.edu'),

 ('2026-07-18', 'Jul 18, 2026 (PASSED)', 'Rochester Institute of Technology',
  '⚠⚠ RIT vending contract priority date — passed; assignment is now first-come',
  'Retained so the countdown reads correctly and so nobody assumes the window is still open. Contracts are '
  'still accepted, just without priority.',
  'https://www.rit.edu/campuslife/vending-agreement',
  'Jackie Zysk · (585) 475-2952'),

 # ---- Term starts, in date order ----
 ('2026-08-18', 'Aug 18, 2026', 'Binghamton University',
  '⚠ EARLIEST TERM START IN NEW YORK — classes begin',
  'Six days ahead of the next SUNY and THREE WEEKS ahead of Columbia. If the tour is planned from a September '
  'mental model, Binghamton is already deep into term. Add/drop closes Aug 31 at 11:59 p.m.',
  'https://www.binghamton.edu/academics/academic-calendar.html',
  'The Union · Catherine Faughnan cfaughn@binghamton.edu · Catering (607) 777-2925'),

 ('2026-08-22', 'Aug 22, 2026 — ⚠ DATE SUSPECT', 'Binghamton University',
  '⚠⚠ U-FEST — ONE OF ONLY TWO NEW YORK FAIRS THAT ADMITS EXTERNAL VENDORS, BUT THE DATE IS PROBABLY STALE',
  'Peace Quad, 11 a.m.–3 p.m. "VENDORS FROM ALL OVER THE BINGHAMTON, VESTAL AND JOHNSON CITY AREA WILL BE ON '
  'CAMPUS" — note the geographic limiter; that may be a local-business tier that excludes a national issuer. '
  '250+ student orgs, 40 Greek chapters, departments. Student-org slots already FULL with a waitlist. '
  '⚠ THE PAGE PRINTS "August 22" WITH NO YEAR AND AUG 22, 2026 IS A SATURDAY (term starts Tue Aug 18) — '
  'almost certainly carried over from 2025. CONFIRM BEFORE TRAVELLING.',
  'https://www.binghamton.edu/campus-activities/events/ufest/index.html',
  'Student Association EVP · evp@binghamtonsa.org · no phone published'),

 ('2026-08-24', 'Aug 24, 2026', 'Stony Brook · Buffalo · Albany · Cornell · RIT',
  'FIVE CAMPUSES START ON THE SAME DAY — the main upstate/Long Island wave',
  'Stony Brook (M–F classes; Sat classes Aug 29), University at Buffalo (15-week session, add/drop Aug 31), '
  'University at Albany (add without permission Aug 31), Cornell (add/drop deadline Sep 8), and RIT (add/drop '
  'Aug 31). ⚠ RIT IS ON SEMESTERS, NOT QUARTERS — it starts with everyone else, not five weeks later. Four '
  'of the five take fall break Oct 12–13; Cornell takes Oct 10–13.',
  'https://www.stonybrook.edu/registrar/academic-calendar/fall2026-summer2027.html',
  'Stony Brook Conference Services (631) 632-1930 · UB University Events (716) 645-6147 · UAlbany '
  '(518) 442-3300 · Cornell Student Activities (607) 255-4169 · RIT (585) 475-2952'),

 ('2026-08-26', 'Aug 26, 2026 — ⚠ UNVERIFIED', 'Fordham University',
  '⚠ FORDHAM CLASSES BEGIN (third-party source only)',
  'This date comes from acadcalendar.com, NOT from Fordham. Fordham\'s official calendar is a JavaScript grid '
  'that renders no data, six fordham.edu URLs 302-redirect to a CAS login gateway, and Fordham\'s own '
  '"Important Dates" page STILL SHOWS 2024-25. Confirm by phone before relying on it. Add/drop reportedly '
  'ends Sep 3.',
  'https://acadcalendar.com/fordham-academic-calendar/',
  '⚠ NO FORDHAM NUMBER CONFIRMED — get main lines from fordham.edu/about/maps-and-directions/ in a browser'),

 ('2026-08-28', 'Aug 28, 2026', 'Baruch · Hunter · City College',
  '⚠ ALL THREE MANHATTAN CUNY CAMPUSES START — one date covers the whole cluster',
  'CUNY common calendar. Add deadline Sep 3; last day to drop without a "W" Sep 4. Baruch, Hunter and City '
  'College are within subway distance of each other and of NYU and Columbia — the densest target audience in '
  'the United States, and Columbia to City College is three stops on the 1 train.',
  'https://our.catalog.cuny.edu/pages/6v5vCLMZ3vBKXnNNscUh',
  'Baruch Student Life (646) 312-4550 · Hunter Student Activities (212) 772-4908 · CCNY main (212) 650-7000'),

 ('2026-08-28', 'Aug 28, 2026, 1:00–5:00 PM', 'Stony Brook University',
  '⚠⚠ SEAWOLVES BLOCK PARTY — THE BEST-DOCUMENTED FAIR IN NEW YORK, AND IT COLLIDES WITH THE CUNY START',
  'Academic Mall ("Seawolves\' Street"). Club tabling in TWO SHIFTS: 1:00–2:30 PM for Academic/Honor Society, '
  'Activism/Advocacy, Greek, Media and Sport clubs; 3:30–5:00 PM for Community Service, Cultural, Graduate, '
  'Religious, Leisure and Performance orgs. Department tabling runs continuously 1–5 PM. OUTSIDE ORGS ARE NOT '
  'ADMITTED — the paid third-party route is a revocable permit through Conference Services instead. '
  '⚠ HARD CONFLICT: this is the same day all three Manhattan CUNY campuses begin classes. Long Island and '
  'Manhattan cannot both be covered.',
  'https://www.stonybrook.edu/commcms/studentaffairs/sac/Get_Involved/Clubs_and_Organizations/involvement_fairs.php',
  'Student Engagement & Activities · studentengagement@stonybrook.edu · (631) 632-9392 · Union Suite 205'),

 ('2026-09-02', 'Sep 2, 2026', 'New York University',
  'NYU CLASSES BEGIN — second-latest start in the state',
  'Labor Day holiday falls Sep 7, five days AFTER classes start. Stern Langone evening/weekend classes begin '
  'Sep 14. Term runs to Dec 22 — the longest tail in New York after Columbia. ⚠ Add/drop deadline is not '
  'published on the CAS calendar PDF.',
  'https://bulletins.nyu.edu/undergraduate/arts-science/academic-calendar/academic-calendar.pdf',
  'NYU Tandon Student Life (646) 997-3600 — the ONLY NYU number confirmable; every www.nyu.edu page 405s'),

 ('2026-09-05', 'Sat Sep 5, 2026', 'Cornell University',
  '⚠ CORNELL CLUBFEST — CONFIRMED. Arts Quad, two sessions',
  'Session One 12:00–1:30 PM, Session Two 2:00–4:00 PM; Barton Hall is the rain venue. Organisations '
  'self-identify their category and are assigned ONE session, so check which one Cornell Blockchain draws '
  'before choosing a slot. OUTSIDE ORGS MAY NOT TABLE — "outside organizations/vendors/businesses are not '
  'permitted to conduct business on campus, including tabling" — but walking it is the fastest way to meet '
  'Cornell Blockchain in person. ⚠ The registration deadline is referenced but NOT PRINTED.',
  'https://scl.cornell.edu/clubfest',
  'studentunion@cornell.edu (no phone) · Office of Student Activities (607) 255-4169'),

 ('2026-09-08', 'Sep 8, 2026', 'Columbia University',
  '⚠ COLUMBIA CLASSES BEGIN — LATEST START IN NEW YORK',
  'Three weeks after Binghamton. "Classes begin for the 273rd academic year." Change of Program (add/drop) '
  'ends Sep 18. ⚠ Columbia has NO October fall break — the only autumn holiday is Election Day, Nov 3 — so it '
  'runs at FULL DENSITY Sep 8 through Nov 24, the best sustained window in the state. Term runs to Dec 23.',
  'https://bulletin.columbia.edu/columbia-college/academic-calendar/academic-calendar.pdf',
  'AVP Event Management · sm4534@columbia.edu · (212) 853-1479'),

 ('2026-09-08', 'Thursdays, Sep 8 – Dec 11, 2026, 9:00 AM–12:15 PM', 'Columbia University',
  '⚠⚠ B8462 "BLOCKCHAIN & CRYPTOCURRENCIES" RUNS — THE BEST-DOCUMENTED DOOR IN NEW YORK',
  'Kravis 840. Huberman and Malekan. FOURTEEN THURSDAY MORNINGS in front of an MBA finance audience, with '
  'INDUSTRY GUEST SPEAKERS ALREADY BUILT INTO THE SYLLABUS. It is a classroom, not a tabling permit: no '
  'facility policy, no sponsor, no fee, no insurance. Malekan is an eight-year crypto industry veteran who '
  'books outside speakers as a matter of routine. THE ONLY COURSE IN THE ENTIRE NEW YORK PACKET CONFIRMED TO '
  'RUN IN FALL 2026. ⚠ His email is obfuscated on the CBS page — route via the Business School faculty office '
  'or the Columbia FinTech and Blockchain Club.',
  'https://courses.business.columbia.edu/B8462',
  'Omid Malekan, 570 Kravis — email obfuscated, no phone published; try Event Mgmt (212) 853-1479'),

 ('2026-09-11', 'Fri Sep 11, 2026 — ⚠ INFERRED', 'Columbia University',
  '⚠ COLUMBIA ACTIVITIES DAY (probable date)',
  'Low Plaza, Butler Plaza and College Walk, 12:00–4:00 PM, 300+ undergraduate student groups. The Fall 2025 '
  'instance was Friday Sep 5, 2025 — the pattern is the Friday of week one, which with a Sep 8 start gives '
  'Sep 11, 2026. NOT CONFIRMED: the Columbia College events mirror returns HTTP 403. Confirm with GS Student '
  'Life.',
  'https://www.gs.columbia.edu/events/activities-day-columbia-club-fair',
  'GS Student Life · AVP Event Management (212) 853-1479'),

 # ---- Traps and dead zones ----
 ('2026-09-07', 'Sep 7, 11, 12, 13 and 21, 2026', 'Baruch · Hunter · City College',
  '⚠⚠ THE CUNY SEPTEMBER DEAD ZONE — FIVE NO-CLASS DAYS IN THREE WEEKS',
  'No classes on Labor Day (Sep 7), Rosh Hashanah (Sep 11–13) and Yom Kippur (Sep 21) across all three '
  'Manhattan CUNY campuses. MID-SEPTEMBER IN CUNY IS SWISS CHEESE — a tour booked into it will find empty '
  'buildings. THE CLEAN WINDOWS ARE Aug 31 – Sep 4 AND EVERYTHING FROM SEP 22 ONWARD. Baruch club hours are '
  'Thursdays 12:40–2:20 PM every week, which is the single best recurring slot in the cluster.',
  'https://our.catalog.cuny.edu/pages/6v5vCLMZ3vBKXnNNscUh',
  'Baruch Student Life (646) 312-4550 · Hunter Student Activities (212) 772-4908'),

 ('2026-10-10', 'Oct 10–18, 2026', 'Binghamton University',
  '⚠⚠ BINGHAMTON EMPTIES — NINE-DAY FALL BREAK WITH THE RESIDENCE HALLS CLOSED',
  'Halls close 10 a.m. Sat Oct 10 and reopen 2 p.m. Sun Oct 18. This is NOT a two-day SUNY breather like '
  'Stony Brook, Buffalo, Albany or RIT (all Oct 12–13) — the students physically leave. DO NOT SCHEDULE '
  'BINGHAMTON INTO OCT 10–18.',
  'https://www.binghamton.edu/academics/academic-calendar.html',
  'The Union · bengaged@binghamton.edu · Catering (607) 777-2925'),

 ('2026-10-12', 'Oct 12–13, 2026', 'Stony Brook · Buffalo · Albany · RIT (Cornell Oct 10–13)',
  'FALL BREAK — four campuses out the same two days; Cornell out four days',
  'The standard SUNY two-day break. Cornell runs Oct 10–13. NYU takes Oct 12 plus a "Legislative Day" Oct 14 '
  'on which Monday classes meet — that is a full-density day, not a break. Columbia and Fordham have no '
  'October break at all.',
  'https://www.rit.edu/calendar',
  'RIT (585) 475-2952 · Stony Brook (631) 632-9392 · UB (716) 645-2055 · UAlbany (518) 442-3300'),

 # ---- Lead-time gates, by how far ahead they must be started ----
 ('', 'Start 20 business days out — Binghamton', 'Binghamton University',
  '⚠ BINGHAMTON LEAD TIMES AND THE $75 VENDOR FEE — AND THE ANTI-FRONTING PENALTY FALLS ON THE CLUB',
  '"EXTERNAL ORGANIZATIONS MUST BE SPONSORED BY A UNIVERSITY RECOGNIZED DEPARTMENT OR STUDENT ORGANIZATION AND '
  'MAY BE SUBJECT TO A $75 VENDOR FEE." Outdoor TABLING requires at least 15 BUSINESS DAYS; outdoor logistics '
  '10 business days, or 20 business days where extra campus support is needed; large events require MEETING '
  'CATHERINE FAUGHNAN AT LEAST THREE WEEKS PRIOR. ⚠⚠ FRONTING IS POLICED AND THE CLUB PAYS: "Groups may not '
  'hold reservations for other groups. If you are found to be holding a reservation for another group, BOTH '
  'GROUPS WILL RISK LOSING B THERE REQUEST ACCESS." Sitting above all of it, Policy 203: "NO AUTHORIZATION '
  'WILL BE GIVEN TO PRIVATE COMMERCIAL ENTERPRISES TO OPERATE ON UNIVERSITY CAMPUSES." Ask for the Director '
  'of the University Union and the Director of Procurement BY TITLE — neither is named or has a phone.',
  'https://www.binghamton.edu/services/union/events-and-reservations/reservation-guidelines.html',
  'Catherine Faughnan, Asst Director, The Union · cfaughn@binghamton.edu · no phone published'),

 ('', 'Start 15 business days out — City College', 'CUNY City College of New York',
  '⚠ CCNY EXTERNAL-ORG TABLING: 15 BUSINESS DAYS AND A VETTING PROCESS — BUT NO MONEY MAY MOVE',
  'THE CLEAREST EXTERNAL-ORG PATHWAY IN CUNY, verbatim: for tabling requests involving external organizations '
  'clubs must submit within 15 business days and the department will "REQUEST ADDITIONAL INFORMATION ON THE '
  'EXTERNAL ORGANIZATION TO VET THEM AND TO ENSURE THEIR AUTHENTICITY AND ITS APPROVAL BY THE COLLEGE." '
  'Ordinary club tables need 10 business days, first-come. ⚠⚠ AND THEN: "AS OF FALL 2023, FUNDRAISING TO '
  'INCREASE CLUB FUNDING IS PROHIBITED" — clubs "cannot accept any form of payments" — and campus-wide "CASH '
  'TRANSACTIONS ARE PROHIBITED." External groups must also show "SIGNIFICANT CCNY INTEREST" and alignment '
  'with the college\'s "mission, goals, and ideals." An education-only posture is the only one available — '
  'which is what the BitLicense forces anyway, so nothing is lost. ⚠ The Beaver Handbook prints NO phone '
  'numbers at all.',
  'https://www.ccny.cuny.edu/sites/default/files/2026-01/2025%20-%202026%20CCNY%20Student%20Club%20handbook.pdf',
  'clubreg@ccny.cuny.edu · NAC 1/210 · main line (212) 650-7000 — no direct number published'),

 ('', 'Start 14 business days out — Buffalo', 'University at Buffalo',
  '⚠ UB: THE STUDENT UNION IS CLOSED TO YOU — GO TO UNIVERSITY EVENTS INSTEAD',
  '"NON-UNIVERSITY GROUPS MAY NOT RESERVE CLASSROOM AND GENERAL CAMPUS SPACE THROUGH THE STUDENT UNIONS" — '
  'those interested are directed to University Events. Union reservations need 14 BUSINESS DAYS and a signed '
  'request; cancellation less than two business days out costs $30 PER SPACE. NO RATE CARD is published for '
  'non-University groups anywhere — get a written quote. SEPARATE AND POSSIBLY BETTER PLAY: UB\'s Sponsorship '
  'and Advertising Policy prohibits firearms, tobacco and illegal goods and says NOTHING about cryptocurrency '
  'or financial products; anything under $25,000 is a UNIT-LEVEL decision ($25k–$50k goes to the VP for '
  'Advancement, over $50k to the Sponsorship Advisory Committee). Complete the Corporate Sponsorship Request '
  'Form BEFORE approaching anyone. ⚠ Keep the message acknowledgement-shaped: "qualitative or comparative '
  'language, price information" converts sponsorship into ADVERTISING, which is taxable UBIT income to UB.',
  'https://www.buffalo.edu/studentlife/who-we-are/departments/student-unions/non-academic-event-reservations.html',
  'Amy Veiders, Assoc Dir University Events (716) 645-3414 · office (716) 645-6147 · Geoffrey Bartlett, AVP '
  'Corporate & Foundation Relations (716) 881-8203'),

 ('', 'Start 10 working days out — Columbia', 'Columbia University',
  '⚠ COLUMBIA: TEN WORKING DAYS, MANDATORY SPONSOR — AND NO SPONSOR EXISTS FOR A COMMERCIAL ENTITY',
  '"ALL EVENTS REQUIRE A RESERVATION AND ADVANCE APPROVAL"; special events need "ten working days advance '
  'notice." Non-affiliates must have a University department sponsor, and the policy PRESCRIBES the sponsor '
  'office for nonprofit, civic, political and governmental groups (Office of Government Relations and '
  'Community Affairs) — ⚠⚠ AND NAMES NONE FOR A FOR-PROFIT COMMERCIAL ENTITY. That silence is not permission. '
  'Columbia may also "LIMIT ANY EVENT TO UNIVERSITY ID HOLDERS," and non-affiliates must print on all '
  'materials, in comparable font size: "THIS EVENT IS NOT AFFILIATED WITH, ENDORSED BY, OR SPONSORED BY '
  'COLUMBIA UNIVERSITY." Ask Event Management the one useful question: which office sponsors a commercial '
  'non-affiliate?',
  'https://universitypolicies.columbia.edu/content/university-event-policy',
  'AVP Event Management · sm4534@columbia.edu · (212) 853-1479'),

 ('', 'Start 3 business days out — Albany', 'University at Albany',
  '⚠ UALBANY: A FREE THIRD-PARTY PUBLIC FORUM — FOR NON-COMMERCIAL SPEECH ONLY',
  'Policy 1.6 (adopted 7/11/2019, amended 8/17/2023): third parties apply to the Office of Facilities '
  'Management AT LEAST THREE BUSINESS DAYS ahead and the university must respond by close of business on the '
  'third business day prior. ⚠⚠ THE INSTITUTION CANNOT CHARGE APPLICATION FEES, USAGE FEES, INSURANCE '
  'REQUIREMENTS OR SECURITY COSTS — the only terms like that in New York — and will provide a microphone on '
  'written request; megaphones prohibited. BLACKOUTS: opening weekend, exam periods, graduation and '
  'Homecoming. ⚠ BUT the freedom-of-speech page conditions third-party use on SUNY\'s policy for NON-COMMERCIAL '
  'organisations (5603), so DGD-the-issuer does not qualify — a STUDENT advocate does. Separately: the three '
  'Campus Center tabling spots are "restricted to recognized student organizations, University departments or '
  'offices," and "non-affiliated entities must obtain a revocable permit from the OFFICE OF THE CONTROLLER," '
  'for which NO PHONE NUMBER IS PUBLISHED ANYWHERE.',
  'https://www.albany.edu/risk-management-compliance/policy/public-forum-time-manner-and-place-rules',
  'Stacy Stern, Office of Facilities Management · (518) 442-3400 · main line (518) 442-3300'),

 ('', 'Start 48 hours out — Hunter', 'CUNY Hunter College',
  '⚠ HUNTER HAS THE SHORTEST OUTSIDE-ENTITY LEAD TIME IN NEW YORK — 48 HOURS',
  '"REQUEST FOR VENDOR SERVICES OR VISITORS SHOULD BE SENT TO THE VISITOR\'S CENTER '
  '(visitors@hunter.cuny.edu) AT LEAST 48 HOURS PRIOR TO ARRIVING ON CAMPUS." Against Columbia\'s ten working '
  'days and Binghamton\'s fifteen business days, that is remarkable — but it is a VISITOR CLEARANCE, NOT A '
  'COMMERCIAL-TABLING PERMIT, and the underlying authority is still CUNY 4.02 category 6 ("may permit"). Only '
  'a registered club\'s named officers (President, VP, Treasurer, Secretary) may reserve space. Budget the AV '
  'floor: tech support is "50/hr. with a 5-hour minimum" = $250, plus possible Public Safety, Cleaning and '
  'Event Host charges. ⚠ Hunter\'s Solicitation of Funds policy TEXT COULD NOT BE RETRIEVED and is the '
  'document most likely to carry a commercial prohibition — get it in a browser first.',
  'https://www.hunter.cuny.edu/central-reservations-and-events/reservation-information/student-organizations/',
  'Office of Student Activities (212) 772-4908 (direct) · main line (212) 772-4000 · '
  'visitors@hunter.cuny.edu'),

 ('', 'No published lead time — Stony Brook', 'Stony Brook University',
  '⚠⚠ STONY BROOK: PAY THE PERMIT, DO NOT ROUTE THROUGH A CLUB — THE ANTI-FRONTING CLAUSE IS AUTOMATIC',
  'Use of Campus Facilities Policy (eff. 07/26/2024): third-party use requires A REVOCABLE PERMIT THROUGH '
  'CONFERENCE SERVICES; "the University must be reimbursed for ALL COSTS INCURRED"; insurance must name "THE '
  'STATE OF NEW YORK, THE STATE UNIVERSITY OF NEW YORK" as additional insureds — ⚠ NO DOLLAR LIMIT AND NO '
  'RATE CARD ARE PUBLISHED, so get both in writing. ⚠⚠ THE DECISIVE CLAUSE: "IF ANY REVENUE GENERATED FROM '
  'THE USE OF FACILITIES IS RECEIVED BY AN EXTERNAL ORGANIZATION OR INDIVIDUAL FOR ITS OWN BENEFIT, THE USE '
  'OF CAMPUS FACILITIES IS NOT A UNIVERSITY USE." A club booking a room for a DGD sign-up drive is '
  'RECLASSIFIED as paid third-party use by operation of the policy — sponsorship buys nothing and endangers '
  'the club. Also: "RAFFLES AND OTHER GAMES OF CHANCE ARE NOT PERMITTED"; student activities may solicit only '
  'with WRITTEN AUTHORIZATION from the VP for Student Affairs; anything projecting over $1,000 goes through '
  'Advancement.',
  'https://www.stonybrook.edu/policy/policies/use_of_campus_facilities_policy.php',
  'Conference & Event Services (631) 632-1930 · Enterprise Risk Mgmt (631) 632-9500 · Advancement '
  '(631) 632-6300 · VP Student Affairs (631) 632-6700 · Procurement (631) 632-6010'),

 # ---- Monitor-only: the doors that are not campus doors ----
 ('', 'Monitor — the best private door in the state', 'Cornell University',
  '⚠⚠ SPONSOR THE CORNELL BLOCKCHAIN CONFERENCE — IT SIDESTEPS THE FLATTEST BAN IN NEW YORK',
  'Cornell\'s tabling policy is absolute: "OUTSIDE ORGANIZATIONS/VENDORS/BUSINESSES ARE NOT PERMITTED TO '
  'CONDUCT BUSINESS ON CAMPUS, INCLUDING TABLING," with no fee tier and no sponsorship cure — the "sponsoring '
  'organization must be physically on site" clause governs a club\'s OWN table, not a vendor\'s. Policy 4.3\'s '
  'only aperture is "limited seasonal or thematic sales" through the 4C committee, which is a craft-fair door. '
  'SO GO THROUGH THE STUDENTS. Cornell Blockchain (founded 2017, a registered student organisation) TEACHES '
  'ITS OWN COURSES — CS-1998 has educated 300+ undergraduates, CS-4998 covers Solidity and Hardhat — runs a '
  'Brooklyn high-school bootcamp, operates an accelerator, and has hosted an ANNUAL CONFERENCE SINCE 2019 '
  'WITH AN EXISTING SPONSOR ROSTER. A student-run conference is a private event with its own pipeline. '
  '⚠ The 2026 conference homepage returns HTTP 404; the 2025 sponsors page is indexed.',
  'https://www.cornellblockchainconference.com/sponsors',
  'cornellblockchain@gmail.com · Office of Student Activities (607) 255-4169 · University Licensing '
  '(607) 255-6074'),

 ('2027-04-24', 'Watch for the 2027 edition (2026 was Apr 24)', 'Cornell Tech, New York City',
  '⚠ AI BLOCKCHAIN CONFERENCE — "THE PROGRAMMABLE ECONOMY" — GET ON THE SPONSOR LIST EARLY',
  'Held at Cornell Tech in New York City across the Verizon Executive Education Center (9am–5pm) and the Tata '
  'Innovation Center (from 12pm), closing reception 5:30–7:00 PM. Sessions on blockchain infrastructure, '
  'digital assets, payments, stablecoins, institutional crypto adoption, wealth management and securities '
  'markets. THE APRIL 24, 2026 EDITION HAS PASSED relative to a Fall 2026 tour. It is a subway ride from the '
  'Manhattan cluster rather than four hours to Ithaca.',
  'https://www.aiblockchaincornelltech.org/agenda',
  'Blockchain @ Cornell Tech · cornellblockchain@gmail.com'),

 ('', 'Monitor — NYU', 'New York University',
  '⚠ THE NYU BLOCKCHAIN CONFERENCE IS THE ONLY NYU DOOR THAT DOES NOT REQUIRE SOLVING THE 405 PROBLEM',
  'Student-run, inaugural edition Nov 1, co-hosted by NYU Blockchain & Fintech and NYU Blockchain Society. A '
  'private student event with its own sponsorship pipeline; it engages no NYU facility policy. This matters '
  'because EVERY PAGE ON www.nyu.edu RETURNS HTTP 405 to research tooling — the Kimmel Center tabling policy, '
  'the Center for Student Life directory and the Fall 2026 Club Fest page are all unreadable, so NYU\'s '
  'access rating is provisional and means nothing. Second door: David Yermack (dy1@stern.nyu.edu), the most '
  'prominent crypto academic in New York — but note his flagship course FINC-GB.3324 runs in SPRING, not '
  'Fall.',
  'https://www.nyubnf.com/',
  'NYU Tandon Student Life (646) 997-3600 — the only confirmable NYU number'),

 ('', 'Monitor — RIT strategic context', 'Rochester Institute of Technology',
  '⚠ ROCHESTER IS A WORKING CRYPTO TOWN — FOUNDRY IS HEADQUARTERED THERE AND HAS ALREADY TAUGHT AT RIT',
  'Foundry, one of the largest bitcoin mining and staking operations in North America (a Digital Currency '
  'Group company), is headquartered in Rochester and CO-BUILT AND DELIVERED A CRYPTOCURRENCY AND BLOCKCHAIN '
  'COURSE WITH RIT CERTIFIED, taught by Jonathan S. Weissman of Golisano College. If the play is a co-branded '
  'educational programme rather than a table, RIT Certified is a counterparty that has already done exactly '
  'that deal once. Combined with the $60 vendor table and an active Blockchain Technology Club, RIT is the '
  'strongest overall stop in New York.',
  'https://www.rit.edu/news/rit-certified-and-foundry-collaborate-cryptocurrency-course',
  'Jackie Zysk (585) 475-2952 · Jonathan Weissman — no email or phone published on the RIT directory'),

 # ---- Documentation blackouts to close by hand ----
 ('', 'Before anyone travels to the Bronx', 'Fordham University',
  '⚠⚠ FORDHAM IS A TOTAL DOCUMENTATION BLACKOUT — ONE HOUR IN A BROWSER BEFORE ANY DECISION',
  'NOT ONE FORDHAM PHONE NUMBER IS CONFIRMED — the only campus in New York with zero. Six fordham.edu URLs '
  'all 302-redirect to loginp.fordham.edu/cas/login: the Office for Student Involvement and its staff page, '
  'the Dean of Students pages, the McShane/McGinley Campus Center pages, and registration information. Every '
  'Fall 2026 date rests on a THIRD-PARTY AGGREGATOR. Fordham\'s own "Important Dates" page STILL SHOWS '
  '2024-25. The USG club-fair page is robots-blocked. Both club directories are gated. 411.fordham.edu is not '
  'a directory — it is extension-dialling instructions with no numbers on it. GET: both campus main lines, '
  'the Office for Student Involvement number, the six Fall 2026 dates, and whether any finance or blockchain '
  'club exists. ⚠ On substance the Student Handbook permits distribution only by registered student orgs or '
  'by students "sponsored by a University club, office, or department" — THERE IS NO CATEGORY FOR AN OUTSIDE '
  'ENTITY. If the hour returns nothing, skip Fordham.',
  'https://www.fire.org/colleges/fordham-university/student-handbook-distribution-literature',
  '⚠ NO FORDHAM NUMBER CONFIRMED — start at fordham.edu/about/maps-and-directions/'),

 ('', 'Before any CUNY or Baruch commitment', 'All CUNY campuses',
  '⚠ THREE CUNY DOCUMENTS ARE BLOCKED TO TOOLING AND A HUMAN SHOULD READ THEM',
  'CUNY\'s primary Facility Use Policy PDF and CUNY Bylaws Article XV are BOTH ROBOTS-BLOCKED. Baruch\'s '
  'Zicklin faculty directory FAILS SSL VERIFICATION (CERTIFICATE_VERIFY_FAILED) — which is why NO BARUCH '
  'FACULTY MEMBER AND NO BARUCH COURSE IS NAMED IN THIS PACKET despite Baruch having the strongest finance '
  'audience in New York. Hunter\'s registrar calendar and club directory both return HTTP 403. The operative '
  'systemwide document that WAS retrievable is CUNY Policy 4.02 (BOT 12/04/2017): commercial users are '
  'category 6 and "colleges SHALL permit use under categories 1 through 5 and MAY permit use under category '
  '6." CUNY insurance tiers: $500k low-risk, $1M/$2M standard, $2M–$5M high-risk; broker InterCity Agency '
  '718-279-7705.',
  'https://policy.cuny.edu/wp-content/uploads/sites/6/page-assets/general-policy/Policy-4.02-Facilities-Use-approved-by-BOT-120417.pdf',
  'Baruch Student Life (646) 312-4550 · Hunter (212) 772-4908 · CCNY (212) 650-7000'),

 ('', 'Do not let an ambassador say this', 'All New York campuses',
  '⚠⚠ THERE IS NO NEW YORK CAMPUS FREE-SPEECH STATUTE — DO NOT CITE ONE',
  'Unlike Oklahoma (70 O.S. s 2120), Wisconsin, Arizona, Florida and roughly twenty other states, NEW YORK '
  'HAS NOT ENACTED A CAMPUS FREE-EXPRESSION STATUTE for SUNY or CUNY. SUNY\'s own 2021 legislative survey '
  'catalogues seventeen-plus other states and discusses NO New York bill; A2309 (2023) was introduced, not '
  'enacted. What New York does have is ARTICLE 129-A of the Education Law — the HENDERSON ACT — which '
  'REQUIRES every college, public AND private, to adopt and file rules for the maintenance of public order. '
  'IT IS A RESTRICTION MANDATE AND IT IS THE STATUTE USED TO EJECT PEOPLE: under SUNY\'s implementation '
  '(Doc 3653, eff. 6/10/2009) the president must tell a non-affiliated violator they are "NOT AUTHORIZED TO '
  'REMAIN ON THE PROPERTY" and direct them to leave, with ejection and trespass or loitering prosecution to '
  'follow. SUNY and CUNY publics are still bound by the First Amendment as state actors, but commercial '
  'speech gets intermediate scrutiny and every fee and approval in this packet is lawful. NYU, Columbia, '
  'Cornell, RIT and Fordham are PRIVATE and owe nothing at all.',
  'https://www.suny.edu/sunypp/documents.cfm?doc_id=351',
  'SUNY systemwide policy portal — https://www.suny.edu/sunypp/'),
]
