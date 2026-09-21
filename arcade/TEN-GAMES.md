# The next ten — working plan

> **This is the v2 plan.** It is built in `C:\src\puzzle-app-v2`, on the
> `v2/ten-games` branch, and mirrored at `arcade/v2/`. None of it goes into
> v1, which is frozen and is what the main DGD app is merging. See
> `VERSIONS.md` before starting work.

The catalogue that replaces the nine games removed on 2026-09-16.

**Game 1 is built.** Passage — the one-tap flyer — was promoted to the first
slot and written on 2026-09-20, along with the shared arcade cabinet every
other game will sit in. Everything below it is still a proposal.

**Settled so far:** scope is mixed and chosen per game; no quiz content in any
of them, themed only; the falling-block game gets its own design rather than a
Tetris reskin; and, new with Passage, **no game in this catalogue ends a run in
failure** unless there is a specific reason it should.

---

## Names

Every one of these is a mechanic wearing DGD clothes. The mechanics are not
protected — courts have consistently held game rules and systems to be
unprotectable ideas. What is protected is the names, the characters and the
specific audiovisual expression, so none of that is going anywhere near this.

| # | Origin | Working name | Mechanic | Scope | State |
|---|---|---|---|---|---|
| 1 | *(new)* | **Passage** | One tap, fly a corridor, land it | 9 eras, finite | **Built** |
| 2 | Space Invaders | **Assay Line** | Fixed shooter, descending ranks | Endless | Proposed |
| 3 | Pac-Man | **Vault Floor** | Maze collect-and-evade | 16 levels | Proposed |
| 4 | Frogger | **Cold Transit** | Lane crossing under timing | 16 levels | Proposed |
| 5 | Dig Dug | **Deep Seam** | Tunnelling, collapse traps | 12 levels | Weakest, see below |
| 6 | Q*bert | **The Refinery** | Isometric hop, convert each face | 16 levels | Proposed |
| 7 | 1942 | **Network Run** | Vertical scrolling shooter | 5 stages, then endless | Proposed |
| 8 | Tetris | **Bullion** | Falling-block stacking — redesigned | Endless | Proposed |
| 9 | Galaga | **Paper Fleet** | Formation flyers, capture-and-rescue | Endless | Proposed |
| 10 | *(open)* | | | | Stack the Bullion recommended |
| ~~—~~ | ~~Asteroids~~ | ~~Ore Field~~ | — | — | **Cut 2026-09-20** |
| ~~—~~ | ~~Tempest~~ | ~~The Rim~~ | — | — | **Cut 2026-09-20** |

---

# 1. Passage — built 2026-09-20

A gold coin flies a corridor through nine eras of monetary history. One tap
holds altitude. Every run ends with the coin on the ground.

## Why it is not an endless flyer

This is the decision the whole game turns on, and it came out of the design
conversation rather than the mechanic.

**In an endless flyer, every session ends in failure** — not sometimes, by
definition. The run is defined as continuing until you fail, so the last thing
a player feels, every single time, is having lost. That is correct for a game
whose hook is the sting of falling just short and whose engine is a
leaderboard. It is wrong for an ambassador training app, where the last beat
should be the one that brings someone back tomorrow.

So the failure model was replaced rather than tuned:

**Every run ends in a landing. The only variable is where.**

- A run is a **finite passage** through nine eras — about seventy seconds.
- Hitting a gate costs one unit of **reserve** (three to start) and knocks the
  coin down. It does not end the run.
- At zero reserve the coin **does not die**. Lift authority fades over about a
  second and it sets down where it is. You landed in 1933. That is a finished
  journey with a story on it, not a death.
- Flying the whole passage triggers a **deliberate landing**: the gates stop,
  the ground rises, and you spend the last of your lift easing onto it.

## The calm stretch

After the final gate there are several seconds of open sky before the ground
appears. This is load-bearing and should not be trimmed for pacing.

Everything before it ramps — gaps narrow from 6.9 coin-diameters to about 4.1,
the scroll quickens — and relief only exists as the release of tension that was
actually held. An endless game can never produce the feeling because it only
ever escalates. The landing is also physically the opposite of a crash:
descending, slowing, settling.

## The honest trade

Guaranteed landings cost replay pressure. "One more go" runs on the sting of
just missing, and this removes the sting on purpose. That is the right call for
this app — it is not trying to maximise session count, it is trying to teach —
but it is a real trade and it was made knowingly.

The mastery headroom moved into the grade instead:

