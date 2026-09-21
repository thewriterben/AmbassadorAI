"""Write the DGD coin into the iOS app icon set.

`install_app_icon.py` covered Android adaptive/legacy/themed mipmaps, the Play
listing icon and the PWA set, but never touched iOS — so `ios/Runner` still
shipped the stock Flutter logo. On a Mac that is the icon that would appear on
the home screen and in TestFlight.

Two things differ from Android and both matter:

  * **No alpha, anywhere.** iOS rejects app icons with transparency, and the
    1024 marketing icon in particular is validated at upload. Every size here
    is flattened onto the same near-black plate the rest of the brand uses.
  * **No rounded corners of our own.** iOS applies its own superellipse mask.
    Baking a radius in leaves a pale halo inside the system's corners, so the
    plate is drawn as a full square.

Source is `assets/app_icon.png`, the 1024px coin on transparency that
`install_app_icon.py` already writes, so this stays in step with whichever coin
style is installed — run it after that one.

    python tools/gen_ios_icon.py
"""
import os

from PIL import Image

APP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(APP, "assets", "app_icon.png")
OUT = os.path.join(APP, "ios", "Runner", "Assets.xcassets", "AppIcon.appiconset")

BG_HEX = "#0E0D0C"

# Exactly the filenames the existing Contents.json references. Point sizes are
# multiplied by the @Nx scale to get pixels.
SIZES = {
    "Icon-App-20x20@1x.png": 20,
    "Icon-App-20x20@2x.png": 40,
    "Icon-App-20x20@3x.png": 60,
    "Icon-App-29x29@1x.png": 29,
    "Icon-App-29x29@2x.png": 58,
    "Icon-App-29x29@3x.png": 87,
    "Icon-App-40x40@1x.png": 40,
    "Icon-App-40x40@2x.png": 80,
    "Icon-App-40x40@3x.png": 120,
    "Icon-App-60x60@2x.png": 120,
    "Icon-App-60x60@3x.png": 180,
    "Icon-App-76x76@1x.png": 76,
    "Icon-App-76x76@2x.png": 152,
    "Icon-App-83.5x83.5@2x.png": 167,
    "Icon-App-1024x1024@1x.png": 1024,
}


def main():
    if not os.path.exists(SRC):
        raise SystemExit(f"missing {SRC} - run tools/install_app_icon.py first")
    coin = Image.open(SRC).convert("RGBA")
    n = coin.size[0]

    bg = tuple(int(BG_HEX[i:i + 2], 16) for i in (1, 3, 5))
    plate = Image.new("RGB", (n, n), bg)
    plate.paste(coin, (0, 0), coin)

    for name, px in SIZES.items():
        plate.resize((px, px), Image.LANCZOS).save(
            os.path.join(OUT, name), optimize=True)

    print("wrote %d iOS icons to ios/Runner/Assets.xcassets/AppIcon.appiconset"
          % len(SIZES))
    print("  source     assets/app_icon.png (%dpx)" % n)
    print("  plate      %s, opaque, square (iOS masks its own corners)" % BG_HEX)


if __name__ == "__main__":
    main()
