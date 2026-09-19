import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import 'arcade/leaderboard_screen.dart';
import 'arcade/ledger/daily_ledger_screen.dart';
import 'arcade/mini/chain_builder_screen.dart';
import 'arcade/mini/design_or_myth_screen.dart';
import 'arcade/mini/pillar_sort_screen.dart';
import 'arcade/progress.dart';
import 'arcade/run/tablet_run_screen.dart';
import 'audio.dart';
import 'dev.dart';
import 'games/blocks_game.dart';
import 'games/merge_game.dart';
import 'games/rope_game.dart';
import 'games/words_game.dart';
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
                const Text(
                    Dev.demoBuild
                        // No expeditions in the demo, so don't promise them.
                        ? 'Match the coins. Sixty levels through the making of Digital Gold.'
                        : 'Learn how Digital Gold is designed — one expedition at a time.',
                    style: TextStyle(fontSize: 14, color: AppTheme.body, height: 1.4)),
                const SizedBox(height: 16),
                // XP, level and the standings link all come from the server.
                // Without one the bar would sit at level 1 with an OFFLINE chip
                // and a leaderboard link that goes nowhere.
                if (!Dev.demoBuild) ...[
                  const _XpBar(),
                  const SizedBox(height: 18),
                ],
                // Both of these are server-authoritative — see Dev.demoBuild.
                if (!Dev.demoBuild) ...[
                  const _Section('EXPEDITIONS'),
                  _GameCard(
                    title: 'Tablet Run',
                    kicker: '01 · EXPEDITION',
                    blurb: 'Roll from 1913 to the network. Three Knowledge Tablets gate the way.',
                    asset: 'assets/images/coin_gold.png',
                    primary: true,
                    onTap: () => _open(context, const TabletRunScreen()),
                  ),
                  const SizedBox(height: 12),
                  ListenableBuilder(
                    listenable: ArcadeProgress.instance,
                    builder: (_, __) {
                      final p = ArcadeProgress.instance;
                      return _GameCard(
                        title: 'Daily Ledger',
                        kicker: '02 · ONE PUZZLE A DAY',
                        blurb: p.ledgerDoneToday
                            ? 'Done for today · streak ${p.streak}. Back at 00:00 UTC.'
                            : 'Same puzzle for everyone. Six attempts. Keep the streak.',
                        asset: 'assets/images/word_correct.png',
                        onTap: () => _open(context, const DailyLedgerScreen()),
                      );
                    },
                  ),
                  const SizedBox(height: 18),
                ],
                if (!Dev.demoBuild) ...[
                  const _Section('KNOWLEDGE MINI-GAMES'),
                _GameCard(
                  title: 'Pillar Sort',
                  kicker: '03 · 60 SECONDS',
                  blurb: 'Statements fly in. Tap the pillar each one belongs to.',
                  asset: 'assets/images/piece_silver.png',
                  onTap: () => _open(context, const PillarSortScreen()),
                ),
                const SizedBox(height: 12),
                _GameCard(
                  title: 'Design or Myth?',
                  kicker: '04 · SWIPE',
                  blurb: 'Right if it\'s how DGD is built, left if it\'s a myth. The misconceptions ambassadors hear most.',
                  asset: 'assets/images/piece_red.png',
                  onTap: () => _open(context, const DesignOrMythScreen()),
                ),
                const SizedBox(height: 12),
                _GameCard(
                  title: 'Chain Builder',
                  kicker: '05 · ORDER THE LINKS',
                  blurb: 'Drag the supply chain, the release flow and custody steps into order.',
                  asset: 'assets/images/piece_copper.png',
                  onTap: () => _open(context, const ChainBuilderScreen()),
                ),
                const SizedBox(height: 18),
                ],
                // The demo is Coin Quest alone, so the section heading would be
                // labelling a list of one.
                if (!Dev.demoBuild) const _Section('ARCADE'),
                ListenableBuilder(
                  listenable: Progress.instance,
                  builder: (_, __) => _GameCard(
                    title: 'Coin Quest: Digital Gold',
                    // The numbering is a position in the catalogue; with one
                    // card there is no catalogue to be sixth in.
                    kicker: Dev.demoBuild ? 'MATCH-3' : '06 · MATCH-3',
                    blurb: 'Match the coins. ${Progress.instance.totalStars}/${levels.length * 3} stars.',
                    asset: 'assets/images/piece_gold.png',
                    onTap: () => _open(context, const LevelMapScreen()),
                  ),
                ),
                // Merge, Words, Blocks and Rope are at a rougher finish than
                // Coin Quest; showing them in the demo invites feedback on the
                // wrong things.
                if (!Dev.demoBuild) ...[
                const SizedBox(height: 12),
                _GameCard(
                  title: 'Merge',
                  kicker: '07 · SWIPE TO 2048',
                  blurb: 'Slide and double the tiles up to the DGD coin.',
                  asset: 'assets/images/merge_2048.png',
                  onTap: () => _open(context, const MergeGame()),
                ),
                const SizedBox(height: 12),
                _GameCard(
                  title: 'Words',
                  kicker: '08 · SIX GUESSES',
                  blurb: 'Five-letter word, six tries, unlimited rounds.',
                  asset: 'assets/images/word_present.png',
                  onTap: () => _open(context, const WordsGame()),
                ),
                const SizedBox(height: 12),
                _GameCard(
                  title: 'Blocks',
                  kicker: '09 · DROP AND CLEAR',
                  blurb: 'Falling ingots. Tap to rotate, swipe down to drop.',
                  asset: 'assets/images/block_0.png',
                  onTap: () => _open(context, const BlocksGame()),
                ),
                const SizedBox(height: 12),
                _GameCard(
                  title: 'Rope',
                  kicker: '10 · CUT AND CATCH',
                  blurb: 'Swipe the ropes so the coin lands in the vault.',
                  asset: 'assets/images/rope_treat.png',
                  onTap: () => _open(context, const RopeGame()),
                ),
                ],
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
                const SizedBox(height: 18),
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

class _Section extends StatelessWidget {
  final String text;
  const _Section(this.text);

  @override
  Widget build(BuildContext context) => Padding(
        padding: const EdgeInsets.only(bottom: 10),
        child: Row(children: [
          Text(text,
              style: const TextStyle(
                  fontFamily: AppTheme.fontMono, fontSize: 10, letterSpacing: 1.4, color: AppTheme.muted)),
          const SizedBox(width: 10),
          const Expanded(child: Divider(color: AppTheme.border, height: 1)),
        ]),
      );
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

  /// Tap response: the coin spins about its vertical axis or flips about its
  /// horizontal one, alternating so a run of taps doesn't repeat itself.
  late final AnimationController _toss =
      AnimationController(vsync: this, duration: const Duration(milliseconds: 900));
  bool _flip = false;

  void _tap() {
    // Ignore taps mid-toss rather than restarting: a coin that resets halfway
    // reads as a glitch, and the sound would retrigger on every jab.
    if (_toss.isAnimating) return;
    setState(() => _flip = !_flip);
    _flip ? Audio.instance.coinFlip() : Audio.instance.coinSpin();
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
        final spin = Curves.easeOutCubic.transform(_toss.value) * pi * 4;
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
                ..rotateY(_flip ? 0 : spin)
                ..rotateX(_flip ? spin : 0),
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
