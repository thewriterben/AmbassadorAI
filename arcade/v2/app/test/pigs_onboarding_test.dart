import 'package:flame/game.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/cabinet/cabinet.dart';
import 'package:puzzle_pack/arcade/passage/passage_game.dart';
import 'package:puzzle_pack/arcade/passage/pigs_onboarding.dart';
import 'package:puzzle_pack/arcade/passage/sim/passage_sim.dart' show PassageTuning;
import 'package:shared_preferences/shared_preferences.dart';

/// A player's first runs ease in to the standard passage, and count.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  group('the ease-in', () {
    test('the first run flies at the easier numbers, the fourth at the standard ones', () {
      final first = PassageTuning.forRun(0);
      const e = PassageTuning.easy, s = PassageTuning.standard;
      expect((first.gapFracStart, first.gapFracEnd, first.speedBase, first.speedRamp, first.reserve),
          (e.gapFracStart, e.gapFracEnd, e.speedBase, e.speedRamp, e.reserve));
      expect(identical(PassageTuning.forRun(3), s), isTrue);
      expect(identical(PassageTuning.forRun(40), s), isTrue);
    });

    test('each run is harder than the last, in every knob, and never harder than standard', () {
      final runs = [for (var n = 0; n <= PassageTuning.introRuns; n++) PassageTuning.forRun(n)];
      for (var i = 1; i < runs.length; i++) {
        final a = runs[i - 1], b = runs[i];
        expect(b.gapFracStart, lessThan(a.gapFracStart), reason: 'run ${i + 1} openings');
        expect(b.gapFracEnd, lessThan(a.gapFracEnd));
        expect(b.speedBase, greaterThan(a.speedBase));
        expect(b.speedRamp, greaterThan(a.speedRamp));
        expect(b.reserve, lessThanOrEqualTo(a.reserve));
      }
      const s = PassageTuning.standard;
      for (final t in runs) {
        expect(t.gapFracEnd, greaterThanOrEqualTo(s.gapFracEnd));
        expect(t.reserve, greaterThanOrEqualTo(s.reserve));
      }
    });

    test('ease-in runs count; the DEV easy variant does not', () {
      for (var n = 0; n < PassageTuning.introRuns; n++) {
        final t = PassageTuning.forRun(n);
        expect(t.fair, isTrue);
        final g = PassageGame(run: CabinetRun(), seed: 7, tuning: t)..onGameResize(Vector2(412, 892));
        expect(g.sim.tainted, isFalse, reason: '${t.id} is the real game');
      }
      final dev = PassageGame(run: CabinetRun(), seed: 7, tuning: PassageTuning.easy)..onGameResize(Vector2(412, 892));
      expect(dev.sim.tainted, isTrue);
    });

    test('a tuning is rebuilt from its id, for a replay', () {
      for (var n = 0; n < PassageTuning.introRuns; n++) {
        final t = PassageTuning.forRun(n);
        final back = PassageTuning.byId(t.id)!;
        expect((back.gapFracStart, back.gapFracEnd, back.speedBase, back.speedRamp, back.reserve, back.fair),
            (t.gapFracStart, t.gapFracEnd, t.speedBase, t.speedRamp, t.reserve, t.fair));
      }
      expect(identical(PassageTuning.byId('standard'), PassageTuning.standard), isTrue);
      expect(PassageTuning.byId('intro9'), isNull);
      expect(PassageTuning.byId('turbo'), isNull);
    });
  });

  group('the run count', () {
    setUp(() => SharedPreferences.setMockInitialValues({}));

    test('a finished run steps the next one on, up to standard, and is saved', () async {
      PigsOnboarding.resetForTest();
      expect(PigsOnboarding.tuning.id, 'intro1');
      final g = PassageGame(run: CabinetRun(), seed: 7, tuning: PigsOnboarding.tuning)..onGameResize(Vector2(412, 892));
      g.flap();
      g.devEndShort();
      var t = 0.0;
      while (t < 30 && !g.run.ended) {
        g.update(1 / 60);
        t += 1 / 60;
      }
      expect(g.run.ended, isTrue);
      expect(PigsOnboarding.runsFinished, 1);
      expect(PigsOnboarding.tuning.id, 'intro2', reason: 'the next run eases on at once');
      PigsOnboarding.recordRun();
      PigsOnboarding.recordRun();
      PigsOnboarding.recordRun();
      expect(PigsOnboarding.runsFinished, PassageTuning.introRuns, reason: 'the count stops at the end of the ease-in');
      expect(identical(PigsOnboarding.tuning, PassageTuning.standard), isTrue);
      await pumpEventQueue();
      final p = await SharedPreferences.getInstance();
      expect(p.getInt('pigs.runsFinished'), PassageTuning.introRuns);
    });
  });
}
