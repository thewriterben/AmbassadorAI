# DGD App 2.1.0 rc3 (live arcade), native half rebuilt in the clean room: 2026-10-01

`arcade/integration/cleanroom/build_native_cleanroom.sh f1c1f43 <host aab>`:

- **Source:** dgd-native `f1c1f43` (branch `dgd-2.1-live`), copied in as a
  git bundle with no mounts. The arcade AAR is the clean-room v2 build of
  `85e621c`, with `ARCADE_API=https://arcade-api.digitalgold.co`.
- **Warm build, network on,** then **the network was cut and verified
  dead.** The offline evidence build then ran:
  - `bundleRelease` passes, and the app's arcade gate matched all 36 files to
    the `85e621c` clean-room build;
  - all 97 unit tests pass;
  - `lintRelease` passes.
- **Comparison with the host-built `DigitalGold-2.1.0-unsigned.aab`
  (`dist-2.1.0-rc3`):** 789 entries each, 785 byte-identical.
- **The 4 that differ** are the same four as every earlier pass:
  - R8's `proguard.map` and `r8.json`, which are build metadata;
  - two `META-INF/services` entries that differ only in CRLF against LF line
    endings.

  No dex, native library, resource or asset differs.
