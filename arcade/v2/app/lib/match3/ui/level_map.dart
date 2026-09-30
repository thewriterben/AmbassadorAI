import 'dart:math';

import 'package:flutter/material.dart';

import '../../audio.dart';
import '../../dev.dart';
import '../../dev_soak.dart';
import '../../theme.dart';
import '../../ui_kit.dart';
import '../model/levels.dart';
import '../progress.dart';
import 'match3_screen.dart';
import '../../arcade/entry.dart';

/// Winding level path, newest at the top. Tap a node to see the goal and play.
class LevelMapScreen extends StatefulWidget {
  const LevelMapScreen({super.key});

  @override
  State<LevelMapScreen> createState() => _LevelMapScreenState();
}

class _LevelMapScreenState extends State<LevelMapScreen> {
  final _scroll = ScrollController();

  /// Coin Quest's tune starts on the map and carries on into every level;
  /// leaving the map for the arcade's menu fades it out.
  late final int _music;

  @override
  void initState() {
    super.initState();
    _music = Audio.instance.claimMusic(Audio.trackQuest);
    // A failure here must not go unreported: load() clears its maps before
    // reading, so a silent throw would leave the map showing level 1 only.
    Progress.instance.load().then(
          (_) => _scrollToCurrent(),
          onError: (Object e) => debugPrint('progress load: $e'),
        );
  }

  @override
  void dispose() {
    Audio.instance.releaseMusic(_music);
    _scroll.dispose();
    super.dispose();
  }

