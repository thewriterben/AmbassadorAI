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

  static const _cards = {
    'basics': (
      'SWAP TO MATCH',
      'Drag a coin onto a neighbour to line up three or more. Four in a row mints a striped coin; five mints a bomb.',
      'piece_gold.png',
    ),
    'collect': (
      'COLLECT',
      'Clear coins of the named kind until you have enough. Cascades count, so set up chains rather than chasing singles.',
      'piece_blue.png',
    ),
    'seals': (
      'LEDGER SEALS',
      'A seal sits under the board. Clear a coin on top of it to strip one layer. Some seals take two.',
      'seal_1.png',
    ),
    'vaults': (
      'SEALED VAULTS',
      'Vaults cannot be swapped. Clear a match right next to one and it breaks open.',
      'piece_vault.png',
    ),
    'vaults_armored': (
      'REINFORCED VAULTS',
      'These take two hits. The first cracks them, the second breaks them open.',
      'piece_vault.png',
    ),
    'ingots': (
      'BRING IT DOWN',
      'Ingots cannot be swapped or destroyed. Clear the coins beneath one so it falls, and get it to the bottom row.',
      'piece_ingot.png',
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
    await showDialog<void>(
      context: context,
      barrierColor: Colors.black87,
      builder: (ctx) => _CoachCard(title: card.$1, body: card.$2, asset: card.$3),
    );
  }
}

class _CoachCard extends StatelessWidget {
  final String title, body, asset;
  const _CoachCard({required this.title, required this.body, required this.asset});

  @override
  Widget build(BuildContext context) {
    return Dialog(
      backgroundColor: Colors.transparent,
      insetPadding: const EdgeInsets.all(24),
      child: Container(
        padding: const EdgeInsets.all(24),
        decoration: AppTheme.glass(radius: 24, fill: AppTheme.card, outline: AppTheme.accent),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(children: [
              Image.asset('assets/images/$asset', width: 46, height: 46),
              const SizedBox(width: 14),
              Expanded(
                child: Text(title,
                    style: const TextStyle(
                        fontFamily: AppTheme.fontMono,
                        fontSize: 12,
                        letterSpacing: 1.3,
                        color: AppTheme.accent)),
              ),
            ]),
            const SizedBox(height: 14),
            Text(body, style: const TextStyle(fontSize: 15, height: 1.45, color: AppTheme.text)),
            const SizedBox(height: 20),
            SizedBox(
              width: double.infinity,
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
