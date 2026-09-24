import 'dart:async';
import 'dart:math';
import 'dart:ui';

import 'package:flame/components.dart';
import 'package:flame/game.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';

import '../../audio.dart';
import '../../theme.dart';
import '../cabinet/cabinet.dart';
import 'boar.dart';
import 'eras.dart';

part 'passage_render.dart';

/// When Pigs Fly — the one-tap flyer, game 1 of the new catalogue. Its id
/// everywhere below the title (server, cabinet, file names) is still
/// `passage`, so rounds, XP and leaderboards carry straight over from the
/// version where the player flew a coin.
///
/// The player is a winged piggy bank in three stages — see `boar.dart`. The
/// simulation still flies a circle of the coin's old radius; only the art
/// changed, which is why most of the names in this file still say "coin".
///
/// ## Why this is not an endless runner
///
/// The mechanic is the familiar one: tap to hold altitude, fly through gaps.
/// The failure model is not. In an endless flyer every session ends in
/// failure, because the run is defined as continuing until you fail — so the
/// last thing a player feels, every single time, is having lost. That works
/// for a game whose hook is the sting of falling short. It is wrong for a
/// training app, where the last beat should be the one that brings someone
/// back tomorrow.
///
/// So: **every run ends in a landing. The only variable is where.**
///
///  * A run is a finite passage through the nine eras in `eras.dart`.
///  * Hitting a gate costs one unit of [reserve] and knocks the coin down.
///    It does not end the run.
///  * At zero reserve the coin does not die. Lift authority fades over about
///    a second and it sets down where it is — a short landing, in whichever
///    era it got to. "Landed in 1933" is a finished journey with a story, not
///    a death.
///  * Flying the whole passage triggers a deliberate landing: the gates stop,
///    the ground rises, and the player spends their remaining lift easing
///    down onto it.
///
/// The final stretch is the part that makes the feeling work. Everything
/// before it ramps up — gaps narrow, the scroll quickens — and then there is
/// several seconds of open sky before the ground appears. Tension needs a
/// release to become relief, and an endless game never has one.
///
/// ## The honest trade
///
/// Guaranteed landings cost replay pressure. "One more go" runs on the sting
/// of just missing, and this removes the sting deliberately. The mastery
/// headroom is moved into the grade instead: the third star needs a soft
/// touchdown, which is a real skill and is the only thing in the game that
/// is hard.
///
/// Star rule, stated once here and shown in the same words on the results
/// sheet:
///
///  * ★     you landed  (always earned — there is no way not to)
///  * ★★    you flew the whole passage
///  * ★★★   you flew the whole passage and set it down softly
///
/// ## Theme
///
/// The corridor is monetary history and nothing else. See the header of
/// `eras.dart` for the rules the content is written under and why there is
/// no "avoid inflation" framing anywhere in this file.

enum PassagePhase {
  /// Normal flight.
  flying,

  /// Out of reserve. Lift fades fast and the coin sets down short.
  descending,

  /// Passage flown. The ground rises; the player eases onto it.
  landing,

  /// Touched down. Rolling to a stop before the results sheet.
  down,
}

class _Gate {
  /// Distance from the start of the passage to this gate's centre line.
  final double worldX;

  /// Centre of the opening, in pixels from the top.
  final double gapY;

  /// Height of the opening, in pixels.
  final double gapH;

  /// Index into [eras].
  final int era;

  /// Already counted towards [gatesCleared].
  bool passed = false;

  /// Already charged a unit of reserve. A coin that clips a pillar stays
  /// overlapping it for several frames; without this it would be charged on
  /// every one of them.
  bool struck = false;

  _Gate({
    required this.worldX,
    required this.gapY,
    required this.gapH,
    required this.era,
  });
}

/// Something the coin can pick up. Three metals, deliberately unequal:
///
///  * A **gold DGD coin** floats inside every opening, drifting between the
///    top lip and the bottom one. Taking it means flying through the gate
///    where the coin is rather than where the gap is easiest, and its phase
///    flips from one gate to the next, so the line through the passage is a
///    weave rather than a groove.
///  * **Silver** and **copper** coins run in a short arc across the open air
///    between gates, silver at the peak of the arc and copper at its ends.
///    Taking them is about tracing a path, not about risking a pillar.
enum PickupKind { copper, silver, gold }

class Pickup {
  final double worldX;

  /// Rest position. A drifting coin oscillates about this.
  final double y;
  final PickupKind kind;

