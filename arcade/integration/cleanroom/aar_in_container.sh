#!/usr/bin/env bash
# Runs INSIDE a dgd-cleanroom-flutter container, driven by build_aar_cleanroom.sh.
#
#   aar_in_container.sh online  <commit>   network on: fetch packages, build A
#   aar_in_container.sh offline <commit>   network cut: clean, build B, compare
#
# DGD_ARCADE (v1 or v2, set on the container) says which arcade line the
# bundle holds. The source is cloned to the same path either way; only the
# module path is compiled into libapp.so.
#
# Build B is the release artefact. Build A exists to fill the caches, and
# comparing it with B proves the build deterministic on every run.
#
# The module path is fixed, because Dart compiles the plugin registrant's file
# URL into libapp.so (AUDIT-v1.0.8-2026-09-29.md, P1). Change it and every
# earlier build stops reproducing.
set -euo pipefail
PHASE="$1"; COMMIT="$2"; ARCADE="${DGD_ARCADE:-v1}"
H=/home/builder; IN=$H/in; OUT=$H/out; MODULE=$H/dgd_arcade_module; V1=$H/puzzle-app
DEFINES="--dart-define=DGD_APP_TAB=true --dart-define=DGD_DEMO=true"
REPO=build/host/outputs/repo
mkdir -p "$OUT"

# The Docker VM is small; the module template asks Gradle for 8 GB. The user
# home properties outrank the project's. Kotlin stays in its own daemon (run
# in-process it pushes Gradle's Metaspace past 640 MB), but capped: left alone
# it inherits Gradle's settings, and the two JVMs together were OOM-killed.
mkdir -p $H/.gradle
printf '%s\n' "org.gradle.jvmargs=-Xmx1024m -XX:MaxMetaspaceSize=768m -XX:ReservedCodeCacheSize=128m -XX:+UseSerialGC -Dfile.encoding=UTF-8" \
  "kotlin.daemon.jvmargs=-Xmx512m -XX:MaxMetaspaceSize=320m -XX:+UseSerialGC" \
  "org.gradle.daemon=false" "org.gradle.workers.max=1" > $H/.gradle/gradle.properties

build() {  # $1 = label
  cd "$MODULE"
  flutter clean > /dev/null 2>&1
  flutter pub get --enforce-lockfile $2 > "$OUT/$1-pubget.log" 2>&1 || { echo "pub get --enforce-lockfile FAILED"; tail -5 "$OUT/$1-pubget.log"; exit 1; }
  cmp -s "$V1/pubspec.lock" pubspec.lock || { echo "module lock differs from $ARCADE's"; diff "$V1/pubspec.lock" pubspec.lock | head; exit 1; }
  flutter build aar --no-debug --no-profile $DEFINES > "$OUT/$1-aar.log" 2>&1 || { echo "build $1 FAILED"; tail -15 "$OUT/$1-aar.log"; return 1; }
  rm -rf "$OUT/$1"; cp -r "$REPO" "$OUT/$1"
  echo "build $1: $(find "$OUT/$1" -name '*.aar' | wc -l) AARs"
}

case "$PHASE" in
online)
  git clone -q "$IN/puzzle-app.bundle" "$V1"
  git -C "$V1" -c advice.detachedHead=false checkout -q "$COMMIT"
  test "$(git -C "$V1" rev-parse HEAD)" = "$COMMIT" || { echo "commit mismatch"; exit 1; }
  echo "$ARCADE $(git -C "$V1" rev-parse HEAD) $(git -C "$V1" describe --tags --always)"
  flutter create -t module --org co.digitalgold.arcade dgd_arcade_module > "$OUT/module-create.log" 2>&1
  DGD_ARCADE="$ARCADE" DGD_V1="$V1" DGD_V2="$V1" DGD_MODULE="$MODULE" python3 "$IN/sync_module.py"
  # Build A only fills caches, so one retry is allowed: a dropped download
  # from Maven Central killed it once, and Gradle keeps what it already has.
  build A "" || { echo "retrying build A once"; build A ""; }
  ;;
offline)
  if getent hosts pub.dev > /dev/null 2>&1; then echo "network is still up; refusing"; exit 1; fi
  build B "--offline" || exit 1
  cd "$OUT"
  # What the app consumes is the AARs, and Gradle picks them through the POMs
  # and .module files: those must match. Three things carry build timestamps
  # and legitimately differ: the Dokka javadoc jars, the .module entries that
  # record those jars' hashes (plus Gradle's per-build id), and
  # maven-metadata.xml's lastUpdated. Each is compared with exactly those
  # parts removed, so anything else that moves still fails the run.
  python3 - <<'EOF'
import hashlib, json, pathlib, re, sys
a, b = pathlib.Path("A"), pathlib.Path("B")
def sums(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file()}
def module_sans_timestamps(p):
    m = json.loads(p.read_text())
    m.get("createdBy", {}).get("gradle", {}).pop("buildId", None)
    m["variants"] = [v for v in m.get("variants", []) if "javadoc" not in v.get("name", "").lower()]
    return m
sa, sb = sums(a), sums(b)
diff = sorted(k for k in sa.keys() | sb.keys() if sa.get(k) != sb.get(k))
bad = []
for k in diff:
    if k not in sa or k not in sb:
        bad.append(k + " (only in one build)")
    elif re.search(r"-javadoc\.jar(\.(md5|sha1|sha256|sha512))?$", k):
        pass
    elif re.search(r"\.module\.(md5|sha1|sha256|sha512)$|maven-metadata\.xml\.(md5|sha1|sha256|sha512)$", k):
        pass  # checksum of a file judged below
    elif k.endswith(".module"):
        if module_sans_timestamps(a / k) != module_sans_timestamps(b / k):
            bad.append(k + " (beyond the javadoc entries and build id)")
    elif k.endswith("maven-metadata.xml"):
        strip = lambda p: re.sub(r"<lastUpdated>\d+</lastUpdated>", "", p.read_text())
        if strip(a / k) != strip(b / k):
            bad.append(k + " (beyond lastUpdated)")
    else:
        bad.append(k)
aars = sorted(k for k in sb if k.endswith(".aar"))
print(f"A vs B: {len(sb)} files, {len(sb) - len(diff)} byte-identical, "
      f"{len(diff) - len(bad)} differ only in build timestamps")
print(f"AARs identical: {sum(sa.get(k) == sb[k] for k in aars)}/{len(aars)}")
for k in bad:
    print("  NOT DETERMINISTIC:", k)
if bad:
    sys.exit(1)
EOF
  {
    echo "# Arcade embed, built in the DGD clean room"
    echo
    echo "source   puzzle-app $ARCADE $COMMIT ($(git -C "$V1" describe --tags --always))"
    echo "defines  $DEFINES"
    echo "module   $MODULE (fixed; it is compiled into libapp.so)"
    echo "lock     $ARCADE pubspec.lock, enforced; sha256 $(sha256sum "$V1/pubspec.lock" | cut -c1-64)"
    echo "network  cut for this build (packages and Gradle caches filled by an identical earlier build)"
    echo "image    ${DGD_IMAGE:-unknown}"
    sed -n 1,4p $H/flutter-version.txt | sed 's/^/flutter  /'
    echo "java     $(java -version 2>&1 | head -1)"
    echo
    echo "## sha256"
    cd B && find . -type f ! -name '*.md5' ! -name '*.sha1' ! -name '*.sha256' ! -name '*.sha512' | sort | xargs sha256sum | sed 's#  \./#  #'
  } > "$OUT/PROVENANCE.md"
  echo "provenance written"
  ;;
esac
