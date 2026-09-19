import 'dart:ui' as ui;

import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';

import '../audio.dart';
import '../theme.dart';
import 'asset_cache.dart';
import 'game_scaffold.dart';

/// Rope-cutting physics puzzle. Swipe across a rope to cut it; drop the coin
/// into the vault. Pure Dart Verlet rope, no physics engine required.
///
/// World coordinates are normalized: x in 0..1, y in 0..1.5 (portrait).
class RopeGame extends StatefulWidget {
  const RopeGame({super.key});

  @override
  State<RopeGame> createState() => _RopeGameState();
}

class _Level {
  final List<Offset> anchors;
  final Offset treat;
  final Offset vault;
  const _Level({required this.anchors, required this.treat, required this.vault});
}

const _levels = <_Level>[
  _Level(anchors: [Offset(0.5, 0.1)], treat: Offset(0.5, 0.5), vault: Offset(0.5, 1.25)),
  _Level(
      anchors: [Offset(0.2, 0.1), Offset(0.8, 0.1)],
      treat: Offset(0.5, 0.45),
      vault: Offset(0.22, 1.25)),
  _Level(
      anchors: [Offset(0.15, 0.1), Offset(0.5, 0.05), Offset(0.85, 0.15)],
      treat: Offset(0.5, 0.5),
      vault: Offset(0.8, 1.2)),
  _Level(
      anchors: [Offset(0.8, 0.1), Offset(0.9, 0.5)],
      treat: Offset(0.7, 0.55),
      vault: Offset(0.2, 1.05)),
];

class _Rope {
  final List<Offset> pts;
  final List<Offset> prev;
  final double segLen;
  bool cut = false;
  _Rope(this.pts, this.segLen) : prev = List.of(pts);
}

const _treatAsset = 'assets/images/rope_treat.png';
const _vaultAsset = 'assets/images/rope_vault.png';
const _anchorAsset = 'assets/images/rope_anchor.png';

class _RopeGameState extends State<RopeGame> with SingleTickerProviderStateMixin {
  static const worldH = 1.5;
  static const gravity = 1.6;
  static const segments = 12;
  static const treatR = 0.05;
  static const vaultR = 0.11;

  late Ticker ticker;
  Duration last = Duration.zero;
  int level = 0;
  late List<_Rope> ropes;
  late Offset treat, treatPrev;
  bool won = false, lost = false;
  Offset? swipeFrom;
  Size boxSize = Size.zero;
  Map<String, ui.Image>? images;

  _Level get lv => _levels[level];

  @override
  void initState() {
    super.initState();
    AssetCache.load([_treatAsset, _vaultAsset, _anchorAsset])
        .then((m) {
      // The decode outlives the screen if the player leaves during it.
      if (mounted) setState(() => images = m);
    });
    _load();
    ticker = createTicker(_frame)..start();
  }

  @override
  void dispose() {
    ticker.dispose();
    super.dispose();
  }

  void _load() {
    treat = lv.treat;
    treatPrev = treat;
    won = false;
    lost = false;
    ropes = lv.anchors.map((a) {
      final len = (lv.treat - a).distance / segments;
      final pts = List.generate(segments + 1, (i) => Offset.lerp(a, lv.treat, i / segments)!);
      return _Rope(pts, len);
    }).toList();
  }

  void _frame(Duration now) {
    if (last == Duration.zero) {
      last = now;
      return;
    }
    var dt = (now - last).inMicroseconds / 1e6;
    last = now;
    if (dt > 0.05) dt = 0.05;
    if (won || lost) return;

    final vel = treat - treatPrev;
    treatPrev = treat;
    treat = treat + vel * 0.995 + Offset(0, gravity * dt * dt);

    for (final r in ropes) {
      for (var i = 1; i <= segments; i++) {
        final v = r.pts[i] - r.prev[i];
        r.prev[i] = r.pts[i];
        r.pts[i] = r.pts[i] + v * 0.98 + Offset(0, gravity * dt * dt);
      }
    }

    for (var iter = 0; iter < 8; iter++) {
      for (var ri = 0; ri < ropes.length; ri++) {
        final r = ropes[ri];
        r.pts[0] = lv.anchors[ri];
        if (!r.cut) r.pts[segments] = treat;
        for (var i = 0; i < segments; i++) {
          final a = r.pts[i], b = r.pts[i + 1];
          final d = b - a;
          final dist = d.distance;
          if (dist == 0) continue;
          final diff = (dist - r.segLen) / dist;
          final corr = d * (0.5 * diff);
          if (i == 0) {
            r.pts[i + 1] = b - corr * 2;
          } else if (i + 1 == segments && !r.cut) {
            r.pts[i] = a + corr * 2;
          } else {
            r.pts[i] = a + corr;
            r.pts[i + 1] = b - corr;
          }
        }
        if (!r.cut) treat = r.pts[segments];
      }
    }

    if ((treat - lv.vault).distance < vaultR * 0.6) {
      won = true;
      Audio.instance.win();
    } else if (treat.dy > worldH + 0.3 || treat.dx < -0.3 || treat.dx > 1.3) {
      lost = true;
      Audio.instance.lose();
    }
    setState(() {});
  }

  Offset _toWorld(Offset px) => Offset(px.dx / boxSize.width, px.dy / boxSize.width);

