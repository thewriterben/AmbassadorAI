"""Flat gold coin launcher icon for the Digital Gold app, plus the shared
coin face for the ticker header.

Two rules this follows rather than inventing:

* The gold and the "G" are *measured off* DGD Arcade's existing flat coin
  (assets/app_icon.png), not picked by eye, so the app and the arcade are
  carrying the same coin.
* The coin sits at 62% of the adaptive-icon canvas, which is the 72/108dp
  safe zone. Anything larger and a circular launcher mask crops the rim off.

The one deliberate difference from the arcade's coin is a **milled double
rim** — a second concentric ring. The arcade coin is plain. It reads even at
48dp, and it means the two icons are not identical if v1 ever also ships to
the store on its own. See ICON-NOTES.md.

Everything is drawn at 4x and downsampled, because Pillow has no antialiased
circle.
"""
import os
import shutil

from PIL import Image, ImageDraw

ARCADE_ICON = r"C:\src\puzzle-app\assets\app_icon.png"
ARCADE_COIN_FACE = r"C:\src\puzzle-app\assets\images\coin_gold.png"
RES = r"C:\src\dgd-native\android\app\src\main\res"
APPLE = r"C:\src\dgd-native\apple\DigitalGoldTicker\Assets.xcassets"
PREVIEW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon_preview")

SS = 4  # supersample factor

# Measured from the arcade coin (see sample_icon.py output).
GOLD_TOP = (255, 214, 121)
GOLD_MID = (251, 204, 97)
GOLD_LOW = (243, 188, 66)
GOLD_RIM_DEEP = (208, 156, 52)
GLYPH = (92, 62, 4)
BACKDROP = (14, 13, 12)  # near-black, the DGD page colour

ADAPTIVE_COIN = 0.62  # of canvas — the 72/108dp safe zone
LEGACY_COIN = 0.74    # legacy icons are not safe-zone cropped


def glyph_mask() -> Image.Image:
    """The DGD spiral G, lifted from the arcade coin as an alpha mask.

    Redrawing the mark from scratch would risk getting it subtly wrong; this
    guarantees the app and the arcade show the identical glyph.
    """
    src = Image.open(ARCADE_ICON).convert("RGBA")
    w, h = src.size
    px = src.load()
    mask = Image.new("L", (w, h), 0)
    mp = mask.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a > 160 and (r + g + b) < 330:  # the dark brown glyph only
                mp[x, y] = 255
    return mask.crop(mask.getbbox())


def vertical_gradient(size: int, stops) -> Image.Image:
    """stops: [(position 0..1, (r,g,b)), ...] ascending."""
    grad = Image.new("RGB", (1, size))
    gp = grad.load()
    for y in range(size):
        t = y / max(1, size - 1)
        lo = max(i for i, (p, _) in enumerate(stops) if p <= t or i == 0)
        hi = min(lo + 1, len(stops) - 1)
        p0, c0 = stops[lo]
        p1, c1 = stops[hi]
        k = 0.0 if p1 == p0 else (t - p0) / (p1 - p0)
        gp[0, y] = tuple(round(c0[i] + (c1[i] - c0[i]) * k) for i in range(3))
    return grad.resize((size, size), Image.NEAREST)


