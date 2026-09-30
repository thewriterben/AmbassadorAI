import 'dart:async';

import 'package:shared_preferences/shared_preferences.dart';

import 'sim/passage_sim.dart';

/// A player's first runs of When Pigs Fly ease in: the first flies at the
/// easier tuning, the next two step back toward the standard one, and from
/// the fourth it is the game as tuned (see [PassageTuning.forRun]).
///
/// Counted on the device, as runs that ended (landed, or ran out), not
/// quit. A reinstall starts the count again, which costs a returning player
/// at most three gentler runs; a server count would need a new field for
/// that and nothing else.
abstract final class PigsOnboarding {
  static const _key = 'pigs.runsFinished';
  static int _runs = 0;
  static bool _loaded = false;

  static int get runsFinished => _runs;

  /// The tuning the next run flies at.
  static PassageTuning get tuning => PassageTuning.forRun(_runs);

  static Future<void> load() async {
    if (_loaded) return;
    _loaded = true;
    try {
      final p = await SharedPreferences.getInstance();
      _runs = p.getInt(_key) ?? 0;
    } catch (_) {
      // No storage: every run is a first run's worth of gentle, which is
      // the safer way to be wrong.
    }
  }

  /// A run ended. Counted at once, so a "Fly again" straight after reads
  /// the next step; saved in the background.
  static void recordRun() {
    if (_runs >= PassageTuning.introRuns) return;
    _runs++;
    unawaited(_save());
  }

  static Future<void> _save() async {
    try {
      final p = await SharedPreferences.getInstance();
      // The count now, not when this save began: saves started in a row
      // can finish out of order, and a stale one landing last would undo
      // the later count.
      await p.setInt(_key, _runs);
    } catch (_) {
      // Unsaved, it counts for this session: the next launch eases in
      // again from where storage last had it.
    }
  }

  /// For tests.
  static void resetForTest([int runs = 0]) {
    _runs = runs;
    _loaded = true;
  }
}
