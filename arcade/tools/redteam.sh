#!/usr/bin/env bash
# DGD Arcade clean-room red-team runner. Policy: ../REDTEAM-POLICY.md
#
# Builds and tests from a PINNED COMMIT in a detached worktree, never from the
# working copy; installs from lockfiles with install scripts disabled; runs
# every suite with the defines it needs; enumerates routes, flags, hosts and
# secret-shaped strings; optionally rebuilds a shipped APK from pristine
# source plus a patch directory and compares it entry by entry.
#
# Exit 0 = pass, 2 = a human must read something, 1 = fail.
#
# Usage:
#   redteam.sh --ref <commit> [--mirror v1|v2|both] [--apk <file>]
#              [--native-zip <zip> --native-patch <dir>] [--out <dir>] [--keep]
#
# Runs in Git Bash on Windows and in bash on Linux/macOS. Needs git, node,
# npm, flutter; aapt2/apksigner if --apk; a JDK 17 or 21 if --native-zip.
set -uo pipefail

# ---------------------------------------------------------------- arguments
REF=""; MIRROR="both"; APK=""; NZIP=""; NPATCH=""; OUT=""; KEEP=0
while [ $# -gt 0 ]; do
  case "$1" in
    --ref) REF="$2"; shift 2 ;;
    --mirror) MIRROR="$2"; shift 2 ;;
    --apk) APK="$(cd "$(dirname "$2")" && pwd)/$(basename "$2")"; shift 2 ;;
    --native-zip) NZIP="$(cd "$(dirname "$2")" && pwd)/$(basename "$2")"; shift 2 ;;
    --native-patch) NPATCH="$(cd "$2" && pwd)"; shift 2 ;;
    --out) OUT="$2"; shift 2 ;;
    --keep) KEEP=1; shift ;;
    -h|--help) sed -n '2,18p' "$0"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 1 ;;
  esac
done
[ -n "$REF" ] || { echo "--ref <commit> is required: the run must be pinned" >&2; exit 1; }
[ -z "$NZIP" ] || [ -n "$NPATCH" ] || { echo "--native-zip needs --native-patch" >&2; exit 1; }

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(git -C "$HERE" rev-parse --show-toplevel)"
HASH="$(git -C "$REPO" rev-parse --verify "${REF}^{commit}")" || { echo "not a commit: $REF" >&2; exit 1; }
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUT="${OUT:-$REPO/arcade/redteam-runs/$STAMP-${HASH:0:7}}"
mkdir -p "$OUT"
REPORT="$OUT/report.md"; ROWS="$OUT/.rows"; SECTIONS="$OUT/.sections"; : > "$ROWS"; : > "$SECTIONS"

# Short scratch path: AAPT2 and Gradle choke on deep Windows paths.
SCRATCH="${REDTEAM_SCRATCH:-${LOCALAPPDATA:-/tmp}/rt-$$}"
SCRATCH="${SCRATCH//\\//}"
mkdir -p "$SCRATCH"
WT="$SCRATCH/wt"

# ---------------------------------------------------------------- reporting
FAILS=0; REVIEWS=0
say()    { printf '%s\n' "$*" | tee -a "$SECTIONS"; }
row()    { printf '| %s | %s | %s |\n' "$1" "$2" "$3" >> "$ROWS"; }
pass()   { row "$1" "PASS" "$2"; echo "PASS  $1 — $2"; }
fail()   { row "$1" "**FAIL**" "$2"; echo "FAIL  $1 — $2"; FAILS=$((FAILS+1)); }
review() { row "$1" "REVIEW" "$2"; echo "REVIEW $1 — $2"; REVIEWS=$((REVIEWS+1)); }
need()   { command -v "$1" >/dev/null 2>&1; }

cleanup() {
  if [ "$KEEP" = 1 ]; then echo "kept: $SCRATCH"; return; fi
  git -C "$REPO" worktree remove --force "$WT" >/dev/null 2>&1 || true
  git -C "$REPO" worktree prune >/dev/null 2>&1 || true
  rm -rf "$SCRATCH"
}
trap cleanup EXIT

