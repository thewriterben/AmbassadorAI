// Core value types for the Match-3 board. Pure Dart, no Flutter imports.

enum GemKind { gold, silver, copper, red, blue, green }

enum Special {
  none,
  stripedH, // clears its row
  stripedV, // clears its column
  wrapped, // clears 3x3
  bomb, // clears every gem of one kind
}

/// Obstacles that occupy a cell instead of a playable coin.
///
/// Both fall with gravity. That is deliberate: a blocker that never moves can
/// strand the cells beneath it in its column, because refill only spawns from
/// the top — the column would drain and never recover. Falling blockers settle
/// at the bottom and the space above them always refills.
enum Blocker {
  /// Sealed vault. Unmatchable; broken by a clear in an adjacent cell or by a
  /// special firing through it. The "break the vaults" goal counts these.
  vault,

  /// Bullion ingot. Unmatchable and indestructible; the player works it down
  /// to the bottom row, where it is delivered. The "bring down" goal counts these.
  ingot,
}

class Pos {
  final int r, c;
  const Pos(this.r, this.c);

  Pos operator +(Pos o) => Pos(r + o.r, c + o.c);
  bool adjacent(Pos o) => (r - o.r).abs() + (c - o.c).abs() == 1;

  /// The four orthogonal neighbours.
  Iterable<Pos> get neighbours sync* {
    yield Pos(r - 1, c);
    yield Pos(r + 1, c);
    yield Pos(r, c - 1);
    yield Pos(r, c + 1);
  }

  @override
  bool operator ==(Object other) => other is Pos && other.r == r && other.c == c;
  @override
  int get hashCode => r * 1000 + c;
  @override
  String toString() => '($r,$c)';
}

class Gem {
  static int _nextId = 0;
  final int id;
  final GemKind kind;
  final Special special;

  /// Non-null when this cell holds an obstacle rather than a playable coin.
  final Blocker? blocker;

  Gem(this.kind, [this.special = Special.none])
      : id = _nextId++,
        blocker = null;
  Gem._(this.id, this.kind, this.special, this.blocker);

  /// An obstacle. It carries a [kind] only so the renderer has a tint to use;
  /// nothing ever matches against it.
  Gem.obstacle(Blocker b, [GemKind tint = GemKind.gold])
      : id = _nextId++,
        kind = tint,
        special = Special.none,
        blocker = b;

  Gem withSpecial(Special s) => Gem._(id, kind, s, blocker);

  bool get isSpecial => special != Special.none;
  bool get isBlocker => blocker != null;

  /// Playable coins take part in runs; obstacles never do.
  bool get matchable => blocker == null;

  /// Swapping is only ever between two playable coins.
  bool get swappable => blocker == null;

  @override
  String toString() => blocker != null
      ? '${blocker!.name}#$id'
      : '${kind.name}${isSpecial ? '/${special.name}' : ''}#$id';
}
