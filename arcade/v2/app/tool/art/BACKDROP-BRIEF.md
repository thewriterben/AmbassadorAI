# When Pigs Fly — backdrop drawing brief

What to draw so the backgrounds, columns and ground match the boars. Every
piece is optional and goes in one era at a time: anything not drawn yet
keeps today's code-drawn look, so the game never breaks half-way.

## The pieces, per era

| Piece | File name | What it is |
|---|---|---|
| Sky | `1816_sky.png` | The whole screen behind everything. Doesn't scroll. |
| Far skyline | `1816_far.png` | Distant city, hazy and pale. Scrolls slowest. |
| Mid skyline | `1816_mid.png` | The main city. |
| Near skyline | `1816_near.png` | Dark rooftops or treeline along the very bottom. Scrolls fastest. |
| Ground | `1816_ground.png` | The floor the boar lands on, seen only at the end of a run. |
| Column capital | `1816_capital.png` | The end of a column at the gap. |
| Column shaft | `1816_shaft.png` | A section of column that repeats along its length. |

The nine years are **1816, 1873, 1913, 1923, 1933, 1944, 1971, 1979, 2009**.
Put the files in `tool/art/source/backdrop/` (PNG, JPG or WebP) and run:

    python tool/art/import_backdrops.py --preview <folder>

The preview shows each era composed as the game shows it, before any build.

## Size and shape

Draw at any resolution; the importer scales each piece by its **height**,
so what matters is the shape (width to height).

The reference is a phone screen, **1080 × 2424**. Each piece's height is a
fixed share of the screen's height:

| Piece | Height on screen | Where it sits | Shape to draw (at reference size) |
|---|---|---|---|
| Sky | the full screen | fills it | **1080 × 2424** portrait; wider screens crop top and bottom, so keep the important things in the middle |
| Far | 45% of the screen | its bottom 86% down, just above the mid city | **1090 tall**, at least **2700 wide** |
| Mid | 40% | its bottom on the screen's bottom | **970 tall**, at least **2400 wide** |
| Near | 20% | its bottom on the screen's bottom | **485 tall**, at least **2400 wide** |
| Ground | 16% | hanging from the ground line down | **390 tall**, at least **2160 wide** |
| Capital | the column's width | at the gap | **92 wide** (draw 368 wide, 4×), any height, about 100–400 at 4× |
| Shaft | the column's width | repeats away from the gap | **92 wide** (368 at 4×), about as tall as wide or taller |

A skyline's height is its whole band, including any empty sky above the
roofs, so leave the top clear where the buildings are low.

## Rules that keep the game playable

**Tiling.**
- The skylines and the ground repeat side by side: the right edge must join
  the left edge seamlessly.
- The shaft repeats end to end: its top must join its bottom.
- The importer warns when a join shows.

