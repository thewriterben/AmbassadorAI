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
import '../sparkle.dart';
import 'abilities.dart';
import 'backdrop.dart';
import 'boar.dart';
import 'city.dart';
import 'eras.dart';
import 'sim/passage_sim.dart';

export 'sim/passage_sim.dart' show PassagePhase, PickupKind, Pickup, PassageSim, SimInput, PassageReplayResult;

part 'passage_abilities.dart';
part 'passage_gates.dart';
part 'passage_render.dart';

/// A short ring where a coin was taken.
class _Pop {
  final Offset at;
  final bool big;
  double age = 0;
  _Pop(this.at, this.big);
}

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
///
/// ## How the code is split
///
/// The game: rendering, sound, haptics and input around a [PassageSim].
///
/// Everything that decides where the boar goes and what a run scores lives
/// in `sim/passage_sim.dart`, stepped here at a fixed 120 Hz whatever the
/// frame rate. That split is what lets the web arcade's server replay a run
/// from its seed and taps and arrive at the same score to the last bit; the
/// game on the phone plays exactly as before.
class PassageGame extends FlameGame {
  final CabinetRun run;

  /// Fixed seed for tests, the DEV menu and the web arcade (which is given
  /// one by its server). Null means a fresh passage.
  final int? seed;

  /// The seed actually flown: [seed], or one drawn for this run.
  late final int simSeed = seed ?? Random().nextInt(1 << 31);

  /// Which boar is flying. Fixed for a run once growth is live; settable now
  /// so the DEV menu can show all three.
  BoarStage stage;

  final List<EquippedAbility> _loadout;

  /// The web arcade runs the simulation at one fixed size on every screen,
  /// and scales the drawing to the canvas, because a replay has to use the
  /// size the run was flown at and the server cannot know a window's. Null
  /// on the phone, where the simulation takes the screen's own size as it
  /// always has.
  final Size? fixedSize;

  PassageGame({
    required this.run,
    this.seed,
    this.stage = BoarStage.piglet,
    List<EquippedAbility> loadout = const [],
    this.fixedSize,
    this.tuning = PassageTuning.standard,
  }) : _loadout = [...loadout.take(2)] {
    run.onTap = flap;
  }

  /// The difficulty. Standard for every real run; the DEV menu can pick
  /// the easier variant (see PassageTuning).
  final PassageTuning tuning;

  /// This run's full reserve, for the HUD's dots.
  int get maxReserve => tuning.reserve;

  PassageSim? _simOrNull;

  /// The simulation. Exists from the first layout.
  PassageSim get sim => _simOrNull!;
  bool get _laidOut => _simOrNull != null;

  /// The abilities this run carries, one per button, at most two.
  List<AbilitySlot> get slots => _simOrNull?.slots ?? const [];

  /// Whether ability button [i] would do something right now.
  bool canUseAbility(int i) => _laidOut && !run.ended && sim.canUse(i);

  /// Fires ability button [i]. False, and nothing spent, if it is not live.
  bool useAbility(int i) => _laidOut && !run.ended && sim.use(i);

  bool get dashing => _laidOut && sim.dashing;
  bool get grappling => _laidOut && sim.grappling;
  bool get tractoring => _laidOut && sim.tractoring;

  // ------------------------------------------------------------ tuning
  // The numbers live on PassageSim; these keep the names the tests and the
  // screens have always used.

  static const startingReserve = PassageSim.startingReserve;
  static const copperValue = PassageSim.copperValue;
  static const silverValue = PassageSim.silverValue;
  static const goldValue = PassageSim.goldValue;
  static const momentumPerCopper = PassageSim.momentumPerCopper;
  static const momentumPerSilver = PassageSim.momentumPerSilver;
  static const momentumPerGold = PassageSim.momentumPerGold;
  static const driftRadPerSecond = PassageSim.driftRadPerSecond;
  static const momentumDecayPerSecond = PassageSim.momentumDecayPerSecond;
  static const maxSpeedBoost = PassageSim.maxSpeedBoost;
  static const spillOnStrike = PassageSim.spillOnStrike;
  static const softLandingAt = PassageSim.softLandingAt;
  static const playTop = PassageSim.playTop;
  static const dashSpeed = PassageSim.dashSpeed;
  static const grappleSpeed = PassageSim.grappleSpeed;

  /// DEV: draw the collision capsule over the boar.
  static bool devShowHitbox = false;

  /// DEV: the era a run starts in, for looking at a later era's city
  /// without flying there. Stepping with "Next era" from the menu races the
  /// game, which keeps running under the sheet.
  static int devStartEra = 0;

