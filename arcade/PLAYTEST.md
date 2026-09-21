# Play test — 2026-09-16

The DEV build on your Pixel right now is `app-release.apk`, 56.3 MB, built from
a clean analyzer and 32 passing tests. Release-optimised, so memory and audio
behave the way a real build does; the DEV chip is compiled in.

Everything below is here for one reason: **a lot of recent fixes have only ever
been checked by a test or by me reading the code. No human has looked at them.**
This list is ordered by how likely I think each one is to be wrong, and it is
short on purpose — you said you cannot spend long playing.

Two DEV menus:

- **Level map → DEV** — jump to any world, reset progress, audio soak test.
- **Inside a level → DEV** — force a combo (x4 / x6 / x9), force a win at
  3 / 1 / 0 stars, force a loss.

The forced win and loss run the *real* end-of-level path, so they are the fast
way to check the celebration and the voice lines without playing to the end.

---

## 1. Audio soak — DONE, and it passed

**Result, 2026-09-16:** 600s, 6000 attempted, 6000 played, **0 failed**, 0
dropped by the limiter. p50 2 ms, p95 16 ms, max 48 ms. First decile 4.5 ms,
last decile 4.6 ms, **drift 1.02×** against a 1.3× threshold.

Flat. The per-file player pool holds over a long run and nothing leaks, so the
original "effects consistently lag then stop" bug is closed on evidence. The
single 48 ms max against a 2 ms median is one outlier out of six thousand —
normal scheduling jitter, not a trend.

Original instructions kept below in case it needs re-running after audio
changes.



Level map → DEV → **Audio soak test** → 10 minutes. It fires ten effects a
second on its own; you do not have to watch it.

What to send me: **failed**, **limited**, **p95**, and **drift**. Healthy is
`failed = 0` and `drift < 1.3`. Drift is the mean latency of the last tenth of
the run over the first tenth, so a number climbing past ~1.5 means it is still
degrading over time and I have not actually fixed it.

## 2. Armoured vaults — level 28, not level 21

You reported "no change in damage state after first hit" in world 3. I have
since read the level table, and on **levels 21–27 and 29 a vault has one hit
point** — it is supposed to break outright. There is no damaged state to see,
so nothing was wrong with what you saw.

The two-stage vault only exists on **28, 30, 42, 47, 51, 55, 58**. Level 28 is
the first. Match beside a vault there: the armour plate should come off and the
vault should stay on the board, then break on the second hit.

If it still looks identical after the first hit on 28, the sprite swap is
broken and I want to know.

## 3. Level win — fireworks and the voice line

Any level, DEV → **Win — 3 stars**.

Six shells, then a muted finale trio, then willows falling for about another
two seconds; a spoken "you win" line lands after the second shell. Roughly
five seconds before the results card.

I rewrote the firework renderer after finding that every star was silently
being given a half-second lifespan regardless of what it asked for. This is the
first look at the rewrite. What I am watching for: stars that vanish abruptly
mid-fall, a show that ends before the results card, or the line landing on top
of the first shell instead of inside the show.

## 3b. The grand finale — level 60 only

Added 2026-09-17. Clearing the **last** vault in the game runs a different,
much longer show: an opening pair wide left and right, a nine-shell climbing
run that rises and accelerates, a deliberate third-of-a-second of silence, then
five shells together across the full width and a gold willow that keeps falling
for three and a half seconds. About seven seconds end to end, with a second
spoken line over the willow. Keyed off the end of the level list rather than a
hardcoded 60, so adding a world moves the finale with it.

DEV → **Win — GRAND FINALE show** triggers it from any level.

Still light and fireworks, never coins — arcade plan §4.3 bars prize and
jackpot imagery, and a shower of gold coins over a gold-backed asset's own app
is exactly what that rule is about.

**The celebration now uses the whole screen — fixed the same day.** Every win in
this game used to be clipped to the board rectangle, because the Flame surface
was an `AspectRatio` sized to the grid inside a container with
`clipBehavior: Clip.antiAlias`. However many shells fired, two-thirds of the
screen was off limits to them, which is why no celebration ever felt as big as
it was.

Flame already centres the board itself — `_layout()` computes
`cell = min(w/cols, h/rows)` and an origin that centres the grid — so the
`AspectRatio` was duplicating work the engine already did. The game now gets
the full area, the glass plate is a widget laid out behind it from the same
arithmetic, and nothing about where the board draws has changed. Shells break
above the board and embers fall past it; on level 60 the willow hangs over the
whole screen.