  void _trySwipe(Offset a, Offset b) {
    for (final r in ropes) {
      if (r.cut) continue;
      for (var i = 0; i < segments; i++) {
        if (_segmentsIntersect(a, b, r.pts[i], r.pts[i + 1])) {
          r.cut = true;
          Audio.instance.swap();
          r.pts[segments] = r.pts[segments - 1];
          r.prev[segments] = r.pts[segments];
          break;
        }
      }
    }
  }

  static bool _segmentsIntersect(Offset p1, Offset p2, Offset p3, Offset p4) {
    double cross(Offset a, Offset b) => a.dx * b.dy - a.dy * b.dx;
    final d1 = cross(p4 - p3, p1 - p3);
    final d2 = cross(p4 - p3, p2 - p3);
    final d3 = cross(p2 - p1, p3 - p1);
    final d4 = cross(p2 - p1, p4 - p1);
    return ((d1 > 0) != (d2 > 0)) && ((d3 > 0) != (d4 > 0));
  }

  void _next() {
    setState(() {
      level = (level + 1) % _levels.length;
      _load();
    });
  }

  @override
  Widget build(BuildContext context) {
    return GameScaffold(
      title: 'Rope',
      score: level + 1,
      scoreLabel: 'Level',
      onReset: () => setState(_load),
      gameOver: lost,
      gameOverText: 'Missed the vault',
      bottom: Padding(
        padding: const EdgeInsets.only(top: 12),
        child: won
            ? FilledButton(onPressed: _next, child: const Text('Next level  →'))
            : const Text('SWIPE ACROSS A ROPE TO CUT IT',
                style: TextStyle(
                    fontFamily: AppTheme.fontMono,
                    fontSize: 11,
                    letterSpacing: 1,
                    color: AppTheme.muted)),
      ),
      child: AspectRatio(
        aspectRatio: 1 / worldH,
        child: LayoutBuilder(builder: (context, c) {
          boxSize = Size(c.maxWidth, c.maxHeight);
          return GestureDetector(
            onPanStart: (d) => swipeFrom = _toWorld(d.localPosition),
            onPanUpdate: (d) {
              final to = _toWorld(d.localPosition);
              if (swipeFrom != null) _trySwipe(swipeFrom!, to);
              swipeFrom = to;
            },
            onPanEnd: (_) => swipeFrom = null,
            child: Container(
              decoration: AppTheme.glass(
                  radius: 20, fill: const Color(0xCC050607), outline: AppTheme.borderStrong),
              clipBehavior: Clip.antiAlias,
              child: CustomPaint(
                painter: _RopePainter(
                  ropes: ropes,
                  treat: treat,
                  vault: lv.vault,
                  anchors: lv.anchors,
                  scale: c.maxWidth,
                  won: won,
                  images: images,
                ),
                size: Size.infinite,
              ),
            ),
          );
        }),
      ),
    );
  }
}

class _RopePainter extends CustomPainter {
  final List<_Rope> ropes;
  final Offset treat, vault;
  final List<Offset> anchors;
  final double scale;
  final bool won;
  final Map<String, ui.Image>? images;
  _RopePainter({
    required this.ropes,
    required this.treat,
    required this.vault,
    required this.anchors,
    required this.scale,
    required this.won,
    required this.images,
  });

  Offset _s(Offset w) => w * scale;

  void _img(Canvas canvas, String key, Offset center, double r) {
    final img = images?[key];
    if (img == null) {
      canvas.drawCircle(center, r, Paint()..color = AppTheme.accent);
      return;
    }
    canvas.drawImageRect(
      img,
      Rect.fromLTWH(0, 0, img.width.toDouble(), img.height.toDouble()),
      Rect.fromCenter(center: center, width: r * 2, height: r * 2),
      Paint()..filterQuality = FilterQuality.medium,
    );
  }

  @override
  void paint(Canvas canvas, Size size) {
    // Faint grid, like the site hero.
    final grid = Paint()
      ..color = const Color(0x08FFFFFF)
      ..strokeWidth = 1;
    for (var x = 0.0; x < size.width; x += size.width / 8) {
      canvas.drawLine(Offset(x, 0), Offset(x, size.height), grid);
    }
    for (var y = 0.0; y < size.height; y += size.width / 8) {
      canvas.drawLine(Offset(0, y), Offset(size.width, y), grid);
    }

    final rope = Paint()
      ..color = AppTheme.body
      ..strokeWidth = 3
      ..strokeCap = StrokeCap.round
      ..style = PaintingStyle.stroke;
    for (final r in ropes) {
      final path = Path()..moveTo(_s(r.pts[0]).dx, _s(r.pts[0]).dy);
      for (var i = 1; i < r.pts.length; i++) {
        path.lineTo(_s(r.pts[i]).dx, _s(r.pts[i]).dy);
      }
      canvas.drawPath(path, rope);
    }
    for (final a in anchors) {
      _img(canvas, _anchorAsset, _s(a), scale * 0.035);
    }

    // Vault glow + image
    final vp = _s(vault);
    canvas.drawCircle(
        vp,
        scale * _RopeGameState.vaultR * 1.4,
        Paint()
          ..color = const Color(0x33EA952D)
          ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 24));
    _img(canvas, _vaultAsset, vp, scale * _RopeGameState.vaultR * 1.15);

    if (!won) {
      _img(canvas, _treatAsset, _s(treat), scale * _RopeGameState.treatR * 1.3);
    }
  }

  @override
  bool shouldRepaint(covariant _RopePainter old) => true;
}
