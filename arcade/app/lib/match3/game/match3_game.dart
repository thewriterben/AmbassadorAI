import 'dart:async';
import 'dart:math';

import 'package:flame/components.dart';
import 'package:flame/effects.dart';
import 'package:flame/events.dart';
import 'package:flame/game.dart';
import 'package:flame/particles.dart';
import 'package:flutter/animation.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart' show Colors;
import 'package:flutter/painting.dart';
import 'package:flutter/services.dart';

import '../../audio.dart';
import '../../theme.dart';
import '../model/board.dart';
import '../model/gem.dart';
import '../model/session.dart';

const _gemAsset = {
  GemKind.gold: 'piece_gold.png',
  GemKind.silver: 'piece_silver.png',
  GemKind.red: 'piece_red.png',
  GemKind.copper: 'piece_copper.png',
  GemKind.blue: 'piece_blue.png',
  GemKind.green: 'piece_green.png',
};

/// A reinforced vault, shown while it still has more than one hit left. Not a
/// [Blocker] of its own — the same vault swaps to `piece_vault.png` when it
/// drops to its last hit, which is the only cue the player gets that the first
/// hit landed.
const _vaultArmoredAsset = 'piece_vault_armored.png';

const _blockerAsset = {
  Blocker.vault: 'piece_vault.png',
  Blocker.ingot: 'piece_ingot.png',
};

const _gemColor = {
  GemKind.gold: Color(0xFFFFD678),
  GemKind.silver: Color(0xFFD6DFE8),
  GemKind.red: Color(0xFFF07E9C),
  GemKind.copper: Color(0xFFECA878),
  GemKind.blue: Color(0xFF6C9CE0),
  GemKind.green: Color(0xFF94E8B4),
};

/// Flame view for one Match-3 level. Owns the animation of [LevelSession]
/// results; the Flutter HUD listens to [notifier] for score/moves/state.
class Match3Game extends FlameGame with DragCallbacks, TapCallbacks {
  final LevelSession session;
  final ValueNotifier<int> notifier = ValueNotifier(0);
  final void Function(SessionState)? onEnd;

  Match3Game({required this.session, this.onEnd});

  Board get board => session.board;

  late final Map<GemKind, Sprite> _sprites;
  late final Map<Blocker, Sprite> _blockerSprites;
  late final Sprite _vaultArmoredSprite;
  Sprite? _cellSprite;
  Sprite? _seal1, _seal2;
  final Map<int, GemComponent> _gems = {};
  final _root = PositionComponent(); // everything lives here so we can shake it
  late double cell;
  late Vector2 origin;
  bool _busy = true; // true until the intro drop-in finishes
  bool _ended = false;
  /// Set once the game is torn down — the player left the level.
  ///
  /// The cascade loop is a chain of awaits on effect completers. Removing the
  /// game completes those early (see [GemComponent.onRemove]) so the chain can
  /// unwind, but the chain must then *stop*: without this it would keep
  /// animating, playing sound and finally call [onEnd] into a route that is no
  /// longer on screen.
  bool _dead = false;
  Pos? _selected;
  Pos? _dragFrom;
  Vector2 _dragAccum = Vector2.zero();
  double _idle = 0;
  (Pos, Pos)? _hint;
  double _shake = 0;
  final _rng = Random();

  @override
  Color backgroundColor() => const Color(0x00000000);

  @override
  void onRemove() {
    _dead = true;
    super.onRemove();
  }

  @override
  Future<void> onLoad() async {
    _sprites = {for (final e in _gemAsset.entries) e.key: await Sprite.load(e.value)};
    _blockerSprites = {for (final e in _blockerAsset.entries) e.key: await Sprite.load(e.value)};
    _vaultArmoredSprite = await Sprite.load(_vaultArmoredAsset);
    _cellSprite = await Sprite.load('board_cell.png');
    _seal1 = await Sprite.load('seal_1.png');
    _seal2 = await Sprite.load('seal_2.png');
    GemComponent.logo = await Sprite.load('logo_white.png');
    _layout();
    add(_root);
    _root.add(_BoardBackdrop(this));
    for (var c = 0; c < board.cols; c++) {
      for (var r = 0; r < board.rows; r++) {
        _spawnComponent(board.cells[r][c]!, Pos(r, c), from: Pos(r - board.rows - 2, c));
      }
    }
    _introPending = true;
  }

  bool _introPending = false;

  /// Intro: pieces rain in column by column. Runs on the first frame after
  /// layout is final so the targets use the real cell size.
  void _runIntro() {
    _introPending = false;
    final drops = <Future>[];
    for (final comp in _gems.values) {
      comp.position = centerOf(Pos(comp.pos.r - board.rows - 2, comp.pos.c));
      drops.add(comp.moveTo(centerOf(comp.pos), 0.45 + comp.pos.r * 0.03,
          curve: Curves.easeOutBack, delay: comp.pos.c * 0.05));
    }
    Audio.instance.coinsPour();
    Future.wait(drops).then((_) {
      Audio.instance.coinDrop();
      _busy = false;
    });
  }

  /// Sprite size as a fraction of a cell.
  ///
  /// The art inside the sprite is inset a further 6% a side, so the coin
  /// itself lands at about 85% of a cell. Much past this and neighbouring
  /// coins touch, which reads as a blob rather than a grid.
  static const _gemScale = 0.96;

  void _layout() {
    final w = size.x, h = size.y;
    cell = min(w / board.cols, h / board.rows);
    origin = Vector2((w - cell * board.cols) / 2, (h - cell * board.rows) / 2);
  }

  @override
  void onGameResize(Vector2 size) {
    super.onGameResize(size);
    if (isLoaded) {
      _layout();
      for (final g in _gems.values) {
        g.size = Vector2.all(_gemScale * cell);
        if (!_busy) g.position = centerOf(g.pos);
      }
    }
  }

  Vector2 centerOf(Pos p) => origin + Vector2((p.c + 0.5) * cell, (p.r + 0.5) * cell);

  Pos? posAt(Vector2 v) {
    final local = v - origin;
    final p = Pos((local.y / cell).floor(), (local.x / cell).floor());
    return board.inBounds(p) ? p : null;
  }

  /// Where a gem currently sits on the board, or null if it has left it.
  Pos? _posOfGem(Gem g) {
    for (var r = 0; r < board.rows; r++) {
      for (var c = 0; c < board.cols; c++) {
        if (board.cells[r][c]?.id == g.id) return Pos(r, c);
      }
    }
    return null;
  }

  /// The sprite a gem should be wearing right now.
  ///
  /// Vaults are the only piece whose art depends on state: one with more than
  /// a single hit left wears the armoured plate.
  Sprite _spriteFor(Gem g) {
    if (g.blocker == Blocker.vault && (board.vaultArmor[g.id] ?? 1) > 1) {
      return _vaultArmoredSprite;
    }
    if (g.blocker != null) return _blockerSprites[g.blocker]!;
    return _sprites[g.kind]!;
  }