  /// Drift amplitude in pixels; zero for a coin that holds still.
  final double amp;

  /// Drift phase in radians, so neighbouring gates can start opposite.
  final double phase;
  bool taken = false;

  Pickup({required this.worldX, required this.y, required this.kind, this.amp = 0, this.phase = 0});

  /// Where the coin is at game time [t].
  double yAt(double t) => amp == 0 ? y : y + amp * sin(phase + t * PassageGame.driftRadPerSecond);

  int get value => switch (kind) {
        PickupKind.copper => PassageGame.copperValue,
        PickupKind.silver => PassageGame.silverValue,
        PickupKind.gold => PassageGame.goldValue,
      };

  double get momentumGain => switch (kind) {
        PickupKind.copper => PassageGame.momentumPerCopper,
        PickupKind.silver => PassageGame.momentumPerSilver,
        PickupKind.gold => PassageGame.momentumPerGold,
      };
}

/// A coin knocked loose by a strike. It arcs up, falls under gravity, drifts
/// back toward the player on screen, and can be caught again for a moment.
class _Spill {
  double worldX, y, vx, vy;
  double age = 0;
  bool taken = false;
  _Spill(this.worldX, this.y, this.vx, this.vy);
}

/// A short ring where a coin was taken.
class _Pop {
  final Offset at;
  final bool big;
  double age = 0;
  _Pop(this.at, this.big);
}

class PassageGame extends FlameGame {
  final CabinetRun run;

  /// Fixed seed for tests and the DEV menu; null means a fresh passage.
  final int? seed;

  /// Which boar is flying. Fixed for a run once growth is live; settable now
  /// so the DEV menu can show all three.
  BoarStage stage;

  PassageGame({required this.run, this.seed, this.stage = BoarStage.piglet}) {
    run.onTap = flap;
  }

  // ------------------------------------------------------------ tuning
  //
  // Everything is a fraction of the viewport, so the game plays identically
  // on a tall phone and a short one. The comments give the value in units a
  // player would feel rather than in pixels.

  /// Gap height at the first era and at the last, as a fraction of height.
  ///
  /// The coin is 0.052 high, so this is 6.9 coin-diameters narrowing to 4.3 —
  /// and to 4.1 at the fourth gate of the last era, once the small per-era
  /// squeeze below is applied. The original this borrows from ran at roughly
  /// 3.3 and was cruel on purpose; that is the one thing from it we are
  /// explicitly not taking, so `passage_test.dart` holds the tightest gate in
  /// the game at four diameters or wider.
  static const _gapFracStart = 0.36;
  static const _gapFracEnd = 0.225;

  /// Reserve units. Three strikes before the descent begins.
  static const startingReserve = 3;

  static const _invulnerableFor = 1.1; // seconds after a strike

  // ------------------------------------------------------- coins and momentum
  //
  // Added after the first device build. The run needed something to chase
  // between the gates, and the reward for chasing it is speed: every coin
  // taken adds momentum, momentum scrolls the passage faster, and a faster
  // passage is both shorter and harder. That is the risk/reward, and it is
  // opt-in — the safe line through every gate takes no coins and runs at
  // base speed.
  //
  // Speed is capped because it is the one thing that makes a flyer
  // unreadable rather than hard (see [_speed]). At full momentum the passage
  // runs about a third faster than base, and the multiplier on coin value
  // steps up with it, so the fast line is also the rich one.
  static const copperValue = 1;
  static const silverValue = 3;
  static const goldValue = 10;
  static const momentumPerCopper = 0.05;
  static const momentumPerSilver = 0.08;
  static const momentumPerGold = 0.16;

  /// How fast a gold coin drifts through its opening: one full top-to-bottom-
  /// to-top cycle in about 2.4 s, which is roughly the time between gates at
  /// base speed. Slow enough to read from a screen away, fast enough that
  /// where it will be when you arrive is a judgement rather than a given.
  static const driftRadPerSecond = 2 * pi / 2.4;

  /// Momentum bleeds off slowly, so it has to be fed rather than banked.
  static const momentumDecayPerSecond = 0.03;
  static const maxSpeedBoost = 0.35;

  /// Points knocked loose by a strike. They fall as coins that can be caught
  /// again, so the cost is visible and recoverable rather than a deduction on
  /// a number — this game does not do stings, and a silent minus would be one.
  static const spillOnStrike = 4;
  static const _spillLife = 2.6; // seconds

