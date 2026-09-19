import 'dart:math';

import 'package:flame/components.dart';
import 'package:flame/events.dart';
import 'package:flame/game.dart';
import 'package:flame/particles.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart' show Colors;
import 'package:flutter/painting.dart';
import 'package:flutter/services.dart';

import '../../audio.dart';
import '../../theme.dart';

/// Tablet Run — an auto-runner through monetary history. The DGD coin rolls
/// from 1913 to the network; printing presses and inflation clouds are the
/// hazards; Knowledge Tablets pause the run for a question. Reflexes cost
/// time, never the reward: a stumble is a spin-out, not a death.
class TabletRunGame extends FlameGame with TapCallbacks, DragCallbacks {
  final int tabletCount;
  final void Function(int index) onTablet;
  final VoidCallback onFinish;
  final ValueNotifier<int> notifier = ValueNotifier(0);

  TabletRunGame({required this.tabletCount, required this.onTablet, required this.onFinish});

  // World
  static const baseSpeed = 300.0;
  double groundY = 0;
  double distance = 0;
  // Fixed length so the HUD can read `progress` before onLoad finishes
  // (on web, Sprite.load takes a real network round-trip).
  final double length = baseSpeed * 115; // ≈ 2 minutes at base speed
  double speed = baseSpeed;
  double speedMul = 1;
  double _stunT = 0;
  bool _paused = false;
  bool _finished = false;
  int stumbles = 0;
  int tabletsReached = 0;
  int tabletsOpened = 0;
  final _rng = Random();

  // Player
  // ignore: library_private_types_in_public_api
  late _Coin coin;
  double vy = 0;
  bool grounded = true;
  double slideT = 0;

  // Timeline
  final List<_Event> _events = [];
  int _nextEvent = 0;
  final List<_Scroller> _live = [];
  final List<_Beat> _beats = [];

  static const eraBeats = [
    '1913 · A new central bank',
    'Since then the dollar lost 96% of its purchasing power',
    r'$3 billion → $21 trillion: a 7,000-fold money supply',
    'At 2% inflation, half your purchasing power goes every 35 years',
    '1976 · Hayek: let the best money win',
    '2024 · The DGSB freezes a fixed benchmark',
    '21,000,000 coins. Ever.',
    'Fees and staking rewards are burned',
    'Money becomes money when it circulates link by link',
    'The network',
  ];

  double get progress => (distance / length).clamp(0, 1);
  List<double> get tabletFractions =>
      List.generate(tabletCount, (i) => (i + 1) / (tabletCount + 1) * 0.92 + 0.04);

  @override
  Color backgroundColor() => const Color(0x00000000);

  @override
  Future<void> onLoad() async {
    final sprite = await Sprite.load('coin_gold.png');
    groundY = size.y * 0.80;
    coin = _Coin(sprite: sprite, position: Vector2(size.x * 0.22, groundY - 30), size: Vector2.all(60));
    add(_Backdrop(this));
    add(coin);
    _buildTimeline();
  }

  void _buildTimeline() {
    final fr = tabletFractions;
    // Tablets at fixed fractions of the run.
    for (var i = 0; i < tabletCount; i++) {
      _events.add(_Event(fr[i] * length, _EventKind.tablet, i));
    }
    // Hazards every 2.5–4.5 s of distance, kept clear of tablets.
    var d = baseSpeed * 4;
    while (d < length - baseSpeed * 3) {
      final nearTablet = fr.any((f) => (f * length - d).abs() < baseSpeed * 1.6);
      if (!nearTablet) {
        _events.add(_Event(d, _rng.nextBool() ? _EventKind.press : _EventKind.cloud, 0));
      }
      d += baseSpeed * (2.5 + _rng.nextDouble() * 2);
    }
    // Era beats spread across the run.
    for (var i = 0; i < eraBeats.length; i++) {
      _events.add(_Event((i + 0.5) / eraBeats.length * length, _EventKind.beat, i));
    }
    _events.sort((a, b) => a.at.compareTo(b.at));
  }

  // ------------------------------------------------------------ input

  @override
  void onTapDown(TapDownEvent event) {
    jump();
  }

  @override
  void onDragUpdate(DragUpdateEvent event) {
    super.onDragUpdate(event);
    if (event.localDelta.y > 8) slide();
    if (event.localDelta.y < -8) jump();
  }

