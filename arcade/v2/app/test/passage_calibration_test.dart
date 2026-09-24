import 'dart:math';

import 'package:flame/game.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/cabinet/cabinet.dart';
import 'package:puzzle_pack/arcade/passage/eras.dart';
import 'package:puzzle_pack/arcade/passage/passage_game.dart';

/// When Pigs Fly calibration: simulated players flying the real simulation.
///
/// Growth thresholds and shop prices are only as good as the guess of what a
/// run scores. Until real runs are on a server (see the server's
/// `passage-report`), this is the best evidence there is: a bot that sees
/// what a player sees — the openings, the coins, its own height and speed —
/// reacts after a delay, aims imperfectly, and taps no faster than a thumb.
/// Three profiles bracket the players we expect.
///
/// It is a bot, not a person. It does not get bored, misread a banner or
/// play one-handed on a bus; it also does not learn. Treat its numbers as a
/// bracket for the first thresholds, and replace them with measured ones.
///
/// By default this runs a short playability check: a skilled bot has to be
/// able to fly the whole passage, or the game has become unfair. The full
/// report runs with
///
///   flutter test test/passage_calibration_test.dart --dart-define=CALIBRATE=true
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  // The passage has to be flyable at human reaction speed by someone who
  // simply flies it: a steady player who ignores the coins and never looks
  // away gets through every gate. If a change to the gaps, the speed or the
  // drift breaks this, the game has become unfair, not harder.
  test('a steady player can fly the whole passage', () {
    final runs = [for (final seed in [11, 12, 13, 14]) _Bot(_Profile.steady, seed).fly()];
    expect(runs.every((r) => r.eras >= eras.length && r.strikes == 0), isTrue, reason: 'runs: $runs');
  });

  test('trace', () {
    _Bot(_Profile.skilled, 11, trace: true).fly();
  }, skip: const bool.fromEnvironment('TRACE') ? false : 'debug only');

  test('calibration report', () {
    const n = 40;
    final out = StringBuffer('\nWhen Pigs Fly calibration, $n runs per profile\n');
    final medians = <String, double>{};
    for (final prof in _Profile.all) {
      final runs = [for (var s = 0; s < n; s++) _Bot(prof, 1000 + s).fly()];
      final scores = [for (final r in runs) r.score]..sort();
      double pct(double q) => scores[((scores.length - 1) * q).round()].toDouble();
      final mean = scores.reduce((a, b) => a + b) / scores.length;
      final full = runs.where((r) => r.eras >= eras.length).length / n;
      final stars = runs.map((r) => r.stars).reduce((a, b) => a + b) / n;
      final eraMean = runs.map((r) => r.eras).reduce((a, b) => a + b) / n;
      medians[prof.name] = pct(0.5);
      out.writeln('${prof.name.padRight(8)} score p25 ${pct(.25).toStringAsFixed(0).padLeft(4)}'
          '  median ${pct(.5).toStringAsFixed(0).padLeft(4)}'
          '  p75 ${pct(.75).toStringAsFixed(0).padLeft(4)}'
          '  mean ${mean.toStringAsFixed(0).padLeft(4)}'
          '  | eras ${eraMean.toStringAsFixed(1)}  full ${(full * 100).toStringAsFixed(0)}%'
          '  stars ${stars.toStringAsFixed(2)}');
    }
    out.writeln('\nDays to each line at four runs a day, median score:');
    for (final e in medians.entries) {
      final perDay = 4 * e.value;
      String days(int at) => perDay <= 0 ? '—' : (at / perDay).toStringAsFixed(1);
      out.writeln('${e.key.padRight(8)} ${perDay.toStringAsFixed(0).padLeft(5)} pts/day'
          '  | first ability (600) ${days(600)} d'
          '  juvenile (1,500) ${days(1500)} d'
          '  razorback (6,000) ${days(6000)} d');
    }
    // ignore: avoid_print
    print(out);
  }, skip: const bool.fromEnvironment('CALIBRATE') ? false : 'set --dart-define=CALIBRATE=true for the report');
}

