#!/usr/bin/env bash
# Runs INSIDE a dgd-cleanroom:1 container, driven by build_native_cleanroom.sh.
#
#   native_in_container.sh warm    <commit>   network on: fill the Gradle cache
#   native_in_container.sh offline <commit>   network cut: the evidence build
#
# The same two phases as the v1.0.8 pass (redteam-runs/20260929T2330Z-v1.0.8-*/
# cleanroom/native.sh), with the commit as an argument instead of a fixed tag.
# Memory is tight (the Docker VM is about 4 GB), so R8 runs alone with one
# worker and the Kotlin compiler in process.
set -uo pipefail
PHASE="$1"; COMMIT="$2"
OUT=/home/builder/out; mkdir -p "$OUT"
cd /home/builder
if [ ! -d native ]; then
  git clone -q /home/builder/in/native.bundle native
  git -C native -c advice.detachedHead=false checkout -q "$COMMIT"
fi
cd native
test "$(git rev-parse HEAD)" = "$COMMIT" || { echo "commit mismatch"; exit 1; }
echo "commit $(git rev-parse HEAD)  clean=$(git status --porcelain | wc -l)"
cd android
printf 'sdk.dir=%s\n' "$ANDROID_HOME" > local.properties
export GRADLE_OPTS="-Xmx96m"
JVM="-Xmx1792m -XX:MaxMetaspaceSize=448m -XX:ReservedCodeCacheSize=96m -XX:+UseSerialGC -Dfile.encoding=UTF-8"
G="bash ./gradlew --no-daemon --console=plain --max-workers=1 -Dorg.gradle.jvmargs=\"$JVM\" -Pkotlin.compiler.execution.strategy=in-process"
run() { eval "$G $*"; }
case "$PHASE" in
  warm)
    # The same tasks as the offline phase, so every tool they resolve is in
    # the cache when the network goes: a narrower warm-up (compile and
    # resources only, as for 1.0.8) left Kotlin 2.4's compose-group-mapping
    # and lint-gradle undownloaded, and the offline build failed on them.
    # Separate runs, so R8 and lint never share the container's memory.
    run :app:bundleRelease > "$OUT/warm.log" 2>&1; echo "warm bundleRelease exit $?"
    grep -E "BUILD|What went wrong" "$OUT/warm.log" | tail -2
    run :app:testDebugUnitTest > "$OUT/warm-test.log" 2>&1; echo "warm tests exit $?"
    run :app:lintRelease > "$OUT/warm-lint.log" 2>&1; echo "warm lintRelease exit $?" ;;
  offline)
    run --offline clean :app:bundleRelease > "$OUT/offline-bundle.log" 2>&1; echo "offline bundleRelease exit $?"
    grep -E "Arcade embed|BUILD" "$OUT/offline-bundle.log" | tail -2
    grep -A12 "What went wrong" "$OUT/offline-bundle.log" | head -14
    cp app/build/outputs/bundle/release/app-release.aab "$OUT/cleanroom-unsigned.aab" 2>/dev/null
    run --offline :app:testDebugUnitTest > "$OUT/offline-test.log" 2>&1; echo "offline tests exit $?"
    t=0; f=0
    for x in app/build/test-results/testDebugUnitTest/*.xml; do
      t=$((t+$(grep -o -E 'tests="[0-9]+"' "$x" | head -1 | tr -dc 0-9)))
      f=$((f+$(grep -o -E 'failures="[0-9]+"' "$x" | head -1 | tr -dc 0-9)+$(grep -o -E 'errors="[0-9]+"' "$x" | head -1 | tr -dc 0-9)))
    done
    echo "unit tests: $t, failures+errors: $f"
    run --offline :app:lintRelease > "$OUT/offline-lint.log" 2>&1; echo "offline lintRelease exit $?"
    grep -E "errors?, [0-9]+ warnings?|Lint found" "$OUT/offline-lint.log" | tail -1
    grep -A8 "What went wrong" "$OUT/offline-lint.log" | head -10
    ls -la "$OUT" | grep -E "\.aab" || true ;;
esac
