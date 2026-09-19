import 'dart:async';
import 'dart:math';
import 'dart:ui' as ui;

import 'package:flutter/material.dart';

import '../audio.dart';
import '../theme.dart';
import 'asset_cache.dart';
import 'game_scaffold.dart';

/// Falling-block line-clear game. Tap to rotate, drag to move, swipe down to drop.
class BlocksGame extends StatefulWidget {
  const BlocksGame({super.key});

  @override
  State<BlocksGame> createState() => _BlocksGameState();
}

class _Piece {
  final List<Point<int>> cells;
  final int kind; // index into block_{kind}.png
  const _Piece(this.cells, this.kind);
  _Piece rotated() => _Piece(cells.map((p) => Point(-p.y, p.x)).toList(), kind);
}

class _BlocksGameState extends State<BlocksGame> {
  static const cols = 10;
  static const rows = 18;
  static const kinds = 7;

  static const shapes = <_Piece>[
    _Piece([Point(-1, 0), Point(0, 0), Point(1, 0), Point(2, 0)], 0),
    _Piece([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)], 1),
    _Piece([Point(-1, 0), Point(0, 0), Point(1, 0), Point(0, 1)], 2),
    _Piece([Point(-1, 0), Point(0, 0), Point(1, 0), Point(1, 1)], 3),
    _Piece([Point(-1, 0), Point(0, 0), Point(1, 0), Point(-1, 1)], 4),
    _Piece([Point(-1, 0), Point(0, 0), Point(0, 1), Point(1, 1)], 5),
    _Piece([Point(1, 0), Point(0, 0), Point(0, 1), Point(-1, 1)], 6),
  ];

  late List<List<int?>> board;
  late _Piece piece;
  late Point<int> pos;
  int score = 0;
  int lines = 0;
  bool gameOver = false;
  Timer? timer;
  final rng = Random();
  Map<String, ui.Image>? images;

  @override
  void initState() {
    super.initState();
    AssetCache.load([for (var i = 0; i < kinds; i++) 'assets/images/block_$i.png'])
        .then((m) {
      // The decode outlives the screen if the player leaves during it.
      if (mounted) setState(() => images = m);
    });
    _reset();
  }

  @override
  void dispose() {
    timer?.cancel();
    super.dispose();
  }

  void _reset() {
    board = List.generate(rows, (_) => List.filled(cols, null));
    score = 0;
    lines = 0;
    gameOver = false;
    _spawn();
    _restartTimer();
  }

  void _restartTimer() {
    timer?.cancel();
    final ms = max(120, 600 - lines * 20);
    timer = Timer.periodic(Duration(milliseconds: ms), (_) => _tick());
  }

  void _spawn() {
    piece = shapes[rng.nextInt(shapes.length)];
    pos = const Point(cols ~/ 2, 0);
    if (!_fits(piece, pos)) {
      gameOver = true;
      timer?.cancel();
      Audio.instance.lose();
    }
  }

  bool _fits(_Piece p, Point<int> at) {
    for (final c in p.cells) {
      final x = at.x + c.x, y = at.y + c.y;
      if (x < 0 || x >= cols || y >= rows) return false;
      if (y >= 0 && board[y][x] != null) return false;
    }
    return true;
  }

  void _tick() {
    if (gameOver) return;
    setState(() {
      final next = Point(pos.x, pos.y + 1);
      if (_fits(piece, next)) {
        pos = next;
      } else {
        _lock();
      }
    });
  }

  void _lock() {
    for (final c in piece.cells) {
      final x = pos.x + c.x, y = pos.y + c.y;
      if (y >= 0) board[y][x] = piece.kind;
    }
    var cleared = 0;
    board.removeWhere((row) {
      final full = row.every((c) => c != null);
      if (full) cleared++;
      return full;
    });
    while (board.length < rows) {
      board.insert(0, List.filled(cols, null));
    }
    Audio.instance.land();
    if (cleared > 0) {
      Audio.instance.combo(cleared + 1);
      lines += cleared;
      score += [0, 100, 300, 500, 800][cleared];
      _restartTimer();
    }
    _spawn();
  }

  void _move(int dx) {
    if (gameOver) return;
    final next = Point(pos.x + dx, pos.y);
    if (_fits(piece, next)) setState(() => pos = next);
  }

  void _rotate() {
    if (gameOver) return;
    final r = piece.rotated();
    for (final kick in const [0, -1, 1, -2, 2]) {
      final at = Point(pos.x + kick, pos.y);
      if (_fits(r, at)) {
        Audio.instance.tap();
        setState(() {
          piece = r;
          pos = at;
        });
        return;
      }
    }
  }

  void _hardDrop() {
    if (gameOver) return;
    setState(() {
      while (_fits(piece, Point(pos.x, pos.y + 1))) {
        pos = Point(pos.x, pos.y + 1);
      }
      _lock();
    });
  }

  double _dragAccum = 0;

  @override
  Widget build(BuildContext context) {
    return GameScaffold(
      title: 'Blocks',
      score: score,
      onReset: () => setState(_reset),
      gameOver: gameOver,
      gameOverText: 'Stacked out',
      bottom: Padding(
        padding: const EdgeInsets.only(top: 12),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            _btn(Icons.arrow_left, () => _move(-1)),
            _btn(Icons.rotate_right, _rotate),
            _btn(Icons.arrow_downward, _hardDrop),
            _btn(Icons.arrow_right, () => _move(1)),
          ],
        ),
      ),
      child: GestureDetector(
        onTap: _rotate,
        onHorizontalDragUpdate: (d) {
          _dragAccum += d.delta.dx;
          if (_dragAccum.abs() > 24) {
            _move(_dragAccum > 0 ? 1 : -1);
            _dragAccum = 0;
          }
        },
        onVerticalDragEnd: (d) {
          if (d.velocity.pixelsPerSecond.dy > 300) _hardDrop();
        },
        child: AspectRatio(
          aspectRatio: cols / rows,
          child: Container(
            decoration: AppTheme.glass(
                radius: 16, fill: const Color(0xCC050607), outline: AppTheme.borderStrong),
            clipBehavior: Clip.antiAlias,
            child: CustomPaint(
              painter: _BoardPainter(board, piece, pos, cols, rows, images),
              size: Size.infinite,
            ),
          ),
        ),
      ),
    );
  }

  Widget _btn(IconData icon, VoidCallback onTap) => Material(
        color: Colors.transparent,
        child: InkWell(
          borderRadius: BorderRadius.circular(999),
          onTap: onTap,
          child: Container(
            width: 60,
            height: 60,
            decoration: AppTheme.glass(radius: 999, outline: AppTheme.borderStrong),
            child: Icon(icon, color: AppTheme.text, size: 28),
          ),
        ),
      );
}

