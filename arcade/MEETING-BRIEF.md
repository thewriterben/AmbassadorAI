# DGD Arcade — publishing meeting brief

For the publishing team, 2026-09-18. Written to be read in five minutes.

**Updated 2026-09-17:** the legal entity, the D-U-N-S, the Apple Developer
Program and the Google Play developer account are all confirmed in place. That
removes every long-lead blocker this brief originally led with, and changes what
the meeting is for: not *starting* things, but handing over and signing off.

---

**What this is.** An Android and iOS app for the ambassador programme. One game
is finished — *Coin Quest: Digital Gold*, a 60-level match-3 — and ten more are
designed and about to be built. A Node backend holds XP, badges, streaks and a
weekly leaderboard. It is educational, free, has no advertising, no in-app
purchases, and no connection to any wallet, exchange or trading function.

**Where it stands.** Android is built, tested and installable today. Nothing is
on any store, because nothing has been uploaded yet — not because anything is
broken.

**What I want out of the meeting.** A decision on how builds get signed and
uploaded, five blanks filled, three sign-offs, and two owners named. All of it
is below.

**Nobody has to give me store console access.** §1.1 sets out three ways to do
this and two of them involve handing me nothing at all. What cannot be avoided
is that *something* has to hold the signing keys — that is how app stores work —
so the decision is where they live, not whether they exist.

---

## 1. What I need from you

### 1.1 Signing and upload — pick one of three models

**Assume I get no access to the store consoles.** That is a reasonable position
and it is workable. But an app cannot reach a store unsigned, so *something*
has to hold the signing keys, and the only real question is what. Three models,
all legitimate. **I need a decision on which, not the access itself.**

#### Model A — DGD uploads, I hand over artifacts
I build, you sign and upload. Nobody gives anyone console access.

- **Android:** I produce an **unsigned** `.aab`. You sign it with DGD's upload
  key using `jarsigner` — a one-line command I will write out — and upload it.
  The key never leaves your side.
- **iOS:** harder. An iPhone build must be signed at build time with a
  distribution certificate from the DGD team, so I cannot hand you an unsigned
  artifact you can simply sign afterwards. Either someone at DGD with a Mac and
  Xcode does the build, or this model does not cover iOS.

**Cost:** a person at DGD in the loop for every release. Fine at this cadence,
tedious later.

#### Model B — CI holds the keys *(my recommendation)*
The build runs in DGD's own CI. The Android upload key and the Apple
certificates live in that CI's secret store. No individual holds a credential,
and nobody needs console access — including me.

This also solves the Mac problem: a hosted macOS runner pins a known-good Xcode
instead of depending on whichever laptop updated last night. That is §1.4, and
last night made the case for it — an OS update cost an evening.

**Cost:** a few hours of setup and a CI account. It is the only model that
scales past a handful of releases.

#### Model C — narrow credentials, not console access
Worth knowing these exist, because "access" usually gets heard as "admin".

- **Play:** an **upload key** is not the app signing key. With Play App Signing
  enabled, Google holds the real key and can reset a compromised upload key.
  Handing over an upload key is a much smaller thing than it sounds.
- **Apple:** an **App Store Connect API key** scoped to *Developer* can upload
  builds and nothing else — it cannot change the listing, see financials, or
  manage users.

**Cost:** two narrow credentials exist outside DGD's direct control.

---

**What is true under every model:** there is no way to put an iPhone build in a
colleague's hands without the DGD Apple Developer account being involved
somewhere. Apple has no sideloading — no iOS equivalent of emailing an APK.
Distribution runs through TestFlight:

| | Who | Apple review | Speed |
|---|---|---|---|
| **Internal** | Up to 100 people, each an App Store Connect user on DGD's team (Admin, App Manager, Developer or Marketing) | None | Minutes after processing |
| **External** | Up to 10,000 by email or link | First build needs Beta App Review | Days first time, quicker after |

**Separate ask, and it costs nothing:** add the people who should receive the
iPhone demo as App Store Connect users with the **Developer** or **Marketing**
role. That is about *them*, not me, and it puts them on the internal track with
no Apple review at all.

### 1.2 The five blanks in the privacy policy
A draft written from what the code actually does is in `PRIVACY-DRAFT.md` — I
read the database schema and the client rather than adapting a template. It is
publishable as soon as someone supplies:

| | |
|---|---|
| Legal entity name | as it should appear in the policy and on both listings |
| Contact address | for privacy requests — needs to be a real monitored inbox |
| Minimum age | drives the target-audience questionnaire on both stores, and whether Families policy applies |
| Hosting URL | a stable public address, ideally on digitalgold.co |
| Retention period | or a decision that records persist until deleted |

Neither store will open a release track without a live policy URL, so this is
the practical critical path now.

### 1.3 Signing — one decision
Whoever holds the Android upload keystore can ship updates to the listing, and
**if it is lost the listing can never be updated again by anyone.** I have
deliberately not created it — it is a DGD credential, not a developer's.

- Does DGD already have an upload keystore for other apps, or is one being made?
- Who holds it and where is the backup?
- Enrolling in Play App Signing at first upload gives a recovery path if the
  upload key is ever lost. Worth accepting unless there is a reason not to.

For iOS, distribution certificates live in App Store Connect and 1.1 covers it.

### 1.4 Is there a CI or hosted build account?
iOS builds need a Mac running a current macOS — Apple has required Xcode 26 or
newer for App Store Connect uploads since 28 April 2026, and that floor rises
with every macOS release. A hosted macOS build service (Codemagic, Bitrise,
GitHub Actions macOS runners) removes that dependency permanently and builds
from the repo instead.

