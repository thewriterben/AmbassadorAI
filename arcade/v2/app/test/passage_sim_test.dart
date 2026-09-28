// The split that lets a When Pigs Fly run be verified by replay.
//
// The web arcade pays for results, so its server replays each run from the
// seed it issued and the taps the browser recorded. These tests pin the
// properties that has to rest on.

import 'dart:io';
import 'dart:math';

import 'package:flutter/widgets.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flame/game.dart';
import 'package:puzzle_pack/arcade/cabinet/cabinet.dart';
import 'package:puzzle_pack/arcade/passage/abilities.dart';
import 'package:puzzle_pack/arcade/passage/boar.dart';
import 'package:puzzle_pack/arcade/passage/passage_game.dart';
import 'package:puzzle_pack/arcade/passage/sim/boar_body.dart';
import 'package:puzzle_pack/arcade/passage/sim/dmath.dart';

const _size = Size(400, 800);

/// Plays a whole run the way a person would: taps when the boar is below the
/// next opening and falling, fires abilities when they are live. Frame time
/// jitters between 1/144 and 1/30 s, so the run crosses every frame-rate
/// case the accumulator has to handle.
PassageGame _play({required int seed, List<EquippedAbility> loadout = const [], int jitterSeed = 1, Size? fixed}) {
  final run = CabinetRun();
  final g = PassageGame(run: run, seed: seed, loadout: loadout, fixedSize: fixed)
    ..onGameResize(Vector2(_size.width, _size.height));
  final jitter = Random(jitterSeed);
  // Hover a moment first: idle ticks are part of the transcript.
  for (var i = 0; i < 20; i++) {
    g.update(1 / 60);
  }
  g.flap();
  var frames = 0;
  while (!run.ended && frames++ < 20000) {
    final dt = [1 / 144, 1 / 120, 1 / 60, 1 / 60, 1 / 45, 1 / 30][jitter.nextInt(6)];
    g.update(dt);
    final target = g.nextGapY ?? g.sim.h * 0.5;
    if (g.boarY > target + g.sim.h * 0.02 && g.boarVy > -g.sim.h * 0.1) g.flap();
    for (var i = 0; i < g.slots.length; i++) {
      if (jitter.nextInt(40) == 0) g.useAbility(i);
    }
  }
  expect(run.ended, isTrue, reason: 'the bot should always finish a run');
  return g;
}

