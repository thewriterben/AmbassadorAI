"""PWA icons from assets/app_icon.png (1024 px, DGD coin on near-black).
Regular icons: straight resize. Maskable: coin scaled into the 80% safe
zone on a solid #020203 field so Android's mask never clips the coin."""
import os
from PIL import Image

ROOT = r"C:\src\puzzle-app"
src = Image.open(os.path.join(ROOT, "assets", "app_icon.png")).convert("RGBA")
out = os.path.join(ROOT, "web", "icons")
os.makedirs(out, exist_ok=True)

for s in (192, 512):
    src.resize((s, s), Image.LANCZOS).save(os.path.join(out, f"Icon-{s}.png"), optimize=True)
    field = Image.new("RGBA", (s, s), (2, 2, 3, 255))
    inner = int(s * 0.78)
    coin = src.resize((inner, inner), Image.LANCZOS)
    field.alpha_composite(coin, ((s - inner) // 2, (s - inner) // 2))
    field.save(os.path.join(out, f"Icon-maskable-{s}.png"), optimize=True)

src.resize((64, 64), Image.LANCZOS).save(os.path.join(ROOT, "web", "favicon.png"), optimize=True)
print("icons:", sorted(os.listdir(out)))