  void jump() {
    if (_paused || _finished || !grounded || _stunT > 0) return;
    vy = -620;
    grounded = false;
    Audio.instance.coinFlip();
  }

  void slide() {
    if (_paused || _finished || _stunT > 0) return;
    if (!grounded) vy = 900; // slam down
    slideT = 0.7;
    Audio.instance.swap();
  }

  // ------------------------------------------------------------ loop

  @override
  void update(double dt) {
    super.update(dt);
    if (_paused || _finished) return;

    // Speed ramps gently; stun slows.
    speedMul = 1 + progress * 0.25;
    if (_stunT > 0) {
      _stunT -= dt;
      speed = baseSpeed * speedMul * 0.35;
    } else {
      speed = baseSpeed * speedMul;
    }
    distance += speed * dt;

    // Player physics.
    vy += 1700 * dt;
    coin.position.y += vy * dt;
    final restY = groundY - coin.size.y / 2;
    if (coin.position.y >= restY) {
      if (!grounded) Audio.instance.coinDrop();
      coin.position.y = restY;
      vy = 0;
      grounded = true;
    }
    coin.angle += (speed * dt) / (coin.size.x / 2);
    if (slideT > 0) {
      slideT -= dt;
      coin.scale = Vector2(1.15, 0.45);
    } else {
      coin.scale = Vector2.all(1);
    }
    coin.stunned = _stunT > 0;

    // Spawn events that have come into view.
    final spawnX = size.x + 80;
    while (_nextEvent < _events.length && _events[_nextEvent].at - distance < spawnX - coin.position.x) {
      _spawn(_events[_nextEvent]);
      _nextEvent++;
    }

    // Scroll + collide.
    for (final s in List.of(_live)) {
      s.position.x -= speed * dt;
      if (s.position.x < -200) {
        s.removeFromParent();
        _live.remove(s);
        continue;
      }
      if (s is _Tablet && !s.triggered && s.position.x <= coin.position.x + 10) {
        s.triggered = true;
        tabletsReached++;
        _paused = true;
        notifier.value++;
        onTablet(s.index);
      } else if (s is _Hazard && !s.hit && _stunT <= 0 && _overlaps(s)) {
        s.hit = true;
        stumbles++;
        _stunT = 0.9;
        HapticFeedback.heavyImpact();
        Audio.instance.invalid();
        _puff(s.position);
        s.removeFromParent();
        _live.remove(s);
        notifier.value++;
      }
    }
    for (final b in List.of(_beats)) {
      b.position.x -= speed * 0.6 * dt; // parallax: beats sit behind
      if (b.position.x < -600) {
        b.removeFromParent();
        _beats.remove(b);
      }
    }

    if (distance >= length) {
      _finished = true;
      notifier.value++;
      onFinish();
    }
  }

  bool _overlaps(_Hazard h) {
    final r = coin.size.x / 2 * (slideT > 0 ? 0.55 : 0.8);
    final cx = coin.position.x, cy = coin.position.y + (slideT > 0 ? coin.size.y * 0.25 : 0);
    final rect = h.rect;
    final nx = cx.clamp(rect.left, rect.right), ny = cy.clamp(rect.top, rect.bottom);
    return (cx - nx) * (cx - nx) + (cy - ny) * (cy - ny) < r * r;
  }

  void _spawn(_Event e) {
    final x = size.x + 80;
    switch (e.kind) {
      case _EventKind.press:
        final h = _Press(position: Vector2(x, groundY));
        _live.add(h);
        add(h);
      case _EventKind.cloud:
        final h = _Cloud(position: Vector2(x, groundY - 92));
        _live.add(h);
        add(h);
      case _EventKind.tablet:
        final t = _Tablet(index: e.index, position: Vector2(x, groundY));
        _live.add(t);
        add(t);
      case _EventKind.beat:
        final b = _Beat(eraBeats[e.index], position: Vector2(x + 200, groundY - 190));
        _beats.add(b);
        add(b);
    }
  }

  void _puff(Vector2 at) {
    add(ParticleSystemComponent(
      position: at,
      particle: Particle.generate(
        count: 14,
        lifespan: 0.5,
        generator: (i) => AcceleratedParticle(
          speed: Vector2((_rng.nextDouble() - 0.3) * 260, -_rng.nextDouble() * 220),
          acceleration: Vector2(0, 500),
          child: CircleParticle(radius: 3, paint: Paint()..color = AppTheme.muted),
        ),
      ),
    ));
  }

