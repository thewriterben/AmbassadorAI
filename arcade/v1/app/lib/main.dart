import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import 'arcade/leaderboard_screen.dart';
import 'arcade/progress.dart';
import 'arcade/settings_screen.dart';
import 'audio.dart';
import 'match3/model/levels.dart';
import 'match3/progress.dart';
import 'match3/ui/level_map.dart';
import 'theme.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp]);
  SystemChrome.setSystemUIOverlayStyle(const SystemUiOverlayStyle(
    statusBarColor: Colors.transparent,
    statusBarIconBrightness: Brightness.light,
  ));
  Audio.instance.init();
  Progress.instance.load();
  ArcadeProgress.instance.load();
  Audio.instance.setTrack(Audio.trackMenu);
  runApp(const ArcadeApp());
}

class ArcadeApp extends StatelessWidget {
  const ArcadeApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: AppTheme.appName,
      theme: AppTheme.data,
      debugShowCheckedModeBanner: false,
      home: const HomeScreen(),
    );
  }
}

/// DGD Arcade home: Explorer track — XP, badges, three games.
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  void _open(BuildContext context, Widget screen) {
    Audio.instance.tap();
    Navigator.push(context, MaterialPageRoute(builder: (_) => screen));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          Positioned.fill(child: Image.asset('assets/images/bg_dark.png', fit: BoxFit.cover)),
          SafeArea(
            child: ListView(
              padding: const EdgeInsets.fromLTRB(20, 16, 20, 28),
              children: [
                Row(
                  children: [
                    Image.asset('assets/images/logo_orange.png', width: 28, height: 28),
                    const SizedBox(width: 10),
                    const Text('Digital Gold',
                        style: TextStyle(fontSize: 15, fontWeight: FontWeight.w600, color: AppTheme.text)),
                    const Text(' .CO', style: TextStyle(fontSize: 15, color: AppTheme.muted)),
                    const Spacer(),
                    const _AudioToggles(),
                  ],
                ),
                const SizedBox(height: 18),
                const Center(child: _HeroCoin(size: 150)),
                const SizedBox(height: 12),
                const _Kicker('PROOF OF PLAY'),
                const SizedBox(height: 10),
                RichText(
                  text: const TextSpan(
                    style: TextStyle(
                        fontFamily: AppTheme.fontSans,
                        fontSize: 34,
                        fontWeight: FontWeight.w600,
                        letterSpacing: -1.3,
                        height: 1.05,
                        color: AppTheme.text),
                    children: [
                      TextSpan(text: 'DGD '),
                      TextSpan(
                          text: 'Arcade',
                          style: TextStyle(
                              fontFamily: AppTheme.fontSerif,
                              fontStyle: FontStyle.italic,
                              fontWeight: FontWeight.w700,
                              color: AppTheme.accent)),
                    ],
                  ),
                ),
                const SizedBox(height: 6),
                const Text('Match the coins. Sixty levels through the making of Digital Gold.',
                    style: TextStyle(fontSize: 14, color: AppTheme.body, height: 1.4)),
                const SizedBox(height: 16),
                // XP, level and the standings link all come from the server.
                // Without one the bar would sit at level 1 with an OFFLINE chip
                // and a leaderboard link that goes nowhere.
                if (!ArcadeProgress.noBackend) ...[
                  const _XpBar(),
                  const SizedBox(height: 18),
                ],
                // The catalogue is Coin Quest alone while the next ten games
                // are built. No section heading — it would be labelling a list
                // of one — and no leading number, because there is no
                // catalogue for it to be sixth in.
                ListenableBuilder(
                  listenable: Progress.instance,
                  builder: (_, __) => _GameCard(
                    title: 'Coin Quest: Digital Gold',
                    kicker: 'MATCH-3',
                    blurb: 'Match the coins. ${Progress.instance.totalStars}/${levels.length * 3} stars.',
                    asset: 'assets/images/piece_gold.png',
                    primary: true,
                    onTap: () => _open(context, const LevelMapScreen()),
                  ),
                ),
                const SizedBox(height: 18),
                Center(
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                    decoration: AppTheme.glass(radius: 999, outline: AppTheme.border),
                    child: const Text('More games coming soon',
                        style: TextStyle(
                            fontFamily: AppTheme.fontMono,
                            fontSize: 11,
                            letterSpacing: 1.1,
                            color: AppTheme.muted)),
                  ),
                ),
                const SizedBox(height: 10),
                // Settings carries the two data-deletion controls, which both
                // stores expect to be reachable from inside the app. It sits
                // by the disclaimer because that is where people look for
                // privacy and legal controls — and because the header row is
                // already full: a third button there overflows by 26px on a
                // 432pt-wide screen, which widget_test catches.
                //
                // Kept compact deliberately. A default TextButton's 48pt tap
                // target plus its own padding pushed the no-monetary-value
                // disclaimer off the bottom of the first screen, and that line
                // is a compliance statement — it has to be readable without
                // scrolling. The tap target is still 36pt, above the 24pt
                // minimum for a secondary text link.
                Center(
                  child: TextButton(
                    style: TextButton.styleFrom(
                      minimumSize: const Size(0, 36),
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
                      tapTargetSize: MaterialTapTargetSize.shrinkWrap,
                    ),
                    onPressed: () {
                      Audio.instance.tap();
                      Navigator.push(context, MaterialPageRoute(builder: (_) => const SettingsScreen()));
                    },
                    child: const Text('Settings and your data',
                        style: TextStyle(
                            fontFamily: AppTheme.fontMono,
                            fontSize: 11,
                            letterSpacing: 0.8,
                            color: AppTheme.muted)),
                  ),
                ),
                const SizedBox(height: 6),
                const Center(
                  child: Text('Educational only. XP and badges have no monetary value.',
                      style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 10, color: AppTheme.dim)),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _XpBar extends StatelessWidget {
  const _XpBar();

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: ArcadeProgress.instance,
      builder: (_, __) {
        final p = ArcadeProgress.instance;
        return Material(
          color: Colors.transparent,
          child: InkWell(
            borderRadius: BorderRadius.circular(18),
            onTap: () {
              Audio.instance.tap();
              Navigator.push(context, MaterialPageRoute(builder: (_) => const LeaderboardScreen()));
            },
            child: Container(
          padding: const EdgeInsets.all(14),
          decoration: AppTheme.glass(radius: 18, fill: AppTheme.card.withValues(alpha: 0.85)),
          child: Column(children: [
            Row(children: [
              Text('LEVEL ${p.level}',
                  style: const TextStyle(
                      fontFamily: AppTheme.fontMono, fontSize: 11, letterSpacing: 1.2, color: AppTheme.accent)),
              if (p.offline) ...[
                const SizedBox(width: 10),
                GestureDetector(
                  onTap: p.refresh,
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                    decoration: AppTheme.glass(radius: 999, outline: AppTheme.danger.withValues(alpha: 0.6)),
                    child: const Row(mainAxisSize: MainAxisSize.min, children: [
                      Icon(Icons.cloud_off_rounded, size: 11, color: AppTheme.danger),
                      SizedBox(width: 4),
                      Text('OFFLINE',
                          style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 9, letterSpacing: 1, color: AppTheme.danger)),
                    ]),
                  ),
                ),
              ],
              const Spacer(),
              Text('${p.xp} XP',
                  style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 12, color: AppTheme.text)),
              const SizedBox(width: 12),
              const Icon(Icons.verified_rounded, size: 14, color: AppTheme.muted),
              const SizedBox(width: 4),
              Text('${p.badges.length}',
                  style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 12, color: AppTheme.muted)),
            ]),
            const SizedBox(height: 8),
            ClipRRect(
              borderRadius: BorderRadius.circular(999),
              child: LinearProgressIndicator(
                  value: p.levelProgress, minHeight: 6, backgroundColor: AppTheme.surface, color: AppTheme.accent),
            ),
            const SizedBox(height: 10),
            const Divider(height: 1, color: AppTheme.border),
            const SizedBox(height: 9),
            Row(children: [
              const Icon(Icons.leaderboard_rounded, size: 13, color: AppTheme.muted),
              const SizedBox(width: 6),
              const Flexible(
                child: Text('WEEKLY STANDINGS',
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 10, letterSpacing: 1.1, color: AppTheme.muted)),
              ),
              Expanded(
                child: Text('${p.weeklyXp} XP',
                    textAlign: TextAlign.right,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, color: AppTheme.text)),
              ),
              const SizedBox(width: 6),
              const Icon(Icons.arrow_forward_rounded, size: 13, color: AppTheme.accent),
            ]),
          ]),
            ),
          ),
        );
      },
    );
  }
}

