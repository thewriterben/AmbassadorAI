"""Placeholder pixel-art sheets for When Pigs Fly: three boar stages.

Each sheet is one row of eight square frames, facing right:
  0-3  wing cycle (up, mid, down, recovery)
  4    hurt
  5    dash
  6    landing (wings braking, legs down)
  7    standing (wings folded)
Authored at 1x (32 / 48 / 72 px frames) and exported at 4x nearest-neighbour
so the game can sample it smoothly while rotating without losing the pixels.

The look is built from shaded primitives: every part carries a colour ramp
and a pseudo-3D intensity, quantised with a 4x4 ordered dither, then given a
selective dark outline and internal contact lines. Placeholder art — the
sheet layout is the contract, so final art drops in over these files.
"""
import math
import sys
import numpy as np
from PIL import Image

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
PREVIEW = sys.argv[2] if len(sys.argv) > 2 else None
EXPORT = 4

BAYER = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]) / 16.0
_l = np.array([-0.55, -0.75, 0.62])
LIGHT = _l / np.linalg.norm(_l)


def hx(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def ramp(*hs):
    return [hx(h) for h in hs]


# ------------------------------------------------------------------ palettes
R = {
    # piglet: golden-blond with cream humbug stripes, pink snout
    "p_fur": ramp("#3b2410", "#6d4a1f", "#9a6d2e", "#c49448", "#e6bc68", "#fbe29c"),
    "p_stripe": ramp("#e8d3a0", "#f8ecc8", "#fffbe8"),
    "p_snout": ramp("#4d2622", "#8c4c42", "#c47e6c", "#e8ab96", "#f8d0c0"),
    "p_wing": ramp("#5a3020", "#94583a", "#c8845a", "#eeb088", "#ffd8b8"),
    "p_bone": ramp("#4a2c12", "#8c5a24", "#c89040", "#f0c878"),
    # juvenile: bristly brown shifting to gold
    "j_fur": ramp("#26170c", "#4f321a", "#7d5428", "#a8783a", "#cfa050", "#ecc878"),
    "j_ridge": ramp("#1c1008", "#3e2612", "#6a4420", "#946430", "#c08c44"),
    "j_snout": ramp("#3a1e18", "#6e3c32", "#a0645a", "#c8907e", "#e2b4a0"),
    "j_wing": ramp("#2a1008", "#4e2012", "#7a341c", "#a44e28", "#c87040"),
    "j_bone": ramp("#3a2410", "#6e4a1e", "#a8782e", "#dcae50"),
    # razorback: glorious gold, amber crest and cape, bronze dragon wings
    "r_fur": ramp("#3a2206", "#6e420e", "#a46a14", "#d89c22", "#f5c843", "#fff0a0"),
    "r_cape": ramp("#260c02", "#521e04", "#86360a", "#b85812", "#e0801c", "#f8b040"),
    "r_crest": ramp("#2a1002", "#5c2806", "#94460c", "#cc7416", "#f4a82c", "#ffe08a"),
    "r_snout": ramp("#3a1a10", "#6a3622", "#9c5a3a", "#c4845c", "#e0aa80"),
    "r_wing": ramp("#2a0c06", "#541a0c", "#842c12", "#b0441a", "#d8642a", "#f08a40"),
    "r_bone": ramp("#3c2406", "#76480e", "#b47a18", "#e8b030", "#fce078"),
    "r_scar": ramp("#c89a78", "#ecc8a4", "#fce6cc"),
    # shared
    "tusk": ramp("#6a5c44", "#b0a282", "#e8e0c6", "#fffcf0"),
    "hoof": ramp("#140a04", "#2e1c0e", "#4e3420"),
    "claw": ramp("#8a7a5c", "#e8e0c6"),
    "inner_ear": ramp("#3a1a14", "#7a3a30", "#b06858"),
}
DARK = (18, 9, 3)
EYE = (20, 12, 6)
GLINT = (255, 250, 236)
SLOT = (22, 12, 3)
SLOT_LIP = (255, 232, 150)


class Canvas:
    def __init__(self, S, g=None):
        self.S = S
        self.g = g or S  # geometry scale: the pig is drawn at g, the frame is S
        self.layer = np.full((S, S), -1, dtype=int)
        self.t = np.zeros((S, S))
        self.meta = []

    def _new(self, rmp, group, decal, dither, outline=True):
        self.meta.append(dict(ramp=rmp, group=group, decal=decal, dither=dither, outline=outline))
        return len(self.meta) - 1

    def fill(self, mask, inten, rmp, group, decal=False, dither=0.32, bbox=None, outline=True):
        lid = self._new(rmp, group, decal, dither, outline)
        x0, y0, x1, y1 = bbox or (0, 0, self.S, self.S)
        x0, y0 = max(0, int(math.floor(x0)) - 1), max(0, int(math.floor(y0)) - 1)
        x1, y1 = min(self.S, int(math.ceil(x1)) + 1), min(self.S, int(math.ceil(y1)) + 1)
        for y in range(y0, y1):
            for x in range(x0, x1):
                px, py = x + 0.5, y + 0.5
                if mask(px, py):
                    self.layer[y, x] = lid
                    self.t[y, x] = inten(px, py)
        return lid

    def decal(self, pts, rmp, bias, group="decal", absolute=None):
        """Recolour existing pixels, keeping the shading underneath."""
        lid = self._new(rmp, group, True, 0.25)
        for x, y in pts:
            x, y = int(x), int(y)
            if 0 <= x < self.S and 0 <= y < self.S and self.layer[y, x] >= 0:
                base = self.t[y, x] if absolute is None else absolute
                self.layer[y, x] = lid
                self.t[y, x] = min(1.0, max(0.0, base + bias))

    def dot(self, x, y, rgb):
        lid = self._new([rgb], "decal", True, 0)
        x, y = int(x), int(y)
        if 0 <= x < self.S and 0 <= y < self.S:
            self.layer[y, x] = lid
            self.t[y, x] = 0.5

    # --------------------------------------------------------------- shapes
    def ellipse(self, cx, cy, rx, ry, rmp, group, bias=0.0, fur=None, dark=1.0, **kw):
        def mask(x, y):
            return ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1

        def inten(x, y):
            nx, ny = (x - cx) / rx, (y - cy) / ry
            nz = math.sqrt(max(0.0, 1 - nx * nx - ny * ny))
            i = max(0.0, nx * LIGHT[0] + ny * LIGHT[1] + nz * LIGHT[2])
            i = 0.12 + 0.88 * i + bias
            if fur:
                i += fur(int(x), int(y))
            return i * dark

        return self.fill(mask, inten, rmp, group, bbox=(cx - rx, cy - ry, cx + rx, cy + ry), **kw)

    def poly(self, pts, rmp, group, inten=None, **kw):
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]

        def mask(x, y):
            inside = False
            n = len(pts)
            for i in range(n):
                (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
                if (y1 > y) != (y2 > y):
                    xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                    if xi > x:
                        inside = not inside
            return inside

        return self.fill(mask, inten or (lambda x, y: 0.5), rmp, group, bbox=(min(xs), min(ys), max(xs), max(ys)), **kw)

    def seg(self, p0, p1, w0, w1, rmp, group, base=0.55, dark=1.0, **kw):
        (ax, ay), (bx, by) = p0, p1
        dx, dy = bx - ax, by - ay
        ll = dx * dx + dy * dy or 1e-9
        ln = math.sqrt(ll)
        nx, ny = -dy / ln, dx / ln  # unit normal
        # Which side of the limb faces the light, in screen space.
        lit = nx * LIGHT[0] + ny * LIGHT[1]

        def closest(x, y):
            t = max(0.0, min(1.0, ((x - ax) * dx + (y - ay) * dy) / ll))
            cx, cy = ax + t * dx, ay + t * dy
            return t, cx, cy

        def mask(x, y):
            t, cx, cy = closest(x, y)
            hw = max(0.55, (w0 + (w1 - w0) * t) / 2)
            return (x - cx) ** 2 + (y - cy) ** 2 <= hw * hw

        def inten(x, y):
            t, cx, cy = closest(x, y)
            hw = max(0.55, (w0 + (w1 - w0) * t) / 2)
            off = ((x - cx) * nx + (y - cy) * ny) / hw
            return (base + 0.35 * off * (1 if lit > 0 else -1)) * dark

        pad = max(w0, w1)
        return self.fill(mask, inten, rmp, group,
                         bbox=(min(ax, bx) - pad, min(ay, by) - pad, max(ax, bx) + pad, max(ay, by) + pad), **kw)

    def curve(self, pts, w0, w1, rmp, group, steps=10, **kw):
        """Quadratic bezier as a chain of tapered segments, one layer."""
        def at(t):
            (x0, y0), (x1, y1), (x2, y2) = pts
            u = 1 - t
            return (u * u * x0 + 2 * u * t * x1 + t * t * x2, u * u * y0 + 2 * u * t * y1 + t * t * y2)

        first = None
        for i in range(steps):
            t0, t1 = i / steps, (i + 1) / steps
            lid = self.seg(at(t0), at(t1), w0 + (w1 - w0) * t0, w0 + (w1 - w0) * t1, rmp, group, **kw)
            if first is None:
                first = lid
            else:
                # merge into the first layer so the curve has no seams
                self.layer[self.layer == lid] = first
        return first

    # --------------------------------------------------------------- output
    def render(self):
        S = self.S
        img = np.zeros((S, S, 4), dtype=np.uint8)
        L = self.layer
        for y in range(S):
            for x in range(S):
                lid = L[y, x]
                if lid < 0:
                    continue
                m = self.meta[lid]
                rmp = m["ramp"]
                n = len(rmp)
                if n == 1:
                    img[y, x] = (*rmp[0], 255)
                    continue
                v = min(1.0, max(0.0, self.t[y, x])) * (n - 1) + (BAYER[y % 4, x % 4] - 0.5) * m["dither"]
                idx = int(round(min(n - 1, max(0, v))))
                if not m["decal"]:
                    # Contact line: a back part darkens where a front part sits on it.
                    for ddx, ddy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        qx, qy = x + ddx, y + ddy
                        if 0 <= qx < S and 0 <= qy < S:
                            q = L[qy, qx]
                            if q > lid and not self.meta[q]["decal"] and self.meta[q]["group"] != m["group"]:
                                idx = max(0, idx - 2)
                                break
                img[y, x] = (*rmp[idx], 255)
        # Selective outline: each empty pixel touching the sprite takes a very
        # dark tint of the part it touches.
        out = img.copy()
        for y in range(S):
            for x in range(S):
                if L[y, x] >= 0:
                    continue
                best = -1
                for ddx, ddy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    qx, qy = x + ddx, y + ddy
                    if 0 <= qx < S and 0 <= qy < S and L[qy, qx] > best and self.meta[L[qy, qx]]["outline"]:
                        best = L[qy, qx]
                if best >= 0:
                    c0 = self.meta[best]["ramp"][0]
                    out[y, x] = (*(int(c0[i] * 0.45 + DARK[i] * 0.55) for i in range(3)), 255)
        return Image.fromarray(out, "RGBA")


def h32(x, y, s=0):
    v = (x * 374761393 + y * 668265263 + s * 2147483647) & 0xFFFFFFFF
    v = ((v ^ (v >> 13)) * 1274126177) & 0xFFFFFFFF
    return (v ^ (v >> 16)) / 0xFFFFFFFF


# ------------------------------------------------------------------ stages
# Everything in fractions of the frame; P() scales to pixels.
STAGES = {
    "piglet": dict(
        S=32, fur="p_fur", snout="p_snout", wingc="p_wing", bone="p_bone",
        body=[(0.44, 0.60, 0.25, 0.185)],
        head=(0.70, 0.54, 0.17, 0.165), snout_e=(0.865, 0.60, 0.065, 0.062), disc=(0.925, 0.60, 0.022, 0.05),
        ear_far=[(0.62, 0.45), (0.615, 0.35), (0.67, 0.43)], ear=[(0.655, 0.44), (0.68, 0.33), (0.735, 0.43)],
        eye=(0.76, 0.495), eye_kind="big",
        legs=dict(front=(0.60, 0.70), rear=(0.31, 0.70), far_dx=0.035, tuck=(-0.06, 0.10), stand_y=0.875, w=2.6, w_end=2.2),
        tail=[(0.20, 0.56), (0.13, 0.52), (0.155, 0.47)], tail_w=1.2,
        wing=dict(sh=(0.46, 0.45), arm=0.16, fingers=[0.27, 0.21], offs=[15, -45], hip=(-0.13, 0.04), arm_w=1.3),
        slot=(0.33, 0.46, 3),
    ),
    "juvenile": dict(
        S=48, fur="j_fur", snout="j_snout", wingc="j_wing", bone="j_bone",
        body=[(0.42, 0.60, 0.27, 0.17), (0.54, 0.555, 0.16, 0.145)],
        head=(0.725, 0.575, 0.13, 0.125), snout_e=(0.87, 0.625, 0.085, 0.058), disc=(0.945, 0.625, 0.018, 0.048),
        ear_far=[(0.63, 0.49), (0.615, 0.385), (0.67, 0.47)], ear=[(0.665, 0.48), (0.665, 0.37), (0.725, 0.465)],
        eye=(0.765, 0.535), eye_kind="mid",
        tusk=[(0.885, 0.67), (0.925, 0.655), (0.915, 0.60)], tusk_w=(1.6, 0.8),
        legs=dict(front=(0.61, 0.69), rear=(0.30, 0.70), far_dx=0.035, tuck=(-0.07, 0.11), stand_y=0.885, w=3.4, w_end=2.8),
        tail=[(0.16, 0.57), (0.10, 0.60), (0.08, 0.66)], tail_w=1.4,
        ridge=dict(start=(0.69, 0.46), end=(0.25, 0.465), h=(0.035, 0.06), n=11, rmp="j_ridge"),
        wing=dict(sh=(0.50, 0.44), arm=0.18, fingers=[0.30, 0.25, 0.18], offs=[15, -28, -70], hip=(-0.15, 0.05), arm_w=1.8),
        slot=(0.28, 0.46, 4),
    ),
    "razorback": dict(
        S=72, fur="r_fur", snout="r_snout", wingc="r_wing", bone="r_bone",
        body=[(0.33, 0.605, 0.165, 0.13), (0.44, 0.625, 0.20, 0.13), (0.55, 0.55, 0.19, 0.19)],
        head=(0.725, 0.605, 0.12, 0.11), snout_e=(0.855, 0.65, 0.095, 0.056), disc=(0.94, 0.65, 0.016, 0.045),
        ear_far=[(0.63, 0.51), (0.605, 0.42), (0.66, 0.49)], ear=[(0.665, 0.505), (0.645, 0.41), (0.71, 0.495)],
        eye=(0.755, 0.585), eye_kind="fierce",
        tusk=[(0.865, 0.695), (0.975, 0.66), (0.905, 0.555)], tusk_w=(2.6, 0.9),
        tusk2=[(0.83, 0.685), (0.87, 0.67), (0.865, 0.62)], tusk2_w=(1.6, 0.7),
        legs=dict(front=(0.60, 0.69), rear=(0.28, 0.69), far_dx=0.035, tuck=(-0.08, 0.12), stand_y=0.90, w=5.0, w_end=3.4),
        tail=[(0.16, 0.56), (0.10, 0.62), (0.085, 0.70)], tail_w=1.5, tail_tuft=True,
        crest=dict(start=(0.71, 0.49), end=(0.30, 0.46), h=(0.08, 0.19), n=9, rmp="r_crest", peak=0.62),
        cape=dict(root0=(0.68, 0.47), root1=(0.42, 0.42), n=11, fall=0.27, back=0.09, w=3.4),
        wedge=[(0.64, 0.53), (0.78, 0.575), (0.90, 0.61), (0.905, 0.685), (0.78, 0.705), (0.66, 0.70)],
        scars=[((0.26, 0.54), (0.34, 0.665)), ((0.30, 0.525), (0.385, 0.655)), ((0.705, 0.545), (0.79, 0.64))],
        wing=dict(sh=(0.50, 0.41), arm=0.24, fingers=[0.39, 0.35, 0.29, 0.21], offs=[15, -20, -55, -90],
                  hip=(-0.20, 0.06), arm_w=2.6),
        slot=(0.26, 0.47, 5),
    ),
}

# Wing pose per frame: (elevation deg from pointing-back, finger scale, spread scale)
POSES = [
    (72, 1.0, 1.0),    # 0 up
    (22, 1.0, 1.0),    # 1 mid
    (-58, 1.0, 0.9),   # 2 down
    (8, 0.78, 0.6),    # 3 recovery, fingers folding
    (40, 0.62, 0.45),  # 4 hurt, crumpled
    (-4, 1.05, 0.35),  # 5 dash, swept back
    (58, 1.0, 1.0),    # 6 landing, braking
    (26, 0.5, 0.45),   # 7 stand, folded
]


def draw_wing(c, st, P, pose, far):
    S = c.g
    w = st["wing"]
    elev, fscale, spread = pose
    sx, sy = P(*w["sh"])
    if far:
        sx, sy = sx - 0.03 * S, sy + 0.01 * S
    def along(ang, length, ox, oy):
        a = math.radians(ang)
        return (ox - math.cos(a) * length * S, oy - math.sin(a) * length * S)
    wx, wy = along(elev, w["arm"], sx, sy)
    tips = []
    for k, (fl, off) in enumerate(zip(w["fingers"], w["offs"])):
        tips.append(along(elev + off * spread, fl * fscale, wx, wy))
    hx_, hy_ = sx + w["hip"][0] * S, sy + w["hip"][1] * S
    # membrane: leading edge, tips with scallops pulled toward the wrist, then the body
    pts = [(sx, sy), (wx, wy)]
    for k, t in enumerate(tips):
        pts.append(t)
        nxt = tips[k + 1] if k + 1 < len(tips) else (hx_, hy_)
        mx, my = (t[0] + nxt[0]) / 2, (t[1] + nxt[1]) / 2
        pull = 0.30 if k + 1 < len(tips) else 0.18
        pts.append((mx + (wx - mx) * pull, my + (wy - my) * pull))
    pts.append((hx_, hy_))
    dark = 0.55 if far else 1.0
    span = max(1e-6, max(math.hypot(t[0] - wx, t[1] - wy) for t in tips))

    def mem(x, y):
        d = math.hypot(x - wx, y - wy) / span
        return (0.78 - 0.45 * d + 0.08 * (h32(int(x), int(y), 3) - 0.5)) * dark

    grp = "wingfar" if far else "wing"
    c.poly(pts, R[st["wingc"]], grp, inten=mem)
    # bones over the membrane, same group so they draw no contact line
    aw = w["arm_w"]
    c.seg((sx, sy), (wx, wy), aw * 1.2, aw, R[st["bone"]], grp, base=0.62, dark=dark)
    for t in tips:
        c.seg((wx, wy), t, max(0.9, aw * 0.6), 0.8, R[st["bone"]], grp, base=0.55, dark=dark)
    if not far:
        # wrist claw
        cx_, cy_ = along(elev - 90, 0.035, wx, wy)
        c.seg((wx, wy), (cx_, cy_ - 0.02 * S), 1.2, 0.7, R["claw"], "claw", base=0.7)


def draw_legs(c, st, P, frame, far):
    lg = st["legs"]
    S = c.g
    for key in ("rear", "front"):
        hx0, hy0 = lg[key]
        if far:
            hx0 += lg["far_dx"]
            hy0 -= 0.01
        if frame in (6, 7):
            ex, ey = hx0 + (0.02 if frame == 6 else 0.005), lg["stand_y"] - (0.01 if far else 0)
        elif frame == 5:
            ex, ey = hx0 + lg["tuck"][0] * 1.4, hy0 + lg["tuck"][1] * 0.6
        else:
            ex, ey = hx0 + lg["tuck"][0], hy0 + lg["tuck"][1]
        a, b = P(hx0, hy0), P(ex, ey)
        dark = 0.6 if far else 1.0
        c.seg(a, b, lg["w"], lg["w_end"], R[st["fur"]], "legfar" if far else "leg", base=0.5, dark=dark)
        # hoof: the last ~18% of the leg
        hxp = (a[0] + (b[0] - a[0]) * 0.8, a[1] + (b[1] - a[1]) * 0.8)
        c.seg(hxp, b, lg["w_end"], lg["w_end"] * 0.95, R["hoof"], "hoof", base=0.5, dark=dark)


def frame_box(st):
    """Frame side and where the pig's geometry sits in it. The frame is half
    as big again as the pig so the wings have room above and behind."""
    S = st["S"]
    F = S * 3 // 2
    return F, S // 6, S // 4


def frame(stage, fi):
    st = STAGES[stage]
    S = st["S"]
    F, ox, oy = frame_box(st)
    c = Canvas(F, S)
    P = lambda u, v: (u * S + ox, v * S + oy)
    pose = POSES[fi]
    fur = R[st["fur"]]

    # --- back to front
    draw_wing(c, st, P, pose, far=True)
    draw_legs(c, st, P, fi, far=True)

    tp = [P(*p) for p in st["tail"]]
    c.curve(tp, st["tail_w"] * 1.3, st["tail_w"], fur, "tail", base=0.55)
    if st.get("tail_tuft"):
        tx, ty = tp[2]
        c.ellipse(tx, ty + 1, 1.8, 2.8, R["r_crest"], "tail", bias=-0.1)

    if stage == "juvenile":
        bristle = lambda x, y: -0.22 if (h32(x, y) > 0.78 or h32(x, y - 1) > 0.86) else 0.0
    elif stage == "razorback":
        bristle = lambda x, y: -0.16 if h32(x // 1, y // 2) > 0.8 else 0.0
    else:
        bristle = None
    for (u, v, ru, rv) in st["body"]:
        cx, cy = P(u, v)
        c.ellipse(cx, cy, ru * S, rv * S, fur, "body", fur=bristle)

    # fur tufts / ridge silhouette along the back
    if stage == "piglet":
        for (u, v, hgt) in ((0.30, 0.435, 0.05), (0.38, 0.418, 0.06), (0.53, 0.42, 0.05)):
            x, y = P(u, v)
            c.poly([(x - 1.2, y + 1.5), (x + 0.3, y - hgt * S), (x + 1.4, y + 1.5)], fur, "body",
                   inten=lambda x_, y_: 0.9)
        # humbug stripes
        body = st["body"][0]
        bx, by = P(body[0], body[1])
        rx, ry = body[2] * S, body[3] * S
        pts = []
        for sv in (-0.35, 0.05, 0.45):
            for x in range(int(bx - rx * 0.85), int(bx + rx * 0.55)):
                y = by + sv * ry + math.sin(x * 0.55) * 0.5
                if ((x + 0.5 - bx) / rx) ** 2 + ((y - by) / ry) ** 2 < 0.8:
                    pts.append((x, y))
        c.decal(pts, R["p_stripe"], 0.0, absolute=0.5)

    if "ridge" in st:
        rd = st["ridge"]
        (u0, v0), (u1, v1) = rd["start"], rd["end"]
        for k in range(rd["n"]):
            f = k / (rd["n"] - 1)
            x, y = P(u0 + (u1 - u0) * f, v0 + (v1 - v0) * f)
            hgt = (rd["h"][0] + (rd["h"][1] - rd["h"][0]) * math.sin(f * math.pi)) * S * (0.75 + 0.5 * h32(k, 7))
            c.poly([(x - 1.6, y + 1.6), (x - 1.8, y - hgt), (x + 1.4, y + 1.6)], R[rd["rmp"]], "ridge",
                   inten=lambda x_, y_: 0.55)

    draw_legs(c, st, P, fi, far=False)

    # coin slot: the piggy bank's one tell
    su, sv, sl = st["slot"]
    sx, sy = P(su, sv)
    for i in range(sl):
        c.dot(sx + i, sy, SLOT)
        c.dot(sx + i, sy + 1, SLOT_LIP)
    c.dot(sx - 1, sy + 1, (200, 150, 60))
    c.dot(sx + sl, sy + 1, (200, 150, 60))

    if "cape" in st:
        # The mane: locks rooted along the nape and hump, falling back and
        # down over the shoulders. Tapered curves, so it reads as hair.
        cp = st["cape"]
        (u0, v0), (u1, v1) = cp["root0"], cp["root1"]
        for k in range(cp["n"]):
            f = k / (cp["n"] - 1)
            r = h32(k, 3, 9)
            rx, ry = u0 + (u1 - u0) * f, v0 + (v1 - v0) * f
            fall = cp["fall"] * (0.75 + 0.5 * r) * (1 - 0.35 * abs(f - 0.4))
            end = (rx - cp["back"] * (0.6 + 0.6 * h32(k, 5, 9)), ry + fall)
            ctrl = (rx + 0.02, ry + fall * 0.35)
            c.curve([P(rx, ry), P(*ctrl), P(*end)], cp["w"], 1.0, R["r_cape"], f"cape{k % 2}",
                    base=0.55 + 0.2 * (1 - f) + (0.12 if k % 2 else -0.08), steps=8)
    if "scars" in st:
        for (a, b) in st["scars"][:2]:
            _scar(c, P(*a), P(*b))

    if "crest" in st:
        _crest(c, st, P, back=True)

    # near wing sits over body and cape, under the head
    draw_wing(c, st, P, pose, far=False)

    # head
    c.poly([P(*p) for p in st["ear_far"]], fur, "earfar", inten=lambda x, y: 0.3)
    hx0, hy0, hrx, hry = st["head"]
    hcx, hcy = P(hx0, hy0)
    c.ellipse(hcx, hcy, hrx * S, hry * S, fur, "head", fur=bristle)
    if "wedge" in st:
        wp = [P(*p) for p in st["wedge"]]
        wt, wb = min(p[1] for p in wp), max(p[1] for p in wp)
        c.poly(wp, fur, "head", inten=lambda x, y: 0.82 - 0.55 * (y - wt) / (wb - wt))
    sx0, sy0, srx, sry = st["snout_e"]
    c.ellipse(*P(sx0, sy0), srx * S, sry * S, R[st["snout"]], "snout", bias=-0.05)
    dx0, dy0, drx, dry = st["disc"]
    c.ellipse(*P(dx0, dy0), drx * S, dry * S, R[st["snout"]], "disc", bias=0.2)
    dcx, dcy = P(dx0, dy0)
    c.dot(dcx, dcy - dry * S * 0.35, EYE)
    c.dot(dcx, dcy + dry * S * 0.35, EYE)
    ear = [P(*p) for p in st["ear"]]
    c.poly(ear, fur, "ear", inten=lambda x, y: 0.7)
    ex_ = [(ear[0][0] * 0.6 + ear[1][0] * 0.2 + ear[2][0] * 0.2, ear[0][1] * 0.45 + ear[1][1] * 0.3 + ear[2][1] * 0.25)]
    c.decal([(ex_[0][0], ex_[0][1]), (ex_[0][0], ex_[0][1] + 1)], R["inner_ear"], -0.2)
    if "tusk2" in st:
        c.curve([P(*p) for p in st["tusk2"]], *st["tusk2_w"], R["tusk"], "tusk", base=0.6, steps=6)
    if "tusk" in st:
        c.curve([P(*p) for p in st["tusk"]], *st["tusk_w"], R["tusk"], "tusk", base=0.62, steps=10)

    if "crest" in st:
        _crest(c, st, P, back=False)
    if stage == "piglet":
        # a blond tuft on the crown
        x, y = P(0.70, 0.40)
        for k, (dx, hgt) in enumerate(((-1.5, 2.5), (0, 3.5), (1.5, 2.2))):
            c.poly([(x + dx - 1, y + 1.2), (x + dx + 0.6, y - hgt), (x + dx + 1, y + 1.2)], fur, "head",
                   inten=lambda x_, y_: 0.95)

    # face
    ex, ey = P(*st["eye"])
    kind = st["eye_kind"]
    if fi == 4:
        c.dot(ex - 1, ey, EYE)
        c.dot(ex, ey, EYE)
        c.dot(ex + 1, ey - 1, EYE)
    elif kind == "big":
        for dx, dy in ((0, 0), (1, 0), (0, 1), (1, 1)):
            c.dot(ex + dx, ey + dy, EYE)
        c.dot(ex, ey, GLINT)
    elif kind == "mid":
        c.dot(ex, ey, EYE)
        c.dot(ex + 1, ey, EYE)
        c.dot(ex, ey + 1, EYE)
        c.dot(ex + 1, ey + 1, (60, 30, 12))
        c.dot(ex, ey, GLINT)
        c.decal([(ex - 1, ey - 1), (ex, ey - 1), (ex + 1, ey - 1)], R[st["fur"]], -0.45)
    else:
        c.dot(ex, ey, (226, 70, 24))
        c.dot(ex + 1, ey, (255, 150, 60))
        c.dot(ex, ey + 1, (120, 24, 8))
        c.dot(ex + 1, ey + 1, (180, 40, 12))
        for dx, dy in ((-2, -2), (-1, -2), (0, -1), (1, -1), (2, -1)):
            c.dot(ex + dx, ey + dy, EYE)
        # snarl
        mx, my = P(0.80, 0.69)
        for dx in range(4):
            c.dot(mx + dx, my - dx * 0.3, (40, 14, 6))
    if "scars" in st:
        _scar(c, P(*st["scars"][2][0]), P(*st["scars"][2][1]))
    return c.render()


def _crest(c, st, P, back):
    cr = st["crest"]
    (u0, v0), (u1, v1) = cr["start"], cr["end"]
    S = c.g
    for k in range(cr["n"]):
        f = k / (cr["n"] - 1)
        # the crown spikes go on after the head, the rest before the wing
        if (f < 0.18) == back:
            continue
        x, y = P(u0 + (u1 - u0) * f, v0 + (v1 - v0) * f)
        d = abs(f - (1 - cr["peak"])) / max(cr["peak"], 1 - cr["peak"])
        hgt = (cr["h"][1] - (cr["h"][1] - cr["h"][0]) * d) * S * (0.8 + 0.4 * h32(k, 11))
        rake = hgt * 0.45
        tip = (x - rake, y - hgt)
        # Each spine its own group, so neighbours get a contact line between them.
        c.poly([(x - 1.6, y + 2.5), tip, (x + 1.6, y + 2.5)], R[cr["rmp"]], f"crest{k % 2}",
               inten=lambda x_, y_, ty=tip[1], by=y: 0.3 + 0.7 * (by - y_) / max(1, by - ty))


def _scar(c, a, b):
    n = int(max(abs(b[0] - a[0]), abs(b[1] - a[1]))) + 1
    pts = [(a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n) for i in range(n + 1)]
    c.decal([(x, y + 1) for x, y in pts], R["r_fur"], -0.45)
    c.decal(pts, R["r_scar"], 0.0, absolute=0.55)


def main():
    import os
    os.makedirs(OUT, exist_ok=True)
    sheets = {}
    for stage, st in STAGES.items():
        S = st["S"]
        F = frame_box(st)[0]
        sheet = Image.new("RGBA", (F * len(POSES), F), (0, 0, 0, 0))
        for fi in range(len(POSES)):
            sheet.paste(frame(stage, fi), (fi * F, 0))
        sheets[stage] = sheet
        big = sheet.resize((sheet.width * EXPORT, sheet.height * EXPORT), Image.NEAREST)
        big.save(os.path.join(OUT, f"boar_{stage}.png"))
        print("wrote", stage, big.size)

    # home-screen card: the razorback mid-flight, trimmed and squared
    F = sheets["razorback"].height
    rb = sheets["razorback"].crop((0, 0, F, F))
    bbox = rb.getbbox()
    rb = rb.crop(bbox)
    side = max(rb.size) + 4
    sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    sq.paste(rb, ((side - rb.width) // 2, (side - rb.height) // 2))
    sq.resize((side * 4, side * 4), Image.NEAREST).save(os.path.join(OUT, "card_pigs.png"))

    if PREVIEW:
        scale = 5
        rows = []
        W = max(s.width for s in sheets.values()) * scale
        H = sum(s.height for s in sheets.values()) * scale + 20 * len(sheets)
        pv = Image.new("RGBA", (W, H), (14, 16, 20, 255))
        y = 0
        for stage, s in sheets.items():
            big = s.resize((s.width * scale, s.height * scale), Image.NEAREST)
            pv.alpha_composite(big, (0, y))
            y += big.height + 20
        pv.save(PREVIEW)
        print("preview", PREVIEW)


if __name__ == "__main__":
    main()
