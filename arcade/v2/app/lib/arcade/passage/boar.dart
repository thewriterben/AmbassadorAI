/// The flying piggy bank — When Pigs Fly's player, in three stages.
///
/// The boar grows across runs (phase 2 wires that to lifetime points on the
/// server); within a run the stage is fixed. What changes with the stage is
/// the art and how big it is drawn. What does **not** change is the hitbox:
/// the simulation still flies a circle of the coin's old radius, so the
/// razorback a player has spent weeks growing is never harder to fit through
/// a gap than the piglet they started with. The wings, crest and mane are
/// allowed to overlap a pillar harmlessly — they are decoration, not body.
///
/// ## The sheet contract
///
/// Each stage is one PNG: a single row of square frames ([BoarFrames.count]
/// of them, eight for a four-drawing wingbeat), facing right, the frame side
/// being the image height. Final art replaces
/// these files without a code change as long as it keeps that layout and
/// roughly the placements in [BoarSpec] — or updates the numbers there.
///
/// The art is the owner's (2026-09-27): a piglet with white angel wings, a
/// juvenile on golden feathered wings, a razorback on golden dragon wings.
/// Each is a single flying pose, imported into the sheet layout by
/// `tool/art/import_boars.py`, which mirrors it to face right, drops the
/// detached sparkles, cuts the wings out and turns them about their
/// shoulders to build the eight frames: a real wingbeat, a red-tinted hurt
/// frame, a swept dash frame and a braking landing frame. The piglet's and
/// the juvenile's wingbeats are drawn instead (2026-09-28): four frames each
/// by the owner, split out of their sheets by `tool/art/split_frames.py`
/// and used as drawn, the other frames borrowing from them. The razorback's
/// wingbeat is drawn too, in six (so its sheet has ten frames). None of the
/// stages uses the rig now; it stays in the importer for new art that comes
/// as a single pose. The old generated placeholders came
/// from `tool/art/boar_sprites.py`.
library;

import 'package:flutter/widgets.dart';

enum BoarStage {
  piglet,
  juvenile,
  razorback;

  /// The server's stage id — the enum name — or null for anything unknown,
  /// so a stage added on the server before the app knows it falls back to
  /// the caller's default rather than throwing.
  static BoarStage? fromId(String? id) {
    for (final s in values) {
      if (s.name == id) return s;
    }
    return null;
  }

  String get label => BoarSpec.all[this]!.name;
}

/// Frame indices within a stage's sheet: the wing cycle first, then four
/// poses.
class BoarFrames {
  /// How many drawings the wingbeat has. Four, starting wings-up; the
  /// razorback's owner-drawn beat has six.
  final int cycleLength;

  /// How long each drawing of the beat holds, relative to the others (one
  /// per drawing; empty is all alike). Drawn animation holds its extremes,
  /// wings high and the full stroke, and passes quickly through the
  /// in-betweens: with every drawing held alike, the beat read as a flicker
  /// rather than a stroke.
  final List<double> holds;
  const BoarFrames([this.cycleLength = 4, this.holds = const []]);

  /// Wing cycle, in order, from wings-up.
  List<int> get cycle => List.generate(cycleLength, (i) => i);

  /// The drawing showing [beat] of the way through a wingbeat (0 is its
  /// start, wings up; 1 its end).
  int cycleFrameAt(double beat) {
    if (holds.length != cycleLength) return (beat * cycleLength).floor().clamp(0, cycleLength - 1);
    final total = holds.fold(0.0, (a, b) => a + b);
    var at = beat * total;
    for (var i = 0; i < cycleLength; i++) {
      at -= holds[i];
      if (at < 0) return i;
    }
    return cycleLength - 1;
  }
  int get hurt => cycleLength;

  /// Swept-back wings, for the dash ability.
  int get dash => cycleLength + 1;

  /// Wings braking, legs down: the last metres before touchdown.
  int get land => cycleLength + 2;

  /// Wings folded, standing on the ground.
  int get stand => cycleLength + 3;
  int get count => cycleLength + 4;
}

class BoarSpec {
  /// Bare file name under assets/images/, the way Flame loads it.
  final String file;

  /// Frame side on screen, in hitbox radii. Grows with the stage; the hitbox
  /// does not.
  final double sizeInRadii;

  /// Where the hitbox centre sits in the frame, as fractions of its side.
  /// Roughly the middle of body-and-head, not the middle of the frame — the
  /// frame has headroom for the wings.
  final double anchorU, anchorV;

  /// Where the hooves meet the ground in the standing frame, as a fraction of
  /// the frame height, so a landed boar stands on the ground line rather
  /// than hovering over it or sinking into it.
  final double footV;

  /// Shown on the pre-run and results screens once growth is live.
  final String name;

