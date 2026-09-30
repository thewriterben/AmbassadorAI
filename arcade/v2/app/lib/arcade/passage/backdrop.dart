/// Drawn backdrops: the owner's art for an era's sky, skyline layers, ground
/// and gate columns, in place of the code-drawn ones.
///
/// The drawing brief is `tool/art/BACKDROP-BRIEF.md`; the art goes in
/// through `tool/art/import_backdrops.py`, which writes the images to
/// `assets/images/backdrop/` and lists them in `manifest.json` there. Every
/// piece is optional and per era: whatever an era lacks is drawn as before
/// (`city.dart`, `passage_gates.dart`, the sky and ground in
/// `passage_render.dart`), so the art can arrive an era, or a layer, at a
/// time. With an empty manifest the game looks exactly as it did.
///
/// | Part    | Drawn as                                                     |
/// |---------|--------------------------------------------------------------|
/// | sky     | Full screen, scaled to cover, over the code-drawn sky        |
/// | far     | Skyline strip, hazy, tiled, slow parallax, on a high horizon |
/// | mid     | Skyline strip, tiled, the main city                          |
/// | near    | Skyline strip, darkest, fastest, along the bottom            |
/// | ground  | Strip tiled under the ground line at landing, scrolling      |
/// | capital | The column's end at the gap, as on a standing column         |
/// | shaft   | A section of column repeated along its length                |
///
/// A strip's height is a fraction of the screen's (its band), its bottom
/// sits at [BackdropLayer.base] of the screen, and it scrolls at
/// [BackdropLayer.parallax] of the gates' speed; the importer writes the
/// defaults into the manifest. Eras change with a crossfade centred on the
/// point where the era does (see [eraWeights]).
///
/// Only the eras around the one being flown are held in memory (see
/// [DrawnBackdrop.keep]): a full set of nine is too many megabytes of
/// texture for a phone to carry at once.
library;

import 'dart:convert';
import 'dart:math';
import 'dart:ui';

import 'package:flame/cache.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart' show rootBundle;

import 'eras.dart';

enum BackdropPart { sky, far, mid, near, ground, capital, shaft }

class BackdropLayer {
  /// Under `assets/images/`, the way Flame loads it.
  final String file;
  final double band, base, parallax;

  /// For the ground: how much of the strip, as a share of its height,
  /// stands above the ground line (grass or kerbs rising above the path).
  final double lip;
  const BackdropLayer({required this.file, this.band = 1, this.base = 1, this.parallax = 0, this.lip = 0});
}

class BackdropManifest {
  static const path = 'assets/images/backdrop/manifest.json';

  /// By era index (the order of [eras]).
  final Map<int, Map<BackdropPart, BackdropLayer>> byEra;
  const BackdropManifest(this.byEra);
  static const empty = BackdropManifest({});

  /// Parses the importer's manifest. Eras are keyed by year; a year or a
  /// part the game does not know is skipped, not an error, so art made for a
  /// later build does not break this one.
  static BackdropManifest parse(String json) {
    final root = jsonDecode(json) as Map<String, dynamic>;
    final out = <int, Map<BackdropPart, BackdropLayer>>{};
    final years = (root['eras'] as Map<String, dynamic>?) ?? const {};
    for (final MapEntry(key: year, value: parts) in years.entries) {
      final era = eras.indexWhere((e) => '${e.year}' == year);
      if (era < 0) continue;
      final m = <BackdropPart, BackdropLayer>{};
      for (final MapEntry(key: name, value: spec) in (parts as Map<String, dynamic>).entries) {
        final part = BackdropPart.values.where((p) => p.name == name).firstOrNull;
        if (part == null) continue;
        final s = spec as Map<String, dynamic>;
        m[part] = BackdropLayer(
          file: 'backdrop/${s['file']}',
          band: (s['band'] as num?)?.toDouble() ?? 1,
          base: (s['base'] as num?)?.toDouble() ?? 1,
          parallax: (s['parallax'] as num?)?.toDouble() ?? 0,
          lip: (s['lip'] as num?)?.toDouble() ?? 0,
        );
      }
      if (m.isNotEmpty) out[era] = m;
    }
    return BackdropManifest(out);
  }

