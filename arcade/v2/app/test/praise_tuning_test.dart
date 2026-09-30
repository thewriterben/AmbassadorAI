import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/audio.dart';

/// The spoken-affirmation tuning knobs.
///
/// These exist because the DGD embed suppresses the winner line (§4.3), which
/// is the line a player would otherwise hear most — so cascade praise carries
/// the whole spoken layer inside the app, and its thresholds stopped being an
/// implementation detail.
///
/// The thresholds used to be literals at two call sites in `match3_game.dart`,
/// held in step by a comment. These tests pin the properties that comment was
/// asserting, so a future edit fails here rather than silently desynchronising
/// the real cascade from the DEV-forced one.
void main() {
  test('praise fires below the big-praise threshold', () {
    // If these ever crossed, the ordinary affirmation would be unreachable:
    // every qualifying cascade would take the `big` branch.
    expect(Audio.praiseCombo, lessThan(Audio.praiseBigCombo));
  });

  test('a cascade can actually reach the thresholds on a small board', () {
    // Level 1 is 7x7. A chain deeper than about five is vanishingly rare
    // there, and the embed was near-silent at 4/6. Anything above this is a
    // tuning regression for early levels, which is where first impressions
    // are formed.
    expect(Audio.praiseCombo, lessThanOrEqualTo(3));
    expect(Audio.praiseBigCombo, lessThanOrEqualTo(5));
  });

  test('praise is still rate-limited enough to stay an event', () {
    // The lower bound is the point of the limiter: an affirmation on every
    // chain stops being one. The upper bound is what made the embed quiet.
    expect(Audio.praiseGapMs, greaterThanOrEqualTo(3000));
    expect(Audio.praiseGapMs, lessThanOrEqualTo(5000));
  });

  test('the winner line stays gated on the embed flag', () {
    // Not a tuning knob. This is the §4.3 suppression, and loosening praise
    // must not be mistaken for permission to bring the winner line back.
    // `inAppTab` is false in a plain test run, which is the standalone build.
    expect(Audio.inAppTab, isFalse, reason: 'test runs are standalone; the embed sets DGD_APP_TAB=true');
  });
}
