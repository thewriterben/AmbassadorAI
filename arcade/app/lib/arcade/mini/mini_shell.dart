import 'package:flutter/material.dart';

import '../../audio.dart';
import '../../theme.dart';
import '../progress.dart';

/// Shared chrome for the knowledge mini-games: header pills, timer bar, and a
/// results sheet that awards XP through [ArcadeProgress.recordMini].
class MiniShell extends StatelessWidget {
  final String title;
  final String kicker;
  final List<(String, String)> pills;
  final double? timer; // 0..1 remaining
  final Widget child;
  final Widget? bottom;

  const MiniShell({
    super.key,
    required this.title,
    required this.kicker,
    required this.child,
    this.pills = const [],
    this.timer,
    this.bottom,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.bg,
      body: Stack(
        children: [
          Positioned.fill(child: Image.asset('assets/images/bg_dark.png', fit: BoxFit.cover)),
          SafeArea(
            child: Column(
              children: [
                Padding(
                  padding: const EdgeInsets.fromLTRB(8, 6, 16, 0),
                  child: Row(children: [
                    IconButton(
                        onPressed: () => Navigator.pop(context),
                        icon: const Icon(Icons.arrow_back, color: AppTheme.text)),
                    Expanded(
                      child: Text(kicker,
                          overflow: TextOverflow.ellipsis,
                          style: const TextStyle(
                              fontFamily: AppTheme.fontMono, fontSize: 11, letterSpacing: 1.2, color: AppTheme.muted)),
                    ),
                    for (final (k, v) in pills) ...[
                      const SizedBox(width: 8),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                        decoration: AppTheme.glass(radius: 999, outline: AppTheme.borderStrong),
                        child: Row(children: [
                          Text('$k ',
                              style: const TextStyle(
                                  fontFamily: AppTheme.fontMono, fontSize: 9, letterSpacing: 1, color: AppTheme.muted)),
                          Text(v,
                              style: const TextStyle(
                                  fontFamily: AppTheme.fontMono,
                                  fontSize: 13,
                                  fontWeight: FontWeight.w700,
                                  color: AppTheme.text)),
                        ]),
                      ),
                    ],
                  ]),
                ),
                if (timer != null)
                  Padding(
                    padding: const EdgeInsets.fromLTRB(20, 8, 20, 0),
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(999),
                      child: LinearProgressIndicator(
                        value: timer,
                        minHeight: 4,
                        backgroundColor: AppTheme.surface,
                        color: (timer ?? 1) < 0.2 ? AppTheme.danger : AppTheme.accent,
                      ),
                    ),
                  ),
                Padding(
                  padding: const EdgeInsets.fromLTRB(24, 12, 24, 0),
                  child: Align(
                    alignment: Alignment.centerLeft,
                    child: Text(title,
                        style: const TextStyle(
                            fontSize: 24, fontWeight: FontWeight.w600, letterSpacing: -0.6, color: AppTheme.text)),
                  ),
                ),
                Expanded(child: child),
                if (bottom != null) bottom!,
              ],
            ),
          ),
        ],
      ),
    );
  }
}

