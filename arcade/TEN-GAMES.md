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
| 1 | *(new)* | **When Pigs Fly** (was Passage; id `passage`) | One tap, fly a corridor, land it | 9 eras, finite | **Built** |
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

# 1. When Pigs Fly (was Passage) — built 2026-09-20, renamed 2026-09-24

A winged piggy bank flies a corridor through nine eras of monetary history.
One tap holds altitude. Every run ends with the pig on the ground. Until
2026-09-24 the player was a gold coin and the game was called Passage; the
game id is still `passage` everywhere below the title, so rounds, XP and the
leaderboard carry over. See "When Pigs Fly" below.

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
| Files | `lib/arcade/passage/{boar,eras,passage_game,passage_render,passage_screen}.dart`; sheet generator `tool/art/boar_sprites.py` |
| Server | `passage` added to the mini-game allow-list; XP `stars × 12`, plus 24 for a full passage, plus `min(12, score ÷ 50)` for coins. The passage bonus keys off stars, not eras reached — reaching 2009 is not flying through it |
| Min round | 4 s — the shortest legitimate run is a player who taps once and never again, which measures at ~5.3 s and is asserted in the test |
| Tests | `test/passage_test.dart` — layout reachability, gap floor, the star rule, that a player who stops tapping lands rather than dies, and the coin rules below |
| Art | The coins are the DGD coin renders Coin Quest ships (`coin_gold`, `coin_silver`, `coin_copper`). The boar is the owner's art, three sheets `boar_{piglet,juvenile,razorback}.png` imported by `tool/art/import_boars.py` (see "Final boar art"). The era skylines and gates are drawn in code. Nothing resembling any existing game's look |

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

## When Pigs Fly — decided 2026-09-24, phase 1 built the same day

The player becomes a flying piggy bank, styled as a wild boar that grows
across runs through three stages, with an upgrade shop between runs. The
title and the piggy bank were kept after the framing concerns below were
raised.

**Decisions taken (asked and answered):**

| Question | Answer |
|---|---|
| When does the boar grow? | Across runs, persistently |
| Grown by what? | Lifetime points earned, held apart from the spendable balance so spending never shrinks the boar |
| How are abilities unlocked? | A shop between runs, paid in points |
| Who draws the sprites? | Placeholders generated in code now; final art replaces the files |
| How are abilities fired? | Two on-screen ability buttons; a tap anywhere else is still a flap |
| Coin pause | A freeze shot: a spat coin stops a gate coin's drift for a few seconds (pillars do not move, so the drift is what freezes) |
| Grapple | Hooks the nearest gold coin and pulls the boar toward it |
| Fairness | Upgraded runs count for stars and scores; the XP cap is unchanged, so upgrades cannot farm XP |

**Framing concerns raised, and the owner's call.** A piggy bank that grows
by collecting DGD coins leans toward the store-of-value framing this plan
rejected for the inflation-dodging coin (see "The content, and what it
deliberately does not say"). The idiom "when pigs fly" beside a DGD coin can
also be read as a joke about price. Both were put to the owner, who kept the
title and the piggy bank. Mitigations held to regardless: the boar grows
from *flying* (lifetime points are a record of play, not a hoard), the shop
currency is called points and never coins or DGD, and no copy says bank,
balance, earn or invest. The coin slot on the boar's back is its one
piggy-bank tell.

**The three stages.**

| Stage | Look | Sheet frame | Drawn at |
|---|---|---|---|
| Piglet | Small and chunky: earthy brown with darker back stripes, golden-blond tufts, big shiny eyes, first tusks, stubby wings | 48 px | 5.6 hitbox radii |
| Juvenile | Filled out, bristly brown, head carried low; a tall dark crest turning gold at the tips, magenta eyes, proper tusks | 72 px | 6.6 |
| Razorback | Full size, head low: a burnished gold coat, a shaggy mane and crest dark at the roots and gold at the tips, two pairs of tusks, battle scars, a red eye, big bronze dragon wings | 108 px | 7.8 |

*Revised 2026-09-27 from three reference boars the owner supplied, one per
stage. The coat now goes brown → gold as the boar grows, where it was golden
throughout. The juvenile and razorback carry their heads low, charging. The
references are described in words in `WHEN-PIGS-FLY-ART-BRIEF.md` and are not
in the repository (other people's work); the placeholders were redrawn toward
them.*

**The hitbox does not grow.** The simulation still flies the coin's circle.
The razorback a player spent weeks growing must never be harder to fit
through a gap than the piglet; wings, crest and mane may overlap a pillar
harmlessly. The body is sized so its height is close to the hitbox's, with
the snout and rump overhanging it, which is forgiving rather than punishing.

**The sheet contract** (`boar.dart`). One PNG per stage, one row of eight
square frames facing right, the frame side being the image height:
0-3 wing cycle (up, mid, down, recovery), 4 hurt, 5 dash (reserved for phase
3), 6 landing, 7 standing. `BoarSpec` holds the three placement numbers per
stage: where the hitbox centre sits in the frame, the frame's on-screen size
in hitbox radii, and the hoof line of the standing frame. Final art replaces
the files and, if its proportions differ, those numbers; no other code
changes. The placeholders are authored at 1x by `tool/art/boar_sprites.py`
(shaded primitives, 4x4 ordered dither, selective outline) and exported at
4x nearest-neighbour; the game draws them unfiltered, so the pixels stay
pixels. A test fails if any sheet is missing or has the wrong frame count;
the renderer falls back to the old gold coin rather than draw a mis-cut
sheet.

**Animation.** The wings beat at 8 frames a second in flight, burst to 20
for a quarter-second on every tap so a flap is visibly a wingbeat, glide at
4 during a descent, and idle at 5 while the first banner is read. A strike
shows the hurt frame for 0.35 s. The body pitches with climb and fall at two
thirds of the coin's tilt, because a long body pitching hard reads as
tumbling. Near the ground the landing frame is held level and lifted so the
hooves never sink into the ground line; after touchdown the boar stands on
it. DEV menu: "Next boar stage" cycles the stage mid-run and keeps it for
the next run.

**Build order.**

1. **The boar replaces the coin** — built 2026-09-24: sheets, animation,
   fixed hitbox, title and home card, DEV stage switch.
2. **Persistent growth** — built 2026-09-24, see below. Ability levels and
   the loadout move to phase 4, where the shop needs them.
3. **Abilities in the run** — built 2026-09-24, see below.
4. **Shop and loadout** — built 2026-09-24, see below.
5. **Tuning and final art** — tooling and calibration built 2026-09-24,
   see below. Real tuning waits on real runs; final art waits on an artist.

**Not yet verified on a phone:** whether each stage reads at game size,
whether the overhang past the hitbox feels fair at the pillars, and whether
the razorback's wings crowd the late, narrow gaps visually.

### Phase 2, persistent growth — built 2026-09-24

**Server.** A `passage_profile` table holds `lifetime` (only ever rises;
decides the stage) and `points` (what the phase 4 shop will spend), kept apart
so spending can never shrink the boar. A claimed passage round adds its
clamped score to both, behind exactly the gate XP uses: an `ok` account,
inside the daily rewarded-round cap. Past the cap, or on the abuse ladder, a
flight is practice and grows nothing. The stage is computed on the server
from `config.passage.stages` and sent in every progress snapshot as a
`passage` block (lifetime, points, stage, where this stage began, the next
stage and where it begins); the claim also returns `passageCredited`. The app
draws whatever stage the server names, so thresholds change without an app
release. `DELETE /v1/me` now clears the profile too.

**Thresholds are provisional:** juvenile at 1,200 lifetime points,
razorback at 4,000 (see the phase 5 feel fixes; originally 1,500 and 6,000), from a guess of about four runs a day at about 150
points (two or three days, then about ten). The first pass was 4,000 and
18,000 (a week, then a month); the owner asked for faster growth the same
day. Both are environment-overridable
(`PASSAGE_JUVENILE_AT`, `PASSAGE_RAZORBACK_AT`) and are to be reset from
measured scores once real runs are on the server.

**App.** Runs start as the player's own stage (the DEV override still wins
when set). Under the hovering boar before the first tap: "PIGLET · 1,240 /
4,000 to juvenile", or "fully grown". The results sheet has a growth panel:
the standing boar, its stage and progress bar, and what this flight did —
"+120 toward juvenile", "Adding up the flight…" while the fire-and-forget
claim is out, "Today's growing flights are used up; this one was practice",
or "Offline: this flight did not count toward growth." On the claim that
crosses a line the panel turns amber: "Your boar grew into a juvenile. It
flies as a juvenile from your next run." Builds with no backend (the demo,
and the standard DEV APK) show no progress figures at all, since nothing
there can ever move them.

**Tests.** Server: a score reaches both totals and comes back on the claim;
another game's score grows nothing; full-score runs cross the juvenile line;
past the cap a run grows nothing; the last stage has no next; a restricted
account grows nothing; deletion clears the profile. App: stage ids map (and
an unknown one does not crash); a snapshot without the block leaves the boar
alone; a claim knows what it credited and whether it crossed a line; the
panel's five states.

**Verified on the Pixel** against a local server with thresholds of 15 and
60: the piglet's progress before and after a run, the grew-into-juvenile
panel, the next run flying as a juvenile, and its progress toward the
razorback. Screenshots in `v2/dist/shots/pigs-growth-*.png`.

### Phase 3, abilities in the run — built 2026-09-24

Five abilities, at most two per run, each on its own button in a bottom
corner. A tap anywhere else is still a flap. Until the shop exists nobody
owns one, so a normal run looks exactly as before; the DEV menu equips
preset pairs at a chosen level for testing. Numbers per level are in
`abilities.dart` and a test holds every level at least as good as the one
below it.

