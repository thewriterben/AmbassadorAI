#!/usr/bin/env bash
# Builds the arcade's iOS frameworks twice, from a fresh clone at a pinned
# commit, and requires the two to match. This is the iOS form of the ship
# gate's reproducibility rule (approved by the owner on 2026-10-01). The Linux
# clean-room container cannot build iOS frameworks, so the Mac builds A with
# the network on, then B from scratch with `pub get --offline`, and compares.
#
# WRITTEN ON THE PC AND NOT YET RUN ON A MAC. Its first run is its test: read
# what it prints, and fix it here rather than working round it by hand.
#
#   ./build_ios_frameworks.sh <puzzle-app-v2.bundle> <commit> demo        <out dir>
#   ./build_ios_frameworks.sh <puzzle-app-v2.bundle> <commit> <https url> <out dir>
#
#   demo         DGD_APP_TAB=true, DGD_DEMO=true: no server, as DGD App 2.0.
#   https://...  DGD_APP_TAB=true, ARCADE_API=<url>: the live build (2.1).
#                Bare https only: no trailing slash, query or credentials.
#
# For DGD App 2.0 (iOS): commit 3c4e42d, demo. That is the arcade Android 2.0.0
# rc2 embeds, so both phones run the same arcade.
#
# The build directory is FIXED (/tmp/dgd-ios-build): Dart compiles the
# module's path into the app snapshot, as it does on Android
# (AUDIT-v1.0.8-2026-09-29.md, P1), so A and B must be built at the same path.
set -euo pipefail

BUNDLE="${1:?bundle}"; COMMIT="${2:?commit}"; MODE="${3:?demo or https url}"; OUT="${4:?out dir}"
HERE="$(cd "$(dirname "$0")" && pwd)"
FIX=/tmp/dgd-ios-build

if [ "$MODE" = demo ]; then
  DEFINES=(--dart-define=DGD_APP_TAB=true --dart-define=DGD_DEMO=true)
elif [[ "$MODE" =~ ^https://[A-Za-z0-9.-]+(:[0-9]{1,5})?(/[A-Za-z0-9._~-]+)*$ ]]; then
  DEFINES=(--dart-define=DGD_APP_TAB=true "--dart-define=ARCADE_API=$MODE")
else
  echo "mode must be 'demo' or a bare https URL with no trailing slash; got: $MODE"; exit 1
fi

command -v flutter >/dev/null || { echo "flutter is not on PATH"; exit 1; }
echo "flutter: $(flutter --version 2>/dev/null | head -1)"
echo "         expected Flutter 3.47.2 / Dart 3.13.2, the same as the PC"
echo "defines: ${DEFINES[*]}"

build() {  # $1 = A or B; $2 = extra pub get flag
  rm -rf "$FIX"; mkdir -p "$FIX"
  git clone -q "$BUNDLE" "$FIX/puzzle-app"
  git -C "$FIX/puzzle-app" -c advice.detachedHead=false checkout -q "$COMMIT"
  test "$(git -C "$FIX/puzzle-app" rev-parse HEAD)" = "$(git -C "$FIX/puzzle-app" rev-parse "$COMMIT^{commit}")"
  (cd "$FIX" && flutter create -t module --org co.digitalgold.arcade dgd_arcade_module >/dev/null)
  DGD_ARCADE=v2 DGD_V2="$FIX/puzzle-app" DGD_MODULE="$FIX/dgd_arcade_module" python3 "$HERE/sync_module.py"
  cd "$FIX/dgd_arcade_module"
  flutter pub get --enforce-lockfile $2
  cmp -s "$FIX/puzzle-app/pubspec.lock" pubspec.lock || { echo "module lock differs from the arcade's"; exit 1; }
  flutter build ios-framework --xcframework --no-debug --no-profile "${DEFINES[@]}" --output="$FIX/out"
  rm -rf "$OUT/$1"; mkdir -p "$OUT/$1"
  cp -R "$FIX/out/Release/." "$OUT/$1/"
  cd "$HERE"
  echo "build $1: $(find "$OUT/$1" -maxdepth 1 -name '*.xcframework' | wc -l | tr -d ' ') xcframeworks"
}

mkdir -p "$OUT"
echo "== build A (network on)"
build A ""
echo "== build B (from scratch, pub offline)"
build B "--offline"

echo "== compare A and B"
( cd "$OUT/A" && find . -type f | sort | xargs shasum -a 256 ) > "$OUT/A.sha256"
( cd "$OUT/B" && find . -type f | sort | xargs shasum -a 256 ) > "$OUT/B.sha256"
if diff -q "$OUT/A.sha256" "$OUT/B.sha256" >/dev/null; then
  echo "A == B: $(wc -l < "$OUT/A.sha256" | tr -d ' ') files, all byte-identical"
  SAME=1
else
  echo "A and B differ:"
  diff "$OUT/A.sha256" "$OUT/B.sha256" | grep '^[<>]' | sed 's/^/  /' | head -40
  echo "Look at each one. Timestamps in Info.plist or a build UUID can be explained;"
  echo "anything inside App.framework/App (the arcade's code) cannot. Do not ship"
  echo "until every difference is written down in PROVENANCE.md and explained."
  SAME=0
fi

{
  echo "# Arcade embed for iOS, built on the Mac"
  echo
  echo "source   puzzle-app v2 $(git -C "$FIX/puzzle-app" rev-parse HEAD)"
  echo "defines  ${DEFINES[*]}"
  echo "module   $FIX/dgd_arcade_module (fixed; it is compiled into App.framework)"
  echo "lock     enforced; sha256 $(shasum -a 256 "$FIX/puzzle-app/pubspec.lock" | cut -c1-64)"
  echo "flutter  $(flutter --version 2>/dev/null | head -1)"
  echo "xcode    $(xcodebuild -version 2>/dev/null | tr '\n' ' ')"
  echo "A vs B   $([ "$SAME" = 1 ] && echo "byte-identical" || echo "DIFFER, see above")"
  echo
  echo "## sha256 (build B, the one to embed)"
  cat "$OUT/B.sha256"
} > "$OUT/PROVENANCE.md"
echo "provenance written: $OUT/PROVENANCE.md"
[ "$SAME" = 1 ] || exit 2
