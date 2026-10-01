# DGD App 2.1.0 rc2 (live arcade), native half rebuilt in the clean room: 2026-10-01

`arcade/integration/cleanroom/build_native_cleanroom.sh 2791096 <host aab>`:

- **Source:** dgd-native `2791096` (branch `dgd-2.1-live`), copied in as a
  git bundle with no mounts. The arcade AAR is the clean-room v2 build of
  `d70534a`, with `ARCADE_API=https://arcade-api.digitalgold.co`.
- **Warm build, network on,** then **the network was cut and verified
  dead.** The offline evidence build then ran:
  - `bundleRelease` passes, and the app's arcade gate matched all 36 files to
    the `d70534a` clean-room build;
  - all 97 unit tests pass, `ArcadeLiveFlagTest` included;
  - `lintRelease` passes.
- **Comparison with the host-built `DigitalGold-2.1.0-unsigned.aab`
  (`dist-2.1.0-rc2`):** 789 entries each (the standings icon is the new one),
  785 byte-identical.
- **The 4 that differ** are the same four as every earlier pass:
  - R8's `proguard.map` and `r8.json`, which are build metadata;
  - two `META-INF/services` entries that differ only in CRLF against LF line
    endings.

  No dex, native library, resource or asset differs.
