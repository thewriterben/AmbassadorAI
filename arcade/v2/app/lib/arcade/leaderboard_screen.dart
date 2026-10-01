import 'dart:async';

import 'package:flutter/material.dart';

import '../audio.dart';
import '../theme.dart';
import '../ui_kit.dart';
import 'api.dart';
import 'entry.dart';
import 'progress.dart';

/// Weekly standings. XP collected since Monday 00:00 UTC, ranked by the
/// server. Recognition only — nothing here can be exchanged for anything.
///
/// Drawn in the 30 Sep design return's system (it predated it), because DGD
/// App 2.1 opens it from the Arcade tab's "Weekly standings" row (audit L3:
/// until then the app had no way to reach it). Ranks are plain numbers: the
/// gold, silver and rose coins the top three used to wear read as prizes on
/// a board that pays nothing, which the arcade plan keeps out of the app.
class LeaderboardScreen extends StatefulWidget {
  const LeaderboardScreen({super.key});

  @override
  State<LeaderboardScreen> createState() => _LeaderboardScreenState();
}

class _Row {
  final int rank;
  final String handle;
  final int xp;
  final bool you;
  _Row.fromJson(Map<String, dynamic> j)
      : rank = (j['rank'] as num).toInt(),
        handle = j['handle'] as String,
        xp = (j['xp'] as num).toInt(),
        you = j['you'] == true;
}

class _LeaderboardScreenState extends State<LeaderboardScreen> {
  List<_Row>? rows;
  String? error;
  String handle = '';
  int myXp = 0;
  int? myRank;
  bool inTop = false;
  int players = 0;
  DateTime? resetsAt;
  bool rerolling = false;
  Timer? _tick;

  @override
  void initState() {
    super.initState();
    _load();
    _tick = Timer.periodic(const Duration(minutes: 1), (_) => setState(() {}));
  }

  @override
  void dispose() {
    _tick?.cancel();
    super.dispose();
  }

  Future<void> _load() async {
    setState(() => error = null);
    try {
      await ArcadeApi.instance.init();
      final j = await ArcadeApi.instance.leaderboard();
      if (!mounted) return;
      final you = field<Map<String, dynamic>>(j, 'you');
      setState(() {
        rows = [for (final r in j['rows'] as List) _Row.fromJson(r as Map<String, dynamic>)];
        handle = you['handle'] as String? ?? '';
        myXp = (you['xp'] as num?)?.toInt() ?? 0;
        myRank = (you['rank'] as num?)?.toInt();
        inTop = you['inTop'] == true;
        players = (j['players'] as num?)?.toInt() ?? 0;
        resetsAt = DateTime.fromMillisecondsSinceEpoch(intField(j, 'resetsAt'), isUtc: true);
      });
      ArcadeProgress.instance.offline = false;
    } on ApiException catch (e) {
      ArcadeProgress.instance.offline = e.offline;
      if (mounted) {
        setState(() => error = e.offline
            ? 'The arcade server can\'t be reached. The standings are kept there.'
            : 'Could not load the standings (${e.code}).');
      }
    }
  }

