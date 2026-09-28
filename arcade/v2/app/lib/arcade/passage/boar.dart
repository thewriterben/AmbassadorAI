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
/// Each stage is one PNG: a single row of [BoarFrame.count] square frames,
/// facing right, the frame side being the image height. Final art replaces
/// these files without a code change as long as it keeps that layout and
/// roughly the placements in [BoarSpec] — or updates the numbers there.
///
/// The art is the owner's (2026-09-27): a piglet with white angel wings, a
/// juvenile on golden feathered wings, a razorback on golden dragon wings.
/// Each is a single flying pose, imported into the sheet layout by
/// `tool/art/import_boars.py`, which mirrors it to face right, drops the
/// detached sparkles, cuts the wings out and turns them about their
/// shoulders to build the eight frames: a real wingbeat, a red-tinted hurt
/// frame, a swept dash frame and a braking landing frame. The old
/// generated placeholders came from `tool/art/boar_sprites.py`.
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

/// Frame indices within every sheet.
abstract final class BoarFrame {
  /// Wing cycle: up, mid, down, recovery.
  static const cycle = [0, 1, 2, 3];
  static const hurt = 4;

  /// Swept-back wings. Reserved for the dash ability (phase 3).
  static const dash = 5;

  /// Wings braking, legs down: the last metres before touchdown.
  static const land = 6;

  /// Wings folded, standing on the ground.
  static const stand = 7;
  static const count = 8;
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

  const BoarSpec({
    required this.file,
    required this.sizeInRadii,
    required this.anchorU,
    required this.anchorV,
    required this.footV,
    required this.name,
    this.bodyRadius = 0.9,
    required this.bodyHalfLength,
  });

  static const all = {
    // Frames are cropped close to the art, wings included, so these sizes are
    // smaller than the old placeholders' (5.6 / 6.6 / 7.8), which carried a
    // wide margin. Anchors are the middle of the body, measured on a grid.
    BoarStage.piglet: BoarSpec(
      file: 'boar_piglet.png',
      sizeInRadii: 4.2,
      anchorU: 0.555,
      anchorV: 0.62,
      footV: 0.963,
      name: 'Piglet',
      bodyHalfLength: 0.35,
    ),
    BoarStage.juvenile: BoarSpec(
      file: 'boar_juvenile.png',
      sizeInRadii: 6.0,
      anchorU: 0.57,
      anchorV: 0.63,
      footV: 0.891,
      name: 'Juvenile',
      bodyHalfLength: 0.5,
    ),
    BoarStage.razorback: BoarSpec(
      file: 'boar_razorback.png',
      sizeInRadii: 6.6,
      anchorU: 0.57,
      anchorV: 0.635,
      footV: 0.856,
      name: 'Razorback',
      bodyRadius: 1.0,
      bodyHalfLength: 0.75,
    ),
  };
}

/// One frame of a stage's sheet as a Flutter widget — the standing boar by
/// default — for the screens around the game. Unfiltered, like in flight.
class BoarPortrait extends StatelessWidget {
  final BoarStage stage;
  final double size;
  final int frame;
  const BoarPortrait({super.key, required this.stage, this.size = 56, this.frame = BoarFrame.stand});

  /// The part of a frame the boar actually occupies when standing, as
  /// fractions: frames carry headroom for raised wings, and drawn whole the
  /// standing boar filled barely half a 58 px portrait on device.
  static const _crop = Rect.fromLTWH(0.02, 0.02, 0.96, 0.96);

  @override
  Widget build(BuildContext context) {
    final f = size / _crop.width; // one frame's side at this zoom
    return SizedBox.square(
      dimension: size,
      child: ClipRect(
        child: OverflowBox(
          alignment: Alignment.topLeft,
          maxWidth: f * BoarFrame.count,
          maxHeight: f,
          child: Transform.translate(
            offset: Offset(-(frame + _crop.left) * f, -_crop.top * f),
            child: Image.asset(
              'assets/images/${BoarSpec.all[stage]!.file}',
              width: f * BoarFrame.count,
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
