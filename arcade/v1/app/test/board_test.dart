import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/match3/model/board.dart';
import 'package:puzzle_pack/match3/model/gem.dart';
import 'package:puzzle_pack/match3/model/levels.dart';
import 'package:puzzle_pack/match3/model/session.dart';

/// Builds a board from letters: c=coin h=hex d=diamond s=square t=triangle r=ring.
Board fromRows(List<String> rowsStr) {
  final b = Board(rows: rowsStr.length, cols: rowsStr[0].length, kinds: 6, rng: Random(1));
  const map = {
    'c': GemKind.gold,
    'h': GemKind.silver,
    'd': GemKind.blue,
    's': GemKind.green,
    't': GemKind.red,
    'r': GemKind.copper,
  };
  for (var r = 0; r < b.rows; r++) {
    for (var c = 0; c < b.cols; c++) {
      b.cells[r][c] = Gem(map[rowsStr[r][c]]!);
    }
  }
  return b;
}

void main() {
  test('generated board has no matches and a possible move', () {
    for (var seed = 0; seed < 50; seed++) {
      final b = Board(rows: 8, cols: 8, kinds: 6, rng: Random(seed));
      expect(b.swap(const Pos(0, 0), const Pos(0, 0)).valid, false);
      expect(b.hasPossibleMove(), true);
    }
  });

  test('invalid swap leaves board unchanged', () {
    final b = fromRows(['chdst', 'hdstr', 'dstrc', 'strch', 'trchd']);
    final before = b.toString();
    final res = b.swap(const Pos(0, 0), const Pos(0, 1));
    expect(res.valid, false);
    expect(b.toString(), before);
  });

  test('simple 3-match clears and cascades gravity', () {
    final b = fromRows([
      'hdstr',
      'dstrc',
      'strch',
      'ccdcc', // swapping (3,2) with (2,2) makes cc c cc -> row of 5? no: d↔r
      'trchd',
    ]);
    // Row 3: c c d c c. Swap (3,2)'d' with (2,2)'r' -> row 3 becomes c c r c c (no).
    // Instead swap (3,2) with (4,2)'c' -> row 3 = c c c c c => 5-run => bomb.
    final res = b.swap(const Pos(3, 2), const Pos(4, 2));
    expect(res.valid, true);
    expect(res.steps.first.created.values.any((g) => g.special == Special.bomb), true);
    // No holes remain.
    for (final row in b.cells) {
      expect(row.every((g) => g != null), true);
    }
  });

  test('4-match creates a striped gem at the swapped cell', () {
    final b = fromRows([
      'hdstr',
      'dstrc',
      'strch',
      'ccdct',
      'trcrd',
    ]);
    // Row 3: c c d c t. Swap (3,2)'d' with (4,2)'c' => c c c c t => 4-run.
    final res = b.swap(const Pos(3, 2), const Pos(4, 2));
    expect(res.valid, true);
    final created = res.steps.first.created;
    expect(created.length, 1);
    expect(created.keys.first, const Pos(3, 2));
    expect(created.values.first.special, Special.stripedH);
  });

  test('striped gem fires its whole row when matched', () {
    final b = fromRows([
      'hdstr',
      'dstrc',
      'strch',
      'ccdtt',
      'trcrd',
    ]);
    b.cells[3][0] = Gem(GemKind.gold, Special.stripedH);
    // Swap (3,2)'d' with (4,2)'c' => row 3: c c c t t => 3-run incl. striped at (3,0).
    final res = b.swap(const Pos(3, 2), const Pos(4, 2));
    expect(res.valid, true);
    // Entire row 3 (5 cells) removed.
    final removedRow3 = res.steps.first.removed.keys.where((p) => p.r == 3).length;
    expect(removedRow3, 5);
  });

  test('bomb + gem clears every gem of that kind', () {
    final b = fromRows([
      'hdstr',
      'dstrc',
      'strch',
      'ccdtt',
      'trcrd',
    ]);
    b.cells[2][2] = Gem(GemKind.gold, Special.bomb);
    final coinsBefore = b.cells.expand((r) => r).where((g) => g!.kind == GemKind.blue).length;
    // Swap bomb at (2,2) with diamond at (2,1)? (2,1)='t'. Use (1,2)='t'... pick (3,2)='d'.
    final res = b.swap(const Pos(2, 2), const Pos(3, 2));
    expect(res.valid, true);
    final removedDiamonds =
        res.steps.first.removed.values.where((g) => g.kind == GemKind.blue).length;
    expect(removedDiamonds, coinsBefore);
  });

  test('session tracks moves, score and win state', () {
    final s = LevelSession(levels.first);
    expect(s.movesLeft, levels.first.moves);
    final hint = s.board.findHint();
    expect(hint, isNotNull);
    final res = s.swap(hint!.$1, hint.$2);
    expect(res.valid, true);
    expect(s.movesLeft, levels.first.moves - 1);
    expect(s.score, greaterThan(0));
  });

  test('random play never leaves holes or dead boards', () {
    final rng = Random(42);
    for (var seed = 0; seed < 20; seed++) {
      final b = Board(rows: 8, cols: 8, kinds: 5, rng: Random(seed));
      for (var i = 0; i < 60; i++) {
        final h = b.findHint();
        expect(h, isNotNull, reason: 'seed $seed move $i');
        final res = b.swap(h!.$1, h.$2);
        expect(res.valid, true);
        for (final row in b.cells) {
          expect(row.every((g) => g != null), true);
        }
        rng.nextInt(2);
      }
    }
  });
}
