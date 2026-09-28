"""Splits a 2x2 sheet of hand-drawn animation frames into registered,
transparent frames, ready for import_boars.py.

    python tool/art/split_frames.py sheet.jpg tool/art/source/boar_piglet_cycle

writes boar_piglet_cycle_1.png .. _4.png (reading order: top-left, top-right,
bottom-left, bottom-right).

The owner's sheets are drawn on white, with a "FRAME n" label above each
frame, and saved as JPEG. For each frame this:

  1. cuts the cell out of the 2x2 grid (split at the blank gutters);
  2. erases the label: its letters are neutral grey-black, where the art's
     darkest outlines are tinted (purple-brown), so it goes by colour, and
     only in the band above the art;
  3. makes the white background transparent by flood-filling from the cell's
     edges through near-white (so white inside the art, such as the wings,
     is untouched), then trims the light JPEG fringe off the outline;
  4. registers the frames on the body: the part below the wings is the same
     drawing in every frame, so each frame is shifted to line its body up
     with the first. Without it the whole pig jitters as the frames cycle.

All four come out on one canvas size, so the importer can crop them alike.
"""
import os
import sys
from collections import deque

import numpy as np
from PIL import Image


def gutters(profile, min_len):
    """Runs of (nearly) empty rows or columns, as (start, end)."""
    out, start = [], None
    for i, v in enumerate(profile):
        if v <= 2 and start is None:
            start = i
        if v > 2 and start is not None:
            if i - start >= min_len:
                out.append((start, i))
            start = None
    if start is not None and len(profile) - start >= min_len:
        out.append((start, len(profile)))
    return out


def split_points(profile, n_cells):
    """Where to cut: the middle of the widest interior gutters."""
    gs = [g for g in gutters(profile, 6) if g[0] > 0 and g[1] < len(profile)]
    gs.sort(key=lambda g: g[1] - g[0], reverse=True)
    cuts = sorted((a + b) // 2 for a, b in gs[: n_cells - 1])
    return [0] + cuts + [len(profile)]


def erase_label(a, band=70):
    """Erases the label above the art.

    Its letters are neutral grey-black (the art's darkest outlines are
    tinted), so their dark cores find the label's box; within that box only,
    neutral pixels up to light grey are painted white. Keeping to the box
    matters: the first version cleared every neutral pixel in the band, and
    took the pale grey tip off a wing that reaches up beside the label."""
    top = a[:band].astype(int)
    mx, mn = top.max(axis=2), top.min(axis=2)
    neutral = (mx - mn) < 22
    cores = neutral & (mx < 130)
    ys, xs = np.nonzero(cores)
    if len(xs) == 0:
        return a
    y0, y1 = max(0, ys.min() - 4), min(band, ys.max() + 5)
    x0, x1 = max(0, xs.min() - 4), min(top.shape[1], xs.max() + 5)
    box = np.zeros_like(neutral)
    box[y0:y1, x0:x1] = True
    top[box & neutral & (mx < 215)] = 255
    a[:band] = top.astype(np.uint8)
    return a


def knock_out(a):
    """RGBA with the background flood-filled out from the edges."""
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
    # The JPEG fringe: light pixels touching the background, twice over.
    for _ in range(2):
        edge = np.zeros_like(bg)
        edge[1:] |= bg[:-1]
        edge[:-1] |= bg[1:]
        edge[:, 1:] |= bg[:, :-1]
        edge[:, :-1] |= bg[:, 1:]
        fringe = edge & ~bg & (ai.min(axis=2) > 185)
        bg |= fringe
    out = np.dstack([a, np.where(bg, 0, 255).astype(np.uint8)])
    return out


def body_anchor(rgba, below):
    """Where the body is: the centroid of the opaque pixels below row
    `below` (under the wings), and the lowest opaque row."""
    m = rgba[:, :, 3] > 0
    m[:below] = False
    ys, xs = np.nonzero(m)
    return xs.mean(), ys.mean(), ys.max()


def main():
    src, prefix = sys.argv[1], sys.argv[2]
    img = np.array(Image.open(src).convert("RGB"))
    nonwhite = img.min(axis=2) < 235
    xs = split_points(nonwhite.sum(axis=0), 2)
    ys = split_points(nonwhite.sum(axis=1), 2)
    cells = []
    for r in range(2):
        for c in range(2):
            cell = img[ys[r]:ys[r + 1], xs[c]:xs[c + 1]].copy()
            cells.append(knock_out(erase_label(cell)))

    # Register on the body. The wings never reach below ~45% of the cell.
    below = int(min(c.shape[0] for c in cells) * 0.45)
    anchors = [body_anchor(c, below) for c in cells]
    ax0, ay0, _ = anchors[0]
    shifts = [(round(ax0 - ax), round(ay0 - ay)) for ax, ay, _ in anchors]
    ch = max(c.shape[0] for c in cells) + 40
    cw = max(c.shape[1] for c in cells) + 40
    os.makedirs(os.path.dirname(prefix) or ".", exist_ok=True)
    for i, (cell, (dx, dy)) in enumerate(zip(cells, shifts), 1):
        canvas = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
        canvas.alpha_composite(Image.fromarray(cell, "RGBA"), (20 + dx, 20 + dy))
        path = f"{prefix}_{i}.png"
        canvas.save(path)
        print(f"frame {i}: shifted {dx:+d},{dy:+d} -> {path}")


if __name__ == "__main__":
    main()
