"""Makes coin_silver.png: metallic silver, from the gold coin's render.

The original silver render sat almost entirely at the top of the range
(median brightness 234 of 255, against 175 for the gold coin), with broad
blown-out areas, so next to gold and copper it read as a white disc rather
than as metal. Remapping its brightness only turned the blown areas into
blotches: the shading was not there to recover.

The gold coin is the same design, with full shading. So silver is taken from
it: the gold's brightness, lifted a little (silver is the brighter metal) and
given a cool blue-grey cast, which is what makes silver read as silver beside
warm gold. Every edge, emboss and highlight is the gold render's.

    python tools/gen_silver_coin.py

The source is tools/source/coin_gold_for_silver.png, a copy of the gold coin
as it was when this was made, so re-running never compounds. The original
silver render is kept beside it as coin_silver_original.png.
"""
import os

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "source", "coin_gold_for_silver.png")
OUT = os.path.join(HERE, "..", "assets", "images", "coin_silver.png")

# Brightness in -> out, piecewise linear: lifts the gold's midtones toward
# silver's and keeps its deep edges and bright highlights.
CURVE_IN = [0, 60, 120, 175, 220, 255]
CURVE_OUT = [22, 78, 140, 192, 232, 252]
# Cool cast, per channel.
CAST = np.array([0.94, 0.975, 1.03])

a = np.array(Image.open(SRC).convert("RGBA")).astype(float)
lum = a[:, :, :3] @ np.array([0.299, 0.587, 0.114])
new = np.interp(lum, CURVE_IN, CURVE_OUT)
rgb = np.clip(new[:, :, None] * CAST[None, None, :], 0, 255)
out = np.dstack([rgb, a[:, :, 3]]).astype(np.uint8)
Image.fromarray(out, "RGBA").save(OUT)
m = out[:, :, 3] > 200
print("wrote", os.path.normpath(OUT), "median brightness", int(np.median(out[m][:, :3].mean(axis=1))))