class _GameCard extends StatelessWidget {
  final String title, kicker, blurb, asset;
  final bool primary;
  final VoidCallback onTap;
  const _GameCard(
      {required this.title,
      required this.kicker,
      required this.blurb,
      required this.asset,
      required this.onTap,
      this.primary = false});

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.transparent,
      child: InkWell(
        borderRadius: BorderRadius.circular(22),
        onTap: onTap,
        child: Container(
          padding: const EdgeInsets.all(16),
          decoration: AppTheme.glass(
              radius: 22,
              fill: AppTheme.card.withValues(alpha: 0.9),
              outline: primary ? AppTheme.accent.withValues(alpha: 0.6) : AppTheme.border),
          child: Row(children: [
            Image.asset(asset, width: 64, height: 64),
            const SizedBox(width: 14),
            Expanded(
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(kicker,
                    style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 10, letterSpacing: 1, color: AppTheme.muted)),
                const SizedBox(height: 3),
                Text(title,
                    style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w600, letterSpacing: -0.5, color: AppTheme.text)),
                const SizedBox(height: 3),
                Text(blurb, style: const TextStyle(fontSize: 13, color: AppTheme.body, height: 1.35)),
              ]),
            ),
            const SizedBox(width: 8),
            Icon(Icons.arrow_forward_rounded, color: primary ? AppTheme.accent : AppTheme.muted),
          ]),
        ),
      ),
    );
  }
}

