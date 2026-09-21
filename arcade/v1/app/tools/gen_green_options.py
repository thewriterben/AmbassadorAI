"""Candidate greens for the sixth Coin Quest piece, shown in context.

The sixth piece has to do a hard job: sit on a near-black board beside a very
dark Old Glory Blue without the two reading as "the dark one" at a glance.
Money green pulls dark, the navy is already dark, and that is the most likely
reason the first pass didn't land. So every candidate below is paired with a
light outline ring and rendered next to the whole set, not on its own.

Writes one contact sheet: each row is the full six-piece set with a different
green, labelled, over the real board colour.
"""
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = r"C:\src\puzzle-app\assets\images"
SHEET = r"C:\src\green_options.png"
S = 128          # piece size on the sheet
SS = 4
N = S * SS
BOARD = (8, 8, 9, 255)

# The five that are settled, for context.
FIXED = {
    "gold":   ((242, 176, 30),  (255, 214, 120), (92, 62, 4)),
    "silver": ((154, 165, 177), (214, 223, 232), (58, 66, 76)),
    "copper": ((193, 112, 58),  (236, 168, 120), (74, 40, 18)),
    "red":    ((179, 25, 66),   (240, 126, 156), (74, 8, 26)),
    "blue":   ((10, 49, 97),    (108, 156, 224), (4, 20, 44)),
}

# fill, ring, mark  — ordered darkest to lightest.
GREENS = [
    ("A  currency ink   #0E4F38", ((14, 79, 56),   (96, 190, 150), (4, 30, 21))),
    ("B  shipped now    #14663B", ((20, 102, 59),  (108, 200, 150), (6, 40, 22))),
    ("C  pine           #1B5E20", ((27, 94, 32),   (118, 196, 124), (8, 34, 10))),
    ("D  bank note      #2E7D52", ((46, 125, 82),  (140, 220, 178), (14, 46, 30))),
    ("E  kelly          #1E8A4C", ((30, 138, 76),  (148, 232, 180), (10, 50, 28))),
    ("F  material 600   #388E3C", ((56, 142, 60),  (160, 226, 162), (18, 52, 20))),
    ("G  jade           #17A673", ((23, 166, 115), (150, 240, 205), (6, 58, 40))),
]


def canvas(size=N):
    return Image.new("RGBA", (size, size), (0, 0, 0, 0))


def elevation(mask, blur=0.035, drop=0.030, alpha=120):
    sh = canvas()
    sh.paste((0, 0, 0, alpha), (0, int(N * drop)), mask)
    return sh.filter(ImageFilter.GaussianBlur(N * blur))


_logo_cache = {}


def logo(size, color):
    key = (size, color)
    if key in _logo_cache:
        return _logo_cache[key]
    src = Image.open(os.path.join(OUT, "logo_white.png")).convert("RGBA")
    src = src.resize((size, size), Image.LANCZOS)
    flat = Image.new("RGBA", (size, size), color + (0,))
    flat.putalpha(src.getchannel("A"))
    _logo_cache[key] = flat
    return flat


def piece(fill, ring, mark):
    """Same geometry as gen_material_pieces.piece, at sheet resolution."""
    img = canvas()
    pad = N * 0.085
    m = Image.new("L", (N, N), 0)
    ImageDraw.Draw(m).ellipse((pad, pad, N - pad, N - pad), fill=255)

    out = canvas()
    out.alpha_composite(elevation(m))

    d = ImageDraw.Draw(img)
    d.ellipse((pad, pad, N - pad, N - pad), fill=fill + (255,))
    d.ellipse((pad, pad, N - pad, N - pad), outline=ring + (255,), width=int(N * 0.030))
    ip = N * 0.20
    d.ellipse((ip, ip, N - ip, N - ip), outline=ring + (70,), width=int(N * 0.016))

    lg = int(N * 0.44)
    img.alpha_composite(logo(lg, mark), ((N - lg) // 2, (N - lg) // 2))
    out.alpha_composite(img)
    return out.resize((S, S), Image.LANCZOS)


def font(sz):
    for p in (r"C:\Windows\Fonts\consola.ttf", r"C:\Windows\Fonts\arial.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()


def main():
    label_w = 230
    row_h = S + 18
    cols = len(FIXED) + 1
    w = label_w + cols * S + 24
    h = 40 + len(GREENS) * row_h + 12

    sheet = Image.new("RGBA", (w, h), BOARD)
    d = ImageDraw.Draw(sheet)
    f = font(15)
    fh = font(17)

    d.text((14, 14), "sixth piece — candidates, shown with the settled five",
           font=fh, fill=(232, 232, 236, 255))

    fixed_imgs = [piece(*v) for v in FIXED.values()]

    for r, (name, (fill, ring, mark)) in enumerate(GREENS):
        y = 40 + r * row_h
        d.text((14, y + S // 2 - 8), name, font=f, fill=(206, 208, 214, 255))
        x = label_w
        for im in fixed_imgs:
            sheet.alpha_composite(im, (x, y))
            x += S
        sheet.alpha_composite(piece(fill, ring, mark), (x, y))
        # Hairline under each row so the rows read as separate sets.
        d.line((14, y + row_h - 8, w - 14, y + row_h - 8), fill=(30, 30, 34, 255))

    sheet.convert("RGB").save(SHEET, optimize=True)
    print(f"wrote {SHEET}  ({os.path.getsize(SHEET) // 1024} KB)")


if __name__ == "__main__":
    main()
