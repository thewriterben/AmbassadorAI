# Compliance Issue Map — LOCKED

> **This file is locked, and it is not legal advice.** It is a sourced issue map for
> licensed counsel to work from. Items marked **[ATTORNEY]** need a practitioner in the
> relevant state. Do not edit it, and do not omit it from a packet — the builders
> regenerate it into every packet as `00-COMPLIANCE.md` from the same source, so the two
> can never drift.

Read this before a packet ships, and any time an ambassador asks whether something is
allowed. The single most common mistake is assuming the risk is state pyramid law. It
isn't — see the headline finding and the first premise correction.

---

## The headline finding

> The single most consequential finding in this research is not about campuses at all.
>
> On March 17, 2026 the SEC issued an interpretive release (Nos. 33-11412; 34-105020, File No. S7-2026-09, effective March 23, 2026) that, for the first time, formally addresses airdrops. It creates a "Covered Airdrop" concept: airdrops of non-security crypto assets where recipients provide NO money, goods, SERVICES, or other consideration do not satisfy Howey's "investment of money" element. But the release expressly "does not extend that conclusion to airdrops for services or other structures that require recipients to provide value in exchange." Practitioner analysis identifies referrals, social-media tasks, and promotional activity as disqualifying.
>
> DGD's new model sits on the wrong side of that line on two independent grounds:   1. Referral rewards are compensation for a SERVICE.   2. The $21 credit is announced in advance with conditions attached — a PROSPECTIVE, conditioned      distribution, which the release treats as materially riskier than a retroactive, unannounced snapshot.
>
> The structural trap: the referral component is TOO LITTLE consideration to trigger state anti-pyramid statutes (which require cash or a purchase) but ENOUGH consideration to break the SEC's airdrop carve-out (which requires zero, including services). The design gets the worst of both frameworks rather than the benefit of either.
>
> The good news is that this is also the cleanest available fix, and it is a product decision rather than a legal one: removing the referral tier — or converting it to a retroactive, unannounced snapshot reward — is the single highest-leverage change available, because it is exactly what moves DGD from outside the Covered Airdrop carve-out to inside it.
>

---

## Assumptions that did not survive checking

These are the working assumptions the original brief carried in. Eleven of them were
wrong, and several change the risk ranking materially. Check a new state's assumptions
against this list before trusting them.

