"""Coin Quest art — money/bullion pieces in the digitalgold.co style.

Compliance (from the DGD ambassador rules): no coin piles/stacks, no price
charts, no jackpot/casino/money-rain imagery. Every piece is a single object.

Pieces (distinct hue AND silhouette):
  gold    – the real DGD coin (brand asset)
  silver  – round silver coin, reeded rim, "S" mark
  copper  – smaller copper cent, plain rim
  bar     – single gold ingot, trapezoid, "999.9" stamp
  note    – folded banknote, teal, DGD seal
  key     – vault key, steel blue
"""
import math, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = "/sessions/compassionate-sleepy-mccarthy/mnt/outputs/cq_assets"
FONTS = "/tmp/fonts"
COIN = "/sessions/compassionate-sleepy-mccarthy/mnt/AmbassadorAI/Knowledge Base/Coin Ref/nbgdgd.png"
os.makedirs(OUT, exist_ok=True)
SS = 4

def hx(h, a=255):
    h = h.lstrip('#'); return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)

BG = hx('020203'); CARD = hx('050607'); ALT = hx('101010')
AMBER = hx('ea952d'); AMBER_HI = hx('ffaf4e'); AMBER_DK = hx('9c5f14')
FG = hx('e8e8e8'); MUTED = hx('7a7a7a'); DIM = hx('4d4d4d')
SILVER = hx('c9cdd6'); SILVER_HI = hx('f2f4f8'); SILVER_DK = hx('7e848f')
COPPER = hx('b5652b'); COPPER_HI = hx('e2955a'); COPPER_DK = hx('6e3a15')
TEAL = hx('2fb37a'); TEAL_HI = hx('7fe0b0'); TEAL_DK = hx('176b47')
STEEL = hx('6f8fd8'); STEEL_HI = hx('b8c8f2'); STEEL_DK = hx('3a4f86')
WHITE = (255, 255, 255)

def font(name, sz):
    p = {"sans": "InstrumentSans[wdth,wght].ttf", "mono": "GeistMono-Bold.ttf",
         "monomed": "GeistMono-Medium.ttf", "serif": "PT_Serif-Web-BoldItalic.ttf"}[name]
    f = ImageFont.truetype(os.path.join(FONTS, p), sz)
    if name == "sans":
        try: f.set_variation_by_axes([100, 600])
        except Exception: pass
    return f

def lerp(a, b, t): return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(min(len(a), len(b))))
def new(s): return Image.new("RGBA", (s, s), (0, 0, 0, 0))

def glow(size, color, alpha, spread=0.38):
    g = new(size); r = size * spread
    ImageDraw.Draw(g).ellipse([size/2 - r, size/2 - r, size/2 + r, size/2 + r], fill=color[:3] + (alpha,))
    return g.filter(ImageFilter.GaussianBlur(r * 0.55))