class _Profile {
  final String name;

  /// Seconds between deciding to tap and the tap landing.
  final double delay;

  /// How far off the middle of an opening this player aims, as a fraction of
  /// screen height (standard deviation, drawn afresh at each gate).
  final double aimNoise;

  /// Chance of going for a gate's gold coin, and for a trail of coins.
  final double goldGreed, trailGreed;

  /// The fastest this player's thumb repeats a tap.
  final double minTapGap;

  /// Whether they try to ease the landing at all.
  final bool eases;

  /// The human part. A bot with only the numbers above sees its own speed
  /// perfectly and never mistimes a tap, and its "casual" player flew the
  /// whole passage nine runs in ten. People misjudge how fast they are
  /// falling ([speedMisread], a fraction), tap a little early or late
  /// ([tapJitter], seconds, standard deviation), and look away
  /// ([lapsesPerMinute], each about a third of a second with no taps).
  final double speedMisread, tapJitter, lapsesPerMinute;

  const _Profile(this.name, this.delay, this.aimNoise, this.goldGreed, this.trailGreed, this.minTapGap, this.eases,
      this.speedMisread, this.tapJitter, this.lapsesPerMinute);

  static const casual = _Profile('casual', 0.22, 0.08, 0.25, 0.10, 0.18, false, 0.30, 0.07, 10);
  static const regular = _Profile('regular', 0.16, 0.05, 0.60, 0.35, 0.15, true, 0.20, 0.045, 5);
  static const skilled = _Profile('skilled', 0.11, 0.03, 0.90, 0.70, 0.12, true, 0.10, 0.025, 2);
  static const all = [casual, regular, skilled];

  /// Human reaction time and nothing else human: the playability check.
  static const steady = _Profile('steady', 0.12, 0.0, 0, 0, 0.12, true, 0, 0, 0);
}

class _Run {
  final int score, eras, stars, strikes;
  const _Run(this.score, this.eras, this.stars, this.strikes);
  @override
  String toString() => '(score $score, eras $eras, stars $stars, strikes $strikes)';
}

class _Bot {
  static final _size = Vector2(412, 892);
  final _Profile p;
  final Random rnd;
  final CabinetRun run = CabinetRun();
  late final PassageGame g;
  RunResult? result;
  int _lastReserve = PassageGame.startingReserve;

  final bool trace;
  _Bot(this.p, int seed, {this.trace = false}) : rnd = Random(seed) {
    run.onEnd = (r) => result = r;
    g = PassageGame(run: run, seed: seed)..onGameResize(_size);
  }

  double get h => _size.y;
  double get w => _size.x;