  static Future<BackdropManifest> load() async {
    try {
      return parse(await rootBundle.loadString(path));
    } catch (_) {
      return empty;
    }
  }
}

/// How much of each era to show at [v], the fractional era of the scroll
/// position ([PassageRender._eraF]: era i runs from i to i + 1). One era at
/// full weight, except within [fade] of a change, where the old era fades
/// out and the new one in, smoothly, crossing at the change itself.
List<(int, double)> eraWeights(double v, int count, double fade) {
  final b = v.round();
  if (fade > 0 && b >= 1 && b <= count - 1 && (v - b).abs() < fade) {
    var t = (v - b + fade) / (2 * fade);
    t = t * t * (3 - 2 * t);
    return [(b - 1, 1 - t), (b, t)];
  }
  return [(v.floor().clamp(0, count - 1), 1.0)];
}

/// The opacity to draw each era's layers at, from its [eraWeights] weight:
/// twice the weight, up to full. Drawn old era first, the new one fades in
/// over a still solid old one, which then fades out under a solid new one.
/// Drawn at the weights themselves, both were half see-through at the
/// change, and the sky showed through both cities: on the phone the whole
/// skyline went pale and ghosted at every era change.
List<(int, double)> layerAlphas(List<(int, double)> weights) =>
    [for (final (e, w) in weights) (e, min(1.0, 2 * w))];

class DrawnBackdrop {
  final BackdropManifest manifest;
  DrawnBackdrop(this.manifest);

  final Map<String, Image> _images = {};
  final Set<String> _loading = {};
  Set<int> _kept = {};

  /// Called when an era's images arrive, so cached drawings that used the
  /// code-drawn version (the gates) can be redrawn.
  VoidCallback? onLoaded;

  bool get isEmpty => manifest.byEra.isEmpty;

  Image? image(int era, BackdropPart part) {
    final l = manifest.byEra[era]?[part];
    return l == null ? null : _images[l.file];
  }

  BackdropLayer? layer(int era, BackdropPart part) => manifest.byEra[era]?[part];

  /// Whether [era]'s skyline is drawn art (any of its strips has arrived):
  /// the code-drawn city leaves that era's buildings out.
  bool hasSkyline(int era) =>
      image(era, BackdropPart.far) != null ||
      image(era, BackdropPart.mid) != null ||
      image(era, BackdropPart.near) != null;

  /// Whether [era]'s columns are drawn art: needs both parts.
  bool hasColumns(int era) => image(era, BackdropPart.capital) != null && image(era, BackdropPart.shaft) != null;

  /// Holds the images of [eraSet] and lets the rest go. Loads in the
  /// background; [onLoaded] fires as each era completes.
  void keep(Set<int> eraSet, Images images) {
    if (isEmpty || setEquals(eraSet, _kept)) return;
    _kept = {...eraSet};
    final wanted = {
      for (final e in eraSet) ...?manifest.byEra[e]?.values.map((l) => l.file),
    };
    for (final f in _images.keys.where((f) => !wanted.contains(f)).toList()) {
      _images.remove(f);
      images.clear(f);
    }
    for (final e in eraSet) {
      final files = manifest.byEra[e]?.values.map((l) => l.file).where((f) => !_images.containsKey(f) && !_loading.contains(f)).toList();
      if (files == null || files.isEmpty) continue;
      _loading.addAll(files);
      Future.wait(files.map((f) async {
        try {
          final img = await images.load(f);
          if (_kept.contains(e)) _images[f] = img;
        } catch (_) {
          // A missing or broken file: that part stays code-drawn.
        } finally {
          _loading.remove(f);
        }
      })).then((_) => onLoaded?.call());
    }
  }

  static Paint _paint(double alpha) => Paint()
    ..filterQuality = FilterQuality.medium
    ..color = Color.fromRGBO(255, 255, 255, alpha);

