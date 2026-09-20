import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'package:puzzle_pack/match3/progress.dart';

/// Progression follows clears, not stars.
///
/// An objective level (seals / vaults / ingots) is won by finishing the
/// objective; its `targetScore` is only the par that star thresholds are
/// measured against. Finishing one under par is a legitimate win worth zero
/// stars, and that case used to save nothing and re-lock the level.
void main() {
  setUp(() async {
    SharedPreferences.setMockInitialValues({});
    // The singleton carries both its maps and its cached store between tests.
    await Progress.instance.resetForTest();
  });

  test('a zero-star win still unlocks the next level', () async {
    expect(Progress.instance.unlocked, 1);

    // Cleared the vault objective, scored under par: zero stars.
    await Progress.instance.record(1, 10, 0, won: true);

    expect(Progress.instance.cleared(1), isTrue);
    expect(Progress.instance.stars(1), 0);
    expect(Progress.instance.unlocked, 2, reason: 'a win must open the next level');
  });

  test('a zero-star win survives a reload', () async {
    await Progress.instance.record(1, 10, 0, won: true);
    await Progress.instance.record(2, 20, 0, won: true);

    await Progress.instance.load();

    expect(Progress.instance.unlocked, 3);
  });

  test('a loss does not unlock anything', () async {
    await Progress.instance.record(1, 5000, 3, won: false);

    expect(Progress.instance.cleared(1), isFalse);
    expect(Progress.instance.unlocked, 1);
    // A good score on a failed run is still the best score seen.
    expect(Progress.instance.best(1), 5000);
  });

  test('stars and best score only ever improve', () async {
    await Progress.instance.record(1, 900, 2, won: true);
    await Progress.instance.record(1, 100, 1, won: true);

    expect(Progress.instance.stars(1), 2);
    expect(Progress.instance.best(1), 900);
  });

  test('a save written before clears were tracked still counts', () async {
    // Old format: stars only, no m3.clear key. Written straight to the store
    // rather than through record(), which is the point — these saves predate
    // the clear flag entirely.
    final p = await SharedPreferences.getInstance();
    await p.setInt('m3.stars.1', 3);
    await p.setInt('m3.stars.2', 1);
    await Progress.instance.load();

    expect(Progress.instance.unlocked, 3);
  });

  test('unlocking stops at the first level not cleared', () async {
    await Progress.instance.record(1, 100, 1, won: true);
    // 2 skipped.
    await Progress.instance.record(3, 100, 1, won: true);

    expect(Progress.instance.unlocked, 2);
  });
}
