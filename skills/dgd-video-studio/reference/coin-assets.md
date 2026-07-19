# Reference — The DGD Coin: assets, scale, and consistency

The single biggest visual-credibility failure in ambassador content is an **inconsistent
coin**. Every AI image generator will happily invent a plausible-looking gold coin, and
every one it invents is *wrong* — wrong face, wrong legend, wrong size, wrong number of
rings. A viewer who sees three different "DGD coins" across three videos concludes the
project is fake.

**The rule: the coin is never generated. It is always rendered from the reference asset —
still or moving.** AI generates the *scene*; the coin is dropped in.

---

## 1. Physical specification

The DGD physical coin is modelled on the **$20 Saint-Gaudens Double Eagle** — the
canonical American gold piece, chosen because it is the size a gold coin *should* feel
like in the hand.

| Property | Value |
|---|---|
| Diameter | **34.1 mm** (1.342 in) |
| Thickness | **2.41 mm** (0.095 in) |
| Weight | **33.436 g** |
| Edge | Lettered — `E PLURIBUS UNUM` with stars (see `sggp2.jpg`) |

Source: `Knowledge Base/Coin Ref/coinref.txt`.

For scale intuition: 34.1 mm is slightly **larger than a US half dollar** (30.6 mm) and
noticeably larger than a quarter (24.3 mm). It is a substantial coin — heavy, thick, and
it fills the middle of an adult palm. Any render where it reads like a dime or a poker
chip is wrong.

---

## 2. Asset inventory — `Knowledge Base/Coin Ref/`

| File | What it is | Use it for |
|---|---|---|
| `nbgdgd.png` | **1920×1905, transparent background.** The primary asset. | **Default for everything.** Compositing over any scene, b-roll, title cards, overlays. |
| `hqdgd.jpg` | 1200×1200, white background, high quality | Light backgrounds only, or when you need a flattened JPG. Prefer the PNG. |
| `sggp1.jpg` | Saint-Gaudens obverse + reverse, face-on | Size/heritage comparison shots; the "real gold coin" visual |
| `sggp2.jpg` | Saint-Gaudens **edge**, three angles | Thickness reference — the *only* good source for how thick the coin reads |
| `sggphandref.jpg` | 960×1280 — Saint-Gaudens held in a palm | Ground-truth scale reference |
| `dgdhandref.jpg` | 843×1124 — **DGD coin composited into that same photo** | **The gold-standard scale reference.** Match this. |

### Verified: the hand reference is correct

`dgdhandref.jpg` is the same source photograph as `sggphandref.jpg`, uniformly resized to
87.813%, with the coin swapped. Measured three independent ways — circular-edge
accumulator, difference-region bounding box, and radial profile — the composited DGD coin
is **1.004× the Saint-Gaudens diameter**. That is a match within measurement error.

**`dgdhandref.jpg` is therefore trustworthy as the canonical scale reference.** When in
doubt about how big the coin should read in a shot, compare against it.

---

## 3. Scale math for compositing

Measurements from the hand reference, normalised to its 960×1280 frame:

- coin rim diameter = **440 px**
- ⇒ **12.9 px per mm**
- ⇒ coin spans **45.8% of the frame width** in a held-in-palm shot

