import 'package:flutter/material.dart';

import '../../audio.dart';
import '../../theme.dart';
import '../progress.dart';
import 'abilities.dart';
import 'boar.dart';
import 'passage_screen.dart';

/// When Pigs Fly's front room: the boar you have grown, the abilities you
/// have unlocked and the two you are taking up, and the button that flies.
///
/// The shop sells only for points earned by flying — there is no other way
/// in, and the copy never says buy, spend money, bank, earn or invest. A
/// build with no server (the demo, the standard DEV APK) shows the boar and
/// the Fly button and nothing else, because nothing here could ever change.
class PigsHomeScreen extends StatefulWidget {
  const PigsHomeScreen({super.key});

  @override
  State<PigsHomeScreen> createState() => _PigsHomeScreenState();
}

class _PigsHomeScreenState extends State<PigsHomeScreen> {
  /// The ability a request is out for, so its button shows it and no second
  /// tap can race it. The server would pay once regardless; this is so the
  /// screen does not look like it is ignoring the first tap.
  String? _busy;

  ArcadeProgress get _p => ArcadeProgress.instance;

  Future<void> _fly() async {
    Audio.instance.tap();
    await Navigator.push(context, MaterialPageRoute(builder: (_) => const PassageScreen()));
  }

  void _say(String text) {
    ScaffoldMessenger.of(context)
      ..hideCurrentSnackBar()
      // Short, and lifted clear of the Fly button: on device the default four
      // seconds sat right over it after every unlock.
      ..showSnackBar(SnackBar(
        content: Text(text),
        behavior: SnackBarBehavior.floating,
        duration: const Duration(milliseconds: 1800),
        margin: const EdgeInsets.fromLTRB(16, 0, 16, 84),
      ));
  }

  Future<void> _upgrade(PassageAbility a) async {
    setState(() => _busy = a.id);
    final err = await _p.upgradeAbility(a.id);
    if (!mounted) return;
    setState(() => _busy = null);
    final kind = AbilityKind.fromId(a.id);
    if (err == null) {
      Audio.instance.coinSpin();
      final now = _p.passageAbilities.firstWhere((x) => x.id == a.id, orElse: () => a);
      _say(now.level == 1 ? '${kind?.label ?? a.id} unlocked.' : '${kind?.label ?? a.id} is level ${now.level}.');
      // A first unlock goes straight into an empty slot: the obvious next
      // step, and one less thing to find.
      if (now.level == 1 && _p.passageLoadout.length < 2) {
        await _p.setPassageLoadout([..._p.passageLoadout, a.id]);
      }
    } else {
      _say(switch (err) {
        'not_enough_points' => 'Not enough points yet.',
        'max_level' => 'Already at the top level.',
        'offline' => 'Could not reach the arcade server. Nothing changed.',
        _ => 'That did not go through. Nothing changed.',
      });
    }
  }

