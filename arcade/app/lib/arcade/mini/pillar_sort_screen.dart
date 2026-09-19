import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';

import '../../audio.dart';
import '../../theme.dart';
import '../knowledge/content.dart';
import '../progress.dart';
import 'mini_shell.dart';

/// Pillar Sort — 60 seconds: statements fly in, tap the pillar they belong to.
class PillarSortScreen extends StatefulWidget {
  const PillarSortScreen({super.key});

  @override
  State<PillarSortScreen> createState() => _PillarSortScreenState();
}

class _PillarSortScreenState extends State<PillarSortScreen> with SingleTickerProviderStateMixin {
  static const seconds = 60;
  late List<PillarStatement> deck;
  int index = 0;
  int right = 0, wrong = 0;
  int streak = 0;
  double remaining = 1;
  Timer? _tick;
  DateTime? _start;
  String? flash; // explanation on a miss
  bool over = false;
  late final AnimationController _in =
      AnimationController(vsync: this, duration: const Duration(milliseconds: 260));

  @override
  void initState() {
    super.initState();
    _begin();
  }

  /// Opened as play begins so the round is already issued by the time it
  /// finishes; awaited only at the results sheet.
  Future<String?>? _round;

  void _begin() {
    _round = ArcadeProgress.instance.startMini('pillar_sort');
    deck = List.of(pillarStatements)..shuffle(Random());
    index = 0;
    right = wrong = streak = 0;
    remaining = 1;
    flash = null;
    over = false;
    _start = DateTime.now();
    _tick?.cancel();
    _tick = Timer.periodic(const Duration(milliseconds: 100), (_) {
      final e = DateTime.now().difference(_start!).inMilliseconds / 1000;
      setState(() => remaining = (1 - e / seconds).clamp(0.0, 1.0));
      if (e >= seconds) _finish();
    });
    _in.forward(from: 0);
    Audio.instance.coinsPour();
  }

  @override
  void dispose() {
    _tick?.cancel();
    _in.dispose();
    super.dispose();
  }

  void _answer(int pillar) {
    if (over || index >= deck.length) return;
    final s = deck[index];
    final ok = s.pillar == pillar;
    setState(() {
      if (ok) {
        right++;
        streak++;
        flash = null;
        Audio.instance.pop(min(3, 1 + streak ~/ 3));
      } else {
        wrong++;
        streak = 0;
        flash = '${pillars[s.pillar]} — "${s.text}"';
        Audio.instance.invalid();
      }
      index++;
    });
    _in.forward(from: 0);
    if (index >= deck.length) _finish();
  }

  Future<void> _finish() async {
    if (over) return;
    over = true;
    _tick?.cancel();
    final token = await _round;
    if (!mounted) return;
    final action = await showMiniResults(context,
        game: 'pillar_sort',
        headline: 'Pillar Sort',
        roundToken: token,
        right: right,
        total: right + wrong,
        note: wrong == 0 ? 'Clean sort — bonus applied.' : 'Misses show the correct pillar so the next sort is faster.');
    if (!mounted) return;
    action == 'again' ? setState(_begin) : Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    final s = index < deck.length ? deck[index] : null;
    return MiniShell(
      kicker: 'PILLAR SORT',
      title: 'Which pillar?',
      timer: remaining,
      pills: [('RIGHT', '$right'), ('STREAK', '$streak')],
      bottom: Padding(
        padding: const EdgeInsets.fromLTRB(16, 4, 16, 16),
        child: GridView.count(
          crossAxisCount: 2,
          shrinkWrap: true,
          physics: const NeverScrollableScrollPhysics(),
          mainAxisSpacing: 8,
          crossAxisSpacing: 8,
          childAspectRatio: 3.2,
          children: [
            for (var i = 0; i < pillars.length; i++)
              Material(
                color: Colors.transparent,
                child: InkWell(
                  borderRadius: BorderRadius.circular(14),
                  onTap: () => _answer(i),
                  child: Container(
                    alignment: Alignment.center,
                    decoration: AppTheme.glass(radius: 14, outline: AppTheme.borderStrong),
                    child: Text(pillars[i],
                        textAlign: TextAlign.center,
                        style: const TextStyle(fontSize: 13, fontWeight: FontWeight.w600, color: AppTheme.text)),
                  ),
                ),
              ),
          ],
        ),
      ),
      child: Column(
        children: [
          const SizedBox(height: 10),
          Expanded(
            child: Center(
              child: s == null
                  ? const SizedBox()
                  : ScaleTransition(
                      scale: CurvedAnimation(parent: _in, curve: Curves.easeOutBack),
                      child: Container(
                        margin: const EdgeInsets.symmetric(horizontal: 24),
                        padding: const EdgeInsets.all(22),
                        decoration: AppTheme.glass(radius: 20, fill: AppTheme.card, outline: AppTheme.accent.withValues(alpha: 0.5)),
                        child: Column(mainAxisSize: MainAxisSize.min, children: [
                          Image.asset('assets/images/logo_orange.png', width: 22, height: 22),
                          const SizedBox(height: 12),
                          Text(s.text,
                              textAlign: TextAlign.center,
                              style: const TextStyle(fontSize: 19, fontWeight: FontWeight.w600, height: 1.3, color: AppTheme.text)),
                        ]),
                      ),
                    ),
            ),
          ),
          SizedBox(
            height: 40,
            child: flash == null
                ? null
                : Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 24),
                    child: Text(flash!,
                        maxLines: 2,
                        overflow: TextOverflow.ellipsis,
                        textAlign: TextAlign.center,
                        style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, color: AppTheme.danger)),
                  ),
          ),
        ],
      ),
    );
  }
}
