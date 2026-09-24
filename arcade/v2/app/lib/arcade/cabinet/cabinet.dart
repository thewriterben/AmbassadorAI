import 'dart:async';

import 'package:flame/game.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../audio.dart';
import '../../dev.dart';
import '../../theme.dart';
import '../progress.dart';

/// The shared arcade cabinet: the frame every game in the catalogue sits in.
///
/// One place holds the things that are identical across ten games and were
/// otherwise going to be written ten times — the run lifecycle, the HUD
/// chrome, pause and resume, backgrounding, the results sheet, and the single
/// XP submit at the end of a run. A game supplies its Flame view, the middle
/// of its HUD row, and the body of its results sheet, and gets the rest.
///
/// The XP rule is deliberate and matches Coin Quest: a round is opened with
/// the server when play starts and claimed when it ends. The server refuses
/// to pay for a round it never issued, or one claimed implausibly fast, so
/// the open has to happen at the start rather than at the end.

/// How a run finished.
enum RunEnding {
  /// Flew the whole thing and set down at the end of it.
  landed,

  /// Set down before the end. Not a death — see `passage_game.dart`.
  short,

  /// The player left. No XP is claimed for this.
  quit,
}

/// The outcome of one run, in the terms the cabinet cares about.
///
/// Anything game-specific — landing speed, reserve left, which era you
/// reached — stays on the game object, which the results sheet builder has a
/// reference to. Putting it here would make this class the union of ten
/// games' scoreboards.
class RunResult {
  final RunEnding ending;

  /// 0..3, the same scale as Coin Quest so one XP formula covers both.
  final int stars;

  /// Stages reached out of [total]. Shown in the HUD and reported as `extra`.
  final int reached;
  final int total;

  /// Points, for games that have them. Reported as `score`; the server caps
  /// it per game and turns it into a small bounded XP bonus. Zero for a game
  /// with no points.
  final int score;

  const RunResult({
    required this.ending,
    required this.stars,
    required this.reached,
    required this.total,
    this.score = 0,
  });
}

/// The handle a game talks to its cabinet through.
///
/// A game never touches navigation, the XP API or the results sheet; it
/// calls [tick] when the HUD needs repainting and [end] exactly once.
class CabinetRun {
  /// Bumped by the game whenever a HUD-visible value changes. The HUD row
  /// rebuilds on this rather than on every frame.
  final ValueNotifier<int> hud = ValueNotifier(0);

  /// A tap anywhere on the play area. The game sets this; the cabinet calls
  /// it.
  ///
  /// Input is handled in Flutter rather than through Flame's gesture mixins
  /// on purpose. The cabinet owns the [GameWidget] and the HUD sits above it
  /// in the same stack, so one hit-test tree deciding all of it is far easier
  /// to reason about than two — and a game that wants only "tap anywhere"
  /// should not have to know what a `TapCallbacks` mixin is.
  VoidCallback? onTap;

  /// Called once, with the outcome, when the game ends the run. Set by the
  /// cabinet. Public so a test can stand in for the cabinet and drive a game
  /// headlessly.
  void Function(RunResult)? onEnd;

  bool _ended = false;

  bool get ended => _ended;

  void tick() => hud.value++;

  /// Ends the run. Safe to call more than once; only the first call counts,
  /// which matters because a landing and a forced descent can both resolve on
  /// the same frame.
  void end(RunResult result) {
    if (_ended) return;
    _ended = true;
    onEnd?.call(result);
  }

  void dispose() => hud.dispose();
}

/// Wraps a Flame game in the cabinet frame.
class CabinetScreen extends StatefulWidget {
  /// Server-side game id, e.g. `passage`. Must match the server's allow-list.
  final String gameId;

  final String title;
  final String kicker;

  /// Builds the Flame view for one run. Called again on every restart, so it
  /// must return a fresh game each time.
  final Game Function(CabinetRun run) builder;

  /// The middle of the HUD row. Rebuilt whenever the game calls
  /// [CabinetRun.tick].
  final Widget Function(BuildContext context, CabinetRun run) hudBuilder;

  /// The body of the results sheet. The buttons around it are the cabinet's.
  final Widget Function(BuildContext context, RunResult result) resultBuilder;

  /// Drawn over the game, under the HUD — era banners, countdowns and the
  /// like. Rebuilt on [CabinetRun.tick].
  final Widget Function(BuildContext context, CabinetRun run)? overlayBuilder;

  /// On-screen controls over the game — ability buttons. Unlike the overlay
  /// this layer takes touches, but only where a control actually is: the
  /// empty space between controls hit-tests through to the play area, so a
  /// tap there is still the game's tap. Hidden while the run is settling.
  final Widget Function(BuildContext context, CabinetRun run)? controlsBuilder;

  /// Music bed for the duration of the run.
  final String musicTrack;

  /// DEV-build shortcuts, rebuilt each frame so they can close over live
  /// state. [DevMenu] renders nothing outside a `DGD_DEV` build, so this
  /// needs no caller-side guard and costs a store build nothing.
  final Map<String, VoidCallback> Function()? devActions;

