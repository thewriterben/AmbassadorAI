"""Compare the AOT snapshot from the two arcade AARs.

If --dart-define=DGD_APP_TAB=true reaches the Dart compiler, libapp.so differs
between the two builds. If the define is being silently dropped, the two are
byte-identical and the whole §4.3 suppression rests on nothing.
"""
import hashlib
import os
import zipfile

OFF = r"C:\src\apptab-ab\flag_off.aar"
ON = r"C:\src\apptab-ab\flag_on.aar"


def snapshots(path):
    out = {}
    with zipfile.ZipFile(path) as z:
        for info in z.infolist():
            if info.filename.endswith("libapp.so"):
                data = z.read(info.filename)
                out[info.filename] = (len(data), hashlib.sha256(data).hexdigest()[:16])
    return out


for label, p in (("flag OFF", OFF), ("flag ON ", ON)):
    if not os.path.exists(p):
        print(f"{label}: MISSING {p}")

if not (os.path.exists(OFF) and os.path.exists(ON)):
    raise SystemExit("both AARs are needed")

a, b = snapshots(OFF), snapshots(ON)
names = sorted(set(a) | set(b))
if not names:
    raise SystemExit("no libapp.so found inside the AARs — check the layout")

print(f"{'abi / entry':46} {'OFF bytes':>11} {'ON bytes':>11}  verdict")
identical = 0
for n in names:
    sa, ha = a.get(n, (0, ""))
    sb, hb = b.get(n, (0, ""))
    same = ha == hb and ha != ""
    identical += 1 if same else 0
    verdict = "IDENTICAL <-- flag not landing" if same else "differs"
    print(f"  {n:44} {sa:>11,} {sb:>11,}  {verdict}")
    if not same:
        print(f"      off sha {ha}   on sha {hb}   delta {sb - sa:+,} bytes")

print()
if identical == 0:
    print("RESULT: every snapshot differs. The define reaches the compiler.")
else:
    print(f"RESULT: {identical} of {len(names)} snapshots identical. "
          "The define is NOT reaching the compiler.")
