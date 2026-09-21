# Store readiness — the backend developer's review, reconciled, 2026-09-20

> **Source.** "DGD App Store Readiness", 2026-09-20, by the backend developer
> (Oleksandr), five pages, filed beside this note as
> `DGD-App-Store-Readiness-2026-09-20.pdf`. It reviewed
> `DGD-merged-arcade-v1.0.2-demo-debug.apk` at sha256 `72837584…`, which is
> **two revisions behind** the current build (`d6812bf2…`, see
> `AUDIT-v1.0.2-2026-09-20.md`). This note maps every item in it to what is
> already done, what is new, and who owns what remains. Items that need code
> are tracked as **S-findings** below with the same conventions as the audits.
>
> **Verdict.** The review is right, and its ordering is right: one security
> action outranks the store work, one product decision gates all of it, and
> the engineering that follows is packaging and honesty, not a rebuild. Two of
> its six mechanical items were already fixed before it arrived. It found one
> thing the audits had not: the stats panel plots an invented series.

---

## 0. Before anything else — the admin credential (theirs, not ours)

The review states that the admin Swagger login shared with the reviewer
controls coin prices, wallets and payouts, and that the Swagger UI at
`/api/doki/` on the production backend is publicly reachable. Their
instruction — rotate the credential and every key exposed with it, and
restrict or remove public access to that endpoint — is the highest-priority
item in the review and in this note.

This is `digitalgold.co` infrastructure. **Nothing here touched it**: the
red-team policy forbids traffic to that host, and no probe was made. What was
checked, defensively and offline: no such credential, host path or admin
token appears anywhere in the AmbassadorAI repo, the native tree
(`C:\src\dgd-native`) or the arcade source (`C:\src\puzzle-app`). Nothing
found. **Owner: DGD. Not tracked here beyond this paragraph.**

## 1. The decision gate — Path A, B or C

The reviewer's three paths are the same fork `NATIVE-SOURCE-REVIEW.md`
raised from the Finance-category angle, now with harder evidence: the backend
exposes stablecoin payment verification, a purchase queue, paid tiers and
wallet RPCs, so both stores will judge the whole ecosystem, not the screens
the app happens to show.

| Path | What ships | Reviewer's view | What it means for this codebase |
|---|---|---|---|
| **A** — free branded game, severed from the coin | arcade only; no price, market cap, buy button, signup, wallet or invite | recommended; near-zero policy risk | the embed already has this shape on the arcade side (demo build, zero requests). The ticker half would be removed or reduced to branding |
| **B** — informational companion | price and stats, login; never buy, sell, send or receive in-app | defensible; may still be classed as crypto | the preview must become live signup, the stats must be real data, and the "Get Digital Gold" destination must be store-compliant |
| **C** — full crypto app | wallet, purchases, tiers | organisation account, per-country licensing, securities review, IAP on iOS; months of legal work | out of scope for any engineering plan here |

**Owner: DGD. Nothing below the mechanical line can be scheduled until this
is chosen.** Every content item in §3 changes meaning with the path.

## 2. Mechanical items — what the review found vs. the current build

| Review item | State of the reviewed build | State now | Tracked as |
|---|---|---|---|
| Version 1.0.0 (1) under a v1.0.2 filename | true | **fixed** — `1.0.2 (2)` (RC3) | — |
| 32-bit x86 declared, engine missing | true | **fixed** — three ABIs, no x86 slice (RC4) | — |
| Debug build, `debuggable=true` | true | still true, by design for a test build | S1 |
| Debug signing key | true | still true; `RELEASE.md` leaves the upload keystore for DGD to create | S1 |
| targetSdk 35; Play requires 36 since 2026-08-31 | true | still 35 — compileSdk was raised to 36 for the embed and target kept at 35 deliberately | **S2** |
| APK rather than App Bundle | true | `RELEASE.md` already builds an `.aab`; the reviewed file was the sideload APK | S1 |
| Placeholder App Store link `id0000000000` | true | still true, on both platforms, with a unit test pinning it | **S3** |
| Two package identities (`com.digitalgold.ticker`, `co.digitalgold.arcade.module`) | true | not a conflict: the second is the Flutter module's own package inside the AAR; the app's identity is the first | — |

## 3. Content items

| Review item | Assessment | Tracked as |
|---|---|---|
| PREVIEW · NOT LIVE watermarks read as unfinished (Apple 4.2, 2.1) | Correct. The framing exists because their App Store notes position signup as an educational preview; the reviewer is right that Apple cuts against that. Under Path A the preview goes; under B it becomes live signup. V1 made the copy honest; it did not, and could not, make the preview a feature | S4 (gated on §1) |
| Illustrative financial figures shown as performance | **Correct, and new to us.** `PreviewStatsSeries` in the native app plots a synthetic growth and price path ending on the live ticker, with a footnote line "Illustrative trend — live historical data is coming soon." The reviewer notes `/analytics/time-report` and `/analytics` already serve real history. A fabricated performance curve for a financial asset is a consumer-protection risk on any path that keeps the stats panel | **S5** |
| Student gating, `.edu` required, age rating | Correct as a store question; not code | DGD |
| "The app creates accounts, so it needs in-app deletion" | **Partly.** The merged app's signup is a local preview and creates nothing on their backend; the arcade has an in-app delete for its own identity (`DELETE /v1/me`). Under Path A there is no account to delete. Under B or C the point stands and the missing backend endpoint becomes real | DGD / backend, gated on §1 |
| Privacy policy URL, Data Safety, Privacy Labels | Correct. `RELEASE.md` already says the policy needs a hosted URL; `PRIVACY-DRAFT.md` describes the arcade alone and carries a drafting note about the merged app's on-device fields (V2) | DGD, with `PRIVACY-DRAFT.md` as the draft |