  /// Opens the map on the level the player is actually up to.
  ///
  /// Two changes here, one of which is not the bug I thought it was.
  ///
  /// I reported that the map "always opens at level 60". It does not — it was
  /// opening at level 60 on the test device because that device is genuinely on
  /// level 59, having been pushed through the first fifty by the DEV world-jump
  /// and then played to 58. `unlocked` was 59, the target clamped to 0, and the
  /// top of the list is correct behaviour. The original code worked.
  ///
  /// What is still worth having:
  ///
  ///  * **The post-frame callback.** `main()` kicks off `Progress.load()` at
  ///    startup, so by the time the map opens that future can already be
  ///    complete and the callback can fire before the ListView has attached the
  ///    controller. `_scroll.hasClients` is then false and the early return
  ///    swallows the scroll silently. It is a real race even if it is not what
  ///    was happening here; waiting a frame removes it.
  ///  * **jumpTo rather than animateTo.** This is where the map should have
  ///    opened, not a place to travel to. Animating it means watching the list
  ///    fly past for half a second before you can touch anything, every visit.
  void _scrollToCurrent() {
    if (!mounted) return;
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (!mounted || !_scroll.hasClients) return;
      // The list runs 60 at the top down to 1 at the bottom, so the offset of a
      // level counts from the end. The 200 leaves the current node a little
      // below the app bar rather than jammed under it.
      final idx = levels.length - Progress.instance.unlocked;
      final target = (idx * _nodeSpacing - 200).clamp(0.0, _scroll.position.maxScrollExtent);
      // Jump rather than animate. This is where the map should have opened, not
      // a place to travel to — animating means watching thirty levels fly past
      // before you can do anything, on every visit.
      _scroll.jumpTo(target);
    });
  }

  static const _nodeSpacing = 112.0;

  void _openSheet(Level level) {
    Audio.instance.coinsPour();
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (_) => _LevelSheet(level: level),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.bg,
      body: SafeArea(
        child: ListenableBuilder(
          listenable: Progress.instance,
          builder: (context, _) {
            final prog = Progress.instance;
            final current = levels[(prog.unlocked - 1).clamp(0, levels.length - 1)];
            return Column(
              children: [
                Padding(
                  padding: const EdgeInsets.fromLTRB(24, 16, 24, 0),
                  child: Column(children: [
                    ScreenHeader(
                      title: 'Coin Quest',
                      subtitle: 'Digital Gold',
                      subtitleUnderTitle: true,
                      onBack: () => leaveScreen(context),
                      actions: [
                        // The `if (Dev.enabled)` is here, at the call site, and
                        // not only inside DevMenu. Dev.enabled is a const false in
                        // any build without --dart-define=DGD_DEV=true, so a
                        // collection-if folds away and the closures below —
                        // including the one naming DevSoakScreen — become
                        // unreachable and are tree-shaken (REDTEAM-1.0.5-2026-09-21.md,
                        // F1).
                        if (Dev.enabled)
                          DevMenu(
                            title: 'COIN QUEST',
                            actions: {
                              for (final w in worlds)
                                'Open ${w.name} — level ${w.firstLevel}': () =>
                                    Progress.instance.devUnlockThrough(w.firstLevel),
                              'Audio soak test': () =>
                                  Navigator.push(context, MaterialPageRoute(builder: (_) => const DevSoakScreen())),
                              'Reset all progress': () => Progress.instance.eraseAll(),
                            },
                          ),
                      ],
                    ),
                    const SizedBox(height: 22),
                    _StarsCard(stars: prog.totalStars, of: levels.length * 3, count: levels.length),
                  ]),
                ),
                Expanded(
                  child: Stack(
                    children: [
                      const Positioned.fill(child: CustomPaint(painter: _DotGrid())),
                      LayoutBuilder(
                        builder: (context, box) {
                          final w = box.maxWidth;
                          return ListView.builder(
                            controller: _scroll,
                            padding: const EdgeInsets.only(top: 16, bottom: 16),
                            itemCount: levels.length,
                            itemBuilder: (context, i) {
                              final lv = levels[levels.length - 1 - i];
                              final x = _xFor(lv.id, w);
                              final next = lv.id < levels.length ? _xFor(lv.id + 1, w) : null;
                              return SizedBox(
                                height: _nodeSpacing,
                                child: Stack(
                                  clipBehavior: Clip.none,
                                  children: [
                                    Positioned.fill(
                                      child: CustomPaint(
                                        painter: _PathPainter(x, next, _nodeSpacing, lit: lv.id < prog.unlocked),
                                      ),
                                    ),
                                    Builder(builder: (context) {
                                      final size = _Node.sizeFor(lv.id == prog.unlocked);
                                      return Positioned(
                                        left: x - size / 2,
                                        top: _nodeSpacing / 2 - size / 2 - 8,
                                        child: _Node(level: lv, onOpen: () => _openSheet(lv)),
                                      );
                                    }),
                                  ],
                                ),
                              );
                            },
                          );
                        },
                      ),
                    ],
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.fromLTRB(24, 10, 24, 16),
                  child: Column(children: [
                    Text('Scroll to explore all ${levels.length} levels',
                        style: const TextStyle(fontSize: 14, color: AppTheme.body)),
                    const SizedBox(height: 18),
                    _CurrentCard(level: current, stars: prog.stars(current.id), onPlay: () => _openSheet(current)),
                  ]),
                ),
              ],
            );
          },
        ),
      ),
    );
  }

  double _xFor(int id, double w) => w / 2 + sin(id * 0.9) * (w * 0.28);
}

/// Level numbers in two digits, as the map and its cards set them.
String _two(int id) => id.toString().padLeft(2, '0');

/// The quiet dot grid the map sits on.
class _DotGrid extends CustomPainter {
  const _DotGrid();

  @override
  void paint(Canvas canvas, Size size) {
    final p = Paint()..color = const Color(0xFF1E1E21);
    const step = 32.0;
    for (var y = step / 2; y < size.height; y += step) {
      for (var x = step / 2; x < size.width; x += step) {
        canvas.drawCircle(Offset(x, y), 1.4, p);
      }
    }
  }

  @override
  bool shouldRepaint(_DotGrid old) => false;
}

/// "Stars collected" with the count, and the number of levels.
class _StarsCard extends StatelessWidget {
  final int stars, of, count;
  const _StarsCard({required this.stars, required this.of, required this.count});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 16),
      decoration: BoxDecoration(
        color: AppTheme.card,
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: AppTheme.border),
      ),
      child: Row(crossAxisAlignment: CrossAxisAlignment.end, children: [
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            const Text('Stars collected', style: TextStyle(fontSize: 14, color: AppTheme.body)),
            const SizedBox(height: 10),
            Row(children: [
              const HugeIcon('star', size: 22, color: AppTheme.accent),
              const SizedBox(width: 14),
              Text('$stars / $of', style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 22, color: AppTheme.text)),
            ]),
          ]),
        ),
        Column(crossAxisAlignment: CrossAxisAlignment.end, children: [
          Text('$count', style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 22, color: AppTheme.text)),
          const SizedBox(height: 6),
          const Text('levels', style: TextStyle(fontSize: 14, color: AppTheme.body)),
        ]),
      ]),
    );
  }
}