| Ability | What it does | Level 1 → 3 |
|---|---|---|
| Dash | Holds altitude, scrolls at 2.2× for 0.35 s, untouchable a little longer | cooldown 8 → 5 s, immunity 0.45 → 0.65 s |
| Grapple | A chain from the snout hooks the nearest gold coin ahead and hauls the boar to its height at 1.5× scroll; a flap lets go. Untouchable while the line is taut | reach 0.9 → 1.3 screens, cooldown 10 → 6 s |
| Blink | Moves the boar straight up or down to the middle of the next opening it has not entered. It never moves the boar along the passage | 1 → 3 charges a run |
| Freeze shot | Spits a coin at the next gold coin ahead; that coin stops drifting and resumes from where it stopped, not where it would have been | hold 3 → 5 s, cooldown 7 → 5 s |
| Tractor beam | Every coin within reach is drawn to the boar and taken | reach 0.20 → 0.30 screen heights, 3 → 5 s, cooldown 12 → 8 s |

**Rules the code keeps.** Nothing fires before the first tap, or in a
descent or a landing: no button changes an ending. No ability carries the boar
past a pillar it has not reached. A button with nothing to act on (no gold
coin in reach, no gate ahead) is dead rather than a wasted cooldown. Ability
immunity is kept apart from the post-strike grace, because that one makes the
boar blink and a dash should read as power, not as having been hit.

**Found on the phone.** The first grapple fired from above a gate hauled the
boar straight down through the top pillar and cost a strike. An ability must
never be what strikes you, so the boar is untouchable while the line is taut.
The line always ends at a coin inside an opening, and the cooldown limits it.

**Controls.** The cabinet gained a controls layer. Unlike the overlay it
takes touches, but only where a control is: empty space hit-tests through to
the play area, so a tap there is still the game's. A widget test holds this.
Buttons fire on touch-down like the flap, show a ring refilling over the
cooldown and the charges left, and are hidden while the run settles.

**Tests** (17): the numbers (every ability limited; levels never worse; at
most two); nothing fires before the first tap or in a descent; cooldowns hold;
a dead button costs nothing; dash holds altitude, speeds the scroll and
survives a pillar that strikes without it; grapple takes its coin, never drags
the boar into a pillar, and lets go on a flap; blink moves only vertically,
to the next opening, and counts its charges; freeze stops a coin and thaws
without a jump; tractor takes what is in reach and nothing far away; and the
controls layer takes its own taps while everywhere else still flaps.

**Verified on the Pixel** with all three DEV loadouts. Dash showed speed
lines and the dash pose; the grapple showed its chain; the freeze shot flew
and left its target ringed in ice; blink burst at both ends; the tractor ring
pulsed; charges and cooldown rings updated.

### Phase 4, shop and loadout — built 2026-09-24

**Flow.** The home card now opens the boar's front room rather than the game.
It shows the boar and its progress, the two buttons the next run will have
("Taking up: left button, right button"), the five abilities with their
level pips and next price, the points available, and a Fly button. After a
run, Done comes back here. With no server (the demo, the standard DEV APK),
the room shows only the boar and Fly.

**Prices** (points, levels 1 / 2 / 3), set in server config, so the app never
hard-codes one:

| Ability | L1 | L2 | L3 |
|---|---|---|---|
| Dash | 600 | 1,500 | 3,000 |
| Grapple | 800 | 1,800 | 3,500 |
| Blink | 1,200 | 2,500 | 5,000 |
| Freeze shot | 700 | 1,600 | 3,200 |
| Tractor beam | 900 | 2,000 | 4,000 |

They are set against the growth thresholds. A first ability arrives about
when the piglet becomes a juvenile, and a full set of level 3s takes weeks.
Blink costs most because it is the strongest.

**Server.** A `passage_abilities` table holds owned levels, and
`passage_profile` gains the loadout.
- **Upgrade:** `POST /v1/passage/abilities/:id/upgrade` pays from `points` and
  never from `lifetime`, so spending never shrinks the boar. The level read,
  the balance check and both writes run in one transaction with no await
  between them. Two taps landing together pay once, and a test fires them
  together.
- **Loadout:** `POST /v1/passage/loadout` takes at most two distinct owned
  abilities.
- **Claims:** a passage claim now carries `loadout: [{id, level}]`. A run that
  flew with an ability the player does not own, or above the level they own,
  pays nothing (no XP, no growth) and is flagged `loadoutRejected`. It is
  recorded rather than refused, so it cannot be quietly retried without the
  field. `mini_rounds.loadout` keeps what each run flew with, for review.
- **Deletion:** `DELETE /v1/me` clears owned abilities too. An unknown ability
  id, including `__proto__`, is a 404.