  // ------------------------------------------------------------- state

  final _rnd = Random();

  /// Not `late final`: the passage is regenerated if the viewport changes
  /// before the player commits to it. See [onGameResize].
  late List<_Gate> _gates;

  double _w = 0, _h = 0;
  bool _laidOut = false;

  /// Distance flown, in pixels.
  double scrollX = 0;
  double _coinY = 0;
  double _vy = 0;
  double _t = 0;
  double _invUntil = -1;

  /// Multiplies the flap impulse. Decays during a descent or a landing, which
  /// is what makes a touchdown inevitable without ever taking the controls
  /// away outright.
  double _lift = 1;

  /// Where the ground is. Starts below the viewport and rises.
  double _groundY = 0;

  double _phaseT = 0;
  PassagePhase phase = PassagePhase.flying;

  int reserve = startingReserve;
  int gatesCleared = 0;

  /// Eras flown end to end. This is what the star rule turns on: two stars
  /// means the whole passage, and entering 2009 is not flying it.
  int erasCleared = 0;

  /// Eras the coin actually reached, counting the one it is in.
  ///
  /// Both numbers are needed and it is worth being clear why. A run that
  /// ends on the first gate of 1816 has cleared zero eras, which is true but
  /// reads as nothing: the sheet said "You set down in 1816" directly above
  /// "0 of 9 eras flown", and skipped the era's fact entirely — so the one
  /// run most in need of a reason to try again got the least. Reached is
  /// what the player experienced and is what the results sheet counts.
  int get erasReached => _started ? (eraNotifier.value + 1).clamp(0, eras.length) : 0;

  /// Vertical speed at the moment of touchdown, in fractions of height per
  /// second. Below [softLandingAt] is a soft landing.
  double touchdownSpeed = 0;
  static const softLandingAt = 0.42;

  bool get softLanding => touchdownSpeed.abs() < softLandingAt;

  /// Drives the era banner in the Flutter overlay.
  final ValueNotifier<int> eraNotifier = ValueNotifier(-1);
  int get eraIndex => eraNotifier.value;

  /// Red flash after a strike, 1 fading to 0.
  double _strikeFlash = 0;

  /// The DGD coin renders, the same three Coin Quest ships and the home
  /// screen shows. Null until [onLoad] has them, or for good if the load
  /// fails — the renderer falls back to drawn coins rather than to nothing,
  /// so a missing image can never take the game down with it.
  final Map<PickupKind, Sprite> _coinSprites = {};

  /// The boar sheets, cut into frames. All three stages are loaded so a DEV
  /// stage switch is instant; the renderer falls back to the drawn coin for
  /// any stage whose sheet is missing.
  final Map<BoarStage, List<Sprite>> _boarFrames = {};

  /// Wing-cycle position, in frames. Advanced in [update] at a rate that
  /// jumps on every flap, so a tap is visibly a wingbeat.
  double _wingPhase = 0;
  double _flapAt = -10;
  double _hurtUntil = -1;

  late List<Pickup> _pickups;
  final List<_Spill> _spills = [];
  final List<_Pop> _pops = [];

  /// Points this run. Shown in the HUD, reported to the server as `score`,
  /// and worth a small capped XP bonus there. Never below zero.
  int score = 0;

  /// Coins taken, of any kind, including recovered spills.
  int coinsTaken = 0;

  /// 0..1. Fed by coins, bled by time, zeroed by a strike.
  double momentum = 0;

  /// How much faster than base the passage is scrolling. 1 at rest.
  double get speedFactor => 1 + maxSpeedBoost * momentum;

  /// Coin value multiplier at the current momentum. Three tiers, so the HUD
  /// can show a whole number that means something.
  int get multiplier => momentum >= 0.98 ? 3 : (momentum >= 0.5 ? 2 : 1);

  /// Recent coin positions, for the trail.
  ///
  /// Stored as (distance flown, height), not as screen points. The first
  /// version stored screen points at the coin's fixed x, so the trail could
  /// only ever be vertical — a streak out of the top of the player rather
  /// than a wake behind it. That passed for a round coin and did not for a
  /// boar, where it read as exhaust from its back.
  final List<Offset> _trail = [];

  /// Total length of the passage, set in [_layout].
  double _totalX = 0;
  double _lastGateX = 0;

  /// True once the player has tapped. The coin hovers until then, so the run
  /// does not start counting down while someone is reading the first banner.
  bool _started = false;
  bool get started => _started;

