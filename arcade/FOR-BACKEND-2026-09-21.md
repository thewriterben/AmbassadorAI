# Backend engineering — DGD app, state at v1.0.5

**2026-09-21. Audience: backend engineering (Oleksandr and whoever picks up the
arcade service).**

This document holds the credential, key and endpoint material. It is the only
one of the two 21 Sep handovers that does — `TEAM-UPDATE-2026-09-21.md` is
written for the rest of the company and carries none of it, deliberately.
Please keep it that way when forwarding.

---

## 0. Credentials — status and ownership

Nothing secret is in this repository, and nothing secret is on the build
machine. That is a standing constraint, not an accident, and it should survive
this handover.

| Item | Where it lives | Owner |
|---|---|---|
| Play **upload keystore** + password | DGD's password manager. **Not created here, not held here.** | DGD |
| Apple Distribution certificate | Apple Developer account | DGD |
| `ARCADE_SECRET` (arcade service) | Not set to a real value yet | backend |
| Admin Swagger credential | DGD's to rotate; nothing in this work touches that host | DGD |

Three things follow:

1. **The release build is unsigned by default and stays that way.** There is no
   signing config in `build.gradle.kts` pointing at a real key. A store build
   is a step DGD runs with DGD's keystore; `RELEASE.md` has the procedure.
2. **`-PdgdReviewSigning` signs with the ordinary Android debug key** so a
   release-configuration APK can be installed for internal review. Play refuses
   it, and the build stamps its own version name `1.0.5-review` so it announces
   what it is from inside the app. It is not a route to the store and cannot
   become one.
3. **`ARCADE_SECRET` must be set to a real value before the arcade service is
   exposed to anything.** It is the signing secret for single-use question
   tokens; with a default or empty value the server's authority over XP is
   decorative.

An independent secret scan of the native tree found nothing; `SECRETS_FINDINGS.md`
in `dgd-native` has the method and the result.

---

## 1. What the app currently talks to

Exactly one public endpoint, and it is read-only.

```
GET https://digitalgold.co/api/forms/stats
```

- Supplies `count`. Price and market cap are **derived on device** from the
  published continuous CFV model — they are not fields in the response.
  `apple/DATA_SOURCE.md` has the constants and the exact arithmetic, verified
  against the site's own numbers.
- Polled on appear and on return to foreground. `recommendedPollInterval` is
  45s to match the site; do not go below it.
- **No `Origin` header.** This was checked rather than assumed —
  `OKHTTP_ORIGIN_DIAGNOSTIC.md` records the check.

There is no other network traffic from the shipped app. No analytics, no crash
reporter, no ad SDK.

### The endpoint the app does not yet use

`/analytics` serves real daily history (`playersCount`, `currentPrice` 2dp,
`currentMarketCap`, `date`). **The app deliberately shows no chart at all
right now.** A generated preview series used to fill that space on both
platforms and was removed on 2026-09-21, because invented performance figures
for a financial asset are a consumer-protection problem however they are
footnoted. When a chart returns it must be plotted from `/analytics` and from
nothing else.

That is the single most important line in this document for backend: **the
chart is waiting on you, not on the client.**

---

## 2. The arcade service

Built and tested, not hosted. That is the open item.

- Node 24, Hono, `node:sqlite`.
- **Server-authoritative** XP, tablets and daily ledger. The client cannot
  assert progress; it submits and the server decides.
- Questions are issued as **signed, single-use** tokens — this is what
  `ARCADE_SECRET` signs.
- Plausibility checks and per-period caps on XP award paths.
- `xp_events` ledger behind the weekly leaderboard, with assigned handles
  rather than user-chosen ones.

### How the client is configured

`build_aar.cmd` **refuses to build** unless one of these is set. That refusal
is deliberate: an earlier build with neither fell back to
`http://localhost:8787` and trusted whatever answered, which is audit finding
RC1.

