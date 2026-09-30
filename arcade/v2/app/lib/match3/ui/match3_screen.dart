import 'dart:async';
import 'dart:math';

import 'package:flame/game.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../arcade/progress.dart';
import '../../audio.dart';
import '../../dev.dart';
import '../../theme.dart';
import '../../ui_kit.dart';
import '../game/match3_game.dart';
import '../model/levels.dart';
import '../model/session.dart';
import 'coach.dart';
import '../progress.dart';
import '../../arcade/entry.dart';

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

  /// Coin Quest's tune, held for as long as the level is on screen. The
  /// level map holds the same tune underneath, so moving between them does
  /// not restart it.
  late final int _music;

  @override
  void initState() {
    super.initState();
    _music = Audio.instance.claimMusic(Audio.trackQuest);
    _start();
    WidgetsBinding.instance.addPostFrameCallback((_) => Coach.maybeShow(context, widget.level));
  }

  @override
  void dispose() {
    Audio.instance.releaseMusic(_music);
    super.dispose();
  }

  /// Opened as the level starts, awaited when it is won. The server refuses to
  /// pay for a round it did not issue, and it will not pay for one claimed
  /// implausibly fast, so this has to be taken at the start of play.
  Future<String?>? _round;

  void _start() {
    session = LevelSession(widget.level);
    game = Match3Game(session: session, onEnd: _onEnd);
    _round = ArcadeProgress.instance.startMini('coin_quest');
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
    // Read before record(): the result says what this clear added.
    final starsBefore = Progress.instance.stars(widget.level.id);
    final clearedBefore = Progress.instance.best(widget.level.id) > 0;
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
      // Not capped at 9/16 of the screen: with larger system text the sheet
      // is taller than that, and its buttons were cut off on a Pixel.
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (_) => _EndSheet(session: session, starsBefore: starsBefore, clearedBefore: clearedBefore),
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
          Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => Match3Screen(level: next)));
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
                // Header, as drawn: back, the vault, and the game under it.
                Padding(
                  padding: const EdgeInsets.fromLTRB(24, 16, 24, 0),
                  child: ScreenHeader(
                    title: 'Vault ${lv.id.toString().padLeft(2, '0')}',
                    subtitle: 'Coin Quest',
                    subtitleUnderTitle: true,
                    onBack: () => leaveScreen(context),
                    actions: [
                      // Guarded at the call site, not only inside DevMenu —
                      // see the note in level_map.dart. Without this the
                      // action closures keep devCombo and the finale show
                      // alive in a store build.
                      if (Dev.enabled)
                        DevMenu(
                          title: 'LEVEL ${lv.id} · ${lv.goalShort}',
                          actions: {
                            'Combo x4 — standard praise': () => game.devCombo(4),
                            'Combo x6 — big praise': () => game.devCombo(6),
                            'Combo x9': () => game.devCombo(9),
                            'Win — 3 stars': () => _devEnd(SessionState.won, stars: 3),
                            'Win — 1 star': () => _devEnd(SessionState.won, stars: 1),
                            'Win — 0 stars (under par)': () => _devEnd(SessionState.won, stars: 0),
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
                    ],
                  ),
                ),
                const SizedBox(height: 22),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 24),
                  child: ValueListenableBuilder<int>(
                    valueListenable: game.notifier,
                    builder: (_, __, ___) => Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        _MovesScore(
                          moves: session.movesLeft,
                          score: session.score,
                          par: lv.targetScore,
                        ),
                        const SizedBox(height: 22),
                        // The goal and its counter share one Expanded, with the
                        // stars pinned right. (A Spacer beside a Flexible once
                        // took half the slack and ellipsised the goal: "BREAK
                        // 12 REINFORCED VAU…".)
                        Row(
                          children: [
                            Expanded(
                              child: Row(children: [
                                Flexible(
                                  child: Text(_withCommas(lv.goalText),
                                      // Two lines before it gives up: the goal
                                      // is the one thing on screen the player
                                      // must be able to read in full.
                                      maxLines: 2,
                                      overflow: TextOverflow.ellipsis,
                                      style: const TextStyle(
                                          fontSize: 16, fontWeight: FontWeight.w500, color: AppTheme.text)),
                                ),
                                // Objective levels are won by the counter, not
                                // the score, so they show it; a score level's
                                // counter is the card above.
                                if (lv.goal != GoalType.score) ...[
                                  const SizedBox(width: 10),
                                  Text(session.goalCounter,
                                      style: TextStyle(
                                          fontFamily: AppTheme.fontMono,
                                          fontSize: 15,
                                          color: session.goalMet ? AppTheme.success : AppTheme.accent)),
                                ],
                              ]),
                            ),
                            const SizedBox(width: 10),
                            _stars(session.stars),
                          ],
                        ),
                        const SizedBox(height: 14),
                        ClipRRect(
                          borderRadius: BorderRadius.circular(999),
                          child: TweenAnimationBuilder<double>(
                            tween: Tween(end: session.goalProgress),
                            duration: const Duration(milliseconds: 400),
                            curve: Curves.easeOut,
                            builder: (_, v, __) => LinearProgressIndicator(
                              value: v,
                              minHeight: 8,
                              backgroundColor: AppTheme.surface,
                              color: AppTheme.accent,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
                const SizedBox(height: 16),
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
                    padding: const EdgeInsets.fromLTRB(24, 8, 24, 8),
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
                                decoration: BoxDecoration(
                                  color: AppTheme.card,
                                  borderRadius: BorderRadius.circular(24),
                                  border: Border.all(color: AppTheme.border),
                                ),
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

  Widget _stars(int n) => Row(children: [
        for (var s = 1; s <= 3; s++) ...[
          if (s > 1) const SizedBox(width: 4),
          HugeIcon('star', size: 20, color: s <= n ? AppTheme.accent : AppTheme.body),
        ],
      ]);
}

/// "1050" as "1,050", inside a sentence.
String _withCommas(String s) => s.replaceAllMapped(
    RegExp(r'\d{4,}'), (m) => m[0]!.replaceAllMapped(RegExp(r'(\d)(?=(\d{3})+$)'), (d) => '${d[1]},'));

/// Moves left, and the score against par, in one card.
class _MovesScore extends StatelessWidget {
  final int moves, score, par;
  const _MovesScore({required this.moves, required this.score, required this.par});

  @override
  Widget build(BuildContext context) {
    const label = TextStyle(fontSize: 14, color: AppTheme.body);
    const big = TextStyle(fontFamily: AppTheme.fontMono, fontSize: 40, height: 1.1);
    return Container(
      padding: const EdgeInsets.fromLTRB(24, 20, 24, 22),
      decoration: BoxDecoration(
        color: AppTheme.card,
        borderRadius: BorderRadius.circular(28),
        border: Border.all(color: AppTheme.border),
      ),
      child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            const Text('Moves left', style: label),
            const SizedBox(height: 12),
            Text('$moves', style: big.copyWith(color: moves <= 5 ? AppTheme.danger : AppTheme.text)),
          ]),
        ),
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            const Text('Score', style: label),
            const SizedBox(height: 12),
            Row(crossAxisAlignment: CrossAxisAlignment.baseline, textBaseline: TextBaseline.alphabetic, children: [
              TweenAnimationBuilder<double>(
                tween: Tween(end: score.toDouble()),
                duration: const Duration(milliseconds: 500),
                curve: Curves.easeOutCubic,
                builder: (_, v, __) => Text('${v.round()}', style: big.copyWith(color: AppTheme.accent)),
              ),
              const SizedBox(width: 10),
              Flexible(
                child: Text('/ $par',
                    overflow: TextOverflow.fade,
                    softWrap: false,
                    style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 17, color: AppTheme.body)),
              ),
            ]),
          ]),
        ),
      ]),
    );
  }
}