  double get progress => _totalX == 0 ? 0 : (scrollX / _totalX).clamp(0.0, 1.0);

  /// The generated passage, flattened, for tests. Gate layout is the one part
  /// of this game that can silently produce an unplayable run, so it is worth
  /// being able to assert on.
  @visibleForTesting
  List<({double worldX, double gapY, double gapH, int era})> get gateSpecs =>
      [for (final g in _gates) (worldX: g.worldX, gapY: g.gapY, gapH: g.gapH, era: g.era)];

  @visibleForTesting
  List<Pickup> get pickups => List.unmodifiable(_pickups);

  @visibleForTesting
  int get spillCount => _spills.length;

  @visibleForTesting
  double get gateWidth => _gateW;

  @visibleForTesting
  double get coinRadius => _coinR;

  /// The frame the boar would be drawn with right now.
  @visibleForTesting
  int get boarFrame => _boarFrame();

  /// Takes a pickup as if the coin had flown through it.
  @visibleForTesting
  void collectForTest(Pickup p) => _collect(p, _coinX + (p.worldX - scrollX));

  /// Lands a strike as if the coin had clipped a pillar.
  @visibleForTesting
  void strikeForTest() => _strike(null);

  // --------------------------------------------------------------- layout

  double get _coinR => _h * 0.026;
  double get _coinX => _w * 0.30;
  double get _gravity => _h * 2.35;
  double get _flapImpulse => -_h * 0.60;
  double get _vMax => _h * 1.05;
  double get _spacing => _w * 0.85;
  double get _leadIn => _w * 1.15;
  double get _eraGap => _spacing * 0.9;
  double get _gateW => _w * 0.085;

  /// Open sky between the last gate and the ground appearing. This is the
  /// release the whole design rests on — do not trim it for pacing.
  double get _calmRun => _w * 2.4;

  double get _skyFloor => _h * 1.3;
  double get _groundAt => _h * 0.87;

  @override
  Future<void> onLoad() async {
    await super.onLoad();
    // Not awaited. A GameWidget holds the whole game — update, render, the
    // era banner — until onLoad completes, and the first version awaited
    // the three images here, which pushed the opening banner late enough
    // for the widget test to miss it. The images arrive within a frame or
    // two on device; until they do the renderer draws coins itself.
    unawaited(_loadCoinSprites());
    unawaited(_loadBoarSheets());
  }

  /// One image per stage, one row of square frames. See the sheet contract
  /// in `boar.dart`; a sheet with the wrong frame count is treated as
  /// missing rather than drawn with frames cut in the wrong places.
  Future<void> _loadBoarSheets() async {
    for (final e in BoarSpec.all.entries) {
      try {
        final img = await images.load(e.value.file);
        final side = img.height.toDouble();
        if ((img.width / img.height).round() != BoarFrame.count) continue;
        _boarFrames[e.key] = [
          for (var i = 0; i < BoarFrame.count; i++)
            Sprite(img, srcPosition: Vector2(i * side, 0), srcSize: Vector2.all(side)),
        ];
      } catch (_) {
        // Drawn fallback. See _coin.
      }
    }
  }

  /// Loaded by their bare names the way Coin Quest loads its pieces; Flame
  /// prefixes assets/images/. assets_test.dart cannot see these names, so
  /// the drawn fallback is what stands between a renamed file and a blank
  /// coin.
  Future<void> _loadCoinSprites() async {
    const files = {
      PickupKind.gold: 'coin_gold.png',
      PickupKind.silver: 'coin_silver.png',
      PickupKind.copper: 'coin_copper.png',
    };
    for (final e in files.entries) {
      try {
        _coinSprites[e.key] = await Sprite.load(e.value);
      } catch (_) {
        // Drawn fallback for this metal. See _smallCoin.
      }
    }
  }

  @override
  void onGameResize(Vector2 size) {
    super.onGameResize(size);
    if (size.x <= 0 || size.y <= 0) return;

    // The whole passage is generated from the viewport, so a resize after the
    // player has committed would move every gate they are already flying
    // towards. Before the first tap there is nothing to disturb, so a late or
    // corrected size is taken then and only then.
    //
    // That "and only then" is what makes this robust rather than merely
    // tidy: Flame can hand over a provisional size on an early layout pass,
    // and the previous version kept the first one forever while still
    // updating _w and _h — which left the gate positions computed from one
    // size and drawn against another.
    if (_laidOut && _started) return;

    _w = size.x;
    _h = size.y;
    _layout();
    _coinY = _h * 0.45;
    _groundY = _skyFloor;
    _laidOut = true;
    // NB: do not touch [eraNotifier] from here. See the note in [update].
  }