```
set ARCADE_API=https://...     a configured build
set DGD_EMBED=demo             no backend at all: Coin Quest only, zero requests
```

**The v1.0.5 build in front of the team is `DGD_EMBED=demo`.** It makes no
network calls from the arcade whatsoever. When you have a host, rebuild with
`ARCADE_API` pointing at it and the XP bar, leaderboard and tablets light up
with no client changes.

### Before exposing it

- Set `ARCADE_SECRET` to a real value.
- Decide the host and give us the URL for `ARCADE_API`.
- `PRIVACY-DRAFT.md` covers what the service stores; the Play Data Safety form
  and Apple Privacy Labels both depend on that being accurate.

---

## 3. What wiring the backend does and does not retire

Worth being precise, because it has been assumed both ways.

**Retires:**

- The arcade's demo mode, and with it the missing XP bar and leaderboard.
- The "no backend" caveat in the store listing copy.

**Does not retire — these are independent of any endpoint:**

- **S1**, the keystore. A hosted backend does not sign an App Bundle.
- **B1**, the primary category and the 3.1.5(v) defence. See §4; it is a
  policy question, and no endpoint changes the answer.
- **B2b**, the iOS arcade embed. Deferred by decision, not blocked by backend.
- The App Store ID placeholder, and app-link verification, which is gated on
  S1.

---

## 4. One question for you to weigh in on

3.1.5(v) names *"encouraging other users to download"* — which describes a
referral programme. The arcade's XP is defensible: it is explicitly
non-monetary, says so on screen, and the vocabulary is policed (XP and badges,
never "earn" or "cash").

The sharper edge is the ticker's `?ref=USERNAME` invite system, and it turns on
a question only DGD can answer:

> **Does anyone receive DGD, or anything convertible to it, for a referral —
> on the site, off-app, manually, or later?**

If **no**, the defence is clean and the reviewer notes should say so
explicitly. If **yes**, that needs separating from the app before submission,
and it is a larger change than anything else outstanding.

Backend will know whether any such crediting path exists in the site's data
model, which is why it is in this document rather than only in the commercial
one.

---

## 5. Client-side things worth knowing

Recent work that touches your surface area:

- **A first-run blocker was fixed** (`bab02c8`). No new user could complete the
  signup preview: forward progress was gated by a ceiling only forward progress
  could raise, and the refusal was silent. Invisible unless you wipe the
  install, which is why it survived several rounds of testing.
- **An API 33 crash was fixed** (v1.0.5). `URLDecoder`/`URLEncoder`'s
  `Charset` overloads are API 33; `minSdk` is 26. Every invite link and QR
  code, and every inbound `?ref=` deep link, threw `NoSuchMethodError` on
  Android 8 through 12. Found by running lint for the first time in the
  release-candidate pass.

  Verified three ways, because the Pixel is API 36 and would never have hit
  this — "it works on my phone" proves nothing here, and the bug shipped in the
  first place precisely because nobody ran those versions:

  1. An **Android 11 (API 30) emulator** was stood up specifically for it. The
     `?ref=` deep link resolves with no `NoSuchMethodError` and the app runs.
  2. The **shipped APK's dex** references exactly
     `URLDecoder.decode(String, String)` and
     `URLEncoder.encode(String, String)` — the API 1 overloads — and no
     `Charset` variant anywhere. That is artefact-level proof, not source-level.
  3. Lint is clean and is now a permanent step in the RC pass.
- **R8 is now on** for release builds, with keep rules for Flutter, Tink,
  ZXing and OkHttp — all four resolve by reflection and fail at runtime rather
  than at build time if shrunk away.

---

*Related: `RELEASE.md`, `PRIVACY-DRAFT.md`, `STORE-READINESS-2026-09-20.md`,
`apple/DATA_SOURCE.md`, `dgd-native/SECRETS_FINDINGS.md`,
`dgd-native/OKHTTP_ORIGIN_DIAGNOSTIC.md`, `integration/build_aar.cmd`.*
