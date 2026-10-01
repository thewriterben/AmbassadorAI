import 'package:flutter/material.dart';

import '../audio.dart';
import '../dev.dart';
import '../match3/progress.dart' as m3;
import '../theme.dart';
import '../ui_kit.dart';
import 'api.dart';
import 'progress.dart';
import 'entry.dart';

/// Settings, and the two data-deletion controls.
///
/// Both app stores ask whether a user can request deletion of their data, and
/// both expect the route to be reachable from inside the app rather than only
/// by writing to a support address. This screen is that route.
///
/// The two deletions are deliberately separate and separately labelled. They
/// remove different things, live in different places, and someone reaching for
/// one of them almost never wants the other:
///
///  * **Play record** — the anonymous row on DGD's server: XP, badges, streak,
///    and the timings behind the anti-farming checks. This is the one the store
///    questionnaire is asking about.
///  * **Progress on this device** — Coin Quest level clears, stars and best
///    scores, held only in shared preferences and already removed by
///    uninstalling.
///
/// Folding them into one button would mean a player tapping a privacy control
/// silently loses sixty levels of progress, which is a nasty surprise dressed
/// up as a data-protection feature.
class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key});

  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  bool _busy = false;

  Future<void> _deleteRecord() async {
    if (ArcadeProgress.noBackend) {
      // Nothing to confirm and nothing to send: this build has no server,
      // so DGD holds no record for this player (review E4, 2026-09-30).
      _say('This version of the arcade has no server, so DGD holds no play '
          'record for you. There is nothing to delete.');
      return;
    }
    final ok = await _confirm(
      title: 'Delete your play record?',
      // Everything DELETE /v1/me removes that a player would notice, and
      // the boar in particular: its growth and abilities live on the server,
      // so deleting the record turns it back into a piglet (audit R12).
      body: 'This erases the anonymous record DGD holds for you: your XP, '
          'badges, your boar\'s growth and abilities, and your play history. '
          'It cannot be undone.\n\n'
          'Your Coin Quest progress on this phone is not affected.\n\n'
          'If you keep playing, a new anonymous record is created: you start '
          'from zero XP, with a piglet.',
      action: 'Delete record',
    );
    if (!ok || !mounted) return;

    setState(() => _busy = true);
    String? error;
    try {
      await ArcadeProgress.instance.deleteAccount();
    } on ApiException catch (e) {
      // Being honest here is the whole point. A failed delete must not read
      // like a successful one.
      error = e.code == 'offline'
          ? 'Could not reach the server, so nothing was deleted. Check your '
              'connection and try again.'
          : 'The server refused the request, so nothing was deleted.';
    } catch (_) {
      error = 'Something went wrong, so nothing was deleted.';
    }
    if (!mounted) return;
    setState(() => _busy = false);
    _say(error ?? 'Your play record has been deleted.', bad: error != null);
  }

  Future<void> _eraseLocal() async {
    final ok = await _confirm(
      title: 'Erase progress on this device?',
      body: 'This clears your Coin Quest level clears, stars and best scores '
          'from this phone. It cannot be undone.\n\n'
          'Your record on DGD\'s server is not affected.',
      action: 'Erase progress',
    );
    if (!ok || !mounted) return;
    await m3.Progress.instance.eraseAll();
    if (!mounted) return;
    _say('Progress on this device erased.');
  }

  Future<bool> _confirm({required String title, required String body, required String action}) async {
    final r = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        backgroundColor: AppTheme.card,
        title: Text(title, style: const TextStyle(fontSize: 18, color: AppTheme.text)),
        content: Text(body, style: const TextStyle(fontSize: 14, color: AppTheme.body, height: 1.45)),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx, false),
            child: const Text('Cancel', style: TextStyle(color: AppTheme.muted)),
          ),
          TextButton(
            onPressed: () => Navigator.pop(ctx, true),
            child: Text(action, style: const TextStyle(color: AppTheme.danger, fontWeight: FontWeight.w600)),
          ),
        ],
      ),
    );
    return r ?? false;
  }

  void _say(String msg, {bool bad = false}) {
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(
      content: Text(msg),
      backgroundColor: bad ? AppTheme.danger.withValues(alpha: 0.92) : AppTheme.card,
      behavior: SnackBarBehavior.floating,
      duration: const Duration(seconds: 5),
    ));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.bg,
      body: SafeArea(
        child: ListenableBuilder(
          listenable: ArcadeProgress.instance,
          builder: (_, __) {
            final p = ArcadeProgress.instance;
            return ListView(
              padding: const EdgeInsets.fromLTRB(24, 16, 24, 32),
              children: [
                ScreenHeader(title: 'Settings', onBack: () => leaveScreen(context)),
                const SizedBox(height: 12),
                // Both flags are compile-time constants, so the whole label folds
                // to a literal and the widget can be const.
                const Text(
                  'DGD Arcade${Dev.demoBuild ? ' · demo' : ''}${Dev.enabled ? ' · dev' : ''}',
                  style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 13, color: AppTheme.body),
                ),
                const SizedBox(height: 12),
                const _Head('Sound'),
                const _AudioCard(),
                const SizedBox(height: 30),

                const _Head('Your record'),
                // The explanation goes above the figures, not below them: it is
                // the context for reading them.
                _Card(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text('Anonymous play record',
                          style: TextStyle(fontSize: 18, fontWeight: FontWeight.w500, color: AppTheme.text)),
                      const SizedBox(height: 14),
                      const Text(
                        'No accounts. We never ask for your name, email or phone. '
                        'Your leaderboard name is assigned from a word list.',
                        style: TextStyle(fontSize: 15, height: 1.4, color: AppTheme.body),
                      ),
                      const SizedBox(height: 18),
                      Row(children: [
                        const Expanded(
                          child: Text('Name on the leaderboard', style: TextStyle(fontSize: 14, color: AppTheme.body)),
                        ),
                        Text(p.handle ?? '—',
                            style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 14, color: AppTheme.text)),
                      ]),
                      const SizedBox(height: 18),
                      Row(children: [
                        Expanded(child: _Stat('XP', '${p.xp}')),
                        const SizedBox(width: 12),
                        Expanded(child: _Stat('Badges', '${p.badges.length}')),
                      ]),
                    ],
                  ),
                ),
                const SizedBox(height: 30),

                const _Head('Your data'),
                _Danger(
                  label: 'Delete my play record',
                  blurb: 'Erases your XP, badges, boar\'s growth, abilities and play '
                      'history from DGD\'s server. Progress on this phone is kept.',
                  onTap: _busy ? null : _deleteRecord,
                  busy: _busy,
                ),
                const SizedBox(height: 12),
                _Danger(
                  label: 'Erase progress on this device',
                  blurb: 'Clears levels, stars and best scores from this phone. '
                      'Your server record is kept.',
                  onTap: _busy ? null : _eraseLocal,
                ),
              ],
            );
          },
        ),
      ),
    );
  }
}