  /// Called by the screen once the tablet sheet closes.
  void resumeAfterTablet(int index, {required bool opened}) {
    if (opened) tabletsOpened++;
    for (final s in _live) {
      if (s is _Tablet && s.index == index) s.opened = opened;
    }
    _paused = false;
    notifier.value++;
  }
}

enum _EventKind { press, cloud, tablet, beat }

class _Event {
  final double at;
  final _EventKind kind;
  final int index;
  _Event(this.at, this.kind, this.index);
}

abstract class _Scroller extends PositionComponent {
  _Scroller({required super.position});
}

class _Coin extends SpriteComponent {
  bool stunned = false;
  double _t = 0;
  _Coin({required super.sprite, required super.position, required super.size})
      : super(anchor: Anchor.center);

  @override
  void update(double dt) {
    super.update(dt);
    _t += dt;
  }

  @override
  void render(Canvas canvas) {
    final s = size.x;
    canvas.drawCircle(
        Offset(s / 2, s / 2),
        s * 0.62,
        Paint()
          ..color = (stunned ? AppTheme.danger : AppTheme.accent).withValues(alpha: 0.35)
          ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 12));
    super.render(canvas);
    // Small trailing sheen flicker so it glimmers as it rolls.
    canvas.drawCircle(Offset(s * 0.32, s * 0.28), s * 0.07,
        Paint()..color = Colors.white.withValues(alpha: 0.35 + 0.3 * sin(_t * 9)));
  }
}

abstract class _Hazard extends _Scroller {
  bool hit = false;
  _Hazard({required super.position});
  Rect get rect;
}

/// Printing press: tall block with two rollers. Jump over it.
class _Press extends _Hazard {
  _Press({required super.position});
  @override
  Rect get rect => Rect.fromLTWH(position.x - 34, position.y - 78, 68, 78);

  @override
  void render(Canvas canvas) {
    const r = Rect.fromLTWH(-34, -78, 68, 78);
    canvas.drawRRect(RRect.fromRectAndRadius(r, const Radius.circular(8)),
        Paint()..color = const Color(0xFF1B1D25));
    canvas.drawRRect(RRect.fromRectAndRadius(r, const Radius.circular(8)),
        Paint()
          ..color = AppTheme.danger.withValues(alpha: 0.8)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2);
    final roller = Paint()..color = const Color(0xFF3A3F50);
    canvas.drawCircle(const Offset(-14, -52), 12, roller);
    canvas.drawCircle(const Offset(14, -52), 12, roller);
    canvas.drawRect(const Rect.fromLTWH(-26, -30, 52, 6), Paint()..color = AppTheme.muted);
    canvas.drawRect(const Rect.fromLTWH(-26, -20, 52, 6), Paint()..color = AppTheme.muted);
    // "printed" bills spilling out
    canvas.drawRect(const Rect.fromLTWH(-40, -10, 30, 8), Paint()..color = const Color(0xB32FB37A));
  }
}

/// Inflation cloud: hangs at head height. Slide under it.
class _Cloud extends _Hazard {
  double _t = 0;
  _Cloud({required super.position});
  @override
  Rect get rect => Rect.fromLTWH(position.x - 52, position.y - 26, 104, 52);

  @override
  void update(double dt) {
    super.update(dt);
    _t += dt;
    position.y += sin(_t * 3) * 0.3;
  }

  @override
  void render(Canvas canvas) {
    final p = Paint()..color = const Color(0xFF3A3F50).withValues(alpha: 0.95);
    for (final c in const [Offset(-30, 4), Offset(-6, -12), Offset(20, -4), Offset(38, 8), Offset(8, 12)]) {
      canvas.drawCircle(c, 22, p);
    }
    canvas.drawCircle(const Offset(-6, -12), 24,
        Paint()
          ..color = AppTheme.danger.withValues(alpha: 0.35)
          ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 10));
    final tp = TextPainter(
        text: const TextSpan(
            text: '%',
            style: TextStyle(
                fontFamily: AppTheme.fontMono, fontSize: 18, fontWeight: FontWeight.w700, color: AppTheme.danger)),
        textDirection: TextDirection.ltr)
      ..layout();
    tp.paint(canvas, const Offset(-7, -14));
  }
}

