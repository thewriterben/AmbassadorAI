import 'dart:async';
import 'dart:ui' as ui;

import 'package:flutter/services.dart';

/// Decodes asset PNGs into [ui.Image]s for use inside CustomPainters.
class AssetCache {
  static final _cache = <String, ui.Image>{};

  static Future<Map<String, ui.Image>> load(List<String> paths) async {
    for (final p in paths) {
      if (_cache.containsKey(p)) continue;
      final data = await rootBundle.load(p);
      final codec = await ui.instantiateImageCodec(data.buffer.asUint8List());
      final frame = await codec.getNextFrame();
      _cache[p] = frame.image;
    }
    return {for (final p in paths) p: _cache[p]!};
  }
}
