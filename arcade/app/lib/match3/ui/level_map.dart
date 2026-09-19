import 'dart:math';

import 'package:flutter/material.dart';

import '../../audio.dart';
import '../../dev.dart';
import '../../dev_soak.dart';
import '../../theme.dart';
import '../model/levels.dart';
import '../progress.dart';
import 'match3_screen.dart';

/// Winding level path, newest at the top. Tap a node to see the goal and play.
class LevelMapScreen extends StatefulWidget {
  const LevelMapScreen({super.key});

  @override
  State<LevelMapScreen> createState() => _LevelMapScreenState();
}

class _LevelMapScreenState extends State<LevelMapScreen> {
  final _scroll = ScrollController();

  @override
  void initState() {
    super.initState();
    Audio.instance.setTrack(Audio.trackMap);
    // A failure here must not go unreported: load() clears its maps before
    // reading, so a silent throw would leave the map showing level 1 only.
    Progress.instance.load().then(
      (_) => _scrollToCurrent(),
      onError: (Object e) => debugPrint('progress load: $e'),
    );
  }

  @override
  void dispose() {
    _scroll.dispose();
    super.dispose();
  }

  void _scrollToCurrent() {
    if (!mounted || !_scroll.hasClients) return;
    final idx = levels.length - Progress.instance.unlocked;
    final target = (idx * _nodeSpacing - 200).clamp(0.0, _scroll.position.maxScrollExtent);
    _scroll.animateTo(target, duration: const Duration(milliseconds: 500), curve: Curves.easeOut);
  }

  static const _nodeSpacing = 118.0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.bg,
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        title: const Text('Coin Quest: Digital Gold', style: TextStyle(fontSize: 18)),
        actions: [
          Center(
            child: DevMenu(
              title: 'COIN QUEST',
              actions: {
                for (final w in worlds)
                  'Open ${w.name} — level ${w.firstLevel}': () =>
                      Progress.instance.devUnlockThrough(w.firstLevel),
                'Audio soak test': () => Navigator.push(context,
                    MaterialPageRoute(builder: (_) => const DevSoakScreen())),
                'Reset all progress': () => Progress.instance.devReset(),
              },
            ),
          ),
          const SizedBox(width: 10),
          ListenableBuilder(
            listenable: Progress.instance,
            builder: (_, __) => Center(
              child: Container(
                margin: const EdgeInsets.only(right: 16),
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                decoration: AppTheme.glass(radius: 999, outline: AppTheme.borderStrong),
                child: Row(children: [
                  const Icon(Icons.star_rounded, size: 16, color: AppTheme.accent),
                  const SizedBox(width: 4),
                  Text('${Progress.instance.totalStars}/${levels.length * 3}',
                      style: const TextStyle(
                          fontFamily: AppTheme.fontMono, fontSize: 13, color: AppTheme.text)),
                ]),
              ),
            ),
          ),
        ],
      ),
      body: Stack(
        children: [
          Positioned.fill(child: Image.asset('assets/images/bg_dark.png', fit: BoxFit.cover)),
          ListenableBuilder(
            listenable: Progress.instance,
            builder: (context, _) {
              final w = MediaQuery.sizeOf(context).width;
              return ListView.builder(
                controller: _scroll,
                padding: const EdgeInsets.only(top: 110, bottom: 60),
                itemCount: levels.length,
                itemBuilder: (context, i) {
                  final lv = levels[levels.length - 1 - i];
                  final x = _xFor(lv.id, w);
                  final next = lv.id < levels.length ? _xFor(lv.id + 1, w) : null;
                  final prev = lv.id > 1 ? _xFor(lv.id - 1, w) : null;
                  return SizedBox(
                    height: _nodeSpacing,
                    child: Stack(
                      children: [
                        Positioned.fill(
                          child: CustomPaint(
                            painter: _PathPainter(x, prev, next, _nodeSpacing,
                                lit: lv.id < Progress.instance.unlocked),
                          ),
                        ),
                        Positioned(
                          left: x - 40,
                          top: _nodeSpacing / 2 - 40,
                          child: _Node(level: lv),
                        ),
                      ],
                    ),
                  );
                },
              );
            },
          ),
        ],
      ),
    );
  }

  double _xFor(int id, double w) => w / 2 + sin(id * 0.9) * (w * 0.28);
}

