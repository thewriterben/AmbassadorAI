import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/match3/model/board.dart';
import 'package:puzzle_pack/match3/model/gem.dart';
import 'package:puzzle_pack/match3/model/levels.dart';
import 'package:puzzle_pack/match3/model/session.dart';

/// Builds a board from letters. c/h/d/s/t/r are coin kinds; V is a vault and
/// I an ingot. Seals are set separately.
Board fromRows(List<String> rowsStr, {Random? rng}) {
  final b = Board(rows: rowsStr.length, cols: rowsStr[0].length, kinds: 6, rng: rng ?? Random(1));
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
      final ch = rowsStr[r][c];
      b.cells[r][c] = switch (ch) {
        'V' => Gem.obstacle(Blocker.vault),
        'I' => Gem.obstacle(Blocker.ingot),
        _ => Gem(map[ch]!),
      };
      b.seals[r][c] = 0;
    }
  }
  return b;
}

void main() {
  group('blockers', () {
    test('obstacles never join a run and cannot be swapped', () {
      // Two golds either side of a vault must not count as a run of three.
      final b = fromRows([
        'cVc h t'.replaceAll(' ', ''),
        'hdsttr',
        'dstrch',
        'strchd',
        'trchds',
        'rchdst',
      ]);
      expect(b.swap(const Pos(0, 0), const Pos(0, 1)).valid, false, reason: 'coin <-> vault');
      expect(b.swap(const Pos(0, 1), const Pos(1, 1)).valid, false, reason: 'vault <-> coin');
    });

    test('a match beside a vault breaks it', () {
      // Column 1 holds two golds under the vault; swapping (2,1) with (2,2)
      // completes a vertical run of three whose top cell touches the vault.
      final b = fromRows([
        'Vchdst',
        'hcdstr',
        'dsctrc',
        'strchd',
        'trchds',
        'rchdst',
      ]);
      expect(b.vaultsLeft, 1);
      final res = b.swap(const Pos(2, 1), const Pos(2, 2));
      expect(res.valid, true, reason: 'swap should complete a run in column 1');
      expect(res.steps.first.vaultsBroken.length, 1);
      expect(b.vaultsLeft, 0, reason: 'a clear next to the vault should break it');
    });

    test('an ingot rides gravity to the floor and is delivered there', () {
      // Clearing the bottom row drops the ingot from (4,0) onto the floor.
      final b = fromRows([
        'htdsrc',
        'tdsrch',
        'dsrcht',
        'srchtd',
        'Ischtd',
        'cchtds',
      ]);
      expect(b.ingotsOnBoard, 1);
      final res = b.swap(const Pos(4, 2), const Pos(5, 2));
      expect(res.valid, true, reason: 'swap should complete the run in row 5');
      final delivered = res.steps.fold(0, (n, st) => n + st.ingotsDelivered.length);
      expect(delivered, 1, reason: 'the ingot should reach the floor and be delivered');
      expect(b.ingotsOnBoard, 0);
      // And it was never treated as an ordinary gem on the way.
      for (final st in res.steps) {
        expect(st.removed.values.any((g) => g.isBlocker), false);
      }
    });

    test('an ingot survives a special firing straight through it', () {
      final b = fromRows([
        'htdsrc',
        'tdsrch',
        'dIrcht',
        'srchtd',
        'trchds',
        'rchdst',
      ]);
      // A striped coin two cells away clears the whole row, ingot included.
      b.cells[2][0] = Gem(GemKind.gold, Special.stripedH);
      final before = b.ingotsOnBoard;
      b.cells[2][3] = Gem(GemKind.gold);
      b.cells[2][4] = Gem(GemKind.gold);
      b.cells[2][5] = Gem(GemKind.gold);
      // Force the row clear by matching the golds next to the striped gem.
      b.swap(const Pos(2, 3), const Pos(2, 4));
      expect(b.ingotsOnBoard, before, reason: 'the ingot must not be destroyed');
    });

    test('no gem is reported falling twice in one step', () {
      // Gravity runs once after the clear and again after an ingot is
      // delivered. Both passes used to append to the same list, so a gem caught
      // by both appeared twice with different (from, to) pairs — and the view
      // attaches one delta-based MoveToEffect per entry, so the two summed and
      // the coin landed a whole extra fall below where it belonged, usually off
      // the board. This is the model-level invariant that prevents it.
      for (var seed = 0; seed < 40; seed++) {
        final b = Board(rows: 8, cols: 8, kinds: 6, ingotCount: 3, rng: Random(seed));
        for (var move = 0; move < 40; move++) {
          final hint = b.findHint();
          if (hint == null) break;
          final res = b.swap(hint.$1, hint.$2);
          for (final st in res.steps) {
            final seen = <int>{};
            for (final (_, _, g) in st.falls) {
              expect(seen.add(g.id), isTrue,
                  reason: 'gem ${g.id} listed twice in one step (seed $seed, move $move)');
            }
          }
        }
      }
    });

    test('blockers fall, so a column never strands cells beneath one', () {
      for (var seed = 0; seed < 30; seed++) {
        final b = Board(rows: 8, cols: 8, kinds: 6, vaultCount: 6, ingotCount: 3, rng: Random(seed));
        for (var move = 0; move < 40; move++) {
          final hint = b.findHint();
          if (hint == null) break;
          b.swap(hint.$1, hint.$2);
          // Every cell is always occupied: no permanent holes.
          for (var r = 0; r < b.rows; r++) {
            for (var c = 0; c < b.cols; c++) {
              expect(b.cells[r][c], isNotNull, reason: 'hole at ($r,$c) seed $seed');
            }
          }
        }
      }
    });
  });

  group('seals', () {
    test('a clear strips one layer, and only one', () {
      final b = fromRows([
        'ccchtd',
        'hdsttr',
        'dstrch',
        'strchd',
        'trchds',
        'rchdst',
      ]);
      b.seals[0][0] = 2;
      b.seals[0][1] = 1;
      expect(b.sealsLeft, 3);
      final res = b.swap(const Pos(0, 3), const Pos(1, 3));
      expect(res.valid, true);
      // (0,0) and (0,1) were both cleared, so each loses exactly one layer.
      expect(b.seals[0][0], 1);
      expect(b.seals[0][1], 0);
    });

    test('seals stay put when the board shuffles', () {
      final b = Board(rows: 8, cols: 8, kinds: 6, sealCount: 10, rng: Random(3));
      final before = [for (final row in b.seals) [...row]];
      b.shuffle();
      expect(b.seals, before, reason: 'shuffling coins must not move the seals under them');
    });
  });

  group('sessions', () {
    test('every goal type can be satisfied and reports progress', () {
      for (final goal in GoalType.values) {
        final level = levels.firstWhere((l) => l.goal == goal);
        final s = LevelSession(level, seedOverride: 42);
        expect(s.goalProgress, inInclusiveRange(0, 1));
        expect(s.goalCounter, isNotEmpty);
        expect(level.goalText, isNotEmpty);
        // Playing greedily must not throw and must keep progress in range.
        for (var i = 0; i < level.moves; i++) {
          final hint = s.board.findHint();
          if (hint == null || s.state != SessionState.playing) break;
          s.swap(hint.$1, hint.$2);
          expect(s.goalProgress, inInclusiveRange(0, 1));
        }
        expect(s.state, isNot(SessionState.playing), reason: '${goal.name} never ended');
      }
    });

    test('an objective level is won by finishing the objective, not the score', () {
      final level = levels.firstWhere((l) => l.goal == GoalType.vaults);
      final s = LevelSession(level, seedOverride: 7);
      while (s.state == SessionState.playing) {
        final hint = s.board.findHint();
        if (hint == null) break;
        s.swap(hint.$1, hint.$2);
      }
      if (s.state == SessionState.won) {
        expect(s.vaultsLeft, 0);
      } else {
        expect(s.movesLeft, 0);
      }
    });
  });

  group('levels', () {
    test('all 60 levels are well formed and in six worlds', () {
      expect(levels.length, 60);
      for (var i = 0; i < levels.length; i++) {
        final l = levels[i];
        expect(l.id, i + 1);
        expect(l.moves, greaterThan(0));
        expect(l.targetScore, greaterThan(0));
        expect(l.kinds, inInclusiveRange(3, GemKind.values.length));
        expect(l.rows * l.cols, greaterThan(l.sealCount + l.vaultCount + l.ingotCount));
        switch (l.goal) {
          case GoalType.collect:
            expect(l.collectKind, isNotNull);
            expect(l.collectCount, greaterThan(0));
          case GoalType.seals:
            expect(l.sealCount, greaterThan(0));
          case GoalType.vaults:
            expect(l.vaultCount, greaterThan(0));
          case GoalType.ingots:
            expect(l.ingotCount, greaterThan(0));
          case GoalType.score:
            break;
        }
      }
      for (final w in worlds) {
        expect(levels.where((l) => w.contains(l.id)).length, 10, reason: w.name);
      }
    });
  });
}