| Assumption | What the research found | So what |
|---|---|---|
| State anti-pyramid statutes are the top risk | NO — they are the LOWEST risk on this list. All nine states define the offence around a participant giving 'consideration,' defined as payment of money or purchase of goods/services/intangible property. Several EXPRESSLY EXCLUDE recruiting effort (UT, WA, MT, AZ; OR excludes 'personal services'). Colorado requires consideration EXCEEDING $50 — a free program is facially outside its statute. A genuinely zero-cost program falls outside the literal text of all nine. | But treat '$0 forever, no purchase path' as a HARD ARCHITECTURAL CONSTRAINT, not a marketing decision. The moment any paid tier appears, all nine switch on simultaneously — and Utah's is a FELONY statute. |
| The CLARITY Act will provide cover | NO — the CLARITY Act IS NOT LAW. It passed the House 294–134 on July 17, 2025 and was placed on the Senate Legislative Calendar June 1, 2026; it still requires 60-vote Senate passage and reconciliation with the Senate Agriculture version. The GENIUS Act (stablecoins) WAS signed July 18, 2025. Do not plan around CLARITY passing before Fall 2026. | Plan for the law as it is in August 2026, not as it may be in 2027. |
| The $600 1099 threshold applies | OUT OF DATE. The One Big Beautiful Bill Act §70433, signed July 4, 2025, raised the IRC §§6041 and 6041A information-reporting threshold from $600 to $2,000, effective for payments made in 2026 (inflation-indexed from 2027). | At $21/validation a single validation is far below — but a heavy referrer clears $2,000 in roughly 95 referrals, which is achievable for a motivated campus ambassador. Sub-threshold amounts remain TAXABLE INCOME regardless. |
| Washington has a comprehensive privacy act to worry about | NO — Washington has NO comprehensive consumer privacy act, only the My Health My Data Act, which is not on point. Washington is LOW privacy risk here. | The state to actually watch is MONTANA: the MCDPA threshold is 50,000 consumers — the lowest of the nine — and it is plausible if the program scales. |
| COPPA is the relevant minors statute | WRONG STATUTE, and it will lull you. COPPA's threshold is UNDER 13 — essentially no undergraduates. The real problem is contract law: a person UNDER 18 can generally disaffirm a contract, meaning a minor can accept the $21, refer friends, and then void the terms of service, arbitration clause, and any clawback. | Dual-enrolled high schoolers are on every campus in all nine states and frequently hold institution-issued .edu addresses — so the .edu path is SPECIFICALLY the path that admits minors. Age-gate at 18 AT THE TABLE. |
| FERPA governs your collection of student emails | NO — FERPA binds funded educational institutions, not third parties. A student voluntarily typing their own email at a table is not a disclosure 'from education records' by the institution. The real constraint is the university's own solicitation/AUP policy and any data-sharing agreement. | DO NOT represent to any student or administrator that DGD is 'FERPA compliant' — the statute doesn't apply to you and the claim would itself be a §5 deception risk. |
| WSU Spokane is a good target | NO — WSU Spokane is WSU's HEALTH SCIENCES campus (Medicine, Nursing, Pharmacy, Medical Sciences). There is no undergraduate business or CS program there. The business and CS students are at WSU PULLMAN. | Redirect that stop to Pullman, 75 miles south. |
| EWU is on semesters | NO — EWU is primarily a QUARTER institution: 'four 10-week terms per year,' with semesters only for specific programs. | Only WSU and Gonzaga are semester schools in Washington. |
| UVU has a blockchain/fintech program | NOT SUPPORTED — no fintech, blockchain, or digital-assets program, center, or institute appears anywhere on the Woodbury School of Business site. | UVU is a place to BUILD a club relationship, not to find one. |
| CU Boulder's Media Archaeology Lab has a blockchain footprint | NO — the MAL is a historical-computing hardware archive directed out of English/Intermedia. No blockchain research footprint found. | CU Boulder's real blockchain presence is Eric Alston at Leeds, the CYBR/CSCI 5240 course, and the CU Blockchain RSO. |
| Arizona campuses have already started Fall 2026 | NO — no campus in the dataset has started as of Aug 11, 2026. Earliest starts are ASU and CU Boulder on Aug 20. | There is a 9-day runway before the first campus opens. |

---

## Issue map

### 1. Referral Compensation / Endless-Chain & Pyramid Law

**Severity: LOW (statutory) — but a cliff, not a slope**

All nine state anti-pyramid statutes require the participant to give 'consideration,' defined as cash or a purchase; several expressly exclude time and effort spent recruiting. A genuinely free program falls outside their literal text. The real referral exposure is FEDERAL and UDAP-based. The FTC's Koscot analysis has no consideration element: it asks whether there is a right to receive rewards for recruiting 'unrelated to the sale of the product to ultimate users,' and directs attention to 'the incentives that the compensation structure creates.' DGD has NO product sold to ultimate users at all — in a Koscot frame the entire compensation structure is recruitment. Whether §5 reaches a scheme with zero participant outlay is genuinely unsettled; no enforcement action against a free-to-join, no-purchase referral program was found.

**What this means for a campus table:** Keep the program genuinely free — no fee, no purchase, no 'buy in to unlock referrals,' no upsell tier. Colorado's $50 floor is per-participant: a $51 anything destroys it.