/// The DGD coin: floating, glowing, with a specular sweep every few seconds.
class _HeroCoin extends StatefulWidget {
  final double size;
  const _HeroCoin({required this.size});

  @override
  State<_HeroCoin> createState() => _HeroCoinState();
}

class _HeroCoinState extends State<_HeroCoin> with TickerProviderStateMixin {
  late final AnimationController _float =
      AnimationController(vsync: this, duration: const Duration(seconds: 4))..repeat(reverse: true);
  late final AnimationController _sheen =
      AnimationController(vsync: this, duration: const Duration(milliseconds: 3600))
        ..addStatusListener((st) {
          if (st == AnimationStatus.forward || st == AnimationStatus.completed) Audio.instance.ting();
        })
        ..repeat();

  /// Tap response: the coin **flips**, end over end about its horizontal axis.
  ///
  /// The flip is the arcade's gesture and the spin is the DGD app's — the same
  /// coin, told apart by how it moves, so a player who has just come through
  /// from the ticker can feel they have arrived somewhere else. This used to
  /// alternate spin/flip on each tap; the alternation is what was given up to
  /// make the two surfaces distinguishable.
  late final AnimationController _toss =
      AnimationController(vsync: this, duration: const Duration(milliseconds: 900));

  void _tap() {
    // Ignore taps mid-toss rather than restarting: a coin that resets halfway
    // reads as a glitch, and the sound would retrigger on every jab.
    if (_toss.isAnimating) return;
    Audio.instance.coinFlip();
    _toss.forward(from: 0).then((_) {
      // A sparkle of sound on landing, at a gentle level — this is idle play,
      // not an achievement.
      if (mounted) Audio.instance.ting();
    });
  }

