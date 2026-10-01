import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/passage/boar.dart';
import 'package:puzzle_pack/arcade/passage/grow_up.dart';

/// The growing-up moment: it builds up in silhouette, reveals the new stage
/// with its line, can't be skipped before the reveal, and closes itself.
void main() {
  Future<void> open(WidgetTester tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(MaterialApp(
      home: Builder(
        builder: (context) => Scaffold(
          body: Center(
            child: TextButton(
              onPressed: () => showGrowUp(context, from: BoarStage.piglet, to: BoarStage.juvenile),
              child: const Text('open'),
            ),
          ),
        ),
      ),
    ));
    await tester.tap(find.text('open'));
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 300));
  }

  final ms = GrowUpMoment.duration.inMilliseconds;
  final revealMs = (ms * GrowUpMoment.revealAt).round();

  testWidgets('builds up in silhouette before the reveal', (tester) async {
    await open(tester);
    expect(find.byType(GrowUpMoment), findsOneWidget);
    expect(find.byType(ColorFiltered), findsOneWidget, reason: 'the boar is a silhouette');
    expect(find.textContaining('grew into'), findsNothing);
  });

  testWidgets('reveals the new stage with its line', (tester) async {
    await open(tester);
    await tester.pump(Duration(milliseconds: revealMs + 400));
    expect(find.byType(ColorFiltered), findsNothing, reason: 'the new stage in full colour');
    expect(find.text('Your boar grew into a juvenile!'), findsOneWidget);
    final portrait = tester.widget<BoarPortrait>(find.byType(BoarPortrait));
    expect(portrait.stage, BoarStage.juvenile);
  });

  testWidgets('a tap during the build-up does not skip it; after the reveal it closes', (tester) async {
    await open(tester);
    await tester.tapAt(const Offset(200, 400));
    await tester.pump(const Duration(milliseconds: 300));
    expect(find.byType(GrowUpMoment), findsOneWidget);
    await tester.pump(Duration(milliseconds: revealMs + 200));
    await tester.tapAt(const Offset(200, 400));
    await tester.pumpAndSettle();
    expect(find.byType(GrowUpMoment), findsNothing);
  });

  testWidgets('closes by itself', (tester) async {
    await open(tester);
    await tester.pump(Duration(milliseconds: ms + 100));
    await tester.pumpAndSettle();
    expect(find.byType(GrowUpMoment), findsNothing);
  });

  // Inside the DGD app the moment is calm (audit E6): the same build-up,
  // stage and line, without the flash or the sparkle burst.
  Future<void> openMoment(WidgetTester tester, {required bool calm}) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(MaterialApp(
      home: GrowUpMoment(from: BoarStage.piglet, to: BoarStage.juvenile, calm: calm),
    ));
  }

  bool whiteFlash(WidgetTester tester) => tester
      .widgetList<Container>(find.byType(Container))
      .any((c) => c.color != null && c.color!.r == 1 && c.color!.g == 1 && c.color!.b == 1 && c.color!.a > 0);

  bool burst(WidgetTester tester) => tester
      .widgetList<CustomPaint>(find.byType(CustomPaint))
      .any((p) => p.painter != null && p.painter.runtimeType.toString() == '_BurstPainter');

  testWidgets('standalone: the reveal flashes white and bursts with sparkles', (tester) async {
    await openMoment(tester, calm: false);
    await tester.pump(Duration(milliseconds: revealMs + 50));
    expect(whiteFlash(tester), isTrue);
    expect(burst(tester), isTrue);
  });

  testWidgets('in the DGD app: no flash and no sparkles, but the stage and its line', (tester) async {
    await openMoment(tester, calm: true);
    var sawStage = false;
    for (var at = 100; at < ms; at += 100) {
      await tester.pump(const Duration(milliseconds: 100));
      expect(whiteFlash(tester), isFalse, reason: 'no white flash at $at ms');
      expect(burst(tester), isFalse, reason: 'no sparkle burst at $at ms');
      if (!sawStage && at >= revealMs + 400) {
        expect(find.text('Your boar grew into a juvenile!'), findsOneWidget);
        expect(tester.widget<BoarPortrait>(find.byType(BoarPortrait)).stage, BoarStage.juvenile);
        sawStage = true;
      }
    }
    expect(sawStage, isTrue);
  });
}
