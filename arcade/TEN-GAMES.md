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
| Art | The coins are the DGD coin renders Coin Quest ships (`coin_gold`, `coin_silver`, `coin_copper`). The boar is three pixel-art sheets, `boar_{piglet,juvenile,razorback}.png` (placeholders, see below). Everything else is drawn from primitives. Nothing resembling any existing game's look |

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
| Piglet | Small, golden-blond with cream humbug stripes and blond tufts, stubby wings | 48 px | 5.6 hitbox radii |
| Juvenile | Filled out, bristly medium fur shifting from brown to gold, a bristle ridge, small tusks | 72 px | 6.6 |
| Razorback | Full size: gold coat, spined crest, a flowing amber mane over the shoulders, large tusks, battle scars, a red eye, big bronze dragon wings | 108 px | 7.8 |

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
5. **Tuning and final art.**

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

**Thresholds are provisional:** juvenile at 1,500 lifetime points,
razorback at 6,000, from a guess of about four runs a day at about 150
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
