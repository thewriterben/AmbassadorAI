# Returning your designs

Everything in this package can be replaced. To make sure each returned file goes
straight into the right place in the app and the web arcade, please follow these
rules.

## 1. One zip, same folders, same names

- Send back one zip, named `DGD-Design-Return-YYYY-MM-DD.zip`.
- Inside it, use **this package's folder structure** (`1-app-shell/…`,
  `2-in-app-arcade/…`, `3-web-arcade/…`, `fonts/…`).
- **Same path and file name = a replacement.** Only include files you changed.
- Put anything that has no existing file (a new icon, a new background, a new
  screen element) in `new/`, and say where it goes in `CHANGES.txt`.
- Add `CHANGES.txt` (start from `CHANGES-TEMPLATE.txt`): one line per file — what changed and anything we should
  know (for example "gold coin: now has a raised rim; same size").
- Screen redesigns (layouts, colours, spacing, type) go in `mockups/` as PNG or
  PDF, or a Figma link in `CHANGES.txt`. Most screens are drawn in code, not
  from images, so a mockup is how a layout change reaches us.

## 2. Images

| Kind | What to send |
|---|---|
| Game pieces, coins, map nodes, seals, vaults | PNG, transparent background, **same pixel size** as the file you replace (listed in `manifest.csv`), artwork centred with roughly the same margin |
| Backgrounds | PNG, same pixel size (1080 × 1920 today), no transparency needed |
| When Pigs Fly boar sheets | **8 square frames in one row**, 448 px each (3584 × 448), boar facing right, transparent. Frame order: 0–3 wingbeat (up, mid, down, recovery), 4 hurt, 5 dash (wings swept back), 6 landing (braking, legs down), 7 standing (wings folded). Keep the body inside the middle two-thirds of each frame; the rest is room for the wings |
| Hi-res masters | Welcome for anything: send at 2× or larger in `masters/`, and we will export |

All images: sRGB, no text baked into game pieces, no drop shadows that cross
the image edge.

## 3. Icons

| Icon | What to send |
|---|---|
| Android app icon | One **1024 × 1024** master, plus the adaptive-icon layers: a **foreground** 432 × 432 PNG (transparent; the phone shows the central 288 × 288 and may mask it to a circle, so keep the artwork inside a central 264 px circle), a **background** colour or 432 × 432 PNG, and a **monochrome** silhouette 432 × 432 (single colour, transparent) for Android's themed icons. We generate every density |
| iOS app icon | 1024 × 1024 PNG, **no transparency**, no rounded corners (iOS rounds them) |
| Google Play icon | 512 × 512 PNG, no transparency |
| Web arcade icons | 512 × 512 master; a **maskable** version whose artwork sits inside the central 80% circle; a favicon at 32 × 32 and 64 × 64. (The current web icons are Flutter's placeholders and need replacing.) |

## 4. Sound and music

- Masters as **WAV**, 44.1 or 48 kHz, 16 or 24-bit. MP3 is fine for music if
  that is all there is.
- Sound effects: trimmed tight at the start (they fire on a touch), no long
  tails. Where a sound has `_1`, `_2`, `_3` takes, send three slightly
  different takes so repeats do not sound mechanical.
- Music: loopable end-to-start if possible. We level every track to about
  −20 LUFS so they all play at one volume; you do not need to master loudness.

## 5. Fonts

TTF or OTF, with the licence, and it must allow embedding in an app and on a
website. The current fonts are all under the SIL Open Font License.

## 6. Things that must stay true

- **Inside the DGD phone app** there is no prize-style celebration: no coin
  showers, jackpots, slot-machine or casino looks. The arcade's words are XP,
  badges and levels — never "earn", "cash", "dollars", "prize" or "win money".
  The line *"Educational only. XP and badges have no monetary value."* stays on
  the arcade home.
- The app's link to the web arcade reads exactly **"DGD Arcade for Web — Play
  in your browser"**. Its look can change; the wording cannot.
- On the web arcade, the rewards line on the landing and the text of the rules
  page are set by DGD's counsel. Restyle them freely; please do not reword.
- The six Coin Quest coin colours must stay easy to tell apart, including for
  colour-blind players (a shape or mark difference helps).
- Text must stay readable on the dark background (WCAG AA contrast).
