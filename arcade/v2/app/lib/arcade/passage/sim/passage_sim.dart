/// When Pigs Fly's simulation: everything that decides a run's outcome, and
/// nothing that draws it.
///
/// Split out of `passage_game.dart` so the same code can run in three places:
/// the phone (inside the Flame game, as before), the browser (the web
/// arcade, same), and the web arcade's server, which replays a run from its
/// seed and the recorded taps to find out what the score really was. For
/// that to work the simulation must be a pure function of
///
///   (seed, viewport size, boar body, loadout, the tick of every input)
///
/// so it follows three rules, all enforced by tests:
///
///  1. **Fixed step.** It only ever advances by [step]. The game accumulates
///     frame time and steps in whole ticks, so frame rate and jank change
///     how smoothly it is drawn, never where the boar goes.
///  2. **Seeded.** Every random number comes from generators seeded by
///     [seed]. There is no clock and no `Random()`.
///  3. **Exact arithmetic only.** No `sin`, `cos` or `pow` from `dart:math`,
///     whose last bit differs between JavaScript engines; see `dmath.dart`.
///
/// The game design is unchanged and is described at length in
/// `passage_game.dart`, which also holds the rendering, audio and haptics.
/// This file raises [SimEvent]s where those used to be called inline.
library;

import 'dart:math' show Random, max, min;

import '../eras.dart' show eras, gatesPerEra;
import 'ability_rules.dart';
import 'dmath.dart';

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

/// Something the coin can pick up. See `passage_game.dart` for why three.
enum PickupKind { copper, silver, gold }

class SimGate {
  /// Distance from the start of the passage to this gate's centre line.
  final double worldX;

  /// Centre of the opening, in pixels from the top.
  final double gapY;

  /// Height of the opening, in pixels.
  final double gapH;

  /// Index into [eras].
  final int era;

  /// Already counted towards `gatesCleared`.
  bool passed = false;

  /// Already charged a unit of reserve. A coin that clips a pillar stays
  /// overlapping it for several ticks; without this it would be charged on
  /// every one of them.
  bool struck = false;

  /// Owned by the renderer (a recorded picture of the gate). The simulation
  /// never reads it.
  Object? renderCache;

  SimGate({required this.worldX, required this.gapY, required this.gapH, required this.era});
}

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

  /// Tractor beam: 0..1 while being drawn to the boar, null otherwise.
  double? pull;

  /// Where the coin was when the beam caught it, in world x and screen y.
  double pullX = 0, pullY = 0;

  Pickup({required this.worldX, required this.y, required this.kind, this.amp = 0, this.phase = 0});

  // The coin's own drift clock. It runs with game time until a freeze shot
  // stops it, holds while frozen, and resumes from where it stopped — so a
  // thawed coin carries on from its frozen height instead of jumping to
  // wherever it would have drifted to meanwhile.
  double _clockBase = 0, _clockResume = 0;
  double _localT(double t) => _clockBase + max(0.0, t - _clockResume);

  /// Game time at which a frozen coin starts drifting again.
  double get clockResume => _clockResume;

  /// Stops this coin's drift for [seconds] from game time [t].
  void freezeAt(double t, double seconds) {
    _clockBase = _localT(t);
    _clockResume = t + seconds;
  }

  bool frozenAt(double t) => t < _clockResume;

  /// Where the coin is at game time [t].
  double yAt(double t) => amp == 0 ? y : y + amp * dsin(phase + _localT(t) * PassageSim.driftRadPerSecond);

  int get value => switch (kind) {
        PickupKind.copper => PassageSim.copperValue,
        PickupKind.silver => PassageSim.silverValue,
        PickupKind.gold => PassageSim.goldValue,
      };

  double get momentumGain => switch (kind) {
        PickupKind.copper => PassageSim.momentumPerCopper,
        PickupKind.silver => PassageSim.momentumPerSilver,
        PickupKind.gold => PassageSim.momentumPerGold,
      };
}

/// A coin knocked loose by a strike. It arcs up, falls under gravity, drifts
/// back toward the player on screen, and can be caught again for a moment.
class SimSpill {
  double worldX, y, vx, vy;
  double age = 0;
  bool taken = false;
  SimSpill(this.worldX, this.y, this.vx, this.vy);
}

