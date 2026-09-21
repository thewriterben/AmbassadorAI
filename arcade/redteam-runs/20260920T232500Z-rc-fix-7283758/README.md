Same procedure as ../20260920T225000Z-rc-07aabe7 (wiped API 35 emulator, airplane
mode, localhost:8787 routed to the impostor backend), against the rebuilt
`DGD-merged-arcade-v1.0.2-demo-debug.apk` (sha256 72837584f16b2e18cfde55b1...).

- `impostor-requests.log` is empty: zero requests at ticker launch and after
  opening the arcade.
- `emulator-arcade-after-impostor.png`: the arcade with no XP bar, no OFFLINE
  chip and no standings link, which is the demo behaviour.
- Nothing was persisted: no FlutterSharedPreferences.xml at rest.
- `libapp.so` contains no `localhost:8787` string at all.