/// A section label: Geist Mono, sentence case, secondary.
class _Head extends StatelessWidget {
  final String text;
  const _Head(this.text);

  @override
  Widget build(BuildContext context) => Padding(
        padding: const EdgeInsets.only(bottom: 16),
        child: Text(text, style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 13, color: AppTheme.body)),
      );
}

/// A settings card: the card colour, a hairline edge, generous padding.
class _Card extends StatelessWidget {
  final Widget child;
  final EdgeInsets padding;
  const _Card({required this.child, this.padding = const EdgeInsets.all(24)});

  @override
  Widget build(BuildContext context) => Container(
        width: double.infinity,
        padding: padding,
        decoration: BoxDecoration(
          color: AppTheme.card,
          borderRadius: BorderRadius.circular(24),
          border: Border.all(color: AppTheme.border),
        ),
        child: child,
      );
}

/// One figure of the record in its inset tile.
class _Stat extends StatelessWidget {
  final String label, value;
  const _Stat(this.label, this.value);

  @override
  Widget build(BuildContext context) => Container(
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 14),
        decoration: BoxDecoration(color: AppTheme.surface, borderRadius: BorderRadius.circular(16)),
        child: Row(children: [
          Expanded(child: Text(label, style: const TextStyle(fontSize: 14, color: AppTheme.body))),
          Text(value, style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 17, color: AppTheme.text)),
        ]),
      );
}

class _AudioCard extends StatefulWidget {
  const _AudioCard();

  @override
  State<_AudioCard> createState() => _AudioCardState();
}

class _AudioCardState extends State<_AudioCard> {
  Widget _row(String icon, String label, bool value, ValueChanged<bool> onChanged) => MergeSemantics(
        child: InkWell(
          onTap: () => onChanged(!value),
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 14),
            child: Row(children: [
              HugeIcon(icon, size: 22, color: AppTheme.body),
              const SizedBox(width: 16),
              Expanded(child: Text(label, style: const TextStyle(fontSize: 16, color: AppTheme.text))),
              Switch(
                value: value,
                onChanged: onChanged,
                activeTrackColor: AppTheme.accent,
                activeThumbColor: AppTheme.onAccent,
                inactiveTrackColor: AppTheme.surface,
                inactiveThumbColor: AppTheme.body,
                trackOutlineColor: WidgetStateProperty.resolveWith(
                    (s) => s.contains(WidgetState.selected) ? AppTheme.accent : AppTheme.border),
              ),
            ]),
          ),
        ),
      );

  @override
  Widget build(BuildContext context) {
    final a = Audio.instance;
    return _Card(
      padding: const EdgeInsets.symmetric(vertical: 10),
      child: Column(children: [
        _row('volume_high', 'Sound effects', a.sfx, (v) => setState(() => a.setSfx(v))),
        _row('music_note1', 'Music', a.music, (v) => setState(() => a.setMusic(v))),
      ]),
    );
  }
}

/// A destructive action: its name in the danger colour, what it does, and
/// the bin. The card itself stays neutral; the colour is in the words.
class _Danger extends StatelessWidget {
  final String label, blurb;
  final VoidCallback? onTap;
  final bool busy;
  const _Danger({required this.label, required this.blurb, this.onTap, this.busy = false});

  @override
  Widget build(BuildContext context) {
    return Material(
      color: AppTheme.card,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24), side: const BorderSide(color: AppTheme.border)),
      child: InkWell(
        borderRadius: BorderRadius.circular(24),
        onTap: onTap,
        child: Padding(
          padding: const EdgeInsets.fromLTRB(24, 20, 20, 22),
          child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Expanded(
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(label, style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w500, color: AppTheme.danger)),
                const SizedBox(height: 10),
                Text(blurb, style: const TextStyle(fontSize: 14, height: 1.45, color: AppTheme.body)),
              ]),
            ),
            const SizedBox(width: 12),
            if (busy)
              const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(strokeWidth: 2, color: AppTheme.danger))
            else
              const HugeIcon('delete2', size: 22, color: AppTheme.danger),
          ]),
        ),
      ),
    );
  }
}
