import 'package:flutter/material.dart';

import '../audio.dart';
import '../dev.dart';
import '../match3/progress.dart' as m3;
import '../theme.dart';
import 'api.dart';
import 'progress.dart';

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
    final ok = await _confirm(
      title: 'Delete your play record?',
      body: 'This erases the anonymous record DGD holds for you: your XP, '
          'badges, streak and play history. It cannot be undone.\n\n'
          'Your Coin Quest progress on this phone is not affected.\n\n'
          'If you keep playing, a new anonymous record is created and you '
          'start from zero XP.',
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
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        title: const Text('Settings', style: TextStyle(fontSize: 18)),
      ),
      body: ListenableBuilder(
        listenable: ArcadeProgress.instance,
        builder: (_, __) {
          final p = ArcadeProgress.instance;
          return ListView(
            padding: const EdgeInsets.fromLTRB(20, 8, 20, 32),
            children: [
              const _Head('SOUND'),
              const _AudioRow(),
              const SizedBox(height: 26),

              const _Head('YOUR RECORD'),
              // The explanation goes above the figures, not below them: it is
              // the context for reading them, and it previously ended "the
              // record below is anonymous" while sitting underneath the record.
              const Text(
                'DGD Arcade has no accounts. We never ask for your name, email '
                'or phone number, and your leaderboard name is assigned from a '
                'word list rather than typed — so this record is anonymous.',
                style: TextStyle(fontSize: 13, color: AppTheme.muted, height: 1.45),
              ),
              const SizedBox(height: 12),
              _Row('Name on the leaderboard', p.handle ?? '—'),
              _Row('XP', '${p.xp}'),
              _Row('Badges', '${p.badges.length}'),
              const SizedBox(height: 26),

              const _Head('YOUR DATA'),
              _Danger(
                label: 'Delete my play record',
                blurb: 'Erases the anonymous record on DGD\'s server — XP, '
                    'badges, streak and play history. Your progress on this '
                    'phone is kept.',
                onTap: _busy ? null : _deleteRecord,
                busy: _busy,
              ),
              const SizedBox(height: 12),
              _Danger(
                label: 'Erase progress on this device',
                blurb: 'Clears Coin Quest levels, stars and best scores from '
                    'this phone. Your record on the server is kept.',
                onTap: _busy ? null : _eraseLocal,
              ),
              const SizedBox(height: 26),

              // Both flags are compile-time constants, so the whole label folds
              // to a literal and the widget can be const.
              const Center(
                child: Text(
                  'DGD Arcade${Dev.demoBuild ? ' · demo' : ''}${Dev.enabled ? ' · dev' : ''}',
                  style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 10, color: AppTheme.dim),
                ),
              ),
            ],
          );
        },
      ),
    );
  }
}

class _Head extends StatelessWidget {
  final String text;
  const _Head(this.text);

  @override
  Widget build(BuildContext context) => Padding(
        padding: const EdgeInsets.only(bottom: 12),
        child: Row(children: [
          Text(text,
              style: const TextStyle(
                  fontFamily: AppTheme.fontMono, fontSize: 10, letterSpacing: 1.4, color: AppTheme.muted)),
          const SizedBox(width: 10),
          const Expanded(child: Divider(color: AppTheme.border, height: 1)),
        ]),
      );
}

class _Row extends StatelessWidget {
  final String label, value;
  const _Row(this.label, this.value);

  @override
  Widget build(BuildContext context) => Padding(
        padding: const EdgeInsets.symmetric(vertical: 7),
        child: Row(children: [
          Expanded(child: Text(label, style: const TextStyle(fontSize: 14, color: AppTheme.body))),
          Text(value,
              style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 13, color: AppTheme.text)),
        ]),
      );
}

class _AudioRow extends StatefulWidget {
  const _AudioRow();

  @override
  State<_AudioRow> createState() => _AudioRowState();
}

class _AudioRowState extends State<_AudioRow> {
  @override
  Widget build(BuildContext context) {
    final a = Audio.instance;
    return Column(children: [
      SwitchListTile(
        contentPadding: EdgeInsets.zero,
        activeThumbColor: AppTheme.accent,
        title: const Text('Sound effects', style: TextStyle(fontSize: 14, color: AppTheme.body)),
        value: a.sfx,
        onChanged: (v) => setState(() => a.setSfx(v)),
      ),
      SwitchListTile(
        contentPadding: EdgeInsets.zero,
        activeThumbColor: AppTheme.accent,
        title: const Text('Music', style: TextStyle(fontSize: 14, color: AppTheme.body)),
        value: a.music,
        onChanged: (v) => setState(() => a.setMusic(v)),
      ),
    ]);
  }
}

class _Danger extends StatelessWidget {
  final String label, blurb;
  final VoidCallback? onTap;
  final bool busy;
  const _Danger({required this.label, required this.blurb, this.onTap, this.busy = false});

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.transparent,
      child: InkWell(
        borderRadius: BorderRadius.circular(14),
        onTap: onTap,
        child: Container(
          padding: const EdgeInsets.all(14),
          decoration: AppTheme.glass(radius: 14, outline: AppTheme.danger.withValues(alpha: 0.45)),
          child: Row(children: [
            Expanded(
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(label,
                    style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w600, color: AppTheme.danger)),
                const SizedBox(height: 4),
                Text(blurb, style: const TextStyle(fontSize: 12.5, color: AppTheme.muted, height: 1.4)),
              ]),
            ),
            const SizedBox(width: 10),
            if (busy)
              const SizedBox(
                  width: 16, height: 16, child: CircularProgressIndicator(strokeWidth: 2, color: AppTheme.danger))
            else
              const Icon(Icons.chevron_right, color: AppTheme.danger, size: 20),
          ]),
        ),
      ),
    );
  }
}