def coin(diameter: int, glyph: Image.Image) -> Image.Image:
    """A flat gold coin on transparency, `diameter` px across."""
    d = diameter * SS
    out = Image.new("RGBA", (d, d), (0, 0, 0, 0))

    body = vertical_gradient(d, [
        (0.00, GOLD_TOP),
        (0.30, GOLD_MID),
        (0.80, GOLD_LOW),
        (1.00, GOLD_TOP),  # bright kick off the bottom rim
    ]).convert("RGBA")
    disc = Image.new("L", (d, d), 0)
    ImageDraw.Draw(disc).ellipse((0, 0, d - 1, d - 1), fill=255)
    out.paste(body, (0, 0), disc)

    draw = ImageDraw.Draw(out)

    # Milled double rim: a deeper ring inset from the edge, then the inner
    # field lifted a shade so the rim reads as raised metal.
    rim_w = max(1, int(d * 0.030))
    inset = d * 0.075
    draw.ellipse((inset, inset, d - 1 - inset, d - 1 - inset),
                 outline=GOLD_RIM_DEEP + (255,), width=rim_w)

    field_inset = d * 0.135
    field_d = int(d - 2 * field_inset)
    field = vertical_gradient(field_d, [
        (0.00, GOLD_TOP),
        (0.55, GOLD_MID),
        (1.00, GOLD_LOW),
    ]).convert("RGBA")
    field_mask = Image.new("L", (field_d, field_d), 0)
    ImageDraw.Draw(field_mask).ellipse((0, 0, field_d - 1, field_d - 1), fill=255)
    out.paste(field, (int(field_inset), int(field_inset)), field_mask)

    # The G, at 58% of the coin.
    g_target = int(d * 0.58)
    gw, gh = glyph.size
    scale = g_target / max(gw, gh)
    g = glyph.resize((max(1, int(gw * scale)), max(1, int(gh * scale))), Image.LANCZOS)
    ink = Image.new("RGBA", g.size, GLYPH + (255,))
    out.paste(ink, ((d - g.size[0]) // 2, (d - g.size[1]) // 2), g)

    return out.resize((diameter, diameter), Image.LANCZOS)


def on_canvas(size: int, coin_frac: float, glyph: Image.Image,
              background=None, round_mask=False) -> Image.Image:
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    if background is not None:
        bg = Image.new("RGBA", (size, size), background + (255,))
        if round_mask:
            m = Image.new("L", (size * SS, size * SS), 0)
            ImageDraw.Draw(m).ellipse((0, 0, size * SS - 1, size * SS - 1), fill=255)
            canvas.paste(bg, (0, 0), m.resize((size, size), Image.LANCZOS))
        else:
            canvas.paste(bg, (0, 0))
    c = coin(max(1, int(size * coin_frac)), glyph)
    canvas.paste(c, ((size - c.size[0]) // 2, (size - c.size[1]) // 2), c)
    return canvas


def monochrome(size: int, glyph: Image.Image) -> Image.Image:
    """Themed-icon layer: solid coin with the G knocked out, so the tinted
    result still reads as a coin rather than a filled blob."""
    d = int(size * ADAPTIVE_COIN) * SS
    layer = Image.new("L", (d, d), 0)
    ImageDraw.Draw(layer).ellipse((0, 0, d - 1, d - 1), fill=255)
    g_target = int(d * 0.58)
    gw, gh = glyph.size
    scale = g_target / max(gw, gh)
    g = glyph.resize((max(1, int(gw * scale)), max(1, int(gh * scale))), Image.LANCZOS)
    layer.paste(Image.new("L", g.size, 0), ((d - g.size[0]) // 2, (d - g.size[1]) // 2), g)
    small = layer.resize((int(size * ADAPTIVE_COIN), int(size * ADAPTIVE_COIN)), Image.LANCZOS)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    white = Image.new("RGBA", small.size, (255, 255, 255, 255))
    out.paste(white, ((size - small.size[0]) // 2, (size - small.size[1]) // 2), small)
    return out


DENSITIES = {  # name: (adaptive layer px @108dp, legacy px @48dp)
    "mdpi": (108, 48),
    "hdpi": (162, 72),
    "xhdpi": (216, 96),
    "xxhdpi": (324, 144),
    "xxxhdpi": (432, 192),
}


def main() -> None:
    os.makedirs(PREVIEW, exist_ok=True)
    g = glyph_mask()
    print(f"glyph mask lifted from the arcade coin: {g.size[0]}x{g.size[1]}")

    written = 0
    for name, (adaptive, legacy) in DENSITIES.items():
        d = os.path.join(RES, f"mipmap-{name}")
        os.makedirs(d, exist_ok=True)
        on_canvas(adaptive, ADAPTIVE_COIN, g).save(
            os.path.join(d, "ic_launcher_foreground.png"))
        monochrome(adaptive, g).save(os.path.join(d, "ic_launcher_monochrome.png"))
        on_canvas(legacy, LEGACY_COIN, g, background=BACKDROP).save(
            os.path.join(d, "ic_launcher.png"))
        on_canvas(legacy, LEGACY_COIN, g, background=BACKDROP, round_mask=True).save(
            os.path.join(d, "ic_launcher_round.png"))
        written += 4
    print(f"android: {written} icon layers across {len(DENSITIES)} densities")

    # The coin face the ticker header spins. Same file the arcade renders.
    face = Image.open(ARCADE_COIN_FACE).convert("RGBA")
    face.save(os.path.join(RES, "drawable", "dgd_coin_face.png"))
    print(f"android: drawable/dgd_coin_face.png {face.size[0]}x{face.size[1]} "
          "(copied from the arcade)")

    # Play listing + previews.
    on_canvas(512, LEGACY_COIN, g, background=BACKDROP).save(
        os.path.join(PREVIEW, "ic_launcher-playstore.png"))

    # Apple: 1024 square, no alpha, iOS applies its own mask.
    ios = on_canvas(1024, ADAPTIVE_COIN, g, background=BACKDROP).convert("RGB")
    ios_path = os.path.join(APPLE, "AppIcon.appiconset", "AppIcon.png")
    if os.path.exists(ios_path):
        shutil.copy2(ios_path, os.path.join(PREVIEW, "AppIcon.previous.png"))
    ios.save(ios_path)
    print(f"apple: AppIcon.png replaced (previous kept in {PREVIEW})")

    face_set = os.path.join(APPLE, "DGDCoinFace.imageset")
    os.makedirs(face_set, exist_ok=True)
    face.save(os.path.join(face_set, "DGDCoinFace.png"))
    with open(os.path.join(face_set, "Contents.json"), "w", encoding="utf-8") as fh:
        fh.write(
            '{\n  "images" : [\n    {\n      "filename" : "DGDCoinFace.png",\n'
            '      "idiom" : "universal",\n      "scale" : "1x"\n    },\n'
            '    {\n      "idiom" : "universal",\n      "scale" : "2x"\n    },\n'
            '    {\n      "idiom" : "universal",\n      "scale" : "3x"\n    }\n'
            '  ],\n  "info" : {\n    "author" : "xcode",\n    "version" : 1\n  }\n}\n'
        )
    print("apple: DGDCoinFace.imageset written")

    # Contact sheet, so the icon can be judged before anything is installed.
    tiles = [
        ("adaptive fg", on_canvas(256, ADAPTIVE_COIN, g)),
        ("as launcher masks it", on_canvas(256, ADAPTIVE_COIN, g, background=BACKDROP,
                                           round_mask=True)),
        ("legacy square", on_canvas(256, LEGACY_COIN, g, background=BACKDROP)),
        ("themed", monochrome(256, g)),
        ("48dp actual size", on_canvas(48, ADAPTIVE_COIN, g, background=BACKDROP,
                                       round_mask=True).resize((256, 256), Image.NEAREST)),
    ]
    sheet = Image.new("RGB", (256 * len(tiles), 256), (40, 40, 44))
    for i, (_, t) in enumerate(tiles):
        sheet.paste(t, (256 * i, 0), t)
    sheet.save(os.path.join(PREVIEW, "contact_sheet.png"))
    print("preview: contact_sheet.png  (" + ", ".join(n for n, _ in tiles) + ")")


if __name__ == "__main__":
    main()