/// The result, as a sheet: the outcome, the stars, the score set large, what
/// this round added on this phone, and the two ways on.
///
/// Worded with care. The approved mockup says "1 star earned" and "Verified
/// score"; "earn" is banned copy (RETURN-SPEC §6), and a demo build has no
/// server to verify anything, so these read "1 of 3 stars" and "Score".
class _EndSheet extends StatelessWidget {
  final LevelSession session;
  final int starsBefore;
  final bool clearedBefore;
  const _EndSheet({required this.session, required this.starsBefore, required this.clearedBefore});

  @override
  Widget build(BuildContext context) {
    final won = session.state == SessionState.won;
    final isLast = session.level.id == levels.length;
    final stars = won ? session.stars : 0;
    final newStars = [for (var s = starsBefore + 1; s <= stars; s++) s];
    final recorded = [
      if (won && !clearedBefore) 'First completion recorded',
      if (newStars.length == 1) 'Star ${newStars.first} recorded',
      if (newStars.length > 1) 'Stars ${newStars.first} to ${newStars.last} recorded',
    ];
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
        children: [
          Container(
            width: 40,
            height: 4,
            decoration: BoxDecoration(color: AppTheme.borderStrong, borderRadius: BorderRadius.circular(2)),
          ),
          const SizedBox(height: 28),
          Text(won ? 'Level complete' : 'Out of moves',
              style: const TextStyle(fontSize: 28, fontWeight: FontWeight.w600, letterSpacing: -0.6, color: AppTheme.text)),
          const SizedBox(height: 20),
          Row(mainAxisSize: MainAxisSize.min, children: [
            for (var s = 1; s <= 3; s++) ...[
              if (s > 1) const SizedBox(width: 18),
              HugeIcon('star', size: s <= stars ? 36 : 30, color: s <= stars ? AppTheme.accent : AppTheme.body),
            ],
          ]),
          const SizedBox(height: 10),
          Text(won ? '$stars of 3 stars' : 'Goal not reached',
              style: const TextStyle(fontSize: 15, color: AppTheme.body)),
          const SizedBox(height: 26),
          const Text('Score', style: TextStyle(fontSize: 15, color: AppTheme.body)),
          Text('${session.score}',
              style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 60, color: AppTheme.text)),
          Text('Coin Quest · level ${session.level.id}${Dev.demoBuild ? ' · demo' : ''}',
              style: const TextStyle(fontSize: 14, color: AppTheme.body)),
          if (recorded.isNotEmpty) ...[
            const SizedBox(height: 14),
            for (final r in recorded)
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 3),
                child: Text(r, style: const TextStyle(fontSize: 15, color: AppTheme.text)),
              ),
          ],
          const SizedBox(height: 24),
          SizedBox(
            width: double.infinity,
            height: 52,
            child: FilledButton(
              onPressed: () {
                Audio.instance.tap();
                Navigator.pop(context, won ? (isLast ? 'map' : 'next') : 'retry');
              },
              child: Text(won ? (isLast ? 'Done' : 'Next level') : 'Play again'),
            ),
          ),
          const SizedBox(height: 12),
          SizedBox(
            width: double.infinity,
            height: 48,
            child: OutlinedButton(
              style: OutlinedButton.styleFrom(
                backgroundColor: AppTheme.surface,
                foregroundColor: AppTheme.text,
                side: const BorderSide(color: AppTheme.border),
                shape: const StadiumBorder(),
                textStyle: const TextStyle(fontFamily: AppTheme.fontSans, fontSize: 16, fontWeight: FontWeight.w500),
              ),
              onPressed: () {
                Audio.instance.tap();
                Navigator.pop(context, 'map');
              },
              child: const Text('Levels'),
            ),
          ),
        ],
        ),
      ),
    );
  }
}
