# DGD App 2.0.0 rc2, native half rebuilt in the clean room: 2026-09-30

`arcade/integration/cleanroom/build_native_cleanroom.sh ab23aef <host aab>`:

- **Source:** dgd-native `ab23aef` (branch `dgd-2.0`), copied in as a git
  bundle with no mounts. The arcade AAR is the commit's `arcade-repo`: the
  clean-room v2 build of `3c4e42d`, demo mode.
- **Warm build, network on:** bundleRelease, the unit tests and lintRelease,
  so every tool the evidence build needs is cached.
- **Network cut and verified dead.** The offline evidence build then ran:
  - `bundleRelease` passes, and the app's own arcade gate matched all 36
    files to the v2 `3c4e42d` clean-room build;
  - all 95 unit tests pass;
  - `lintRelease` passes.
- **Comparison with the host-built `DigitalGold-2.0.0-unsigned.aab`
  (`dist-2.0.0-rc2`):** 788 entries each, 784 byte-identical.
- **The 4 that differ:**
  - R8's `proguard.map` and `r8.json`, which are build metadata and are not
    installed on a device;
  - two `META-INF/services` entries, `Q2.u` and `R2.a`. They name the same
    classes in both builds and differ only in line endings: the Windows host
    writes CRLF, the Linux container LF.

  rc1 also differed in the two baseline-profile files; rc2 does not. No dex,
  native library, resource or asset differs.

The image is in `IMAGE.txt`, the hashes in `aab.sha256`, and the logs sit
alongside.