  GemComponent _spawnComponent(Gem g, Pos at, {required Pos from}) {
    final comp = GemComponent(
      gem: g,
      sprite: _spriteFor(g),
      pos: at,
      position: centerOf(from),
      size: Vector2.all(_gemScale * cell),
    );
    _gems[g.id] = comp;
    _root.add(comp);
    return comp;
  }

  // ------------------------------------------------------------ input

  @override
  void onTapUp(TapUpEvent event) {
    if (_busy || _ended) return;
    final p = posAt(event.localPosition);
    if (p == null) return;
    if (_selected == null) {
      _select(p);
    } else if (_selected == p) {
      _select(null);
    } else if (_selected!.adjacent(p)) {
      final a = _selected!;
      _select(null);
      _trySwap(a, p);
    } else {
      _select(p);
    }
  }

  @override
  void onDragStart(DragStartEvent event) {
    super.onDragStart(event);
    if (_busy || _ended) return;
    _dragFrom = posAt(event.localPosition);
    _dragAccum = Vector2.zero();
  }

  @override
  void onDragUpdate(DragUpdateEvent event) {
    super.onDragUpdate(event);
    if (_dragFrom == null || _busy || _ended) return;
    _dragAccum += event.localDelta;
    if (_dragAccum.length < cell * 0.35) return;
    final d = _dragAccum.x.abs() > _dragAccum.y.abs()
        ? Pos(0, _dragAccum.x > 0 ? 1 : -1)
        : Pos(_dragAccum.y > 0 ? 1 : -1, 0);
    final from = _dragFrom!;
    _dragFrom = null;
    _select(null);
    final to = from + d;
    if (board.inBounds(to)) _trySwap(from, to);
  }

  @override
  void onDragEnd(DragEndEvent event) {
    super.onDragEnd(event);
    _dragFrom = null;
  }

  void _select(Pos? p) {
    // Obstacles are scenery — tapping one should not arm a swap.
    if (p != null && (board.at(p)?.isBlocker ?? false)) {
      Audio.instance.invalid();
      _gems[board.at(p)!.id]?.wiggle();
      return;
    }
    if (_selected != null) _gems[board.at(_selected!)?.id]?.selected = false;
    _selected = p;
    if (p != null) {
      _gems[board.at(p)?.id]?.selected = true;
      Audio.instance.coinFlip();
    }
  }

  // ------------------------------------------------------------ swap + cascade

  Future<void> _trySwap(Pos a, Pos b) async {
    if (_busy || _ended || _dead) return;
    _busy = true;
    _clearHint();
    final ga = _gems[board.at(a)!.id]!, gb = _gems[board.at(b)!.id]!;

    await Future.wait([ga.moveTo(centerOf(b), 0.14), gb.moveTo(centerOf(a), 0.14)]);
    if (_dead) return;

    final res = session.swap(a, b);
    if (!res.valid) {
      HapticFeedback.lightImpact();
      Audio.instance.invalid();
      ga.wiggle();
      gb.wiggle();
      await Future.wait([ga.moveTo(centerOf(a), 0.14), gb.moveTo(centerOf(b), 0.14)]);
      _busy = false;
      return;
    }
    ga.pos = b;
    gb.pos = a;
    HapticFeedback.mediumImpact();
    Audio.instance.coinRoll();
    notifier.value++;

    for (final step in res.steps) {
      await _animateStep(step);
      if (_dead) return;
      notifier.value++;
    }
    // The board reshuffles itself when it runs out of moves; say so rather
    // than letting the coins rearrange under the player's hands.
    if (board.shuffledLastMove) {
      Audio.instance.coinsPour();
      shake(6);
      _root.add(_FloatText('NO MOVES — RESHUFFLED', Vector2(size.x / 2, size.y * 0.42),
          size: 22, color: AppTheme.accentHover));
      for (final g in _gems.values) {
        g.pos = _posOfGem(g.gem) ?? g.pos;
        await g.moveTo(centerOf(g.pos), 0.28, curve: Curves.easeInOut);
        if (_dead) return;
      }
      await Future.delayed(const Duration(milliseconds: 220));
      if (_dead) return;
    }
    _busy = false;
    if (session.state != SessionState.playing && !_ended) {
      _ended = true;
      await Future.delayed(const Duration(milliseconds: 250));
      if (_dead) return;
      onEnd?.call(session.state);
    }
  }