# The table of checks comes first, then the enumerations; both are collected
# while the run goes and assembled at the end so the table is never broken.
assemble() {
  {
    echo "# Clean-room red-team run — $STAMP"
    echo
    echo "Commit \`$HASH\` (\`$REF\`). Policy: \`arcade/REDTEAM-POLICY.md\`."
    echo "Worktree is detached at the hash; the working copy is not consulted."
    echo
    echo "| Check | Result | Detail |"
    echo "|---|---|---|"
    cat "$ROWS"
    echo
    cat "$SECTIONS"
  } > "$REPORT"
  rm -f "$ROWS" "$SECTIONS"
}

# ---------------------------------------------------------------- worktree
git -C "$REPO" worktree add --detach "$WT" "$HASH" >/dev/null 2>&1 \
  || { fail "worktree" "could not create detached worktree at $HASH"; exit 1; }
pass "worktree" "detached at ${HASH:0:12}"

# Allowlist of hosts the app's own code may name. Anything else is a finding.
ALLOWED_HOSTS='^(digitalgold\.co|www\.digitalgold\.co|digitalgoldx\.com|explorer\.digitalgoldx\.com|localhost|127\.0\.0\.1|10\.0\.2\.2|0\.0\.0\.0|apps\.apple\.com|play\.google\.com|schemas\.android\.com|www\.w3\.org)$'
hosts_in() { grep -r -h -o -E 'https?://[A-Za-z0-9._-]+' "$@" 2>/dev/null | sed -E 's#https?://##' | sort -u; }
secrets_in() {
  grep -r -n -E -i 'api[_-]?key\s*[:=]|sk_live_[A-Za-z0-9]+|AIza[0-9A-Za-z_-]{30,}|BEGIN (RSA |EC )?PRIVATE KEY|ghp_[A-Za-z0-9]{30,}|xox[abp]-[A-Za-z0-9-]+' "$@" 2>/dev/null \
    | grep -v -E 'redteam\.sh|REDTEAM-POLICY|AUDIT-' || true
}

# ---------------------------------------------------------------- server
run_server() {
  local m="$1"
  local d="$WT/arcade/$m/server" log="$OUT/$m-server.log"
  [ -d "$d" ] || { review "$m server" "no such directory at this commit"; return; }
  ( cd "$d" && npm ci --ignore-scripts --no-audit --no-fund >"$log.install" 2>&1 ) \
    || { fail "$m server install" "npm ci --ignore-scripts failed (see $m-server.log.install)"; return; }
  ( cd "$d" && npm test >"$log" 2>&1 ); local rc=$?
  local t p f todo
  t=$(grep -E '^ℹ tests ' "$log" | awk '{print $3}'); p=$(grep -E '^ℹ pass ' "$log" | awk '{print $3}')
  f=$(grep -E '^ℹ fail ' "$log" | awk '{print $3}'); todo=$(grep -E '^ℹ todo ' "$log" | awk '{print $3}')
  if [ $rc -eq 0 ] && [ "${f:-1}" = 0 ]; then pass "$m server tests" "$t tests: $p pass, $todo todo"; else fail "$m server tests" "exit $rc, ${f:-?} failing (see $m-server.log)"; fi
  # Ledger: which findings are open, accepted, holding.
  {
    echo; echo "### $m server red-team ledger"; echo
    grep -E '^(✔|⚠|✖) (HOLDS|ACCEPTED|OPEN) ' "$log" | sed -E 's/ \([0-9.]+ms\)//; s/^✔/- ✔/; s/^⚠/- ⚠/; s/^✖/- ✖/' | awk '!seen[$0]++'
  } >> "$SECTIONS"
  # Enumeration: routes and flags.
  {
    echo; echo "### $m server routes (from source)"; echo; echo '```'
    grep -r -h -o -E "app\.(get|post|put|patch|delete)\('[^']+'" "$d/src" | sed -E "s/app\.([a-z]+)\('/\U\1 /; s/'$//" | sort -u
    echo '```'; echo; echo "### $m server environment flags"; echo; echo '```'
    grep -r -h -o -E 'process\.env\.[A-Z_]+' "$d/src" | sed 's/process.env.//' | sort -u | tr '\n' ' '; echo
    echo '```'
  } >> "$SECTIONS"
  local unlisted; unlisted=$(hosts_in "$d/src" | grep -v -E "$ALLOWED_HOSTS" || true)
  if [ -z "$unlisted" ]; then pass "$m server hosts" "only allowlisted hosts in src/"; else review "$m server hosts" "unlisted: $(echo "$unlisted" | tr '\n' ' ')"; fi
  local sec; sec=$(secrets_in "$d/src" "$d/data")
  if [ -z "$sec" ]; then pass "$m server secrets" "no secret-shaped strings"; else fail "$m server secrets" "$(echo "$sec" | head -3 | tr '\n' ';')"; fi
  # Lockfile drift against the previous commit is a human read.
  if ! git -C "$WT" diff --quiet "$HASH~1" "$HASH" -- "arcade/$m/server/package-lock.json" 2>/dev/null; then
    review "$m server lockfile" "package-lock.json changed in this commit; read the diff"
  fi
}

