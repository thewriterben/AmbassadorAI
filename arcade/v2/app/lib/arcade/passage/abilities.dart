/// When Pigs Fly abilities. The rules and numbers live in
/// `sim/ability_rules.dart` (pure Dart, shared with the web arcade's
/// verifier); this adds what only Flutter needs: the button icons.
library;

import 'package:flutter/material.dart';

import 'sim/ability_rules.dart';

export 'sim/ability_rules.dart';

extension AbilityIcon on AbilityKind {
  IconData get icon => switch (this) {
        AbilityKind.dash => Icons.keyboard_double_arrow_right_rounded,
        AbilityKind.grapple => Icons.link_rounded,
        AbilityKind.teleport => Icons.auto_awesome_rounded,
        AbilityKind.freeze => Icons.ac_unit_rounded,
        AbilityKind.tractor => Icons.wifi_tethering_rounded,
      };
}
