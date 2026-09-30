/// The skylines behind When Pigs Fly: one city per era, in silhouette.
///
/// Each era of the passage has a place — London in 1816, an American city in
/// 1873, New York in 1913, Berlin in 1923, a Depression-era American city in
/// 1933, the resort at Bretton Woods in 1944, Washington in 1971, a
/// late-seventies downtown in 1979, and a glass city at night for 2009, when
/// the thing that happened did not happen anywhere in particular.
///
/// The cities are evocative, never portraits. Period architecture — gables
/// and chimney pots, mansard roofs, water towers, sawtooth factories,
/// Art Deco setbacks, brutalist blocks, glass — says where and when without
/// drawing any specific building, which is both safer (a few famous
/// buildings' likenesses are trademarked) and never wrong about a date.
///
/// Two parallax layers, a hazy far one and a darker near one, scroll slower
/// than the gates. A building takes the style of the era the player is in
/// when it passes mid-screen, so the skyline changes as the eras do, with
/// the new city rolling in from the right. Each building is drawn once into
/// a cached [Picture]; per frame the skyline is a handful of picture draws
/// plus a little smoke and a few blinking lights.
library;

import 'dart:math';
import 'dart:ui';

import 'package:flutter/foundation.dart';

enum BuildingKind { terrace, spire, dome, brick, mansard, tower, factory, deco, classical, glass, brutal, hotel, pine, mountain }

/// What an era's city is built from.
class _Style {
  /// Kinds and their weights, for the near and the far layer.
  final Map<BuildingKind, double> near, far;

  /// Chance a window is lit.
  final double lit;

  /// Fluorescent or LED light rather than lamp and gaslight.
  final bool cool;

  /// Chimneys and stacks smoke.
  final bool smoke;

  /// Water tanks on the flat roofs.
  final bool waterTanks;

  const _Style({
    required this.near,
    required this.far,
    required this.lit,
    this.cool = false,
    this.smoke = false,
    this.waterTanks = false,
  });
}

const _styles = <_Style>[
  // 1816, London: terraces with chimney pots, church spires, the odd dome.
  _Style(
    near: {BuildingKind.terrace: 0.65, BuildingKind.spire: 0.2, BuildingKind.dome: 0.08},
    far: {BuildingKind.terrace: 0.6, BuildingKind.spire: 0.28, BuildingKind.dome: 0.12},
    lit: 0.22,
    smoke: true,
  ),
  // 1873, an American city: brick blocks with cornices, mansard roofs, spires.
  _Style(
    near: {BuildingKind.brick: 0.5, BuildingKind.mansard: 0.28, BuildingKind.spire: 0.12, BuildingKind.terrace: 0.1},
    far: {BuildingKind.brick: 0.45, BuildingKind.mansard: 0.3, BuildingKind.spire: 0.25},
    lit: 0.28,
    smoke: true,
  ),
  // 1913, New York: brick with water tanks, and the first skyscrapers.
  _Style(
    near: {BuildingKind.brick: 0.5, BuildingKind.tower: 0.3, BuildingKind.mansard: 0.12, BuildingKind.spire: 0.05},
    far: {BuildingKind.tower: 0.45, BuildingKind.brick: 0.45, BuildingKind.spire: 0.1},
    lit: 0.34,
    waterTanks: true,
  ),
  // 1923, Berlin: factories and their stacks, tenement blocks, domes. Few
  // windows lit.
  _Style(
    near: {BuildingKind.factory: 0.38, BuildingKind.brick: 0.4, BuildingKind.dome: 0.1, BuildingKind.spire: 0.12},
    far: {BuildingKind.factory: 0.35, BuildingKind.brick: 0.35, BuildingKind.dome: 0.15, BuildingKind.spire: 0.15},
    lit: 0.12,
    smoke: true,
  ),
  // 1933, a Depression-era American city: Art Deco setbacks, many dark
  // windows.
  _Style(
    near: {BuildingKind.deco: 0.42, BuildingKind.brick: 0.38, BuildingKind.tower: 0.2},
    far: {BuildingKind.deco: 0.55, BuildingKind.tower: 0.25, BuildingKind.brick: 0.2},
    lit: 0.16,
    waterTanks: true,
  ),
  // 1944, Bretton Woods: dark mountains, pines, and a grand hotel.
  _Style(
    near: {BuildingKind.pine: 1.0},
    far: {BuildingKind.mountain: 1.0},
    lit: 0.6,
  ),
  // 1971, Washington: low and classical — a height limit, domes, pediments —
  // among modern blocks and trees.
  _Style(
    near: {BuildingKind.classical: 0.42, BuildingKind.brick: 0.33, BuildingKind.pine: 0.25},
    far: {BuildingKind.classical: 0.5, BuildingKind.brick: 0.35, BuildingKind.dome: 0.15},
    lit: 0.34,
  ),
  // 1979, a late-seventies downtown: brutalist blocks and glass boxes under
  // fluorescent light.
  _Style(
    near: {BuildingKind.brutal: 0.42, BuildingKind.glass: 0.33, BuildingKind.brick: 0.25},
    far: {BuildingKind.glass: 0.45, BuildingKind.brutal: 0.4, BuildingKind.deco: 0.15},
    lit: 0.45,
    cool: true,
  ),
  // 2009, a glass city at night: towers of lit windows, aviation lights.
  _Style(
    near: {BuildingKind.glass: 0.8, BuildingKind.brutal: 0.1, BuildingKind.deco: 0.1},
    far: {BuildingKind.glass: 0.9, BuildingKind.deco: 0.1},
    lit: 0.55,
    cool: true,
  ),
];

