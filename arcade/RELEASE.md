# DGD Arcade — demo and release

> **This document is about v1** — Coin Quest only, the version going to the
> stores and into the main DGD app. Build it from `arcade/v1/`. The ten-game
> catalogue is v2 and is not a store candidate yet. See `VERSIONS.md`.

Status as of 2026-09-16. This covers getting the app to internal testers and,
from there, to a public listing. It is a runbook, not a plan document: every
step is either done, or blocked on something named.

## Identity — settled, and now permanent

| | |
|---|---|
| Application ID | `co.digitalgold.arcade` |
| iOS bundle ID | `co.digitalgold.arcade` |
| App name | DGD Arcade |
| Version | from `pubspec.yaml` (`version: 0.1.0+1` → versionName 0.1.0, versionCode 1) |

The ID was `com.puzzlepack.puzzle_pack`, left over from the original scaffold.
It was changed **before** the first upload on purpose: an application ID cannot
be changed once anything is published to a Play listing, and it is visible in
the store URL, in Android's app settings and to anyone who inspects the APK.

The Dart package is still `puzzle_pack` (it appears in `import
'package:puzzle_pack/…'`). That is internal, invisible to users, and renaming it
touches every file in `lib/`, so it was left alone. Say if you want it changed.

**The rename means the app installs as a new app.** It does not replace the one
already on your phone — Android treats a different application ID as a different
program. Uninstall "DGD Arcade" before installing the new build, or you will
have two icons and the old one will keep its own saved progress.

## Signing — needs you, once

Release builds read `android/key.properties`, which is git-ignored. Without it
the build falls back to the debug key and prints:

    DGD: release signing = DEBUG KEY (not uploadable to Play)

With it:

    DGD: release signing = upload keystore

I have deliberately not created this keystore. It is a credential: whoever holds
it can ship updates to the listing, and **if it is lost, the listing can never be
updated again** — not by you, not by anyone. It belongs to DGD, in DGD's password
manager, and I should not be generating or holding its password.

Create it yourself:

```
keytool -genkey -v -keystore C:\path\you\choose\dgd-upload.jks ^
  -keyalg RSA -keysize 2048 -validity 10000 -alias dgd-upload
```

Then create `C:\src\puzzle-app\android\key.properties`:

```
storePassword=…
keyPassword=…
keyAlias=dgd-upload
storeFile=C:/path/you/choose/dgd-upload.jks
```

Back up the `.jks` file and both passwords somewhere that survives this laptop.
Enrolling in Play App Signing at upload time gives you a recovery path if the
upload key is lost later, and is worth accepting when offered.

## Backend — blocked on a host

XP, badges, the streak and the weekly leaderboard are server-authoritative by
design — the client never submits a score. The server currently runs only on
the build PC at `localhost:8787`, which **no tester's phone can reach**.

Its tablet, ledger and mini-game endpoints have had no client since the nine
games were removed on 2026-09-16 (`REMOVED-GAMES.md`). They were left in place
deliberately: tested, hardened, and the natural landing point for whichever of
the new ten games need server-verified scoring.

Before the demo goes out:

1. **Deploy `arcade/v1/server`.** Node 24, Hono, `node:sqlite`, no build step.
   Any host that runs a Node process with a persistent disk works; SQLite is
   the pilot store and the schema is plain SQL, so Postgres is a driver swap
   if it outgrows that.
2. **Set a real `ARCADE_SECRET`.** It is still on the development default. It
   signs the single-use tablet tokens; on the default, those signatures are
   forgeable by anyone who reads this repo. Generate a long random value and
   set it in the host's environment, not in a file in the repo.
3. **Serve it over HTTPS.** Android blocks cleartext HTTP by default, so a
   plain `http://` backend will fail on device with no useful error.
4. **Point the build at it:** `set ARCADE_API=https://…` before `demobuild.cmd`.

Until that exists I can only build testers a Coin-Quest-only demo, or one that
shows the offline banner and has no Tablet Run questions at all.

## Builds