  Future<void> _animateStep(CascadeStep step) async {
    if (_dead) return;
    final a = Audio.instance;
    final removedSpecials = step.removed.values.where((g) => g.isSpecial).toList();
    final hadBomb = removedSpecials.any((g) => g.special == Special.bomb);

    // Sound + camera reaction scale with what happened.
    if (hadBomb) {
      a.bomb();
      shake(14);
      _flash(AppTheme.accentHover, 0.55);
    } else if (removedSpecials.isNotEmpty) {
      a.specialFire();
      shake(7);
      _flash(Colors.white, 0.25);
    } else {
      a.pop(step.combo);
      if (step.removed.length >= 5) shake(3);
    }
    if (step.created.isNotEmpty) {
      a.specialCreate();
      a.ting();
    }
    if (step.combo > 1) {
      a.combo(step.combo);
      HapticFeedback.mediumImpact();
    }
    // Deep chains earn a spoken affirmation, rate-limited in Audio so it
    // stays an event rather than a tic.
    if (step.combo >= 4) a.voPraise(big: step.combo >= 6);

    // Special fire visuals: beams and shockwaves at their former positions.
    for (final e in step.removed.entries) {
      final g = e.value;
      switch (g.special) {
        case Special.stripedH:
          _beam(e.key, horizontal: true);
        case Special.stripedV:
          _beam(e.key, horizontal: false);
        case Special.wrapped:
          _shockwave(centerOf(e.key), cell * 2.2, AppTheme.accentHover);
        case Special.bomb:
          _shockwave(centerOf(e.key), cell * 6, AppTheme.accent);
          _shockwave(centerOf(e.key), cell * 9, Colors.white, delay: 0.08);
        case Special.none:
          break;
      }
    }

    // Score popup at the centroid of the clear.
    if (step.removed.isNotEmpty) {
      final pts = step.removed.keys.map(centerOf).toList();
      final centroid = pts.reduce((x, y) => x + y) / pts.length.toDouble();
      _root.add(_FloatText('+${step.score}', centroid,
          size: step.combo > 1 ? 30 : 24,
          color: step.combo > 1 ? AppTheme.accentHover : AppTheme.accent));
    }
    if (step.combo > 1) _comboBanner(step.combo);

    // Objectives: seals strip, vaults burst, ingots leave at the floor.
    for (final e in step.sealsCleared.entries) {
      _shockwave(centerOf(e.key), cell * 1.1, AppTheme.accent);
    }
    if (step.sealsCleared.isNotEmpty) a.sealStrip();
    for (final e in step.vaultsDamaged.entries) {
      _shockwave(centerOf(e.key), cell * 1.3, const Color(0xFF8A93A3));
      final g = board.at(e.key);
      final comp = _gems[g?.id];
      comp?.wiggle();
      // The armour comes off. Without this the vault looks untouched after the
      // first hit and the player has no way to know it landed.
      if (g != null) comp?.sprite = _spriteFor(g);
    }
    if (step.vaultsDamaged.isNotEmpty) {
      a.vaultHit();
      shake(4);
    }
    for (final e in step.vaultsBroken.entries) {
      final comp = _gems.remove(e.value.id);
      _shockwave(centerOf(e.key), cell * 2.0, const Color(0xFF8A93A3));
      _burst(centerOf(e.key), GemKind.silver, big: true);
      _root.add(_FloatText('VAULT', centerOf(e.key), size: 18, color: AppTheme.accentHover));
      comp?.pop();
    }
    if (step.vaultsBroken.isNotEmpty) {
      a.vaultBreak();
      shake(9);
      HapticFeedback.heavyImpact();
    }
    for (final e in step.ingotsDelivered.entries) {
      final comp = _gems.remove(e.value.id);
      _shockwave(centerOf(e.key), cell * 2.4, AppTheme.accentHover);
      _burst(centerOf(e.key), GemKind.gold, big: true);
      _root.add(_FloatText('DELIVERED', centerOf(e.key), size: 20, color: AppTheme.accentHover));
      comp?.pop();
    }
    if (step.ingotsDelivered.isNotEmpty) {
      a.ingotLand();
      shake(12);
      _flash(AppTheme.accentHover, 0.4);
      HapticFeedback.heavyImpact();
    }

    // 1. Pops.
    final pops = <Future>[];
    for (final e in step.removed.entries) {
      final comp = _gems[e.value.id];
      if (comp == null) continue;
      if (step.created.containsKey(e.key)) {
        comp.gem = step.created[e.key]!;
        _gems[comp.gem.id] = comp;
        _shockwave(comp.position, cell * 1.6, Colors.white);
        pops.add(comp.pulse());
      } else {
        _gems.remove(e.value.id);
        _burst(comp.position, e.value.kind, big: e.value.isSpecial || step.combo > 2);
        pops.add(comp.pop());
      }
    }
    await Future.wait(pops);
    if (_dead) return;

    // 2. Falls + spawns.
    final moves = <Future>[];
    for (final (from, to, g) in step.falls) {
      final comp = _gems[g.id];
      if (comp == null) continue;
      comp.pos = to;
      final dist = (to.r - from.r).toDouble();
      moves.add(comp.moveTo(centerOf(to), 0.09 + dist * 0.045, curve: Curves.easeIn));
    }
    final spawnCols = <int, int>{};
    for (final e in step.spawns.entries) {
      spawnCols[e.key.c] = (spawnCols[e.key.c] ?? 0) + 1;
    }
    for (final e in step.spawns.entries) {
      final above = spawnCols[e.key.c]!;
      final comp = _spawnComponent(e.value, e.key, from: Pos(e.key.r - above, e.key.c));
      moves.add(comp.moveTo(centerOf(e.key), 0.09 + above * 0.045, curve: Curves.easeIn));
    }
    await Future.wait(moves);
    if (_dead) return;
    if (moves.isNotEmpty) {
      a.land();
      if (step.spawns.length >= 4) a.coinDrop();
      for (final (_, to, g) in step.falls) {
        _gems[g.id]?.squash();
        if (to.r == board.rows - 1) break;
      }
    }
    await Future.delayed(const Duration(milliseconds: 40));
  }

  // ------------------------------------------------------------ effects

  void shake(double amount) => _shake = max(_shake, amount);

  void _flash(Color color, double alpha) {
    final r = RectangleComponent(
      size: size,
      paint: Paint()..color = color.withValues(alpha: alpha),
      priority: 50,
    );
    r.add(OpacityEffect.fadeOut(EffectController(duration: 0.28), onComplete: r.removeFromParent));
    add(r);
  }