/// Height range per kind, as a fraction of screen height, for the near
/// layer. The far layer is scaled down.
///
/// The first version was a third of this, and on a phone the whole city was
/// a strip of rooftops half hidden behind the navigation bar.
(double, double) _heights(BuildingKind k) => switch (k) {
      BuildingKind.terrace => (0.14, 0.22),
      BuildingKind.spire => (0.30, 0.44),
      BuildingKind.dome => (0.26, 0.38),
      BuildingKind.brick => (0.20, 0.34),
      BuildingKind.mansard => (0.20, 0.30),
      BuildingKind.tower => (0.40, 0.56),
      BuildingKind.factory => (0.22, 0.40),
      BuildingKind.deco => (0.42, 0.60),
      BuildingKind.classical => (0.15, 0.24),
      BuildingKind.glass => (0.36, 0.60),
      BuildingKind.brutal => (0.26, 0.46),
      BuildingKind.hotel => (0.20, 0.26),
      BuildingKind.pine => (0.12, 0.24),
      BuildingKind.mountain => (0.40, 0.56),
    };

/// Width range per kind, as a fraction of screen width.
(double, double) _widths(BuildingKind k) => switch (k) {
      BuildingKind.terrace => (0.16, 0.30),
      BuildingKind.spire => (0.09, 0.14),
      BuildingKind.dome => (0.16, 0.24),
      BuildingKind.brick => (0.10, 0.18),
      BuildingKind.mansard => (0.12, 0.20),
      BuildingKind.tower => (0.08, 0.12),
      BuildingKind.factory => (0.20, 0.34),
      BuildingKind.deco => (0.10, 0.16),
      BuildingKind.classical => (0.22, 0.36),
      BuildingKind.glass => (0.08, 0.14),
      BuildingKind.brutal => (0.14, 0.24),
      BuildingKind.hotel => (0.9, 1.1),
      BuildingKind.pine => (0.10, 0.20),
      BuildingKind.mountain => (0.5, 0.9),
    };

class _Building {
  final double x, w, h;
  final BuildingKind kind;
  final int era, seed;
  Picture? pic;

  /// Chimney and stack tops, from the building's base-left, for smoke.
  final List<Offset> stacks = [];

  /// Aviation lights, likewise.
  final List<Offset> beacons = [];

  _Building(this.x, this.w, this.h, this.kind, this.era, this.seed);
}

class _Layer {
  final double parallax;

  /// Height scale against the near layer, and how much of the sky's colour
  /// the silhouettes keep — the far layer is lower and hazier.
  final double scale, haze;
  final bool far;
  final List<_Building> buildings;
  _Layer(this.parallax, this.scale, this.haze, this.far, this.buildings);
}

class CityScape {
  final double w, h;
  final List<Color> eraTints;
  final Color bg;
  final Color warm;
  static const _cool = Color(0xFFBFE0FF);
  late final List<_Layer> _layers;

