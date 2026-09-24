import 'dart:math';

import 'package:flutter/material.dart';

import '../../audio.dart';
import '../../theme.dart';
import '../cabinet/cabinet.dart';
import '../progress.dart';
import 'abilities.dart';
import 'boar.dart';
import 'eras.dart';
import 'passage_game.dart';

/// When Pigs Fly (game id `passage`): the Flutter side. The cabinet supplies
/// the frame, the pause sheet and the XP submit; everything here is the
/// game's own chrome.
class PassageScreen extends StatefulWidget {
  const PassageScreen({super.key});

  @override
  State<PassageScreen> createState() => _PassageScreenState();
}

class _PassageScreenState extends State<PassageScreen> {
  /// The live game. Set by the cabinet's builder, which runs before any of
  /// the three builders below are first called.
  PassageGame? _game;

  /// The DEV menu's stage choice, kept across "Fly again" so a stage being
  /// looked at does not reset every run. Null means the player's own boar.
  static BoarStage? _devStage;

  /// The boar this player has grown, as the server last said. Read when a
  /// run is built, so a stage reached on one run's claim flies on the next.
  static BoarStage get _ownStage => BoarStage.fromId(ArcadeProgress.instance.passageStage) ?? BoarStage.piglet;

  /// DEV loadouts, cycled from the menu, until the shop (phase 4) sells
  /// abilities. Index 0 is none, which is what every player has today.
  static const _devLoadouts = [
    <AbilityKind>[],
    [AbilityKind.dash, AbilityKind.grapple],
    [AbilityKind.teleport, AbilityKind.freeze],
    [AbilityKind.tractor, AbilityKind.dash],
  ];
  static int _devLoadout = 0;
  static int _devLevel = 1;

  static List<EquippedAbility> get _loadout =>
      [for (final k in _devLoadouts[_devLoadout]) EquippedAbility(k, _devLevel)];

  static String _loadoutLabel() {
    final l = _devLoadouts[_devLoadout];
    return l.isEmpty ? 'none' : '${l.map((k) => k.label).join(' + ')}, level $_devLevel';
  }

  @override
  Widget build(BuildContext context) {
    return CabinetScreen(
      gameId: 'passage',
      title: 'When Pigs Fly',
      kicker: 'ONE TAP',
      musicTrack: Audio.trackLevel,
      builder: (run) => _game = PassageGame(run: run, stage: _devStage ?? _ownStage, loadout: _loadout),
      hudBuilder: (context, run) => _Hud(game: _game!),
      overlayBuilder: (context, run) => _Overlay(game: _game!),
      controlsBuilder: (context, run) => _Controls(game: _game!),
      resultBuilder: (context, result) => _Result(result: result, game: _game!),
      devActions: () => {
        'Skip to the landing': () => _game?.devSkipToLanding(),
        'End short, here': () => _game?.devEndShort(),
        'Full momentum': () => _game?.devMaxMomentum(),
        'Next boar stage': () {
          final g = _game;
          if (g != null) _devStage = g.devNextStage();
        },
        // Loadouts apply from the next run: a run's abilities are fixed when
        // it starts, the way the shop's will be.
        'Abilities (next run): ${_devLoadouts[(_devLoadout + 1) % _devLoadouts.length].map((k) => k.label).join(' + ').ifEmpty('none')}':
            () => _devLoadout = (_devLoadout + 1) % _devLoadouts.length,
        'Ability level (next run): ${_devLevel % maxAbilityLevel + 1}': () => _devLevel = _devLevel % maxAbilityLevel + 1,
        'Now equipped: ${_loadoutLabel()}': () {},
      },
    );
  }
}

extension on String {
  String ifEmpty(String other) => isEmpty ? other : this;
}

/// The two ability buttons, in the bottom corners where thumbs already are.
/// Nothing at all for a run without abilities, so the screen is exactly as
/// it was for everyone until the shop exists.
class _Controls extends StatelessWidget {
  final PassageGame game;
  const _Controls({required this.game});

  @override
  Widget build(BuildContext context) {
    if (game.slots.isEmpty) return const SizedBox.shrink();
    return Stack(
      children: [
        for (var i = 0; i < game.slots.length; i++)
          Positioned(
            left: i == 0 ? 22 : null,
            right: i == 1 ? 22 : null,
            bottom: 26,
            child: AbilityButton(game: game, index: i),
          ),
      ],
    );
  }
}