  void _beam(Pos at, {required bool horizontal}) {
    final c = centerOf(at);
    final len = horizontal ? cell * board.cols : cell * board.rows;
    final beam = RectangleComponent(
      position: horizontal ? Vector2(origin.x + len / 2, c.y) : Vector2(c.x, origin.y + len / 2),
      size: horizontal ? Vector2(len, cell * 0.5) : Vector2(cell * 0.5, len),
      anchor: Anchor.center,
      paint: Paint()
        ..color = AppTheme.accentHover.withValues(alpha: 0.9)
        ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 6),
      priority: 40,
    );
    beam.add(ScaleEffect.to(
        horizontal ? Vector2(1, 0.15) : Vector2(0.15, 1), EffectController(duration: 0.35)));
    beam.add(OpacityEffect.fadeOut(EffectController(duration: 0.35), onComplete: beam.removeFromParent));
    _root.add(beam);
    // Sparks along the beam.
    _root.add(ParticleSystemComponent(
      position: c,
      priority: 41,
      particle: Particle.generate(
        count: 18,
        lifespan: 0.4,
        generator: (i) {
          final dir = horizontal ? Vector2(i.isEven ? 1 : -1, 0) : Vector2(0, i.isEven ? 1 : -1);
          return AcceleratedParticle(
            speed: dir * (300 + _rng.nextDouble() * 500) + Vector2.random(_rng) * 60,
            child: CircleParticle(
                radius: 3, paint: Paint()..color = AppTheme.accentHover.withValues(alpha: 0.9)),
          );
        },
      ),
    ));
  }

  void _shockwave(Vector2 at, double radius, Color color, {double delay = 0}) {
    final ring = CircleComponent(
      radius: cell * 0.3,
      position: at,
      anchor: Anchor.center,
      paint: Paint()
        ..color = color.withValues(alpha: 0.85)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 4,
      priority: 45,
    );
    final k = radius / (cell * 0.3);
    ring.add(ScaleEffect.to(Vector2.all(k),
        EffectController(duration: 0.4, startDelay: delay, curve: Curves.easeOut)));
    ring.add(OpacityEffect.fadeOut(EffectController(duration: 0.4, startDelay: delay),
        onComplete: ring.removeFromParent));
    _root.add(ring);
  }

  void _burst(Vector2 at, GemKind kind, {bool big = false}) {
    final color = _gemColor[kind]!;
    final sprite = _sprites[kind]!;
    final n = big ? 14 : 7;
    // Coin fragments: tiny spinning sprites.
    _root.add(ParticleSystemComponent(
      position: at,
      priority: 30,
      particle: Particle.generate(
        count: n,
        lifespan: big ? 0.8 : 0.55,
        generator: (i) {
          final a = _rng.nextDouble() * pi * 2;
          final sp = (big ? 260 : 170) * (0.5 + _rng.nextDouble());
          final sz = cell * (big ? 0.34 : 0.26) * (0.6 + _rng.nextDouble() * 0.5);
          return AcceleratedParticle(
            speed: Vector2(cos(a), sin(a)) * sp - Vector2(0, 120),
            acceleration: Vector2(0, 700),
            child: RotatingParticle(
              from: _rng.nextDouble() * pi,
              to: _rng.nextDouble() * pi * 6,
              child: SpriteParticle(sprite: sprite, size: Vector2.all(sz)),
            ),
          );
        },
      ),
    ));
    // Glow sparks.
    _root.add(ParticleSystemComponent(
      position: at,
      priority: 31,
      particle: Particle.generate(
        count: big ? 22 : 10,
        lifespan: 0.45,
        generator: (i) {
          final a = _rng.nextDouble() * pi * 2;
          final sp = (big ? 220 : 140) * (0.4 + _rng.nextDouble());
          return AcceleratedParticle(
            speed: Vector2(cos(a), sin(a)) * sp,
            acceleration: Vector2(0, 200),
            child: ComputedParticle(renderer: (canvas, p) {
              canvas.drawCircle(Offset.zero, 4 * (1 - p.progress),
                  Paint()..color = color.withValues(alpha: 1 - p.progress));
            }),
          );
        },
      ),
    ));
  }

  /// Fires the whole cascade-feedback path at a chosen depth. Test builds only.
  ///
  /// Reaching a nine-chain by playing is rare enough that the deep-combo audio
  /// and visuals would otherwise go unreviewed until a player found them. This
  /// runs the same calls a real cascade of [depth] makes — banner, combo sting,
  /// haptics, the tiered affirmation — so they can be checked on demand.
  ///
  /// It does not touch the board: no pieces clear and no score is added, so it
  /// cannot be used to win a level.
  void devCombo(int depth) {
    final a = Audio.instance;
    _comboBanner(depth);
    a.combo(depth);
    HapticFeedback.mediumImpact();
    shake(3.0 + depth.toDouble());
    for (var i = 0; i < depth; i++) {
      final at = Vector2(
        origin.x + (_rng.nextDouble() * board.cols) * cell,
        origin.y + (_rng.nextDouble() * board.rows) * cell,
      );
      _root.add(TimerComponent(
        period: 0.001 + i * 0.09,
        removeOnFinish: true,
        onTick: () {
          a.pop(i + 1);
          _burst(at, GemKind.values[_rng.nextInt(GemKind.values.length)]);
          _shockwave(at, cell * 1.2, AppTheme.accent);
        },
      ));
    }
    // Same threshold the real cascade uses.
    if (depth >= 4) a.voPraise(big: depth >= 6);
  }

  void _comboBanner(int combo) {
    add(_FloatText('COMBO ×$combo', Vector2(size.x / 2, origin.y + cell * 1.2),
        size: 34 + combo * 3, color: AppTheme.accentHover, rise: 40, life: 0.9, bounce: true));
    if (combo >= 3) {
      // Gold rain from the top edge for big chains.
      _root.add(ParticleSystemComponent(
        position: Vector2(size.x / 2, origin.y - cell),
        priority: 32,
        particle: Particle.generate(
          count: 12 + combo * 6,
          lifespan: 1.2,
          generator: (i) => AcceleratedParticle(
            position: Vector2((_rng.nextDouble() - 0.5) * size.x, 0),
            speed: Vector2((_rng.nextDouble() - 0.5) * 80, 80 + _rng.nextDouble() * 120),
            acceleration: Vector2(0, 500),
            child: RotatingParticle(
              to: pi * 4,
              child: SpriteParticle(
                  sprite: _sprites[GemKind.gold]!,
                  size: Vector2.all(cell * (0.2 + _rng.nextDouble() * 0.2))),
            ),
          ),
        ),
      ));
    }
  }

  /// A star: one glowing dot that leaves a short trail behind it.
  ///
  /// Drawn as a streak from where the particle was a moment ago to where it is
  /// now, which is what reads as motion. A plain circle at 60 fps reads as a
  /// dot sitting still, however fast it is actually travelling.
  Particle _star(
    Vector2 velocity,
    Color color, {
    required double lifespan,
    required double radius,
    double gravity = 250,
    double drag = 1.6,
    double twinkle = 14,
    double trail = 0.055,
  }) {
    return ComputedParticle(
      lifespan: lifespan,
      renderer: (canvas, p) {
        final t = p.progress * lifespan;
        // Position under linear drag with gravity — closed form, so the trail
        // can be sampled at any earlier time without storing history.
        Offset at(double s) {
          final k = (1 - exp(-drag * s)) / drag;
          return Offset(
            velocity.x * k,
            velocity.y * k + 0.5 * gravity * s * s,
          );
        }

        final fade = pow(1 - p.progress, 1.6).toDouble();
        // Stars flicker as they burn, and flicker harder as they die.
        final tw = 0.6 + 0.4 * sin(p.progress * pi * twinkle) * (0.4 + p.progress);
        final a = (fade * tw).clamp(0.0, 1.0);
        if (a <= 0.01) return;

        final head = at(t);
        final tailPt = at(max(0, t - trail));
        final paint = Paint()
          ..color = color.withValues(alpha: a)
          ..blendMode = BlendMode.plus
          ..strokeCap = StrokeCap.round
          ..strokeWidth = radius * 2 * (0.5 + 0.5 * fade);
        canvas.drawLine(tailPt, head, paint);
        // A brighter core keeps the head of the streak reading as the star.
        canvas.drawCircle(
            head,
            radius * fade,
            Paint()
              ..color = Color.lerp(color, Colors.white, 0.55 * fade)!
                  .withValues(alpha: a)
              ..blendMode = BlendMode.plus);
      },
    );
  }

  /// The flash of light a break throws across the sky.
  void _skyFlash(Vector2 at, Color color, double radius) {
    _root.add(ParticleSystemComponent(
      position: at,
      priority: 69,
      particle: ComputedParticle(
        lifespan: 0.34,
        renderer: (canvas, p) {
          final a = (1 - p.progress) * 0.5;
          canvas.drawCircle(
              Offset.zero,
              radius * (0.35 + p.progress * 0.9),
              Paint()
                ..shader = RadialGradient(colors: [
                  color.withValues(alpha: a),
                  color.withValues(alpha: 0),
                ]).createShader(
                    Rect.fromCircle(center: Offset.zero, radius: radius))
                ..blendMode = BlendMode.plus);
        },
      ),
    ));
  }

  /// One firework: a shell climbs trailing sparks, then breaks into a shell of
  /// stars with a slower inner core and a few long-falling willow trails.
  void _firework(Vector2 at, Color color,
      {double delay = 0, double scale = 1, bool mute = false, VoidCallback? onBreak}) {
    // Launch from just below the board, under the burst point, so the climb
    // reads as one object travelling rather than a streak appearing.
    final from = Vector2(at.x + (_rng.nextDouble() - 0.5) * size.x * 0.10, size.y * 1.02);
    final rise = (from.y - at.y);
    // Taller shells take longer, so a high break feels higher.
    final riseTime = (0.42 + rise / size.y * 0.42).clamp(0.4, 0.95);

    _root.add(TimerComponent(
      period: max(delay, 0.001),
      removeOnFinish: true,
      onTick: () {
        if (!mute) Audio.instance.fwLift();

        // The shell itself, plus the sparks it sheds on the way up.
        _root.add(ParticleSystemComponent(
          position: from,
          priority: 68,
          particle: ComputedParticle(
            lifespan: riseTime,
            renderer: (canvas, p) {
              // Decelerate towards the apex.
              final k = 1 - pow(1 - p.progress, 2.0).toDouble();
              final y = -rise * k;
              final x = (at.x - from.x) * k;
              final head = Offset(x, y);
              final paint = Paint()
                ..color = color.withValues(alpha: 0.85)
                ..blendMode = BlendMode.plus;
              // Trail: a handful of fading sparks strung out behind.
              for (var i = 1; i <= 7; i++) {
                final s = (p.progress - i * 0.028).clamp(0.0, 1.0);
                final kk = 1 - pow(1 - s, 2.0).toDouble();
                final a = (1 - i / 8) * 0.45 * (1 - p.progress * 0.3);
                canvas.drawCircle(
                    Offset((at.x - from.x) * kk, -rise * kk),
                    cell * 0.035 * (1 - i / 9),
                    Paint()
                      ..color = color.withValues(alpha: a)
                      ..blendMode = BlendMode.plus);
              }
              canvas.drawCircle(head, cell * 0.06, paint);
            },
          ),
        ));

        // The break.
        _root.add(TimerComponent(
          period: riseTime,
          removeOnFinish: true,
          onTick: () {
            // Muted shells belong to the finale, which has one prebuilt sound
            // covering all three — three one-shots fired 70 ms apart sum to
            // mush rather than to a finale.
            if (!mute) Audio.instance.fwBurst();
            onBreak?.call();
            _skyFlash(at, color, cell * 3.2 * scale);
            _shockwave(at, cell * 1.4 * scale, color);

            final outer = (30 * scale).round().clamp(18, 46);
            _root.add(ParticleSystemComponent(
              position: at,
              priority: 70,
              particle: Particle.generate(
                count: outer,
                // Particle.generate defaults to a 0.5 s lifespan AND to
                // applyLifespanToChildren, which silently overwrites whatever
                // each star asked for. Without these two arguments every star
                // below dies in half a second regardless of its own lifespan.
                lifespan: 2.0,
                applyLifespanToChildren: false,
                generator: (i) {
                  // Even spread with jitter — a perfectly regular ring looks
                  // like a gear, and pure random leaves bald patches.
                  final a = (i / outer) * pi * 2 + (_rng.nextDouble() - 0.5) * 0.35;
                  final sp = (250 + _rng.nextDouble() * 170) * scale;
                  return _star(
                    Vector2(cos(a), sin(a)) * sp,
                    color,
                    lifespan: 1.5 + _rng.nextDouble() * 0.5,
                    radius: cell * 0.05,
                  );
                },
              ),
            ));

            // Inner core: slower, whiter, shorter-lived. Two speeds is what
            // gives a break depth instead of a flat ring.
            _root.add(ParticleSystemComponent(
              position: at,
              priority: 70,
              particle: Particle.generate(
                count: 14,
                lifespan: 1.3,
                applyLifespanToChildren: false,
                generator: (i) {
                  final a = _rng.nextDouble() * pi * 2;
                  final sp = (70 + _rng.nextDouble() * 110) * scale;
                  return _star(
                    Vector2(cos(a), sin(a)) * sp,
                    Color.lerp(color, Colors.white, 0.6)!,
                    lifespan: 0.9 + _rng.nextDouble() * 0.4,
                    radius: cell * 0.042,
                    twinkle: 20,
                  );
                },
              ),
            ));

            // Willows: a few heavy stars that arc over and fall a long way.
            _root.add(ParticleSystemComponent(
              position: at,
              priority: 70,
              particle: Particle.generate(
                count: 7,
                lifespan: 2.4,
                applyLifespanToChildren: false,
                generator: (i) {
                  final a = (i / 7) * pi * 2 + _rng.nextDouble() * 0.5;
                  final sp = (120 + _rng.nextDouble() * 80) * scale;
                  return _star(
                    Vector2(cos(a), sin(a)) * sp,
                    color,
                    lifespan: 2.4,
                    radius: cell * 0.035,
                    gravity: 150,
                    drag: 0.9,
                    twinkle: 7,
                    trail: 0.10,
                  );
                },
              ),
            ));

            if (!mute) {
              _root.add(TimerComponent(
                period: 0.22,
                removeOnFinish: true,
                onTick: Audio.instance.fwCrackle,
              ));
            }
          },
        ));
      },
    ));
  }

  /// Fireworks over the finished board. Standalone builds only — the arcade
  /// plan bars prize-style celebration inside the DGD App tab, which is the
  /// same reason the coin fountain became a shine wave.
  void _fireworkShow({bool grand = false}) {
    if (Audio.inAppTab) return;
    const colors = [
      Color(0xFFFFD678), // gold
      Color(0xFFF07E9C), // flag red, lightened
      Color(0xFF6C9CE0), // flag blue, lightened
      Color(0xFF94E8B4), // money green
      Colors.white,
    ];

    if (grand) {
      _grandShow(colors);
      return;
    }

    // Six shells at a walking pace, then three together as a finale. The
    // stagger matters more than the count: all at once is just a flash.
    var t = 0.10;
    for (var i = 0; i < 6; i++) {
      final at = Vector2(
        size.x * (0.16 + _rng.nextDouble() * 0.68),
        size.y * (0.12 + _rng.nextDouble() * 0.36),
      );
      _firework(at, colors[i % colors.length],
          delay: t, scale: 0.85 + _rng.nextDouble() * 0.35);
      t += 0.30 + _rng.nextDouble() * 0.16;
    }
    for (var i = 0; i < 3; i++) {
      final at = Vector2(
        size.x * (0.22 + _rng.nextDouble() * 0.56),
        size.y * (0.10 + _rng.nextDouble() * 0.30),
      );
      _firework(at, colors[(i + 3) % colors.length],
          delay: t + i * 0.07,
          scale: 1.25 + _rng.nextDouble() * 0.3,
          mute: true,
          onBreak: i == 0 ? Audio.instance.fwFinale : null);
    }
  }

  /// The last vault in the game gets a real display.
  ///
  /// Structure, because a firework show is pacing rather than quantity — the
  /// ordinary show is six shells and reads as "well done"; simply firing
  /// twenty at once would read as noise, not as more:
  ///
  ///   1. **Opening pair**, wide left and right, to say something different is
  ///      happening before the player has finished reading the board.
  ///   2. **A climbing run** of nine, alternating sides and rising as it goes,
  ///      so the eye is dragged upward.
  ///   3. **A held beat.** Nothing at all for a third of a second. This is what
  ///      makes the last movement land; without it the finale is just more of
  ///      the same.
  ///   4. **The finale**: five together across the full width, then a gold
  ///      willow overhead that keeps falling for three seconds.
  ///
  /// Deliberately still light and fireworks, never coins: arcade plan §4.3
  /// bars prize-style and jackpot imagery, and a shower of gold coins over a
  /// gold-backed asset's own app is exactly what it is warning about. It is
  /// also why this whole method is behind the App-tab gate in the caller.
  void _grandShow(List<Color> colors) {
    // 1. Opening pair, hard left and hard right.
    for (var i = 0; i < 2; i++) {
      _firework(
        Vector2(size.x * (i == 0 ? 0.14 : 0.86), size.y * 0.30),
        const Color(0xFFFFD678),
        delay: 0.08 + i * 0.09,
        scale: 1.15,
      );
    }

    // 2. The climbing run: alternating sides, apex rising, tempo tightening.
    var t = 0.48;
    for (var i = 0; i < 9; i++) {
      final k = i / 8; // 0 -> 1 as the run progresses
      final side = i.isEven ? 0.18 : 0.82;
      final at = Vector2(
        size.x * (side + (_rng.nextDouble() - 0.5) * 0.30),
        // Starts low, finishes high: 0.42 of the screen down to 0.10.
        size.y * (0.42 - k * 0.32 + (_rng.nextDouble() - 0.5) * 0.05),
      );
      _firework(at, colors[i % colors.length],
          delay: t, scale: 0.95 + k * 0.5 + _rng.nextDouble() * 0.2);
      t += 0.26 - k * 0.10; // accelerando
    }

    // 3. The held beat — the most important third of a second in the show.
    t += 0.34;

    // 4. Five across the full width, one sound covering all of them.
    for (var i = 0; i < 5; i++) {
      final at = Vector2(
        size.x * (0.12 + i * 0.19 + (_rng.nextDouble() - 0.5) * 0.06),
        size.y * (0.10 + _rng.nextDouble() * 0.22),
      );
      _firework(at, colors[(i + 2) % colors.length],
          delay: t + i * 0.06,
          scale: 1.5 + _rng.nextDouble() * 0.35,
          mute: true,
          onBreak: i == 0 ? Audio.instance.fwFinale : null);
    }

    // ...and the willow that hangs over the whole thing.
    _willow(Vector2(size.x * 0.5, size.y * 0.16), delay: t + 0.30);
  }

  /// A gold willow: a wide, slow canopy that keeps falling after the bangs.
  ///
  /// Separate from [_firework] because it is the opposite shape — where a shell
  /// is fast and radial and gone in a second and a half, this is slow, heavily
  /// drag-damped and lasts three, so the screen is still alive while the
  /// results card is on its way in. It is what stops the show ending on a bang
  /// and then nothing.
  void _willow(Vector2 at, {double delay = 0}) {
    _root.add(TimerComponent(
      period: max(delay, 0.001),
      removeOnFinish: true,
      onTick: () {
        Audio.instance.fwCrackle();
        _skyFlash(at, const Color(0xFFFFD678), cell * 5.0);
        const n = 54;
        _root.add(ParticleSystemComponent(
          position: at,
          priority: 69,
          particle: Particle.generate(
            count: n,
            lifespan: 3.4,
            applyLifespanToChildren: false,
            generator: (i) {
              // Biased towards the horizontal so the canopy spreads wide before
              // gravity takes it, which is what makes a willow read as a willow
              // rather than as a slow sphere.
              final a = (i / n) * pi * 2 + (_rng.nextDouble() - 0.5) * 0.3;
              final sp = (150 + _rng.nextDouble() * 120);
              return _star(
                Vector2(cos(a) * sp * 1.35, sin(a) * sp * 0.55),
                const Color(0xFFFFD678),
                lifespan: 2.6 + _rng.nextDouble() * 0.8,
                radius: cell * 0.055,
              );
            },
          ),
        ));
      },
    ));
  }

  /// Win celebration: a shine wave across the board, light motes, one ring —
  /// then, outside the App tab, fireworks and a spoken line over a drum fill.
  ///
  /// [finale] is the last vault in the game. It runs the grand show instead,
  /// and holds roughly twice as long so the willow is still falling rather than
  /// being cut off by the results card — a finale that gets interrupted is
  /// worse than no finale, because the player sees that something was meant to
  /// happen and did not.
  Future<void> celebrate({bool finale = false}) async {
    _busy = true;
    Audio.instance.ting();
    _flash(AppTheme.accentHover, 0.35);
    shake(4);
    final diag = board.rows + board.cols - 2;
    for (final g in _gems.values) {
      final d = (g.pos.r + g.pos.c) / max(1, diag);
      g.shine(delay: d * 0.9);
      g.add(ScaleEffect.to(Vector2.all(1.18),
          EffectController(duration: 0.14, reverseDuration: 0.22, startDelay: d * 0.9, curve: Curves.easeOut)));
    }
    _root.add(ParticleSystemComponent(
      priority: 60,
      particle: Particle.generate(
        count: 40,
        lifespan: 1.6,
        generator: (i) {
          final x = _rng.nextDouble() * size.x, y = size.y * (0.4 + _rng.nextDouble() * 0.6);
          final r = 1.5 + _rng.nextDouble() * 2.5;
          return AcceleratedParticle(
            position: Vector2(x, y),
            speed: Vector2((_rng.nextDouble() - 0.5) * 30, -40 - _rng.nextDouble() * 70),
            child: ComputedParticle(renderer: (canvas, p) {
              final a = (1 - p.progress) * (0.5 + 0.5 * sin(p.progress * pi * 6));
              canvas.drawCircle(
                  Offset.zero, r * (1 + p.progress * 0.5), Paint()..color = AppTheme.accentHover.withValues(alpha: a));
            }),
          );
        },
      ),
    ));
    await Future.delayed(const Duration(milliseconds: 450));
    if (_dead) return;
    Audio.instance.win();
    _shockwave(Vector2(size.x / 2, size.y / 2), size.x * (finale ? 1.15 : 0.8),
        AppTheme.accent);
    if (finale) _flash(AppTheme.accentHover, 0.5);
    _fireworkShow(grand: finale);
    if (!Audio.inAppTab) {
      Audio.instance.winFill();
      // Let two shells break before the line, so it lands inside the show
      // rather than on top of the first lift.
      await Future.delayed(const Duration(milliseconds: 950));
      if (_dead) return;
      Audio.instance.voWinner();
      if (finale) {
        // The grand show: opening pair, a nine-shell climbing run, the held
        // beat, five together, then the willow falling for 3.4 s. About 7 s
        // end to end from the first lift; 950 ms of it has already passed.
        await Future.delayed(const Duration(milliseconds: 5200));
        if (_dead) return;
        // One more spoken line over the falling willow. The show has earned a
        // second one by this point, and it fills what would otherwise be the
        // quietest part of it.
        Audio.instance.voPraise(big: true);
        await Future.delayed(const Duration(milliseconds: 1400));
      } else {
        // The six shells run ~2.2 s, the finale trio breaks around 2.6 s, and
        // the willows fall for another 2.4 s after that. Hold for it — cutting
        // to the results card mid-break is what made the old one feel clipped.
        await Future.delayed(const Duration(milliseconds: 3600));
      }
    } else {
      await Future.delayed(const Duration(milliseconds: 900));
    }
  }

  // ------------------------------------------------------------ loop

  @override
  void update(double dt) {
    super.update(dt);
    if (_introPending && size.x > 0) _runIntro();
    if (_shake > 0.2) {
      _root.position = Vector2((_rng.nextDouble() - 0.5) * _shake, (_rng.nextDouble() - 0.5) * _shake);
      _shake *= pow(0.02, dt).toDouble();
    } else if (_root.position != Vector2.zero()) {
      _root.position = Vector2.zero();
      _shake = 0;
    }
    if (_busy || _ended) {
      _idle = 0;
      return;
    }
    _idle += dt;
    if (_idle > 4 && _hint == null) {
      _hint = board.findHint();
      if (_hint != null) {
        Audio.instance.coinSpin();
        _gems[board.at(_hint!.$1)?.id]?.hinting = true;
        _gems[board.at(_hint!.$2)?.id]?.hinting = true;
      }
    }
  }

  void _clearHint() {
    _idle = 0;
    if (_hint != null) {
      for (final g in _gems.values) {
        g.hinting = false;
      }
      _hint = null;
    }
  }
}