  /// The body's collision shape: a horizontal capsule centred on the anchor,
  /// in radii of the old coin. [bodyRadius] is its half-height, never more
  /// than the coin's, so no stage is harder to fit through a gap than the
  /// coin was — the razorback's heavier body takes the whole of it. [bodyHalfLength] is the straight
  /// run between the two round ends, and grows with the body, so a snout or
  /// a rump that visibly meets a pillar counts. The first version kept the
  /// coin's circle, and on device the razorback's snout sank most of a
  /// radius into a pillar before a strike registered.
  final double bodyRadius, bodyHalfLength;

  /// The layout of this stage's sheet, and how long each drawing of the
  /// wingbeat holds.
  final BoarFrames frames;

  /// Seconds for one wingbeat: the one a tap sets off, and the steady beat
  /// in between taps. Bigger boars beat slower, so their size reads in the
  /// motion; the piglet's glide is the old beat, half a second.
  final double flapBeat, glideBeat;

  const BoarSpec({
    required this.file,
    required this.sizeInRadii,
    required this.anchorU,
    required this.anchorV,
    required this.footV,
    required this.name,
    this.bodyRadius = 0.9,
    required this.bodyHalfLength,
    this.frames = const BoarFrames(),
    required this.flapBeat,
    required this.glideBeat,
  });

  static const all = {
    // Frames hold the art at 1/1.5 of their side, the rest being room for the
    // wings to beat into (tool/art/import_boars.py, PAD). Anchors are the
    // middle of the body, measured on a grid at the old padding of 1.08 and
    // rescaled with it; the boar is drawn the same size as before.
    BoarStage.piglet: BoarSpec(
      file: 'boar_piglet.png',
      sizeInRadii: 5.83,
      anchorU: 0.54,
      anchorV: 0.586,
      // The owner's drawn stand, placed on the wingbeat's hoof line.
      footV: 0.821,
      name: 'Piglet',
      bodyHalfLength: 0.35,
      // Up, level, down, folding in.
      frames: BoarFrames(4, [1.3, 0.8, 1.2, 0.7]),
      flapBeat: 0.30,
      glideBeat: 0.50,
    ),
    BoarStage.juvenile: BoarSpec(
      file: 'boar_juvenile.png',
      sizeInRadii: 8.33,
      anchorU: 0.55,
      anchorV: 0.594,
      footV: 0.782,
      name: 'Juvenile',
      bodyHalfLength: 0.5,
      // Rest/high, downstroke, low/compact, upstroke.
      frames: BoarFrames(4, [1.3, 0.7, 1.3, 0.7]),
      flapBeat: 0.36,
      glideBeat: 0.62,
    ),
    BoarStage.razorback: BoarSpec(
      file: 'boar_razorback.png',
      sizeInRadii: 9.17,
      anchorU: 0.55,
      anchorV: 0.597,
      // The drawn "fully down and folding" frame, which is also the
      // standing one.
      footV: 0.77,
      name: 'Razorback',
      bodyRadius: 1.0,
      bodyHalfLength: 0.75,
      // High and spread, mid-down, full cup, fully down and folding, mid-up,
      // re-lifting.
      frames: BoarFrames(6, [1.4, 0.7, 1.1, 1.1, 0.8, 0.9]),
      flapBeat: 0.44,
      glideBeat: 0.78,
    ),
  };
}

/// One frame of a stage's sheet as a Flutter widget — the standing boar by
/// default — for the screens around the game. Unfiltered, like in flight.
class BoarPortrait extends StatelessWidget {
  final BoarStage stage;
  final double size;
  /// The frame to show; null is the standing one.
  final int? frame;
  const BoarPortrait({super.key, required this.stage, this.size = 56, this.frame});

  /// The part of a frame the boar actually occupies when standing, as
  /// fractions: frames carry headroom for raised wings, and drawn whole the
  /// standing boar filled barely half a 58 px portrait on device.
  /// The art fills the middle 1/1.5 of each frame (import_boars.py, PAD).
  static const _crop = Rect.fromLTWH(0.155, 0.155, 0.69, 0.69);

  @override
  Widget build(BuildContext context) {
    final f = size / _crop.width; // one frame's side at this zoom
    final spec = BoarSpec.all[stage]!;
    final count = spec.frames.count;
    final frame = this.frame ?? spec.frames.stand;
    return SizedBox.square(
      dimension: size,
      child: ClipRect(
        child: OverflowBox(
          alignment: Alignment.topLeft,
          maxWidth: f * count,
          maxHeight: f,
          child: Transform.translate(
            offset: Offset(-(frame + _crop.left) * f, -_crop.top * f),
            child: Image.asset(
              'assets/images/${spec.file}',
              width: f * count,
              height: f,
              fit: BoxFit.fill,
              filterQuality: FilterQuality.medium,
              errorBuilder: (_, __, ___) => const SizedBox.shrink(),
            ),
          ),
        ),
      ),
    );
  }
}