  /// [eraAt] maps a scroll position to an era index. [totalScroll] is how far
  /// the run can scroll, landing included.
  CityScape({
    required this.w,
    required this.h,
    required double totalScroll,
    required int Function(double scroll) eraAt,
    required this.eraTints,
    required this.bg,
    required this.warm,
    int seed = 0,
  }) {
    _layers = [
      _build(0.12, 0.8, 0.38, true, totalScroll, eraAt, seed + 1),
      _build(0.30, 1.0, 0.70, false, totalScroll, eraAt, seed + 2),
    ];
  }

  _Layer _build(double p, double scale, double haze, bool far, double total, int Function(double) eraAt, int seed) {
    final rnd = Random(seed);
    final out = <_Building>[];
    final span = total * p + w * 1.5;
    var x = -w * 0.1;
    var hotelDone = false;
    while (x < span) {
      // The era a building belongs to is the one in play when it passes the
      // middle of the screen.
      double eraOf(double bx, double bw) => ((bx + bw / 2 - w / 2) / p);
      final probe = eraAt(eraOf(x, w * 0.1).clamp(0.0, total));
      final style = _styles[probe];
      BuildingKind kind = _pick(far ? style.far : style.near, rnd);
      // Bretton Woods has one hotel, in the near layer, mid-era.
      if (!far && probe == 5 && !hotelDone && rnd.nextDouble() < 0.25) {
        kind = BuildingKind.hotel;
        hotelDone = true;
      }
      final (w0, w1) = _widths(kind);
      final (h0, h1) = _heights(kind);
      final bw = w * (w0 + (w1 - w0) * rnd.nextDouble());
      final bh = h * (h0 + (h1 - h0) * rnd.nextDouble()) * scale;
      final era = eraAt(eraOf(x, bw).clamp(0.0, total));
      out.add(_Building(x, bw, bh, kind, era, rnd.nextInt(1 << 30)));
      // Mountains and pines overlap; buildings sit shoulder to shoulder with
      // the odd gap.
      final overlap = kind == BuildingKind.mountain ? 0.45 : (kind == BuildingKind.pine ? 0.3 : 0.0);
      final gap = (kind == BuildingKind.mountain || kind == BuildingKind.pine) ? 0.0 : w * 0.012 * rnd.nextInt(3);
      x += bw * (1 - overlap) + gap;
    }
    return _Layer(p, scale, haze, far, out);
  }

  static BuildingKind _pick(Map<BuildingKind, double> m, Random rnd) {
    final total = m.values.fold(0.0, (a, b) => a + b);
    var r = rnd.nextDouble() * total;
    for (final e in m.entries) {
      r -= e.value;
      if (r <= 0) return e.key;
    }
    return m.keys.last;
  }

  /// For tests: every building of a layer (0 far, 1 near).
  @visibleForTesting
  List<({double x, double w, double h, BuildingKind kind, int era})> layerSpecs(int layer) => [
        for (final b in _layers[layer].buildings) (x: b.x, w: b.w, h: b.h, kind: b.kind, era: b.era),
      ];

  @visibleForTesting
  double parallaxOf(int layer) => _layers[layer].parallax;

  /// [hide] leaves out the buildings of the eras it returns true for: those
  /// with a drawn skyline (see `backdrop.dart`).
  void render(Canvas canvas, double scroll, double t, {bool Function(int era)? hide}) {
    for (final layer in _layers) {
      final off = scroll * layer.parallax;
      // The far layer stands on a higher horizon, so it shows above the near
      // one rather than hiding behind it.
      final base = layer.far ? h * 0.86 : h * 1.0;
      for (final b in layer.buildings) {
        final sx = b.x - off;
        if (sx > w || sx + b.w < 0) continue;
        if (hide != null && hide(b.era)) continue;
        final pic = b.pic ??= _record(b, layer);
        canvas.save();
        canvas.translate(sx, base);
        canvas.drawPicture(pic);
        canvas.restore();
        _live(canvas, b, layer, sx, base, t);
      }
    }
  }

