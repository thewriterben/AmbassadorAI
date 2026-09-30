import 'package:flame/game.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/cabinet/cabinet.dart';
import 'package:puzzle_pack/arcade/passage/boar.dart';
import 'package:puzzle_pack/arcade/passage/eras.dart';
import 'package:puzzle_pack/arcade/passage/passage_game.dart';
import 'package:puzzle_pack/arcade/passage/sim/autopilot.dart';

/// The DEV autopilot (`sim/autopilot.dart`) flies a whole passage, every era
/// to the landing, for each boar and several layouts. It is what the phone
/// checks of a full run rely on, so if it stops getting through, those
/// checks quietly stop reaching the later eras.
///
/// The game's own hook runs the rule only in a DEV build (it is compiled out
/// of a store build; review E2, 2026-09-30), and tests are not DEV builds. So
/// the test applies the same rule the same way: decided before every tick,
/// tapping through the sim's flap(), one tick per update.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  final size = Vector2(412, 892);

  for (final stage in BoarStage.values) {
    for (final seed in [3, 7, 11, 42]) {
      test('$stage, seed $seed: flies every era and lands after a passage flown', () {
        final run = CabinetRun();
        final g = PassageGame(run: run, seed: seed, stage: stage)..onGameResize(size);
        g.flap();
        final f = BoarSpec.all[stage]!.frames;
        var landedGlad = false, t = 0.0;
        while (t < 240 && !run.ended) {
          if (g.sim.started && Autopilot.wantsFlap(g.sim)) g.sim.flap();
          g.update(PassageSim.step);
          t += PassageSim.step;
          if (g.phase == PassagePhase.down && g.boarFrame == f.landWin) landedGlad = true;
        }
        expect(g.sim.erasCleared, eras.length, reason: 'stopped in ${eras[g.sim.eraIndex].year}');
        // It flies clean (30 of 30 layouts did, when written): a strike
        // means the rule has started to cut it fine, well before it fails.
        expect(g.sim.reserve, g.sim.tuning.reserve, reason: 'no pillar struck');
        expect(landedGlad, isTrue, reason: 'the landing after a passage flown');
      });
    }
  }

  test('the in-game autopilot is DEV-only: a store build ignores the switch', () {
    PassageGame.devAutopilot = true;
    addTearDown(() => PassageGame.devAutopilot = false);
    final run = CabinetRun();
    final g = PassageGame(run: run, seed: 3, stage: BoarStage.piglet)..onGameResize(size);
    g.flap();
    for (var i = 0; i < 600; i++) {
      g.update(PassageSim.step);
    }
    expect(g.sim.tainted, isFalse, reason: 'the hook flew, and tainted, a non-DEV run');
  });
}
