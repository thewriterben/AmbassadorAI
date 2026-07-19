#!/usr/bin/env python3
"""
dgd_assets.py - In-agent brand asset generator for DGD Video Studio.

Renders on-brand, compliance-safe assets with ZERO external services, so the
agent can actually PRODUCE Stage-5 visuals instead of only emitting prompts.

Commands
--------
  title       vertical 9:16 (1080x1920) title / cover card
  thumb       16:9 (1280x720) thumbnail
  lower       transparent lower-third caption strip (9:16 canvas)
  disclosure  reusable transparent "SPONSORED - NOT FINANCIAL ADVICE" overlay
  contact-sheet  composite a folder's assets into one preview image
  motif       abstract 9:16 b-roll background, compliance-safe themes:
              network | scarcity | erosion | supply-chain |
              monetary-history | vault
  coin        composite the REFERENCE DGD coin at a correct, consistent scale
  coin-motion seamlessly-looping coin motion: spin | flip | tumble | wobble | orbit

Design notes
------------
* Text cards are deterministic on purpose: the wiki's own rule is "generate title
  cards WITHOUT AI text (it misspells), add crisp text later." This does that step
  reliably, on-brand (gold + deep navy editorial), and free.
* Motifs are abstract/illustrative only (gold, nodes, grids, supply flow) - never
  realistic people or events - matching reference/tool-matcher.md Step 4.
* The disclosure overlay is first-class because FTC + "not financial advice" are
  mandatory per the compliance gate; the rail is baked into the toolchain.
* All user text passes a fail-closed compliance pre-scan (banned investment/price/
  return framing aborts the render with exit code 2).
* The coin is NEVER generated - stills and motion both render from the reference
  asset, so the coin is identical everywhere. Motion drives the rim from the real
  2.41mm/34.1mm ratio (7.07% of diameter); that ratio is what makes a turning coin
  read as a coin rather than a flat disc. See reference/coin-assets.md.

Usage
-----
  python3 dgd_assets.py title --headline "Why money quietly loses value" \
      --kicker "SOUND MONEY - EP. 1" --out cover.png
  python3 dgd_assets.py thumb --headline "The 1% rule" --kicker "Digital Gold" --out t.png
  python3 dgd_assets.py disclosure --out disclosure_overlay.png
  python3 dgd_assets.py lower --text "Not financial advice - Educational" --out lt.png
  python3 dgd_assets.py motif --theme vault --out broll_vault.png
  python3 dgd_assets.py kit --headline "Why money loses value" \
      --kicker "Sound Money - Ep. 1" --outdir raw/ep1
  python3 dgd_assets.py coin --preset hero --out coin_hero.png
  python3 dgd_assets.py coin --preset hand --onto plate.png --out shot.png
  python3 dgd_assets.py coin-motion --mode flip --frames 48 --outdir raw/flip --webp f.webp
"""
import argparse
import math
import os
import random
import re
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

NAVY      = (16, 23, 42)
CHARCOAL  = (10, 12, 18)
GOLD      = (212, 168, 83)
GOLD_HI   = (240, 208, 130)
WHITE     = (244, 244, 240)
MUTE      = (150, 158, 178)

# ---------------------------------------------------------------- coin -----
# The DGD coin is NEVER generated - it is composited from the reference asset.
# Generators invent a different coin every time; an inconsistent coin reads as a
# fake project. See skills/dgd-video-studio/reference/coin-assets.md.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import compliance_lint as CL   # single source of truth for the rails
except Exception:
    CL = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COIN_REF = os.path.join(ROOT, "Knowledge Base", "Coin Ref", "nbgdgd.png")
COIN_MM = 34.1          # $20 Saint-Gaudens Double Eagle diameter - the spec size
COIN_THICKNESS_MM = 2.41
COIN_THICKNESS_RATIO = COIN_THICKNESS_MM / COIN_MM   # 7.07% of the diameter

# Physical realism is a MODE, not a constraint. Presets below anchor the coin to
# its real 34.1mm size for in-hand and product shots; --diameter sizes it freely
# for hero, monumental and abstract treatments where real-world scale is beside
# the point. What must stay constant in every mode is the coin's IDENTITY -
# the face, the legend, the ring count - and, when it turns, the rim ratio.

# Coin width as a fraction of frame width, measured from the hand reference
# (dgdhandref.jpg: 440px rim in a 960px frame = 45.8%).
COIN_PRESETS = {
    "hand":   0.458,    # true-to-life, matches the hand reference
    "hero":   0.55,     # title card / product shot
    "accent": 0.15,     # corner mark, lower-third
    "macro":  0.85,     # detail shot, rings legible
}

def _winfont(name):
    return os.path.join(os.environ.get("WINDIR", r"C:\\Windows"), "Fonts", name)

# Per-role font candidates across Linux / Windows / macOS, in preference order.
_FONT_CANDIDATES = {
    "serif_bold": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSerif-Bold.ttf",
        _winfont("georgiab.ttf"), _winfont("timesbd.ttf"),
        "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
        "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
        "/Library/Fonts/Georgia Bold.ttf",
    ],
    "sans": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
        _winfont("arial.ttf"), _winfont("segoeui.ttf"),
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf", "/System/Library/Fonts/Helvetica.ttc",
    ],
    "sans_bold": [
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        _winfont("arialbd.ttf"), _winfont("segoeuib.ttf"),
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
    ],
}


def _resolve(role):
    for path in _FONT_CANDIDATES[role]:
        if path and os.path.exists(path):
            return path
    return None  # _font() falls back to Pillow's bundled scalable font


