import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../match3/ui/level_map.dart';
import 'passage/pigs_home_screen.dart';
import 'settings_screen.dart';

/// Where the DGD app opens the arcade.
///
/// Inside the DGD app (DGD App 2.0), the app's own Arcade tab lists the games
/// and has the settings button, as the 2026-09-30 design return draws it. So
/// the app opens the arcade straight into a game, not at the arcade's home.
/// It says where on the `dgd/arcade` channel before it shows the arcade:
///
///   open(coin_quest | pigs | settings | home)
///
/// That screen becomes the whole stack, so backing out of it leaves the
/// arcade and returns to the app ([leaveScreen]). Standalone, nothing calls
/// this, and the arcade opens at its home as it always has.
abstract final class ArcadeEntry {
  static const _channel = MethodChannel('dgd/arcade');
  static final navigator = GlobalKey<NavigatorState>();

  /// A destination that arrived before the navigator was built.
  static String? _pending;

  /// The arcade's home screen, set by main.dart (which defines it).
  static Widget Function()? home;

  static void listen() {
    _channel.setMethodCallHandler((call) async {
      if (call.method == 'open') _open(call.arguments as String? ?? 'home');
      return null;
    });
  }

  static Widget? _screenFor(String where) => switch (where) {
        'coin_quest' => const LevelMapScreen(),
        'pigs' => const PigsHomeScreen(),
        'settings' => const SettingsScreen(),
        _ => home?.call(),
      };

  static void _open(String where) {
    final nav = navigator.currentState;
    if (nav == null) {
      _pending = where;
      return;
    }
    final screen = _screenFor(where);
    if (screen == null) return;
    // No page transition. The app is already animating the arcade in, and a
    // Material route would slide the new screen over whatever the cached
    // engine showed last time, so a warm open briefly showed the previous
    // game (audit R9). The new screen has to be the first frame.
    nav.pushAndRemoveUntil(
      PageRouteBuilder<void>(
        pageBuilder: (_, __, ___) => screen,
        transitionDuration: Duration.zero,
        reverseTransitionDuration: Duration.zero,
      ),
      (_) => false,
    );
  }

  /// Called once the app's navigator exists, for a destination that came in
  /// while the engine was still starting.
  static void takePending() {
    final where = _pending;
    _pending = null;
    if (where != null) _open(where);
  }
}

/// A screen's back button. Pops if there is a screen to go back to; at the
/// bottom of the stack (a screen the DGD app opened directly) it leaves the
/// arcade, as the system back gesture does there.
void leaveScreen(BuildContext context) {
  final nav = Navigator.of(context);
  if (nav.canPop()) {
    nav.pop();
  } else {
    SystemNavigator.pop();
  }
}
