import 'dart:math';

import 'gem.dart';

/// One animation-friendly step of a cascade.
class CascadeStep {
  /// Positions whose gems were removed (already null on the board).
  final Set<Pos> cleared;

  /// Gems removed, keyed by position — for goal counting and pop effects.
  final Map<Pos, Gem> removed;

  /// Specials created this step (placed on the board at [Pos]).
  final Map<Pos, Gem> created;

  /// Existing gems that fell: (from, to, gem).
  final List<(Pos, Pos, Gem)> falls;

  /// New gems spawned at the top: position -> gem. spawnRow is the negative
  /// row index they "fall from" so the view can animate them in.
  final Map<Pos, Gem> spawns;

  /// Cells whose seal lost a layer this step, with the layers now remaining.
  final Map<Pos, int> sealsCleared;

  /// Vaults broken this step.
  final Map<Pos, Gem> vaultsBroken;

  /// Vaults that took a hit but held, with the armour now remaining.
  final Map<Pos, int> vaultsDamaged;

  /// Ingots that reached the bottom row and were delivered.
  final Map<Pos, Gem> ingotsDelivered;

  /// Points earned this step.
  final int score;

  /// Cascade depth: 1 for the swap match, 2+ for chain reactions.
  final int combo;

  CascadeStep({
    required this.cleared,
    required this.removed,
    required this.created,
    required this.falls,
    required this.spawns,
    required this.sealsCleared,
    required this.vaultsBroken,
    required this.vaultsDamaged,
    required this.ingotsDelivered,
    required this.score,
    required this.combo,
  });
}

class SwapResult {
  final bool valid;
  final List<CascadeStep> steps;
  const SwapResult(this.valid, this.steps);
  int get score => steps.fold(0, (s, st) => s + st.score);
}

class Board {
  final int rows, cols;
  final int kinds;
  final Random rng;
  late List<List<Gem?>> cells;

  /// Ledger seals: layers of seal remaining under each cell. A clear on the
  /// cell strips one layer. Nothing else touches them.
  late List<List<int>> seals;

  /// Set when the board ran out of moves and reshuffled itself, so the view
  /// can say so instead of the coins silently rearranging.
  bool shuffledLastMove = false;

  /// Hits a vault still needs, keyed by gem id (so it survives falling).
  ///
  /// Without this, vaults break to any neighbouring clear and difficulty can
  /// only be scaled by piling more of them on: bot testing pinned four
  /// different levels to an identical "21 vaults" because the count had
  /// saturated. Armour makes eight reinforced vaults a real level.
  final Map<int, int> vaultArmor = {};

  Board({
    required this.rows,
    required this.cols,
    required this.kinds,
    int sealCount = 0,
    int sealLayers = 1,
    int vaultCount = 0,
    int vaultArmorLevel = 1,
    int ingotCount = 0,
    Random? rng,
  }) : rng = rng ?? Random() {
    assert(kinds >= 3 && kinds <= GemKind.values.length);
    _generate();
    _placeSeals(sealCount, sealLayers);
    _placeBlockers(vaultCount, ingotCount, vaultArmorLevel);
    if (!hasPossibleMove()) shuffle();
  }

  Gem? at(Pos p) => cells[p.r][p.c];
  bool inBounds(Pos p) => p.r >= 0 && p.r < rows && p.c >= 0 && p.c < cols;
  int sealAt(Pos p) => seals[p.r][p.c];

  int get sealsLeft {
    var n = 0;
    for (final row in seals) {
      for (final s in row) {
        n += s;
      }
    }
    return n;
  }

  int get vaultsLeft => _countBlockers(Blocker.vault);
  int get ingotsOnBoard => _countBlockers(Blocker.ingot);

  int _countBlockers(Blocker b) {
    var n = 0;
    for (final row in cells) {
      for (final g in row) {
        if (g?.blocker == b) n++;
      }
    }
    return n;
  }

  GemKind _randomKind() => GemKind.values[rng.nextInt(kinds)];