SERIF_BOLD = _resolve("serif_bold")
SANS       = _resolve("sans")
SANS_BOLD  = _resolve("sans_bold")

BANNED = [
    r"\binvest(ment|ing|or)?\b", r"\bROI\b", r"\breturns?\b", r"\bprofit",
    r"\bgains?\b", r"\bpassive income\b", r"\bto the moon\b", r"\bmoon\b",
    r"\bpump\b", r"\b100x\b", r"\bget in (early|now)\b", r"\bdon'?t miss out\b",
    r"\bbuy now\b", r"\bape in\b", r"\bsecure your bag\b",
    r"\bsafe (haven|bet|investment)\b", r"\bstore of value\b", r"\bcan'?t lose\b",
    r"\bnext bitcoin\b", r"\bportfolio\b",
]
ALLOWED = {"not financial advice", "sponsored"}


def compliance_scan(*texts):
    """Fail-closed pre-scan for any text rendered onto an asset.

    Delegates to compliance_lint - the single source of truth for the rails.
    The local BANNED list below is only a fallback for when the linter can't be
    imported; it is deliberately narrower, and a divergence here was how
    "Buy DGD now", "guaranteed" and "risk-free" once rendered onto title cards.
    """
    hits = []
    for t in texts:
        if not t:
            continue
        if t.lower().strip() in ALLOWED:
            continue
        if CL is not None:
            for f in CL.lint_text(t)["findings"]:
                if f["severity"] == "FAIL":
                    hits.append((t, f["term"]))
        else:
            low = t.lower()
            for pat in BANNED:
                m = re.search(pat, low)
                if m:
                    hits.append((t, m.group(0)))
    return hits


def _font(path, size):
    """Load a TrueType font; fall back to Pillow's bundled scalable font anywhere."""
    if path:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    try:
        return ImageFont.load_default(size=size)   # Pillow >= 10.1 -> scalable DejaVu
    except TypeError:
        return ImageFont.load_default()            # very old Pillow -> bitmap


def gradient_bg(w, h, top=NAVY, bottom=CHARCOAL):
    # Build one column, then stretch it. The old per-pixel loop cost ~w*h Python
    # writes per call, which made multi-frame renders unusable.
    col = Image.new("RGB", (1, h))
    px = col.load()
    for y in range(h):
        t = (y / max(1, h - 1)) ** 1.15
        px[0, y] = (int(top[0] + (bottom[0] - top[0]) * t),
                    int(top[1] + (bottom[1] - top[1]) * t),
                    int(top[2] + (bottom[2] - top[2]) * t))
    return col.resize((w, h), Image.NEAREST)


def add_gold_dust(img, density=0.00018, seed=7):
    rnd = random.Random(seed)
    w, h = img.size
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for _ in range(int(w * h * density)):
        x, y = rnd.randint(0, w - 1), rnd.randint(0, h - 1)
        vert = 1.0 - (y / h) * 0.6
        a = int(rnd.randint(20, 70) * vert)
        rad = rnd.choice([1, 1, 1, 2])
        d.ellipse([x - rad, y - rad, x + rad, y + rad], fill=GOLD_HI + (a,))
    img.alpha_composite(layer.filter(ImageFilter.GaussianBlur(0.4)))
    return img


def vignette(img, strength=0.55):
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).ellipse([-w * 0.25, -h * 0.18, w * 1.25, h * 1.18], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(int(min(w, h) * 0.12)))
    dark = Image.new("RGBA", (w, h), (0, 0, 0, int(255 * strength)))
    img.paste(dark, (0, 0), Image.eval(mask, lambda v: 255 - v))
    return img


def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_font(draw, text, path, max_w, max_h, start, min_size=28):
    size = start
    while size >= min_size:
        font = _font(path, size)
        lines = wrap(draw, text, font, max_w)
        lh = int(sum(font.getmetrics()) * 1.12)
        if len(lines) * lh <= max_h:
            return font, lines, lh
        size -= 4
    font = _font(path, min_size)
    return font, wrap(draw, text, font, max_w), int(sum(font.getmetrics()) * 1.12)


def draw_disclosure_lozenge(draw, cx, y, scale=1.0):
    f = _font(SANS_BOLD, int(26 * scale))
    label = "SPONSORED   -   NOT FINANCIAL ADVICE"
    tw = draw.textlength(label, font=f)
    pad_x, pad_y = int(28 * scale), int(16 * scale)
    box_w = tw + pad_x * 2
    box_h = sum(f.getmetrics()) + pad_y * 2
    x0 = cx - box_w / 2
    draw.rounded_rectangle([x0, y, x0 + box_w, y + box_h], radius=box_h / 2,
                           fill=(0, 0, 0, 150), outline=GOLD + (255,),
                           width=max(2, int(2 * scale)))
    draw.text((cx, y + box_h / 2), label, font=f, fill=GOLD_HI + (255,), anchor="mm")
    return y + box_h


