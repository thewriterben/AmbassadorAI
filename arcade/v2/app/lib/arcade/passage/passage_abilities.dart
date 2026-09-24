part of 'passage_game.dart';

/// A coin spat by the freeze shot, flying at a gold coin ahead.
class _Shot {
  double worldX, y;
  final Pickup target;
  _Shot(this.worldX, this.y, this.target);
}

/// The five abilities, as the simulation runs them. Their numbers are in
/// `abilities.dart`; the rules each one keeps are here, next to the code that
/// has to keep them:
///
///  * Nothing fires before the first tap or outside normal flight. A descent
///    or a landing is the run's ending, and no button changes an ending.
///  * Nothing carries the boar past a pillar it has not reached. Blink moves
///    it vertically, to the middle of the next opening; dash is a speed-up in
///    the passage it is already in, not a jump.
///  * A button is only live when its ability would do something: a grapple
///    with no gold coin in reach, or a blink with no gate ahead, is a dead
///    button rather than a wasted cooldown.
extension PassageAbilities on PassageGame {
  /// Pull speed of a grapple, as the spring constant on the height gap.
  static const _grappleSpring = 9.0;
  static const _shotSpeed = 1.8; // screen widths per second
  static const _pullTime = 0.22; // seconds for a tractored coin to arrive

  bool _canUse(int i) {
    if (i < 0 || i >= slots.length) return false;
    if (!_started || phase != PassagePhase.flying || run.ended) return false;
    final s = slots[i];
    if (s.cooldownLeft > 0 || s.spent) return false;
    return switch (s.ability.kind) {
      AbilityKind.dash => _t >= _dashUntil,
      AbilityKind.grapple => _grapple == null && _goldAhead(s.stats.reach * _w) != null,
      AbilityKind.teleport => _nextGate() != null,
      AbilityKind.freeze => _shot == null && _goldAhead(_w * 1.4) != null,
      AbilityKind.tractor => _t >= _tractorUntil,
    };
  }

  bool _use(int i) {
    if (!_canUse(i)) return false;
    final s = slots[i];
    final st = s.stats;
    switch (s.ability.kind) {
      case AbilityKind.dash:
        _dashUntil = _t + st.duration;
        _immuneUntil = max(_immuneUntil, _t + st.immunity);
        _vy = 0;
        Audio.instance.fwLift();
      case AbilityKind.grapple:
        _grapple = _goldAhead(st.reach * _w);
        _grappleUntil = _t + st.duration;
        Audio.instance.specialFire();
      case AbilityKind.teleport:
        final g = _nextGate()!;
        _pops.add(_Pop(Offset(_coinX, _coinY), true));
        _coinY = g.gapY;
        _vy = 0;
        _immuneUntil = max(_immuneUntil, _t + st.immunity);
        _pops.add(_Pop(Offset(_coinX, _coinY), true));
        _trail.clear(); // a blink leaves no wake between the two places
        Audio.instance.fwBurst();
      case AbilityKind.freeze:
        _shot = _Shot(scrollX + _coinR, _coinY, _goldAhead(_w * 1.4)!);
        Audio.instance.coinFlip();
      case AbilityKind.tractor:
        _tractorUntil = _t + st.duration;
        _tractorReach = st.reach * _h;
        Audio.instance.specialCreate();
    }
    s.cooldownLeft = st.cooldown;
    if (st.charges > 0) s.chargesLeft--;
    HapticFeedback.selectionClick();
    run.tick();
    return true;
  }

  /// The nearest untaken gold coin ahead of the boar, within [maxAhead] of it.
  Pickup? _goldAhead(double maxAhead) {
    Pickup? best;
    for (final p in _pickups) {
      if (p.taken || p.pull != null || p.kind != PickupKind.gold) continue;
      final dx = p.worldX - scrollX;
      if (dx <= _coinR || dx > maxAhead) continue;
      if (best == null || p.worldX < best.worldX) best = p;
    }
    return best;
  }

  /// The first gate the boar has not yet entered.
  _Gate? _nextGate() {
    for (final g in _gates) {
      if (g.worldX - scrollX > _gateW / 2 + _coinR) return g;
    }
    return null;
  }

  void _updateAbilities(double dt) {
    var changed = false;
    for (final s in slots) {
      if (s.cooldownLeft > 0) {
        s.cooldownLeft = max(0.0, s.cooldownLeft - dt);
        if (s.cooldownLeft == 0) changed = true;
      }
    }

    // A grapple lets go when it has its coin, when the coin is behind, when
    // time is up, or when the run stops being normal flight.
    final g = _grapple;
    if (g != null &&
        (g.taken || g.worldX < scrollX - _coinR || _t > _grappleUntil || phase != PassagePhase.flying)) {
      _grapple = null;
      changed = true;
    }

    final shot = _shot;
    if (shot != null) {
      shot.worldX += _shotSpeed * _w * dt;
      final ty = shot.target.yAt(_t);
      shot.y += (ty - shot.y) * min(1.0, dt * 10);
      if (shot.target.taken) {
        _shot = null; // taken before the shot arrived: nothing to freeze
      } else if (shot.worldX >= shot.target.worldX) {
        final st = slots.firstWhere((s) => s.ability.kind == AbilityKind.freeze).stats;
        shot.target.freezeAt(_t, st.duration);
        _pops.add(_Pop(Offset(_coinX + (shot.target.worldX - scrollX), ty), false));
        Audio.instance.ting();
        _shot = null;
      }
    }
    if (changed) run.tick();
  }

  /// Tractor beam: coins within reach are caught and drawn to the boar over
  /// [_pullTime], then taken. Called from the coin update.
  void _updateTractor(double dt) {
    final beam = _t < _tractorUntil && phase == PassagePhase.flying;
    for (final p in _pickups) {
      if (p.taken) continue;
      if (p.pull == null) {
        if (!beam) continue;
        final dx = p.worldX - scrollX;
        if (dx < -_w * 0.4 || dx > _w) continue;
        final dy = p.yAt(_t) - _coinY;
        if (dx * dx + dy * dy <= _tractorReach * _tractorReach) {
          p.pull = 0;
          p.pullX = p.worldX;
          p.pullY = p.yAt(_t);
        }
      } else {
        p.pull = p.pull! + dt / _pullTime;
        if (p.pull! >= 1) _collect(p, _coinX);
      }
    }
  }

  /// Where a coin being drawn in is, on screen.
  Offset _pulledAt(Pickup p) {
    final f = _easeOut(p.pull!.clamp(0.0, 1.0));
    final from = Offset(_coinX + (p.pullX - scrollX), p.pullY);
    return Offset.lerp(from, Offset(_coinX, _coinY), f)!;
  }
}
