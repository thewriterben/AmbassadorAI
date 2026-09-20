"""App icon: a DGD gold coin.

"Shiny" and "Material" pull against each other — Material is flat, shine is
specular — so this renders four points along that axis and shows them at the
size a launcher actually draws them, on both a dark and a light home screen.
An icon judged at 512 px tells you very little.

Run with no arguments to write the comparison sheet only:

    python tools/gen_app_icon.py

Run with a style letter to install that one everywhere — adaptive layers,
legacy mipmaps, Play listing icon, PWA icons and the in-app asset:

    python tools/gen_app_icon.py C
"""
import os
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter

IMG = r"C:\src\puzzle-app\assets\images"
SHEET = r"C:\src\app_icon_options.png"

SS = 4
N = 256 * SS          # working canvas

GOLD = (242, 176, 30)
GOLD_LIGHT = (255, 214, 120)
GOLD_DEEP = (198, 132, 12)
MARK = (92, 62, 4)

# The coin's share of the icon canvas. Android's adaptive foreground is 108dp
# with only the central 72dp guaranteed visible, so content stays well inside.
COIN = 0.62


def canvas(size=N, rgba=(0, 0, 0, 0)):
    return Image.new("RGBA", (size, size), rgba)


def disc_mask(size, pad):
    m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).ellipse((pad, pad, size - pad, size - pad), fill=255)
    return m


_logo = {}


def logo(size, color, weight=0.011):
    key = (size, color, weight)
    if key in _logo:
        return _logo[key]
    src = Image.open(os.path.join(IMG, "logo_white.png")).convert("RGBA")
    a = src.resize((size, size), Image.LANCZOS).getchannel("A")
    grow = int(size * weight) | 1
    if grow >= 3:
        a = a.filter(ImageFilter.MaxFilter(grow))
    flat = Image.new("RGBA", (size, size), color + (0,))
    flat.putalpha(a)
    _logo[key] = flat
    return flat


def radial(size, inner, outer):
    """Soft radial body light, brighter towards the upper left."""
    g = Image.new("RGBA", (size, size))
    px = g.load()
    cx, cy = size * 0.38, size * 0.34
    maxd = size * 0.95
    for y in range(size):
        for x in range(size):
            d = min(1.0, (((x - cx) ** 2 + (y - cy) ** 2) ** 0.5) / maxd)
            t = d ** 0.9
            px[x, y] = (
                int(inner[0] + (outer[0] - inner[0]) * t),
                int(inner[1] + (outer[1] - inner[1]) * t),
                int(inner[2] + (outer[2] - inner[2]) * t),
                255,
            )
    return g


def sheen(size, mask, strength=110, width=0.26, angle_at=0.34):
    """A single diagonal specular band, clipped to the coin."""
    band = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(band)
    w = size * width
    # A broad diagonal stripe across the upper-left third.
    d.polygon(
        [
            (-size, size * angle_at + w),
            (size * 1.4, -size * 0.5 + w),
            (size * 1.4, -size * 0.5 - w),
            (-size, size * angle_at - w),
        ],
        fill=strength,
    )
    band = band.filter(ImageFilter.GaussianBlur(size * 0.055))
    band = ImageChops.multiply(band, mask)
    out = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    out.putalpha(band)
    return out


def rim(size, pad, color, width, alpha):
    r = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ImageDraw.Draw(r).ellipse((pad, pad, size - pad, size - pad),
                              outline=color + (alpha,), width=int(width))
    return r


