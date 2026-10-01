"""Import the unbranded pickups drawn from COIN-PROMPTS.md.

    python tool/art/import_coins.py [--src tool/art/source] [--out assets/images]

Reads coin_gold.png, coin_silver.png and coin_copper.png (any size, on a
magenta #FF00FF background), and writes pickup_gold.png, pickup_silver.png and
pickup_copper.png: 512 px square, transparent, the coin centred and filling the
same share of the square as the DGD coins it replaces (about 99%), so nothing in
the game's sizing changes.

The key is by distance from magenta, with a soft edge, and the magenta cast
that bleeds into antialiased edge pixels is taken back out (the same idea as
the backdrop importer's unmixing, simpler here: a coin's edge only ever mixes
with the one background colour).
"""

import argparse
import os
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
METALS = ("gold", "silver", "copper")
SIZE = 512
FILL = 0.99  # the DGD renders' coin spans 511 of 512 px


def key_magenta(im: Image.Image) -> Image.Image:
    im = im.convert("RGB")
    w, h = im.size
    src = im.load()
    # The background as drawn, not as asked for: a generated "magenta" is
    # rarely exactly #FF00FF, so take the median of the four corners.
    corners = [src[x, y] for x in (0, 1, w - 2, w - 1) for y in (0, 1, h - 2, h - 1)]
    bg = tuple(sorted(c[i] for c in corners)[len(corners) // 2] for i in range(3))
    bg_m = min(bg[0], bg[2]) - bg[1]
    if bg_m < 150:
        raise ValueError(f"the background {bg} is not magenta")
    out = Image.new("RGBA", im.size)
    dst = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b = src[x, y]
            # How magenta the pixel is: high red and blue, low green. The
            # background scores bg_m; a metal scores well under 40.
            m = min(r, b) - g
            if m >= bg_m - 25:
                dst[x, y] = (0, 0, 0, 0)
                continue
            if m <= 40:
                dst[x, y] = (r, g, b, 255)
                continue
            # The soft edge: the pixel is a mix a*coin + (1-a)*background, so
            # take the background back out of every channel, green included.
            a = (bg_m - 25 - m) / (bg_m - 65)
            k = 1 - a
            px = tuple(max(0, min(255, round((v - k * bv) / a))) for v, bv in zip((r, g, b), bg))
            dst[x, y] = (*px, round(255 * a))
    return out


def trim_and_place(im: Image.Image) -> Image.Image:
    box = im.getchannel("A").point(lambda v: 255 if v > 24 else 0).getbbox()
    if box is None:
        raise ValueError("no coin found: is the background magenta #FF00FF?")
    coin = im.crop(box)
    side = round(SIZE * FILL)
    scale = side / max(coin.size)
    coin = coin.resize((max(1, round(coin.width * scale)), max(1, round(coin.height * scale))), Image.LANCZOS)
    canvas = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    canvas.alpha_composite(coin, ((SIZE - coin.width) // 2, (SIZE - coin.height) // 2))
    return defringe(canvas)


def defringe(im: Image.Image) -> Image.Image:
    """The faintest edge pixels can keep a pink cast after the resize. No
    metal is ever magenta (red and blue both well above green), so on the
    semi-transparent edge, red and blue are held to at most 30 above green."""
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if 0 < a < 255 and min(r, b) - g > 30:
                cap = g + 30
                px[x, y] = (min(r, cap), g, min(b, cap), a)
    return im


def mean_colour(im: Image.Image) -> tuple:
    data = im.get_flattened_data() if hasattr(im, "get_flattened_data") else im.getdata()
    px = [p for p in data if p[3] > 200]
    n = max(1, len(px))
    return tuple(round(sum(p[i] for p in px) / n) for i in range(3))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=os.path.join(HERE, "source"))
    ap.add_argument("--out", default=os.path.join(ROOT, "assets", "images"))
    args = ap.parse_args()
    missing = [m for m in METALS if not os.path.exists(os.path.join(args.src, f"coin_{m}.png"))]
    if missing:
        print("missing: " + ", ".join(f"coin_{m}.png" for m in missing) + f" in {args.src}")
        return 1
    for m in METALS:
        coin = trim_and_place(key_magenta(Image.open(os.path.join(args.src, f"coin_{m}.png"))))
        path = os.path.join(args.out, f"pickup_{m}.png")
        coin.save(path, optimize=True)
        r, g, b = mean_colour(coin)
        print(f"pickup_{m}.png  mean colour #{r:02X}{g:02X}{b:02X}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
