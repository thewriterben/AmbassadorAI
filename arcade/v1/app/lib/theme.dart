import 'package:flutter/material.dart';

/// Single place to re-skin the whole app.
/// Tokens mirror digitalgold.co's CSS variables.
class AppTheme {
  static const appName = 'DGD Arcade';

  // --background / --bg-2 / --card / --section-alt
  static const bg = Color(0xFF020203);
  static const bg2 = Color(0xFF08090B);
  static const card = Color(0xFF050607);
  static const surface = Color(0xFF101010);

  // --primary / --primary-hover
  static const accent = Color(0xFFEA952D);
  static const accentHover = Color(0xFFFFAF4E);

  // --foreground / --text-body / --text-muted / --text-dim
  static const text = Color(0xFFE8E8E8);
  static const body = Color(0xFF9A9A9A);
  static const muted = Color(0xFF7A7A7A);
  static const dim = Color(0xFF4D4D4D);

  // --border / --border-strong / --surface-elevated
  static const border = Color(0x12FFFFFF);
  static const borderStrong = Color(0x24FFFFFF);
  static const glassFill = Color(0x0DFFFFFF);

  // status
  static const info = Color(0xFF3080FF);
  static const success = Color(0xFF28C93F);
  static const danger = Color(0xFFFF6568);
  static const warning = Color(0xFFEDB200);

  /// Piece palette for Match / Blocks (site accent + status colors).
  static const tileColors = <Color>[
    accent,
    text,
    info,
    success,
    danger,
    warning,
    Color(0xFFB57BEE),
  ];

  static const fontSans = 'InstrumentSans';
  static const fontMono = 'GeistMono';
  static const fontSerif = 'PTSerif';

  static const glow = [
    BoxShadow(color: Color(0x4DEA952D), blurRadius: 15),
    BoxShadow(color: Color(0x0DEA952D), blurRadius: 40),
  ];

  static BoxDecoration glass({double radius = 16, Color? fill, Color? outline}) =>
      BoxDecoration(
        color: fill ?? glassFill,
        borderRadius: BorderRadius.circular(radius),
        border: Border.all(color: outline ?? border, width: 0.5),
      );

  /// Outer margin for a floating (card-style) modal bottom sheet.
  ///
  /// `showModalBottomSheet` does not inset its child for system UI, so a sheet
  /// with a plain 16px margin ends up with its bottom edge — and in practice
  /// its primary button — underneath the navigation bar. Verified on a Pixel:
  /// the Play button on the level sheet sat directly on the gesture pill.
  ///
  /// `viewPadding` rather than `padding`, because the sheet route consumes the
  /// latter on its way down; `viewPadding` still reports the physical inset.
  static EdgeInsets sheetMargin(BuildContext context) => EdgeInsets.fromLTRB(
        16,
        16,
        16,
        16 + MediaQuery.viewPaddingOf(context).bottom,
      );

  static ThemeData get data => ThemeData(
        useMaterial3: true,
        brightness: Brightness.dark,
        fontFamily: fontSans,
        scaffoldBackgroundColor: bg,
        colorScheme: const ColorScheme.dark(
          primary: accent,
          onPrimary: Color(0xFF030303),
          surface: card,
          onSurface: text,
        ),
        appBarTheme: const AppBarTheme(
          backgroundColor: bg,
          foregroundColor: text,
          elevation: 0,
          titleTextStyle: TextStyle(
            fontFamily: fontSans,
            fontSize: 20,
            fontWeight: FontWeight.w600,
            letterSpacing: -0.5,
            color: text,
          ),
        ),
        filledButtonTheme: FilledButtonThemeData(
          style: FilledButton.styleFrom(
            backgroundColor: accent,
            foregroundColor: const Color(0xFF030303),
            textStyle: const TextStyle(fontFamily: fontSans, fontWeight: FontWeight.w600),
            shape: const StadiumBorder(),
            padding: const EdgeInsets.symmetric(horizontal: 28, vertical: 16),
          ),
        ),
      );
}

/// Metadata for each game shown on the menu.
class GameInfo {
  final String id;
  final String title;
  final String kicker;
  final String tagline;
  final String asset;
  const GameInfo(this.id, this.title, this.kicker, this.tagline, this.asset);
}

const games = <GameInfo>[
  GameInfo('merge', 'Merge', '01 · SWIPE', 'Swipe tiles, double up', 'assets/images/merge_256.png'),
  GameInfo('words', 'Words', '02 · GUESS', 'Guess the five-letter word', 'assets/images/word_correct.png'),
  GameInfo('blocks', 'Blocks', '03 · DROP', 'Drop shapes, clear lines', 'assets/images/block_0.png'),
  GameInfo('match', 'Match', '04 · SWAP', 'Line up three to pop', 'assets/images/gem_coin.png'),
  GameInfo('rope', 'Rope', '05 · CUT', 'Cut the rope, fill the vault', 'assets/images/rope_treat.png'),
];
