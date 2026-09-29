"""Imports the owner's drawn backdrops into the game.

    python tool/art/import_backdrops.py
    python tool/art/import_backdrops.py --preview some/folder

The brief is tool/art/BACKDROP-BRIEF.md. Sources go in
tool/art/source/backdrop/, named {year}_{part}.{png,jpg,jpeg,webp}:

    1816_sky.png   1816_far.png   1816_mid.png   1816_near.png
    1816_ground.png   1816_capital.png   1816_shaft.png

Every part is optional. For each source this:

  1. makes the background transparent, for the parts that need it (the
     skyline strips and the column parts), if the file has no transparency
     of its own: the background is pure white or pure magenta, whichever
     lines more of the border (the brief asks for one the art does not
     use), cleared everywhere it covers a patch of any size, with its JPEG
     fringe. The first version took the commonest border colour, and on a
     skyline whose buildings line the bottom edge that was the buildings;
  2. trims what the image generator leaves round the art. A column part is
     cut to the art's own width (the prompts ask for margins of background
     either side), and the shaft is then set in a margin so its width
     matches the neck under the capital: a shaft drawn filling its image
     would otherwise come out as wide as the capital's top, and the two
     would not line up (1816's neck is 61% of the capital's width). The
     ground loses plain rows off its bottom, below the last row with any
     detail: the game fills under it with its own dark. A skyline loses the
     clear rows above its tallest building, all but a margin of 6%: the
     generator has no wide enough shape, so the prompts ask for the city in
     the lower part of a 16:9 image, and the trim takes the strip to its
     shape, as cropping by hand did for 1816;
  3. sizes it: a skyline strip, the sky and the ground to their band of the
     screen height (the image's height is its band; the width follows),
     stored at half the reference phone's pixels, which the game scales
     back up; a column part to the column's width. Parts that repeat are
     resized with a wrapped margin, so the resampling joins across the
     seam instead of making one;
  4. checks that it tiles: a strip's or the ground's left and right edges,
     and the shaft's top and bottom, must join, or the seam shows every
     repeat. The join is compared with the art's own steps from one column
     (or row) to the next: a building's edge at the seam is fine, a jump
     rougher than nearly any step inside the art is flagged. A warning,
     not an error;
  5. writes assets/images/backdrop/{year}_{part}.png, and lists everything
     in manifest.json there with its band, base and parallax, which the game
     reads (lib/arcade/passage/backdrop.dart).

The defaults for band, base and parallax are below. To change one for an
era, put tool/art/source/backdrop/tuning.json beside the sources:

    {"1816": {"far": {"parallax": 0.1}}}

With --preview, it also writes each era composed as the game shows it at
landing, sky to ground with a pair of columns, at the reference size, for
checking before a build.
"""
import argparse
import json
import os
import sys
from collections import deque

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.normpath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(HERE, "source", "backdrop")
OUT = os.path.join(APP, "assets", "images", "backdrop")

YEARS = [1816, 1873, 1913, 1923, 1933, 1944, 1971, 1979, 2009]

# The reference phone the art is sized against: the Pixel it is tested on.
REF_W, REF_H = 1080, 2424
# Strips are stored at this fraction of the reference pixels. A full set of
# nine eras is a lot of texture; the art's own pixels are several screen
# pixels wide, so half loses nothing that shows.
STORE = 0.5
# A column's width on the reference phone, in pixels (the game's gate width).
COLUMN_W = 92

PARTS = {
    # band: height as a fraction of the screen's; base: where its bottom
    # sits, as a fraction of the screen's height; parallax: its speed
    # against the gates'. Matches what the code-drawn city does.
    "sky": dict(band=1.0),
    "far": dict(band=0.45, base=0.86, parallax=0.12),
    "mid": dict(band=0.40, base=1.0, parallax=0.30),
    "near": dict(band=0.20, base=1.0, parallax=0.55),
    "ground": dict(band=0.16),
    "capital": dict(),
    "shaft": dict(),
}
KEYED = {"far", "mid", "near", "capital", "shaft"}


def has_alpha(img):
    if img.mode != "RGBA":
        return False
    a = np.array(img.getchannel("A"))
    return (a < 250).mean() > 0.01


KEYS = {"white": (255, 255, 255), "magenta": (255, 0, 255)}


