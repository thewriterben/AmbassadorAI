part of 'passage_game.dart';

/// Drawing for [PassageGame]. Split out because the simulation above is the
/// part worth reviewing and it should not be buried under paint calls.
///
/// The coins are the DGD coin renders Coin Quest uses — gold, silver and
/// copper — so the two games read as one app. The player is the boar, from
/// the sprite sheets described in `boar.dart`. Everything else is drawn from
/// primitives in the app's own art direction: near-black sky, one amber
/// accent, brushed metal. Nothing here resembles any existing game's look,
/// which is the part of an arcade homage that actually carries legal risk.
extension PassageRender on PassageGame {
  void renderWorld(Canvas canvas) {
    if (!_laidOut) return;
    _sky(canvas);
    _strata(canvas);
    _pillars(canvas);
    _pickupsLayer(canvas);
    _ground(canvas);
    _spillLayer(canvas);
    _coin(canvas);
    _popLayer(canvas);
    _flash(canvas);
  }

  /// Highlight, body and shadow for each metal. Gold is the player's own
  /// palette; silver and copper are cooler and warmer neighbours of it, kept
  /// dull enough that gold is unmistakably the one worth going for.
  static const _metal = {
    PickupKind.gold: (Color(0xFFFFE7B2), AppTheme.accent, Color(0xFF8A5310), Color(0xFFFFD98C)),
    PickupKind.silver: (Color(0xFFF4F6F8), Color(0xFFB4BCC6), Color(0xFF596068), Color(0xFFE6EAEE)),
    PickupKind.copper: (Color(0xFFE8A97E), Color(0xFFB4652A), Color(0xFF52280D), Color(0xFFD98A55)),
  };

  /// The DGD coin render for [kind], drawn centred on [c] at radius [r],
  /// optionally tilted. Returns false when the image is not available so the
  /// caller can draw a coin instead.
  bool _spriteCoin(Canvas canvas, Offset c, double r, PickupKind kind, {double alpha = 1, double tilt = 0}) {
    final s = _coinSprites[kind];
    if (s == null) return false;
    final paint = alpha >= 1 ? null : (Paint()..color = const Color(0xFFFFFFFF).withValues(alpha: alpha));
    if (tilt == 0) {
      s.render(canvas, position: Vector2(c.dx, c.dy), size: Vector2.all(r * 2), anchor: Anchor.center, overridePaint: paint);
      return true;
    }
    canvas.save();
    canvas.translate(c.dx, c.dy);
    canvas.rotate(tilt);
    s.render(canvas, position: Vector2.zero(), size: Vector2.all(r * 2), anchor: Anchor.center, overridePaint: paint);
    canvas.restore();
    return true;
  }

  /// A small coin in one of the three metals: the DGD render when it is
  /// loaded, a drawn coin in the same palette when it is not.
  void _smallCoin(Canvas canvas, Offset c, double r, PickupKind kind, {double alpha = 1}) {
    final (hi, body, lo, rim) = _metal[kind]!;
    final gold = kind == PickupKind.gold;
    if (gold) {
      canvas.drawCircle(
        c,
        r * 2.3,
        Paint()
          ..shader = Gradient.radial(
            c,
            r * 2.3,
            [
              AppTheme.accent.withValues(alpha: 0.24 * alpha),
              AppTheme.accent.withValues(alpha: 0),
            ],
          ),
      );
    }
    if (_spriteCoin(canvas, c, r, kind, alpha: alpha)) return;
    canvas.drawCircle(
      c,
      r,
      Paint()
        ..shader = Gradient.radial(
          c.translate(-r * 0.3, -r * 0.35),
          r * 1.5,
          [hi.withValues(alpha: alpha), body.withValues(alpha: alpha), lo.withValues(alpha: alpha)],
          [0.0, 0.55, 1.0],
        ),
    );
    canvas.drawCircle(
      c,
      r,
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = r * 0.14
        ..color = rim.withValues(alpha: 0.55 * alpha),
    );
    if (gold) _dgdMark(canvas, c, r, alpha);
  }

