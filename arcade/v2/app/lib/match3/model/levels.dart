import 'gem.dart';

enum GoalType {
  /// Reach a score.
  score,

  /// Collect N coins of one kind.
  collect,

  /// Strip every ledger seal on the board.
  seals,

  /// Break every sealed vault.
  vaults,

  /// Work every bullion ingot down to the bottom row.
  ingots,
}

/// The six worlds the level map is grouped into.
class World {
  final String name;
  final String blurb;
  final int firstLevel, lastLevel;
  const World(this.name, this.blurb, this.firstLevel, this.lastLevel);
  bool contains(int levelId) => levelId >= firstLevel && levelId <= lastLevel;
}

const worlds = <World>[
  World('The Mint', 'Where coins are struck. Learn the swap.', 1, 10),
  World('The Ledger', 'Seals to strip, one layer at a time.', 11, 20),
  World('The Vaults', 'Sealed vaults crack open beside a match.', 21, 30),
  World('The Chain', 'Move bullion down the line.', 31, 40),
  World('The Exchange', 'Everything at once, with fewer moves.', 41, 50),
  World('The Network', 'The long haul.', 51, 60),
];

class Level {
  final int id;
  final int rows, cols, kinds, moves;
  final GoalType goal;
  final int targetScore;
  final GemKind? collectKind;
  final int collectCount;

  /// Board furniture. Seals are per-cell layers; vaults and ingots are
  /// obstacles placed at generation.
  final int sealCount, sealLayers, vaultCount, ingotCount;

  /// Hits each vault takes before it breaks.
  final int vaultArmor;

  final int seed;

  const Level({
    required this.id,
    required this.rows,
    required this.cols,
    required this.kinds,
    required this.moves,
    required this.goal,
    required this.targetScore,
    this.collectKind,
    this.collectCount = 0,
    this.sealCount = 0,
    this.sealLayers = 1,
    this.vaultCount = 0,
    this.vaultArmor = 1,
    this.ingotCount = 0,
    required this.seed,
  });

  /// Star thresholds on score: 1★ = target, 2★ = 1.5×, 3★ = 2.2×.
  /// On objective levels the target is the par score, not the win condition.
  int starsFor(int score) {
    if (score >= targetScore * 2.2) return 3;
    if (score >= targetScore * 1.5) return 2;
    if (score >= targetScore) return 1;
    return 0;
  }

  World get world => worlds.firstWhere((w) => w.contains(id), orElse: () => worlds.last);

  /// One line in the goal bar. Kept short on purpose: the bar shares its row
  /// with the counter chip, and "Break all 12 reinforced vaults" was being cut
  /// to "BREAK ALL 12 R…" on a phone.
  String get goalText => switch (goal) {
        GoalType.score => 'Reach $targetScore points',
        GoalType.collect => 'Collect $collectCount ${_kindName(collectKind!)}',
        // sealCount is cells; the counter tracks layers, which is what has to
        // be cleared. On a two-layer level the text said 8 beside a 0/16.
        GoalType.seals => 'Strip ${sealCount * sealLayers} ledger seals',
        GoalType.vaults =>
          vaultArmor > 1 ? 'Break $vaultCount reinforced vaults' : 'Break $vaultCount vaults',
        GoalType.ingots => 'Bring down $ingotCount ${ingotCount == 1 ? 'ingot' : 'ingots'}',
      };

  /// Short form for the HUD chip.
  String get goalShort => switch (goal) {
        // "VALUE" on a rising counter, in an app for a gold-backed asset, sat
        // directly above a disclaimer saying XP has no monetary value.
        GoalType.score => 'SCORE',
        GoalType.collect => 'COLLECT',
        GoalType.seals => 'SEALS',
        GoalType.vaults => 'VAULTS',
        GoalType.ingots => 'INGOTS',
      };

  /// Plain colour names. The gem-stone names these replaced were left over
  /// from the old palette and no longer described what is on the board — a
  /// goal cannot ask for "sapphire coins" when the piece is a flat navy disc.
  static String _kindName(GemKind k) => switch (k) {
        GemKind.gold => 'gold coins',
        GemKind.silver => 'silver coins',
        GemKind.red => 'red coins',
        GemKind.copper => 'copper coins',
        GemKind.blue => 'blue coins',
        GemKind.green => 'green coins',
      };
}

