"""Makes coin_gold_shiny.png: When Pigs Fly's gold coin, polished.

The shared coin_gold.png is also the brand's hero coin on the home screen
and the leaderboard's first-place medal, so it is left as it is; this is a
separate, shinier copy for the game only. Like the copper
(gen_copper_coin.py) it maps the gold render's brightness through a colour
ramp: deep amber in the grooves, rich saturated gold in the body, and a
near-white warm glint at the top. The wider range, darker shadows and
hotter highlights, is what reads as polish; the game adds a moving glint on
top (passage_render.dart).

    python tools/gen_shiny_gold_coin.py

Source: tools/source/coin_gold_for_silver.png (the gold coin as it was).
"""
import os

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "source", "coin_gold_for_silver.png")
OUT = os.path.join(HERE, "..", "assets", "images", "coin_gold_shiny.png")

STOPS = [
    (0, (30, 14, 0)),
    (60, (92, 48, 4)),
    (120, (170, 102, 10)),
    (170, (224, 160, 30)),
    (205, (248, 204, 70)),
    (230, (255, 232, 140)),
    (246, (255, 248, 210)),
    (255, (255, 255, 244)),
]

a = np.array(Image.open(SRC).convert("RGBA")).astype(float)
lum = a[:, :, :3] @ np.array([0.299, 0.587, 0.114])
xs = [s[0] for s in STOPS]
rgb = np.stack([np.interp(lum, xs, [s[1][c] for s in STOPS]) for c in range(3)], axis=-1)
out = np.dstack([rgb, a[:, :, 3]]).astype(np.uint8)
Image.fromarray(out, "RGBA").save(OUT)
m = out[:, :, 3] > 200
print("wrote", os.path.normpath(OUT), "median brightness", int(np.median(out[m][:, :3].mean(axis=1))))
