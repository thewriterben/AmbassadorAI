import 'dart:math';

import 'board.dart';
import 'gem.dart';
import 'levels.dart';

enum SessionState { playing, won, lost }

/// A single play-through of a level: board + moves + goal progress.
class LevelSession {
  final Level level;
  final Board board;
  int movesLeft;
  int score = 0;
  int collected = 0;
  int vaultsBroken = 0;
  int ingotsDelivered = 0;
  SessionState state = SessionState.playing;

  LevelSession(this.level, {int? seedOverride})
      : board = Board(
          rows: level.rows,
          cols: level.cols,
          kinds: level.kinds,
          sealCount: level.sealCount,
          sealLayers: level.sealLayers,
          vaultCount: level.vaultCount,
          vaultArmorLevel: level.vaultArmor,
          ingotCount: level.ingotCount,
          rng: Random(seedOverride ?? (level.seed ^ DateTime.now().millisecondsSinceEpoch)),
        ),
        movesLeft = level.moves {
    // Counted after generation: placement can collide, so the level's requested
    // counts are an upper bound, not a promise.
    _sealsAtStart = board.sealsLeft;
    _vaultsAtStart = board.vaultsLeft;
    _ingotsAtStart = board.ingotsOnBoard;
  }

  int _sealsAtStart = 0;
  int _vaultsAtStart = 0;
  int _ingotsAtStart = 0;
  int get sealsTotal => _sealsAtStart;
  int get vaultsTotal => _vaultsAtStart;
  int get ingotsTotal => _ingotsAtStart;
  int get sealsLeft => board.sealsLeft;
  int get vaultsLeft => board.vaultsLeft;

  bool get goalMet => switch (level.goal) {
        GoalType.score => score >= level.targetScore,
        GoalType.collect => collected >= level.collectCount,
        GoalType.seals => board.sealsLeft == 0,
        GoalType.vaults => board.vaultsLeft == 0,
        GoalType.ingots => ingotsDelivered >= _ingotsAtStart,
      };

  double get goalProgress => switch (level.goal) {
        GoalType.score => (score / level.targetScore).clamp(0, 1),
        GoalType.collect => (collected / level.collectCount).clamp(0, 1),
        GoalType.seals =>
          _sealsAtStart == 0 ? 1 : ((_sealsAtStart - board.sealsLeft) / _sealsAtStart).clamp(0, 1),
        GoalType.vaults =>
          _vaultsAtStart == 0 ? 1 : ((_vaultsAtStart - board.vaultsLeft) / _vaultsAtStart).clamp(0, 1),
        GoalType.ingots => (ingotsDelivered / max(1, _ingotsAtStart)).clamp(0, 1),
      };

  /// "3/8" style readout for the HUD.
  String get goalCounter => switch (level.goal) {
        GoalType.score => '$score/${level.targetScore}',
        GoalType.collect => '$collected/${level.collectCount}',
        GoalType.seals => '${_sealsAtStart - board.sealsLeft}/$_sealsAtStart',
        GoalType.vaults => '${_vaultsAtStart - board.vaultsLeft}/$_vaultsAtStart',
        GoalType.ingots => '$ingotsDelivered/$_ingotsAtStart',
      };

  int get stars => level.starsFor(score);

  /// Applies a swap. Returns the result (invalid swaps don't cost a move).
  SwapResult swap(Pos a, Pos b) {
    if (state != SessionState.playing) return const SwapResult(false, []);
    final res = board.swap(a, b);
    if (!res.valid) return res;
    movesLeft--;
    for (final st in res.steps) {
      score += st.score;
      if (level.goal == GoalType.collect) {
        collected += st.removed.values.where((g) => g.kind == level.collectKind).length;
      }
      vaultsBroken += st.vaultsBroken.length;
      ingotsDelivered += st.ingotsDelivered.length;
    }
    if (goalMet) {
      state = SessionState.won;
    } else if (movesLeft <= 0) {
      state = SessionState.lost;
    } else if (board.deadlocked) {
      // The board has no legal move and reshuffling could not produce one, so
      // no further swap can ever be valid. Ending the level is the only honest
      // outcome: leaving it playing is a soft lock the player cannot escape
      // except by backing out, losing the run anyway with no explanation.
      state = SessionState.lost;
    }
    return res;
  }
}
