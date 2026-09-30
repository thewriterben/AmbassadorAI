import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/entry.dart';
import 'package:puzzle_pack/arcade/passage/pigs_home_screen.dart';
import 'package:puzzle_pack/arcade/settings_screen.dart';
import 'package:puzzle_pack/main.dart';
import 'package:puzzle_pack/match3/ui/level_map.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// The DGD app opens the arcade straight into a screen (arcade/entry.dart).
/// That screen must be the whole stack, so the back gesture leaves the arcade
/// for the app rather than landing on an arcade home the app never showed.
void main() {
  setUp(() => SharedPreferences.setMockInitialValues({}));

  Future<void> send(WidgetTester tester, String where) async {
    const codec = StandardMethodCodec();
    await tester.binding.defaultBinaryMessenger.handlePlatformMessage(
      'dgd/arcade',
      codec.encodeMethodCall(MethodCall('open', where)),
      (_) {},
    );
    // Past the page transition: the replaced routes are disposed when the
    // new one has finished coming in.
    for (var i = 0; i < 4; i++) {
      await tester.pump(const Duration(milliseconds: 400));
    }
  }

  Future<void> pumpApp(WidgetTester tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    ArcadeEntry.home = () => const HomeScreen();
    ArcadeEntry.listen();
    await tester.pumpWidget(const ArcadeApp());
    await tester.pump();
  }

  for (final (where, type) in [
    ('pigs', PigsHomeScreen),
    ('coin_quest', LevelMapScreen),
    ('settings', SettingsScreen),
  ]) {
    testWidgets('open($where) shows that screen, alone on the stack', (tester) async {
      await pumpApp(tester);
      await send(tester, where);
      expect(find.byType(type), findsOneWidget);
      expect(find.byType(HomeScreen), findsNothing, reason: 'the arcade home must not sit underneath');
      expect(ArcadeEntry.navigator.currentState!.canPop(), isFalse);
    });
  }

  testWidgets('open(home) goes back to the arcade home', (tester) async {
    await pumpApp(tester);
    await send(tester, 'pigs');
    await send(tester, 'home');
    expect(find.byType(HomeScreen), findsOneWidget);
  });
}
