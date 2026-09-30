#!/usr/bin/env bash
# Runs INSIDE the clean-room container. Phase "warm" (network on) fills the
# dependency cache without running R8; phase "offline" (network cut) is the
# evidence build. Memory is tight (the Docker VM is 4 GB), so R8 runs alone.
set -uo pipefail
PHASE="$1"
OUT=/home/builder/out; mkdir -p "$OUT"
cd /home/builder
[ -d native ] || git clone -q --branch "${TAG:-android-1.0.8-rc2}" /home/builder/in/native.bundle native
cd native
echo "commit $(git rev-parse HEAD)  tag $(git describe --tags)  clean=$(git status --porcelain | wc -l)"
cd android
printf 'sdk.dir=%s\n' "$ANDROID_HOME" > local.properties
export GRADLE_OPTS="-Xmx96m"
JVM="-Xmx1792m -XX:MaxMetaspaceSize=448m -XX:ReservedCodeCacheSize=96m -XX:+UseSerialGC -Dfile.encoding=UTF-8"
G="bash ./gradlew --no-daemon --console=plain --max-workers=1 -Dorg.gradle.jvmargs=\"$JVM\" -Pkotlin.compiler.execution.strategy=in-process"
run() { eval "$G $*"; }
case "$PHASE" in
  warm)
    run :app:compileReleaseKotlin :app:processReleaseResources :app:testDebugUnitTest :app:produceReleaseComposeMapping :app:lintAnalyzeRelease > "$OUT/warm.log" 2>&1; echo "warm exit $?"; grep -E "BUILD|What went wrong" "$OUT/warm.log" | tail -2 ;;
  offline)
    run --offline clean :app:bundleRelease > "$OUT/offline-bundle.log" 2>&1; echo "offline bundleRelease exit $?"; grep -E "BUILD|What went wrong" "$OUT/offline-bundle.log" | tail -2
    cp app/build/outputs/bundle/release/app-release.aab "$OUT/cleanroom-rc2-unsigned.aab" 2>/dev/null
    run --offline :app:testDebugUnitTest > "$OUT/offline-test.log" 2>&1; echo "offline tests exit $?"
    t=0; f=0; for x in app/build/test-results/testDebugUnitTest/*.xml; do t=$((t+$(grep -o -E 'tests="[0-9]+"' "$x" | head -1 | tr -dc 0-9))); f=$((f+$(grep -o -E 'failures="[0-9]+"' "$x" | head -1 | tr -dc 0-9)+$(grep -o -E 'errors="[0-9]+"' "$x" | head -1 | tr -dc 0-9))); done; echo "unit tests: $t, failures+errors: $f"
    run --offline :app:lintRelease > "$OUT/offline-lint.log" 2>&1; echo "offline lintRelease exit $?"; grep -E "errors?, [0-9]+ warnings?|Lint found" "$OUT/offline-lint.log" | tail -1
    ls -la "$OUT" | grep -E "\.aab|\.apk" ;;
esac