  void _layout() {
    final rnd = seed == null ? _rnd : Random(seed);
    final gates = <_Gate>[];
    final block = gatesPerEra * _spacing + _eraGap;
    var lastGapY = _h * 0.5;

    for (var era = 0; era < eras.length; era++) {
      final eraFrac = eras.length == 1 ? 0.0 : era / (eras.length - 1);
      final baseGap = _h * lerpDouble(_gapFracStart, _gapFracEnd, eraFrac)!;
      for (var i = 0; i < gatesPerEra; i++) {
        // A small extra squeeze across an era, so each one has its own arc
        // rather than being four gates at one difficulty.
        final gapH = baseGap * (1 - 0.02 * i);
        final half = gapH / 2;
        final lo = _h * 0.06 + half;
        final hi = _h * 0.94 - half;
        // Cap the step between consecutive gates. Without this the generator
        // will eventually put a gap at the top immediately after one at the
        // bottom, which is not hard, it is impossible.
        final step = _h * 0.26;
        final want = lastGapY + (rnd.nextDouble() * 2 - 1) * step;
        final gapY = want.clamp(lo, hi);
        lastGapY = gapY;
        gates.add(_Gate(
          worldX: _leadIn + era * block + i * _spacing,
          gapY: gapY,
          gapH: gapH,
          era: era,
        ));
      }
    }
    _gates = gates;
    _lastGateX = gates.last.worldX;
    _totalX = _lastGateX + _calmRun;

    // Coins. A short trail in the lead-in teaches the pickup before the first
    // gate; then one gate coin in every opening and a trail across every
    // stretch of open air. Nothing after the last gate: the calm stretch is a
    // release, and a coin there would be one more thing to chase.
    final pickups = <Pickup>[];
    for (var k = 0; k < 4; k++) {
      pickups.add(Pickup(
        worldX: _leadIn * (0.42 + k * 0.13),
        y: _h * (0.45 + 0.03 * sin(k * 1.9)),
        kind: PickupKind.copper,
      ));
    }
    for (var i = 0; i < gates.length; i++) {
      final g = gates[i];
      // The gold coin drifts the full height of the opening, half a coin
      // clear of either lip at the extremes. Even gates start at the top,
      // odd gates at the bottom, so consecutive coins are always moving in
      // opposite directions when you reach them. The risk scales itself: in
      // a wide early gap the extremes are well off centre, in the tightest
      // late gap they are barely off it.
      pickups.add(Pickup(
        worldX: g.worldX,
        y: g.gapY,
        amp: g.gapH / 2 - _coinR * 1.35,
        phase: i.isEven ? -pi / 2 : pi / 2,
        kind: PickupKind.gold,
      ));
      if (i + 1 < gates.length) {
        final n = gates[i + 1];
        final bulge = (rnd.nextBool() ? 1 : -1) * _h * 0.11;
        for (var k = 0; k < 4; k++) {
          final t = 0.30 + k * 0.15;
          final arc = sin((t - 0.30) / 0.45 * pi);
          pickups.add(Pickup(
            worldX: lerpDouble(g.worldX, n.worldX, t)!,
            y: (lerpDouble(g.gapY, n.gapY, t)! + bulge * arc).clamp(_h * 0.09, _h * 0.91),
            // Silver at the peak of the arc, copper at its ends: the coins
            // furthest off the straight line are the ones worth bending for.
            kind: k == 1 || k == 2 ? PickupKind.silver : PickupKind.copper,
          ));
        }
      }
    }
    _pickups = pickups;
  }

  /// Scroll speed at the current point of the passage. Rises gently — the
  /// ramp is in the gaps, not mainly in the speed, because speed is the one
  /// that makes a game unreadable rather than hard.
  double get _speed => _w * (0.52 + 0.20 * progress) * speedFactor;

  int _eraFor(double x) {
    final block = gatesPerEra * _spacing + _eraGap;
    final i = ((x - _leadIn + _spacing * 0.8) / block).floor();
    return i.clamp(0, eras.length - 1);
  }

  // ---------------------------------------------------------------- input