// ---------------------------------------------------------------- the levels
//
// Move counts and targets below were tuned by tools/calibrate_levels.dart,
// which plays each level 400 times with a greedy bot and reports a win rate.
// The intended curve: ~85% in world 1 falling to ~45% by world 6, with no
// level the bot cannot win.

Level _score(int id, int rows, int cols, int kinds, int moves, int target,
        {int seals = 0, int layers = 1, int vaults = 0, int ingots = 0}) =>
    Level(
      id: id, rows: rows, cols: cols, kinds: kinds, moves: moves,
      goal: GoalType.score, targetScore: target,
      sealCount: seals, sealLayers: layers, vaultCount: vaults, ingotCount: ingots,
      seed: 1000 + id * 7919,
    );

Level _collect(int id, int rows, int cols, int kinds, int moves, int par, GemKind kind, int count,
        {int seals = 0, int layers = 1, int vaults = 0, int ingots = 0}) =>
    Level(
      id: id, rows: rows, cols: cols, kinds: kinds, moves: moves,
      goal: GoalType.collect, targetScore: par, collectKind: kind, collectCount: count,
      sealCount: seals, sealLayers: layers, vaultCount: vaults, ingotCount: ingots,
      seed: 1000 + id * 7919,
    );

Level _seals(int id, int rows, int cols, int kinds, int moves, int par, int seals,
        {int layers = 1, int vaults = 0, int ingots = 0}) =>
    Level(
      id: id, rows: rows, cols: cols, kinds: kinds, moves: moves,
      goal: GoalType.seals, targetScore: par,
      sealCount: seals, sealLayers: layers, vaultCount: vaults, ingotCount: ingots,
      seed: 1000 + id * 7919,
    );

Level _vaults(int id, int rows, int cols, int kinds, int moves, int par, int vaults,
        {int seals = 0, int layers = 1, int ingots = 0, int armor = 1}) =>
    Level(
      id: id, rows: rows, cols: cols, kinds: kinds, moves: moves,
      goal: GoalType.vaults, targetScore: par,
      sealCount: seals, sealLayers: layers, vaultCount: vaults, vaultArmor: armor, ingotCount: ingots,
      seed: 1000 + id * 7919,
    );

Level _ingots(int id, int rows, int cols, int kinds, int moves, int par, int ingots,
        {int seals = 0, int layers = 1, int vaults = 0}) =>
    Level(
      id: id, rows: rows, cols: cols, kinds: kinds, moves: moves,
      goal: GoalType.ingots, targetScore: par,
      sealCount: seals, sealLayers: layers, vaultCount: vaults, ingotCount: ingots,
      seed: 1000 + id * 7919,
    );