/// One ability button: its icon, a ring that fills back in over the
/// cooldown, and the charges left for an ability counted by use.
///
/// It fires on touch-down, like the flap does, because a button that waits
/// for the finger to lift is a quarter-second late in a game this fast. It
/// repaints every frame from the game's own clock, so the ring stops when
/// the game is paused.
class AbilityButton extends StatefulWidget {
  final PassageGame game;
  final int index;
  const AbilityButton({super.key, required this.game, required this.index});

  @override
  State<AbilityButton> createState() => _AbilityButtonState();
}

class _AbilityButtonState extends State<AbilityButton> with SingleTickerProviderStateMixin {
  late final AnimationController _frames =
      AnimationController(vsync: this, duration: const Duration(seconds: 1))..repeat();

  @override
  void dispose() {
    _frames.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final slot = widget.game.slots[widget.index];
    final kind = slot.ability.kind;
    return Semantics(
      button: true,
      label: kind.label,
      child: GestureDetector(
        behavior: HitTestBehavior.opaque,
        onTapDown: (_) => widget.game.useAbility(widget.index),
        child: AnimatedBuilder(
          animation: _frames,
          builder: (context, _) {
            final live = widget.game.canUseAbility(widget.index);
            return SizedBox.square(
              dimension: 68,
              child: CustomPaint(
                painter: _RingPainter(cooldown: slot.cooldownFrac, live: live),
                child: Stack(
                  alignment: Alignment.center,
                  children: [
                    Icon(kind.icon, size: 28, color: live ? AppTheme.accent : AppTheme.dim),
                    if (slot.stats.charges > 0)
                      Positioned(
                        right: 6,
                        bottom: 6,
                        child: Text(
                          '${slot.chargesLeft}',
                          style: TextStyle(
                            fontFamily: AppTheme.fontMono,
                            fontSize: 12,
                            color: slot.spent ? AppTheme.dim : AppTheme.text,
                          ),
                        ),
                      ),
                  ],
                ),
              ),
            );
          },
        ),
      ),
    );
  }
}

class _RingPainter extends CustomPainter {
  final double cooldown;
  final bool live;
  _RingPainter({required this.cooldown, required this.live});

  @override
  void paint(Canvas canvas, Size size) {
    final c = size.center(Offset.zero);
    final r = size.shortestSide / 2 - 3;
    canvas.drawCircle(c, r, Paint()..color = AppTheme.bg.withValues(alpha: 0.62));
    canvas.drawCircle(
      c,
      r,
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = 3
        ..color = AppTheme.border,
    );
    // The recharged part of the ring, sweeping round clockwise from the top.
    final ready = 1 - cooldown;
    if (ready > 0) {
      canvas.drawArc(
        Rect.fromCircle(center: c, radius: r),
        -pi / 2,
        2 * pi * ready,
        false,
        Paint()
          ..style = PaintingStyle.stroke
          ..strokeWidth = 3
          ..strokeCap = StrokeCap.round
          ..color = live ? AppTheme.accent : AppTheme.muted,
      );
    }
  }

  @override
  bool shouldRepaint(_RingPainter old) => old.cooldown != cooldown || old.live != live;
}

class _Hud extends StatelessWidget {
  final PassageGame game;
  const _Hud({required this.game});

  @override
  Widget build(BuildContext context) {
    final era = game.eraIndex.clamp(0, eras.length - 1);
    return Row(
      children: [
        // Reserve. Not "lives" — nothing in this game dies, and the word
        // shapes what a player expects to happen when it runs out.
        for (var i = 0; i < PassageGame.startingReserve; i++)
          Padding(
            padding: const EdgeInsets.only(right: 5),
            child: Container(
              width: 10,
              height: 10,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: i < game.reserve ? AppTheme.accent : Colors.transparent,
                border: Border.all(
                  color: i < game.reserve ? AppTheme.accent : AppTheme.dim,
                  width: 1.2,
                ),
              ),
            ),
          ),
        const SizedBox(width: 8),
        // Points, with the momentum multiplier when it is above one. The dot
        // is the same accent as the reserve so the row reads as one line.
        Container(
          width: 8,
          height: 8,
          decoration: const BoxDecoration(shape: BoxShape.circle, color: AppTheme.accent),
        ),
        const SizedBox(width: 5),
        Text(
          '${game.score}',
          style: const TextStyle(
            fontFamily: AppTheme.fontMono,
            fontSize: 14,
            color: AppTheme.accent,
          ),
        ),
        if (game.multiplier > 1)
          Padding(
            padding: const EdgeInsets.only(left: 5),
            child: Text(
              '×${game.multiplier}',
              style: const TextStyle(
                fontFamily: AppTheme.fontMono,
                fontSize: 12,
                color: AppTheme.text,
              ),
            ),
          ),
        const Spacer(),
        Text(
          '${eras[era].year}',
          style: const TextStyle(
            fontFamily: AppTheme.fontMono,
            fontSize: 15,
            color: AppTheme.text,
            letterSpacing: 0.5,
          ),
        ),
        const SizedBox(width: 10),
        Text(
          '${game.erasCleared}/${eras.length}',
          style: const TextStyle(
            fontFamily: AppTheme.fontMono,
            fontSize: 13,
            color: AppTheme.muted,
          ),
        ),
      ],
    );
  }
}

