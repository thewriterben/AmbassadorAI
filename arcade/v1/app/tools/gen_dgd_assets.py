"""Digital Gold themed sample assets for Puzzle Pack — digitalgold.co style.

Tokens pulled from the live site CSS:
  --background #020203  --bg-2 #08090b  --card #050607  --section-alt #101010
  --primary #ea952d  --primary-hover #ffaf4e  --foreground #e8e8e8
  --text-body #9a9a9a  --text-muted #7a7a7a  --text-dim #4d4d4d
  --border #ffffff12  --border-strong #ffffff24  --surface-elevated #ffffff05
  --info #3080ff  --success #28c93f  --danger #ff6568  --warning #edb200
  glass: 0.5px white/8% ring, inset 1px white/5% top highlight, deep soft shadow
  glow: 0 0 15px #ea952d4d
Fonts: Instrument Sans (headings), Geist Mono (numbers/labels), PT Serif Italic (accent).
"""
import math, os, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = "/sessions/compassionate-sleepy-mccarthy/mnt/outputs/dgd_assets_v2"
FONTS = "/tmp/fonts"
COIN = "/sessions/compassionate-sleepy-mccarthy/mnt/AmbassadorAI/Knowledge Base/Coin Ref/nbgdgd.png"
os.makedirs(OUT, exist_ok=True)
SS = 4
random.seed(11)

def hx(h, a=255):
    h = h.lstrip('#'); return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)

BG = hx('020203'); BG2 = hx('08090b'); CARD = hx('050607'); ALT = hx('101010')
AMBER = hx('ea952d'); AMBER_HI = hx('ffaf4e'); FG = hx('e8e8e8'); BODY = hx('9a9a9a')
MUTED = hx('7a7a7a'); DIM = hx('4d4d4d')
INFO = hx('3080ff'); SUCCESS = hx('28c93f'); DANGER = hx('ff6568'); WARNING = hx('edb200')
WHITE = (255, 255, 255)

def font(name, sz):
    p = {"sans": "InstrumentSans[wdth,wght].ttf", "mono": "GeistMono-Bold.ttf",
         "monomed": "GeistMono-Medium.ttf", "serif": "PT_Serif-Web-BoldItalic.ttf"}[name]
    f = ImageFont.truetype(os.path.join(FONTS, p), sz)
    if name == "sans":
        try: f.set_variation_by_axes([100, 600])
        except Exception: pass
    return f

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(min(len(a), len(b))))

def new(s): return Image.new("RGBA", (s, s), (0, 0, 0, 0))

def radial_glow(size, color, alpha, spread=0.5, cx=0.5, cy=0.5):
    """Soft radial glow layer."""
    s = size
    g = new(s)
    d = ImageDraw.Draw(g)
    r = s * spread
    d.ellipse([s*cx - r, s*cy - r, s*cx + r, s*cy + r], fill=color[:3] + (alpha,))
    return g.filter(ImageFilter.GaussianBlur(r * 0.55))

def grid_lines(size, step, alpha=12, w=1):
    g = new(size); d = ImageDraw.Draw(g)
    for x in range(0, size, step):
        d.line([(x, 0), (x, size)], fill=WHITE + (alpha,), width=w)
    for y in range(0, size, step):
        d.line([(0, y), (size, y)], fill=WHITE + (alpha,), width=w)
    return g