  /// The era's sky, scaled to cover the screen, centred.
  void drawSky(Canvas canvas, int era, double alpha, double w, double h) {
    final img = image(era, BackdropPart.sky);
    if (img == null || alpha <= 0) return;
    final s = max(w / img.width, h / img.height);
    final dw = img.width * s, dh = img.height * s;
    canvas.drawImageRect(
      img,
      Rect.fromLTWH(0, 0, img.width.toDouble(), img.height.toDouble()),
      Rect.fromLTWH((w - dw) / 2, (h - dh) / 2, dw, dh),
      _paint(alpha),
    );
  }

  /// One skyline strip of the era, tiled across the screen.
  void drawStrip(Canvas canvas, int era, BackdropPart part, double alpha, double scroll, double w, double h) {
    final img = image(era, part), l = layer(era, part);
    if (img == null || l == null || alpha <= 0) return;
    final dh = l.band * h, dw = img.width * dh / img.height;
    _tileAcross(canvas, img, alpha, scroll * l.parallax, l.base * h - dh, dw, dh, w);
  }

  /// The era's ground strip, hanging from the ground line (its lip, if
  /// any, standing above it) and scrolling with the gates.
  void drawGround(Canvas canvas, int era, double alpha, double scroll, double groundY, double w, double h) {
    final img = image(era, BackdropPart.ground), l = layer(era, BackdropPart.ground);
    if (img == null || l == null || alpha <= 0) return;
    final dh = l.band * h, dw = img.width * dh / img.height;
    _tileAcross(canvas, img, alpha, scroll, groundY - l.lip * dh, dw, dh, w);
  }

  void _tileAcross(Canvas canvas, Image img, double alpha, double off, double top, double dw, double dh, double w) {
    final src = Rect.fromLTWH(0, 0, img.width.toDouble(), img.height.toDouble());
    final paint = _paint(alpha);
    // Overlap by a hair so the seams never show as a hairline of sky.
    for (var x = -(off % dw); x < w; x += dw) {
      canvas.drawImageRect(img, src, Rect.fromLTWH(x, top, dw + 0.5, dh), paint);
    }
  }

  /// One half of a gate in the era's drawn column, [gw] wide, from [y0] to
  /// [y1], the capital at the end facing the opening: [y1] for the upper
  /// half ([capAtEnd]). The capital is drawn as on a standing column, and
  /// flipped for the hanging one. Returns false when the era has none.
  bool drawColumn(Canvas c, int era, double y0, double y1, double gw, {required bool capAtEnd}) {
    final cap = image(era, BackdropPart.capital), shaft = image(era, BackdropPart.shaft);
    if (cap == null || shaft == null) return false;
    final paint = _paint(1);
    final capH = cap.height * gw / cap.width, shaftH = shaft.height * gw / shaft.width;
    final capSrc = Rect.fromLTWH(0, 0, cap.width.toDouble(), cap.height.toDouble());
    final shaftSrc = Rect.fromLTWH(0, 0, shaft.width.toDouble(), shaft.height.toDouble());
    c.save();
    c.clipRect(Rect.fromLTRB(0, y0, gw, y1));
    if (capAtEnd) {
      // Hanging: the shaft from the capital up, then the capital, flipped.
      for (var y = y1 - capH - shaftH; y + shaftH > y0; y -= shaftH) {
        c.drawImageRect(shaft, shaftSrc, Rect.fromLTWH(0, y, gw, shaftH + 0.5), paint);
      }
      c.save();
      c.translate(0, y1);
      c.scale(1, -1);
      c.drawImageRect(cap, capSrc, Rect.fromLTWH(0, 0, gw, capH), paint);
      c.restore();
    } else {
      for (var y = y0 + capH; y < y1; y += shaftH) {
        c.drawImageRect(shaft, shaftSrc, Rect.fromLTWH(0, y - 0.5, gw, shaftH + 0.5), paint);
      }
      c.drawImageRect(cap, capSrc, Rect.fromLTWH(0, y0, gw, capH), paint);
    }
    c.restore();
    return true;
  }
}
