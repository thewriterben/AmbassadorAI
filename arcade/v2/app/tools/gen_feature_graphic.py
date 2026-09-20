"""Play feature graphic, 1024x500.

Play shows this at the top of the listing and crops it hard on some surfaces,
so everything that matters stays well inside the middle. Constraints Play
enforces: exactly 1024x500, no alpha channel, PNG or JPEG.

Built from assets already in the app rather than anything new, so it cannot
drift from what the app looks like.
"""
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

APP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(APP, "assets")
OUT = r"F:\Documents\GitHub\AmbassadorAI\arcade\store"

W, H = 1024, 500
BG = (14, 13, 12)
GOLD = (233, 163, 25)
TEXT = (245, 243, 240)
MUTED = (150, 145, 138)


def _font(names, size):
    for n in names:
        for d in (r"C:\Windows\Fonts",):
            p = os.path.join(d, n)
            if os.path.exists(p):
                try:
                    return ImageFont.truetype(p, size)
                except OSError:
                    pass
    return ImageFont.load_default()


def main():
    os.makedirs(OUT, exist_ok=True)
    img = Image.new("RGB", (W, H), BG)

    # Warm glow behind the coin, matching the app's home screen.
    glow = Image.new("RGB", (W, H), BG)
    gd = ImageDraw.Draw(glow)
    gd.ellipse((W - 470, H // 2 - 240, W - 30, H // 2 + 200), fill=(70, 46, 8))
    img = Image.blend(img, glow.filter(ImageFilter.GaussianBlur(90)), 0.95)

    # The coin, from the icon source so it always matches the shipped art.
    coin_path = os.path.join(ASSETS, "app_icon.png")
    coin = Image.open(coin_path).convert("RGBA")
    size = 360
    coin = coin.resize((size, size), Image.LANCZOS)
    img.paste(coin, (W - size - 70, (H - size) // 2), coin)

    d = ImageDraw.Draw(img)
    title_a = _font(["seguisb.ttf", "segoeui.ttf", "arialbd.ttf"], 78)
    title_b = _font(["georgiai.ttf", "georgia.ttf", "timesi.ttf"], 78)
    sub = _font(["segoeui.ttf", "arial.ttf"], 30)
    mono = _font(["consola.ttf", "cour.ttf"], 22)

    x, y = 64, 150
    d.text((x, y), "DGD ", font=title_a, fill=TEXT)
    w = d.textlength("DGD ", font=title_a)
    d.text((x + w, y), "Arcade", font=title_b, fill=GOLD)

    d.text((x, y + 104), "Match the coins through the", font=sub, fill=MUTED)
    d.text((x, y + 144), "story of Digital Gold.", font=sub, fill=MUTED)

    d.text((x, H - 74), "SIXTY LEVELS  ·  NO ADS  ·  NO PURCHASES", font=mono, fill=(120, 116, 110))

    out = os.path.abspath(os.path.join(OUT, "feature-graphic-1024x500.png"))
    img.save(out, optimize=True)
    print("wrote", out, img.size, img.mode)


if __name__ == "__main__":
    main()
