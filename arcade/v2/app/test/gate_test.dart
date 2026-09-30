import 'package:flutter_test/flutter_test.dart';
import 'package:puzzle_pack/arcade/api.dart';
import 'package:puzzle_pack/dev.dart';

/// Makes an incomplete test run **red** instead of green-with-skips.
///
/// Finding D1, `AUDIT-DYNAMIC-1.0.5-2026-09-21.md`. Everything in
/// `arcade_api_test.dart` hangs off one `needsDefine` expression, so without
/// `--dart-define=ARCADE_API=http://127.0.0.1:<port>` the whole network layer
/// skips. Before this file, three different invocations all printed
/// *All tests passed* while running none of it:
///
///   flutter test                              45 passed,  8 skipped
///   flutter test --dart-define=DGD_DEMO=true  45 passed,  8 skipped
///
/// The second is the trap. It looks like the demo run and executes none of
/// the eight, including the one it appears to be for — the invariant that a
/// demo build makes zero requests, which is what the shipped review build
/// rests on.
///
/// The policy already warned that a plain run "does not count"
/// (`REDTEAM-POLICY.md` §4). A warning in a document does not fail a build.
/// This does.
///
/// **The waiver is deliberately noisy.** A partial run is legitimate during an
/// inner loop; it just has to be asked for, on the command line, where the
/// next person reading the command can see it:
///
///   flutter test --dart-define=DGD_ALLOW_PARTIAL=true
///
/// That is the policy's own reasoning about exemptions — an unreviewed waiver
/// is the cleanest place to hide a bypass, so make the bypass visible.
void main() {
  // Same condition as arcade_api_test.dart:96. If that one moves, the second
  // test below fails rather than this gate silently going slack.
  final base = Uri.parse(ArcadeApi.base);
  final loop = base.host == '127.0.0.1' || base.host == 'localhost';
  final loopbackReady = loop && base.port != 8787;

  const allowPartial = bool.fromEnvironment('DGD_ALLOW_PARTIAL');

  test('the network-layer suite is actually running', () {
    if (allowPartial) {
      markTestSkipped('waived with --dart-define=DGD_ALLOW_PARTIAL=true');
      return;
    }
    expect(
      loopbackReady,
      isTrue,
      reason: '\n'
          '  The arcade network tests are being SKIPPED, so this run proves\n'
          '  nothing about the API layer or the demo-build invariant.\n'
          '\n'
          '  Run both of these — neither alone covers everything:\n'
          '\n'
          '    flutter test --dart-define=ARCADE_API=http://127.0.0.1:8799\n'
          '    flutter test --dart-define=ARCADE_API=http://127.0.0.1:8799 \\\n'
          '                 --dart-define=DGD_DEMO=true\n'
          '\n'
          '  The second needs BOTH defines: proving "zero requests" requires a\n'
          '  live loopback listener to count the arrivals that never come.\n'
          '\n'
          '  For a deliberate partial run:\n'
          '    flutter test --dart-define=DGD_ALLOW_PARTIAL=true\n',
    );
  });

  test('a demo run without the loopback define would prove nothing', () {
    // The trap in one assertion. DGD_DEMO alone does not enable the demo test,
    // because needsDefine takes precedence over the demoBuild branch. If
    // someone later reorders that expression so DGD_DEMO alone is enough, this
    // fails and they find out here rather than in an audit.
    if (Dev.demoBuild && !loopbackReady) {
      fail('\n'
          '  DGD_DEMO=true is set but ARCADE_API is not, so the demo-build\n'
          '  test is skipped and this run does NOT check that a demo build\n'
          '  makes zero requests.\n'
          '\n'
          '    flutter test --dart-define=ARCADE_API=http://127.0.0.1:8799 \\\n'
          '                 --dart-define=DGD_DEMO=true\n');
    }
    expect(true, isTrue);
  });
}
