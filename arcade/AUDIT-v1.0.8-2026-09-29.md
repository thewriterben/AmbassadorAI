# DGD app 1.0.8 release candidate — full red-team pass, clean room in a separate container, 2026-09-29

> **Scope and authorisation.** The Android 1.0.8 release candidate, dgd-native
> tag `android-1.0.8-rc1` at `0520865` (`05208654b8e8…`), embedding the arcade
> from puzzle-app v1 `99a5c36` built with Flutter 3.47.2. Artefacts, from
> `C:\src\dgd-native\android\dist-1.0.8\`:
>
> | File | sha256 | Bytes |
> |---|---|---|
> | `DigitalGold-1.0.8-unsigned.aab` (goes to Play) | `43E1F5FD36ABEAA05E492FB19B2F4BDF06E6816829A5EDE8D09AF10893D14B67` | 57,189,687 |
> | `DigitalGold-1.0.8-review.apk` (debug-signed, `1.0.8-review`, versionCode 8) | `7C2567C26A23F84C628A0CD891EF24DA76A41C7228488B922E2D02CDD8B6C6A8` | 64,127,072 |
>
> Policy: `REDTEAM-POLICY.md`. Builds were reproduced in **Docker
> containers**, not on the host. Sources went in as git bundles via
> `docker cp`, with no bind mounts. The network was cut before each evidence
> build. Dynamic work ran on **two wiped emulators**, Android 16 (API 36,
> the target) and Android 8.0 (API 26, the minSdk). Nothing ran on the Pixel.
> No fixes were applied.
>
> **One exception to §2, deliberate.** The online phase let the app's own
> stats fetch reach `digitalgold.co` so the egress could be recorded. Nothing
> else in this pass contacted DGD services.
>
> **Verdict in one line.** The native half reproduces from the tag in a
> sealed offline container: the Dalvik code, every library and every asset
> are byte-identical, and the six remaining entries have benign
> explanations. The dynamic runs are clean on Android 16 and 8.0. **The
> embedded arcade binary does not reproduce byte for byte off Windows.** Its
> program content traces to `99a5c36`, but its bytes depend on the host OS
> and build path. **That trips the policy's ship gate (P1, MEDIUM)** until
> the AAR is built in the pinned container, or the gate is formally waived.

---

## Method: the clean room

| Container | Image | Contents | Network |
|---|---|---|---|
| `rt108-native` | `dgd-cleanroom:1` (`0ef9b2810304`) | eclipse-temurin 21 JDK (jammy), Google cmdline-tools `16111833`, platforms;android-36, build-tools 35.0.0, NDK 28.2.13676358; user `builder` | warm pass on, then `docker network disconnect bridge`; DNS and route verified dead |
| `rt108-arcade` | `dgd-cleanroom-flutter:1` (`966e6843be6c`) | the above plus Flutter 3.47.2 from GitHub, engine `1cf1c4773fb9…` (the host's engine) | pub get with `--enforce-lockfile`, then cut |

- **Inputs.** Only git bundles of dgd-native (`android-1.0.8-rc1`) and
  puzzle-app v1 (`99a5c36`), the module sync script, and the shipped
  artefacts for comparison. `docker inspect` showed 0 mounts on both
  containers.
- **Memory.** Docker's VM is capped at 4 GB by the user's `.wslconfig`
  (left unchanged). The containers ran at `--memory 3100m`, and Gradle ran
  with one worker, `-Xmx1792m`, SerialGC and in-process Kotlin. The Flutter
  module template asks for `-Xmx8G`; this was overridden to `-Xmx1024m`
  inside the container only.
- **Warm, then seal.** A first pass with the network on filled the Gradle
  cache without producing an artefact. Two lazily resolved artefacts
  (`compose-group-mapping:2.4.0`, `lint-gradle:31.9.1`) needed a second warm
  pass. The evidence build ran `--offline` after the cut, from `clean`.
- The scripts, Dockerfiles and comparisons are filed in
  `redteam-runs/20260929T2330Z-v1.0.8-7c2567c2/cleanroom/`.

## Verified

### Static (review APK and AAB)

- **Not debuggable.** `PreviewActivity` is gone.
- **Exported components.** Only `MainActivity` (launcher) and
  `ProfileInstallReceiver`, which requires the DUMP permission.
- **No link handling.** There is no app-link or `VIEW` intent filter;
  `https://digitalgold.co/app` does not resolve to the app.