  void _generate() {
    cells = List.generate(rows, (_) => List.filled(cols, null));
    seals = List.generate(rows, (_) => List.filled(cols, 0));
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        GemKind k;
        var guard = 0;
        do {
          k = _randomKind();
        } while (_wouldMatch(r, c, k) && ++guard < 50);
        cells[r][c] = Gem(k);
      }
    }
  }

  /// Seals go down as a centred contiguous band, not scattered.
  ///
  /// Scattered seals need a clear on one exact cell each, which is punishing
  /// out of proportion to how it looks — bot testing put a 28-seal board at a
  /// 7% win rate. A block is reachable by ordinary cascades and reads as a
  /// region of the board to work through.
  void _placeSeals(int count, int layers) {
    if (count <= 0 || layers <= 0) return;
    final total = min(count, rows * cols);
    final bandRows = (total / cols).ceil();
    final startRow = max(0, (rows - bandRows) ~/ 2);
    var placed = 0;
    for (var r = startRow; r < rows && placed < total; r++) {
      final remaining = total - placed;
      if (remaining >= cols) {
        for (var c = 0; c < cols; c++) {
          seals[r][c] = layers;
        }
        placed += cols;
      } else {
        // Centre the short last row.
        final off = (cols - remaining) ~/ 2;
        for (var c = off; c < off + remaining; c++) {
          seals[r][c] = layers;
        }
        placed += remaining;
      }
    }
  }

  /// Vaults go anywhere in the upper two-thirds; ingots start in the top rows
  /// so the player has to work them down. Neither can sit on the bottom row at
  /// generation — an ingot there would deliver itself for free.
  void _placeBlockers(int vaultCount, int ingotCount, int armor) {
    if (vaultCount <= 0 && ingotCount <= 0) return;
    final taken = <Pos>{};
    Pos? pick(int minRow, int maxRow) {
      final lo = minRow.clamp(0, rows - 1);
      final hi = maxRow.clamp(lo + 1, rows);
      for (var attempt = 0; attempt < 200; attempt++) {
        final p = Pos(lo + rng.nextInt(hi - lo), rng.nextInt(cols));
        if (taken.contains(p)) continue;
        taken.add(p);
        return p;
      }
      return null;
    }

    // Ingots start in the middle band, not the top.
    //
    // An ingot has to be worked down its whole column, and the player cannot
    // aim cascades at one column reliably. Starting them at the top made every
    // ingot level collapse to a single ingot under tuning — twelve levels with
    // identical settings. From mid-board, three is a real objective.
    for (var i = 0; i < ingotCount; i++) {
      final p = pick(rows ~/ 3, (rows * 2) ~/ 3);
      if (p != null) cells[p.r][p.c] = Gem.obstacle(Blocker.ingot);
    }
    for (var i = 0; i < vaultCount; i++) {
      final p = pick(0, (rows * 2) ~/ 3);
      if (p != null) {
        final g = Gem.obstacle(Blocker.vault, GemKind.silver);
        cells[p.r][p.c] = g;
        vaultArmor[g.id] = max(1, armor);
      }
    }
  }

  bool _wouldMatch(int r, int c, GemKind k) {
    if (c >= 2 && _kindAt(r, c - 1) == k && _kindAt(r, c - 2) == k) return true;
    if (r >= 2 && _kindAt(r - 1, c) == k && _kindAt(r - 2, c) == k) return true;
    return false;
  }

  /// The kind a cell contributes to a run, or null if it cannot be in one.
  GemKind? _kindAt(int r, int c) {
    final g = cells[r][c];
    return (g != null && g.matchable) ? g.kind : null;
  }

  /// Reshuffles playable kinds (keeps specials, blockers and seals in place)
  /// until a move exists and no matches are pending.
  void shuffle() {
    final movable = <Gem>[];
    final slots = <Pos>[];
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        final g = cells[r][c];
        if (g != null && g.matchable) {
          movable.add(g);
          slots.add(Pos(r, c));
        }
      }
    }
    if (movable.length < 3) {
      deadlocked = true;
      return;
    }
    for (var attempt = 0; attempt < 100; attempt++) {
      movable.shuffle(rng);
      for (var i = 0; i < slots.length; i++) {
        cells[slots[i].r][slots[i].c] = movable[i];
      }
      if (_findRuns().isEmpty && hasPossibleMove()) {
        deadlocked = false;
        return;
      }
    }
    // Both exits above used to fall through silently, leaving whatever the last
    // attempt produced. If that arrangement has no legal move, every swap is
    // rejected, movesLeft never decrements, and the level can neither be won
    // nor lost — a soft lock with only the back button. Vanishingly unlikely on
    // a 9x9, but there was no handling at all, so say so and let the session
    // end the level rather than sit there.
    deadlocked = !hasPossibleMove();
  }

  /// True when the board has no legal move and shuffling could not find one.
  bool deadlocked = false;

  // ---------------------------------------------------------------- moves

  bool hasPossibleMove() {
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        final p = Pos(r, c);
        final g = at(p);
        if (g == null || !g.swappable) continue;
        if (g.special == Special.bomb) return true;
        for (final d in const [Pos(0, 1), Pos(1, 0)]) {
          final q = p + d;
          if (!inBounds(q)) continue;
          final h = at(q);
          if (h == null || !h.swappable) continue;
          if (h.isSpecial && g.isSpecial) return true;
          _swapCells(p, q);
          final ok = _findRuns().isNotEmpty;
          _swapCells(p, q);
          if (ok) return true;
        }
      }
    }
    return false;
  }

  /// Finds a valid move for hints, or null.
  (Pos, Pos)? findHint() {
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        final p = Pos(r, c);
        final g = at(p);
        if (g == null || !g.swappable) continue;
        for (final d in const [Pos(0, 1), Pos(1, 0)]) {
          final q = p + d;
          if (!inBounds(q)) continue;
          final h = at(q);
          if (h == null || !h.swappable) continue;
          _swapCells(p, q);
          final ok = _findRuns().isNotEmpty;
          _swapCells(p, q);
          if (ok) return (p, q);
        }
      }
    }
    return null;
  }

  void _swapCells(Pos a, Pos b) {
    final t = cells[a.r][a.c];
    cells[a.r][a.c] = cells[b.r][b.c];
    cells[b.r][b.c] = t;
  }

  /// Attempts to swap [a] and [b]. On success the board is mutated through the
  /// full cascade and the steps are returned for animation. On failure the
  /// board is unchanged and `valid` is false.
  SwapResult swap(Pos a, Pos b) {
    if (!inBounds(a) || !inBounds(b) || !a.adjacent(b)) return const SwapResult(false, []);
    final ga = at(a), gb = at(b);
    if (ga == null || gb == null) return const SwapResult(false, []);
    // Obstacles are scenery: they never move by hand.
    if (!ga.swappable || !gb.swappable) return const SwapResult(false, []);

    shuffledLastMove = false;
    _swapCells(a, b);

    // Special-special / bomb combos resolve without needing a run.
    final combo = _comboClear(a, b);
    final runs = combo == null ? _findRuns() : null;
    if (combo == null && runs!.isEmpty) {
      _swapCells(a, b);
      return const SwapResult(false, []);
    }

    final steps = <CascadeStep>[];
    var depth = 1;
    Set<Pos>? forced = combo;
    List<Pos> swapPos = [a, b];
    while (true) {
      final step = _resolveStep(depth, forced: forced, swapPos: swapPos);
      if (step == null) break;
      steps.add(step);
      forced = null;
      swapPos = const [];
      depth++;
      if (depth > 40) break; // safety
    }
    if (!hasPossibleMove()) {
      shuffle();
      shuffledLastMove = true;
    }
    return SwapResult(true, steps);
  }

  /// Handles swaps involving bombs or two specials. Returns the set to clear.
  Set<Pos>? _comboClear(Pos a, Pos b) {
    final ga = at(a)!, gb = at(b)!; // already swapped: ga now sits at a
    final out = <Pos>{};
    if (ga.special == Special.bomb && gb.special == Special.bomb) {
      for (var r = 0; r < rows; r++) {
        for (var c = 0; c < cols; c++) {
          out.add(Pos(r, c));
        }
      }
      return out;
    }
    if (ga.special == Special.bomb || gb.special == Special.bomb) {
      final bombPos = ga.special == Special.bomb ? a : b;
      final other = ga.special == Special.bomb ? gb : ga;
      out.add(bombPos);
      // Consume the bomb itself so it doesn't also fire its "cleared" effect.
      cells[bombPos.r][bombPos.c] = at(bombPos)!.withSpecial(Special.none);
      for (var r = 0; r < rows; r++) {
        for (var c = 0; c < cols; c++) {
          final g = cells[r][c];
          if (g != null && g.matchable && g.kind == other.kind) {
            out.add(Pos(r, c));
            // bomb + striped: every gem of that kind becomes striped and fires.
            if (other.special == Special.stripedH || other.special == Special.stripedV) {
              cells[r][c] = g.withSpecial(rng.nextBool() ? Special.stripedH : Special.stripedV);
            } else if (other.special == Special.wrapped) {
              cells[r][c] = g.withSpecial(Special.wrapped);
            }
          }
        }
      }
      return out;
    }
    if (ga.isSpecial && gb.isSpecial) {
      final s = {ga.special, gb.special};
      final center = a;
      if (s.contains(Special.wrapped) && s.length == 1) {
        // wrapped + wrapped: 5x5
        for (var dr = -2; dr <= 2; dr++) {
          for (var dc = -2; dc <= 2; dc++) {
            final p = center + Pos(dr, dc);
            if (inBounds(p)) out.add(p);
          }
        }
      } else if (s.contains(Special.wrapped)) {
        // wrapped + striped: 3 rows + 3 cols
        for (var d = -1; d <= 1; d++) {
          for (var c = 0; c < cols; c++) {
            final p = Pos(center.r + d, c);
            if (inBounds(p)) out.add(p);
          }
          for (var r = 0; r < rows; r++) {
            final p = Pos(r, center.c + d);
            if (inBounds(p)) out.add(p);
          }
        }
      } else {
        // striped + striped: row + col
        for (var c = 0; c < cols; c++) {
          out.add(Pos(center.r, c));
        }
        for (var r = 0; r < rows; r++) {
          out.add(Pos(r, center.c));
        }
      }
      // Consume the two specials so they don't re-trigger expansion oddly.
      cells[a.r][a.c] = ga.withSpecial(Special.none);
      cells[b.r][b.c] = gb.withSpecial(Special.none);
      return out;
    }
    return null;
  }

  // ---------------------------------------------------------------- runs

  /// A straight run of 3+ same-kind playable gems.
  List<List<Pos>> _findRuns() {
    final runs = <List<Pos>>[];
    for (var r = 0; r < rows; r++) {
      var c = 0;
      while (c < cols) {
        final k = _kindAt(r, c);
        var e = c;
        while (k != null && e < cols && _kindAt(r, e) == k) {
          e++;
        }
        if (k != null && e - c >= 3) runs.add([for (var i = c; i < e; i++) Pos(r, i)]);
        c = k == null ? c + 1 : e;
      }
    }
    for (var c = 0; c < cols; c++) {
      var r = 0;
      while (r < rows) {
        final k = _kindAt(r, c);
        var e = r;
        while (k != null && e < rows && _kindAt(e, c) == k) {
          e++;
        }
        if (k != null && e - r >= 3) runs.add([for (var i = r; i < e; i++) Pos(i, c)]);
        r = k == null ? r + 1 : e;
      }
    }
    return runs;
  }

  /// Resolves one cascade step: clear runs (+ forced), fire specials, create
  /// specials, strip seals, break vaults, apply gravity, deliver ingots, spawn.
  /// Returns null when nothing matched.
  CascadeStep? _resolveStep(int depth, {Set<Pos>? forced, List<Pos> swapPos = const []}) {
    final runs = _findRuns();
    if (runs.isEmpty && (forced == null || forced.isEmpty)) return null;

    final cleared = <Pos>{...?forced};
    final created = <Pos, Gem>{};

    // Group runs into match shapes and decide specials.
    final horizontal = runs.where((r) => r.first.r == r.last.r).toList();
    final vertical = runs.where((r) => r.first.c == r.last.c).toList();
    final usedForSpecial = <Pos>{};

    Pos pickAnchor(List<Pos> run) {
      for (final s in swapPos) {
        if (run.contains(s)) return s;
      }
      return run[run.length ~/ 2];
    }

    // Intersections -> wrapped
    for (final h in horizontal) {
      for (final v in vertical) {
        final x = h.where(v.contains).toList();
        if (x.isNotEmpty && h.first.r == x.first.r) {
          final p = x.first;
          if (!usedForSpecial.contains(p)) {
            final g = at(p)!;
            created[p] = g.withSpecial(Special.wrapped);
            usedForSpecial.add(p);
          }
        }
      }
    }
    for (final run in runs) {
      cleared.addAll(run);
      if (run.length >= 5) {
        final p = pickAnchor(run);
        if (!created.containsKey(p)) {
          created[p] = at(p)!.withSpecial(Special.bomb);
          usedForSpecial.add(p);
        }
      } else if (run.length == 4) {
        final p = pickAnchor(run);
        if (!created.containsKey(p)) {
          final horizontalRun = run.first.r == run.last.r;
          created[p] = at(p)!.withSpecial(horizontalRun ? Special.stripedH : Special.stripedV);
          usedForSpecial.add(p);
        }
      }
    }

    // Fire any specials caught in the clear, iterating to a fixed point.
    final fired = <Pos>{};
    var changed = true;
    while (changed) {
      changed = false;
      for (final p in cleared.toList()) {
        if (fired.contains(p) || created.containsKey(p)) continue;
        final g = at(p);
        if (g == null || !g.isSpecial) continue;
        fired.add(p);
        final before = cleared.length;
        switch (g.special) {
          case Special.stripedH:
            for (var c = 0; c < cols; c++) {
              cleared.add(Pos(p.r, c));
            }
          case Special.stripedV:
            for (var r = 0; r < rows; r++) {
              cleared.add(Pos(r, p.c));
            }
          case Special.wrapped:
            for (var dr = -1; dr <= 1; dr++) {
              for (var dc = -1; dc <= 1; dc++) {
                final q = p + Pos(dr, dc);
                if (inBounds(q)) cleared.add(q);
              }
            }
          case Special.bomb:
            // Bomb cleared by a neighbouring match: takes out the most common kind.
            final counts = <GemKind, int>{};
            for (final row in cells) {
              for (final gg in row) {
                if (gg != null && gg.matchable) counts[gg.kind] = (counts[gg.kind] ?? 0) + 1;
              }
            }
            if (counts.isNotEmpty) {
              final top = counts.entries.reduce((a, b) => a.value >= b.value ? a : b).key;
              for (var r = 0; r < rows; r++) {
                for (var c = 0; c < cols; c++) {
                  final gg = cells[r][c];
                  if (gg != null && gg.matchable && gg.kind == top) cleared.add(Pos(r, c));
                }
              }
            }
          case Special.none:
            break;
        }
        if (cleared.length != before) changed = true;
      }
    }

    // A clear next to a vault cracks it open, and a special firing through one
    // hits it directly. Ingots shrug both off — they only leave at the bottom.
    // Gather every vault taking a hit this step; each vault takes at most one
    // per step however many neighbouring cells cleared.
    final vaultHits = <Pos, Gem>{};
    for (final p in cleared.toList()) {
      final g = at(p);
      if (g?.blocker == Blocker.vault) {
        vaultHits[p] = g!;
        continue;
      }
      if (g == null || g.isBlocker) continue;
      for (final n in p.neighbours) {
        if (!inBounds(n)) continue;
        final h = at(n);
        if (h?.blocker == Blocker.vault) vaultHits[n] = h!;
      }
    }
    final vaultsBroken = <Pos, Gem>{};
    final vaultsDamaged = <Pos, int>{};
    for (final e in vaultHits.entries) {
      final left = (vaultArmor[e.value.id] ?? 1) - 1;
      if (left <= 0) {
        vaultArmor.remove(e.value.id);
        vaultsBroken[e.key] = e.value;
      } else {
        vaultArmor[e.value.id] = left;
        vaultsDamaged[e.key] = left;
      }
    }
    // Obstacles are never "removed as gems": drop them from the clear set and
    // handle them explicitly, so an indestructible ingot is never deleted.
    cleared.removeWhere((p) => at(p)?.isBlocker ?? false);
    for (final p in vaultsBroken.keys) {
      cells[p.r][p.c] = null;
    }

    // Seals sit under the cell; any clear on top strips one layer.
    final sealsCleared = <Pos, int>{};
    for (final p in {...cleared, ...vaultsBroken.keys}) {
      if (seals[p.r][p.c] > 0) {
        seals[p.r][p.c]--;
        sealsCleared[p] = seals[p.r][p.c];
      }
    }

    // Remove gems (except cells receiving a new special).
    final removed = <Pos, Gem>{};
    for (final p in cleared) {
      final g = at(p);
      if (g == null) continue;
      removed[p] = g;
      cells[p.r][p.c] = created[p];
    }
    final actuallyCleared = cleared.where((p) => !created.containsKey(p)).toSet();

    // Gravity runs up to twice — once after the clear, and again after any
    // ingot leaves the floor. Both passes collect into `falls`, which the view
    // turns into one MoveToEffect per entry.
    //
    // Those effects are delta-based, so a gem listed twice gets two of them and
    // they SUM: it lands a whole extra pass-1 distance below where it belongs,
    // usually off the board, where the clip hides it. So the two passes are
    // merged here into a single (from, to) per gem — the origin of the first
    // fall and the destination of the last.
    final firstFrom = <int, Pos>{};
    final lastTo = <int, (Pos, Gem)>{};
    void collect(List<(Pos, Pos, Gem)> raw) {
      for (final (from, to, g) in raw) {
        firstFrom.putIfAbsent(g.id, () => from);
        lastTo[g.id] = (to, g);
      }
    }

    final pass = <(Pos, Pos, Gem)>[];
    _applyGravity(pass);
    collect(pass);

    // Ingots that have reached the floor are delivered, then everything above
    // them settles again into the space they leave.
    final ingotsDelivered = <Pos, Gem>{};
    for (var c = 0; c < cols; c++) {
      final g = cells[rows - 1][c];
      if (g?.blocker == Blocker.ingot) {
        ingotsDelivered[Pos(rows - 1, c)] = g!;
        cells[rows - 1][c] = null;
      }
    }
    if (ingotsDelivered.isNotEmpty) {
      pass.clear();
      _applyGravity(pass);
      collect(pass);
    }

    final falls = <(Pos, Pos, Gem)>[
      for (final e in lastTo.entries)
        if (firstFrom[e.key] != e.value.$1) (firstFrom[e.key]!, e.value.$1, e.value.$2),
    ];

    // Spawn into whatever is still empty. Obstacles are never spawned.
    final spawns = <Pos, Gem>{};
    for (var c = 0; c < cols; c++) {
      for (var r = 0; r < rows; r++) {
        if (cells[r][c] == null) {
          final g = Gem(_randomKind());
          cells[r][c] = g;
          spawns[Pos(r, c)] = g;
        }
      }
    }

    final base = removed.length * 10;
    final specialBonus = created.length * 50 + fired.length * 30;
    final objectiveBonus = vaultsBroken.length * 40 + vaultsDamaged.length * 12 + ingotsDelivered.length * 120 + sealsCleared.length * 20;
    final score = (base + specialBonus + objectiveBonus) * depth;

    return CascadeStep(
      cleared: actuallyCleared,
      removed: removed,
      created: created,
      falls: falls,
      spawns: spawns,
      sealsCleared: sealsCleared,
      vaultsBroken: vaultsBroken,
      vaultsDamaged: vaultsDamaged,
      ingotsDelivered: ingotsDelivered,
      score: score,
      combo: depth,
    );
  }

  /// Settles every column downward, appending to [falls].
  void _applyGravity(List<(Pos, Pos, Gem)> falls) {
    for (var c = 0; c < cols; c++) {
      var write = rows - 1;
      for (var r = rows - 1; r >= 0; r--) {
        final g = cells[r][c];
        if (g != null) {
          if (write != r) {
            cells[write][c] = g;
            cells[r][c] = null;
            falls.add((Pos(r, c), Pos(write, c), g));
          }
          write--;
        }
      }
    }
  }

  @override
  String toString() {
    final sb = StringBuffer();
    for (var r = 0; r < rows; r++) {
      final row = <String>[];
      for (var c = 0; c < cols; c++) {
        final g = cells[r][c];
        final ch = g == null
            ? '.'
            : g.blocker == Blocker.vault
                ? 'V'
                : g.blocker == Blocker.ingot
                    ? 'I'
                    : g.kind.name[0];
        row.add(seals[r][c] > 0 ? '$ch*' : '$ch ');
      }
      sb.writeln(row.join(' '));
    }
    return sb.toString();
  }
}
