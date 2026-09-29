"""Splits a sheet of hand-drawn animation frames into registered,
transparent frames, ready for import_boars.py.

    python tool/art/split_frames.py sheet.jpg tool/art/source/boar_piglet_cycle
    python tool/art/split_frames.py sheet.jpg tool/art/source/boar_juvenile_cycle --holes
    python tool/art/split_frames.py sheet.jpg tool/art/source/boar_razorback_cycle --holes --frames 6

writes boar_piglet_cycle_1.png .. _N.png, in reading order (rows top to
bottom, each left to right). --frames is how many drawings the sheet holds
(default 4).

The owner's sheets are drawn on white, with a "Frame n" label by each
frame, and saved as JPEG: the piglet's in a 2x2 grid with the labels above,
the juvenile's in a 2x2 grid with them below, the razorback's in a 3x2 grid
with two-line labels below, a wing of its first frame reaching over into
the second's columns. This:

  1. erases labels that have rows to themselves: a strip of rows, blank
     above and below, all neutral grey (the art is tinted). Done first,
     since a label strip between two rows of art would otherwise join them;
  2. finds the frames as shapes, not grid cells: the N largest connected
     shapes on the sheet are the boars, and a smaller one (a sparkle, a
     puff, a stray tip) goes with the boar nearest it, unless it is neutral
     grey, which is a label beside the art (the piglet's) and is dropped.
     The razorback's sheet has no clean gutter between its first two frames,
     so a grid cannot cut it;
  3. makes the white background transparent by flood-filling from the
     frame's edges through near-white (so white inside the art, such as the
     piglet's wings, is untouched), then trims the light JPEG fringe off the
     outline. White the fill cannot reach goes too where it is edged with
     warm colour (sky between a belly and its dust), and with --holes all
     of it, the gaps inside a curled tail or a tusk's curve, down to a few
     dozen pixels (smaller is a highlight). --holes is only for art with no
     white of its own; the piglet's white feathers hold pockets of the same
     colour and size;
  4. turns every frame to face the way the first one does: the razorback's
     second row faces the other way. Each frame is tried both ways round
     and kept the way its head matches the first frame's better;
  5. registers the frames on the head: the front of the lower body (the
     sheets face left) is the part a wingbeat does not move, so each frame
     is shifted to line its head up with the first's. Without it the whole
     boar jitters as the frames cycle. The centroid of the lower body is
     the first guess; legs tucked up in a compact frame move it (the
     juvenile's came out 38px off on the centroid alone), so the match
     searches round it.

All frames come out on one canvas size, so the importer can crop them alike.
"""
import argparse
import os
import sys
from collections import deque

import numpy as np
from PIL import Image, ImageFilter


def blocks(profile, gap=4):
    """Runs of rows (or columns) with content, split at >= [gap] blank ones."""
    out, start, blank, last = [], None, 0, 0
    for i, v in enumerate(profile):
        if v > 2:
            if start is None:
                start = i
            blank, last = 0, i
        else:
            blank += 1
            if start is not None and blank >= gap:
                out.append((start, last + 1))
                start = None
    if start is not None:
        out.append((start, len(profile)))
    return out


def neutral_share(px):
    """How much of a set of RGB pixels is neutral grey."""
    px = px.astype(int)
    return ((px.max(axis=1) - px.min(axis=1)) < 30).mean() if len(px) else 0.0


def erase_label_rows(img, max_height=160):
    """Whitens strips of rows that hold only labels. [max_height] allows a
    two-line label run together (the razorback's last, 114 rows)."""
    nonwhite = img.min(axis=2) < 235
    for y0, y1 in blocks(nonwhite.sum(axis=1)):
        if y1 - y0 <= max_height and neutral_share(img[y0:y1][nonwhite[y0:y1]]) > 0.9:
            img[max(0, y0 - 2):y1 + 2] = 255


