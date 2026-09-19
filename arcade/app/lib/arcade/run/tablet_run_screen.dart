import 'package:flame/game.dart';
import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../audio.dart';
import '../../theme.dart';
import '../api.dart';
import '../knowledge/tablet_sheet.dart';
import '../progress.dart';
import 'tablet_run_game.dart';

/// One expedition: run + tablets + results. The server owns the expedition:
/// it picks and signs each question, scores answers, checks the run is
/// humanly plausible, and awards XP (plan §5.1).
class TabletRunScreen extends StatefulWidget {
  const TabletRunScreen({super.key});

  @override
  State<TabletRunScreen> createState() => _TabletRunScreenState();
}

class _TabletRunScreenState extends State<TabletRunScreen> {
  int tablets = 3; // Explorer track; the server decides
  TabletRunGame? game;
  String? expeditionId;
  bool rewarded = true;
  DateTime? startedAt;
  final answers = <bool>[];
  bool loading = true;
  String? error;

  @override
  void initState() {
    super.initState();
    _start();
  }

  Future<void> _start() async {
    setState(() {
      loading = true;
      error = null;
    });
    try {
      await ArcadeApi.instance.init();
      final r = await ArcadeApi.instance.startExpedition();
      expeditionId = r['expeditionId'] as String;
      tablets = (r['tabletCount'] as num).toInt();
      rewarded = r['rewarded'] == true;
    } on ApiException catch (e) {
      setState(() {
        loading = false;
        error = e.offline
            ? 'The arcade server is unreachable. Expeditions need it to open tablets and award XP.'
            : 'Could not start an expedition (${e.code}).';
      });
      ArcadeProgress.instance.offline = e.offline;
      return;
    }
    answers.clear();
    startedAt = DateTime.now();
    game = TabletRunGame(tabletCount: tablets, onTablet: _onTablet, onFinish: _onFinish);
    Audio.instance.coinsPour();
    setState(() => loading = false);
  }