**One visible side effect, and it is your call.** The intro drop-in is no longer
hidden until it reaches the board. Coins are now visible falling through the
empty space above the plate, column by column, for about a second before they
land. The clip used to cut that off at the board's edge.

I have left it in because it reads as coins pouring into a vault, which is the
theme — but it is a change to the first second of every level, so look at it
and say if you would rather it went back to appearing at the board edge. That
would be a clip on the intro only, not on the celebration.

Also worth checking: the board should sit exactly where it always did, same
size, same 6px surround. It is laid out by the same arithmetic, but it is the
kind of thing worth one glance.

## 3c. The level map opens where you are — and always did

I reported that the map "always opens at level 60 instead of where you are".
**That was my mistake.** It opens at 60 on your Pixel because your Pixel is
genuinely on level 59: the DEV world-jump marked the first fifty cleared, and
you played through to 58. The top of the list was the right answer.

Two changes went in anyway, both small and both defensible: the scroll now waits
for the first frame (there is a real race where the progress future can resolve
before the list has attached its controller, and the scroll is then silently
dropped), and it jumps rather than animating, because an initial position should
not cost half a second of watching the list fly past.

**Worth checking on a fresh install**, where the answer is not obviously the top
of the list: clear a couple of levels, back out to the arcade home, come back in,
and confirm the map lands on your current level rather than on 60 or on 1.

## 4. Voice lines — the tiers

- DEV → **Combo x4** → one of five standard praise lines.
- DEV → **Combo x6** → one of four bigger lines.
- DEV → **Lose** → one of five encouragement lines, softest first.

Sixteen lines total, all yours from ElevenLabs. There is a seven-second gate
across both praise tiers so they stay an event rather than a tic. Trigger x4
twice in a row quickly — the second one should stay silent.

Two of your uploads did not match their filenames (`nice 3.mp3` is "You win!",
`You're on fire!.mp3` is "Fire!"), so I keyed everything on what the audio
actually says. Worth confirming each line lands where it belongs.

## 5. Ingots — level 31

An ingot used to be drawn twice in one step because two gravity passes each
reported it moving, and the renderer got two conflicting positions for the same
piece. Fixed by merging the passes into one move per piece.

On 31, work an ingot to the floor. It should slide, not flicker or teleport,
and "DELIVERED" should fire once.

## 6. HUD wording

You reported "break all 12 R..." truncated. Goal text is shorter now and the
chip reads SCORE rather than VALUE. Check 28 and 57 — the longest goals.

## 7. Leaving a level mid-cascade

New today. Start a big cascade and hit back while coins are still falling, a
few times over. Nothing should visibly happen — that is the point. Before
today the animation loop stayed suspended forever and held the whole board in
memory, so five quits meant five boards still resident.

If backing out mid-cascade ever plays a sound on the map screen, or drops you
onto a results card for a level you left, tell me.

## 8. Home screen

Tap the big coin — it should alternate spin and flip with a small hop, with a
sound on each and a ting when it lands; taps during a toss are ignored. The
badge under the title reads PROOF OF PLAY and there is a "More games coming
soon" line above the disclaimer.

---

## Two things you may hit that are working as intended

- **A level can now end as a loss with moves left.** If the board runs out of
  legal moves and reshuffling cannot find one either, the level ends rather
  than hanging. It is rare. If you see it happen on a board that obviously
  *does* have a move, that is a bug.
- **PROOF OF PLAY is aspirational in the demo build.** In the sideload demo
  there is no server, so nothing is actually verifying rounds. It is honest in
  the DEV build you are holding, and it will be honest in the tester build once
  the backend is hosted.

## Not covered, and why

The other nine games were removed on 2026-09-16 ahead of the new list of ten —
see `REMOVED-GAMES.md`. The home screen is Coin Quest and nothing else.

The standings bar still needs the server, which is only on this PC at
`localhost:8787`, so it shows OFFLINE in the DEV build and is hidden in the
demo. Nothing to test there until it is hosted.

## Afterwards

I cleared the device log before handing this over, so whatever happens during
your session is the only thing in it. If anything crashes or looks wrong, say
so and I will read the log rather than ask you to reproduce it.
