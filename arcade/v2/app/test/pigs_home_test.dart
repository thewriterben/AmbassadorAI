import 'package:flame/game.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/api.dart';
import 'package:puzzle_pack/arcade/cabinet/cabinet.dart';
import 'package:puzzle_pack/arcade/passage/abilities.dart';
import 'package:puzzle_pack/arcade/passage/passage_game.dart';
import 'package:puzzle_pack/arcade/passage/pigs_home_screen.dart';
import 'package:puzzle_pack/arcade/progress.dart';

/// When Pigs Fly phase 4, app side: the shop as the server lists it, and the
/// loadout a run carries to its claim. Prices and ownership are the server's
/// (see its api.test.ts); this checks the app shows them faithfully and never
/// offers what it should not.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  final p = ArcadeProgress.instance;

  Map<String, dynamic> shop({int points = 1000, Map<String, int> owned = const {}, List<String> loadout = const []}) => {
        'passage': {
          'lifetime': 5000,
          'points': points,
          'stage': 'juvenile',
          'stageAt': 1500,
          'nextStage': 'razorback',
          'nextAt': 6000,
          'abilities': [
            for (final (id, costs) in [
              ('dash', [600, 1500, 3000]),
              ('grapple', [800, 1800, 3500]),
              ('teleport', [1200, 2500, 5000]),
              ('freeze', [700, 1600, 3200]),
              ('tractor', [900, 2000, 4000]),
            ])
              {
                'id': id,
                'level': owned[id] ?? 0,
                'maxLevel': 3,
                'nextCost': (owned[id] ?? 0) < 3 ? costs[owned[id] ?? 0] : null,
              },
          ],
          'loadout': loadout,
        },
      };

  test('the snapshot carries the shop and the loadout', () {
    p.apply(shop(owned: {'dash': 2}, loadout: ['dash']), persist: false);
    final dash = p.passageAbilities.firstWhere((a) => a.id == 'dash');
    expect((dash.level, dash.nextCost, dash.owned), (2, 3000, true));
    expect(p.passageAbilities.firstWhere((a) => a.id == 'teleport').owned, isFalse);
    expect(p.passageLoadout, ['dash']);
  });

  test('a run reports what it flew with, in the shape the claim checks', () {
    final run = CabinetRun();
    RunResult? result;
    run.onEnd = (r) => result = r;
    final g = PassageGame(
      run: run,
      seed: 7,
      loadout: const [EquippedAbility(AbilityKind.dash, 2), EquippedAbility(AbilityKind.freeze)],
    )..onGameResize(Vector2(412, 892));
    g.flap();
    g.devSkipToLanding();
    for (var i = 0; i < 60 * 30 && result == null; i++) {
      g.update(1 / 60);
    }
    expect(result!.loadout, [
      {'id': 'dash', 'level': 2},
      {'id': 'freeze', 'level': 1},
    ]);
  });

  group('the front room', () {
    setUp(() => ArcadeApi.baseOverride = 'http://127.0.0.1:1'); // shop visible; nothing is called
    tearDown(() => ArcadeApi.baseOverride = null);

    Future<void> pump(WidgetTester tester) async {
      tester.view.physicalSize = const Size(1080, 3200);
      tester.view.devicePixelRatio = 2.5;
      addTearDown(tester.view.reset);
      await tester.pumpWidget(const MaterialApp(home: PigsHomeScreen()));
      await tester.pump();
    }

    testWidgets('lists every ability with the next price, and only offers what is affordable', (tester) async {
      p.apply(shop(points: 700, owned: {'dash': 1}), persist: false);
      await pump(tester);
      expect(find.text('Juvenile'), findsOneWidget);
      expect(find.text('700 points'), findsOneWidget);
      for (final k in AbilityKind.values) {
        expect(find.text(k.label), findsWidgets, reason: '${k.label} missing from the shop');
      }
      FilledButton button(String label) => tester.widget<FilledButton>(find.widgetWithText(FilledButton, label));
      expect(button('Unlock · 700').onPressed, isNotNull, reason: 'freeze is affordable');
      expect(button('Unlock · 1,200').onPressed, isNull, reason: 'blink is not');
      expect(button('Level 2 · 1,500').onPressed, isNull, reason: 'dash level 2 is not');
    });

    testWidgets('only an owned ability can be taken up, and never a third', (tester) async {
      p.apply(shop(owned: {'dash': 1, 'grapple': 1, 'freeze': 1}, loadout: ['dash', 'grapple']), persist: false);
      await pump(tester);
      expect(find.text('Take it'), findsOneWidget, reason: 'freeze, owned and not taken');
      expect(find.text('Taking it'), findsNWidgets(2));
      await tester.tap(find.text('Take it'));
      await tester.pump();
      expect(find.text('Two at a time. Take one off first.'), findsOneWidget);
      expect(p.passageLoadout, ['dash', 'grapple']);
    });

    testWidgets('the loadout shows as the two buttons a run will have', (tester) async {
      p.apply(shop(owned: {'teleport': 1}, loadout: ['teleport']), persist: false);
      await pump(tester);
      expect(find.text('LEFT BUTTON'), findsOneWidget);
      expect(find.text('Empty'), findsOneWidget);
      expect(find.text('Blink'), findsNWidgets(2), reason: 'in the loadout and in the shop');
    });

    testWidgets('with no server there is no shop, only the boar and Fly', (tester) async {
      ArcadeApi.baseOverride = '';
      p.apply(shop(), persist: false);
      await pump(tester);
      expect(find.text('Fly'), findsOneWidget);
      expect(find.text('ABILITIES'), findsNothing);
      expect(find.textContaining('Unlock'), findsNothing);
    });
  });
}