**Need:** whether DGD already has a CI account or budget, or whether keeping a
Mac current is the plan. It is a procurement question with a lead time, which
is why it belongs in this meeting rather than after it.

### 1.5 Backend — where does it live
The server runs only on my build PC, so no tester's phone can reach it. It needs
any host that runs a Node process with a persistent disk, over HTTPS.

Also: the signing secret is still the development default, which is published in
the repo and therefore forgeable by anyone who reads it. A real value needs
setting in the host environment — **not** in a file in the repo.

**Need:** where it is hosted and who owns that environment.

---

## 2. Sign-offs — someone who owns risk, not me

I have flagged all of these and am not qualified to close any of them.

### 2.1 The financial-products question — the big one
DGD is a gold-backed digital asset, and both stores have distinct policy areas
for financial products and crypto. This app has no trading, wallet or purchase
in it, which *should* keep it clear — but the questionnaire wording decides it,
and a wrong answer is a rejected or pulled listing.

### 2.2 The signup call-to-action — most likely to cause a problem
The app links out to a digitalgold.co signup. An app that awards points, linking
to a gold-backed asset product, is exactly what a reviewer looks at twice.
**This needs legal review before release.** It is a two-line change if the
answer is no, and far cheaper to hear tomorrow than after a rejection.

### 2.3 Content rating — simulated gambling
The rating questionnaire asks about it. Coin Quest is a match-3 with no
wagering, and the coin-shower and jackpot visuals the arcade plan bars in §4.3
were removed partly for this reason. Still needs a human answer.

### 2.4 The ten new games — trademark
The next ten are takes on well-known arcade mechanics. Mechanics are not
protected; names, characters and specific audiovisual presentation are. Every
game will carry a DGD-native name and our own art, and the falling-block one is
being deliberately redesigned because it is the one genre where a
differently-named, independently-written clone has lost in court.

**Need:** counsel to see the name list before the games ship. Cheap now,
expensive after ten games are named and drawn.

### 2.5 Question bank exemptions
The educational bank carries 47 items marked *unreviewed — awaiting sign-off*.
Not in the current build, but they will be when the bank comes back.

---

## 3. What I am providing

Everything here is written and ready to hand over. See `STORE-LISTING.md` for
the full text.

| | Status |
|---|---|
| App name, short and full description | Drafted, both stores |
| iOS subtitle, keywords, promotional text | Drafted |
| App icon, 512×512, no transparency | Done |
| Play feature graphic, 1024×500 | Done |
| Phone screenshots | Captured from a real device |
| Data safety answers (Play) | Drafted from the schema |
| Privacy nutrition labels (Apple) | Drafted from the schema |
| Content rating answers | Drafted — needs 2.3 signed off |
| Privacy policy text | Drafted — needs the five blanks |
| Android app bundle | On request, once signing is settled |

**Notable for the forms, and true:** there are no accounts. No name, email,
phone or date of birth is ever collected. Leaderboard names are assigned from a
word list and cannot be typed, so the board cannot carry a real name. There is
no advertising identifier, no analytics SDK, no crash-reporting SDK, and no
third-party tracker of any kind. The only Android permission is `INTERNET`.

**Users can delete their data.** Built 2026-09-17: a control in Settings erases
the anonymous server record — XP, badges, streak, play history — in one
transaction, and a second, separate control clears local progress. Both stores
ask this question and the answer is now yes rather than no.

---

## 3b. iOS — it builds and runs, verified 2026-09-17

The app was built and launched on an iPhone simulator on a Mac tonight. That
matters because until this evening iOS was a claim; now it is a thing that has
been seen working.

| | |
|---|---|
| Builds for iOS | **Yes**, Flutter 3.47.2 + Xcode 27 on macOS 27 |
| Runs | **Yes**, on the iPhone 16 Pro simulator |
| Bundle ID | `co.digitalgold.arcade`, matching Android |
| Deployment target | iOS 15, so iPhone 6s and later |
| App icon | DGD coin, all 15 sizes, opaque as Apple requires |
| Screenshots | Taken from the simulator |

**Not yet done, and not doable without you:** running on a physical iPhone, and
getting it onto anyone else's. Both need the DGD Apple Developer account —
§1.1. The honest summary for the room is: *the iOS build is finished and
proven; it reaches testers the day I get App Store Connect access.*

Two caveats I would not want anyone to over-read. A simulator says nothing
about **audio**, which is the one part of this app most likely to behave
differently on iOS — different audio session, and the silent switch does not
exist on a simulator. And frame rate on a simulator is meaningless. Both need a
real handset.

## 4. What is genuinely ready

- Coin Quest: 60 levels across six worlds, difficulty tuned by simulation.
- Android demo APK, installable today, with a tester note in `TESTERS.md`.
- Backend: server-authoritative scoring, single-use signed tokens, anti-farming
  checks, 18 passing tests.
- A ten-minute audio soak on a real device: 6000 effects, zero failures,
  latency flat across the run.
- App identity settled and permanent: `co.digitalgold.arcade` on both platforms,
  with DGD icons.
- Compliance vocabulary throughout: XP and badges, never "earn" or "cash", and
  an in-app footer stating they have no monetary value.

## 5. After the meeting

| Unblocked by | Same-day result |
|---|---|
| A signing model chosen (1.1) | Android build handed over ready to upload |
| Policy URL + blanks (1.2) | Declarations submitted |
| Signing decision (1.3) | Build uploaded to Play internal testing |
| Backend host (1.4) | XP, badges and the leaderboard live for testers |
| Sign-offs (2.1–2.3) | Release track can actually go live |
