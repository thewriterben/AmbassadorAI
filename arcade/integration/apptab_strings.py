"""Byte-difference alone could be AOT non-determinism. This is the stronger test.

Dart string literals survive into the AOT snapshot. If the tree shaker really
removed the win-VO and firework code paths, the literals only those paths
reference should be present in the flagless snapshot and absent in the flagged
one. A one-directional disappearance is not something a non-deterministic
compiler produces.
"""
import re
import zipfile

OFF = r"C:\src\apptab-ab\flag_off.aar"
ON = r"C:\src\apptab-ab\flag_on.aar"
ENTRY = "jni/arm64-v8a/libapp.so"

# Literals the suppressed paths reference, and a control that must survive.
PROBES = [
    ("audio/vo/", "win VO asset directory"),
    ("win_", "win VO filename stem"),
    ("firework", "firework code/identifier"),
    ("assets/audio/", "CONTROL: audio assets generally"),
    ("Digital Gold", "CONTROL: app name"),
]


def blob(path):
    with zipfile.ZipFile(path) as z:
        return z.read(ENTRY)


a, b = blob(OFF), blob(ON)
print(f"{ENTRY}   OFF {len(a):,} bytes   ON {len(b):,} bytes\n")
print(f"{'probe':34} {'OFF':>6} {'ON':>6}  reading")
for needle, label in PROBES:
    pat = needle.encode()
    na = len(re.findall(re.escape(pat), a, re.I))
    nb = len(re.findall(re.escape(pat), b, re.I))
    if na and not nb:
        reading = "GONE under the flag"
    elif na == nb and na:
        reading = "unchanged"
    elif not na and not nb:
        reading = "absent from both (probe misses)"
    else:
        reading = "changed count"
    print(f"  {label:32} {na:>6} {nb:>6}  {reading}")