def make_title(headline, kicker=None, subtitle=None, disclosure=True,
               w=1080, h=1920, seed=7):
    img = vignette(add_gold_dust(gradient_bg(w, h).convert("RGBA"), seed=seed))
    d = ImageDraw.Draw(img)
    margin = int(w * 0.10)
    box_w = w - margin * 2
    y = int(h * 0.30)
    if kicker:
        kf = _font(SANS_BOLD, 34)
        d.line([margin, y, margin + 70, y], fill=GOLD, width=4)
        d.text((margin + 90, y), kicker.upper(), font=kf, fill=GOLD, anchor="lm")
        y += 70
    hf, lines, lh = fit_font(d, headline, SERIF_BOLD, box_w, int(h * 0.34),
                             start=120, min_size=52)
    for ln in lines:
        d.text((margin, y), ln, font=hf, fill=WHITE, anchor="lm")
        y += lh
    if subtitle:
        y += 24
        sf = _font(SANS, 40)
        for ln in wrap(d, subtitle, sf, box_w):
            d.text((margin, y), ln, font=sf, fill=MUTE, anchor="lm")
            y += int(sum(sf.getmetrics()) * 1.2)
    d.text((margin, h - int(h * 0.06)), "DIGITAL GOLD - EDUCATIONAL",
           font=_font(SANS_BOLD, 32), fill=GOLD, anchor="lm")
    if disclosure:
        draw_disclosure_lozenge(d, w / 2, int(h * 0.055))
    return img.convert("RGB")


def make_thumb(headline, kicker=None, w=1280, h=720, seed=11):
    img = vignette(add_gold_dust(gradient_bg(w, h, top=(20, 28, 50)).convert("RGBA"),
                                 density=0.00012, seed=seed), strength=0.45)
    d = ImageDraw.Draw(img)
    margin = int(w * 0.07)
    box_w = int(w * 0.62)
    d.rectangle([w - 16, 0, w, h], fill=GOLD)
    if kicker:
        d.text((margin, int(h * 0.18)), kicker.upper(),
               font=_font(SANS_BOLD, 30), fill=GOLD, anchor="lm")
    y = int(h * 0.38)
    hf, lines, lh = fit_font(d, headline, SERIF_BOLD, box_w, int(h * 0.5),
                             start=104, min_size=44)
    for ln in lines:
        d.text((margin, y), ln, font=hf, fill=WHITE, anchor="lm")
        y += lh
    return img.convert("RGB")


def make_disclosure(w=1080, h=300):
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw_disclosure_lozenge(ImageDraw.Draw(img), w / 2, h * 0.32, scale=1.4)
    return img


def make_lower_third(text, w=1080, h=1920):
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    strip_h, y0 = 150, int(h * 0.74)
    d.rectangle([0, y0, w, y0 + strip_h], fill=(10, 12, 18, 205))
    d.rectangle([0, y0, 14, y0 + strip_h], fill=GOLD)
    d.text((60, y0 + strip_h / 2), text, font=_font(SANS_BOLD, 44),
           fill=WHITE, anchor="lm")
    return img


def _glow_line(d, p0, p1, color, width, alpha):
    d.line([p0, p1], fill=color + (alpha,), width=width)


def motif_network(d, w, h, rnd):
    pts = [(rnd.randint(int(w * 0.08), int(w * 0.92)),
            rnd.randint(int(h * 0.10), int(h * 0.90))) for _ in range(34)]
    for i, a in enumerate(pts):
        for b in pts[i + 1:]:
            dist = math.hypot(a[0] - b[0], a[1] - b[1])
            if dist < w * 0.28:
                al = int(70 * (1 - dist / (w * 0.28)))
                _glow_line(d, a, b, GOLD, 2, al)
    for (x, y) in pts:
        r = rnd.choice([4, 5, 6, 8])
        d.ellipse([x - r - 3, y - r - 3, x + r + 3, y + r + 3], fill=GOLD + (60,))
        d.ellipse([x - r, y - r, x + r, y + r], fill=GOLD_HI + (255,))


def motif_scarcity(d, w, h, rnd):
    step = int(w * 0.075)
    for x in range(int(w * 0.12), int(w * 0.88), step):
        _glow_line(d, (x, int(h * 0.16)), (x, int(h * 0.84)), GOLD, 1, 40)
    for y in range(int(h * 0.16), int(h * 0.84), step):
        _glow_line(d, (int(w * 0.12), y), (int(w * 0.88), y), GOLD, 1, 40)
    cx, cy, r = w // 2, h // 2, int(w * 0.18)
    for rr, al in ((r + 26, 50), (r + 12, 90)):
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=GOLD + (al,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD_HI + (255,), width=6)
    d.ellipse([cx - r + 18, cy - r + 18, cx + r - 18, cy + r - 18],
              outline=GOLD + (160,), width=3)


def motif_erosion(d, w, h, rnd):
    bx, bw = int(w * 0.34), int(w * 0.32)
    bar_h, gap = int(h * 0.022), int(h * 0.012)
    y = int(h * 0.30)
    while y < int(h * 0.80):
        intact = 1.0 - max(0, (int(h * 0.50) - y)) / (h * 0.45)
        right = bx + int(bw * min(1.0, 0.35 + intact))
        d.rectangle([bx, y, right, y + bar_h], fill=GOLD + (200,))
        y += bar_h + gap
    for _ in range(900):
        x = rnd.randint(bx, bx + bw + int(w * 0.18))
        yy = rnd.randint(int(h * 0.14), int(h * 0.40))
        a = int(120 * (1 - (yy - h * 0.14) / (h * 0.26)))
        d.ellipse([x, yy, x + 2, yy + 2], fill=GOLD_HI + (max(0, a),))


