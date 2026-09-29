part of 'passage_game.dart';

/// The gates, built from the materials of the era they stand in, so the
/// passage belongs to the city behind it (see `city.dart`):
///
/// | Era  | Gate                                             |
/// |------|--------------------------------------------------|
/// | 1816 | Fluted Portland-stone columns                    |
/// | 1873 | Cast-iron columns with bands and a flared head   |
/// | 1913 | Riveted steel I-beams with lattice bracing       |
/// | 1923 | Brick factory chimneys, sooty at the mouth       |
/// | 1933 | Art Deco pillars, brass flutes and a chevron     |
/// | 1944 | Timber posts bound with iron straps              |
/// | 1971 | White marble columns                             |
/// | 1979 | Board-marked concrete                            |
/// | 2009 | Dark glass with cyan edge light and circuit      |
///
/// What does not change, whatever the material: the collision rectangle
/// (these are drawn inside it, never beyond it), the amber lip at the
/// opening — still the one thing that says where the gap is at a glance —
/// and a body lighter than the skyline behind, so a gate never sinks into
/// the city. Each gate is drawn once into a cached [Picture].
extension PassageGates on PassageGame {
  Picture _gatePicture(SimGate g) {
    final rec = PictureRecorder();
    final c = Canvas(rec);
    final top = g.gapY - g.gapH / 2, bottom = g.gapY + g.gapH / 2;
    _gateBlock(c, g.era, -_h * 0.1, top, capAtEnd: true);
    _gateBlock(c, g.era, bottom, _h * 1.1, capAtEnd: false);
    final lip = _h * 0.0045;
    final cap = Paint()..color = AppTheme.accent.withValues(alpha: 0.8);
    c.drawRect(Rect.fromLTRB(0, top - lip, _gateW, top), cap);
    c.drawRect(Rect.fromLTRB(0, bottom, _gateW, bottom + lip), cap);
    return rec.endRecording();
  }