def coin_img(size):
    c = Image.open(COIN).convert("RGBA"); w, h = c.size; s = max(w, h)
    sq = new(s); sq.paste(c, ((s - w) // 2, (s - h) // 2)); return sq.resize((size, size), Image.LANCZOS)

def radial_metal(size, cx, cy, r, base, hi, dk, steps=40):
    """Disc with diagonal metallic sheen (light top-left)."""
    im = new(size); d = ImageDraw.Draw(im)
    for i in range(steps):
        t = i / (steps - 1)
        rr = r * (1 - t * 0.02)
        # sheen: interpolate from hi (top-left) to dk (bottom-right) along the diagonal
        col = lerp(hi, dk, t)
        off = r * 0.35 * t
        d.ellipse([cx - rr + off * 0.6, cy - rr + off * 0.6, cx + rr - off * 0.2, cy + rr - off * 0.2], fill=col)
    d.ellipse([cx - r * 0.86, cy - r * 0.86, cx + r * 0.86, cy + r * 0.86], fill=base)
    # specular
    hl = new(size); hd = ImageDraw.Draw(hl)
    hd.ellipse([cx - r * 0.7, cy - r * 0.85, cx - r * 0.05, cy - r * 0.3], fill=(255, 255, 255, 80))
    hl = hl.filter(ImageFilter.GaussianBlur(r * 0.18))
    return Image.alpha_composite(im, hl)

def reeded_rim(d, cx, cy, r, n, color, w):
    for k in range(n):
        a = 2 * math.pi * k / n
        d.line([(cx + r * 0.93 * math.cos(a), cy + r * 0.93 * math.sin(a)), (cx + r * math.cos(a), cy + r * math.sin(a))], fill=color, width=w)

def text_center(d, xy, txt, f, fill):
    bb = d.textbbox((0, 0), txt, font=f)
    d.text((xy[0] - (bb[2]-bb[0])/2 - bb[0], xy[1] - (bb[3]-bb[1])/2 - bb[1]), txt, font=f, fill=fill)

def save(im, name, size):
    if im.size[0] != size: im = im.resize((size, size), Image.LANCZOS)
    im.save(os.path.join(OUT, name)); return im

S = 256 * SS
made = {}

# ---------------- gold: brand coin ----------------
im = new(S); im.alpha_composite(glow(S, AMBER, 80)); im.alpha_composite(coin_img(int(S * 0.92)), (int(S*0.04), int(S*0.04)))
made["gold"] = save(im, "piece_gold.png", 256)

# ---------------- silver coin ----------------
im = new(S); im.alpha_composite(glow(S, SILVER, 60))
cx = cy = S/2; r = S * 0.42
im.alpha_composite(radial_metal(S, cx, cy, r, SILVER, SILVER_HI, SILVER_DK))
d = ImageDraw.Draw(im)
reeded_rim(d, cx, cy, r, 60, SILVER_DK, int(S*0.008))
d.ellipse([cx - r*0.72, cy - r*0.72, cx + r*0.72, cy + r*0.72], outline=SILVER_DK, width=int(S*0.012))
text_center(d, (cx, cy + S*0.01), "S", font("serif", int(S*0.42)), SILVER_DK)
made["silver"] = save(im, "piece_silver.png", 256)

# ---------------- copper cent (smaller) ----------------
im = new(S); im.alpha_composite(glow(S, COPPER, 60))
r = S * 0.35
im.alpha_composite(radial_metal(S, cx, cy, r, COPPER, COPPER_HI, COPPER_DK))
d = ImageDraw.Draw(im)
d.ellipse([cx - r*0.8, cy - r*0.8, cx + r*0.8, cy + r*0.8], outline=COPPER_DK, width=int(S*0.012))
text_center(d, (cx, cy + S*0.005), "1", font("mono", int(S*0.34)), COPPER_DK)
made["copper"] = save(im, "piece_copper.png", 256)

# ---------------- gold bar (single ingot) ----------------
im = new(S); im.alpha_composite(glow(S, AMBER, 60))
d = ImageDraw.Draw(im)
top = [(S*0.20, S*0.30), (S*0.80, S*0.30), (S*0.90, S*0.48), (S*0.10, S*0.48)]
front = [(S*0.10, S*0.48), (S*0.90, S*0.48), (S*0.90, S*0.70), (S*0.10, S*0.70)]
d.polygon(front, fill=AMBER_DK)
d.polygon(top, fill=AMBER)
# sheen band on top
d.polygon([(S*0.28, S*0.30), (S*0.46, S*0.30), (S*0.38, S*0.48), (S*0.20, S*0.48)], fill=AMBER_HI)
d.line([(S*0.10, S*0.48), (S*0.90, S*0.48)], fill=AMBER_HI, width=int(S*0.008))
d.polygon(top, outline=AMBER_DK, width=int(S*0.008))
text_center(d, (S*0.5, S*0.59), "999.9", font("mono", int(S*0.10)), AMBER_HI)
text_center(d, (S*0.5, S*0.39), "DGD", font("sans", int(S*0.08)), AMBER_DK)
made["bar"] = save(im, "piece_bar.png", 256)

# ---------------- banknote (teal) ----------------
im = new(S); im.alpha_composite(glow(S, TEAL, 55))
d = ImageDraw.Draw(im)
note = [S*0.10, S*0.30, S*0.90, S*0.70]
d.rounded_rectangle(note, radius=S*0.03, fill=TEAL_DK)
d.rounded_rectangle([note[0]+S*0.02, note[1]+S*0.02, note[2]-S*0.02, note[3]-S*0.02], radius=S*0.025, fill=TEAL)
d.rounded_rectangle([note[0]+S*0.05, note[1]+S*0.05, note[2]-S*0.05, note[3]-S*0.05], radius=S*0.02, outline=TEAL_HI, width=int(S*0.008))
# guilloche-ish arcs
for k in range(6):
    rr = S * (0.05 + k * 0.03)
    d.ellipse([S*0.5 - rr, S*0.5 - rr, S*0.5 + rr, S*0.5 + rr], outline=TEAL_HI[:3] + (90,), width=int(S*0.004))
d.ellipse([S*0.5 - S*0.11, S*0.5 - S*0.11, S*0.5 + S*0.11, S*0.5 + S*0.11], fill=TEAL_DK, outline=TEAL_HI, width=int(S*0.008))
text_center(d, (S*0.5, S*0.5), "DGD", font("sans", int(S*0.075)), TEAL_HI)
for x in (S*0.19, S*0.81):
    text_center(d, (x, S*0.5), "1", font("mono", int(S*0.11)), TEAL_HI)
made["note"] = save(im, "piece_note.png", 256)

# ---------------- vault key (steel) ----------------
im = new(S); im.alpha_composite(glow(S, STEEL, 55))
d = ImageDraw.Draw(im)
# bow (ring) + shank + bits, rotated 45° by drawing then rotating layer
k = new(S); kd = ImageDraw.Draw(k)
bow_c = (S*0.32, S*0.5); bow_r = S*0.16
kd.ellipse([bow_c[0]-bow_r, bow_c[1]-bow_r, bow_c[0]+bow_r, bow_c[1]+bow_r], fill=STEEL, outline=STEEL_DK, width=int(S*0.02))
kd.ellipse([bow_c[0]-bow_r*0.45, bow_c[1]-bow_r*0.45, bow_c[0]+bow_r*0.45, bow_c[1]+bow_r*0.45], fill=(0,0,0,0))
hole = new(S); ImageDraw.Draw(hole).ellipse([bow_c[0]-bow_r*0.45, bow_c[1]-bow_r*0.45, bow_c[0]+bow_r*0.45, bow_c[1]+bow_r*0.45], fill=(0,0,0,255))
a = k.split()[3]; a = Image.composite(Image.new("L", (S, S), 0), a, hole.split()[3]); k.putalpha(a)
kd = ImageDraw.Draw(k)
kd.rounded_rectangle([S*0.46, S*0.46, S*0.86, S*0.54], radius=S*0.02, fill=STEEL, outline=STEEL_DK, width=int(S*0.012))
kd.rectangle([S*0.72, S*0.54, S*0.77, S*0.64], fill=STEEL, outline=STEEL_DK, width=int(S*0.01))
kd.rectangle([S*0.80, S*0.54, S*0.85, S*0.62], fill=STEEL, outline=STEEL_DK, width=int(S*0.01))
kd.line([(S*0.50, S*0.485), (S*0.84, S*0.485)], fill=STEEL_HI, width=int(S*0.012))
k = k.rotate(35, resample=Image.BICUBIC, center=(S/2, S/2))
im.alpha_composite(k)
made["key"] = save(im, "piece_key.png", 256)

# ---------------- app icon ----------------
s = 1024 * SS
ic = Image.new("RGBA", (s, s), BG)
ic.alpha_composite(glow(s, (30, 32, 42), 255, 0.5))
g = new(s); gd = ImageDraw.Draw(g)
for x in range(0, s, s // 12): gd.line([(x, 0), (x, s)], fill=WHITE + (10,), width=max(1, s // 512))
for y in range(0, s, s // 12): gd.line([(0, y), (s, y)], fill=WHITE + (10,), width=max(1, s // 512))
ic.alpha_composite(g)
ic.alpha_composite(glow(s, AMBER, 120, 0.42))
ic.alpha_composite(coin_img(int(s * 0.62)), (int(s * 0.19), int(s * 0.10)))
d = ImageDraw.Draw(ic)
text_center(d, (s*0.5, s*0.84), "Coin Quest", font("sans", int(s*0.11)), FG)
made["icon"] = save(ic, "app_icon.png", 1024)

# ---------------- map medallions ----------------
def medallion(kind):
    s = 160 * SS; im = new(s); cx = cy = s/2; r = s*0.42
    if kind == "current":
        im.alpha_composite(glow(s, AMBER, 150, 0.45))
        im.alpha_composite(radial_metal(s, cx, cy, r, AMBER, AMBER_HI, AMBER_DK))
        d = ImageDraw.Draw(im); reeded_rim(d, cx, cy, r, 48, AMBER_DK, int(s*0.01))
        d.ellipse([cx-r*0.74, cy-r*0.74, cx+r*0.74, cy+r*0.74], outline=AMBER_DK, width=int(s*0.012))
    elif kind == "done":
        im.alpha_composite(radial_metal(s, cx, cy, r, lerp(AMBER, CARD, 0.35), lerp(AMBER_HI, CARD, 0.3), lerp(AMBER_DK, CARD, 0.3)))
        d = ImageDraw.Draw(im); reeded_rim(d, cx, cy, r, 48, AMBER_DK, int(s*0.01))
        d.ellipse([cx-r*0.74, cy-r*0.74, cx+r*0.74, cy+r*0.74], outline=AMBER_DK[:3] + (160,), width=int(s*0.012))
    else:  # locked
        d = ImageDraw.Draw(im)
        d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=ALT, outline=(255,255,255,40), width=int(s*0.012))
        d.ellipse([cx-r*0.74, cy-r*0.74, cx+r*0.74, cy+r*0.74], outline=(255,255,255,25), width=int(s*0.01))
    return im
for kd in ("current", "done", "locked"):
    made[f"node_{kd}"] = save(medallion(kd), f"node_{kd}.png", 160)

# ---------------- board cell tile (vault tray) ----------------
s = 128 * SS; cell = new(s); d = ImageDraw.Draw(cell)
d.rounded_rectangle([2, 2, s-3, s-3], radius=s*0.18, fill=(255,255,255,12), outline=(255,255,255,28), width=max(2, s//128))
d.rounded_rectangle([s*0.12, s*0.12, s*0.88, s*0.88], radius=s*0.14, outline=AMBER[:3] + (22,), width=max(2, s//128))
made["cell"] = save(cell, "board_cell.png", 128)

# ---------------- wordmark (for home) ----------------
W, H = 900, 260
wm = Image.new("RGBA", (W*2, H*2), (0,0,0,0)); d = ImageDraw.Draw(wm)
d.text((0, 0), "Coin", font=font("sans", 200), fill=FG)
d.text((470, 0), "Quest", font=font("serif", 200), fill=AMBER)
wm = wm.resize((W, H), Image.LANCZOS); wm.save(f"{OUT}/wordmark.png"); made["wordmark"] = wm

# ---------------- contact sheet ----------------
sheet = Image.new("RGBA", (1400, 760), BG)
sheet.alpha_composite(glow(1400, (30,32,42), 255, 0.6).crop((0, 0, 1400, 760)))
d = ImageDraw.Draw(sheet); fk = font("monomed", 15)
sheet.alpha_composite(made["wordmark"].resize((450, 130)), (30, 20))
d.text((30, 170), "PIECES · gold · silver · copper · bar · note · key", font=fk, fill=MUTED)
x = 30
for k in ("gold", "silver", "copper", "bar", "note", "key"):
    sheet.alpha_composite(made[k].resize((200, 200)), (x, 200)); x += 215
d.text((30, 430), "ICON · MAP NODES (current / done / locked) · CELL", font=fk, fill=MUTED)
sheet.alpha_composite(made["icon"].resize((220, 220)), (30, 460))
x = 280
for k in ("node_current", "node_done", "node_locked"):
    sheet.alpha_composite(made[k].resize((160, 160)), (x, 490)); x += 175
sheet.alpha_composite(made["cell"].resize((128, 128)), (x + 20, 506))
sheet.save(f"{OUT}/contact_sheet.png")
print("done", len(os.listdir(OUT)))