| Citation | What it says | Source |
|---|---|---|
| **Utah Code §76-17-301 to -304** | ⚠ Former Title 76 Ch. 6a was REPEALED 5/7/2025 and recodified into Ch. 17. Any memo citing 76-6a-101 et seq. cites DEAD LAW. §76-17-301(2): consideration 'does not include… time or effort spent in selling or recruiting.' Conducting = 3rd-degree FELONY. | <https://le.utah.gov/xcode/Title76/Chapter17/C76-17_2025050720250507.pdf> |
| **RCW 19.275.010–.030 (WA)** | Consideration = 'cash or the purchase of goods, services, or intangible property'; expressly excludes 'time and effort spent in pursuit of sales or recruiting activities.' Per se violation of the Consumer Protection Act, Ch. 19.86 RCW. | <https://app.leg.wa.gov/rcw/default.aspx?cite=19.275&full=true> |
| **C.R.S. §6-1-102(9) (CO)** | Requires 'valuable consideration IN EXCESS OF FIFTY DOLLARS.' A free program is FACIALLY OUTSIDE Colorado's statute — the NARROWEST of the nine for this fact pattern. | <https://law.justia.com/codes/colorado/title-6/fair-trade-and-restraint-of-trade/article-1/part-1/section-6-1-102/> |
| **Idaho Code §18-3101** | Consideration = 'a payment of any money, or the purchase of goods, services, or intangible property.' | <https://legislature.idaho.gov/statutesrules/idstat/title18/t18ch31/sect18-3101/> |
| **ORS 646.609; ORS 646.608(1)(r)** | 'Pyramid club' requires an 'investment'; investment is expressly 'for a consideration OTHER THAN PERSONAL SERVICES.' The clearest textual exclusion of a labor/referral-only structure. | <https://oregon.public.law/statutes/ors_646.609> |
| **MCA §30-10-324, §30-10-325 (MT)** | Excludes 'a participant's time and effort expended in the pursuit of sales or in recruiting activities.' | <https://mca.legmt.gov/bills/mca/title_0300/chapter_0100/part_0030/section_0240/0300-0100-0030-0240.html> |
| **A.R.S. §44-1731 (AZ)** | Excludes 'Time and effort spent in pursuit of sales or recruiting activities.' | <https://codes.findlaw.com/az/title-44-trade-and-commerce/az-rev-st-sect-44-1731.html> |
| **W.S. §§40-3-101 to -125 (WY)** | ⚠ §40-3-103 is titled 'ENDLESS CHAINS AND REFERRAL SALES PROHIBITED' — the closest textual hook of the nine. [ATTORNEY] — full verbatim text of §40-3-103 could NOT be retrieved. | <https://law.justia.com/codes/wyoming/title-40/chapter-3/> |
| **NRS 598.100, .110, .120 (NV)** | ⚠ Verbatim §598.100 definitions COULD NOT BE VERIFIED — Nevada's server and two mirrors returned only tables of contents. NRS 598.110 makes pyramid schemes/endless chains deceptive trade practices; NRS 598.120 makes participant contracts VOIDABLE. [ATTORNEY] | <https://www.leg.state.nv.us/nrs/NRS-598.html> |
| **FTC Business Guidance Concerning MLM** | 'There is no percentage-based test to determine whether an MLM is a pyramid scheme' — attention goes to 'the incentives that the compensation structure creates.' Under BurnLounge: is the 'focus in promoting the program rather than selling the products'? | <https://www.ftc.gov/business-guidance/resources/business-guidance-concerning-multi-level-marketing> |


### 2. Securities & Money Transmission

**Severity: ⚠ HIGHEST — this should gate the Fall 2026 launch**

See the headline finding. Beyond Howey: state money-transmitter exposure turns on whether USD-denominated redeemable 'credit' is stored value. PEER-TO-PEER TRANSFERABILITY IS THE SINGLE FACT MOST LIKELY TO CONVERT THIS INTO MONEY TRANSMISSION EVERYWHERE. If credit is non-transferable and redeemable only for DGD's own goods, the analysis gets much easier; if it is transferable or cashable, assume licensing exposure in ID/WA/OR/UT/CO/NV/AZ.

**What this means for a campus table:** Do not launch the campus program until counsel has answered whether the referral tier forfeits the Covered Airdrop carve-out, and whether a restructured retroactive distribution gets back inside it.