/// A level's three stars as outlines, the earned ones in orange.
class _Stars extends StatelessWidget {
  final int earned;
  final double size;
  const _Stars(this.earned, {this.size = 16});

  @override
  Widget build(BuildContext context) => Row(mainAxisSize: MainAxisSize.min, children: [
        for (var s = 1; s <= 3; s++) ...[
          if (s > 1) SizedBox(width: size * 0.15),
          HugeIcon('star', size: size, color: s <= earned ? AppTheme.accent : AppTheme.body),
        ],
      ]);
}

/// The level the player is up to, with Play: it opens the same goal sheet a
/// tap on the node does.
class _CurrentCard extends StatelessWidget {
  final Level level;
  final int stars;
  final VoidCallback onPlay;
  const _CurrentCard({required this.level, required this.stars, required this.onPlay});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(24, 22, 24, 16),
      decoration: BoxDecoration(
        color: AppTheme.card,
        borderRadius: BorderRadius.circular(28),
        border: Border.all(color: AppTheme.border),
      ),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Row(children: [
          Expanded(
            child: Text('Level ${_two(level.id)}',
                style: const TextStyle(fontSize: 24, fontWeight: FontWeight.w500, letterSpacing: -0.4, color: AppTheme.text)),
          ),
          _Stars(stars, size: 18),
        ]),
        const SizedBox(height: 8),
        Text('$stars / 3 stars', style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 14, color: AppTheme.body)),
        const SizedBox(height: 18),
        SizedBox(
          width: double.infinity,
          height: 52,
          child: FilledButton(
            onPressed: onPlay,
            style: FilledButton.styleFrom(padding: EdgeInsets.zero),
            child: Row(mainAxisSize: MainAxisSize.min, children: [
              const HugeIcon('play', size: 18, color: AppTheme.onAccent),
              const SizedBox(width: 10),
              Text('Play level ${level.id}'),
            ]),
          ),
        ),
      ]),
    );
  }
}

class _PathPainter extends CustomPainter {
  final double x;
  final double? next;
  final double h;
  final bool lit;
  _PathPainter(this.x, this.next, this.h, {required this.lit});

  @override
  void paint(Canvas canvas, Size size) {
    if (next == null) return;
    // Dotted, as drawn: a dot every 11 dp along the curve to the next level
    // (above). Walked levels' paths are in the accent.
    final path = Path()
      ..moveTo(x, h / 2 - 8)
      ..cubicTo(x, 0, next!, h / 2, next!, -h / 2 - 8);
    final dot = Paint()..color = lit ? AppTheme.accent.withValues(alpha: 0.7) : const Color(0xFF4A4A4A);
    // Each row paints after the row above it, so a dot inside either node's
    // box would land on top of that node: leave those out.
    final ends = [Offset(x, h / 2 - 8), Offset(next!, -h / 2 - 8)];
    bool inNode(Offset o) => ends.any((e) => (o.dx - e.dx).abs() < 46 && (o.dy - e.dy).abs() < 50);
    for (final m in path.computeMetrics()) {
      for (var d = 0.0; d < m.length; d += 11) {
        final t = m.getTangentForOffset(d);
        if (t != null && !inNode(t.position)) canvas.drawCircle(t.position, 2.2, dot);
      }
    }
  }

  @override
  bool shouldRepaint(covariant _PathPainter old) => old.lit != lit || old.x != x || old.next != next;
}

class _Node extends StatelessWidget {
  final Level level;
  final VoidCallback onOpen;
  const _Node({required this.level, required this.onOpen});

  /// The level the player is up to is drawn larger, as the map shows it.
  static double sizeFor(bool current) => current ? 100.0 : 80.0;

