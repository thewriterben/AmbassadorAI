"""Shrink runtime image assets for the web bundle without visible loss.

- coin_*/piece_* 512px RGBA (~380 KB each): keep 512 px, quantize to a
  256-colour palette with Floyd-Steinberg dithering (metallic gradients
  survive at this size; alpha preserved).
- everything else >60 KB: quantize likewise.
- app_icon.png is moved out of assets/images (only the launcher needs it).
Writes a before/after report and a side-by-side contact sheet.
"""
import hashlib, os, shutil, sys
from PIL import Image

ROOT = r"C:\src\puzzle-app"
IMG = os.path.join(ROOT, "assets", "images")
OUT = sys.argv[1] if len(sys.argv) > 1 else r"C:\src\asset_report"
os.makedirs(OUT, exist_ok=True)
BACKUP = os.path.join(ROOT, "assets", "_images_full")
os.makedirs(BACKUP, exist_ok=True)

def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()

# 1. app icon out of the runtime bundle
icon = os.path.join(IMG, "app_icon.png")
if os.path.exists(icon):
    shutil.move(icon, os.path.join(ROOT, "assets", "app_icon.png"))
    print("moved app_icon.png -> assets/app_icon.png")

# 2. duplicates
seen = {}
for f in sorted(os.listdir(IMG)):
    h = md5(os.path.join(IMG, f))
    if h in seen:
        print(f"DUPLICATE {f} == {seen[h]}")
    seen[h] = f

# 3. quantize
before = after = 0
rows = []
pairs = []
for f in sorted(os.listdir(IMG)):
    p = os.path.join(IMG, f)
    if not f.endswith(".png"):
        continue
    b = os.path.getsize(p)
    before += b
    if b < 60 * 1024:
        after += b
        continue
    shutil.copy2(p, os.path.join(BACKUP, f))
    im = Image.open(p).convert("RGBA")
    q = im.quantize(colors=256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.FLOYDSTEINBERG)
    q.save(p, optimize=True)
    a = os.path.getsize(p)
    after += a
    rows.append((f, b // 1024, a // 1024))
    if f.startswith(("coin_gold", "piece_sapphire", "node_current")):
        pairs.append((f, im, Image.open(p).convert("RGBA")))

for f, b, a in rows:
    print(f"{f:28} {b:5d} KB -> {a:4d} KB")
print(f"TOTAL images {before//1024} KB -> {after//1024} KB")

# contact sheet: original | quantized, at 1:1
if pairs:
    w = sum(max(im.width, 256) for _, im, _ in pairs)
    sheet = Image.new("RGBA", (w * 2 + 40, max(im.height for _, im, _ in pairs) + 40), (16, 16, 16, 255))
    x = 20
    for f, a, b in pairs:
        sheet.alpha_composite(a, (x, 20)); x += a.width + 8
        sheet.alpha_composite(b, (x, 20)); x += b.width + 24
    sheet.save(os.path.join(OUT, "quantize_compare.png"))
    print("sheet ->", os.path.join(OUT, "quantize_compare.png"))
