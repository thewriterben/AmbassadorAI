import 'dart:math';
import 'dart:ui';

/// A glint of light on polished metal: a soft glowing core, four long rays
/// that taper to fine points and fade outward, and four shorter, fainter
/// rays on the diagonals, turning slightly as it flares.
///
/// Shared by When Pigs Fly's gold coins and the home screen's hero coin, so
/// both catch the light the same way. It replaced two stroked lines, which
/// read as a plus sign laid on the coin rather than as light.
///
/// [size] is the length of the long rays at full strength; [strength] runs
/// 0..1 (0 draws nothing); [spin] is the turn, in radians.
void paintSparkle(Canvas canvas, Offset at, double size, double strength, {double spin = 0}) {
  if (strength <= 0) return;
  final f = strength.clamp(0.0, 1.0);
  const warm = Color(0xFFFFF6DC);

  // The glow: brightest at the centre, gone well inside the rays' reach.
  final glow = size * (0.28 + 0.12 * f);
  canvas.drawCircle(
    at,
    glow,
    Paint()
      ..blendMode = BlendMode.plus
      ..shader = Gradient.radial(
        at,
        glow,
        [warm.withValues(alpha: 0.85 * f), warm.withValues(alpha: 0.25 * f), warm.withValues(alpha: 0)],
        const [0.0, 0.35, 1.0],
      ),
  );

  void ray(double angle, double length, double width, double alpha) {
    final dir = Offset(cos(angle), sin(angle));
    final side = Offset(-dir.dy, dir.dx) * width;
    final tip = at + dir * length;
    final path = Path()
      ..moveTo(at.dx + side.dx, at.dy + side.dy)
      ..lineTo(tip.dx, tip.dy)
      ..lineTo(at.dx - side.dx, at.dy - side.dy)
      ..close();
    canvas.drawPath(
      path,
      Paint()
        ..blendMode = BlendMode.plus
        ..shader = Gradient.linear(
          at,
          tip,
          [warm.withValues(alpha: alpha * f), warm.withValues(alpha: alpha * f * 0.35), warm.withValues(alpha: 0)],
          const [0.0, 0.45, 1.0],
        ),
    );
  }

  final long = size * (0.55 + 0.45 * f);
  final thick = size * 0.075;
  for (var k = 0; k < 4; k++) {
    ray(spin + k * pi / 2, long, thick, 0.95);
    ray(spin + pi / 4 + k * pi / 2, long * 0.42, thick * 0.6, 0.55);
  }
}
