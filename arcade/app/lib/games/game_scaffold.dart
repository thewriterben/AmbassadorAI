import 'package:flutter/material.dart';

import '../theme.dart';

/// Shared chrome for every game: site background, title, mono score,
/// reset, and a glass game-over overlay.
class GameScaffold extends StatelessWidget {
  final String title;
  final int? score;
  final String? scoreLabel;
  final VoidCallback onReset;
  final bool gameOver;
  final String gameOverText;
  final Widget child;
  final Widget? bottom;

  const GameScaffold({
    super.key,
    required this.title,
    required this.onReset,
    required this.child,
    this.score,
    this.scoreLabel,
    this.gameOver = false,
    this.gameOverText = 'Game over',
    this.bottom,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.bg,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        title: Text(title),
        actions: [
          if (score != null)
            Center(
              child: Container(
                margin: const EdgeInsets.only(right: 8),
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                decoration: AppTheme.glass(radius: 999, outline: AppTheme.borderStrong),
                child: Row(
                  children: [
                    Text('${(scoreLabel ?? 'SCORE').toUpperCase()} ',
                        style: const TextStyle(
                            fontFamily: AppTheme.fontMono,
                            fontSize: 10,
                            letterSpacing: 1,
                            color: AppTheme.muted)),
                    Text('$score',
                        style: const TextStyle(
                            fontFamily: AppTheme.fontMono,
                            fontSize: 14,
                            fontWeight: FontWeight.w700,
                            color: AppTheme.accent)),
                  ],
                ),
              ),
            ),
          IconButton(onPressed: onReset, icon: const Icon(Icons.refresh, color: AppTheme.body)),
        ],
      ),
      extendBodyBehindAppBar: true,
      body: Stack(
        children: [
          Positioned.fill(
            child: Image.asset('assets/images/bg_dark.png', fit: BoxFit.cover),
          ),
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(16, 56, 16, 16),
              child: Column(
                children: [
                  Expanded(child: Center(child: child)),
                  if (bottom != null) bottom!,
                ],
              ),
            ),
          ),
          if (gameOver)
            Positioned.fill(
              child: Container(
                color: const Color(0xCC020203),
                alignment: Alignment.center,
                child: Container(
                  padding: const EdgeInsets.all(28),
                  margin: const EdgeInsets.all(32),
                  decoration: AppTheme.glass(radius: 24, fill: AppTheme.card, outline: AppTheme.borderStrong),
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(gameOverText,
                          textAlign: TextAlign.center,
                          style: const TextStyle(
                              fontSize: 28,
                              fontWeight: FontWeight.w600,
                              letterSpacing: -0.8,
                              color: AppTheme.text)),
                      if (score != null) ...[
                        const SizedBox(height: 8),
                        Text('${scoreLabel ?? 'Score'} $score',
                            style: const TextStyle(
                                fontFamily: AppTheme.fontMono, fontSize: 16, color: AppTheme.accent)),
                      ],
                      const SizedBox(height: 20),
                      FilledButton(onPressed: onReset, child: const Text('Play again')),
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

/// Glass board container used by grid games.
class GlassBoard extends StatelessWidget {
  final Widget child;
  final EdgeInsets padding;
  const GlassBoard({super.key, required this.child, this.padding = const EdgeInsets.all(8)});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: padding,
      decoration: AppTheme.glass(radius: 20, fill: const Color(0xCC050607), outline: AppTheme.borderStrong),
      child: child,
    );
  }
}
