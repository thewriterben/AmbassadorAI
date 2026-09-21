"""Coin Quest pieces v3 — one hero: the DGD coin, in six precious finishes.

Source: the new DGD_coin_gold.png render (yellow background, keyed out here).
Variants are made by remapping hue/saturation/value of the *same* coin so the
whole set reads as one family: gold, silver, rose gold, obsidian, sapphire,
emerald. Also regenerates the app icon, map medallions and launcher icons.
"""
import colorsys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

SRC = "/sessions/compassionate-sleepy-mccarthy/mnt/uploads/DGD_coin_gold.png"
OUT = "/sessions/compassionate-sleepy-mccarthy/mnt/outputs/cq_v3"
FONTS = "/tmp/fonts"
os.makedirs(OUT, exist_ok=True)

# ---------- 1. key out the yellow background ----------
src = Image.open(SRC).convert("RGB")
a = np.asarray(src).astype(np.float32)
bg = np.median(np.concatenate([a[:8, :8].reshape(-1, 3), a[-8:, -8:].reshape(-1, 3)]), axis=0)
dist = np.sqrt(((a - bg) ** 2).sum(axis=2))
# soft key: fully transparent within 18, opaque beyond 60
alpha = np.clip((dist - 18) / 42, 0, 1)
# clean holes inside the coin: anything inside the disc radius is opaque
h, w = alpha.shape
yy, xx = np.mgrid[:h, :w]
cx, cy = w / 2, h / 2
r_est = 0.5 * min(w, h) * 0.93
inside = ((xx - cx) ** 2 + (yy - cy) ** 2) < (r_est * 0.97) ** 2
alpha[inside] = 1.0
alpha_img = Image.fromarray((alpha * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
coin = src.copy().convert("RGBA"); coin.putalpha(alpha_img)
# crop to content
bbox = alpha_img.point(lambda v: 255 if v > 8 else 0).getbbox()
coin = coin.crop(bbox)
s = max(coin.size); sq = Image.new("RGBA", (s, s), (0, 0, 0, 0)); sq.paste(coin, ((s - coin.width) // 2, (s - coin.height) // 2)); coin = sq
coin.save(f"{OUT}/coin_gold_raw.png")

# ---------- 2. finishes via HSV remap ----------
def remap(img, hue=None, sat=1.0, val=1.0, gamma=1.0, tint=None, tint_amt=0.0, contrast=1.0):
    arr = np.asarray(img).astype(np.float32) / 255.0
    rgb, al = arr[..., :3], arr[..., 3:]
    mx = rgb.max(axis=2); mn = rgb.min(axis=2); v = mx; d = mx - mn
    s_ = np.where(mx > 0, d / np.maximum(mx, 1e-6), 0)
    # hue
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    hh = np.zeros_like(mx)
    mask = d > 1e-6
    rc = np.where(mask, (mx - r) / np.maximum(d, 1e-6), 0); gc = np.where(mask, (mx - g) / np.maximum(d, 1e-6), 0); bc = np.where(mask, (mx - b) / np.maximum(d, 1e-6), 0)
    hh = np.where(mx == r, bc - gc, np.where(mx == g, 2.0 + rc - bc, 4.0 + gc - rc))
    hh = (hh / 6.0) % 1.0
    if hue is not None: hh = np.full_like(hh, hue / 360.0)
    s_ = np.clip(s_ * sat, 0, 1)
    v = np.clip(((v ** gamma) - 0.5) * contrast + 0.5, 0, 1) * val
    v = np.clip(v, 0, 1)
    # hsv -> rgb
    i = np.floor(hh * 6).astype(int) % 6; f = hh * 6 - np.floor(hh * 6)
    p = v * (1 - s_); q = v * (1 - s_ * f); t = v * (1 - s_ * (1 - f))
    out = np.zeros_like(rgb)
    for k, (rr, gg, bb) in enumerate([(v, t, p), (q, v, p), (p, v, t), (p, q, v), (t, p, v), (v, p, q)]):
        m = i == k
        out[..., 0][m] = rr[m]; out[..., 1][m] = gg[m]; out[..., 2][m] = bb[m]
    if tint is not None and tint_amt > 0:
        tt = np.array(tint, dtype=np.float32) / 255.0
        out = out * (1 - tint_amt) + tt * tint_amt * (0.35 + 0.65 * v[..., None])
    out = np.clip(out, 0, 1)
    return Image.fromarray((np.concatenate([out, al], axis=2) * 255).astype(np.uint8))

finishes = {
    "gold":     dict(),
    "silver":   dict(sat=0.10, val=1.02, gamma=0.9, tint=(205, 215, 235), tint_amt=0.12),
    "rose":     dict(hue=8, sat=0.72, val=1.0, tint=(255, 150, 160), tint_amt=0.18),
    "copper":   dict(hue=22, sat=0.95, val=0.88, gamma=1.15, tint=(200, 100, 50), tint_amt=0.15),
    "sapphire": dict(hue=222, sat=1.0, val=0.98, gamma=1.05, tint=(90, 140, 255), tint_amt=0.12),
    "emerald":  dict(hue=148, sat=0.95, val=0.95, gamma=1.05, tint=(60, 220, 150), tint_amt=0.10),
}
glow_col = {
    "gold": (255, 175, 78), "silver": (220, 230, 250), "rose": (255, 150, 170),
    "copper": (230, 130, 70), "sapphire": (100, 150, 255), "emerald": (70, 230, 160),
}

def glow(size, color, alpha, spread=0.40):
    g = Image.new("RGBA", (size, size), (0, 0, 0, 0)); r = size * spread
    ImageDraw.Draw(g).ellipse([size/2 - r, size/2 - r, size/2 + r, size/2 + r], fill=tuple(color) + (alpha,))
    return g.filter(ImageFilter.GaussianBlur(r * 0.5))

variants = {}
for name, kw in finishes.items():
    v = remap(coin, **kw)
    variants[name] = v
    # piece: glow + coin at 92%
    S = 512
    piece = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    piece.alpha_composite(glow(S, glow_col[name], 90, 0.40))
    c = v.resize((int(S * 0.92), int(S * 0.92)), Image.LANCZOS)
    piece.alpha_composite(c, ((S - c.width) // 2, (S - c.height) // 2))
    piece.save(f"{OUT}/piece_{name}.png")
    # clean coin without glow (for hero / particles)
    v.resize((512, 512), Image.LANCZOS).save(f"{OUT}/coin_{name}.png")

# ---------- 3. icon + launcher ----------
def font(name, sz):
    p = {"sans": "InstrumentSans[wdth,wght].ttf", "serif": "PT_Serif-Web-BoldItalic.ttf", "mono": "GeistMono-Bold.ttf"}[name]
    f = ImageFont.truetype(os.path.join(FONTS, p), sz)
    if name == "sans":
        try: f.set_variation_by_axes([100, 600])
        except Exception: pass
    return f

s = 1024
ic = Image.new("RGBA", (s, s), (2, 2, 3, 255))
ic.alpha_composite(glow(s, (30, 32, 42), 255, 0.55))
ic.alpha_composite(glow(s, (234, 149, 45), 150, 0.42))
c = variants["gold"].resize((int(s * 0.80), int(s * 0.80)), Image.LANCZOS)
ic.alpha_composite(c, ((s - c.width) // 2, (s - c.height) // 2))
ic.save(f"{OUT}/app_icon.png")
for name, sz in [('mipmap-mdpi', 48), ('mipmap-hdpi', 72), ('mipmap-xhdpi', 96), ('mipmap-xxhdpi', 144), ('mipmap-xxxhdpi', 192)]:
    os.makedirs(f"{OUT}/launcher/{name}", exist_ok=True)
    ic.resize((sz, sz), Image.LANCZOS).save(f"{OUT}/launcher/{name}/ic_launcher.png")

# ---------- 4. map medallions ----------
def medallion(kind):
    S = 320; im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    if kind == "current":
        im.alpha_composite(glow(S, (255, 175, 78), 170, 0.46)); v = variants["gold"]
    elif kind == "done":
        v = remap(coin, val=0.72, sat=0.8)
    else:
        v = remap(coin, sat=0.12, val=0.42, gamma=1.9, contrast=1.35, tint=(40, 48, 70), tint_amt=0.30)
    c = v.resize((int(S * 0.78), int(S * 0.78)), Image.LANCZOS)
    im.alpha_composite(c, ((S - c.width) // 2, (S - c.height) // 2))
    return im
for k in ("current", "done", "locked"):
    medallion(k).save(f"{OUT}/node_{k}.png")

# ---------- 5. contact sheet ----------
sheet = Image.new("RGBA", (1400, 560), (2, 2, 3, 255))
sheet.alpha_composite(glow(1400, (30, 32, 42), 255, 0.6).crop((0, 0, 1400, 560)))
d = ImageDraw.Draw(sheet); d.text((30, 20), "COIN QUEST · PIECES v3 · one coin, six finishes", font=font("mono", 16), fill=(122, 122, 122))
x = 30
for name in finishes:
    sheet.alpha_composite(Image.open(f"{OUT}/piece_{name}.png").resize((210, 210)), (x, 50)); d.text((x + 70, 262), name.upper(), font=font("mono", 14), fill=(154, 154, 154)); x += 225
sheet.alpha_composite(Image.open(f"{OUT}/app_icon.png").resize((220, 220)), (30, 310))
x = 280
for k in ("current", "done", "locked"):
    sheet.alpha_composite(Image.open(f"{OUT}/node_{k}.png").resize((200, 200)), (x, 320)); x += 210
sheet.save(f"{OUT}/contact_sheet.png")
print("done", coin.size)

# ---------- 6. DGD logo (from DGD.svg) in white and brand orange ----------
import cairosvg, io
svg = open("/sessions/compassionate-sleepy-mccarthy/mnt/uploads/DGD.svg").read()
for name, col in (("logo_orange", "#f7931a"), ("logo_white", "#ffffff"), ("logo_dark", "#030303")):
    data = cairosvg.svg2png(bytestring=svg.replace("#f7931a", col).encode(), output_width=512, output_height=512)
    Image.open(io.BytesIO(data)).convert("RGBA").save(f"{OUT}/{name}.png")
print("logos ok")