## 4. Tracked engineering items

Same conventions as the audits: a stable ID, a severity for store readiness,
an owner, and a status that this file is updated to when it changes.

### S1. BLOCKER — release build, upload keystore, App Bundle
`debuggable=false` with shrinking on, a production upload keystore enrolled
in Play App Signing, an Apple Distribution certificate and profile, and an
`.aab` upload. The keystore is a credential and is deliberately not created
by anyone but DGD (`RELEASE.md` §"release signing"). The build scripts
already produce an `.aab`. **Owner: DGD for the keystore; then one release
build here. Status: open, waiting on DGD.**

### S2. BLOCKER — targetSdk 35 → 36 — DONE 2026-09-20
Native commit `5958514`: `targetSdk = 36`, and the version moved to
`1.0.3 (3)` with it (S6). The arcade's standalone build already targeted
36 through Flutter's default. Retested on a **wiped Android 16 (API 36,
Google APIs) emulator** with `localhost:8787` routed to the impostor backend
(`redteam-runs/20260921T003000Z-s2-api36-fd23e0c3/`): cold start, arcade, Coin Quest into a board, four predictive-back
presses returning to the ticker, the hostile deep link, and the login sheet
with the keyboard up — insets correct under Android 16's enforced
edge-to-edge, zero requests, nothing at rest in plaintext, no crash. Every
native library was already 16 KB page-aligned (`PT_LOAD` 0x4000 or 0x10000;
`zipalign -P 16` clean), which Android 16 devices require. Two things to
know: (1) the portrait lock on both activities is ignored on large screens
once the app targets 36, so tablets and unfolded foldables will show the
ticker and arcade in whatever orientation the device is in — not tested, and
a product call rather than a defect; (2) the Android 16 emulator survives
only with `-gpu host`; the software renderer segfaults seconds after boot.
Rebuilt APK: `integration/DGD-merged-arcade-v1.0.3-demo-debug.apk`, sha256
`fd23e0c3…`, gitignored. **Status: done.**

### S3. HIGH — placeholder App Store link
`https://apps.apple.com/app/id0000000000` in `DigitalGoldSite.kt`,
`invite-handoff/DigitalGoldSite.kt` and `DigitalGoldTickerApp.swift`, pinned
by `DigitalGoldSiteTest`. The invite and share flow points at a dead link
until the real App Store ID exists, which needs the iOS app registered in
App Store Connect first. **Owner: DGD for the ID; then one edit and one test
here. Status: open, waiting on the ID.**

### S4. HIGH — the preview framing (gated on the path decision)
Under A: remove the ticker's signup, wallet and invite screens, or the ticker
half entirely. Under B: make signup live against the existing
`/forms/*` endpoints, which then pulls in account deletion, password reset
and the privacy items. Either way the PREVIEW · NOT LIVE header and the
"coming soon" line leave. **Owner: DGD decides, then here. Status: open,
gated.**

### S5. HIGH — the synthetic stats series
`PreviewStatsSeries` must plot real history from `/analytics` or the stats
panel must lose its chart and change tiles. Independent of the path decision
on any path that keeps the panel, and the fix is straightforward because the
data exists. **Owner: here. Status: open.**

### S6. LOW — version bump on the next shipped change — DONE with S2
`1.0.3 (3)` as of native commit `5958514`. The next shipped change
is `1.0.4 (4)`; Play never accepts a reused code. **Status: done.**

### S7. LOW — app links are unverified, so the deep link opens the browser
`MainActivity` declares `autoVerify` app links for `digitalgold.co/app`, but
on the Android 16 emulator `pm get-app-links` reports `legacy_failure` for
both hosts and the `https://digitalgold.co/app/…` intent opened Chrome
instead of the app. That is correct Android 12+ behaviour for an unverified
link: the app needs `https://digitalgold.co/.well-known/assetlinks.json`
listing its **release** signing certificate's SHA-256, which does not exist
until S1 produces that certificate. The debug certificate seen on the
emulator would never verify anyway. Found during the S2 retest; not a
regression from the target bump. **Owner: DGD hosts the file after S1; then
one verification here. Status: open, gated on S1.**

## 5. What the review does not change

Everything the red-team line established still stands: RC1–RC4 closed, V1
and V2 closed on Android, the server ledger with nothing open, the native
tree under git. The review adds no security finding on the app itself — it
calls it "technically clean" — and the one it adds on the backend is §0.

## 6. Order of work

1. §0, today, by DGD.
2. §1, by DGD, before any of the below is scheduled.
3. ~~S2 and S6~~ done. S5 can start now regardless of the path.
4. S1 and S3 wait on DGD artefacts (keystore, App Store ID); S7 waits on S1.
5. S4 follows the decision.

*Related: `RELEASE.md` (the release procedure and the keystore stance),
`MERGE.md`, `NATIVE-SOURCE-REVIEW.md` (the category question),
`PRIVACY-DRAFT.md`, `AUDIT-v1.0.2-2026-09-20.md`.*