# ---------------------------------------------------------------- flutter
free_port() { echo $((18000 + RANDOM % 2000)); }
sum() { grep -o -E '\+[0-9]+( ~[0-9]+)?( -[0-9]+)?: (All tests passed|Some tests failed)' "$1" | tail -1; }
run_flutter() {
  local m="$1"
  local d="$WT/arcade/$m/app" log="$OUT/$m-app.log"
  [ -d "$d" ] || { review "$m app" "no such directory at this commit"; return; }
  ( cd "$d" && flutter pub get --enforce-lockfile >"$log.pubget" 2>&1 ) \
    || { fail "$m app pub get" "lockfile not honoured or resolution failed (see $m-app.log.pubget)"; return; }
  ( cd "$d" && flutter analyze >"$log.analyze" 2>&1 ) \
    && pass "$m app analyze" "no issues" || fail "$m app analyze" "see $m-app.log.analyze"
  local p1 p2 s1 s2 s3
  p1=$(free_port); p2=$(free_port)
  ( cd "$d" && flutter test >"$log.plain" 2>&1 ); s1=$?
  ( cd "$d" && flutter test --dart-define=ARCADE_API=http://127.0.0.1:$p1 >"$log.api" 2>&1 ); s2=$?
  ( cd "$d" && flutter test --dart-define=ARCADE_API=http://127.0.0.1:$p2 --dart-define=DGD_DEMO=true test/arcade_api_test.dart >"$log.demo" 2>&1 ); s3=$?
  [ $s1 -eq 0 ] && pass "$m app tests (plain)" "$(sum "$log.plain")" || fail "$m app tests (plain)" "$(sum "$log.plain")"
  [ $s2 -eq 0 ] && pass "$m app tests (ARCADE_API loopback)" "$(sum "$log.api")" || fail "$m app tests (ARCADE_API loopback)" "$(sum "$log.api")"
  [ $s3 -eq 0 ] && pass "$m app demo zero-request group" "$(sum "$log.demo")" || fail "$m app demo zero-request group" "$(sum "$log.demo")"
  # The network layer must actually have run: the loopback run must pass more cases than the plain one.
  local n1 n2
  n1=$(grep -o -E '\+[0-9]+' "$log.plain" | tail -1 | tr -d +); n2=$(grep -o -E '\+[0-9]+' "$log.api" | tail -1 | tr -d +)
  if [ "${n2:-0}" -gt "${n1:-0}" ]; then pass "$m app network cases ran" "$((n2-n1)) more cases with the define"; else fail "$m app network cases ran" "the loopback define did not add cases; the network suite was skipped"; fi
  {
    echo; echo "### $m app dart-defines read by the code"; echo; echo '```'
    grep -r -h -o -E "fromEnvironment\('[A-Z_]+'" "$d/lib" | sed -E "s/fromEnvironment\('//; s/'//" | sort -u | tr '\n' ' '; echo
    echo '```'
  } >> "$SECTIONS"
  local unlisted; unlisted=$(hosts_in "$d/lib" | grep -v -E "$ALLOWED_HOSTS" || true)
  if [ -z "$unlisted" ]; then pass "$m app hosts" "only allowlisted hosts in lib/"; else review "$m app hosts" "unlisted: $(echo "$unlisted" | tr '\n' ' ')"; fi
  local sec; sec=$(secrets_in "$d/lib" "$d/android/app/src" 2>/dev/null)
  if [ -z "$sec" ]; then pass "$m app secrets" "no secret-shaped strings"; else fail "$m app secrets" "$(echo "$sec" | head -3 | tr '\n' ';')"; fi
}

# ---------------------------------------------------------------- apk
sdk_tool() { # sdk_tool aapt2|apksigner
  local sdk="${ANDROID_SDK_ROOT:-${ANDROID_HOME:-${LOCALAPPDATA:-}/Android/Sdk}}"; sdk="${sdk//\\//}"
  local bt; bt=$(ls -d "$sdk"/build-tools/*/ 2>/dev/null | sort -V | tail -1)
  for c in "$bt$1" "$bt$1.exe" "$bt$1.bat"; do [ -x "$c" ] && { echo "$c"; return; }; done
  need "$1" && command -v "$1"
}
inspect_apk() {
  local apk="$1"
  local x="$SCRATCH/apk-shipped" aapt apks
  [ -f "$apk" ] || { fail "apk" "not found: $apk"; return; }
  mkdir -p "$x" && ( cd "$x" && unzip -o -q "$apk" ) || { fail "apk" "unzip failed"; return; }
  say ""; say "### Shipped APK: \`$(basename "$apk")\`"; say ""
  say "sha256 \`$(sha256sum "$apk" | cut -d' ' -f1)\`"
  aapt=$(sdk_tool aapt2); apks=$(sdk_tool apksigner)
  if [ -n "$aapt" ]; then
    local badge; badge=$("$aapt" dump badging "$apk" 2>/dev/null)
    { echo; echo '```'; echo "$badge" | grep -E "^package:|^sdkVersion|^targetSdkVersion|^uses-permission" ; echo '```'; } >> "$SECTIONS"
    if "$aapt" dump xmltree "$apk" --file AndroidManifest.xml 2>/dev/null | grep -q 'debuggable(0x0101000f)=true'; then
      review "apk debuggable" "android:debuggable=true — a test build, not for distribution"
    else pass "apk debuggable" "not debuggable"; fi
    local exported; exported=$("$aapt" dump xmltree "$apk" --file AndroidManifest.xml 2>/dev/null | awk '/E: (activity|receiver|service|provider)/{c=$0} /:name\(.*\)=/{n=$0} /exported\(0x01010010\)=true/{print n}' | grep -o -E 'Raw: "[^"]+"' | sort -u | tr '\n' ' ')
    { echo; echo "Exported components: $exported"; } >> "$SECTIONS"
  else review "apk badging" "aapt2 not found; manifest not inspected"; fi
  if [ -n "$apks" ]; then
    local dn; dn=$("$apks" verify --print-certs "$apk" 2>/dev/null | grep -m1 'certificate DN' | sed 's/.*DN: //')
    case "$dn" in *"Android Debug"*) review "apk signer" "debug certificate ($dn)";; "") fail "apk signer" "signature did not verify";; *) pass "apk signer" "$dn";; esac
  fi
  # Hosts and secrets in the APP's OWN dex only (library dex is noise).
  local own=(); for f in "$x"/classes*.dex; do grep -a -q -E 'Lco/digitalgold/|Lcom/digitalgold/' "$f" && own+=("$f"); done
  local unlisted; unlisted=$(grep -a -h -o -E 'https?://[A-Za-z0-9._-]+' "${own[@]}" 2>/dev/null | sed -E 's#https?://##' | sort -u | grep -v -E "$ALLOWED_HOSTS" || true)
  if [ -z "$unlisted" ]; then pass "apk hosts" "only allowlisted hosts in the app's dex (${#own[@]} files)"; else fail "apk hosts" "unlisted: $(echo "$unlisted" | tr '\n' ' ')"; fi
  local sec; sec=$(grep -a -h -o -E -i 'sk_live_[A-Za-z0-9]+|AIza[0-9A-Za-z_-]{30,}|BEGIN (RSA |EC )?PRIVATE KEY|ghp_[A-Za-z0-9]{30,}' "${own[@]}" 2>/dev/null | sort -u || true)
  if [ -z "$sec" ]; then pass "apk secrets" "none in the app's dex"; else fail "apk secrets" "$(echo "$sec" | head -3 | tr '\n' ';')"; fi
  if [ -d "$x/lib" ]; then review "apk native libs" "$(find "$x/lib" -type f | sed 's#.*/lib/##' | sort -u | tr '\n' ' ')"; fi
}

# ---------------------------------------------------------------- native clean room
native_cleanroom() {
  local zip="$1" patch="$2" apk="$3"
  local cr="$SCRATCH/native" gh="$SCRATCH/gh"
  mkdir -p "$cr" "$gh" && ( cd "$cr" && unzip -o -q "$zip" ) || { fail "native unzip" "$zip"; return; }
  local android; android=$(find "$cr" -maxdepth 3 -type d -name android | head -1)
  [ -n "$android" ] && [ -f "$android/gradlew" ] || { fail "native" "no android/ with gradlew inside the zip"; return; }
  say ""; say "### Native clean room"; say ""
  say "zip sha256 \`$(sha256sum "$zip" | cut -d' ' -f1)\`, patch dir \`$patch\`"
  # Apply the patch: every file in the patch dir replaces its namesake under app/src. Report exactly what changed.
  local applied=0 f target
  while IFS= read -r f; do
    target=$(find "$android/app/src" -name "$(basename "$f")" | head -1)
    [ -n "$target" ] || { fail "native patch" "no target for $(basename "$f")"; continue; }
    cp "$f" "$target"; applied=$((applied+1))
  done < <(find "$patch" -maxdepth 1 -type f -name '*.kt' -o -maxdepth 1 -type f -name '*.java' -o -maxdepth 1 -type f -name '*.xml')
  pass "native patch" "$applied source files applied"
  { echo; echo '```'; ( cd "$cr" && find . -type f -newer "$zip" -name '*.kt' | sed 's#^\./##' ); echo '```'; } >> "$SECTIONS"
  local sdk="${ANDROID_SDK_ROOT:-${ANDROID_HOME:-${LOCALAPPDATA:-}/Android/Sdk}}"; sdk="${sdk//\\//}"
  echo "sdk.dir=$sdk" > "$android/local.properties"
  local jh="${JAVA_HOME_21:-${JAVA_HOME:-}}"
  local log="$OUT/native-build.log"
  ( cd "$android" && GRADLE_USER_HOME="$gh" JAVA_HOME="$jh" ./gradlew --no-daemon --no-build-cache test assembleDebug >"$log" 2>&1 ) \
    || { fail "native build" "gradle failed (see native-build.log); JDK 17/21 required, set JAVA_HOME_21"; return; }
  local total=0 failed=0 x
  for x in "$android"/app/build/test-results/testDebugUnitTest/*.xml; do
    total=$((total + $(grep -o -E 'tests="[0-9]+"' "$x" | head -1 | tr -dc 0-9)))
    failed=$((failed + $(grep -o -E 'failures="[0-9]+"' "$x" | head -1 | tr -dc 0-9) + $(grep -o -E 'errors="[0-9]+"' "$x" | head -1 | tr -dc 0-9)))
  done
  [ "$failed" = 0 ] && pass "native unit tests" "$total tests, 0 failures" || fail "native unit tests" "$failed of $total failed"
  local built; built=$(ls "$android"/app/build/outputs/apk/debug/*.apk 2>/dev/null | head -1)
  [ -n "$built" ] || { fail "native apk" "no APK produced"; return; }
  [ -n "$apk" ] || { review "native apk" "built $(basename "$built"), nothing to compare against (pass --apk)"; return; }
  local a="$SCRATCH/apk-built" b="$SCRATCH/apk-shipped"; mkdir -p "$a" "$b"
  ( cd "$a" && unzip -o -q "$built" ); ( cd "$b" && unzip -o -q "$apk" )
  local same=0 diffcode=() diffres=() e
  while IFS= read -r e; do
    if cmp -s "$b/$e" "$a/$e"; then same=$((same+1))
    else case "$e" in classes*.dex) diffcode+=("$e");; *) diffres+=("$e");; esac; fi
  done < <(cd "$b" && find . -type f \( -name 'classes*.dex' -o -name 'AndroidManifest.xml' -o -name 'resources.arsc' -o -path './assets/*' -o -path './res/*' -o -path './lib/*' \) | sed 's#^\./##')
  # Where a dex differs, is it only D8's incremental checksum map line (no bytecode)?
  local maponly=() realdiff=() n mapl
  for e in "${diffcode[@]}"; do
    n=$(diff <(grep -a -o -E '[[:print:]]{6,}' "$b/$e" | sort -u) <(grep -a -o -E '[[:print:]]{6,}' "$a/$e" | sort -u) | grep -c -E '^[<>]')
    mapl=$(diff <(grep -a -o -E '[[:print:]]{6,}' "$b/$e" | sort -u) <(grep -a -o -E '[[:print:]]{6,}' "$a/$e" | sort -u) | grep -c -E '^[<>] ~~~\{')
    if [ "$n" = "$mapl" ] && [ "$n" -gt 0 ]; then maponly+=("$e"); else realdiff+=("$e ($n strings)"); fi
  done
  if [ ${#diffres[@]} -gt 0 ]; then fail "native reproducibility" "manifest/resources/assets differ: ${diffres[*]}"
  elif [ ${#realdiff[@]} -gt 0 ]; then review "native reproducibility" "$same entries identical; bytecode differs in ${realdiff[*]} — read the strings"
  elif [ ${#maponly[@]} -gt 0 ]; then pass "native reproducibility" "$same entries byte-identical; ${maponly[*]} differ only in D8's incremental checksum map (no bytecode difference)"
  else pass "native reproducibility" "$same entries byte-identical to the shipped APK"; fi
}

# ---------------------------------------------------------------- run
case "$MIRROR" in
  v1|v2) run_server "$MIRROR"; run_flutter "$MIRROR" ;;
  both) run_server v1; run_flutter v1; run_server v2; run_flutter v2 ;;
  none) ;;
  *) echo "--mirror must be v1, v2, both or none" >&2; exit 1 ;;
esac
[ -z "$APK" ] || inspect_apk "$APK"
[ -z "$NZIP" ] || native_cleanroom "$NZIP" "$NPATCH" "$APK"

# ---------------------------------------------------------------- verdict
assemble
say() { printf '%s\n' "$*" | tee -a "$REPORT"; }
say ""
if [ $FAILS -gt 0 ]; then say "**Verdict: FAIL** — $FAILS failing check(s), $REVIEWS to review. Report: $REPORT"; exit 1
elif [ $REVIEWS -gt 0 ]; then say "**Verdict: REVIEW** — $REVIEWS item(s) need a human read. Report: $REPORT"; exit 2
else say "**Verdict: PASS**. Report: $REPORT"; exit 0; fi