  @override
  void dispose() {
    _float.dispose();
    _sheen.dispose();
    _toss.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final s = widget.size;
    return AnimatedBuilder(
      animation: Listenable.merge([_float, _sheen, _toss]),
      builder: (_, __) {
        final f = Curves.easeInOut.transform(_float.value);
        final dy = -8 + 16 * f;
        final t = (_sheen.value / 0.3).clamp(0.0, 1.0);
        final x = -1.6 + 3.2 * t;

        // Two full turns, decelerating, so it settles face-on rather than
        // stopping edge-on where the coin would be invisible.
        final flip = Curves.easeOutCubic.transform(_toss.value) * pi * 4;
        // A small hop, peaking mid-toss.
        final hop = sin(_toss.value * pi) * s * 0.10;

        return Transform.translate(
          offset: Offset(0, dy - hop),
          child: GestureDetector(
            onTap: _tap,
            // The glow extends past the artwork, so without this only the
            // opaque pixels would take the tap.
            behavior: HitTestBehavior.opaque,
            child: Transform(
              alignment: Alignment.center,
              transform: Matrix4.identity()
                // Perspective, or the rotation reads as a flat squash.
                ..setEntry(3, 2, 0.0012)
                ..rotateX(flip),
              child: SizedBox(
            width: s * 1.3,
            height: s * 1.3,
            child: Stack(
              alignment: Alignment.center,
              children: [
                Container(
                  width: s * (1.1 + 0.08 * f),
                  height: s * (1.1 + 0.08 * f),
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    boxShadow: [
                      BoxShadow(
                          color: AppTheme.accent.withValues(alpha: 0.35 + 0.15 * f), blurRadius: 50, spreadRadius: 4),
                    ],
                  ),
                ),
                ShaderMask(
                  blendMode: BlendMode.srcATop,
                  shaderCallback: (rect) => LinearGradient(
                    begin: Alignment(x - 0.5, -1),
                    end: Alignment(x + 0.5, 1),
                    colors: const [Color(0x00FFFFFF), Color(0x80FFFFFF), Color(0x00FFFFFF)],
                    stops: const [0.35, 0.5, 0.65],
                  ).createShader(rect),
                      child: Image.asset('assets/images/coin_gold.png', width: s, height: s),
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

/// Sound / music toggles as small glass buttons.
class _AudioToggles extends StatelessWidget {
  const _AudioToggles();

  @override
  Widget build(BuildContext context) {
    final a = Audio.instance;
    return ListenableBuilder(
      listenable: a,
      builder: (_, __) => Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          _toggle(a.sfx ? Icons.volume_up_rounded : Icons.volume_off_rounded, a.sfx, () {
            a.setSfx(!a.sfx);
            a.tap();
          }),
          const SizedBox(width: 8),
          _toggle(a.music ? Icons.music_note_rounded : Icons.music_off_rounded, a.music, () {
            a.setMusic(!a.music);
            a.tap();
          }),
        ],
      ),
    );
  }

  Widget _toggle(IconData icon, bool on, VoidCallback onTap) => Material(
        color: Colors.transparent,
        child: InkWell(
          borderRadius: BorderRadius.circular(999),
          onTap: onTap,
          child: Container(
            width: 40,
            height: 40,
            decoration: AppTheme.glass(radius: 999, outline: on ? AppTheme.accent.withValues(alpha: 0.6) : AppTheme.border),
            child: Icon(icon, size: 20, color: on ? AppTheme.accent : AppTheme.dim),
          ),
        ),
      );
}

/// Site-style pill label: DGD mark + small mono uppercase.
class _Kicker extends StatelessWidget {
  final String text;
  const _Kicker(this.text);

  @override
  Widget build(BuildContext context) {
    return Row(children: [
      Container(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
        decoration: AppTheme.glass(radius: 999, outline: AppTheme.borderStrong),
        child: Row(mainAxisSize: MainAxisSize.min, children: [
          Image.asset('assets/images/logo_orange.png', width: 12, height: 12),
          const SizedBox(width: 8),
          Text(text,
              style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, letterSpacing: 1.2, color: AppTheme.text)),
        ]),
      ),
    ]);
  }
}
