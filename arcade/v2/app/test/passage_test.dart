import 'dart:io';
import 'dart:typed_data';

import 'package:flame/game.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/cabinet/cabinet.dart';
import 'package:puzzle_pack/arcade/passage/boar.dart';
import 'package:puzzle_pack/arcade/passage/eras.dart';
import 'package:puzzle_pack/arcade/passage/passage_game.dart';

/// A tall phone. Every tuning value in the game is a fraction of these, so
/// the exact numbers only matter for readability.
final _size = Vector2(412, 892);

PassageGame _game(CabinetRun run, {int seed = 7}) {
  final g = PassageGame(run: run, seed: seed);
  g.onGameResize(_size);
  return g;
}

/// Steps the simulation at 60 fps for up to [seconds], stopping early once
/// the run ends. Returns the simulated seconds elapsed.
double _fly(PassageGame g, CabinetRun run, double seconds, {void Function(double t)? each}) {
  const dt = 1 / 60;
  var t = 0.0;
  while (t < seconds && !run.ended) {
    each?.call(t);
    g.update(dt);
    t += dt;
  }
  return t;
}

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  group('passage layout', () {
    test('has one gate per era slot', () {
      final g = _game(CabinetRun());
      expect(g.gateSpecs.length, eras.length * gatesPerEra);
    });

    test('every opening fits on screen', () {
      final g = _game(CabinetRun());
      for (final s in g.gateSpecs) {
        expect(s.gapY - s.gapH / 2, greaterThanOrEqualTo(_size.y * 0.06 - 0.001));
        expect(s.gapY + s.gapH / 2, lessThanOrEqualTo(_size.y * 0.94 + 0.001));
      }
    });

    test('consecutive openings are reachable', () {
      // The generator is free to put a gap anywhere in range. Without the
      // step cap it will eventually follow a gap at the top with one at the
      // bottom, which is not difficult, it is impossible.
      final g = _game(CabinetRun());
      final specs = g.gateSpecs;
      for (var i = 1; i < specs.length; i++) {
        expect(
          (specs[i].gapY - specs[i - 1].gapY).abs(),
          lessThanOrEqualTo(_size.y * 0.26 + 0.001),
          reason: 'gate $i jumps too far from gate ${i - 1}',
        );
      }
    });

    test('openings narrow across the passage but never below four coins', () {
      final g = _game(CabinetRun());
      final specs = g.gateSpecs;
      final first = specs.first.gapH;
      final last = specs.last.gapH;
      expect(last, lessThan(first));
      // The coin is 0.052 of the height across. Anything under four
      // diameters is the cruelty this game was explicitly not built with.
      expect(last / (_size.y * 0.052), greaterThanOrEqualTo(3.9));
    });

    test('the same seed lays out the same passage', () {
      final a = _game(CabinetRun(), seed: 42).gateSpecs;
      final b = _game(CabinetRun(), seed: 42).gateSpecs;
      expect(a.map((s) => s.gapY).toList(), b.map((s) => s.gapY).toList());
    });
  });

  group('coins', () {
    test('every gate carries one gold coin that drifts the height of its opening', () {
      final g = _game(CabinetRun());
      final gates = g.gateSpecs;
      final gold = g.pickups.where((p) => p.kind == PickupKind.gold).toList();
      expect(gold.length, gates.length);
      for (var i = 0; i < gates.length; i++) {
        final s = gates[i];
        final c = gold.singleWhere((p) => p.worldX == s.worldX);
        expect(c.y, s.gapY, reason: 'it drifts about the centre of the opening');
        // At either extreme the whole coin is clear of the lip...
        expect(c.amp + g.coinRadius * 0.85, lessThan(s.gapH / 2), reason: 'gold coin in era ${s.era} touches a lip');
        // ...and the extremes are genuinely off the safe line, or the drift
        // would be decoration.
        expect(c.amp, greaterThan(g.coinRadius), reason: 'gold coin in era ${s.era} barely moves');
        // Never at rest: it sweeps top to bottom and back.
        for (var t = 0.0; t < 3; t += 0.1) {
          expect((c.yAt(t) - s.gapY).abs(), lessThanOrEqualTo(c.amp + 1e-9));
        }
        expect(c.yAt(0) != c.yAt(0.5), isTrue);
      }
    });

    test('consecutive gold coins start at opposite ends and stay opposed', () {
      final g = _game(CabinetRun());
      final gold = g.pickups.where((p) => p.kind == PickupKind.gold).toList();
      for (var i = 1; i < gold.length; i++) {
        final a = gold[i - 1], b = gold[i];
        // Normalised offset from centre, so gaps of different heights compare.
        for (var t = 0.0; t < 3; t += 0.2) {
          final fa = (a.yAt(t) - a.y) / a.amp, fb = (b.yAt(t) - b.y) / b.amp;
          expect(fa, closeTo(-fb, 1e-6), reason: 'gates ${i - 1} and $i are not in antiphase at t=$t');
        }
        expect(gold.first.yAt(0), lessThan(gold.first.y), reason: 'the first coin starts at the top');
      }
    });

    test('the metals are worth what the plan says, gold most', () {
      expect(PassageGame.goldValue, greaterThan(PassageGame.silverValue));
      expect(PassageGame.silverValue, greaterThan(PassageGame.copperValue));
      final g = _game(CabinetRun());
      // Every trail has silver at the peak of its arc and copper at the ends.
      final trail = g.pickups.where((p) => p.kind != PickupKind.gold).toList();
      expect(trail.where((p) => p.kind == PickupKind.silver), isNotEmpty);
      expect(trail.where((p) => p.kind == PickupKind.copper), isNotEmpty);
      expect(trail.where((p) => p.kind == PickupKind.silver).length,
          lessThan(trail.where((p) => p.kind == PickupKind.copper).length),
          reason: 'silver is the rarer of the two');
    });

    test('trail coins sit in open air, never in a pillar', () {
      final g = _game(CabinetRun());
      final gates = g.gateSpecs;
      for (final p in g.pickups.where((p) => p.kind != PickupKind.gold)) {
        for (final s in gates) {
          expect((p.worldX - s.worldX).abs(), greaterThan(g.gateWidth),
              reason: 'a trail coin overlaps the gate at ${s.worldX}');
        }
        expect(p.y, inInclusiveRange(_size.y * 0.06, _size.y * 0.94));
      }
    });

    test('there is nothing to chase in the calm stretch', () {
      // The open sky after the last gate is the release the design rests on.
      final g = _game(CabinetRun());
      final lastGate = g.gateSpecs.last.worldX;
      for (final p in g.pickups) {
        expect(p.worldX, lessThanOrEqualTo(lastGate));
      }
    });

    test('coins build momentum, momentum builds speed, and both are capped', () {
      final g = _game(CabinetRun());
      expect(g.speedFactor, 1.0);
      expect(g.multiplier, 1);
      var taken = 0;
      for (final p in g.pickups.where((p) => p.kind == PickupKind.gold)) {
        g.collectForTest(p);
        taken++;
        expect(g.momentum, lessThanOrEqualTo(1.0));
        expect(g.speedFactor, lessThanOrEqualTo(1 + PassageGame.maxSpeedBoost + 1e-9));
        if (taken >= 8) break;
      }
      expect(g.momentum, 1.0, reason: 'eight gold coins in a row is full momentum');
      expect(g.multiplier, 3);
      expect(g.speedFactor, closeTo(1 + PassageGame.maxSpeedBoost, 1e-9));
      expect(g.coinsTaken, taken);
      // The first coin paid ×1, the later ones more: the total is above flat
      // value and below the ceiling.
      expect(g.score, greaterThan(PassageGame.goldValue * taken));
      expect(g.score, lessThan(PassageGame.goldValue * taken * 3));
    });

    test('momentum bleeds off when nothing is taken', () {
      final run = CabinetRun();
      final g = _game(run);
      // The calm stretch: no gates to strike, nothing to take, so the only
      // thing acting on momentum is time.
      g.devSkipToLanding();
      g.devMaxMomentum();
      _fly(g, run, 2, each: (_) => g.flap());
      expect(g.momentum, lessThan(1.0));
      expect(g.momentum, greaterThan(0.85), reason: 'slowly — it is a leak, not a cliff');
    });

    test('a strike spills a few coins and resets momentum; the score never goes negative', () {
      final g = _game(CabinetRun());
      g.devMaxMomentum();
      g.score = 10;
      g.strikeForTest();
      expect(g.momentum, 0);
      expect(g.speedFactor, 1.0);
      expect(g.score, 10 - PassageGame.spillOnStrike);
      expect(g.spillCount, PassageGame.spillOnStrike, reason: 'every spilled point is a coin that can be caught');

      final h = _game(CabinetRun());
      h.score = 2;
      h.strikeForTest();
      expect(h.score, 0);
      expect(h.spillCount, 2);

      final k = _game(CabinetRun());
      k.strikeForTest();
      expect(k.score, 0);
      expect(k.spillCount, 0, reason: 'nothing to spill from nothing');
    });

    test('spilled coins that are not caught fall away', () {
      final run = CabinetRun();
      final g = _game(run);
      // Calm stretch again, and a player holding the coin up so the run does
      // not end under the spill before it has had time to fall away.
      g.devSkipToLanding();
      g.score = 10;
      g.strikeForTest();
      expect(g.spillCount, greaterThan(0));
      _fly(g, run, 4, each: (_) => g.flap());
      expect(g.spillCount, 0);
    });

    test('the score rides on the result', () {
      final run = CabinetRun();
      final g = _game(run);
      RunResult? result;
      run.onEnd = (r) => result = r;
      for (final p in g.pickups.take(6)) {
        g.collectForTest(p);
      }
      final expected = g.score;
      expect(expected, greaterThan(0));
      g.devSkipToLanding();
      _fly(g, run, 25);
      expect(result!.score, expected);
    });
  });

  group('the boar', () {
    // The sheets are loaded by bare name, which assets_test.dart cannot see,
    // and a sheet cut into the wrong number of frames would draw the wrong
    // pose for every state. The renderer refuses such a sheet and falls back
    // to the coin; this makes the same mistake fail here instead of quietly
    // shipping the coin.
    test('every stage has a sheet of eight square frames', () {
      for (final spec in BoarSpec.all.values) {
        final f = File('assets/images/${spec.file}');
        expect(f.existsSync(), isTrue, reason: '${spec.file} is missing');
        final head = ByteData.sublistView(f.readAsBytesSync(), 16, 24);
        final w = head.getUint32(0), h = head.getUint32(4);
        expect(w, h * BoarFrame.count, reason: '${spec.file} is ${w}x$h');
      }
    });

    test('grows on screen but never grows the hitbox', () {
      final specs = BoarStage.values.map((s) => BoarSpec.all[s]!).toList();
      for (var i = 1; i < specs.length; i++) {
        expect(specs[i].sizeInRadii, greaterThan(specs[i - 1].sizeInRadii));
      }
      final r = _game(CabinetRun()).coinRadius;
      for (final stage in BoarStage.values) {
        final g = PassageGame(run: CabinetRun(), seed: 7, stage: stage)..onGameResize(_size);
        expect(g.coinRadius, r, reason: '$stage changed the hitbox');
      }
    });

    test('flaps in flight, flinches on a strike, stands once landed', () {
      final run = CabinetRun();
      final g = _game(run);
      g.flap();
      final seen = <int>{};
      _fly(g, run, 0.6, each: (_) => seen.add(g.boarFrame));
      expect(seen, containsAll(BoarFrame.cycle), reason: 'the wings should beat');

      g.strikeForTest();
      g.update(1 / 60);
      expect(g.boarFrame, BoarFrame.hurt);

      g.devSkipToLanding();
      var stood = false;
      _fly(g, run, 30, each: (_) {
        if (g.phase == PassagePhase.down && g.boarFrame == BoarFrame.stand) stood = true;
      });
      expect(stood, isTrue, reason: 'a landed boar should end standing');
    });
  });

  group('star rule', () {
    // Stated once in the game's class comment and shown in those words on the
    // results sheet. If this test changes, both of those have to change too.
    test('a landing anywhere is one star', () {
      final g = _game(CabinetRun())
        ..erasCleared = 3
        ..touchdownSpeed = 0.9;
      expect(g.stars, 1);
    });

    test('a short landing does not get the soft-landing star', () {
      final g = _game(CabinetRun())
        ..erasCleared = 3
        ..touchdownSpeed = 0.01;
      expect(g.stars, 1, reason: 'a gentle touchdown short of the end is still short');
    });

    test('the whole passage is two stars', () {
      final g = _game(CabinetRun())
        ..erasCleared = eras.length
        ..touchdownSpeed = 0.9;
      expect(g.stars, 2);
    });

    test('the whole passage set down softly is three', () {
      final g = _game(CabinetRun())
        ..erasCleared = eras.length
        ..touchdownSpeed = 0.2;
      expect(g.stars, 3);
    });
  });

  group('the run always ends in a landing', () {
    test('a player who stops tapping sets down rather than dying', () {
      final run = CabinetRun();
      final g = _game(run);
      RunResult? result;
      run.onEnd = (r) => result = r;

      g.flap(); // one tap to start, then nothing
      final t = _fly(g, run, 20);

      expect(result, isNotNull, reason: 'the run must finish on its own');
      expect(result!.ending, RunEnding.short);
      expect(result!.stars, 1, reason: 'a landing is always worth a star');
      expect(result!.reached, lessThan(eras.length));
      // Reached, not cleared. A run that ends on the first gate of 1816 has
      // cleared nothing, and reporting that put "0 of 9 eras flown" directly
      // under "You set down in 1816" and dropped the era's fact — the worst
      // run got the least reason to try again.
      expect(result!.reached, greaterThanOrEqualTo(1),
          reason: 'the era the coin was in counts as reached');

      // The server refuses a mini round claimed faster than its floor, which
      // is set at 4 s for this game. If this run gets quicker than that, the
      // shortest legitimate passage stops paying.
      expect(t, greaterThan(4.5), reason: 'see config.ts mini.minDurationMs.passage');
      expect(t, lessThan(12), reason: 'and it must not drag');
    });

    test('nothing happens until the first tap', () {
      final run = CabinetRun();
      final g = _game(run);
      _fly(g, run, 5);
      expect(g.started, isFalse);
      expect(g.scrollX, 0);
      expect(run.ended, isFalse);
    });

    test('running out of reserve starts a descent, not a death', () {
      final run = CabinetRun();
      final g = _game(run);
      g.flap();
      _fly(g, run, 6);
      // Somewhere in there the reserve ran out. Whatever else happened, the
      // coin was never removed and the run never ended abruptly.
      expect(g.reserve, 0);
      expect(g.phase, anyOf(PassagePhase.descending, PassagePhase.down));
    });

    test('a skipped-ahead run lands and reports the full passage', () {
      final run = CabinetRun();
      final g = _game(run);
      RunResult? result;
      run.onEnd = (r) => result = r;
      g.devSkipToLanding();
      _fly(g, run, 25);
      expect(result, isNotNull);
      expect(result!.ending, RunEnding.landed);
      expect(result!.reached, eras.length);
      expect(result!.stars, greaterThanOrEqualTo(2));
    });
  });

  group('era content', () {
    test('is in chronological order', () {
      for (var i = 1; i < eras.length; i++) {
        expect(eras[i].year, greaterThan(eras[i - 1].year));
      }
    });

    test('every era carries a source', () {
      for (final e in eras) {
        expect(e.source.trim(), isNotEmpty, reason: '${e.year} has no source');
        expect(e.fact.trim(), isNotEmpty);
      }
    });

    test('no fact makes a claim about the product or the future', () {
      // A blunt instrument, deliberately. The rules live in the header of
      // eras.dart; this is the tripwire for the ones that are mechanical
      // enough to check, so a line added in a hurry cannot ship a claim.
      const banned = [
        'digital gold',
        'dgd',
        'invest',
        'return',
        'hedge',
        'protect',
        'store of value',
        'will ',
        'outperform',
        'better than',
        'safer',
        'unlike',
      ];
      for (final e in eras) {
        final text = e.fact.toLowerCase();
        for (final word in banned) {
          expect(text.contains(word), isFalse,
              reason: '${e.year} contains "$word", which is a claim rather than a fact');
        }
      }
    });
  });
}