def motif_supply(d, w, h, rnd):
    cy = h // 2
    xs = [int(w * f) for f in (0.16, 0.38, 0.60, 0.82)]
    ys = [cy - int(h * 0.06), cy + int(h * 0.05),
          cy - int(h * 0.04), cy + int(h * 0.06)]
    pts = list(zip(xs, ys))
    for a, b in zip(pts, pts[1:]):
        _glow_line(d, a, b, GOLD, 5, 120)
        _glow_line(d, a, b, GOLD_HI, 2, 220)
    s = int(w * 0.05)
    for i, (x, y) in enumerate(pts):
        d.ellipse([x - s - 6, y - s - 6, x + s + 6, y + s + 6], fill=GOLD + (50,))
        if i == 0:
            d.rectangle([x - s, y - s, x + s, y + s], outline=GOLD_HI + (255,), width=5)
        elif i == 1:
            d.rounded_rectangle([x - s, y - s * 0.7, x + s, y + s * 0.7],
                                radius=10, outline=GOLD_HI + (255,), width=5)
        elif i == 2:
            d.polygon([(x, y - s), (x - s, y + s), (x + s, y + s)],
                      outline=GOLD_HI + (255,), width=5)
        else:
            d.ellipse([x - s, y - s, x + s, y + s], outline=GOLD_HI + (255,), width=5)


def motif_history(d, w, h, rnd):
    """Monetary history: a classical temple (abstract antiquity, no people)."""
    n, cw = 4, int(w * 0.10)
    gap = int((w * 0.74 - n * cw) / (n - 1))
    x0, top, bot = int(w * 0.13), int(h * 0.34), int(h * 0.70)
    last = x0
    for i in range(n):
        x = x0 + i * (cw + gap)
        last = x
        d.rectangle([x - 8, top - 16, x + cw + 8, top], fill=GOLD + (170,))
        d.rectangle([x - 12, bot, x + cw + 12, bot + 16], fill=GOLD + (170,))
        d.rectangle([x, top, x + cw, bot], outline=GOLD_HI + (220,), width=3)
        for f in range(1, 4):
            fx = x + int(cw * f / 4)
            _glow_line(d, (fx, top + 6), (fx, bot - 6), GOLD, 1, 110)
    left, right = x0 - 18, last + cw + 18
    d.polygon([(left, top - 16), (right, top - 16), ((left + right) / 2, top - 96)],
              outline=GOLD_HI + (220,), width=3)


def motif_vault(d, w, h, rnd):
    """Scarcity/security: a vault door ajar to a seam of golden light."""
    cx, cy, R = w // 2, h // 2, int(w * 0.33)
    for rr, al in ((R + 24, 40), (R + 10, 80)):
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=GOLD + (al,))
    d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=GOLD_HI + (255,), width=8)
    d.ellipse([cx - int(R * 0.8), cy - int(R * 0.8),
               cx + int(R * 0.8), cy + int(R * 0.8)], outline=GOLD + (160,), width=4)
    for k in range(8):
        ang = k * math.pi / 4
        p0 = (cx + int(math.cos(ang) * R * 0.2), cy + int(math.sin(ang) * R * 0.2))
        p1 = (cx + int(math.cos(ang) * R * 0.78), cy + int(math.sin(ang) * R * 0.78))
        _glow_line(d, p0, p1, GOLD_HI, 4, 200)
    d.ellipse([cx - int(R * 0.18), cy - int(R * 0.18),
               cx + int(R * 0.18), cy + int(R * 0.18)], outline=GOLD_HI + (255,), width=6)
    d.rectangle([cx - 5, cy - R, cx + 5, cy + R], fill=GOLD_HI + (120,))
    for k in range(12):
        ang = k * math.pi / 6
        bx, by = cx + int(math.cos(ang) * R * 0.9), cy + int(math.sin(ang) * R * 0.9)
        d.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=GOLD_HI + (220,))


MOTIFS = {
    "network": motif_network,
    "scarcity": motif_scarcity,
    "erosion": motif_erosion,
    "supply-chain": motif_supply,
    "monetary-history": motif_history,
    "vault": motif_vault,
}


def make_motif(theme, w=1080, h=1920, seed=7):
    if theme not in MOTIFS:
        raise SystemExit(f"unknown theme '{theme}'. choose: {', '.join(MOTIFS)}")
    rnd = random.Random(seed)
    img = add_gold_dust(gradient_bg(w, h).convert("RGBA"), density=0.00010, seed=seed)
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    MOTIFS[theme](ImageDraw.Draw(layer), w, h, rnd)
    img.alpha_composite(layer.filter(ImageFilter.GaussianBlur(0.6)))
    img.alpha_composite(layer)
    return vignette(img, strength=0.40).convert("RGB")


def load_coin(size_px):
    """Load the reference coin as a true circle at the requested pixel diameter.

    The source asset is 1920x1905 - 0.8% wider than tall - so a naive paste
    renders a subtle ellipse (an 8px error at 1080px, visible on the rim).
    Squaring the canvas first forces a real circle.
    """
    if not os.path.exists(COIN_REF):
        raise SystemExit(
            f"COIN REFERENCE MISSING: {COIN_REF}\n"
            "The DGD coin must be composited from the reference asset, never generated.\n"
            "Restore 'Knowledge Base/Coin Ref/nbgdgd.png' (transparent-background coin)."
        )
    im = Image.open(COIN_REF).convert("RGBA")
    n = max(im.size)
    if im.size[0] != im.size[1]:
        im = im.resize((n, n), Image.LANCZOS)      # de-squash to a true circle
    return im.resize((int(size_px), int(size_px)), Image.LANCZOS)


def _tint(img, f):
    """Multiply RGB brightness by f, preserving alpha."""
    r, g, b, a = img.split()
    lut = [max(0, min(255, int(i * f))) for i in range(256)]
    return Image.merge("RGBA", (r.point(lut), g.point(lut), b.point(lut), a))