| Citation | What it says | Source |
|---|---|---|
| **SEC Release Nos. 33-11412; 34-105020** | File No. S7-2026-09, announced Mar 17, 2026, effective Mar 23, 2026. §VII: 'Application of the Howey Test to Certain Crypto Asset Disseminations Known as Airdrops' (A. Airdrops Generally; B. Covered Airdrops; C. Interpretation). Five-category taxonomy: digital commodities, digital collectibles, digital tools, stablecoins, digital securities. | <https://www.sec.gov/files/rules/interp/2026/33-11412.pdf> |
| **In re Tomahawk Exploration LLC (SEC 2018)** | Historic baseline, still instructive: 'free' bounty-program tokens held to be a SALE of securities because the issuer received value (promotional services). The 2026 release narrows but does not overrule the logic that SERVICES RENDERED = CONSIDERATION. | <https://blogs.orrick.com/securities-litigation/2018/09/11/in-the-matter-of-tomahawk-exploration-llc-no-such-thing-as-a-free-launch/> |
| **CLARITY Act status** | NOT LAW. House 294–134 Jul 17, 2025; Senate Legislative Calendar Jun 1, 2026. GENIUS Act (stablecoins) signed Jul 18, 2025. | <https://www.lw.com/en/us-crypto-policy-tracker/legislative-developments> |
| **Montana — no MT licensing** | 'The Montana Division of Banking and Financial Institutions does not regulate money transmitters.' | <https://banking.mt.gov/moneytransmitters> |
| **Wyoming — W.S. §40-22-104(a)(vi)** | EXPRESS VIRTUAL-CURRENCY EXEMPTION: exempts 'buying, selling, issuing, or taking custody of payment instruments in the form of virtual currency or receiving virtual currency for transmission.' ⚠ [ATTORNEY] — exempts VIRTUAL CURRENCY, not necessarily a USD-denominated balance. | <https://law.justia.com/codes/wyoming/title-40/chapter-22/section-40-22-104/> |
| **MTMA adoption grid** | AZ (2022 Ch. 236, full CSBS model); NV (A.B. 21, eff. Jul 1, 2023); CO (H.B. 25-1201, eff. Jul 17, 2025); UT partial only (S.B. 183 2022 control provisions, NOT full MTMA); ID, WA, OR not shown as MTMA adopters — LEGACY state acts apply and are often BROADER, not narrower. [ATTORNEY] | <https://www.csbs.org/mtma-legislative-update-4232026> |
| **FinCEN FIN-2019-G001** | 'Acceptance and transmission' test. An administrator becomes a money transmitter 'the moment that person issues [CVC] against the receipt of another type of value.' If DGD issues credit purely gratuitously and receives nothing, the acceptance prong is arguably unmet — but the guidance recognizes NO exemption for free distributions or closed-loop systems. [ATTORNEY] | <https://www.fincen.gov/system/files/2019-05/FinCEN%20CVC%20Guidance%20FINAL.pdf> |


### 3. KYC / AML / Privacy

**Severity: MODERATE — and largely self-inflicted**

A BSA/KYC obligation attaches only if DGD is a money services business — which loops back to Issue 2. IF DGD IS NOT AN MSB, IT HAS NO BSA OBLIGATION, AND COLLECTING GOVERNMENT ID IS A PURE LIABILITY WITH NO OFFSETTING COMPLIANCE BENEFIT. Meanwhile collecting ID documents may pull DGD into the GLBA Safeguards Rule and creates breach exposure.

**What this means for a campus table:** DON'T COLLECT WHAT YOU DON'T NEED. Since the KYC path is optional and the BSA likely doesn't compel it, the cheapest risk reduction available is to NOT SCAN GOVERNMENT ID AT A FOLDING TABLE AT ALL.

| Citation | What it says | Source |
|---|---|---|
| **GLBA Safeguards Rule, 16 C.F.R. Part 314** | Amended 2023 to add breach notification for non-banking financial institutions. [ATTORNEY] — whether DGD is a 'financial institution' under the Rule is genuinely contestable and fact-dependent. | <https://www.ftc.gov/legal-library/browse/rules/safeguards-rule> |
| **State comprehensive privacy acts** | CO CPA (SB 21-190, eff. Jul 1 2023, 100k consumers); OR OCPA (SB 619, eff. Jul 1 2024, 100k); UT UCPA (SB 227, eff. Dec 31 2023, $25M revenue AND volume); ⚠ MT MCDPA (SB 384, eff. Oct 1 2024, 50,000 consumers — LOWEST OF THE NINE, plausible if the program scales); WA: NONE (MHMDA only); NV, ID, WY, AZ: no comprehensive act. | <https://www.zerodaylaw.com/blog/us-state-privacy-acts> |
| **Biometrics** | None of the nine has an Illinois-BIPA-style private right of action. [ATTORNEY] if ID-document scanning extracts facial geometry. | — |