  /// Smoke and aviation lights: the only moving parts.
  void _live(Canvas canvas, _Building b, _Layer layer, double sx, double base, double t) {
    if (b.stacks.isNotEmpty && _styles[b.era].smoke) {
      final tint = eraTints[b.era];
      final smoke = Paint()..color = Color.lerp(tint, const Color(0xFFB8B0A8), 0.35)!.withValues(alpha: layer.far ? 0.07 : 0.11);
      for (var i = 0; i < b.stacks.length; i++) {
        final s = b.stacks[i];
        for (var k = 0; k < 4; k++) {
          final f = ((t * 0.18 + k / 4 + i * 0.37 + b.seed % 7 / 7) % 1.0);
          final r = h * (0.003 + 0.009 * f) * layer.scale;
          canvas.drawCircle(
            Offset(sx + s.dx - f * h * 0.05, base + s.dy - f * h * 0.08 * layer.scale),
            r,
            smoke..color = smoke.color.withValues(alpha: (layer.far ? 0.07 : 0.11) * (1 - f)),
          );
        }
      }
    }
    for (var i = 0; i < b.beacons.length; i++) {
      final on = ((t * 0.8 + i * 0.5 + b.seed % 5 * 0.13) % 1.0) < 0.35;
      if (!on) continue;
      canvas.drawCircle(
        Offset(sx + b.beacons[i].dx, base + b.beacons[i].dy),
        h * 0.0028,
        Paint()..color = const Color(0xFFFF3B30).withValues(alpha: layer.far ? 0.5 : 0.85),
      );
    }
  }

