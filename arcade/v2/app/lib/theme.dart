import 'package:flutter/material.dart';

/// Single place to re-skin the whole app.
///
/// Colours are the design return of 2026-09-30 (`phoneAppRedesign` in its
/// design-tokens.json, "Direction 03"): a flat page, cards one step up with a
/// hairline edge, insets one step further. The names are the ones the code
/// already used, so every screen picks the new values up.
class AppTheme {
  static const appName = 'DGD Arcade';

  // v3-page / v3-inset (cards) / v3-surface (insets, secondary buttons)
  static const bg = Color(0xFF09090B);
  static const bg2 = Color(0xFF09090B);
  static const card = Color(0xFF141414);
  static const surface = Color(0xFF202020);

  // --primary / --primary-hover
  static const accent = Color(0xFFEA952D);
  static const accentHover = Color(0xFFFFAF4E);

  // v3-text / v3-secondary; muted and dim stay for the quietest labels and
  // for what is not yet reached.
  static const text = Color(0xFFE8E8E8);
  static const body = Color(0xFFA7A7A7);
  static const muted = Color(0xFF8A8A8A);
  static const dim = Color(0xFF4D4D4D);

  // v3-edge. Cards are opaque now (v3-inset), not a tint over the page.
  static const border = Color(0xFF303030);
  static const borderStrong = Color(0xFF3C3C3C);
  static const glassFill = card;

  /// Text on the orange button (v3-on-orange).
  static const onAccent = Color(0xFF09090B);

  // status
  static const info = Color(0xFF3080FF);
  static const success = Color(0xFF28C93F);
  static const danger = Color(0xFFFF6B6B); // the return's red, as its icons
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

  static const fontSans = 'Inter';
  static const fontMono = 'Geist Mono';

  static const glow = [
    BoxShadow(color: Color(0x4DEA952D), blurRadius: 15),
    BoxShadow(color: Color(0x0DEA952D), blurRadius: 40),
  ];

  static BoxDecoration glass({double radius = 16, Color? fill, Color? outline}) =>
      BoxDecoration(
        color: fill ?? glassFill,
        borderRadius: BorderRadius.circular(radius),
        border: Border.all(color: outline ?? border, width: 1),
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
          onPrimary: onAccent,
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
            foregroundColor: onAccent,
            textStyle: const TextStyle(fontFamily: fontSans, fontWeight: FontWeight.w600, fontSize: 16),
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