/// One piece sprite with special-overlay rendering and small animations.
class GemComponent extends SpriteComponent {
  /// DGD circle-G logo, white, used as the special-piece badge.
  static Sprite? logo;
  Gem gem;
  Pos pos;
  bool selected = false;
  bool hinting = false;
  double _t = 0;
  // Shine: periodic specular sweep + occasional sparkle.
  static final _r = Random();
  double _sheenAt = 1 + _r.nextDouble() * 6;
  double _sheenT = -1;
  double _sparkAt = 2 + _r.nextDouble() * 8;
  double _sparkT = -1;
  Offset _sparkPos = Offset.zero;

  GemComponent({
    required this.gem,
    required Sprite sprite,
    required this.pos,
    required Vector2 position,
    required Vector2 size,
  }) : super(sprite: sprite, position: position, size: size, anchor: Anchor.center);

  /// Completers handed out by [moveTo], [pop] and [pulse] that have not fired.
  ///
  /// An effect's `onComplete` never runs if the component is removed while the
  /// effect is mid-flight — which is exactly what happens when the player backs
  /// out of a level during a cascade. The cascade loop in Match3Game is sitting
  /// on one of these futures, so it would never resume, never return, and would
  /// hold the game, its board and every sprite alive for the life of the
  /// process. Completing them on removal lets the loop unwind and the whole
  /// graph get collected.
  final List<Completer<void>> _pending = [];

