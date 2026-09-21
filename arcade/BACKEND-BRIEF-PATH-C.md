# Backend brief — Path C, and what we need from you

**2026-09-21. For Oleksandr and backend engineering.**
Supersedes `FOR-BACKEND-2026-09-21.md`, which remains in the repo for history.

Everything credential-, key- and endpoint-related for this project lives in
this document. The team-facing update carries none of it; please keep that
split when forwarding.

---

## Why you are getting this

DGD has confirmed that **referrals are compensated in DGD, or in something
convertible to it.**

That makes App Store Guideline 3.1.5(v) bite. Verbatim:

> *"Cryptocurrency apps may not offer currency for completing tasks, such as
> downloading other apps, **encouraging other users to download**, posting to
> social networks, etc."*

There are five ways out (`B1-DECISION-2026-09-21.md` has all of them). Four are
decisions for DGD and counsel. **One of them — Path C — is a backend question,
and it is the only one that keeps the invite feature in the app.** Hence this
brief.

**Path C:** keep the feature, keep the website programme, but do not pay
referral credit on `?ref=` codes that came from the app. The claim to Apple
then becomes "the app's invite tools earn nobody anything", which is a much
stronger position than "the payout happens elsewhere".

---

## What we found looking at it from the app side

The app emits exactly **two** referral URLs. They are not equally tractable,
and the difference decides whether Path C is cheap or impossible.

| Feature | URL the app produces | Distinguishable from a website referral? |
|---|---|---|
| **Display QR** | `https://digitalgold.co/app?ref=USERNAME` | **Probably yes** — by path |
| **Copy Invite Link** | `https://digitalgold.co/signup?ref=USERNAME` | **No. Byte-identical** to a site-originated referral |

Source: `DigitalGoldSite.inviteLinkURL` / `appInviteURL` in the Android tree,
with the same strings mirrored on iOS.

### The good half

`/app?ref=` exists as the app-download handoff page. If **only** the app ever
produces that path, you can exclude it from credit today, with no app change
and no ambiguity.

**Question 1 below is whether that "only" holds** — if the website also links
to `/app?ref=`, the path stops being a reliable channel marker.

### The hard half

`/signup?ref=USERNAME` carries **no channel information whatsoever**. It is the
same URL the website's own share would generate. Nothing in it, or in the
request that follows it, says "a phone produced this". So today, Path C cannot
be applied to Copy Invite Link at all.

### The part that may kill Path C outright

The obvious fix is for the app to add a marker — `&src=app` or similar — and
for you to skip credit when you see it.

**That marker is trivially removable.** Copy Invite Link puts the URL on the
clipboard; the user pastes it wherever they like. Deleting five characters
before sending turns an uncredited referral into a credited one. So the
mechanism would be:

- unenforceable in the only direction that matters, and
- **a claim we would be making to Apple that a motivated user can falsify in
  two seconds.**

That is worse than not making the claim. If Path C only works via a strippable
marker, our recommendation is that Path C is not viable and the decision goes
back to removing the feature (Path A) or changing the compensation (Path B).

Path C survives only if the distinction can be made **server-side, from
something the user cannot edit.** Which is question 2.

---

## What we need from you

Five questions. Four are yes/no. None require any change to the app first.

**1. Does anything other than the app link to `/app?ref=`?**
The website, an email template, a campaign, a partner. If nothing does, the
path is a clean channel marker for the QR.

**2. Is there any server-side signal that already distinguishes an
app-originated referral from a website one?**
Anything the user does not control and cannot edit: a distinct landing path, a
User-Agent pattern on the first hit, an app-only endpoint in the signup flow,
a session or attribution record, an install referrer. If something like this
exists, Path C is viable and cheap. If it does not, say so plainly — a "no"
here is as useful as a "yes", and faster.

**3. Can referral credit be suppressed for a subset of referrals without
disturbing the rest of the programme?**
Mechanically: is crediting a rule you can scope, or is it baked into signup?
This matters even if the answer to 2 is no, because Paths A and B may still
need a way to stop crediting a cohort.

**4. What is the actual shape of the crediting path?**
Automatic on signup, manual, or batched later? Per-referrer or per-referral?
Reversible? We have been describing it to reviewers in general terms and would
rather describe it accurately.

**5. Is any of it retroactive?**
If referrals made before today can still be credited later, then removing the
feature now does not fully clear the position, and counsel should know that.

---

## The current build

`DigitalGold-1.0.5-review.apk` is in this folder — the same artefact the rest
of the team has.

- Android, 61.5 MB, version **1.0.5-review**.
- Release configuration: R8 and resource shrinking on.
- **Signed with the ordinary Android debug key.** Play refuses it. It exists so
  the release build can be installed and inspected; the version name says so
  from inside the app.
- The arcade in it is a **`DGD_EMBED=demo`** build: no backend, zero network
  calls from the game. Coin Quest only, no XP bar, no leaderboard.

To see the thing this brief is about: **Get Digital Gold → through to Receive →
Invite Friends.** That screen is the compliance surface. Copy Invite Link and
Display QR are the two URLs in the table above.

---

## Reference — unchanged from the previous brief

### Credentials and ownership

Nothing secret is in the repository or on the build machine, by standing
policy.

| Item | Where it lives | Owner |
|---|---|---|
| Play **upload keystore** + password | DGD's password manager. Not created or held by the build side. | DGD |
| Apple Distribution certificate | Apple Developer account | DGD |
| `ARCADE_SECRET` | **Not yet set to a real value** | backend |
| Admin Swagger credential | DGD's to rotate; untouched by this work | DGD |

**`ARCADE_SECRET` must be a real value before the arcade service is exposed.**
It signs the single-use question tokens; with a default or empty value the
server's authority over XP is decorative.

### What the app talks to

One public endpoint, read-only:

```
GET https://digitalgold.co/api/forms/stats
```

Supplies `count`. Price and market cap are derived on device from the published
continuous CFV model — they are not response fields. Polled on appear and on
foreground return; `recommendedPollInterval` is 45s to match the site. No
`Origin` header. No analytics, no crash reporter, no ad SDK.

### The endpoint the app does not use yet

`/analytics` serves real daily history. **The app shows no chart at all** — a
generated preview series was removed from both platforms on 2026-09-21, because
invented performance figures for a financial asset are a problem no footnote
fixes. When a chart returns it comes from `/analytics` and nothing else.

**The chart is waiting on you, not on the client.**

### The arcade service

Built and tested, not hosted. Node 24, Hono, `node:sqlite`. Server-authoritative
XP, tablets and daily ledger; signed single-use question tokens; plausibility
checks and per-period caps; `xp_events` ledger behind the weekly leaderboard.

`build_aar.cmd` refuses to build unless one of these is set — an earlier build
with neither fell back to `http://localhost:8787` and trusted whatever answered
(audit RC1):

```
set ARCADE_API=https://...     a configured build
set DGD_EMBED=demo             no backend, zero requests
```

Give us a host URL and the XP bar, leaderboard and tablets light up with no
client changes.

### What hosting the backend does *not* retire

- **S1**, the keystore. A hosted backend does not sign an App Bundle.
- **B1**, this document's subject.
- **B2b**, the iOS arcade embed. Deferred by decision.
- The App Store ID placeholder, and app-link verification, which waits on S1.

---

*Related: `B1-DECISION-2026-09-21.md` (all five options),
`STORE-READINESS-2026-09-20.md` §B1, `RELEASE.md`, `PRIVACY-DRAFT.md`,
`apple/DATA_SOURCE.md`.*
