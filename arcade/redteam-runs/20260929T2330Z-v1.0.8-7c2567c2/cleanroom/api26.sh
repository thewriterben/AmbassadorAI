#!/usr/bin/env bash
# DGD 1.0.8 on Android 8.0 (API 26, the minSdk): the old-Android crash class
# (API-33 methods), Flutter on an old GPU stack, backup rules (API 26 reads
# fullBackupContent, not dataExtractionRules), encrypted prefs on an old Keystore.
# Offline, localhost -> impostor. Usage: api26.sh <apk> <outdir>
APK="$1"; OUT="$2"; mkdir -p "$OUT"
ADB="$LOCALAPPDATA/Android/Sdk/platform-tools/adb.exe -e"; C="$LOCALAPPDATA/Temp/rt108"; PKG=com.digitalgold.ticker; D=/data/data/$PKG
export MSYS_NO_PATHCONV=1
dump() { $ADB shell "uiautomator dump /sdcard/u.xml >/dev/null 2>&1; cat /sdcard/u.xml"; }
center() { echo "$1" | grep -o -E 'bounds="\[[0-9]+,[0-9]+\]\[[0-9]+,[0-9]+\]"' | head -1 | grep -o -E '[0-9]+' | tr '\n' ' ' | awk '{print int(($1+$3)/2), int(($2+$4)/2)}'; }
tap() { local c; c=$(center "$(dump | grep -o -E "(text|content-desc)=\"$1\"[^>]*bounds=\"[^\"]+\"" | head -1)"); [ -n "$c" ] && { $ADB shell input tap $c; echo "  tapped '$1'"; } || echo "  !! not found: $1"; }
crashes() { $ADB logcat -d | grep -E "FATAL EXCEPTION|NoSuchMethodError|NoClassDefFoundError|UnsatisfiedLinkError|VerifyError" | grep -c -v "^\s*$"; }
fg() { $ADB shell 'dumpsys activity activities | grep -E "mResumedActivity|topResumedActivity"' | grep -o -E '[a-z][a-z0-9_.]+/[^ }]+' | head -1; }
launch() { $ADB shell am force-stop $PKG; $ADB shell am start -W -n $PKG/.MainActivity >/dev/null; sleep 6; }
texts() { dump | grep -o -E '(text|content-desc)="[^"]{1,160}"' | sort -u; }
field() { center "$(dump | grep -o -E '<node[^>]*class="android.widget.EditText"[^>]*>' | sed -n "$1p")"; }

echo "== device: API $($ADB shell getprop ro.build.version.sdk | tr -d '\r'), Android $($ADB shell getprop ro.build.version.release | tr -d '\r'), root=$($ADB shell id -u | tr -d '\r')"
echo "== install"; $ADB install "$APK" 2>&1 | tail -1; $ADB reverse tcp:8787 tcp:18788 >/dev/null; : > "$C/impostor.log"; $ADB logcat -c
echo; echo "== 1. cold start"; $ADB shell am start -W -n $PKG/.MainActivity | grep -E "Status|TotalTime"; sleep 8; $ADB exec-out screencap -p > "$OUT/api26-1-home.png"; echo "  home: $(texts | grep -E 'text="(Arcade|Log in|Stats unavailable|LIVE)"' | tr '\n' ' ')  crashes: $(crashes)"
echo; echo "== 2. arcade in the app (Flutter on API 26)"; tap Arcade; sleep 3; tap "Play in the app"; sleep 10; $ADB exec-out screencap -p > "$OUT/api26-2-arcade.png"; echo "  fg: $(fg)  arcade: $(texts | grep -E 'DGD Arcade|Coin Quest' | head -2 | tr '\n' ' ')  crashes: $(crashes)"
tap "MATCH-3[^\"]*"; sleep 6; $ADB exec-out screencap -p > "$OUT/api26-2-levelmap.png"; echo "  level map: $(texts | grep -E 'Coin Quest|/180' | head -2 | tr '\n' ' ')  crashes: $(crashes)"
for i in 1 2 3; do $ADB shell input keyevent BACK; sleep 2; done; echo "  impostor requests: $(wc -l < "$C/impostor.log")"
echo; echo "== 3. web arcade link"; launch; $ADB logcat -c; tap Arcade; sleep 2; tap "Play in your browser"; sleep 4; echo "  fg: $(fg)  crashes: $(crashes)"; $ADB logcat -d | grep -o -E "START u0 \{act=android.intent.action.VIEW[^}]*\}" | head -1 | sed 's/^/  /'
echo; echo "== 4. signup preview through to Invite Friends (the URLEncoder crash area)"; launch; $ADB logcat -c; tap "Log in"; sleep 3
for i in 1 2; do c=$(field $i); [ -n "$c" ] && { $ADB shell input tap $c; sleep 1; case $i in 1) t="api26@example.edu";; 2) t="Api26Secret!";; esac; $ADB shell input text "$t"; sleep 1; $ADB shell input keyevent BACK; sleep 1; }; done; tap Continue; sleep 3
echo "  at rest after login:"; $ADB shell "for f in $D/shared_prefs/*.xml; do echo \"    \$(basename \$f): \$(grep -o -E 'name=\"[^\"]+\"' \$f | sed 's/name=//' | tr '\n' ' ')\"; done"; echo "  plaintext typed values: $($ADB shell "grep -rl -E 'api26@example|Api26Secret' $D 2>/dev/null | wc -l" | tr -d '\r')  crashes: $(crashes)"
echo; echo "== 5. backup on API 26 (fullBackupContent rules)"; $ADB shell "bmgr enable true; bmgr transport android/com.android.internal.backup.LocalTransport >/dev/null 2>&1; bmgr list transports" | tr -d '\r' | sed 's/^/  transports: /' | head -3
$ADB shell "bmgr fullbackup $PKG" 2>&1 | tr -d '\r' | tail -1 | sed 's/^/  /'; sleep 5; F=$($ADB shell "ls /data/cache/backup/*/_full/ /cache/backup/*/_full/ 2>/dev/null" | tr -d '\r' | grep -m1 $PKG); P=$($ADB shell "ls -d /data/cache/backup/*/_full/$PKG /cache/backup/*/_full/$PKG 2>/dev/null" | tr -d '\r' | head -1); echo "  backup file: ${P:-none}"
[ -n "$P" ] && { $ADB pull "$P" "$OUT/api26-backup.tar" >/dev/null 2>&1; python -c "import tarfile;print('  entries:', ' '.join(m.name.replace('apps/$PKG/','') for m in tarfile.open(r'$(cygpath -w "$OUT/api26-backup.tar")').getmembers()))" 2>&1; }
echo; echo "== totals: crashes $(crashes), impostor requests $(wc -l < "$C/impostor.log")"; $ADB logcat -d > "$OUT/api26-logcat.txt"; $ADB reverse --remove-all