- **Permissions.** `INTERNET` and `VIBRATE` only. Cleartext traffic is off.
- **Hosts.** The only host the app itself names is `digitalgold.co` (stats
  API, `/app`, `/arcade/`). The manifest `<queries>` (mailto, `SEND`
  text/plain, twitter, linkedin) serve the invite share and nothing else.
- **Secrets.** None found by the static scan.
- **Alignment.** 16 KB page alignment on every `.so`, and
  `zipalign -c -P 16` passes.
- **Backup rules.** Three excludes in each rule file: the two signup files
  and `FlutterSharedPreferences.xml` (W1).
- **Review APK versus AAB.** The review APK's `classes.dex` is identical to
  the AAB's, and all 180 libraries and assets are identical. The APK
  reviewers install is the code Play receives.
- **Embedded binary versus checked-in AAR.** The AAB's `libapp.so` equals the
  checked-in `flutter_release-1.0.aar`, and that AAR matches its `.sha256`
  sidecar.

### Native clean room: the AAB reproduces

`cleanroom-1.0.8-unsigned.aab` sha256 `ED2E310A…6E90`, compared entry by
entry with the shipped AAB: **636 of 642 identical**, including
`classes.dex`, every native library and every asset. The six that differ:

| Entry | Difference | Why it is benign |
|---|---|---|
| `BUNDLE-METADATA/…/proguard.map` | same lines, different order | R8 writes the map in thread-completion order |
| `BUNDLE-METADATA/…/r8.json` | build time and thread count | build-environment metadata |
| `BUNDLE-METADATA/…/baseline.prof`, `baseline.profm` | 2 and 4 bytes | profile serialisation; metadata, not code |
| `base/root/META-INF/services/Q2.u`, `R2.a` | CRLF (shipped) vs LF (clean room) | the Windows checkout's line endings reach two service files (P4) |

None of these is in the manifest, resources or code, so under §2.3 the
native half passes. Offline in the container: **unit tests 95/95**, and
**lint 0 errors, 35 warnings**. The host shows 8 more warnings, all
`GradleDependency` "newer version available" checks, which need the network.

### Dynamic, Android 16 (API 36), offline with the impostor on `localhost:8787`

- **The arcade makes zero requests.** The impostor logged 0 requests across
  the arcade menu, Coin Quest, the level map and a board with moves.
- **The Arcade menu** offers "Play in the app" and "Play in your browser"
  under the heading "DGD Arcade for Web". The web link is a bare
  `VIEW`/`BROWSABLE` intent for `https://digitalgold.co/arcade/`, handed to
  Chrome's IntentDispatcher. No user data is in the URL.
- **Hostile intents.** Nine hostile `VIEW` intents were sent to the activity
  by component:
  - an injected `?ref=` and a `<script>` `?ref=`
  - a 300-character ref
  - `javascript:`
  - `file://` aimed at the app's own `dgd.signup.xml`
  - `intent://…;end`
  - a contacts `content://` URI
  - NUL bytes
  - a 4,000-character path

  A separate intent carried a 20,000-character `EXTRA_TEXT`. Nothing
  crashed and no friend code was stored.
- **The legacy key is removed.** A seeded legacy `dgd.friendCode` preference
  was deleted on the next launch.
- **Login at rest.** After a login, the email and password exist only as
  encrypted entries. A recursive search of the data directory, and of
  logcat, found neither value in plaintext.
- **Backup.** Captured as root through the local transport, before and
  after login. It holds only `_manifest`, `r/app_flutter` and
  `f/profileInstalled`: no signup files and no shared preferences.

### Dynamic, Android 16, online behind a logging proxy

- **Egress is one host.** An on-device sampler read the app uid's sockets
  once a second. The only remote endpoint was `15.204.87.31:443`
  (`digitalgold.co`). The proxy log's other lines are Google system traffic
  (GMS on `:5228`, connectivity check, `clients2.google.com`).
- **Stats.** The Stats panel shows live figures only.
- **Signup preview.** Walked through credentials, verification, wallet and
  Receive with no requests beyond the stats fetch. The Receive step was not
  reached in the 1.0.3 pass.
