import 'package:shared_preferences/shared_preferences.dart';

import '../../dev.dart';
import '../progress.dart';
import 'boar.dart';

/// DEV: which boar to fly, instead of the one the player has grown.
///
/// Set from the front room's stepper or the in-game DEV menu, and kept on
/// the device, so a stage chosen for testing — the piglet, say — is still
/// the stage after a restart. [stage] null means the player's own boar.
/// In a build without DGD_DEV the override is never read: [effective] is
/// always the player's own stage.
abstract final class PigsDev {
  static const _key = 'dev.pigs.stage';
  static BoarStage? _stage;
  static bool _loaded = false;

  static BoarStage? get stage => Dev.enabled ? _stage : null;

  /// The player's own stage, as the server last reported it.
  static BoarStage get own => BoarStage.fromId(ArcadeProgress.instance.passageStage) ?? BoarStage.piglet;

  /// The boar that will fly.
  static BoarStage get effective => stage ?? own;

  static Future<void> load() async {
    if (_loaded || !Dev.enabled) return;
    _loaded = true;
    final p = await SharedPreferences.getInstance();
    _stage = BoarStage.fromId(p.getString(_key));
  }

  static Future<void> set(BoarStage? s) async {
    if (!Dev.enabled) return;
    _stage = s;
    final p = await SharedPreferences.getInstance();
    if (s == null) {
      await p.remove(_key);
    } else {
      await p.setString(_key, s.name);
    }
  }

  /// The stage one step up or down from [from], wrapping at the ends.
  static BoarStage step(BoarStage from, int by) =>
      BoarStage.values[(from.index + by) % BoarStage.values.length];
}
