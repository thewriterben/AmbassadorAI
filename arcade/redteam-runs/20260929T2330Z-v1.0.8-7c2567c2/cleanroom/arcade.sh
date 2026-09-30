#!/usr/bin/env bash
# Runs INSIDE the Flutter clean-room container. Rebuilds the embedded arcade AAR
# from arcade v1 at the commit the release notes name, the way build_aar.cmd
# does it (sync_module.py, then flutter build aar with the demo defines), and
# runs the arcade's three required test configurations first.
set -uo pipefail
OUT=/home/builder/out; mkdir -p "$OUT"; cd /home/builder
cat flutter-version.txt | head -4
git clone -q --branch main /home/builder/in/arcade.bundle puzzle-app
echo "arcade commit $(git -C puzzle-app rev-parse --short HEAD)  clean=$(git -C puzzle-app status --porcelain | wc -l)"

echo "== arcade v1: analyze and the three test configurations"
cd puzzle-app
flutter pub get --enforce-lockfile > "$OUT/arcade-pubget.log" 2>&1; echo "pub get --enforce-lockfile exit $?"
flutter analyze > "$OUT/arcade-analyze.log" 2>&1; echo "analyze exit $? : $(tail -1 "$OUT/arcade-analyze.log")"
flutter test > "$OUT/arcade-test-plain.log" 2>&1; echo "test plain exit $? : $(grep -E 'All tests passed|Some tests failed' "$OUT/arcade-test-plain.log" | tail -1)"
flutter test --dart-define=ARCADE_API=http://127.0.0.1:18799 > "$OUT/arcade-test-api.log" 2>&1; echo "test loopback exit $? : $(grep -E 'All tests passed|Some tests failed' "$OUT/arcade-test-api.log" | tail -1)"
flutter test --dart-define=ARCADE_API=http://127.0.0.1:18798 --dart-define=DGD_DEMO=true test/arcade_api_test.dart > "$OUT/arcade-test-demo.log" 2>&1; echo "test demo exit $? : $(grep -E 'All tests passed|Some tests failed' "$OUT/arcade-test-demo.log" | tail -1)"
cd ..

echo "== generate the module the way build_aar.cmd does"
flutter create -t module --org co.digitalgold.arcade dgd_arcade_module > "$OUT/module-create.log" 2>&1; echo "create exit $?"
sed -e 's#^V1 = .*#V1 = pathlib.Path("/home/builder/puzzle-app")#' -e 's#^MODULE = .*#MODULE = pathlib.Path("/home/builder/dgd_arcade_module")#' in/sync_module.py > sync_module.py
python3 sync_module.py 2>&1 | tail -6
# Pin dependencies from the versioned arcade lock (sync_module.py does not copy it).
cp puzzle-app/pubspec.lock dgd_arcade_module/pubspec.lock
cd dgd_arcade_module
flutter pub get > "$OUT/module-pubget.log" 2>&1; echo "module pub get exit $?"
cp pubspec.lock "$OUT/cleanroom-module-pubspec.lock"
flutter build aar --no-debug --no-profile --dart-define=DGD_APP_TAB=true --dart-define=DGD_DEMO=true > "$OUT/aar.log" 2>&1; echo "build aar exit $?"; tail -3 "$OUT/aar.log"
cp build/host/outputs/repo/co/digitalgold/arcade/module/flutter_release/1.0/flutter_release-1.0.aar "$OUT/cleanroom-flutter_release-1.0.aar" 2>/dev/null
ls -la "$OUT" | grep -E "\.aar|\.lock"
