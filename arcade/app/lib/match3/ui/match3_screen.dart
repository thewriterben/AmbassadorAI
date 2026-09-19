import 'dart:async';
import 'dart:math';

import 'package:flame/game.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../arcade/progress.dart';
import '../../audio.dart';
import '../../dev.dart';
import '../../theme.dart';
import '../game/match3_game.dart';
import '../model/levels.dart';
import '../model/session.dart';
import 'coach.dart';
import '../progress.dart';

/// Plays one level: Flame board + Flutter HUD + end-of-level sheet.
class Match3Screen extends StatefulWidget {
  final Level level;
  const Match3Screen({super.key, required this.level});

  @override
  State<Match3Screen> createState() => _Match3ScreenState();
}

class _Match3ScreenState extends State<Match3Screen> {
  late LevelSession session;
  late Match3Game game;

  @override
  void initState() {
    super.initState();
    _start();
    WidgetsBinding.instance.addPostFrameCallback((_) => Coach.maybeShow(context, widget.level));
  }

  /// Opened as the level starts, awaited when it is won. The server refuses to
  /// pay for a round it did not issue, and it will not pay for one claimed
  /// implausibly fast, so this has to be taken at the start of play.
  Future<String?>? _round;

  void _start() {
    session = LevelSession(widget.level);
    game = Match3Game(session: session, onEnd: _onEnd);
    _round = ArcadeProgress.instance.startMini('coin_quest');
    Audio.instance.setTrack(Audio.trackLevel);
  }

  /// Ends the level now at a chosen star count. Test builds only.
  ///
  /// Goes through the real [_onEnd], so it exercises the whole tail: the
  /// clear is persisted, XP is posted, and the celebration and fireworks run.
  /// A shortcut that just bumped the unlock counter would skip the parts most
  /// worth looking at.
  void _devEnd(SessionState state, {int stars = 3}) {
    final t = widget.level.targetScore;
    if (state == SessionState.won) {
      // Star thresholds are 1x / 1.5x / 2.2x of par, so aim just past one.
      session.score = switch (stars) {
        3 => (t * 2.2).ceil(),
        2 => (t * 1.5).ceil(),
        1 => t,
        _ => 0,
      };
    }
    session.state = state;
    _onEnd(state);
  }

  Future<void> _onEnd(SessionState state) async {
    if (!mounted) return;
    if (state == SessionState.won) {
      // The win sting is fired by celebrate(); firing it here as well restarted
      // the same sample 450 ms later and cut the first one off.
      HapticFeedback.heavyImpact();
      await Progress.instance.record(widget.level.id, session.score, session.stars, won: true);
      // Coin Quest reports to the arcade backend like every other game, so a
      // cleared vault is worth XP on the weekly board.
      final round = _round;
      if (round != null) {
        unawaited(round.then((t) => ArcadeProgress.instance
            .recordMini('coin_quest', token: t, right: session.stars, total: 3, extra: widget.level.id)));
      }
      // celebrate() runs ~5 s of audio and fireworks. Without this guard,
      // backing out during the record above left it playing over the level map.
      if (!mounted) return;
      // Clearing the last vault in the game gets the grand show rather than
      // the ordinary one. Keyed off the end of the level list, not a hardcoded
      // 60, so adding a world moves the finale with it.
      await game.celebrate(finale: widget.level.id == levels.last.id);
      if (!mounted) return;
      for (var s = 1; s <= session.stars; s++) {
        await Future.delayed(const Duration(milliseconds: 260));
        Audio.instance.star(s);
      }
    } else {
      Audio.instance.lose();
      // After the lose sting, not over it.
      await Future.delayed(const Duration(milliseconds: 600));
      if (!mounted) return;
      Audio.instance.voEncourage();
    }
    if (!mounted) return;
    final action = await showModalBottomSheet<String>(
      context: context,
      isDismissible: false,
      enableDrag: false,
      backgroundColor: Colors.transparent,
      builder: (_) => _EndSheet(session: session),
    );
    if (!mounted) return;
    switch (action) {
      case 'retry':
        setState(_start);
      case 'next':
        final next = levels.where((l) => l.id == widget.level.id + 1).firstOrNull;
        if (next == null) {
          Navigator.pop(context);
        } else {
          Navigator.pushReplacement(
              context, MaterialPageRoute(builder: (_) => Match3Screen(level: next)));
        }
      default:
        Navigator.pop(context);
    }
  }

