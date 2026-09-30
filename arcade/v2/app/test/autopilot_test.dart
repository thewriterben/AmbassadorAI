import 'package:flame/game.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/cabinet/cabinet.dart';
import 'package:puzzle_pack/arcade/passage/boar.dart';
import 'package:puzzle_pack/arcade/passage/eras.dart';
import 'package:puzzle_pack/arcade/passage/passage_game.dart';

/// The DEV autopilot (`sim/autopilot.dart`) flies a whole passage, every era
/// to the landing, for each boar and several layouts. It is what the phone
/// checks of a full run rely on, so if it stops getting through, those
/// checks quietly stop reaching the later eras.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  final size = Vector2(412, 892);

  tearDown(() => PassageGame.devAutopilot = false);

  for (final stage in BoarStage.values) {
    for (final seed in [3, 7, 11, 42]) {
      test('$stage, seed $seed: flies every era and lands after a passage flown', () {
        PassageGame.devAutopilot = true;
        final run = CabinetRun();
        final g = PassageGame(run: run, seed: seed, stage: stage)..onGameResize(size);
        g.flap();
        final f = BoarSpec.all[stage]!.frames;
        var landedGlad = false, t = 0.0;
        while (t < 240 && !run.ended) {
          g.update(1 / 60);
          t += 1 / 60;
          if (g.phase == PassagePhase.down && g.boarFrame == f.landWin) landedGlad = true;
        }
        expect(g.sim.erasCleared, eras.length, reason: 'stopped in ${eras[g.sim.eraIndex].year}');
        // It flies clean (30 of 30 layouts did, when written): a strike
        // means the rule has started to cut it fine, well before it fails.
        expect(g.sim.reserve, g.sim.tuning.reserve, reason: 'no pillar struck');
        expect(landedGlad, isTrue, reason: 'the landing after a passage flown');
        expect(g.sim.tainted, isTrue, reason: 'an autopilot run is not a player\'s');
      });
    }
  }
}
