"""Entry-by-entry comparison of two zip artefacts (AAB, APK or AAR).
Usage: compare.py <shipped> <cleanroom> [--show N]"""
import hashlib, sys, zipfile

a_path, b_path = sys.argv[1], sys.argv[2]
show = int(sys.argv[sys.argv.index("--show") + 1]) if "--show" in sys.argv else 40


def entries(p):
    with zipfile.ZipFile(p) as z:
        return {i.filename: hashlib.sha256(z.read(i.filename)).hexdigest() for i in z.infolist() if not i.is_dir()}


a, b = entries(a_path), entries(b_path)
same = sorted(k for k in a if k in b and a[k] == b[k])
diff = sorted(k for k in a if k in b and a[k] != b[k])
only_a = sorted(set(a) - set(b))
only_b = sorted(set(b) - set(a))
print(f"shipped entries {len(a)}, clean-room entries {len(b)}")
print(f"identical {len(same)}, differ {len(diff)}, only in shipped {len(only_a)}, only in clean room {len(only_b)}")
for label, items in (("DIFFER", diff), ("ONLY SHIPPED", only_a), ("ONLY CLEAN ROOM", only_b)):
    for k in items[:show]:
        print(f"  {label:16s} {k}")
    if len(items) > show:
        print(f"  ... {len(items) - show} more")