  Future<void> _toggle(PassageAbility a) async {
    final now = [..._p.passageLoadout];
    if (now.contains(a.id)) {
      now.remove(a.id);
    } else if (now.length >= 2) {
      _say('Two at a time. Take one off first.');
      return;
    } else {
      now.add(a.id);
    }
    Audio.instance.tap();
    setState(() => _busy = a.id);
    final err = await _p.setPassageLoadout(now);
    if (!mounted) return;
    setState(() => _busy = null);
    if (err != null) _say('Could not reach the arcade server. Your loadout is unchanged.');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.bg,
      appBar: AppBar(
        backgroundColor: AppTheme.bg,
        foregroundColor: AppTheme.text,
        title: const Text('When Pigs Fly'),
      ),
      body: ListenableBuilder(
        listenable: _p,
        builder: (context, _) {
          final shop = !ArcadeProgress.noBackend;
          return Column(
            children: [
              Expanded(
                child: ListView(
                  padding: const EdgeInsets.fromLTRB(16, 4, 16, 16),
                  children: [
                    _BoarCard(p: _p, showProgress: shop),
                    if (shop) ...[
                      const SizedBox(height: 18),
                      _Loadout(ids: _p.passageLoadout),
                      const SizedBox(height: 18),
                      Row(
                        children: [
                          const Text('ABILITIES', style: _kicker),
                          const Spacer(),
                          Text(
                            '${_fmt(_p.passagePoints)} points',
                            style: const TextStyle(
                              fontFamily: AppTheme.fontMono,
                              fontSize: 13,
                              color: AppTheme.accent,
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 8),
                      for (final a in _p.passageAbilities)
                        if (AbilityKind.fromId(a.id) case final kind?)
                          _AbilityRow(
                            kind: kind,
                            a: a,
                            points: _p.passagePoints,
                            equipped: _p.passageLoadout.contains(a.id),
                            busy: _busy == a.id,
                            locked: _busy != null,
                            onUpgrade: () => _upgrade(a),
                            onToggle: () => _toggle(a),
                          ),
                      if (_p.passageAbilities.isEmpty)
                        const Padding(
                          padding: EdgeInsets.symmetric(vertical: 12),
                          child: Text(
                            'The shop opens once the arcade server has been reached.',
                            style: TextStyle(fontSize: 13, color: AppTheme.muted),
                          ),
                        ),
                      const SizedBox(height: 6),
                      const Text(
                        'Points come only from flying. They unlock abilities and nothing else, '
                        'and using them never shrinks your boar.',
                        style: TextStyle(fontSize: 12, height: 1.4, color: AppTheme.muted),
                      ),
                    ],
                  ],
                ),
              ),
              SafeArea(
                top: false,
                child: Padding(
                  padding: const EdgeInsets.fromLTRB(16, 8, 16, 12),
                  child: SizedBox(
                    width: double.infinity,
                    height: 52,
                    child: FilledButton(
                      onPressed: _fly,
                      child: const Text('Fly', style: TextStyle(fontSize: 17, fontWeight: FontWeight.w600)),
                    ),
                  ),
                ),
              ),
            ],
          );
        },
      ),
    );
  }
}

const _kicker = TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, letterSpacing: 1.6, color: AppTheme.muted);

String _fmt(int v) {
  final s = v.toString();
  final b = StringBuffer();
  for (var i = 0; i < s.length; i++) {
    if (i > 0 && (s.length - i) % 3 == 0) b.write(',');
    b.write(s[i]);
  }
  return b.toString();
}

class _BoarCard extends StatelessWidget {
  final ArcadeProgress p;
  final bool showProgress;
  const _BoarCard({required this.p, required this.showProgress});

  @override
  Widget build(BuildContext context) {
    final stage = BoarStage.fromId(p.passageStage) ?? BoarStage.piglet;
    final next = BoarStage.fromId(p.passageNextStage);
    final nextAt = p.passageNextAt;
    final span = nextAt == null ? 1 : (nextAt - p.passageStageAt).clamp(1, 1 << 31);
    final frac = nextAt == null ? 1.0 : ((p.passageLifetime - p.passageStageAt) / span).clamp(0.0, 1.0);
    return Container(
      padding: const EdgeInsets.fromLTRB(12, 12, 16, 16),
      decoration: AppTheme.glass(radius: 16),
      child: Row(
        children: [
          BoarPortrait(stage: stage, size: 112),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('YOUR BOAR', style: _kicker),
                const SizedBox(height: 4),
                Text(
                  stage.label,
                  style: const TextStyle(fontSize: 24, fontWeight: FontWeight.w600, color: AppTheme.text),
                ),
                if (showProgress) ...[
                  const SizedBox(height: 10),
                  ClipRRect(
                    borderRadius: BorderRadius.circular(99),
                    child: LinearProgressIndicator(
                      value: frac,
                      minHeight: 6,
                      backgroundColor: AppTheme.border,
                      valueColor: const AlwaysStoppedAnimation(AppTheme.accent),
                    ),
                  ),
                  const SizedBox(height: 6),
                  Text(
                    next == null
                        ? 'Fully grown'
                        : '${_fmt(p.passageLifetime)} / ${_fmt(nextAt ?? 0)} to ${next.label.toLowerCase()}',
                    style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 12, color: AppTheme.body),
                  ),
                ],
              ],
            ),
          ),
        ],
      ),
    );
  }
}

/// The two buttons a run will have, left and right, as they will appear.
class _Loadout extends StatelessWidget {
  final List<String> ids;
  const _Loadout({required this.ids});