| | |
|---|---|
| ★ | you landed — always earned, there is no way not to |
| ★★ | you flew the whole passage |
| ★★★ | you flew the whole passage **and set it down softly** |

The third star is the only hard thing in the game, and it is a skill rather
than an endurance test: the ground comes up either way, so it is about what you
do with your last lift. The wording above is identical in the code, on the
results sheet and in `passage_test.dart`; if one changes, all three do.

## The content, and what it deliberately does not say

The earlier "your DGD coin avoids things that cause inflation" framing was not
used. A core loop in which the product dodges inflation says, in play rather
than in words, that the product is protected against inflation — a performance
claim about a financial asset, in an app whose every other surface says "XP and
badges have no monetary value". `APK-FINDINGS.md` §3 already has the merged app
drifting into the stores' financial-products category; a game teaching an
inflation-hedge message lands squarely in it.

Both replacement framings were accepted, and both are in the shipped game:

1. **Descriptive** — the coin flies a corridor; obstacles are gates, not
   "inflation".
2. **Historical** — the corridor is monetary history. Nine dated facts, each
   with a source, none of them about Digital Gold at all.

`lib/arcade/passage/eras.dart` carries the rules the content is written under:
sources required, no comparatives, no forward-looking language, no adjectives
doing argumentative work. A unit test greps the facts for the mechanical
failures (`invest`, `hedge`, `outperform`, `will `, `DGD`, …) so a line added in
a hurry cannot ship a claim.

### The fact-check found four errors before any of it was drawn

Worth recording, because they were all the kind that reads fine:

1. **1971 cited the wrong instrument.** Executive Order 11615 is the 90-day
   wage and price freeze; it says nothing about gold. Also softened "ending the
   Bretton Woods system" to "beginning the collapse of" — convertibility was
   suspended in 1971, but the system ran on until 1973.
2. **1923 cited the wrong date.** The Rentenmark was introduced 15 November
   1923; the one-to-a-million-million rate was fixed on 20 November. The figure
   is now written as a numeral, because 10¹² is a trillion on the short scale
   and historically a billion on the long one, and this app ships in both kinds
   of country.
3. **2009 claimed "the first blockchain"** — loses to one search, since
   Bitcoin's own whitepaper cites Haber and Stornetta's 1991 hash-linked
   timestamping. Now says *decentralized*.
4. **Three editorial clauses were cut**: "rather than leaving it to practice"
   (1816), "moving the country onto gold alone" (1873 — which asserts as
   settled the exact thing contemporaries fought over), and "rather than
   decided by a committee" (2009). None was supported by its source.

### Why 1979 is in the list

The fact-check raised something more useful than any of the four. Read as a
sequence, the eight original items told one story: hard money adopted, hard
money abandoned, paper money destroys savings, gold seized, the last link cut,
then a fixed issuance schedule arrives. No line made a claim — **the arc did**,
and it is exactly the argument a compliance reviewer would expect this app to
be making.

So the Volcker disinflation was added as the ninth era. It is a major monetary
event in its own right and it is the counterexample: a central bank
deliberately ending a serious inflation. It is what makes the set read as
history rather than as a thesis with dates attached. **Do not remove it for
pacing without replacing it with something that does the same work.**

## Build notes

| | |
|---|---|
| Files | `lib/arcade/passage/{eras,passage_game,passage_render,passage_screen}.dart` |
| Server | `passage` added to the mini-game allow-list; XP `stars × 12`, plus 24 for a full passage, plus `min(12, score ÷ 50)` for coins. The passage bonus keys off stars, not eras reached — reaching 2009 is not flying through it |
| Min round | 4 s — the shortest legitimate run is a player who taps once and never again, which measures at ~5.3 s and is asserted in the test |
| Tests | `test/passage_test.dart` — layout reachability, gap floor, the star rule, that a player who stops tapping lands rather than dies, and the coin rules below |
| Art | The coins are the DGD coin renders Coin Quest ships (`coin_gold`, `coin_silver`, `coin_copper`); everything else is drawn from primitives. Nothing resembling any existing game's look |

## What playing it on a Pixel found, 2026-09-20

Analyze was clean and fifty tests passed before the APK was ever installed.
Five things were still wrong, and all five are the kind that only a device
shows. Recorded because the lesson generalises to the other nine games.

1. **The game rendered in a 400px strip at the top of a black screen.** The
   cabinet's stack is all `Positioned.fill` except the HUD row, and a Stack
   takes its size from its *non-positioned* children — so it collapsed to the
   height of the HUD. `StackFit.expand`. A test now asserts the GameWidget is
   the size of the screen.