def components(mask):
    """8-connected components of [mask]: a label map, and each one's size."""
    h, w = mask.shape
    lab = np.zeros((h, w), np.int32)
    sizes = [0]
    for y in range(h):
        for x in range(w):
            if mask[y, x] and not lab[y, x]:
                cur = len(sizes)
                lab[y, x] = cur
                q, n = deque([(y, x)]), 0
                while q:
                    cy, cx = q.popleft()
                    n += 1
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            ny, nx = cy + dy, cx + dx
                            if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not lab[ny, nx]:
                                lab[ny, nx] = cur
                                q.append((ny, nx))
                sizes.append(n)
    return lab, sizes


def shrink(mask, scale=4):
    h, w = mask.shape
    return np.array(Image.fromarray(mask.astype(np.uint8) * 255).resize((w // scale, h // scale), Image.BOX)) > 40


def grow(lab, full_size):
    """A label map shrunk by shrink(), back at full size, grown a few pixels
    so the thin outline the shrinking lost is labelled too."""
    out = Image.fromarray(lab.astype(np.uint8)).resize(full_size, Image.NEAREST)
    for _ in range(3):
        grown = out.filter(ImageFilter.MaxFilter(5))
        out = Image.fromarray(np.where(np.array(out) == 0, np.array(grown), np.array(out)).astype(np.uint8))
    return np.array(out)


def find_frames(img, n, scale=4):
    """The n drawings on the sheet, each as (y0, x0, y1, x1, mask), in
    reading order. Found on a copy shrunk by [scale], where a sparkle stays
    apart from its boar."""
    nonwhite = img.min(axis=2) < 235
    lab, sizes = components(shrink(nonwhite, scale))
    big = sorted(range(1, len(sizes)), key=lambda i: sizes[i], reverse=True)[:n]
    boxes = {}
    for i in range(1, len(sizes)):
        ys, xs = np.nonzero(lab == i)
        boxes[i] = (ys.min(), xs.min(), ys.max() + 1, xs.max() + 1)
    owner = np.zeros(len(sizes), np.int32)
    for k, i in enumerate(big, 1):
        owner[i] = k
    full = (img.shape[1], img.shape[0])
    for i in range(1, len(sizes)):
        if owner[i]:
            continue
        y0, x0, y1, x1 = boxes[i]
        piece = np.kron(lab[y0:y1, x0:x1] == i, np.ones((scale, scale), bool))
        region = (slice(y0 * scale, y1 * scale), slice(x0 * scale, x1 * scale))
        if neutral_share(img[region][piece & nonwhite[region]]) > 0.9:
            continue  # a label beside the art
        cy, cx = (y0 + y1) / 2, (x0 + x1) / 2

        def dist(b):
            by0, bx0, by1, bx1 = boxes[b]
            return max(by0 - cy, 0, cy - by1) + max(bx0 - cx, 0, cx - bx1)

        owner[i] = big.index(min(big, key=dist)) + 1
    who = grow(owner[lab], full)
    frames = []
    for k in range(1, n + 1):
        m = (who == k) & nonwhite
        ys, xs = np.nonzero(m)
        frames.append((ys.min(), xs.min(), ys.max() + 1, xs.max() + 1, m))
    # Reading order: into rows by where they sit, then left to right.
    frames.sort(key=lambda f: (f[0] + f[2]) / 2)
    height = np.median([f[2] - f[0] for f in frames])
    rows, row = [], [frames[0]]
    for f in frames[1:]:
        if (f[0] + f[2]) / 2 - (row[-1][0] + row[-1][2]) / 2 > height / 2:
            rows.append(row)
            row = []
        row.append(f)
    rows.append(row)
    return [f for r in rows for f in sorted(r, key=lambda f: f[1])]


def cut(img, frame, pad=12):
    """The frame on white: its box with a margin, everything not its own
    painted out (a neighbour's wing tip reaching into the box), and any
    label letters that came with it. The piglet's "FRAME 1" sits close
    enough to a wing tip to join it on the shrunk copy; at full size each
    letter is a shape of its own, all grey, where everything of the boar's
    (tusks, outline) joins the boar."""
    y0, x0, y1, x1, m = frame
    h, w = m.shape
    y0, x0, y1, x1 = max(0, y0 - pad), max(0, x0 - pad), min(h, y1 + pad), min(w, x1 + pad)
    out = img[y0:y1, x0:x1].copy()
    out[~m[y0:y1, x0:x1]] = 255
    nonwhite = out.min(axis=2) < 235
    lab, sizes = components(nonwhite)
    biggest = max(sizes)
    for i, n in enumerate(sizes):
        if i and n < biggest * 0.02 and neutral_share(out[lab == i]) > 0.9:
            out[lab == i] = 255
    return out


def knock_out(a, holes=False, min_hole=30, warm_share=0.005):
    """RGBA with the background flood-filled out from the edges, and the
    enclosed patches of it at least [min_hole] pixels that are background
    too: with [holes] all of them; without, the big ones edged with warm
    colour (fur, dust), which are sky showing through. The piglet's dash
    has a gap between its belly and the dust it kicks up, about 2% of the
    boar, half its rim warm; every pocket of white in its feathers is edged
    in lavender (at most 8% of the rim warm). Size tells it from a
    highlight against fur, such as the one on the snout (0.04%, which the
    first version of this rule punched out): the gap must be at least
    [warm_share] of the boar, a share rather than pixels because a
    close-up is knocked out at full size."""
    h, w, _ = a.shape
    ai = a.astype(int)
    bgish = (ai.min(axis=2) > 226) & ((ai.max(axis=2) - ai.min(axis=2)) < 24)
    bg = np.zeros((h, w), bool)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if bgish[y, x] and not bg[y, x]:
                bg[y, x] = True
                q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if bgish[y, x] and not bg[y, x]:
                bg[y, x] = True
                q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and bgish[ny, nx] and not bg[ny, nx]:
                bg[ny, nx] = True
                q.append((ny, nx))
    lab, sizes = components(bgish & ~bg)
    opaque = ~bg
    boar = opaque.sum()
    for i, n in enumerate(sizes):
        if not i or n < min_hole or (not holes and n < warm_share * boar):
            continue
        m = lab == i
        if not holes:
            rim = np.zeros_like(m)
            rim[1:] |= m[:-1]
            rim[:-1] |= m[1:]
            rim[:, 1:] |= m[:, :-1]
            rim[:, :-1] |= m[:, 1:]
            rim &= ~m & opaque
            px = ai[rim]
            if not len(px) or ((px[:, 0] - px[:, 2]) > 20).mean() < 0.25:
                continue
        bg |= m
    # The JPEG fringe: light pixels touching the background, twice over.
    for _ in range(2):
        edge = np.zeros_like(bg)
        edge[1:] |= bg[:-1]
        edge[:-1] |= bg[1:]
        edge[:, 1:] |= bg[:, :-1]
        edge[:, :-1] |= bg[:, 1:]
        bg |= edge & ~bg & (ai.min(axis=2) > 185)
    return np.dstack([a, np.where(bg, 0, 255).astype(np.uint8)])


def lower_centroid(rgba):
    """The centroid of the lower half of the art: a first guess at where the
    body is."""
    m = rgba[:, :, 3] > 0
    ys, xs = np.nonzero(m)
    m[: (ys.min() + ys.max()) // 2] = False
    ys, xs = np.nonzero(m)
    return xs.mean(), ys.mean()


def head_match(ref, img, reach):
    """How well, and with what shift, [img]'s head lines up with [ref]'s:
    the offset within [reach] where [img] best matches the head region of
    [ref] (the front 45% and lower 60% of its art; the sheets face left) in
    colour and outline. Returns (cost, dx, dy)."""
    rf, im = ref.astype(float), img.astype(float)
    ys, xs = np.nonzero(ref[:, :, 3] > 0)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    hy0, hx1 = int(y0 + (y1 - y0) * 0.40), int(x0 + (x1 - x0) * 0.45)
    R = rf[hy0:y1, x0:hx1]
    ra = R[:, :, 3] > 0
    H, W = im.shape[:2]

    def cost(dx, dy):
        ya, xa = hy0 - dy, x0 - dx
        if ya < 0 or xa < 0 or ya + R.shape[0] > H or xa + R.shape[1] > W:
            return float("inf")
        C = im[ya:ya + R.shape[0], xa:xa + R.shape[1]]
        ca = C[:, :, 3] > 0
        both = ra & ca
        colour = np.abs(R[:, :, :3] - C[:, :, :3]).mean(axis=2)[both].mean() if both.any() else 255.0
        return colour + 200 * (ra ^ ca).mean()

    c, bx, by = min((cost(dx, dy), dx, dy) for dx in range(-reach, reach + 1, 4) for dy in range(-reach, reach + 1, 4))
    return min((cost(dx, dy), dx, dy) for dx in range(bx - 4, bx + 5) for dy in range(by - 4, by + 5))


def scaled(cell, s):
    if s == 1.0:
        return cell
    h, w = cell.shape[:2]
    return np.array(Image.fromarray(cell, "RGBA").resize((round(w * s), round(h * s)), Image.LANCZOS))


def register_to(ref, cells, names, prefix, scale=None, floor=None):
    """Registers each frame to [ref], an already registered frame of the
    same boar (its wingbeat's first), and writes it on [ref]'s canvas: the
    pose sheets, drawn apart from the wingbeat, whose poses must sit exactly
    where the flying boar does or it jumps each time one shows. A separate
    sheet may be drawn at another size, so the frames are also scaled to
    match the head: each is tried at a few sizes and both ways round, the
    best refined, and then all are drawn at the median of their best sizes,
    since a sheet is drawn at one size (alone, one frame of a test sheet
    shrunk to 85% came out 2% off). The sizes tried are round a first
    estimate from how much art there is, so a pose drawn much bigger (the
    piglet's hurt came as a close-up four times the wingbeat's size) is
    found too.

    [scale] skips the size search, for a pose the head match cannot size:
    the piglet's landing, head drooped and turned, came out 18% too big.
    The owner's close-ups are drawn at one zoom, so the size found for
    another pose of the same set is the one to give. [floor] is a frame
    whose lowest row the drawing's lowest row is set on, for a pose on the
    ground (landing, standing): the game stands that frame's hoof line on
    the ground, so the pose is placed by it, not by a head that droops."""
    ch, cw = ref.shape[:2]
    rx, ry = lower_centroid(ref)
    reach = max(ch, cw) // 10

    def place(c, x, y):
        canvas = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
        canvas.paste(Image.fromarray(c, "RGBA"), (x, y))
        return np.array(canvas)

    def fit(c):
        h, w = c.shape[:2]
        bx, by = (cw - w) // 2, (ch - h) // 2
        cx, cy = lower_centroid(place(c, bx, by))
        gx, gy = bx + round(rx - cx), by + round(ry - cy)
        cost, hx, hy = head_match(ref, place(c, gx, gy), reach)
        return cost, gx + hx, gy + hy

    area = (ref[:, :, 3] > 0).sum()
    guess = float(np.median([np.sqrt(area / (c[:, :, 3] > 0).sum()) for c in cells]))
    best = []
    for cell in cells:
        if scale:
            costs = [(fit(scaled(cell[:, ::-1].copy() if f else cell, scale))[0], f) for f in (False, True)]
            best.append((min(costs)[1], scale))
            continue
        tries = []
        for flip in (False, True):
            base = cell[:, ::-1].copy() if flip else cell
            for s in (guess * k for k in (0.8, 0.9, 1.0, 1.1, 1.2)):
                tries.append((*fit(scaled(base, s)), flip, s))
        _, _, _, flip, s0 = min(tries, key=lambda t: t[0])
        base = cell[:, ::-1].copy() if flip else cell
        for s in (s0 * k for k in (0.95, 0.975, 1.025, 1.05)):
            tries.append((*fit(scaled(base, s)), flip, s))
        best.append(min(tries, key=lambda t: t[0])[3:])
    s = scale or round(float(np.median([b[1] for b in best])), 4)
    ground = np.nonzero((floor[:, :, 3] > 0).any(axis=1))[0].max() if floor is not None else None

    for name, cell, (flip, _) in zip(names, cells, best):
        c = scaled(cell[:, ::-1].copy() if flip else cell, s)
        _, x, y = fit(c)
        if ground is not None:
            y = ground - np.nonzero((c[:, :, 3] > 0).any(axis=1))[0].max()
        out = place(c, x, y)
        path = f"{prefix}_{name}.png"
        Image.fromarray(out, "RGBA").save(path)
        clipped = (c[:, :, 3] > 0).sum() - (out[:, :, 3] > 0).sum()
        note = (", turned round" if flip else "") + (f", {clipped} px CUT OFF by the canvas" if clipped > 0 else "")
        print(f"{name}: scaled {s:.3f}, at {x:+d},{y:+d}{note} -> {path}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sheet")
    ap.add_argument("prefix")
    ap.add_argument("--frames", type=int, default=4)
    ap.add_argument("--holes", action="store_true")
    ap.add_argument("--ref", help="register to this frame (a wingbeat's first) instead of the sheet's own first")
    ap.add_argument("--names", help="comma-separated names for the frames, in reading order, instead of 1..N")
    ap.add_argument("--scale", type=float, help="with --ref: this size, not one searched for")
    ap.add_argument("--floor", help="with --ref: set each frame's lowest row on this frame's (a pose on the ground)")
    args = ap.parse_args()
    img = np.array(Image.open(args.sheet).convert("RGB"))
    erase_label_rows(img)
    cells = [knock_out(cut(img, f), holes=args.holes) for f in find_frames(img, args.frames)]
    prefix = args.prefix
    names = args.names.split(",") if args.names else [str(i) for i in range(1, len(cells) + 1)]
    if len(names) != len(cells):
        sys.exit(f"{len(names)} names for {len(cells)} frames")
    os.makedirs(os.path.dirname(prefix) or ".", exist_ok=True)
    if args.ref:
        floor = np.array(Image.open(args.floor).convert("RGBA")) if args.floor else None
        register_to(np.array(Image.open(args.ref).convert("RGBA")), cells, names, prefix, args.scale, floor)
        return

    M = max(max(c.shape[:2]) for c in cells) // 3  # room round each frame for the shifts
    reach = M // 2
    ch = max(c.shape[0] for c in cells) + 2 * M
    cw = max(c.shape[1] for c in cells) + 2 * M

    def place(cell, dx, dy):
        canvas = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
        canvas.alpha_composite(Image.fromarray(cell, "RGBA"), (M + dx, M + dy))
        return np.array(canvas)

    ref = place(cells[0], 0, 0)
    rx, ry = lower_centroid(ref)
    for i, (name, cell) in enumerate(zip(names, cells), 1):
        dx = dy = 0
        turned = False
        if i > 1:
            tries = []
            for flip in (False, True):
                c = cell[:, ::-1].copy() if flip else cell
                cx, cy = lower_centroid(place(c, 0, 0))
                gx, gy = round(rx - cx), round(ry - cy)
                cost, hx, hy = head_match(ref, place(c, gx, gy), reach)
                tries.append((cost, flip, gx + hx, gy + hy, c))
            cost, turned, dx, dy, cell = min(tries, key=lambda t: t[0])
        path = f"{prefix}_{name}.png"
        Image.fromarray(place(cell, dx, dy), "RGBA").save(path)
        note = ", turned round" if turned else ""
        print(f"frame {name}: shifted {dx:+d},{dy:+d}{note} -> {path}")


if __name__ == "__main__":
    main()