  /// The spiral G. One and three-quarter turns opening outward, then a short
  /// bar back toward the centre for the G's crossbar.
  void _dgdMark(Canvas canvas, Offset c, double r, double alpha) {
    final path = Path();
    const turns = 1.75;
    const steps = 40;
    for (var i = 0; i <= steps; i++) {
      final f = i / steps;
      final a = f * turns * 2 * pi;
      final rr = r * (0.12 + 0.46 * f);
      final p = Offset(c.dx + rr * cos(a), c.dy + rr * sin(a));
      if (i == 0) {
        path.moveTo(p.dx, p.dy);
      } else {
        path.lineTo(p.dx, p.dy);
      }
    }
    // Crossbar: from the spiral's end, inward along the horizontal.
    const endA = turns * 2 * pi;
    final end = Offset(c.dx + r * 0.58 * cos(endA), c.dy + r * 0.58 * sin(endA));
    path.lineTo(end.dx - r * 0.34, end.dy);
    canvas.drawPath(
      path,
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeCap = StrokeCap.round
        ..strokeJoin = StrokeJoin.round
        ..strokeWidth = r * 0.13
        ..color = const Color(0xFF6E3F0C).withValues(alpha: 0.85 * alpha),
    );
  }

  void _pickupsLayer(Canvas canvas) {
    for (final p in _pickups) {
      if (p.taken) continue;
      final sx = _coinX + (p.worldX - scrollX);
      if (sx < -_coinR * 3 || sx > _w + _coinR * 3) continue;
      // Trail coins get a slow bob, phased by position so a trail ripples
      // rather than nodding in unison. Gold coins drift on their own.
      final bob = p.amp == 0 ? sin(_t * 3.0 + p.worldX * 0.02) * _h * 0.004 : 0.0;
      _smallCoin(canvas, Offset(sx, p.yAt(_t) + bob), _pickR(p.kind), p.kind);
    }
  }

  void _spillLayer(Canvas canvas) {
    for (final s in _spills) {
      if (s.taken) continue;
      final sx = _coinX + (s.worldX - scrollX);
      // Fade over the last stretch of its life so it does not blink out.
      final left = (PassageGame._spillLife - s.age) / 0.6;
      _smallCoin(canvas, Offset(sx, s.y), _coinR * 0.6, PickupKind.copper, alpha: left.clamp(0.0, 1.0));
    }
  }

  void _popLayer(Canvas canvas) {
    for (final p in _pops) {
      final f = (p.age / 0.45).clamp(0.0, 1.0);
      final r = _coinR * ((p.big ? 1.2 : 0.8) + f * (p.big ? 2.2 : 1.4));
      canvas.drawCircle(
        p.at,
        r,
        Paint()
          ..style = PaintingStyle.stroke
          ..strokeWidth = _coinR * 0.12 * (1 - f) + 0.5
          ..color = AppTheme.accent.withValues(alpha: 0.7 * (1 - f)),
      );
    }
  }

  /// Fractional position through the era list, for tinting.
  double get _eraF {
    final block = gatesPerEra * _spacing + _eraGap;
    final v = (scrollX - _leadIn + _spacing * 0.8) / block;
    return v.clamp(0.0, (eras.length - 1).toDouble());
  }

  void _sky(Canvas canvas) {
    final i = _eraF.floor().clamp(0, eras.length - 1);
    final j = min(i + 1, eras.length - 1);
    final tint = Color.lerp(Color(eras[i].tint), Color(eras[j].tint), _eraF - i)!;
    final rect = Rect.fromLTWH(0, 0, _w, _h);
    canvas.drawRect(
      rect,
      Paint()
        ..shader = Gradient.linear(
          Offset.zero,
          Offset(0, _h),
          [
            AppTheme.bg,
            Color.lerp(AppTheme.bg, tint, 0.55)!,
            Color.lerp(AppTheme.bg, tint, 0.95)!,
          ],
          [0.0, 0.62, 1.0],
        ),
    );
  }