### 4. The .edu Email Path

**Severity: MODERATE — the credential is weaker than it looks**

FERPA does not bind DGD (see Premise Corrections). The real constraint is each university's own solicitation policy and acceptable-use policy. Separately, .edu verification is TRIVIALLY DEFEATED — alumni addresses that never expire, dual-enrollment accounts issued to minors, community-college self-service signup, forwarding aliases. That is a serious problem when the credential gates $21 of transferable value.

**What this means for a campus table:** Treat .edu as a WEAK SIGNAL, NOT A CREDENTIAL. Assume a nontrivial fraction of .edu accounts belong to alumni and to under-18 dual-enrolled students.

| Citation | What it says | Source |
|---|---|---|
| **US Dept. of Education, 'Responsibilities of Third-Party Service Providers under FERPA'** | Where PII is disclosed under the school-official exception, 'FERPA still governs its use, and the school or district is responsible for its protection.' The vendor is bound because it is 'under the direct control of the agency or institution.' 34 C.F.R. §99.31(a)(1)(i). | <https://studentprivacy.ed.gov/sites/default/files/resource_document/file/Vendor%20FAQ.pdf> |
| **University AUP language** | ⚠ COULD NOT VERIFY — a survey of university acceptable-use-policy language expressly barring third-party use of .edu addresses as a verification credential was not completed. Search each target institution's IT AUP and solicitation policy directly. | — |


### 5. Minors

**Severity: ⚠ HIGH — and the .edu path is what creates it**

A minor can accept the $21, refer friends, and then disaffirm the terms of service, the arbitration clause and any clawback. Dual-enrolled high schoolers are on every campus in all nine states and frequently hold institution-issued .edu addresses.

**What this means for a campus table:** AGE-GATE AT 18, AT THE TABLE, BEFORE THE PHONE COMES OUT — not at 13. Because the Colorado and Oregon provisions are keyed to ACTUAL KNOWLEDGE, a tabling rep who can see they're talking to a high schooler creates knowledge the company then has.

| Citation | What it says | Source |
|---|---|---|
| **COPPA, 15 U.S.C. §§6501–6506; 16 C.F.R. Part 312** | Applies to children UNDER 13 — essentially no undergraduates. Well-established but not independently fetched this session; verify before quoting. | — |
| **Minor's right to disaffirm** | General common-law contract principle. [ATTORNEY] — state-by-state; the rule and its exceptions were not verified in any of the nine. | — |
| **Utah App Store Accountability Act, SB 142** | Enacted Mar 26, 2025 — app-store age verification + age signals to apps. DIRECTLY RELEVANT if DGD ships a mobile app. | <https://www.khlaw.com/insights/kids-and-teens-privacy-2025-look-back-and-2026-predictions-part-ii-state-privacy-patchwork> |
| **Colorado Privacy Act minors amendments** | Eff. Oct 1, 2025: duty to address 'heightened risk of harm' to minors, DPIAs, and a prohibition on design features that 'significantly increase, sustain, or extend' minor use. ⚠ A REFERRAL LEADERBOARD IS EXACTLY THIS KIND OF FEATURE. | — |
| **Montana CDPA amendments** | Eff. Oct 1, 2025 (parallel to Colorado). | — |
| **Oregon HB 2008** | Eff. Jan 1, 2026: bans TARGETED ADVERTISING to consumers known to be 13–15. | — |


### 6. Tax

**Severity: LOW severity, but expensive to fix retroactively**

Promotional credit and referral rewards are taxable income to recipients regardless of reporting thresholds. Referral rewards paid for RECRUITING ACTIVITY look like §6041A compensation for services — a 1099-NEC question, not a prize question.

**What this means for a campus table:** Collect W-9 information FROM HIGH-VOLUME REFERRERS BEFORE paying them past $2,000 — chasing TINs from graduated students in January is how backup-withholding liability happens.

