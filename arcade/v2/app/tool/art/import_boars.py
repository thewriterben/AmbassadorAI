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

A stage can instead have a drawn wingbeat: tool/art/source/boar_{stage}_cycle_1
.. _N.png, the owner's frames split out of a sheet by split_frames.py (all
three stages, 2026-09-28: four drawings for the piglet and the juvenile,
six for the razorback). Then those are the wing cycle as drawn, with no rig,
and the other frames are made from them (see drawn_sheet); the sheet has
N + 4 frames, and boar.dart must say so for N other than four
(BoarFrames(6)). The single pose given on the command line is not used for
that stage.

The six frames after the wing cycle (hurt, dash, land, stand, landwin,
stand2) can be drawn too: tool/art/source/boar_{stage}_{pose}.png, any of
them. Each drawn one replaces the one made from the wingbeat. landwin is the
touchdown after a whole passage (glad, where land may be a teary flop) and
stand2 a second standing pose the boar alternates with stand; undrawn, they
repeat land and stand. They come from a
pose sheet, split and registered to the wingbeat by split_frames.py:

    python tool/art/split_frames.py poses.jpg tool/art/source/boar_juvenile \
        --ref tool/art/source/boar_juvenile_cycle_1.png --names hurt,dash,land,stand

(add --holes for the juvenile and razorback, as for their wingbeats; for a
sheet of only some poses, --frames and --names say which, in reading order).
The poses are cropped and scaled with the wingbeat's box, not a box of their
own, so adding them moves nothing: the placement numbers in boar.dart stay
right, and a pose that reaches past the frame's margin is reported as cut
off. Standing is the frame footV is measured on, so a drawn stand means
running check_sheets.py again.

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

# For a drawn wingbeat: which drawing (from 0, in cycle order) has the wings
# most tucked in, for standing and the dash. The piglet's is its last,
# folding in; the juvenile's its third, "low/compact" (its last is the
# upstroke, wings raised again); the razorback's its fourth of six, "fully
# down and folding".
DRAWN_FOLDED = {"piglet": 3, "juvenile": 2, "razorback": 3}

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