2. **The opening era banner never appeared.** The real cause is worth knowing
   for anything else that talks to Flutter from a Flame game: Flame drives
   `onGameResize` from inside a `LayoutBuilder` callback, i.e. during the
   build phase, so notifying a `ValueNotifier` there calls `setState` on a
   widget mid-build. Flutter throws and drops the notification — and in a
   release build that exception is invisible. Notify from the game loop
   instead, which is why the HUD's `run.tick()` always worked. The banner was
   also rebuilt to use a `ValueListenableBuilder` and a
   `TweenAnimationBuilder`, which have no ordering to get wrong.
3. **The pillars were nearly invisible.** `#16181C → #2E3238` looked like
   brushed metal on a monitor and vanished into the sky on the phone; only
   the amber lip showed, so a gate read as a floating line rather than an
   opening. Now `#32373F → #767F8D`.
4. **A run ending in the first era reported "0 of 9 eras flown"** with no
   fact shown — directly under "You set down in 1816". `erasCleared` counts
   eras flown end to end, which is right for the star rule and wrong for the
   summary. Added `erasReached`. The run most in need of a reason to try
   again was getting the least.
5. **The results sheet lost its buttons off the bottom.** Nine era chips plus
   a paragraph of history is taller than a bottom sheet's default 9/16 cap.
   Body scrolls, footer pinned.

Verified on device after the fixes: the opening banner, a flight through
gates, three strikes, a short landing with its fact, and a full-passage
landing at two stars with all nine eras lit. Screenshots in `dist/shots/`.

**Still not verified:** the third star. It needs a human feathering the
descent — adb taps land it hard every time, which is the mechanic working as
designed. Whether four coin-diameters is generous enough, and whether seventy
seconds is the right run length, are also still open.

## Coins and momentum — added 2026-09-20, same day

The first device build was an MVP with nothing to do between gates. The
second pass adds something to chase, and the reward for chasing it is speed.
Four decisions, each taken deliberately:

1. **Three metals, unequal on purpose, all DGD.** Every coin in the game —
   the one you fly and the ones you collect — is one of the three DGD coin
   renders Coin Quest uses. A **gold coin** (10 points) floats in every
   opening and **drifts the
   full height of it**, half a coin clear of either lip at the extremes, one
   cycle in about 2.4 s. Even gates start at the top and odd gates at the
   bottom, so consecutive coins are always moving in opposite directions
   when you reach them and the line through the passage is a weave rather
   than a groove. Taking one means flying through the gate where the coin
   is, not where the gap is easiest; the risk scales itself — the extremes
   are well off centre in a wide early gap, barely off it in the tightest
   late one. **Silver** (3) and **copper** (1) coins run in a four-coin arc
   across the open air between gates, silver at the peak of the arc and
   copper at its ends, so the coins furthest off the straight line are the
   ones worth bending for. A short copper trail in the lead-in teaches the
   pickup before the first gate. **There are no coins in the calm stretch**,
   for the same reason it is not trimmed: a coin there is one more thing to
   chase.
2. **Momentum, capped.** Every coin adds momentum; momentum scrolls the
   passage faster, up to 1.35× base, and bleeds off slowly when nothing is
   taken. So the fast line is the rich line and the run gets shorter and
   harder the better it is flown — but it is opt-in, because the safe line
   through every gate takes nothing and runs at base speed. The cap exists
   because speed is the one thing that makes a flyer unreadable rather than
   hard. The coin-value multiplier steps ×1 → ×2 → ×3 with momentum and is
   shown in the HUD.
3. **A strike spills, it does not deduct.** Momentum goes to zero and up to
   four points come loose as coins, thrown up and ahead so they arc back
   toward the player and can be caught again for about two and a half
   seconds. The cost is visible and recoverable; a silent minus on a number
   would be a sting, and this game does not do stings.
4. **Points are a bounded XP nudge, never the main event.** The server caps
   the reported score at 1999 and pays `min(12, score ÷ 50)` on top of the
   star formula. The stars are what the design pays for; the coins cannot
   out-earn them. `score` is a new optional field on the mini-round claim,
   stored in a new column, and ignored for any game not listed in
   `config.mini.maxScore`.