def coin(style):
    """One coin at working resolution, transparent outside the disc."""
    size = N
    pad = size * 0.5 * (1 - COIN) * 2 / 2  # inset so the disc spans COIN of the canvas
    pad = size * (1 - COIN) / 2
    mask = disc_mask(size, pad)
    out = canvas(size)

    # Body.
    if style in ("A", "B"):
        body = Image.new("RGBA", (size, size), GOLD + (255,))
    else:
        body = radial(size, GOLD_LIGHT, GOLD_DEEP if style == "D" else GOLD)
    out.paste(body, (0, 0), mask)

    # Outline ring, as on the board pieces.
    out.alpha_composite(rim(size, pad, GOLD_LIGHT, size * 0.022, 255))

    if style == "D":
        # A bevelled edge: a bright inner rim and a dark one opposite it.
        out.alpha_composite(rim(size, pad + size * 0.020, (255, 236, 190), size * 0.016, 190))
        dark = rim(size, pad + size * 0.020, (120, 78, 8), size * 0.016, 150)
        out.alpha_composite(dark.transform(
            (size, size), Image.AFFINE, (1, 0, 0, 0, 1, -size * 0.010)))

    # The mark.
    lg = int(size * COIN * 0.62)
    out.alpha_composite(logo(lg, MARK), ((size - lg) // 2, (size - lg) // 2))

    # Shine, over the mark so it reads as light on the coin's surface.
    if style == "B":
        out.alpha_composite(sheen(size, mask, strength=70))
    elif style == "C":
        out.alpha_composite(sheen(size, mask, strength=105))
    elif style == "D":
        out.alpha_composite(sheen(size, mask, strength=150, width=0.20))
        out.alpha_composite(sheen(size, mask, strength=70, width=0.07, angle_at=0.66))

    # Elevation, so it sits on the launcher rather than floating.
    sh = canvas(size)
    sh.paste((0, 0, 0, 120), (0, int(size * 0.016)), mask)
    sh = sh.filter(ImageFilter.GaussianBlur(size * 0.020))
    base = canvas(size)
    base.alpha_composite(sh)
    base.alpha_composite(out)
    return base


STYLES = {
    "A": "flat, matches the board pieces",
    "B": "flat + soft sheen",
    "C": "graded body + sheen",
    "D": "bevelled edge + hard specular",
}

BG = (14, 13, 12, 255)      # icon plate behind the coin


def sheet():
    from PIL import ImageFont

    def font(sz):
        for p in (r"C:\Windows\Fonts\consola.ttf", r"C:\Windows\Fonts\arial.ttf"):
            if os.path.exists(p):
                return ImageFont.truetype(p, sz)
        return ImageFont.load_default()

    small = 96          # about what a launcher draws
    big = 288
    pad_x, gap = 300, 26
    row_h = big + 34
    w = pad_x + small * 2 + gap * 3 + big + 60
    h = 40 + len(STYLES) * row_h

    out = Image.new("RGBA", (w, h), (24, 24, 28, 255))
    d = ImageDraw.Draw(out)
    d.text((14, 14), "app icon — drawn at launcher size (96px) on dark and light, "
                     "then 3x", font=font(14), fill=(232, 232, 236, 255))

    for i, (k, desc) in enumerate(STYLES.items()):
        y = 40 + i * row_h
        d.text((14, y + row_h // 2 - 16), f"{k}  {desc}", font=font(14),
               fill=(206, 208, 214, 255))
        c = coin(k)

        x = pad_x
        for plate in (BG, (236, 236, 238, 255)):
            tile = Image.new("RGBA", (N, N), plate)
            tile.alpha_composite(c)
            # Launcher-ish rounded mask.
            m = Image.new("L", (N, N), 0)
            ImageDraw.Draw(m).rounded_rectangle((0, 0, N, N), radius=int(N * 0.22), fill=255)
            tile.putalpha(m)
            out.alpha_composite(tile.resize((small, small), Image.LANCZOS),
                                (x, y + (row_h - small) // 2 - 10))
            x += small + gap

        tile = Image.new("RGBA", (N, N), BG)
        tile.alpha_composite(c)
        m = Image.new("L", (N, N), 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, N, N), radius=int(N * 0.22), fill=255)
        tile.putalpha(m)
        out.alpha_composite(tile.resize((big, big), Image.LANCZOS), (x + 20, y + 4))

        d.line((14, y + row_h - 8, w - 14, y + row_h - 8), fill=(44, 44, 50, 255))

    out.convert("RGB").save(SHEET, optimize=True)
    print(f"wrote {SHEET} ({os.path.getsize(SHEET)//1024} KB)")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        from install_app_icon import install
        install(coin(sys.argv[1].upper()), sys.argv[1].upper())
    else:
        sheet()