def key_out(img, tol=40, fringe=70):
    """Clears the flat background: pure white or pure magenta, whichever
    lines more of the border, everywhere it covers a patch of 30 pixels or
    more (so sky between buildings goes too, not only sky touching the
    edge), then the fringe JPEG leaves round the art, twice over. Returns
    (None, None) when neither is on the border: nothing to clear."""
    a = np.array(img.convert("RGB")).astype(int)
    h, w, _ = a.shape
    border = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]])
    share = {n: (np.abs(border - np.array(k)).max(axis=1) < tol).mean() for n, k in KEYS.items()}
    name = max(share, key=share.get)
    if share[name] < 0.05:
        return None, None
    key = np.array(KEYS[name])
    near = np.abs(a - key).max(axis=2) < tol
    bg = np.zeros((h, w), bool)
    seen = np.zeros((h, w), bool)
    for y in range(h):
        for x in range(w):
            if near[y, x] and not seen[y, x]:
                seen[y, x] = True
                region, dq = [(y, x)], deque([(y, x)])
                while dq:
                    cy, cx = dq.popleft()
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and near[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True
                            region.append((ny, nx))
                            dq.append((ny, nx))
                if len(region) >= 30:
                    ys, xs = zip(*region)
                    bg[list(ys), list(xs)] = True
    loose = np.abs(a - key).max(axis=2) < fringe
    for _ in range(2):
        edge = np.zeros_like(bg)
        edge[1:] |= bg[:-1]
        edge[:-1] |= bg[1:]
        edge[:, 1:] |= bg[:, :-1]
        edge[:, :-1] |= bg[:, 1:]
        bg |= edge & loose
    alpha = np.where(bg, 0.0, 1.0)
    rgb = a.astype(float)
    if name == "magenta":
        # Magenta is unlike anything in the art, so it is taken out wherever
        # it is, not only where the fill reached: slivers of it between
        # chimney pots and in the crooks of branches, cut off from the rest
        # of the background, were left bright pink on 1816's first import.
        # Every pixel is unmixed: its magenta share is how far its red and
        # blue stand above its green (the art's own purples barely do), and
        # that share comes out of its colour and into its transparency, so
        # outlines blended part-way into the magenta lose the pink and keep
        # a soft edge. White can't be told from light stone this way, so a
        # white background keeps the plain cut.
        ring = ~bg
        # How much magenta the art itself carries, measured away from the
        # background (3px in): only the cast above that is the background's.
        # A fixed allowance of 20 left 1816's slate-blue edges a faint lilac
        # (a cast of 20-50 on the edges, against -15 inside the art); a mauve
        # era keeps its purples, since its own cast raises the allowance.
        cast = np.minimum(rgb[:, :, 0], rgb[:, :, 2]) - rgb[:, :, 1]
        inside = ~bg
        for _ in range(3):
            shrunk = inside.copy()
            shrunk[1:] &= inside[:-1]
            shrunk[:-1] &= inside[1:]
            shrunk[:, 1:] &= inside[:, :-1]
            shrunk[:, :-1] &= inside[:, 1:]
            inside = shrunk
        # A pixel is touched only when its cast is above nearly all the art's
        # own (98th percentile, +4). How much of it is background is then
        # measured from the art's typical cast (the median), not from zero:
        # 1816's blues sit at -16, and measuring from zero left each edge
        # pixel part magenta, amplified as it was unmixed, a violet line.
        typical = float(np.median(cast[inside])) if inside.any() else 0.0
        own = float(np.percentile(cast[inside], 98)) if inside.any() else 20.0
        allowance = min(own + 4.0, 40.0)
        share = np.where(cast > allowance, np.clip((cast - typical) / (255.0 - typical), 0, 1), 0.0)
        share = np.where(ring, share, 0.0)
        keep = 1 - share
        unmixed = (rgb - share[:, :, None] * key) / np.maximum(keep, 1e-3)[:, :, None]
        rgb = np.where((share > 0)[:, :, None], np.clip(unmixed, 0, 255), rgb)
        alpha = np.where(ring, np.where(keep < 0.12, 0.0, keep), alpha)
    # Cleared pixels keep no colour: resampling would otherwise pull the
    # background's colour back in round every edge.
    rgb[alpha == 0] = 0
    out = np.dstack([rgb.round().astype(np.uint8), (alpha * 255).round().astype(np.uint8)])
    return Image.fromarray(out, "RGBA"), name


def resize_rgba(img, size):
    """Resized with its colour premultiplied by its alpha, so transparent
    pixels add nothing to their neighbours. Resized straight, the colour
    still stored under the cleared magenta bled back in as a bright line
    round every roof and branch on 1816's first import."""
    return img.convert("RGBa").resize(size, Image.LANCZOS).convert("RGBA")


def seam(img, axis):
    """Whether the image's opposite edges join: the step across the seam
    (last column to first, axis 1; last row to first, axis 0), and the step
    only 0.5% of the art's own steps between neighbours exceed: a grid line
    or a building's edge is rare in the art, and fine at the seam. The seam
    is bad when the first is well over the second."""
    a = np.array(img.convert("RGBA")).astype(float)
    if axis == 0:
        a = a.transpose(1, 0, 2)
    # Premultiplied, so clear pixels count as nothing whatever their colour.
    a = a[:, :, :3] * (a[:, :, 3:] / 255.0)
    steps = np.abs(np.diff(a, axis=1)).mean(axis=(0, 2))
    across = float(np.abs(a[:, 0] - a[:, -1]).mean())
    return across, float(np.percentile(steps, 99.5))


def trim_seam_edges(img, axis, most=0.01):
    """A repeating part without a drawn line along its joining edges: tries
    dropping up to [most] of it at each end, and keeps the cut that joins
    best if it more than halves the step across the seam. 2009's ground had
    a bright four-pixel rule down its left edge, which would have shown as a
    stripe at every repeat. Returns the image and how many pixels went."""
    n = img.width if axis == 1 else img.height
    k = max(1, int(n * most))

    def cut(a, b):
        return img.crop((a, 0, img.width - b, img.height)) if axis == 1 else img.crop((0, a, img.width, img.height - b))

    base, usual = seam(img, axis)
    # Only for a seam that would be flagged: one that already joins is left
    # alone (the first version trimmed a dozen that joined, to join them
    # better still, and cut real art).
    if base <= max(1.5 * usual, 12):
        return img, 0
    best = (base, 0, 0)
    for a in range(0, k + 1, 2):
        for b in range(0, k + 1, 2):
            if a or b:
                v = seam(cut(a, b), axis)[0]
                if v < best[0]:
                    best = (v, a, b)
    v, a, b = best
    if (a or b) and v < base / 2:
        return cut(a, b), a + b
    return img, 0


def resize_wrapped(img, size, axis):
    """Resizes a part that repeats along [axis] (1 across, 0 down) with a
    margin of itself wrapped round each end, then crops the margin off, so
    the edges are resampled from their true neighbours."""
    w, h = img.size
    tw, th = size
    a = np.array(img)
    if axis == 1:
        m = max(4, w // 16)
        padded = Image.fromarray(np.concatenate([a[:, -m:], a, a[:, :m]], axis=1))
        mt = round(m * tw / w)
        big = resize_rgba(padded, (tw + 2 * mt, th))
        return big.crop((mt, 0, mt + tw, th))
    m = max(4, h // 16)
    padded = Image.fromarray(np.concatenate([a[-m:], a, a[:m]], axis=0))
    mt = round(m * th / h)
    big = resize_rgba(padded, (tw, th + 2 * mt))
    return big.crop((0, mt, tw, mt + th))


def art_columns(img, share=0.2):
    """The first and last column (x) where the art covers at least [share]
    of the rows: the art's own width, ignoring a stray speck at an edge."""
    a = np.array(img.getchannel("A")) > 32
    cols = np.nonzero(a.mean(axis=0) >= share)[0]
    return (int(cols.min()), int(cols.max()) + 1) if len(cols) else (0, img.width)


def fill_column_gaps(img):
    """A column part with its see-through gaps filled: in each row, clear
    pixels between the art's first and last are painted the art's own
    darkest shade. A column is solid in play, so it has to look solid:
    1913's steel lattice came with the city showing through between the
    bars, which reads as a way through. Returns the image and how many
    pixels were filled."""
    a = np.array(img).copy()
    op = a[:, :, 3] > 128
    if not op.any():
        return img, 0
    rgb = a[:, :, :3][op].astype(float)
    lum = rgb.mean(axis=1)
    dark = rgb[lum <= np.percentile(lum, 8)].mean(axis=0)
    fill = np.zeros(op.shape, bool)
    for y in range(a.shape[0]):
        xs = np.nonzero(op[y])[0]
        if len(xs) >= 2:
            fill[y, xs[0]:xs[-1] + 1] = ~op[y, xs[0]:xs[-1] + 1]
    n = int(fill.sum())
    if n:
        # Blend under what is there, so soft edges stay soft.
        al = a[:, :, 3:4].astype(float) / 255.0
        mixed = a[:, :, :3] * al + dark * (1 - al)
        a[fill, :3] = mixed[fill].round().astype(np.uint8)
        a[fill, 3] = 255
    return Image.fromarray(a, "RGBA"), n


def neck_share(capital):
    """How wide the column is just under the capital, as a share of the
    capital's width: the art's width across its bottom tenth."""
    a = np.array(capital.getchannel("A")) > 32
    h, w = a.shape
    rows = a[h - max(1, h // 10):]
    cols = np.nonzero(rows.mean(axis=0) >= 0.5)[0]
    return (cols.max() + 1 - cols.min()) / w if len(cols) else 1.0


def trim_ground(img, spread=6, margin=0.12):
    """The ground without the plain rows off its bottom (everything below
    the last row whose colours vary, plus a little margin), and without the
    white above its top edge. Returns the image and its lip: how much of it,
    as a share of its height, stands above the ground line.

    1816's second ground came with a white band across its top 14%, which
    would have become the ground line; those whole white rows go. 1944's
    has grass tufts rising above the line into the white: the line is the
    first row the art spans all the way across, the white above it is made
    clear, and what stands there (the tufts) is kept as a lip, drawn above
    the line in play, so the hooves stand on the path and not on the tips
    of the grass."""
    a = np.array(img.convert("RGB")).astype(float)
    whiteish = (a.min(axis=2) > 200) & ((a.max(axis=2) - a.min(axis=2)) < 30)
    blank = whiteish.mean(axis=1) > 0.99
    top = 0
    while top < len(blank) - 1 and blank[top]:
        top += 1
    full = np.nonzero((~whiteish).mean(axis=1) > 0.95)[0]
    full = full[full >= top]
    line = int(full[0]) if len(full) else top
    busy = np.nonzero(a.std(axis=(1, 2)) > spread)[0]
    busy = busy[busy >= line]
    bottom = img.height if not len(busy) else min(img.height, line + int((busy.max() - line) * (1 + margin)) + 1)
    out = np.array(img.convert("RGBA"))
    out[:line][whiteish[:line]] = 0
    out = out[top:bottom]
    return Image.fromarray(out, "RGBA"), (line - top) / (bottom - top)


def trim_sky_above(img, margin=0.06):
    """A skyline strip without the clear rows above its tallest building,
    but for a margin of [margin] of what is left."""
    a = np.array(img.getchannel("A")) > 32
    rows = np.nonzero(a.mean(axis=1) > 0.002)[0]
    if not len(rows):
        return img
    top = rows.min()
    keep = img.height - top
    top = max(0, top - round(keep * margin / (1 - margin)))
    return img.crop((0, top, img.width, img.height))


def trim_frame(img, most=0.04, tol=6):
    """The image without a flat border drawn round it: from each edge,
    strips of one even colour, stopping at the first that varies or at
    [most] of the image. 2009's sky came framed in a 12px dark rule, which
    would have run along the top of the screen."""
    a = np.array(img.convert("RGB")).astype(int)
    h, w, _ = a.shape

    def flat(strip):
        return strip.std(axis=0).max() < tol

    def depth(get, n):
        d = 0
        while d < n * most and flat(get(d)):
            d += 1
        return d if d >= 3 else 0

    t = depth(lambda i: a[i], h)
    b = depth(lambda i: a[h - 1 - i], h)
    l = depth(lambda i: a[:, i], w)
    r = depth(lambda i: a[:, w - 1 - i], w)
    # A frame has all four sides; a sky merely plain at its top has one.
    if min(t, b, l, r) == 0:
        return img, 0
    return img.crop((l, t, w - r, h - b)), max(t, b, l, r)


def size_for(part, img):
    w, h = img.size
    if part in ("capital", "shaft"):
        tw = COLUMN_W
        return tw, max(1, round(h * tw / w))
    th = round(PARTS[part]["band"] * REF_H * STORE)
    return max(1, round(w * th / h)), th


def find_sources():
    found = {}
    if not os.path.isdir(SRC):
        return found
    for name in sorted(os.listdir(SRC)):
        stem, ext = os.path.splitext(name)
        if ext.lower() not in (".png", ".jpg", ".jpeg", ".webp") or "_" not in stem:
            continue
        year, part = stem.split("_", 1)
        if not year.isdigit() or int(year) not in YEARS:
            print(f"  skipped {name}: no era {year}")
            continue
        if part not in PARTS:
            print(f"  skipped {name}: the parts are {', '.join(PARTS)}")
            continue
        path = os.path.join(SRC, name)
        prev = found.get((int(year), part))
        if prev:
            # Two files for one piece (a redo saved as .jpg beside the old
            # .webp, say): the newer one wins, and it says so.
            newer, older = sorted([prev, path], key=os.path.getmtime, reverse=True)
            print(f"  note: two files for {year} {part}; using {os.path.basename(newer)}, "
                  f"not {os.path.basename(older)} (delete the one you don't want)")
            path = newer
        found[(int(year), part)] = path
    return found


def preview(year, parts, path):
    """The era as the game draws it at landing, at the reference size."""
    W, H = REF_W, REF_H
    canvas = Image.new("RGBA", (W, H), (12, 13, 16, 255))

    def load(part):
        return Image.open(os.path.join(OUT, parts[part]["file"])).convert("RGBA") if part in parts else None

    sky = load("sky")
    if sky:
        s = max(W / sky.width, H / sky.height)
        sky = resize_rgba(sky, (round(sky.width * s), round(sky.height * s)))
        canvas.alpha_composite(sky, ((W - sky.width) // 2, (H - sky.height) // 2))
    for part in ("far", "mid", "near"):
        img = load(part)
        if not img:
            continue
        spec = parts[part]
        dh = round(spec["band"] * H)
        img = resize_rgba(img, (round(img.width * dh / img.height), dh))
        top = round(spec["base"] * H) - dh
        for x in range(0, W, img.width):
            canvas.alpha_composite(img, (x, top))
    # The columns either side of a gap in the middle, where the boar flies.
    cap, shaft = load("capital"), load("shaft")
    if cap and shaft:
        cw = COLUMN_W
        cap = resize_rgba(cap, (cw, round(cap.height * cw / cap.width)))
        shaft = resize_rgba(shaft, (cw, round(shaft.height * cw / shaft.width)))
        cx, gap0, gap1 = W // 2 + 200, round(H * 0.36), round(H * 0.58)
        col = Image.new("RGBA", (cw, H), (0, 0, 0, 0))
        for y in range(gap1 + cap.height, H, shaft.height):
            col.alpha_composite(shaft, (0, y))
        col.alpha_composite(cap, (0, gap1))
        for y in range(gap0 - cap.height - shaft.height, -shaft.height, -shaft.height):
            col.alpha_composite(shaft, (0, y))
        col.alpha_composite(cap.transpose(Image.FLIP_TOP_BOTTOM), (0, gap0 - cap.height))
        amber = Image.new("RGBA", (cw, round(H * 0.0045)), (234, 149, 45, 204))
        col.alpha_composite(amber, (0, gap0 - amber.height))
        col.alpha_composite(amber, (0, gap1))
        canvas.alpha_composite(col, (cx - cw // 2, 0))
    ground_y = round(H * 0.87)
    ground = Image.new("RGBA", (W, H - ground_y), (35, 38, 43, 255))
    canvas.alpha_composite(ground, (0, ground_y))
    g = load("ground")
    if g:
        dh = round(PARTS["ground"]["band"] * H)
        g = resize_rgba(g, (round(g.width * dh / g.height), dh))
        top = ground_y - round(parts["ground"].get("lip", 0) * dh)
        for x in range(0, W, g.width):
            canvas.alpha_composite(g, (x, top))
    canvas.alpha_composite(Image.new("RGBA", (W, round(H * 0.004)), (234, 149, 45, 217)), (0, ground_y))
    canvas.convert("RGB").save(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preview", help="also write each era composed, to this folder")
    args = ap.parse_args()

    tuning = {}
    tpath = os.path.join(SRC, "tuning.json")
    if os.path.exists(tpath):
        tuning = json.load(open(tpath, encoding="utf-8"))

    os.makedirs(OUT, exist_ok=True)
    sources = find_sources()
    manifest = {"version": 1, "eras": {}}
    written = set()
    necks = {}
    # Capitals before shafts: a shaft is sized to its capital's neck.
    order = sorted(sources.items(), key=lambda kv: (kv[0][0], kv[0][1] == "shaft", kv[0][1]))
    for (year, part), path in order:
        img = Image.open(path)
        img = img.convert("RGBA") if img.mode in ("RGBA", "LA", "P") else img.convert("RGB")
        note = ""
        if part in KEYED and not has_alpha(img):
            keyed, key = key_out(img)
            if keyed is None:
                print(f"{year} {part}: {os.path.basename(path)} SKIPPED: it needs a transparent background, "
                      "or pure white or pure magenta round its edges, and has neither")
                continue
            img, note = keyed, f", {key} background cleared"
        img = img.convert("RGBA")
        if part in ("capital", "shaft"):
            x0, x1 = art_columns(img)
            if (x0, x1) != (0, img.width):
                img = img.crop((x0, 0, x1, img.height))
                note += f", trimmed to the art's width ({x1 - x0}px)"
        if part in ("capital", "shaft"):
            img, filled = fill_column_gaps(img)
            if filled > img.width * img.height * 0.01:
                note += f", see-through gaps filled with its darkest shade ({filled * 100 // (img.width * img.height)}%)"
        if part == "capital":
            necks[year] = neck_share(img)
        if part == "shaft" and year in necks and necks[year] < 0.97:
            full = round(img.width / necks[year])
            padded = Image.new("RGBA", (full, img.height), (0, 0, 0, 0))
            padded.paste(img, ((full - img.width) // 2, 0))
            img = padded
            note += f", set to the capital's neck ({necks[year]:.0%} of its width)"
        lip = 0.0
        if part == "sky":
            img, framed = trim_frame(img)
            if framed:
                note += f", drawn frame trimmed ({framed}px)"
        if part == "ground":
            before = img.height
            img, lip = trim_ground(img)
            if img.height < before * 0.97:
                note += f", blank rows trimmed ({img.height}/{before} rows kept)"
            if lip > 0.01:
                note += f", {lip:.0%} of it stands above the ground line"
        if part in ("far", "mid", "near"):
            before = img.height
            img = trim_sky_above(img)
            if img.height < before * 0.97:
                note += f", clear sky above trimmed ({img.height}/{before} rows kept)"
        # The band is the image's height as drawn, clear rows and all: space
        # above a skyline is part of the composition, so nothing is trimmed.
        tw, th = size_for(part, img)
        axis = 1 if part in ("far", "mid", "near", "ground") else 0 if part == "shaft" else None
        if axis is not None:
            img, dropped = trim_seam_edges(img, axis)
            if dropped:
                note += f", a drawn line along its joining edges trimmed ({dropped}px)"
        img = resize_wrapped(img, (tw, th), axis) if axis is not None else resize_rgba(img, (tw, th))
        if axis is not None:
            across, usual = seam(img, axis)
            if across > max(1.5 * usual, 12):
                edges = "left and right edges" if axis == 1 else "top and bottom"
                note += (f"; WARNING the {edges} do not join (a step of {across:.0f} across the seam, "
                         f"where the art's own steps are at most about {usual:.0f}): the seam will show")
        if part in ("far", "mid", "near") and img.width < img.height * REF_W / REF_H * 2 * PARTS[part]["band"]:
            note += "; narrow: it repeats within two screens, consider drawing it wider"
        name = f"{year}_{part}.png"
        img.save(os.path.join(OUT, name))
        written.add(name)
        spec = {"file": name, **PARTS[part], **({"lip": round(lip, 4)} if lip > 0.01 else {}),
                **tuning.get(str(year), {}).get(part, {})}
        manifest["eras"].setdefault(str(year), {})[part] = spec
        print(f"{year} {part}: {os.path.basename(path)} -> backdrop/{name} {tw}x{th}{note}")
        if part in ("capital", "shaft") and ((year, "capital") in sources) != ((year, "shaft") in sources):
            print(f"  note: {year} needs both capital and shaft for drawn columns; until then its columns stay code-drawn")

    for name in os.listdir(OUT):
        if name.endswith(".png") and name not in written:
            os.remove(os.path.join(OUT, name))
            print(f"removed stale backdrop/{name}")
    with open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")
    eras_done = sorted(manifest["eras"])
    print(f"manifest: {len(written)} images, eras {', '.join(eras_done) or 'none'}")

    if args.preview:
        os.makedirs(args.preview, exist_ok=True)
        for year, parts in manifest["eras"].items():
            p = os.path.join(args.preview, f"backdrop_{year}.png")
            preview(year, parts, p)
            print(f"preview: {p}")


if __name__ == "__main__":
    sys.exit(main())