Tests hold all of this: every gate's gold coin drifts the height of its
opening without touching a lip, consecutive gold coins are in antiphase, the
metals are ordered gold > silver > copper with silver the rarer trail coin,
no trail coin overlaps a pillar, nothing sits past the last gate,
momentum and speed stop at the cap, a strike spills and never drives the
score negative, uncaught spills fall away, and the score arrives on the
result. The server test checks the formula, the cap, and that a game without
a score ignores one.

**Not yet verified on a phone:** whether the drifting gold coin is a
judgement or a coin-flip at the late gaps, whether 1.35× still reads, and
whether the spill is catchable by a human who has just been knocked down.

---

## The shared cabinet — also built

`lib/arcade/cabinet/cabinet.dart`. The frame all ten games sit in, so the parts
that are identical are written once rather than ten times: run lifecycle, HUD
chrome, pause, backgrounding, the results sheet, and the single XP submit.

A game supplies its Flame view, the middle of its HUD row and the body of its
results sheet. It never touches navigation, the XP API or the sheet. Input is
one `onTap` on the run handle — a game that wants "tap anywhere" should not
have to know what a Flame gesture mixin is.

Two details that are deliberate and easy to undo by accident:

- **The results sheet says "Fly again", never "Retry".** A run that ends is not
  a run that failed.
- **A round is opened with the server when play starts**, not claimed at the
  end from nothing. The server refuses to pay for a round it never issued.

---

## Two cuts, 2026-09-20 — controls, and a catalogue that was shooter-heavy

**Ore Field (Asteroids)** and **The Rim (Tempest)** are out. Both fail on the
same axis: their feel came from a control device that does not exist on glass.

- **Tempest** ran on a **spinner** — a free-spinning rotary dial, the hardest
  arcade input to reproduce on touch. Swiping round a ring is imprecise, and
  your thumb covers the rim you are defending.
- **Asteroids** needs rotate-left, rotate-right, thrust and fire at once, with
  inertia. Touch versions go twin-stick — two thumbs on a small screen, both
  occluding it — or simplify until it stops being Asteroids.

**The stronger reason is variety.** Five of the original ten were shooting
games. Cutting these two drops it to three. The controls argument and the
variety argument pointed at the same two games, which is usually a sign.

**Still the weakest of what remains: Deep Seam (Dig Dug).** Four-direction
movement plus a pump button while carving a maze where precision matters.
Playable, not good. If a third slot is ever wanted, take that one.

## Touch fitness of the survivors

The ones that are genuinely excellent on mobile share one trait: **drag to
position, everything else automatic.**

| Game | Touch fit | Why |
|---|---|---|
| Passage | Excellent | One tap. Nothing else exists |
| Network Run | Excellent | Drag to move, auto-fire. Better on mobile than it was in an arcade |
| Bullion | Excellent | Tap to rotate, swipe to drop. The most proven mobile mechanic there is |
| Assay Line | Excellent | Drag and auto-fire |
| Paper Fleet | Excellent | Drag and auto-fire |
| Cold Transit | Excellent | Discrete hops, vertical lanes suit portrait |
| The Refinery | Good | Discrete diagonal hops; pyramid suits a tall screen |
| Vault Floor | Marginal | Swipe-to-turn works because you follow corridors rather than choosing a path |
| Deep Seam | Poor | See above |

The app is portrait-locked, which suits all of these.

## 10. The open slot — candidates

What the catalogue lacks is **pace variety**: almost everything left is twitch.

| Candidate | Touch fit | Theme | Build |
|---|---|---|---|
| **Stack the Bullion** — one-tap timing, align falling bars, overhang shaved off | Excellent | Bars into a vault | Tiny |
| **Breakout** — drag a paddle, assay beam breaks the vault ceiling | Excellent | Direct | Small |
| **Sokoban** — push bullion onto marks, calm and turn-based | Excellent | Direct | Small, levels are the work |
| **Tower defence** — hold a route to the vault, tap to place | Excellent | Direct | Large |
| **Snake** — swipe; the chain grows as it collects | Good | "The Chain" | Tiny |

**Recommendation: Stack the Bullion.** One tap like Passage but a completely
different feeling — timing and nerve rather than reaction. **Sokoban** is the
best second choice if a genuinely calm, thinking game is wanted.

## Themes

Each maps to something an ambassador has to explain, so the theming does the
teaching the removed quiz games used to do.

- **Passage** — two centuries of monetary history, one era per leg.
- **Assay Line** — ranks of unverified claims descend; your beam assays them.
- **Vault Floor** — collect bullion through a vault plan while leaks spread.
  The power-up is an audit seal, which closes leaks for a few seconds.
