"""Install a chosen coin as the app icon, everywhere it is needed.

The project shipped only legacy square `ic_launcher.png` mipmaps. Modern
Android masks those to the launcher's shape, which crops a square artwork badly
and cannot do Material You themed icons at all. This writes a proper adaptive
icon instead:

  * `foreground` — the coin on transparency, on a 108dp canvas where only the
    central 72dp is guaranteed visible, so the art stays well inside;
  * `background` — a flat colour resource, which is what lets the launcher
    animate and mask the layers independently;
  * `monochrome` — the silhouette the system tints for themed icons.

Legacy mipmaps are still written for pre-26 devices, plus the 512px Play
listing icon and the PWA set.
"""
import os
import subprocess
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter

APP = r"C:\src\puzzle-app"
RES = os.path.join(APP, "android", "app", "src", "main", "res")
ASSETS = os.path.join(APP, "assets")

# Adaptive foreground is a 108dp canvas; legacy launcher icons are 48dp.
ADAPTIVE = {"mdpi": 108, "hdpi": 162, "xhdpi": 216, "xxhdpi": 324, "xxxhdpi": 432}
LEGACY = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}

BG_HEX = "#0E0D0C"

ADAPTIVE_XML = """<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/ic_launcher_background" />
    <foreground android:drawable="@mipmap/ic_launcher_foreground" />
    <monochrome android:drawable="@mipmap/ic_launcher_monochrome" />
</adaptive-icon>
"""

BG_XML = f"""<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="ic_launcher_background">{BG_HEX}</color>
</resources>
"""


def _write(img, path, size):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.resize((size, size), Image.LANCZOS).save(path, optimize=True)


def _monochrome(coin_img):
    """Flat silhouette for themed icons: solid disc with the mark punched out.

    A themed icon is tinted by the system, so any colour in it is thrown away —
    only the alpha matters. Keeping the mark as a hole is what stops it
    becoming a featureless blob.
    """
    n = coin_img.size[0]
    a = coin_img.getchannel("A")
    # The disc, minus the soft shadow: threshold hard.
    disc = a.point(lambda v: 255 if v > 200 else 0)
    # Re-derive the mark and subtract it.
    from gen_app_icon import COIN, logo
    lg = int(n * COIN * 0.62)
    mark = logo(lg, (255, 255, 255)).getchannel("A")
    hole = Image.new("L", (n, n), 0)
    hole.paste(mark, ((n - lg) // 2, (n - lg) // 2))
    out = Image.new("RGBA", (n, n), (255, 255, 255, 0))
    out.putalpha(ImageChops.subtract(disc, hole))
    return out


def install(coin_img, style):
    n = coin_img.size[0]

    # --- adaptive foreground + monochrome -------------------------------
    mono = _monochrome(coin_img)
    for d, size in ADAPTIVE.items():
        _write(coin_img, os.path.join(RES, f"mipmap-{d}", "ic_launcher_foreground.png"), size)
        _write(mono, os.path.join(RES, f"mipmap-{d}", "ic_launcher_monochrome.png"), size)

    os.makedirs(os.path.join(RES, "mipmap-anydpi-v26"), exist_ok=True)
    for name in ("ic_launcher.xml", "ic_launcher_round.xml"):
        with open(os.path.join(RES, "mipmap-anydpi-v26", name), "w") as f:
            f.write(ADAPTIVE_XML)
    os.makedirs(os.path.join(RES, "values"), exist_ok=True)
    with open(os.path.join(RES, "values", "ic_launcher_background.xml"), "w") as f:
        f.write(BG_XML)

    # --- legacy square mipmaps (pre-26) ---------------------------------
    # These are drawn as-is, so the coin needs the plate baked in.
    plate = Image.new("RGBA", (n, n), tuple(int(BG_HEX[i:i + 2], 16) for i in (1, 3, 5)) + (255,))
    m = Image.new("L", (n, n), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, n, n), radius=int(n * 0.22), fill=255)
    legacy = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    legacy.paste(plate, (0, 0), m)
    legacy.alpha_composite(coin_img)
    for d, size in LEGACY.items():
        _write(legacy, os.path.join(RES, f"mipmap-{d}", "ic_launcher.png"), size)

    # --- Play listing: 512x512, no transparency -------------------------
    store = Image.new("RGB", (n, n), tuple(int(BG_HEX[i:i + 2], 16) for i in (1, 3, 5)))
    store.paste(coin_img, (0, 0), coin_img)
    store.resize((512, 512), Image.LANCZOS).save(
        os.path.join(APP, "..", "play-icon-512.png"), optimize=True)

    # --- in-app asset + PWA icons ---------------------------------------
    app_icon = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    app_icon.alpha_composite(coin_img)
    _write(app_icon, os.path.join(ASSETS, "app_icon.png"), 1024)

    print(f"installed style {style}")
    print(f"  adaptive     {len(ADAPTIVE)} densities + anydpi-v26 xml")
    print(f"  monochrome   {len(ADAPTIVE)} densities (themed icons)")
    print(f"  legacy       {len(LEGACY)} densities")
    print("  play icon    C:\\src\\play-icon-512.png")
    print("  assets/app_icon.png")

    web = os.path.join(APP, "tools", "gen_web_icons.py")
    if os.path.exists(web):
        subprocess.run([sys.executable, web], cwd=APP, check=False)
