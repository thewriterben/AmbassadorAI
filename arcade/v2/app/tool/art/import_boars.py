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
  4. rigs the wings: each is cut out along the line where it meets the back
     (WINGS below, measured on a grid) and turned about its shoulder, so the
     sheet has a real wingbeat — up, level, down, folding back — while the
     body, and all its detail, stays exactly as drawn. The wings sit behind
     the body layer, which covers their roots, so a lowered wing tucks behind
     the back instead of leaving a hole where it was;
  5. writes the eight-frame sheet (see lib/arcade/passage/boar.dart): the
     wing cycle with a small bob, a red-tinted hurt frame, a swept-back dash
     frame, and a landing frame braking with the wings raised;
  6. rebuilds the home-card image from the razorback.

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
FRAME = 448  # px per square frame in the sheet

# The frame's side as a multiple of the art's larger dimension. The art sits
# in the middle; the rest is headroom for the wings to swing into. At the
# first, gentle beat 1.08 was enough; the bigger beat needs this. Changing it
# changes where the boar sits in the frame: BoarSpec in boar.dart has to be
# rescaled with it (sizes up by the ratio, anchors toward 0.5 by it).
PAD = 1.5
FRAMES = 8

# WINGS was measured on frames padded by this much; split_wings maps it onto
# the current PAD, so the padding can change without re-measuring.
WINGS_PAD = 1.08

# Each wing: the region to lift off (a polygon in fractions of the frame,
# drawn above the line where the wing meets the back, so the root stays on
# the body), and the shoulder it turns about. "key" lifts only pixels of the
# wing's own colouring (and their outline) from inside the polygon — the
# piglet's white feathers, which the polygon alone cannot separate from the
# gold-striped back they overlap.
WINGS = {
    "piglet": [
        dict(poly=[(0.03, 0.12), (0.22, 0.15), (0.36, 0.28), (0.45, 0.43), (0.44, 0.50), (0.36, 0.49),
                   (0.18, 0.45), (0.06, 0.37), (0.03, 0.24)], pivot=(0.41, 0.47), key="white"),
        dict(poly=[(0.60, 0.01), (0.80, 0.01), (0.81, 0.30), (0.74, 0.36), (0.62, 0.36), (0.59, 0.15)],
             pivot=(0.68, 0.34), key="white"),
    ],
    "juvenile": [
        # Down to just above the tail and the back: the lowest feathers hang to
        # 0.53, and cut higher they stayed behind as a sliver on the upstroke.
        dict(poly=[(0.01, 0.06), (0.14, 0.04), (0.30, 0.18), (0.41, 0.29), (0.48, 0.41), (0.49, 0.47),
                   (0.44, 0.52), (0.38, 0.535), (0.32, 0.53), (0.285, 0.51), (0.24, 0.52), (0.18, 0.50),
                   (0.02, 0.43)], pivot=(0.45, 0.47)),
        dict(poly=[(0.59, 0.37), (0.71, 0.22), (0.86, 0.07), (0.99, 0.08), (0.99, 0.31), (0.86, 0.38),
                   (0.74, 0.43), (0.66, 0.43), (0.61, 0.41)], pivot=(0.64, 0.42)),
    ],
    "razorback": [
        # The membrane's lowest point nearly touches the tail's curl; the cut
        # runs between them at x = 0.278.
        dict(poly=[(0.01, 0.11), (0.21, 0.13), (0.38, 0.22), (0.41, 0.33), (0.44, 0.44), (0.46, 0.48),
                   (0.40, 0.50), (0.30, 0.485), (0.279, 0.49), (0.279, 0.535), (0.25, 0.535), (0.21, 0.52),
                   (0.09, 0.45), (0.01, 0.30)],
             pivot=(0.43, 0.47)),
        dict(poly=[(0.63, 0.43), (0.65, 0.30), (0.70, 0.24), (0.85, 0.15), (0.98, 0.13), (0.93, 0.30),
                   (0.86, 0.41), (0.77, 0.46), (0.70, 0.46)], pivot=(0.66, 0.45)),
    ],
}

# Wing angle per frame, degrees: positive lowers the wing tip. Frames 0-3 are
# the beat (up, level, down, folding back); 4 hurt; 5 dash; 6 landing; 7 at
# rest.
WING_ANGLES = [-30, 0, 48, 14, 8, 18, -32, 0]

