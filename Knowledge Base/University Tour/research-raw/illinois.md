# ILLINOIS — DGD Campus Tour Research, Fall 2026 (Sept–Dec 2026)

Research date: August 12, 2026. Ten campuses, priority order as assigned.

**RESEARCH-TOOLING CONSTRAINT — READ FIRST.** This session's WebSearch budget was
exhausted before Illinois research began (200/200 calls used by prior states). All
findings below were obtained by direct WebFetch against known and inferred URLs plus
site-navigation crawling. Every general-purpose search engine tested was unavailable to
the tooling: `duckduckgo.com/html` (robots.txt fetch failure), `lite.duckduckgo.com`
(same), `bing.com` (robots-disallowed), `mojeek.com` (robots-disallowed). Direct `curl`
was blocked by the session's egress proxy (CONNECT 403). **Consequence: gaps in this
document are disproportionately "could not find the URL," not "the university does not
publish it."** Where that is the case it is stated explicitly. This is a real limitation
and an ambassador should treat the phone numbers below as the primary instrument.

---

## THE ILLINOIS PLANNING STORY IN ONE PARAGRAPH

**Chicago is the densest campus cluster in the United States after Manhattan.** Five of
these ten campuses — UIC (West Loop/Near West Side), DePaul (Lincoln Park + Loop), Loyola
(Rogers Park + Water Tower), the University of Chicago (Hyde Park) and Illinois Tech
(Bronzeville/Mies campus) — are inside the Chicago city limits, and Northwestern sits in
Evanston immediately north on the Purple Line. Six of ten campuses are reachable from one
hotel room on CTA. The remaining four are outstate: Urbana-Champaign (~2h15m south),
Normal (~2h15m southwest), DeKalb (~1h15m west) and Carbondale (~5h30m south, effectively
a separate trip). **But the cluster is defeated by the calendar.** Northwestern, DePaul and
the University of Chicago are on QUARTERS; UChicago's autumn quarter does not begin until
**Monday, September 28, 2026** and ends **Saturday, December 12** — before Christmas. A
tour built around the semester wave (Aug 17 / Aug 24 starts) will arrive in Hyde Park five
weeks before anyone is there. **Illinois needs two Chicago trips, not one:** a late-August
semester trip (UIC, Loyola, IIT) and a late-September/October quarter trip (Northwestern,
DePaul, UChicago).

---

## STATE-LEVEL LEGAL FINDINGS (apply to every campus in this packet)

### 1. ⚠⚠ BIPA — Biometric Information Privacy Act, 740 ILCS 14 — HIGH PRIORITY

The single most dangerous statute in the United States for an ID-scanning or
facial-recognition KYC step at a table. It is the **only** US biometric statute with a
private right of action and per-violation statutory damages, and it has generated
nine-figure class settlements.