PassageReplayResult _replay(PassageGame g, {Size size = _size}) {
  final spec = BoarSpec.all[g.stage]!;
  return PassageSim.replay(
    w: size.width,
    h: size.height,
    seed: g.simSeed,
    bodyRadiusK: spec.bodyRadius,
    bodyHalfLengthK: spec.bodyHalfLength,
    loadout: [for (final s in g.slots) s.ability],
    inputs: g.sim.inputs,
  );
}

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  test('a replay of the recorded taps reaches the live result exactly', () {
    for (final seed in [1, 7, 42, 2026, 99991]) {
      final g = _play(seed: seed, jitterSeed: seed);
      expect(g.sim.tainted, isFalse);
      final r = _replay(g);
      expect(r.ok, isTrue, reason: 'seed $seed: ${r.error}');
      expect(r.score, g.score, reason: 'seed $seed');
      expect(r.stars, g.stars, reason: 'seed $seed');
      expect(r.erasReached, g.erasReached, reason: 'seed $seed');
      expect(r.ticks, g.sim.ticks, reason: 'seed $seed');
      expect(r.softLanding, g.softLanding, reason: 'seed $seed');
    }
  });

  test('frame rate changes how a run is drawn, never where it goes', () {
    // Same seed, same bot, very different frame timing: the bot's taps land
    // on different ticks so the runs differ — but each replays exactly.
    for (final j in [3, 4, 5]) {
      final g = _play(seed: 1234, jitterSeed: j);
      final r = _replay(g);
      expect(r.ok, isTrue);
      expect(r.score, g.score);
    }
  });

  test('abilities replay too', () {
    const loadouts = [
      [EquippedAbility(AbilityKind.dash, 3), EquippedAbility(AbilityKind.grapple, 2)],
      [EquippedAbility(AbilityKind.teleport, 3), EquippedAbility(AbilityKind.freeze, 1)],
      [EquippedAbility(AbilityKind.tractor, 2), EquippedAbility(AbilityKind.dash, 1)],
    ];
    for (var k = 0; k < loadouts.length; k++) {
      final g = _play(seed: 500 + k, loadout: loadouts[k], jitterSeed: 50 + k);
      expect(g.sim.inputs.any((i) => i[1] != SimInput.flap), isTrue, reason: 'the bot should fire an ability');
      final r = _replay(g);
      expect(r.ok, isTrue, reason: '${r.error}');
      expect(r.score, g.score);
    }
  });

  test('the web arcade size is fixed whatever the canvas', () {
    const fixed = Size(450, 800);
    final g = _play(seed: 77, fixed: fixed);
    expect(g.sim.w, fixed.width);
    expect(g.sim.h, fixed.height);
    final r = _replay(g, size: fixed);
    expect(r.ok, isTrue);
    expect(r.score, g.score);
  });

  test('a transcript is refused on the wrong seed, the wrong body, or with an extra tap', () {
    final g = _play(seed: 31337);
    final spec = BoarSpec.all[g.stage]!;
    PassageReplayResult again({int? seed, double? bodyK, List<List<int>>? inputs}) => PassageSim.replay(
          w: _size.width,
          h: _size.height,
          seed: seed ?? g.simSeed,
          bodyRadiusK: bodyK ?? spec.bodyRadius,
          bodyHalfLengthK: spec.bodyHalfLength,
          loadout: const [],
          inputs: inputs ?? g.sim.inputs,
        );
    expect(again().ok, isTrue);
    // A different seed builds a different passage; the same taps then earn a
    // different score even when nothing is outright refused.
    final other = again(seed: 31338);
    expect(other.ok && other.score == g.score && other.ticks == g.sim.ticks, isFalse);
    // A tap after the run finished did nothing, so it cannot be in a real
    // transcript.
    final extra = [...g.sim.inputs, [g.sim.ticks + 10, SimInput.flap]];
    expect(again(inputs: extra).ok, isFalse);
    // An ability the loadout does not have.
    final forged = [...g.sim.inputs]..insert(1, [g.sim.inputs[1][0], SimInput.ability0]);
    expect(again(inputs: forged).ok, isFalse);
    // Out of order.
    final shuffled = [...g.sim.inputs.reversed];
    expect(again(inputs: shuffled).ok, isFalse);
  });

  test('DEV and test shortcuts taint the run', () {
    final g = PassageGame(run: CabinetRun(), seed: 5)..onGameResize(Vector2(_size.width, _size.height));
    g.update(1 / 60);
    expect(g.sim.tainted, isFalse);
    g.devMaxMomentum();
    expect(g.sim.tainted, isTrue);
  });

  test('the exact sine agrees with dart:math to well past what the game can show', () {
    var worst = 0.0;
    for (var i = -20000; i <= 20000; i++) {
      final x = i * 0.00731;
      worst = max(worst, (dsin(x) - sin(x)).abs());
      worst = max(worst, (dcos(x) - cos(x)).abs());
    }
    expect(worst, lessThan(1e-12));
    expect(easeOut(0.3), closeTo(1 - pow(0.7, 3), 1e-15));
  });

  test('the server-side body table matches the boar sheets', () {
    for (final s in BoarStage.values) {
      final spec = BoarSpec.all[s]!;
      final body = BoarBody.byStageId[s.name]!;
      expect(body.radius, spec.bodyRadius, reason: s.name);
      expect(body.halfLength, spec.bodyHalfLength, reason: s.name);
    }
    expect(BoarBody.byStageId.length, BoarStage.values.length);
  });

  test('the simulation is pure Dart: no Flutter, Flame or dart:ui', () {
    for (final f in Directory('lib/arcade/passage/sim').listSync().whereType<File>()) {
      final src = f.readAsStringSync();
      for (final banned in ['package:flutter', 'package:flame', 'dart:ui', 'dart:io']) {
        expect(src.contains(banned), isFalse, reason: '${f.path} imports $banned');
      }
      // No transcendental functions from dart:math inside the simulation.
      expect(RegExp(r'(?<![d\w])(sin|cos|pow|tan|exp|log)\(').hasMatch(src.replaceAll(RegExp(r'//.*'), '')), isFalse,
          reason: '${f.path} uses a platform maths function');
    }
    final eras = File('lib/arcade/passage/eras.dart').readAsStringSync();
    expect(eras.contains('package:flutter'), isFalse, reason: 'the simulation imports eras.dart');
  });
}
