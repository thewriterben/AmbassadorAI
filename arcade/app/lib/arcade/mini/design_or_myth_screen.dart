import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';

import '../../audio.dart';
import '../../theme.dart';
import '../knowledge/content.dart';
import '../progress.dart';
import 'mini_shell.dart';

/// Design or Myth? — rapid-fire swipe: right = how DGD is designed, left = myth.
class DesignOrMythScreen extends StatefulWidget {
  const DesignOrMythScreen({super.key});

  @override
  State<DesignOrMythScreen> createState() => _DesignOrMythScreenState();
}

class _DesignOrMythScreenState extends State<DesignOrMythScreen> {
  static const seconds = 60;
  static const perRound = 16;
  late List<MythCard> deck;
  int index = 0, right = 0, wrong = 0, streak = 0;
  double remaining = 1;
  Timer? _tick;
  DateTime? _start;
  MythCard? lastMissed;
  bool over = false;

  @override
  void initState() {
    super.initState();
    _begin();
  }

  /// See PillarSort: opened as play begins, awaited at the results sheet.
  Future<String?>? _round;

  void _begin() {
    _round = ArcadeProgress.instance.startMini('design_or_myth');
    deck = (List.of(mythCards)..shuffle(Random())).take(perRound).toList();
    index = right = wrong = streak = 0;
    remaining = 1;
    lastMissed = null;
    over = false;
    _start = DateTime.now();
    _tick?.cancel();
    _tick = Timer.periodic(const Duration(milliseconds: 100), (_) {
      final e = DateTime.now().difference(_start!).inMilliseconds / 1000;
      setState(() => remaining = (1 - e / seconds).clamp(0.0, 1.0));
      if (e >= seconds) _finish();
    });
    Audio.instance.coinsPour();
  }

  @override
  void dispose() {
    _tick?.cancel();
    super.dispose();
  }

  void _answer(bool saidDesign) {
    if (over || index >= deck.length) return;
    final c = deck[index];
    final ok = c.design == saidDesign;
    setState(() {
      if (ok) {
        right++;
        streak++;
        lastMissed = null;
        Audio.instance.pop(min(3, 1 + streak ~/ 3));
      } else {
        wrong++;
        streak = 0;
        lastMissed = c;
        Audio.instance.invalid();
      }
      index++;
    });
    if (index >= deck.length) _finish();
  }

  Future<void> _finish() async {
    if (over) return;
    over = true;
    _tick?.cancel();
    final token = await _round;
    if (!mounted) return;
    final action = await showMiniResults(context,
        game: 'design_or_myth',
        headline: 'Design or Myth?',
        roundToken: token,
        right: right,
        total: right + wrong,
        note: 'Myths are the misconceptions ambassadors hear most. Knowing why they\'re wrong is the point.');
    if (!mounted) return;
    action == 'again' ? setState(_begin) : Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    final c = index < deck.length ? deck[index] : null;
    return MiniShell(
      kicker: 'DESIGN OR MYTH?',
      title: 'Swipe right if it\'s how DGD works',
      timer: remaining,
      pills: [('RIGHT', '$right'), ('LEFT', '${deck.length - index}')],
      bottom: Padding(
        padding: const EdgeInsets.fromLTRB(16, 4, 16, 16),
        child: Row(children: [
          Expanded(
            child: OutlinedButton.icon(
              style: OutlinedButton.styleFrom(
                  foregroundColor: AppTheme.danger,
                  side: BorderSide(color: AppTheme.danger.withValues(alpha: 0.6)),
                  shape: const StadiumBorder(),
                  padding: const EdgeInsets.symmetric(vertical: 16)),
              onPressed: () => _answer(false),
              icon: const Icon(Icons.close_rounded),
              label: const Text('Myth'),
            ),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: FilledButton.icon(
              style: FilledButton.styleFrom(backgroundColor: AppTheme.success, foregroundColor: const Color(0xFF030303)),
              onPressed: () => _answer(true),
              icon: const Icon(Icons.check_rounded),
              label: const Text('Design'),
            ),
          ),
        ]),
      ),
      child: Column(
        children: [
          Expanded(
            child: Center(
              child: c == null
                  ? const SizedBox()
                  : Dismissible(
                      key: ValueKey('$index-${c.text}'),
                      direction: DismissDirection.horizontal,
                      onDismissed: (d) => _answer(d == DismissDirection.startToEnd),
                      background: _edge(true),
                      secondaryBackground: _edge(false),
                      child: Container(
                        margin: const EdgeInsets.symmetric(horizontal: 24),
                        padding: const EdgeInsets.all(24),
                        decoration: AppTheme.glass(radius: 22, fill: AppTheme.card, outline: AppTheme.borderStrong),
                        child: Column(mainAxisSize: MainAxisSize.min, children: [
                          Image.asset('assets/images/coin_gold.png', width: 56, height: 56),
                          const SizedBox(height: 16),
                          Text(c.text,
                              textAlign: TextAlign.center,
                              style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w600, height: 1.3, color: AppTheme.text)),
                          const SizedBox(height: 18),
                          const Text('◀ MYTH        DESIGN ▶',
                              style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, letterSpacing: 1.5, color: AppTheme.muted)),
                        ]),
                      ),
                    ),
            ),
          ),
          SizedBox(
            height: 56,
            child: lastMissed == null
                ? null
                : Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 24),
                    child: Text(
                        '${lastMissed!.design ? 'DESIGN' : 'MYTH'} · ${lastMissed!.why} (${lastMissed!.source})',
                        maxLines: 3,
                        overflow: TextOverflow.ellipsis,
                        textAlign: TextAlign.center,
                        style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, height: 1.3, color: AppTheme.danger)),
                  ),
          ),
        ],
      ),
    );
  }

  Widget _edge(bool design) => Container(
        margin: const EdgeInsets.symmetric(horizontal: 24),
        alignment: design ? Alignment.centerLeft : Alignment.centerRight,
        padding: const EdgeInsets.symmetric(horizontal: 24),
        decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(22),
            color: (design ? AppTheme.success : AppTheme.danger).withValues(alpha: 0.18)),
        child: Icon(design ? Icons.check_rounded : Icons.close_rounded,
            color: design ? AppTheme.success : AppTheme.danger, size: 36),
      );
}
