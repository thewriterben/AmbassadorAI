"""Makes coin_rose.png: polished rose gold, the leaderboard's third place.

Like the silver and copper (gen_silver_coin.py, gen_copper_coin.py) it is
made from the gold coin's render, the same design with full shading,
through a colour ramp: deep plum-brown in the grooves, a warm pink-copper
body, and a pale blush at the top. It sits between the copper's orange and
the silver's cool grey, so the three medals read as a set of metals.

    python tools/gen_rose_coin.py

Source: tools/source/coin_gold_for_silver.png. The original rose render is
kept as tools/source/coin_rose_original.png.
"""
import os

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "source", "coin_gold_for_silver.png")
OUT = os.path.join(HERE, "..", "assets", "images", "coin_rose.png")

STOPS = [
    (0, (26, 8, 8)),
    (70, (80, 30, 28)),
    (125, (150, 72, 64)),
    (165, (200, 112, 98)),
    (195, (228, 148, 132)),
    (222, (246, 188, 172)),
    (242, (255, 222, 210)),
    (255, (255, 244, 238)),
]

a = np.array(Image.open(SRC).convert("RGBA")).astype(float)
lum = a[:, :, :3] @ np.array([0.299, 0.587, 0.114])
xs = [s[0] for s in STOPS]
rgb = np.stack([np.interp(lum, xs, [s[1][c] for s in STOPS]) for c in range(3)], axis=-1)
out = np.dstack([rgb, a[:, :, 3]]).astype(np.uint8)
Image.fromarray(out, "RGBA").save(OUT)
m = out[:, :, 3] > 200
print("wrote", os.path.normpath(OUT), "median brightness", int(np.median(out[m][:, :3].mean(axis=1))))