- **Cold Transit** — move one bar from refinery to vault across transport,
  customs and handover lanes. Mistime a lane and the bar goes back.
- **Deep Seam** — extraction. Dig, collapse strata onto hazards, bring ore up.
- **The Refinery** — hop a pyramid of bars, each landing refining a face from
  ore to struck coin.
- **Network Run** — fly the chain, clearing what's in the way. The stage names
  are the release flow.
- **Bullion** — stack bars into a vault; a sealed row is assayed and clears.
- **Paper Fleet** — squadrons of paper claims fly in, wheel into formation and
  dive.

## Two fixed shooters — how they differ

Assay Line and Paper Fleet are both "ship at the bottom, things above". Built
naively they would be the same game twice. The originals solved this and the
*distinction* is mechanics, therefore not protected:

| | **Assay Line** | **Paper Fleet** |
|---|---|---|
| Enemies | A rigid block that steps sideways and drops a row | Fly in along curved paths, then hold formation |
| Threat | The wall descending on you | Individual divers peeling off |
| Tempo | Accelerates as the block thins out | Constant, with waves |
| Cover | Destructible shields you erode yourself | None — you dodge |
| The hook | Survive the descent | One flyer can capture your ship; shoot the captor and you fly as a double |
| Feels like | Pressure closing in | Dogfighting |

The capture-and-rescue hook is worth getting right: it is the only mechanic in
the list besides Passage's landing that turns a loss into a gain. Themed, a
claim seizes one of your bullion bars, and shooting it down returns the bar and
doubles your assay beam.

## A note on "Paper Fleet"

"Paper gold" is a standard industry term for claims on gold that are not
allocated bullion, and the contrast is genuinely part of what an ambassador
explains, so the name does real educational work.

The risk is that it reads as aimed at named competitors rather than at a
concept. My view is that it does not — it is a category term, the enemies are
abstract shapes, nothing names or depicts a company. But it is a naming
decision on a financial product's own app, so it belongs in the same counsel
review as the rest (§2.4 of `MEETING-BRIEF.md`). If counsel would rather avoid
it, **Squadron** or **Interception** cost nothing to swap in.

Nothing in this catalogue should frame a hazard as a person, a critic or a
competitor. Abstract shapes only.

## Why the scope split

Maze, lane-crossing, tunnelling and isometric games are **layout** games: the
design work is the level, and endless variants of them are weak. Shooters and
stackers are **pressure** games: the design work is the escalation curve, and
discrete levels get in the way. That means roughly 60 layouts across four
games, a quarter of what Coin Quest's 60 levels took, because these layouts are
far simpler than a calibrated match-3 board.

## Bullion — what "redesigned" means concretely

The Tetris ruling turned on the piece shapes with their colour, shading and
borders, the playfield dimensions, and how pieces behave. So:

- **Not the seven tetrominoes.** A six-piece set built from bar and ingot
  silhouettes, including at least one piece that is not four cells.
- **Not a 10×20 board.** Wider and shorter, sized to a vault shelf.
- **Different clear rule.** A row clears when it is *sealed* — complete and
  with no gap beneath it — which changes stacking strategy rather than being a
  cosmetic difference.
- **Own presentation** throughout: no ghost piece, no hold queue.

This is defensive design, not paranoia. It is the one genre where a
differently-named, independently-written clone has lost.

## Build order

1. ~~**Arcade cabinet**~~ — done.
2. ~~**One vertical slice**~~ — done, and Passage turned out to be a better
   first slice than Assay Line would have been: it is simpler, it exercised the
   whole cabinet end to end, and it forced the failure-model question early
   enough to apply the answer to the other nine.
3. **Next: Assay Line**, then in pairs sharing what they can — the two
   shooters together, the two layout-heavy ones together.

The XP, badge, streak and standings layer is what these plug into. No new
backend work beyond adding each game to the allow-list.

## The educational claim

With no quiz content in the ten, the app's "Educational only" footer rests on
the theming plus Coin Quest — **and now on Passage**, which carries nine
sourced historical facts and shows them on the landing screen. That is a
materially better answer to the Play content-rating and target-audience
questionnaires than the theming alone was.

Two cheap ways to firm it up further, both of which can wait:

- A one-line explainer on each game's start screen saying what the theme maps
  to. Passage already does this by construction.
- Bringing the question bank back as an opt-in mode rather than as
  interstitials, which is what you ruled out.