def site_bg(size, grid=True, glow=True):
    im = Image.new("RGBA", (size, size), BG)
    if glow:
        im = Image.alpha_composite(im, radial_glow(size, (30, 32, 42), 255, 0.45))
        im = Image.alpha_composite(im, radial_glow(size, AMBER, 26, 0.32))
    if grid:
        g = grid_lines(size, size // 12, alpha=10, w=max(1, size // 512))
        # fade grid to edges
        m = radial_glow(size, WHITE, 255, 0.55)
        g.putalpha(Image.eval(Image.composite(g.split()[3], Image.new("L", (size, size), 0), m.split()[3]), lambda v: v))
        im = Image.alpha_composite(im, g)
    return im

def glass(size, radius, fill=(255, 255, 255, 14), border=(255, 255, 255, 36), bw=None, inner_hi=True):
    """Glass card: subtle fill, hairline border, top inset highlight."""
    s = size; bw = bw or max(2, s // 128)
    im = new(s); d = ImageDraw.Draw(im)
    d.rounded_rectangle([bw, bw, s-1-bw, s-1-bw], radius=radius, fill=fill, outline=border, width=bw)
    if inner_hi:
        hi = new(s); hd = ImageDraw.Draw(hi)
        hd.rounded_rectangle([bw*2, bw*2, s-1-bw*2, s*0.5], radius=radius*0.9, fill=(255, 255, 255, 10))
        hi = hi.filter(ImageFilter.GaussianBlur(s * 0.02))
        mask = new(s); ImageDraw.Draw(mask).rounded_rectangle([bw, bw, s-1-bw, s-1-bw], radius=radius, fill=(0,0,0,255))
        im.alpha_composite(Image.composite(hi, new(s), mask.split()[3]))
    return im

def amber_glow_behind(size, alpha=90, spread=0.40):
    return radial_glow(size, AMBER, alpha, spread)

def coin_img(size):
    c = Image.open(COIN).convert("RGBA")
    w, h = c.size; s = max(w, h)
    sq = new(s); sq.paste(c, ((s - w) // 2, (s - h) // 2))
    return sq.resize((size, size), Image.LANCZOS)

def text_center(d, xy, txt, f, fill):
    bb = d.textbbox((0, 0), txt, font=f)
    d.text((xy[0] - (bb[2]-bb[0])/2 - bb[0], xy[1] - (bb[3]-bb[1])/2 - bb[1]), txt, font=f, fill=fill)

def save(im, name, size):
    if im.size[0] != size: im = im.resize((size, size), Image.LANCZOS)
    im.save(os.path.join(OUT, name)); return im

made = {}

# ---------- 1. Background (phone) ----------
W, H = 1080, 1920
bg = Image.new("RGBA", (W, H), BG)
def ell_glow(color, alpha, rx, ry, cx, cy):
    g = Image.new("RGBA", (W, H), (0,0,0,0))
    ImageDraw.Draw(g).ellipse([cx-rx, cy-ry, cx+rx, cy+ry], fill=color[:3] + (alpha,))
    return g.filter(ImageFilter.GaussianBlur(min(rx, ry) * 0.6))
bg.alpha_composite(ell_glow((30, 32, 42), 255, W*0.7, H*0.36, W*0.5, H*0.45))
bg.alpha_composite(ell_glow(AMBER, 22, W*0.45, H*0.22, W*0.5, H*0.42))
g = Image.new("RGBA", (W, H), (0,0,0,0)); gd = ImageDraw.Draw(g)
for x in range(0, W, 90): gd.line([(x, 0), (x, H)], fill=WHITE + (9,))
for y in range(0, H, 90): gd.line([(0, y), (W, y)], fill=WHITE + (9,))
m = ell_glow(WHITE, 255, W*0.6, H*0.32, W*0.5, H*0.45).split()[3]
g.putalpha(Image.composite(g.split()[3], Image.new("L", (W, H), 0), m))
bg.alpha_composite(g)
bg.save(f"{OUT}/bg_dark.png"); made["bg"] = bg

# ---------- 2. App icon ----------
s = 1024 * SS
ic = site_bg(s, grid=True)
ic.alpha_composite(amber_glow_behind(s, 110, 0.42))
coin = coin_img(int(s * 0.70))
ic.alpha_composite(coin, (int(s * 0.15), int(s * 0.15)))
made["icon"] = save(ic, "app_icon.png", 1024)

# ---------- 3. Merge tiles ----------
vals = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
merge = []
for i, v in enumerate(vals):
    s = 256 * SS; rad = s * 0.14
    t = i / (len(vals) - 1)
    im = new(s)
    if v == 2048:
        im.alpha_composite(amber_glow_behind(s, 150, 0.38))
        im.alpha_composite(glass(s, rad, fill=(234, 149, 45, 40), border=AMBER[:3] + (160,)))
        c = coin_img(int(s * 0.80)); im.alpha_composite(c, (int(s*0.10), int(s*0.10)))
    else:
        # glass → amber-tinted glass → solid amber
        if t < 0.5:
            k = t / 0.5
            fill = (255, 255, 255, int(12 + 10 * k)); border = lerp((255,255,255,40), AMBER[:3]+(120,), k)
            txt_col = FG
        else:
            k = (t - 0.5) / 0.5
            im.alpha_composite(amber_glow_behind(s, int(60 + 80 * k), 0.38))
            fill = lerp((234, 149, 45, 60), AMBER, k); border = lerp(AMBER[:3]+(160,), AMBER_HI, k)
            txt_col = hx('030303') if v >= 512 else FG
        im.alpha_composite(glass(s, rad, fill=fill, border=border))
        d = ImageDraw.Draw(im)
        f = font("mono", int(s * (0.36 if v < 100 else 0.30 if v < 1000 else 0.24)))
        text_center(d, (s/2, s/2), str(v), f, txt_col)
    merge.append(save(im, f"merge_{v}.png", 256))
made["merge"] = merge

# ---------- 4. Match gems ----------
def gem(shape, col):
    s = 256 * SS; im = new(s); cx = cy = s/2; R = s*0.40
    im.alpha_composite(radial_glow(s, col, 70, 0.36))
    d = ImageDraw.Draw(im)
    fill = col[:3] + (150,); edge = lerp(col[:3], WHITE, 0.35) + (230,); bw = int(s*0.028)
    if shape == "coin":
        return Image.alpha_composite(im, coin_img(s).resize((s, s)))
    if shape == "hex":
        pts = [(cx + R*math.cos(math.radians(60*k+30)), cy + R*math.sin(math.radians(60*k+30))) for k in range(6)]
        d.polygon(pts, fill=fill, outline=edge, width=bw)
        d.regular_polygon((cx, cy, R*0.45), 6, rotation=30, outline=edge, width=bw//2)
    elif shape == "diamond":
        d.polygon([(cx, cy-R), (cx+R*0.8, cy), (cx, cy+R), (cx-R*0.8, cy)], fill=fill, outline=edge, width=bw)
        d.line([(cx-R*0.8, cy), (cx+R*0.8, cy)], fill=edge, width=bw//2)
    elif shape == "square":
        d.rounded_rectangle([cx-R*0.85, cy-R*0.85, cx+R*0.85, cy+R*0.85], radius=s*0.07, fill=fill, outline=edge, width=bw)
        d.rounded_rectangle([cx-R*0.4, cy-R*0.4, cx+R*0.4, cy+R*0.4], radius=s*0.03, outline=edge, width=bw//2)
    elif shape == "triangle":
        d.polygon([(cx, cy-R), (cx+R*0.95, cy+R*0.72), (cx-R*0.95, cy+R*0.72)], fill=fill, outline=edge, width=bw)
    elif shape == "ring":
        d.ellipse([cx-R, cy-R, cx+R, cy+R], fill=fill, outline=edge, width=bw)
        d.ellipse([cx-R*0.42, cy-R*0.42, cx+R*0.42, cy+R*0.42], fill=(0,0,0,0), outline=edge, width=bw)
        # punch hole
        hole = new(s); ImageDraw.Draw(hole).ellipse([cx-R*0.42+bw, cy-R*0.42+bw, cx+R*0.42-bw, cy+R*0.42-bw], fill=(0,0,0,255))
        a = im.split()[3]; a = Image.composite(Image.new("L", (s, s), 0), a, hole.split()[3]); im.putalpha(a)
    return im

gem_spec = [("coin", AMBER), ("hex", FG), ("diamond", INFO), ("square", SUCCESS), ("triangle", DANGER), ("ring", WARNING)]
gems = [save(gem(n, c), f"gem_{n}.png", 256) for n, c in gem_spec]
made["gems"] = gems

# ---------- 5. Block textures ----------
tints = [AMBER, FG, INFO, SUCCESS, DANGER, WARNING, hx('b57bee')]
blocks = []
for i, c in enumerate(tints):
    s = 128 * SS; im = new(s)
    im.alpha_composite(glass(s, s*0.12, fill=c[:3] + (120,), border=lerp(c[:3], WHITE, 0.3) + (200,), bw=max(2, s//64)))
    blocks.append(save(im, f"block_{i}.png", 128))
made["blocks"] = blocks

# ---------- 6. Word tiles ----------
word = []
for name, fill, border, glow in [
    ("correct", AMBER, AMBER_HI, 120),
    ("present", (234, 149, 45, 40), AMBER[:3] + (170,), 0),
    ("absent", ALT, (255, 255, 255, 30), 0),
    ("empty", (255, 255, 255, 8), (255, 255, 255, 60), 0),
]:
    s = 128 * SS; im = new(s)
    if glow: im.alpha_composite(amber_glow_behind(s, glow, 0.38))
    im.alpha_composite(glass(s, s*0.12, fill=fill, border=border, bw=max(2, s//64)))
    word.append(save(im, f"word_{name}.png", 128))
made["word"] = word

# ---------- 7. Rope: treat, vault, anchor ----------
s = 256 * SS; treat = new(s)
treat.alpha_composite(amber_glow_behind(s, 100, 0.38))
treat.alpha_composite(coin_img(int(s*0.86)), (int(s*0.07), int(s*0.07)))
made["treat"] = save(treat, "rope_treat.png", 256)

s = 256 * SS; v = new(s); d = ImageDraw.Draw(v)
v.alpha_composite(glass(s, s*0.12, fill=CARD[:3] + (235,), border=(255, 255, 255, 50)))
d = ImageDraw.Draw(v)
# slot
d.rounded_rectangle([s*0.25, s*0.14, s*0.75, s*0.24], radius=s*0.03, fill=BG, outline=AMBER[:3] + (200,), width=int(s*0.012))
# dial
cx, cy, R = s*0.5, s*0.60, s*0.20
v.alpha_composite(radial_glow(s, AMBER, 90, 0.30, 0.5, 0.60))
d = ImageDraw.Draw(v)
d.ellipse([cx-R, cy-R, cx+R, cy+R], fill=ALT, outline=AMBER[:3] + (230,), width=int(s*0.02))
for k in range(12):
    a = math.radians(30*k)
    d.line([(cx+R*0.72*math.cos(a), cy+R*0.72*math.sin(a)), (cx+R*0.86*math.cos(a), cy+R*0.86*math.sin(a))], fill=MUTED, width=int(s*0.012))
d.ellipse([cx-R*0.35, cy-R*0.35, cx+R*0.35, cy+R*0.35], fill=AMBER)
d.ellipse([cx-R*0.12, cy-R*0.12, cx+R*0.12, cy+R*0.12], fill=hx('030303'))
# eyes
for ex in (s*0.38, s*0.62):
    d.ellipse([ex-s*0.035, s*0.36-s*0.035, ex+s*0.035, s*0.36+s*0.035], fill=FG)
    d.ellipse([ex-s*0.015, s*0.365-s*0.015, ex+s*0.015, s*0.365+s*0.015], fill=BG)
made["vault"] = save(v, "rope_vault.png", 256)

s = 64 * SS; a = new(s); d = ImageDraw.Draw(a)
d.ellipse([2, 2, s-2, s-2], fill=ALT, outline=(255, 255, 255, 60), width=max(2, s//32))
d.ellipse([s*0.32]*2 + [s*0.68]*2, fill=AMBER)
made["anchor"] = save(a, "rope_anchor.png", 64)

# ---------- 8. UI chrome samples: kicker pill, primary button, menu card ----------
def pill(txt, w=420, h=64):
    S = SS; im = Image.new("RGBA", (w*S, h*S), (0,0,0,0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([1, 1, w*S-2, h*S-2], radius=h*S//2, fill=(255,255,255,10), outline=(255,255,255,40), width=2*S)
    r = h*S*0.12; d.ellipse([h*S*0.45-r, h*S/2-r, h*S*0.45+r, h*S/2+r], fill=AMBER)
    f = font("monomed", int(h*S*0.34))
    d.text((h*S*0.8, h*S/2), txt, font=f, fill=FG, anchor="lm")
    return im.resize((w, h), Image.LANCZOS)
made["pill"] = pill("PROOF OF PLAY"); made["pill"].save(f"{OUT}/ui_kicker.png")

def button(txt, w=360, h=88):
    S = SS; im = Image.new("RGBA", (w*S, (h+40)*S), (0,0,0,0))
    im.alpha_composite(radial_glow(w*S, AMBER, 110, 0.5).resize((w*S, (h+40)*S)))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 20*S, w*S-1, (h+20)*S-1], radius=h*S//2, fill=AMBER, outline=AMBER_HI, width=S)
    f = font("sans", int(h*S*0.36))
    d.text((w*S/2, (h/2+20)*S), txt, font=f, fill=hx('030303'), anchor="mm")
    return im.resize((w, h+40), Image.LANCZOS)
made["button"] = button("Play"); made["button"].save(f"{OUT}/ui_button.png")

def menu_card(title, kicker, sample, w=520, h=400):
    S = 2; im = Image.new("RGBA", (w*S, h*S), (0,0,0,0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([1, 1, w*S-2, h*S-2], radius=24*S, fill=CARD[:3] + (245,), outline=(255,255,255,36), width=S)
    g = grid_lines(w*S, 40*S, alpha=8); im.alpha_composite(g.crop((0, 0, w*S, h*S)))
    im.alpha_composite(radial_glow(w*S, AMBER, 40, 0.4).crop((0, 0, w*S, h*S)))
    sp = sample.resize((200*S, 200*S), Image.LANCZOS); im.alpha_composite(sp, ((w*S-200*S)//2, 30*S))
    d = ImageDraw.Draw(im)
    d.text((32*S, 262*S), kicker, font=font("monomed", 13*S), fill=MUTED)
    d.text((32*S, 290*S), title, font=font("sans", 34*S), fill=FG)
    d.text((32*S, 340*S), "Tap to play  →", font=font("monomed", 14*S), fill=AMBER)
    return im.resize((w, h), Image.LANCZOS)
cards = []
for name, title, kicker, sample in [("merge", "Merge", "01 · SWIPE", merge[7]), ("words", "Words", "02 · GUESS", word[0]),
                                    ("blocks", "Blocks", "03 · DROP", blocks[0]), ("match", "Match", "04 · SWAP", gems[0]),
                                    ("rope", "Rope", "05 · CUT", made["treat"])]:
    c = menu_card(title, kicker, sample); c.save(f"{OUT}/card_{name}.png"); cards.append(c)
made["cards"] = cards

# ---------- Contact sheet ----------
sheet = Image.new("RGBA", (1500, 1560), BG)
sheet.alpha_composite(radial_glow(1500, (30, 32, 42), 255, 0.6).resize((1500, 1560)))
d = ImageDraw.Draw(sheet)
fk = font("monomed", 15); ft = font("sans", 26); fser = font("serif", 44)
d.text((30, 24), "Puzzle Pack", font=ft, fill=FG); d.text((190, 14), "in the digitalgold.co style", font=fser, fill=AMBER)
y = 90
def row(label, imgs, size, y, gap=14):
    d.text((30, y), label.upper(), font=fk, fill=MUTED); y += 28; x = 30; rh = 0
    for im in imgs:
        r = im.resize((size, int(size * im.size[1] / im.size[0])), Image.LANCZOS)
        sheet.alpha_composite(r, (x, y)); x += r.size[0] + gap; rh = max(rh, r.size[1])
    return y + rh + 36
y = row("App icon · phone background · UI chrome", [made["icon"], made["bg"].resize((160, 160)), made["pill"].resize((420, 64)), made["button"]], 160, y)
y = row("Menu cards", cards, 280, y)
y = row("Merge tiles 2 → 2048", merge, 118, y)
y = row("Match gems", gems, 150, y)
y = row("Block textures", blocks, 96, y)
y = row("Word tiles: correct · present · absent · empty", word, 118, y)
y = row("Rope: treat · vault · anchor", [made["treat"], made["vault"], made["anchor"]], 170, y)
sheet.save(f"{OUT}/contact_sheet.png")
print("done", len(os.listdir(OUT)))