/// Knowledge Tablet: a stone slab with the DGD mark; opens (glows) when answered.
class _Tablet extends _Scroller {
  final int index;
  bool triggered = false;
  bool? opened;
  double _t = 0;
  _Tablet({required this.index, required super.position});

  @override
  void update(double dt) {
    super.update(dt);
    _t += dt;
  }

  @override
  void render(Canvas canvas) {
    final glowColor = opened == null
        ? AppTheme.accent
        : (opened! ? AppTheme.success : AppTheme.danger);
    canvas.drawCircle(const Offset(0, -60), 70,
        Paint()
          ..color = glowColor.withValues(alpha: 0.18 + 0.1 * sin(_t * 4))
          ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 30));
    final slab = RRect.fromRectAndRadius(const Rect.fromLTWH(-30, -110, 60, 110), const Radius.circular(14));
    canvas.drawRRect(slab, Paint()..color = const Color(0xFF14161E));
    canvas.drawRRect(slab, Paint()..color = glowColor..style = PaintingStyle.stroke..strokeWidth = 2);
    for (var i = 0; i < 4; i++) {
      canvas.drawLine(Offset(-18, -86 + i * 16), Offset(18, -86 + i * 16),
          Paint()..color = AppTheme.dim..strokeWidth = 3..strokeCap = StrokeCap.round);
    }
    canvas.drawCircle(const Offset(0, -24), 12, Paint()..color = glowColor);
    canvas.drawCircle(const Offset(0, -24), 6, Paint()..color = const Color(0xFF14161E));
  }
}

/// Era sign post, scrolled at parallax speed behind the action.
class _Beat extends PositionComponent {
  final String text;
  late final TextPainter _tp;
  _Beat(this.text, {required super.position}) {
    _tp = TextPainter(
      text: TextSpan(
        text: text,
        style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 12, color: AppTheme.body, letterSpacing: 0.5),
      ),
      textDirection: TextDirection.ltr,
    )..layout(maxWidth: 240);
  }

  @override
  void render(Canvas canvas) {
    final w = _tp.width + 24, h = _tp.height + 16;
    final r = RRect.fromRectAndRadius(Rect.fromLTWH(-w / 2, -h, w, h), const Radius.circular(10));
    canvas.drawRRect(r, Paint()..color = const Color(0xCC0B0D14));
    canvas.drawRRect(r, Paint()..color = AppTheme.borderStrong..style = PaintingStyle.stroke..strokeWidth = 1);
    _tp.paint(canvas, Offset(-w / 2 + 12, -h + 8));
    canvas.drawLine(const Offset(0, 0), const Offset(0, 190), Paint()..color = AppTheme.dim..strokeWidth = 2);
  }
}

/// Parallax backdrop: grid, skyline blocks, ground.
class _Backdrop extends Component {
  final TabletRunGame game;
  _Backdrop(this.game) : super(priority: -10);

  @override
  void render(Canvas canvas) {
    final s = game.size;
    final d = game.distance;
    // Far skyline (very slow)
    final far = Paint()..color = const Color(0xFF0D0F16);
    for (var i = -1; i < 12; i++) {
      final x = ((i * 140) - (d * 0.08) % 140);
      final h = (60 + (i * 37) % 90).toDouble();
      canvas.drawRect(Rect.fromLTWH(x, game.groundY - h, 90, h), far);
    }
    // Mid grid (slow)
    final grid = Paint()..color = const Color(0x12FFFFFF)..strokeWidth = 1;
    final off = (d * 0.3) % 80;
    for (var x = -off; x < s.x; x += 80) {
      canvas.drawLine(Offset(x, game.groundY - 220), Offset(x, game.groundY), grid);
    }
    // Ground
    canvas.drawRect(Rect.fromLTWH(0, game.groundY, s.x, s.y - game.groundY), Paint()..color = const Color(0xFF07080C));
    canvas.drawLine(Offset(0, game.groundY), Offset(s.x, game.groundY),
        Paint()..color = AppTheme.accent.withValues(alpha: 0.6)..strokeWidth = 2);
    final dash = Paint()..color = AppTheme.dim..strokeWidth = 2;
    final doff = d % 60;
    for (var x = -doff; x < s.x; x += 60) {
      canvas.drawLine(Offset(x, game.groundY + 18), Offset(x + 26, game.groundY + 18), dash);
    }
  }
}
