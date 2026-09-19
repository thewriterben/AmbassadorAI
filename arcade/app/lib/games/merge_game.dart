import 'dart:math';

import 'package:flutter/material.dart';

import '../audio.dart';
import '../theme.dart';
import 'game_scaffold.dart';

/// 2048-style merge game. Swipe to slide; equal tiles merge.
class MergeGame extends StatefulWidget {
  const MergeGame({super.key});

  @override
  State<MergeGame> createState() => _MergeGameState();
}

class _MergeGameState extends State<MergeGame> {
  static const n = 4;
  late List<List<int>> grid;
  int score = 0;
  bool gameOver = false;
  final rng = Random();

  @override
  void initState() {
    super.initState();
    _reset();
  }

  void _reset() {
    grid = List.generate(n, (_) => List.filled(n, 0));
    score = 0;
    gameOver = false;
    _spawn();
    _spawn();
  }

  void _spawn() {
    final empty = <Point<int>>[];
    for (var r = 0; r < n; r++) {
      for (var c = 0; c < n; c++) {
        if (grid[r][c] == 0) empty.add(Point(r, c));
      }
    }
    if (empty.isEmpty) return;
    final p = empty[rng.nextInt(empty.length)];
    grid[p.x][p.y] = rng.nextDouble() < 0.9 ? 2 : 4;
  }

  (List<int>, int) _slideRow(List<int> row) {
    final tiles = row.where((v) => v != 0).toList();
    final out = <int>[];
    var gained = 0;
    for (var i = 0; i < tiles.length; i++) {
      if (i + 1 < tiles.length && tiles[i] == tiles[i + 1]) {
        out.add(tiles[i] * 2);
        gained += tiles[i] * 2;
        i++;
      } else {
        out.add(tiles[i]);
      }
    }
    while (out.length < n) {
      out.add(0);
    }
    return (out, gained);
  }

  void _move(int dr, int dc) {
    if (gameOver) return;
    var moved = false;
    var gained = 0;
    final next = List.generate(n, (r) => List<int>.from(grid[r]));

    for (var i = 0; i < n; i++) {
      final line = <int>[];
      for (var j = 0; j < n; j++) {
        final r = dr == 0 ? i : (dr > 0 ? n - 1 - j : j);
        final c = dc == 0 ? i : (dc > 0 ? n - 1 - j : j);
        line.add(grid[r][c]);
      }
      final (slid, g) = _slideRow(line);
      gained += g;
      for (var j = 0; j < n; j++) {
        final r = dr == 0 ? i : (dr > 0 ? n - 1 - j : j);
        final c = dc == 0 ? i : (dc > 0 ? n - 1 - j : j);
        if (next[r][c] != slid[j]) moved = true;
        next[r][c] = slid[j];
      }
    }

    if (!moved) return;
    if (gained > 0) {
      Audio.instance.pop(gained >= 128 ? 3 : gained >= 16 ? 2 : 1);
    } else {
      Audio.instance.swap();
    }
    setState(() {
      grid = next;
      score += gained;
      _spawn();
      gameOver = !_canMove();
      if (gameOver) Audio.instance.lose();
    });
  }

  bool _canMove() {
    for (var r = 0; r < n; r++) {
      for (var c = 0; c < n; c++) {
        if (grid[r][c] == 0) return true;
        if (r + 1 < n && grid[r][c] == grid[r + 1][c]) return true;
        if (c + 1 < n && grid[r][c] == grid[r][c + 1]) return true;
      }
    }
    return false;
  }

  String _assetFor(int v) => 'assets/images/merge_${min(v, 2048)}.png';

  @override
  Widget build(BuildContext context) {
    return GameScaffold(
      title: 'Merge',
      score: score,
      onReset: () => setState(_reset),
      gameOver: gameOver,
      gameOverText: 'No moves left',
      child: GestureDetector(
        onPanEnd: (d) {
          final v = d.velocity.pixelsPerSecond;
          if (v.distance < 100) return;
          if (v.dx.abs() > v.dy.abs()) {
            _move(0, v.dx > 0 ? 1 : -1);
          } else {
            _move(v.dy > 0 ? 1 : -1, 0);
          }
        },
        child: AspectRatio(
          aspectRatio: 1,
          child: GlassBoard(
            child: Column(
              children: [
                for (var r = 0; r < n; r++)
                  Expanded(
                    child: Row(
                      children: [
                        for (var c = 0; c < n; c++)
                          Expanded(
                            child: Padding(
                              padding: const EdgeInsets.all(4),
                              child: grid[r][c] == 0
                                  ? Container(
                                      decoration: AppTheme.glass(
                                          radius: 12, fill: const Color(0x08FFFFFF)),
                                    )
                                  : AnimatedSwitcher(
                                      duration: const Duration(milliseconds: 120),
                                      transitionBuilder: (child, anim) =>
                                          ScaleTransition(scale: anim, child: child),
                                      child: Image.asset(
                                        _assetFor(grid[r][c]),
                                        key: ValueKey(grid[r][c]),
                                        fit: BoxFit.contain,
                                      ),
                                    ),
                            ),
                          ),
                      ],
                    ),
                  ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
