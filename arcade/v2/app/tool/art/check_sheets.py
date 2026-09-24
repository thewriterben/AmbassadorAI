"""Checks When Pigs Fly boar sheets against the sheet contract in
lib/arcade/passage/boar.dart, and suggests the three placement numbers per
stage (anchorU, anchorV, footV) from the art itself.

    python tool/art/check_sheets.py            # checks assets/images/boar_*.png
    python tool/art/check_sheets.py path/to/delivery/

Run it on final art before dropping it in. It exits non-zero on anything
that would make the game refuse a sheet (and draw the fallback coin) or draw
it wrong; everything else is a warning with the numbers to paste.
"""
import os
import re
import sys

from PIL import Image

FRAMES = 8
STAND, FLY_MID = 7, 1
STAGES = ["piglet", "juvenile", "razorback"]
HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.normpath(os.path.join(HERE, "..", ".."))
BOAR_DART = os.path.join(APP, "lib", "arcade", "passage", "boar.dart")


def current_specs():
    """The numbers boar.dart has now, per stage."""
    src = open(BOAR_DART, encoding="utf-8").read()
    out = {}
    for stage in STAGES:
        m = re.search(r"BoarStage\.%s: BoarSpec\((.*?)\)," % stage, src, re.S)
        if not m:
            continue
        body = m.group(1)
        out[stage] = {k: float(v) for k, v in re.findall(r"(anchorU|anchorV|footV|sizeInRadii): ([0-9.]+)", body)}
    return out


def _centroid(frame):
    a = frame.getchannel("A")
    w, h = frame.size
    px = a.load()
    sx = sy = n = 0
    for y in range(h):
        for x in range(w):
            if px[x, y] > 32:
                sx += x
                sy += y
                n += 1
    return (sx / n, sy / n) if n else (w / 2, h / 2)


def alpha_bbox(frame):
    return frame.getchannel("A").point(lambda a: 255 if a > 32 else 0).getbbox()


def check(path, stage, spec):
    errors, warns = [], []
    im = Image.open(path)
    if im.mode != "RGBA":
        errors.append(f"mode is {im.mode}, needs RGBA with a transparent background")
        im = im.convert("RGBA")
    w, h = im.size
    if w != h * FRAMES:
        errors.append(f"{w}x{h}: must be one row of {FRAMES} square frames ({h * FRAMES}x{h})")
        return errors, warns, None
    if h < 96:
        warns.append(f"frames are {h}px; export at an integer scale to at least 96px so rotation stays crisp")
    frames = [im.crop((i * h, 0, (i + 1) * h, h)) for i in range(FRAMES)]
    for i, f in enumerate(frames):
        bb = alpha_bbox(f)
        if bb is None:
            errors.append(f"frame {i} is empty")
            continue
        if bb[0] == 0 or bb[1] == 0 or bb[2] == h or bb[3] == h:
            warns.append(f"frame {i} touches the frame edge {bb}: part of it may be cut off")
    if im.getpixel((0, 0))[3] != 0:
        warns.append("top-left pixel is not transparent: is the background knocked out?")

    stand = alpha_bbox(frames[STAND])
    mid = alpha_bbox(frames[FLY_MID])
    suggest = None
    if stand and mid:
        foot = stand[3] / h
        # The hitbox centre: the centre of mass of the standing frame (wings
        # folded), which the body and head dominate — a bounding box is
        # dragged backwards by the tail. Legs pull the mass down, so the
        # vertical is taken from the mid-flight frame, legs tucked.
        au = _centroid(frames[STAND])[0] / h
        av = _centroid(frames[FLY_MID])[1] / h
        suggest = {"anchorU": round(au, 3), "anchorV": round(av, 3), "footV": round(foot, 3)}
        # Only the hoof line is exact. Where the hitbox centre belongs — the
        # middle of body-and-head — is a judgement no measurement makes: a
        # bounding box is dragged back by the tail, a centre of mass by the
        # mane and wings (on the placeholders it lands 0.03-0.05 behind the
        # hand-set numbers). So the anchors are printed as a starting point
        # to confirm on a phone with the DEV stage switch, not warned about.
        if spec and "footV" in spec and abs(spec["footV"] - suggest["footV"]) > 0.01:
            warns.append(f"footV in boar.dart is {spec['footV']}, the hooves are at {suggest['footV']}")
    return errors, warns, suggest


def main():
    folder = sys.argv[1] if len(sys.argv) > 1 else os.path.join(APP, "assets", "images")
    specs = current_specs()
    failed = False
    for stage in STAGES:
        path = os.path.join(folder, f"boar_{stage}.png")
        print(f"\n{stage}: {path}")
        if not os.path.exists(path):
            print("  ERROR missing")
            failed = True
            continue
        errors, warns, suggest = check(path, stage, specs.get(stage))
        for e in errors:
            print("  ERROR", e)
        for w in warns:
            print("  warn ", w)
        if suggest:
            now = specs.get(stage) or {}
            print(f"  footV: {suggest['footV']} (now {now.get('footV')})")
            print(f"  centre of mass, a starting point for anchorU/anchorV: {suggest['anchorU']}, {suggest['anchorV']}"
                  f" (now {now.get('anchorU')}, {now.get('anchorV')})")
        if not errors:
            print("  ok" if not warns else "  ok, with warnings")
        failed |= bool(errors)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
