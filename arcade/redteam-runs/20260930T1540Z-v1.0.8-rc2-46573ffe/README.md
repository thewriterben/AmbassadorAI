# Run 20260930T1540Z — DGD 1.0.8 rc2 re-verification (review APK `46573ffe…`, AAB `2f768698…`)

Step 3 of the fix pass for `arcade/AUDIT-v1.0.8-2026-09-29.md`. The rc2
source is dgd-native `a22c194` (tag `android-1.0.8-rc2`). The arcade is
built from puzzle-app `99a5c36` (tag `embed-android-1.0.8`) in the clean
room.

## 1. The rc2 Play bundle reproduces in a fresh, offline container

The container ran `dgd-cleanroom:1`, with the source as a git bundle and 0
mounts. Gradle caches were filled with the network on, then the network was
cut (no DNS), and the evidence build ran from `clean` with `--offline`.
Scripts and logs are in `cleanroom/`.

- **Checkout.** `a22c194`, tag `android-1.0.8-rc2`, a clean tree.
- **P4 holds.** `gradlew` checks out as `-rwxr-xr-x`, and `./gradlew` runs
  directly.
- **The ship gate ran in the container.** `verifyArcadeProvenance` passed:
  "36 files match the clean-room build". So the committed `arcade-repo` is
  byte-exact on a Linux checkout too.
- **Tests and lint.** Unit tests 95/95; `lintRelease` exit 0 (no errors).
- **The bundles match.** The container's AAB
  (`2d91ef58…`, `cleanroom/cleanroom-rc2-aab.sha256`) against the rc2 AAB
  (`2f768698…`): **638 of 642 entries identical**. That includes
  `classes.dex`, every native library (`libapp.so` in all ABIs), every
  asset and the baseline profiles. The four that differ
  (`cleanroom/aab-rc2-compare.txt`):
  - `proguard.map`: the same 333,231 mapping lines in a different order.
    The only differing line is the `# pg_map_hash` header, which hashes
    that order.
  - `r8.json`: `buildTimeNs` and `numberOfThreads` only.
  - `META-INF/services/Q2.u` and `R2.a`: CRLF on Windows, LF in the
    container. R8 writes them with the host's line separator (audit P5).

  None of these is in the manifest, resources or code, so under §2.3 the
  rc2 bundle passes.

## 2. Emulator smoke test, Android 16 (API 36), offline

**The emulator.** A wiped `dgd_api36` emulator, rooted, with the rc2
review APK installed. The installed APK's sha256 equals
`DigitalGold-1.0.8-review.apk` (`46573ffe…`). The impostor backend ran on
`localhost:8787`.

**The network was verifiably off for the whole run:**
- airplane mode, plus `svc wifi/data disable`;
- a watcher logged "Active default network: none" in all 56 samples,
  once every 5 seconds (`rc2-network-watch.txt`);
- the on-device sampler recorded **no sockets at all** for the app's uid
  (`rc2-app-sockets.txt` is empty);
- the impostor logged 0 requests (`rc2-impostor-requests.txt`).

**Results:**
- **Arcade.** It starts on the Linux-built `libapp.so`: the Arcade menu,
  then Coin Quest, level 1 and a board with swaps (`rc2-2-*.png`). There
  were no crashes, and the arcade's only preference is the coach flag.
  Music was not re-measured this pass.
- **Hostile intents.** The nine hostile `VIEW` intents plus the
  20,000-character extra caused no crash and stored no friend code.
  `digitalgold.co/app` does not resolve to the app.
- **Legacy key.** A seeded legacy `dgd.friendCode` was deleted on relaunch.
- **Login at rest.** The email and password are stored only as encrypted
  entries, with no plaintext anywhere in app storage or in logcat.
- **No `FLAG_SECURE`.** Unchanged (audit P6).
- **Web arcade link.** Checked by hand, because the scripted step lost its
  way after the in-app arcade: a bare `VIEW`/`BROWSABLE` intent for
  `https://digitalgold.co/...` to Chrome's IntentDispatcher, as in rc1
  (`rc2-3-web-link.png`).
- **Backup.** `_manifest`, `r/app_flutter`, `f/profileInstalled`, and
  `sp/dgd.ticker.xml`. The ticker's snapshot file is not excluded, by
  design (it is public market data: accounts, price, market cap), and it
  was present only because of the discarded first run below.
- **Not reached by automation, as in the audit:** process death with the
  login sheet open, and the Invite Friends step.

### A discarded first run, and one unplanned stats fetch

The first attempt disabled the network with `svc wifi/data disable` only.
Mobile data came back up on its own: after the run the network was
`CONNECTED`, validated LTE. During that run the app's own stats fetch
reached `digitalgold.co` once, at 15:42:13 UTC. The live snapshot it
cached shows this. That is the same request the audit made deliberately
in its online phase, but here it was not planned. It is recorded as an
unplanned exception to §2.

That run was discarded, because "0 impostor requests" proves nothing while
another route is open. Its backup is kept in `discarded-first-run/`. The
app was uninstalled, and the second run above used airplane mode and the
watcher. Android then restored `dgd.ticker.xml` from the first run's local
backup when the app was reinstalled. That is why a snapshot with the same
15:42:13 timestamp appears in the offline run.

## 3. Independent rebuild of the arcade AAR — not completed

A second, independent container build of the AAR was started, without
publishing, to compare against `arcade-repo`. The Docker engine hung for
about 5 minutes: it answered HTTP 500, while another project's FPGA
synthesis containers were sharing the 4 GB VM. Build A stalled for 38
minutes and failed on a missing intermediate file, and build B found a
broken module. This is an infrastructure failure and says nothing about
the AAR. Nothing was published.

The AAR remains verified by:
- the fix-pass run itself, where the online build A equals the offline
  build B in all six AARs;
- the audit's own independent container build from 2026-09-29, whose
  `libapp.so` is byte-identical in all three ABIs to the one in
  `arcade-repo`.

Re-run `build_aar_cleanroom.sh embed-android-1.0.8` without `--publish`
when the VM is otherwise idle.