**§ 15(b)** — verbatim, from FindLaw's reproduction of the current text
(https://codes.findlaw.com/il/chapter-740-civil-liabilities/il-st-sect-740-14-15/):

> "No private entity may collect, capture, purchase, receive through trade, or otherwise
> obtain a person's or a customer's biometric identifier or biometric information, unless
> it first: (1) informs the subject or the subject's legally authorized representative **in
> writing** that a biometric identifier or biometric information is being collected or
> stored; (2) informs the subject … **in writing of the specific purpose and length of
> term** for which a biometric identifier or biometric information is being collected,
> stored, and used; and (3) **receives a written release** executed by the subject …"

**§ 15(a)** — retention schedule:

> "A private entity in possession of biometric identifiers or biometric information must
> develop a **written policy, made available to the public,** establishing a retention
> schedule and guidelines for permanently destroying biometric identifiers and biometric
> information when the initial purpose for collecting or obtaining such identifiers or
> information has been satisfied or **within 3 years of the individual's last interaction**
> with the private entity, whichever occurs first."

**§ 15(c)** — no profiting:

> "No private entity in possession of a biometric identifier or biometric information may
> **sell, lease, trade, or otherwise profit from** a person's or a customer's biometric
> identifier or biometric information."

**§ 15(e)** — storage: reasonable standard of care within the industry, and protection
"in a manner that is the same as or more protective than the manner in which the private
entity stores, transmits, and protects other confidential and sensitive information."

**§ 20 — Right of action** (https://codes.findlaw.com/il/chapter-740-civil-liabilities/il-st-sect-740-14-20/):

> "Any person aggrieved by a violation of this Act shall have a right of action … A
> prevailing party may recover for each violation: (1) against a private entity that
> **negligently** violates … liquidated damages of **$1,000** or actual damages, whichever
> is greater; (2) against a private entity that **intentionally or recklessly** violates …
> liquidated damages of **$5,000** or actual damages, whichever is greater; (3) reasonable
> attorneys' fees and costs, including expert witness fees …"

**§ 20(b)–(c)** carry the 2024 amendment limiting repeat collections of the *same*
identifier from the *same* person by the *same* method to a single recovery. That caps
per-person exposure; it does **not** cap per-person-count exposure. Two hundred students
scanned at a table is still 200 potential claims.

**§ 10 definitions** (https://codes.findlaw.com/il/chapter-740-civil-liabilities/il-st-sect-740-14-10/):
"biometric identifier" = "a retina or iris scan, fingerprint, voiceprint, or scan of hand
or face geometry," expressly **excluding** writing samples, photographs and demographic
data. "Written release" = "informed written consent, electronic signature, or, in the
context of employment, a release executed by an employee as a condition of employment."
"Private entity" excludes government agencies and courts — **DGD is a private entity.**

**Operational meaning for a DGD table in Illinois:** a photograph of a driver's licence is
outside the definition; a *face-geometry scan* derived from it is inside it. Any liveness
check, selfie-match, face-match-to-ID or fingerprint step in an onboarding flow run on
Illinois soil requires a signed written release, a published retention policy, and a
no-sale commitment — before the first scan. Section 10's photograph carve-out has been
read narrowly by Illinois courts, so do not rely on it.

### 2. ⚠⚠ Digital Assets and Consumer Protection Act, 205 ILCS 731 (P.A. 104-428, effective August 18, 2025)

Illinois now has a **digital-asset business registration regime**, and the operative
sentence reaches marketing, not just transacting.

**§ 15-5** (https://law.justia.com/codes/illinois/chapter-205/act-205-ilcs-731/article-15/):

> "A person shall not engage in digital asset business activity, **or hold itself out as
> being able to engage in digital asset business activity,** with or on behalf of a
> resident unless the person is registered."

"Digital asset business activity" (Article 1) = "exchanging, transferring, or storing a
digital asset as part of a business or on behalf of a customer," digital asset
administration, and other activity the Department designates. **Express exclusions:**
peer-to-peer exchanges, decentralized exchanges, software development, NFT issuance, and
blockchain validation. Registration is with IDFPR, application fee **"$5,000 or greater,
nonrefundable,"** and registration is effective only on the later of Department issuance
or posting of the Section 20-5 security. Effective date confirmed at Article 99: "This Act
takes effect upon becoming law," P.A. 104-428, 8-18-25.

**Operational meaning:** an ambassador standing behind a DGD banner in Illinois telling a
student that DGD can hold, transfer or exchange their digital assets is arguably "holding
itself out as being able to engage in digital asset business activity … with a resident."
Get legal sign-off on registration status **before** the first Illinois table, and know
which side of the peer-to-peer / decentralised exclusions DGD's product sits on.

Companion Illinois statutes, all in Chapter 205 (https://law.justia.com/codes/illinois/chapter-205/):
- **205 ILCS 732 Digital Asset Kiosks Act** — regulates crypto ATMs/kiosks. Relevant only
  if DGD ever puts hardware on or near a campus.
- **205 ILCS 730 Blockchain Technology Act** and **205 ILCS 725 Blockchain Business
  Development Act** — enabling/friendly statutes, useful framing in conversation with
  faculty, of no help at a permit desk.
- **205 ILCS 658 Uniform Money Transmission Modernization Act** — replaced the Transmitters
  of Money Act (205 ILCS 657, repealed by P.A. 103-991). Article II definitions and
  Article V licensing were not retrievable in full to the tooling; the statutory text
  pages on Justia returned tables of contents only. **GAP: confirm whether DGD's flow is
  money transmission under 205 ILCS 658 separately from DACPA registration.** Note that
  Illinois's older IDFPR "Digital Currency Regulatory Guidance" (2017) is superseded in
  substance by DACPA; the 2017 guidance page could not be located at any tested IDFPR URL
  (idfpr.illinois.gov returned no digital-currency links from its homepage).

### 3. ⚠ Credit Card Marketing Act of 2009, 110 ILCS 26 — the on-campus financial-product statute

This is the Illinois statute that regulates marketing financial products to students **on
campus**, and it is largely unknown outside Illinois
(https://law.justia.com/codes/illinois/chapter-110/act-110-ilcs-26/):

- "credit card marketing activity" = **"any action designed to promote the completion of an
  application by a student to qualify to receive a credit card."**
- **"No institution of higher education shall knowingly allow on its campus credit card
  marketing activity that involves the offer of gifts, coupons, or other tangible personal
  property."**
- Institutions may not release student names, addresses, phone numbers, SSNs or emails
  for credit-card marketing purposes unless the student is 21 or older.
- Institutions entering credit-card agreements must make a financial education program
  available to all students, and must disclose issuer relationships conspicuously on their
  webpages and annually to the Illinois Board of Higher Education.
- **"The Attorney General may bring an action … to restrain and prevent any violation of
  this Act and seek penalties in amounts up to $1,000 per incident."**

**Operational meaning:** the statute is drafted around *credit cards*, so a pure token or
wallet pitch is outside it. But (a) if DGD's product line includes any card, the swag table
is the exact fact pattern the legislature banned — the duty falls on the *university*,
which is why a campus officer may refuse a table without being able to articulate why; and
(b) it explains the reflexive Illinois-administrator hostility to any financial-product
booth. Do not offer gifts/coupons/merch as an inducement to complete a card application in
Illinois. Related: **110 ILCS 115 University Credit and Retail Sales Act** bars state
institutions from operating retail stores competing with private merchants and from making
direct institutional credit sales (P.A. 102-781, eff. 5/13/2022, expanded course-material
credit) — background only, but it is the reason "sales on campus" is a fraught category in
Illinois public-university policy language.

### 4. ⚠ THERE IS NO ILLINOIS CAMPUS FREE-EXPRESSION STATUTE, AND THE BOUNDARY IS THE POINT

A full read of the acts in Chapter 110 (Higher Education) found **no FORUM-Act-style
campus free-expression statute** — nothing resembling the Oklahoma, Texas or Florida
statutes that declare outdoor campus areas public forums. What Illinois has instead:

- **110 ILCS 10 — Campus Demonstrations Policy Act.** Substantively thin. §2: "The
  administration of each State-supported institution of higher learning is responsible for
  maintaining decorum and order on the campus of that institution." §1 asks for a "Policy
  on Demonstrations" that is "an outline of rules and regulations to maintain order on the
  campus" with "special attention to firmness." **This statute is an order-maintenance
  mandate, not a speech right.** It runs against DGD, not for it.
- **110 ILCS 13 — College Campus Press Act.** "All campus media produced primarily by
  students at a State-sponsored institution of higher learning is a public forum for
  expression by **the student journalists and editors** at the particular institution." It
  binds the named public universities (U of I, SIU, ISU, NIU and the rest) and community
  colleges. **It creates rights for student journalists in student media — not for outside
  commercial entities on the quad.** It is, however, the reason a paid ad in the *Daily
  Illini*, *Daily Northwestern* or *Chicago Maroon* is comparatively easy: editorial
  control sits with students, not administrators. That is a genuine and underused door.

**The operative point:** in Illinois, an ambassador has **no statutory forum right to
assert.** Every campus below may lawfully impose approval, fees, insurance and outright
commercial bans. Do not let anyone cite a "campus free speech law" in Illinois — there
isn't one that helps.

### 5. University of Illinois System — Board of Trustees General Rules (binds UIUC, UIC and UIS only)

https://www.bot.uillinois.edu/governance/general_rules — **Article V, Section 1**, applying
system-wide to Urbana-Champaign, Chicago and Springfield:

> "The use of system premises and facilities by individuals **other than in connection with
> educational or research programs** will be permitted **only under regulations formulated
> and administered by the appropriate chancellor/vice president and approved by the
> president.**"

Facility use agreements must "articulate the terms of use." The Board draws no
commercial/non-commercial line itself — it delegates entirely. **So at UIUC and UIC the
campus-level documents (Student Code Article 2 at Urbana, DOS-8100-004 at Chicago) are the
operative law, and there is no systemwide override to appeal to.** Reported once here;
cited once in the anchor campus record. It does **not** bind Northwestern, DePaul, Loyola,
UChicago, IIT, ISU, NIU or SIU.

---

# CAMPUS 1 — UNIVERSITY OF ILLINOIS URBANA-CHAMPAIGN (Public, semesters)

Champaign-Urbana, IL. ~56,000 students. Flagship; Grainger Engineering and Gies Business;
one of the top-5 CS programmes in the country by any ranking. Highest-value audience in
the state and, as it turns out, one of the hardest written policies.

## A. Academic calendar — Fall 2026 — CONFIRMED

Source: https://registrar.illinois.edu/academic-calendars/fall-2026-academic-calendar/

- **First day of instruction: Monday, August 24, 2026** — "First day of instruction for
  Fall POT 1 (full semester) and POT A (1st 8 week) courses."
- Add/drop, POT A (first 8 weeks): add by **August 28**; drop without W by **September 18**.
- Add/drop, POT 1 (full semester): add and drop for refund by **September 4**; drop without
  a W grade by **October 16**.
- POT B (second 8 weeks): add by **October 23**; drop without W by **November 13**.
- **Fall Break: November 21 – 29, 2026** — note this is a *nine-day* break spanning
  Thanksgiving, not a separate October break. Urbana empties for it.
- **Last day of instruction: Wednesday, December 9, 2026.**
- Reading day: **December 10** — "no classes, no final examinations."
- **Final examinations: December 11–17, weekdays only** (Law and Vet Med may extend to
  Dec 18). Degree conferral December 21.

**Access window:** Aug 24 → Nov 20 is one uninterrupted run with no mid-semester break.
That is the single best sustained access window of any campus in this packet.

## B. Involvement fair — Quad Day — PARTIAL

**Quad Day** is UIUC's involvement fair and one of the largest in American higher education
— roughly a thousand organisations on the Main and South Quads.

- **Welcome Week 2026: August 17–23, 2026** — CONFIRMED at
  https://newstudent.illinois.edu/orientation/welcomeweek
- That page places Quad Day on **August 22, 2026 (a Saturday)**. ⚠ **Treat this as
  PARTIAL.** The historical pattern is the *Sunday* before classes, which in 2026 is
  August 23. Aug 22 is a Saturday and Aug 23 a Sunday; both fall inside the confirmed
  Welcome Week window, so either is internally consistent and the page did not render an
  explicit weekday to the tooling. **Call New Student & Family Experiences at
  (217) 333-4057 and get the day.**
- The dedicated Quad Day site **quadday.illinois.edu did not resolve** for research tooling
  (robots.txt fetch failed: name resolution error). `union.illinois.edu/quad-day`,
  `/get-involved/quad-day` and `/quadday` all returned 404.
  `studentengagement.illinois.edu/quadday` returned a **zone/booth map and an alphabetised
  organisation index but no date, time, fee or eligibility statement.**
- **Can outside organisations table? NO PUBLISHED ANSWER, and the surrounding policy says
  no.** Quad Day booths are organised by RSO category on the zone map; the Illini Union's
  own tabling rule (below) restricts information tables to RSOs and university departments.
  Do not assume a purchasable booth exists. **Confirm by phone before travelling.**

## C. Solicitation / outside-vendor policy — the operative documents

UIUC's rules live in the **Student Code, Article 2** (which is university regulation, not
just student conduct) plus the **Campus Administrative Manual**.

**§ 2-506 Requirements and Limitations** — https://studentcode.illinois.edu/article2/part5/2-506/
This is the decisive provision. Prohibited uses **for outside organizations**:

> "**Solicitations, collections, fund drives, or any events for which an admission will be
> charged, even though the funds are for public benefit**"

Also in § 2-506:
> "All events to which the public will be invited and/or for which a fee will be charged
> must receive formal approval prior to the assignment of space."
> "If an outside organization requesting space has a local affiliate, **the local affiliate
> shall participate in the arrangements**."
> "University Property shall not be used for benefit events, charitable or otherwise,
> except with the special approval of the Chancellor."

**§ 2-502 Eligibility** — https://studentcode.illinois.edu/article2/part5/2-502/
Organizations under § 2-301 other than campus-community organizations, outside
organizations and individuals may use University Property. Outside organizations "shall be
similarly eligible **upon a finding by the facility Designated Official** that the proposed
event or activity is consistent with the rules and regulations referred to above." And:
"The university's grant of permission to use University Property **does not imply an
endorsement** of the purposes or viewpoints of the event or the sponsoring organization."

**§ 2-407 Posting and Distribution of Handout Materials** —
https://studentcode.illinois.edu/article2/part4/2-407/ — the sentence to have memorised:

> "Individuals may distribute written or printed materials regarding a **non-commercial**
> topic on a person-to-person basis in outdoor, publicly accessible areas of university
> property."
> "Individuals may post written or printed materials regarding any **non-commercial** topic
> on general campus bulletin boards and general campus kiosks."

Materials may not be affixed to statues, doors, light posts, walls, trees or trash cans.
**The distribution right on the Urbana quad is expressly limited to non-commercial topics.
A DGD flyer is commercial.**

**§ 2-406 Solicitation and Commercial Activity in University Residence Halls** —
https://studentcode.illinois.edu/article2/part4/2-406/ —
"Solicitation or commercial activity is prohibited in university residence halls except
under the following conditions": canvassers must register with the Dean of Students office
and Residential Life; activity only "between the hours of 2:00 p.m. and 10:00 p.m.";
"**Door-to-door canvassing is not permitted**"; "Canvassing is prohibited in dining rooms
and meal lines." Political canvassers "shall not solicit contributions or attempt to sell,
or advertise for purposes of sale, any item." **Residence halls are closed.**

**CAM FO-81 Reservation of University Property** — https://cam.illinois.edu/policies/fo-81/
Issued July 15, 2021; revised **August 21, 2024**. Contact: OVCFA@illinois.edu. Outside
applicants "should submit a reservation request to the Designated Official"; must enter
into a written **Facility Use Agreement (FUA)** and provide proof of insurance; must pay
"any applicable service charge and rental, equipment, staffing, security and cleaning
fees"; "the applicant charges admission or concession fees and **sells merchandise only as
permitted in the FUA**." Rates follow the Business and Finance Policy Manual. No dollar
figures published on the page.

**Illini Union Event Services policies** — https://union.illinois.edu/event-services-policies
- "**Registered Student Organizations and university departments** may reserve information
  tables" (Anniversary Plaza and vestibules).
- "**Solicitation is not permitted by any person or organization that did not reserve a
  table.**"
- "Goods (food, t-shirts, etc.) **may be sold only if the transaction is for the benefit of
  a Registered Student Organization**."
- Insurance: the Illini Union's Designated Official "will determine … if a certificate of
  insurance is required for any outside organization. If insurance is required, the outside
  organization must provide a certificate of insurance **naming the Board of Trustees as an
  additional insurer.**" No dollar limit published.
- All food and beverage through University Catering or an approved Illini Union Dining
  Partner.
- Contact: 217-333-0691, iueventservices@illinois.edu, 1401 W. Green St, Urbana IL 61801.

**Anti-fronting:** no clause using the word "fronting" was found at UIUC. But § 2-506's ban
on outside-organization solicitations *combined* with the Illini Union rule that goods may
be sold only "for the benefit of a Registered Student Organization" produces the same
result functionally: an RSO cannot rent its table to DGD and keep the arrangement lawful,
because the transaction must benefit the RSO, not the outside entity.

**Does sponsorship cure it?** **Not for solicitation.** § 2-506's prohibition attaches to
the *activity* (solicitations, collections, fund drives) when the user is an outside
organization; § 2-502 makes outside organizations eligible only on a Designated Official's
finding. A genuine RSO co-programme where the RSO plans and benefits is the only realistic
route, and it still cannot involve DGD soliciting.

**No language reaching payment credentials or on-site contract signing was found** in any
UIUC document retrieved.

## D. Relevant student clubs — INCONCLUSIVE, and honestly so

UIUC's directory is **one.illinois.edu/club_signup** (the "Illinois Student Org Directory,"
linked from https://studentengagement.illinois.edu/). It claims **1,127 groups**. Findings:

- The directory paginates alphabetically and **defeated keyword querying**: requests with
  `?search_word=blockchain` and `?keyword=blockchain` both returned the same default
  alphabetical first page (4 Paws for Ability → Alpha Epsilon Delta), i.e. the query
  parameters are ignored server-side and filtering is client-side JavaScript.
- Partial login-gating is visible: at least one group is marked "restricted to Some
  University of Illinois Urbana-Champaign users only," and a "Sign In" control is present.
- **On the pages that were machine-readable, no blockchain, cryptocurrency, Bitcoin, Web3
  or fintech organisation appeared.** The nearest finance-adjacent entries were Accounting
  Club, Actuarial Science Club and ALPFA Illinois.
- ⚠ **DO NOT record this as "UIUC has no blockchain club."** Only a fraction of 1,127
  entries was retrievable. This is a tooling gap, not a finding of absence. Close it by
  calling Student Engagement at **(217) 300-8757** and asking them to search the directory
  for "blockchain," "crypto" and "Web3."
- Gies College of Business maintains its own student-organization page separately from
  one.illinois.edu; that page was not retrieved.

## E. Faculty / staff and phone numbers

**Faculty**
- **Andrew Miller** — Adjunct Associate Professor, Electrical & Computer Engineering.
  Research listed as "computer security, privacy, and information trust; cryptographic
  systems and protocols." Publications include "The Honey Badger of BFT Protocols" and
  Bitcoin/Ethereum network analysis. **Email soc1024@illinois.edu. No phone published on
  the directory entry; no office listed.** Source:
  https://ece.illinois.edu/about/directory/faculty/soc1024
  ⚠ Note the title: **"Adjunct"** — his primary appointment has moved. Verify he is
  physically in Urbana in Fall 2026 before building a visit around him.
- No other blockchain/digital-asset faculty were confirmable on a live page within the
  fetch budget. **Do not guess names.** Gies finance directory:
  https://giesbusiness.illinois.edu/ — look up here.

**Offices and phone numbers (all confirmed on a live page)**

| Office | Phone | What it controls |
|---|---|---|
| Illini Union Event Services | **(217) 333-0691** | Information tables, Union space, the insurance determination. THE decision-maker for tabling. |
| Office of the Dean of Students | **(217) 333-0050** | 300 Turner Student Services Bldg, 610 E John St, Champaign. helpdean@illinois.edu. Canvasser registration under § 2-406. |
| Student Engagement (RSOs / SODA / SOFC) | **(217) 300-8757** | Illini Union Suite 284. RSO recognition; the org directory. studentengagement@illinois.edu |
| New Student & Family Experiences | **(217) 333-4057** | 616 E Green St Suite 210, Champaign. Welcome Week and Quad Day scheduling. newstudent@illinois.edu |
| Vice Chancellor for Finance & Administration | email only — OVCFA@illinois.edu | Owner of CAM FO-81. No phone published on the policy page. |

## F. Courses

From https://courses.illinois.edu/schedule/2026/fall/CS (the department course list; the
keyword search endpoint `courses.illinois.edu/search?keyword=blockchain` returned **HTTP
403** to tooling):
- **CS 407 — Cryptography**
- **CS 507 — Topics in Cryptography**
- **CS 425 — Distributed Systems**
No course with "blockchain" or "cryptocurrency" in the title surfaced in the CS listing.
⚠ **Fall 2026 offering status not confirmed for any of these** — the term filter was not
readable. Gies (FIN/ACCY) course listings were not retrieved.

## G. Events

- **HackIllinois** — https://hackillinois.org/ — "the premier student-run hackathon at the
  University of Illinois at Urbana-Champaign." The 2026 edition ran in **February** and
  "distributed over $75,000 in prizes"; **HackIllinois 2027 is upcoming** with an interest
  form open. Contact **contact@hackillinois.org**; no phone, no published sponsorship tier
  sheet on the landing page. ⚠ **This is the highest-value UIUC door in this document.**
  It is a private student-run event with a real prize budget, which means a real sponsor
  pipeline, and sponsoring it sidesteps § 2-506 entirely because DGD is not soliciting on
  university property — it is a named sponsor of a student organisation's event. February
  is outside the Fall 2026 window, but **sponsor conversations happen in the autumn.**
- No blockchain-specific research centre at UIUC was confirmable within budget.

## Source URLs — UIUC
- https://registrar.illinois.edu/academic-calendars/fall-2026-academic-calendar/
- https://newstudent.illinois.edu/orientation/welcomeweek
- https://studentcode.illinois.edu/article2/part5/2-506/
- https://studentcode.illinois.edu/article2/part5/2-502/
- https://studentcode.illinois.edu/article2/part4/2-407/
- https://studentcode.illinois.edu/article2/part4/2-406/
- https://cam.illinois.edu/policies/fo-81/
- https://union.illinois.edu/event-services-policies
- https://union.illinois.edu/reserve-space/reserve-union
- https://studentengagement.illinois.edu/
- https://odos.illinois.edu/
- https://one.illinois.edu/club_signup
- https://ece.illinois.edu/about/directory/faculty/soc1024
- https://hackillinois.org/
- https://www.bot.uillinois.edu/governance/general_rules

---

# CAMPUS 2 — UNIVERSITY OF ILLINOIS CHICAGO (UIC) (Public, semesters)

Chicago (Near West Side / Illinois Medical District). ~34,000 students. R1, and unusually
for this list it has an actual undergraduate **blockchain course in the business school**.

## A. Academic calendar — Fall 2026 — CONFIRMED

Source: https://catalog.uic.edu/ucat/academic-calendar/ (weekday letters printed in the
catalog itself, which is why these are high-confidence)

- **First day of instruction: Monday, August 24, 2026** ("August 24, M")
- Eight-week Part of Term A ends **Friday, October 16** ("October 16, F"); Part B begins
  **Monday, October 19** ("October 19, M")
- **Student Wellness Day: Wednesday, November 25** — no classes
- **Thanksgiving holiday: Thursday–Friday, November 26–27**
- **Last day of instruction: Friday, December 4, 2026** ("December 4, F")
- **Final examinations: Monday–Friday, December 7–11, 2026**
- **No separate October fall break.**

⚠ **UIC ends a full week earlier than UIUC.** Last instruction Dec 4 vs Dec 9; finals end
Dec 11 vs Dec 17. If you are planning a "December Chicago swing," UIC is already gone.

## B. Involvement fair — UNVERIFIED DATE

The **"Fall Involvement Fair & Service Expo"** is confirmed by name as an annual event of
the Center for Student Involvement (https://involvement.uic.edu/). Other CSI events named
on the same page: **SPARK** (semester kickoff), **Flames in the City**, **UIC Homecoming
Week**.

- **Fall 2026 date, time, location, cost and eligibility: NOT PUBLISHED at any URL
  reachable.** `involvement.uic.edu/events/fall-involvement-fair/` → 404;
  `involvement.uic.edu/programs/` → 404; `involvement.uic.edu/programs-events/` returned
  boilerplate only.
- ⚠ **events.uic.edu is unreadable to research tooling — SSL certificate verification
  failure** ("unable to get local issuer certificate"). Same failure on
  `studentaffairs.uic.edu` and `connect.uic.edu`. This is a UIC-wide certificate-chain
  problem for automated clients, not a robots block. A human browser will load these
  fine.
- Recurring pattern: first two weeks of the fall semester, outdoors on the East Campus
  quad. **Will post at https://involvement.uic.edu/ — call (312) 413-5070.**
- **Whether outside organisations may table: NOT PUBLISHED.** The governing policy (below)
  requires a written agreement and insurance for any non-affiliated user, so the honest
  expectation is "not at the student fair, but yes as a paid facility user."

## C. Solicitation / outside-vendor policy — GOOD NEWS, a named policy for exactly this

UIC has a policy titled for the situation, which is rare.

**DOS-8100-004 — "Non-affiliated Persons, Groups, Organizations and/or Entities Use of
University Facilities," effective March 15, 2024.**
https://policies.uic.edu/uic-policy-library/student-affairs/non-affiliated-persons-groups-organizations-and-or-entities-use-of-university-facilities/

- Definition of a non-affiliated user: "Those that are **neither affiliated with a major
  administrative or college unit nor a registered university student or campus
  organization**" — examples given include **private companies**, nonprofits and
  unincorporated associations. DGD is squarely inside this definition.
- What they may do: reserve "designated property owned and controlled by UIC, **provided
  the proposed use conforms to the Board of Trustees policies and does not interfere with
  the functions of the university.**"
- Requirements: "The Non-affiliated User must **enter into a written agreement** for use of
  the specified university property and **provide proof of insurance**"; pay applicable
  charges per that agreement; undergo a **security assessment, with the user bearing
  security costs**.
- "The university grant of permission **does not imply or signify the university's
  endorsement, sponsorship, approval or disapproval**." Requests evaluated in a
  "**viewpoint-neutral manner**."
- Does not apply to invited guest lecturers/speakers in closed forums.
- Procedures and forms: **https://venues.uic.edu/**. Policy questions: policies@uic.edu.
- ⚠ The policy text contains **no explicit commercial-activity ban, no solicitation clause
  and no anti-fronting language.** That absence is the finding: UIC's written rule is
  *transactional* (contract + insurance + security + fee), not prohibitory.

**DOS-8100-002 — UIC Policy on Open Expression.**
https://policies.uic.edu/uic-policy-library/student-affairs/uic-policy-on-open-expression-3/

> "Individuals/groups that are not members of the university community **may only
> participate in an open expression activity on campus if they are sponsored by a
> university department or organization and approved in advance of the event.**"
> "Space should be reserved **at least 48 hours in advance** of the event."
> Participants "must not attempt, **by repeated demands, threats, or otherwise, to coerce
> individuals into accepting or paying for materials.**"

Reservations for Student Centers and outdoor spaces go through the Office of Meetings and
Conferences. **So there are two parallel doors: sponsorship under Open Expression, or a
paid contract under DOS-8100-004.** Sponsorship genuinely helps at UIC — unlike at UIUC.

**Rates: NOT PUBLISHED.** venues.uic.edu lists Credit Union 1 Arena (8,500 cap), Dorin
Forum (2,500) and Student Center East/West meeting rooms, with **no rate card, no tabling
fee, no insurance dollar limit, no deposit or cancellation terms online.** Get them by
phone.

## D. Relevant student clubs — DIRECTORY UNREADABLE

- UIC's directory is **UIC Connection at connect.uic.edu** ("over 300 student
  organizations"), per https://involvement.uic.edu/.
- ⚠ **connect.uic.edu failed SSL certificate verification** to research tooling; the
  Campus Labs/Anthology mirrors (`uic.campuslabs.com/engage/organizations`,
  `uic.presence.io/organizations`) returned 404 / DNS failure. **No UIC club could be
  confirmed or ruled out.** Do not fabricate names.
- The existence of **FIN 481 (below)** implies a finance/fintech student population in the
  College of Business Administration; ask CSI to search Connection for "blockchain,"
  "crypto," "investment" and "fintech."

## E. Faculty / staff and phone numbers

**Offices (all confirmed live)**

| Office | Phone | What it controls |
|---|---|---|
| Center for Student Involvement (CSI) | **(312) 413-5070** | 340 Student Center East, 750 S Halsted. The Fall Involvement Fair. studentinvolvement@uic.edu |
| UIC Meetings & Conferences | **(312) 965-1708** | 750 S Halsted, SCE Suite B-19. Books RSOs, departments **and non-university clients**. uicmeetings@uic.edu |
| UIC Venues & Events | **(312) 413-5700** (fax 312-413-5774) | 525 S Racine Ave. Arena, Dorin Forum, external contracts. uicvenues@uic.edu |
| Office of the Dean of Students | **(312) 996-4857** | 1200 W Harrison St, 3030 SSB. dos@uic.edu. Owns DOS-8100-004 and the Open Expression policy. |
| Student Veteran Affairs (DOS unit) | (312) 413-5112 | 248 SCE — listed for completeness |
| UIC Student Centers | no direct number published — studentcenters@uic.edu | Meeting space; look up at https://studentcenters.uic.edu/meet-here/ |

**Faculty: NOT CONFIRMED.** No individual UIC faculty member was verified on a live page
within budget. The instructor of FIN 481 is the obvious target — look up at the College of
Business Administration finance directory rather than guessing.

## F. Courses

- ⚠ **FIN 481 — Introduction to Blockchain and Cryptocurrencies (3 hours).** Catalog
  description: "introduces students to blockchain and cryptocurrencies so they can safely
  navigate these spaces" and explore related career applications; "requires significant
  computer work"; **prerequisite FIN 300**. Source: https://catalog.uic.edu/search/?P=blockchain
  **This is the only named undergraduate blockchain course confirmed anywhere in this
  packet.** Fall 2026 offering status not confirmed — check the schedule of classes.

## G. Events

Not confirmed within budget. UIC's events calendar (events.uic.edu) is SSL-blocked to
tooling; UIC Today (today.uic.edu) surfaced no Fall 2026 involvement-fair listing.

## Source URLs — UIC
- https://catalog.uic.edu/ucat/academic-calendar/
- https://policies.uic.edu/uic-policy-library/student-affairs/
- https://policies.uic.edu/uic-policy-library/student-affairs/non-affiliated-persons-groups-organizations-and-or-entities-use-of-university-facilities/
- https://policies.uic.edu/uic-policy-library/student-affairs/uic-policy-on-open-expression-3/
- https://involvement.uic.edu/
- https://venues.uic.edu/
- https://meetings.uic.edu/
- https://dos.uic.edu/
- https://studentcenters.uic.edu/meet-here/
- https://catalog.uic.edu/search/?P=blockchain

---

# CAMPUS 3 — NORTHWESTERN UNIVERSITY (Private, ⚠ QUARTERS)

Evanston, IL (plus a Chicago campus). ~23,000 students. Kellogg, McCormick, Medill.
Private — **no public-forum obligation whatsoever.**

## A. Academic calendar — Fall Quarter 2026 — ⚠ PARTIAL / UNVERIFIED

⚠ **This is the weakest calendar in the packet and the ambassador must confirm it.**

Northwestern's registrar publishes a single filterable calendar application at
https://www.registrar.northwestern.edu/calendars/academic-calendars/index.html . The
markdown conversion delivered **dates and programme names but stripped the event-type
column entirely** — repeated prompting could not recover labels like "Classes begin."
Every year-specific URL pattern tested returned 404
(`/calendars/academic-calendar-2026-27.html`, `/calendars/academic-calendars/2026-27.html`,
`/calendars/planning-calendars/index.html`, `/calendars/academic-calendar-2026-27/index.html`).
`catalogs.northwestern.edu/undergraduate/academic-calendar/` still served the **2025-2026
edition** and did not render its table.

Dates on which the **Undergraduate** programme has a calendar entry in Fall 2026, taken
from the registrar application:

| Date (2026) | Actual weekday | Most likely meaning (NOT CONFIRMED) |
|---|---|---|
| Sept 22 | Tuesday | Fall Quarter classes begin |
| Sept 26 | Saturday | Add deadline |
| Oct 5 | Monday | Drop deadline |
| Nov 24 | Tuesday | Thanksgiving recess begins / last class before break |
| Nov 26 | Thursday | Thanksgiving |
| Dec 1 | Tuesday | Classes resume |
| Dec 5 | Saturday | Last day of classes |
| Dec 6–8 | Sun–Tue | Reading period |
| Dec 12 | Saturday | Quarter ends / exams conclude |
| Dec 15 | Tuesday | Grades due |

⚠ **STALE-PAGE / RENDER WARNING.** The extraction attached weekday names to several of
these dates that do **not** match 2026 (it labelled Sept 22 "Monday" and Dec 6 "Saturday";
in 2026 those are Tuesday and Sunday). The weekdays it produced correspond to **2025**.
Either the page mixes years or the converter hallucinated weekdays. **Do not print any
Northwestern weekday from this packet.** The *dates* are consistent with Northwestern's
long-standing pattern (classes begin the Tuesday after Wildcat Welcome; quarter ends
mid-December). **Confirm with the Registrar before booking travel.**

**The one thing that is certain: Northwestern is on QUARTERS and starts roughly five weeks
after UIUC/UIC.** A late-August Illinois trip misses Evanston completely.

## B. Involvement fair — NOT LOCATED

Northwestern runs a **Student Organization Fair** during **Wildcat Welcome** (its
new-student orientation week, immediately preceding the quarter). Neither the fair page nor
the Wildcat Welcome page could be reached: `northwestern.edu/newstudent/wildcat-welcome/`,
`northwestern.edu/wildcat-welcome/`, `northwestern.edu/csi/`,
`northwestern.edu/studentinvolvement/`, `northwestern.edu/campus-life/student-organizations/`
and `northwestern.edu/norris/get-involved/student-organizations/index.html` **all returned
404**. `norris/` itself loads but exposes no navigation URLs to the converter.

**Fall 2026 fair date, cost and outside-organisation eligibility: UNVERIFIED.** Pattern:
mid-September, during Wildcat Welcome, on Deering Meadow / at Norris. Given the written
policy below (third parties need sponsorship), assume outside organisations are **not**
admitted to the fair. **Call the Dean of Students office at (847) 491-8430 and ask them to
route you to Student Organizations & Activities.**

## C. Solicitation / outside-vendor policy — RETRIEVED IN FULL, and it is clear

Two current, dated, university-wide policies. Both are PDFs in the policy catalog
(https://policies.northwestern.edu/all-policies/university.html).

**"Display and Solicitation," effective September 5, 2024** —
https://policies.northwestern.edu/docs/display-and-solicitation.pdf

- Defines **"Commercial Solicitation"** as "**Selling or offering goods and services … for-
  profit or personal economic benefit**," distinguished from "Noncommercial Solicitation"
  ("Requests for action … including … petitioning, opinion polling, membership drives").
- "**Any community member or third party must obtain permission to solicit on campus**"
  from "the appropriate unit officer or University official."
- "**Commercial solicitation is prohibited at the Rock, door to door within University
  buildings, or in residence halls.**"
- "Persons or groups that are not community members … **have no right or privilege to post
  … unless they receive the proper sponsorship from a recognized student organization,
  campus unit, or University official.**"
- Named contact: Norris-events@northwestern.edu / Norris Event Planning Office (Evanston).

**"Use of University Facilities and Space," effective September 23, 2024** —
https://policies.northwestern.edu/docs/facilities-and-space.pdf

- "**Third parties have no right or privilege to use university space or facilities without
  a sponsoring recognized student organization, campus unit or University official.**"
- "Use of facilities or space for the purposes of **commercial use, selling, or advertising
  goods and services, is permitted only with permission from the appropriate unit
  officer.**"
- "Events and other requests to use university space and facilities **must be sponsored by
  a University Official, department, campus unit, or recognized student organization.**"
- "**The sponsor / sponsoring unit is responsible** for the Event or other use of space,
  which includes compliance with all applicable policies and laws."
- Contacts printed in the policy: **Assistant Vice President and Dean of Students,
  (847) 491-8430**; university.compliance@northwestern.edu; Norris-events@northwestern.edu.

**Does sponsorship cure it? YES — sponsorship is the designated mechanism at Northwestern,
and it is the only one.** But note the sting in the tail: **the sponsor carries the
compliance liability.** A student club that fronts for DGD is the party on the hook. Be
straight with them about that.

**Anti-fronting:** no clause found. **Insurance limits, deposits, cancellation terms: not
stated in either policy** — those live in Norris's event agreements, which were not
retrievable. **Nothing found reaching payment credentials or on-site contract signing.**

## D. Clubs — NOT CONFIRMED

Northwestern's directory is **Wildcat Connection**; `northwestern.campuslabs.com/engage/
organizations` returned 404 to tooling and no alternative host was located. **No
Northwestern club was confirmed.** Do not guess — Northwestern has a well-known
entrepreneurship ecosystem (The Garage) and Kellogg finance clubs, but none was verified on
a live page.

## E. Phone numbers

| Office | Phone | What it controls |
|---|---|---|
| Assistant VP & Dean of Students | **(847) 491-8430** | Named in the facilities policy as the student-issues contact. **The single best Northwestern number in this packet.** |
| Norris Event Planning | no phone published — Norris-events@northwestern.edu | Named in both policies as the Evanston reservation channel. `norris/about/contact.html`, `norris/services/event-planning.html` → 404. **Ask the Dean of Students office for the Norris scheduling line.** |
| University Compliance | email only — university.compliance@northwestern.edu | Policy interpretation |

## F–G. Courses and events — NOT RETRIEVED

Not reached within the fetch budget. Kellogg and McCormick both teach fintech/crypto
material; nothing was confirmed on a live page and nothing is asserted here.

## Source URLs — Northwestern
- https://www.registrar.northwestern.edu/calendars/academic-calendars/index.html
- https://policies.northwestern.edu/all-policies/university.html
- https://policies.northwestern.edu/docs/display-and-solicitation.pdf
- https://policies.northwestern.edu/docs/facilities-and-space.pdf

---

# CAMPUS 4 — DEPAUL UNIVERSITY (Private, Catholic, ⚠ QUARTERS)

Chicago — Lincoln Park and Loop campuses. ~21,000 students. **The largest Catholic
university in the United States**, and the largest private university in the Midwest. Big
CDM (Jarvis College of Computing and Digital Media) and Kellstadt business populations, and
the Loop campus puts you inside the financial district.

## A. Academic calendar — Autumn Quarter 2026 — ⚠ NOT RETRIEVED

⚠ **DePaul's academic calendar is a JavaScript/SharePoint application and none of its data
was machine-readable.** https://academics.depaul.edu/calendar/Pages/default.aspx renders
only the year and term dropdowns (2020-21 through 2029-30; Autumn/Winter/Spring/Summer);
appending `?Year=2026-2027&Term=Autumn` changed nothing. Every alternative path tested
returned 404: `catalog.depaul.edu/academic-year-calendars/`, `catalog.depaul.edu/academic-
calendar/`, `depaul.edu/academics/Pages/academic-calendar.aspx`,
`offices.depaul.edu/registrar/`, `offices.depaul.edu/enrollment-management/registration-
records/Pages/academic-calendar.aspx`, `law.depaul.edu/academics/Pages/academic-
calendar.aspx`, `cdm.depaul.edu/Current Students/Pages/AcademicCalendar.aspx`.

**What is certain: DePaul is on QUARTERS.** The calendar interface itself is organised by
Autumn/Winter/Spring/Summer *Terms*, confirming the quarter system. DePaul's autumn quarter
historically begins in **early-to-mid September** — earlier than Northwestern (late Sept)
and much earlier than UChicago (late Sept) — and ends before the winter holidays.

⚠⚠ **This is the single biggest date gap in the Illinois packet. Get the Autumn 2026 start,
add/drop and finals dates by phone before any Chicago trip is booked.** Division of Student
Affairs: **(312) 362-8610**.

## B. Involvement fair — NOT LOCATED

DePaul runs an involvement/activities fair during its Welcome Week ("Blue Demon Week"
programming) at Lincoln Park. `offices.depaul.edu/student-affairs/student-involvement/…`,
`offices.depaul.edu/student-involvement/…` and
`offices.depaul.edu/student-affairs/student-life/student-involvement/…` all returned 404;
the Student Affairs departments index confirms an **Office of Student Involvement** exists
but publishes no direct number on that page. **Date, cost and outside-org eligibility:
UNVERIFIED.** Call (312) 362-8610 and ask for Student Involvement.

## C. Solicitation / outside-vendor policy — ⚠ RETRIEVED, AND DEPAUL IS THE MOST OPEN
PRIVATE IN THE PACKET

Two current policies, both from the Office of the Secretary's policy library
(https://offices.depaul.edu/secretary/policies-procedures/policies/Pages/default.aspx).

**"Use of DePaul Facilities by External Groups," effective February 14, 2025** —
https://offices.depaul.edu/secretary/policies-procedures/policies/Documents/Use%20of%20DePaul%20Facilities%20by%20External%20Groups.pdf

- The university may **deny** a reservation where the external group's purpose conflicts
  with DePaul's "**identity, mission, and values**." (This is the Catholic-mission veto and
  it is real.)
- ⚠ **THE EXEMPTION IS THE WHOLE GAME:** "**External groups who are working with a
  University unit or recognized student organization are exempt from this policy**" —
  provided the unit or student organisation is an "**active participant** in the event."
- All external groups must submit "a written statement about the **identity and purpose**
  of the sponsoring group."
- Escalation: where a question arises about purpose, "the request will be forwarded by the
  reservation authority to the **Senior Executive for University Mission**, who will make a
  determination **within 48 hours**."
- Reservations may be **cancelled** if groups provide inaccurate information.
- Contacts printed: Vice President, Student Affairs; **Senior Executive for University
  Mission, (312) 362-8042**.

**"Space Reservations at University Student Center Facilities," effective February 13,
2025** —
https://offices.depaul.edu/secretary/policies-procedures/policies/Documents/Space%20Reservations%20at%20University%20Student%20Center%20Facilities.pdf

- Account eligibility: "**You must be a DePaul University faculty/staff member or
  representative of a recognized student organization**" to hold a reservation account.
- ⚠ **The paid external route, verbatim:** "**The Student Center facilities are available
  to outside organizations for use; however those groups must pay a fee to use space.**"
- Requires a **signed contract** and a **certificate of insurance naming DePaul as
  additionally insured**.
- Fee tiers: "**External Group Event**" = **100% of rental fees**; DePaul events with
  majority-internal audiences = "**No Rental Fee Charged**."
- Money terms: **50% deposit to hold the space; 100% of the total room rental fee due at
  least two weeks before the event.**
- Deadlines: "Requests are accepted **up to five business days before an event**" at most
  locations; **Cortelyou Commons requires ten business days**.
- Contacts: **Lincoln Park Student Center 773/325-7346; Loop Student Center
  312/362-8624**; studentcenters@depaul.edu.

**Does sponsorship cure it? YES, decisively — and it is cheaper than the alternative.** A
DePaul unit or recognised student organisation as an *active participant* takes DGD out of
the External Groups policy entirely and out of the 100% rental tier. **No anti-fronting
clause was found**, but the "active participant" qualifier and the "inaccurate information
→ cancellation" clause together function as one: a nominal sponsor who does not show up is
a cancellation risk.

**Nothing found reaching payment credentials or contract signing on site.**

## D. Clubs — NOT CONFIRMED

DePaul's directory is **DeHUB**. No reachable URL was found. **No DePaul club is asserted.**

## E. Phone numbers

| Office | Phone | What it controls |
|---|---|---|
| Lincoln Park Student Center reservations | **(773) 325-7346** | Books the LP student centre, including external groups. **Best first call.** |
| Loop Student Center reservations | **(312) 362-8624** | Loop campus space |
| Division of Student Affairs | **(312) 362-8610** | 2250 N Sheffield, Student Center 307. Routes to Student Involvement and Dean of Students. studentaffairs@depaul.edu |
| Senior Executive for University Mission | **(312) 362-8042** | ⚠ The mission-conflict veto under the External Groups policy. If DGD is going to be refused at DePaul, it will be refused here. |
| Office of the General Counsel — Mary Devona Stark (policy contact) | **(312) 362-7503** | Named on the policies-and-procedures landing page |

## F–G. Courses and events — NOT RETRIEVED

## Source URLs — DePaul
- https://academics.depaul.edu/calendar/Pages/default.aspx (JavaScript app — unreadable)
- https://offices.depaul.edu/secretary/policies-procedures/policies/Pages/default.aspx
- …/Documents/Use%20of%20DePaul%20Facilities%20by%20External%20Groups.pdf
- …/Documents/Space%20Reservations%20at%20University%20Student%20Center%20Facilities.pdf
- https://offices.depaul.edu/student-affairs/Pages/default.aspx
- https://offices.depaul.edu/student-affairs/about/departments/Pages/default.aspx

---

# CAMPUS 5 — ILLINOIS STATE UNIVERSITY (Public, semesters)

Normal, IL. ~20,000 students. Illinois's oldest public university.

## A. Academic calendar — Fall 2026 — CONFIRMED

Source: the Provost's official multi-year PDF,
https://provost.illinoisstate.edu/downloads/AcademicCalendar2022-2031.pdf
(linked from https://events.illinoisstate.edu/academic-calendar/)

- **Classes begin: Monday, August 17, 2026** — ⚠ **tied for the earliest start in the
  state** with SIU and Illinois Tech.
- **Welcome Week 2026: August 11–16** (confirmed on the Dean of Students site).
- **Thanksgiving break: Saturday, November 21 at noon → Sunday, November 29** (classes
  resume Nov 30). A nine-day break, same shape as UIUC's.
- **Last day of classes: Saturday, December 5, 2026.**
- **Final evaluation period: December 5–11 (Sat–Fri).**
- **Commencement: Saturday, December 12, 2026.**
- **No separate October fall break listed.**
- Add/drop deadlines are **not** in the multi-year PDF — they live in the term calendar at
  events.illinoisstate.edu, which did not render its Fall 2026 entries to tooling. GAP.

## B. Involvement fair — ⚠ FESTIVAL ISU — CONFIRMED DATE, AND A CLEAN "NO"

Source: https://deanofstudents.illinoisstate.edu/involvement/involvement-fairs/festival-isu/

- **Festival ISU: Tuesday, August 25 – Wednesday, August 26, 2026, 10:00 a.m. – 2:00 p.m.,
  on the Quad.** (Two-day event. Winter Fest is the January equivalent.)
- Who may register: **Registered Student Organizations** (Festival ISU RSO Registration
  form) and **campus departments** (Festival ISU Campus Department Registration form).
- ⚠⚠ **OUTSIDE ORGANISATIONS: EXPRESSLY NO.** "**Community business vendors**" are
  explicitly excluded and their applications "**will not be accepted.**" Bloomington/Normal
  **nonprofits** may participate through a separate **Civic Engagement Fair**, arranged by
  direct contact only. DGD is a business, not a nonprofit — the Civic Engagement Fair is
  not a workaround.
- Fees: none published (moot for DGD).
- Registration deadline: not published.
- Contact named on the page: **Maren Keller, mkelle4@IllinoisState.edu.** ⚠ No phone on
  that page — use the Dean on Duty line, (309) 438-2008.

This is one of the cleanest published answers in the packet, and it is a no. It saves a
trip.

## C. Solicitation / outside-vendor policy

**Policy 6.1.1 — University Facility and Space Use**, initiated **January 2020**; it
consolidated and replaced the former standalone policies on **solicitation (6.1.14)**,
exterior communications (6.1.15) and special services requests (6.1.31).
https://policy.illinoisstate.edu/facilities/6-1-1/

- Defines "**Public**" as "**a person or public organization not affiliated with Illinois
  State University.**"
- "**Solicitation**" is defined broadly: "canvassing, soliciting or seeking to obtain
  membership in or support for any organization, **requesting contributions, and posting or
  distributing any materials**" using university resources.
- "**Sales**" is defined as "offering goods and services for sale or purchase,
  **distributing advertising materials, circulars or product samples.**" ⚠ Note that
  **handing out a product sample or a circular is "sales" at ISU** — that sweeps in a
  literature table.
- ⚠ **Non-university groups may not conduct sales or solicitations on campus except as
  approved**, with categorical prohibitions in **University Housing, the Dining Centers and
  Milner Library**. **Door-to-door solicitation to residents and employees is prohibited.**
- Vendors require **designated official approval**.
- Fees: the university "**establishes fee rates for use of University facilities and spaces
  based on the relationship between the University and the person or organization**" —
  i.e. an outside-entity rate exists but is not published on the policy page.
- Insurance: the university "**reserves the right to impose reasonable security, insurance,
  or safety requirements on events based on a risk assessment.**" No dollar limits
  published.
- Reservations run through **Conference Services**,
  https://conferences.illinoisstate.edu/scheduling/
- Policy owner: **Office of the President, (309) 438-5677.**

**Sponsorship:** the policy does not create an explicit RSO-sponsorship cure; it routes
everything through "as approved" by the designated official. Sponsorship helps in practice
but is not a named safe harbour. **No anti-fronting clause found. Nothing reaching payment
credentials.**

## D. Clubs — NOT CONFIRMED

ISU's directory is **Redbird Life**. It is referenced on the Dean of Students site but no
reachable directory URL was captured, and no ISU organisation is asserted here.

## E. Phone numbers

| Office | Phone | What it controls |
|---|---|---|
| Dean of Students — "Dean on Duty" | **(309) 438-2008** | Student Services Building 387. Fastest human at ISU; owns Festival ISU and student involvement. |
| Policy owner, Office of the President (Policy 6.1.1) | **(309) 438-5677** | The facility/solicitation policy itself and the "as approved" discretion. |
| Office of the Provost | **(309) 438-7018** | Academic calendar; Provost@IllinoisState.edu |
| Conference Services | no direct number published — https://conferences.illinoisstate.edu/scheduling/ | Space reservations and the outside-entity rate card. **Look up here / ask the Dean on Duty to transfer.** |
| Festival ISU — Maren Keller | no phone published — mkelle4@IllinoisState.edu | Festival ISU registration |

## F–G. Courses and events

- **Family Weekend 2026: September 18–20, 2026** (confirmed on the Dean of Students site) —
  a high-footfall public weekend, and the only ISU event date confirmed here.
- No blockchain/fintech course or faculty member was confirmed at ISU within budget.

## Source URLs — ISU
- https://provost.illinoisstate.edu/downloads/AcademicCalendar2022-2031.pdf
- https://events.illinoisstate.edu/academic-calendar/
- https://deanofstudents.illinoisstate.edu/
- https://deanofstudents.illinoisstate.edu/involvement/involvement-fairs/festival-isu/
- https://policy.illinoisstate.edu/facilities/6-1-1/

---

# CAMPUS 6 — NORTHERN ILLINOIS UNIVERSITY (Public, semesters)

DeKalb, IL — about 65 miles west of Chicago. ~15,000 students.

## A. Academic calendar — Fall 2026 — CONFIRMED (with an add/drop gap)

Source: https://www.niu.edu/academics/calendars/

- **Classes begin: Monday, August 24, 2026.**
- **Thanksgiving break: November 25 – 29, 2026** — "no classes on Wednesday" (Nov 25),
  through Sunday Nov 29.
- **Last day of classes: Saturday, December 5, 2026.**
- **Final examinations: December 7 – 12, 2026 (Monday–Saturday).**
- **Add/drop deadlines: NOT CAPTURED.** GAP.
- ⚠ NIU's full academic calendar lives in a **Localist** application at
  https://calendar.niu.edu/academic_calendar which renders per-term **tabs**. The tooling
  could read the Spring 2026, Summer 2026, Spring 2027 and Summer 2027 tabs but **never the
  Fall 2026 tab**; one attempt returned **HTTP 429 (rate-limited)**. The dates above come
  from the separate `niu.edu/academics/calendars/` page and should be re-confirmed with
  Registration & Records.

## B. Involvement fair — NOT LOCATED

NIU's org platform is **Huskie Hub** (https://go.niu.edu/get-involved). No involvement-fair
page was reachable: `niu.edu/involvement/index.shtml` and `niu.edu/involvement/` → 404.
**Fall 2026 fair name, date, cost and eligibility: UNVERIFIED.** Start at
https://go.niu.edu/get-involved and call Registration & Records or the Policy Library for
a transfer to Student Involvement & Leadership Development.

## C. Solicitation / outside-vendor policy — ⚠ NOT RETRIEVED

**This is a genuine hole and it should be treated as one.** NIU maintains a Policy Library
(https://www.niu.edu/policies/) organised into 15 categories. The
**Campus Health, Safety and Facilities** category
(https://www.niu.edu/policies/categories/pdcampushealthsafetyfacilities.shtml) was read in
full and contains **no solicitation, vendor, commercial-activity or general facility-use
policy** — it covers access control, law-library access, facility naming, recreation
facilities, AED placement, environmental health and safety, and vehicle use. The
`niu.edu/policies/facilities/index.shtml` and `niu.edu/policies/index.shtml` paths returned
404 / a bare category list.

**Rating NIU provisionally at 3 with the gap named**, per the packet rule. The policy
almost certainly exists — probably under Governance/Administration or a Student Affairs
handbook rather than the facilities category — but it was not retrieved and **nothing is
asserted about its contents.**

**To close it:** the **NIU Policy Library, (815) 753-5560**, policy-library@niu.edu, will
find it by keyword in one call. Also ask for the **Holmes Student Center** reservation
rules (`niu.edu/holmes/index.shtml` → 404) and whether external commercial entities may
rent tables there.

## D. Clubs — NOT CONFIRMED (Huskie Hub not read)

## E. Phone numbers

| Office | Phone | What it controls |
|---|---|---|
| Registration & Records | **(815) 753-0681** | Williston Hall 220, DeKalb IL 60115; Mon–Fri 8:00–4:30; regrec@niu.edu. Academic calendar and add/drop dates. |
| NIU Policy Library | **(815) 753-5560** | policy-library@niu.edu. ⚠ **The call that closes the NIU policy gap.** |

## F–G. Courses and events — NOT RETRIEVED

## Source URLs — NIU
- https://www.niu.edu/academics/calendars/
- https://calendar.niu.edu/academic_calendar (Localist; Fall 2026 tab unreadable, one 429)
- https://www.niu.edu/registration-records/index.shtml
- https://www.niu.edu/policies/
- https://www.niu.edu/policies/categories/pdcampushealthsafetyfacilities.shtml
- https://go.niu.edu/get-involved

---

# CAMPUS 7 — SOUTHERN ILLINOIS UNIVERSITY CARBONDALE (Public, semesters)

Carbondale, IL — 330 miles from Chicago, roughly 5.5 hours' drive. ~11,000 students.
**Geographically isolated from every other campus in this packet.**

## A. Academic calendar — Fall 2026 — CONFIRMED

Source: https://registrar.siu.edu/calendars/academic/2026-2027.php

- **First day of classes: Monday, August 17, 2026** — earliest wave.
- **Fall break: Friday, October 2, 2026** (single day).
- **Thanksgiving break: Saturday, November 21 at 12:00 noon → Sunday, November 29, 2026.**
- **Final examinations: Monday, December 7 – Friday, December 11, 2026.**
- **Commencement: Saturday, December 12, 2026.**
- Last day of classes not stated explicitly on the page; add/drop deadlines live on a
  separate **Registration Deadlines Calendar**
  (https://registrar.siu.edu/calendars/registration/index.php) — not retrieved. GAP.
- ⚠ The parent page warns that "academic calendars for future years have not yet been
  approved" — the 2026-27 page itself, however, is published with these dates.

## B. Involvement fair — NOT LOCATED

No SIU involvement-fair page was reached. The Student Center is the venue for most such
events. **UNVERIFIED.**

## C. Solicitation / outside-vendor policy — ⚠⚠ THE HARDEST WRITTEN POLICY IN ILLINOIS

**"Fund-Raising, Canvassing, Soliciting, Vending, and Allied Advertising on University
Property"** — approved **December 8, 1982**, amended December 22, 1997, August 13, 2020 and
**August 1, 2021**. https://policies.siu.edu/other-policies/chapter6/fundraising.php

Solicitation is permitted to recognized student organizations, university faculty/staff
organizations, university-affiliated or allied organizations — and to non-university groups
**only** if they meet one of these criteria:

> - they "**have applied for and received a solicitation permit for each of the years
>   commencing July 1, 1978**"; **OR**
> - they have contracted specifically with the university's **Board of Trustees**; **OR**
> - they participate in a specially recognized event such as the **fall Flea Market**;
>   **OR**
> - they **sell constitutionally protected printed material** not otherwise available on
>   campus.

⚠ **Read the first criterion again.** It grandfathers a closed class of vendors who have
held a continuous permit since 1978 and admits nobody else. **DGD cannot satisfy any of the
four.** It is not a 48-year permit holder; it has no Board of Trustees contract; it is not
the Flea Market; and a wallet is not constitutionally protected printed material. **On the
written policy, SIU is closed to DGD.**

Procedure for those who *do* qualify: apply **in person** at the designated office "**at
least two full working days prior**" to commencing; present organisational credentials;
obtain both location-specific and activity-specific approvals; competing requests are
handled **first come, first served**. Applicants must show educational, cultural or service
benefit to the university community, proper credentials, legal compliance, and
accountability for funds collected.

**"University Property, Use and Control of"** (approved 10/27/2017) —
https://policies.siu.edu/other-policies/chapter6/use-control-property.php —
"**The private use of university property is not permitted. No one connected with the
university in any capacity may use any university property of whatever description for any
personal purposes.**" Property use is limited to the institution's educational, research or
public-service missions, and property may not benefit "any person, group or organization
within or outside the university, except in pursuit of the public purposes of the
university."

**The one countervailing fact:** SIU's **Student Center Event Services** publishes a
three-tier rate structure that expressly includes **off-campus organizations**
(https://studentcenter.siu.edu/event-services/forms-policies-rates.php): RSOs get "room
rental … waived for most spaces in the Student Center" (no-show fees only); on-campus
departments pay departmental rates; **off-campus organizations pay commercial rates**. The
same page notes "**separate request forms and policies regulate fundraising activities and
donation box placement**." So SIU will rent a *room* to an outside company — while the
1982 solicitation policy forbids the outside company from *soliciting*. **Renting a room is
not permission to solicit in it.** Anyone quoting the rate card at you has not read the
solicitation policy. Actual dollar rates are in fiscal-year rate sheets not retrieved.

**No anti-fronting clause found. Nothing reaching payment credentials.**

## D. Clubs — NOT CONFIRMED

Registration of student organisations is governed by
https://policies.siu.edu/other-policies/chapter3/student-groups.php (approved 08/13/2013).
The org directory itself was not read.

## E. Phone numbers

| Office | Phone | What it controls |
|---|---|---|
| Student Center Event Services | **(618) 536-3351** | 1255 Lincoln Drive, Mailcode 4407, Carbondale IL 62901. scenter@siu.edu. Rates, space, and the fundraising/solicitation request forms. **Best call at SIU.** |
| Office of the Registrar | **(618) 453-2963** | registrar@siu.edu. Calendar and registration deadlines. |
| Office of the Chancellor | **(618) 453-2341** | chancellor@siu.edu. Named as the contact for locating policies. |
| SIU main line | **(618) 453-2121** | Campus operator — **labelled as the main line.** |

## F–G. Courses and events — NOT RETRIEVED

## Source URLs — SIU Carbondale
- https://registrar.siu.edu/calendars/academic/2026-2027.php
- https://registrar.siu.edu/calendars/
- https://policies.siu.edu/master-index.php
- https://policies.siu.edu/other-policies/chapter6/fundraising.php
- https://policies.siu.edu/other-policies/chapter6/use-control-property.php
- https://studentcenter.siu.edu/event-services/index.php
- https://studentcenter.siu.edu/event-services/forms-policies-rates.php

---

# CAMPUS 8 — LOYOLA UNIVERSITY CHICAGO (Private, Jesuit, semesters)

Chicago — Lake Shore (Rogers Park), Water Tower (Michigan Avenue) and Health Sciences
(Maywood) campuses. ~17,000 students. Quinlan School of Business sits at Water Tower, in
the middle of the Magnificent Mile.

## A. Academic calendar — Fall 2026 — CONFIRMED

Source: https://www.luc.edu/academics/schedules/fall/academic_calendar.shtml

- **First day of classes: Monday, August 24, 2026.**
- **Last day to add and swap a class: Monday, August 31, 2026.**
- **Mid-Semester Break: Monday–Tuesday, October 5–6, 2026** ("No classes"). ⚠ **One of only
  two campuses in this packet with a true October fall break** (the other is Illinois
  Tech's Oct 12–13 in-service days).
- **Thanksgiving break: Wednesday–Saturday, November 25–28, 2026** — "Wednesday classes do
  not meet."
- **Last day of classes: Saturday, December 5, 2026.**
- **Final exams: December 7–12, 2026** — "Study Day Wednesdays: No daytime exams will be
  held."

Note: `luc.edu/academics/schedules/fall/` (the parent index) returned **HTTP 403** to
tooling while the calendar page itself loaded fine.

## B. Involvement fair — NOT LOCATED

Loyola's **Center for Student Engagement** runs Welcome Week and the recognised-student-
organisation programme, and its directory is **LUCommunity**
(https://www.luc.edu/studentengagement/). Named special events on that page: **Welcome
Week**, Finals Breakfast, Senior Send-Off. **No involvement-fair date, cost or eligibility
was published at any reachable URL. UNVERIFIED.** Events calendar: events.luc.edu.

## C. Solicitation / outside-vendor policy — ⚠ NOT FOUND IN THE POLICY LIBRARY

The complete alphabetical university policy index
(https://www.luc.edu/policy/alphabetical.shtml) was read end-to-end — roughly 130 policies,
A through W. **There is no solicitation policy, no commercial-activity policy and no
general use-of-facilities policy in it.** The only facilities-adjacent entries are
"Filming and Photography on Campus," "Wedding Ceremonies at Loyola Facilities," "Guidelines
for Political Activities," a "Speaker Policy (Political Activity)" and "Engage with Empathy:
Guidelines for Campus Dialogue."

That is a real finding about *where the rules live*, not evidence that none exist. At
Loyola the operative rules are almost certainly in (a) the **Student Handbook / Community
Standards** and the **Recognized Student Organization handbook** (referenced from
studentengagement.luc.edu but not retrieved), and (b) the **Conference Services** rental
contract.

**What is confirmed:** Loyola **does** rent to outside parties. Conference Services markets
"top-tier event spaces … now available for **all bookings**" across Lake Shore, Water
Tower, Health Sciences and the Retreat & Ecology Campus, including weddings and
non-university conferences (https://www.luc.edu/conference/). **No rate card, no insurance
limit, no deposit or cancellation terms are published** — all are quoted on request.

**Rating Loyola provisionally at 3 with the gap named.** As a private Jesuit institution it
has **no public-forum obligation**; do not import any assumption from the publics.

## D. Clubs — NOT CONFIRMED (LUCommunity not read)

## E. Phone numbers

| Office | Phone | What it controls |
|---|---|---|
| Conference Services | **(773) 508-8090** | 1032 W Sheridan Rd, Chicago IL 60660. conferences@luc.edu (events), loyolalodging@luc.edu (lodging). **The external-rental door — best first call.** |
| Center for Student Engagement | **(773) 274-3000** | 1032 W Sheridan Rd. RSOs, LUCommunity, Welcome Week. |
| Division of Student Development | **(773) 508-3890** | 1032 W Sheridan Rd. Parent division — student conduct, residence life, engagement. |

## F–G. Courses and events — NOT RETRIEVED

## Source URLs — Loyola
- https://www.luc.edu/academics/schedules/fall/academic_calendar.shtml
- https://www.luc.edu/academics/schedules/
- https://www.luc.edu/policy/alphabetical.shtml
- https://www.luc.edu/conference/
- https://www.luc.edu/studentengagement/
- https://www.luc.edu/saga/ (redirects to the Division of Student Development)

---

# CAMPUS 9 — UNIVERSITY OF CHICAGO (Private, ⚠⚠ QUARTERS, LATEST START IN THE STATE)

Hyde Park, Chicago. ~18,000 students. Booth School of Business; the Chicago Principles on
free expression originate here.

## A. Academic calendar — Autumn Quarter 2026 — CONFIRMED

Source: https://events.uchicago.edu/academic/calendar/year.php (the current-academic-year
view; verified as 2026-27 rather than 2025-26 by weekday arithmetic — the page prints
"Saturday, December 12," and Dec 12 is a Saturday in 2026, a Friday in 2025)

- ⚠⚠ **Autumn Quarter begins: Monday, September 28, 2026 — THE LATEST START IN ILLINOIS,
  five weeks after UIUC, UIC, Loyola and NIU, and six weeks after ISU, SIU and Illinois
  Tech.**
- **Thanksgiving break: Monday, November 23 – Friday, November 27, 2026** — UChicago takes
  the **entire** Thanksgiving week off.
- **Reading period: Saturday, December 5 – Monday, December 7, 2026.**
- **Final examinations: Tuesday, December 8 – Friday, December 11, 2026.**
- ⚠ **Quarter ends: Saturday, December 12, 2026 — the autumn quarter is entirely finished
  before Christmas.**
- Add/drop deadline: not on this view. See
  https://registrar.uchicago.edu/calendars/registration-dates-deadlines/ . GAP.

**The practical shape of UChicago's autumn:** a ten-week term with a dead week in the
middle (Thanksgiving) and no October break. **The usable window is Sept 28 – Nov 20 and
Nov 30 – Dec 4. That is it.** Do not plan a September Chicago trip around Hyde Park.

Other calendar URLs: `registrar.uchicago.edu/calendars/academic-calendar-2026-27/` → 404;
`events.uchicago.edu/academic/calendar/future.php` shows only 2027-28 onward;
`www.uchicago.edu/academics/calendar/` requires JavaScript ("You need to enable JavaScript
to run this app").

## B. Involvement fair — NOT LOCATED

UChicago's **Center for Leadership and Involvement (CLI)** runs the RSO fair (historically
"the RSO Fair" / "Student Activities Fair" during O-Week, late September). The CLI site
(https://leadership.uchicago.edu/) confirms the centre, "RSO Resources," "Programs &
Events," "Blueprint" and "space scheduling" — but **no fair date, cost or eligibility was
published at any reachable URL**, and `leadership.uchicago.edu/rso-resources/policies`
returned "**Too many redirects**." **UNVERIFIED.**

## C. Solicitation / outside-vendor policy — ⚠ NOT RETRIEVED (redirect loop)

⚠ **The University of Chicago Student Manual is unreadable to research tooling.**
https://studentmanual.uchicago.edu/ loads and lists its five sections — University
Policies, Academic Policies, Administrative Policies, Student Life & Conduct, Disciplinary
Reports — but **every attempt to open a subsection returned "Too many redirects"**
(`/university-policies/`, `/university-policies`, `/university-policies/use-of-university-
space/`, `/university-policies/university-policy-on-solicitation/`). `/student-life-conduct/`
loaded but rendered only a "use the links on the left" stub. `www.uchicago.edu/about/policies`
→ 404.

**Nothing is asserted about UChicago's written solicitation or space rules. Rating 3,
provisional, gap named.**

What can be said with confidence: UChicago is **private**, has **no public-forum
obligation**, and its celebrated free-expression commitment (the Chicago Principles) is
about **the intellectual freedom of members of the University community** — it has never
been a right of access for outside commercial entities, and citing it at a permit desk will
not help.

**The route to the answer:** **Student Centers, (773) 834-0858** — Ida Noyes Hall and the
Reynolds Club are the tabling venues and that office holds the scheduling rules
(studentcenters.sched@lists.uchicago.edu). Second call: **CLI, (773) 702-8787.**

## D. Clubs — DIRECTORY IS JAVASCRIPT-RENDERED

UChicago's RSO platform is **Blueprint** (https://blueprint.uchicago.edu/organizations).
The page returns "**This application requires JavaScript to be enabled**" and exposes **no
organisation names** to tooling. **No UChicago club is asserted.**

## E. Phone numbers

| Office | Phone | What it controls |
|---|---|---|
| Center for Leadership and Involvement (CLI) — Director Jimmy Brown | **(773) 702-8787** | Reynolds Club, 5706 S University Ave. RSOs, the RSO fair, Blueprint, space scheduling. |
| Student Centers — Director Christopher Burpee | **(773) 834-0858** | Ida Noyes Hall (1212 E 59th St) and Reynolds Club. studentcenters.sched@lists.uchicago.edu. ⚠ **The office that actually says yes or no to a table.** |
| Campus and Student Life (CSL) | **(773) 702-5243** | Behar Family House, 5711 S Woodlawn Ave. Parent division. |
| International House | (773) 753-2270 | 1414 E 59th St — rentable venue, listed for completeness |
| Housing & Residence Life | (773) 702-7366 | Listed for completeness; residence halls are not a tabling route |

Directors' names above are published on the CSL programmes-and-services page and are
reproduced as printed; **verify before addressing correspondence**, as these rotate.

## F–G. Courses and events — NOT RETRIEVED

Booth teaches crypto/fintech material and UChicago hosts significant blockchain-adjacent
economics research, but **nothing was confirmed on a live page and nothing is asserted.**

## Source URLs — University of Chicago
- https://events.uchicago.edu/academic/calendar/year.php
- https://registrar.uchicago.edu/calendars/
- https://studentmanual.uchicago.edu/ (subsections: redirect loop)
- https://leadership.uchicago.edu/
- https://csl.uchicago.edu/
- https://csl.uchicago.edu/programs-services/
- https://blueprint.uchicago.edu/organizations (JavaScript-rendered)

---

# CAMPUS 10 — ILLINOIS INSTITUTE OF TECHNOLOGY (Private, technical, semesters)

Chicago — Mies Campus, Bronzeville/Bridgeport (35th & State), plus Chicago-Kent College of
Law downtown. ~7,000 students. Technical, engineering- and CS-heavy, with an unusually high
international-graduate proportion. Small but exceptionally well-targeted audience.

## A. Academic calendar — Fall 2026 — CONFIRMED

Sources: https://www.iit.edu/registrar/academic-calendar and
https://www.iit.edu/registrar/academic-calendar/subsequent-academic-years

- **Fall term starts: Monday, August 17, 2026** — earliest wave, tied with ISU and SIU.
- **Add/drop: August 25, 2026** — "Last Day to Add/Drop for Full Semester, ID Full Semester,
  ID A Session and Online A Session Courses **with No Tuition Charges**."
- **Labor Day: September 7, 2026 — no classes.**
- **Fall break: October 12–13, 2026** — no-class days for faculty in-service activities.
  (An unusual two-day break; students are on campus but not in class.)
- **Thanksgiving break: November 25–28, 2026 — classes cancelled.**
- **Last day of classes: December 5, 2026.**
- **Final examinations: December 7–12, 2026** (grading opens December 7).
- **Final grades due at noon CST: December 16, 2026.**
- The page carries the caveat "**All future dates are subject to change.**"

## B. Involvement fair — NOT LOCATED

`iit.edu/student-affairs/student-organizations` → 404. IIT's fair is run by the **Office of
Student Life** during Welcome Week. **UNVERIFIED — date, cost and outside-organisation
eligibility all unpublished at reachable URLs.** Start at
https://www.iit.edu/student-affairs and call **(312) 567-3081**.

## C. Solicitation / outside-vendor policy — PARTIAL

No standalone solicitation or outside-vendor policy was located. What was retrieved, from
the Student Handbook's HTML sections:

**Posting Policy (Section K)** —
https://www.iit.edu/student-affairs/student-handbook/fine-print/policies-regulations-and-procedures

> "All items for posting including, but not limited to, **flyers, posters, table tents,
> leaflets, handbills or similar material must receive prior approval from the Office of
> Student Affairs.**"

Materials may go on designated bulletin boards only — not on walls, windows or doors.
"Questions, complaints, reports of violations, or appeals regarding the policy should be
directed to the Office of Student Affairs (dos@illinoistech.edu)."

**Mies Campus Student Organizations: Policies and Regulations** —
https://www.iit.edu/student-affairs/student-handbook/fine-print/mies-campus-student-organizations-policies-and-regulations

> "Organizations must fill out an **event space request form** to book space on campus."
> "Organizations wishing to have events that exceed the **2:1 guests per member ratio** may
> propose to do so by contacting the appropriate department (either Office of Student Life
> or Residence Life) and submitting an **event registration form at least 30 days in
> advance** of the proposed event."

⚠ **The 2:1 guest ratio is the sleeper clause.** An RSO-hosted DGD event whose attendees
are mostly non-members trips a 30-day advance registration requirement. Build that lead
time in.

**Not found:** any commercial-solicitation ban, any external-vendor rate, any insurance
requirement, any anti-fronting language, anything about payment credentials.
**The full handbook PDF was not parsed and is the place to look:**
https://www.iit.edu/sites/default/files/2026-03/2025-2026%20Student%20Handbook%20Final%20Copy_0.pdf
⚠ Note that PDF is the **2025-2026** edition — a 2026-2027 edition should supersede it.

**Rating IIT at 3, provisional.** Private institution, no public-forum obligation, an
approval gate on every piece of paper, and no published route for an outside company —
but equally no published prohibition.

## D. Clubs — NOT CONFIRMED

## E. Phone numbers

| Office | Phone | What it controls |
|---|---|---|
| Office of Student Affairs | **(312) 567-3081** | ⚠ Approves **all** posted/distributed materials under the Posting Policy, and is the escalation point for organisation policy. dos@illinoistech.edu. **The only confirmed IIT number and the one that matters.** (Number printed in the handbook's alcohol section; it is the Student Affairs office line.) |
| Office of Student Life — Welcome Desk | no phone published — welcomedesk@illinoistech.edu | Event space request forms, org events, the fair |
| Office of the Registrar | no phone published — https://www.iit.edu/registrar | Calendar; look up here |

⚠ Note the domain split: IIT uses both `iit.edu` (web) and `illinoistech.edu` (email).
Neither is a typo.

## F–G. Courses and events — NOT RETRIEVED

## Source URLs — Illinois Tech
- https://www.iit.edu/registrar/academic-calendar
- https://www.iit.edu/registrar/academic-calendar/subsequent-academic-years
- https://www.iit.edu/student-affairs/student-handbook
- https://www.iit.edu/student-affairs/student-handbook/fine-print/policies-regulations-and-procedures
- https://www.iit.edu/student-affairs/student-handbook/fine-print/mies-campus-student-organizations-policies-and-regulations
- https://www.iit.edu/sites/default/files/2026-03/2025-2026%20Student%20Handbook%20Final%20Copy_0.pdf

---

# CROSS-CAMPUS SUMMARY — ILLINOIS

## (1) Fall 2026 term starts at a glance — semester vs quarter

| Date | Campus | System | Term ends |
|---|---|---|---|
| **Mon Aug 17** | **Illinois State** | Semester | Classes Dec 5; finals Dec 5–11 |
| **Mon Aug 17** | **SIU Carbondale** | Semester | Finals Dec 7–11; commencement Dec 12 |
| **Mon Aug 17** | **Illinois Tech** | Semester | Classes Dec 5; finals Dec 7–12 |
| **Mon Aug 24** | **UIUC** | Semester | Classes Dec 9; finals Dec 11–17 ⚠ latest finish in the state |
| **Mon Aug 24** | **UIC** | Semester | Classes Dec 4; finals Dec 7–11 |
| **Mon Aug 24** | **Loyola Chicago** | Semester | Classes Dec 5; finals Dec 7–12 |
| **Mon Aug 24** | **NIU** | Semester | Classes Dec 5; finals Dec 7–12 |
| **~Tue Sep 22** ⚠ UNVERIFIED | **Northwestern** | ⚠ **QUARTER** | ~Dec 12 |
| **Early–mid Sept** ⚠ NOT RETRIEVED | **DePaul** | ⚠ **QUARTER** | ⚠ unknown |
| **Mon Sep 28** | **University of Chicago** | ⚠ **QUARTER** | **Ends Sat Dec 12 — before Christmas** ⚠⚠ LATEST START IN THE STATE |

**Two waves, six weeks apart.** Everything semester-based is running by August 24. Nothing
quarter-based is running before roughly September 22. **Hyde Park is five weeks behind the
rest of Chicago.**

Breaks worth knowing: UIUC and ISU and SIU all take a **nine-day Thanksgiving** (Nov 21–29).
UChicago takes the **whole Thanksgiving week** (Nov 23–27). Only **Loyola (Oct 5–6)** and
**Illinois Tech (Oct 12–13)** have a genuine October break. UIUC, UIC and NIU have none.

## (2) Outside-entity access, ranked most to least open

| Rank | Campus | Access | Why |
|---|---|---|---|
| 1 | **DePaul** | **4** | A published paid external route ("outside organizations … must pay a fee to use space," 100% rental, 50% deposit, COI naming DePaul) **and** a clean sponsorship exemption ("External groups working with a University unit or recognized student organization are **exempt**"). Two doors. Only risk: the mission-conflict veto. |
| 2 | **UIC** | **4** | DOS-8100-004 exists specifically for non-affiliated entities: written agreement + insurance + security assessment + fees, evaluated "viewpoint-neutral." No commercial ban anywhere in the text. Parallel sponsorship door in the Open Expression policy. Rates unpublished. |
| 3 | **Northwestern** | **3** | Sponsorship is the named and only mechanism; commercial use "permitted only with permission from the appropriate unit officer." Workable, but the sponsor carries the liability and commercial solicitation is banned outright at the Rock, door-to-door and in residence halls. |
| 4= | **Loyola** | **3 (provisional)** | Conference Services rents to all comers, but **no solicitation policy was found in the full A–Z index** — the operative rule is in an unretrieved handbook. Gap, not a green light. |
| 4= | **UChicago** | **3 (provisional)** | Student Manual is **unreadable (redirect loop)**. Nothing known either way. Private, no forum obligation. |
| 4= | **Illinois Tech** | **3 (provisional)** | Prior approval required for **every** flyer; 30-day lead time for guest-heavy events; no published external-vendor route and no published ban. |
| 4= | **NIU** | **3 (provisional)** | Policy simply **not located** in the Policy Library's facilities category. One phone call closes it. |
| 8 | **Illinois State** | **2** | Non-university groups "cannot conduct sales or solicitations on campus except as approved"; the definition of "sales" sweeps in distributing circulars and product samples; Festival ISU **expressly refuses community business vendors**. A fee schedule for outside entities exists but is unpublished. |
| 9 | **UIUC** | **2** | § 2-506 bars outside organizations from "**solicitations, collections, fund drives**"; § 2-407 limits quad distribution to **non-commercial** topics; Illini Union tables are RSO/department-only and goods may be sold "only … for the benefit of a Registered Student Organization." A paid FUA route exists under CAM FO-81 for *space*, not for soliciting. |
| 10 | **SIU Carbondale** | **1** | Non-university solicitation permits are limited to entities holding a permit **every year since July 1, 1978**, Board of Trustees contractors, Flea Market participants, or sellers of constitutionally protected printed material. **DGD qualifies under none of the four. Effectively closed.** |

## (3) Every confirmed phone number, consolidated

| Campus | Office / person | Number | What it controls |
|---|---|---|---|
| UIUC | Illini Union Event Services | **(217) 333-0691** | Information tables, Union space, insurance determination |
| UIUC | Office of the Dean of Students | **(217) 333-0050** | Canvasser registration; Student Code enforcement |
| UIUC | Student Engagement (RSOs) | **(217) 300-8757** | RSO recognition; the 1,127-org directory |
| UIUC | New Student & Family Experiences | **(217) 333-4057** | Welcome Week and **Quad Day date** |
| UIC | Center for Student Involvement | **(312) 413-5070** | Fall Involvement Fair & Service Expo |
| UIC | Meetings & Conferences | **(312) 965-1708** | Books RSOs, departments **and non-university clients** |
| UIC | Venues & Events | **(312) 413-5700** | Arena, Dorin Forum, external contracts |
| UIC | Dean of Students | **(312) 996-4857** | Owns DOS-8100-004 and Open Expression |
| UIC | Student Veteran Affairs | (312) 413-5112 | (listed for completeness) |
| Northwestern | Assistant VP & Dean of Students | **(847) 491-8430** | Named contact in the facilities policy — the one NU number |
| DePaul | Lincoln Park Student Center | **(773) 325-7346** | External bookings, LP campus |
| DePaul | Loop Student Center | **(312) 362-8624** | External bookings, Loop campus |
| DePaul | Division of Student Affairs | **(312) 362-8610** | Routes to Student Involvement; academic-calendar chase |
| DePaul | Senior Executive for University Mission | **(312) 362-8042** | ⚠ The mission-conflict veto |
| DePaul | Office of General Counsel — Mary Devona Stark | **(312) 362-7503** | Policy library contact |
| Illinois State | Dean of Students — Dean on Duty | **(309) 438-2008** | Festival ISU; student involvement |
| Illinois State | Office of the President (owner, Policy 6.1.1) | **(309) 438-5677** | The facility/solicitation policy and its "as approved" discretion |
| Illinois State | Office of the Provost | **(309) 438-7018** | Academic calendar |
| NIU | Registration & Records | **(815) 753-0681** | Calendar, add/drop |
| NIU | Policy Library | **(815) 753-5560** | ⚠ Closes the NIU policy gap in one call |
| SIU Carbondale | Student Center Event Services | **(618) 536-3351** | Rates, space, solicitation/fundraising forms |
| SIU Carbondale | Registrar | **(618) 453-2963** | Calendar, registration deadlines |
| SIU Carbondale | Office of the Chancellor | **(618) 453-2341** | Policy location |
| SIU Carbondale | Main line | **(618) 453-2121** | **Campus operator — main line** |
| Loyola | Conference Services | **(773) 508-8090** | External rentals across all campuses |
| Loyola | Center for Student Engagement | **(773) 274-3000** | RSOs, LUCommunity, Welcome Week |
| Loyola | Division of Student Development | **(773) 508-3890** | Parent division |
| UChicago | Center for Leadership and Involvement | **(773) 702-8787** | RSOs, RSO fair, space scheduling |
| UChicago | Student Centers | **(773) 834-0858** | ⚠ Ida Noyes + Reynolds Club — says yes or no to a table |
| UChicago | Campus and Student Life | **(773) 702-5243** | Parent division |
| UChicago | International House | (773) 753-2270 | Rentable venue |
| UChicago | Housing & Residence Life | (773) 702-7366 | (listed for completeness) |
| Illinois Tech | Office of Student Affairs | **(312) 567-3081** | ⚠ Approves every posted or distributed item |

**32 confirmed numbers across 10 campuses.** Offices with **no** published number, kept as
rows with the URL to try: UIUC OVCFA (OVCFA@illinois.edu), UIC Student Centers
(studentcenters@uic.edu), Northwestern Norris Event Planning
(Norris-events@northwestern.edu), ISU Conference Services
(conferences.illinoisstate.edu/scheduling/), ISU Festival contact Maren Keller
(mkelle4@IllinoisState.edu), Illinois Tech Office of Student Life
(welcomedesk@illinoistech.edu), Illinois Tech Registrar.

## (4) The state campus free-speech statute

**There isn't one.** Illinois has enacted no FORUM-Act-style campus free-expression
statute. The two Chapter 110 acts that touch expression are:

- **110 ILCS 10, Campus Demonstrations Policy Act** — imposes an order-maintenance duty on
  administrations ("responsible for maintaining decorum and order on the campus"), with a
  directive that demonstration policies show "special attention to firmness." **Runs
  against outside actors, not for them.**
- **110 ILCS 13, College Campus Press Act** — "All campus media produced primarily by
  students at a State-sponsored institution of higher learning is a public forum for
  expression by **the student journalists and editors**." Binds the named public
  universities and community colleges only, protects student editorial independence, and
  **does not reach commercial speech by non-affiliated entities.** Its practical value to
  DGD is indirect but real: advertising in a student newspaper is an editorial decision
  made by students, not an administrative permission.

**Consequence: in Illinois there is no statute an ambassador can invoke at a table.** Every
fee, approval requirement and commercial ban documented above is lawful. What Illinois has
instead of a speech statute is a **regulatory** stack — BIPA, DACPA and the Credit Card
Marketing Act — that runs the other way, against DGD. Illinois is a state where the law is
a constraint on the project, not a lever for it.

## (5) Known gaps to close by phone

⚠⚠ **Blocking:**
1. **DePaul Autumn Quarter 2026 dates** — entirely unknown; the calendar is a JavaScript
   app. **(312) 362-8610.** Nothing about a DePaul visit can be planned until this lands.
2. **Northwestern Fall 2026 calendar** — dates inferred from an unlabelled registrar
   application, with weekday labels that matched 2025 rather than 2026. **(847) 491-8430**,
   then the Registrar.
3. **DACPA registration status for DGD** (205 ILCS 731 § 15-5). Legal question, not a phone
   call to a campus — but it gates every Illinois activity, including a table.
4. **BIPA compliance artefacts** — written release, published retention schedule, no-sale
   commitment — must exist before any scan-based onboarding happens on Illinois soil.

⚠ **Important:**
5. **NIU's solicitation / facility-use policy** — not located. **(815) 753-5560.**
6. **UChicago's use-of-space and solicitation policy** — Student Manual returns a redirect
   loop. **(773) 834-0858.**
7. **Loyola's solicitation rule** — absent from the university A–Z; it is in a handbook.
   **(773) 508-8090** or **(773) 274-3000.**
8. **Quad Day 2026 exact date** (Sat Aug 22 vs Sun Aug 23) and whether any non-RSO booth
   exists. **(217) 333-4057.**
9. **UIC Fall Involvement Fair date** and whether non-affiliated entities may buy in.
   **(312) 413-5070.**
10. **Rate cards** — unpublished at UIUC (Illini Union), UIC (venues), ISU (Conference
    Services outside-entity rate), SIU (FY rate sheets), Loyola (all), UChicago, IIT.
11. **UIUC blockchain/crypto RSO** — the 1,127-entry directory defeated keyword search.
    Ask Student Engagement to search it: **(217) 300-8757.** Do **not** record "none exists."
12. **UIC clubs** — connect.uic.edu fails SSL verification for automated clients.
    **(312) 413-5070.**
13. **Illinois Tech 2026-2027 Student Handbook** — only the 2025-2026 PDF is posted; check
    for a superseding edition and read its solicitation section. **(312) 567-3081.**
14. **Fall 2026 offering status** for UIUC CS 407/507/425 and UIC FIN 481.
15. **HackIllinois 2027 sponsorship tiers** — no tier sheet published;
    contact@hackillinois.org.

## (6) Audience-mismatch check

No campus in this set is health-sciences-only, law-only or graduate-only. All ten have
substantial undergraduate populations with business and/or computer-science programmes.
Two notes:

- **Loyola's Health Sciences Campus (Maywood)** is medical/nursing only — go to **Lake
  Shore** (Rogers Park) for undergraduates, or **Water Tower** for Quinlan business.
- **Illinois Tech** is genuinely small (~7,000) and heavily graduate/international. High fit
  per student, low absolute numbers. It is a half-day stop, not a full one.
- **DePaul's Loop campus** is business/law/adult-learner weighted; **Lincoln Park** is where
  the traditional undergraduate population and the involvement fair are.
