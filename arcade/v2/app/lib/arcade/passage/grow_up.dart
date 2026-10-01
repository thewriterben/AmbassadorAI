import 'dart:math';

import 'package:flutter/material.dart';

import '../../audio.dart';
import '../../theme.dart';
import '../sparkle.dart';
import 'boar.dart';

/// The boar growing up: played over the results sheet on the run whose
/// points carry it into its next stage.
///
///  1. The old stage stands in white silhouette, glowing, and starts to
///     flicker between its own shape and the new one, faster and faster,
///     while the glow swells (about 1.6 s).
///  2. A white flash.
///  3. The new stage in full colour, settling from a little large, with
///     sparkles bursting round it, the stage-up fanfare, and the line
///     "Your boar grew into a …!".
///
/// Tap anywhere to close; it closes itself a few seconds after the reveal.
///
/// Inside the DGD app ([Audio.inAppTab]) it is [GrowUpMoment.calm]: no white
/// flash, no sparkle burst and no fanfare. The arcade plan keeps celebration
/// out of the app's tab (the same gate as Coin Quest's fireworks and winner
/// line), and growth arrives only from the server, so a live build would be
/// the first to show it there (audit E6). The build-up, the new stage and its
/// line stay: the player still needs to know the boar grew.
Future<void> showGrowUp(BuildContext context, {required BoarStage from, required BoarStage to}) {
  return showGeneralDialog(
    context: context,
    barrierDismissible: false,
    barrierLabel: 'Your boar grew',
    // Deep enough that the screen underneath (a results sheet, or the
    // game's own prompts in the DEV preview) does not read through.
    barrierColor: Colors.black.withValues(alpha: 0.9),
    transitionDuration: const Duration(milliseconds: 250),
    // A bare dialog route has no Material above it, and text without one
    // draws with Flutter's yellow double underline, as the first build did
    // on device.
    pageBuilder: (_, __, ___) => Material(type: MaterialType.transparency, child: GrowUpMoment(from: from, to: to)),
  );
}

class GrowUpMoment extends StatefulWidget {
  final BoarStage from, to;

  /// No flash, sparkles or fanfare. Defaults to the build's own setting;
  /// tests set it, because [Audio.inAppTab] is a compile-time constant.
  final bool calm;
  const GrowUpMoment({super.key, required this.from, required this.to, this.calm = Audio.inAppTab});

  /// When the flash lands and the new stage is revealed, as a fraction of
  /// the whole animation.
  static const revealAt = 0.52;
  static const duration = Duration(milliseconds: 3200);

  @override
  State<GrowUpMoment> createState() => _GrowUpMomentState();
}

class _GrowUpMomentState extends State<GrowUpMoment> with SingleTickerProviderStateMixin {
  late final AnimationController _c = AnimationController(vsync: this, duration: GrowUpMoment.duration)
    ..addListener(_onTick)
    ..forward();
  bool _revealed = false;
  bool _closing = false;

  void _onTick() {
    if (!_revealed && _c.value >= GrowUpMoment.revealAt) {
      _revealed = true;
      if (!widget.calm) Audio.instance.stageUp();
    }
    if (_c.isCompleted) _close();
  }

  void _close() {
    if (_closing || !mounted) return;
    _closing = true;
    Navigator.of(context).maybePop();
  }

