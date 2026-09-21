import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../dev.dart';
import 'api.dart';

/// Explorer-track progress as the server last reported it. XP, badges and
/// streaks are computed server-side (arcade/server); this is a read cache so
/// the home screen renders instantly and survives being offline. No monetary
/// value anywhere.
class ArcadeProgress extends ChangeNotifier {
  static final ArcadeProgress instance = ArcadeProgress._();
  ArcadeProgress._();

  SharedPreferences? _p;
  String? handle; // assigned display name, shown on the weekly board
  int xp = 0;
  int weeklyXp = 0;
  int level = 1;
  double levelProgress = 0;
  int expeditions = 0;
  int expeditionsComplete = 0;
  int tabletsCorrect = 0;
  int ledgersSolved = 0;
  int streak = 0;
  int? lastLedgerDay;
  int day = 0;
  bool ledgerDoneToday = false;
  int rewardedExpeditionsToday = 0;
  int rewardedExpeditionsPerDay = 2;
  double mastery = 0;
  final Set<String> badges = {};
  final Map<String, int> miniPlays = {};

  /// True when the last server call failed; XP shown may be stale.
  bool offline = false;
  bool _loaded = false;

  Future<void> load() async {
    _p ??= await SharedPreferences.getInstance();
    if (!_loaded) {
      final cached = _p!.getString('ar.snapshot');
      if (cached != null) apply(jsonDecode(cached) as Map<String, dynamic>, persist: false);
      _loaded = true;
    }
    await refresh();
  }

  /// Pulls the current snapshot from the server; flips [offline] on failure.
  ///
  /// A demo build has no backend and must never register a player. This was
  /// the one unguarded path: `main()` calls [load] on every cold start, and
  /// [ArcadeApi.init] registers an anonymous player the first time it is
  /// reached, so a demo that could reach a server created an identity on
  /// launch (audit 2026-09-18, A1). The gate lives here rather than in
  /// `main()` so no future caller of [refresh] can reopen it.
  Future<void> refresh() async {
    if (Dev.demoBuild) {
      notifyListeners();
      return;
    }
    try {
      await ArcadeApi.instance.init();
      apply(await ArcadeApi.instance.me());
      offline = false;
    } on ApiException {
      offline = true;
    } catch (_) {
      offline = true;
    }
    notifyListeners();
  }

  /// Applies a `progress` object from any API response.
  void apply(Map<String, dynamic> s, {bool persist = true}) {
    int i(String k, [int d = 0]) => (s[k] as num?)?.toInt() ?? d;
    handle = s['handle'] as String? ?? handle;
    xp = i('xp');
    weeklyXp = i('weeklyXp');
    level = i('level', 1);
    levelProgress = (s['levelProgress'] as num?)?.toDouble() ?? 0;
    expeditions = i('expeditions');
    expeditionsComplete = i('expeditionsComplete');
    tabletsCorrect = i('tabletsCorrect');
    ledgersSolved = i('ledgersSolved');
    streak = i('streak');
    lastLedgerDay = (s['lastLedgerDay'] as num?)?.toInt();
    if (s['day'] != null) day = i('day');
    if (s['ledgerDoneToday'] != null) ledgerDoneToday = s['ledgerDoneToday'] == true;
    if (s['rewardedExpeditionsToday'] != null) rewardedExpeditionsToday = i('rewardedExpeditionsToday');
    if (s['rewardedExpeditionsPerDay'] != null) rewardedExpeditionsPerDay = i('rewardedExpeditionsPerDay');
    if (s['mastery'] != null) mastery = (s['mastery'] as num).toDouble();
    badges
      ..clear()
      ..addAll((s['badges'] as List?)?.cast<String>() ?? const []);
    miniPlays
      ..clear()
      ..addAll(((s['miniPlays'] as Map?) ?? const {}).map((k, v) => MapEntry(k as String, (v as num).toInt())));
    if (persist) _p?.setString('ar.snapshot', jsonEncode(s));
    offline = false;
    notifyListeners();
  }

  /// Deletes the server-side play record and resets this cache to a new player.
  ///
  /// Throws [ApiException] if the server cannot be reached. That is deliberate:
  /// the screen must be able to say "we could not reach the server, nothing was
  /// deleted" rather than clearing the local cache and implying otherwise. An
  /// offline delete is not a delete.
  ///
  /// The cached snapshot is dropped too — leaving it would show the deleted
  /// player's XP and badges on the home screen until the next refresh.
  Future<void> deleteAccount() async {
    await ArcadeApi.instance.deleteMe();
    final p = _p ??= await SharedPreferences.getInstance();
    await p.remove('ar.snapshot');
    handle = null;
    xp = weeklyXp = expeditions = expeditionsComplete = 0;
    tabletsCorrect = ledgersSolved = streak = 0;
    level = 1;
    levelProgress = 0;
    mastery = 0;
    lastLedgerDay = null;
    ledgerDoneToday = false;
    rewardedExpeditionsToday = 0;
    badges.clear();
    miniPlays.clear();
    offline = false;
    notifyListeners();
  }

  /// Opens a server-issued round. Call when the player actually starts playing.
  ///
  /// Returns null when the server is unreachable; [recordMini] then no-ops
  /// rather than failing loudly, which is the same shape as before for an
  /// offline player.
  Future<String?> startMini(String game) async {
    if (Dev.demoBuild) return null; // no backend in the demo
    try {
      return await ArcadeApi.instance.miniStart(game);
    } on ApiException {
      offline = true;
      notifyListeners();
      return null;
    }
  }

  /// Claims a round opened by [startMini]; the server applies the XP formula
  /// and caps. Returns (xpGained, newBadges).
  ///
  /// [token] is required by the server — a round it never issued is not paid.
  /// A null token means the round was never opened (offline, or a demo build),
  /// so there is nothing to claim.
  Future<(int, List<String>)> recordMini(
    String game, {
    required String? token,
    required int right,
    required int total,
    int extra = 0,
    int score = 0,
  }) async {
    if (token == null) return (0, const <String>[]);
    try {
      final r = await ArcadeApi.instance
          .miniResult(game, token: token, right: right, total: total, extra: extra, score: score);
      // These casts are deliberately inside the try, but a malformed body
      // raises TypeError rather than ApiException, so catch broadly: a bad
      // response must not dead-end a results screen.
      apply(r['progress'] as Map<String, dynamic>);
      return ((r['xpGained'] as num).toInt(), (r['badges'] as List).cast<String>());
    } catch (e) {
      offline = true;
      notifyListeners();
      return (0, const <String>[]);
    }
  }

  static const badgeNames = {
    'first_expedition': 'First Expedition',
    'ten_tablets': 'Ten Tablets',
    'fifty_tablets': 'Fifty Tablets',
    'streak_3': '3-Day Ledger Streak',
    'streak_7': '7-Day Ledger Streak',
    'streak_30': '30-Day Ledger Streak',
    'level_5': 'Level 5 Explorer',
    'sorter': 'Pillar Sorter',
    'mythbuster': 'Myth Buster',
    'chainsmith': 'Chainsmith',
  };
}
