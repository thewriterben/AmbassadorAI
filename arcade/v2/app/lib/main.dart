import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import 'arcade/leaderboard_screen.dart';
import 'arcade/passage/pigs_home_screen.dart';
import 'arcade/progress.dart';
import 'arcade/settings_screen.dart';
import 'audio.dart';
import 'match3/model/levels.dart';
import 'match3/progress.dart';
import 'match3/ui/level_map.dart';
import 'theme.dart';
import 'ui_kit.dart';
import 'arcade/entry.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  registerDesignLicences();
  // Inside the DGD app, the app says which screen to open (arcade/entry.dart).
  ArcadeEntry.home = () => const HomeScreen();
  ArcadeEntry.listen();
  SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp]);
  SystemChrome.setSystemUIOverlayStyle(const SystemUiOverlayStyle(
    statusBarColor: Colors.transparent,
    statusBarIconBrightness: Brightness.light,
  ));
  Audio.instance.init();
  Progress.instance.load();
  ArcadeProgress.instance.load();
  // No music here: the arcade's menus are silent, and each game claims its
  // own track (Audio.claimMusic).
  runApp(const ArcadeApp());
}

class ArcadeApp extends StatelessWidget {
  const ArcadeApp({super.key});

  @override
  Widget build(BuildContext context) {
    WidgetsBinding.instance.addPostFrameCallback((_) => ArcadeEntry.takePending());
    return MaterialApp(
      navigatorKey: ArcadeEntry.navigator,
      title: AppTheme.appName,
      theme: AppTheme.data,
      debugShowCheckedModeBanner: false,
      home: const HomeScreen(),
    );
  }
}