  /// One half of a gate, from [y0] to [y1]. The capital (or cornice, or
  /// plate) is at the end facing the opening: [y1] for the upper half.
  void _gateBlock(Canvas c, int era, double y0, double y1, {required bool capAtEnd}) {
    // The owner's drawn column, where the era has one (see `backdrop.dart`).
    if (_backdrop.drawColumn(c, era, y0, y1, _gateW, capAtEnd: capAtEnd)) return;
    final gw = _gateW;
    final capY = capAtEnd ? y1 : y0;
    final into = capAtEnd ? -1.0 : 1.0; // from the cap into the body
    final u = _h * 0.01; // a unit of height

    // Lit from the left, like everything else in the game. Stops default to
    // even spacing: dart:ui insists on them for more than two colours.
    Paint shade(List<Color> cols, [List<double>? stops, double inset = 0]) => Paint()
      ..shader = Gradient.linear(Offset(gw * inset, 0), Offset(gw * (1 - inset), 0), cols,
          stops ?? [for (var i = 0; i < cols.length; i++) i / (cols.length - 1)]);
    Rect body(double inset) => Rect.fromLTRB(gw * inset, y0, gw * (1 - inset), y1);
    // A band of height [hgt] starting [from] units in from the cap.
    Rect band(double from, double hgt, [double inset = 0]) {
      final a = capY + into * from * u, b = capY + into * (from + hgt) * u;
      return Rect.fromLTRB(gw * inset, min(a, b), gw * (1 - inset), max(a, b));
    }

    void vlines(int n, double inset, Paint p) {
      for (var k = 1; k < n; k++) {
        final x = gw * inset + (gw * (1 - 2 * inset)) * k / n;
        c.drawLine(Offset(x, y0), Offset(x, y1), p);
      }
    }

    void hlines(double every, Paint p, [double inset = 0]) {
      for (var y = capY + into * every; capAtEnd ? y > y0 : y < y1; y += into * every) {
        c.drawLine(Offset(gw * inset, y), Offset(gw * (1 - inset), y), p);
      }
    }

    final thin = Paint()..strokeWidth = 1;

    // Texture loops step past the ends of a block; clipped here, nothing a
    // gate draws can spill into the opening. (The steel lattice did, on the
    // first render, as two stray lines hanging under the girder.)
    c.save();
    c.clipRect(Rect.fromLTRB(0, min(y0, y1), gw, max(y0, y1)));
    switch (era) {
      case 0: // Portland stone
        c.drawRect(body(0.1), shade(const [Color(0xFF6F6A5E), Color(0xFFD2CBB6), Color(0xFF8B8576), Color(0xFF5E5A50)], const [0, 0.35, 0.7, 1], 0.1));
        vlines(5, 0.1, thin..color = const Color(0x22000000));
        hlines(u * 7, thin..color = const Color(0x18000000), 0.1);
        c.drawRect(band(0, 1.1), shade(const [Color(0xFF8A8475), Color(0xFFE2DBC6), Color(0xFF7A7568)]));
        c.drawRect(band(1.1, 0.9, 0.05), shade(const [Color(0xFF7A7568), Color(0xFFCFC8B3), Color(0xFF6A665A)]));
        final vy = capY + into * 1.6 * u;
        final volute = Paint()
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1.2
          ..color = const Color(0xFF5E5A50);
        c.drawCircle(Offset(gw * 0.12, vy), gw * 0.08, volute);
        c.drawCircle(Offset(gw * 0.88, vy), gw * 0.08, volute);
      case 1: // cast iron
        c.drawRect(body(0.14), shade(const [Color(0xFF26322C), Color(0xFF647A6C), Color(0xFF34423A), Color(0xFF1C2420)], const [0, 0.35, 0.7, 1], 0.14));
        for (var k = 6; k < 200; k += 10) {
          final r = band(k.toDouble(), 0.7, 0.1);
          if (r.top > max(y0, y1) || r.bottom < min(y0, y1)) break;
          c.drawRect(r, shade(const [Color(0xFF3A4A42), Color(0xFF8AA092), Color(0xFF2E3A34)]));
        }
        // Flared head: a trapezoid from the shaft out to the full width.
        final a = capY + into * 0.8 * u, b = capY + into * 2.6 * u;
        c.drawPath(
          Path()
            ..moveTo(0, a)
            ..lineTo(gw, a)
            ..lineTo(gw * 0.86, b)
            ..lineTo(gw * 0.14, b)
            ..close(),
          shade(const [Color(0xFF34423A), Color(0xFF7C9486), Color(0xFF26322C)]),
        );
        c.drawRect(band(0, 0.8), shade(const [Color(0xFF3A4A42), Color(0xFF94AA9C), Color(0xFF2E3A34)]));
        c.drawCircle(Offset(gw / 2, capY + into * 1.7 * u), gw * 0.09, Paint()..color = const Color(0xFFB4C8BA));
      case 2: // riveted steel I-beam
        c.drawRect(body(0), shade(const [Color(0xFF3A4450), Color(0xFF6E7A88), Color(0xFF444E5A)]));
        final flange = shade(const [Color(0xFF5A6674), Color(0xFFA2AEBC), Color(0xFF5A6674)]);
        c.drawRect(Rect.fromLTRB(0, y0, gw * 0.18, y1), flange);
        c.drawRect(Rect.fromLTRB(gw * 0.82, y0, gw, y1), flange);
        // Lattice bracing across the web.
        final brace = Paint()
          ..strokeWidth = 1.4
          ..color = const Color(0xFF8C98A6);
        final step = u * 6;
        for (var y = min(y0, y1); y < max(y0, y1); y += step) {
          c.drawLine(Offset(gw * 0.2, y), Offset(gw * 0.8, y + step), brace);
          c.drawLine(Offset(gw * 0.8, y), Offset(gw * 0.2, y + step), brace);
        }
        final rivet = Paint()..color = const Color(0xFFCAD4DE);
        for (var y = min(y0, y1) + u; y < max(y0, y1); y += u * 2) {
          c.drawCircle(Offset(gw * 0.09, y), 0.9, rivet);
          c.drawCircle(Offset(gw * 0.91, y), 0.9, rivet);
        }
        c.drawRect(band(0, 1.2), shade(const [Color(0xFF6E7A88), Color(0xFFB4C0CC), Color(0xFF5A6674)]));
        for (final x in [0.2, 0.4, 0.6, 0.8]) {
          c.drawCircle(Offset(gw * x, capY + into * 0.6 * u), 1.0, rivet);
        }
      case 3: // brick chimney
        c.drawRect(body(0), shade(const [Color(0xFF4E2419), Color(0xFF9A4E36), Color(0xFF5E2C1F)]));
        final mortar = Paint()
          ..strokeWidth = 0.8
          ..color = const Color(0x66200E08);
        final bh = u * 1.3;
        var row = 0;
        for (var y = min(y0, y1); y < max(y0, y1); y += bh, row++) {
          c.drawLine(Offset(0, y), Offset(gw, y), mortar);
          final off = row.isEven ? 0.0 : gw * 0.2;
          for (var x = off + gw * 0.4; x < gw; x += gw * 0.4) {
            c.drawLine(Offset(x, y), Offset(x, y + bh), mortar);
          }
        }
        // Soot at the mouth, and an iron band below it.
        final sootA = capY, sootB = capY + into * 7 * u;
        c.drawRect(
          Rect.fromLTRB(0, min(sootA, sootB), gw, max(sootA, sootB)),
          Paint()
            ..shader = Gradient.linear(Offset(0, sootA), Offset(0, sootB), const [Color(0xAA0E0806), Color(0x000E0806)]),
        );
        c.drawRect(band(4.5, 0.6), Paint()..color = const Color(0xFF2A2A2E));
        c.drawRect(band(0, 1.4), shade(const [Color(0xFF3E1A12), Color(0xFF7A3A28), Color(0xFF3E1A12)]));
      case 4: // Art Deco
        c.drawRect(body(0.06), shade(const [Color(0xFF2E2634), Color(0xFF7A6C84), Color(0xFF3E3446), Color(0xFF241E2A)], const [0, 0.35, 0.7, 1], 0.06));
        vlines(4, 0.06, thin..color = const Color(0x99C9A24A));
        // Chevron near the head, in brass.
        final ch = Path();
        final cy = capY + into * 3.2 * u;
        for (var k = 0; k <= 4; k++) {
          final x = gw * (0.06 + 0.88 * k / 4);
          final y = cy + (k.isEven ? 0 : into * 1.1 * u);
          k == 0 ? ch.moveTo(x, y) : ch.lineTo(x, y);
        }
        c.drawPath(
          ch,
          Paint()
            ..style = PaintingStyle.stroke
            ..strokeWidth = 1.5
            ..color = const Color(0xFFD6B058),
        );
        c.drawRect(band(0, 0.9), shade(const [Color(0xFF8A6A2A), Color(0xFFE6C470), Color(0xFF7A5A20)]));
        c.drawRect(band(0.9, 0.8, 0.12), shade(const [Color(0xFF3E3446), Color(0xFF8A7C94), Color(0xFF2E2634)]));
      case 5: // timber, iron-strapped
        c.drawRect(body(0.1), shade(const [Color(0xFF3E2816), Color(0xFF8A5E36), Color(0xFF4E341E)], null, 0.1));
        final grain = Paint()
          ..style = PaintingStyle.stroke
          ..strokeWidth = 0.9
          ..color = const Color(0x40200E04);
        for (final gx in [0.28, 0.5, 0.7]) {
          final p = Path();
          for (var y = min(y0, y1); y < max(y0, y1); y += 4) {
            final x = gw * gx + sin(y * 0.05 + gx * 9) * 1.4;
            y == min(y0, y1) ? p.moveTo(x, y) : p.lineTo(x, y);
          }
          c.drawPath(p, grain);
        }
        final strap = Paint()..color = const Color(0xFF2C2C30);
        final bolt = Paint()..color = const Color(0xFF8A8A90);
        for (var k = 3; k < 200; k += 12) {
          final r = band(k.toDouble(), 0.9, 0.06);
          if (r.top > max(y0, y1) || r.bottom < min(y0, y1)) break;
          c.drawRect(r, strap);
          c.drawCircle(r.center, 0.9, bolt);
        }
        c.drawRect(band(0, 1.3), shade(const [Color(0xFF5A5650), Color(0xFF9A948A), Color(0xFF4A4640)]));
      case 6: // white marble
        c.drawRect(body(0.1), shade(const [Color(0xFF8E8E8A), Color(0xFFF0EFE8), Color(0xFFB8B7B0), Color(0xFF7D7C77)], const [0, 0.35, 0.7, 1], 0.1));
        vlines(6, 0.1, thin..color = const Color(0x1C000000));
        c.drawRect(band(0, 1.0), shade(const [Color(0xFFA8A7A0), Color(0xFFF6F5EE), Color(0xFF9A9992)]));
        c.drawRect(band(1.0, 0.6, 0.06), shade(const [Color(0xFF9A9992), Color(0xFFE6E5DE), Color(0xFF8A8982)]));
      case 7: // board-marked concrete
        c.drawRect(body(0), shade(const [Color(0xFF5E5C56), Color(0xFF96938A), Color(0xFF6E6C66)]));
        hlines(u * 1.8, thin..color = const Color(0x1E000000));
        // Rain stains running from the head.
        for (final sx in [0.25, 0.62]) {
          final a = capY, b = capY + into * 9 * u;
          c.drawRect(
            Rect.fromLTRB(gw * sx, min(a, b), gw * (sx + 0.08), max(a, b)),
            Paint()
              ..shader = Gradient.linear(Offset(0, a), Offset(0, b), const [Color(0x33000000), Color(0x00000000)]),
          );
        }
        c.drawRect(band(0, 1.6), shade(const [Color(0xFF6E6C66), Color(0xFFA6A39A), Color(0xFF5E5C56)]));
      default: // glass and light
        c.drawRect(body(0.1), shade(const [Color(0xFF14242E), Color(0xFF2E5468), Color(0xFF162834)], null, 0.1));
        final edge = Paint()
          ..strokeWidth = 1.5
          ..color = const Color(0xCC7FE0FF);
        c.drawLine(Offset(gw * 0.1, y0), Offset(gw * 0.1, y1), edge);
        c.drawLine(Offset(gw * 0.9, y0), Offset(gw * 0.9, y1), edge);
        final trace = Paint()
          ..strokeWidth = 1
          ..color = const Color(0x807FE0FF);
        c.drawLine(Offset(gw * 0.5, y0), Offset(gw * 0.5, y1), trace);
        for (var y = min(y0, y1) + u * 3; y < max(y0, y1); y += u * 7) {
          final right = ((y / u).round() % 2) == 0;
          final ex = gw * (right ? 0.76 : 0.24);
          c.drawLine(Offset(gw * 0.5, y), Offset(ex, y), trace);
          c.drawCircle(Offset(ex, y), 1.3, Paint()..color = const Color(0xCC7FE0FF));
        }
        c.drawRect(band(0, 0.9), Paint()..color = const Color(0xFF7FE0FF).withValues(alpha: 0.55));
    }
    c.restore();
  }
}