- **Share bodies.** Every invite share text is built by a function that
  takes no arguments (checked statically), so no user-entered data can reach
  a share. The live share intent was not captured (see "Not tested").

### Dynamic, Android 8.0 (API 26, the minSdk)

- **Cold start works**, and the Flutter arcade and level map render on the
  old GPU stack. The impostor logged 0 requests.
- **No old-API crashes.** No `FATAL EXCEPTION`, `NoSuchMethodError`,
  `NoClassDefFoundError` or `VerifyError` anywhere. The log clear failed on
  this image, so the whole boot log was counted.
- **Web link.** Goes to the system resolver (no default browser on this
  image), with the same bare URL.
- **Login** is stored encrypted only.
- **Backup.** `fullBackupContent` applies (triggered with `bmgr run`), and
  the backup holds no preferences.

### Arcade clean room

- **Analyze.** `flutter analyze` is clean.
- **Tests.** The loopback suite passes 58 tests and the demo suite 5. The
  plain `flutter test` run is red by design: the check in `gate_test.dart`
  that "the network-layer suite is actually running" fails when run without
  its defines.
- **Module lock.** The generated module's resolved lock equals the v1 lock
  minus `flutter_lints` and `lints`, which matches the host module
  (`cleanroom/cleanroom-module-pubspec.lock`).

## Findings

### P1. MEDIUM — the embedded arcade binary cannot be reproduced by the clean room; the ship gate trips — OPEN

The checked-in `flutter_release-1.0.aar`, whose `libapp.so` is the one in the
AAB, was compared with container rebuilds from `99a5c36`
(`cleanroom/aar-compare.txt`):

| Comparison | Identical / 171 | `libapp.so` bytes differing |
|---|---|---|
| clean build 1 vs clean build 2, same path | **171** | 0; the container build is deterministic |
| build 1 (LF) vs build 5 (CRLF module and SDK), same path | 168 | 41–47 per ABI (0.001%): build-id and source hashes |
| build 1 vs build 3, different path | 168 | 15–26% |
| **shipped vs clean build 1** | **166** | **~90%**, same size in all three ABIs |
| shipped vs build 6, same-length path with the same registrant hash | 166 | still ~90% |

**What the evidence shows**

- **Program content matches.** Identifier and string tokens were extracted
  from shipped `libapp.so` and from build 6. The sets are equal except
  where a symbol-table tag byte sits next to a string (`lookUpLayout` vs
  `lookUpLayoutL`) and for the plugin-registrant file URL.
- **The build path is compiled in.** The Dart VM's private-name key for the
  registrant library was reimplemented (`cleanroom/dart_private_key.py`). It
  reproduces the keys of both container builds and the shipped
  `_PluginRegistrant@571119033` from `file:///C:/src/dgd_arcade_module/…`,
  so the path goes into the binary.
- **The path explains only part of it.** With the path and its hash
  matched (build 6), about 90% of bytes still move. Line endings account
  for about 47 bytes. What remains is layout: Windows `gen_snapshot`
  versus Linux `gen_snapshot` from the same engine.
- **Traced, not independently checked.** The host module's `lib/` equals
  `99a5c36` apart from CRLF and three empty directories. Its assets are
  identical. The checked-in AAR equals the host module's last build output.

**Why it matters.** The binary that ships can be traced to source, but not
verified independently. A change to the Windows toolchain or working tree
between commit and build could not be caught by this clean room. That is
the gap §2.3 exists to close, and the ship gate says nothing ships with "an
artefact the clean room could not reproduce".

**Fix.**
- Build the AAR inside the pinned Linux container: `dgd-cleanroom-flutter:1`
  or its Dockerfile, filed with the run.
- Build from a fixed path such as `/home/builder/dgd_arcade_module`, from a
  clean checkout of a tagged commit.
- Commit that output with its `.sha256` and the source commit.
- Any later clean room then reproduces it byte for byte, which build 1 vs
  build 2 already demonstrates.

The alternative is a signed waiver under the exemption gate, with two
names.

### P2. LOW — the embed's dependency lock is not versioned with the embed — OPEN