def _rim_band(w, h, seed=3):
    """The coin's rim, seen edge-on: a shaded gold band with fine striations.

    Colours sampled from the Saint-Gaudens edge reference (sggp2.jpg), which
    runs from deep shadow (60,42,8) to catchlight (232,200,120).
    """
    band = Image.new("RGBA", (max(1, w), max(1, h)), (0, 0, 0, 0))
    d = ImageDraw.Draw(band)
    rnd = random.Random(seed)
    for x in range(max(1, w)):
        t = x / max(1, w - 1)
        # cylindrical falloff: bright through the middle, dark at both extremes
        curve = math.sin(math.pi * t) ** 0.55
        jitter = 1.0 + (rnd.random() - 0.5) * 0.20          # lettering / reeding
        f = max(0.0, min(1.0, curve * jitter))
        col = (int(60 + (232 - 60) * f),
               int(42 + (200 - 42) * f),
               int(8 + (120 - 8) * f), 255)
        d.line([(x, 0), (x, h)], fill=col)
    return band


def render_coin_pose(diameter, angle=0.0, axis="flip", spin=0.0,
                     thickness_ratio=COIN_THICKNESS_RATIO, back=None,
                     back_mode="same"):
    """Render the coin at an arbitrary rotation, with a correctly-scaled rim.

    axis:
      'spin'   - in-plane rotation. A coin spinning flat-on, like a record.
      'flip'   - rotation about the HORIZONTAL axis; the face foreshortens
                 vertically and the rim appears above or below it.
      'tumble' - rotation about the VERTICAL axis; foreshortens horizontally.

    The rim thickness is driven by the real 2.41mm / 34.1mm ratio (7.07% of the
    diameter), which is what makes a turning coin read as a coin instead of a
    flat disc. Override with thickness_ratio for stylised or oversized renders.

    Only one face exists in the reference set, so the reverse is approximated:
      back_mode='same'   (default) the reverse reads upright, exactly like the
                         obverse - what a medal-aligned two-sided coin looks
                         like, and it keeps the legend readable through a flip.
      back_mode='mirror' the strict mirror. Physically what a single-sided disc
                         would do, but it renders the legend upside down, which
                         viewers read as a rendering bug.
    Pass back=<path> once a true reverse asset exists - it beats both.
    """
    D = max(2, int(diameter))
    th = math.radians(angle)
    c, s = math.cos(th), math.sin(th)

    front = load_coin(D)
    if spin:
        front = front.rotate(-spin, resample=Image.BICUBIC)

    if axis == "spin":
        return front.rotate(-angle, resample=Image.BICUBIC)

    # Work in "flip" space; tumble is the same maths on a transposed canvas.
    transposed = (axis == "tumble")
    if transposed:
        front = front.transpose(Image.ROTATE_90)

    if back:
        rear = Image.open(back).convert("RGBA").resize((D, D), Image.LANCZOS)
        if transposed:
            rear = rear.transpose(Image.ROTATE_90)
    elif back_mode == "mirror":
        rear = ImageOps.flip(front)
    else:
        rear = front
    face_src = front if c >= 0 else rear

    face_h = int(round(D * abs(c)))                   # foreshortened face
    rim_h = int(round(D * thickness_ratio * abs(s)))  # visible rim
    if face_h < 1 and rim_h < 1:
        face_h = 1                                    # degenerate: keep 1px alive
    H = max(1, face_h + rim_h)
    out = Image.new("RGBA", (D, H), (0, 0, 0, 0))

    if rim_h > 0:
        # Silhouette: two ellipses (face at each end of the extrusion) joined by
        # the rim. Union is a capsule; the face then sits on one end of it.
        mask = Image.new("L", (D, H), 0)
        md = ImageDraw.Draw(mask)
        eh = max(1, face_h)                 # exactly edge-on: face has no height
        md.ellipse([0, 0, D - 1, eh - 1], fill=255)
        md.ellipse([0, rim_h, D - 1, eh + rim_h - 1], fill=255)
        md.rectangle([0, eh // 2, D - 1, eh // 2 + rim_h], fill=255)
        rim = _rim_band(D, H)
        rim.putalpha(mask)
        out.alpha_composite(rim)

    if face_h >= 1:
        face = face_src.resize((D, face_h), Image.LANCZOS)
        # sin(2t) > 0 -> the far side is the top, so the rim shows below the face
        face_y = 0 if math.sin(2 * th) > 0 else rim_h
        out.alpha_composite(face, (0, face_y))

    # Light falls off as the face turns away from the viewer.
    out = _tint(out, 0.74 + 0.26 * abs(c))
    if transposed:
        out = out.transpose(Image.ROTATE_270)
    return out


def coin_diameter_px(frame_w, preset="hero", mm=None, ppmm=None):
    """Resolve a coin diameter in px from either a preset or physical scale."""
    if mm is not None and ppmm is not None:
        raise SystemExit("use --mm or --ppmm, not both")
    if ppmm is not None:
        return COIN_MM * ppmm                       # scene scale: px per mm
    if mm is not None:
        # caller states how wide the frame is in mm; coin keeps its true size
        return frame_w * (COIN_MM / mm)
    if preset not in COIN_PRESETS:
        raise SystemExit(f"unknown preset '{preset}'. "
                         f"choose from: {', '.join(COIN_PRESETS)}")
    return frame_w * COIN_PRESETS[preset]


def make_coin(preset="hero", w=1080, h=1920, onto=None, plate=True,
              shadow=True, mm=None, ppmm=None, cx=None, cy=None, seed=7,
              diameter=None, angle=0.0, axis="flip", spin=0.0,
              thickness_ratio=None, back=None, back_mode="same"):
    """Composite the reference coin onto a plate, a supplied scene, or nothing.

    Renders exactly ONE coin. Stacks, piles and heaps are wealth-accumulation
    imagery and are out of bounds per the compliance rail - so there is
    deliberately no --count option.
    """
    if onto:
        base = Image.open(onto).convert("RGBA")
        w, h = base.size
    elif plate:
        base = gradient_bg(w, h).convert("RGBA")
        base = add_gold_dust(base, seed=seed)
        base = vignette(base, strength=0.45)
    else:
        base = Image.new("RGBA", (w, h), (0, 0, 0, 0))

    # --diameter sizes the coin freely (hero / monumental / abstract work);
    # presets and --mm/--ppmm anchor it to its real 34.1mm size.
    d = int(diameter) if diameter else int(round(coin_diameter_px(w, preset, mm, ppmm)))
    if d < 100:
        sys.stderr.write(
            f"note: coin is {d}px across - below ~100px the rings and legend "
            "stop reading as a coin.\n")
    if not diameter and d > max(w, h) * 3:
        raise SystemExit(f"coin would be {d}px in a {w}x{h} frame - check --mm/--ppmm")

    if angle or spin:
        coin = render_coin_pose(d, angle, axis, spin=spin, back=back,
                                back_mode=back_mode,
                                thickness_ratio=(COIN_THICKNESS_RATIO
                                                 if thickness_ratio is None
                                                 else thickness_ratio))
    else:
        coin = load_coin(d)
    cw, ch = coin.size
    x = int((cx if cx is not None else w / 2) - cw / 2)
    y = int((cy if cy is not None else h / 2) - ch / 2)

    if shadow:
        # contact shadow - an unshadowed coin floats off the plate
        sh = Image.new("RGBA", base.size, (0, 0, 0, 0))
        sd = ImageDraw.Draw(sh)
        off = max(2, int(cw * 0.035))
        sd.ellipse([x + off, y + off * 1.6, x + cw + off, y + ch + off * 1.6],
                   fill=(0, 0, 0, 110))
        sh = sh.filter(ImageFilter.GaussianBlur(max(3, int(cw * 0.045))))
        base.alpha_composite(sh)

    base.alpha_composite(coin, (x, y))
    return base


MOTION_MODES = ("spin", "flip", "tumble", "orbit", "wobble")


def make_coin_motion(mode="flip", frames=48, w=1080, h=1920, diameter=None,
                     preset="hero", plate=True, turns=1.0, thickness_ratio=None,
                     back=None, back_mode="same", seed=7):
    """Render a looping motion cycle of the coin as a list of RGBA frames.

    Every mode returns a SEAMLESS loop - frame N continues into frame 0 - so the
    sequence can be looped in the edit without a visible seam.

      spin    in-plane rotation, face always toward camera
      flip    end over end, about the horizontal axis
      tumble  about the vertical axis
      wobble  a settling coin: tilts back and forth without going fully over
      orbit   travels an elliptical path with perspective scaling, while turning
    """
    if mode not in MOTION_MODES:
        raise SystemExit(f"unknown mode '{mode}'. choose from: {', '.join(MOTION_MODES)}")
    tr = COIN_THICKNESS_RATIO if thickness_ratio is None else thickness_ratio
    D = int(diameter) if diameter else int(round(coin_diameter_px(w, preset)))
    if mode == "orbit":
        D = int(D * 0.62)                     # leave room for the path

    # The plate is identical in every frame - build it once, then copy.
    if plate:
        plate_img = gradient_bg(w, h).convert("RGBA")
        plate_img = add_gold_dust(plate_img, seed=seed)
        plate_img = vignette(plate_img, strength=0.45)
    else:
        plate_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))

    out = []
    for i in range(frames):
        t = i / frames                        # 0..1, exclusive of 1 -> seamless
        base = plate_img.copy()

        ang = 360.0 * turns * t
        cx, cy, scale, spin = w / 2, h / 2, 1.0, 0.0

        if mode == "spin":
            coin = render_coin_pose(D, ang, "spin", thickness_ratio=tr, back=back,
                                     back_mode=back_mode)
        elif mode in ("flip", "tumble"):
            coin = render_coin_pose(D, ang, mode, thickness_ratio=tr, back=back,
                                    back_mode=back_mode)
        elif mode == "wobble":
            # a coin settling: decaying tilt, never passing edge-on
            coin = render_coin_pose(D, 62.0 * math.sin(2 * math.pi * t), "flip",
                                    spin=18.0 * math.sin(4 * math.pi * t),
                                    thickness_ratio=tr, back=back,
                                    back_mode=back_mode)
        else:  # orbit
            phase = 2 * math.pi * t
            cx = w / 2 + math.sin(phase) * (w * 0.26)
            cy = h / 2 + math.cos(phase) * (h * 0.055)
            scale = 0.80 + 0.20 * (1 + math.cos(phase)) / 2   # nearer = larger
            coin = render_coin_pose(int(D * scale), ang, "tumble",
                                    thickness_ratio=tr, back=back,
                                    back_mode=back_mode)

        cw, ch = coin.size
        base.alpha_composite(coin, (int(cx - cw / 2), int(cy - ch / 2)))
        out.append(base)
    return out