| Citation | What it says | Source |
|---|---|---|
| **One Big Beautiful Bill Act §70433** | Signed Jul 4, 2025: raises the IRC §§6041 and 6041A information-reporting threshold from $600 to $2,000, effective for payments made in 2026, inflation-indexed from 2027. Sub-threshold amounts remain TAXABLE. | <https://www.littler.com/news-analysis/asap/tax-bill-changes-1099-reporting-thresholds> |
| **Form 1099-DA** | Gross proceeds for transactions on/after Jan 1, 2025; basis reporting on/after Jan 1, 2026. 'Broker' = custodial platforms that 'take possession of the digital assets being sold.' NON-CUSTODIAL PLATFORMS ARE EXCLUDED, and a platform that merely distributes tokens without effecting sales is outside these rules — so 1099-DA is likely NOT DGD's problem. 1099-NEC/MISC is. | <https://www.irs.gov/newsroom/final-regulations-and-related-irs-guidance-for-reporting-by-brokers-on-sales-and-exchanges-of-digital-assets> |


### 7. Campus Marketing Restrictions

**Severity: ⚠ MOST LIKELY TO ACTUALLY HALT THE PROGRAM**

The binding constraint here is contractual and institutional, not statutory — universities control their own property and most require sponsorship or prior approval for third-party solicitation. The CARD Act does not cover crypto, but it established a durable institutional INSTINCT: many schools adopted flat bans on marketing financial products to students, written broadly enough to capture DGD by their terms. This is the area most likely to end the program operationally, quickly, and without any lawsuit.

**What this means for a campus table:** Get WRITTEN permission per campus, per event, before Fall 2026. Assume the sponsoring-student-org route is the only viable one at public universities. Budget for the possibility that a single bad local news story propagates a ban across a state system.

| Citation | What it says | Source |
|---|---|---|
| **CARD Act of 2009, Pub. L. 111-24, 12 C.F.R. §1026.57** | Prohibits issuers from offering a college student 'any tangible item to induce such student to apply for or open an open-end consumer credit plan' where the offer is made ON CAMPUS, NEAR CAMPUS, or at an institution-sponsored event. ⚠ This does NOT reach DGD (no open-end credit plan) — but '$21 in exchange for signing up, at a table on campus' is a near-perfect factual match to the conduct Congress banned. EXPECT ADMINISTRATORS TO REACT TO THE PATTERN, NOT THE CITATION. | <https://www.ecfr.gov/current/title-12/chapter-X/part-1026/subpart-G/section-1026.57> |
| **Columbia University — Prohibition of On-Campus Credit Card Marketing to Students** | A real policy that would capture DGD by its terms: 'The on-campus advertising, marketing or merchandising of credit cards directed at students is prohibited.' Enforcement: 'Violating commercial entities MAY LOSE CAMPUS ACCESS.' | <https://universitypolicies.columbia.edu/content/prohibition-campus-credit-card-marketing-students> |
| **Boise State Policy 1160 — Solicitation** | A target-state example: outside groups may solicit only 'if sponsored by a University unit or University-recognized student organization'; financial-product promotion is permitted only for state-endorsed programs coordinated through HR. Expect this structure across public universities in all nine states. | <https://www.boisestate.edu/policy/governance-legal/solicitation/> |
| **⚠ FTX campus ambassadors — the closest real-world precedent** | CNBC, Feb 14, 2023. The program was EXPLICITLY RECRUITMENT-COMPENSATED: one ambassador described the job as 'referring people and getting them to sign up, and making sure they started trading and depositing money,' paid 'as long as he fulfilled certain tasks and met targets.' Ambassadors ran campus events targeting '500 to 1,000 or 1,500 students.' On collapse, ambassadors bore the reputational damage from peers who lost money on their recommendation. THIS IS THE REFERENCE CASE EVERY GENERAL COUNSEL AND DEAN OF STUDENTS IN THE COUNTRY NOW HAS IN MIND. | <https://www.cnbc.com/2023/02/14/promoting-ftx-was-their-side-hustle-now-theyre-picking-up-the-pieces-.html> |
| **Could not verify** | No US university policy expressly naming cryptocurrency or digital assets in its solicitation policy was found, nor a documented instance of a crypto company being formally banned from a US campus. Web-search budget was exhausted — this is a GAP, not a negative finding. | — |


### 8. Advertising / UDAP — student ambassadors as compensated endorsers

**Severity: HIGH probability, moderate severity, ENTIRELY PREVENTABLE**