  @override
  Widget build(BuildContext context) {
    final prog = Progress.instance;
    final locked = level.id > prog.unlocked;
    final current = level.id == prog.unlocked;
    final stars = prog.stars(level.id);
    final size = sizeFor(current);
    return Semantics(
      button: !locked,
      label: locked ? 'Level ${level.id}, locked' : 'Level ${level.id}, $stars of 3 stars',
      excludeSemantics: true,
      child: GestureDetector(
        onTap: locked ? null : onOpen,
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            SizedBox(
              width: size,
              height: size,
              child: Stack(
                alignment: Alignment.center,
                children: [
                  // The locked node draws its padlock where the number goes.
                  Image.asset('assets/images/node_${current ? 'current' : locked ? 'locked' : 'done'}.png',
                      width: size, height: size),
                  // The number is part of the node's artwork, in the slot below
                  // the coin, so it does not grow with the system text size
                  // (it would cover the coin); the node's semantics label
                  // carries it for screen readers.
                  if (!locked)
                    Positioned(
                      bottom: size * 0.1,
                      child: Text(_two(level.id),
                          textScaler: TextScaler.noScaling,
                          style: TextStyle(
                              fontFamily: AppTheme.fontMono,
                              height: 1.0,
                              fontSize: size * 0.18,
                              fontWeight: FontWeight.w600,
                              color: current ? AppTheme.onAccent : AppTheme.text)),
                    ),
                ],
              ),
            ),
            const SizedBox(height: 4),
            if (!current) _Stars(stars, size: 15),
          ],
        ),
      ),
    );
  }
}

/// The goal, as a sheet: the vault's number, the goal with its figure set
/// large, moves and board, and Play.
class _LevelSheet extends StatelessWidget {
  final Level level;
  const _LevelSheet({required this.level});

  @override
  Widget build(BuildContext context) {
    final best = Progress.instance.best(level.id);
    final (verb, n, noun) = level.goalParts;
    return Container(
      margin: AppTheme.sheetMargin(context),
      padding: const EdgeInsets.fromLTRB(24, 10, 24, 24),
      decoration: BoxDecoration(
        color: AppTheme.card,
        borderRadius: BorderRadius.circular(28),
        border: Border.all(color: AppTheme.border),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Center(
            child: Container(
              width: 40,
              height: 4,
              decoration: BoxDecoration(color: AppTheme.borderStrong, borderRadius: BorderRadius.circular(2)),
            ),
          ),
          const SizedBox(height: 22),
          Text('VAULT ${_two(level.id)}',
              style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 12, letterSpacing: 1.4, color: AppTheme.accent)),
          const SizedBox(height: 18),
          Text(verb, style: const TextStyle(fontSize: 24, fontWeight: FontWeight.w500, color: AppTheme.text)),
          Text('$n',
              style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 60, height: 1.15, color: AppTheme.text)),
          Text(noun, style: const TextStyle(fontSize: 18, color: AppTheme.body)),
          const SizedBox(height: 20),
          Row(children: [
            Expanded(child: _stat('Moves', '${level.moves}')),
            const SizedBox(width: 12),
            Expanded(child: _stat('Board', '${level.rows} × ${level.cols}')),
            if (best > 0) ...[
              const SizedBox(width: 12),
              Expanded(child: _stat('Best', '$best')),
            ],
          ]),
          const SizedBox(height: 22),
          SizedBox(
            width: double.infinity,
            height: 52,
            child: FilledButton(
              onPressed: () {
                Audio.instance.tap();
                Navigator.pop(context);
                Navigator.push(context, MaterialPageRoute(builder: (_) => Match3Screen(level: level)));
              },
              child: const Text('Play'),
            ),
          ),
        ],
      ),
    );
  }

  Widget _stat(String k, String v) => Container(
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 14),
        decoration: BoxDecoration(color: AppTheme.surface, borderRadius: BorderRadius.circular(16)),
        child: Row(children: [
          Expanded(child: Text(k, style: const TextStyle(fontSize: 13, color: AppTheme.body))),
          Text(v, style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 16, color: AppTheme.text)),
        ]),
      );
}
