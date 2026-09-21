"""Coin Quest obstacle art: sealed vault, bullion ingot, and ledger seals.

Matches the digitalgold.co palette already used by the coin pieces: near-black
bodies, amber rims, a single soft highlight. Everything is drawn at 4x and
downsampled so the edges stay clean on a phone.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFilter

OUT = r"C:\src\puzzle-app\assets\images"
S = 256
SS = 4  # supersample

AMBER = (234, 149, 45)
AMBER_HI = (255, 175, 78)
INK = (5, 6, 7)
STEEL = (58, 62, 70)
STEEL_HI = (120, 128, 140)
GOLD_LO = (150, 96, 18)
GOLD = (214, 160, 54)
GOLD_HI = (255, 226, 150)


def canvas(size=S * SS):
    return Image.new("RGBA", (size, size), (0, 0, 0, 0))


def finish(img, name):
    img = img.resize((S, S), Image.LANCZOS)
    img.save(os.path.join(OUT, name), optimize=True)
    print(f"{name}  {os.path.getsize(os.path.join(OUT, name)) // 1024} KB")


def rr(d, box, r, **kw):
    d.rounded_rectangle(box, radius=r, **kw)


def vault():
    """A sealed vault door: steel body, amber rim, a dial and four bolts."""
    img = canvas()
    d = ImageDraw.Draw(img)
    n = S * SS
    pad = n * 0.09
    body = (pad, pad, n - pad, n - pad)
    # Body with a vertical steel gradient.
    grad = Image.new("RGBA", (1, int(n)), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for y in range(int(n)):
        t = y / n
        c = tuple(int(STEEL_HI[i] * (1 - t) + STEEL[i] * t) for i in range(3))
        gd.point((0, y), fill=c + (255,))
    grad = grad.resize((int(n), int(n)))
    mask = Image.new("L", (int(n), int(n)), 0)
    rr(ImageDraw.Draw(mask), body, int(n * 0.14), fill=255)
    img.paste(grad, (0, 0), mask)
    # Amber rim.
    rr(d, body, int(n * 0.14), outline=AMBER + (255,), width=int(n * 0.028))
    # Inset panel.
    ip = n * 0.19
    rr(d, (ip, ip, n - ip, n - ip), int(n * 0.10), outline=(0, 0, 0, 90), width=int(n * 0.016))
    # Dial.
    cx = cy = n / 2
    rad = n * 0.17
    d.ellipse((cx - rad, cy - rad, cx + rad, cy + rad), fill=INK + (235,), outline=AMBER + (255,), width=int(n * 0.022))
    for i in range(8):
        a = i * math.pi / 4
        r0, r1 = rad * 0.45, rad * 0.86
        d.line(
            (cx + math.cos(a) * r0, cy + math.sin(a) * r0, cx + math.cos(a) * r1, cy + math.sin(a) * r1),
            fill=AMBER_HI + (215,), width=int(n * 0.016),
        )
    d.ellipse((cx - rad * 0.2, cy - rad * 0.2, cx + rad * 0.2, cy + rad * 0.2), fill=AMBER + (255,))
    # Corner bolts.
    b = n * 0.145
    br = n * 0.028
    for bx, by in ((b, b), (n - b, b), (b, n - b), (n - b, n - b)):
        d.ellipse((bx - br, by - br, bx + br, by + br), fill=STEEL_HI + (255,), outline=INK + (180,), width=int(n * 0.008))
    # Top-left sheen.
    sheen = canvas()
    sd = ImageDraw.Draw(sheen)
    sd.polygon([(pad, pad), (n * 0.62, pad), (pad, n * 0.62)], fill=(255, 255, 255, 34))
    sheen = sheen.filter(ImageFilter.GaussianBlur(n * 0.02))
    img.alpha_composite(Image.composite(sheen, Image.new("RGBA", sheen.size, (0, 0, 0, 0)), mask))
    finish(img, "piece_vault.png")


def ingot():
    """A bullion bar in trimetric: trapezoid top face, two shaded sides."""
    img = canvas()
    d = ImageDraw.Draw(img)
    n = S * SS
    # Footprint
    top_y = n * 0.30
    bot_y = n * 0.76
    top_l, top_r = n * 0.30, n * 0.70
    bot_l, bot_r = n * 0.14, n * 0.86
    # Front face
    d.polygon([(bot_l, bot_y), (bot_r, bot_y), (top_r + n * 0.055, top_y + n * 0.10),
               (top_l - n * 0.055, top_y + n * 0.10)], fill=GOLD + (255,))
    # Top face
    d.polygon([(top_l, top_y), (top_r, top_y), (top_r + n * 0.055, top_y + n * 0.10),
               (top_l - n * 0.055, top_y + n * 0.10)], fill=GOLD_HI + (255,))
    # Right shadow wedge
    d.polygon([(bot_r, bot_y), (top_r + n * 0.055, top_y + n * 0.10), (top_r + n * 0.055, top_y + n * 0.16),
               (bot_r, bot_y + n * 0.02)], fill=GOLD_LO + (255,))
    # Outline
    d.line([(bot_l, bot_y), (bot_r, bot_y), (top_r + n * 0.055, top_y + n * 0.10),
            (top_l - n * 0.055, top_y + n * 0.10), (bot_l, bot_y)], fill=GOLD_LO + (255,), width=int(n * 0.012))
    d.line([(top_l, top_y), (top_r, top_y), (top_r + n * 0.055, top_y + n * 0.10),
            (top_l - n * 0.055, top_y + n * 0.10), (top_l, top_y)], fill=GOLD_LO + (200,), width=int(n * 0.010))
    # Stamp lines on the front face.
    for i, w in enumerate((0.30, 0.22, 0.26)):
        y = top_y + n * (0.22 + i * 0.10)
        d.line((n * 0.5 - n * w / 2, y, n * 0.5 + n * w / 2, y), fill=GOLD_LO + (150,), width=int(n * 0.014))
    # Specular streak across the top face.
    st = canvas()
    sd = ImageDraw.Draw(st)
    sd.polygon([(top_l + n * 0.02, top_y + n * 0.02), (top_l + n * 0.16, top_y + n * 0.02),
                (top_l + n * 0.07, top_y + n * 0.10), (top_l - n * 0.03, top_y + n * 0.10)],
               fill=(255, 255, 255, 120))
    st = st.filter(ImageFilter.GaussianBlur(n * 0.012))
    img.alpha_composite(st)
    # Warm glow.
    glow = canvas()
    ImageDraw.Draw(glow).ellipse((n * 0.10, n * 0.26, n * 0.90, n * 0.86), fill=AMBER + (46,))
    glow = glow.filter(ImageFilter.GaussianBlur(n * 0.05))
    out = canvas()
    out.alpha_composite(glow)
    out.alpha_composite(img)
    finish(out, "piece_ingot.png")


def seal(layers):
    """A wax ledger seal drawn over the cell. Two layers reads heavier."""
    img = canvas()
    d = ImageDraw.Draw(img)
    n = S * SS
    alpha = 150 if layers == 1 else 210
    ring = AMBER if layers == 1 else AMBER_HI
    pad = n * 0.06
    rr(d, (pad, pad, n - pad, n - pad), int(n * 0.16),
       fill=(234, 149, 45, 40 if layers == 1 else 66),
       outline=ring + (alpha,), width=int(n * (0.022 if layers == 1 else 0.034)))
    # Hatching, denser on the second layer.
    step = n * (0.16 if layers == 1 else 0.10)
    x = -n
    while x < n * 2:
        d.line((x, 0, x + n, n), fill=ring + (int(alpha * 0.30),), width=int(n * 0.012))
        x += step
    # Clip the hatching to the rounded square.
    mask = Image.new("L", (int(n), int(n)), 0)
    rr(ImageDraw.Draw(mask), (pad, pad, n - pad, n - pad), int(n * 0.16), fill=255)
    img.putalpha(Image.composite(img.getchannel("A"), Image.new("L", mask.size, 0), mask))
    # Layer pips so the count is readable at a glance.
    if layers == 2:
        pr = n * 0.030
        for i in range(2):
            px = n * 0.5 + (i - 0.5) * n * 0.10
            d.ellipse((px - pr, n * 0.86 - pr, px + pr, n * 0.86 + pr), fill=AMBER_HI + (255,))
    finish(img, f"seal_{layers}.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    vault()
    ingot()
    seal(1)
    seal(2)