  Completer<void> _track() {
    final c = Completer<void>();
    _pending.add(c);
    return c;
  }

  void _settle(Completer<void> c) {
    _pending.remove(c);
    if (!c.isCompleted) c.complete();
  }

  @override
  void onRemove() {
    for (final c in _pending) {
      if (!c.isCompleted) c.complete();
    }
    _pending.clear();
    super.onRemove();
  }

  Future<void> moveTo(Vector2 target, double seconds,
      {Curve curve = Curves.easeOut, double delay = 0}) {
    final c = _track();
    add(MoveToEffect(target, EffectController(duration: seconds, curve: curve, startDelay: delay),
        onComplete: () => _settle(c)));
    return c.future;
  }

  Future<void> pop() {
    final c = _track();
    add(ScaleEffect.to(Vector2.all(1.3), EffectController(duration: 0.06)));
    add(ScaleEffect.to(Vector2.zero(),
        EffectController(duration: 0.14, startDelay: 0.06, curve: Curves.easeIn), onComplete: () {
      removeFromParent();
      _settle(c);
    }));
    return c.future;
  }

  Future<void> pulse() {
    final c = _track();
    add(ScaleEffect.to(Vector2.all(1.35),
        EffectController(duration: 0.12, reverseDuration: 0.14, curve: Curves.easeOut),
        onComplete: () => _settle(c)));
    return c.future;
  }