  /// Drives the era banner in the Flutter overlay.
  final ValueNotifier<int> eraNotifier = ValueNotifier(-1);
  int get eraIndex => eraNotifier.value;

  // ------------------------------------------------- simulation, read-only

  PassagePhase get phase => _laidOut ? sim.phase : PassagePhase.flying;
  int get reserve => _laidOut ? sim.reserve : tuning.reserve;
  int get gatesCleared => _laidOut ? sim.gatesCleared : 0;
  int get erasCleared => _laidOut ? sim.erasCleared : 0;
  int get erasReached => _laidOut ? sim.erasReached : 0;
  double get touchdownSpeed => _laidOut ? sim.touchdownSpeed : 0;
  bool get touchdownScraped => _laidOut && sim.touchdownScraped;
  bool get softLanding => _laidOut && sim.softLanding;
  int get score => _laidOut ? sim.score : 0;
  int get coinsTaken => _laidOut ? sim.coinsTaken : 0;
  double get momentum => _laidOut ? sim.momentum : 0;
  double get speedFactor => _laidOut ? sim.speedFactor : 1;
  int get multiplier => _laidOut ? sim.multiplier : 1;
  bool get started => _laidOut && sim.started;
  double get progress => _laidOut ? sim.progress : 0;
  double get scrollX => _laidOut ? sim.scrollX : 0;

  /// 0..3 — see the star rule in the class comment.
  int get stars => _laidOut ? sim.stars : 1;

  // Private views for the renderer, named as they were before the split so
  // passage_render.dart reads the same.
  double get _w => sim.w;
  double get _h => sim.h;
  double get _t => sim.t;
  double get _coinX => sim.coinX;
  double get _coinY => sim.coinY;
  double get _coinR => sim.coinR;
  double get _bodyR => sim.bodyR;
  double get _bodyL => sim.bodyL;
  double get _vy => sim.vy;
  double get _vMax => sim.vMax;
  double get _groundY => sim.groundY;
  double get _phaseT => sim.phaseT;
  double get _playTop => sim.playTopPx;
  double get _spacing => sim.spacing;
  double get _leadIn => sim.leadIn;
  double get _eraGap => sim.eraGap;
  double get _gateW => sim.gateW;
  double get _invUntil => sim.invUntil;
  double get _dashUntil => sim.dashUntil;
  double get _tractorUntil => sim.tractorUntil;
  double get _tractorReach => sim.tractorReach;
  Pickup? get _grapple => sim.grapple;
  SimShot? get _shot => sim.shot;
  List<SimGate> get _gates => sim.gates;
  List<Pickup> get _pickups => sim.pickups;
  List<SimSpill> get _spills => sim.spills;
  double _pickR(PickupKind k) => sim.pickR(k);

  // ------------------------------------------------------------- visuals

  /// Red flash after a strike, 1 fading to 0.
  double _strikeFlash = 0;

  final Map<PickupKind, Sprite> _coinSprites = {};
  final Map<BoarStage, List<Sprite>> _boarFrames = {};

  /// Wing-cycle position, in beats: the whole part counts them, the
  /// fraction is how far through this one. Advanced every frame at a rate
  /// that jumps on every flap, so a tap is visibly a wingbeat.
  double _wingPhase = 0;
  double _flapAt = -10;
  double _hurtUntil = -1;

  /// The era skylines behind the passage. Rebuilt with the layout.
  CityScape? _city;

  /// The owner's drawn backdrops, where there are any (see `backdrop.dart`).
  /// Empty until the manifest has loaded, and for good if it lists nothing.
  DrawnBackdrop _backdrop = DrawnBackdrop(BackdropManifest.empty);

  /// The era whose neighbourhood [_backdrop] last loaded.
  int _backdropEra = -1;

  final List<_Pop> _pops = [];

  /// Recent boar positions, as (distance flown, height), for the wake.
  final List<Offset> _trail = [];

  /// Frame time not yet turned into simulation ticks.
  double _acc = 0;

  /// The canvas size, which is the simulation size unless [fixedSize] is set.
  double _canvasW = 0, _canvasH = 0;

  // ------------------------------------------------------- test accessors

  @visibleForTesting
  List<({double worldX, double gapY, double gapH, int era})> get gateSpecs =>
      [for (final g in sim.gates) (worldX: g.worldX, gapY: g.gapY, gapH: g.gapH, era: g.era)];

  @visibleForTesting
  List<Pickup> get pickups => List.unmodifiable(sim.pickups);

  @visibleForTesting
  double get boarY => sim.coinY;

