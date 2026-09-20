import 'dart:async';

import 'package:flutter/material.dart';

import '../audio.dart';
import '../theme.dart';
import 'api.dart';
import 'progress.dart';

/// Weekly standings. XP earned since Monday 00:00 UTC, ranked by the server.
/// Recognition only — nothing here can be exchanged for anything.
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
            ? 'The arcade server is unreachable. Standings are ranked there.'
            : 'Could not load the standings (${e.code}).');
      }
    }
  }

  Future<void> _reroll() async {
    if (rerolling) return;
    setState(() => rerolling = true);
    Audio.instance.coinSpin();
    try {
      final j = await ArcadeApi.instance.rerollHandle();
      if (!mounted) return;
      setState(() => handle = j['handle'] as String);
      ArcadeProgress.instance.handle = handle;
      Audio.instance.ting();
      await _load();
    } on ApiException catch (e) {
      if (!mounted) return;
      final left = e.body?['handle'] as String?;
      if (left != null) setState(() => handle = left);
      Audio.instance.invalid();
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
          content: Text(e.code == 'reroll_limit'
              ? 'Three new names a day is the limit — the board needs to stay recognizable.'
              : 'Could not change your name right now.')));
    } finally {
      if (mounted) setState(() => rerolling = false);
    }
  }

  String get _countdown {
    final r = resetsAt;
    if (r == null) return '';
    final d = r.difference(DateTime.now().toUtc());
    if (d.isNegative) return 'resetting…';
    if (d.inHours >= 24) return 'resets in ${d.inDays}d ${d.inHours % 24}h';
    if (d.inHours >= 1) return 'resets in ${d.inHours}h ${d.inMinutes % 60}m';
    return 'resets in ${d.inMinutes}m';
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.bg,
      body: Stack(
        children: [
          Positioned.fill(child: Image.asset('assets/images/bg_dark.png', fit: BoxFit.cover)),
          SafeArea(
            child: Column(
              children: [
                _header(),
                Expanded(child: _body()),
                if (rows != null) _youStrip(),
                const Padding(
                  padding: EdgeInsets.fromLTRB(20, 6, 20, 12),
                  child: Text('Recognition only. XP and badges have no monetary value and cannot be exchanged.',
                      textAlign: TextAlign.center,
                      style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 10, height: 1.4, color: AppTheme.dim)),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _header() {
    return Padding(
      padding: const EdgeInsets.fromLTRB(8, 6, 20, 0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(children: [
            IconButton(onPressed: () => Navigator.pop(context), icon: const Icon(Icons.arrow_back, color: AppTheme.text)),
            const Text('WEEKLY STANDINGS',
                style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, letterSpacing: 1.2, color: AppTheme.muted)),
            const Spacer(),
            if (resetsAt != null)
              Text(_countdown.toUpperCase(),
                  style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 10, letterSpacing: 1, color: AppTheme.accent)),
          ]),
          Padding(
            padding: const EdgeInsets.fromLTRB(12, 2, 0, 12),
            child: Row(children: [
              Expanded(
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  const Text('YOU ARE',
                      style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 9, letterSpacing: 1.2, color: AppTheme.dim)),
                  const SizedBox(height: 2),
                  Text(handle.isEmpty ? '—' : handle,
                      overflow: TextOverflow.ellipsis,
                      style: const TextStyle(fontSize: 19, fontWeight: FontWeight.w600, color: AppTheme.text)),
                ]),
              ),
              TextButton.icon(
                onPressed: rerolling ? null : _reroll,
                icon: rerolling
                    ? const SizedBox(width: 13, height: 13, child: CircularProgressIndicator(strokeWidth: 2, color: AppTheme.accent))
                    : const Icon(Icons.casino_rounded, size: 15, color: AppTheme.accent),
                label: const Text('New name',
                    style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, color: AppTheme.accent)),
              ),
            ]),
          ),
        ],
      ),
    );
  }

  Widget _body() {
    if (error != null) {
      return Center(
        child: Container(
          margin: const EdgeInsets.all(24),
          padding: const EdgeInsets.all(20),
          decoration: AppTheme.glass(radius: 18, fill: AppTheme.card, outline: AppTheme.danger),
          child: Column(mainAxisSize: MainAxisSize.min, children: [
            const Icon(Icons.cloud_off_rounded, color: AppTheme.danger),
            const SizedBox(height: 10),
            Text(error!, textAlign: TextAlign.center, style: const TextStyle(color: AppTheme.text, height: 1.4)),
            const SizedBox(height: 14),
            FilledButton(onPressed: _load, child: const Text('Try again')),
          ]),
        ),
      );
    }
    final list = rows;
    if (list == null) return const Center(child: CircularProgressIndicator(color: AppTheme.accent));
    if (list.isEmpty) {
      return Center(
        child: Padding(
          padding: const EdgeInsets.all(32),
          child: Column(mainAxisSize: MainAxisSize.min, children: [
            Image.asset('assets/images/coin_gold.png', width: 56, height: 56),
            const SizedBox(height: 16),
            const Text('Nobody has scored this week yet.',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 17, fontWeight: FontWeight.w600, color: AppTheme.text)),
            const SizedBox(height: 8),
            const Text('Finish an expedition or the Daily Ledger and you will be first on the board.',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 13, height: 1.4, color: AppTheme.body)),
          ]),
        ),
      );
    }
    return RefreshIndicator(
      onRefresh: _load,
      color: AppTheme.accent,
      backgroundColor: AppTheme.card,
      child: ListView.builder(
        padding: const EdgeInsets.fromLTRB(16, 0, 16, 8),
        itemCount: list.length + 1,
        itemBuilder: (_, i) {
          if (i == list.length) {
            return Padding(
              padding: const EdgeInsets.fromLTRB(4, 14, 4, 0),
              child: Text('$players explorer${players == 1 ? '' : 's'} scored this week.',
                  style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 10, color: AppTheme.dim)),
            );
          }
          return _row(list[i]);
        },
      ),
    );
  }

  /// Top three wear the precious-metal coins; everyone else gets a mono rank.
  Widget _rank(int rank) {
    const medals = {1: 'coin_gold.png', 2: 'coin_silver.png', 3: 'coin_rose.png'};
    final medal = medals[rank];
    if (medal != null) {
      return SizedBox(
        width: 38,
        child: Stack(
          alignment: Alignment.center,
          children: [
            Image.asset('assets/images/$medal', width: 34, height: 34),
            Text('$rank',
                style: const TextStyle(
                    fontFamily: AppTheme.fontMono,
                    fontSize: 13,
                    fontWeight: FontWeight.w700,
                    color: Color(0xFF231703),
                    shadows: [Shadow(color: Color(0x66FFFFFF), blurRadius: 2)])),
          ],
        ),
      );
    }
    return SizedBox(
      width: 38,
      child: Text('$rank',
          textAlign: TextAlign.center,
          style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 14, fontWeight: FontWeight.w700, color: AppTheme.muted)),
    );
  }

  Widget _row(_Row r) {
    return Container(
      margin: const EdgeInsets.only(bottom: 6),
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 11),
      decoration: AppTheme.glass(
        radius: 14,
        fill: r.you ? const Color(0x1AEA952D) : AppTheme.glassFill,
        outline: r.you ? AppTheme.accent : AppTheme.border,
      ),
      child: Row(children: [
        _rank(r.rank),
        const SizedBox(width: 10),
        Expanded(
          child: Text(r.handle,
              overflow: TextOverflow.ellipsis,
              style: TextStyle(
                  fontSize: 15,
                  fontWeight: r.you ? FontWeight.w700 : FontWeight.w500,
                  color: r.you ? AppTheme.accent : AppTheme.text)),
        ),
        if (r.you)
          const Padding(
            padding: EdgeInsets.only(right: 8),
            child: Text('YOU',
                style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 9, letterSpacing: 1.2, color: AppTheme.accent)),
          ),
        Text('${r.xp}',
            style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 14, fontWeight: FontWeight.w700, color: AppTheme.text)),
        const SizedBox(width: 3),
        const Text('XP', style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 9, color: AppTheme.dim)),
      ]),
    );
  }

  /// Your standing, pinned, for when you are outside the visible slice.
  Widget _youStrip() {
    if (inTop) return const SizedBox.shrink();
    return Container(
      margin: const EdgeInsets.fromLTRB(16, 4, 16, 0),
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 11),
      decoration: AppTheme.glass(radius: 14, fill: const Color(0x1AEA952D), outline: AppTheme.accent),
      child: Row(children: [
        SizedBox(
          width: 38,
          child: Text(myRank == null ? '—' : '$myRank',
              textAlign: TextAlign.center,
              style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 14, fontWeight: FontWeight.w700, color: AppTheme.accent)),
        ),
        const SizedBox(width: 10),
        Expanded(
          child: Text(myXp > 0 ? handle : 'Not on the board yet',
              overflow: TextOverflow.ellipsis,
              style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w700, color: AppTheme.accent)),
        ),
        Text('$myXp',
            style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 14, fontWeight: FontWeight.w700, color: AppTheme.text)),
        const SizedBox(width: 3),
        const Text('XP', style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 9, color: AppTheme.dim)),
      ]),
    );
  }
}