  void squash() {
    add(ScaleEffect.to(Vector2(1.12, 0.86),
        EffectController(duration: 0.06, reverseDuration: 0.10, curve: Curves.easeOut)));
  }

  void wiggle() {
    add(RotateEffect.by(0.18, EffectController(duration: 0.05, reverseDuration: 0.05, repeatCount: 2)));
  }

  /// Force a sheen sweep and a sparkle after [delay] seconds.
  void shine({double delay = 0}) {
    _sheenT = -1;
    _sheenAt = _t + delay;
    _sparkT = -1;
    _sparkAt = _t + delay + 0.3;
  }

  @override
  void update(double dt) {
    super.update(dt);
    _t += dt;
    if (_sheenT < 0) {
      if (_t >= _sheenAt) _sheenT = 0;
    } else {
      _sheenT += dt / 0.75;
      if (_sheenT >= 1) {
        _sheenT = -1;
        _sheenAt = _t + 2 + _r.nextDouble() * 7;
      }
    }
    if (_sparkT < 0) {
      if (_t >= _sparkAt) {
        _sparkT = 0;
        final a = _r.nextDouble() * pi * 2, d = 0.18 + _r.nextDouble() * 0.22;
        _sparkPos = Offset(0.5 + cos(a) * d, 0.5 + sin(a) * d);
      }
    } else {
      _sparkT += dt / 0.45;
      if (_sparkT >= 1) {
        _sparkT = -1;
        _sparkAt = _t + 3 + _r.nextDouble() * 9;
      }
    }
  }

  /// Material pieces are flat and tonal: no specular sweep, no sparkle.
  /// Kept as a no-op so the call sites and the shine() hook stay intact.
  void _renderShine(Canvas canvas, double s, Offset center) {
    return;
    // ignore: dead_code
    if (_sheenT >= 0) {
      canvas.save();
      canvas.clipPath(Path()..addOval(Rect.fromCircle(center: center, radius: s * 0.45)));
      canvas.translate(center.dx, center.dy);
      canvas.rotate(-0.6);
      final x = -s * 1.1 + _sheenT * s * 2.2;
      final band = Rect.fromLTWH(x - s * 0.22, -s, s * 0.44, s * 2);
      canvas.drawRect(
          band,
          Paint()
            ..shader = const LinearGradient(
              colors: [Color(0x00FFFFFF), Color(0x99FFFFFF), Color(0x00FFFFFF)],
            ).createShader(band)
            ..blendMode = BlendMode.plus);
      canvas.restore();
    }
    if (_sparkT >= 0) {
      final p = _sparkT;
      final k = p < 0.5 ? p * 2 : (1 - p) * 2; // in/out
      final c = Offset(_sparkPos.dx * s, _sparkPos.dy * s);
      final len = s * 0.16 * k;
      final paint = Paint()
        ..color = Colors.white.withValues(alpha: 0.95 * k)
        ..strokeWidth = s * 0.03
        ..strokeCap = StrokeCap.round;
      canvas.drawLine(c - Offset(len, 0), c + Offset(len, 0), paint);
      canvas.drawLine(c - Offset(0, len), c + Offset(0, len), paint);
      canvas.drawLine(c - Offset(len * 0.4, len * 0.4), c + Offset(len * 0.4, len * 0.4), paint..strokeWidth = s * 0.018);
      canvas.drawLine(c - Offset(len * 0.4, -len * 0.4), c + Offset(len * 0.4, -len * 0.4), paint);
      canvas.drawCircle(c, s * 0.05 * k, Paint()..color = Colors.white.withValues(alpha: 0.9 * k)..maskFilter = const MaskFilter.blur(BlurStyle.normal, 4));
    }
  }

