import 'package:flutter/material.dart';

import 'theme.dart';

/// Test-only shortcuts.
///
/// [enabled] is a `const` read of the environment, so in a build without
/// `--dart-define=DGD_DEV=true` every `if (Dev.enabled)` below folds to
/// `if (false)` and the compiler drops the branch. The shortcuts are not
/// hidden in a store build, they are absent from it.
///
/// Build a test APK with:
///   flutter build apk --release --dart-define=DGD_DEV=true
class Dev {
  static const enabled = bool.fromEnvironment('DGD_DEV');

  /// The internal demo: Coin Quest alone, and no backend behind it.
  ///
  /// Two reasons for the cut. Tablet Run, the Daily Ledger and the weekly
  /// standings are server-authoritative — tablet questions in particular never
  /// ship inside the app, so without a server Tablet Run has nothing to ask.
  /// And the remaining games are at a rougher finish than Coin Quest, so
  /// showing them invites feedback on the wrong things.
  ///
  /// Build with:
  ///   flutter build apk --release --dart-define=DGD_DEMO=true
  static const demoBuild = bool.fromEnvironment('DGD_DEMO');
}

/// A small amber "DEV" chip that opens a sheet of shortcuts.
///
/// Renders nothing when [Dev.enabled] is false, so it can be dropped into a
/// layout unconditionally without a caller-side check.
class DevMenu extends StatelessWidget {
  final String title;

  /// Label -> action. Ordered; the sheet closes before the action runs, so an
  /// action is free to navigate or rebuild the screen underneath it.
  final Map<String, VoidCallback> actions;

  const DevMenu({super.key, required this.title, required this.actions});

  @override
  Widget build(BuildContext context) {
    if (!Dev.enabled) return const SizedBox.shrink();
    return GestureDetector(
      onTap: () => _open(context),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 5),
        decoration: BoxDecoration(
          color: AppTheme.accent.withValues(alpha: 0.16),
          borderRadius: BorderRadius.circular(8),
          border: Border.all(color: AppTheme.accent.withValues(alpha: 0.55)),
        ),
        child: const Text(
          'DEV',
          style: TextStyle(
            fontFamily: AppTheme.fontMono,
            fontSize: 10,
            letterSpacing: 1.2,
            color: AppTheme.accent,
          ),
        ),
      ),
    );
  }

  void _open(BuildContext context) {
    showModalBottomSheet<void>(
      context: context,
      backgroundColor: Colors.transparent,
      builder: (sheet) => Container(
        decoration: const BoxDecoration(
          color: AppTheme.card,
          borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
        ),
        padding: const EdgeInsets.fromLTRB(16, 14, 16, 26),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Row(
              children: [
                Text(title,
                    style: const TextStyle(
                      fontFamily: AppTheme.fontMono,
                      fontSize: 11,
                      letterSpacing: 1.4,
                      color: AppTheme.accent,
                    )),
                const Spacer(),
                const Text('not in store builds',
                    style: TextStyle(fontSize: 11, color: AppTheme.muted)),
              ],
            ),
            const SizedBox(height: 10),
            for (final e in actions.entries)
              Padding(
                padding: const EdgeInsets.only(bottom: 8),
                child: OutlinedButton(
                  style: OutlinedButton.styleFrom(
                    foregroundColor: AppTheme.text,
                    side: const BorderSide(color: AppTheme.border),
                    padding: const EdgeInsets.symmetric(vertical: 13),
                    alignment: Alignment.centerLeft,
                  ),
                  onPressed: () {
                    // Close first: several of these navigate or rebuild the
                    // screen the sheet is sitting on.
                    Navigator.pop(sheet);
                    e.value();
                  },
                  child: Text(e.key),
                ),
              ),
          ],
        ),
      ),
    );
  }
}
