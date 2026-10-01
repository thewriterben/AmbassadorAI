# DGD App 2.0 native half, rebuilt in the clean room — 2026-09-30

`arcade/integration/cleanroom/build_native_cleanroom.sh f04b884 <host aab>`:

- **Source:** dgd-native `f04b884` (branch `dgd-2.0`), copied in as a git
  bundle with no mounts. The arcade AAR is the commit's `arcade-repo`: the
  clean-room v2 build of `7fc97da`.
- **Warm build, network on:** bundleRelease, the unit tests and lintRelease.
  These are the same tasks as the evidence build, so every tool they need is
  in the cache. A narrower warm-up left Kotlin 2.4's `compose-group-mapping`
  and `lint-gradle` undownloaded on the first two tries.
- **Network cut and verified dead.** The offline evidence build then ran:
  - `bundleRelease` passes, and the app's own arcade gate matched all 36
    files to the v2 `7fc97da` clean-room build;
  - all 95 unit tests pass;
  - `lintRelease` passes.
- **Comparison with the host-built `DigitalGold-2.0.0-unsigned.aab`:** 788
  entries each, 782 byte-identical.
- **The 6 that differ** are the same six as in the v1.0.8 pass
  (`AUDIT-v1.0.8-2026-09-29.md`): R8's `proguard.map` and `r8.json`, the
  baseline profiles, and two `META-INF/services` entries whose names R8
  assigns. No dex, native library, resource or asset differs.

The image is in `IMAGE.txt`, the hashes in `aab.sha256`, and the logs sit
alongside.