/// DGD Arcade home, as the 2026-09-30 design return draws it: a header with
/// the sound and music buttons, Coin Quest's card with its board and its Play
/// button, the stars row, When Pigs Fly's card (the return drew Coin Quest
/// alone; this card follows the same rules), settings, and the notice.
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  void _open(BuildContext context, Widget screen) {
    Audio.instance.tap();
    Navigator.push(context, MaterialPageRoute(builder: (_) => screen));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.bg,
      body: SafeArea(
        // Same cap as the host app's ticker column, and for the same
        // reason: embedded in the DGD app at targetSdk 36, Android hands
        // this a ~1280dp-wide window on any tablet or unfolded foldable,
        // whatever the manifest asks for. Uncapped, the game cards become
        // metre-wide bars with their icon at one end and their arrow at
        // the other. The game boards are unaffected — they size
        // themselves from the shorter edge already.
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 520),
            child: ListView(
              padding: const EdgeInsets.fromLTRB(24, 16, 24, 28),
              children: [
                ScreenHeader(
                  title: 'Arcade',
                  subtitle: 'Discover through play.',
                  // Inside the DGD app the arcade is its own screen, and the
                  // design gives it a back button to the app. Standalone it is
                  // the app, and there is nothing behind it to go back to.
                  onBack: Audio.inAppTab ? () => SystemNavigator.pop() : null,
                  actions: const [_AudioToggles()],
                ),
                const SizedBox(height: 22),
                ListenableBuilder(
                  listenable: Progress.instance,
                  builder: (_, __) => _CoinQuestCard(onPlay: () => _open(context, const LevelMapScreen())),
                ),
                const SizedBox(height: 16),
                ListenableBuilder(
                  listenable: Progress.instance,
                  builder: (_, __) => _StarsRow(stars: Progress.instance.totalStars, of: levels.length * 3),
                ),
                const SizedBox(height: 12),
                // When Pigs Fly (id `passage`) ships in the demo build as well as the dev one. It
                // needs no backend — `startMini` no-ops without a server and
                // the run simply pays no XP — so the reason the old games were
                // cut from the demo does not apply to it. If it should be held
                // back from a tester build after all, wrap this card in
                // `if (!Dev.demoBuild)`; nothing else has to change.
                RowCard(
                  leading: Image.asset('assets/images/card_pigs.png', width: 34, height: 34),
                  title: 'When Pigs Fly',
                  subtitle: 'Fly a winged piggy bank through nine eras of money, and land it.',
                  onTap: () => _open(context, const PigsHomeScreen()),
                ),
                // XP, level and the standings link all come from the server.
                // Without one the bar would sit at level 1 with an OFFLINE chip
                // and a leaderboard link that goes nowhere.
                if (!ArcadeProgress.noBackend) ...[
                  const SizedBox(height: 12),
                  const _XpBar(),
                ],
                const SizedBox(height: 22),
                const Center(
                  child: Text('More games coming soon', style: TextStyle(fontSize: 14, color: AppTheme.body)),
                ),
                const SizedBox(height: 22),
                // Settings carries the two data-deletion controls, which both
                // stores expect to be reachable from inside the app.
                RowCard(
                  leading: const HugeIcon('settings2', size: 20, color: AppTheme.body),
                  title: 'Settings and your data',
                  onTap: () => _open(context, const SettingsScreen()),
                ),
                const SizedBox(height: 26),
                // Verbatim, as the design return requires. When Pigs Fly's own
                // screens say the same of its points and coins.
                const InfoNotice('Educational only. XP and badges have no monetary value.'),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

/// Coin Quest's card: kicker, name, three words, the board, and Play.
class _CoinQuestCard extends StatelessWidget {
  final VoidCallback onPlay;
  const _CoinQuestCard({required this.onPlay});

  @override
  Widget build(BuildContext context) {
    return Container(
      clipBehavior: Clip.antiAlias,
      decoration: BoxDecoration(
        color: AppTheme.card,
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: AppTheme.border),
      ),
      child: Column(
        children: [
          // The upper part carries a faint warm light from the lower middle,
          // as drawn; the footer with the button is the plain card colour.
          Container(
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topRight,
                end: Alignment.bottomLeft,
                colors: [Color(0xFF232323), Color(0xFF171717), Color(0xFF1B1916)],
                stops: [0.0, 0.45, 1.0],
              ),
            ),
            padding: const EdgeInsets.fromLTRB(24, 30, 16, 26),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text('MATCH-3 · ${levels.length} LEVELS',
                          style: const TextStyle(
                              fontFamily: AppTheme.fontMono, fontSize: 12, letterSpacing: 1.1, color: AppTheme.body)),
                      const SizedBox(height: 16),
                      const Text('Coin Quest',
                          style: TextStyle(
                              fontSize: 40, fontWeight: FontWeight.w600, height: 1.08, letterSpacing: -1.2, color: AppTheme.text)),
                      const SizedBox(height: 22),
                      const Text('Match.\nLearn.\nExplore.',
                          style: TextStyle(fontSize: 15, height: 1.4, color: AppTheme.body)),
                    ],
                  ),
                ),
                const Padding(
                  padding: EdgeInsets.only(top: 64),
                  child: _BoardArt(size: 150),
                ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.fromLTRB(24, 16, 24, 24),
            child: SizedBox(
              width: double.infinity,
              height: 48,
              child: FilledButton(
                onPressed: onPlay,
                style: FilledButton.styleFrom(padding: EdgeInsets.zero),
                child: const Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    HugeIcon('play', size: 18, color: AppTheme.onAccent),
                    SizedBox(width: 10),
                    Text('Play Coin Quest'),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

/// The little board on Coin Quest's card: nine of the game's own coins in
/// their wells, on a tile turned a few degrees.
class _BoardArt extends StatelessWidget {
  final double size;
  const _BoardArt({required this.size});

  static const _coins = ['gold', 'blue', 'silver', 'copper', 'gold', 'green', 'red', 'silver', 'gold'];

  @override
  Widget build(BuildContext context) {
    final cell = size / 3.3;
    return ExcludeSemantics(
      child: Transform.rotate(
        angle: -0.105,
        child: Container(
          width: size,
          height: size,
          padding: EdgeInsets.all(size * 0.05),
          decoration: BoxDecoration(
            color: const Color(0xFF242424),
            borderRadius: BorderRadius.circular(size * 0.16),
            border: Border.all(color: AppTheme.border),
            boxShadow: const [BoxShadow(color: Color(0x80000000), blurRadius: 18, offset: Offset(0, 8))],
          ),
          child: GridView.count(
            crossAxisCount: 3,
            physics: const NeverScrollableScrollPhysics(),
            padding: EdgeInsets.zero,
            mainAxisSpacing: size * 0.02,
            crossAxisSpacing: size * 0.02,
            children: [
              for (final c in _coins)
                Container(
                  decoration: BoxDecoration(
                    color: const Color(0xFF1F1F1F),
                    borderRadius: BorderRadius.circular(cell * 0.28),
                  ),
                  padding: EdgeInsets.all(cell * 0.1),
                  child: Image.asset('assets/images/piece_$c.png'),
                ),
            ],
          ),
        ),
      ),
    );
  }
}

/// "Stars collected", with the count.
class _StarsRow extends StatelessWidget {
  final int stars, of;
  const _StarsRow({required this.stars, required this.of});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 18),
      decoration: BoxDecoration(
        color: AppTheme.surface,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: AppTheme.border),
      ),
      child: Row(
        children: [
          const Expanded(child: Text('Stars collected', style: TextStyle(fontSize: 14, color: AppTheme.body))),
          const HugeIcon('star', size: 20, color: AppTheme.accent),
          const SizedBox(width: 16),
          Text('$stars / $of',
              style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 17, color: AppTheme.text)),
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

/// Sound and music, as the header's two square buttons. Off is the icon in
/// the dimmest grey; the button stays where it is.
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
          SquareIconButton(
            icon: 'volume_high',
            label: a.sfx ? 'Sound effects on' : 'Sound effects off',
            selected: a.sfx,
            iconColor: a.sfx ? AppTheme.body : AppTheme.dim,
            onTap: () {
              a.setSfx(!a.sfx);
              a.tap();
            },
          ),
          const SizedBox(width: 12),
          SquareIconButton(
            icon: 'music_note1',
            label: a.music ? 'Music on' : 'Music off',
            selected: a.music,
            iconColor: a.music ? AppTheme.body : AppTheme.dim,
            onTap: () {
              a.setMusic(!a.music);
              a.tap();
            },
          ),
        ],
      ),
    );
  }
}
