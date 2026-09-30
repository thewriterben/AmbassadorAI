import 'package:flame/game.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/cabinet/cabinet.dart';
import 'package:puzzle_pack/arcade/passage/abilities.dart';
import 'package:puzzle_pack/arcade/passage/passage_game.dart';

final _size = Vector2(412, 892);

PassageGame _game(List<AbilityKind> kinds, {int level = 1, CabinetRun? run}) {
  final g = PassageGame(
    run: run ?? CabinetRun(),
    seed: 7,
    loadout: [for (final k in kinds) EquippedAbility(k, level)],
  );
  g.onGameResize(_size);
  return g;
}

/// Steps [seconds] at 60 fps with no input.
void _step(PassageGame g, double seconds) {
  for (var t = 0.0; t < seconds; t += 1 / 60) {
    g.update(1 / 60);
  }
}

/// Starts the run and parks the boar just short of gate [i], in its opening.
void _parkBefore(PassageGame g, int i, {double short = 0.25}) {
  g.flap();
  final gate = g.gateSpecs[i];
  g.scrollX = gate.worldX - _size.x * short;
  g.boarYForTest = gate.gapY;
}

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  group('ability numbers', () {
    test('every ability is held back by a cooldown or a charge count', () {
      for (final k in AbilityKind.values) {
        for (var l = 1; l <= maxAbilityLevel; l++) {
          final s = AbilityStats.of(k, l);
          expect(s.cooldown > 0 || s.charges > 0, isTrue, reason: '$k at $l is free');
        }
      }
    });

    test('a higher level is never worse', () {
      for (final k in AbilityKind.values) {
        for (var l = 2; l <= maxAbilityLevel; l++) {
          final a = AbilityStats.of(k, l - 1), b = AbilityStats.of(k, l);
          expect(b.cooldown, lessThanOrEqualTo(a.cooldown), reason: '$k cooldown at $l');
          expect(b.duration, greaterThanOrEqualTo(a.duration), reason: '$k duration at $l');
          expect(b.charges, greaterThanOrEqualTo(a.charges), reason: '$k charges at $l');
          expect(b.reach, greaterThanOrEqualTo(a.reach), reason: '$k reach at $l');
          expect(b.immunity, greaterThanOrEqualTo(a.immunity), reason: '$k immunity at $l');
        }
      }
    });

    test('a run carries at most two', () {
      expect(_game(AbilityKind.values).slots.length, 2);
      expect(_game(const []).slots, isEmpty);
    });
  });

  group('when abilities can fire', () {
    test('not before the first tap, and not in a descent', () {
      final g = _game([AbilityKind.dash]);
      expect(g.useAbility(0), isFalse);
      g.flap();
      g.devEndShort();
      g.update(1 / 60);
      expect(g.useAbility(0), isFalse);
    });

    test('a used ability waits out its cooldown', () {
      final g = _game([AbilityKind.dash]);
      _parkBefore(g, 0, short: 0.6);
      final x = g.scrollX, y = g.boarY;
      // Held in open air, so the run does not crash out while we wait.
      void hold(double seconds) {
        for (var t = 0.0; t < seconds; t += 1 / 60) {
          g.scrollX = x;
          g.boarYForTest = y;
          g.update(1 / 60);
        }
      }

      expect(g.useAbility(0), isTrue);
      hold(1);
      expect(g.useAbility(0), isFalse);
      hold(AbilityStats.of(AbilityKind.dash, 1).cooldown);
      expect(g.canUseAbility(0), isTrue);
    });

    test('a button with nothing to act on is dead, and costs nothing', () {
      final g = _game([AbilityKind.teleport]);
      g.flap();
      g.devSkipToLanding(); // the calm stretch: no gate ahead
      expect(g.useAbility(0), isFalse);
      expect(g.slots[0].chargesLeft, 1);
    });
  });

  group('dash', () {
    test('holds altitude, doubles the scroll, and is untouchable at a pillar', () {
      final g = _game([AbilityKind.dash]);
      final gate = g.gateSpecs[2];
      _parkBefore(g, 2, short: 0.02);
      // Well outside the opening, where the pillar is.
      g.boarYForTest = (gate.gapY - gate.gapH / 2 - 40).clamp(30, _size.y * 0.5);
      final y = g.boarY, x = g.scrollX;
      expect(g.useAbility(0), isTrue);
      _step(g, 0.2);
      expect(g.boarY, closeTo(y, 0.01));
      expect(g.reserve, PassageGame.startingReserve, reason: 'struck while dashing');
      expect(g.scrollX - x, greaterThan(0.2 * _size.x * 0.52 * 1.8));
    });

    test('the same pillar, without a dash, is a strike', () {
      final g = _game(const []);
      final gate = g.gateSpecs[2];
      _parkBefore(g, 2, short: 0.02);
      g.boarYForTest = (gate.gapY - gate.gapH / 2 - 40).clamp(30, _size.y * 0.5);
      _step(g, 0.1);
      expect(g.reserve, PassageGame.startingReserve - 1);
    });
  });

  group('grapple', () {
    test('hauls the boar to the nearest gold coin ahead and takes it', () {
      final g = _game([AbilityKind.grapple]);
      _parkBefore(g, 3, short: 0.5);
      final gold = g.pickups.firstWhere((p) => p.kind == PickupKind.gold && p.worldX == g.gateSpecs[3].worldX);
      g.boarYForTest = gold.yAt(0) + (gold.yAt(0) > _size.y / 2 ? -120 : 120);
      expect(g.useAbility(0), isTrue);
      expect(g.grappling, isTrue);
      _step(g, 1.2);
      expect(gold.taken, isTrue);
      expect(g.grappling, isFalse);
    });

    test('never drags the boar into a pillar on the way', () {
      final g = _game([AbilityKind.grapple]);
      final gate = g.gateSpecs[3];
      _parkBefore(g, 3, short: 0.12);
      // High above the opening, so the haul down crosses the top pillar.
      g.boarYForTest = (gate.gapY - gate.gapH / 2 - 90).clamp(30.0, gate.gapY);
      expect(g.useAbility(0), isTrue);
      for (var i = 0; i < 72 && g.grappling; i++) {
        g.update(1 / 60);
      }
      expect(g.reserve, PassageGame.startingReserve);
    });

    test('a flap lets go', () {
      final g = _game([AbilityKind.grapple]);
      _parkBefore(g, 3, short: 0.5);
      expect(g.useAbility(0), isTrue);
      g.flap();
      expect(g.grappling, isFalse);
    });
  });

  group('blink', () {
    test('moves only vertically, to the middle of the next opening, and is counted', () {
      final g = _game([AbilityKind.teleport]);
      _parkBefore(g, 4, short: 0.5);
      g.boarYForTest = 60;
      final x = g.scrollX, target = g.nextGapY!;
      expect(g.useAbility(0), isTrue);
      expect(g.boarY, target);
      expect(g.scrollX, x, reason: 'a blink must never carry the boar along the passage');
      expect(g.slots[0].chargesLeft, 0);
      _step(g, 2);
      expect(g.useAbility(0), isFalse, reason: 'level 1 has one blink');
    });

    test('a higher level carries more blinks', () {
      expect(_game([AbilityKind.teleport], level: 3).slots[0].chargesLeft, 3);
    });
  });

  group('freeze shot', () {
    test('stops the next gold coin drifting, and it resumes from where it stopped', () {
      final g = _game([AbilityKind.freeze]);
      _parkBefore(g, 5, short: 0.9);
      expect(g.useAbility(0), isTrue);
      expect(g.shotInFlight, isTrue);
      var frozen = false;
      for (var i = 0; i < 120 && !frozen; i++) {
        g.update(1 / 60);
        frozen = g.pickups.any((p) => p.kind == PickupKind.gold && p.frozenAt(g.clock));
      }
      expect(frozen, isTrue);
    });

    test('a frozen coin holds still and thaws without a jump', () {
      final p = Pickup(worldX: 0, y: 400, kind: PickupKind.gold, amp: 80);
      p.freezeAt(1.0, 3.0);
      final held = p.yAt(1.0);
      expect(p.yAt(2.5), held);
      expect(p.yAt(3.99), held);
      expect(p.yAt(4.01), closeTo(held, 2));
      // And it carries on drifting after.
      expect(p.yAt(4.6), isNot(closeTo(held, 1)));
    });
  });

  group('tractor beam', () {
    test('draws in the coins within reach, and only those', () {
      final g = _game([AbilityKind.tractor]);
      final reach = AbilityStats.of(AbilityKind.tractor, 1).reach * _size.y;
      // A trail coin well past the first gates, with the boar parked at
      // level with it, most of a beam's reach behind: out of touching range,
      // inside the beam.
      final coin = g.pickups.firstWhere((p) => p.kind == PickupKind.silver && p.worldX > g.gateSpecs[6].worldX);
      g.flap();
      g.scrollX = coin.worldX - reach * 0.6;
      g.boarYForTest = coin.y;
      final far = g.pickups.where((p) => p.worldX - g.scrollX > _size.x * 3).toList();
      final before = g.coinsTaken;
      expect(g.useAbility(0), isTrue);
      g.update(1 / 60);
      expect(coin.pull, isNotNull, reason: 'the beam should have caught it');
      _step(g, 0.3);
      expect(coin.taken, isTrue);
      expect(g.coinsTaken, greaterThan(before));
      expect(far.any((p) => p.taken), isFalse);
    });
  });

  group('the controls layer', () {
    testWidgets('a button takes its own tap; everywhere else is still the game\'s', (tester) async {
      var flaps = 0, presses = 0;
      await tester.pumpWidget(MaterialApp(
        home: CabinetScreen(
          gameId: 'test',
          title: 'Test',
          kicker: 'TEST',
          builder: (run) {
            run.onTap = () => flaps++;
            return FlameGame();
          },
          hudBuilder: (_, __) => const SizedBox.shrink(),
          resultBuilder: (_, __) => const SizedBox.shrink(),
          controlsBuilder: (_, __) => Stack(children: [
            Positioned(
              left: 20,
              bottom: 20,
              child: GestureDetector(
                behavior: HitTestBehavior.opaque,
                onTapDown: (_) => presses++,
                child: const SizedBox.square(key: Key('btn'), dimension: 60),
              ),
            ),
          ]),
        ),
      ));
      await tester.pump();
      await tester.tap(find.byKey(const Key('btn')));
      expect((presses, flaps), (1, 0));
      await tester.tapAt(tester.getCenter(find.byType(CabinetScreen)));
      expect((presses, flaps), (1, 1));
    });
  });
}