  @override
  void render(Canvas canvas) {
    final s = size.x;
    final center = Offset(s / 2, s / 2);
    if (selected || hinting) {
      final pulse = 0.5 + 0.5 * sin(_t * 7);
      canvas.drawCircle(
          center,
          s * (0.6 + 0.05 * pulse),
          Paint()
            ..color = AppTheme.accentHover.withValues(alpha: selected ? 0.5 : 0.22 + 0.18 * pulse)
            ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 12));
    }
    if (gem.isSpecial) {
      // All specials glow; bombs glow hardest.
      final strong = gem.special == Special.bomb;
      canvas.drawCircle(
          center,
          s * (strong ? 0.62 : 0.55) + sin(_t * 5) * s * 0.03,
          Paint()
            ..color = AppTheme.accentHover.withValues(alpha: strong ? 0.55 : 0.3)
            ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 14));
    }
    super.render(canvas);
    _renderShine(canvas, s, center);
    void badge(double frac, double alpha, {Offset? at}) {
      logo?.render(canvas,
          position: Vector2((at ?? center).dx, (at ?? center).dy),
          size: Vector2.all(s * frac),
          anchor: Anchor.center,
          overridePaint: Paint()..color = Colors.white.withValues(alpha: alpha));
    }

    switch (gem.special) {
      case Special.stripedH:
      case Special.stripedV:
        // Two comet stripes either side of a small DGD badge, in the fire direction.
        final p = Paint()
          ..color = Colors.white.withValues(alpha: 0.92)
          ..strokeWidth = s * 0.075
          ..strokeCap = StrokeCap.round;
        final h = gem.special == Special.stripedH;
        for (final sgn in [-1, 1]) {
          final a0 = s * 0.5 + sgn * s * 0.22, a1 = s * 0.5 + sgn * s * 0.42;
          if (h) {
            canvas.drawLine(Offset(a0, s * 0.5), Offset(a1, s * 0.5), p);
          } else {
            canvas.drawLine(Offset(s * 0.5, a0), Offset(s * 0.5, a1), p);
          }
        }
        badge(0.34, 0.95);
      case Special.wrapped:
        // Coin-roll wrapper band + DGD badge.
        canvas.drawRRect(
            RRect.fromRectAndRadius(
                Rect.fromLTWH(s * 0.08, s * 0.08, s * 0.84, s * 0.84), Radius.circular(s * 0.2)),
            Paint()
              ..color = Colors.white.withValues(alpha: 0.9)
              ..style = PaintingStyle.stroke
              ..strokeWidth = s * 0.07);
        badge(0.36, 0.95);
      case Special.bomb:
        // Big pulsing DGD mark over the coin.
        final k = 0.5 + 0.5 * sin(_t * 6);
        canvas.drawCircle(center, s * 0.46,
            Paint()..color = const Color(0xFF030303).withValues(alpha: 0.35 + 0.15 * k));
        badge(0.62 + 0.06 * k, 1.0);
        canvas.drawCircle(
            center,
            s * 0.49 + k * s * 0.03,
            Paint()
              ..color = Colors.white.withValues(alpha: 0.9)
              ..style = PaintingStyle.stroke
              ..strokeWidth = s * 0.05);
      case Special.none:
        break;
    }
  }
}

class _BoardBackdrop extends Component {
  final Match3Game game;
  _BoardBackdrop(this.game) : super(priority: -1);

  @override
  void render(Canvas canvas) {
    final sprite = game._cellSprite;
    for (var r = 0; r < game.board.rows; r++) {
      for (var c = 0; c < game.board.cols; c++) {
        final pos = Vector2(game.origin.x + c * game.cell, game.origin.y + r * game.cell);
        if (sprite != null) {
          sprite.render(canvas, position: pos, size: Vector2.all(game.cell));
        } else {
          canvas.drawRRect(
              RRect.fromRectAndRadius(
                  Rect.fromLTWH(pos.x + 1.5, pos.y + 1.5, game.cell - 3, game.cell - 3),
                  Radius.circular(game.cell * 0.18)),
              Paint()..color = const Color(0x0AFFFFFF));
        }
        // Ledger seals sit under the coins, so they are part of the backdrop.
        final layers = game.board.seals[r][c];
        if (layers > 0) {
          final seal = layers >= 2 ? game._seal2 : game._seal1;
          seal?.render(canvas, position: pos, size: Vector2.all(game.cell));
        }
      }
    }
  }
}

/// Floating text (score popups, combo banner) with its own rise/fade/bounce.
class _FloatText extends PositionComponent {
  final String text;
  final double fontSize;
  final Color color;
  final double rise;
  final double life;
  final bool bounce;
  double _t = 0;
  late final TextPainter _tp;

  _FloatText(this.text, Vector2 at,
      {required double size,
      required this.color,
      this.rise = 26,
      this.life = 0.7,
      this.bounce = false})
      : fontSize = size,
        super(position: at, anchor: Anchor.center, priority: 70) {
    _tp = TextPainter(
      text: TextSpan(
        text: text,
        style: TextStyle(
          fontFamily: AppTheme.fontMono,
          fontSize: fontSize,
          fontWeight: FontWeight.w700,
          color: color,
          shadows: [Shadow(color: color.withValues(alpha: 0.7), blurRadius: 12)],
        ),
      ),
      textDirection: TextDirection.ltr,
    )..layout();
  }

  @override
  void update(double dt) {
    _t += dt;
    if (_t >= life) removeFromParent();
  }

  @override
  void render(Canvas canvas) {
    final p = (_t / life).clamp(0.0, 1.0);
    final alpha = p < 0.7 ? 1.0 : 1 - (p - 0.7) / 0.3;
    final scale = bounce ? (p < 0.15 ? 0.6 + 0.4 * Curves.elasticOut.transform(p / 0.15) : 1.0) : 1.0;
    final dy = -rise * Curves.easeOut.transform(p);
    canvas.save();
    canvas.translate(0, dy);
    canvas.scale(scale);
    final paint = Paint()..color = Colors.white.withValues(alpha: alpha);
    canvas.saveLayer(null, paint);
    _tp.paint(canvas, Offset(-_tp.width / 2, -_tp.height / 2));
    canvas.restore();
    canvas.restore();
  }
}