def save_motion(frames, outdir, gif=None, webp=None, fps=24, flatten=CHARCOAL):
    """Write PNG frames, plus optional animated GIF / WebP."""
    os.makedirs(outdir, exist_ok=True)
    for i, f in enumerate(frames):
        f.save(os.path.join(outdir, f"frame_{i:03d}.png"))
    print(f"wrote {len(frames)} frames to {outdir}  ({frames[0].size[0]}x{frames[0].size[1]})")

    dur = int(round(1000.0 / max(1, fps)))
    if webp:
        frames[0].save(webp, save_all=True, append_images=frames[1:],
                       duration=dur, loop=0, lossless=False, quality=88)
        print(f"wrote {webp}  ({fps}fps, alpha preserved)")
    if gif:
        # GIF has no partial alpha - flatten onto a solid plate first.
        flat = []
        for f in frames:
            bg = Image.new("RGBA", f.size, flatten + (255,))
            bg.alpha_composite(f)
            flat.append(bg.convert("P", palette=Image.ADAPTIVE, colors=200))
        flat[0].save(gif, save_all=True, append_images=flat[1:],
                     duration=dur, loop=0, optimize=True)
        print(f"wrote {gif}  ({fps}fps, flattened - GIF cannot hold alpha)")


def make_contact_sheet(indir, out, cols=4, title=None):
    """Composite every asset PNG in a folder into one labelled preview image."""
    files = sorted(f for f in os.listdir(indir)
                   if f.lower().endswith(".png") and not f.startswith("_"))
    if not files:
        raise SystemExit(f"no PNGs in {indir}")
    cell_w, cell_h, pad, label_h = 300, 400, 16, 30
    rows = (len(files) + cols - 1) // cols
    head = 64 if title else pad
    W = cols * cell_w + pad
    H = head + rows * (cell_h + label_h) + pad
    sheet = Image.new("RGB", (W, H), (12, 16, 28))
    d = ImageDraw.Draw(sheet)
    if title:
        d.text((pad, 30), title, font=_font(SANS_BOLD, 30), fill=GOLD, anchor="lm")
    for i, fn in enumerate(files):
        r, c = divmod(i, cols)
        x0, y0 = pad + c * cell_w, head + r * (cell_h + label_h)
        im = Image.open(os.path.join(indir, fn)).convert("RGBA")
        backing = Image.new("RGBA", im.size, (20, 26, 44, 255))  # reveal transparents
        backing.alpha_composite(im)
        thumb = backing.convert("RGB")
        thumb.thumbnail((cell_w - pad * 2, cell_h - pad), Image.LANCZOS)
        px = x0 + (cell_w - thumb.width) // 2
        py = y0 + (cell_h - thumb.height) // 2
        sheet.paste(thumb, (px, py))
        d.rectangle([px, py, px + thumb.width, py + thumb.height],
                    outline=(44, 52, 72), width=1)
        d.text((x0 + cell_w / 2, y0 + cell_h + label_h / 2), fn,
               font=_font(SANS_BOLD, 18), fill=WHITE, anchor="mm")
    sheet.save(out)
    return out