/// A coin spat by the freeze shot, flying at a gold coin ahead.
class SimShot {
  double worldX, y;
  final Pickup target;
  SimShot(this.worldX, this.y, this.target);
}

enum SimEventKind {
  /// The first flap. The run's clock is now running.
  started,
  flap,

  /// [SimEvent.value] is the new era index.
  eraChanged,
  gatePassed,

  /// A pickup taken at ([SimEvent.x], [SimEvent.y]) on screen.
  collected,

  /// A spilled coin caught again.
  recovered,

  /// [SimEvent.value] is how many points came loose.
  struck,

  /// [SimEvent.phase] is the phase entered.
  phaseChanged,

  /// [SimEvent.value]: 0 short, 1 full passage, 2 full and soft.
  touchdown,
  finished,

  /// [SimEvent.ability] fired. For a blink, [SimEvent.y] is where it left.
  ability,

  /// A freeze shot reached its coin, at ([SimEvent.x], [SimEvent.y]).
  frozeCoin,

  /// A cooldown ran out or a grapple let go: repaint the buttons.
  slotChanged,
}

class SimEvent {
  final SimEventKind kind;
  final double x, y;
  final int value;
  final PickupKind? pickup;
  final AbilityKind? ability;
  final PassagePhase? phase;
  const SimEvent(this.kind, {this.x = 0, this.y = 0, this.value = 0, this.pickup, this.ability, this.phase});
}

/// Input codes in a transcript: `[tick, code]`.
abstract final class SimInput {
  static const flap = 0;
  static const ability0 = 1;
  static const ability1 = 2;
}

/// The difficulty knobs: how wide the openings are at the first era and the
/// last, how fast the passage scrolls and how much faster it gets, and the
/// reserve. [standard] is the game; [easy] is a DEV-only variant for judging
/// whether the standard passage is too hard (TEN-GAMES.md, "An easier
/// variant"), and is never submitted anywhere (see [PassageSim.tainted]).
class PassageTuning {
  final String id;
  final double gapFracStart, gapFracEnd;
  final double speedBase, speedRamp;
  final int reserve;

  const PassageTuning({
    required this.id,
    required this.gapFracStart,
    required this.gapFracEnd,
    required this.speedBase,
    required this.speedRamp,
    required this.reserve,
  });

  static const standard = PassageTuning(
    id: 'standard',
    gapFracStart: 0.36,
    gapFracEnd: 0.225,
    speedBase: 0.52,
    speedRamp: 0.20,
    reserve: 3,
  );

  static const easy = PassageTuning(
    id: 'easy',
    gapFracStart: 0.40,
    gapFracEnd: 0.32,
    speedBase: 0.48,
    speedRamp: 0.06,
    reserve: 5,
  );
}

class PassageSim {
  /// The only step the simulation ever takes: 120 ticks a second.
  static const double step = 1 / 120;

  // ------------------------------------------------------------ tuning
  // Unchanged from the Flame version; see passage_game.dart for the why.

  /// The standard reserve. A run's own is [tuning].reserve.
  static const startingReserve = 3;
  static const _invulnerableFor = 1.1;

  static const copperValue = 1;
  static const silverValue = 3;
  static const goldValue = 10;
  static const momentumPerCopper = 0.05;
  static const momentumPerSilver = 0.08;
  static const momentumPerGold = 0.16;
  static const driftRadPerSecond = 2 * dPi / 2.4;
  static const momentumDecayPerSecond = 0.03;
  static const maxSpeedBoost = 0.35;
  static const spillOnStrike = 4;
  static const spillLife = 2.6;
  static const softLandingAt = 0.42;
  static const _scrapeWindow = 1.5;
  static const playTop = 0.12;
  static const dashSpeed = 2.2;
  static const grappleSpeed = 1.5;
  static const grappleSpring = 9.0;
  static const _shotSpeed = 1.8;
  static const pullTime = 0.22;

  // ------------------------------------------------------------ inputs

  final double w, h;
  final int seed;