  /// One tap. The entire control scheme.
  void flap() {
    if (phase == PassagePhase.down || run.ended) return;
    if (!_started) {
      _started = true;
      run.tick();
    }
    _vy = _flapImpulse * _lift;
    _flapAt = _t;
    Audio.instance.tap();
  }

  // --------------------------------------------------------------- update

  @override
  void update(double dt) {
    super.update(dt);
    if (!_laidOut || run.ended) return;

    // Show the first era as soon as there is a viewport, rather than waiting
    // for the first tap: the coin hovers precisely so there is time to read
    // it, which only works if there is something to read.
    //
    // This belongs here and not in [onGameResize], which is where it was
    // first written. Flame drives onGameResize from inside a LayoutBuilder
    // callback — that is, during the build phase — so notifying a
    // ValueNotifier there calls setState on a widget mid-build. Flutter
    // throws, the notification is dropped, and in a release build the
    // exception is invisible: the banner simply never appeared, with analyze
    // and every test still green. The game loop is the safe place to notify,
    // which is why the HUD's `run.tick()` has always worked.
    if (eraNotifier.value < 0) {
      eraNotifier.value = 0;
      run.tick();
    }

    // A long frame must never teleport the coin through a pillar. After a
    // resume from background, or a bad jank spike, dt can be hundreds of
    // milliseconds; at that size the swept position skips the gate entirely
    // and a hit reads as a phantom miss.
    dt = min(dt, 1 / 30);
    _t += dt;
    _wingPhase += dt * _wingRate;
    if (_strikeFlash > 0) _strikeFlash = max(0, _strikeFlash - dt * 2.2);

    if (!_started) {
      // Idle hover while the first banner is read. Nothing advances.
      _coinY = _h * 0.45 + sin(_t * 2.2) * _h * 0.012;
      _pushTrail();
      return;
    }

    switch (phase) {
      case PassagePhase.flying:
        _updateFlying(dt);
      case PassagePhase.descending:
        _updateSettling(dt, riseTime: 1.4, liftFloor: 0.0, liftTime: 1.2, drag: 1.6);
      case PassagePhase.landing:
        _updateSettling(dt, riseTime: 3.2, liftFloor: 0.35, liftTime: 5.0, drag: 0.35);
      case PassagePhase.down:
        _updateDown(dt);
    }
    if (phase != PassagePhase.down) _updateCoins(dt);
    for (final p in _pops) {
      p.age += dt;
    }
    _pops.removeWhere((p) => p.age > 0.45);
    _pushTrail();
  }

  /// Pickups, spilled coins and momentum decay. Runs in every phase but the
  /// roll-out, so a spill from a last strike can still be caught on the way
  /// down.
  void _updateCoins(double dt) {
    if (momentum > 0) momentum = max(0.0, momentum - momentumDecayPerSecond * dt);

    for (final p in _pickups) {
      if (p.taken) continue;
      final dx = p.worldX - scrollX;
      if (dx < -_w * 0.4 || dx > _w) continue;
      final sx = _coinX + dx;
      if (_touches(sx, p.yAt(_t), _pickR(p.kind))) _collect(p, sx);
    }

    for (final s in _spills) {
      s.age += dt;
      s.vy += _gravity * 0.5 * dt;
      s.y += s.vy * dt;
      s.worldX += s.vx * dt;
      final sx = _coinX + (s.worldX - scrollX);
      if (!s.taken && _touches(sx, s.y, _coinR * 0.6)) {
        // Recovered at face value, no multiplier: getting it back is not the
        // same as having flown for it.
        s.taken = true;
        score += 1;
        coinsTaken++;
        _pops.add(_Pop(Offset(sx, s.y), false));
        Audio.instance.coinFlip();
        run.tick();
      }
    }
    _spills.removeWhere((s) => s.taken || s.age > _spillLife || s.y > _h * 1.05);
  }

  bool _touches(double x, double y, double r) {
    final dx = x - _coinX, dy = y - _coinY, rr = r + _coinR;
    return dx * dx + dy * dy < rr * rr;
  }

  double _pickR(PickupKind k) => _coinR * (k == PickupKind.gold ? 0.85 : 0.6);

  void _collect(Pickup p, double sx) {
    if (p.taken) return;
    p.taken = true;
    coinsTaken++;
    // The multiplier is read before this coin feeds momentum, so the coin
    // that crosses a tier line pays at the tier it was taken in.
    score += p.value * multiplier;
    momentum = min(1.0, momentum + p.momentumGain);
    _pops.add(_Pop(Offset(sx, p.yAt(_t)), p.kind == PickupKind.gold));
    if (p.kind == PickupKind.gold) {
      Audio.instance.coinSpin();
    } else {
      Audio.instance.coinFlip();
    }
    run.tick();
  }