  const CabinetScreen({
    super.key,
    required this.gameId,
    required this.title,
    required this.kicker,
    required this.builder,
    required this.hudBuilder,
    required this.resultBuilder,
    this.overlayBuilder,
    this.controlsBuilder,
    this.musicTrack = Audio.trackLevel,
    this.devActions,
  });

  @override
  State<CabinetScreen> createState() => CabinetScreenState();
}

class CabinetScreenState extends State<CabinetScreen> with WidgetsBindingObserver {
  late CabinetRun run;
  late Game game;

  /// Opened as play starts, awaited when the run ends. See the class comment.
  Future<String?>? _round;

  bool _paused = false;

  /// True while the results sheet is up, so a stray tap on the game underneath
  /// cannot start a second end sequence.
  bool _settling = false;

  /// Bumped on every run. Keys the [GameWidget] so a restart replaces the
  /// view rather than leaving the finished run on screen.
  int _runCount = 0;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
    _start();
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    run.dispose();
    super.dispose();
  }

  void _start() {
    _runCount++;
    run = CabinetRun()..onEnd = _onEnd;
    game = widget.builder(run);
    _paused = false;
    _settling = false;
    _round = ArcadeProgress.instance.startMini(widget.gameId);
    Audio.instance.setTrack(widget.musicTrack);
  }

  /// Backgrounding pauses the run rather than letting it play on unseen.
  /// Without this a player who takes a call comes back to a finished run.
  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state != AppLifecycleState.resumed && !_paused && !run.ended) {
      _setPaused(true);
    }
  }

  void _setPaused(bool v) {
    if (_paused == v) return;
    setState(() => _paused = v);
    if (v) {
      game.pauseEngine();
    } else {
      game.resumeEngine();
    }
  }

  Future<void> _onEnd(RunResult result) async {
    if (!mounted) return;
    setState(() => _settling = true);
    HapticFeedback.mediumImpact();

    // Claim the round. Fire-and-forget on purpose: the results sheet must not
    // wait on a network call, and `recordMini` already swallows failures into
    // the offline flag rather than throwing.
    if (result.ending != RunEnding.quit) {
      final round = _round;
      if (round != null) {
        unawaited(round.then((t) => ArcadeProgress.instance.recordMini(
              widget.gameId,
              token: t,
              right: result.stars,
              total: 3,
              extra: result.reached,
              score: result.score,
            )));
      }
    }

    // Let the game's own end animation breathe before the sheet slides over
    // it. The landing is the point of this game; covering it immediately
    // would throw away the beat the whole design is built around.
    await Future.delayed(const Duration(milliseconds: 900));
    if (!mounted) return;

    final action = await showModalBottomSheet<String>(
      context: context,
      isDismissible: false,
      enableDrag: false,
      // Without this the sheet is capped at 9/16 of the screen and the tall
      // Passage summary loses its buttons off the bottom.
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (_) => _ResultSheet(body: widget.resultBuilder(context, result)),
    );
    if (!mounted) return;
    if (action == 'again') {
      setState(() {
        run.dispose();
        _start();
      });
    } else {
      Navigator.pop(context);
    }
  }

  /// Abandons the current run and starts a fresh one. Used by the pause sheet
  /// and by the DEV menu.
  void restart() {
    setState(() {
      run.dispose();
      _start();
    });
  }

  Future<void> _openPauseSheet() async {
    Audio.instance.tap();
    _setPaused(true);
    final action = await showModalBottomSheet<String>(
      context: context,
      backgroundColor: Colors.transparent,
      isDismissible: false,
      enableDrag: false,
      builder: (_) => const _PauseSheet(),
    );
    if (!mounted) return;
    switch (action) {
      case 'restart':
        restart();
      case 'quit':
        Navigator.pop(context);
      default:
        _setPaused(false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.bg,
      // StackFit.expand is load-bearing. A Stack takes its size from its
      // NON-positioned children, and every layer here except the HUD is a
      // Positioned.fill — so without this the whole stack collapsed to the
      // height of the HUD row, and the game rendered in a 400px strip at the
      // top of the screen with the rest black. Caught on device, 2026-09-20.
      body: Stack(
        fit: StackFit.expand,
        children: [
          Positioned.fill(
            child: Image.asset('assets/images/bg_dark.png', fit: BoxFit.cover),
          ),
          // A fresh key per run: GameWidget keeps its game in State, so
          // handing it a new instance without one leaves the old run on
          // screen after a restart.
          Positioned.fill(
            child: GestureDetector(
              behavior: HitTestBehavior.opaque,
              onTapDown: (_) {
                if (_paused || _settling || run.ended) return;
                run.onTap?.call();
              },
              child: GameWidget(key: ValueKey(_runCount), game: game),
            ),
          ),
          if (widget.overlayBuilder != null)
            Positioned.fill(
              child: IgnorePointer(
                child: ValueListenableBuilder<int>(
                  valueListenable: run.hud,
                  builder: (c, __, ___) => widget.overlayBuilder!(c, run),
                ),
              ),
            ),
          if (widget.controlsBuilder != null && !_settling)
            Positioned.fill(
              child: SafeArea(
                child: ValueListenableBuilder<int>(
                  valueListenable: run.hud,
                  builder: (c, __, ___) => widget.controlsBuilder!(c, run),
                ),
              ),
            ),
          // Under StackFit.expand this gets tight constraints, so the Column
          // is what keeps the HUD at the top instead of centring it down the
          // middle of the screen.
          SafeArea(
            child: Column(
              children: [
                Padding(
              padding: const EdgeInsets.fromLTRB(4, 4, 8, 0),
              child: Row(
                children: [
                  IconButton(
                    onPressed: () => Navigator.pop(context),
                    icon: const Icon(Icons.arrow_back, color: AppTheme.text),
                    tooltip: 'Leave',
                  ),
                  Expanded(
                    child: ValueListenableBuilder<int>(
                      valueListenable: run.hud,
                      builder: (c, __, ___) => widget.hudBuilder(c, run),
                    ),
                  ),
                  if (widget.devActions != null) ...[
                    const SizedBox(width: 8),
                    DevMenu(title: widget.title, actions: widget.devActions!()),
                  ],
                  IconButton(
                    onPressed: _settling || run.ended ? null : _openPauseSheet,
                    icon: const Icon(Icons.pause_rounded, color: AppTheme.text),
                    tooltip: 'Pause',
                  ),
                ],
                  ),
                ),
              ],
            ),
          ),
          if (_paused)
            Positioned.fill(
              child: Container(color: AppTheme.bg.withValues(alpha: 0.72)),
            ),
        ],
      ),
    );
  }
}