  /// The boar's collision capsule, in radii of the old coin (see BoarSpec).
  /// Fixed for a run; only [devSetBody] changes it, and that taints the run.
  double bodyRadiusK, bodyHalfLengthK;

  final List<AbilitySlot> slots;

  /// Raised where the Flame version played a sound, buzzed, or asked the
  /// HUD to repaint.
  void Function(SimEvent e)? onEvent;

  /// Every input that changed the run, as `[tick, code]` (see [SimInput]).
  /// This, the seed and the loadout are the whole transcript.
  final List<List<int>> inputs = [];

  /// The difficulty this run flies at. Part of the transcript: a replay
  /// has to be given the same tuning to reach the same result.
  final PassageTuning tuning;

  /// Set by any DEV or test shortcut that moves state directly, and by any
  /// tuning but the standard one. A tainted run is not submitted by the web
  /// arcade; one moved by a shortcut cannot be replayed either.
  bool tainted;

  PassageSim({
    required this.w,
    required this.h,
    required this.seed,
    this.bodyRadiusK = 0.9,
    required this.bodyHalfLengthK,
    List<EquippedAbility> loadout = const [],
    this.onEvent,
    this.tuning = PassageTuning.standard,
  })  : slots = [for (final a in loadout.take(2)) AbilitySlot(a)],
        _spillRnd = Random(seed ^ 0x2545F491),
        reserve = tuning.reserve,
        tainted = !identical(tuning, PassageTuning.standard) {
    _layout();
    coinY = h * 0.45;
    groundY = _skyFloor;
  }

  final Random _spillRnd;

  // ------------------------------------------------------------- state

  late List<SimGate> gates;
  late List<Pickup> pickups;
  final List<SimSpill> spills = [];

  int ticks = 0;
  double t = 0;
  double scrollX = 0;
  double coinY = 0;
  double vy = 0;
  double invUntil = -1;
  double lift = 1;
  double groundY = 0;
  double phaseT = 0;
  double _creep = 0;
  PassagePhase phase = PassagePhase.flying;

  int reserve;
  int gatesCleared = 0;
  int erasCleared = 0;
  int eraIndex = 0;

  double touchdownSpeed = 0;
  bool touchdownScraped = false;
  double floorAt = -10;

  int score = 0;
  int coinsTaken = 0;
  double momentum = 0;

  bool started = false;
  bool finished = false;

  double totalX = 0;
  double lastGateX = 0;

  // Ability state.
  double dashUntil = -1;
  double immuneUntil = -1;
  Pickup? grapple;
  double grappleUntil = -1;
  SimShot? shot;
  double tractorUntil = -1;
  double tractorReach = 0;

  // ------------------------------------------------------------ derived

  double get coinR => h * 0.026;
  double get coinX => w * 0.30;
  double get gravity => h * 2.35;
  double get flapImpulse => -h * 0.60;
  double get vMax => h * 1.05;
  double get spacing => w * 0.85;
  double get leadIn => w * 1.15;
  double get eraGap => spacing * 0.9;
  double get gateW => w * 0.085;
  double get calmRun => w * 2.4;
  double get _skyFloor => h * 1.3;
  double get _groundAt => h * 0.87;
  double get playTopPx => h * playTop;
  double get _groundStart => h * 0.94;
  double get bodyR => coinR * bodyRadiusK;
  double get bodyL => coinR * bodyHalfLengthK;

  bool get vulnerable => t > invUntil && t > immuneUntil && grapple == null;
  double get abilitySpeed => t < dashUntil ? dashSpeed : (grapple != null ? grappleSpeed : 1.0);
  bool get dashing => t < dashUntil;
  bool get grappling => grapple != null;
  bool get tractoring => t < tractorUntil;

  double get speedFactor => 1 + maxSpeedBoost * momentum;
  int get multiplier => momentum >= 0.98 ? 3 : (momentum >= 0.5 ? 2 : 1);
  double get progress => totalX == 0 ? 0 : (scrollX / totalX).clamp(0.0, 1.0);
  double get speed => w * (tuning.speedBase + tuning.speedRamp * progress) * speedFactor * abilitySpeed;