/// Era banners, the opening prompt, and the one line that explains the
/// landing while it is happening.
class _Overlay extends StatelessWidget {
  final PassageGame game;
  const _Overlay({required this.game});

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        Positioned.fill(child: _EraBanner(key: ObjectKey(game), game: game)),
        if (!game.started) ...[
          Align(
            alignment: const Alignment(0, 0.44),
            child: _StageLine(stage: game.stage),
          ),
          const Align(
            alignment: Alignment(0, 0.62),
            child: _Prompt('Tap to fly'),
          ),
        ],
        if (game.phase == PassagePhase.landing)
          const Align(
            alignment: Alignment(0, 0.62),
            child: _Prompt('Ease it down'),
          ),
        if (game.phase == PassagePhase.descending)
          const Align(
            alignment: Alignment(0, 0.62),
            child: _Prompt('Setting down'),
          ),
      ],
    );
  }
}

/// Which boar is about to fly, and how far it is from the next stage. Shown
/// under the hovering boar until the first tap.
class _StageLine extends StatelessWidget {
  final BoarStage stage;
  const _StageLine({required this.stage});

  @override
  Widget build(BuildContext context) {
    final p = ArcadeProgress.instance;
    // A DEV override, or a build with nothing to grow against, shows the
    // name alone: a progress figure that can never move would be a lie.
    final own = BoarStage.fromId(p.passageStage) == stage;
    final next = BoarStage.fromId(p.passageNextStage);
    final detail = ArcadeProgress.noBackend || !own
        ? null
        : next == null
            ? 'fully grown'
            : '${_n(p.passageLifetime)} / ${_n(p.passageNextAt ?? 0)} to ${next.label.toLowerCase()}';
    return Text(
      detail == null ? stage.label.toUpperCase() : '${stage.label.toUpperCase()}  ·  $detail',
      style: const TextStyle(
        fontFamily: AppTheme.fontMono,
        fontSize: 11,
        letterSpacing: 1.4,
        color: AppTheme.muted,
      ),
    );
  }
}

/// 12345 -> "12,345".
String _n(int v) {
  final s = v.toString();
  final b = StringBuffer();
  for (var i = 0; i < s.length; i++) {
    if (i > 0 && (s.length - i) % 3 == 0) b.write(',');
    b.write(s[i]);
  }
  return b.toString();
}

class _Prompt extends StatelessWidget {
  final String text;
  const _Prompt(this.text);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      decoration: BoxDecoration(
        color: AppTheme.bg.withValues(alpha: 0.55),
        borderRadius: BorderRadius.circular(999),
        border: Border.all(color: AppTheme.border),
      ),
      child: Text(
        text,
        style: const TextStyle(
          fontSize: 13,
          letterSpacing: 1.6,
          color: AppTheme.body,
        ),
      ),
    );
  }
}

/// Fades a year and a fact in as the coin enters each era, holds it, and
/// clears. Deliberately near the top of the screen and deliberately short:
/// the player is flying while it is up, and a banner that has to be read to
/// survive is a banner that gets someone hit.
///
/// Built with no listeners and no controller on purpose.
///
/// The first version drove this from an [AnimationController] started by a
/// listener on `eraNotifier`, and on device the opening banner never
/// appeared: the game sets the first era from `onGameResize`, which runs in
/// the layout phase, and whether the listener is registered in time depends
/// on build ordering inside the Flame widget. Nothing in analyze or the tests
/// catches that — the widget was in the tree, it was just sitting at t = 0.
///
/// A [ValueListenableBuilder] keyed by era index reads the value whenever it
/// changes, however late that is, and the [TweenAnimationBuilder] beneath it
/// restarts simply because its key changed. No ordering to get right.
class _EraBanner extends StatelessWidget {
  final PassageGame game;
  const _EraBanner({super.key, required this.game});