| Script | Output | Log | DEV menu | For |
|---|---|---|---|---|
| `devbuild.cmd` | `.apk` | `rel.log` | **yes** | you and me |
| `sideloadbuild.cmd` | `.apk` | `sideload.log` | no | sideloaded Coin-Quest-only demo |
| `demobuild.cmd` | `.aab` | `demo.log` | no | testers, via Play |
| `relbuild.cmd` | `.apk` | `rel.log` | no | quick local release check |
| `check.cmd` | — | `check.log` | — | analyzer + tests, no build |

`sideloadbuild.cmd` and `demobuild.cmd` used to share `demo.log`, and both
truncate on start, so whichever ran second destroyed the other's output. They
have separate logs now.

Flutter writes every release APK to the same `app-release.apk`, so the DEV build
and the demo were silently overwriting each other — the file on disk was always
whichever ran last, with nothing to say which it was. Both scripts now copy
their output to `arcade/v1/dist/` under its own name:

| | |
|---|---|
| `arcade/v1/dist/DGD-Arcade-DEV.apk` | DEV menu in, for you and me |
| `arcade/v1/dist/DGD-Arcade-demo.apk` | Coin Quest only, hand this to testers |

`arcade/v1/dist/` is git-ignored — these are 55 MB each and rebuilt constantly.
`TESTERS.md` is the note to send alongside the demo.

`demobuild.cmd` refuses to run without `ARCADE_API` set, because a demo silently
pointed at localhost is worse than no demo.

The DEV menu is gated on `--dart-define=DGD_DEV=true`, read as a `const`, so in
the tester build those branches fold to `if (false)` and the compiler drops
them. They are absent from the artifact, not hidden in it.

## Play internal testing

1. Create the Play developer account (one-off fee) — **needs you**, it is tied
   to a DGD identity and payment method.
2. Create the app: name "DGD Arcade", package `co.digitalgold.arcade`.
3. Complete the declarations Play requires before any track can go live:
   content rating questionnaire, target audience, data safety, privacy policy
   URL, ads declaration. **The privacy policy needs a real hosted URL.**
4. Internal testing → create a release → upload the `.aab` → add testers by
   email (up to 100). They opt in via a link and install through Play.

The store icon is generated at `C:\src\play-icon-512.png` (512×512, no
transparency, as Play requires).

### Worth checking before you fill in the questionnaires

I have **not** verified these against current Play policy and you should not
treat them as settled:

- DGD is a gold-backed digital asset, and Play has a distinct policy area for
  financial products and crypto. Even though the arcade is educational and has
  no trading, wallet or purchase in it, the questionnaire may route it there.
- The app awards XP and badges with no monetary value and no purchase. That
  should keep it clear of both real-money gaming and the in-app-purchase rules,
  and the in-app footer already states it, but the declaration wording matters.
- Content rating will ask about simulated gambling. Coin Quest is a match-3
  with no wagering; the coin-shower and jackpot visuals the arcade plan bars in
  §4.3 were removed partly for this reason.

Get someone at DGD who owns compliance to review the answers before submitting.

## Still open

- ~~Long-session audio soak test~~ — **done, 2026-09-16.** Ten minutes,
  6000 effects attempted, 6000 played, 0 failed, 0 dropped by the limiter.
  p50 2 ms, p95 16 ms, max 48 ms. Drift 1.02× (first decile 4.5 ms, last
  4.6 ms), against a 1.3× threshold. The original "effects consistently lag
  then stop" report is closed on evidence, not inference: latency is flat
  across the run and the per-file player pool holds.
- iOS: **builds and runs, verified on a simulator 2026-09-17.** Flutter 3.47.2
  with Xcode 27 on macOS 27. Bundle ID, deployment target and the DGD app icon
  are all in place. What is left needs the DGD Apple Developer account: running
  on a physical handset, and TestFlight for anyone else. Audio on iOS is
  untested and is the part most likely to differ — a simulator has no silent
  switch and its own sound stack. See `MAC-SETUP.md`.
- Question bank is at 170 of the 300-item Phase 1 target.
- `ALLOWLIST.md` in the question bank carries 47 exemptions still marked
  **unreviewed — awaiting sign-off**.
