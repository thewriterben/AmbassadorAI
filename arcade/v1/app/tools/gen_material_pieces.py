"""Coin Quest board pieces, Material style.

Flat tonal discs: one solid fill, a lighter outline ring, the DGD mark, and a
soft elevation shadow underneath. No gradients, no specular highlight, no
lettering.

Two decisions here are about reading the piece at the size it is actually used
— roughly a 44 px cell on a 9-column board, not the 256 px it is authored at:

  * The mark is an "on-colour" — near-black or white, whichever contrasts more
    with the fill — at full opacity. It was a dark tint of the piece's own hue,
    which is a small luminance step, and hue contrast does almost nothing this
    small. On the flag blue and the money green it was invisible.
  * There is no decorative inner ring. It was concentric with the mark's own
    circular form, so the two merged into rings-inside-rings.

Padding is tight (6%) so the coin fills its cell; the sprite is drawn at
cell * 0.96 in match3_game.dart, which together put the disc at ~85% of a cell.
The shadow offset and blur are sized to fit inside that padding rather than
clip at the sprite edge.

Only `piece_*.png` is regenerated. `coin_*.png` stays as the rendered DGD coin,
because that is the brand mark used by the arcade home, the leaderboard medals
and Tablet Run — not a game piece.

Reds and blues are the flag's own values (Old Glory Red / Old Glory Blue).
"""
import os

from PIL import Image, ImageDraw, ImageFilter

OUT = r"C:\src\puzzle-app\assets\images"
S = 256
SS = 4
N = S * SS

PAD = 0.060          # disc inset; the shadow lives in here
LOGO = 0.64          # mark size as a fraction of the sprite
LOGO_WEIGHT = 0.011  # stroke thickening, as a fraction of the sprite
RING_W = 0.030

# fill, outline ring
PALETTE = {
    "gold":   ((242, 176, 30),  (255, 214, 120)),
    "silver": ((154, 165, 177), (214, 223, 232)),
    "copper": ((193, 112, 58),  (236, 168, 120)),
    "red":    ((179, 25, 66),   (240, 126, 156)),   # Old Glory Red
    "blue":   ((10, 49, 97),    (108, 156, 224)),   # Old Glory Blue
    "green":  ((30, 138, 76),   (148, 232, 180)),   # money green, kelly
}


def luminance(c):
    r, g, b = [v / 255 for v in c]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def on_color(fill):
    """Material's on-colour rule: whichever of near-black / white contrasts more."""
    return (10, 12, 14) if luminance(fill) > 0.42 else (255, 255, 255)


def canvas(size=N):
    return Image.new("RGBA", (size, size), (0, 0, 0, 0))


def finish(img, name):
    img.resize((S, S), Image.LANCZOS).save(os.path.join(OUT, name), optimize=True)
    print(f"  {name:22} {os.path.getsize(os.path.join(OUT, name)) // 1024} KB")


def elevation(shape_mask, blur=0.026, drop=0.020, alpha=125):
    """Material elevation: a soft dark shadow offset downward.

    Offset and blur are kept under PAD so the shadow cannot clip at the sprite
    edge now that the disc sits close to it.
    """
    sh = canvas()
    sh.paste((0, 0, 0, alpha), (0, int(N * drop)), shape_mask)
    return sh.filter(ImageFilter.GaussianBlur(N * blur))


_logo_cache = {}


def logo(size, color):
    """The DGD mark, flattened to a single colour at the requested size.

    The source artwork is drawn for large display and its strokes go thin and
    grey once scaled to a board cell. `MaxFilter` dilates the alpha, which
    thickens every stroke by the same amount in every direction — the cheap
    equivalent of setting a heavier weight, and it keeps the counters open
    where simply scaling the mark up would not.
    """
    key = (size, color)
    if key in _logo_cache:
        return _logo_cache[key]
    src = Image.open(os.path.join(OUT, "logo_white.png")).convert("RGBA")
    a = src.resize((size, size), Image.LANCZOS).getchannel("A")

    grow = int(N * LOGO_WEIGHT) | 1  # MaxFilter needs an odd window
    if grow >= 3:
        a = a.filter(ImageFilter.MaxFilter(grow))

    flat = Image.new("RGBA", (size, size), color + (0,))
    flat.putalpha(a)
    _logo_cache[key] = flat
    return flat


