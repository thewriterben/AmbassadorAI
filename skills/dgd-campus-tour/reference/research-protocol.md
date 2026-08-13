# Research Protocol — adding a state, and verifying one

Two procedures live here. **Research** gathers a state that isn't bundled yet.
**Verification** re-checks time-critical facts before anyone spends money. They are
different jobs and the second is not optional.

---

## Part 1 — Researching a new state

### Choose the campuses first

Ten per state is a sensible ceiling. Past that the marginal campus is a community college
with no finance club and no published policy, and the data thins out. Work in this order:

1. **Flagship publics** — the biggest audience and the best-documented policies.
2. **Regional publics** — often *more* permissive than flagships and consistently
   overlooked. Lewis-Clark State turned out to have the most permissive written policy in
   Idaho; nobody would have guessed that from reputation.
3. **Private universities** — usually restrictive, sometimes flatly closed, but worth
   knowing which.
4. **Community colleges** — cheap to include if they're in a metro you're already visiting.

Two traps worth naming, because both bit the original research:

- **Check what a campus actually teaches.** WSU Spokane looks like a major campus and is
  in fact a health-sciences campus — no undergraduate business or CS program at all. The
  audience was 75 miles away in Pullman.
- **Check the academic calendar system.** Semester and quarter schools start five weeks
  apart. A tour built around late-August welcome weeks misses every quarter school, and
  misses BYU-Idaho by a month.

### The subagent prompt

Spawn **one general-purpose subagent per state**, in parallel. Copy this and fill the
bracketed parts:

> You are researching [STATE] university campuses for a [TERM] student-outreach tour by a
> cryptocurrency project (Digital Gold / DGD). Today is [DATE]. Use WebSearch and WebFetch
> extensively. This is a real-world research task — accuracy matters more than completeness.
>
> CAMPUSES (in priority order): [LIST]
>
> For EACH campus, find and report:
>
> **A. ACADEMIC CALENDAR** — [TERM]: first day of classes, add/drop deadline, fall break,
> Thanksgiving break, last day of classes, finals week. Note whether the school is on
> semesters or quarters, and flag any distinctive block/track/quad system.
>
> **B. INVOLVEMENT / CLUB FAIR EVENTS** — the actual [TERM] involvement fair, org fair, or
> welcome-week tabling event: name, date, location, **whether outside organizations can
> table**, cost, application deadline and URL. If the date is not yet published, say so
> explicitly and give the recurring pattern plus the URL where it will be posted.
>
> **C. SOLICITATION / OUTSIDE-VENDOR POLICY** — the actual written policy governing
> non-university entities distributing materials, tabling, or soliciting students. **Quote
> the key restrictions verbatim.** Find: policy name/number, effective date, URL, whether a
> registered student organization must sponsor an outside group, the space-reservation
> process and fees, free-speech-zone rules, insurance requirements, and any explicit ban on
> commercial solicitation or financial-product marketing. Note any anti-"fronting" rule —
> language forbidding a campus group from reserving space on behalf of an outside entity.
> Private institutions have no public-forum obligation; capture that honestly.
>
> **D. RELEVANT STUDENT CLUBS** — search the campus org directory for: blockchain,
> cryptocurrency, bitcoin, Web3, fintech, investment/finance, economics, entrepreneurship,
> computer science/ACM, data science, and any Financial Management Association chapter.
> Give club name, whether currently active, the directory URL, and any published contact.
> **Do NOT invent officers' names** — rosters rotate annually and a stale name is worse
> than none.
>
> **E. FACULTY / STAFF** — only where you can confirm it on a live university page:
> faculty who teach or research blockchain, cryptocurrency, fintech, digital assets,
> monetary economics or payments; plus the administrative offices that actually grant
> permission (Student Involvement, Dean of Students, Business/Auxiliary Services, Campus
> Reservations, Event Scheduling). Give name, title, department, official email or phone,
> and the URL. Where you cannot confirm an individual, **do not guess** — give the
> department directory URL and say "look up here."
>
> **F. COURSES** — actual catalog courses touching blockchain/crypto/fintech/digital money,
> with course code, title, and URL. Note whether they are offered in [TERM] specifically,
> and if a course is typically offered in another term, say so.
>
> **G. RELEVANT EVENTS** — career fairs, entrepreneurship/startup weeks, business-school
> speaker series, hackathons in [TERM], with dates and URLs. Hackathons with open sponsor
> pipelines are especially valuable — they are private events and sidestep campus
> commercial-use rules.
>
> **CRITICAL RULES:**
> - NEVER fabricate a person's name, email, phone number, fee, or date. If you cannot
>   verify it on a live page, mark it UNVERIFIED and give the URL to check.
> - Every factual claim must carry the source URL it came from.
> - Distinguish clearly between "confirmed on the university's [TERM] page" and "this is
>   the historical pattern."
> - If a page is robots-blocked, 403s, or is JavaScript-rendered and unreadable, say so
>   plainly and give the URL. That is a useful finding, not a failure.
>
> **OUTPUT:** Structured markdown, one section per campus, using the A–G headings above,
> with a "Source URLs" list at the end of each campus section. Finish with a cross-campus
> summary: term-start dates at a glance, and outside-entity access ranked from most to
> least open. This output is data for a document build, not a message to a human.

