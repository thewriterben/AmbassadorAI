import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/passage/backdrop.dart';
import 'package:puzzle_pack/arcade/passage/eras.dart';

/// Drawn backdrops (`backdrop.dart`): the importer's manifest is read the
/// way it is written, and eras hand over to each other with a crossfade.
void main() {
  group('manifest', () {
    test('reads eras by year, parts by name, with the importer\'s numbers', () {
      final m = BackdropManifest.parse('''
        {"version": 1, "eras": {
          "1816": {
            "sky": {"file": "1816_sky.png", "band": 1.0},
            "far": {"file": "1816_far.png", "band": 0.45, "base": 0.86, "parallax": 0.12},
            "capital": {"file": "1816_capital.png"}
          },
          "2009": {"ground": {"file": "2009_ground.png", "band": 0.16, "lip": 0.12}}
        }}''');
      expect(m.byEra.keys, unorderedEquals([0, eras.length - 1]));
      final far = m.byEra[0]![BackdropPart.far]!;
      expect(far.file, 'backdrop/1816_far.png');
      expect((far.band, far.base, far.parallax), (0.45, 0.86, 0.12));
      expect(m.byEra[0]![BackdropPart.capital]!.file, 'backdrop/1816_capital.png');
      expect(m.byEra[eras.length - 1]![BackdropPart.ground]!.band, 0.16);
      expect(m.byEra[eras.length - 1]![BackdropPart.ground]!.lip, 0.12);
      expect(far.lip, 0, reason: 'no lip unless the manifest gives one');
    });

    test('skips a year or a part it does not know, rather than failing', () {
      final m = BackdropManifest.parse('''
        {"eras": {"1900": {"sky": {"file": "x.png"}},
                  "1816": {"clouds": {"file": "y.png"}, "mid": {"file": "1816_mid.png"}}}}''');
      expect(m.byEra.keys, [0]);
      expect(m.byEra[0]!.keys, [BackdropPart.mid]);
    });

    test('the shipped manifest parses', () {
      final text = File(BackdropManifest.path).readAsStringSync();
      expect(() => BackdropManifest.parse(text), returnsNormally);
    });

    test('with nothing drawn, every era stays code-drawn', () {
      final b = DrawnBackdrop(BackdropManifest.empty);
      expect(b.isEmpty, isTrue);
      for (var e = 0; e < eras.length; e++) {
        expect(b.hasSkyline(e), isFalse);
        expect(b.hasColumns(e), isFalse);
      }
    });
  });

  group('era crossfade', () {
    const n = 9, fade = 0.1;
    double weightOf(List<(int, double)> ws, int era) =>
        ws.where((w) => w.$1 == era).fold(0.0, (a, w) => a + w.$2);

    test('mid-era, only that era shows', () {
      expect(eraWeights(3.5, n, fade), [(3, 1.0)]);
      expect(eraWeights(0.0, n, fade), [(0, 1.0)]);
    });

    test('at the change, half each; the weights always add to one', () {
      final at = eraWeights(4.0, n, fade);
      expect(weightOf(at, 3), closeTo(0.5, 1e-9));
      expect(weightOf(at, 4), closeTo(0.5, 1e-9));
      for (var v = 0.0; v <= n - 1; v += 0.013) {
        final ws = eraWeights(v, n, fade);
        expect(ws.fold(0.0, (a, w) => a + w.$2), closeTo(1, 1e-9), reason: 'at $v');
      }
    });

    test('the new era fades in steadily across the change', () {
      var last = -1.0;
      for (var v = 4 - fade; v <= 4 + fade; v += fade / 20) {
        final w = weightOf(eraWeights(v, n, fade), 4);
        expect(w, greaterThanOrEqualTo(last - 1e-9));
        last = w;
      }
      expect(weightOf(eraWeights(4 - fade * 1.01, n, fade), 4), 0);
      expect(weightOf(eraWeights(4 + fade * 1.01, n, fade), 4), 1);
    });

    test('layers draw solid through the change: the old until halfway, the new from halfway', () {
      for (var v = 4 - fade; v <= 4 + fade; v += fade / 20) {
        final a = layerAlphas(eraWeights(v, n, fade));
        final cover = a.fold(0.0, (c, x) => c + x.$2 - c * x.$2);
        expect(cover, greaterThanOrEqualTo(1 - 1e-9), reason: 'no see-through gap at $v');
      }
      expect(layerAlphas(eraWeights(4.0, n, fade)), [(3, 1.0), (4, 1.0)]);
    });

    test('past the last era, the last era', () {
      expect(eraWeights((n - 1).toDouble(), n, fade).last.$1, n - 1);
    });
  });
}
