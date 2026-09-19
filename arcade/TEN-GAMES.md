# The next ten — proposal

Working plan for the ten arcade games replacing the nine removed on 2026-09-16.
Nothing is built yet. React to the names, the themes and the scope column, and
I'll start on the shared scaffold.

**Settled so far:** scope is mixed and I choose per game; no quiz content in any
of them, themed only; the falling-block game gets its own design rather than a
Tetris reskin.

**The list is complete.** The tenth is a Galaga-style fixed shooter, added
2026-09-17. Galaga is Bandai Namco's trademark, so as with the other nine the
name is ours and only the mechanic carries over.

---

## Names

Every one of these is a mechanic wearing DGD clothes. The mechanics are not
protected — courts have consistently held game rules and systems to be
unprotectable ideas. What is protected is the names, the characters and the
specific audiovisual expression, so none of that is going anywhere near this.

The working names below are mine and are meant to be argued with.

| # | Your shorthand | Working name | Mechanic | Scope |
|---|---|---|---|---|
| 1 | Space Invaders | **Assay Line** | Fixed shooter, descending ranks | Endless |
| 2 | Pac-Man | **Vault Floor** | Maze collect-and-evade | 16 levels |
| 3 | Frogger | **Cold Transit** | Lane crossing under timing | 16 levels |
| 4 | Dig Dug | **Deep Seam** | Tunnelling, collapse traps | 12 levels |
| 5 | Q*bert | **The Refinery** | Isometric hop, convert each face | 16 levels |
| 6 | 1942 | **Network Run** | Vertical scrolling shooter | 5 stages, then endless |
| 7 | Tetris | **Bullion** | Falling-block stacking — redesigned | Endless |
| 8 | Asteroids | **Ore Field** | Inertial drift, splitting targets | Endless |
| 9 | Tempest | **The Rim** | Tube shooter on a closed ring | Endless |
| 10 | Galaga | **Paper Fleet** | Formation flyers, divers, capture-and-rescue | Endless |

## Themes

Each maps to something an ambassador actually has to explain, so the theming
does the teaching that the removed quiz games used to do.

- **Assay Line** — ranks of unverified claims descend; your beam assays them.
  Abstract shapes, no characters, nothing resembling a person or a competitor.
- **Vault Floor** — collect bullion through a vault plan while leaks spread.
  The power-up is an audit seal, which closes leaks for a few seconds.
- **Cold Transit** — move one bar from refinery to vault across transport,
  customs and handover lanes. Mistime a lane and the bar goes back.
- **Deep Seam** — extraction. Dig, collapse strata onto hazards, bring ore up.
- **The Refinery** — hop a pyramid of bars, each landing refining a face from
  ore to struck coin. Clear the pyramid.
- **Network Run** — fly the chain, clearing what's in the way. The stage names
  are the release flow.
- **Bullion** — stack bars into a vault; a sealed row is assayed and clears.
- **Ore Field** — drift among ore bodies that split as you break them.
- **The Rim** — hold the perimeter of a closed network ring.
- **Paper Fleet** — squadrons of paper claims fly in, wheel into formation and
  dive. See below on the name.

## Two fixed shooters — how they differ

Assay Line (#1) and Paper Fleet (#10) are both "ship at the bottom, things
above". Built naively they would be the same game twice, which is the risk in a
ten-game list with two shooters in it. The originals solved this and we can
borrow the *distinction*, which is mechanics and therefore not protected:

| | **Assay Line** | **Paper Fleet** |
|---|---|---|
| Enemies | A rigid block that steps sideways and drops a row | Fly in along curved paths, then hold formation |
| Threat | The wall descending on you | Individual divers peeling off and attacking |
| Tempo | Accelerates as the block thins out | Constant, with waves |
| Cover | Destructible shields you erode yourself | None — you dodge |
| The hook | Survive the descent | One flyer can capture your ship; shoot the captor and you fly as a double |
| Feels like | Pressure closing in | Dogfighting |

The capture-and-rescue hook is the one worth getting right, because it is the
only mechanic in the ten that risks a loss and turns it into a gain. Themed:
a claim seizes one of your bullion bars, and shooting it down returns the bar
and doubles your assay beam.

## A note on "Paper Fleet"

The name is mine and I want to flag the reasoning rather than bury it.

"Paper gold" is a standard industry term for claims on gold that are not
allocated bullion, and the contrast with allocated metal is genuinely part of
what an ambassador explains. So the name does real educational work.

The risk is that it could read as aimed at named competitors rather than at a
concept. My view is that it does not — it is a category term, the enemies are
abstract shapes, and nothing in the game names or depicts a company. But it is
a naming decision on a financial product's own app, so it belongs in the same
counsel review as the rest of the list (§2.4 of `MEETING-BRIEF.md`).

If counsel would rather avoid it entirely, **Squadron** or **Interception** are
neutral alternatives that cost nothing to swap in — the mechanic does not
change.

Nothing here should frame a hazard as a person, a critic or a competitor. Abstract
shapes only — that keeps the content rating low and keeps the app well away from
anything that reads as disparaging a third party.

## Why the scope split

Maze, lane-crossing, tunnelling and isometric games are **layout** games: the
design work is the level, and endless variants of them are weak. Shooters and
stackers are **pressure** games: the design work is the escalation curve, and
discrete levels get in the way. Splitting them this way means roughly 60 layouts
to design across four games, which is a quarter of what Coin Quest's 60 levels
took, because these layouts are far simpler than a calibrated match-3 board.

## Bullion — what "redesigned" means concretely

The Tetris ruling turned on the piece shapes with their colour, shading and
borders, the playfield dimensions, and how pieces behave. So:

- **Not the seven tetrominoes.** A six-piece set built from bar and ingot
  silhouettes, including at least one piece that is not four cells.
- **Not a 10×20 board.** Wider and shorter, sized to a vault shelf.
- **Different clear rule.** A row clears when it is *sealed* — complete and
  with no gap beneath it — which changes stacking strategy rather than being a
  cosmetic difference.
- **Own presentation** throughout: DGD metals, our own drop and lock feel, no
  ghost piece convention, no hold queue.

This is defensive design, not paranoia. It is the one genre where a
differently-named, independently-written clone has lost.

## Shared work, and the build order

These ten have far more in common with each other than the old nine did. Before
any game gets built I want the shared layer in place, or I will write it ten
times:

1. **Arcade scaffold** — a cabinet frame: lives, score, high score, wave/level
   readout, pause, game over, "insert coin" restart, and a single XP submit at
   the end of a run. One place, ten users.
2. **One vertical slice.** I'd build **Assay Line** first: it is the simplest
   mechanic on the list, it exercises the whole scaffold end to end, and it
   proves the shape before nine more are poured into it.
3. **Then in pairs**, sharing what they can — the two shooters together, the
   two layout-heavy ones together, and so on.

The XP, badge, streak and standings layer kept from the old arcade is what these
plug into. No new backend work is needed unless a game wants server-verified
scoring, which none of them do as specified.

## The educational claim

With no quiz content in any of the ten, the app's "Educational only" footer and
the arcade plan's framing now rest on the theming above plus Coin Quest. That is
defensible but thinner than it was, and the Play content-rating and
target-audience questionnaires will ask. Two cheap ways to firm it up later, both
of which can wait until the games exist:

- A one-line explainer on each game's start screen saying what the theme maps to.
- Bringing the question bank back as an opt-in mode rather than as interstitials,
  which is what you ruled out.

Worth a decision before submission, not before building.