class _BoardPainter extends CustomPainter {
  final List<List<int?>> board;
  final _Piece piece;
  final Point<int> pos;
  final int cols, rows;
  final Map<String, ui.Image>? images;
  _BoardPainter(this.board, this.piece, this.pos, this.cols, this.rows, this.images);

  @override
  void paint(Canvas canvas, Size size) {
    final cw = size.width / cols, ch = size.height / rows;
    final gridPaint = Paint()
      ..color = const Color(0x0AFFFFFF)
      ..strokeWidth = 1;
    for (var x = 1; x < cols; x++) {
      canvas.drawLine(Offset(x * cw, 0), Offset(x * cw, size.height), gridPaint);
    }
    for (var y = 1; y < rows; y++) {
      canvas.drawLine(Offset(0, y * ch), Offset(size.width, y * ch), gridPaint);
    }

    final paint = Paint();
    void cell(int x, int y, int kind) {
      final r = Rect.fromLTWH(x * cw + 1, y * ch + 1, cw - 2, ch - 2);
      final img = images?['assets/images/block_$kind.png'];
      if (img != null) {
        canvas.drawImageRect(
            img, Rect.fromLTWH(0, 0, img.width.toDouble(), img.height.toDouble()), r, paint);
      } else {
        paint.color = AppTheme.tileColors[kind % AppTheme.tileColors.length];
        canvas.drawRRect(RRect.fromRectAndRadius(r, const Radius.circular(3)), paint);
      }
    }

    for (var y = 0; y < rows; y++) {
      for (var x = 0; x < cols; x++) {
        final k = board[y][x];
        if (k != null) cell(x, y, k);
      }
    }
    // Ghost (landing preview)
    var gy = pos.y;
    bool fits(int yy) {
      for (final c in piece.cells) {
        final x = pos.x + c.x, y = yy + c.y;
        if (x < 0 || x >= cols || y >= rows) return false;
        if (y >= 0 && board[y][x] != null) return false;
      }
      return true;
    }
    while (fits(gy + 1)) {
      gy++;
    }
    final ghost = Paint()
      ..color = const Color(0x33EA952D)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.5;
    for (final c in piece.cells) {
      final x = pos.x + c.x, y = gy + c.y;
      if (y >= 0) {
        canvas.drawRRect(
            RRect.fromRectAndRadius(
                Rect.fromLTWH(x * cw + 2, y * ch + 2, cw - 4, ch - 4), const Radius.circular(3)),
            ghost);
      }
    }
    for (final c in piece.cells) {
      final x = pos.x + c.x, y = pos.y + c.y;
      if (y >= 0) cell(x, y, piece.kind);
    }
  }

  @override
  bool shouldRepaint(covariant _BoardPainter old) => true;
}
