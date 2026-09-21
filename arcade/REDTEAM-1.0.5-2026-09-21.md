# Red-team sweep — v1.0.5 review build

**2026-09-21.** Static sweep of the built artefact, run in an isolated Linux
container with no access to the build machine's toolchain, before the build
goes to backend engineering.

**Artefact under test**

```
DigitalGold-1.0.5-review.apk
sha256  c44ded289a7369d7c4eed6806011417de2f3cedb200d702f2cd52c6329629c41
size    61,514,019 bytes      635 entries
package com.digitalgold.ticker    1.0.5-review (5)
minSdk  26    targetSdk 36
```

The hash was computed independently in the container and matches the one taken
on the build machine, so this report describes the same bytes the team and
backend receive.

**No network calls were made.** The red-team policy for this project forbids
traffic to `digitalgold.co`, and a sweep that probed a host to check it would
break the rule it exists to enforce. Everything below was read out of the
artefact.

---

## Verdict

**Nothing blocking. Two findings worth acting on, both low severity, neither a
credential or a live vulnerability.**

| | Finding | Severity |
|---|---|---|
| **F1** | Dev-only screens are compiled into the shipped binary, and a source comment claims they cannot be | **Low** (unreachable) / **Medium** as a documentation defect |
| **F2** | `assets/stats-source.json` ships ~8 KB of internal API reconnaissance notes that the app never reads | **Low** (information disclosure) |

Everything else checked clean or was confirmed correct-by-design.

---

## F1 — dev surfaces ship, and the comment says they don't

`lib/dev.dart` states:

> *"in a build without `--dart-define=DGD_DEV=true` every `if (Dev.enabled)`
> below folds to `if (false)` and the compiler drops the branch. **The
> shortcuts are not hidden in a store build, they are absent from it.**"*

The artefact does not have that property. Present in `libapp.so`:

```
dev_soak.dart      1      DevSoakScreen   3
DevMenu            1      "Audio soak test"
```

**Why.** The gate is inside the widget, not at the call site:

```dart
// dev.dart
Widget build(BuildContext context) {
  if (!Dev.enabled) return const SizedBox.shrink();   // runtime check
```

and callers construct it unconditionally:

```dart
// level_map.dart:92
child: DevMenu(
  title: 'COIN QUEST',
  actions: { ... () => Navigator.push(..., const DevSoakScreen()) },
),
```

So `DevMenu` is instantiated on every build, its `actions` map is built, and
the closures inside it reference `DevSoakScreen`. The tree shaker cannot drop
what is still referenced. The comment's convenience — *"can be dropped into a
layout unconditionally without a caller-side check"* — is exactly what defeats
its own tree-shaking claim.

**Is it reachable?** No. `DGD_DEV` does not appear in the snapshot at all,
which means `Dev.enabled` const-folded to `false` at compile time; the gate
cannot be flipped at runtime, and there is no other route to `DevSoakScreen`.
This is dead code that ships, not a live backdoor.

**Why it still matters.** Someone reading that comment would reasonably
conclude that dev code cannot reach a store build, and would stop checking.
The same codebase contains the pattern done correctly — `Audio.inAppTab`
guards genuinely const-fold, which is why `voWinner` and `fireworkShow` are
absent from this binary (verified below). Two patterns, one claim, and the
claim only holds for one of them.

**Fix**, if wanted: move the condition to the call sites, where Dart's
collection-`if` folds on a `const` condition —

```dart
actions: [ if (Dev.enabled) DevMenu(...) ]
```

— or correct the comment to say the shortcuts are *inert* in a store build
rather than absent. Either is fine; the current pairing is not.

---

## F2 — shipped API reconnaissance notes

`assets/stats-source.json`, 9,069 bytes, **is read at runtime** — confirmed by
dex cross-reference (`Lc2/c;-><init>(Landroid/app/Application;)V`) and by
`TickerAndroidViewModel.kt:38`.

But `StatsEndpoint.kt:37` says what it actually consumes:

> *"Reads the investigation `stats-source.json` (endpoint + accounts path
> only)."*

Two fields. The other ~90% of the file is investigation provenance that ships
to every user and is never parsed:

- **Five endpoints**, not one — `/api/forms/stats`, `/api/forms/count`,
  `/api/forms/stats-next`, `/api/forms/stats-history` (annotated
  *"404 Cannot GET"*), `/api/analytics?page=1&limit=40`.
- **`"Foreign Origin values cause HTTP 500"`** — a documented way to make
  DGD's endpoint error, shipped inside the product.
- Commentary: *"stats_history_in_js_but_missing"*, *"More fragile than JSON"*.
- `digitalgoldx.com` as a 301 alias of `digitalgold.co`.

None of this is a credential and none of it is secret in the strict sense —
the endpoints are public. But it is a map of DGD's API surface, including
which parts are broken and how to error one, packaged for anyone who unzips
the APK.

**Fix:** ship a minimal file containing only `endpoint`, the accounts `path`
and `alt_path`. Keep the full investigation in `apple/DATA_SOURCE.md`, which
lives in the repository and not in the product.