  _Run fly() {
    const dt = 1 / 60;
    var lastTap = -1.0;
    double? queued;
    var lastScroll = 0.0;
    var speed = w * 0.52;
    var aimGate = -1;
    var aimOffset = 0.0;
    var chaseGold = false, chaseTrail = false;
    var lapseUntil = -1.0;
    g.flap();

    for (var i = 0; i < 60 * 150 && result == null; i++) {
      final t = g.clock;
      if (queued != null && t >= queued) {
        g.flap();
        queued = null;
      }
      g.update(dt);
      if (g.scrollX > lastScroll) speed = (g.scrollX - lastScroll) / dt;
      lastScroll = g.scrollX;

      final r = g.coinRadius;
      double target;
      if (g.phase == PassagePhase.landing) {
        // Come down to just above the ground, and — if this player tries —
        // slow the last of the fall.
        target = g.groundY - r * 3;
        if (p.eases && g.groundY - g.boarY < r * 4 && g.boarVy > h * 0.22) target = g.boarY - r;
      } else if (g.phase != PassagePhase.flying) {
        continue;
      } else {
        final specs = g.gateSpecs;
        final gi = specs.indexWhere((s) => s.worldX - g.scrollX > -g.gateWidth / 2 - r);
        if (gi < 0) {
          target = h * 0.5;
        } else {
          final gate = specs[gi];
          if (gi != aimGate) {
            aimGate = gi;
            aimOffset = _gauss() * p.aimNoise * h;
            chaseGold = rnd.nextDouble() < p.goldGreed;
            chaseTrail = rnd.nextDouble() < p.trailGreed;
          }
          // Every flap swings the boar about 0.08 of the screen, so the
          // band it can safely aim for is the opening less a radius and
          // half that swing. The first version aimed to 1.6 radii of the
          // lip, and the bot clipped a pillar on nearly every gold coin.
          final safe = max(0.0, gate.gapH / 2 - r - h * 0.045);
          final dx = gate.worldX - g.scrollX;
          target = gate.gapY + aimOffset;
          if (chaseGold) {
            final gold = g.pickups
                .where((c) => !c.taken && c.kind == PickupKind.gold && c.worldX == gate.worldX)
                .firstOrNull;
            if (gold != null) target = gold.yAt(t + dx / max(speed, 1)) + aimOffset * 0.3;
          }
          target = target.clamp(gate.gapY - safe, gate.gapY + safe);
          // Far from the next gate, a trail coin may be worth a detour.
          if (chaseTrail && dx > w * 0.45) {
            final trail = g.pickups
                .where((c) => !c.taken && c.kind != PickupKind.gold && c.worldX - g.scrollX > r && c.worldX - g.scrollX < w * 0.3)
                .firstOrNull;
            if (trail != null) target = trail.y;
          }
        }
      }

      if (trace && (i % 15 == 0 || g.reserve != _lastReserve)) {
        final gi = g.gateSpecs.indexWhere((s) => s.worldX - g.scrollX > -g.gateWidth / 2 - g.coinRadius);
        final gs = gi < 0 ? null : g.gateSpecs[gi];
        // ignore: avoid_print
        print('t=${t.toStringAsFixed(2)} y=${g.boarY.toStringAsFixed(0)} vy=${g.boarVy.toStringAsFixed(0)} target=${target.toStringAsFixed(0)}'
            ' gate=$gi dx=${gs == null ? '-' : (gs.worldX - g.scrollX).toStringAsFixed(0)} gap=${gs == null ? '-' : '${(gs.gapY - gs.gapH / 2).toStringAsFixed(0)}..${(gs.gapY + gs.gapH / 2).toStringAsFixed(0)}'}'
            ' reserve=${g.reserve} phase=${g.phase.name}');
        _lastReserve = g.reserve;
      }
      if (t < lapseUntil) continue;
      if (rnd.nextDouble() < p.lapsesPerMinute * dt / 60) {
        lapseUntil = t + 0.25 + 0.2 * rnd.nextDouble();
        continue;
      }
      // Tap if, by the time a tap would land and bite, the boar will have
      // sunk below the target.
      if (queued == null && t - lastTap >= p.minTapGap) {
        // Where the boar will be when the tap lands: that is the bottom of
        // the next swing. (The first version looked a further 0.12 s past
        // it, and hovered a whole swing above every target.)
        final lead = p.delay;
        final g2 = h * 2.35;
        final seenVy = g.boarVy * (1 + _gauss() * p.speedMisread);
        final predicted = g.boarY + seenVy * lead + 0.5 * g2 * lead * lead;
        // Tap when about to sink half a swing below the target, so the
        // hover is centred on it rather than riding a whole swing above.
        if (predicted > target + h * 0.035) {
          queued = t + max(0.03, p.delay + _gauss() * p.tapJitter);
          lastTap = t;
        }
      }
    }
    final res = result;
    return _Run(res?.score ?? g.score, res?.reached ?? 0, res?.stars ?? 0, PassageGame.startingReserve - g.reserve);
  }

  double _gauss() {
    final u1 = max(1e-9, rnd.nextDouble()), u2 = rnd.nextDouble();
    return sqrt(-2 * log(u1)) * cos(2 * pi * u2);
  }
}