Student referrers are COMPENSATED ENDORSERS. Under the FTC Endorsement Guides the material connection must be disclosed EVERY TIME a student promotes DGD — including in a dorm-room conversation and in an unlabeled Instagram story. Liability for ambassador non-disclosure RUNS TO THE COMPANY, and 19-year-olds paid per signup will not disclose consistently without training and monitoring. Separately, describing $21 as 'free money' while it is locked, non-transferable, or contingent is a straightforward deception risk.

**What this means for a campus table:** Put '#ad' / 'I get paid if you sign up' in the ambassador contract as a MATERIAL TERM WITH A CLAWBACK, provide pre-written disclosure copy, and spot-check ambassador social posts. Ban unqualified 'free money,' 'risk-free,' and any statement about future token value outright.

| Citation | What it says | Source |
|---|---|---|
| **FTC Endorsement Guides, 16 C.F.R. Part 255 (2023 revision)** | Material connections must be clearly and conspicuously disclosed; the revision expanded treatment of employee/ambassador endorsements and of ADVERTISER RESPONSIBILITY FOR ENDORSER CONDUCT. | <https://www.ftc.gov/system/files/ftc_gov/pdf/p204500_endorsement_guides_in_2023.pdf> |
| **Washington — Ch. 19.86 RCW (Consumer Protection Act)** | Confirmed as the enforcement vehicle for RCW 19.275. | — |
| **Oregon — ORS 646.608 (UTPA)** | §646.608(1)(r) expressly reaches one who 'organizes or induces or attempts to induce membership in a pyramid club.' | <https://oregon.public.law/statutes/ors_646.608> |
| **Idaho — Idaho Code §48-603 (Consumer Protection Act)** | Catch-all at §48-603(17): 'Engaging in any act or practice that is otherwise misleading, false, or deceptive to the consumer.' Note §48-603 does NOT reference pyramid schemes — Idaho's pyramid provision is the criminal §18-3101. | — |
| **Colorado — C.R.S. §6-1-101 et seq.** | Colorado Consumer Protection Act. | — |
| **Nevada — NRS Ch. 598** | NRS 598.110 makes pyramid schemes/endless chains a deceptive trade practice. | — |
| **⚠ Could not verify** | UT CSPA, MT, WY and AZ general UDAP section numbers were NOT verified. Do not cite them without checking at le.utah.gov, mca.legmt.gov, wyoleg.gov, azleg.gov. | — |


---

## Red flags, ranked

Ranked by expected damage, not by how alarming they sound. Note that state anti-pyramid
statutes are last, deliberately.

| # | Risk | Detail | Severity |
|---|---|---|---|
| 1 | **The referral tier forfeits the SEC's brand-new airdrop safe harbor.** | Release 33-11412 (Mar 2026) excludes airdrops requiring recipients to provide 'services or other consideration,' and referrals are named as disqualifying. The single most consequential finding — and the cleanest fix. | HIGHEST severity, cleanest fix |
| 2 | **Prospective, pre-announced, conditioned distribution.** | Even setting referrals aside, the release treats retroactive, unannounced snapshots as far safer than prospective distributions announced with conditions attached. DGD's entire model is a pre-announced conditional offer. | High |
| 3 | **Campus access will be denied or revoked on institutional-policy grounds.** | Boise State Policy 1160 requires a sponsoring unit or RSO; Columbia-style flat bans on student-directed financial marketing are widespread. This stops the program in Fall 2026 without anyone filing anything. | MOST LIKELY TO ACTUALLY HALT THE PROGRAM |
| 4 | **The FTX ambassador precedent poisons the well.** | A recruitment-compensated crypto campus ambassador program is a pattern administrators have already been burned by. Reputational reaction is likely to outrun legal analysis. | High |
| 5 | **Minors obtained via the .edu path.** | Dual-enrolled high schoolers hold .edu addresses; a minor can disaffirm the TOS while keeping the value. Colorado's Oct 2025 minors amendments target exactly the engagement-maximizing design a referral leaderboard embodies. | High |
| 6 | **Money transmission if credit is transferable or fiat-redeemable.** | MT and WY are permissive; the other seven are not. TRANSFERABILITY is the fact that flips this. | Moderate–High |
| 7 | **FTC Act §5 / Endorsement Guides non-disclosure by student referrers.** | High probability, moderate severity, entirely preventable with training and contract terms. | Moderate |
| 8 | **Any future paid tier detonates nine state anti-pyramid statutes at once.** | Including Utah's felony provision (§76-17-303). Currently dormant — but it is a cliff, not a slope. | Dormant / catastrophic if triggered |
| 9 | **1099-NEC exposure for high-volume referrers at the new $2,000/2026 threshold.** | Low severity, easy to manage prospectively, expensive to fix retroactively. | Low |
| 10 | **State anti-pyramid statutes as currently structured.** | GENUINELY LOW RISK given the verified consideration requirements — contrary to the initial framing. Listed last deliberately. | Low |

