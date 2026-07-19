# Bug report — digitalgold.co serves a pre-migration white paper

**Reported:** 2026-07-19
**Reported by:** Benji (DGD Ambassador Program / AmbassadorAI wiki)
**Affects:** `https://digitalgold.co/Digital_Gold_White_Paper_2026.pdf` and every page linking it
**Severity:** High — the linked specification describes a distribution mechanic the product no
longer uses. Ambassadors, prospective participants and anyone doing diligence are reading it.

**Summary:** the white paper served at digitalgold.co is the **digitalgoldx.com-era document**,
carried across during the domain migration and never refreshed. It describes the superseded
1,000-level distribution and a $40 minimum; the site around it, and the running protocol, use the
continuous per-account model with a $20 minimum.

Four findings below — actionable independently, but **Findings 1 and 2 should be fixed
together**, because fixing 1 alone leaves a contradiction standing.

---

# Finding 1 — the hosted white paper is a pre-migration artifact

**Owner:** web / content
**Status:** verified, reproducible in ~2 minutes

## The problem in one line

The site's own copy describes a **continuous** distribution driven by account count. The PDF the
site links describes a **1,000-discrete-level** distribution. These are not the same mechanic, and
both are currently published under the digitalgold.co domain.

## Side by side

| | digitalgold.co page copy | `Digital_Gold_White_Paper_2026.pdf` (linked from the same site) |
|---|---|---|
| Distribution structure | **Continuous curve**, no levels | **1,000 discrete levels** |
| What advances it | Each confirmed account | The network reaching the next level |
| Release trigger | Per signup — "*Each signup triggers immediate distribution*" | Per level; no per-signup concept exists in the document |
| Minimum to participate | **$20** | **~$40** |
| Stats page label | "**continuous-N model**" | n/a |

## Evidence — the site

From `https://digitalgold.co` (captured 2026-07-19):

> "As new nodes/wallets add value to the network, new DGD releases are allocated equally across
> funded accounts. Your DGD is sent to your QT wallet **immediately when each new account joins**."

> "DGD's model uses confirmed network accounts as the input. **Each new account advances the
> curve**, updating price, circulating supply, and the next release amount."

> "Distribution continues through the published **continuous curve**…"

From `https://digitalgold.co/stats` — page metadata:

> "Explore the DGD **continuous-N model** with live network count, price, circulating supply,
> market cap, treasury, and per-user release estimates."

The Stats page also exposes a live **"Next Release"** figure that changes per account — a quantity
that only exists under the continuous model.

## Evidence — the linked PDF

From `Digital_Gold_White_Paper_2026.pdf`, §5.3:

> "Operating across **1,000 levels**, with three quantities increasing incrementally from level to
> level. Account growth proceeds at 1.136518147 percent per level, starting at 1,000 at Level 1
> and reaching 80,000,000 at Level 1,000."

§5.4:

> "At each level, three outcomes are possible. **Full validation.** If a member's account has
> enough funds to cover their full per-member share at that level's price…"

§5.7 / §12.14:

> "A participant can begin participating in DGD with as little as approximately **$40** pre-loaded
> into their DigitalGoldX account."

## Evidence — the continuous-model document exists

A copy of the white paper describing the continuous model has been in the AmbassadorAI repository
since **2026-06-23**. Its text, verbatim:

> "This is the fairness mechanism that prevents whale accumulation and ensures broad distribution.
> **There are no discrete levels.** Instead, the system is driven by a single quantity: N, the
> current total number of users. Each time a new user signs up, the protocol does two things
> instantly."

> "A participant can begin participating in DGD with as little as approximately **$20** pre-loaded
> into their DigitalGoldX account. The mechanics follow directly from the **continuous validation
> structure**."

That copy contains **zero** occurrences of the string "1,000 levels".

Identifying details, so the right file can be located:

```
Pages:        58
Bytes:        551,299
SHA-256:      31609cd02b7f91957c711ee32d47a921e9b647da173140c8790f2238cb34e440
CreationDate: 2026-06-16 01:07:38 MDT
Producer:     macOS Quartz PDFContext (created in Pages)
```

## Reproduction

1. Open `https://digitalgold.co` — note "continuous curve", "each new account advances the curve",
   and "each signup triggers immediate distribution".
2. Open `https://digitalgold.co/stats` — note the "continuous-N model" description and the live
   "Next Release" figure.
3. Download `https://digitalgold.co/Digital_Gold_White_Paper_2026.pdf`.
4. Search it for "1,000 levels" — present. Search for "no discrete levels" — absent.
5. Compare the stated minimum: **$20** on the site, **~$40** in the PDF.

## Provenance — confirmed

**The hosted PDF is a `digitalgoldx.com`-era asset that survived the domain migration.**

Confirmed by the DGD project: the 1,000-level structure and the $40 minimum are both consistent
with the specification as published on **digitalgoldx.com prior to the digitalgold.co launch**.
The old site is no longer online and `digitalgoldx.com` now redirects to `digitalgold.co`
(verified 2026-07-19 — the redirect resolves and serves .co content).

So this is a **migration artifact**: the white paper file was carried across to the new host and
never refreshed, while every surrounding page was rewritten for the continuous model.

## Independent confirmation that the continuous model is what's running

During a single working session on 2026-07-19, the live site advanced by **one account**:

| | First fetch | Second fetch |
|---|---|---|
| Accounts | 3,210 | **3,211** |
| Price | $9.84630 | **$9.84909** |
| Circulating supply | 7,413,838 DGD | 7,413,879 DGD |
| Next release | 40.989393 DGD | 40.980951 DGD |

**A single account joining moved the price and released ~41 DGD.** That is the continuous mechanic
executing. Under the 1,000-level model in the hosted PDF, price and supply advance *per level* —
one account out of the ~1,000 in a level bracket could not do this. The running system is
demonstrably the one described in the continuous-model document, not the hosted one.

## Suggested fix

1. **Replace the hosted PDF** with the continuous-model version — **but see Finding 2 first.**
   That swap alone does *not* fully resolve the mismatch: the continuous-model paper still
   contradicts the site on *who receives a release*.
2. **Audit for other assets carried over in the same migration.** The white paper reached the new
   host as a file copy rather than a redirect, so anything else migrated that way is a candidate
   for the same staleness — other PDFs, downloadable one-pagers, media kits, embedded diagrams,
   cached OG images. This file was only caught because someone read it closely.
3. **Add a version string and revision date to the document itself** — see Finding 4. Had the file
   carried `v2.0 (2026-03)` in its header, the migration gap would have been obvious at a glance.

---

# Finding 2 — the CURRENT white paper also contradicts the site, on who receives a release

**Owner:** whoever maintains the white paper text
**Status:** verified
**Severity:** High — this is the single fact a participant most needs to be right about.

**This is not fixed by swapping the hosted file.** The continuous-model paper — the one that
should replace it — still describes the *old* recipient rule.

| | Says who receives a release |
|---|---|
| digitalgold.co (live) | "allocated equally across **funded accounts**" · "accounts with an **active validation balance**" |
| Continuous-model white paper | "split equally among **all current users**" |

Verbatim from the continuous-model paper:

> "…the protocol advances the price along a fixed curve and releases a small number of coins from
> the treasury, **split equally among all current users**."

The paper explicitly treats funded-only distribution as a change that **has not been made**:

> "…under the assumption that **every user holds a balance and validates**. **If the design were
> later changed to exclude zero-balance users**, the only change would be the divisor: each release
> would be split among the count of eligible users instead of all users, with the unclaimed
> remainder…"

The site indicates that change **is now live**. The paper has not been revised to match.

## Why this matters more than the levels discrepancy

Under the paper's wording, an unfunded account still receives coins. Under the live model it
receives nothing. A reader relying on the white paper would also reasonably infer that unclaimed
shares inflate everyone else's — the paper's own §5.6 says the remainder is handled differently.
That is a materially wrong expectation about whether and when someone gets paid.

## Suggested fix

Revise §5.1 / §5.6 and the Abstract to state the shipped rule directly: releases are split across
accounts holding an active validation balance, and unclaimed shares return to the treasury rather
than being redistributed.

**If the site is the thing that's wrong here — i.e. distribution really does still go to all
users — that is more urgent than everything else in this report**, because ambassador material and
the AmbassadorAI wiki have already been updated to follow the site.

---

# Finding 3 — arithmetic error in the white paper

**Owner:** whoever maintains the white paper text
**Status:** verified; present in *both* versions
**Severity:** Medium — but it is a maths error in a document whose central argument is that
readers should verify the maths.

The paper states:

> "The Federal Reserve has expanded the United States money supply from approximately **$3 billion**
> in 1913 to more than **$21 trillion**, an increase of roughly **7,000 percent**."

$3 billion → $21 trillion is a **7,000-fold** increase, i.e. approximately **700,000%**.

"7,000 percent" would describe $3 billion → **$213 billion** — off by two orders of magnitude.

The underlying figures ($3B, $21T) appear correct; only the percentage conversion is wrong. The
cleanest fix is to state the ratio rather than a percentage:

> "…an increase of roughly **7,000-fold**."

**Why this matters more than a typo normally would:** the sentence is quoted in ambassador-facing
scripts and gets spoken on camera. Any viewer with a calculator can falsify it in seconds, in a
video arguing that DGD's design is transparent and checkable.

*(The AmbassadorAI wiki has already been corrected to say "7,000-fold" and carries a note
explaining the divergence from the source document.)*

---

# Finding 4 — root cause: the documents are not distinguishable

**Owner:** web / document
**Severity:** Low individually, but this is why Finding 1 was difficult to diagnose.

The two versions share:

- the same filename stem (`Digital_Gold_White_Paper…`)
- the same page count (58)
- the same terminal date in the body text (17 March 2026)

and **neither carries a version number, revision date, or changelog**.

There is currently no way to tell two revisions apart except by reading their distribution
mechanics and noticing they differ. Any future revision will have the same problem.

**Suggested fix:** add to the document header or footer —

```
Version 2.1 · Revised 2026-06-16 · Supersedes v2.0 (2026-03)
```

and a one-page revision history. This makes the whole class of problem self-diagnosing, and lets
anyone confirm in one glance whether they're holding the current specification.

---

## Contact / follow-up

Happy to supply the continuous-model PDF, the full extracted text of either version, or the exact
byte offsets of any quotation above.

The AmbassadorAI wiki has been updated to follow the **site's live behaviour** (continuous model,
releases to funded accounts) rather than the linked PDF, and records this discrepancy in
`Knowledge Base/SOURCES.md`. If Finding 1 resolves the other way — i.e. the 1,000-level model is
authoritative — please say so, because the wiki and every ambassador script derived from it will
need reverting.