# How far from the shoulder (fraction of the frame) the fan that fills the
# root of a turned wing reaches. See posed().
ROOT_FAN = 0.10


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


def split_wings(frame, stage):
    """The body without its wings, and each wing on its own layer with the
    sign that lowers its tip."""
    from PIL import ImageDraw
    body = frame.copy()
    wings = []
    arr = np.array(frame)
    k = WINGS_PAD / PAD

    def at(x, y):
        return ((0.5 + (x - 0.5) * k) * FRAME, (0.5 + (y - 0.5) * k) * FRAME)

    for w in WINGS.get(stage, []):
        m = Image.new("L", frame.size, 0)
        ImageDraw.Draw(m).polygon([at(x, y) for x, y in w["poly"]], fill=255)
        mask = np.array(m) > 0
        if w.get("key") == "white":
            # Everything in the region that is not the warm brown and gold of
            # the body: the white feathers, their lavender shading and their
            # dark outline. Keying on "white" alone left the shading and the
            # outline behind as faint ghost lines where the wing had been.
            rgb = arr[:, :, :3].astype(int)
            r, b = rgb[:, :, 0], rgb[:, :, 2]
            warm = (r > b + 35) & (r > 90)
            mask &= ~warm
        mask &= arr[:, :, 3] > 0
        layer = np.zeros_like(arr)
        layer[mask] = arr[mask]
        b = np.array(body)
        b[mask, 3] = 0
        body = Image.fromarray(b, "RGBA")
        ys, xs = np.nonzero(mask)
        px, py = at(*w["pivot"])
        # PIL turns counter-clockwise for a positive angle: that lowers the
        # tip of a wing reaching up and back (to the left), and raises one
        # reaching up and forward, so the sign follows the tip's side.
        sign = 1 if (xs.mean() if len(xs) else px) < px else -1
        wings.append((Image.fromarray(layer, "RGBA"), (px, py), sign))
    return body, wings


def posed(body, wings, angle):
    """The body with its wings turned by [angle].

    Turning a wing about its shoulder opens a wedge at the root between
    where it was drawn and where it now is, and on the upstroke that wedge
    showed sky through the back. It is filled with a fan: the same wing at
    the in-between angles, kept only close to the shoulder (fading out by
    ROOT_FAN), laid under the turned wing. Near the pivot a wing barely
    moves, so the fan is feathers, not a ghost. (A copy of the whole resting
    wing did the same job at the first, gentle beat; at the bigger one it
    showed as a second wing.)"""
    out = Image.new("RGBA", body.size, (0, 0, 0, 0))
    yy, xx = np.mgrid[0:body.size[1], 0:body.size[0]]
    for layer, pivot, sign in wings:
        if angle < 0:  # upstroke only: on the downstroke the wedge is sky above the back
            d = np.hypot(xx - pivot[0], yy - pivot[1]) / (ROOT_FAN * FRAME)
            fade = np.clip((1.0 - d) / 0.35, 0.0, 1.0)
            steps = max(2, int(abs(angle) / 3))
            for i in range(steps):
                a = angle * i / steps
                t = layer.rotate(sign * a, resample=Image.BICUBIC, center=pivot)
                arr = np.array(t)
                arr[:, :, 3] = (arr[:, :, 3] * fade).astype(np.uint8)
                out.alpha_composite(Image.fromarray(arr, "RGBA"))
        out.alpha_composite(layer.rotate(sign * angle, resample=Image.BICUBIC, center=pivot))
    out.alpha_composite(body)
    return out


def to_frame(img):
    """Crop to the art and centre it in a square with 4% margin."""
    img = img.crop(img.getchannel("A").getbbox())
    side = int(max(img.size) * PAD)
    sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    sq.paste(img, ((side - img.width) // 2, (side - img.height) // 2), img)
    return sq.resize((FRAME, FRAME), Image.LANCZOS)


def sheet(frame, stage):
    body, wings = split_wings(frame, stage)
    frames = []
    for i in range(FRAMES):
        frame = posed(body, wings, WING_ANGLES[i])
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
        sheet(fr, stage).save(os.path.join(OUT, f"boar_{stage}.png"))
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