  int get erasReached => started ? (eraIndex + 1).clamp(0, eras.length) : 0;
  bool get softLanding => touchdownSpeed.abs() < softLandingAt && !touchdownScraped;
  int get stars {
    if (erasCleared < eras.length) return 1;
    return softLanding ? 3 : 2;
  }

  double pickR(PickupKind k) => coinR * (k == PickupKind.gold ? 0.85 : 0.6);

  int eraFor(double x) {
    final block = gatesPerEra * spacing + eraGap;
    final i = ((x - leadIn + spacing * 0.8) / block).floor();
    return i.clamp(0, eras.length - 1);
  }

  void _emit(SimEvent e) => onEvent?.call(e);

  // ------------------------------------------------------------- layout

  void _layout() {
    final rnd = Random(seed);
    final out = <SimGate>[];
    final block = gatesPerEra * spacing + eraGap;
    var lastGapY = h * 0.5;

    for (var era = 0; era < eras.length; era++) {
      final eraFrac = eras.length == 1 ? 0.0 : era / (eras.length - 1);
      final baseGap = h * lerp(tuning.gapFracStart, tuning.gapFracEnd, eraFrac);
      for (var i = 0; i < gatesPerEra; i++) {
        final gapH = baseGap * (1 - 0.02 * i);
        final half = gapH / 2;
        final lo = playTopPx + half;
        final hi = h * 0.94 - half;
        final step = h * 0.26;
        final want = lastGapY + (rnd.nextDouble() * 2 - 1) * step;
        final gapY = want.clamp(lo, hi);
        lastGapY = gapY;
        out.add(SimGate(worldX: leadIn + era * block + i * spacing, gapY: gapY, gapH: gapH, era: era));
      }
    }
    gates = out;
    lastGateX = out.last.worldX;
    totalX = lastGateX + calmRun;

    final p = <Pickup>[];
    for (var k = 0; k < 4; k++) {
      p.add(Pickup(
        worldX: leadIn * (0.42 + k * 0.13),
        y: h * (0.45 + 0.03 * dsin(k * 1.9)),
        kind: PickupKind.copper,
      ));
    }
    for (var i = 0; i < out.length; i++) {
      final g = out[i];
      p.add(Pickup(
        worldX: g.worldX,
        y: g.gapY,
        amp: g.gapH / 2 - coinR * 1.35,
        phase: i.isEven ? -dPi / 2 : dPi / 2,
        kind: PickupKind.gold,
      ));
      if (i + 1 < out.length) {
        final n = out[i + 1];
        final bulge = (rnd.nextBool() ? 1 : -1) * h * 0.11;
        for (var k = 0; k < 4; k++) {
          final f = 0.30 + k * 0.15;
          final arc = dsin((f - 0.30) / 0.45 * dPi);
          p.add(Pickup(
            worldX: lerp(g.worldX, n.worldX, f),
            y: (lerp(g.gapY, n.gapY, f) + bulge * arc).clamp(playTopPx + h * 0.03, h * 0.91),
            kind: k == 1 || k == 2 ? PickupKind.silver : PickupKind.copper,
          ));
        }
      }
    }
    pickups = p;
  }

  // ---------------------------------------------------------------- input

  /// One tap. The entire control scheme. False if it did nothing.
  bool flap() {
    if (phase == PassagePhase.down || finished) return false;
    if (!started) {
      started = true;
      _emit(const SimEvent(SimEventKind.started));
    }
    vy = flapImpulse * lift;
    grapple = null;
    inputs.add([ticks, SimInput.flap]);
    _emit(const SimEvent(SimEventKind.flap));
    return true;
  }

  // ---------------------------------------------------------------- step

