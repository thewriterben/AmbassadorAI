// Plays every level many times with a greedy bot and reports the win rate.
// Pure Dart — run it with the Dart SDK, no Flutter needed:
//
//   dart run tools/calibrate_levels.dart            # full table
//   dart run tools/calibrate_levels.dart 31 400     # one level, 400 trials
//   dart run tools/calibrate_levels.dart --trace 31 # one game, move by move
//
// The bot is deliberately mediocre: it looks one move ahead and takes the
// highest-scoring swap, weighting moves that serve the level's objective. A
// level the bot cannot win is unwinnable in practice; a level it wins 95% of
// the time is not asking anything of the player.

import 'dart:math';

import '../lib/match3/model/board.dart';
import '../lib/match3/model/gem.dart';
import '../lib/match3/model/levels.dart';
import '../lib/match3/model/session.dart';

/// Scores a candidate swap by simulating it on a scratch copy.
class _Move {
  final Pos a, b;
  final double value;
  _Move(this.a, this.b, this.value);
}

/// The bot's view of what a move is worth, given the level's objective.
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
        // Reward downward progress, not just delivery.
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

/// Plays one session to completion. Returns true if won.
bool _play(Level level, int seed, {bool trace = false}) {
  final s = LevelSession(level, seedOverride: seed);
  final rng = Random(seed ^ 0x5eed);
  while (s.state == SessionState.playing) {
    // Enumerate legal swaps, score each on a scratch board.
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
    if (moves.isEmpty) {
      // Board is stuck in a way shuffle did not fix; treat as a loss.
      if (trace) print('  no legal moves left');
      return false;
    }
    moves.sort((x, y) => y.value.compareTo(x.value));
    // Take the best move most of the time, a near-best one otherwise, so the
    // sample reflects a decent-but-human player rather than a solver.
    final pick = (rng.nextDouble() < 0.75 || moves.length == 1) ? moves.first : moves[rng.nextInt(min(3, moves.length))];
    s.swap(pick.a, pick.b);
    if (trace) {
      print('  move ${level.moves - s.movesLeft}/${level.moves}  '
          'goal ${s.goalCounter}  score ${s.score}  '
          'seals ${s.sealsLeft} vaults ${s.vaultsLeft} ingots ${s.board.ingotsOnBoard}');
    }
  }
  return s.state == SessionState.won;
}

/// A structural copy of a board, so candidate moves don't mutate the real one.
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

void main(List<String> args) {
  final trace = args.contains('--trace');
  final rest = args.where((a) => !a.startsWith('--')).toList();
  final only = rest.isNotEmpty ? int.tryParse(rest[0]) : null;
  final trials = rest.length > 1 ? int.parse(rest[1]) : 200;

  if (trace && only != null) {
    final level = levels.firstWhere((l) => l.id == only);
    print('${level.id}  ${level.goalText}  (${level.moves} moves)');
    print('won: ${_play(level, 1, trace: true)}');
    return;
  }

  final target = <String>[];
  print('lvl  world          goal      moves  win%   verdict');
  for (final level in levels) {
    if (only != null && level.id != only) continue;
    var wins = 0;
    for (var t = 0; t < trials; t++) {
      if (_play(level, 1000 + t * 31)) wins++;
    }
    final rate = wins / trials;
    // Intended curve: generous early, demanding late, never impossible.
    final want = switch (level.id) {
      <= 10 => (0.75, 0.95),
      <= 20 => (0.62, 0.88),
      <= 30 => (0.55, 0.82),
      <= 40 => (0.48, 0.78),
      <= 50 => (0.42, 0.72),
      _ => (0.35, 0.68),
    };
    final verdict = rate < want.$1 ? 'TOO HARD' : (rate > want.$2 ? 'too easy' : 'ok');
    if (verdict != 'ok') target.add('${level.id}:${(rate * 100).round()}%:$verdict');
    print('${level.id.toString().padLeft(3)}  '
        '${level.world.name.padRight(14)} '
        '${level.goal.name.padRight(9)} '
        '${level.moves.toString().padLeft(5)}  '
        '${(rate * 100).toStringAsFixed(0).padLeft(4)}%  $verdict');
  }
  print('\n${target.length} level(s) outside the intended band');
  if (target.isNotEmpty) print(target.join('  '));
}
