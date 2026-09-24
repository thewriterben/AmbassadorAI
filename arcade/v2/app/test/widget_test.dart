import 'package:flame/game.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:puzzle_pack/arcade/passage/eras.dart';
import 'package:puzzle_pack/main.dart';

/// The home catalogue is Coin Quest and Passage while the rest are built.
///
/// The nine removed on 2026-09-16 — Tablet Run, the Daily Ledger, the three
/// knowledge mini-games, Merge, Words, Blocks and Rope — are asserted *absent*
/// rather than simply dropped from the list. Their screens were deleted, but a
/// half-finished revert or a stray import could put a card back on the home
/// screen pointing at nothing, and the symptom would be a crash on tap rather
/// than anything visible here.
void main() {
  const removed = [
    'Tablet Run',
    'Daily Ledger',
    'Pillar Sort',
    'Design or Myth?',
    'Chain Builder',
    'Merge',
    'Words',
    'Blocks',
    'Rope',
  ];

  testWidgets('home lists the two built games and nothing else', (tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(const ArcadeApp());
    await tester.pump();

    await tester.scrollUntilVisible(
        find.text('Coin Quest: Digital Gold'), 150, scrollable: find.byType(Scrollable).first);
    expect(find.text('Coin Quest: Digital Gold'), findsOneWidget);
    expect(find.text('When Pigs Fly'), findsOneWidget);

    for (final t in removed) {
      expect(find.text(t), findsNothing, reason: '$t was removed but is still on the home screen');
    }
  });

  // Passage opens, takes a tap and does not end the run on contact. This is
  // the cheapest guard on the thing the whole design rests on: if a future
  // change turns a strike back into a death, the run would end during this
  // pump and the result sheet would appear.
  testWidgets('Passage opens and a strike does not end the run', (tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(const ArcadeApp());
    await tester.pump();

    final card = find.text('When Pigs Fly');
    await tester.scrollUntilVisible(card, 150, scrollable: find.byType(Scrollable).first);
    await tester.tap(card);
    // The card opens the boar's front room; Fly opens the game.
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 400));
    await tester.tap(find.text('Fly'));
    // Not pumpAndSettle: a Flame game schedules a frame forever, so nothing
    // on this screen ever settles. Two pumps is the route transition.
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 500));

    expect(find.text('Tap to fly'), findsOneWidget);

    // One more frame: the game sets the first era from its update loop, which
    // marks the banner dirty for the frame after.
    await tester.pump(const Duration(milliseconds: 100));

    // The opening era banner has to be up before the first tap — the coin
    // hovers precisely so there is time to read it. The first implementation
    // started its animation from a listener registered during build, which
    // raced the game's own layout and on device left the banner sitting at
    // t = 0 forever. The year alone is not enough to assert on, because the
    // HUD shows it too; the era name appears only on the banner.
    expect(find.text(eras.first.name.toUpperCase()), findsOneWidget);

    await tester.tapAt(const Offset(200, 500));

    // Real frames, not one four-second jump: the game clamps a long frame to
    // 1/30 s precisely so a stall cannot teleport the coin, which would make
    // a single big pump advance almost nothing.
    for (var i = 0; i < 240; i++) {
      await tester.pump(const Duration(milliseconds: 16));
    }
    expect(find.text('Fly again'), findsNothing, reason: 'a strike must not end the run');
  });

  // The cabinet's stack is all Positioned.fill except the HUD row, and a
  // Stack takes its size from its non-positioned children. Without
  // StackFit.expand it collapsed to the height of the HUD and the game
  // rendered in a ~400px strip at the top of a black screen. Everything else
  // — analyze, 50 unit tests — was clean, because the game itself was fine
  // and only the box it was handed was wrong. This is the assertion that
  // would have caught it.
  testWidgets('the game fills the screen', (tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(const ArcadeApp());
    await tester.pump();

    final card = find.text('When Pigs Fly');
    await tester.scrollUntilVisible(card, 150, scrollable: find.byType(Scrollable).first);
    await tester.tap(card);
    // The card opens the boar's front room; Fly opens the game.
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 400));
    await tester.tap(find.text('Fly'));
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 500));

    final screen = tester.view.physicalSize / tester.view.devicePixelRatio;
    final game = tester.getSize(find.byType(GameWidget));
    expect(game.width, moreOrLessEquals(screen.width, epsilon: 1));
    expect(game.height, moreOrLessEquals(screen.height, epsilon: 1));
  });

  // Both stores ask whether a user can request deletion of their data, and
  // expect the route to be reachable in the app. Answering "yes" on the
  // questionnaire is a statement about this screen existing and being findable,
  // so it is worth a test rather than an assumption.
  testWidgets('the data-deletion controls are reachable from home', (tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(const ArcadeApp());
    await tester.pump();

    final entry = find.text('Settings and your data');
    await tester.scrollUntilVisible(entry, 150, scrollable: find.byType(Scrollable).first);
    // scrollUntilVisible stops as soon as the list has built the entry, which
    // can be just below the fold; a longer home-card blurb put it 11 px off
    // screen and the tap landed on nothing.
    // Not pumpAndSettle: home runs an ambient animation that never settles
    // until a route covers it.
    await tester.ensureVisible(entry);
    await tester.pump(const Duration(milliseconds: 300));
    await tester.tap(entry);
    await tester.pumpAndSettle();

    expect(find.text('Delete my play record'), findsOneWidget);
    expect(find.text('Erase progress on this device'), findsOneWidget);
  });

  testWidgets('home still promises the games to come', (tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(const ArcadeApp());
    await tester.pump();

    await tester.scrollUntilVisible(
        find.text('More games coming soon'), 150, scrollable: find.byType(Scrollable).first);
    expect(find.text('More games coming soon'), findsOneWidget);
  });
}
