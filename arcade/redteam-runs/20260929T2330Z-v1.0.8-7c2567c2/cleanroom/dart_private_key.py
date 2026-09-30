"""Reproduces the Dart VM private-name key for a library URL: '@' + load-order + 6-digit (hash & 0xFFFFF).
Calibrated against two clean-room builds; the Windows path yields the shipped value 119033."""
import sys
M32 = 0xFFFFFFFF
def dart_hash(s):
    x = 0
    for c in s.encode():
        x = (x + c) & M32; x = (x + (x << 10)) & M32; x ^= x >> 6
    x = (x + (x << 3)) & M32; x ^= x >> 11; x = (x + (x << 15)) & M32; x &= (1 << 30) - 1
    return x or 1
SUF = "/.dart_tool/flutter_build/dart_plugin_registrant.dart"
for root, seen in (("/home/builder/dgd_arcade_module", "396501"), ("/home/builder/elsewhere/dgd_arcade_module", "262856"), ("/C:/src/dgd_arcade_module", "119033 (shipped)"), ("/aj/3lf/dgd_arcade_module", "119033 (build 6)")):
    print(f"{root:45s} computed {dart_hash('file://' + root + SUF) & 0xFFFFF:06d}   observed {seen}")
