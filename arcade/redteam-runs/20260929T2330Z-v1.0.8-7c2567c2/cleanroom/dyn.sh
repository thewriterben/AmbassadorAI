#!/usr/bin/env bash
# DGD 1.0.8 dynamic red-team, offline phase. Emulator already booted (rooted, network off),
# localhost:8787 -> impostor on the host. Usage: dyn.sh <apk> <outdir> <label>
APK="$1"; OUT="$2"; TAG="$3"; mkdir -p "$OUT"
ADB="$LOCALAPPDATA/Android/Sdk/platform-tools/adb.exe -e"; S="$LOCALAPPDATA/Temp/rt108"; PKG=com.digitalgold.ticker; D=/data/data/$PKG
export MSYS_NO_PATHCONV=1
dump() { $ADB shell "uiautomator dump /sdcard/u.xml >/dev/null 2>&1; cat /sdcard/u.xml"; }
center() { echo "$1" | grep -o -E 'bounds="\[[0-9]+,[0-9]+\]\[[0-9]+,[0-9]+\]"' | head -1 | grep -o -E '[0-9]+' | tr '\n' ' ' | awk '{print int(($1+$3)/2), int(($2+$4)/2)}'; }
tap() { local c; c=$(center "$(dump | grep -o -E "(text|content-desc)=\"$1\"[^>]*bounds=\"[^\"]+\"" | head -1)"); [ -n "$c" ] && { $ADB shell input tap $c; echo "  tapped '$1'"; } || echo "  !! not found: $1"; }
crashes() { $ADB logcat -d | grep -c -E "FATAL EXCEPTION|AndroidRuntime: Process: $PKG|NoSuchMethodError|NoClassDefFoundError|UnsatisfiedLinkError"; }
fg() { $ADB shell 'dumpsys activity activities | grep -E "topResumedActivity|mResumedActivity"' | grep -o -E '[a-z][a-z0-9_.]+/[^ }]+' | head -1; }
reqs() { wc -l < "$S/impostor.log"; }
prefs() { $ADB shell "ls $D/shared_prefs/ 2>/dev/null; for f in $D/shared_prefs/*.xml; do echo \"  \$f: \$(grep -o -E 'name=\"[^\"]+\"' \$f | tr '\n' ' ')\"; done" 2>/dev/null; }
texts() { dump | grep -o -E '(text|content-desc)="[^"]{1,120}"' | sort -u; }

echo "== device: API $($ADB shell getprop ro.build.version.sdk | tr -d '\r'), Android $($ADB shell getprop ro.build.version.release | tr -d '\r'), root=$($ADB shell id -u | tr -d '\r'), net=$($ADB shell "dumpsys connectivity | grep -E '^Active default network'" | tr -d '\r')"
echo "== install"; $ADB install "$APK" 2>&1 | tail -1; $ADB shell dumpsys package $PKG | grep -o -E "versionCode=[0-9]+ minSdk=[0-9]+ targetSdk=[0-9]+|versionName=[^ ]+|flags=\[[^]]*\]" | head -3 | tr '\n' ' '; echo
$ADB reverse tcp:8787 tcp:18788 >/dev/null; : > "$S/impostor.log"; $ADB logcat -c

echo; echo "== 1. cold start, arcade never opened"; $ADB shell am start -W -n $PKG/.MainActivity | grep -E "Status|TotalTime"; sleep 8; echo "  requests: $(reqs)  crashes: $(crashes)"; $ADB exec-out screencap -p > "$OUT/$TAG-1-home.png"
echo "  home: $(texts | grep -E 'text="(Arcade|Log in|Stats|Stats unavailable|Get Digital Gold|LIVE)"' | tr '\n' ' ')"

echo; echo "== 2. Arcade menu (1.0.7) -> play in the app -> Coin Quest -> level 1 -> board, swaps, out"; tap Arcade; sleep 3; echo "  menu: $(texts | grep -i -E 'arcade|web|browser|play' | head -6 | tr '\n' ' ')"; $ADB exec-out screencap -p > "$OUT/$TAG-2-arcade-menu.png"
M=$(dump | grep -o -E '(text|content-desc)="[^"]*(in the app|Play in|Open in the app|Play here)[^"]*"[^>]*bounds="[^"]+"' | head -1); [ -n "$M" ] && { $ADB shell input tap $(center "$M"); echo "  tapped in-app"; } || tap "Coin Quest[^\"]*"; sleep 8
echo "  arcade: $(texts | grep -E 'DGD Arcade|OFFLINE|Educational|Coin Quest' | head -4 | tr '\n' ' ')  fg: $(fg)"; $ADB exec-out screencap -p > "$OUT/$TAG-2-arcade.png"
tap "MATCH-3[^\"]*"; sleep 5; $ADB shell input tap 778 2088; sleep 3; tap Play; sleep 7; tap "Got it"; sleep 2; $ADB shell input swipe 300 1300 420 1300 200; sleep 2; $ADB shell input swipe 540 1500 540 1620 200; sleep 2; $ADB exec-out screencap -p > "$OUT/$TAG-2-board.png"
echo "  audio tracks while on the board: $($ADB shell dumpsys media.audio_flinger 2>/dev/null | grep -c -E '^\s+[0-9]+\s+yes|Track' )"
for i in 1 2 3 4; do $ADB shell input keyevent BACK; sleep 2; done; echo "  back on ticker: $(texts | grep -c 'text="Arcade"')  requests: $(reqs)  crashes: $(crashes)"
echo "  arcade prefs at rest:"; $ADB shell "cat $D/shared_prefs/FlutterSharedPreferences.xml 2>/dev/null" | grep -o -E 'name="[^"]+"' | tr '\n' ' '; echo

echo; echo "== 3. web arcade link (1.0.7): what intent leaves the app"; $ADB logcat -c; tap Arcade; sleep 3; W=$(dump | grep -o -E '(text|content-desc)="[^"]*(Web|web|browser)[^"]*"[^>]*bounds="[^"]+"' | head -1); [ -n "$W" ] && { $ADB shell input tap $(center "$W"); sleep 4; } || echo "  !! no web entry"
echo "  START intents from the app: $($ADB logcat -d | grep -o -E 'START u0 \{act=android.intent.action.VIEW[^}]*\}' | head -2)"; echo "  fg now: $(fg)"; $ADB shell am force-stop com.android.chrome 2>/dev/null; $ADB shell am start -W -n $PKG/.MainActivity >/dev/null; sleep 3

echo; echo "== 4. referral injection and hostile intents, delivered to the activity by component"
$ADB logcat -c
for d in "https://digitalgold.co/app?ref=injected_friend" "https://www.digitalgold.co/app?ref=%3Cscript%3E" "https://digitalgold.co/signup?ref=$(printf 'R%.0s' $(seq 1 300))" "javascript:alert(1)" "file:///data/data/$PKG/shared_prefs/dgd.signup.xml" "intent://x#Intent;scheme=https;package=com.android.chrome;end" "content://com.android.contacts/contacts" "https://digitalgold.co/app/%00%00?ref=a%00b" "https://digitalgold.co/app/$(printf 'B%.0s' $(seq 1 4000))"; do
  $ADB shell "am start -n $PKG/.MainActivity -a android.intent.action.VIEW -d '$d'" >/dev/null 2>&1; sleep 2; done
$ADB shell "am start -n $PKG/.MainActivity --es android.intent.extra.TEXT \"\$(printf 'X%.0s' \$(seq 1 20000))\" --ei junk 7 --ez flag true" >/dev/null 2>&1; sleep 2
echo "  crashes: $(crashes)  fg: $(fg)"; echo "  any friendCode stored?: $($ADB shell "grep -c friendCode $D/shared_prefs/*.xml 2>/dev/null" | tr '\n' ' ')"
echo "  resolves digitalgold.co/app to this app?: $($ADB shell "cmd package query-activities -a android.intent.action.VIEW -d https://digitalgold.co/app?ref=x" 2>/dev/null | grep -c $PKG)"

echo; echo "== 5. legacy key deletion: seed dgd.friendCode, relaunch"; $ADB shell am force-stop $PKG; $ADB shell "grep -q '<map' $D/shared_prefs/dgd.signup.xml 2>/dev/null && sed -i 's#</map>#    <string name=\"dgd.friendCode\">seeded_legacy</string>\n</map>#' $D/shared_prefs/dgd.signup.xml || printf '<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\" ?>\n<map>\n    <string name=\"dgd.friendCode\">seeded_legacy</string>\n</map>\n' > $D/shared_prefs/dgd.signup.xml; chown \$(stat -c %u $D) $D/shared_prefs/dgd.signup.xml; chmod 660 $D/shared_prefs/dgd.signup.xml; grep -c friendCode $D/shared_prefs/dgd.signup.xml"
$ADB shell am start -W -n $PKG/.MainActivity >/dev/null; sleep 5; tap "Get Digital Gold"; sleep 3; $ADB shell input keyevent BACK; sleep 2; echo "  friendCode after relaunch + opening signup: $($ADB shell "grep -c friendCode $D/shared_prefs/dgd.signup.xml" | tr -d '\r')"

echo; echo "== 6. log in: at rest, logcat, FLAG_SECURE"; $ADB logcat -c; tap "Log in"; sleep 3
E=$(dump | grep -o -E '<node[^>]*class="android.widget.EditText"[^>]*>' | grep -o -E 'bounds="\[[0-9]+,[0-9]+\]\[[0-9]+,[0-9]+\]"'); i=0; for b in $E; do c=$(center "$b"); i=$((i+1)); case $i in 1) t="rt108@example.edu";; 2) t="Rt108Secret!";; *) continue;; esac; $ADB shell input tap $c; sleep 1; $ADB shell input text "$t"; sleep 1; $ADB shell input keyevent BACK; sleep 1; done
echo "  FLAG_SECURE on the app window: $($ADB shell 'dumpsys window windows' | grep -B2 -A25 "$PKG" | grep -c SECURE)"; $ADB exec-out screencap -p > "$OUT/$TAG-6-login.png"; tap Continue; sleep 3
echo "  at rest:"; prefs; echo "  plaintext of typed values anywhere in app storage: $($ADB shell "grep -rl -E 'rt108@example|Rt108Secret' $D 2>/dev/null | wc -l" | tr -d '\r')"; echo "  typed values in logcat: $($ADB logcat -d | grep -c -E 'rt108@example|Rt108Secret')"
echo "  file modes:"; $ADB shell "ls -ln $D/shared_prefs/" | awk 'NR>1{print "   ", $1, $NF}'

echo; echo "== 7. process death with the login sheet open"; tap "Log in"; sleep 2; c=$(center "$(dump | grep -o -E '<node[^>]*class="android.widget.EditText"[^>]*>' | head -1)"); $ADB shell input tap $c; $ADB shell input text "halftyped"; $ADB shell input keyevent BACK; sleep 1; $ADB shell input keyevent HOME; sleep 2; $ADB shell am kill $PKG; sleep 2; $ADB shell am start -W -n $PKG/.MainActivity >/dev/null; sleep 5; echo "  restored half-typed text: $(texts | grep -c halftyped)  crashes: $(crashes)"

echo; echo "== 8. Invite Friends share (the API 33 crash area on old Android)"; $ADB logcat -c; tap "Get Digital Gold"; sleep 3; for s in 1 2 3; do $ADB shell input swipe 540 2000 540 800 300; sleep 1; done
echo "  signup texts: $(texts | grep -i -E 'invite|share|screenshot|QR|friend|email|mail' | head -6 | tr '\n' ' ')"; echo "  crashes: $(crashes)"; $ADB shell input keyevent BACK; sleep 1

echo; echo "== 9. backup through the local transport"; $ADB shell "bmgr enable true; bmgr transport com.android.localtransport/.LocalTransport >/dev/null; bmgr backupnow $PKG" 2>&1 | grep -i "Backup finished" | head -1
F=$($ADB shell "ls /data/data/com.android.localtransport/files/1/_full/ 2>/dev/null" | tr -d '\r' | grep $PKG); if [ -n "$F" ]; then $ADB pull "/data/data/com.android.localtransport/files/1/_full/$F" "$OUT/$TAG-backup.tar" >/dev/null 2>&1; echo "  entries: $(python -c "import tarfile;print(' '.join(m.name.replace('apps/$PKG/','') for m in tarfile.open(r'$(cygpath -w "$OUT/$TAG-backup.tar")').getmembers()))")"; else echo "  (no full-backup file)"; fi
echo; echo "== totals: crashes $(crashes), impostor requests $(reqs)"; $ADB logcat -d > "$OUT/$TAG-logcat.txt"; $ADB reverse --remove-all