  Picture _record(_Building b, _Layer layer) {
    final rec = PictureRecorder();
    final c = Canvas(rec);
    final rnd = Random(b.seed);
    final tint = eraTints[b.era];
    final body = Color.lerp(tint, bg, layer.haze)!;
    final style = _styles[b.era];
    // Dim enough never to be mistaken for a coin: the first pass lit windows
    // at half strength and the city's amber competed with the coins'.
    final lamp = (style.cool ? _cool : warm).withValues(alpha: layer.far ? 0.18 : 0.32);
    // One path per shape, all filled the same colour. Added to a single path,
    // overlapping shapes of opposite winding cancel and punch holes.
    final shapes = <Path>[];
    void rect(Rect r) => shapes.add(Path()..addRect(r));
    void poly(List<Offset> pts, [bool _ = true]) => shapes.add(Path()..addPolygon(pts, true));
    void oval(Rect r) => shapes.add(Path()..addOval(r));
    final windows = <Rect>[];
    final bw = b.w, bh = b.h;
    final s = layer.scale;

    // Windows on a rectangle: a grid, each lit or not.
    void grid(double x0, double x1, double top, double bottom, {double cw = 0.012, double ch = 0.016, double lit = -1}) {
      final ww = w * cw * s, wh = h * 0.006 * s * (ch / 0.016) + h * 0.004 * s;
      final gx = ww * 2.2, gy = wh * 2.0;
      final p = lit < 0 ? style.lit : lit;
      for (var y = top + gy * 0.7; y < bottom - gy * 0.5; y += gy) {
        for (var x = x0 + gx * 0.5; x < x1 - ww; x += gx) {
          if (rnd.nextDouble() < p) windows.add(Rect.fromLTWH(x, y, ww, wh));
        }
      }
    }

    switch (b.kind) {
      case BuildingKind.terrace:
        final hb = bh * 0.68;
        rect(Rect.fromLTRB(0, -hb, bw, 0));
        final n = max(1, (bw / (w * 0.07)).round());
        final gw = bw / n;
        for (var i = 0; i < n; i++) {
          poly([Offset(i * gw, -hb), Offset(i * gw + gw / 2, -bh * 0.94), Offset((i + 1) * gw, -hb)], true);
          if (i > 0 || n == 1) {
            final cx = n == 1 ? bw * 0.7 : i * gw;
            final cw = w * 0.014 * s;
            rect(Rect.fromLTRB(cx - cw / 2, -bh, cx + cw / 2, -hb - (bh - hb) * 0.4));
            b.stacks.add(Offset(cx, -bh));
          }
        }
        grid(0, bw, -hb, 0);
      case BuildingKind.spire:
        final nave = bh * 0.42, towerTop = bh * 0.62;
        rect(Rect.fromLTRB(0, -nave, bw, 0));
        final tx0 = bw * 0.2, tx1 = bw * 0.55;
        rect(Rect.fromLTRB(tx0, -towerTop, tx1, 0));
        poly([Offset(tx0, -towerTop), Offset((tx0 + tx1) / 2, -bh), Offset(tx1, -towerTop)], true);
        grid(bw * 0.6, bw, -nave, 0, lit: style.lit * 0.6);
      case BuildingKind.dome:
        final hb = bh * 0.5, drum = bh * 0.62;
        rect(Rect.fromLTRB(0, -hb, bw, 0));
        rect(Rect.fromLTRB(bw * 0.28, -drum, bw * 0.72, -hb + 1));
        oval(Rect.fromLTRB(bw * 0.28, -bh * 0.9, bw * 0.72, -drum + (bh * 0.9 - drum)));
        rect(Rect.fromLTRB(bw * 0.47, -bh, bw * 0.53, -bh * 0.86));
        grid(0, bw, -hb, 0);
      case BuildingKind.brick:
        rect(Rect.fromLTRB(0, -bh, bw, 0));
        rect(Rect.fromLTRB(-w * 0.004, -bh - h * 0.004 * s, bw + w * 0.004, -bh + h * 0.004 * s));
        if (style.waterTanks && rnd.nextDouble() < 0.5) {
          final tx = bw * (0.2 + 0.5 * rnd.nextDouble()), tw = w * 0.022 * s, th = h * 0.022 * s;
          rect(Rect.fromLTRB(tx, -bh - th, tx + tw, -bh - th * 0.25));
          poly([Offset(tx - 1, -bh - th), Offset(tx + tw / 2, -bh - th * 1.45), Offset(tx + tw + 1, -bh - th)], true);
          rect(Rect.fromLTRB(tx + 1, -bh - th * 0.3, tx + 2, -bh));
          rect(Rect.fromLTRB(tx + tw - 2, -bh - th * 0.3, tx + tw - 1, -bh));
        }
        grid(0, bw, -bh, 0);
      case BuildingKind.mansard:
        final hb = bh * 0.78;
        rect(Rect.fromLTRB(0, -hb, bw, 0));
        poly([Offset(-w * 0.004, -hb), Offset(bw * 0.1, -bh), Offset(bw * 0.9, -bh), Offset(bw + w * 0.004, -hb)], true);
        grid(0, bw, -hb, 0);
        grid(bw * 0.15, bw * 0.85, -bh, -hb, lit: style.lit * 0.7);
      case BuildingKind.tower:
        final shaft = bh * 0.85;
        rect(Rect.fromLTRB(0, -shaft, bw, 0));
        poly([Offset(0, -shaft), Offset(bw / 2, -bh * 0.97), Offset(bw, -shaft)], true);
        rect(Rect.fromLTRB(bw / 2 - 0.6, -bh, bw / 2 + 0.6, -bh * 0.95));
        grid(0, bw, -shaft, 0, cw: 0.008);
      case BuildingKind.factory:
        final hb = bh * 0.42;
        rect(Rect.fromLTRB(0, -hb, bw, 0));
        final n = max(2, (bw / (w * 0.04)).round());
        final tw = bw / n;
        for (var i = 0; i < n; i++) {
          poly([Offset(i * tw, -hb), Offset(i * tw, -hb - bh * 0.12), Offset((i + 1) * tw, -hb)], true);
        }
        final sx = bw * (0.7 + 0.2 * rnd.nextDouble()), sw = w * 0.018 * s;
        rect(Rect.fromLTRB(sx, -bh, sx + sw, -hb));
        b.stacks.add(Offset(sx + sw / 2, -bh));
        if (bw > w * 0.26) {
          final sx2 = bw * 0.15;
          rect(Rect.fromLTRB(sx2, -bh * 0.8, sx2 + sw, -hb));
          b.stacks.add(Offset(sx2 + sw / 2, -bh * 0.8));
        }
        grid(0, bw, -hb, 0, lit: style.lit * 1.5);
      case BuildingKind.deco:
        final tiers = [(1.0, 0.55), (0.76, 0.75), (0.52, 0.88), (0.26, 0.95)];
        for (final (fw, fh) in tiers) {
          final inset = bw * (1 - fw) / 2;
          rect(Rect.fromLTRB(inset, -bh * fh, bw - inset, 0));
        }
        rect(Rect.fromLTRB(bw / 2 - 0.7, -bh, bw / 2 + 0.7, -bh * 0.94));
        if (b.era >= 7) b.beacons.add(Offset(bw / 2, -bh));
        grid(0, bw, -bh * 0.55, 0, cw: 0.007, ch: 0.022);
        grid(bw * 0.12, bw * 0.88, -bh * 0.75, -bh * 0.55, cw: 0.007, ch: 0.022);
      case BuildingKind.classical:
        final hb = bh * 0.6;
        rect(Rect.fromLTRB(0, -hb, bw, 0));
        if (rnd.nextDouble() < 0.35) {
          rect(Rect.fromLTRB(bw * 0.4, -bh * 0.78, bw * 0.6, -hb + 1));
          oval(Rect.fromLTRB(bw * 0.4, -bh, bw * 0.6, -bh * 0.56));
        } else {
          poly([Offset(bw * 0.25, -hb), Offset(bw * 0.5, -bh * 0.82), Offset(bw * 0.75, -hb)], true);
        }
        // Tall windows between columns.
        for (var x = bw * 0.08; x < bw * 0.92; x += bw * 0.07) {
          if (rnd.nextDouble() < style.lit) windows.add(Rect.fromLTWH(x, -hb * 0.85, w * 0.008 * s, hb * 0.5));
        }
      case BuildingKind.glass:
        final slant = rnd.nextBool();
        poly([
          const Offset(0, 0),
          Offset(0, slant ? -bh * 0.88 : -bh),
          Offset(bw, -bh),
          Offset(bw, 0),
        ], true);
        if (bh > h * 0.4 * s) {
          rect(Rect.fromLTRB(bw * 0.6, -bh - h * 0.04 * s, bw * 0.6 + 1.2, -bh));
          b.beacons.add(Offset(bw * 0.6 + 0.6, -bh - h * 0.04 * s));
        }
        grid(0, bw, slant ? -bh * 0.86 : -bh, 0, cw: 0.007, ch: 0.01);
      case BuildingKind.brutal:
        rect(Rect.fromLTRB(0, -bh * 0.7, bw, 0));
        rect(Rect.fromLTRB(bw * 0.18, -bh, bw * 0.82, -bh * 0.69));
        for (var y = -bh * 0.95; y < -h * 0.01; y += h * 0.022 * s) {
          if (rnd.nextDouble() < style.lit * 1.2) {
            final top = y < -bh * 0.7;
            windows.add(Rect.fromLTRB(top ? bw * 0.24 : bw * 0.06, y, top ? bw * 0.76 : bw * 0.94, y + h * 0.005 * s));
          }
        }
      case BuildingKind.hotel:
        final hb = bh * 0.58;
        rect(Rect.fromLTRB(0, -hb, bw, 0));
        poly([const Offset(0, 0), Offset(bw * 0.04, -bh * 0.75), Offset(bw * 0.96, -bh * 0.75), Offset(bw, 0)], true);
        for (final tx in [bw * 0.08, bw * 0.5, bw * 0.88]) {
          final tw = w * 0.035 * s;
          rect(Rect.fromLTRB(tx - tw / 2, -bh * 0.95, tx + tw / 2, -hb));
          oval(Rect.fromLTRB(tx - tw / 2, -bh * 1.05, tx + tw / 2, -bh * 0.88));
        }
        grid(0, bw, -hb, 0, lit: style.lit);
      case BuildingKind.pine:
        final n = 3 + rnd.nextInt(4);
        for (var i = 0; i < n; i++) {
          final cx = bw * (0.1 + 0.8 * rnd.nextDouble());
          final th = bh * (0.5 + 0.5 * rnd.nextDouble());
          final tw = th * 0.42;
          poly([Offset(cx - tw / 2, 0), Offset(cx, -th), Offset(cx + tw / 2, 0)], true);
        }
      case BuildingKind.mountain:
        final pts = <Offset>[const Offset(0, 0)];
        final n = 5 + rnd.nextInt(4);
        for (var i = 0; i <= n; i++) {
          final f = i / n;
          final peak = sin(f * pi);
          pts.add(Offset(bw * f, -bh * (0.35 + 0.65 * peak) * (0.8 + 0.2 * rnd.nextDouble())));
        }
        pts.add(Offset(bw, 0));
        poly(pts, true);
    }

    final fill = Paint()..color = body;
    for (final sh in shapes) {
      c.drawPath(sh, fill);
    }
    // Mountains catch a little sky light on their ridge.
    if (b.kind == BuildingKind.mountain) {
      c.drawPath(
        shapes.first,
        Paint()
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1
          ..color = Color.lerp(body, tint, 0.5)!,
      );
    }
    final wp = Paint()..color = lamp;
    for (final r in windows) {
      c.drawRect(r, wp);
    }
    return rec.endRecording();
  }

  void dispose() {
    for (final l in _layers) {
      for (final b in l.buildings) {
        b.pic?.dispose();
        b.pic = null;
      }
    }
  }
}
