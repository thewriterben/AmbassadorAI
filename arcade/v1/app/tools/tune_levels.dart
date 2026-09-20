// Auto-tunes every level into its intended win-rate band and prints the
// resulting Dart for levels.dart.
//
//   dart run tools/tune_levels.dart > tuned.txt
//
// Two knobs, tried in order:
//   1. the objective count (seals / vaults / ingots / collect / target score)
//   2. the move budget
// Objective count first, because it is what actually makes a level feel
// different; moves are the fine adjustment.

import 'dart:io';

import '../lib/match3/model/levels.dart';
import 'bot.dart';

const searchTrials = 60; // cheap during the search
const verifyTrials = 200; // honest at the end

/// Upper bounds that keep an objective from being hopeless regardless of moves.
/// Derived from the first calibration sweep: seals need a clear on one exact
/// cell so they scale badly, vaults break from any neighbouring clear so they
/// scale well, and each extra ingot needs a whole column worked down.
int _capFor(Level l) => switch (l.goal) {
      GoalType.seals => l.sealLayers >= 2 ? 10 : 18,
      GoalType.vaults => l.vaultArmor > 1 ? 14 : 22,
      GoalType.ingots => 4,
      GoalType.collect => 34,
      GoalType.score => 6000,
    };

int _countOf(Level l) => switch (l.goal) {
      GoalType.seals => l.sealCount,
      GoalType.vaults => l.vaultCount,
      GoalType.ingots => l.ingotCount,
      GoalType.collect => l.collectCount,
      GoalType.score => l.targetScore,
    };

Level _withCount(Level l, int n) => switch (l.goal) {
      GoalType.seals => withKnobs(l, seals: n),
      GoalType.vaults => withKnobs(l, vaults: n),
      GoalType.ingots => withKnobs(l, ingots: n),
      GoalType.collect => withKnobs(l, collect: n),
      GoalType.score => withKnobs(l, target: n),
    };

/// Non-goal furniture still makes a board harder; trim it when a level is
/// stubbornly too hard even at the count and move limits.
Level _trimFurniture(Level l) => withKnobs(
      l,
      seals: l.goal == GoalType.seals ? null : (l.sealCount * 0.7).round(),
      vaults: l.goal == GoalType.vaults ? null : (l.vaultCount * 0.7).round(),
      ingots: l.goal == GoalType.ingots ? null : (l.ingotCount > 1 ? l.ingotCount - 1 : l.ingotCount),
    );

Level tune(Level level) {
  final band = bandFor(level.id);
  var best = level;
  var bestRate = winRate(best, searchTrials);

  bool inBand(double r) => r >= band.$1 && r <= band.$2;
  if (inBand(bestRate)) return best;

  // Pass 1: objective count. Clamp to the cap first, then walk toward the band.
  final cap = _capFor(level);
  if (_countOf(best) > cap) {
    best = _withCount(best, cap);
    bestRate = winRate(best, searchTrials);
  }
  for (var step = 0; step < 8 && !inBand(bestRate); step++) {
    final n = _countOf(best);
    final scale = bestRate < band.$1 ? 0.82 : 1.15; // too hard -> fewer; too easy -> more
    var next = (n * scale).round();
    if (next == n) next = bestRate < band.$1 ? n - 1 : n + 1;
    if (level.goal == GoalType.score) next = next.clamp(800, 7000);
    if (next < 1 || next > cap) break;
    final cand = _withCount(best, next);
    final rate = winRate(cand, searchTrials);
    best = cand;
    bestRate = rate;
  }

  // Pass 2: moves.
  for (var step = 0; step < 10 && !inBand(bestRate); step++) {
    final m = best.moves;
    final next = bestRate < band.$1 ? m + 2 : m - 1;
    if (next < 10 || next > 34) break;
    final cand = withKnobs(best, moves: next);
    final rate = winRate(cand, searchTrials);
    best = cand;
    bestRate = rate;
  }

  // Pass 3: last resort, thin out the decoration.
  if (bestRate < band.$1) {
    final cand = _trimFurniture(best);
    final rate = winRate(cand, searchTrials);
    if (rate > bestRate) {
      best = cand;
      bestRate = rate;
    }
  }
  return best;
}

String _emit(Level l) {
  final extras = <String>[];
  if (l.goal != GoalType.seals && l.sealCount > 0) extras.add('seals: ${l.sealCount}');
  if (l.sealLayers != 1) extras.add('layers: ${l.sealLayers}');
  if (l.goal != GoalType.vaults && l.vaultCount > 0) extras.add('vaults: ${l.vaultCount}');
  if (l.goal != GoalType.ingots && l.ingotCount > 0) extras.add('ingots: ${l.ingotCount}');
  final tail = extras.isEmpty ? '' : ', ${extras.join(', ')}';
  final head = '${l.id}, ${l.rows}, ${l.cols}, ${l.kinds}, ${l.moves}';
  return switch (l.goal) {
    GoalType.score => '  _score($head, ${l.targetScore}$tail),',
    GoalType.collect =>
      '  _collect($head, ${l.targetScore}, GemKind.${l.collectKind!.name}, ${l.collectCount}$tail),',
    GoalType.seals => '  _seals($head, ${l.targetScore}, ${l.sealCount}$tail),',
    GoalType.vaults => '  _vaults($head, ${l.targetScore}, ${l.vaultCount}$tail),',
    GoalType.ingots => '  _ingots($head, ${l.targetScore}, ${l.ingotCount}$tail),',
  };
}

void main() {
  final out = <String>[];
  var outside = 0;
  for (final level in levels) {
    final tuned = tune(level);
    final rate = winRate(tuned, verifyTrials);
    final band = bandFor(tuned.id);
    final ok = rate >= band.$1 && rate <= band.$2;
    if (!ok) outside++;
    stderr.writeln('${tuned.id.toString().padLeft(3)}  '
        '${tuned.goal.name.padRight(8)} moves ${tuned.moves.toString().padLeft(2)} '
        'count ${_countOf(tuned).toString().padLeft(4)}  '
        '${(rate * 100).toStringAsFixed(0).padLeft(3)}%  ${ok ? 'ok' : 'OUTSIDE'}');
    out.add(_emit(tuned));
  }
  stderr.writeln('\n$outside level(s) still outside the band');
  print(out.join('\n'));
}
