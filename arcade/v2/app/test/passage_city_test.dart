import 'dart:ui';

import 'package:flame/game.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/cabinet/cabinet.dart';
import 'package:puzzle_pack/arcade/passage/city.dart';
import 'package:puzzle_pack/arcade/passage/eras.dart';
import 'package:puzzle_pack/arcade/passage/passage_game.dart';

/// The era skylines. What can go wrong without anyone noticing: an era with
/// no city, a gap in the skyline, a tower tall enough to crowd the top of the
/// screen, or a city that throws when first drawn.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  final size = Vector2(412, 892);

  PassageGame game({int seed = 7}) => PassageGame(run: CabinetRun(), seed: seed)..onGameResize(size);

  test('every era has a city in both layers', () {
    final city = game().city!;
    for (var layer = 0; layer < 2; layer++) {
      final eraSet = city.layerSpecs(layer).map((b) => b.era).toSet();
      expect(eraSet, containsAll(List.generate(eras.length, (i) => i)), reason: 'layer $layer');
    }
  });

  test('the skyline has no holes', () {
    final city = game().city!;
    for (var layer = 0; layer < 2; layer++) {
      final specs = city.layerSpecs(layer);
      for (var i = 1; i < specs.length; i++) {
        final prevEnd = specs[i - 1].x + specs[i - 1].w;
        expect(specs[i].x - prevEnd, lessThan(size.x * 0.03), reason: 'layer $layer, building $i');
      }
    }
  });

  test('nothing crowds the top of the screen', () {
    final city = game().city!;
    for (var layer = 0; layer < 2; layer++) {
      for (final b in city.layerSpecs(layer)) {
        expect(b.h, lessThanOrEqualTo(size.y * 0.62), reason: '${b.kind} in era ${b.era}');
      }
    }
  });

  test('Bretton Woods is mountains, pines and a hotel, not a city', () {
    final city = game().city!;
    final far = city.layerSpecs(0).where((b) => b.era == 5).map((b) => b.kind).toSet();
    final near = city.layerSpecs(1).where((b) => b.era == 5).map((b) => b.kind).toSet();
    expect(far, {BuildingKind.mountain});
    expect(near, containsAll([BuildingKind.pine, BuildingKind.hotel]));
    expect(near.difference({BuildingKind.pine, BuildingKind.hotel}), isEmpty);
  });

  test('the same seed builds the same city', () {
    final a = game(seed: 3).city!.layerSpecs(1);
    final b = game(seed: 3).city!.layerSpecs(1);
    expect(a.length, b.length);
    expect([for (final x in a) x.kind], [for (final x in b) x.kind]);
  });

  test('every era draws', () {
    final g = game();
    g.flap();
    for (var era = 0; era < eras.length; era++) {
      if (era > 0) g.devNextEra();
      for (var i = 0; i < 10; i++) {
        g.update(1 / 60);
      }
      final rec = PictureRecorder();
      g.render(Canvas(rec));
      rec.endRecording().dispose();
    }
    expect(g.eraIndex, eras.length - 1);
  });
}