`sync_module.py` generates the Flutter module but does not copy
`pubspec.lock`. The versions compiled into the AAR are whatever `pub get`
resolved on the build machine that day. This time they matched v1's lock,
minus two lint packages. Fix: copy v1's `pubspec.lock` into the module and
build with `--enforce-lockfile`, as the clean room did.

### P3. LOW — the AAR was built from the working tree, before its commit existed — OPEN

Timeline:
- The module was synced at 22:11.
- `99a5c36` was committed at 22:15:37.
- The AAR was built at 22:21.

The content matches, but the provenance is a working tree, not a commit.
Fix: `sync_module.py` refuses a dirty tree and stamps the source commit
next to the AAR's `.sha256`.

### P4. LOW — `android/gradlew` is committed without the executable bit — OPEN

The file is mode `100644` in git, so `./gradlew` fails with "Permission
denied" on any Linux or macOS checkout, including CI and the clean room.
The container used `bash ./gradlew` as a workaround. Fix:
`git update-index --chmod=+x android/gradlew`.

### P5. INFO — Windows line endings leak into the artefacts

Windows builds carry CRLF into two AAB service files and the AAR manifest,
and NOTICES orders one Flutter licence block differently. None of this
affects behaviour. It goes away with P1's container build, or with a
`.gitattributes` `eol=lf`.

### P6. INFO — no `FLAG_SECURE` on the login sheet

The window flags are `LAYOUT_IN_SCREEN` only, so the email field can appear
in screenshots, screen recordings and the recents thumbnail. The password
field is masked. This matters more once the app handles a live account.

### P7. INFO — the Receive address field accepts arbitrary text

Anything typed is accepted and rendered inertly, and nothing is sent. It
needs validation before any real transfer uses it.

### P8. INFO — the arcade's DataStore backend is outside the W1 exclusion

W1 excludes `FlutterSharedPreferences.xml`. `shared_preferences` can also
store data in `datastore/` through its async API. Nothing uses that API
today, and the backup contained no `datastore/` entry. If the arcade adopts
it for the token, the backup rules need a matching exclude.

## Notes and carried items

- **Lint.** The host reports 8 more warnings than the container, all
  `GradleDependency` checks that need network access. They are not a
  difference in the code.
- **Carried from the readiness note, unchanged by this build:**
  - S1, S3, S4, S7 (server side).
  - The iOS build.
  - The share copy "predictably-priced, wealth-preserving", which is
    flagged for counsel.

## Not tested

- **Process death.** Restoring a live signup or board after the process is
  killed.
- **The live share intent.** Only the static check was done.
- **The won-level celebration** on either API level.
- **The Play-signed artefact.** Play re-signs the AAB, so the installable
  build users get was not in hand. It should be checked on internal
  testing.
- **iOS.**
- **Tablets and foldables.**

## Incidents during the pass

- **Docker engine hangs.** The engine hung twice under memory pressure from
  the 4 GB VM cap. `docker desktop restart` recovered it. That restart also
  restarted the user's `localllmdeployment-open_notebook-1` and
  `localllmdeployment-surrealdb-1`; both are running again. `.wslconfig` was
  not changed.
- **Containers not touched.** `nice_black` and `vibrant_elion`
  (`nvnci/fpga-cleanroom`) belong to other work and were left alone.
- **Cleanup.** Both `rt108-*` containers, which held the sources, are
  deleted. The images `dgd-cleanroom:1` (5.45 GB) and
  `dgd-cleanroom-flutter:1` (8.74 GB) hold toolchains only. They are kept
  so the P1 fix can reuse them.

## How to re-run

The scripts are in `redteam-runs/20260929T2330Z-v1.0.8-7c2567c2/cleanroom/`:

- `Dockerfile`, `Dockerfile.flutter`: the images.
- `native.sh warm|offline`: the AAB reproduction, tests and lint.
- `arcade.sh`, `rebuild.sh`: the Flutter module and AAR builds.
- `compare.py`: entry-by-entry comparison of two zips.
- `dart_private_key.py`: the registrant key calculation.
- `dyn.sh`, `online.sh`, `api26.sh`: the emulator phases.
- `impostor.py`, `egress_proxy.py`, `sampler.sh`: the fake backend, the
  logging proxy and the on-device socket sampler.
