import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/passage/boar.dart';
import 'package:puzzle_pack/arcade/passage/passage_screen.dart';
import 'package:puzzle_pack/arcade/progress.dart';

/// When Pigs Fly growth, app side. The server decides the stage (see the
/// server's api.test.ts); these check that the app reads it faithfully and
/// says the right thing about a flight.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  final p = ArcadeProgress.instance;

  setUp(() {
    p.offline = false;
    p.passageClaim = null;
    p.setPassageForTest(lifetime: 0, stage: 'piglet', nextStage: 'juvenile', nextAt: 4000);
  });

  test('stage ids are the enum names, and an unknown one is not a crash', () {
    expect(BoarStage.fromId('piglet'), BoarStage.piglet);
    expect(BoarStage.fromId('razorback'), BoarStage.razorback);
    expect(BoarStage.fromId('dragon'), isNull);
    expect(BoarStage.fromId(null), isNull);
  });

  test('a snapshot without a passage block leaves the boar alone', () {
    p.setPassageForTest(lifetime: 5000, stage: 'juvenile', stageAt: 4000, nextStage: 'razorback', nextAt: 18000);
    p.apply({'xp': 10}, persist: false);
    expect(p.passageStage, 'juvenile');
    expect(p.passageLifetime, 5000);
  });

  test('a claim knows what it credited and whether it crossed a line', () {
    final grew = PassageClaim.from({'passageCredited': 300}, stageBefore: 'piglet', stageAfter: 'juvenile');
    expect(grew.credited, 300);
    expect(grew.grewInto, 'juvenile');
    final same = PassageClaim.from({'passageCredited': 40}, stageBefore: 'piglet', stageAfter: 'piglet');
    expect(same.grewInto, isNull);
    // An older server sends no figure at all: that is nothing credited.
    expect(PassageClaim.from({}, stageBefore: 'piglet', stageAfter: 'piglet').credited, 0);
  });

  Future<void> pump(WidgetTester tester, {int score = 120}) => tester.pumpWidget(MaterialApp(
        home: Scaffold(body: GrowthPanel(score: score, flew: BoarStage.piglet)),
      ));

  testWidgets('shows the stage and how far to the next while the claim is out', (tester) async {
    p.setPassageForTest(lifetime: 1240, stage: 'piglet', nextStage: 'juvenile', nextAt: 4000);
    await pump(tester);
    expect(find.text('Piglet · 1,240 / 4,000'), findsOneWidget);
    expect(find.text('Adding up the flight…'), findsOneWidget);
  });

  testWidgets('fills in what the flight added when the claim lands', (tester) async {
    await pump(tester);
    p.setPassageForTest(lifetime: 120, stage: 'piglet', nextStage: 'juvenile', nextAt: 4000);
    p.passageClaim = const PassageClaim(credited: 120);
    p.apply({}, persist: false); // notify, as a real claim does
    await tester.pump();
    expect(find.text('+120 toward juvenile'), findsOneWidget);
  });

  testWidgets('says so, once, when the boar grows', (tester) async {
    p.setPassageForTest(lifetime: 4100, stage: 'juvenile', stageAt: 4000, nextStage: 'razorback', nextAt: 18000);
    p.passageClaim = const PassageClaim(credited: 300, grewInto: 'juvenile');
    await pump(tester);
    expect(find.text('Your boar grew into a juvenile.'), findsOneWidget);
    expect(find.text('It flies as a juvenile from your next run.'), findsOneWidget);
  });

  testWidgets('a practice flight is called one, not silently ignored', (tester) async {
    p.passageClaim = const PassageClaim(credited: 0);
    await pump(tester, score: 80);
    expect(find.textContaining('practice'), findsOneWidget);
  });

  testWidgets('offline says the flight did not count', (tester) async {
    p.offline = true;
    await pump(tester);
    expect(find.textContaining('did not count'), findsOneWidget);
  });

  testWidgets('a razorback is fully grown', (tester) async {
    p.setPassageForTest(lifetime: 20000, stage: 'razorback', stageAt: 18000);
    p.passageClaim = const PassageClaim(credited: 500);
    await pump(tester);
    expect(find.text('Razorback · fully grown'), findsOneWidget);
    expect(find.text('+500. Fully grown.'), findsOneWidget);
  });
}
