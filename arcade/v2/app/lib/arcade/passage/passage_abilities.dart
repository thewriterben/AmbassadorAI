part of 'passage_game.dart';

/// The five abilities. Their numbers are in `sim/ability_rules.dart` and the
/// simulation runs them in `sim/passage_sim.dart`; the rules each one keeps
/// are stated here, where they have always been:
///
///  * Nothing fires before the first tap or outside normal flight. A descent
///    or a landing is the run's ending, and no button changes an ending.
///  * Nothing carries the boar past a pillar it has not reached. Blink moves
///    it vertically, to the middle of the next opening; dash is a speed-up in
///    the passage it is already in, not a jump.
///  * A button is only live when its ability would do something: a grapple
///    with no gold coin in reach, or a blink with no gate ahead, is a dead
///    button rather than a wasted cooldown.
///
/// What remains here is drawing.
extension PassageAbilities on PassageGame {
  /// Where a coin being drawn in by the tractor beam is, on screen.
  Offset _pulledAt(Pickup p) {
    final f = _easeOut(p.pull!.clamp(0.0, 1.0));
    final from = Offset(_coinX + (p.pullX - scrollX), p.pullY);
    return Offset.lerp(from, Offset(_coinX, _coinY), f)!;
  }
}