  @visibleForTesting
  double get clock => sim.t;

  @visibleForTesting
  double get bodyRadius => sim.bodyR;
  @visibleForTesting
  double get bodyHalfLength => sim.bodyL;

  @visibleForTesting
  double get boarVy => sim.vy;

  @visibleForTesting
  double get groundY => sim.groundY;

  @visibleForTesting
  double? get nextGapY => sim.nextGate()?.gapY;

  @visibleForTesting
  bool get shotInFlight => sim.shot != null;

  /// Forces the boar's height, for tests. Taints the run.
  @visibleForTesting
  set boarYForTest(double y) {
    sim.tainted = true;
    sim.coinY = y;
    sim.vy = 0;
  }

  @visibleForTesting
  int get spillCount => sim.spills.length;

  @visibleForTesting
  double get gateWidth => sim.gateW;

  @visibleForTesting
  double get coinRadius => sim.coinR;

  @visibleForTesting
  int get boarFrame => _boarFrame();

  /// Takes a pickup as if the coin had flown through it. Taints the run.
  @visibleForTesting
  void collectForTest(Pickup p) {
    sim.tainted = true;
    sim.collect(p, sim.coinX + (p.worldX - sim.scrollX));
  }

  /// Lands a strike as if the coin had clipped a pillar. Taints the run.
  @visibleForTesting
  void strikeForTest() {
    sim.tainted = true;
    sim.strike(null);
  }

  @visibleForTesting
  CityScape? get city => _city;

  // Direct writes, which the tests have always made. Each taints the run.

  @visibleForTesting
  set scrollX(double v) {
    sim.tainted = true;
    sim.scrollX = v;
  }

  @visibleForTesting
  set score(int v) {
    sim.tainted = true;
    sim.score = v;
  }

  @visibleForTesting
  set erasCleared(int v) {
    sim.tainted = true;
    sim.erasCleared = v;
  }

  @visibleForTesting
  set touchdownSpeed(double v) {
    sim.tainted = true;
    sim.touchdownSpeed = v;
  }

  // ----------------------------------------------------------- lifecycle

  @override
  Future<void> onLoad() async {
    await super.onLoad();
    // Not awaited: see the note in the Flame-only version's history — a
    // GameWidget holds update and render until onLoad completes, and the
    // images arrive within a frame or two. Until then the renderer draws
    // coins itself.
    unawaited(_loadCoinSprites());
    unawaited(_loadBoarSheets());
    unawaited(_loadBackdrop());
  }

  Future<void> _loadBackdrop() async {
    final m = await BackdropManifest.load();
    if (m.byEra.isEmpty) return;
    _backdrop = DrawnBackdrop(m)
      // Gates already drawn in the code-drawn columns are redrawn with the
      // art once it arrives.
      ..onLoaded = _disposeGatePictures;
    _backdropEra = -1;
  }

  /// One image per stage, one row of square frames. See `boar.dart`.
  Future<void> _loadBoarSheets() async {
    for (final e in BoarSpec.all.entries) {
      try {
        final img = await images.load(e.value.file);
        final side = img.height.toDouble();
        final count = e.value.frames.count;
        if ((img.width / img.height).round() != count) continue;
        _boarFrames[e.key] = [
          for (var i = 0; i < count; i++)
            Sprite(img, srcPosition: Vector2(i * side, 0), srcSize: Vector2.all(side)),
        ];
      } catch (_) {
        // Drawn fallback. See _coin.
      }
    }
  }

