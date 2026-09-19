import 'dart:io';

import 'package:flutter_test/flutter_test.dart';

/// Every `assets/...` path written in lib/ must exist on disk.
///
/// A missing image is not a compile error and not a crash — Flutter renders an
/// error box in its place, which is unbounded and quietly wrecks whatever
/// layout it sits in. Two home cards shipped pointing at art that had been
/// deleted in a rename, and the only symptom was a broken tile on the phone.
/// This turns that into a failing test instead.
void main() {
  test('every asset referenced in lib/ exists', () {
    final root = Directory.current.path;
    final ref = RegExp(r'''['"](assets/[^'"]+)['"]''');

    final missing = <String>[];
    for (final f in Directory('$root/lib')
        .listSync(recursive: true)
        .whereType<File>()
        .where((f) => f.path.endsWith('.dart'))) {
      for (final m in ref.allMatches(f.readAsStringSync())) {
        final rel = m.group(1)!;
        // Interpolated paths — 'assets/images/block_$i.png' — only resolve at
        // runtime, so there is nothing to look up here. The families they
        // index (block_N, merge_N, node_*, the coach cards, the medals) are
        // small and change together; a static check would have to guess the
        // range and would go stale.
        if (rel.contains(r'$')) continue;
        if (!File('$root/$rel').existsSync()) {
          missing.add('$rel  <- ${f.path.substring(root.length + 1)}');
        }
      }
    }

    expect(missing, isEmpty, reason: 'missing assets:\n${missing.join('\n')}');
  });

  test('every sound named in audio.dart exists', () {
    final root = Directory.current.path;
    final src = File('$root/lib/audio.dart').readAsStringSync();

    // Bare file names — 'tap_1.wav', 'music_menu.mp3' — resolved against the
    // audio cache prefix rather than written as full asset paths.
    final names = RegExp(r"""['"]([A-Za-z0-9_]+\.(?:wav|mp3|ogg))['"]""")
        .allMatches(src)
        .map((m) => m.group(1)!)
        .toSet();

    expect(names, isNotEmpty, reason: 'no sounds found — did audio.dart move?');

    final missing = names
        .where((n) => !File('$root/assets/audio/$n').existsSync())
        .toList()
      ..sort();

    expect(missing, isEmpty, reason: 'missing audio:\n${missing.join('\n')}');
  });
}