  /// In over the first 0.34 s, hold, out over the last 0.8 s.
  static double _opacity(double t) {
    if (t < 0.08) return t / 0.08;
    if (t > 0.81) return (1 - t) / 0.19;
    return 1;
  }

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<int>(
      valueListenable: game.eraNotifier,
      builder: (context, i, _) {
        if (i < 0 || i >= eras.length) return const SizedBox.shrink();
        return _banner(eras[i], i);
      },
    );
  }

  Widget _banner(Era era, int i) {
    return TweenAnimationBuilder<double>(
      key: ValueKey(i),
      tween: Tween(begin: 0, end: 1),
      duration: const Duration(milliseconds: 4200),
      builder: (_, t, __) {
        final o = _opacity(t).clamp(0.0, 1.0);
        if (o <= 0) return const SizedBox.shrink();
        return Align(
          alignment: const Alignment(0, -0.52),
          child: Opacity(
            opacity: o,
            child: Transform.translate(
              offset: Offset(0, 10 * (1 - o)),
              child: Padding(
                padding: const EdgeInsets.symmetric(horizontal: 26),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text(
                      '${era.year}',
                      style: const TextStyle(
                        fontFamily: AppTheme.fontMono,
                        fontSize: 34,
                        color: AppTheme.accent,
                        letterSpacing: 2,
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(
                      era.name.toUpperCase(),
                      textAlign: TextAlign.center,
                      style: const TextStyle(
                        fontSize: 11,
                        letterSpacing: 2.2,
                        color: AppTheme.text,
                      ),
                    ),
                    const SizedBox(height: 8),
                    Text(
                      era.fact,
                      textAlign: TextAlign.center,
                      style: const TextStyle(
                        fontSize: 12.5,
                        height: 1.35,
                        color: AppTheme.body,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        );
      },
    );
  }
}

/// The landing summary.
///
/// There is no "game over" and no "you failed" anywhere on this sheet, in any
/// wording, because in this game there is no such event. A run that ends
/// early ended in a landing too — a shorter journey, with fewer eras on it.
/// The copy's whole job is to make the short landing read as an arrival.
class _Result extends StatelessWidget {
  final RunResult result;
  final PassageGame game;
  const _Result({required this.result, required this.game});

  @override
  Widget build(BuildContext context) {
    final full = result.ending == RunEnding.landed;
    final soft = game.softLanding;
    final lastYear = eras[(result.reached - 1).clamp(0, eras.length - 1)].year;

    final headline = switch ((full, soft)) {
      (true, true) => 'A clean landing.',
      (true, false) => 'You flew the whole passage.',
      _ => 'You set down in $lastYear.',
    };

    final detail = switch ((full, soft)) {
      (true, true) => 'All ${eras.length} eras, and you put it down gently. '
          'That is the whole thing.',
      (true, false) => 'All ${eras.length} eras. The third star is for '
          'setting it down softly.',
      _ => '${result.reached} of ${eras.length} eras flown, and a landing to '
          'show for it. The reserve ran out, so the pig glided in early.',
    };

    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        CabinetStars(stars: result.stars),
        const SizedBox(height: 16),
        Text(
          headline,
          textAlign: TextAlign.center,
          style: const TextStyle(
            fontSize: 21,
            fontWeight: FontWeight.w600,
            color: AppTheme.text,
          ),
        ),
        const SizedBox(height: 8),
        Text(
          detail,
          textAlign: TextAlign.center,
          style: const TextStyle(fontSize: 13.5, height: 1.45, color: AppTheme.body),
        ),
        const SizedBox(height: 14),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.baseline,
          textBaseline: TextBaseline.alphabetic,
          children: [
            Text(
              '${result.score}',
              style: const TextStyle(
                fontFamily: AppTheme.fontMono,
                fontSize: 22,
                color: AppTheme.accent,
              ),
            ),
            const SizedBox(width: 6),
            Text(
              result.score == 1 ? 'point' : 'points',
              style: const TextStyle(fontSize: 13, color: AppTheme.body),
            ),
            const SizedBox(width: 12),
            Text(
              '${game.coinsTaken} ${game.coinsTaken == 1 ? 'coin' : 'coins'} taken',
              style: const TextStyle(fontSize: 12.5, color: AppTheme.muted),
            ),
          ],
        ),
        if (!ArcadeProgress.noBackend) ...[
          const SizedBox(height: 16),
          GrowthPanel(score: result.score, flew: game.stage),
        ],
        const SizedBox(height: 18),
        // Every era, with the ones you reached lit. Seeing the unlit ones is
        // the invitation to fly again; it is doing the work that a score
        // would do in an endless game.
        Wrap(
          alignment: WrapAlignment.center,
          spacing: 6,
          runSpacing: 6,
          children: [
            for (var i = 0; i < eras.length; i++)
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(6),
                  color: i < result.reached
                      ? AppTheme.accent.withValues(alpha: 0.16)
                      : Colors.transparent,
                  border: Border.all(
                    color: i < result.reached ? AppTheme.accent : AppTheme.border,
                    width: 0.8,
                  ),
                ),
                child: Text(
                  '${eras[i].year}',
                  style: TextStyle(
                    fontFamily: AppTheme.fontMono,
                    fontSize: 11.5,
                    color: i < result.reached ? AppTheme.accent : AppTheme.dim,
                  ),
                ),
              ),
          ],
        ),
        if (result.reached > 0) ...[
          const SizedBox(height: 18),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: AppTheme.glass(radius: 14),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  '$lastYear · ${eras[(result.reached - 1).clamp(0, eras.length - 1)].name}',
                  style: const TextStyle(
                    fontFamily: AppTheme.fontMono,
                    fontSize: 11,
                    letterSpacing: 1.1,
                    color: AppTheme.muted,
                  ),
                ),
                const SizedBox(height: 6),
                Text(
                  eras[(result.reached - 1).clamp(0, eras.length - 1)].fact,
                  style: const TextStyle(
                    fontSize: 13,
                    height: 1.45,
                    color: AppTheme.text,
                  ),
                ),
              ],
            ),
          ),
        ],
      ],
    );
  }
}

