# DGD App 2.1.0 rc1 (live arcade), native half rebuilt in the clean room: 2026-09-30

`arcade/integration/cleanroom/build_native_cleanroom.sh 89d1e38 <host aab>`:

- **Source:** dgd-native `89d1e38` (branch `dgd-2.1-live`), copied in as a
  git bundle with no mounts. The arcade AAR is the commit's `arcade-repo`: the
  clean-room v2 build of `ef16aa6`, with
  `ARCADE_API=https://arcade-api.digitalgold.co`.
- **Warm build, network on,** then **the network was cut and verified
  dead.** The offline evidence build then ran:
  - `bundleRelease` passes, and the app's arcade gate matched all 36 files to
    the `ef16aa6` clean-room build;
  - all 95 unit tests pass;
  - `lintRelease` passes.
- **Comparison with the host-built `DigitalGold-2.1.0-unsigned.aab`
  (`dist-2.1.0-rc1`):** 788 entries each, 784 byte-identical.
- **The 4 that differ** are the same four as 2.0.0 rc2:
  - R8's `proguard.map` and `r8.json`, which are build metadata;
  - two `META-INF/services` entries that differ only in CRLF against LF line
    endings.

  No dex, native library, resource or asset differs.