  @override
  void dispose() {
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final size = min(MediaQuery.sizeOf(context).width * 0.62, 280.0);
    return GestureDetector(
      behavior: HitTestBehavior.opaque,
      // Taps only close it once the new stage is showing: tapping through
      // the build-up would skip the whole point.
      onTap: () {
        if (_revealed) _close();
      },
      child: AnimatedBuilder(
        animation: _c,
        builder: (context, _) {
          final t = _c.value / GrowUpMoment.revealAt; // 0..1 through the build-up
          final revealed = _c.value >= GrowUpMoment.revealAt;
          final after = revealed ? (_c.value - GrowUpMoment.revealAt) / (1 - GrowUpMoment.revealAt) : 0.0;

          // Build-up: flicker between the two silhouettes, the swaps coming
          // faster (a chirp), the glow growing.
          Widget boar;
          double glow;
          if (!revealed) {
            final phase = 2.5 * t + 9.0 * t * t * t; // accelerating swaps
            final showNew = t > 0.18 && phase.floor().isOdd;
            boar = _silhouette(showNew ? widget.to : widget.from, size);
            glow = 0.25 + 0.75 * t;
          } else {
            // Reveal: from a little large, settling with an overshoot.
            final s = 1.0 + 0.25 * pow(1 - Curves.easeOutBack.transform(after.clamp(0.0, 1.0)), 1).toDouble();
            boar = Transform.scale(scale: s, child: BoarPortrait(stage: widget.to, size: size));
            glow = (1 - after * 1.4).clamp(0.3, 1.0);
          }
          // The flash: white across the screen at the reveal, fading fast.
          final flash = revealed ? (1 - after * 5).clamp(0.0, 1.0) : (t > 0.9 ? (t - 0.9) * 10 : 0.0);

          return Stack(
            alignment: Alignment.center,
            children: [
              // The glow behind the boar.
              Container(
                width: size * 1.5,
                height: size * 1.5,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  gradient: RadialGradient(colors: [
                    AppTheme.accent.withValues(alpha: 0.55 * glow),
                    AppTheme.accent.withValues(alpha: 0),
                  ]),
                ),
              ),
              boar,
              if (revealed && !widget.calm)
                IgnorePointer(
                  child: CustomPaint(size: Size.square(size * 1.6), painter: _BurstPainter(after)),
                ),
              if (revealed)
                Positioned(
                  left: 24,
                  right: 24,
                  top: MediaQuery.sizeOf(context).height / 2 + size * 0.62,
                  child: Opacity(
                    opacity: ((after - 0.08) * 4).clamp(0.0, 1.0),
                    child: Column(
                      children: [
                        Text(
                          'Your boar grew into a ${widget.to.label.toLowerCase()}!',
                          textAlign: TextAlign.center,
                          style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w700, color: AppTheme.accent),
                        ),
                        const SizedBox(height: 10),
                        Text(
                          'It flies as a ${widget.to.label.toLowerCase()} from your next run.',
                          textAlign: TextAlign.center,
                          style: const TextStyle(fontSize: 14, color: AppTheme.body),
                        ),
                        const SizedBox(height: 18),
                        const Text('Tap to continue', style: TextStyle(fontSize: 12, color: AppTheme.muted)),
                      ],
                    ),
                  ),
                ),
              if (flash > 0 && !widget.calm)
                IgnorePointer(child: Container(color: Colors.white.withValues(alpha: flash * 0.9))),
            ],
          );
        },
      ),
    );
  }

  Widget _silhouette(BoarStage stage, double size) => ColorFiltered(
        colorFilter: const ColorFilter.mode(Color(0xFFFFF4D8), BlendMode.srcIn),
        child: BoarPortrait(stage: stage, size: size),
      );
}

/// Sparkles flung out round the new stage, flaring and fading.
class _BurstPainter extends CustomPainter {
  final double t;
  _BurstPainter(this.t);

  @override
  void paint(Canvas canvas, Size size) {
    final c = size.center(Offset.zero);
    const n = 9;
    for (var i = 0; i < n; i++) {
      final a = i / n * 2 * pi + 0.35;
      // Each sparkle a little later than the last, flying out and fading.
      final local = ((t - i * 0.025) * 2.2).clamp(0.0, 1.0);
      if (local <= 0 || local >= 1) continue;
      final r = size.width * (0.22 + 0.3 * Curves.easeOut.transform(local));
      final strength = sin(local * pi);
      paintSparkle(canvas, c + Offset(cos(a), sin(a)) * r, size.width * (0.05 + 0.03 * (i % 3)), strength,
          spin: local * 0.8);
    }
  }

  @override
  bool shouldRepaint(_BurstPainter old) => old.t != t;
}
