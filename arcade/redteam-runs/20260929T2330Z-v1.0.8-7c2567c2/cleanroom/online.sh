#!/usr/bin/env bash
# DGD 1.0.8 online phase: network on through the logging proxy. Usage: online.sh <apk> <outdir>
APK="$1"; OUT="$2"; mkdir -p "$OUT"
ADB="$LOCALAPPDATA/Android/Sdk/platform-tools/adb.exe -e"; C="$LOCALAPPDATA/Temp/rt108"; PKG=com.digitalgold.ticker; D=/data/data/$PKG
export MSYS_NO_PATHCONV=1
dump() { $ADB shell "uiautomator dump /sdcard/u.xml >/dev/null 2>&1; cat /sdcard/u.xml"; }
center() { echo "$1" | grep -o -E 'bounds="\[[0-9]+,[0-9]+\]\[[0-9]+,[0-9]+\]"' | head -1 | grep -o -E '[0-9]+' | tr '\n' ' ' | awk '{print int(($1+$3)/2), int(($2+$4)/2)}'; }
tap() { local c; c=$(center "$(dump | grep -o -E "(text|content-desc)=\"$1\"[^>]*bounds=\"[^\"]+\"" | head -1)"); [ -n "$c" ] && { $ADB shell input tap $c; echo "  tapped '$1'"; } || echo "  !! not found: $1"; }
crashes() { $ADB logcat -d | grep -c -E "FATAL EXCEPTION|AndroidRuntime: Process: $PKG|NoSuchMethodError"; }
launch() { $ADB shell am force-stop $PKG; $ADB shell am start -W -n $PKG/.MainActivity >/dev/null; sleep 6; dismiss; }
texts() { dump | grep -o -E '(text|content-desc)="[^"]{1,160}"' | sort -u; }
appegress() { grep -v -E "gstatic|googleapis|google\.com|googleusercontent|gvt[0-9]|142\.25[0-9]|172\.217|216\.239|192\.178|2001:4860|2607:f8b0|34\.104|:5228|ERROR" "$C/egress.log"; }
uid() { $ADB shell "dumpsys package $PKG" | grep -o -E "(userId|appId)=[0-9]+" | head -1 | cut -d= -f2 | tr -d '
'; }
appsockets() { $ADB shell "cat /proc/net/tcp /proc/net/tcp6" | awk -v u="$1" '$8==u && $4=="01" {print $3}' | sort -u; }

echo "== net: $($ADB shell "dumpsys connectivity | grep -E '^Active default network'" | tr -d '\r')"
echo "== install"; $ADB install "$APK" 2>&1 | tail -1; U=$(uid); echo "  app uid: $U"
# dismiss any system ANR dialog, then sample every socket the app's uid holds, once a second, on the device
dismiss() { local w; w=$(dump | grep -o -E 'text="Wait"[^>]*bounds="[^"]+"' | head -1); [ -n "$w" ] && { $ADB shell input tap $(center "$w"); echo "  (dismissed a system ANR dialog)"; sleep 2; }; }
$ADB push "$C/sampler.sh" /data/local/tmp/sampler.sh >/dev/null; $ADB shell "chmod 755 /data/local/tmp/sampler.sh; rm -f /data/local/tmp/socks.txt; nohup /data/local/tmp/sampler.sh $U >/dev/null 2>&1 &"
: > "$C/egress.log"; $ADB logcat -c
echo; echo "== 1. cold start online"; launch; sleep 6; echo "  home: $(texts | grep -E 'text="(LIVE|Stats unavailable|Get Digital Gold|Arcade|Log in)"|content-desc="Price[^"]*"' | tr '\n' ' ')"; echo "  app sockets now: $(appsockets $U | tr '\n' ' ')"
echo "  app egress so far:"; appegress | sed 's/^/    /'
echo; echo "== 2. Stats panel"; tap Stats; sleep 3; $ADB exec-out screencap -p > "$OUT/online-stats.png"; echo "  $(texts | grep -E 'Live figures|LIVE ·|Illustrative|7D|Network Growth' | tr '\n' ' ')"; $ADB shell input keyevent BACK; sleep 1
echo; echo "== 3. signup preview: credentials, verification, wallet, receive (Invite Friends)"; launch; L0=$(wc -l < "$C/egress.log"); tap "Get Digital Gold"; sleep 4
E=$(dump | grep -o -E '<node[^>]*class="android.widget.EditText"[^>]*>' | grep -o -E 'bounds="\[[0-9]+,[0-9]+\]\[[0-9]+,[0-9]+\]"' | head -3); i=0; for b in $E; do c=$(center "$b"); i=$((i+1)); case $i in 1) t="rt108user";; 2) t="rt108@example.edu";; 3) t="Rt108Secret!";; esac; $ADB shell input tap $c; sleep 1; $ADB shell input text "$t"; sleep 1; $ADB shell input keyevent BACK; sleep 1; done
echo "  step 1 texts: $(texts | grep -i -E 'friend|invite code|3\+ characters|Learn more' | tr '\n' ' ')"
$ADB shell input swipe 540 2100 540 1000 400; sleep 2; tap Continue; sleep 3; echo "  verify step: $(texts | grep -E 'Verify your email|In the live app' | tr '\n' ' ')"
c=$(center "$(dump | grep -o -E '<node[^>]*class="android.widget.EditText"[^>]*>' | head -1)"); $ADB shell input tap $c; sleep 1; $ADB shell input text "000000"; sleep 1
# Verify sits under the keyboard; hide the keyboard with a tap on the sheet's header text, then tap Verify
H=$(dump | grep -o -E 'text="Verify your email"[^>]*bounds="[^"]+"' | head -1); [ -n "$H" ] && $ADB shell input tap $(center "$H"); sleep 2; tap Verify; sleep 3
echo "  now: $(texts | grep -E 'text="(2 Wallet|3 Receive)"|Download|desktop|QT|Windows|Invite|screenshot|QR' | head -8 | tr '\n' ' ')"; $ADB exec-out screencap -p > "$OUT/online-wallet.png"
tap Continue; sleep 3; $ADB exec-out screencap -p > "$OUT/online-receive.png"; echo "  receive: $(texts | grep -i -E 'invite|screenshot|QR|share|friend|Finish|Welcome|text it' | head -10 | tr '\n' ' ')"
echo "  crashes: $(crashes)"; echo "  app egress during the signup walk:"; tail -n +$((L0+1)) "$C/egress.log" | grep -v -E "gstatic|googleapis|google\.com|googleusercontent|gvt[0-9]|142\.25[0-9]|172\.217|216\.239|192\.178|2001:4860|2607:f8b0|34\.104|:5228|ERROR" | sed 's/^/    /'
echo; echo "== 4. share: the text that would leave the app"; $ADB logcat -c; S=$(dump | grep -o -E '(text|content-desc)="[^"]*(Share|share|Email|email|Text)[^"]*"[^>]*bounds="[^"]+"' | head -1); echo "  share control: $(echo "$S" | grep -o -E '(text|content-desc)="[^"]+"' | head -1)"; [ -n "$S" ] && { $ADB shell input tap $(center "$S"); sleep 3; }
echo "  intents: $($ADB logcat -d -s ActivityTaskManager | grep -o -E 'START u0 \{[^}]*\}' | grep -v "cmp=$PKG/.MainActivity" | head -2)"; $ADB exec-out screencap -p > "$OUT/online-share.png"; $ADB shell input keyevent BACK; sleep 1
echo; echo "== 5. web arcade: the URL handed to the browser"; launch; $ADB logcat -c; tap Arcade; sleep 2; tap "Play in your browser"; sleep 5; echo "  START: $($ADB logcat -d -s ActivityTaskManager | grep -o -E 'START u0 \{[^}]*(VIEW|chrome)[^}]*\}' | head -1)"; echo "  browser egress (browser uid, not the app):"; tail -5 "$C/egress.log" | sed 's/^/    /'; $ADB shell am force-stop com.android.chrome
echo; echo "== 6. at rest after the whole walk"; $ADB shell "for f in $D/shared_prefs/*.xml; do echo \"    \$(basename \$f): \$(grep -o -E 'name=\"[^\"]+\"' \$f | sed 's/name=//' | tr '\n' ' ')\"; done"; echo "  plaintext typed values: $($ADB shell "grep -rl -E 'rt108@example|Rt108Secret' $D 2>/dev/null | wc -l" | tr -d '\r')  in logcat: $($ADB logcat -d | grep -c -E 'rt108@example|Rt108Secret')"
echo; echo "== app egress, whole phase (Google system traffic filtered):"; appegress | sed 's/^/    /'; echo "== remote endpoints the app's uid held (on-device sampler):"; $ADB shell "sort -u /data/local/tmp/socks.txt" | tr -d '
' | python -c "
import sys,socket,struct
seen=set()
for l in sys.stdin:
    l=l.strip()
    if ':' not in l: continue
    a,p=l.split(':'); port=int(p,16)
    if len(a)==8: ip=socket.inet_ntoa(struct.pack('<I',int(a,16)))
    else:
        w=[int(a[i:i+8],16) for i in range(0,32,8)]; ip=socket.inet_ntop(socket.AF_INET6,struct.pack('<IIII',*w))
    if ip.startswith('::ffff:'): ip=ip[7:]
    if (ip,port) in seen or ip in ('0.0.0.0','::','127.0.0.1','::1'): continue
    seen.add((ip,port)); print('    ',ip,port)
"; $ADB shell "pkill -f sampler.sh" 2>/dev/null
echo "== crashes: $(crashes)"; $ADB logcat -d > "$OUT/online-logcat.txt"; cp "$C/egress.log" "$OUT/online-proxy-egress.log"