/// Shown while paused. Deliberately three plain choices — a pause menu is not
/// a place to be clever.
class _PauseSheet extends StatelessWidget {
  const _PauseSheet();

  @override
  Widget build(BuildContext context) {
    return _SheetFrame(
      children: [
        const Text(
          'Paused',
          style: TextStyle(fontSize: 22, fontWeight: FontWeight.w600, color: AppTheme.text),
        ),
        const SizedBox(height: 20),
        FilledButton(
          onPressed: () => Navigator.pop(context, 'resume'),
          child: const Text('Resume'),
        ),
        const SizedBox(height: 8),
        TextButton(
          onPressed: () => Navigator.pop(context, 'restart'),
          child: const Text('Start again', style: TextStyle(color: AppTheme.body)),
        ),
        TextButton(
          onPressed: () => Navigator.pop(context, 'quit'),
          child: const Text('Leave', style: TextStyle(color: AppTheme.muted)),
        ),
      ],
    );
  }
}

/// The results sheet. The body is the game's; the two buttons are the same
/// everywhere, and neither of them is the word "retry" — see the design note
/// in `TEN-GAMES.md` §1 on why a run that ends is not a run that failed.
class _ResultSheet extends StatelessWidget {
  final Widget body;
  const _ResultSheet({required this.body});

  @override
  Widget build(BuildContext context) {
    return _SheetFrame(
      footer: [
        const SizedBox(height: 18),
        FilledButton(
          onPressed: () => Navigator.pop(context, 'again'),
          child: const Text('Fly again'),
        ),
        const SizedBox(height: 4),
        TextButton(
          onPressed: () => Navigator.pop(context, 'done'),
          child: const Text('Done', style: TextStyle(color: AppTheme.muted)),
        ),
      ],
      children: [body],
    );
  }
}

/// The body scrolls, the buttons do not.
///
/// A Passage results sheet is stars, a headline, a paragraph, nine era chips
/// and a historical fact — taller than the default bottom sheet's cap, which
/// put "Fly again" underneath the navigation bar on a Pixel. Pinning the
/// footer means the sheet can grow without the only way out of it going
/// off-screen.
class _SheetFrame extends StatelessWidget {
  final List<Widget> children;
  final List<Widget> footer;
  const _SheetFrame({required this.children, this.footer = const []});

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      top: false,
      child: Container(
        width: double.infinity,
        margin: const EdgeInsets.all(12),
        padding: const EdgeInsets.fromLTRB(22, 24, 22, 16),
        constraints: BoxConstraints(maxHeight: MediaQuery.sizeOf(context).height * 0.86),
        decoration: BoxDecoration(
          color: AppTheme.card,
          borderRadius: BorderRadius.circular(22),
          border: Border.all(color: AppTheme.borderStrong, width: 0.5),
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Flexible(
              child: SingleChildScrollView(
                child: Column(mainAxisSize: MainAxisSize.min, children: children),
              ),
            ),
            ...footer,
          ],
        ),
      ),
    );
  }
}

/// Three stars in the Coin Quest style, so the two games read as one app.
class CabinetStars extends StatelessWidget {
  final int stars;
  final double size;
  const CabinetStars({super.key, required this.stars, this.size = 30});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        for (var i = 1; i <= 3; i++)
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 3),
            child: Icon(
              i <= stars ? Icons.star_rounded : Icons.star_outline_rounded,
              size: size,
              color: i <= stars ? AppTheme.accent : AppTheme.dim,
            ),
          ),
      ],
    );
  }
}
