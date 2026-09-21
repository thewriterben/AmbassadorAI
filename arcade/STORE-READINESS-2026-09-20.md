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
> **Added 2026-09-21:** §5 answers what is left if **Path B** is chosen, once
> the backend and API elements are attached. Items specific to that path are
> tracked as **B-findings**, same conventions; they are numbered separately
> because they evaporate or change shape under A.
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

### S5. HIGH — the synthetic stats series — DONE 2026-09-20 (Android)
Native commit `27e4b2a`: the Stats panel now shows the live snapshot and
nothing else — Accounts, Price, Market cap, and a line stating the source and
the time of the fetch. The generated series (`PreviewStatsSeries`, with its
timeframes, section pills, sparkline, percent captions and the "Illustrative
trend — live historical data is coming soon" footnote) is deleted along with
its tests and the growth-sentence formatter; the chart-motion constants went
with it. 92 unit tests pass (was 106; the fourteen removed all tested the
generator). The rebuilt APK (sha256 `0f8dd848…`, 80,821,760 bytes) contains no
"Illustrative trend" string. Verified on the Android 16 emulator with the
network on: the panel opens from the Stats button with the three live figures
and the source line, no chart, no crash. The smaller option was chosen over
plotting `/analytics` history: that is a feature with product decisions in it
(which timeframes, two-decimal history against a five-decimal ticker), and
the panel's doc comment says where real history goes when it comes.
**iOS is not done:** `HomeStatsPanel.swift` still draws the same generated
chart; a Swift change for someone with a Mac. **Status: done on Android.**

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

## 5. If Path B is chosen — what remains after the backend

*Added 2026-09-21, in answer to a direct question: with proper backend and API
elements attached, what is left?*

**First, an ambiguity in §1 that has to be closed before any of this can be
scheduled.** The Path B row says "price and stats, login" and is **silent on
whether the arcade stays in the binary**. Path A says "arcade only"; B says
nothing either way. Everything in B1 below is heavy if the arcade stays and
largely evaporates if it goes. Nobody has written the answer down.

### What the backend actually retires

| Item | Becomes |
|---|---|
| S4, signup half | live signup against the existing `/forms/*` |
| S5, "real data" half | already live-only on Android; real *history* from `/analytics/time-report` is a further feature, not a fix |
| In-app account deletion (§3) | a real endpoint, once accounts are real |
| Password reset | same |
| `ARCADE_API` | the arcade stops showing OFFLINE — and its bearer token then needs Keystore-backed storage, the open half of W1 in `AUDIT-v1.0.3-2026-09-21.md` |

That is roughly **one and a half of the seven S-findings**. The rest does not
move, and four of the five items below cannot be moved by engineering at all.

### B1. BLOCKER — the primary category, and who signs the 3.1.5(v) defence
Not currently tracked as an S-finding; the analysis is in
`NATIVE-SOURCE-REVIEW.md` §"the merged app has a category problem".

**Path B is the configuration that maximises this exposure.** A game
catalogue awarding XP, ranking players on a weekly leaderboard, with a
referral system encoding `?ref=USERNAME`, inside a **Finance**-category app
showing a live USD price for a cryptocurrency. One app gets one primary
category: Finance keeps their positioning and puts a game catalogue where
reviewers do not expect one; Games inverts it and puts a live crypto price
inside a game. Both are answerable. Neither is obvious.

Their existing review notes state the app "does not award currency in-app".
That sentence has to survive the arcade being in the same binary. It does —
XP is not currency, has no monetary value and cannot be exchanged — but
**somebody at DGD has to be confident enough to sign their name under it.**
No endpoint changes this. **Owner: DGD. Status: open, unscheduled.**

### B2. BLOCKER — iOS is a build-out, not a port
Path B ships both platforms. Android is far ahead:

- **The arcade is not embedded on iOS at all.** Not started; needs a Mac and
  the `.xcframework` route specced in `integration/INTEGRATION.md`.
- **S5's iOS half is open.** `HomeStatsPanel.swift` still draws the generated
  growth-and-price chart — the fabricated performance curve for a financial
  asset, which is the one genuine consumer-protection finding in the review,
  still shipping on iOS.
- `SpinningCoinView.swift` has never been compiled (`COIN-AND-ICON.md`).

**Owner: here, with a Mac. Status: open, blocked on hardware.**

### B3. HIGH — the "Get Digital Gold" destination
Named in §1's Path B row and nowhere else. Under B the buy path leaves the
app, which runs into Apple's anti-steering treatment of outbound purchase
links. A copy-and-policy decision, not an API. **Owner: DGD. Status: open.**

### B4. ~~HIGH~~ **BLOCKER — the signup preview could not be completed at all** — DONE 2026-09-21

Rated HIGH on the assumption these were three cosmetic annoyances. They were
one deterministic defect, and it was a blocker: **no new user could get past
the email verification step.**

On a fresh install, Verify — or the keyboard's Go key — returned the user to
Credentials, discarded the typed code, and left Wallet and Receive locked.
`handlePrimary` cleared the verification state and then called `moveToStep(2)`,
which consults `isSignupStepUnlocked`: a fresh install has
`signupMaxReached = 1`, so the question for step 2 is `2 <= 1` and the answer
is no. Forward progress was gated by a ceiling only forward progress could
raise, and because `moveToStep` returns `Unit` the refusal was silent.

`moveToStep` was doing two incompatible jobs. Now it does one — it guards the
step pills — and a new `advanceToStep` handles forward progress by raising the
ceiling. `handlePrimary` advances before clearing, so a future refusal does
nothing instead of destroying state. `DigitalGoldSiteTest` pins the invariant.

Also fixed: the primary button sat below the keyboard with no scroll-into-view,
so the step showed a code field and no visible way to submit — which is why
the 21 Sept automation logged Verify as "not reached" rather than as broken.

**Why it survived every check.** Every previous manual walk was on a device
that had already completed the preview once, which sets
`membershipPreviewCompleted` and opens the gate permanently. The defect is
invisible unless the install is wiped. O1 and O2 were two sightings of it,
both written off as flaky IME behaviour.

Verified on a wiped Pixel against the staged artefact: Credentials → Verify →
**Wallet** → **Receive**, no crashes. Shipped as **1.0.4 (4)**,
`DGD-merged-arcade-v1.0.4-demo-debug.apk`, sha256 `e803e800…`, with
`integration/FOR-OLEKSANDR-v1.0.4.md` for the reviewer. **Status: done.**

The general lesson is in B5: the app has no instrumented tests, so a blocker
on its main flow had nothing to catch it.

### B1 status — 2026-09-21
Decided: **arcade stays in the binary, Finance stays as the primary
category.** Draft reviewer-notes text and the reasoning are in
`integration/B1-B3-CATEGORY-AND-PURCHASE.md`.

That work surfaced something this section had missed. 3.1.5(v) names
*"encouraging other users to download"* — a referral programme, described
exactly. The arcade's XP is defensible; the **`?ref=USERNAME` invite system on
the ticker side** is the sharper edge, and it turns on a question only DGD can
answer: *does anyone receive DGD, or anything convertible to it, for a
referral — on the site, off-app, manually, or later?* If no, the defence is
clean and should say so explicitly. If yes, that needs separating from the app
before submission, and it is a bigger change than anything else in track B.
**Owner: DGD. Status: open, and it should be answered early.**

### B2 status — 2026-09-21
`integration/IOS-B2-RUNBOOK.md`, plus the Swift itself. `HomeStatsPanel.swift`
is rewritten to the live-figures-only panel that Android already ships
(commit `27e4b2a`), 565 lines down to 86. **None of it is compiled** — no Mac
here — and the runbook says so in its first paragraph. It splits the work:
B2a (delete the synthetic chart, the compliance item, no Flutter needed) and
B2b (the arcade embed via `.xcframework`, half a day with a Flutter install).
The arcade's iOS entry point is deliberately **not** written: the Android
engine lifecycle took three attempts, and a plausible-looking uncompiled
Swift file would be worse than the shape plus a reference implementation.
**Status: handed over.**

### B3 status — 2026-09-21 — largely dissolved
Checked against the current guidelines rather than recalled. Following the
Epic injunction, Apple's May 2025 update means that **on the US storefront**
3.1.1 imposes no prohibition on external links or calls to action and needs no
entitlement, and 3.1.3's anti-steering prohibition does not apply. A "Get
Digital Gold" button opening the website is now the low-risk option rather
than the risky one. Three caveats survive: it is storefront-specific, it rests
on an injunction Apple is appealing, and it says nothing about what the user
finds at the other end. **Status: resolved for the US; note the caveats.**

### B5. LOW — engineering hygiene that a release will expose — MOSTLY DONE 2026-09-21
- ~~The first minified build has never been run.~~ **Done.** `isMinifyEnabled`
  and `isShrinkResources` are on, with keep rules for everything that resolves
  by reflection and so fails at runtime rather than at build time: the Flutter
  engine and plugins, Tink behind `EncryptedSharedPreferences`, ZXing, OkHttp's
  platform probes. Release APK **74,098,986 → 61,501,727 bytes**. Verified on
  the device, because a successful R8 build proves nothing here — ticker
  renders, arcade opens and draws, no `ClassNotFoundException`,
  `NoSuchMethodError` or `UnsatisfiedLinkError` in logcat.
- ~~No instrumented or Compose UI tests exist.~~ **Done.**
  `SignupPreviewFirstRunTest` walks the preview as a brand-new user through to
  Finish, using a fresh-preferences fake so it cannot drift into the state
  where B4 hid. **Proven to fail:** reverting `advanceToStep` to `moveToStep`
  fails two of the three on the Wallet assertion.
  Two pins were needed and neither is optional on a current device —
  `ui-test-junit4` drags in espresso-core 3.5.0, whose
  `InputManagerEventInjectionStrategy` reflects on
  `InputManager.getInstance()`, a method that no longer exists. Every test died
  before reaching an assertion. **espresso-core 3.7.0 fixes it; 3.6.1 does
  not.**
- ~~Gradle 8.11.1 must reach 8.14.4.~~ **Done**, and the Kotlin deprecation
  warning is gone. A separate forward-looking note about Gradle 9 remains.
- ~~`DGD_APP_TAB` celebration suppression is unverified.~~ **Closed by an A/B
  build diff, 21 Sep.** The doubt was never whether the Dart guard reads
  correctly — it was whether `--dart-define` survives `flutter build aar` at
  all, since a dropped define fails silently and leaves `bool.fromEnvironment`
  at its `false` default. That is answerable without playing a level: build the
  AAR twice from identical source, changing only the define, and compare the
  AOT snapshot.

  Result — all three ABIs differ, and the flagged build is *smaller*
  (armeabi-v7a −16,384 bytes, x86_64 −65,536; arm64 unchanged in size but
  differing in content, as its sections are page-aligned). Code was removed,
  not merely rearranged.

  Byte difference alone could in principle be compiler non-determinism, so the
  snapshots were also probed for the symbols only the suppressed paths define:

  | probe in `arm64-v8a/libapp.so` | flagless | flagged |
  |---|---|---|
  | `voWinner` | 1 | **0** |
  | `fireworkShow` | 1 | **0** |
  | `grand` (the firework show's parameter) | 1 | **0** |
  | `assets/audio/` (control) | 1 | 1 |
  | `Digital Gold` (control) | 3 | 3 |

  Both suppressed methods are gone from the flagged snapshot while the controls
  are untouched. A one-directional disappearance of exactly the guarded code is
  not something a non-deterministic compiler produces. **The define reaches the
  Dart compiler and the tree shaker removes the celebration paths.**

  One honest caveat: the two VO filename literals (`vo_level_complete.wav`,
  `vo_you_win.wav`) still appear in the flagged snapshot. They are `const` list
  entries that survive in the constant pool even though the only method that
  read them was eliminated — dead data, not reachable code.

  `arcade-repo` was left holding the flagged AAR, verified by hash
  (`64ea9d16e2c5b85a6f…`, 12,145,742 bytes) against the build that produced it.
  The flagless build was produced first and never published, so at no point did
  the app's local repo hold an arcade with fireworks in it. **Status: done.**

  One correction, recorded rather than quietly overwritten. The two A/B builds
  were made by driving `flutter build aar` directly, so that the *only*
  difference between them was the define. That skipped two things
  `build_aar.cmd` does: the `sync_module.py` step, and the mandatory
  `ARCADE_API` / `DGD_EMBED` choice from audit RC1. Fine for the experiment —
  both sides skipped them equally — but it meant `arcade-repo` briefly held an
  arcade with no backend explicitly chosen. It was rebuilt the same day through
  `build_aar.cmd` with `DGD_EMBED=demo`, which is the correct configuration
  while the backend is unhosted, and that build (12,143,286 bytes, 21 Sep
  12:01) is what the app now links. The hash above therefore identifies the
  experiment's artefact, not what ships.
- ~~**Large screens:** at targetSdk 36 the portrait lock is ignored (S2).
  Untested; a product call.~~ **Tested and fixed, 21 Sep.**

  The rule, from Google's own wording: for apps targeting API 36,
  `screenOrientation`, `resizableActivity`, `minAspectRatio`, `maxAspectRatio`
  and `setRequestedOrientation()` are all ignored on any display whose
  smallest width is at least 600dp. A manifest property,
  `android.window.PROPERTY_COMPAT_ALLOW_RESTRICTED_RESIZABILITY`, opts out and
  restores the old letterboxing — **but Google removes that escape hatch at API
  37**, at which point the restrictions are ignored unconditionally.

  Rather than reason about it, this was run: a Pixel Tablet AVD on the
  installed android-36 image, 2560×1600 at density 2.0, so 1280×800dp and a
  smallest width of 800dp — squarely inside the rule. `dumpsys window
  displays` confirmed the app receives `app=2560x1600`. The lock is ignored, as
  documented.

  What that actually did to the app, screen by screen (`arcade/tab36-shots/`):

  | screen | landscape at 800dp | verdict |
  |---|---|---|
  | Ticker home | coin, price and footer centred; **Stats and Get Digital Gold stretched the full 1280dp**, Accounts and Market Cap flung to opposite edges | needed fixing |
  | Signup sheet | already capped and centred — Material 3's `ModalBottomSheet` limits itself to 640dp | fine, free |
  | Arcade home | **Coin Quest card a metre wide**, icon at one end and arrow at the other | needed fixing |
  | Level map | scrolling path, sparse but correct | fine |
  | Match-3 board | square, centred, all 7 rows visible — it sizes from the shorter edge | fine |

  So: a polish problem, not breakage. Nothing was unreachable or clipped.
  **That is why no opt-out property was added.** It would buy cosmetics for one
  API level and then have to be taken out again at 37, and the app does not
  need it.

  The fix is a width cap at each content root, and nothing else:

  - `TickerScreen.kt` — the ticker column is wrapped in
    `widthIn(max = 480.dp)`, centred. The corner buttons and the hairline frame
    stay outside it: those belong to the window, not the column.
  - `main.dart` (arcade home) — the same idea, `BoxConstraints(maxWidth: 520)`
    around the home `ListView`.

  480dp is close to a phone's width on purpose. A tablet then gets **the
  layout that was designed**, centred, rather than a second layout nobody has
  reviewed — which matters when this whole tree is about to go to a designer.
  On the Pixel (393dp wide) the cap never binds, so the phone is byte-for-byte
  the same screen as before; verified by re-installing and comparing.

  The portrait lock stays in the manifest. It is still honoured below 600dp,
  which is every phone, and that is where it was earning its keep anyway.

  Re-verified after the change on both the tablet AVD and the Pixel, and the
  three B4 signup instrumented tests were re-run **on the tablet**, because the
  B4 fix scrolls the primary button into view and a window twice as wide is
  exactly where that could have behaved differently. **Status: done.**

  Still open for a designer, not for the store: a tablet shows a phone-width
  column in a lot of black. A two-pane or larger-type treatment is a design
  decision, not a compliance one.

### Already covered elsewhere, not repeated here
Privacy policy URL, Play Data Safety and Apple Privacy Labels are §3. The
keystore, Apple Distribution certificate, App Store ID and `assetlinks.json`
are S1, S3 and S7 — all of them artefacts only DGD can mint, none of them
backend work. The age rating / IARC questionnaire changes under B because one
binary then holds a game *and* crypto content; that sits with §3's store
questions.

## 6. What the review does not change

Everything the red-team line established still stands: RC1–RC4 closed, V1
and V2 closed on Android, the server ledger with nothing open, the native
tree under git. The review adds no security finding on the app itself — it
calls it "technically clean" — and the one it adds on the backend is §0.

## 7. Order of work

1. §0, today, by DGD.
2. §1, by DGD, before any of the below is scheduled. **If the answer is B,
   answer §5's opening question in the same breath: does the arcade stay in
   the binary?**
3. ~~S2, S5 and S6~~ done on Android; the iOS halves of S5 (and V2) need a Mac.
4. S1 and S3 wait on DGD artefacts (keystore, App Store ID); S7 waits on S1.
5. S4 follows the decision.
6. Under Path B specifically: B1 and B3 are DGD's and gate nothing technical
   but everything commercial; B2 is the long pole in engineering terms and is
   blocked on a Mac; B4 wants a human with the app in hand for ten minutes.

*Related: `RELEASE.md` (the release procedure and the keystore stance),
`MERGE.md`, `NATIVE-SOURCE-REVIEW.md` (the category question),
`PRIVACY-DRAFT.md`, `AUDIT-v1.0.2-2026-09-20.md`,
`AUDIT-v1.0.3-2026-09-21.md` (O1/O2 and W1),
`integration/INTEGRATION.md` (the iOS route),
`integration/KOTLIN-2.4-REGRESSION.md` (the test-coverage gap).*