### Turning the result into `data/<state>.py`

Copy `data/_TEMPLATE.py` and fill it in. `reference/data-schema.md` explains every field.
Three things you must do yourself, because the subagent can't:

**Set the `access` rating (1–5).** This answers *"what does the written policy permit an
outside for-profit organization to do here"* — not "how good is the audience." A campus
with a thriving blockchain club and a flat solicitation ban is a **1 with a note**, not a
4. Getting this wrong sends ambassadors to campuses that will turn them away.

**Write the `play`.** One paragraph: what should the ambassador actually do here, and why.
Name the single best door. If the honest answer is "skip this campus," say that plainly
and give the reason — a clear "no" saves more time than a vague "maybe."

**Write the `DEADLINES` rows.** Every date-certain item: registration closes, event day,
term start. Use a real ISO date in position 0 so countdowns compute correctly next term.
Undated monitor-only items take `""` and sort last.

### Also research the statutory layer

Campus policy is only one layer. `reference/compliance.md` ends with three statutory
questions to answer for each new state — anti-pyramid, money transmission, and privacy /
minors. Add findings to the existing issues rather than creating new ones.

---

## Part 2 — The verification pass

Do this before an ambassador registers for anything, pays anything, or books travel.

Research subagents are good but not infallible, and university pages go stale without
changing their URL — a page can display last year's dates indefinitely. So spawn a
**second, independent** agent and give it a specific adversarial job.

### What to verify

Only the things that cost money or miles if wrong:

- fair dates and times
- registration deadlines
- fees, and which tier applies
- any contact you are about to hand an ambassador
- anything you marked as urgent

Not the whole packet. Policy text and faculty pages are stable; dates and fees are not.

### The framing that matters

Ask the agent to **refute**, not to confirm:

> Independently VERIFY (or refute) the following claims by fetching the live pages. Do not
> assume the claims are true — your job is to catch errors before someone spends money on
> them. For EACH claim report CONFIRMED / REFUTED / CANNOT VERIFY, what the live page
> actually says today, and the URL. If a date or fee has CHANGED from what is claimed,
> that is the single most valuable thing you can report — flag it loudly. If a page is
> unreachable, say so plainly rather than guessing.
>
> Finish with a "CORRECTIONS NEEDED" section for anything wrong or stale, and a "NEWLY
> FOUND" section for details the first pass missed — obfuscated emails, additional fee
> tiers, deadlines.

This framing is not a stylistic preference. On the original nine-state run it is exactly
what caught the one real error: a vendor-fair page still showing the previous year's
cycle, whose "deadline" was a leftover date that fell on a **Sunday**. Seven of eight
claims confirmed; a confirmation-seeking check would have sailed past the eighth and sent
someone chasing a deadline that didn't exist.

Watch for that specific tell — **a weekday that doesn't match the date is almost always a
stale page.**

### After a correction

Fix `data/<state>.py`, rebuild, and tell the ambassador what changed and why. Be
especially clear when something they thought was urgent turns out not to be — the relief
is worth as much as the warning, and it teaches them to trust the packet.