  void _updateFlying(double dt) {
    scrollX += _speed * dt;
    _integrate(dt);

    final era = _eraFor(scrollX);
    if (era != eraNotifier.value) {
      eraNotifier.value = era;
      Audio.instance.sealStrip();
      run.tick();
    }

    for (final g in _gates) {
      final dx = g.worldX - scrollX;
      if (dx < -_gateW && !g.passed) {
        g.passed = true;
        gatesCleared++;
        if (gatesCleared % gatesPerEra == 0) erasCleared = gatesCleared ~/ gatesPerEra;
        Audio.instance.ting();
        run.tick();
      }
      if (reserve > 0 && !g.struck && _t > _invUntil && dx.abs() < _gateW) {
        if (_hits(g)) _strike(g);
      }
    }

    if (scrollX >= _totalX) _enter(PassagePhase.landing);
  }

  /// Shared tail for both endings: lift authority decays, the ground rises,
  /// and the coin sets down. The two differ only in how fast, which is the
  /// whole difference between "you ran out" and "you arrived".
  void _updateSettling(
    double dt, {
    required double riseTime,
    required double liftFloor,
    required double liftTime,
    required double drag,
  }) {
    _phaseT += dt;
    _lift = lerpDouble(1, liftFloor, _easeOut((_phaseT / liftTime).clamp(0.0, 1.0)))!;
    scrollX += _speed * dt * max(0.0, 1 - _phaseT * drag / 2);

    final rise = _easeOut((_phaseT / riseTime).clamp(0.0, 1.0));
    _groundY = lerpDouble(_skyFloor, _groundAt, rise)!;
    // Once it has arrived it keeps creeping, so that someone tapping as fast
    // as they physically can still touches down inside a few seconds rather
    // than hovering out the clock.
    if (rise >= 1) _groundY -= _h * 0.014 * dt * (_phaseT - riseTime);

    _integrate(dt, ceilingOnly: true);

    if (_coinY + _coinR >= _groundY) {
      touchdownSpeed = _vy / _h;
      _coinY = _groundY - _coinR;
      _vy = 0;
      _enter(PassagePhase.down);
      _onTouchdown();
    }
  }

  void _updateDown(double dt) {
    _phaseT += dt;
    // Roll to a stop.
    scrollX += _speed * dt * max(0.0, 1 - _phaseT * 1.4);
    _coinY = _groundY - _coinR;
    if (_phaseT > 1.5) _finish();
  }

  /// Gravity and the ceiling. [ceilingOnly] skips the soft floor, which only
  /// applies while there are still gates to fly.
  void _integrate(double dt, {bool ceilingOnly = false}) {
    _vy = (_vy + _gravity * dt).clamp(-_vMax, _vMax);
    _coinY += _vy * dt;

    final ceiling = _coinR * 1.2;
    if (_coinY < ceiling) {
      // Not a penalty. Clipping the ceiling in a flyer is usually a player
      // who over-tapped, and charging them for it is a hidden death.
      _coinY = ceiling;
      if (_vy < 0) _vy = 0;
    }
    if (ceilingOnly) return;

    final floor = _h * 0.94 - _coinR;
    if (_coinY > floor) {
      _coinY = floor;
      if (_vy > 0) _vy = 0;
      if (reserve > 0 && _t > _invUntil) _strike(null);
    }
  }

  bool _hits(_Gate g) {
    final gx = _coinX + (g.worldX - scrollX);
    final left = gx - _gateW / 2, right = gx + _gateW / 2;
    final top = g.gapY - g.gapH / 2, bottom = g.gapY + g.gapH / 2;
    bool overlaps(double ry0, double ry1) {
      final cx = _coinX.clamp(left, right);
      final cy = _coinY.clamp(ry0, ry1);
      final dx = _coinX - cx, dy = _coinY - cy;
      return dx * dx + dy * dy < _coinR * _coinR;
    }

    return overlaps(0, top) || overlaps(bottom, _h);
  }

