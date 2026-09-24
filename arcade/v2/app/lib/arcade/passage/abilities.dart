/// When Pigs Fly abilities: what each one does, and its numbers per level.
///
/// A run carries at most two, one per on-screen button. Tapping anywhere
/// else is still a flap. The shop (phase 4) sells them and their levels;
/// until then the DEV menu is the only way to equip one, so a normal run
/// has no buttons at all.
///
/// Every ability is held back by a cooldown or a charge count, and none of
/// them can carry the boar past a pillar it has not flown to. The upgraded
/// run still counts for stars and scores (TEN-GAMES.md, "Fairness"); what
/// keeps that honest is that the server's XP cap does not move, and that
/// the third star is a soft landing, which no ability touches.
library;

import 'package:flutter/material.dart';

enum AbilityKind {
  dash('Dash', 'A burst forward. Nothing can touch you while it lasts.', Icons.keyboard_double_arrow_right_rounded),
  grapple('Grapple', 'Hooks the nearest gold coin ahead and hauls you to it, safe while the line holds.', Icons.link_rounded),
  teleport('Blink', 'Jumps you to the middle of the next opening.', Icons.auto_awesome_rounded),
  freeze('Freeze shot', 'Spits a coin that stops the next gold coin drifting.', Icons.ac_unit_rounded),
  tractor('Tractor beam', 'Draws in every coin within reach for a few seconds.', Icons.wifi_tethering_rounded);

  final String label;
  final String blurb;
  final IconData icon;
  const AbilityKind(this.label, this.blurb, this.icon);

  static AbilityKind? fromId(String? id) {
    for (final k in values) {
      if (k.name == id) return k;
    }
    return null;
  }
}

/// Levels run 1 to [maxLevel].
const maxAbilityLevel = 3;

/// One ability's numbers at one level. Times are seconds; distances are
/// fractions of the viewport so they feel the same on every phone.
class AbilityStats {
  /// Seconds before the button is live again.
  final double cooldown;

  /// How long the effect lasts, where it lasts at all.
  final double duration;

  /// Uses per run, for abilities limited by count rather than by time. Zero
  /// means unlimited (cooldown only).
  final int charges;

  /// Grapple: how far ahead a gold coin can be hooked, in screen widths.
  /// Tractor: the beam's radius, in screen heights.
  final double reach;

  /// Seconds of immunity to strikes on use.
  final double immunity;

  const AbilityStats({
    required this.cooldown,
    this.duration = 0,
    this.charges = 0,
    this.reach = 0,
    this.immunity = 0,
  });

  static AbilityStats of(AbilityKind kind, int level) {
    final i = (level.clamp(1, maxAbilityLevel)) - 1;
    return switch (kind) {
      // Holds altitude and doubles the scroll for a moment. The immunity
      // outlasts the burst slightly, so a dash begun at a pillar's face is
      // clear of it by the time the immunity ends.
      AbilityKind.dash => AbilityStats(
          cooldown: const [8.0, 6.5, 5.0][i],
          duration: 0.35,
          immunity: const [0.45, 0.55, 0.65][i],
        ),
      AbilityKind.grapple => AbilityStats(
          cooldown: const [10.0, 8.0, 6.0][i],
          duration: 1.2,
          reach: const [0.9, 1.1, 1.3][i],
        ),
      // Charges, not a cooldown: a blink is the strongest thing here, so a
      // run gets a fixed number of them. The short cooldown only stops a
      // double tap spending two.
      AbilityKind.teleport => AbilityStats(
          cooldown: 1.0,
          charges: const [1, 2, 3][i],
          immunity: 0.35,
        ),
      AbilityKind.freeze => AbilityStats(
          cooldown: const [7.0, 6.0, 5.0][i],
          duration: const [3.0, 4.0, 5.0][i],
        ),
      AbilityKind.tractor => AbilityStats(
          cooldown: const [12.0, 10.0, 8.0][i],
          duration: const [3.0, 4.0, 5.0][i],
          reach: const [0.20, 0.25, 0.30][i],
        ),
    };
  }
}

/// An ability equipped for a run, at a level.
class EquippedAbility {
  final AbilityKind kind;
  final int level;
  const EquippedAbility(this.kind, [this.level = 1]);

  AbilityStats get stats => AbilityStats.of(kind, level);
}

/// A slot's live state during a run. Owned by the game; read by the HUD.
class AbilitySlot {
  final EquippedAbility ability;
  double cooldownLeft = 0;
  int chargesLeft;

  AbilitySlot(this.ability) : chargesLeft = ability.stats.charges;

  AbilityStats get stats => ability.stats;

  /// 1 when just used, 0 when ready.
  double get cooldownFrac => stats.cooldown <= 0 ? 0 : (cooldownLeft / stats.cooldown).clamp(0.0, 1.0);

  bool get spent => stats.charges > 0 && chargesLeft <= 0;
}
