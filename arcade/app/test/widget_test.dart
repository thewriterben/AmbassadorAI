import 'package:flutter/widgets.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:puzzle_pack/main.dart';

void main() {
  testWidgets('arcade home lists every game', (tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(const ArcadeApp());
    await tester.pump();
    for (final t in [
      'Tablet Run', 'Daily Ledger', 'Pillar Sort', 'Design or Myth?', 'Chain Builder',
      'Coin Quest: Digital Gold', 'Merge', 'Words', 'Blocks', 'Rope',
    ]) {
      await tester.scrollUntilVisible(find.text(t), 150, scrollable: find.byType(Scrollable).first);
      expect(find.text(t), findsOneWidget);
    }
  });
}
