# DGD App 2.0.0 rc3, native half rebuilt in the clean room: 2026-10-01

`arcade/integration/cleanroom/build_native_cleanroom.sh 16394ec <host aab>`:

- **Source:** dgd-native `16394ec` (branch `dgd-2.0`), copied in as a git
  bundle with no mounts. The arcade AAR is the clean-room v2 build of
  `85e621c`, demo mode.
- **Warm build, network on,** then **the network was cut and verified
  dead.** The offline evidence build then ran:
  - `bundleRelease` passes, and the app's arcade gate matched all 36 files to
    the `85e621c` clean-room build;
  - all 95 unit tests pass;
  - `lintRelease` passes.
- **Comparison with the host-built `DigitalGold-2.0.0-unsigned.aab`
  (`dist-2.0.0-rc3`):** 788 entries each, 784 byte-identical.
- **The 4 that differ** are the same four as every earlier pass:
  - R8's `proguard.map` and `r8.json`, which are build metadata;
  - two `META-INF/services` entries that differ only in CRLF against LF line
    endings.

  No dex, native library, resource or asset differs.