/// Reports the round to the server (which applies the XP formula and the
/// daily cap) and shows the results sheet. Returns 'again' or 'home'.
Future<String> showMiniResults(
  BuildContext context, {
  required String game,
  required String headline,
  required int right,
  required int total,
  // The round token from ArcadeProgress.startMini, taken when play began. The
  // server will not pay out a round it did not issue, so a null token here
  // means no XP — which is the correct outcome for an offline or demo build.
  required String? roundToken,
  int extra = 0,
  String? note,
}) async {
  right == total ? Audio.instance.win() : Audio.instance.coinDrop();
  final (gained, badges) =
      await ArcadeProgress.instance.recordMini(game, token: roundToken, right: right, total: total, extra: extra);
  final offline = ArcadeProgress.instance.offline;
  if (!context.mounted) return 'home';
  final action = await showModalBottomSheet<String>(
    context: context,
    isDismissible: false,
    enableDrag: false,
    backgroundColor: Colors.transparent,
    builder: (_) => Container(
      margin: const EdgeInsets.all(16),
      padding: const EdgeInsets.all(24),
      decoration: AppTheme.glass(radius: 24, fill: AppTheme.card, outline: AppTheme.borderStrong),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(headline.toUpperCase(),
              style: const TextStyle(
                  fontFamily: AppTheme.fontMono, fontSize: 11, letterSpacing: 1.2, color: AppTheme.accent)),
          const SizedBox(height: 6),
          RichText(
            text: TextSpan(
              style: const TextStyle(
                  fontFamily: AppTheme.fontSans,
                  fontSize: 28,
                  fontWeight: FontWeight.w600,
                  letterSpacing: -0.8,
                  color: AppTheme.text),
              children: [
                TextSpan(text: '$right of $total '),
                const TextSpan(
                    text: 'right.',
                    style: TextStyle(
                        fontFamily: AppTheme.fontSerif,
                        fontStyle: FontStyle.italic,
                        fontWeight: FontWeight.w700,
                        color: AppTheme.accent)),
              ],
            ),
          ),
          const SizedBox(height: 12),
          Row(children: [
            _stat('XP', '+$gained', accent: true),
            const SizedBox(width: 10),
            _stat('LEVEL', '${ArcadeProgress.instance.level}'),
          ]),
          if (offline) ...[
            const SizedBox(height: 12),
            const Text('Server unreachable — this round was not recorded.',
                style: TextStyle(fontSize: 13, color: AppTheme.danger, height: 1.4)),
          ] else if (gained == 0 && right > 0) ...[
            const SizedBox(height: 12),
            const Text('Practice round — today\'s XP-eligible rounds for this game are used up.',
                style: TextStyle(fontSize: 13, color: AppTheme.body, height: 1.4)),
          ],
          if (note != null) ...[
            const SizedBox(height: 12),
            Text(note, style: const TextStyle(fontSize: 13, color: AppTheme.body, height: 1.4)),
          ],
          if (badges.isNotEmpty) ...[
            const SizedBox(height: 12),
            Wrap(spacing: 8, children: [
              for (final b in badges)
                Chip(
                  avatar: const Icon(Icons.verified_rounded, size: 16, color: AppTheme.accent),
                  label: Text(ArcadeProgress.badgeNames[b] ?? b, style: const TextStyle(fontSize: 12)),
                  backgroundColor: AppTheme.surface,
                  side: const BorderSide(color: AppTheme.borderStrong),
                ),
            ]),
          ],
          const SizedBox(height: 18),
          Row(children: [
            Expanded(
              child: OutlinedButton(
                style: OutlinedButton.styleFrom(
                    foregroundColor: AppTheme.text,
                    side: const BorderSide(color: AppTheme.borderStrong),
                    shape: const StadiumBorder(),
                    padding: const EdgeInsets.symmetric(vertical: 16)),
                onPressed: () {
                  Audio.instance.tap();
                  Navigator.pop(context, 'home');
                },
                child: const Text('Arcade'),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: FilledButton(
                onPressed: () {
                  Audio.instance.tap();
                  Navigator.pop(context, 'again');
                },
                child: const Text('Play again  →'),
              ),
            ),
          ]),
        ],
      ),
    ),
  );
  return action ?? 'home';
}

Widget _stat(String k, String v, {bool accent = false}) => Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
      decoration: AppTheme.glass(radius: 999),
      child: Row(children: [
        Text('$k ',
            style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 10, letterSpacing: 1, color: AppTheme.muted)),
        Text(v,
            style: TextStyle(
                fontFamily: AppTheme.fontMono,
                fontSize: 14,
                fontWeight: FontWeight.w700,
                color: accent ? AppTheme.accent : AppTheme.text)),
      ]),
    );
