import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../../audio.dart';
import '../../theme.dart';
import '../model/levels.dart';

/// First-run coaching for Coin Quest.
///
/// One card, the first time a mechanic can actually appear. Nothing is
/// explained before it is relevant, and every card is shown at most once —
/// the flags live in prefs so a reinstall teaches again but a replay doesn't.
class Coach {
  static const _prefix = 'cq.coach.';

  static Future<bool> _seen(String id) async {
    final p = await SharedPreferences.getInstance();
    return p.getBool('$_prefix$id') ?? false;
  }

  static Future<void> _mark(String id) async {
    final p = await SharedPreferences.getInstance();
    await p.setBool('$_prefix$id', true);
  }

  /// Which card, if any, this level should open with.
  static String? cardFor(Level level) {
    if (level.id == 1) return 'basics';
    switch (level.goal) {
      case GoalType.collect:
        return 'collect';
      case GoalType.seals:
        return 'seals';
      case GoalType.vaults:
        return level.vaultArmor > 1 ? 'vaults_armored' : 'vaults';
      case GoalType.ingots:
        return 'ingots';
      case GoalType.score:
        // Furniture can show up on a score level before its own world.
        if (level.ingotCount > 0) return 'ingots';
        if (level.vaultCount > 0) return 'vaults';
        if (level.sealCount > 0) return 'seals';
        return null;
    }
  }

  /// Title, the instruction, the detail under it, and the art: a row of
  /// tiles, each a stack of images drawn on top of each other (a seal is a
  /// translucent overlay on its coin, as the game draws it).
  static const _cards = <String, (String, String, String, List<List<String>>)>{
    'basics': (
      'Swap to match',
      'Drag a coin onto a neighbour to match three or more.',
      'Match four in a row for a striped coin. Match five for a bomb.',
      [['piece_gold.png'], ['piece_gold.png'], ['piece_gold.png']],
    ),
    'collect': (
      'Collect',
      'Clear coins of the named kind until you have enough.',
      'Cascades count, so set up chains rather than chasing singles.',
      [['piece_blue.png'], ['piece_blue.png'], ['piece_blue.png']],
    ),
    'seals': (
      'Ledger seals',
      'A seal sits under the board. Clear a coin on top of it to strip one layer.',
      'Some seals take two.',
      [['piece_gold.png', 'seal_1.png'], ['piece_silver.png', 'seal_2.png']],
    ),
    'vaults': (
      'Sealed vaults',
      'Clear a match right next to a vault and it breaks open.',
      'Vaults cannot be swapped.',
      [['piece_vault.png']],
    ),
    'vaults_armored': (
      'Reinforced vaults',
      'These take two hits: the first cracks them, the second breaks them open.',
      'Reinforced vaults cannot be swapped either.',
      [['piece_vault_armored.png']],
    ),
    'ingots': (
      'Bring it down',
      'Clear the coins beneath an ingot so it falls, and get it to the bottom row.',
      'Ingots cannot be swapped or destroyed.',
      [['piece_ingot.png']],
    ),
  };

  /// Shows the card for [level] if it has not been shown before.
  static Future<void> maybeShow(BuildContext context, Level level) async {
    final id = cardFor(level);
    if (id == null || await _seen(id)) return;
    final card = _cards[id];
    if (card == null || !context.mounted) return;
    await _mark(id);
    if (!context.mounted) return;
    Audio.instance.ting();
    // A sheet, as drawn, but one that has to be answered: it is the only
    // time this is said, so a stray swipe must not throw it away.
    await showModalBottomSheet<void>(
      context: context,
      isDismissible: false,
      enableDrag: false,
      isScrollControlled: true,
      barrierColor: Colors.black.withValues(alpha: 0.7),
      backgroundColor: Colors.transparent,
      builder: (ctx) => _CoachCard(title: card.$1, lead: card.$2, detail: card.$3, art: card.$4),
    );
  }
}

class _CoachCard extends StatelessWidget {
  final String title, lead, detail;
  final List<List<String>> art;
  const _CoachCard({required this.title, required this.lead, required this.detail, required this.art});

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: AppTheme.sheetMargin(context),
      padding: const EdgeInsets.fromLTRB(24, 10, 24, 24),
      decoration: BoxDecoration(
        color: AppTheme.card,
        borderRadius: BorderRadius.circular(28),
        border: Border.all(color: AppTheme.border),
      ),
      // Scrolls only if a small screen with large text cannot fit it.
      child: SingleChildScrollView(
        child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Center(
            child: Container(
              width: 40,
              height: 4,
              decoration: BoxDecoration(color: AppTheme.borderStrong, borderRadius: BorderRadius.circular(2)),
            ),
          ),
          const SizedBox(height: 30),
          Text(title,
              style: const TextStyle(fontSize: 28, fontWeight: FontWeight.w600, letterSpacing: -0.6, color: AppTheme.text)),
          const SizedBox(height: 26),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.symmetric(vertical: 18),
            decoration: BoxDecoration(color: AppTheme.surface, borderRadius: BorderRadius.circular(20)),
            child: ExcludeSemantics(
              child: Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                for (var i = 0; i < art.length; i++) ...[
                  if (i > 0) const SizedBox(width: 18),
                  SizedBox(
                    width: 48,
                    height: 48,
                    child: Stack(children: [
                      for (final layer in art[i]) Positioned.fill(child: Image.asset('assets/images/$layer')),
                    ]),
                  ),
                ],
              ]),
            ),
          ),
          const SizedBox(height: 26),
          Text(lead, style: const TextStyle(fontSize: 18, height: 1.45, color: AppTheme.text)),
          const SizedBox(height: 18),
          Text(detail, style: const TextStyle(fontSize: 15, height: 1.45, color: AppTheme.body)),
          const SizedBox(height: 26),
          SizedBox(
            width: double.infinity,
            height: 52,
            child: FilledButton(
              onPressed: () {
                Audio.instance.tap();
                Navigator.pop(context);
              },
              child: const Text('Got it'),
            ),
          ),
        ],
        ),
      ),
    );
  }
}