`nbgdgd.png` at native resolution is 1920 px across for a 34.1 mm coin ⇒ **56.3 px/mm**.
It has no transparent padding — the disc runs edge to edge (opaque fraction 0.783 against
a perfect inscribed circle's 0.785), so **the image width *is* the coin diameter.** Scaling
is a straight multiply, no padding compensation needed.

**One correction to apply:** the canvas is 1920×1905, so the asset is 0.8% wider than tall.
Resize to a square (e.g. `1920×1920`) when compositing, or the coin renders as a subtle
ellipse. On a title card at 1080 px this is an 8 px error — visible on a rim.

### Sizing recipe for a 1080×1920 vertical frame

| Shot | Coin width | Reads as |
|---|---|---|
| Held in hand / palm | ~495 px (45.8%) | true-to-life, matches `dgdhandref.jpg` |
| Hero / title card | 540–650 px (50–60%) | premium product shot |
| Corner accent / lower-third | 120–180 px | logo-mark, not a subject |
| Macro / detail | 900+ px, cropped | texture and depth, rings legible |

Never render it below ~100 px — the rings and legend turn to mush and it stops reading as
a coin at all.

---

## 4. Coin anatomy — what is actually on the face

Measured radially from centre, as a percentage of the coin's **radius**:

| Zone | Radius | Content |
|---|---|---|
| Core | 0–8% | The stylised **G** mark, brushed gold, raised |
| Ring 1 | 10–16% | Raised gold ring |
| Field | 18–32% | Recessed copper circuit-board field |
| Ring 2 | 34–40% | Raised gold ring |
| Field | 42–52% | Recessed circuit field |
| Ring 3 | 54–60% | Raised gold ring |
| Field | 62–72% | Recessed circuit field |
| Rim | 74–100% | Outer gold band carrying the legend |

The overall read is a **concentric target / spiral-G motif**: three raised gold rings
interleaved with recessed copper circuitry, wrapped by a legend rim.

**Legend on the rim:** `Digital Gold` across the top, `DGD` across the bottom, with binary
octets around the sides. Those octets are ASCII — `01000100` = **D**, `01000111` = **G** —
spelling **D-G-D**. (A nice educational beat for a video, and it's verifiable on screen.)

### Palette (sampled from the asset)

| Role | Hex | RGB |
|---|---|---|
| Gold ring, highlight | `#E7C062` | 231, 192, 98 |
| Gold ring, mid | `#E0B04F` | 224, 176, 79 |
| Outer rim | `#CBA555` | 203, 165, 85 |
| Circuit field, mid | `#A45C17` | 164, 89, 24 |
| Circuit field, deep | `#8C430F` | 140, 67, 15 |

This sits inside the studio's existing gold/amber + navy identity. Keep backgrounds navy,
charcoal, or dark marble; let the coin carry the warmth.

---

## 5. Workflow — how to actually get a consistent coin

**Preferred — use the tool. It does §3 for you:**

```
python tools/dgd.py assets coin --preset hero --out coin_hero.png
python tools/dgd.py assets coin --preset hand --onto plate.png --out shot.png
python tools/dgd.py assets coin --preset accent --no-plate --out corner.png
```

It loads the reference asset, **squares the 1920×1905 canvas** so the disc is a true
circle, scales to the preset, and adds a contact shadow. Presets map to §3:
`hand` 45.8% · `hero` 55% · `accent` 15% · `macro` 85% of frame width.

For physical accuracy in a scene where you know the scale, skip presets:

```
--ppmm 12.903        # scene is 12.903 px per mm -> coin renders at true 34.1mm
--mm 76              # frame is 76mm wide       -> coin holds its true size
```

`kit` now emits `00_coin.png` automatically, so every asset set ships with a correct coin.
There is deliberately **no `--count`** — see §8.

**Doing it by hand** (other tools, video editors):

1. Generate or shoot the *scene* with no coin in it. Prompt for an empty hand, an empty
   surface, a dark marble plinth — and say **"no coin, no currency, empty"** explicitly.
2. Composite `nbgdgd.png` in, **resized to a square**, at the size from §3.
3. Match the plate: warm the coin to the scene's colour temperature, add contact shadow,
   and match the highlight direction to the scene's key light. An unshadowed coin floats.

**For motion, use `coin-motion` (§6)** — spin, flip, tumble, wobble and orbit all render
from the reference asset, so a moving coin is the same coin as a still one.

**If you must prompt a generator for a coin-in-scene** (e.g. a video model that can't take
a composite and needs motion `coin-motion` doesn't cover), then:

- Describe it precisely: *"a gold coin with three concentric raised rings, a recessed
  copper circuit-board texture between them, a stylised G at the centre, and a lettered
  outer rim"*
- Treat the output as **b-roll texture only** — motion, glint, depth of field. Never as a
  hero shot where the face is legible.
- Any frame where a viewer could read the face must use the real asset.

**Never:**
- let a generator invent the legend, the ring count, or the G mark
- stretch the coin non-uniformly (it is a circle — lock the aspect)
- put the coin at a size that contradicts `dgdhandref.jpg`
- show it alongside other cryptocurrency coins in a way that implies a comparison of value

---

## 6. Motion — spinning, flipping, tumbling, orbiting

A turning coin is the single most useful piece of DGD b-roll, and the thing generators
get most wrong. `coin-motion` renders it from the reference asset, so a spinning coin is
the *same* coin as a still one.

```
python tools/dgd.py assets coin-motion --mode flip --frames 48 --outdir raw/flip \
    --webp flip.webp                     # alpha preserved
python tools/dgd.py assets coin-motion --mode orbit --no-plate --outdir raw/orbit
```

| Mode | Motion | Use for |
|---|---|---|
| `spin` | in-plane, face always to camera | logo stings, loops behind text |
| `flip` | end over end, horizontal axis | "two sides to this" beats, transitions |
| `tumble` | about the vertical axis | hero reveals, slow rotating b-roll |
| `wobble` | tilts back and forth, never fully over | a settling coin; subtle ambient motion |
| `orbit` | elliptical path with perspective scaling | supply/circulation, "moving through an economy" |

**Every mode loops seamlessly** — frame *N* continues into frame 0, verified by comparing
the wrap delta against its neighbours. Drop the sequence on a loop with no cross-fade.

Output is always numbered PNG frames (what editors want), plus optional `--webp`
(keeps alpha) and `--gif` (flattened — GIF cannot hold partial alpha). Use `--no-plate`
for transparent frames to composite over your own footage.

### What makes it read as a coin: the rim

When the coin turns, the rim becomes visible, and its thickness is what separates a coin
from a flat disc. The renderer drives it from the real ratio:

**2.41 mm ÷ 34.1 mm = 7.07% of the diameter.**

Verified across the rotation — at every angle the silhouette matches the physics exactly:
face height = D·|cos θ|, rim = D·0.0707·|sin θ|. Edge-on renders a pure rim at 7.1% of
the diameter. The rim correctly swaps from below the face to above it past 90°, and light
falls off as the face turns away.

`--thickness 0.12` exaggerates the rim for stylised or oversized work. Leave it alone for
anything meant to read as the real coin.

### The reverse face

Only the obverse exists in the reference set, so the reverse is approximated:

- **`--back-mode same`** (default) — the reverse reads upright, identical to the obverse.
  This is what a medal-aligned two-sided coin looks like, and it keeps the legend readable
  through a flip.
- **`--back-mode mirror`** — the strict mirror. Physically what a single-sided disc would
  do, but it renders `Digital Gold` upside down, which viewers read as a rendering bug.
- **`--back <file>`** — beats both. Use it the moment a true reverse asset exists.

---

## 7. Scale is a mode, not a constraint

Physical accuracy matters for **in-hand and product shots**, where a wrong-sized coin
breaks the illusion. It is irrelevant for hero, title-card, and monumental treatments —
a coin filling the frame as a graphic device is not claiming to be 34.1 mm.

| Intent | How to size it |
|---|---|
| In-hand, product, realism | `--preset hand`, or `--ppmm` / `--mm` for a known scene scale |
| Hero, title card | `--preset hero` / `macro` |
| Monumental, abstract, oversized | `--diameter <px>` — free, ignores physical scale |

What must **never** vary, at any size, is the coin's **identity**: the face, the legend,
the ring count, the palette — and, when it turns, the 7.07% rim ratio. Size is free.
Identity is not.

---

## 8. Compliance rail — coin imagery is not exempt

The coin is the most seductive route into non-compliant framing, because gold-coin imagery
carries investment connotations by default. The prime directive applies to pictures exactly
as it applies to words.

**Do not render the coin:**
- in stacks, piles, heaps, or spilling from a container — that is wealth-accumulation
  imagery. (This is why `assets coin` has no `--count`: it renders exactly one.)
- on or beside a price chart, candlesticks, or an upward arrow
- with rocket, moon, casino, or money-rain motifs
- being handed over in a transaction framed as buying in
- as a prize, jackpot, or trophy

**Do render the coin:**
- as a **single** coin — one object, studied and explained
- held in a hand, on a plain surface, on dark marble, in a raking light
- exploded, cut away, or annotated to explain how it works
- alongside the Saint-Gaudens for **heritage and size** context, never for value comparison

The gut check from the prime directive holds: *if a viewer never acquires a single coin, is
this image still honest and educational?* A single coin on marble passes. A pile of coins
next to a green arrow does not.

Coin imagery still needs the **AI-generated disclosure** if the surrounding scene was
AI-generated — compositing a real asset into a synthetic plate makes the frame synthetic.

---

## Connects to
- Asset rendering: `asset-generation.md` · Prompts: `../../LLMWiki/prompts/image-and-video-prompts.md`
- Rails: `compliance-gate.md` · `../../LLMWiki/compliance/communications-discipline.md`
- Source files: `../../Knowledge Base/Coin Ref/`
