// Leaving a level mid-cascade must not strand the board in memory.
//
// The cascade loop in Match3Game is a chain of `await`s on completers handed out
// by GemComponent. A Flame effect's onComplete never fires if the component is
// removed while the effect is in flight, so before this fix those awaits never
// resumed: the loop stayed suspended forever, holding the game, the board and
// every sprite alive. Quitting five levels mid-cascade leaked five boards.
//
// This asserts the contract the fix rests on — every future GemComponent hands
// out completes when the component is removed, whether or not its effect ran.
import 'dart:async';
import 'dart:ui' as ui;

import 'package:flame/components.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/match3/game/match3_game.dart';
import 'package:puzzle_pack/match3/model/gem.dart';

Future<ui.Image> _pixel() {
  final recorder = ui.PictureRecorder();
  Canvas(recorder).drawRect(const Rect.fromLTWH(0, 0, 1, 1), Paint());
  return recorder.endRecording().toImage(1, 1);
}

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late GemComponent gem;

  setUp(() async {
    gem = GemComponent(
      gem: Gem(GemKind.gold),
      sprite: Sprite(await _pixel()),
      pos: const Pos(0, 0),
      position: Vector2.zero(),
      size: Vector2.all(10),
    );
  });

  // Durations are long enough that nothing can complete on its own in-test.
  test('moveTo completes when the component is removed mid-flight', () async {
    var done = false;
    unawaited(gem.moveTo(Vector2.all(100), 30).then((_) => done = true));
    await Future<void>.delayed(Duration.zero);
    expect(done, isFalse);

    gem.onRemove();
    await Future<void>.delayed(Duration.zero);
    expect(done, isTrue, reason: 'the cascade loop would never resume');
  });

  test('pop completes when the component is removed mid-flight', () async {
    var done = false;
    unawaited(gem.pop().then((_) => done = true));

    gem.onRemove();
    await Future<void>.delayed(Duration.zero);
    expect(done, isTrue);
  });

  test('pulse completes when the component is removed mid-flight', () async {
    var done = false;
    unawaited(gem.pulse().then((_) => done = true));

    gem.onRemove();
    await Future<void>.delayed(Duration.zero);
    expect(done, isTrue);
  });

  test('several pending futures settle, and removing twice does not throw', () async {
    var n = 0;
    for (var i = 0; i < 4; i++) {
      unawaited(gem.moveTo(Vector2.all(100), 30).then((_) => n++));
    }
    gem.onRemove();
    gem.onRemove(); // must not complete an already-completed completer
    await Future<void>.delayed(Duration.zero);
    expect(n, 4);
  });
}
