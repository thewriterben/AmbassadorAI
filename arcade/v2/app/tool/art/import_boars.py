"""Imports finished boar art into the game's sheet contract.

    python tool/art/import_boars.py tool/art/source/boar_piglet.webp         tool/art/source/boar_juvenile.webp tool/art/source/boar_razorback.webp

The owner's originals (2026-09-27) are in tool/art/source/, so the sheets can
always be rebuilt from them.

Each source is one transparent image of the boar in flight, facing either
way (--facing left mirrors it; the game's boar faces right). For each stage
this:

  1. mirrors it to face right, if needed;
  2. drops detached specks (sparkles, stray pixels) that are not part of the
     boar, so the frame fits the boar, not its glitter;
  3. crops and centres it in a square frame with a little margin;
  4. writes an eight-frame sheet (see lib/arcade/passage/boar.dart): the one
     pose throughout, with a small bob across the wing cycle, a red-tinted
     hurt frame, and a stretched dash frame. The game adds the rest of the
     motion (pitch, a wingbeat squash, the glow);
  5. rebuilds the home-card image from the razorback.

Then run tool/art/check_sheets.py for the hoof line, and set the placement
numbers in BoarSpec.
"""
import argparse
import os
from collections import deque

import numpy as np
from PIL import Image, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "..", "assets", "images"))
STAGES = ["piglet", "juvenile", "razorback"]
FRAME = 320  # px per square frame in the sheet
FRAMES = 8


def main_component(img, keep=0.02, scale=4):
    """The boar alone: the largest connected shape, plus anything touching it
    or at least [keep] of its size. Found on a mask shrunk by [scale], where
    sparkles fall apart into specks."""
    a = np.array(img.getchannel("A")) > 0
    h, w = a.shape
    small = np.array(Image.fromarray(a.astype(np.uint8) * 255).resize((w // scale, h // scale), Image.BOX)) > 40
    sh, sw = small.shape
    lab = np.zeros((sh, sw), dtype=np.int32)
    sizes = [0]
    cur = 0
    for y in range(sh):
        for x in range(sw):
            if small[y, x] and not lab[y, x]:
                cur += 1
                q = deque([(y, x)])
                lab[y, x] = cur
                n = 0
                while q:
                    cy, cx = q.popleft()
                    n += 1
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            ny, nx = cy + dy, cx + dx
                            if 0 <= ny < sh and 0 <= nx < sw and small[ny, nx] and not lab[ny, nx]:
                                lab[ny, nx] = cur
                                q.append((ny, nx))
                sizes.append(n)
    biggest = max(sizes)
    keep_ids = [i for i, n in enumerate(sizes) if i and n >= biggest * keep]
    keep_small = np.isin(lab, keep_ids)
    keep_full = np.array(Image.fromarray(keep_small.astype(np.uint8) * 255).resize((w, h), Image.NEAREST)) > 0
    # Grow the kept mask a few pixels so its edge does not nick the outline.
    grown = np.array(Image.fromarray(keep_full.astype(np.uint8) * 255).filter(__import__("PIL.ImageFilter", fromlist=["x"]).MaxFilter(9))) > 0
    out = np.array(img)
    out[~(grown & a), 3] = 0
    dropped = len(sizes) - 1 - len(keep_ids)
    return Image.fromarray(out, "RGBA"), dropped


def to_frame(img):
    """Crop to the art and centre it in a square with 4% margin."""
    img = img.crop(img.getchannel("A").getbbox())
    side = int(max(img.size) * 1.08)
    sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    sq.paste(img, ((side - img.width) // 2, (side - img.height) // 2), img)
    return sq.resize((FRAME, FRAME), Image.LANCZOS)


def sheet(frame):
    frames = []
    for i in range(FRAMES):
        f = frame
        if i in (0, 1, 2, 3):
            # A small bob across the wing cycle: up, level, down, level.
            dy = [-3, 0, 3, 0][i]
            f = Image.new("RGBA", frame.size, (0, 0, 0, 0))
            f.paste(frame, (0, dy), frame)
        elif i == 4:
            # Hurt: tinted toward red, alpha untouched.
            r, g, b, a = frame.split()
            rgb = Image.merge("RGB", (r, g, b))
            red = Image.new("RGB", frame.size, (255, 60, 50))
            rgb = Image.blend(rgb, red, 0.35)
            f = Image.merge("RGBA", (*rgb.split(), a))
        elif i == 5:
            # Dash: stretched along the line of flight.
            w = int(FRAME * 1.05)
            st = frame.resize((w, int(FRAME * 0.95)), Image.LANCZOS)
            f = Image.new("RGBA", frame.size, (0, 0, 0, 0))
            f.paste(st, ((FRAME - w) // 2, int(FRAME * 0.025)), st)
        frames.append(f)
    out = Image.new("RGBA", (FRAME * FRAMES, FRAME), (0, 0, 0, 0))
    for i, f in enumerate(frames):
        out.paste(f, (i * FRAME, 0), f)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sources", nargs=3, help="piglet, juvenile, razorback images")
    ap.add_argument("--facing", default="left", choices=["left", "right"], help="which way the sources face")
    ap.add_argument("--preview")
    args = ap.parse_args()
    frames = {}
    for stage, src in zip(STAGES, args.sources):
        img = Image.open(src).convert("RGBA")
        if args.facing == "left":
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img, dropped = main_component(img)
        fr = to_frame(img)
        frames[stage] = fr
        sheet(fr).save(os.path.join(OUT, f"boar_{stage}.png"))
        print(f"{stage}: {src} -> boar_{stage}.png, {dropped} detached specks dropped")
    # Home card: the razorback, trimmed and squared.
    rb = frames["razorback"]
    rb = rb.crop(rb.getchannel("A").getbbox())
    side = max(rb.size) + 8
    card = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    card.paste(rb, ((side - rb.width) // 2, (side - rb.height) // 2), rb)
    card.resize((256, 256), Image.LANCZOS).save(os.path.join(OUT, "card_pigs.png"))
    if args.preview:
        pv = Image.new("RGBA", (FRAME * 3, FRAME), (22, 28, 44, 255))
        for i, st in enumerate(STAGES):
            pv.alpha_composite(frames[st], (i * FRAME, 0))
        pv.save(args.preview)


if __name__ == "__main__":
    main()
