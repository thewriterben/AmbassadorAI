import 'package:flutter/widgets.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:puzzle_pack/main.dart';

/// The home catalogue is Coin Quest alone while the next ten games are built.
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

  testWidgets('home lists Coin Quest and nothing else', (tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(const ArcadeApp());
    await tester.pump();

    await tester.scrollUntilVisible(
        find.text('Coin Quest: Digital Gold'), 150, scrollable: find.byType(Scrollable).first);
    expect(find.text('Coin Quest: Digital Gold'), findsOneWidget);

    for (final t in removed) {
      expect(find.text(t), findsNothing, reason: '$t was removed but is still on the home screen');
    }
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