class _PathPainter extends CustomPainter {
  final double x;
  final double? prev, next;
  final double h;
  final bool lit;
  _PathPainter(this.x, this.prev, this.next, this.h, {required this.lit});

  @override
  void paint(Canvas canvas, Size size) {
    final p = Paint()
      ..color = lit ? AppTheme.accent.withValues(alpha: 0.5) : AppTheme.borderStrong
      ..strokeWidth = 3
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round;
    // Line to the next level (above) and previous level (below).
    if (next != null) {
      canvas.drawPath(
          Path()
            ..moveTo(x, h / 2)
            ..cubicTo(x, 0, next!, h / 2, next!, -h / 2),
          p);
    }
  }

  @override
  bool shouldRepaint(covariant _PathPainter old) => old.lit != lit || old.x != x;
}

class _Node extends StatelessWidget {
  final Level level;
  const _Node({required this.level});

  @override
  Widget build(BuildContext context) {
    final prog = Progress.instance;
    final locked = level.id > prog.unlocked;
    final current = level.id == prog.unlocked;
    final stars = prog.stars(level.id);
    return GestureDetector(
      onTap: locked
          ? null
          : () {
              Audio.instance.coinsPour();
              _open(context);
            },
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          SizedBox(
            width: 80,
            height: 80,
            child: Stack(
              alignment: Alignment.center,
              children: [
                Image.asset(
                  'assets/images/node_${current ? 'current' : locked ? 'locked' : 'done'}.png',
                  width: 80,
                  height: 80,
                ),
                locked
                    ? const Icon(Icons.lock_rounded, color: AppTheme.dim, size: 22)
                    : Text('${level.id}',
                        style: TextStyle(
                            fontFamily: AppTheme.fontMono,
                            fontSize: 22,
                            fontWeight: FontWeight.w700,
                            color: current ? const Color(0xFF030303) : AppTheme.text)),
              ],
            ),
          ),
          const SizedBox(height: 6),
          Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              for (var s = 1; s <= 3; s++)
                Icon(Icons.star_rounded,
                    size: 16, color: s <= stars ? AppTheme.accent : AppTheme.dim),
            ],
          ),
        ],
      ),
    );
  }

  void _open(BuildContext context) {
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      builder: (_) => _LevelSheet(level: level),
    );
  }
}

class _LevelSheet extends StatelessWidget {
  final Level level;
  const _LevelSheet({required this.level});

  @override
  Widget build(BuildContext context) {
    final best = Progress.instance.best(level.id);
    return Container(
      margin: const EdgeInsets.all(16),
      padding: const EdgeInsets.all(24),
      decoration: AppTheme.glass(radius: 24, fill: AppTheme.card, outline: AppTheme.borderStrong),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('VAULT ${level.id}',
              style: const TextStyle(
                  fontFamily: AppTheme.fontMono,
                  fontSize: 11,
                  letterSpacing: 1.2,
                  color: AppTheme.muted)),
          const SizedBox(height: 6),
          Text(level.goalText,
              style: const TextStyle(
                  fontSize: 26,
                  fontWeight: FontWeight.w600,
                  letterSpacing: -0.6,
                  color: AppTheme.text)),
          const SizedBox(height: 12),
          Row(children: [
            _stat('MOVES', '${level.moves}'),
            const SizedBox(width: 12),
            _stat('BOARD', '${level.rows}×${level.cols}'),
            const SizedBox(width: 12),
            if (best > 0) _stat('BEST', '$best'),
          ]),
          const SizedBox(height: 20),
          SizedBox(
            width: double.infinity,
            child: FilledButton(
              onPressed: () {
                Audio.instance.tap();
                Navigator.pop(context);
                Navigator.push(
                    context, MaterialPageRoute(builder: (_) => Match3Screen(level: level)));
              },
              child: const Text('Play'),
            ),
          ),
        ],
      ),
    );
  }

  Widget _stat(String k, String v) => Container(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
        decoration: AppTheme.glass(radius: 999),
        child: Row(children: [
          Text('$k ',
              style: const TextStyle(
                  fontFamily: AppTheme.fontMono, fontSize: 10, letterSpacing: 1, color: AppTheme.muted)),
          Text(v,
              style: const TextStyle(
                  fontFamily: AppTheme.fontMono,
                  fontSize: 14,
                  fontWeight: FontWeight.w700,
                  color: AppTheme.text)),
        ]),
      );
}