/// The boar's growth, on the results sheet: its stage, how far it is to the
/// next, what this flight added, and — once, on the run that crosses a line —
/// that it grew.
///
/// The claim is fire-and-forget (see the cabinet), so this listens rather
/// than waiting: it can open on "counting" and fill in a moment later.
class GrowthPanel extends StatelessWidget {
  final int score;

  /// The stage that flew this run, which is not always the player's own —
  /// the DEV menu can override it.
  final BoarStage flew;
  const GrowthPanel({super.key, required this.score, required this.flew});

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: ArcadeProgress.instance,
      builder: (context, _) {
        final p = ArcadeProgress.instance;
        final stage = BoarStage.fromId(p.passageStage) ?? BoarStage.piglet;
        final next = BoarStage.fromId(p.passageNextStage);
        final claim = p.passageClaim;
        final grew = BoarStage.fromId(claim?.grewInto);

        final nextAt = p.passageNextAt;
        final span = nextAt == null ? 1 : (nextAt - p.passageStageAt).clamp(1, 1 << 31);
        final frac = nextAt == null ? 1.0 : ((p.passageLifetime - p.passageStageAt) / span).clamp(0.0, 1.0);

        final caption = switch (claim) {
          null when p.offline => 'Offline: this flight did not count toward growth.',
          null => 'Adding up the flight…',
          PassageClaim(credited: > 0) when next != null =>
            '+${_n(claim.credited)} toward ${next.label.toLowerCase()}',
          PassageClaim(credited: > 0) => '+${_n(claim.credited)}. Fully grown.',
          _ when score > 0 => "Today's growing flights are used up; this one was practice.",
          _ => null,
        };

        return Container(
          padding: const EdgeInsets.fromLTRB(10, 10, 14, 12),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(14),
            color: grew != null ? AppTheme.accent.withValues(alpha: 0.10) : Colors.transparent,
            border: Border.all(color: grew != null ? AppTheme.accent : AppTheme.border),
          ),
          child: Row(
            children: [
              BoarPortrait(stage: grew ?? stage, size: 58),
              const SizedBox(width: 10),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      grew != null
                          ? 'Your boar grew into a ${grew.label.toLowerCase()}.'
                          : next == null
                              ? '${stage.label} · fully grown'
                              : '${stage.label} · ${_n(p.passageLifetime)} / ${_n(nextAt ?? 0)}',
                      style: TextStyle(
                        fontSize: grew != null ? 14.5 : 13,
                        fontWeight: grew != null ? FontWeight.w600 : FontWeight.w500,
                        color: grew != null ? AppTheme.accent : AppTheme.text,
                      ),
                    ),
                    const SizedBox(height: 7),
                    ClipRRect(
                      borderRadius: BorderRadius.circular(99),
                      child: LinearProgressIndicator(
                        value: frac,
                        minHeight: 5,
                        backgroundColor: AppTheme.border,
                        valueColor: const AlwaysStoppedAnimation(AppTheme.accent),
                      ),
                    ),
                    if (grew != null || caption != null) ...[
                      const SizedBox(height: 6),
                      Text(
                        grew != null ? 'It flies as a ${grew.label.toLowerCase()} from your next run.' : caption!,
                        style: const TextStyle(fontSize: 12, height: 1.35, color: AppTheme.body),
                      ),
                    ],
                  ],
                ),
              ),
            ],
          ),
        );
      },
    );
  }
}