**Transparency.**
- The skylines and column parts need a transparent background.
- A PNG with real transparency is best.
- Otherwise draw on **pure white (#FFFFFF)** or **pure magenta (#FF00FF)**
  and don't use that colour anywhere in the art: the importer clears it,
  including gaps between buildings.
- Sky and ground are solid.

**Keep the play space readable.** Coins (gold, silver, copper) and the boar
fly over all of this:
- **Sky:** dark and low-contrast. Nothing bright, gold or round in the
  upper two-thirds. A moon is fine as a thin, pale, cool crescent off to a
  side; a full gold moon reads as a coin.
- **The top 12% is under the HUD** (the back arrow, the momentum dots, the
  era, the pause button). Keep it plain sky; a moon or a landmark there
  hides behind the HUD. The first stand-in's moon did.
- **Skylines:** darker and duller than the columns, with small lit windows.
  Far is hazier and paler than mid; near is the darkest, nearly a
  silhouette.
- **Columns:** the lightest, crispest things on screen after the coins and
  the boar. A player must see a column at a glance against any city.

**Columns.**
- Draw the capital as the **top of a standing column**. The game flips it
  for columns hanging from above.
- Fill the full width at the capital. The shaft may be narrower but
  centred.
- **Don't draw the amber strip at the gap**: the game draws it, and it
  must stay the brightest thing there.
- Light comes from the left, as on the boars.
- A column never ends on screen, so there's no base to draw.

**Ground.**
- The top edge is where the boar's hooves stand. Keep it level and plain;
  the game draws an amber line along it.
- Only the **top part** shows: the ground rises from 94% of the screen's
  height to 87% as the boar comes in to land, so 6–13% of the screen, a
  third to four-fifths of the strip. The phone's own navigation bar can
  cover the bottom few percent. Put the ground's character in its top
  third.

**Content.**
- Evocative, not portraits: period architecture that says where and when,
  not recognisable real buildings.
- No logos, brand names, readable signs, or real people.

**Style.** The same pixel-art look and palette family as the boars.

## Each era, as it stands today

Keep or replace these; they're how the code-drawn version sets each era.

| Year | The era in the game | Today's city | Today's columns |
|---|---|---|---|
| 1816 | The pound, by weight | London: terraces and chimney pots, church spires, the odd dome | Fluted Portland stone |
| 1873 | Silver steps back | An American city: brick blocks with cornices, mansard roofs, spires | Cast iron, banded, flared head |
| 1913 | A central banking system | New York: brick with water tanks, the first skyscrapers | Riveted steel with lattice |
| 1923 | The papiermark | Berlin: factories and stacks, tenements, domes, few lit windows | Brick chimneys, sooty mouth |
| 1933 | Gold called in | A Depression-era American city: Art Deco setbacks, many dark windows | Art Deco, brass flutes, chevron |
| 1944 | Bretton Woods | Dark mountains, pines, a grand hotel | Timber posts with iron straps |
| 1971 | The window closes | Washington: low and classical, domes, pediments | White marble |
| 1979 | Rates raised | Late-seventies downtown: brutalist blocks, glass boxes | Board-marked concrete |
| 2009 | Issuance in code | A glass city at night, towers of lit windows | Dark glass, cyan edge light |

The sky warms from blue-black in 1816 to amber-brown by 2009. The game
blends skies between eras, so matching that progression makes the changes
smooth.

## How it behaves in the game

- **Crossfades:** eras change with a crossfade about a third of a screen
  either side of the change.
- **Partly drawn:** while only some eras are drawn, the code-drawn city of
  the next era rolls in from the right a screen or two before the change,
  behind a drawn skyline. That's the old look arriving on time, and it
  goes once the next era is drawn too.
- **Parallax:** far scrolls at 0.12 of the columns' speed, mid 0.30, near
  0.55; the ground moves with the columns. Any of these can be changed per
  era in `tool/art/source/backdrop/tuning.json`.
- **Memory:** only the era being flown and its neighbours are held in
  memory.

## Making the pieces with Nano Banana

The prompts, every era written out in full, are in
[BACKDROP-PROMPTS.md](BACKDROP-PROMPTS.md), generated by
`backdrop_prompts.py` (edit the eras or wording there and regenerate). The
same prompts are on a page with a copy button for each.

**Every time:**
- Start a **new Nano Banana chat for each era**. Long chats stop working
  properly, so no prompt relies on the chat's history.
- Attach one of the boar drawings, for style, and that era's code-drawn
  background render, for mood. From the second piece on, also attach the
  era's finished sky, so the palette carries over; for the shaft, attach the
  finished capital.
- Make the pieces in the given order: sky, far, mid, near, capital, shaft,
  ground. If a chat misbehaves partway, start another with the same
  attachments.
- Save each as `{year}_{piece}` (`.webp`, `.png` or `.jpg`) in
  `tool/art/source/backdrop/`.

**Aspect ratios:** Nano Banana has no 21:9, so the wide pieces are made at
16:9 with the art kept to the lower part of the frame.

| Piece | Aspect |
|---|---|
| Sky | 9:16 |
| Far, mid, near skylines | 16:9 |
| Column capital | 1:1 |
| Column shaft | 9:16 |
| Ground | 16:9 |

**No cropping by hand.** The importer trims every piece to shape:
- **Skylines:** loses the clear sky above the tallest building, but for a
  6% margin.
- **Ground:** loses the plain rows below its detail.
- **Column parts:** trimmed to the art's width, with the shaft set to the
  width of the neck under the capital.
- **All pieces:** the magenta is taken out of the art's edges, so pink
  outlines aren't a reason to regenerate.
- **Skies:** a flat frame drawn round the edges is trimmed.
- **Repeating pieces:** a drawn line along the joining edges (2009's ground
  had one) is trimmed, when the seam would otherwise show.
- **Ground above its line:** grass or kerbs rising above the ground line
  are kept, drawn standing over it.
- **Brightness:** a piece that came out too bright or dark can be adjusted
  instead of regenerated, with `shade` and `tint` in
  `tool/art/source/backdrop/tuning.json` (1944's mountains use it).

**What the prompts learned from 1816:**
- **Several depths in one skyline.** The first far skyline drew three
  depths in one image, filled the gaps with pale beige haze, and had
  mismatched ends. In the game that would have been an opaque,
  daylight-coloured wall with a jump at every repeat. Every skyline prompt
  now says "only this one layer", asks for night colours, and puts magenta
  in every gap.
- **The moon hidden.** It came out 77% of the way down, behind the city. The
  sky prompt now places it 20–35% down, and eras with heavy haze or smog
  have none.
- **Shaft and capital in different tones.** The shaft came out warm beige
  under a cool grey capital. The shaft prompt now asks it to match the
  capital exactly.

The replies for fixing a result are at the end of the prompts file. In a
long or misbehaving chat, paste the piece's prompt into a new chat with its
attachments and add the reply to the end of it.