def to_frames(imgs, extra=()):
    """Several drawings of one boar, cropped alike to the box that holds all
    of them and centred as to_frame does, so a body that does not move
    between drawings does not move between frames either. [extra] drawings
    (the poses) are cropped with the same box, without widening it; what of
    them falls outside the frame is cut off, and reported."""
    boxes = [im.getchannel("A").getbbox() for im in imgs]
    box = (min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes))
    w, h = box[2] - box[0], box[3] - box[1]
    side = int(max(w, h) * PAD)
    # The square each drawing is cut to, in its own coordinates.
    sq_box = (box[0] - (side - w) // 2, box[1] - (side - h) // 2)
    sq_box = (*sq_box, sq_box[0] + side, sq_box[1] + side)
    out = []
    for im in [*imgs, *extra]:
        # Cropped straight to the square, and not pasted with its own alpha
        # as the mask: that squares a partial alpha, and thinned the soft
        # edges of a pose scaled to fit. The colour under clear pixels is
        # cleared, as the paste left it, so the sheets from solid drawings
        # come out as before.
        a = np.array(im.crop(sq_box))
        a[a[:, :, 3] == 0] = 0
        ys, xs = np.nonzero(np.array(im.getchannel("A")) > 0)
        cut = int(((xs < sq_box[0]) | (xs >= sq_box[2]) | (ys < sq_box[1]) | (ys >= sq_box[3])).sum())
        if cut > 0:
            print(f"  warning: {cut} px of a drawing fall outside its frame and are cut off")
        out.append(Image.fromarray(a, "RGBA").resize((FRAME, FRAME), Image.LANCZOS))
    return out


POSES = ("hurt", "dash", "land", "stand", "landwin", "stand2")


def drawn_cycle(stage, facing):
    """The owner's drawn wingbeat for [stage], mirrored and de-sparkled, and
    whichever of its poses are drawn (a dict by name), as frames; or None
    if the stage has no drawn wingbeat."""
    paths = []
    while os.path.exists(p := os.path.join(HERE, "source", f"boar_{stage}_cycle_{len(paths) + 1}.png")):
        paths.append(p)
    if len(paths) < 2:
        return None
    def load(p):
        im = Image.open(p).convert("RGBA")
        if facing == "left":
            im = im.transpose(Image.FLIP_LEFT_RIGHT)
        return main_component(im)[0]

    names = [n for n in POSES if os.path.exists(os.path.join(HERE, "source", f"boar_{stage}_{n}.png"))]
    frames = to_frames([load(p) for p in paths], [load(os.path.join(HERE, "source", f"boar_{stage}_{n}.png")) for n in names])
    return frames[:len(paths)], dict(zip(names, frames[len(paths):]))


def drawn_sheet(cycle, stage, poses=None):
    """The sheet from a drawn wingbeat. The drawings are the cycle frames,
    in order, starting wings-up (the owner's sheets do); then the poses,
    each as drawn if it is in [poses], else borrowed from the wingbeat:
    hurt the second drawing tinted red, dash the most folded one
    (DRAWN_FOLDED) stretched along the line of flight, landing the wings-up
    one (braking), and standing the folded one."""
    poses = poses or {}
    up, mid = cycle[0], cycle[1]
    fold = cycle[DRAWN_FOLDED.get(stage, 3)]
    made = {"hurt": hurt(mid), "dash": dash(fold), "land": up, "stand": fold}
    got = {n: poses.get(n, made.get(n)) for n in ("hurt", "dash", "land", "stand")}
    # The two later poses repeat land and stand where they are not drawn: a
    # glad landing that is the landing, a second stand that is the stand.
    got["landwin"] = poses.get("landwin", got["land"])
    got["stand2"] = poses.get("stand2", got["stand"])
    frames = [*cycle, *[got[n] for n in POSES]]
    out = Image.new("RGBA", (FRAME * len(frames), FRAME), (0, 0, 0, 0))
    for i, f in enumerate(frames):
        out.paste(f, (i * FRAME, 0), f)
    return out


def hurt(frame):
    """Tinted toward red, alpha untouched."""
    r, g, b, a = frame.split()
    rgb = Image.blend(Image.merge("RGB", (r, g, b)), Image.new("RGB", frame.size, (255, 60, 50)), 0.35)
    return Image.merge("RGBA", (*rgb.split(), a))


def dash(frame):
    """Stretched along the line of flight."""
    w = int(FRAME * 1.05)
    st = frame.resize((w, int(FRAME * 0.95)), Image.LANCZOS)
    f = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    f.paste(st, ((FRAME - w) // 2, int(FRAME * 0.025)), st)
    return f


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
            f = hurt(frame)
        elif i == 5:
            f = dash(frame)
        frames.append(f)
    # The glad landing and the second stand, as the landing and the stand.
    frames += [frames[6], frames[7]]
    out = Image.new("RGBA", (FRAME * len(frames), FRAME), (0, 0, 0, 0))
    for i, f in enumerate(frames):
        out.paste(f, (i * FRAME, 0), f)
    return out


def save_sheet(img, stage):
    """Writes a stage's sheet as lossy WebP, quality 90: the three sheets
    came to 2.7 MB as PNG and a fraction of it this way, with the fur and
    feathers unchanged at four times zoom. An old PNG of it is removed, so
    the app does not ship both."""
    img.save(os.path.join(OUT, f"boar_{stage}.webp"), "WEBP", quality=90, method=6)
    old = os.path.join(OUT, f"boar_{stage}.png")
    if os.path.exists(old):
        os.remove(old)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sources", nargs=3, help="piglet, juvenile, razorback images")
    ap.add_argument("--facing", default="left", choices=["left", "right"], help="which way the sources face")
    ap.add_argument("--preview")
    args = ap.parse_args()
    frames = {}
    for stage, src in zip(STAGES, args.sources):
        drawn = drawn_cycle(stage, args.facing)
        if drawn:
            cycle, poses = drawn
            frames[stage] = cycle[0]
            save_sheet(drawn_sheet(cycle, stage, poses), stage)
            made = ", ".join(n for n in POSES[:4] if n not in poses)
            repeated = [n for n in POSES[4:] if n not in poses]
            print(f"{stage}: drawn wingbeat (source/boar_{stage}_cycle_1..{len(cycle)}.png)"
                  f", drawn poses: {', '.join(poses) or 'none'}"
                  f"{f', made from the wingbeat: {made}' if made else ''}"
                  f"{f', repeating land/stand for: {chr(44).join(repeated)}' if repeated else ''} -> boar_{stage}.webp")
            continue
        img = Image.open(src).convert("RGBA")
        if args.facing == "left":
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img, dropped = main_component(img)
        fr = to_frame(img)
        frames[stage] = fr
        save_sheet(sheet(fr, stage), stage)
        print(f"{stage}: {src} -> boar_{stage}.webp, {dropped} detached specks dropped")
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