**App.** The snapshot's `passage` block now lists every ability as `{id,
level, maxLevel, nextCost}` plus the loadout. `ArcadeProgress.upgradeAbility`
and `setPassageLoadout` return null or a reason. A refusal still refreshes
the cache from the snapshot it carries, so a stale balance corrects itself.
- **First unlock:** goes straight into an empty slot.
- **Unaffordable:** a level shows its price but its button is disabled.
- **A third ability:** is refused on the spot ("Two at a time").
- **The run:** takes the player's own loadout at their owned levels. A DEV
  loadout still wins when set, and the server pays such a run nothing unless
  it happens to be owned.
- **Copy:** says Unlock and Level 2, never buy. It says points come only from
  flying and that using them never shrinks the boar.

**Tests.** Server:
- the shop lists every ability with its next price
- an upgrade pays from points only, until the top level
- concurrent upgrades pay once
- loadout validation (unowned, duplicate, three, not a list)
- a claim with an unowned or over-level ability pays nothing
- deletion clears abilities

App:
- the snapshot parses
- a run reports its loadout in the claim's shape
- the room lists every ability and enables only affordable ones
- only owned abilities can be taken up, and never a third
- the loadout shows as the two buttons
- no shop without a server

A test also caught the ability card's button row overflowing when text is
wide. It now wraps.

**Verified on the Pixel** against a local server with 2,400 points seeded.
- **The room:** read the server's shop.
- **Unlocking dash:** took points from 2,400 to 1,800 while the boar stayed
  at 2,400 / 6,000, and dash went into the left slot. Grapple went into the
  right.
- **The next run:** had both buttons.
- **The claimed round:** recorded `["dash","grapple"]`, was accepted as owned,
  and paid.
- **One fix:** the confirmation message sat over the Fly button for four
  seconds. It is now shorter and lifted clear.

### The piglet's drawn wingbeat — 2026-09-28

The owner drew the piglet's wingbeat as four frames on one 2×2 sheet: white
background, a "FRAME n" label over each, saved as JPEG. It replaces the
rigged wingbeat, where the wings were cut out and turned about the shoulder,
for the piglet only.

- **`tool/art/split_frames.py`** splits the sheet in four steps:
  1. It cuts the cells at the blank gutters.
  2. It erases each label. The letters are neutral grey and the art's
     outlines are tinted, so the colour difference finds the letters.
     Erasing is kept to the label's own box, because the first version also
     took the pale tip off frame 1's far wing, which reaches up beside its
     label.
  3. It flood-fills the white out from the edges, then trims the JPEG
     fringe.
  4. It registers each frame on the body so the pig does not jitter as the
     frames cycle.

  The sheet and the four split frames are kept in `tool/art/source/`.
- **`import_boars.py`** uses a stage's drawn frames whenever
  `boar_{stage}_cycle_1..4.png` exist:
  - All four frames are cropped to one shared box, so the body stays where
    it was drawn.
  - The drawings, in order, are the cycle: up, level, down, folding in.
  - Hurt is the level frame tinted red.
  - Dash is the folded frame stretched.
  - Landing is the wings-up frame.
  - Standing is the folded frame.
- **BoarSpec:** the body landed within 3px of the old piglet art, so the size
  and anchors stand. The foot line moved from 0.833 to 0.824, because
  standing is now the folded drawing.
- **Verified on the Pixel:** a DEV flight as the piglet was recorded and
  stepped through. It cycles the four drawings with the body steady. The
  juvenile and razorback sheets came out unchanged.

### The juvenile's drawn wingbeat — 2026-09-28

The owner sent the juvenile's wingbeat in the same form, labelled "rest/high,
downstroke, low/compact, upstroke". Only the razorback still has the rig.
Three differences from the piglet's sheet needed changes to the splitter:

- **Labels under the art.** The splitter now clears, across the whole sheet
  and before cutting, any strip of rows that holds only grey text. Otherwise
  a label between two rows of art passes for part of the gap between cells.
  The piglet-style box erase still runs for labels above the art. It stays
  off for this sheet: its wing tops hold hundreds of dark grey outline
  pixels that it would take for letters.
- **A closed gap in the tail's curl.** The flood fill can't reach that white.
  `--holes` clears every patch of background, and is only for art with no
  white of its own. The piglet's white feathers have pockets of the same
  colour and size.
- **A compact frame with tucked legs.** Its body centroid registered it 38px
  too high, so the boar lurched every wingbeat. The centroid is now only a
  first guess. It is refined by matching the head, the front of the lower
  body that a wingbeat does not move, against frame 1.

  The piglet was re-split with the same fixes. Its registration moved by a
  pixel or two, and its foot line is now 0.828. Its frames 3 and 4 get back
  the outline along the top of the far wing, which the old box erase had
  cut off: that wing sits just under the middle label.

The dust puff in the downstroke frame is dropped by the importer as a
detached speck. Hurt, dash, landing and standing are built as for the
piglet, except that the folded drawing is per stage (`DRAWN_FOLDED`): the
compact third frame for the juvenile, because its fourth is wings-up again.
The juvenile's body matched the old art to the pixel, 173px wide in the
standing frame, so its BoarSpec is unchanged. Verified on the Pixel: a DEV
flight as the juvenile cycles all four drawings with the head steady.

### The piglet's drawn hurt — 2026-09-28

The first drawn pose is the piglet's hurt: a flinch with a squint, gritted
teeth, and dust flying. It came as a single close-up, about four times the
wingbeat's size, with no label. It is kept as
`tool/art/source/boar_piglet_hurt_drawn.jpg` and went in with:

    python tool/art/split_frames.py tool/art/source/boar_piglet_hurt_drawn.jpg tool/art/source/boar_piglet \
        --frames 1 --ref tool/art/source/boar_piglet_cycle_1.png --names hurt

It needed two fixes:

- **Scale.** The size search covered 0.8× to 1.2× only. It now searches
  round a first estimate from how much art there is (the square root of the
  opaque-area ratio), so any size is found. This one came out at 0.245. An
  onion skin over the flying frames shows the snout, body, hooves and tail
  in place.
- **A false "cut off" warning, and thinned edges.** The importer pasted each
  drawing with its own alpha as the mask. That squares a partial alpha, so
  the soft edges of a pose scaled to fit came out thinner, and the cut-off
  check counted them as lost. Drawings are now cropped straight into the
  frame square, and cut-off pixels are counted by position. The sheets from
  solid drawings are byte-identical to before.

The dust specks around the flinch are detached, so the importer drops them
like sparkles. The drawn hurt has no red tint; the strike's red screen wash
still shows. Verified on the Pixel: the piglet flown into a pillar shows the
flinch for the hurt window, in place, with no jump from the flying frames.
Still made from the wingbeat for the piglet: dash, land and stand.

### The piglet's drawn dash — 2026-09-28

The second drawn pose is the piglet's dash: wings swept back, speed streaks,
and a dust wake trailing from the hooves. It came as a close-up like the
hurt one, is kept as `boar_piglet_dash_drawn.jpg`, and went in the same way
(`--names dash`) at scale 0.244. It lines up with the flying frames on the
snout, eye and ear.

**One fix.** Between the belly and the dust wake is a gap of white, the sky
through the dust. The dust closes it off, so the flood fill left it as a
solid white patch. `--holes` would clear it, but would also punch out the
pockets of white in the piglet's feathers. Instead, `knock_out` now clears
by default any enclosed white that is:
- **edged with warm colour** (fur, dust): at least a quarter of its rim.
  Every feather pocket is edged in lavender, with at most 8% of its rim
  warm. The dash gap's rim is about half warm.
- **big**: at least 0.5% of the boar. The gap is about 2%. The first
  version had no size test and punched out the white highlight on top of
  the snout (0.04%), which is edged by fur too.

The size is a share rather than pixels, because a close-up is knocked out at
full size. With the rule in place, the piglet's wingbeat and hurt re-split
byte-identical. The juvenile and razorback use `--holes`, which this doesn't
change.

The dust wake is kept, as the owner drew it. Still made from the wingbeat
for the piglet: land and stand.

**Verified on the Pixel (dash):** the piglet dashed and the game was paused
within the dash window. It shows the drawn pose with its dust wake, the sky through
the gap and no white patch, alongside the game's own speed streaks. (The
first install attempt failed because the Pixel had dropped off adb; the
check was redone once it was plugged back in.)

### 1873, drawn — 2026-09-29

The owner's second era, from the full-era prompts:
- **Mid:** red-brick blocks with mansard roofs and cornices, a grey
  commercial block, and a brick church with a bell tower.
- **Far:** steeples and a bell tower behind.
- **Near:** roofs with telegraph poles and sagging wires.
- **Sky:** a purple haze under a dark top.
- **Columns:** green cast iron.
- **Ground:** brick with an iron rail.

It imported with no changes to the importer and no magenta left.

**Notes on the art:**
- **The mid ignored "the lower 65%".** Its buildings fill the image, so
  they reach the top of the mid band. Nothing breaks, but there's no sky
  showing above that layer.
- **The shaft looks bamboo-like.** Its drawing bunches three raised bands in
  the middle, so repeated, they come every 1.5 column widths. A redo with a
  plain shaft and at most one band would read better.
- **The ground's join is mildly off** (a step of 16 across the seam against
  the art's usual 9); against the rails it hardly shows.
- **The sky steps down in a coarse checkerboard dither.** It also shows as a
  pinkish checker between the far buildings. That's the sky's purple, not
  leftover magenta (0 strongly magenta pixels).

**Verified on the Pixel:** DEV "Next era" into 1873. The columns read
clearly against the brick, the coins stand out, and the layers are in
parallax. Two eras are drawn: 14 images, 3.8 MB.

### Full-era prompts, and 1816 redone — 2026-09-29

**The prompts:**
- **Written out in full:** every era's seven prompts, with no placeholders,
  are generated by `tool/art/backdrop_prompts.py` into
  `BACKDROP-PROMPTS.md`. A private claude.ai page has era tabs, a copy
  button per prompt, and Done ticks kept on the device.
- **What they carry from the first 1816 set:**
  - Each skyline asks for one layer only, in night colours, with magenta in
    every gap.
  - The moon is placed 20–35% down; smoggy and hazy eras have none.
  - The shaft must match the capital just before it.
  - Every prompt rules out text, people and landmarks.
- **The monetary events are left out of the prompts:** gold-standard
  language invites gold into the image.

**The importer no longer needs hand-cropping.** It trims:
- a skyline's clear sky above its tallest building, but for a 6% margin;
- the ground's blank white rows off its top as well as its plain bottom.
  The redo came with a white band across its top 14%, which would have
  been the ground line.

When two files exist for one piece, it uses the newer and says so.

**Magenta edges, fixed properly.** The redo still showed a faint lilac line
round every skyline on the phone. The unmixing measured each pixel's
magenta against zero, but 1816's blues sit at a cast of −16. That
underestimated how much of an edge pixel was background, and the error grew
as the pixel was unmixed toward its colour. Now:
- a pixel is touched only above the art's own 98th-percentile cast (+4);
- its share is measured from the art's median cast.

Edge pixels now match the art (far: edges (62, 77, 106) against the body's
(45, 62, 87), where they were (73, 73, 115)), and a mauve era keeps its
purples.

**1816, redone by the owner:**
- The moon shows, a quarter of the way down.
- The capital and shaft are one cool grey.
- Three London depths: the far layer has a dome and spires, the mid layer
  terraces and a clock tower, and the near layer chimney pots and bare
  trees.
- Cobbles for the ground.

**One flaw in the art:** the sky has a hard edge about 17% down, where
Nano Banana drew "keep the top 15% plain" as a separate band. The sky
prompt now asks for a smooth sky with no band, and there's a fix-up reply
for it.

**Verified on the Pixel:** 1816 in flight: moon, stone columns, three
layers in parallax, coins reading clearly in front. Analyze and the 148
tests pass. The old 1816 set's `.webp` sources were replaced by the redo's
`.jpg`.

### 1816 London, drawn — 2026-09-29

The first real backdrop set: sky, far, mid and near skylines, ground, and
capital and shaft, all made by the owner with Nano Banana from the prompts
in the brief. They're kept as `tool/art/source/backdrop/1816_*.webp`.

**Earlier attempts.** The first try at the far skyline drew three depths in
one image, filled the gaps with pale beige haze, and had mismatched ends.
The "only this one layer" and "night colours" lines were added to the
skyline prompts because of it. The second set came back one layer each,
dark, and tiling cleanly: every seam is smaller than the art's own steps.

**What the importer needed** to take Nano Banana's output as it comes:
- **Column parts trimmed to the art's width.** Trimmed by column coverage,
  so a stray edge speck doesn't count.
- **Shaft set to the capital's neck.** The shaft fills its image, but under
  the capital the column is only 61–65% of the capital's width. Scaled as
  it came, the shaft would have been as wide as the capital's top.
- **Ground's plain bottom trimmed.** The image wasn't cropped, and the
  cobbles were its top 34%. The rest is dropped; the game fills below with
  its own dark.
- **No magenta fringes.** The first import drew a bright pink line round
  every roof and branch. Two causes:
  - **Resizing:** the cleared background kept its magenta colour under zero
    alpha, and resizing blended it back in. The importer now clears that
    colour and resizes premultiplied (`resize_rgba`).
  - **Isolated slivers:** magenta cut off between chimney pots and in
    branch crooks was never reached by the fill. Every pixel is now
    unmixed: its magenta share (red and blue above green) moves from its
    colour into its transparency. The 1816 palette's purples barely
    register.

  After the fix, the composed preview has 0 pixels with a strong magenta
  cast, down from about 27,000.
- **White backgrounds keep the plain cut:** white can't be told from light
  stone the same way.

**Notes on the art itself:**
- **The moon is hidden.** It sits 77% of the way down the sky, behind the
  skyline. A regenerate with the moon about a quarter of the way down would
  show it.
- **The column's two parts differ in tone:** the capital is cool
  grey-white, the shaft warm beige. In the preview they read as one column.
- **Most of the far layer is hidden,** covered by the mid layer. Its front
  row of brown houses with lit windows shows between gaps.

**Not yet seen on the phone:** the Pixel dropped off adb before the
install. Analyze and the 148 tests pass, and the build is in `dist/`.

### Drawn backdrops: the brief and the importer — 2026-09-28

The boars are the owner's pixel art; the skies, cities, columns and ground
are still flat shapes drawn in code. The next art is those, so the path for
it is built first, as it was for the poses.

**The brief:** `tool/art/BACKDROP-BRIEF.md`. It covers:
- **The pieces, per era:** sky, three skyline strips (far, mid, near),
  ground, and a column capital and shaft. All optional, one era or one
  piece at a time.
- **Size:** each piece's height as a share of the screen, with the shape to
  draw at the 1080×2424 reference.
- **Rules:**
  - Tiling: strips and ground join left to right; the shaft joins end to end.
  - Transparency: real transparency, or pure white or magenta.
  - Readability: dark, low-contrast sky; no gold or round shapes up high;
    columns lighter than the city; no amber at the gap.
  - The top 12% sits under the HUD, and only the top of the ground shows.
  - Evocative, not portraits.
- **Each era as the code draws it today**, as a starting point.

**The importer:** `tool/art/import_backdrops.py`. It reads
`tool/art/source/backdrop/{year}_{part}.png|jpg|webp` and:
1. **Clears the background** of the pieces that need it: pure white or
   magenta, whichever lines more of the border, including gaps between
   buildings, with the JPEG fringe.
2. **Sizes each piece by its height to its band.** Strips are stored at half
   the reference pixels; column parts at the column's 92px. Repeating parts
   are resized with a wrapped margin, so resampling adds no seam.
3. **Checks each join.** The step across the seam is compared with the 99.5th
   percentile of the art's own neighbour steps. A building edge or grid
   line at the seam passes; a real mismatch warns.
4. **Writes `assets/images/backdrop/`** and `manifest.json`, with band, base
   and parallax per piece. Per-era changes go in `tuning.json`.
5. **With `--preview`**, composes each era at landing: sky to ground, with a
   column pair.

**In the game:** `lib/arcade/passage/backdrop.dart`.
- **Where a piece is drawn:** the sky covers the code-drawn one, and the
  drift lines fade with it. The far strip sits behind the code-drawn city,
  mid and near in front, tiled with parallax. The ground strip hangs from
  the ground line under the amber edge. Columns are the capital at the gap,
  flipped for hanging ones, with the shaft repeated away from it; the amber
  lip stays.
- **Replacing the code-drawn city:** an era with a drawn skyline hides its
  code-drawn buildings (`CityScape.render(hide:)`). Anything not drawn stays
  code-drawn.
- **Crossfade:** eras change over a third of a screen either side
  (`eraWeights`, smoothstep).
- **Memory:** only the flown era and its neighbours are loaded; a full set
  is too much texture.
- **Gates:** gates drawn before their columns' art arrived are redrawn.
- **Empty manifest:** with nothing listed, the game is unchanged.

**Tested:**
- **Unit tests:** `test/backdrop_test.dart` covers manifest parsing
  (unknown years and parts skipped), the empty case, and the crossfade
  (weights sum to one, half each at the change, monotonic, clamped). 148
  tests pass.
- **Stand-in art:** an obvious pixelated 1816 set (sky with stars and
  crescent, three strips, capital and shaft) and a 2009 ground grid,
  across all three input kinds (PNG with transparency, white JPEG, magenta
  PNG). Two importer bugs surfaced and were fixed:
  - **Wrong background colour:** the commonest-border-colour rule picked
    the buildings on the far strip and the stone on the capital, so white
    and magenta are now named outright.
  - **False seam warnings:** a first-versus-last-column comparison flagged
    ordinary building edges; the percentile test replaced it. Deliberately
    broken tiles still flag.
- **On the Pixel with the stand-ins:** the sky, three layers in parallax
  and drawn columns all rendered, and the ground grid showed at touchdown.
  The moon sat under the HUD, which is how the brief's 12% rule came about.
- **Stand-ins removed:** the manifest shipped is empty, and on the Pixel
  1816 looks as before.

### The razorback's drawn stand: bucking — every frame is drawn — 2026-09-28

The razorback's stand is the buck the owner described: weight on the
forelegs, hind legs kicked up behind, wings folded, and the same fierce face
as in flight. It came at half the close-ups' width (1024 against 2000). It
is kept as `boar_razorback_stand_drawn.jpg` and went in with:

    python tool/art/split_frames.py tool/art/source/boar_razorback_stand_drawn.jpg tool/art/source/boar_razorback \
        --frames 1 --ref tool/art/source/boar_razorback_cycle_1.png --names stand --holes \
        --floor tool/art/source/boar_razorback_cycle_4.png

**Placement:**
- **Size:** the face is the flying face, so the head match sized it unaided,
  at 0.736. That is twice the close-ups' 0.375, as the half-width image
  predicts.
- **Floor:** the front hooves are its lowest point, on the same hoof line as
  the landing.

footV is unchanged at 0.77.

**The owner has now drawn every frame in the game:** three wingbeats (4, 4
and 6 drawings) and all three stages' hurt, dash, land and stand. Nothing
is made from other frames any more. The rig, tint and stretch code stays in
`import_boars.py` for new art that comes as a single pose.

**Verified on the Pixel:**
- **Front room:** the card shows the buck.
- **Touchdown:** DEV "Skip to the landing", recorded. It lands wings-spread,
  then drops into the buck on the same ground line, with no jump.

### The razorback's drawn landing — 2026-09-28

Wings raised and spread wide, forelegs reaching down, the same fierce face
as in flight. It is kept as `boar_razorback_land_drawn.jpg` and went in
with:

    python tool/art/split_frames.py tool/art/source/boar_razorback_land_drawn.jpg tool/art/source/boar_razorback \
        --frames 1 --ref tool/art/source/boar_razorback_cycle_1.png --names land --holes \
        --floor tool/art/source/boar_razorback_cycle_4.png

**Placement:**
- **Size:** 0.375 by head match, beside the hurt's 0.380 and the dash's
  0.375.
- **Floor:** on the hoof line of `cycle_4`, the "fully down and folding"
  drawing that is the razorback's stand for now. A drawn stand should be
  floored on the same line.
- **Nothing cut off:** the wing tips reach the drawing's top corners but fit
  the frame.

footV is unchanged at 0.77. Verified on the Pixel: DEV "Skip to the
landing", recorded. It comes in wings-spread, touches down on the ground
line, then folds into the stand, with no jump. Still made from the wingbeat
for the razorback: stand. The owner's note: it will buck forward.

### The razorback's drawn dash — 2026-09-28

Teeth gritted, wings swept flat back, gold speed streaks trailing. It is
kept as `boar_razorback_dash_drawn.jpg` and went in like the hurt
(`--names dash --holes`) at 0.375, beside the hurt's 0.380. The tusks and
snout sit on the flying frame's. The streaks joined to the body and wings
stay; the loose ones drop out. Verified on the Pixel: dashed and paused
within the dash window, it shows the charge alongside the game's speed
streaks. Still made from the wingbeat for the razorback: land and stand.

### The razorback's drawn hurt — 2026-09-28

Eyes squeezed shut, tears, red impact slashes across the flank, and loose
scales flying. It is kept as `boar_razorback_hurt_drawn.jpg` and went in
like the others (`--names hurt --holes`, ref `boar_razorback_cycle_1.png`).
Size by head match, 0.380. The head, tusks and body sit on the flying
frame's.

The red slashes are drawn onto the body, so they stay. The loose X marks
and scales drop out like sparkles. Verified on the Pixel: after a strike,
the razorback shows the hurt pose for the hurt window, in place, then
returns to its wingbeat. Still made from the wingbeat for the razorback:
dash, land and stand. The owner's note: its stand will buck forward.

### The juvenile's drawn stand: rearing — the juvenile is fully drawn — 2026-09-28

The owner gave the juvenile a bolder stand than the piglet's: rearing on its
hind legs, forelegs up, wings spread high and snout to the sky. It is kept as
`boar_juvenile_stand_drawn.jpg`. The owner's note for the razorback is that
its stand will buck forward instead.

It went in with:

    python tool/art/split_frames.py tool/art/source/boar_juvenile_stand_drawn.jpg tool/art/source/boar_juvenile \
        --frames 1 --ref tool/art/source/boar_juvenile_cycle_1.png --names stand --holes \
        --shadow --scale 0.262 --floor tool/art/source/boar_juvenile_cycle_3.png --center

Two new splitter options:

- **`--shadow`** erases a ground shadow drawn under the hooves. This one is a
  flat ellipse, (127, 96, 104) with no variation, joined to the hooves, so
  it would have come in as part of the boar and been stood on the ground in
  place of the hooves. The splitter takes the commonest colour along the
  bottom of the art and whitens it, with its blend into the white, from the
  shadow's top row down. The first version left the shadow's slightly
  darker rim, (112, 96, 99), as a line under the hooves, and the floor stood
  that on the ground, 9px low. The test now reaches a little past the
  shadow colour (t up to 1.15). The hooves are far darker (t 1.3 and more),
  so they stay.
- **`--center`** (with `--floor` and `--scale`) places the pose across by its
  centre of mass over the floor frame's, not by the head, and keeps it
  facing as drawn. With the snout pointing up, there is no head to match.
  The size, 0.262, is the juvenile close-ups' (hurt 0.260, dash and
  landing 0.263), since this image has the same width.

The stand is floored on the same line as the landing. footV reads 0.779
against 0.782, so it is left. **The juvenile is fully drawn** by the owner:
wingbeat, hurt, dash, land and stand.

**Verified on the Pixel:**
- **Front room:** the card shows the rearing stand with its wings whole
  inside the portrait crop.
- **Touchdown:** DEV "Skip to the landing", recorded. It comes in
  wings-high, touches down, then rears up on the ground line, with no jump.

### The juvenile's drawn landing — 2026-09-28

Wings raised high, forelegs reaching down, a weary look and a sweat drop.
It is kept as `boar_juvenile_land_drawn.jpg` and went in with:

    python tool/art/split_frames.py tool/art/source/boar_juvenile_land_drawn.jpg tool/art/source/boar_juvenile \
        --frames 1 --ref tool/art/source/boar_juvenile_cycle_1.png --names land --holes \
        --floor tool/art/source/boar_juvenile_cycle_3.png

**Placement:**
- **Size:** the head match found 0.263 unaided, the same as the hurt
  (0.260) and dash (0.263), so no `--scale` was needed. The head is weary
  but not drooped the way the piglet's was.
- **Floor:** `cycle_3` is the compact drawing, the juvenile's standing frame
  for now. A drawn stand should be floored on the same line.

footV is unchanged (the checker reads 0.781 against 0.782). Verified on the
Pixel: DEV "Skip to the landing", recorded. It comes in wings-high and
touches down on the ground line, then settles into the stand. Still made
from the wingbeat for the juvenile: stand.

### The juvenile's drawn dash — 2026-09-28

The owner's "adult boar dash": golden wings swept flat back, head down in a
charge, speed streaks trailing. It is kept as
`boar_juvenile_dash_drawn.jpg` and went in like the hurt (`--names dash
--holes`) at 0.263. The tusks, snout and eye sit on the flying frame's. The
streaks joined to the wings and body stay; the loose ones drop like
sparkles. Verified on the Pixel: dashed and paused within the dash window,
it shows the charge alongside the game's speed streaks. Still made from the
wingbeat for the juvenile: land and stand.

### The juvenile's drawn hurt — 2026-09-28

The owner's "adult boar hurt": a tumble, body curled and rotated about 30°,
eyes squeezed shut, red impact marks, and loose feathers flying. The golden
feathered wings make it the juvenile's. The razorback's wings are membrane.
It is kept as `boar_juvenile_hurt_drawn.jpg` and went in with:

    python tool/art/split_frames.py tool/art/source/boar_juvenile_hurt_drawn.jpg tool/art/source/boar_juvenile \
        --frames 1 --ref tool/art/source/boar_juvenile_cycle_1.png --names hurt --holes

The rotated body was a worry for the head match, but it placed well:
- **Size:** 0.260, the same size as the wingbeat.
- **Head:** the tusks and snout sit on the flying frame's.
- **Body:** its centre of mass is within 13px of the flying frame's, so the
  curl tumbles about the same point.

The impact marks and feathers are detached, so the importer drops them like
sparkles. Verified on the Pixel: after a strike, the juvenile shows the
tumble for the hurt window, in place, then returns to its wingbeat. Still
made from the wingbeat for the juvenile: dash, land and stand.

### The piglet's drawn stand: the piglet is fully drawn — 2026-09-28

The last pose is the piglet standing, wings folded flat along its back, with
the same smile as in flight. It came at a different zoom from the close-ups
(the image is about half their width). It is kept as
`boar_piglet_stand_drawn.jpg` and went in with:

    python tool/art/split_frames.py tool/art/source/boar_piglet_stand_drawn.jpg tool/art/source/boar_piglet \
        --frames 1 --ref tool/art/source/boar_piglet_cycle_1.png --names stand \
        --floor tool/art/source/boar_piglet_cycle_4.png

**How it was placed:**
- **Size by head match.** The face is the flying face, so the match sized it
  unaided, at 0.482. An onion skin over the flying frame lines up the head
  and body.
- **Floored on the same hoof line as the landing,** so the two share a
  ground and the landing needs no re-split.

**Foot line.** The checker measures the stand's hooves at 0.821, against the
0.828 in boar.dart. A pose scaled by about half has softer hoof tips, which
the checker's alpha > 32 reads a few pixels higher. Left alone, the standing
piglet would have sunk about 3px, so footV is now 0.821.

**The piglet is fully drawn** by the owner: four wingbeat drawings, hurt,
dash, land and stand. Nothing in its sheet is made from other frames any
more. The front-room card and the growing-up moment show the drawn stand.

**Verified on the Pixel:**
- **Front room:** the card shows the drawn stand.
- **Touchdown**, recorded with DEV "Skip to the landing": flying, then the
  teary flop on the ground line, then the stand. All on one line, with no
  jump.

### The piglet's drawn landing — 2026-09-28

The third drawn pose is the piglet's landing: flopped on its belly with its
legs tucked and head drooped, a tear, a sweat drop, and two feathers coming
loose. It is kept as `boar_piglet_land_drawn.jpg`.

**Placing a grounded pose.** The head match alone got it wrong: the drooped,
turned head read as a bigger boar. It came out at scale 0.290 against 0.245
for the hurt and dash, visibly too big and hovering above the hoof line.
Two new `--ref` options fix it:
- **`--scale`** fixes the size. The owner's close-ups are drawn at one zoom,
  so the hurt and dash's 0.245 is used. The snouts measure within 7% across
  the three, the landing's being narrowed by the turn.
- **`--floor FRAME`** puts the drawing's lowest row on that frame's lowest
  row. The game stands the landing frame's hoof line (footV, measured on the
  standing frame) on the ground, so a grounded pose is placed by the ground,
  not by a head that droops. The horizontal position still comes from the
  head match.

The command used:

    python tool/art/split_frames.py tool/art/source/boar_piglet_land_drawn.jpg tool/art/source/boar_piglet \
        --frames 1 --ref tool/art/source/boar_piglet_cycle_1.png --names land \
        --scale 0.245 --floor tool/art/source/boar_piglet_cycle_4.png

`cycle_4` is the folded drawing, which was also the piglet's standing frame
at the time. The drawn stand that followed was floored on the same line, so
the two share a ground.

**The falling feathers** are detached from the boar, so the importer drops
them like sparkles. Keeping them would need an exception in
`main_component`.

**Shown on every touchdown.** The pose shows on the approach and for the
first quarter-second after touchdown, then the stand. That includes a
triumphant full passage ("You flew the whole passage"), so the tearful
flop plays after a win too. That's the owner's call.

**Verified on the Pixel:** DEV "Skip to the landing", recorded. The flop
touches down on the ground line, neither hovering nor sunk, then gives way
to the standing pose. Still made from the wingbeat for the piglet: stand.

### Pose sheets: the importer is ready — 2026-09-28

The four frames after the wingbeat (hurt, dash, land, stand) are still made
from the wingbeat drawings:
- **Hurt:** a wing frame tinted red.
- **Dash:** the folded frame stretched sideways.
- **Land:** the wings-up frame.
- **Stand:** the folded frame.

The tools now take drawn ones, so the owner's drawings drop in.

**What to draw.** One sheet per stage, in the same form as the wingbeat
sheets: white background, labels anywhere, any grid, facing either way. Four
poses in reading order:
1. **Hurt:** a flinch, struck.
2. **Dash:** wings swept back, stretched for speed.
3. **Land:** braking just above the ground, legs reaching down, wings
   raised.
4. **Stand:** on the ground, wings folded. This is the pose on the
   front-room card and in the growing-up moment.

Drawing it at the same size as the wingbeat helps, but isn't required. A
sheet of only some poses works too.

**How it goes in.**

    python tool/art/split_frames.py poses.jpg tool/art/source/boar_juvenile \
        --ref tool/art/source/boar_juvenile_cycle_1.png --names hurt,dash,land,stand --holes

This writes `boar_juvenile_hurt.png` and the rest. `import_boars.py` uses
each drawn pose in place of the made one, and reports which are drawn and
which are still made.

- **`--ref` registers the poses to the stage's wingbeat,** not to each other,
  so the boar doesn't jump when it switches to a pose. Each pose is tried at
  sizes from 0.8× to 1.2× and both ways round, matched on the head. The
  sheet is then drawn at the median of those sizes, since a sheet is drawn
  at one size. Frame by frame, one test frame came out 2% off.
- **The poses take the wingbeat's crop and scale** and don't widen it, so the
  placement numbers in boar.dart stay right. A pose that reaches past the
  frame's margin is reported as cut off. A drawn stand moves the foot line,
  so check_sheets.py runs again after it.

**Tested with stand-in poses** (the juvenile's own wingbeat sheet fed back
in as a pose sheet):
- **Same size:** every pose landed exactly on its wingbeat frame (IoU 1.000,
  zero offset).
- **Shrunk to 85% and re-saved as JPEG:** the scale was recovered as 1.175
  against a true 1.176, within 2px.
- **Imported end to end:** each stand-in pose sat within a pixel of its
  wingbeat frame in the finished sheet (IoU 0.98).
- **With no pose files:** all three sheets rebuild byte-identical.

The stand-ins were removed afterwards.

### Wingbeat timing to fit the drawings — 2026-09-28

The wing cycle used to run at a frame rate: 8 drawings a second while
gliding, and 20 a second for 0.28 s after a tap. Every drawing held equally
long, and a tap's beat lasted a fifth of a second (a tenth of a second on
top for the razorback's six). The drawn beats flickered past instead of
reading as a stroke. Now:

- **Holds per drawing** (`BoarFrames.holds`, relative). The extremes hold
  longer and the in-betweens pass quickly.

  | Stage     | Drawings                                                        | Holds                        |
  |-----------|-----------------------------------------------------------------|------------------------------|
  | Piglet    | up, level, down, folding in                                     | 1.3, 0.8, 1.2, 0.7           |
  | Juvenile  | high, downstroke, compact, upstroke                             | 1.3, 0.7, 1.3, 0.7           |
  | Razorback | spread, mid-down, full cup, folding, mid-up, re-lifting         | 1.4, 0.7, 1.1, 1.1, 0.8, 0.9 |

- **Beat tempo per stage, in seconds per beat** (`BoarSpec.flapBeat` /
  `glideBeat`). A tap starts a fresh beat from wings up and plays it at the
  flap tempo, then the glide beat carries on. Before the start the beat is
  1.4× the glide; on the way down it's 1.6×.

  | Stage     | Flap | Glide |
  |-----------|------|-------|
  | Piglet    | 0.30 | 0.50  |
  | Juvenile  | 0.36 | 0.62  |
  | Razorback | 0.44 | 0.78  |

  Bigger boars beat slower, so their size shows in the motion. The piglet's
  glide is the old half-second beat. `_wingPhase` now counts beats, not
  frames. The drawing shown comes from how far through the beat it is.
- **Test:** checks that every stage shows every drawing in order, holds
  wings-up longer than the next drawing, taps faster than it glides, and
  beats slower as it grows.
- **Verified on the Pixel:** the razorback was recorded and stepped through
  at 15 fps. In the pre-start hover each drawing holds for several samples.
  After a tap, spread, mid-down, cup, fold and re-lift all show within the
  0.44 s beat.

These are first numbers, chosen on principle and checked on video. How the
beat feels in the hand is the owner's call, and every number above is one
line in `boar.dart`.

### The razorback's drawn wingbeat, in six — 2026-09-28

The owner's razorback sheet has six drawings, in a 3×2 grid with two-line
labels underneath:

1. high up and spread
2. mid-downward stroke
3. low-down stroke, a full cup
4. fully down and folding
5. mid-upward stroke
6. re-lifting

With this sheet, no stage uses the wing rig any more. It stays in the
importer for new art that arrives as a single pose.

**Splitting by shape, not by grid.** Frame 1's right wing crosses into frame
2's columns, so there is no gutter to cut at. The frames of the second row
also face right, where the first row faces left. `split_frames.py` now works
for any sheet this way:
- Label strips are cleared first. A label strip can be up to 160 rows, since
  a two-line label can run together.
- The N largest shapes on the sheet are the boars (`--frames N`, default 4).
  A smaller shape goes to the nearest boar, unless it is grey. Grey is a
  label, or the juvenile's dust puff, and is dropped.
- Grey letters that join a boar only on the shrunk copy are removed at full
  size.
- `--holes` now leaves enclosed pockets smaller than 30 pixels (a
  highlight).
- Every frame is tried both ways round and kept the way its head matches
  frame 1's. Frames 4–6 came out turned round, as they should.
- Registration is by the head, as before, starting from the centroid of the
  lower half of the art.

The piglet and juvenile came through the new path within a few pixels of
before. One real difference: the piglet's frame 1 was committed with the tip
of its far wing as a broken ghost, left by the old label erase. It is whole
now, and the "FRAME 1" letters beside it are gone. The earlier note's "the
wing tip survives" was wrong.

**A cycle length per stage.** `BoarFrame`, with its fixed indices, became
`BoarFrames(cycleLength)` on each `BoarSpec`. A sheet is the cycle and then
hurt, dash, land and stand, so the razorback's `BoarFrames(6)` sheet has 10
frames:
- The flap resets to wings-up whatever the length.
- The wing rate scales with the length, so every stage beats its wings in the
  same time.
- `BoarPortrait` finds the standing frame from the spec.
- `check_sheets.py` reads the length out of boar.dart.
- A new test flies the razorback and checks all six drawings show and no
  frame index runs past its sheet.

**Placement.** Frame 1 is the drawing the old razorback art was made from:
its body band measures 180px against the old 182. The size and anchors stand.
Standing is now the "fully down and folding" drawing, so footV moves from
0.756 to 0.77. The home card, built from the razorback's first frame, is the
same wings-spread drawing.

**Verified on the Pixel:** a DEV flight as the razorback, recorded, runs
through all six drawings with the head steady. The front-room portrait shows
the standing frame from the 10-frame sheet.

### Picking the boar's stage in DEV, both ways — 2026-09-28

The owner wanted to start as the piglet. DEV could only step the stage
forward, the choice was lost on restart, and the front room always showed
the player's own stage. On the test phone that was a juvenile, cached from
a local-server session that the no-backend DEV build can never refresh.

`PigsDev` (`pigs_dev.dart`) now holds the DEV stage choice:
- **Saved on the device.** A stage picked for testing survives a restart.
- **Picked from the front room.** DEV builds show a ◀ stage ▶ row under the
  boar card, plus Reset to go back to the player's own stage.
- **Stepped both ways in play.** The in-game DEV menu has "Previous boar
  stage" beside "Next".
- **Visible.** The boar card shows the boar that will actually fly, labelled
  "FLYING AS (DEV)" when it isn't the player's own.

Without DGD_DEV none of it is read: the boar that flies is always the
player's own, and a test pins that. Verified on the Pixel: juvenile, one
step back to piglet, the app force-stopped and relaunched, still piglet, and
the flight started as the piglet. "Use my own" became "Reset" because the
longer label ran off the phone's edge.

### An easier variant, behind a DEV toggle — 2026-09-28

The simulated players say the standard passage is hard: most runs end before
the landing the whole game is built around. Whether that is too hard needs
someone to fly it, so there is now an easier variant to compare against,
behind the DEV menu's "Difficulty (next run)".

The difficulty knobs moved into a `PassageTuning` passed to the simulation
(`sim/passage_sim.dart`). `standard` is the game unchanged; `easy` changes
every knob:

| | Standard | Easy |
|---|---|---|
| Opening at the first era / the last | 0.36 / 0.225 of the screen | 0.40 / 0.32 |
| Scroll speed, and its ramp | 0.52 + 0.20 across the passage | 0.48 + 0.06 |
| Reserve | 3 | 5 |

The easy values were picked with the calibration bots (40 runs per profile)
rather than guessed. A first, milder set still left casual players at 0%.

| Whole passage flown | Standard | Easy |
|---|---|---|
| Casual | 0% | 10% |
| Regular | 5% | 50% |
| Skilled | 25% | 88% |

**Guardrails:**
- **Never counted.** The tuning is part of a run's transcript: a replay has
  to be given the same one to reach the same result, and a test checks that
  the same taps under standard don't reproduce an easy run. Any tuning but
  standard marks the run tainted, so the web arcade never submits it.
- **Always visible.** In play an "EASY · DEV" badge sits under the HUD. It
  first went in the HUD row, where with five reserve dots the score ran into
  the year.
- **The HUD fits.** Its reserve dots follow the run's own reserve.
- **Reproducible.** The calibration report can fly either tuning with
  `--dart-define=TUNING=easy`.

If flying it shows the standard passage is too hard, the fix is moving the
standard values toward these; nothing else has to change.

### Growing up — 2026-09-28

The moment the boar reaches its next stage was only a fanfare and an amber
panel on the results sheet. It is now an animation over the results
(`grow_up.dart`, about 3.2 s):
1. The old stage stands in a glowing white silhouette and flickers between
   its own shape and the new one. The swaps come faster and faster as the
   glow swells.
2. A white flash.
3. The new stage appears in full colour, settling from a little large, with
   sparkles (the shared glint) bursting out round it. The stage-up fanfare
   plays, with "Your boar grew into a juvenile!" and "It flies as a
   juvenile from your next run."

Taps are ignored until the reveal, so the build-up can't be skipped by
accident. After it, a tap closes the moment; otherwise it closes itself. It
opens once per growth, from a widget that mounts with the panel, so
rebuilding the panel can't replay it.

Growth only happens against a server, so the DEV menu has "Preview growing
up", which plays the moment from the current stage to the next.

**Found on the Pixel:** the first build's text drew with Flutter's yellow
double underline, which is what text gets outside a Material. The moment now
sits on a transparent Material, and the dim behind it was deepened so the
screen underneath doesn't read through.

**Tests** check that it builds up in silhouette, reveals the right stage
and line, ignores taps before the reveal, closes by itself, and opens once
from the panel.

### The replay refactor, merged — 2026-09-28

A separate piece of work for the web arcade moved the game's rules into a
pure, seeded, fixed-step simulation (`lib/arcade/passage/sim/`), so a server
can replay a run from its seed and taps and reach the same score to the last
bit. It lived on `web/replayable-passage` (9c3f74a) while `v2/ten-games`
gained eight commits: the bigger wingbeat, the polished coins and medals,
the sparkle, the home coin, and the boar's sounds.

It is now merged into `v2/ten-games` (85a84af). One file conflicted,
`passage_game.dart`: the boar's sounds had been added to the flap, strike
and touchdown code the refactor had moved into the simulation. They now play
from the simulation's `flapped`, `struck` and `touchdown` events. Everything
else merged cleanly. Analyze is clean and all 128 tests pass, including the
refactor's replay-equals-live checks across seeds, frame rates and every
ability.

### The boar's sounds — 2026-09-28

The boar borrowed Coin Quest's sounds: a UI tap on every flap and a vault
clang on every strike. It now has its own (`tools/gen_pigs_sfx.py`), which
change as it grows:

| Moment | Piglet | Juvenile | Razorback |
|---|---|---|---|
| Flap | A light, feathery flutter | A feathered whoosh | A heavy leathery beat with a low thump |
| Strike (over the impact) | A squeal | A grunt | A deep snorting growl |
| Touchdown | A contented snort, pitched to the stage | | |
| Growing up | A rising bell arpeggio over a shimmer, on the results sheet's grew-into panel | | |

**How they're made.** They are synthesised like the app's other effects:
22 kHz mono, three round-robin takes of anything that repeats, a tone below
concert pitch.
- **Wings:** noise through a band sweeping down over the stroke, with a
  feather ripple for the feathered wings and a low thump for the dragon's.
- **Voices:** a pulse train with a pitch contour, through nasal formants
  (strong near 1 kHz, a dip near 2 kHz), with breath under it.

**Checked by spectrogram, since no one here can listen.** The first pass left
the grunts as broadband hiss. They are now kept below about 2.5 kHz with the
breath as a whisper under the voice, and the harmonics show plainly.

**On the Pixel:** the effects player started 33 times in one run with no load
errors. Whether they sound right is for a human.

**Tuning.** Flaps play quietly (0.42) and spaced by at least 70 ms, since
players flap constantly. The stage-up plays once, from a widget that mounts
with the panel, so a rebuild cannot replay it.

A test checks that every effect the app lists exists on disk, the boar's
included.

**Ability sounds, the same day.** The five abilities also borrowed Coin
Quest's effects. They now have their own, from the same generator. They
sound like gear rather than like the boar, since they are what the shop
sells:

| Ability | Sound |
|---|---|
| Dash | A sharp rushing whoosh with a rising drive tone |
| Grapple | A whip crack and a chain rattling out |
| Blink | A teleport zap: a fast sweep and a sparkle pop |
| Freeze shot | An icy "pew" leaving the snout, and a crystalline crackle when it freezes its coin |
| Tractor beam | A warbling hum that swells up |

The spectrograms caught two faults:
- **Aliasing.** The grapple's and freeze-hit's top bell partials sat above
  the file's frequency limit and folded back as stray tones. They are now
  dropped.
- **An inaudible tractor.** The hum was pitched at 180-240 Hz, which phone
  speakers barely play. It now sits at 340-450 Hz, with harmonics.

On the Pixel, every ability was fired across three loadouts with no errors.

### Silver coins re-toned — 2026-09-28

The owner noticed the silver coins read as white, not metal. The render
Coin Quest shipped sat almost entirely at the top of the brightness range
(median 234 of 255, against 175 for gold), with broad blown-out areas.
Remapping its brightness only turned those areas into blotches, because the
shading was not there to recover.

`coin_silver.png` is now made from the gold coin's render instead
(`tools/gen_silver_coin.py`). The coins are the same design with full
shading, so the script takes the gold's brightness, lifts the midtones
slightly, and adds a cool blue-grey cast. Median brightness is 209: brighter
than gold, as silver should be, but with real shadow and highlight.

The originals are kept in `tools/source/`. The file is also the
leaderboard's second-place medal, which improves the same way.

**Copper, the same day.** The copper render was flat and matte beside the
new silver, with a narrow, dull range and little specular. It is now made
from the gold coin too (`tools/gen_copper_coin.py`), but through a colour
ramp rather than a tint: deep brown in shadow, saturated orange in the
midtones, a warm glint at the top. That contrast is what makes copper read
as polished metal. Median brightness is 137, darker than silver and gold as
copper is. Only When Pigs Fly uses the copper coin. All three metals now
share one lighting, so they read as a set.

**Gold, shinier, the same day.** The shared `coin_gold.png` is also the
brand's hero coin on the home screen and the leaderboard's first-place
medal, so it was left alone. The game uses its own `coin_gold_shiny.png`
instead (`tools/gen_shiny_gold_coin.py`):
- the gold render through a colour ramp: deep amber in the grooves, rich
  saturated gold, and a near-white warm top
- every 2.2 s, light catches it: two narrow streaks sweep across the face
  and a small star flares at the rim
- the sweep is phased by the coin's position on screen, so a row of coins
  shimmers in turn

The first streak spread its light across the whole gradient and washed the
coin white; it now sits in a narrow slice.

The owner then asked for the home screen's hero coin to match, and it does
(`main.dart`, `_HeroCoin`):
- it now shows `coin_gold_shiny.png`
- its sheen, once a single soft band, is now the same two narrow streaks
- the same star flares at the rim as they cross the middle

The float, the chime on each sweep and the tap-to-flip are unchanged. The
leaderboard's first-place medal, and its empty-board coin, followed the same
day, so every gold coin in the app is now `coin_gold_shiny.png`. The original
`coin_gold.png` stays in the repo as the source render, unused by the app.

The leaderboard's third-place rose-gold medal followed too
(`tools/gen_rose_coin.py`). It is made from the gold render through a
rose-gold ramp: plum-brown grooves, a warm pink-copper body and a pale blush
at the top. It stays rose gold rather than becoming the game's copper, since
the medals are precious metals. The original is kept in `tools/source/`.
Every coin in the app, the game's three and the leaderboard's three, now
shares the one lit render.

**The flare, redone.** The owner didn't like the first flare, two stroked
lines that read as a plus sign laid on the coin. It is now light
(`lib/arcade/sparkle.dart`, shared by the game's coins and the home coin):
- a soft glowing core
- four long rays tapering to fine points and fading outward
- four short, faint rays on the diagonals
- all added as light rather than painted over, turning slightly as it flares

### Music — 2026-09-27

"Flight of the Swine", the owner's own track (2:36), is the game's music. It
starts in the front room and carries on into the flight without a break,
since both use the same track and the switch to it is a no-op. Leaving the
front room hands back to the menu bed. Before, the game borrowed Coin Quest's
level bed.

**Preparing it** (`assets/audio/music_pigs.mp3`, 2.5 MB):
- from the 48 kHz WAV, encoded at 128 kbps MP3, which plays on iOS as well as
  Android
- loudness measured and brought down linearly from −8.5 LUFS to about −20,
  where the other beds sit (−19 to −22), because all music plays at one
  volume. At its original level it would have been roughly four times louder
  than the rest of the app. The source's slight overs (+0.3 dBTP) are gone
  with the gain.
- a 20 ms fade in and a 1.5 s fade out, so the loop restarts gently. The
  source ends at full level rather than fading.

A full passage is shorter than the track, so most runs never reach the loop.
If the owner wants it to loop perfectly, a version made to loop (matching
ends, or a crossfaded tail) would drop straight in.

**Verified on the Pixel from the phone's audio system:**
- the pre-run screen and the flight run a looping 44.1 kHz stereo player
- the older beds are 22 kHz mono, so that is this track
- home returns to the 22 kHz menu bed

A test checks the file ships. The source WAV stays with the owner; only the
encoded MP3 is in the repository.

### Final boar art — 2026-09-27

The owner made the boars, one flying pose per stage, and they replace the
generated placeholders:

| Stage | Look |
|---|---|
| Piglet | A chunky striped piglet in brown and gold, on small white angel wings |
| Juvenile | A golden boar on broad golden feathered wings, tusks in |
| Razorback | A scaled golden razorback with a shaggy mane, great curved tusks, on golden dragon wings |

The wings tell the growth story as much as the coat does: angel, bird,
dragon.

**Import.** `tool/art/import_boars.py` turns each image into the sheet
contract. It:
- mirrors the image to face right
- drops the detached sparkles (a flood fill on a shrunk mask)
- crops the boar into a square 320 px frame
- builds the eight frames: a small bob across the wing cycle, a red-tinted hurt
  frame, and a gently stretched dash frame

The originals are kept in `tool/art/source/` so the sheets can be rebuilt.

**The wings are rigged** (added the same day, on the owner's request).
- **The cut:** each wing is cut out of the art along the line where it meets
  the back, and turned about its shoulder. The cut lines and pivots were
  measured per stage on a grid. The piglet's white feathers are lifted by
  colour, since they overlap the gold-striped back.
- **The beat:** the sheet has a real wingbeat (up, level, down, folding back),
  plus braking wings for the landing and swept-back wings for the dash. The
  body and all its detail stay exactly as drawn.
- **Layering:** wings sit behind the body, which covers their roots.
- **Upstroke fill:** on the upstroke, a copy of the wing at rest is laid
  underneath. Without it, the wing's lower edge, which lay across the back and
  tail, left a sliver of sky through the body. On the razorback the membrane
  nearly touches the tail's curl, so the cut runs between them.
- **The tap:** each tap jumps the cycle to wings-up, so the next frames beat
  them down as the boar rises. This replaces the squash-and-stretch the
  renderer used to fake a wingbeat.
- **Bigger beat** (2026-09-28, owner's request): the wings swing 30° up and
  48° down from the drawn pose, up from 14° and 26°. Frames gained headroom
  for it: the art now fills 1/1.5 of the frame instead of 1/1.08, and
  BoarSpec was rescaled so the boar draws the same size. At this size, the
  resting-wing underlay showed as a ghost second wing. The root wedge is now
  filled with a fan of the wing at in-between angles, kept near the shoulder
  and used on the upstroke only.

**The art is sampled smoothly now.** It is detailed rather than on a strict
pixel grid, and nearest-neighbour shimmered as it scaled and pitched.

**Placement, measured on a grid.** The frames are cropped close, so each
stage is drawn smaller in hitbox radii than the padded placeholders were: 4.2,
6.0 and 6.6. The chunky piglet stays small and the razorback is clearly the
biggest.

**Hitbox.** The capsules fit the new bodies. The razorback's heavier body
takes the old coin's full height (radius 1.0, half-run 0.75); the others keep
0.9. No stage is harder to fit through a gap than the coin was, and the
steady-player guard still flies every stage clean.

**Verified on the Pixel** with the hitbox shown: the front-room portrait, and
each stage in flight and landing.

### Era skylines — 2026-09-27

The sky behind the passage now carries a city for each era, in silhouette
(`lib/arcade/passage/city.dart`). They are evocative, not portraits, by the
owner's choice: period architecture says where and when without drawing any
specific building. That avoids the likeness questions a few famous buildings
carry, and it can't be wrong about a date.

| Era | Scene |
|---|---|
| 1816 | London: gabled terraces with smoking chimney pots, church spires, domes |
| 1873 | An American city: brick blocks with cornices, mansard roofs, spires |
| 1913 | New York: brick with rooftop water tanks, the first skyscrapers |
| 1923 | Berlin: sawtooth factories and smoking stacks, tenements, few lit windows |
| 1933 | A Depression-era American city: Art Deco setbacks, many dark windows |
| 1944 | Bretton Woods: mountains, pines and a grand hotel. The agreement was made at a resort, not in a city |
| 1971 | Washington: low and classical (the height limit), domes and pediments among trees |
| 1979 | A late-seventies downtown: brutalist blocks and glass under fluorescent light |
| 2009 | A glass city at night with aviation lights, and a faint grid across the sky. The first block was not mined anywhere in particular |

**How it's drawn.**
- Two parallax layers, a hazy far skyline on a higher horizon and a darker
  near one, both scroll slower than the gates.
- A building takes the style of the era in play when it passes mid-screen, so
  each new city rolls in from the right as the era changes.
- Each building is drawn once into a cached picture. Per frame the skyline is
  a few picture draws, plus smoke in 1816 and 1923 and a few blinking lights.
- Lit windows are held dim, so they are never mistaken for coins.

**Found in the first on-device pass.** At first scale the whole city was a
strip of rooftops half behind the navigation bar, and the chimney smoke read
as bubbles. Heights were roughly doubled, the far layer raised, and the smoke
made smaller and fainter.

**Tests.**
- every era has a city in both layers
- the skyline has no holes
- nothing reaches into the top of the screen
- 1944 is mountains, pines and a hotel and nothing else
- the same seed builds the same city
- every era draws

A labelled sheet of all nine, rendered by the game itself, is in
`v2/dist/shots/pigs-cities.png`. DEV menu: "Next era (see its city)" jumps
to the start of the next era.

### Era gates — 2026-09-27

The gates were one brushed-metal pillar throughout. They are now built from
the materials of their era, so the passage belongs to the city behind it
(`passage_gates.dart`):

| Era | Gate |
|---|---|
| 1816 | Fluted Portland-stone columns with volutes |
| 1873 | Cast-iron columns, banded, with a flared head |
| 1913 | Riveted steel I-beams with lattice bracing |
| 1923 | Brick factory chimneys, sooty at the mouth, with an iron band |
| 1933 | Art Deco pillars: dark stone, brass flutes, a brass chevron and stepped head |
| 1944 | Timber posts bound with iron straps, on stone caps |
| 1971 | White marble columns |
| 1979 | Board-marked concrete with rain stains |
| 2009 | Dark glass with cyan edge light and circuit traces |

**What doesn't change, whatever the material:**
- the collision rectangle. Every gate draws inside it and never beyond, and
  the texture is clipped to its block. The first render showed the steel
  lattice spilling into the opening.
- the amber lip at the opening, which is still the one thing that says where
  the gap is at a glance.
- a body lighter than the skyline behind, so a gate never sinks into the city.

Each gate is drawn once into a cached picture when it first comes into view.
A labelled sheet of all nine is in `v2/dist/shots/pigs-gates.png`.

### Phase 5, tuning and final art — tooling built 2026-09-24

Tuning properly needs real players on a deployed server, and final art needs
an artist. What could be done ahead of both was done.

**Calibration from simulated players**
(`test/passage_calibration_test.dart`). A bot flies the real simulation
headlessly. It sees what a player sees — the openings, the coins, its own
height and speed — taps after a reaction delay, and aims imperfectly. It also
has the human part: it misjudges its own speed, taps early or late, and looks
away now and then. Without those, its "casual" player flew the whole passage
nine runs in ten.

Three profiles, 40 runs each:

| Player | Median run | p25–p75 | Eras reached | Whole passage |
|---|---|---|---|---|
| Casual | 130 | 61–239 | 3.6 | 0% |
| Regular | 339 | 246–412 | 4.7 | 3% |
| Skilled | 729 | 503–1,003 | 6.6 | 28% |

At four runs a day the casual player reaches the juvenile in about 3 days and
the razorback in about 11.5. That is the pace the owner asked for when the
thresholds were lowered, so the thresholds stood at 1,500 and 6,000 — until
the feel fixes below moved the numbers, and they were lowered again to 1,200
and 4,000.
Regular players take about 1 and 4.5 days, skilled about half a day and 2.

**Prices** also stand. A first ability comes in about a day for a casual
player. Every ability at level 3 is 32,300 points, about two months casual,
three weeks regular, and eleven days skilled. The daily cap of 10 paid runs
bounds all of it.

The skilled bot flies the whole passage less often than its score suggests,
because chasing gold coins to the lips of the late, narrow gaps costs strikes.
That is the risk the drifting gold coin was designed to carry, and here it is
measured.

These are a bot's numbers, not people's. They bracket the first settings and
are to be replaced by measured ones.

**Playability guard.** By default the same file runs a steady profile: human
reaction time, no coin chasing, no lapses. It has to fly the whole passage
with no strikes on four seeds. If a change to the gaps, speed or drift ever
breaks that, the game has become unfair rather than harder, and the suite goes
red. The full report runs with `--dart-define=CALIBRATE=true`.

**The real report** (server, `npm run report:passage -- --db <path>`,
`src/report.ts`). It is read-only and covers:
- claimed runs and players
- score percentiles, the star split and eras reached
- the typical player's points and runs on a day they play (the median of each
  player's median day, counting only paid runs, as growth does)
- active days to each stage at the current thresholds
- suggested thresholds for target days (default 2.5 and 10)
- boars at each stage, unlocks by level, abilities flown with, and rejected
  loadouts

Below 20 players it suggests nothing, because a threshold tuned to three
testers is worse than the calibrated guess. A test checks every figure against
hand-made rows. The same test caught its median taking the upper middle value.
Thresholds change by env var (`PASSAGE_JUVENILE_AT`, `PASSAGE_RAZORBACK_AT`),
so acting on the report needs no deploy.

**Final art handoff.**
- **`WHEN-PIGS-FLY-ART-BRIEF.md`** gives an artist: the character and three
  stages in the owner's words, the required coin slot, style and originality
  rules, the eight-frame sheet contract with each pose, headroom and export
  size, and the steps to drop the art in.
- **`tool/art/check_sheets.py`** validates a delivery against the contract.
  It checks mode, frame count, empty frames, art touching the frame edge and
  background, measures the hoof line exactly, and prints a starting point for
  the anchors.
- **Already found by it:** the placeholder razorback's dash-pose wing ran off
  the frame, now fixed.
- **What it cannot measure:** where the hitbox belongs is a judgement, so the
  brief says to confirm on a phone.

The three feel issues from the phase 1 notes were fixed the same day; see
"Feel fixes" below. Those fixes moved the calibration, and the table above is
the before; the after is in that section.

### Feel fixes — 2026-09-24

1. **The razorback's wings under the HUD.**
   - The play area now starts below the HUD, at 12% of the screen height
     (`PassageGame.playTop`). Before, openings reached to 6% and the boar's
     ceiling sat under the status bar, so a razorback at the top had wings and
     part of its body behind the reserve dots.
   - Openings, trail coins and the boar's ceiling all respect the line.
   - A soft shade behind the HUD row makes the wing tips that still reach up
     under it read as flying behind the bar.
2. **The snout and rump overhanging the hitbox.**
   - The body now collides as a horizontal capsule, per stage in `BoarSpec`:
     half-height 0.9 of the old coin radius at every stage, and a straight run
     of 0.35 / 0.5 / 0.62 radii.
   - The half-height is below the coin's, so no stage is harder to fit through
     a gap than the coin was. The length means a snout that visibly meets a
     pillar is a strike.
   - Coins are taken by the same capsule, and the floor and touchdown use its
     half-height.
   - A test caught the old broad-phase check (pillar within one gate width)
     skipping the razorback's snout entirely. It now reaches as far as the
     capsule does.
   - DEV menu: "Hitbox: show" draws the capsule and the play-area line.
3. **An untapped landing out of sight.**
   - When a run settles, the ground now appears at the floor line (94%) and
     rises to 87%, instead of rising from below the screen. A boar left
     untapped touches down in view.
   - That alone would have handed out the soft-landing star to anyone parked
     on the floor, because the ground would meet them at a crawl. So a
     touchdown within 1.5 s of touching the floor is never soft.
   - Easing down stays a thing you do from the air.

**An older bug, found on the way.** The ground's creep after it settles — there
so a player tapping as fast as possible still touches down — never
accumulated. It was subtracted from a height recomputed every frame, so a fast
tapper could hover forever. The calibration bot hovered for a minute and a
half. The creep now accumulates, and a test taps ten times a second through a
landing and requires a touchdown inside 20 s.

**Calibration after the fixes** (same bot, 40 runs each):

| Player | Median run | Eras reached | Whole passage | Juvenile / razorback at 4 runs a day |
|---|---|---|---|---|
| Casual | 96 | 2.9 | 0% | 3.9 / 15.6 days |
| Regular | 385 | 5.4 | 5% | 1.0 / 3.9 days |
| Skilled | 731 | 6.4 | 25% | 0.5 / 2.1 days |

The narrower play area and the longer body made casual play a little harder.
The casual player was now slower than the owner's 2–3 / ~10 day target, so on
the owner's word **the thresholds were lowered to 1,200 and 4,000**. That puts
casual play at 3.1 / 10.4 days, regular at 0.8 / 2.6 and skilled at 0.4 / 1.4.

The fairness guard now flies every stage: a steady player gets through the
whole passage with no strikes as a piglet, a juvenile and a razorback.

**Tests added:**
- nothing to see or reach sits under the HUD, and a frantic tapper stops at
  the line
- no stage's capsule is taller than the old coin
- a razorback snout meeting a pillar is a strike
- an untapped landing touches down on screen
- parking on the floor is not a soft landing
- a fast tapper still touches down

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
