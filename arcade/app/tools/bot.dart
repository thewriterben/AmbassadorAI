// A greedy Coin Quest player, shared by the calibration and tuning tools.
//
// It looks one move ahead and takes the highest-value swap, weighting moves
// that serve the level's objective. It is deliberately mediocre: a level it
// cannot win is unwinnable in practice, and one it wins nearly every time is
// not asking anything of the player.

import 'dart:math';

import '../lib/match3/model/board.dart';
import '../lib/match3/model/gem.dart';
import '../lib/match3/model/levels.dart';
import '../lib/match3/model/session.dart';

class _Move {
  final Pos a, b;
  final double value;
  _Move(this.a, this.b, this.value);
}

double _valueOf(List<CascadeStep> steps, Level level) {
  var v = 0.0;
  for (final st in steps) {
    v += st.score * 0.02;
    v += st.created.length * 6;
    switch (level.goal) {
      case GoalType.collect:
        v += st.removed.values.where((g) => g.kind == level.collectKind).length * 8;
      case GoalType.seals:
        v += st.sealsCleared.length * 14;
      case GoalType.vaults:
        v += st.vaultsBroken.length * 20;
      case GoalType.ingots:
        v += st.ingotsDelivered.length * 60;
        for (final f in st.falls) {
          if (f.$3.blocker == Blocker.ingot) v += (f.$2.r - f.$1.r) * 6;
        }
      case GoalType.score:
        break;
    }
  }
  return v;
}

Board _clone(Board src, {required int seed}) {
  final b = Board(rows: src.rows, cols: src.cols, kinds: src.kinds, rng: Random(seed));
  for (var r = 0; r < src.rows; r++) {
    for (var c = 0; c < src.cols; c++) {
      b.cells[r][c] = src.cells[r][c];
      b.seals[r][c] = src.seals[r][c];
    }
  }
  return b;
}

/// Plays one session to completion. Returns true if won.
bool playLevel(Level level, int seed, {void Function(LevelSession)? onMove}) {
  final s = LevelSession(level, seedOverride: seed);
  final rng = Random(seed ^ 0x5eed);
  while (s.state == SessionState.playing) {
    final moves = <_Move>[];
    for (var r = 0; r < s.board.rows; r++) {
      for (var c = 0; c < s.board.cols; c++) {
        for (final d in const [Pos(0, 1), Pos(1, 0)]) {
          final a = Pos(r, c), b = Pos(r + d.r, c + d.c);
          if (!s.board.inBounds(b)) continue;
          final ga = s.board.at(a), gb = s.board.at(b);
          if (ga == null || gb == null || !ga.swappable || !gb.swappable) continue;
          final scratch = _clone(s.board, seed: rng.nextInt(1 << 30));
          final res = scratch.swap(a, b);
          if (!res.valid) continue;
          moves.add(_Move(a, b, _valueOf(res.steps, level)));
        }
      }
    }
    if (moves.isEmpty) return false;
    moves.sort((x, y) => y.value.compareTo(x.value));
    // Best move most of the time, a near-best one otherwise, so the sample
    // reflects a decent human rather than a solver.
    final pick = (rng.nextDouble() < 0.75 || moves.length == 1)
        ? moves.first
        : moves[rng.nextInt(min(3, moves.length))];
    s.swap(pick.a, pick.b);
    onMove?.call(s);
  }
  return s.state == SessionState.won;
}

double winRate(Level level, int trials, {int seedBase = 1000}) {
  var wins = 0;
  for (var t = 0; t < trials; t++) {
    if (playLevel(level, seedBase + t * 31)) wins++;
  }
  return wins / trials;
}

/// The intended difficulty curve: generous early, demanding late, never
/// impossible. Returns (min, max) acceptable win rate for a level id.
(double, double) bandFor(int id) => switch (id) {
      <= 5 => (0.88, 1.00), // tutorial: winning is the lesson
      <= 10 => (0.75, 0.95),
      <= 20 => (0.62, 0.88),
      <= 30 => (0.55, 0.82),
      <= 40 => (0.48, 0.78),
      <= 50 => (0.42, 0.72),
      _ => (0.35, 0.68),
    };

/// Rebuilds a level with different knobs.
Level withKnobs(Level l, {int? moves, int? seals, int? vaults, int? ingots, int? target, int? collect}) =>
    Level(
      id: l.id,
      rows: l.rows,
      cols: l.cols,
      kinds: l.kinds,
      moves: moves ?? l.moves,
      goal: l.goal,
      targetScore: target ?? l.targetScore,
      collectKind: l.collectKind,
      collectCount: collect ?? l.collectCount,
      sealCount: seals ?? l.sealCount,
      sealLayers: l.sealLayers,
      vaultCount: vaults ?? l.vaultCount,
      vaultArmor: l.vaultArmor,
      ingotCount: ingots ?? l.ingotCount,
      seed: l.seed,
    );
