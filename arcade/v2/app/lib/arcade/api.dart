import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

/// Thin client for the Arcade backend (arcade/server). The server is the
/// authority on XP, badges, streaks, which question is asked, and whether an
/// answer counts; this class just moves JSON.
///
/// Base URL: `--dart-define=ARCADE_API=https://…`. Without it, the web build
/// talks to same-origin `/api` (the host reverse-proxies that to the
/// backend, which keeps the page cross-origin isolated with no CORS), and
/// native builds talk to localhost:8787 — the dev server, reachable from a
/// USB-connected phone via `adb reverse tcp:8787 tcp:8787`.
class ArcadeApi {
  static final ArcadeApi instance = ArcadeApi._();
  ArcadeApi._();

  static const _env = String.fromEnvironment('ARCADE_API');

  /// Where the backend is, or empty when this build has none.
  ///
  /// Decided once by [resolveBase] from the environment and the build mode.
  /// [baseOverride] exists for tests only.
  static String get base => baseOverride ?? _resolvedBase;
  static final String _resolvedBase = resolveBase(
    env: _env,
    isWeb: kIsWeb,
    webOrigin: kIsWeb ? Uri.base : null,
    debug: kDebugMode,
  );
  @visibleForTesting
  static String? baseOverride;

  /// True when this build can talk to a server at all.
  static bool get hasBackend => base.isNotEmpty;

  /// Pure, so the release case can be tested: `flutter test` is always debug.
  ///
  /// The localhost fallback is for `flutter run` against the dev server and
  /// nothing else. Compiled into anything that leaves the machine it means
  /// "trust whatever is listening on 127.0.0.1:8787", which on Android is any
  /// installed app — the merged app's release candidate registered a player
  /// there at every launch (audit 2026-09-20, RC1). So the fallback exists in
  /// debug mode only; a release or profile build with no ARCADE_API has no
  /// backend, and behaves exactly like the demo.
  @visibleForTesting
  static String resolveBase({required String env, required bool isWeb, Uri? webOrigin, required bool debug}) {
    if (env.isNotEmpty) return env;
    if (isWeb && webOrigin != null) return webOrigin.resolve('/api').toString();
    return debug ? 'http://localhost:8787' : '';
  }

  /// Every request passes through here, so no caller — present or future —
  /// can reach a backend this build does not have. Callers already handle
  /// [ApiException]; this is the same contract with a code of its own.
  void _requireBackend() {
    if (!hasBackend) throw const ApiException('no_backend', 0, 'this build has no ARCADE_API');
  }
  static const _timeout = Duration(seconds: 8);

  final _client = http.Client();
  SharedPreferences? _prefs;
  String? _token;
  String? playerId;

  bool get ready => _token != null;

  /// In flight, if a registration is already running.
  ///
  /// The guard has to memoise the *Future*, not the token. `main()` fires
  /// `ArcadeProgress.load()` without awaiting it, so tapping a server-backed
  /// screen during that round trip re-entered `init()` with `_token` still
  /// null and registered a second anonymous player. The second response
  /// overwrote the stored token, orphaning any XP already credited to the
  /// first and leaving a ghost row on the weekly board.
  Future<void>? _initing;

  /// Loads the stored player token or registers an anonymous player.
  Future<void> init() {
    if (_token != null) return Future.value();
    return _initing ??= _init().whenComplete(() => _initing = null);
  }

  Future<void> _init() async {
    _prefs ??= await SharedPreferences.getInstance();
    _token = _prefs!.getString('api.token');
    playerId = _prefs!.getString('api.player');
    if (_token != null) return;
    final res = await _post('/v1/players', {'deviceHint': kIsWeb ? 'web' : defaultTargetPlatform.name}, auth: false);
    // A malformed body here would otherwise throw TypeError past every
    // `on ApiException` handler in the app.
    final token = res['token'], id = res['playerId'];
    if (token is! String || id is! String) {
      throw const ApiException('bad_player_response', 0, 'registration response was not usable');
    }
    _token = token;
    playerId = id;
    await _prefs!.setString('api.token', token);
    await _prefs!.setString('api.player', id);
  }

  Future<Map<String, dynamic>> me() => _get('/v1/me');

  /// Erases this player's server record, then forgets the local identity.
  ///
  /// The order matters. The stored token is the only way to name the record on
  /// the server, so clearing it first would leave an unreachable row behind and
  /// tell the player their data was deleted when it was not. The local wipe
  /// happens only after the server confirms.
  ///
  /// Afterwards the app has no identity at all. The next call to [init] simply
  /// registers a new anonymous player, which is the right behaviour: someone
  /// who deletes their record and keeps playing starts again from nothing.
  Future<void> deleteMe() async {
    await _delete('/v1/me');
    _token = null;
    playerId = null;
    final p = _prefs ??= await SharedPreferences.getInstance();
    await p.remove('api.token');
    await p.remove('api.player');
  }

