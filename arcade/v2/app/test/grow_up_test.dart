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
}
