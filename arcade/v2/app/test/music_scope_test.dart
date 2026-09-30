import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/audio.dart';

// Music plays only inside a game, never in the arcade's menus (2026-09-29).
// Screens claim a track and give it back; with no claim the arcade is silent.
// Audio is not initialised here, so these exercise the bookkeeping only —
// which track is asked for — without touching a platform player.
void main() {
  final a = Audio.instance;

  test('the menu is silent until a game screen claims its track', () {
    expect(a.track, isNull);
  });

  test('Coin Quest: one tune from the map through its levels, silence after', () {
    final map = a.claimMusic(Audio.trackQuest);
    expect(a.track, Audio.trackQuest);

    final level1 = a.claimMusic(Audio.trackQuest);
    // "Next level" is a pushReplacement: the new level claims before the old
    // one is disposed. The tune must not drop out in between.
    final level2 = a.claimMusic(Audio.trackQuest);
    a.releaseMusic(level1);
    expect(a.track, Audio.trackQuest);

    a.releaseMusic(level2); // back on the map
    expect(a.track, Audio.trackQuest);

    a.releaseMusic(map); // back in the arcade menu
    expect(a.track, isNull);
  });

  test('When Pigs Fly: its front room and its flights share one track, then silence', () {
    final home = a.claimMusic(Audio.trackPigs);
    final flight = a.claimMusic(Audio.trackPigs); // the cabinet
    a.releaseMusic(flight);
    expect(a.track, Audio.trackPigs);
    a.releaseMusic(home);
    expect(a.track, isNull);
  });

  test('a cabinet game plays its bed only while it is open', () {
    final game = a.claimMusic(Audio.trackLevel);
    expect(a.track, Audio.trackLevel);
    a.releaseMusic(game);
    expect(a.track, isNull);
  });

  test('a claim given back twice, or out of order, cannot leave music playing in the menu', () {
    final x = a.claimMusic(Audio.trackQuest);
    final y = a.claimMusic(Audio.trackPigs);
    a.releaseMusic(x);
    a.releaseMusic(x);
    expect(a.track, Audio.trackPigs);
    a.releaseMusic(y);
    expect(a.track, isNull);
  });

  test('Quest Tune ships; the old menu, map and tension beds do not', () {
    expect(File('assets/audio/${Audio.trackQuest}').existsSync(), isTrue);
    for (final gone in ['music_menu.mp3', 'music_map.mp3', 'music_tension.mp3']) {
      expect(File('assets/audio/$gone').existsSync(), isFalse, reason: gone);
    }
  });
}
