# When Pigs Fly — unbranded coin prompts

Prompts for Nano Banana Pro that replace the three pickups (gold, silver,
copper) with coins that carry **no DGD identity**. This closes review finding
**E1** (`arcade/AUDIT-DGD2.0-2026-09-30.md`).

The pickups are the DGD coin renders today, and they are worth 10, 3 and 1
points. Inside a finance app, collecting "DGD coins" of three worths can
read as the token having in-game value. The owner's call (2026-09-30):
test with them now, replace them before the public release.

**The new design.** One design struck in three metals:
- a plain raised rim;
- a small pair of outstretched wings in the middle. That is the game's own
  mark, so the coins read as When Pigs Fly's tokens, not as money.

There must be **no letters, numbers, currency signs, faces, portraits, stars
of state or national emblems**: nothing that resembles real coinage or the
DGD coin.

**Every time:**
- Start a new chat for each prompt.
- Attach the files named with the prompt.
- If a coin comes out wrong, run the prompt again in a new chat rather than
  correcting it over several replies.
- Make gold first. Silver and copper are made from the finished gold coin,
  so all three share one design.

**Background:** solid magenta `#FF00FF`, not white, because a silver coin
on white cannot be keyed out cleanly. `tool/art/import_coins.py` removes the
magenta, trims to the coin and writes the 512 px pickups.

**Size on screen:** about 40 dp in flight. Keep the wings bold and simple.
Fine engraving disappears at that size.

## The shared part

Every prompt below starts with this paragraph:

```
Create a pixel art game sprite of a single round coin, seen straight on (a flat circle, not tilted, no perspective, no thickness showing), centred and filling about 85% of a square image. Match the pixel art style, pixel size and shading of the attached boar drawing, which is the game's style reference. The coin has a plain raised rim and, in the middle, a small pair of outstretched feathered wings, embossed in the metal. No letters, no numbers, no words, no currency symbols, no faces, no portraits, no emblems, no stars, nothing that resembles a real coin or banknote. Solid flat magenta #FF00FF background filling the whole image: no gradient, no shadow, no glow, no sparkle, no border, no text.
```

## Gold

Attach `tool/art/source/boar_piglet_stand_drawn.jpg` (the style reference).
Save the result as `tool/art/source/coin_gold.png`.
```
Create a pixel art game sprite of a single round coin, seen straight on (a flat circle, not tilted, no perspective, no thickness showing), centred and filling about 85% of a square image. Match the pixel art style, pixel size and shading of the attached boar drawing, which is the game's style reference. The coin has a plain raised rim and, in the middle, a small pair of outstretched feathered wings, embossed in the metal. No letters, no numbers, no words, no currency symbols, no faces, no portraits, no emblems, no stars, nothing that resembles a real coin or banknote. Solid flat magenta #FF00FF background filling the whole image: no gradient, no shadow, no glow, no sparkle, no border, no text.
Metal: warm polished gold, bright yellow highlights on the upper left, deeper amber in the recesses.
```

## Silver

Attach the finished `coin_gold.png` and `boar_piglet_stand_drawn.jpg`. Save
the result as `tool/art/source/coin_silver.png`.
```
Create a pixel art game sprite of a single round coin, seen straight on (a flat circle, not tilted, no perspective, no thickness showing), centred and filling about 85% of a square image. Match the pixel art style, pixel size and shading of the attached boar drawing, which is the game's style reference. The coin has a plain raised rim and, in the middle, a small pair of outstretched feathered wings, embossed in the metal. No letters, no numbers, no words, no currency symbols, no faces, no portraits, no emblems, no stars, nothing that resembles a real coin or banknote. Solid flat magenta #FF00FF background filling the whole image: no gradient, no shadow, no glow, no sparkle, no border, no text.
Exactly the same coin as the attached gold coin, the same design, size and wings, struck in cool bright silver instead: white highlights on the upper left, blue-grey in the recesses.
```

## Copper

Attach the finished `coin_gold.png` and `boar_piglet_stand_drawn.jpg`. Save
the result as `tool/art/source/coin_copper.png`.
```
Create a pixel art game sprite of a single round coin, seen straight on (a flat circle, not tilted, no perspective, no thickness showing), centred and filling about 85% of a square image. Match the pixel art style, pixel size and shading of the attached boar drawing, which is the game's style reference. The coin has a plain raised rim and, in the middle, a small pair of outstretched feathered wings, embossed in the metal. No letters, no numbers, no words, no currency symbols, no faces, no portraits, no emblems, no stars, nothing that resembles a real coin or banknote. Solid flat magenta #FF00FF background filling the whole image: no gradient, no shadow, no glow, no sparkle, no border, no text.
Exactly the same coin as the attached gold coin, the same design, size and wings, struck in warm reddish copper instead: pinkish highlights on the upper left, dark brown in the recesses.
```

## After the three are drawn

```
python tool/art/import_coins.py
```

This keys out the magenta, trims to the coin, centres it, and writes
`assets/images/pickup_gold.png`, `pickup_silver.png` and
`pickup_copper.png` (512 px, transparent). It also prints each coin's
colour, so a silver that came out yellowish shows up before it ships.

`PassageGame`'s pickups then point at those files instead of the DGD
renders (`passage_game.dart`, the `PickupKind` image map). The in-flight
glint is drawn in code over whatever image is there, so it carries over.
The leaderboard's medals stay the DGD coins: they only appear in a backend
build, outside the demo.
