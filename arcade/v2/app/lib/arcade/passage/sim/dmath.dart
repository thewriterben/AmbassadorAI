/// Deterministic maths for the When Pigs Fly simulation.
///
/// The web arcade verifies a run by replaying it on the server, so the
/// simulation must produce bit-identical results in every JavaScript engine
/// and on the Dart VM. `+ - * /` and comparisons are exactly rounded
/// everywhere (IEEE 754), but `dart:math`'s `sin`, `cos` and `pow` call the
/// platform's library, and V8, JavaScriptCore, SpiderMonkey and the VM do not
/// promise the same last bit. So the simulation uses these instead: only
/// basic arithmetic, a fixed evaluation order, and constants written out.
///
/// Accuracy is far beyond anything the game can show (|error| < 5e-14 on the
/// sine), and the rendering side is free to keep using `dart:math`.
library;

const double dPi = 3.141592653589793;
const double _twoPi = 6.283185307179586;
const double _halfPi = 1.5707963267948966;

/// sin(x), deterministic. Range-reduced to [-π/2, π/2], then an odd Taylor
/// series to x^19 in Horner form.
double dsin(double x) {
  // Reduce to [-π, π]. `roundToDouble` is exact.
  var r = x - _twoPi * (x / _twoPi).roundToDouble();
  // Fold to [-π/2, π/2]: sin(π - r) = sin(r).
  if (r > _halfPi) {
    r = dPi - r;
  } else if (r < -_halfPi) {
    r = -dPi - r;
  }
  final r2 = r * r;
  // 1 - r²/3! + r⁴/5! - ... - r¹⁸/19!
  var p = -8.22063524662433e-18; // -1/19!
  p = p * r2 + 2.8114572543455206e-15; // 1/17!
  p = p * r2 - 7.647163731819816e-13; // -1/15!
  p = p * r2 + 1.6059043836821613e-10; // 1/13!
  p = p * r2 - 2.505210838544172e-8; // -1/11!
  p = p * r2 + 2.7557319223985893e-6; // 1/9!
  p = p * r2 - 1.984126984126984e-4; // -1/7!
  p = p * r2 + 8.333333333333333e-3; // 1/5!
  p = p * r2 - 1.6666666666666666e-1; // -1/3!
  p = p * r2 + 1.0;
  return r * p;
}

/// cos(x), deterministic.
double dcos(double x) => dsin(x + _halfPi);

/// Cubic ease-out, 1 - (1 - t)³, without `pow`.
double easeOut(double t) {
  final u = 1 - t;
  return 1 - u * u * u;
}

/// Same formula as Flutter's `lerpDouble`, so moving the simulation out of
/// Flutter changes no number.
double lerp(double a, double b, double t) => a * (1.0 - t) + b * t;
