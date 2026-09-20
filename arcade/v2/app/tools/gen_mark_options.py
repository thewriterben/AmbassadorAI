"""Legibility treatments for the DGD mark on a board piece.

The mark currently renders as a dark tint of the piece's own hue at 44% of the
coin, with a faint inner ring just outside it. Three things work against it:

  * a dark tint of the same hue is a small luminance step, and hue contrast
    does almost nothing at this size;
  * the decorative inner ring is concentric with the mark's own circular form,
    so the two merge into rings-inside-rings;
  * we last judged it on a 256 px contact sheet. On a 9-column board it lands
    near 44 logical px.

So every option below is rendered at the size it is actually used, with a 3x
inspection blow-up beside it.
"""
import os

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

OUT = r"C:\src\puzzle-app\assets\images"
SHEET = r"C:\src\mark_options.png"
CELL = 52           # roughly a board cell in logical pixels
SS = 8              # supersample for the render, then down to CELL
N = CELL * SS
BOARD = (8, 8, 9, 255)

# fill, ring, current dark mark
PALETTE = {
    "gold":   ((242, 176, 30),  (255, 214, 120), (92, 62, 4)),
    "silver": ((154, 165, 177), (214, 223, 232), (58, 66, 76)),
    "copper": ((193, 112, 58),  (236, 168, 120), (74, 40, 18)),
    "red":    ((179, 25, 66),   (240, 126, 156), (74, 8, 26)),
    "blue":   ((10, 49, 97),    (108, 156, 224), (4, 20, 44)),
    "green":  ((30, 138, 76),   (148, 232, 180), (10, 50, 28)),
}


def luminance(c):
    r, g, b = [v / 255 for v in c]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def on_color(fill):
    """Material's 'on-color' rule: whichever of black/white contrasts more."""
    return (10, 12, 14) if luminance(fill) > 0.42 else (255, 255, 255)


_logo_cache = {}


def logo_alpha(size):
    if size not in _logo_cache:
        src = Image.open(os.path.join(OUT, "logo_white.png")).convert("RGBA")
        _logo_cache[size] = src.resize((size, size), Image.LANCZOS).getchannel("A")
    return _logo_cache[size]


def tinted(size, color, alpha=255):
    a = logo_alpha(size)
    flat = Image.new("RGBA", (size, size), tuple(color) + (0,))
    if alpha != 255:
        a = a.point(lambda v: int(v * alpha / 255))
    flat.putalpha(a)
    return flat


def base(fill, ring, inner_ring=True):
    img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    pad = N * 0.085
    d.ellipse((pad, pad, N - pad, N - pad), fill=tuple(fill) + (255,))
    d.ellipse((pad, pad, N - pad, N - pad), outline=tuple(ring) + (255,), width=int(N * 0.030))
    if inner_ring:
        ip = N * 0.20
        d.ellipse((ip, ip, N - ip, N - ip), outline=tuple(ring) + (70,), width=int(N * 0.016))
    return img


def place(img, mark, frac):
    sz = int(N * frac)
    img.alpha_composite(mark, ((N - sz) // 2, (N - sz) // 2))
    return img


# ---------------------------------------------------------------- treatments

def t_current(fill, ring, dark):
    return place(base(fill, ring, True), tinted(int(N * 0.44), dark), 0.44)


def t_oncolor(fill, ring, dark):
    return place(base(fill, ring, False), tinted(int(N * 0.44), on_color(fill)), 0.44)


def t_oncolor_big(fill, ring, dark):
    return place(base(fill, ring, False), tinted(int(N * 0.54), on_color(fill)), 0.54)


def t_ringcolor(fill, ring, dark):
    return place(base(fill, ring, False), tinted(int(N * 0.54), ring), 0.54)


def t_halo(fill, ring, dark):
    """On-colour mark with a soft dark halo, so it holds on any fill."""
    img = base(fill, ring, False)
    sz = int(N * 0.54)
    a = logo_alpha(sz)
    halo = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (sz, sz), (0, 0, 0, 0))
    shadow.putalpha(a.point(lambda v: int(v * 0.55)))
    halo.alpha_composite(shadow, ((N - sz) // 2, (N - sz) // 2))
    halo = halo.filter(ImageFilter.GaussianBlur(N * 0.018))
    img.alpha_composite(halo)
    return place(img, tinted(sz, on_color(fill)), 0.54)


def t_knockout(fill, ring, dark):
    """The mark punched clean out of the coin, showing the board behind."""
    img = base(fill, ring, False)
    sz = int(N * 0.54)
    a = logo_alpha(sz)
    hole = Image.new("L", (N, N), 0)
    hole.paste(a, ((N - sz) // 2, (N - sz) // 2))
    # Keep the coin's silhouette, subtract only where the mark is.
    img.putalpha(ImageChops.subtract(img.getchannel("A"), hole))
    return img


TREATMENTS = [
    ("A  current  dark tint + inner ring", t_current),
    ("B  on-colour mark, no inner ring", t_oncolor),
    ("C  on-colour, larger (0.54)", t_oncolor_big),
    ("D  ring-colour mark, larger", t_ringcolor),
    ("E  on-colour + soft halo", t_halo),
    ("F  knocked out of the coin", t_knockout),
]


def font(sz):
    for p in (r"C:\Windows\Fonts\consola.ttf", r"C:\Windows\Fonts\arial.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()


def main():
    label_w = 300
    zoom = 3
    gap = 10
    row_h = max(CELL, CELL * zoom) + 16
    w = label_w + len(PALETTE) * (CELL + gap) + 30 + CELL * zoom + 20
    h = 34 + len(TREATMENTS) * row_h

    sheet = Image.new("RGBA", (w, h), BOARD)
    d = ImageDraw.Draw(sheet)
    d.text((14, 12), f"DGD mark legibility — pieces shown at {CELL}px (a board cell), "
                     f"gold blown up {zoom}x at right",
           font=font(14), fill=(232, 232, 236, 255))

    for r, (name, fn) in enumerate(TREATMENTS):
        y = 34 + r * row_h
        d.text((14, y + row_h // 2 - 8), name, font=font(13), fill=(206, 208, 214, 255))
        x = label_w
        for fill, ring, dark in PALETTE.values():
            im = fn(fill, ring, dark).resize((CELL, CELL), Image.LANCZOS)
            sheet.alpha_composite(im, (x, y + (row_h - CELL) // 2 - 8))
            x += CELL + gap
        big = fn(*PALETTE["gold"]).resize((CELL * zoom, CELL * zoom), Image.LANCZOS)
        sheet.alpha_composite(big, (x + 20, y + 2))
        d.line((14, y + row_h - 6, w - 14, y + row_h - 6), fill=(30, 30, 34, 255))

    sheet.convert("RGB").save(SHEET, optimize=True)
    print(f"wrote {SHEET} ({os.path.getsize(SHEET)//1024} KB)")


if __name__ == "__main__":
    main()
