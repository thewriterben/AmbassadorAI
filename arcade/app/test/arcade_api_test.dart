// Red-team coverage for the network and identity layer, 18 Sep 2026.
// See ../../AUDIT-2026-09-18.md.
//
// ArcadeApi is a private-constructor singleton with an inline http.Client and
// a compile-time base URL, so there is no seam for a mock client. Instead the
// tests stand up a real loopback HttpServer and point the app at it:
//
//   flutter test --dart-define=ARCADE_API=http://127.0.0.1:8799
//
// Without that define the group is skipped with a reason rather than silently
// passing. The cases run in order and share the singleton on purpose: the
// interesting behaviour is what the singleton does across a 401.

import 'dart:async';
import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/api.dart';
import 'package:puzzle_pack/arcade/progress.dart';
import 'package:puzzle_pack/dev.dart';
import 'package:shared_preferences/shared_preferences.dart';

class Seen {
  final String method;
  final String path;
  final String? auth;
  final Map<String, dynamic> body;
  Seen(this.method, this.path, this.auth, this.body);
}

/// A scripted server. `script` decides the reply for each request; everything
/// the client sends is recorded in `seen`.
class FakeServer {
  final HttpServer _server;
  final List<Seen> seen = [];
  (int, String) Function(Seen) script = (_) => (200, '{}');
  /// While set, every request waits on it before being answered.
  Completer<void>? hang;
  int issued = 0;
  FakeServer._(this._server);

  static Future<FakeServer> start(InternetAddress host, int port) async {
    final s = FakeServer._(await HttpServer.bind(host, port));
    s._server.listen(s._handle);
    return s;
  }

  Future<void> _handle(HttpRequest req) async {
    final raw = await utf8.decoder.bind(req).join();
    final body = raw.isEmpty ? <String, dynamic>{} : jsonDecode(raw) as Map<String, dynamic>;
    final s = Seen(req.method, req.uri.path, req.headers.value('authorization'), body);
    seen.add(s);
    if (hang != null) await hang!.future;
    final (status, text) = script(s);
    req.response
      ..statusCode = status
      ..headers.contentType = ContentType.json
      ..write(text);
    await req.response.close();
  }

  /// The ordinary happy path: register, report, pay.
  (int, String) happy(Seen s) {
    switch (s.path) {
      case '/v1/players':
        issued++;
        return (201, jsonEncode({'playerId': 'p_test$issued', 'token': 'tok$issued', 'progress': progress(10 * issued)}));
      case '/v1/me':
        return (200, jsonEncode(progress(42)));
      case '/v1/mini/coin_quest/start':
        return (201, jsonEncode({'token': 'round.nonce.9999999999999.sig'}));
      case '/v1/mini/coin_quest':
        return (200, jsonEncode({'xpGained': 60, 'badges': [], 'progress': progress(102)}));
      default:
        return (404, '{"error":"not_found"}');
    }
  }

  static Map<String, dynamic> progress(int xp) => {
        'handle': 'Quiet Ledger 123',
        'xp': xp,
        'weeklyXp': xp,
        'level': 1,
        'levelProgress': 0.1,
        'badges': <String>[],
        'miniPlays': <String, int>{},
      };

  Future<void> close() => _server.close(force: true);
}