  Future<void> _onTablet(int index) async {
    final exp = expeditionId!;
    bool ok = false;
    try {
      final issued = await ArcadeApi.instance.openTablet(exp, index);
      if (!mounted) return;
      final q = TabletQuestion.fromJson(issued);
      ok = await showTablet(
        context,
        q,
        answer: (choice) async =>
            TabletVerdict.fromJson(await ArcadeApi.instance.answerTablet(exp, index, token: q.token, choice: choice)),
      );
    } on ApiException {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Tablet could not be opened — server unreachable. The run continues.')));
      }
    } catch (e) {
      // Anything else here is a bug in us, not a server problem — but it must
      // still not strand the player.
      debugPrint('tablet $index: $e');
    } finally {
      // The game set _paused before calling this and only this can clear it.
      // In `finally` because any escape from the block above — an unexpected
      // exception, or an early return when the screen is gone — otherwise left
      // the run frozen with no error shown, since this future is never awaited.
      answers.add(ok);
      game?.resumeAfterTablet(index, opened: ok);
    }
  }

  Future<void> _onFinish() async {
    final g = game!;
    final runMs = DateTime.now().difference(startedAt!).inMilliseconds;
    int right = answers.where((a) => a).length;
    bool complete = right == tablets;
    int gained = 0;
    var badges = const <String>[];
    bool plausible = true;
    try {
      final r = await ArcadeApi.instance.finishExpedition(expeditionId!, stumbles: g.stumbles, runMs: runMs);
      right = intField(r, 'right');
      complete = r['complete'] == true;
      gained = intField(r, 'xpGained');
      badges = stringsField(r, 'badges');
      plausible = r['plausible'] != false;
      rewarded = r['rewarded'] == true;
      ArcadeProgress.instance.apply(field(r, 'progress'));
    } on ApiException catch (e) {
      // Includes a malformed body — see field() in api.dart. The locally
      // computed right/complete above stand in, so the results sheet still
      // appears rather than the run ending on a blank screen.
      ArcadeProgress.instance.offline = e.offline;
    }
    complete ? Audio.instance.win() : Audio.instance.coinDrop();
    if (!mounted) return;
    final action = await showModalBottomSheet<String>(
      context: context,
      isDismissible: false,
      enableDrag: false,
      backgroundColor: Colors.transparent,
      builder: (_) => _Results(
          right: right,
          total: tablets,
          complete: complete,
          stumbles: g.stumbles,
          gained: gained,
          badges: badges,
          rewarded: rewarded,
          plausible: plausible),
    );
    if (!mounted) return;
    if (action == 'again') {
      _start();
    } else {
      Navigator.pop(context);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.bg,
      body: Stack(
        children: [
          Positioned.fill(child: Image.asset('assets/images/bg_dark.png', fit: BoxFit.cover)),
          if (!loading && game != null) Positioned.fill(child: GameWidget(game: game!)),
          if (loading) const Center(child: CircularProgressIndicator(color: AppTheme.accent)),
          if (error != null)
            Center(
              child: Container(
                margin: const EdgeInsets.all(24),
                padding: const EdgeInsets.all(20),
                decoration: AppTheme.glass(radius: 18, fill: AppTheme.card, outline: AppTheme.danger),
                child: Column(mainAxisSize: MainAxisSize.min, children: [
                  const Icon(Icons.cloud_off_rounded, color: AppTheme.danger),
                  const SizedBox(height: 10),
                  Text(error!, textAlign: TextAlign.center, style: const TextStyle(color: AppTheme.text, height: 1.4)),
                  const SizedBox(height: 14),
                  FilledButton(onPressed: _start, child: const Text('Try again')),
                ]),
              ),
            ),
          SafeArea(
            child: Column(
              children: [
                Padding(
                  padding: const EdgeInsets.fromLTRB(8, 6, 16, 0),
                  child: Row(children: [
                    IconButton(
                        onPressed: () => Navigator.pop(context),
                        icon: const Icon(Icons.arrow_back, color: AppTheme.text)),
                    const Text('EXPEDITION',
                        style: TextStyle(
                            fontFamily: AppTheme.fontMono, fontSize: 11, letterSpacing: 1.2, color: AppTheme.muted)),
                    const Spacer(),
                    if (game != null)
                      ValueListenableBuilder<int>(
                        valueListenable: game!.notifier,
                        builder: (_, __, ___) => Row(children: [
                          _pill('TABLETS', '${game!.tabletsOpened}/$tablets'),
                          const SizedBox(width: 8),
                          _pill('STUMBLES', '${game!.stumbles}'),
                        ]),
                      ),
                  ]),
                ),
                if (game != null)
                  Padding(
                    padding: const EdgeInsets.fromLTRB(20, 8, 20, 0),
                    child: ValueListenableBuilder<int>(
                      valueListenable: game!.notifier,
                      builder: (_, __, ___) => _Track(progress: game!.progress, marks: game!.tabletFractions),
                    ),
                  ),
                const Spacer(),
                const Padding(
                  padding: EdgeInsets.only(bottom: 14),
                  child: Text('TAP TO JUMP  ·  SWIPE DOWN TO SLIDE',
                      style: TextStyle(
                          fontFamily: AppTheme.fontMono, fontSize: 10, letterSpacing: 1.2, color: AppTheme.dim)),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _pill(String k, String v) => Container(
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
        decoration: AppTheme.glass(radius: 999, outline: AppTheme.borderStrong),
        child: Row(children: [
          Text('$k ', style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 9, letterSpacing: 1, color: AppTheme.muted)),
          Text(v, style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 13, fontWeight: FontWeight.w700, color: AppTheme.text)),
        ]),
      );
}

/// Progress bar with tablet markers, moving coin dot.
class _Track extends StatelessWidget {
  final double progress;
  final List<double> marks;
  const _Track({required this.progress, required this.marks});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 22,
      child: LayoutBuilder(builder: (_, c) {
        final w = c.maxWidth;
        return Stack(
          alignment: Alignment.centerLeft,
          children: [
            Container(height: 4, decoration: BoxDecoration(color: AppTheme.surface, borderRadius: BorderRadius.circular(999))),
            Container(
                width: w * progress,
                height: 4,
                decoration: BoxDecoration(color: AppTheme.accent, borderRadius: BorderRadius.circular(999))),
            for (final m in marks)
              Positioned(
                left: w * m - 5,
                child: Container(
                  width: 10,
                  height: 14,
                  decoration: BoxDecoration(
                      color: progress >= m ? AppTheme.accent : AppTheme.surface,
                      border: Border.all(color: AppTheme.accent, width: 1),
                      borderRadius: BorderRadius.circular(3)),
                ),
              ),
            Positioned(
              left: (w * progress - 9).clamp(0, w - 18),
              child: Image.asset('assets/images/coin_gold.png', width: 18, height: 18),
            ),
          ],
        );
      }),
    );
  }
}

class _Results extends StatelessWidget {
  final int right, total, stumbles, gained;
  final bool complete, rewarded, plausible;
  final List<String> badges;
  const _Results(
      {required this.right,
      required this.total,
      required this.complete,
      required this.stumbles,
      required this.gained,
      required this.badges,
      this.rewarded = true,
      this.plausible = true});

  @override
  Widget build(BuildContext context) {
    final p = ArcadeProgress.instance;
    return Container(
      margin: const EdgeInsets.all(16),
      padding: const EdgeInsets.all(24),
      decoration: AppTheme.glass(radius: 24, fill: AppTheme.card, outline: AppTheme.borderStrong),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(complete ? 'EXPEDITION COMPLETE' : 'EXPEDITION FINISHED',
              style: TextStyle(
                  fontFamily: AppTheme.fontMono,
                  fontSize: 11,
                  letterSpacing: 1.2,
                  color: complete ? AppTheme.success : AppTheme.accent)),
          const SizedBox(height: 6),
          RichText(
            text: TextSpan(
              style: const TextStyle(fontFamily: AppTheme.fontSans, fontSize: 28, fontWeight: FontWeight.w600, letterSpacing: -0.8, color: AppTheme.text),
              children: [
                TextSpan(text: '$right of $total tablets '),
                const TextSpan(
                    text: 'opened.',
                    style: TextStyle(fontFamily: AppTheme.fontSerif, fontStyle: FontStyle.italic, fontWeight: FontWeight.w700, color: AppTheme.accent)),
              ],
            ),
          ),
          const SizedBox(height: 14),
          Row(children: [
            _stat('XP', '+$gained', accent: true),
            const SizedBox(width: 10),
            _stat('LEVEL', '${p.level}'),
            const SizedBox(width: 10),
            _stat('STUMBLES', '$stumbles'),
          ]),
          if (!plausible) ...[
            const SizedBox(height: 12),
            const Text('This run did not pass the server\'s plausibility check, so no XP was awarded.',
                style: TextStyle(fontSize: 13, color: AppTheme.danger, height: 1.4)),
          ] else if (!rewarded) ...[
            const SizedBox(height: 12),
            const Text('Practice run — today\'s XP-eligible expeditions are used up. Tablets still count toward mastery.',
                style: TextStyle(fontSize: 13, color: AppTheme.body, height: 1.4)),
          ] else if (!complete) ...[
            const SizedBox(height: 12),
            const Text('Missed tablets come back in 1, 3 and 7 days. Open them all in one run to complete the expedition.',
                style: TextStyle(fontSize: 13, color: AppTheme.body, height: 1.4)),
          ],
          if (badges.isNotEmpty) ...[
            const SizedBox(height: 12),
            Wrap(
              spacing: 8,
              children: [
                for (final b in badges)
                  Chip(
                    avatar: const Icon(Icons.verified_rounded, size: 16, color: AppTheme.accent),
                    label: Text(ArcadeProgress.badgeNames[b] ?? b, style: const TextStyle(fontSize: 12)),
                    backgroundColor: AppTheme.surface,
                    side: const BorderSide(color: AppTheme.borderStrong),
                  ),
              ],
            ),
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
                child: const Text('Run again  →'),
              ),
            ),
          ]),
          const SizedBox(height: 12),
          Center(
            child: TextButton(
              onPressed: () => launchUrl(Uri.parse('https://digitalgold.co/'), mode: LaunchMode.externalApplication),
              child: const Text('Ready to validate? Create your account at digitalgold.co',
                  style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, color: AppTheme.muted)),
            ),
          ),
        ],
      ),
    );
  }

  Widget _stat(String k, String v, {bool accent = false}) => Container(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
        decoration: AppTheme.glass(radius: 999),
        child: Row(children: [
          Text('$k ', style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 10, letterSpacing: 1, color: AppTheme.muted)),
          Text(v,
              style: TextStyle(
                  fontFamily: AppTheme.fontMono,
                  fontSize: 14,
                  fontWeight: FontWeight.w700,
                  color: accent ? AppTheme.accent : AppTheme.text)),
        ]),
      );
}