  /// Advances one tick. [dt] must be [step]; the parameter exists so a test
  /// can say so explicitly.
  void advance([double dt = step]) {
    if (finished) return;
    t += dt;
    if (started) _updateAbilities(dt);
    if (!started) {
      // Idle hover while the first banner is read. Nothing advances.
      coinY = h * 0.45 + dsin(t * 2.2) * h * 0.012;
      ticks++;
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
    ticks++;
  }

  void _updateCoins(double dt) {
    if (momentum > 0) momentum = max(0.0, momentum - momentumDecayPerSecond * dt);

    _updateTractor(dt);
    for (final p in pickups) {
      if (p.taken || p.pull != null) continue;
      final dx = p.worldX - scrollX;
      if (dx < -w * 0.4 || dx > w) continue;
      final sx = coinX + dx;
      if (_touches(sx, p.yAt(t), pickR(p.kind))) collect(p, sx);
    }

    for (final s in spills) {
      s.age += dt;
      s.vy += gravity * 0.5 * dt;
      s.y += s.vy * dt;
      s.worldX += s.vx * dt;
      final sx = coinX + (s.worldX - scrollX);
      if (!s.taken && _touches(sx, s.y, coinR * 0.6)) {
        s.taken = true;
        score += 1;
        coinsTaken++;
        _emit(SimEvent(SimEventKind.recovered, x: sx, y: s.y));
      }
    }
    spills.removeWhere((s) => s.taken || s.age > spillLife || s.y > h * 1.05);
  }

  bool _touches(double x, double y, double r) {
    final cx = x.clamp(coinX - bodyL, coinX + bodyL);
    final dx = x - cx, dy = y - coinY, rr = r + bodyR;
    return dx * dx + dy * dy < rr * rr;
  }

  /// Takes [p]. [sx] is its screen x, for the pop.
  void collect(Pickup p, double sx) {
    if (p.taken) return;
    p.taken = true;
    coinsTaken++;
    // The multiplier is read before this coin feeds momentum, so the coin
    // that crosses a tier line pays at the tier it was taken in.
    score += p.value * multiplier;
    momentum = min(1.0, momentum + p.momentumGain);
    _emit(SimEvent(SimEventKind.collected, x: sx, y: p.pull != null ? coinY : p.yAt(t), pickup: p.kind));
  }

  void _updateFlying(double dt) {
    scrollX += speed * dt;
    _integrate(dt);

    final era = eraFor(scrollX);
    if (era != eraIndex) {
      eraIndex = era;
      _emit(SimEvent(SimEventKind.eraChanged, value: era));
    }

    for (final g in gates) {
      final dx = g.worldX - scrollX;
      if (dx < -gateW && !g.passed) {
        g.passed = true;
        gatesCleared++;
        if (gatesCleared % gatesPerEra == 0) erasCleared = gatesCleared ~/ gatesPerEra;
        _emit(const SimEvent(SimEventKind.gatePassed));
      }
      if (reserve > 0 && !g.struck && vulnerable && dx.abs() < gateW / 2 + bodyL + bodyR) {
        if (_hits(g)) strike(g);
      }
    }

    if (scrollX >= totalX) _enter(PassagePhase.landing);
  }

  void _updateSettling(
    double dt, {
    required double riseTime,
    required double liftFloor,
    required double liftTime,
    required double drag,
  }) {
    phaseT += dt;
    lift = lerp(1, liftFloor, easeOut((phaseT / liftTime).clamp(0.0, 1.0)));
    scrollX += speed * dt * max(0.0, 1 - phaseT * drag / 2);

    final rise = easeOut((phaseT / riseTime).clamp(0.0, 1.0));
    if (rise >= 1) _creep += h * 0.014 * dt * (phaseT - riseTime);
    groundY = lerp(_groundStart, _groundAt, rise) - _creep;

    _integrate(dt, ceilingOnly: true);

    if (coinY + bodyR >= groundY) {
      touchdownSpeed = vy / h;
      touchdownScraped = t - floorAt < _scrapeWindow;
      coinY = groundY - bodyR;
      vy = 0;
      _enter(PassagePhase.down);
      final full = erasCleared >= eras.length;
      _emit(SimEvent(SimEventKind.touchdown, value: full ? (softLanding ? 2 : 1) : 0));
    }
  }

  void _updateDown(double dt) {
    phaseT += dt;
    scrollX += speed * dt * max(0.0, 1 - phaseT * 1.4);
    coinY = groundY - bodyR;
    if (phaseT > 1.5) {
      finished = true;
      _emit(const SimEvent(SimEventKind.finished));
    }
  }

  void _integrate(double dt, {bool ceilingOnly = false}) {
    final hook = grapple;
    if (t < dashUntil) {
      vy = 0; // a dash holds altitude
    } else if (hook != null) {
      vy = ((hook.yAt(t) - coinY) * grappleSpring).clamp(-vMax, vMax);
    } else {
      vy = (vy + gravity * dt).clamp(-vMax, vMax);
    }
    coinY += vy * dt;

    final ceiling = playTopPx + bodyR;
    if (coinY < ceiling) {
      coinY = ceiling;
      if (vy < 0) vy = 0;
    }
    if (ceilingOnly) return;

    final floor = h * 0.94 - bodyR;
    if (coinY > floor) {
      coinY = floor;
      floorAt = t;
      if (vy > 0) vy = 0;
      if (reserve > 0 && vulnerable) strike(null);
    }
  }

  bool _hits(SimGate g) {
    final gx = coinX + (g.worldX - scrollX);
    final left = gx - gateW / 2, right = gx + gateW / 2;
    final top = g.gapY - g.gapH / 2, bottom = g.gapY + g.gapH / 2;
    bool overlaps(double ry0, double ry1) {
      final dx = max(0.0, max(left - (coinX + bodyL), (coinX - bodyL) - right));
      final dy = max(0.0, max(ry0 - coinY, coinY - ry1));
      return dx * dx + dy * dy < bodyR * bodyR;
    }

    return overlaps(0, top) || overlaps(bottom, h);
  }

  /// A strike costs a unit of reserve and knocks the coin down. It does not
  /// end the run.
  void strike(SimGate? g) {
    g?.struck = true;
    reserve--;
    invUntil = t + _invulnerableFor;
    vy = h * 0.26;
    momentum = 0;
    final spill = min(spillOnStrike, score);
    score -= spill;
    for (var i = 0; i < spill; i++) {
      spills.add(SimSpill(
        scrollX + coinR * (1.5 + i * 0.9),
        coinY,
        speed * (0.55 + _spillRnd.nextDouble() * 0.35),
        -h * (0.42 + _spillRnd.nextDouble() * 0.30),
      ));
    }
    _emit(SimEvent(SimEventKind.struck, value: spill));
    if (reserve <= 0) _enter(PassagePhase.descending);
  }

  void _enter(PassagePhase p) {
    if (phase == p) return;
    phase = p;
    phaseT = 0;
    _creep = 0;
    _emit(SimEvent(SimEventKind.phaseChanged, phase: p));
  }

  // ------------------------------------------------------------ abilities
  // The rules each keeps are described in passage_abilities.dart.

  bool canUse(int i) {
    if (i < 0 || i >= slots.length) return false;
    if (!started || phase != PassagePhase.flying || finished) return false;
    final s = slots[i];
    if (s.cooldownLeft > 0 || s.spent) return false;
    return switch (s.ability.kind) {
      AbilityKind.dash => t >= dashUntil,
      AbilityKind.grapple => grapple == null && goldAhead(s.stats.reach * w) != null,
      AbilityKind.teleport => nextGate() != null,
      AbilityKind.freeze => shot == null && goldAhead(w * 1.4) != null,
      AbilityKind.tractor => t >= tractorUntil,
    };
  }

  bool use(int i) {
    if (!canUse(i)) return false;
    final s = slots[i];
    final st = s.stats;
    var fromY = coinY;
    switch (s.ability.kind) {
      case AbilityKind.dash:
        dashUntil = t + st.duration;
        immuneUntil = max(immuneUntil, t + st.immunity);
        vy = 0;
      case AbilityKind.grapple:
        grapple = goldAhead(st.reach * w);
        grappleUntil = t + st.duration;
      case AbilityKind.teleport:
        final g = nextGate()!;
        fromY = coinY;
        coinY = g.gapY;
        vy = 0;
        immuneUntil = max(immuneUntil, t + st.immunity);
      case AbilityKind.freeze:
        shot = SimShot(scrollX + coinR, coinY, goldAhead(w * 1.4)!);
      case AbilityKind.tractor:
        tractorUntil = t + st.duration;
        tractorReach = st.reach * h;
    }
    s.cooldownLeft = st.cooldown;
    if (st.charges > 0) s.chargesLeft--;
    inputs.add([ticks, i == 0 ? SimInput.ability0 : SimInput.ability1]);
    _emit(SimEvent(SimEventKind.ability, ability: s.ability.kind, y: fromY));
    return true;
  }

  /// The nearest untaken gold coin ahead of the boar, within [maxAhead] of it.
  Pickup? goldAhead(double maxAhead) {
    Pickup? best;
    for (final p in pickups) {
      if (p.taken || p.pull != null || p.kind != PickupKind.gold) continue;
      final dx = p.worldX - scrollX;
      if (dx <= coinR || dx > maxAhead) continue;
      if (best == null || p.worldX < best.worldX) best = p;
    }
    return best;
  }

  /// The first gate the boar has not yet entered.
  SimGate? nextGate() {
    for (final g in gates) {
      if (g.worldX - scrollX > gateW / 2 + coinR) return g;
    }
    return null;
  }

  void _updateAbilities(double dt) {
    var changed = false;
    for (final s in slots) {
      if (s.cooldownLeft > 0) {
        s.cooldownLeft = max(0.0, s.cooldownLeft - dt);
        if (s.cooldownLeft == 0) changed = true;
      }
    }

    final g = grapple;
    if (g != null && (g.taken || g.worldX < scrollX - coinR || t > grappleUntil || phase != PassagePhase.flying)) {
      grapple = null;
      changed = true;
    }

    final sh = shot;
    if (sh != null) {
      sh.worldX += _shotSpeed * w * dt;
      final ty = sh.target.yAt(t);
      sh.y += (ty - sh.y) * min(1.0, dt * 10);
      if (sh.target.taken) {
        shot = null;
      } else if (sh.worldX >= sh.target.worldX) {
        final st = slots.firstWhere((s) => s.ability.kind == AbilityKind.freeze).stats;
        sh.target.freezeAt(t, st.duration);
        _emit(SimEvent(SimEventKind.frozeCoin, x: coinX + (sh.target.worldX - scrollX), y: ty));
        shot = null;
      }
    }
    if (changed) _emit(const SimEvent(SimEventKind.slotChanged));
  }

  void _updateTractor(double dt) {
    final beam = t < tractorUntil && phase == PassagePhase.flying;
    for (final p in pickups) {
      if (p.taken) continue;
      if (p.pull == null) {
        if (!beam) continue;
        final dx = p.worldX - scrollX;
        if (dx < -w * 0.4 || dx > w) continue;
        final dy = p.yAt(t) - coinY;
        if (dx * dx + dy * dy <= tractorReach * tractorReach) {
          p.pull = 0;
          p.pullX = p.worldX;
          p.pullY = p.yAt(t);
        }
      } else {
        p.pull = p.pull! + dt / pullTime;
        if (p.pull! >= 1) collect(p, coinX);
      }
    }
  }

  // ------------------------------------------------------------ DEV only
  // Each of these moves state directly, so each taints the run: a tainted
  // run is not a transcript and the web arcade refuses to submit it.

  /// Jumps to the calm stretch with the passage flown.
  void devSkipToLanding() {
    tainted = true;
    started = true;
    for (final g in gates) {
      g.passed = true;
    }
    gatesCleared = gates.length;
    erasCleared = eras.length;
    eraIndex = eras.length - 1;
    _emit(SimEvent(SimEventKind.eraChanged, value: eraIndex));
    scrollX = totalX - w * 0.35;
  }

  /// Jumps to just before the first gate of the next era, in its opening.
  void devNextEra() {
    if (phase != PassagePhase.flying) return;
    tainted = true;
    started = true;
    final next = eraIndex + 1;
    if (next >= eras.length) return;
    final g = gates.firstWhere((g) => g.era == next);
    scrollX = g.worldX - spacing * 0.75;
    eraIndex = next;
    _emit(SimEvent(SimEventKind.eraChanged, value: next));
    for (final x in gates) {
      if (x.worldX < scrollX) x.passed = true;
    }
    gatesCleared = gates.where((x) => x.passed).length;
    erasCleared = next;
    coinY = g.gapY;
    vy = 0;
    invUntil = t + 1.5;
  }

  void devMaxMomentum() {
    tainted = true;
    momentum = 1;
  }

  /// Forces the short ending from wherever the coin currently is.
  void devEndShort() {
    tainted = true;
    started = true;
    reserve = 0;
    _enter(PassagePhase.descending);
  }

  void devSetBody(double radiusK, double halfLengthK) {
    tainted = true;
    bodyRadiusK = radiusK;
    bodyHalfLengthK = halfLengthK;
  }

  // ------------------------------------------------------------- replay

  /// Replays a transcript. The web arcade's server calls this (compiled to
  /// JavaScript) with the seed it issued and the inputs the browser
  /// recorded, and believes only what comes back.
  ///
  /// An input that would not have done anything is a transcript this seed
  /// did not produce, and fails the replay rather than being skipped.
  static PassageReplayResult replay({
    required double w,
    required double h,
    required int seed,
    required double bodyRadiusK,
    required double bodyHalfLengthK,
    required List<EquippedAbility> loadout,
    required List<List<int>> inputs,
    int maxTicks = 120 * 60 * 6,
    PassageTuning tuning = PassageTuning.standard,
  }) {
    final sim = PassageSim(
      w: w,
      h: h,
      seed: seed,
      bodyRadiusK: bodyRadiusK,
      bodyHalfLengthK: bodyHalfLengthK,
      loadout: loadout,
      tuning: tuning,
    );
    var next = 0;
    var lastTick = -1;
    for (var i = 0; i < inputs.length; i++) {
      final at = inputs[i][0];
      if (at < lastTick) return PassageReplayResult.fail('inputs-out-of-order', i, sim);
      lastTick = at;
    }
    while (!sim.finished) {
      if (sim.ticks > maxTicks) return PassageReplayResult.fail('too-long', next, sim);
      while (next < inputs.length && inputs[next][0] == sim.ticks) {
        final code = inputs[next][1];
        final ok = switch (code) {
          SimInput.flap => sim.flap(),
          SimInput.ability0 => sim.use(0),
          SimInput.ability1 => sim.use(1),
          _ => false,
        };
        if (!ok) return PassageReplayResult.fail('ineffective-input', next, sim);
        next++;
      }
      if (next < inputs.length && inputs[next][0] < sim.ticks) {
        return PassageReplayResult.fail('input-after-its-tick', next, sim);
      }
      sim.advance();
    }
    if (next < inputs.length) return PassageReplayResult.fail('input-after-end', next, sim);
    return PassageReplayResult.ok(sim);
  }
}

class PassageReplayResult {
  final bool ok;
  final String? error;
  final int? invalidAt;
  final int score, stars, erasReached, erasCleared, gatesCleared, coinsTaken, ticks, reserve;
  final bool softLanding;

  PassageReplayResult._(this.ok, this.error, this.invalidAt, PassageSim s)
      : score = s.score,
        stars = s.finished ? s.stars : 0,
        erasReached = s.erasReached,
        erasCleared = s.erasCleared,
        gatesCleared = s.gatesCleared,
        coinsTaken = s.coinsTaken,
        ticks = s.ticks,
        reserve = s.reserve,
        softLanding = s.finished && s.softLanding;

  factory PassageReplayResult.ok(PassageSim s) => PassageReplayResult._(true, null, null, s);
  factory PassageReplayResult.fail(String why, int at, PassageSim s) => PassageReplayResult._(false, why, at, s);

  Map<String, Object?> toJson() => {
        'ok': ok,
        if (error != null) 'error': error,
        if (invalidAt != null) 'invalidAt': invalidAt,
        'score': score,
        'stars': stars,
        'erasReached': erasReached,
        'erasCleared': erasCleared,
        'gatesCleared': gatesCleared,
        'coinsTaken': coinsTaken,
        'reserve': reserve,
        'softLanding': softLanding,
        'ticks': ticks,
      };
}