def make_kit(outdir, headline, kicker=None, subtitle=None, themes=None, seed=7):
    """Render a brief's whole asset set into one folder."""
    os.makedirs(outdir, exist_ok=True)
    written = []

    def save(img, name):
        path = os.path.join(outdir, name)
        img.save(path)
        written.append(name)
        print(f"wrote {path}  ({img.size[0]}x{img.size[1]})")

    # 00 sorts first so the existing 01-10 timeline map is undisturbed.
    try:
        save(make_coin(preset="hero", seed=seed), "00_coin.png")
    except SystemExit as e:
        print(f"skipping coin: {e}")

    save(make_title(headline, kicker, subtitle, seed=seed), "01_title.png")
    save(make_thumb(headline, kicker, seed=seed + 4), "02_thumb.png")
    save(make_disclosure(), "03_disclosure.png")
    save(make_lower_third("Not financial advice - Educational"), "04_lower_third.png")
    themes = themes or ["network", "scarcity", "erosion", "supply-chain"]
    for i, th in enumerate(themes, start=5):
        save(make_motif(th, seed=seed + i), f"{i:02d}_motif_{th.replace('-', '_')}.png")
    sheet = os.path.join(outdir, "_contact.png")
    make_contact_sheet(outdir, sheet, title=f"{kicker or 'DGD'} - asset set")
    print(f"contact sheet: {sheet}")
    print(f"kit complete: {len(written)} files (+ preview) in {outdir}")
    return written