  /// Wingbeats per second, in frames of the four-frame cycle. Idle hover is
  /// lazy, flight is steady, a fresh flap is a hard burst, and a descent is
  /// a slow glide — the wings are the one place the boar says how it feels.
  double get _wingRate {
    if (!_started) return 5;
    if (phase == PassagePhase.down) return 0;
    if (phase == PassagePhase.descending) return 4;
    return _t - _flapAt < 0.28 ? 20 : 8;
  }

  /// A strike costs a unit of reserve and knocks the coin down. It does not
  /// end the run, and there is no lose sting anywhere in this game.
  void _strike(_Gate? g) {
    g?.struck = true;
    reserve--;
    _invUntil = _t + _invulnerableFor;
    _hurtUntil = _t + 0.35;
    _vy = _h * 0.26;
    _strikeFlash = 1;
    Audio.instance.vaultHit();
    HapticFeedback.mediumImpact();

    // Momentum goes, and a handful of points come loose as coins. They are
    // thrown up and ahead with a little less forward speed than the world,
    // so on screen they arc up and drift back toward the coin: catchable by
    // a player who taps up into them, gone if they do not.
    momentum = 0;
    final spill = min(spillOnStrike, score);
    score -= spill;
    for (var i = 0; i < spill; i++) {
      _spills.add(_Spill(
        scrollX + _coinR * (1.5 + i * 0.9),
        _coinY,
        _speed * (0.55 + _rnd.nextDouble() * 0.35),
        -_h * (0.42 + _rnd.nextDouble() * 0.30),
      ));
    }
    if (spill > 0) Audio.instance.coinsPour();

    run.tick();
    if (reserve <= 0) _enter(PassagePhase.descending);
  }

  void _enter(PassagePhase p) {
    if (phase == p) return;
    phase = p;
    _phaseT = 0;
    if (p == PassagePhase.landing) Audio.instance.coinRoll();
    run.tick();
  }

  void _onTouchdown() {
    final full = erasCleared >= eras.length;
    if (full && softLanding) {
      Audio.instance.win();
      Audio.instance.voWinner();
      HapticFeedback.heavyImpact();
    } else if (full) {
      Audio.instance.ingotLand();
      HapticFeedback.mediumImpact();
    } else {
      // Deliberately not `lose()`. Setting down early is a shorter journey,
      // not a failure, and the audio is the strongest signal of which of
      // those two things just happened.
      Audio.instance.land();
    }
    run.tick();
  }

  /// 0..3 — see the star rule in the class comment.
  int get stars {
    if (erasCleared < eras.length) return 1;
    return softLanding ? 3 : 2;
  }

  void _finish() {
    run.end(RunResult(
      ending: erasCleared >= eras.length ? RunEnding.landed : RunEnding.short,
      stars: stars,
      reached: erasReached,
      total: eras.length,
      score: score,
    ));
  }

  void _pushTrail() {
    _trail.add(Offset(scrollX, _coinY));
    final keep = 14 + (12 * momentum).round();
    while (_trail.length > keep) {
      _trail.removeAt(0);
    }
  }

  // ------------------------------------------------------------- DEV only
  //
  // A full passage is seventy seconds. Checking the landing — the part the
  // whole design turns on — should not cost seventy seconds every time.

  /// Jumps to the calm stretch with the passage flown, so the landing can be
  /// looked at on its own.
  void devSkipToLanding() {
    if (!_laidOut) return;
    _started = true;
    for (final g in _gates) {
      g.passed = true;
    }
    gatesCleared = _gates.length;
    erasCleared = eras.length;
    eraNotifier.value = eras.length - 1;
    scrollX = _totalX - _w * 0.35;
    run.tick();
  }

  /// Cycles the boar through its three stages, mid-run.
  BoarStage devNextStage() {
    stage = BoarStage.values[(stage.index + 1) % BoarStage.values.length];
    run.tick();
    return stage;
  }

  /// Full momentum, to look at the fast passage without earning it.
  void devMaxMomentum() {
    momentum = 1;
    run.tick();
  }

  /// Forces the short ending from wherever the coin currently is.
  void devEndShort() {
    if (!_laidOut) return;
    _started = true;
    reserve = 0;
    _enter(PassagePhase.descending);
  }

  @override
  void render(Canvas canvas) {
    super.render(canvas);
    renderWorld(canvas);
  }

  @override
  void onRemove() {
    eraNotifier.dispose();
    super.onRemove();
  }
}

/// A cubic ease-out, inlined so this file does not depend on the animation
/// library for one curve.
double _easeOut(double t) => 1 - pow(1 - t, 3).toDouble();