**Also worth confirming with DGD:** that they own `digitalgoldx.com`. The file
says it 301s to `digitalgold.co`, which is consistent with an owned alias, but
a lookalike domain named inside the app is worth being certain about rather
than inferring.

---

## What checked clean

**Secrets — nothing.** Eleven credential patterns across all 635 entries: AWS,
Google API, Slack, Stripe, GitHub, JWT, PEM/RSA private keys, `Bearer`
literals, `password=`, `secret=`. No matches. No `.pem`, `.jks`, `.keystore`,
`.env`, `.db`, `.sql` or `.log` files packaged.

**Trackers — none.** Firebase Analytics, GA, Crashlytics, AdMob, Facebook,
AppsFlyer, Adjust, Branch, Mixpanel, Amplitude, Sentry, Bugsnag, OneSignal,
Segment: all absent. The privacy policy's claim that the app carries no
analytics holds in the binary.

**Manifest posture.**

| | |
|---|---|
| `debuggable` | not set (correct for release) |
| `usesCleartextTraffic` | `false` |
| `allowBackup` | `true` — **and the rules are correct**, see below |
| permissions | `INTERNET`, `VIBRATE`, and Flutter's own receiver permission. Nothing sensitive. |

**Backup rules — verified, not assumed.** R8 renamed them to `res/4j.xml` and
`res/Qq.xml`, so a filename search finds nothing; decoded, both exclude
`dgd.signup.xml`, `dgd.signup.secure.xml` and `FlutterSharedPreferences.xml`
from cloud backup *and* device transfer. The credential prefs stay out of
backups, which is audit item W1 holding.

**Exported components — two, both justified.** `MainActivity` (launcher and
app-link target, must be reachable) and `androidx.profileinstaller.ProfileInstallReceiver`
(guarded by `android.permission.DUMP`). Three components not exported.

**§4.3 suppression — intact in the shipped binary.**

```
voWinner       0 occurrences      fireworkShow   0 occurrences
voPraise       present            voEncourage    present
```

**RC1 — clean.** No `localhost:8787` or `10.0.2.2` loopback arcade endpoint.

**RC4 — clean.** All three declared ABIs (`arm64-v8a`, `armeabi-v7a`,
`x86_64`) carry both `libflutter.so` and `libapp.so`. No ABI is declared
without an engine behind it.

**Question bank — does not ship.** No question or answer asset is packaged,
so the server-authoritative design holds: a player cannot extract answers from
the APK.

**Compliance vocabulary — clean after triage.** Two patterns matched and both
are false positives, confirmed by inspection rather than dismissed:

- `\bbet\b` → the byte sequence `bEt` inside compiled code, matched
  case-insensitively. Not copy.
- `\$\d+` → 1,733 hits in the dex, all R8 synthetic names (`$1`, `$5F`, `$0K`)
  and Kotlin inner-class suffixes. No money copy. `earn`, `cash`, `dollars`,
  `jackpot`, `casino`, `payout`, `winnings`, `prize`, `wager` all clean.

**Signing — debug key, as intended.** `CN=Android Debug`, v2 scheme, serial 1.
Play will refuse it. This is the review build, and the `-review` version
suffix says so from inside the app.

**Hosts — 30 distinct, all accounted for.** `digitalgold.co` (12 URLs) plus
library, licence and certificate-revocation hosts: `crl.thawte.com`,
`ocsp.verisign.com`, `scripts.sil.org` and `paratype.com` (font licences),
`dartbug.com`, `pub.dev`, `llvm.googlesource.com`, `youtrack.jetbrains.com`,
`issuetracker.google.com` (toolchain comments), `publicsuffix.org`,
`ns.adobe.com` (XMP in images). One parsing artefact,
`www.paratype.comhttp`, from two concatenated URLs in a licence blob. Nothing
unexplained.

---

## Method, and what this sweep does not cover

Run in a container that does not share the build machine's toolchain, against
a copy of the artefact, with androguard 4.1.4 for manifest and dex analysis
and hand-written scanners for the rest. The script is
`arcade/tools/redteam_sweep.py`.

**Static only.** This sweep does not cover:

- **Runtime behaviour.** Nothing was executed. A dynamic pass — traffic
  capture on a device, checking what the app actually sends — is a different
  exercise and would need the red-team policy's no-`digitalgold.co` rule
  resolved first, since the app's only endpoint is on that host.
- **The arcade service.** Not hosted yet, so there is nothing to test. When it
  is, it wants its own pass: `ARCADE_SECRET` strength, token replay, the
  plausibility caps, and whether the XP ledger can be forced.
- **iOS.** Different artefact, and B2b is deferred.
- **Third-party library CVEs.** No SBOM or dependency-vulnerability scan was
  run here.

---

*Related: `STORE-READINESS-2026-09-20.md`, `REDTEAM-POLICY.md`,
`AUDIT-v1.0.3-2026-09-21.md` (W1, backup exclusions),
`AUDIT-RC-2026-09-20.md` (RC1, RC4).*