void main() {
  final base = Uri.parse(ArcadeApi.base);
  final loop = base.host == '127.0.0.1' || base.host == 'localhost';
  final needsDefine = loop && base.port != 8787 ? null : 'needs --dart-define=ARCADE_API=http://127.0.0.1:<port> (not the dev server port)';
  final skip = needsDefine ?? (Dev.demoBuild ? 'not a demo build test; run without DGD_DEMO' : false);

  // Run with --dart-define=DGD_DEMO=true as well as ARCADE_API. A demo build
  // has no backend: cold start must not register a player, and a level start
  // must not open a round. This was open on 2026-09-18 (audit A1).
  group('a demo build never talks to the server', () {
    late FakeServer server;
    setUpAll(() async {
      SharedPreferences.setMockInitialValues({});
      server = await FakeServer.start(InternetAddress.loopbackIPv4, base.port);
      server.script = server.happy;
    });
    tearDownAll(() => server.close());

    test('cold start, refresh and a level start make zero requests', () async {
      await ArcadeProgress.instance.load();
      await ArcadeProgress.instance.refresh();
      expect(await ArcadeProgress.instance.startMini('coin_quest'), isNull);
      final (gained, _) = await ArcadeProgress.instance.recordMini('coin_quest', token: null, right: 3, total: 3);
      expect(gained, 0);
      await Future<void>.delayed(const Duration(milliseconds: 300));
      expect(server.seen, isEmpty, reason: 'a demo build registered or opened a round');
      expect(ArcadeApi.instance.ready, isFalse);
      expect(ArcadeProgress.instance.offline, isFalse, reason: 'no backend is not "offline"');
    });
  }, skip: needsDefine ?? (Dev.demoBuild ? false : 'run with --dart-define=DGD_DEMO=true'));

  group('ArcadeApi against a loopback server', () {
    late FakeServer server;

    setUpAll(() async {
      // Seed the cache with an absurd XP figure before either singleton has
      // touched SharedPreferences, so both see the same store.
      SharedPreferences.setMockInitialValues({
        'ar.snapshot': jsonEncode({...FakeServer.progress(999999), 'handle': 'Forged Handle 1'}),
      });
      server = await FakeServer.start(InternetAddress.loopbackIPv4, base.port);
      server.script = server.happy;
    });
    tearDownAll(() => server.close());

    test('concurrent init() registers exactly one anonymous player (F4 fix holds)', () async {
      await Future.wait([ArcadeApi.instance.init(), ArcadeApi.instance.init(), ArcadeApi.instance.init()]);
      expect(server.seen.where((s) => s.path == '/v1/players').length, 1);
      expect(server.seen.first.auth, isNull, reason: 'registration is unauthenticated');
      expect(ArcadeApi.instance.ready, isTrue);
      expect(ArcadeApi.instance.playerId, 'p_test1');
      await ArcadeApi.instance.me();
      expect(server.seen.last.auth, 'Bearer tok1');
    });

    test('the local cache paints first and is then overwritten by the server; it is never sent', () async {
      final p = ArcadeProgress.instance;
      var painted = <int>[];
      void spy() => painted.add(p.xp);
      p.addListener(spy);
      await p.load();
      p.removeListener(spy);
      expect(painted.first, 999999, reason: 'the cached snapshot renders immediately');
      expect(p.xp, 42, reason: 'and /v1/me replaces it');
      expect(p.handle, 'Quiet Ledger 123');
      expect(p.offline, isFalse);

      // Claiming a round sends only what the server needs to identify the
      // round and the reported score. Nothing from the cache rides along.
      server.seen.clear();
      final token = await p.startMini('coin_quest');
      expect(token, isNotNull);
      final (gained, badges) = await p.recordMini('coin_quest', token: token, right: 3, total: 3, extra: 7);
      expect(gained, 60);
      expect(badges, isEmpty);
      final claim = server.seen.singleWhere((s) => s.path == '/v1/mini/coin_quest');
      expect(claim.body.keys.toSet(), {'token', 'right', 'total', 'extra'});
      expect(claim.body, {'token': 'round.nonce.9999999999999.sig', 'right': 3, 'total': 3, 'extra': 7});
      expect(p.xp, 102, reason: 'the response progress wins again');
    });

    test('a 401 from any endpoint drops the identity, and the next call registers a new one', () async {
      server.seen.clear();
      server.script = (s) => s.path == '/v1/me' ? (401, '{"error":"unauthorized"}') : server.happy(s);
      await expectLater(
        ArcadeApi.instance.me(),
        throwsA(isA<ApiException>().having((e) => e.code, 'code', 'unauthorized').having((e) => e.status, 'status', 401)),
      );
      expect(ArcadeApi.instance.ready, isFalse, reason: 'token forgotten on 401');

      // This is the identity-churn finding: any 401 — a server reset, a
      // proxy misconfiguration, a hostile MITM on a cleartext dev URL —
      // silently costs the player their XP history and adds a ghost row to
      // the board, with no prompt and no way back.
      server.script = server.happy;
      await ArcadeProgress.instance.refresh();
      final regs = server.seen.where((s) => s.path == '/v1/players').toList();
      expect(regs.length, 1, reason: 'a second anonymous player was created');
      expect(ArcadeApi.instance.playerId, 'p_test2');
      expect(server.seen.last.auth, 'Bearer tok2');
      expect(ArcadeProgress.instance.offline, isFalse);
    });

    test('a malformed or wrong-shaped body surfaces as ApiException, never TypeError', () async {
      server.script = (s) => s.path == '/v1/me' ? (200, '{not json') : server.happy(s);
      await expectLater(
        ArcadeApi.instance.me(),
        throwsA(isA<ApiException>().having((e) => e.offline, 'offline', isTrue)),
      );
      server.script = (s) => s.path == '/v1/me' ? (200, '[1,2,3]') : server.happy(s);
      await expectLater(ArcadeApi.instance.me(), throwsA(isA<ApiException>()));
      // A 401 with a body that is not JSON is reported as offline, and the
      // token is kept: _decode parses before it looks at the status.
      server.script = (s) => s.path == '/v1/me' ? (401, 'nope') : server.happy(s);
      await expectLater(ArcadeApi.instance.me(), throwsA(isA<ApiException>().having((e) => e.status, 'status', 0)));
      expect(ArcadeApi.instance.ready, isTrue, reason: 'a non-JSON 401 does not clear the token');
      server.script = server.happy;

      // The typed readers refuse the wrong shape the same way.
      expect(() => field<String>({'a': 1}, 'a'), throwsA(isA<ApiException>()));
      expect(() => intField({'a': 'x'}, 'a'), throwsA(isA<ApiException>()));
      expect(() => stringsField({'a': [1]}, 'a'), throwsA(isA<ApiException>()));
      expect(intField({'a': 2.9}, 'a'), 2);
      expect(stringsField({'a': ['x']}, 'a'), ['x']);
    });

    test('a server that never answers times out as offline and leaves the identity alone', () async {
      server.hang = Completer<void>();
      await expectLater(
        ArcadeApi.instance.me().timeout(const Duration(seconds: 12)),
        throwsA(isA<ApiException>().having((e) => e.offline, 'offline', isTrue)),
      );
      expect(ArcadeApi.instance.ready, isTrue);
      server.hang!.complete();
      server.hang = null;
    }, timeout: const Timeout(Duration(seconds: 20)));
  }, skip: skip);
}