final levels = <Level>[
  // World 1 - The Mint (1-10)
  _score(1, 7, 7, 5, 20, 1050),
  _score(2, 7, 7, 5, 20, 1500),
  _collect(3, 7, 7, 5, 18, 2000, GemKind.gold, 10),
  _score(4, 8, 8, 5, 20, 2200),
  _collect(5, 8, 8, 5, 18, 2000, GemKind.blue, 16),
  _score(6, 8, 8, 6, 22, 2800),
  _collect(7, 8, 8, 6, 20, 2200, GemKind.red, 19),
  _score(8, 8, 8, 6, 20, 2829),
  _collect(9, 9, 9, 6, 22, 2400, GemKind.gold, 28),
  _score(10, 9, 9, 6, 20, 3239),

  // World 2 - The Ledger (11-20)
  _seals(11, 8, 8, 5, 12, 1800, 18),
  _seals(12, 8, 8, 5, 12, 2000, 18),
  _score(13, 9, 9, 6, 20, 3731, seals: 6),
  _seals(14, 8, 8, 6, 19, 2100, 16),
  _collect(15, 9, 9, 6, 19, 2000, GemKind.green, 26, seals: 10),
  _seals(16, 9, 9, 6, 20, 2300, 20),
  _seals(17, 8, 8, 6, 21, 2200, 8, layers: 2),
  _score(18, 9, 9, 6, 18, 3526, seals: 14),
  _seals(19, 9, 9, 6, 19, 2400, 24),
  _seals(20, 9, 9, 6, 18, 2500, 8, layers: 2),

  // World 3 - The Vaults (21-30)
  _vaults(21, 8, 8, 5, 16, 1900, 14),
  _vaults(22, 8, 8, 6, 19, 2000, 18),
  _score(23, 9, 9, 6, 19, 3608, vaults: 5),
  _vaults(24, 9, 9, 6, 18, 2200, 21),
  _seals(25, 9, 9, 6, 19, 2300, 14, vaults: 4),
  _vaults(26, 9, 9, 6, 18, 2400, 21),
  _collect(27, 9, 9, 6, 18, 2000, GemKind.copper, 24, vaults: 6),
  _vaults(28, 9, 9, 6, 18, 2500, 12, armor: 2),
  _vaults(29, 8, 8, 6, 17, 2400, 18, seals: 10),
  _vaults(30, 9, 9, 6, 18, 2600, 11, armor: 2),

  // World 4 - The Chain (31-40)
  _ingots(31, 8, 8, 5, 22, 1900, 2),
  _ingots(32, 8, 8, 5, 22, 2000, 2),
  _ingots(33, 9, 9, 6, 22, 2200, 1),
  _score(34, 9, 9, 6, 20, 3690, ingots: 2),
  _ingots(35, 9, 9, 6, 21, 2400, 1),
  _ingots(36, 8, 8, 6, 20, 2300, 1, seals: 10),
  _ingots(37, 9, 9, 6, 21, 2500, 1),
  _ingots(38, 9, 9, 6, 23, 2600, 1, vaults: 6),
  _collect(39, 9, 9, 6, 19, 2100, GemKind.silver, 26, ingots: 2),
  _ingots(40, 9, 9, 6, 20, 2800, 1),

  // World 5 - The Exchange (41-50)
  _seals(41, 9, 9, 6, 17, 2600, 18, vaults: 6),
  _vaults(42, 9, 9, 6, 17, 2600, 12, seals: 12, armor: 2),
  _ingots(43, 9, 9, 6, 19, 2700, 1, vaults: 6),
  _score(44, 9, 9, 6, 17, 4800, seals: 16, vaults: 4),
  _seals(45, 9, 9, 6, 17, 2700, 10, layers: 2),
  _ingots(46, 9, 9, 6, 18, 2800, 1, seals: 14),
  _vaults(47, 9, 9, 6, 16, 2700, 9, ingots: 2, armor: 2),
  _collect(48, 9, 9, 6, 16, 2200, GemKind.green, 28, seals: 12, vaults: 4),
  _seals(49, 9, 9, 6, 17, 2900, 26, vaults: 6),
  _ingots(50, 9, 9, 6, 18, 3000, 1, seals: 12, vaults: 4),

  // World 6 - The Network (51-60)
  _vaults(51, 9, 9, 6, 16, 2800, 14, seals: 14, armor: 2),
  _seals(52, 9, 9, 6, 17, 3000, 10, layers: 2, vaults: 4),
  _ingots(53, 9, 9, 6, 18, 3000, 1, vaults: 8),
  _score(54, 9, 9, 6, 16, 4100, seals: 18, vaults: 6, ingots: 2),
  _vaults(55, 9, 9, 6, 16, 2900, 9, ingots: 2, armor: 2),
  _seals(56, 9, 9, 6, 16, 3100, 28, vaults: 6),
  _ingots(57, 9, 9, 6, 21, 3100, 2, seals: 14),
  _vaults(58, 9, 9, 6, 15, 3000, 9, seals: 14, ingots: 2, armor: 2),
  _seals(59, 9, 9, 6, 16, 3200, 10, layers: 2, vaults: 8),
  _ingots(60, 9, 9, 6, 17, 3400, 1, seals: 16, vaults: 8),
];