  /// Three parallax layers of horizontal rules. They read as distance and as
  /// a ledger at the same time, which is the only visual pun in the game and
  /// is quiet enough to survive being noticed.
  void _strata(Canvas canvas) {
    const layers = [
      (0.10, 0.030, 7),
      (0.24, 0.055, 5),
      (0.46, 0.085, 4),
    ];
    for (final (speed, alpha, count) in layers) {
      final paint = Paint()
        ..color = AppTheme.text.withValues(alpha: alpha)
        ..strokeWidth = _h * 0.0016;
      final period = _w * 0.55;
      final off = (scrollX * speed) % period;
      for (var k = 0; k < count; k++) {
        final y = _h * (0.18 + k * 0.17);
        for (var x = -off; x < _w; x += period) {
          canvas.drawLine(
            Offset(x, y),
            Offset(x + period * 0.42, y),
            paint,
          );
        }
      }
    }
  }

  void _pillars(Canvas canvas) {
    final body = Paint();
    final cap = Paint()..color = AppTheme.accent.withValues(alpha: 0.75);
    for (final g in _gates) {
      final gx = _coinX + (g.worldX - scrollX);
      if (gx < -_gateW * 2 || gx > _w + _gateW * 2) continue;
      final left = gx - _gateW / 2;
      final top = g.gapY - g.gapH / 2;
      final bottom = g.gapY + g.gapH / 2;

      // Brushed metal, and brighter than it looks like it should be on a
      // monitor. The first pass ran #16181C → #2E3238 and on the phone the
      // pillars all but vanished into the sky — only the amber lip was
      // visible, so the gap read as a floating line rather than an opening.
      body.shader = Gradient.linear(
        Offset(left, 0),
        Offset(left + _gateW, 0),
        [
          const Color(0xFF32373F),
          const Color(0xFF767F8D),
          const Color(0xFF2A2E35),
        ],
        [0.0, 0.34, 1.0],
      );

      final r = Radius.circular(_gateW * 0.16);
      canvas.drawRRect(
        RRect.fromRectAndCorners(
          Rect.fromLTRB(left, -_h * 0.1, left + _gateW, top),
          bottomLeft: r,
          bottomRight: r,
        ),
        body,
      );
      canvas.drawRRect(
        RRect.fromRectAndCorners(
          Rect.fromLTRB(left, bottom, left + _gateW, _h * 1.1),
          topLeft: r,
          topRight: r,
        ),
        body,
      );
      // The amber lip is the only thing that tells you where the opening is
      // at a glance, so it gets the accent colour and nothing else does.
      final lip = _h * 0.0045;
      canvas.drawRect(Rect.fromLTRB(left, top - lip, left + _gateW, top), cap);
      canvas.drawRect(Rect.fromLTRB(left, bottom, left + _gateW, bottom + lip), cap);
    }
  }

  void _ground(Canvas canvas) {
    if (_groundY > _h) return;
    canvas.drawRect(
      Rect.fromLTRB(0, _groundY, _w, _h),
      Paint()
        ..shader = Gradient.linear(
          Offset(0, _groundY),
          Offset(0, _h),
          [const Color(0xFF23262B), const Color(0xFF0C0D0F)],
        ),
    );
    canvas.drawRect(
      Rect.fromLTRB(0, _groundY, _w, _groundY + _h * 0.004),
      Paint()..color = AppTheme.accent.withValues(alpha: 0.85),
    );
  }