  Future<void> _loadCoinSprites() async {
    const files = {
      // The polished gold (tools/gen_shiny_gold_coin.py), which the home
      // coin and the leaderboard's first place use too.
      PickupKind.gold: 'coin_gold_shiny.png',
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
    _canvasW = size.x;
    _canvasH = size.y;

    // The passage is generated from the simulation's size, so a resize after
    // the first tap would move every gate the player is flying towards.
    // Before it there is nothing to disturb, so a late or corrected size is
    // taken then and only then. With a fixed size there is nothing to take.
    if (_laidOut && sim.started) return;
    final w = fixedSize?.width ?? size.x;
    final h = fixedSize?.height ?? size.y;
    if (_laidOut && sim.w == w && sim.h == h) return;

    _disposeGatePictures();
    final spec = BoarSpec.all[stage]!;
    _simOrNull = PassageSim(
      w: w,
      h: h,
      seed: simSeed,
      bodyRadiusK: spec.bodyRadius,
      bodyHalfLengthK: spec.bodyHalfLength,
      loadout: _loadout,
      onEvent: _onSimEvent,
      tuning: tuning,
    );
    _city?.dispose();
    _city = CityScape(
      w: w,
      h: h,
      // The roll-out after touchdown scrolls a little past the passage.
      totalScroll: sim.totalX + w * 2,
      eraAt: sim.eraFor,
      eraTints: [for (final e in eras) Color(e.tint)],
      bg: AppTheme.bg,
      warm: AppTheme.accent,
      seed: simSeed,
    );
    // NB: do not touch [eraNotifier] from here. See the note in [update].
  }

  void _disposeGatePictures() {
    final s = _simOrNull;
    if (s == null) return;
    for (final g in s.gates) {
      (g.renderCache as Picture?)?.dispose();
      g.renderCache = null;
    }
  }

  // ---------------------------------------------------------------- input

  /// One tap. The entire control scheme.
  void flap() {
    if (!_laidOut || run.ended) return;
    sim.flap();
  }

  // --------------------------------------------------------------- update

  @override
  void update(double dt) {
    super.update(dt);
    if (!_laidOut || run.ended) return;

    // Show the first era as soon as there is a viewport. This belongs here
    // and not in [onGameResize], which Flame calls during the build phase:
    // notifying a ValueNotifier there calls setState mid-build, Flutter
    // throws, and in a release build the banner simply never appeared.
    if (eraNotifier.value < 0) {
      eraNotifier.value = 0;
      run.tick();
    }

    // Hold the drawn backdrops of this era and its neighbours only.
    final era = _eraF.floor();
    if (era != _backdropEra && !_backdrop.isEmpty) {
      _backdropEra = era;
      _backdrop.keep({for (var e = era - 1; e <= era + 1; e++) if (e >= 0 && e < eras.length) e}, images);
    }

    // A long frame must never be a long step (see the history of this file:
    // a resume from background teleported the coin through a pillar). The
    // clamp now only limits how much simulation one frame may catch up on.
    dt = min(dt, 1 / 30);
    _wingPhase += dt * _wingRate;
    if (_strikeFlash > 0) _strikeFlash = max(0, _strikeFlash - dt * 2.2);

    _acc += dt;
    // The tolerance absorbs float drift in the accumulator, so 1/60 of a
    // second is always exactly two ticks.
    while (_acc >= PassageSim.step - 1e-9 && !sim.finished && !run.ended) {
      sim.advance();
      _acc -= PassageSim.step;
    }

    for (final p in _pops) {
      p.age += dt;
    }
    _pops.removeWhere((p) => p.age > 0.45);
    _pushTrail();
  }

  void _onSimEvent(SimEvent e) {
    switch (e.kind) {
      case SimEventKind.started:
        run.tick();
        for (var i = 0; i < devStartEra; i++) {
          sim.devNextEra();
        }
      case SimEventKind.flap:
        _flapAt = sim.t;
        // A tap is a downstroke: start a fresh beat from wings up, so the
        // boar beats its wings down as it rises.
        _wingPhase = _wingPhase.floorToDouble() + 1;
        Audio.instance.pigFlap(stage.name);
      case SimEventKind.eraChanged:
        eraNotifier.value = e.value;
        Audio.instance.sealStrip();
        run.tick();
      case SimEventKind.gatePassed:
        Audio.instance.ting();
        run.tick();
      case SimEventKind.collected:
        final gold = e.pickup == PickupKind.gold;
        _pops.add(_Pop(Offset(e.x, e.y), gold));
        if (gold) {
          Audio.instance.coinSpin();
        } else {
          Audio.instance.coinFlip();
        }
        run.tick();
      case SimEventKind.recovered:
        _pops.add(_Pop(Offset(e.x, e.y), false));
        Audio.instance.coinFlip();
        run.tick();
      case SimEventKind.struck:
        _hurtUntil = sim.t + 0.35;
        _strikeFlash = 1;
        Audio.instance.vaultHit();
        Audio.instance.pigGrunt(stage.name);
        HapticFeedback.mediumImpact();
        if (e.value > 0) Audio.instance.coinsPour();
        run.tick();
      case SimEventKind.phaseChanged:
        if (e.phase == PassagePhase.landing) Audio.instance.coinRoll();
        run.tick();
      case SimEventKind.touchdown:
        Audio.instance.pigSnort(stage.name);
        switch (e.value) {
          case 2:
            Audio.instance.win();
            Audio.instance.voWinner();
            HapticFeedback.heavyImpact();
          case 1:
            Audio.instance.ingotLand();
            HapticFeedback.mediumImpact();
          default:
            // Deliberately not `lose()`. Setting down early is a shorter
            // journey, not a failure.
            Audio.instance.land();
        }
        run.tick();
      case SimEventKind.finished:
        _finish();
      case SimEventKind.ability:
        switch (e.ability!) {
          case AbilityKind.dash:
            Audio.instance.abDash();
          case AbilityKind.grapple:
            Audio.instance.abGrapple();
          case AbilityKind.teleport:
            _pops.add(_Pop(Offset(sim.coinX, e.y), true));
            _pops.add(_Pop(Offset(sim.coinX, sim.coinY), true));
            _trail.clear(); // a blink leaves no wake between the two places
            Audio.instance.abBlink();
          case AbilityKind.freeze:
            Audio.instance.abFreezeFire();
          case AbilityKind.tractor:
            Audio.instance.abTractor();
        }
        HapticFeedback.selectionClick();
        run.tick();
      case SimEventKind.frozeCoin:
        _pops.add(_Pop(Offset(e.x, e.y), false));
        Audio.instance.abFreezeHit();
      case SimEventKind.slotChanged:
        run.tick();
    }
  }

  /// How fast the wings beat, in beats per second: a tap's beat at the
  /// stage's flap tempo, then its steady glide beat, slower still before
  /// the start and on the way down. (It was a frame rate, 20 a second after
  /// a tap: a whole beat in a fifth of a second, which blurred the
  /// razorback's six drawings.)
  double get _wingRate {
    final spec = BoarSpec.all[stage]!;
    if (phase == PassagePhase.down) return 0;
    if (!started) return 1 / (spec.glideBeat * 1.4);
    if (phase == PassagePhase.descending) return 1 / (spec.glideBeat * 1.6);
    return 1 / (_t - _flapAt < spec.flapBeat ? spec.flapBeat : spec.glideBeat);
  }

  void _finish() {
    run.end(RunResult(
      ending: sim.erasCleared >= eras.length ? RunEnding.landed : RunEnding.short,
      stars: sim.stars,
      reached: sim.erasReached,
      total: eras.length,
      score: sim.score,
      loadout: [
        for (final s in sim.slots) {'id': s.ability.kind.name, 'level': s.ability.level},
      ],
    ));
  }

  void _pushTrail() {
    _trail.add(Offset(sim.scrollX, sim.coinY));
    final keep = 14 + (12 * sim.momentum).round();
    while (_trail.length > keep) {
      _trail.removeAt(0);
    }
  }

  // ------------------------------------------------------------- DEV only
  // A full passage is seventy seconds. These taint the run (see PassageSim).

  void devSkipToLanding() {
    if (!_laidOut) return;
    sim.devSkipToLanding();
    run.tick();
  }

  /// Cycles the boar through its three stages, mid-run.
  BoarStage devNextStage() => devStepStage(1);

  /// Moves the boar [by] stages (negative is back toward the piglet),
  /// wrapping at the ends, mid-run.
  BoarStage devStepStage(int by) {
    stage = BoarStage.values[(stage.index + by) % BoarStage.values.length];
    if (_laidOut) {
      final spec = BoarSpec.all[stage]!;
      sim.devSetBody(spec.bodyRadius, spec.bodyHalfLength);
    }
    run.tick();
    return stage;
  }

  void devNextEra() {
    if (!_laidOut) return;
    sim.devNextEra();
    run.tick();
  }

  void devMaxMomentum() {
    if (!_laidOut) return;
    sim.devMaxMomentum();
    run.tick();
  }

  void devEndShort() {
    if (!_laidOut) return;
    sim.devEndShort();
  }

  @override
  void render(Canvas canvas) {
    super.render(canvas);
    final fs = fixedSize;
    if (fs == null || !_laidOut) {
      renderWorld(canvas);
      return;
    }
    // Web: the simulation's fixed size, scaled to fit and centred.
    final scale = min(_canvasW / fs.width, _canvasH / fs.height);
    canvas.save();
    canvas.translate((_canvasW - fs.width * scale) / 2, (_canvasH - fs.height * scale) / 2);
    canvas.scale(scale);
    canvas.clipRect(Rect.fromLTWH(0, 0, fs.width, fs.height));
    renderWorld(canvas);
    canvas.restore();
  }

  @override
  void onRemove() {
    _city?.dispose();
    _disposeGatePictures();
    eraNotifier.dispose();
    super.onRemove();
  }
}

/// A cubic ease-out, for drawing. The simulation has its own, exact one.
double _easeOut(double t) => 1 - pow(1 - t, 3).toDouble();