  // Expeditions
  Future<Map<String, dynamic>> startExpedition() => _post('/v1/expeditions', {});
  Future<Map<String, dynamic>> openTablet(String exp, int idx) => _post('/v1/expeditions/$exp/tablets/$idx', {});
  Future<Map<String, dynamic>> answerTablet(String exp, int idx, {required String token, required int? choice}) =>
      _post('/v1/expeditions/$exp/tablets/$idx/answer', {'token': token, 'choice': choice});
  Future<Map<String, dynamic>> finishExpedition(String exp, {required int stumbles, required int runMs}) =>
      _post('/v1/expeditions/$exp/finish', {'stumbles': stumbles, 'runMs': runMs});

  // Daily Ledger
  Future<Map<String, dynamic>> ledgerToday() => _get('/v1/ledger/today');
  Future<Map<String, dynamic>> ledgerGuess(String guess) => _post('/v1/ledger/guess', {'guess': guess});

  // Scoreboard
  Future<Map<String, dynamic>> leaderboard({int limit = 50}) => _get('/v1/leaderboard?limit=$limit');
  Future<Map<String, dynamic>> rerollHandle() => _post('/v1/me/handle/reroll', {});

  // Mini-games (XP only).
  //
  // A round must be opened on the server before it can be claimed: the server
  // returns a signed single-use token, and only redeems it once, for the player
  // it was issued to, after a plausible amount of time has passed. Without the
  // token the claim is refused, which is what stops XP being minted by anyone
  // who can spell the endpoint.
  Future<String> miniStart(String game) async =>
      (await _post('/v1/mini/$game/start', {}))['token'] as String;

  Future<Map<String, dynamic>> miniResult(
    String game, {
    required String token,
    required int right,
    required int total,
    int extra = 0,
    int score = 0,
  }) =>
      _post('/v1/mini/$game', {'token': token, 'right': right, 'total': total, 'extra': extra, 'score': score});

  // ------------------------------------------------------------------ http

  Map<String, String> _headers({bool auth = true}) => {
        'content-type': 'application/json',
        if (auth && _token != null) 'authorization': 'Bearer $_token',
      };

  Future<Map<String, dynamic>> _get(String path) async {
    _requireBackend();
    try {
      final r = await _client.get(Uri.parse('$base$path'), headers: _headers()).timeout(_timeout);
      return _decode(r);
    } on ApiException {
      rethrow;
    } catch (e) {
      throw ApiException('offline', 0, '$e');
    }
  }

  Future<Map<String, dynamic>> _delete(String path) async {
    _requireBackend();
    try {
      final r = await _client.delete(Uri.parse('$base$path'), headers: _headers()).timeout(_timeout);
      return _decode(r);
    } on ApiException {
      rethrow;
    } catch (e) {
      throw ApiException('offline', 0, '$e');
    }
  }

  Future<Map<String, dynamic>> _post(String path, Map<String, dynamic> body, {bool auth = true}) async {
    _requireBackend();
    try {
      final r = await _client
          .post(Uri.parse('$base$path'), headers: _headers(auth: auth), body: jsonEncode(body))
          .timeout(_timeout);
      return _decode(r);
    } on ApiException {
      rethrow;
    } catch (e) {
      throw ApiException('offline', 0, '$e');
    }
  }

  Map<String, dynamic> _decode(http.Response r) {
    final json = r.body.isEmpty ? <String, dynamic>{} : jsonDecode(r.body) as Map<String, dynamic>;
    if (r.statusCode >= 400) {
      final code = json['error'] as String? ?? 'http_${r.statusCode}';
      if (r.statusCode == 401) {
        // Token no longer valid (server reset): forget it so the next init re-registers.
        _token = null;
        _prefs?.remove('api.token');
      }
      throw ApiException(code, r.statusCode, r.body, json);
    }
    return json;
  }
}

/// Reads a field from a server response, or fails as an [ApiException].
///
/// Every screen already handles `ApiException` — that is the contract for "the
/// server did not give us what we need". A bare `as` cast breaks that contract:
/// it raises `TypeError`, which sails past every `on ApiException` clause in the
/// app. One such cast in the Tablet Run question parser left the game paused
/// forever with the error swallowed, because the future was never awaited.
T field<T>(Map<String, dynamic> j, String key) {
  final v = j[key];
  if (v is T) return v;
  throw ApiException('bad_response', 0, 'expected $T at "$key", got ${v.runtimeType}', j);
}

/// Same, for numbers, which arrive as either int or double.
int intField(Map<String, dynamic> j, String key) {
  final v = j[key];
  if (v is num) return v.toInt();
  throw ApiException('bad_response', 0, 'expected a number at "$key", got ${v.runtimeType}', j);
}

List<String> stringsField(Map<String, dynamic> j, String key) {
  final v = j[key];
  if (v is List && v.every((e) => e is String)) return v.cast<String>();
  throw ApiException('bad_response', 0, 'expected a list of strings at "$key"', j);
}

class ApiException implements Exception {
  final String code;
  final int status;
  final String detail;
  final Map<String, dynamic>? body;
  const ApiException(this.code, this.status, this.detail, [this.body]);
  bool get offline => status == 0;
  @override
  String toString() => 'ApiException($code, $status)';
}