  @override
  Widget build(BuildContext context) {
    Widget slot(int i, String side) {
      final kind = i < ids.length ? AbilityKind.fromId(ids[i]) : null;
      return Expanded(
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 12),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(14),
            border: Border.all(color: kind == null ? AppTheme.border : AppTheme.accent.withValues(alpha: 0.6)),
          ),
          child: Row(
            children: [
              Icon(kind?.icon ?? Icons.add_rounded, size: 22, color: kind == null ? AppTheme.dim : AppTheme.accent),
              const SizedBox(width: 8),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(side, style: _kicker.copyWith(fontSize: 9.5)),
                    const SizedBox(height: 2),
                    Text(
                      kind?.label ?? 'Empty',
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(fontSize: 13.5, color: kind == null ? AppTheme.muted : AppTheme.text),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      );
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Text('TAKING UP', style: _kicker),
        const SizedBox(height: 8),
        Row(children: [slot(0, 'LEFT BUTTON'), const SizedBox(width: 10), slot(1, 'RIGHT BUTTON')]),
      ],
    );
  }
}

class _AbilityRow extends StatelessWidget {
  final AbilityKind kind;
  final PassageAbility a;
  final int points;
  final bool equipped, busy, locked;
  final VoidCallback onUpgrade, onToggle;

  const _AbilityRow({
    required this.kind,
    required this.a,
    required this.points,
    required this.equipped,
    required this.busy,
    required this.locked,
    required this.onUpgrade,
    required this.onToggle,
  });

  @override
  Widget build(BuildContext context) {
    final cost = a.nextCost;
    final affordable = cost != null && points >= cost;
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      padding: const EdgeInsets.fromLTRB(12, 12, 12, 12),
      decoration: AppTheme.glass(radius: 14, outline: equipped ? AppTheme.accent.withValues(alpha: 0.5) : null),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(kind.icon, size: 24, color: a.owned ? AppTheme.accent : AppTheme.dim),
              const SizedBox(width: 10),
              Expanded(
                child: Text(
                  kind.label,
                  style: TextStyle(
                    fontSize: 15.5,
                    fontWeight: FontWeight.w600,
                    color: a.owned ? AppTheme.text : AppTheme.body,
                  ),
                ),
              ),
              // Level pips: filled for each level owned.
              for (var i = 0; i < a.maxLevel; i++)
                Container(
                  margin: const EdgeInsets.only(left: 4),
                  width: 8,
                  height: 8,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: i < a.level ? AppTheme.accent : Colors.transparent,
                    border: Border.all(color: i < a.level ? AppTheme.accent : AppTheme.dim),
                  ),
                ),
            ],
          ),
          const SizedBox(height: 6),
          Text(kind.blurb, style: const TextStyle(fontSize: 12.5, height: 1.35, color: AppTheme.body)),
          const SizedBox(height: 10),
          // A Wrap, not a Row: with large text the two buttons do not fit side
          // by side, and a Row would overflow rather than drop one below.
          Wrap(
            alignment: WrapAlignment.spaceBetween,
            crossAxisAlignment: WrapCrossAlignment.center,
            spacing: 10,
            runSpacing: 8,
            children: [
              if (a.owned)
                OutlinedButton(
                  onPressed: locked ? null : onToggle,
                  style: OutlinedButton.styleFrom(
                    foregroundColor: equipped ? AppTheme.accent : AppTheme.text,
                    side: BorderSide(color: equipped ? AppTheme.accent : AppTheme.border),
                    visualDensity: VisualDensity.compact,
                  ),
                  child: Text(equipped ? 'Taking it' : 'Take it'),
                )
              else
                const SizedBox.shrink(),
              if (cost == null)
                const Text('Top level', style: TextStyle(fontSize: 12.5, color: AppTheme.muted))
              else
                FilledButton(
                  onPressed: locked || !affordable ? null : onUpgrade,
                  style: FilledButton.styleFrom(visualDensity: VisualDensity.compact),
                  child: busy
                      ? const SizedBox.square(dimension: 14, child: CircularProgressIndicator(strokeWidth: 2))
                      : Text('${a.owned ? 'Level ${a.level + 1}' : 'Unlock'} · ${_fmt(cost)}'),
                ),
            ],
          ),
        ],
      ),
    );
  }
}