  @override
  Widget build(BuildContext context) {
    final lv = widget.level;
    return Scaffold(
      backgroundColor: AppTheme.bg,
      body: Stack(
        children: [
          Positioned.fill(child: Image.asset('assets/images/bg_dark.png', fit: BoxFit.cover)),
          SafeArea(
            child: Column(
              children: [
                // HUD
                Padding(
                  padding: const EdgeInsets.fromLTRB(12, 8, 12, 4),
                  child: ValueListenableBuilder<int>(
                    valueListenable: game.notifier,
                    builder: (_, __, ___) => Row(
                      children: [
                        IconButton(
                          onPressed: () => Navigator.pop(context),
                          icon: const Icon(Icons.arrow_back, color: AppTheme.text),
                        ),
                        Image.asset('assets/images/logo_orange.png', width: 22, height: 22),
                        const SizedBox(width: 8),
                        _pill('VAULT', '${lv.id}'),
                        const SizedBox(width: 8),
                        _pill('MOVES', '${session.movesLeft}',
                            warn: session.movesLeft <= 5),
                        const Spacer(),
                        DevMenu(
                          title: 'LEVEL ${lv.id} · ${lv.goalShort}',
                          actions: {
                            'Combo x4 — standard praise': () => game.devCombo(4),
                            'Combo x6 — big praise': () => game.devCombo(6),
                            'Combo x9': () => game.devCombo(9),
                            'Win — 3 stars': () => _devEnd(SessionState.won, stars: 3),
                            'Win — 1 star': () => _devEnd(SessionState.won, stars: 1),
                            'Win — 0 stars (under par)': () =>
                                _devEnd(SessionState.won, stars: 0),
                            // The grand show only fires on the last level, so
                            // without this the only way to see it is to clear
                            // all sixty.
                            'Win — GRAND FINALE show': () => unawaited(
                                  game.celebrate(finale: true).then((_) {
                                    if (mounted) _devEnd(SessionState.won, stars: 3);
                                  }),
                                ),
                            'Lose — encouragement line': () => _devEnd(SessionState.lost),
                          },
                        ),
                        const SizedBox(width: 8),
                        TweenAnimationBuilder<double>(
                          tween: Tween(end: session.score.toDouble()),
                          duration: const Duration(milliseconds: 500),
                          curve: Curves.easeOutCubic,
                          builder: (_, v, __) => _pill('SCORE', '${v.round()}', accent: true),
                        ),
                      ],
                    ),
                  ),
                ),
                // Goal bar
                Padding(
                  padding: const EdgeInsets.fromLTRB(20, 6, 20, 10),
                  child: ValueListenableBuilder<int>(
                    valueListenable: game.notifier,
                    builder: (_, __, ___) => Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        // The goal and its counter share one Expanded, with the
                        // stars pinned right.
                        //
                        // This used to be Flexible(text), counter, Spacer(),
                        // stars — and a Spacer *is* an Expanded, so it competed
                        // with the Flexible for the slack and took half of it.
                        // The goal text was left with about a third of the row
                        // and ellipsised on its second line however short the
                        // wording got: "BREAK 12 REINFORCED VAU…". Shortening
                        // the strings treated the symptom; this is the cause.
                        Row(
                          crossAxisAlignment: CrossAxisAlignment.center,
                          children: [
                            Expanded(
                              child: Row(
                                children: [
                                  Flexible(
                                    child: Text(lv.goalText.toUpperCase(),
                                        // Two lines before it gives up: the
                                        // goal is the one thing on screen the
                                        // player must be able to read in full.
                                        maxLines: 2,
                                        overflow: TextOverflow.ellipsis,
                                        style: const TextStyle(
                                            fontFamily: AppTheme.fontMono,
                                            fontSize: 11,
                                            letterSpacing: 1.2,
                                            color: AppTheme.muted)),
                                  ),
                                  const SizedBox(width: 8),
                                  // Objective levels are won by the counter,
                                  // not the score, so it gets the accent.
                                  Text(session.goalCounter,
                                      style: TextStyle(
                                          fontFamily: AppTheme.fontMono,
                                          fontSize: 12,
                                          fontWeight: FontWeight.w700,
                                          color: session.goalMet ? AppTheme.success : AppTheme.accent)),
                                ],
                              ),
                            ),
                            const SizedBox(width: 10),
                            _stars(session.stars),
                          ],
                        ),
                        const SizedBox(height: 6),
                        ClipRRect(
                          borderRadius: BorderRadius.circular(999),
                          child: TweenAnimationBuilder<double>(
                            tween: Tween(end: session.goalProgress),
                            duration: const Duration(milliseconds: 400),
                            curve: Curves.easeOut,
                            builder: (_, v, __) => LinearProgressIndicator(
                              value: v,
                              minHeight: 6,
                              backgroundColor: AppTheme.surface,
                              color: AppTheme.accent,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
                // Board.
                //
                // The game surface is the whole area, not a board-shaped box.
                //
                // It used to be an AspectRatio sized to the grid, inside a
                // Container with `clipBehavior: Clip.antiAlias`. That clipped
                // everything the game drew to the board rectangle — including
                // the fireworks, which is why every win celebration looked
                // small however many shells it fired. Two-thirds of the screen
                // was off limits to them.
                //
                // Flame already centres the board itself (`_layout()` computes
                // `cell = min(w/cols, h/rows)` and an `origin` that centres the
                // grid), so the AspectRatio was doing work the engine already
                // did. Handing the game the full area changes nothing about
                // where the board is drawn, and lets the celebration use the
                // whole screen.
                //
                // The glass plate stays a Flutter widget behind the game, laid
                // out from the same arithmetic so it lands exactly under the
                // grid with the 6px surround it always had.
                Expanded(
                  child: Padding(
                    padding: const EdgeInsets.all(8),
                    child: LayoutBuilder(
                      builder: (context, c) {
                        final cell = min(c.maxWidth / lv.cols, c.maxHeight / lv.rows);
                        final bw = cell * lv.cols, bh = cell * lv.rows;
                        const surround = 6.0;
                        return Stack(
                          children: [
                            Positioned(
                              left: (c.maxWidth - bw) / 2 - surround,
                              top: (c.maxHeight - bh) / 2 - surround,
                              width: bw + surround * 2,
                              height: bh + surround * 2,
                              child: Container(
                                decoration: AppTheme.glass(
                                    radius: 20,
                                    fill: const Color(0xCC050607),
                                    outline: AppTheme.borderStrong),
                              ),
                            ),
                            Positioned.fill(child: GameWidget(game: game)),
                          ],
                        );
                      },
                    ),
                  ),
                ),
                const SizedBox(height: 8),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _pill(String k, String v, {bool accent = false, bool warn = false}) => Container(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 7),
        decoration: AppTheme.glass(
            radius: 999,
            outline: warn ? AppTheme.danger.withValues(alpha: 0.7) : AppTheme.borderStrong),
        child: Row(children: [
          Text('$k ',
              style: const TextStyle(
                  fontFamily: AppTheme.fontMono, fontSize: 10, letterSpacing: 1, color: AppTheme.muted)),
          Text(v,
              style: TextStyle(
                  fontFamily: AppTheme.fontMono,
                  fontSize: 15,
                  fontWeight: FontWeight.w700,
                  color: warn ? AppTheme.danger : (accent ? AppTheme.accent : AppTheme.text))),
        ]),
      );

  Widget _stars(int n) => Row(children: [
        for (var s = 1; s <= 3; s++)
          Icon(Icons.star_rounded, size: 18, color: s <= n ? AppTheme.accent : AppTheme.dim),
      ]);
}

class _EndSheet extends StatelessWidget {
  final LevelSession session;
  const _EndSheet({required this.session});

  @override
  Widget build(BuildContext context) {
    final won = session.state == SessionState.won;
    final isLast = session.level.id == levels.length;
    return Container(
      margin: const EdgeInsets.all(16),
      padding: const EdgeInsets.all(24),
      decoration: AppTheme.glass(radius: 24, fill: AppTheme.card, outline: AppTheme.borderStrong),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(won ? 'VAULT ${session.level.id} OPENED' : 'VAULT SEALED',
              style: TextStyle(
                  fontFamily: AppTheme.fontMono,
                  fontSize: 11,
                  letterSpacing: 1.2,
                  color: won ? AppTheme.accent : AppTheme.danger)),
          const SizedBox(height: 6),
          RichText(
            text: TextSpan(
              style: const TextStyle(
                  fontFamily: AppTheme.fontSans,
                  fontSize: 30,
                  fontWeight: FontWeight.w600,
                  letterSpacing: -1,
                  color: AppTheme.text),
              children: [
                TextSpan(text: won ? 'Cracked ' : 'Out of moves. '),
                TextSpan(
                    text: won ? 'it.' : 'Try again?',
                    style: const TextStyle(
                        fontFamily: AppTheme.fontSerif,
                        fontStyle: FontStyle.italic,
                        fontWeight: FontWeight.w700,
                        color: AppTheme.accent)),
              ],
            ),
          ),
          const SizedBox(height: 14),
          Row(children: [
            for (var s = 1; s <= 3; s++)
              Icon(Icons.star_rounded,
                  size: 34, color: s <= session.stars && won ? AppTheme.accent : AppTheme.dim),
            const Spacer(),
            Text('${session.score}',
                style: const TextStyle(
                    fontFamily: AppTheme.fontMono,
                    fontSize: 28,
                    fontWeight: FontWeight.w700,
                    color: AppTheme.text)),
          ]),
          const SizedBox(height: 20),
          Row(children: [
            Expanded(
              child: OutlinedButton(
                style: OutlinedButton.styleFrom(
                  foregroundColor: AppTheme.text,
                  side: const BorderSide(color: AppTheme.borderStrong),
                  shape: const StadiumBorder(),
                  padding: const EdgeInsets.symmetric(vertical: 16),
                ),
                onPressed: () {
                  Audio.instance.tap();
                  Navigator.pop(context, won ? 'map' : 'retry');
                },
                child: Text(won ? 'Map' : 'Retry'),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: FilledButton(
                onPressed: () {
                  Audio.instance.tap();
                  Navigator.pop(context, won ? (isLast ? 'map' : 'next') : 'map');
                },
                child: Text(won ? (isLast ? 'Done' : 'Next level  →') : 'Map'),
              ),
            ),
          ]),
        ],
      ),
    );
  }
}
