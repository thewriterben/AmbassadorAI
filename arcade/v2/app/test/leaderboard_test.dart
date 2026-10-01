import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/api.dart';
import 'package:puzzle_pack/arcade/leaderboard_screen.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// The weekly standings, as DGD App 2.1 opens them from the Arcade tab
/// (audit L3). Recognition only: the screen says so, and its ranks are
/// plain numbers rather than the coin medals it used to give the top three.
void main() {
  setUp(() => SharedPreferences.setMockInitialValues({}));
  tearDown(() => ArcadeApi.baseOverride = null);

  Future<void> pump(WidgetTester tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(const MaterialApp(home: LeaderboardScreen()));
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 100));
  }

  testWidgets('says it is recognition only, and wears no coin medals', (tester) async {
    ArcadeApi.baseOverride = '';
    await pump(tester);
    expect(find.text('Weekly standings'), findsOneWidget);
    expect(
      find.text('Recognition only. XP, points and badges have no monetary value and cannot be exchanged.'),
      findsOneWidget,
    );
    final assets = tester
        .widgetList<Image>(find.byType(Image))
        .map((i) => i.image)
        .whereType<AssetImage>()
        .map((a) => a.assetName);
    expect(assets.where((n) => n.contains('coin_')), isEmpty, reason: 'no prize-like medals on a board that pays nothing');
  });

  testWidgets('with no server, it says the standings live there, and offers to try again', (tester) async {
    ArcadeApi.baseOverride = '';
    await pump(tester);
    final unreachable = find.text("The arcade server can't be reached. The standings are kept there.");
    final refused = find.textContaining('Could not load the standings');
    expect(unreachable.evaluate().length + refused.evaluate().length, 1);
    expect(find.text('Try again'), findsOneWidget);
    expect(find.textContaining('Expedition'), findsNothing, reason: 'v1 copy is gone');
    expect(find.textContaining('Ledger'), findsNothing);
  });
}