def piece(name, fill, ring):
    img = canvas()
    pad = N * PAD
    mask = Image.new("L", (N, N), 0)
    ImageDraw.Draw(mask).ellipse((pad, pad, N - pad, N - pad), fill=255)

    out = canvas()
    out.alpha_composite(elevation(mask))

    d = ImageDraw.Draw(img)
    d.ellipse((pad, pad, N - pad, N - pad), fill=fill + (255,))
    # Outline ring: Material's outline token, and what keeps a navy piece
    # legible on a near-black board.
    d.ellipse((pad, pad, N - pad, N - pad), outline=ring + (255,), width=int(N * RING_W))

    lg = int(N * LOGO)
    img.alpha_composite(logo(lg, on_color(fill)), ((N - lg) // 2, (N - lg) // 2))

    out.alpha_composite(img)
    finish(out, f"piece_{name}.png")


def vault(reinforced=False):
    """Material vault: a flat rounded square, outline ring, simple dial.

    Two states, because a reinforced vault takes two hits and the player has
    no way to count them otherwise. The reinforced one is armour-plated —
    heavier bands across the face and corner rivets, in a colder steel — and
    the first hit drops it to this plain one. The difference has to be legible
    at a glance at cell size, so it is a change of structure, not a tint.
    """
    img = canvas()
    d = ImageDraw.Draw(img)
    pad = N * PAD
    r = int(N * 0.18)
    body = (pad, pad, N - pad, N - pad)

    mask = Image.new("L", (N, N), 0)
    ImageDraw.Draw(mask).rounded_rectangle(body, radius=r, fill=255)
    out = canvas()
    out.alpha_composite(elevation(mask))

    steel = (58, 66, 76) if reinforced else (69, 78, 89)
    edge = (168, 180, 194) if reinforced else (150, 162, 176)
    d.rounded_rectangle(body, radius=r, fill=steel + (255,))
    d.rounded_rectangle(body, radius=r, outline=edge + (255,),
                        width=int(N * (RING_W * 1.5 if reinforced else RING_W)))

    if reinforced:
        # Two armour bands across the face.
        for y in (0.30, 0.70):
            d.line((pad, N * y, N - pad, N * y), fill=edge + (120,), width=int(N * 0.035))
        # Corner rivets.
        rv = N * 0.030
        for cxr in (0.20, 0.80):
            for cyr in (0.20, 0.80):
                d.ellipse((N * cxr - rv, N * cyr - rv, N * cxr + rv, N * cyr + rv),
                          fill=edge + (230,))

    # Dial: two flat rings and a centre dot.
    cx = cy = N / 2
    for rad, w in ((N * 0.21, 0.032), (N * 0.13, 0.026)):
        d.ellipse((cx - rad, cy - rad, cx + rad, cy + rad), outline=edge + (235,), width=int(N * w))
    dot = N * 0.048
    d.ellipse((cx - dot, cy - dot, cx + dot, cy + dot), fill=edge + (255,))
    out.alpha_composite(img)
    finish(out, "piece_vault_armored.png" if reinforced else "piece_vault.png")


def ingot():
    """Material ingot: a flat trapezoid, one tone, one outline. No specular."""
    img = canvas()
    d = ImageDraw.Draw(img)
    gold, ring = (242, 176, 30), (255, 214, 120)
    top_y, bot_y = N * 0.30, N * 0.72
    pts = [(N * 0.14, bot_y), (N * 0.86, bot_y), (N * 0.70, top_y), (N * 0.30, top_y)]

    mask = Image.new("L", (N, N), 0)
    ImageDraw.Draw(mask).polygon(pts, fill=255)
    out = canvas()
    out.alpha_composite(elevation(mask))

    d.polygon(pts, fill=gold + (255,))
    d.line(pts + [pts[0]], fill=ring + (255,), width=int(N * 0.030), joint="curve")
    # Two flat stamp bars, no shading.
    for i, w in enumerate((0.28, 0.21)):
        y = top_y + N * (0.11 + i * 0.10)
        d.line((N * 0.5 - N * w / 2, y, N * 0.5 + N * w / 2, y), fill=ring + (150,), width=int(N * 0.024))
    out.alpha_composite(img)
    finish(out, "piece_ingot.png")


def seals():
    """Flat seal overlays to match: tonal square, outline, layer pips."""
    for layers in (1, 2):
        img = canvas()
        d = ImageDraw.Draw(img)
        pad = N * 0.06
        r = int(N * 0.18)
        a = 54 if layers == 1 else 92
        ring = (234, 149, 45)
        d.rounded_rectangle((pad, pad, N - pad, N - pad), radius=r, fill=ring + (a,))
        d.rounded_rectangle((pad, pad, N - pad, N - pad), radius=r,
                            outline=ring + (190 if layers == 1 else 240,),
                            width=int(N * (0.022 if layers == 1 else 0.034)))
        if layers == 2:
            pr = N * 0.032
            for i in range(2):
                px = N * 0.5 + (i - 0.5) * N * 0.11
                d.ellipse((px - pr, N * 0.84 - pr, px + pr, N * 0.84 + pr), fill=ring + (255,))
        finish(img, f"seal_{layers}.png")


if __name__ == "__main__":
    print("material pieces")
    for name, (fill, ring) in PALETTE.items():
        piece(name, fill, ring)
    vault()
    vault(reinforced=True)
    ingot()
    seals()
    # Contact sheet at board size, which is where legibility is decided.
    names = [f"piece_{k}.png" for k in PALETTE] + [
        "piece_vault_armored.png", "piece_vault.png", "piece_ingot.png"]
    cell = 52
    sheet = Image.new("RGBA", (cell * len(names), cell), (8, 8, 9, 255))
    for i, n in enumerate(names):
        im = Image.open(os.path.join(OUT, n)).convert("RGBA").resize((cell, cell), Image.LANCZOS)
        sheet.alpha_composite(im, (i * cell, 0))
    sheet.resize((cell * len(names) * 3, cell * 3), Image.NEAREST).save(r"C:\src\pieces_sheet.png")
    print("  sheet -> C:\\src\\pieces_sheet.png")