  Future<void> _reroll() async {
    if (rerolling) return;
    setState(() => rerolling = true);
    Audio.instance.tap();
    try {
      final j = await ArcadeApi.instance.rerollHandle();
      if (!mounted) return;
      setState(() => handle = j['handle'] as String);
      ArcadeProgress.instance.handle = handle;
      await _load();
    } on ApiException catch (e) {
      if (!mounted) return;
      final left = e.body?['handle'] as String?;
      if (left != null) setState(() => handle = left);
      Audio.instance.invalid();
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
          content: Text(e.code == 'reroll_limit'
              ? 'Three new names a day is the limit, so the board stays recognisable.'
              : 'Could not change your name right now.')));
    } finally {
      if (mounted) setState(() => rerolling = false);
    }
  }

  String get _countdown {
    final r = resetsAt;
    if (r == null) return 'Monday to Sunday, UTC';
    final d = r.difference(DateTime.now().toUtc());
    if (d.isNegative) return 'Resetting now';
    if (d.inHours >= 24) return 'Resets in ${d.inDays}d ${d.inHours % 24}h';
    if (d.inHours >= 1) return 'Resets in ${d.inHours}h ${d.inMinutes % 60}m';
    return 'Resets in ${d.inMinutes}m';
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.bg,
      body: SafeArea(
        bottom: false,
        child: RefreshIndicator(
          onRefresh: _load,
          color: AppTheme.accent,
          backgroundColor: AppTheme.card,
          child: ListView(
            padding: const EdgeInsets.fromLTRB(24, 16, 24, 32),
            children: [
              ScreenHeader(
                title: 'Weekly standings',
                subtitle: _countdown,
                subtitleUnderTitle: true,
                onBack: () => leaveScreen(context),
              ),
              const SizedBox(height: 22),
              _you(),
              const SizedBox(height: 22),
              ..._body(),
              const SizedBox(height: 22),
              const InfoNotice('Recognition only. XP, points and badges have no monetary value and cannot be exchanged.'),
            ],
          ),
        ),
      ),
    );
  }

  /// Your name, your week, and the one thing you can change: the name.
  Widget _you() {
    return Container(
      padding: const EdgeInsets.fromLTRB(16, 14, 12, 14),
      decoration: AppTheme.glass(radius: 20, fill: AppTheme.card),
      child: Row(children: [
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            const Text('YOUR NAME ON THE BOARD', style: _kicker),
            const SizedBox(height: 6),
            Text(handle.isEmpty ? '—' : handle,
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w600, color: AppTheme.text)),
            const SizedBox(height: 4),
            Text(
              rows == null
                  ? ' '
                  : myXp > 0
                      ? '${myRank == null ? '' : 'Rank $myRank · '}$myXp XP this week'
                      : 'Not on the board yet this week',
              style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 12, color: AppTheme.body),
            ),
          ]),
        ),
        const SizedBox(width: 10),
        TextButton.icon(
          onPressed: rerolling || error != null ? null : _reroll,
          style: TextButton.styleFrom(
            foregroundColor: AppTheme.accent,
            side: const BorderSide(color: AppTheme.border),
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(99)),
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
          ),
          icon: rerolling
              ? const SizedBox(width: 14, height: 14, child: CircularProgressIndicator(strokeWidth: 2, color: AppTheme.accent))
              : const HugeIcon('reload', size: 16, color: AppTheme.accent),
          label: const Text('New name', style: TextStyle(fontSize: 13, fontWeight: FontWeight.w500)),
        ),
      ]),
    );
  }

  List<Widget> _body() {
    if (error != null) {
      return [
        Container(
          padding: const EdgeInsets.all(18),
          decoration: AppTheme.glass(radius: 20, fill: AppTheme.card),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(error!, style: const TextStyle(fontSize: 14, height: 1.4, color: AppTheme.text)),
            const SizedBox(height: 14),
            OutlinedButton(
              onPressed: _load,
              style: OutlinedButton.styleFrom(
                foregroundColor: AppTheme.text,
                side: const BorderSide(color: AppTheme.border),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(99)),
              ),
              child: const Text('Try again'),
            ),
          ]),
        ),
      ];
    }
    final list = rows;
    if (list == null) {
      return const [
        Padding(
          padding: EdgeInsets.symmetric(vertical: 40),
          child: Center(child: CircularProgressIndicator(color: AppTheme.accent)),
        ),
      ];
    }
    if (list.isEmpty) {
      return const [
        Text('Nobody is on the board this week yet.',
            style: TextStyle(fontSize: 16, fontWeight: FontWeight.w500, color: AppTheme.text)),
        SizedBox(height: 6),
        Text('Clear a Coin Quest level or fly When Pigs Fly, and you will be first.',
            style: TextStyle(fontSize: 14, height: 1.4, color: AppTheme.body)),
      ];
    }
    return [
      const Text('THIS WEEK', style: _kicker),
      const SizedBox(height: 10),
      for (final r in list) _row(r),
      if (!inTop && myXp > 0) ...[
        const SizedBox(height: 4),
        _row(_Row.fromJson({'rank': myRank ?? 0, 'handle': handle, 'xp': myXp, 'you': true})),
      ],
      const SizedBox(height: 10),
      Text('$players player${players == 1 ? '' : 's'} on the board this week.',
          style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 12, color: AppTheme.muted)),
    ];
  }

  Widget _row(_Row r) {
    return Container(
      margin: const EdgeInsets.only(bottom: 8),
      padding: const EdgeInsets.fromLTRB(14, 12, 16, 12),
      decoration: AppTheme.glass(
        radius: 16,
        fill: AppTheme.card,
        outline: r.you ? AppTheme.accent : AppTheme.border,
      ),
      child: Row(children: [
        SizedBox(
          width: 34,
          child: Text(r.rank > 0 ? '${r.rank}' : '—',
              style: TextStyle(
                  fontFamily: AppTheme.fontMono,
                  fontSize: 14,
                  fontWeight: FontWeight.w600,
                  color: r.you ? AppTheme.accent : AppTheme.muted)),
        ),
        Expanded(
          child: Text(r.handle,
              overflow: TextOverflow.ellipsis,
              style: TextStyle(
                  fontSize: 15,
                  fontWeight: r.you ? FontWeight.w600 : FontWeight.w500,
                  color: r.you ? AppTheme.accent : AppTheme.text)),
        ),
        if (r.you)
          const Padding(
            padding: EdgeInsets.only(right: 10),
            child: Text('YOU', style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, letterSpacing: 1.2, color: AppTheme.accent)),
          ),
        Text('${r.xp} XP',
            style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 14, fontWeight: FontWeight.w600, color: AppTheme.text)),
      ]),
    );
  }
}

const _kicker = TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, letterSpacing: 1.6, color: AppTheme.muted);
