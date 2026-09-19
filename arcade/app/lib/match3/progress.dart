import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// Persisted per-level clears, stars and best scores.
///
/// Clearing and scoring are deliberately separate. On an objective level —
/// seals, vaults, ingots — the win condition is the objective and `targetScore`
/// is only the par used for star thresholds, so it is entirely normal to finish
/// a vault level under par and earn zero stars. Progression has to follow the
/// clear, not the stars, or those levels never open the next one.
class Progress extends ChangeNotifier {
  static final Progress instance = Progress._();
  Progress._();

  SharedPreferences? _prefs;
  final Set<int> _cleared = {};
  final Map<int, int> _stars = {};
  final Map<int, int> _best = {};

  Future<void> load() async {
    final p = _prefs ??= await SharedPreferences.getInstance();
    // A reload, not a merge. main() and the level map both call this, and
    // leaving stale in-memory entries in place would let a cleared flag
    // outlive the store it came from.
    _cleared.clear();
    _stars.clear();
    _best.clear();
    // Every read is defensive. This walks *every* key in the shared store, so a
    // key added elsewhere that happens to share a prefix, or a value of an
    // unexpected type, must not throw: the maps are cleared above, so a throw
    // here would leave them empty while the store is intact — the map would
    // show level 1 only, and the next win would overwrite a stored 3-star,
    // because record() compares against a zero that isn't really there.
    for (final k in p.getKeys()) {
      if (k.startsWith('m3.stars.')) {
        final id = int.tryParse(k.substring(9));
        final v = id == null ? null : p.getInt(k);
        if (id == null || v == null) continue;
        _stars[id] = v;
        // Saves written before clears were tracked only recorded stars, so any
        // level with a star is retroactively a clear.
        if (v > 0) _cleared.add(id);
      } else if (k.startsWith('m3.best.')) {
        final id = int.tryParse(k.substring(8));
        final v = id == null ? null : p.getInt(k);
        if (id != null && v != null) _best[id] = v;
      } else if (k.startsWith('m3.clear.')) {
        final id = int.tryParse(k.substring(9));
        if (id != null) _cleared.add(id);
      }
    }
    notifyListeners();
  }

  /// Drops the cached store and every in-memory entry.
  ///
  /// Only for tests. This is a singleton, and `setMockInitialValues` swaps in
  /// a fresh store while `_prefs` still points at the old one, so without this
  /// one test's writes land in a store the next test has already replaced.
  @visibleForTesting
  Future<void> resetForTest() async {
    _cleared.clear();
    _stars.clear();
    _best.clear();
    _prefs = await SharedPreferences.getInstance();
    await _prefs!.clear();
  }

  /// Marks every level below [level] cleared, so the map opens up to it.
  ///
  /// Test builds only — reached from the DEV menu, which is compiled out
  /// unless DGD_DEV is defined. Deliberately does not award stars: the point
  /// is to reach a world quickly, and a fake 3-star run would hide exactly the
  /// zero-star progression case that needs testing.
  Future<void> devUnlockThrough(int level) async {
    final p = _prefs ??= await SharedPreferences.getInstance();
    for (var i = 1; i < level; i++) {
      if (_cleared.add(i)) await p.setBool('m3.clear.$i', true);
    }
    notifyListeners();
  }

  /// Wipes all Coin Quest progress, including the first-run coaching cards.
  ///
  /// Not dev-only despite its origins: this is also what the "erase progress on
  /// this device" control in Settings calls, so it is a user-facing action and
  /// has to stay correct rather than merely convenient.
  Future<void> eraseAll() async {
    final p = _prefs ??= await SharedPreferences.getInstance();
    for (final k in p.getKeys().where((k) => k.startsWith('m3.')).toList()) {
      await p.remove(k);
    }
    _cleared.clear();
    _stars.clear();
    _best.clear();
    notifyListeners();
  }

  int stars(int level) => _stars[level] ?? 0;
  int best(int level) => _best[level] ?? 0;
  bool cleared(int level) => _cleared.contains(level);
  int get totalStars => _stars.values.fold(0, (a, b) => a + b);

  /// Highest level id the player may attempt.
  ///
  /// Walks the clears from level 1. A gap stops the walk, which is intended —
  /// levels open in order — but the gap is now "you have not finished it",
  /// not "you finished it without scoring par".
  int get unlocked {
    var u = 1;
    while (_cleared.contains(u)) {
      u++;
    }
    return u;
  }

  /// Records the outcome of a finished level.
  ///
  /// [won] is what unlocks the next level. Stars and best score are still only
  /// written when they improve, but a win always persists, including a
  /// zero-star one — that was the bug: `stars > _stars[level]` is false for
  /// 0 > 0, so a cleared objective level saved nothing at all and re-locked
  /// itself on the next launch.
  Future<void> record(int level, int score, int stars, {required bool won}) async {
    // record() can be reached before load() on a cold start into a level, and
    // a null _prefs would have silently dropped the write.
    final p = _prefs ??= await SharedPreferences.getInstance();
    var changed = false;

    if (won && _cleared.add(level)) {
      await p.setBool('m3.clear.$level', true);
      changed = true;
    }
    if (stars > (_stars[level] ?? 0)) {
      _stars[level] = stars;
      await p.setInt('m3.stars.$level', stars);
      changed = true;
    }
    if (score > (_best[level] ?? 0)) {
      _best[level] = score;
      await p.setInt('m3.best.$level', score);
      changed = true;
    }
    if (changed) notifyListeners();
  }
}
