"""Makes coin_copper.png: metallic copper, from the gold coin's render.

The original copper render was flat and matte next to the gold: a narrow,
dull brightness range with little specular (see tools/source/
coin_copper_original.png). Like silver (gen_silver_coin.py) it is now made
from the gold coin, the same design with full shading, but through a colour
ramp rather than a flat tint: real copper runs from deep brown in shadow
through saturated orange to pale, rosy highlights, and it is that climb
toward pink-white at the top that makes it read as polished metal.

    python tools/gen_copper_coin.py

Source: tools/source/coin_gold_for_silver.png (the gold coin as it was).
"""
import os

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "source", "coin_gold_for_silver.png")
OUT = os.path.join(HERE, "..", "assets", "images", "coin_copper.png")

# Gold brightness -> copper colour, a gradient map. Darker overall than
# silver and gold, as copper is, with the top end lifting to rose.
STOPS = [
    (0, (18, 6, 2)),
    (70, (62, 20, 6)),
    (125, (128, 50, 18)),
    (165, (182, 86, 36)),
    (195, (218, 120, 58)),
    (222, (244, 164, 100)),
    (242, (255, 212, 170)),
    (255, (255, 240, 222)),
]

a = np.array(Image.open(SRC).convert("RGBA")).astype(float)
lum = a[:, :, :3] @ np.array([0.299, 0.587, 0.114])
xs = [s[0] for s in STOPS]
rgb = np.stack([np.interp(lum, xs, [s[1][c] for s in STOPS]) for c in range(3)], axis=-1)
out = np.dstack([rgb, a[:, :, 3]]).astype(np.uint8)
Image.fromarray(out, "RGBA").save(OUT)
m = out[:, :, 3] > 200
print("wrote", os.path.normpath(OUT), "median brightness", int(np.median(out[m][:, :3].mean(axis=1))))