def main():
    p = argparse.ArgumentParser(description="DGD brand asset generator")
    sub = p.add_subparsers(dest="cmd", required=True)

    pt = sub.add_parser("title")
    pt.add_argument("--headline", required=True)
    pt.add_argument("--kicker")
    pt.add_argument("--subtitle")
    pt.add_argument("--no-disclosure", action="store_true")
    pt.add_argument("--seed", type=int, default=7)
    pt.add_argument("--out", required=True)

    th = sub.add_parser("thumb")
    th.add_argument("--headline", required=True)
    th.add_argument("--kicker")
    th.add_argument("--seed", type=int, default=11)
    th.add_argument("--out", required=True)

    ds = sub.add_parser("disclosure")
    ds.add_argument("--out", required=True)

    lt = sub.add_parser("lower")
    lt.add_argument("--text", required=True)
    lt.add_argument("--out", required=True)

    mo = sub.add_parser("motif")
    mo.add_argument("--theme", required=True, choices=list(MOTIFS))
    mo.add_argument("--seed", type=int, default=7)
    mo.add_argument("--out", required=True)

    kt = sub.add_parser("kit")
    kt.add_argument("--headline", required=True)
    kt.add_argument("--kicker")
    kt.add_argument("--subtitle")
    kt.add_argument("--themes", help="comma-separated motif themes (default: 4 core)")
    kt.add_argument("--seed", type=int, default=7)
    kt.add_argument("--outdir", required=True)

    cn = sub.add_parser("coin", help="composite the reference DGD coin (never generated)")
    cn.add_argument("--preset", default="hero", choices=list(COIN_PRESETS),
                    help="coin width as a share of frame width (default: hero)")
    cn.add_argument("--onto", help="composite onto this image instead of a plate")
    cn.add_argument("--no-plate", action="store_true",
                    help="transparent background instead of a navy plate")
    cn.add_argument("--no-shadow", action="store_true")
    cn.add_argument("--mm", type=float,
                    help="frame width in mm; coin holds its true 34.1mm size")
    cn.add_argument("--ppmm", type=float, help="scene scale in pixels per mm")
    cn.add_argument("--cx", type=int, help="coin centre x (default: centred)")
    cn.add_argument("--cy", type=int, help="coin centre y (default: centred)")
    cn.add_argument("--diameter", type=int,
                    help="coin width in px - free sizing, ignores physical scale")
    cn.add_argument("--angle", type=float, default=0.0,
                    help="rotate the coin (degrees); rim appears as it turns")
    cn.add_argument("--axis", default="flip", choices=("flip", "tumble", "spin"))
    cn.add_argument("--spin", type=float, default=0.0,
                    help="extra in-plane rotation, degrees")
    cn.add_argument("--thickness", type=float,
                    help=f"rim as a share of diameter (default {COIN_THICKNESS_RATIO:.4f} = true)")
    cn.add_argument("--back", help="true reverse-face asset, if one exists")
    cn.add_argument("--back-mode", default="same", choices=("same", "mirror"),
                    help="how to fake the reverse when --back is absent")
    cn.add_argument("--width", type=int, default=1080)
    cn.add_argument("--height", type=int, default=1920)
    cn.add_argument("--seed", type=int, default=7)
    cn.add_argument("--out", required=True)

    cm = sub.add_parser("coin-motion",
                        help="looping motion cycle: spin / flip / tumble / orbit / wobble")
    cm.add_argument("--mode", default="flip", choices=MOTION_MODES)
    cm.add_argument("--frames", type=int, default=48)
    cm.add_argument("--fps", type=int, default=24)
    cm.add_argument("--turns", type=float, default=1.0,
                    help="full rotations across the loop (default 1)")
    cm.add_argument("--preset", default="hero", choices=list(COIN_PRESETS))
    cm.add_argument("--diameter", type=int, help="free sizing in px")
    cm.add_argument("--thickness", type=float, help="rim as a share of diameter")
    cm.add_argument("--back", help="true reverse-face asset, if one exists")
    cm.add_argument("--back-mode", default="same", choices=("same", "mirror"))
    cm.add_argument("--no-plate", action="store_true",
                    help="transparent frames, for compositing over your own footage")
    cm.add_argument("--width", type=int, default=1080)
    cm.add_argument("--height", type=int, default=1920)
    cm.add_argument("--gif", help="also write an animated GIF (flattened)")
    cm.add_argument("--webp", help="also write an animated WebP (keeps alpha)")
    cm.add_argument("--seed", type=int, default=7)
    cm.add_argument("--outdir", required=True)

    cs = sub.add_parser("contact-sheet")
    cs.add_argument("--indir", required=True)
    cs.add_argument("--cols", type=int, default=4)
    cs.add_argument("--title")
    cs.add_argument("--out", required=True)

    a = p.parse_args()

    hits = compliance_scan(*[getattr(a, k, None)
                             for k in ("headline", "kicker", "subtitle", "text")])
    if hits:
        sys.stderr.write("COMPLIANCE FAIL - banned framing in text:\n")
        for t, hit in hits:
            sys.stderr.write(f"  '{hit}' in: {t!r}\n")
        sys.stderr.write("Reframe to design/idea language (mechanism, not forecast).\n")
        sys.exit(2)

    if a.cmd == "kit":
        themes = [t.strip() for t in a.themes.split(",")] if a.themes else None
        make_kit(a.outdir, a.headline, a.kicker, a.subtitle, themes, seed=a.seed)
        return

    if a.cmd == "contact-sheet":
        print(f"wrote {make_contact_sheet(a.indir, a.out, cols=a.cols, title=a.title)}")
        return

    if a.cmd == "coin-motion":
        frames = make_coin_motion(
            mode=a.mode, frames=a.frames, w=a.width, h=a.height,
            diameter=a.diameter, preset=a.preset, plate=not a.no_plate,
            turns=a.turns, thickness_ratio=a.thickness, back=a.back,
            back_mode=a.back_mode, seed=a.seed)
        save_motion(frames, a.outdir, gif=a.gif, webp=a.webp, fps=a.fps)
        return

    if a.cmd == "title":
        img = make_title(a.headline, a.kicker, a.subtitle,
                         disclosure=not a.no_disclosure, seed=a.seed)
    elif a.cmd == "thumb":
        img = make_thumb(a.headline, a.kicker, seed=a.seed)
    elif a.cmd == "disclosure":
        img = make_disclosure()
    elif a.cmd == "lower":
        img = make_lower_third(a.text)
    elif a.cmd == "motif":
        img = make_motif(a.theme, seed=a.seed)
    elif a.cmd == "coin":
        img = make_coin(preset=a.preset, w=a.width, h=a.height, onto=a.onto,
                        plate=not a.no_plate, shadow=not a.no_shadow,
                        mm=a.mm, ppmm=a.ppmm, cx=a.cx, cy=a.cy, seed=a.seed,
                        diameter=a.diameter, angle=a.angle, axis=a.axis,
                        spin=a.spin, thickness_ratio=a.thickness, back=a.back,
                        back_mode=a.back_mode)
    img.save(a.out)
    print(f"wrote {a.out}  ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