---

## Questions that require a licensed attorney

Hand this table to counsel as-is. Several entries flag citations that could NOT be
verified — those especially need a practitioner, not a search engine.

| Jurisdiction | Question |
|---|---|
| **Federal / multistate** | Does the DGD referral tier fall outside the 'Covered Airdrop' interpretation in Release 33-11412 — and can a restructured (retroactive, unannounced) distribution get back inside it? — Securities counsel with crypto practice. |
| **Federal / multistate** | Is DGD an MSB under FIN-2019-G001 where it issues credit gratuitously and receives no value? — BSA/AML counsel. |
| **Federal / multistate** | Is DGD a 'financial institution' under the GLBA Safeguards Rule, 16 C.F.R. Part 314, if it collects government ID? |
| **Federal / multistate** | Is the $21 credit a prize, compensation for services, or a rebate for §§6041/6041A purposes, and when is it recognized? — Tax counsel/CPA. |
| **Federal / multistate** | Does FTC Act §5 reach a free-to-join, no-purchase recruitment-reward structure? (No enforcement precedent found — an OPEN question, not a settled one.) |
| **All nine states** | Is USD-denominated, redeemable 'credit' money transmission or stored value under that state's act? Does peer-to-peer transferability change the answer? |
| **All nine states** | Can a minor disaffirm the TOS, and what survives disaffirmance (arbitration clause, clawback, class waiver)? |
| **Wyoming** | Does the §40-22-104(a)(vi) virtual-currency exemption cover a DOLLAR-DENOMINATED balance? And what exactly does §40-3-103 ('Endless Chains and Referral Sales Prohibited') prohibit — its text COULD NOT BE RETRIEVED. |
| **Nevada** | Verify NRS 598.100's definitions of 'consideration' and 'endless chain' — UNVERIFIED. Note NRS 598.120 makes participant contracts voidable. |
| **Utah** | Confirm the 76-6a → 76-17 recodification is correctly applied; confirm the App Store Accountability Act (SB 142) does not impose age-signal duties on a DGD mobile app. |
| **Colorado** | Confirm the >$50 threshold in §6-1-102(9) forecloses pyramid liability, and assess the Oct 2025 minors amendments against a referral leaderboard. |
| **Montana** | Confirm no MT licensing applies to this product notwithstanding the Division's general statement; monitor the 50k MCDPA threshold. |
| **UT, MT, WY, AZ** | Confirm the correct general UDAP section numbers — these COULD NOT BE VERIFIED. |
| **Per campus** | Review each institution's solicitation policy, IT acceptable-use policy, and facility-use agreement before booking tabling. — Higher-education counsel. |

---

## Researching a new state

When you add a state that isn't bundled, the campus policy research (reference/
research-protocol.md) covers institutional rules. The **statutory** layer needs three
additions to this map, and they are quick:

1. **The state's anti-pyramid / endless-chain statute** — find the definition of
   'consideration' and check whether recruiting effort is expressly excluded. Most
   states exclude it; Colorado additionally requires consideration over $50.
2. **The state's money-transmission act** — whether a USD-denominated redeemable balance
   is stored value there, and whether peer-to-peer transferability changes the answer.
   Transferability is the fact most likely to flip it.
3. **Any comprehensive consumer-privacy act and its threshold**, plus minors provisions.
   Thresholds vary by an order of magnitude and the low ones matter as a program scales.

Add findings to the relevant issue above rather than creating a new one — the issue
structure is national and should stay stable.
