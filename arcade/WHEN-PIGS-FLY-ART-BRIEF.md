# When Pigs Fly — boar art brief

Final sprite art for the player character of *When Pigs Fly*, game 1 of the
DGD Arcade v2 catalogue (design: `TEN-GAMES.md`, "When Pigs Fly"). The game
ships today with generated placeholder sheets. The art below replaces them
file for file. No code changes are needed if the sheet layout is kept.

**Placeholders to beat:** `v2/dist/shots/boar-sheets.png`, a preview of all
three sheets, and `v2/dist/shots/pigs-*.png`, the placeholders in the game on
a Pixel 9a.

## The character

A winged **piggy bank styled as a wild boar**. It flies a one-tap corridor
through two centuries of monetary history, collecting gold, silver and copper
coins, and every run ends in a landing. It grows across many play sessions
through three stages, and a player keeps the stage they reach.

**One detail must appear at every stage: the coin slot.** A short dark slot
along the spine, just behind the shoulders, with a bright lower lip. It is the
only thing that says "piggy bank", so it has to read at game size. Nothing
else should turn it into a bank: no padlock, no dollar signs, no coins
spilling out of it at rest.

| Stage | Description (the owner's words, condensed) |
|---|---|
| **Piglet** | Small wild-boar piglet with tufts of golden-blond fur. Wild piglets are striped, so cream humbug stripes along the flank are welcome. Small, stubby wings. Cute rather than fierce. |
| **Juvenile** | Filled out, with bristly, medium-length fur whose colour is shifting from brown toward gold. Small tusks have come in. A bristle ridge along the spine. Wings grown to working size. |
| **Razorback** | Full-size razorback, fierce and intense. A glorious golden coat, a luxurious crest along the spine, and a cape-like mane flowing back over the shoulders. Large curved tusks. Battle-scarred on the flank and face. Large, dragon-like wings with finger bones and a scalloped membrane. |

**Style.** "32-bit" pixel art in the sense of the high-colour console era:
crisp pixels, a considered limited palette per stage, shading by hand-placed
clusters or ordered dither, and a selective dark outline. No anti-aliased
edges, painted gradients or blur. The game draws the sheets with
nearest-neighbour sampling, so what is delivered is what is seen.

**It must read against the game's sky,** a near-black navy grading to deep
blue, tinted per era toward amber, plum and teal. Gold on navy is the point.
Keep the darkest outline colours warm (dark brown, not black) so the silhouette
doesn't vanish.

**Originality.** The design must not resemble any existing game's boar,
pig or winged-pig character. That is the part of an arcade homage that
carries legal risk, and it is a hard requirement. No text or logos
on the sprite. The coins carry the brand, the boar does not.

## The sheet contract

The code enforces all of this (`lib/arcade/passage/boar.dart`).

- **One PNG per stage:** `boar_piglet.png`, `boar_juvenile.png`,
  `boar_razorback.png`. RGBA, sRGB, transparent background.
- **One row of eight square frames**, facing right. The frame side is the
  image height, so the image is exactly 8 × as wide as it is tall. A sheet of
  any other shape is refused, and the game draws a plain gold coin instead.
- **Frame order:**

| # | Pose | Notes |
|---|---|---|
| 0 | Wings up | Top of the wingbeat |
| 1 | Wings mid, level | Legs tucked. The vertical anchor is measured from this frame |
| 2 | Wings down | Bottom of the wingbeat |
| 3 | Recovery | Wings folding on the way back up |
| 4 | Hurt | Wings crumpled, eyes squeezed shut. Shown for 0.35 s after a strike |
| 5 | Dash | Wings swept straight back, body level. Shown during the dash ability |
| 6 | Landing | Wings raised to brake, legs down. Shown in the last metres before touchdown |
| 7 | Standing | Wings folded, all four hooves on the ground line. Shown after touchdown, and as the portrait on the results sheet and front room |

- **Animation.** Frames 0–3 loop at 8 fps in flight, 20 fps for a quarter
  second after each tap, and 4 fps in a glide. They need to cycle smoothly in
  that order.
- **Headroom.** The frame is about 1.5 × the boar's body length, with the body
  in the lower-middle. Raised wings go above it and swept wings behind it.
  Nothing may touch a frame edge. The checker flags it.
- **Same scale in all eight frames** of a sheet. The body stays in the same
  place from frame to frame, apart from the landing and standing frames' legs.
- **Size.** Author at 1× in whatever resolution suits the detail, then export
  at an integer scale (×2, ×3, ×4) so each frame is at least 96 px. The
  placeholders are authored at 48, 72 and 108 px frames and exported at ×4. The
  game scales the frame to a size set per stage, so the absolute resolution
  sets detail, not size on screen.
- **Relative size:** the razorback should look clearly bigger and heavier than
  the juvenile, and the juvenile bigger than the piglet. On screen the frames
  are drawn at 5.6, 6.6 and 7.8 hitbox radii. The hitbox itself never grows,
  so the razorback's wings and mane may overlap a pillar harmlessly.

## Placement numbers

`BoarSpec` in `boar.dart` holds three numbers per stage, as fractions of the
frame side:

- **`footV`:** where the hooves meet the ground in frame 7. It is exact, and
  the checker measures it.
- **`anchorU`, `anchorV`:** where the hitbox centre sits. It should be the
  middle of body-and-head, not of the frame. This is a judgement call:
  - The checker prints the centre of mass as a starting point, but it runs
    behind the true centre because of the mane and wings.
  - Set the anchor so the boar's body sits over the collision circle.
  - Then confirm on a phone by flying through a tight gap. A strike should
    look like a strike.
- **`sizeInRadii`:** only if the new art's proportions change how big each
  stage should look.

## Handing it over

1. Run the checker on the delivery folder:

   ```bash
   python tool/art/check_sheets.py path/to/delivery
   ```

   It must exit 0, and any warnings should be understood.
2. Copy the three PNGs over `assets/images/boar_*.png`.
3. Update `footV` from the checker, and `anchorU` / `anchorV` as above.
4. Regenerate the home-card image `assets/images/card_pigs.png` from the
   razorback's frame 0, trimmed and squared. The generator's `main()` shows
   how.
5. Build the DEV APK. In the game, use **DEV → Next boar stage** to fly each
   stage, and check the landing (DEV → Skip to the landing) and the results
   portrait.

`tool/art/boar_sprites.py` generated the placeholders and can be kept or
deleted once final art lands. Nothing in the game depends on it.
