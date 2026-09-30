import 'passage_sim.dart';

/// DEV: flies the passage by itself, so a whole run (every era, every
/// crossfade, the landing after a passage flown) can be watched on a phone,
/// and so a test can fly one without a player.
///
/// It is a tap and nothing more: [wantsFlap] says whether to tap now, and
/// the caller taps through the same `flap()` a player uses. So the run it
/// flies is an ordinary run, recorded input by input, not a special mode of
/// the simulation. The caller taints the run: an autopilot score is not a
/// player's.
///
/// The rule. A flap sets the climb to [PassageSim.flapImpulse], which
/// gravity turns into a rise of about 7.7% of the screen before the fall.
/// So hold a line a little below the middle of the next opening, and tap
/// whenever the boar has sunk past it and is not already climbing: the arc
/// then rides through the middle. Between gates the line eases from one
/// opening to the next, so a big step in height is not left to the last
/// moment.
abstract final class Autopilot {
  static bool wantsFlap(PassageSim s) {
    if (s.phase != PassagePhase.flying || s.finished) return false;
    final target = targetY(s);
    return s.coinY > target && s.vy > -s.h * 0.05;
  }

  /// The height to hold now: the next opening's middle, lowered by a third
  /// of a flap's rise, eased toward the opening after it once the boar is
  /// through.
  static double targetY(PassageSim s) {
    final gates = s.gates;
    // The next gate the body has not yet cleared.
    var i = gates.indexWhere((g) => g.worldX + s.gateW / 2 + s.bodyL + s.bodyR > s.scrollX);
    if (i < 0) return s.h * 0.5;
    final g = gates[i];
    final below = s.h * 0.026;
    var y = g.gapY + below;
    // Past the gate's front edge: already inside, hold its opening. Before
    // it, and still far off, lean toward it from the last one.
    if (i > 0) {
      final prev = gates[i - 1];
      final span = g.worldX - prev.worldX;
      final f = ((s.scrollX - prev.worldX) / span).clamp(0.0, 1.0);
      final lean = (f * 1.6).clamp(0.0, 1.0);
      y = prev.gapY + below + (y - prev.gapY - below) * lean;
    }
    return y;
  }
}