  void _coin(Canvas canvas) {
    // Trail: oldest first, fading.
    for (var i = 0; i < _trail.length; i++) {
      final f = i / _trail.length;
      canvas.drawCircle(
        Offset(_coinX - (scrollX - _trail[i].dx), _trail[i].dy),
        _coinR * (0.28 + 0.34 * f),
        Paint()..color = AppTheme.accent.withValues(alpha: 0.05 + 0.10 * f),
      );
    }

    // Blink while the strike grace period is running, so a player can see
    // that the next pillar is free.
    var alpha = 1.0;
    if (_t < _invUntil) alpha = 0.45 + 0.55 * (sin(_t * 26) * 0.5 + 0.5);

    final c = Offset(_coinX, _coinY);
    // A flat alpha circle is not a glow — against a near-black sky it reads
    // as a hard-edged brown disc around the coin, which is exactly how it
    // looked on device. It needs to fade to nothing at its edge.
    canvas.drawCircle(
      c,
      _coinR * 2.1,
      Paint()
        ..shader = Gradient.radial(
          c,
          _coinR * 2.1,
          [
            AppTheme.accent.withValues(alpha: 0.20 * alpha),
            AppTheme.accent.withValues(alpha: 0.10 * alpha),
            AppTheme.accent.withValues(alpha: 0),
          ],
          [0.0, 0.52, 1.0],
        ),
    );
    if (_boar(canvas, alpha)) return;
    // No boar sheet: the gold coin, the way the game first shipped.
    final tilt = (_vy / _vMax).clamp(-1.0, 1.0) * 0.45;
    if (_spriteCoin(canvas, c, _coinR, PickupKind.gold, alpha: alpha, tilt: tilt)) return;
    canvas.drawCircle(
      c,
      _coinR,
      Paint()
        ..shader = Gradient.radial(
          c.translate(-_coinR * 0.32, -_coinR * 0.38),
          _coinR * 1.5,
          [
            Color.lerp(const Color(0xFFFFE7B2), AppTheme.accent, 0.12)!.withValues(alpha: alpha),
            AppTheme.accent.withValues(alpha: alpha),
            const Color(0xFF8A5310).withValues(alpha: alpha),
          ],
          [0.0, 0.55, 1.0],
        ),
    );
    canvas.drawCircle(
      c,
      _coinR * 0.62,
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = _coinR * 0.09
        ..color = const Color(0xFF7A4A10).withValues(alpha: 0.55 * alpha),
    );
    canvas.drawCircle(
      c,
      _coinR,
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = _coinR * 0.10
        ..color = const Color(0xFFFFD98C).withValues(alpha: 0.50 * alpha),
    );
  }

  /// Which frame of the sheet to draw. See [BoarFrame].
  int _boarFrame() {
    if (phase == PassagePhase.down) return _phaseT < 0.25 ? BoarFrame.land : BoarFrame.stand;
    if (phase != PassagePhase.flying && _groundY - _coinY < _coinR * 3.2) return BoarFrame.land;
    if (_t < _hurtUntil) return BoarFrame.hurt;
    return BoarFrame.cycle[_wingPhase.floor() % BoarFrame.cycle.length];
  }

  /// The boar, centred on the hitbox and pitched with its climb and fall.
  /// Returns false when this stage's sheet is not loaded.
  ///
  /// Drawn with nearest-neighbour sampling so the pixels stay pixels at any
  /// scale; the sheets are exported at 4x so a rotated frame still reads.
  bool _boar(Canvas canvas, double alpha) {
    final frames = _boarFrames[stage];
    if (frames == null) return false;
    final spec = BoarSpec.all[stage]!;
    final side = _coinR * spec.sizeInRadii;
    final frame = _boarFrame();
    final paint = Paint()
      ..filterQuality = FilterQuality.none
      ..isAntiAlias = false
      ..color = const Color(0xFFFFFFFF).withValues(alpha: alpha);

    canvas.save();
    if (phase == PassagePhase.down) {
      // Standing: hooves on the ground line, level.
      canvas.translate(_coinX, _groundY);
      frames[frame].render(canvas,
          position: Vector2(-spec.anchorU * side, -spec.footV * side), size: Vector2.all(side), overridePaint: paint);
    } else {
      // Nose up on a climb, down in a fall — gentler than the coin's tilt,
      // because a long body pitching hard reads as tumbling.
      //
      // With its legs down the boar reaches further below the hitbox than
      // it does in flight, so the landing frame is held level and lifted to
      // keep the hooves out of the ground. Without this it sank in and then
      // popped up by most of a radius on touchdown.
      final landing = frame == BoarFrame.land;
      final tilt = landing ? 0.0 : (_vy / _vMax).clamp(-1.0, 1.0) * 0.30;
      final y = landing ? min(_coinY, _groundY - (spec.footV - spec.anchorV) * side) : _coinY;
      canvas.translate(_coinX, y);
      canvas.rotate(tilt);
      frames[frame].render(canvas,
          position: Vector2(-spec.anchorU * side, -spec.anchorV * side), size: Vector2.all(side), overridePaint: paint);
    }
    canvas.restore();
    return true;
  }

  void _flash(Canvas canvas) {
    if (_strikeFlash <= 0) return;
    canvas.drawRect(
      Rect.fromLTWH(0, 0, _w, _h),
      Paint()..color = AppTheme.danger.withValues(alpha: 0.20 * _strikeFlash),
    );
  }
}
