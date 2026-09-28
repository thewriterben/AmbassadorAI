/// The boar's collision capsule per stage, in radii of the old coin.
///
/// The same numbers as `BoarSpec` in `boar.dart` (which a test holds them
/// to), kept here in pure Dart because the web arcade's server needs them to
/// replay a run and cannot import Flutter.
library;

class BoarBody {
  final double radius, halfLength;
  const BoarBody(this.radius, this.halfLength);

  /// Keyed by the stage id the server uses (`BoarStage.name`).
  static const byStageId = {
    'piglet': BoarBody(0.9, 0.35),
    'juvenile': BoarBody(0.9, 0.5),
    'razorback': BoarBody(1.0, 0.75),
  };
}
