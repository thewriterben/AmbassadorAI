import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:puzzle_pack/theme.dart';

/// Regression cover for the v1.0.1 fix.
///
/// `showModalBottomSheet` does not inset its child for system UI, so both
/// sheets in Coin Quest — the level sheet and the end-of-run sheet — had their
/// bottom edge under the navigation bar, with the Play button sitting on the
/// gesture pill. Both now take their margin from [AppTheme.sheetMargin].
///
/// This is the cheapest place to hold the behaviour still. Driving a real
/// sheet on a device proves it once; this proves the arithmetic every run, and
/// would fail if someone "simplified" it back to a constant.
void main() {
  Future<EdgeInsets> marginUnder(WidgetTester tester, EdgeInsets viewPadding) async {
    late EdgeInsets captured;
    await tester.pumpWidget(
      MediaQuery(
        data: MediaQueryData(viewPadding: viewPadding),
        child: Builder(
          builder: (context) {
            captured = AppTheme.sheetMargin(context);
            return const SizedBox.shrink();
          },
        ),
      ),
    );
    return captured;
  }

  testWidgets('leaves room for the navigation bar', (tester) async {
    final margin = await marginUnder(tester, const EdgeInsets.only(bottom: 48));
    expect(margin.bottom, 16 + 48, reason: 'the sheet must clear the nav bar');
    expect(margin.left, 16);
    expect(margin.right, 16);
    expect(margin.top, 16);
  });

  testWidgets('falls back to a plain margin with no inset', (tester) async {
    final margin = await marginUnder(tester, EdgeInsets.zero);
    expect(margin, const EdgeInsets.all(16),
        reason: 'no system inset should mean no extra padding');
  });

  testWidgets('a taller gesture inset pushes the sheet further up', (tester) async {
    final small = await marginUnder(tester, const EdgeInsets.only(bottom: 24));
    final large = await marginUnder(tester, const EdgeInsets.only(bottom: 64));
    expect(large.bottom, greaterThan(small.bottom));
  });
}
