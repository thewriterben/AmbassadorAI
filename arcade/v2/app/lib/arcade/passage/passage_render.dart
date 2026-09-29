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
    final drawn = _backdrop.isEmpty ? null : layerAlphas(eraWeights(_eraF, eras.length, _backdropFade));
    var skyCover = 0.0;
    for (final (e, a) in drawn ?? const <(int, double)>[]) {
      if (_backdrop.image(e, BackdropPart.sky) == null) continue;
      _backdrop.drawSky(canvas, e, a, _w, _h);
      skyCover += a;
    }
    _net(canvas);
    // The drift lines belong to the code-drawn sky; a drawn one has its own.
    _strata(canvas, 1 - min(1.0, skyCover));
    for (final (e, a) in drawn ?? const <(int, double)>[]) {
      _backdrop.drawStrip(canvas, e, BackdropPart.far, a, scrollX, _w, _h);
    }
    _city?.render(canvas, scrollX, _t, hide: drawn == null ? null : _backdrop.hasSkyline);
    for (final part in const [BackdropPart.mid, BackdropPart.near]) {
      for (final (e, a) in drawn ?? const <(int, double)>[]) {
        _backdrop.drawStrip(canvas, e, part, a, scrollX, _w, _h);
      }
    }
    _pillars(canvas);
    _pickupsLayer(canvas);
    _shotLayer(canvas);
    _ground(canvas);
    _spillLayer(canvas);
    _abilityFx(canvas);
    _coin(canvas);
    _popLayer(canvas);
    if (PassageGame.devShowHitbox) _hitbox(canvas);
    _flash(canvas);
  }

  /// DEV: the collision capsule, and the play area's top edge.
  void _hitbox(Canvas canvas) {
    final paint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.5
      ..color = const Color(0xFF3CFFB4);
    canvas.drawRRect(
      RRect.fromLTRBR(
        _coinX - _bodyL - _bodyR,
        _coinY - _bodyR,
        _coinX + _bodyL + _bodyR,
        _coinY + _bodyR,
        Radius.circular(_bodyR),
      ),
      paint,
    );
    canvas.drawLine(Offset(0, _playTop), Offset(_w, _playTop), paint..color = const Color(0x803CFFB4));
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
    if (_spriteCoin(canvas, c, r, kind, alpha: alpha)) {
      if (gold) _glint(canvas, c, r, alpha);
      return;
    }
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

  /// Light catching a gold coin: every couple of seconds a bright diagonal
  /// band sweeps across the face, and as it crosses the middle a small star
  /// flares at the rim. Phased by where the coin is on screen, so a row of
  /// coins shimmers in turn rather than all at once.
  void _glint(Canvas canvas, Offset c, double r, double alpha) {
    const period = 2.2, sweep = 0.45;
    final phase = ((_t + c.dx / _w * 0.9) % period) / sweep;
    if (phase > 1) return;
    canvas.save();
    canvas.clipPath(Path()..addOval(Rect.fromCircle(center: c, radius: r * 0.96)));
    // Two streaks across the face, a broad one and a thin one just behind
    // it, slanting down to the left. The gradient runs across the streaks,
    // so the light sits in a narrow slice of it; spread over the whole
    // gradient, the first version washed the entire coin white.
    final x = c.dx - r * 1.8 + phase * r * 3.6;
    const clear = Color(0x00FFF4D0);
    final peak = const Color(0xFFFFF4D0).withValues(alpha: 0.6 * alpha);
    final band = Paint()
      ..blendMode = BlendMode.plus
      ..shader = Gradient.linear(
        Offset(x - r * 0.9, c.dy - r * 0.35),
        Offset(x + r * 0.9, c.dy + r * 0.35),
        [clear, clear, peak, clear, clear, peak.withValues(alpha: 0.35 * alpha), clear, clear],
        const [0.0, 0.40, 0.47, 0.54, 0.58, 0.62, 0.66, 1.0],
      );
    canvas.drawRect(Rect.fromCircle(center: c, radius: r), band);
    canvas.restore();
    // The flare, strongest mid-sweep, turning a little as it comes and goes.
    final f = (1 - (phase - 0.5).abs() * 2).clamp(0.0, 1.0);
    paintSparkle(canvas, c.translate(r * 0.42, -r * 0.46), r * 0.8, f * alpha, spin: (phase - 0.5) * 0.5);
  }

  void _pickupsLayer(Canvas canvas) {
    for (final p in _pickups) {
      if (p.taken) continue;
      if (p.pull != null) {
        // Being drawn in by the tractor beam: shrinking as it arrives.
        final at = _pulledAt(p);
        _smallCoin(canvas, at, _pickR(p.kind) * (1 - 0.4 * p.pull!.clamp(0.0, 1.0)), p.kind);
        continue;
      }
      final sx = _coinX + (p.worldX - scrollX);
      if (sx < -_coinR * 3 || sx > _w + _coinR * 3) continue;
      if (p.frozenAt(_t)) {
        // Frozen by a shot: an icy ring, fading in its last second.
        final left = (p.clockResume - _t).clamp(0.0, 1.0);
        canvas.drawCircle(
          Offset(sx, p.yAt(_t)),
          _pickR(p.kind) * 1.45,
          Paint()
            ..style = PaintingStyle.stroke
            ..strokeWidth = _coinR * 0.16
            ..color = const Color(0xFFBFE8FF).withValues(alpha: 0.85 * left),
        );
      }
      // Trail coins get a slow bob, phased by position so a trail ripples
      // rather than nodding in unison. Gold coins drift on their own.
      final bob = p.amp == 0 ? sin(_t * 3.0 + p.worldX * 0.02) * _h * 0.004 : 0.0;
      _smallCoin(canvas, Offset(sx, p.yAt(_t) + bob), _pickR(p.kind), p.kind);
    }
  }

  void _shotLayer(Canvas canvas) {
    final s = _shot;
    if (s == null) return;
    final at = Offset(_coinX + (s.worldX - scrollX), s.y);
    for (var k = 1; k <= 4; k++) {
      canvas.drawCircle(
        at.translate(-k * _coinR * 0.45, 0),
        _coinR * (0.34 - k * 0.05),
        Paint()..color = const Color(0xFFBFE8FF).withValues(alpha: 0.35 - k * 0.07),
      );
    }
    _smallCoin(canvas, at, _coinR * 0.4, PickupKind.gold);
  }

  /// Everything the abilities draw around the boar, under it.
  void _abilityFx(Canvas canvas) {
    final c = Offset(_coinX, _coinY);

    if (_t < _tractorUntil) {
      final pulse = 0.5 + 0.5 * sin(_t * 9);
      canvas.drawCircle(
        c,
        _tractorReach,
        Paint()..color = AppTheme.accent.withValues(alpha: 0.05 + 0.03 * pulse),
      );
      canvas.drawCircle(
        c,
        _tractorReach,
        Paint()
          ..style = PaintingStyle.stroke
          ..strokeWidth = _coinR * 0.08
          ..color = AppTheme.accent.withValues(alpha: 0.35 + 0.25 * pulse),
      );
      final beam = Paint()
        ..strokeWidth = _coinR * 0.12
        ..color = AppTheme.accent.withValues(alpha: 0.45);
      for (final p in _pickups) {
        if (p.pull != null && !p.taken) canvas.drawLine(c, _pulledAt(p), beam);
      }
    }

    final hook = _grapple;
    if (hook != null) {
      // The tusk-chain: links from the snout to the hooked coin.
      final from = c.translate(_coinR * 1.1, _coinR * 0.2);
      final to = Offset(_coinX + (hook.worldX - scrollX), hook.yAt(_t));
      final d = to - from;
      final n = max(2, (d.distance / (_coinR * 0.55)).floor());
      final link = Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = _coinR * 0.12
        ..color = const Color(0xFFE8C66A);
      for (var k = 0; k <= n; k++) {
        canvas.drawCircle(Offset.lerp(from, to, k / n)!, _coinR * 0.16, link);
      }
    }

    if (_t < _dashUntil) {
      // Speed lines streaming off the boar.
      final f = ((_dashUntil - _t) / 0.35).clamp(0.0, 1.0);
      final line = Paint()
        ..strokeWidth = _coinR * 0.14
        ..strokeCap = StrokeCap.round
        ..color = AppTheme.text.withValues(alpha: 0.55 * f);
      for (final dy in const [-0.7, 0.0, 0.7]) {
        final y = _coinY + dy * _coinR;
        canvas.drawLine(Offset(_coinX - _coinR * 1.8, y), Offset(_coinX - _coinR * (4.5 + dy.abs() * 2), y), line);
      }
    }
  }

  void _spillLayer(Canvas canvas) {
    for (final s in _spills) {
      if (s.taken) continue;
      final sx = _coinX + (s.worldX - scrollX);
      // Fade over the last stretch of its life so it does not blink out.
      final left = (PassageSim.spillLife - s.age) / 0.6;
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
  /// Half the width of the crossfade between two eras' drawn backdrops, in
  /// eras (see [eraWeights]): a third of a screen of scrolling either side
  /// of the change.
  double get _backdropFade => _w * 0.33 / (gatesPerEra * _spacing + _eraGap);

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

  /// 2009: a faint grid across the sky, the network the era is about. It
  /// fades in over the crossing into the last era. Drawn after a drawn sky,
  /// so it stays: the image itself carries no grid (asked for one, the
  /// image generator drew graph paper).
  void _net(Canvas canvas) {
    final net = (_eraF - (eras.length - 2)).clamp(0.0, 1.0);
    if (net > 0) {
      final line = Paint()
        ..strokeWidth = 1
        ..color = const Color(0xFFBFE0FF).withValues(alpha: 0.05 * net);
      final step = _w * 0.11;
      final off = (scrollX * 0.08) % step;
      for (var x = -off; x < _w; x += step) {
        canvas.drawLine(Offset(x, 0), Offset(x, _h * 0.7), line);
      }
      for (var y = step * 0.5; y < _h * 0.7; y += step) {
        canvas.drawLine(Offset(0, y), Offset(_w, y), line);
      }
    }
  }

  /// Three parallax layers of horizontal rules. They read as distance and as
  /// a ledger at the same time, which is the only visual pun in the game and
  /// is quiet enough to survive being noticed.
  void _strata(Canvas canvas, [double fade = 1]) {
    if (fade <= 0) return;
    const layers = [
      (0.10, 0.030, 7),
      (0.24, 0.055, 5),
      (0.46, 0.085, 4),
    ];
    for (final (speed, alpha, count) in layers) {
      final paint = Paint()
        ..color = AppTheme.text.withValues(alpha: alpha * fade)
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

  /// The gates, each in its era's materials (see `passage_gates.dart`),
  /// drawn from a picture recorded the first time the gate comes into view.
  void _pillars(Canvas canvas) {
    for (final g in _gates) {
      final gx = _coinX + (g.worldX - scrollX);
      if (gx < -_gateW * 2 || gx > _w + _gateW * 2) continue;
      final pic = (g.renderCache ??= _gatePicture(g)) as Picture;
      canvas.save();
      canvas.translate(gx - _gateW / 2, 0);
      canvas.drawPicture(pic);
      canvas.restore();
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
    if (!_backdrop.isEmpty) {
      for (final (e, a) in layerAlphas(eraWeights(_eraF, eras.length, _backdropFade))) {
        _backdrop.drawGround(canvas, e, a, scrollX, _groundY, _w, _h);
      }
    }
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

  /// Seconds each standing pose holds in the idle.
  static const _standBeat = 0.55;

  /// Which frame of the sheet to draw. See [BoarFrames].
  int _boarFrame() {
    final f = BoarSpec.all[stage]!.frames;
    // A whole passage flown lands glad; a run that ran out short, as it is.
    final land = sim.erasCleared >= eras.length ? f.landWin : f.land;
    if (phase == PassagePhase.down) {
      if (_phaseT < 0.25) return land;
      // Standing: two poses in turn, a beat each.
      return ((_phaseT - 0.25) / _standBeat).floor().isEven ? f.stand : f.standAlt;
    }
    if (phase != PassagePhase.flying && _groundY - _coinY < _coinR * 3.2) return land;
    if (_t < _hurtUntil) return f.hurt;
    if (_t < _dashUntil) return f.dash;
    return f.cycleFrameAt(_wingPhase - _wingPhase.floorToDouble());
  }

  /// The boar, centred on the hitbox and pitched with its climb and fall.
  /// Returns false when this stage's sheet is not loaded.
  ///
  /// Drawn from the owner's art, sampled smoothly. The frames carry the
  /// owner's drawn wingbeat (`tool/art/import_boars.py`).
  bool _boar(Canvas canvas, double alpha) {
    final frames = _boarFrames[stage];
    if (frames == null) return false;
    final spec = BoarSpec.all[stage]!;
    final side = _coinR * spec.sizeInRadii;
    final frame = _boarFrame();
    // Smooth sampling: the art is detailed and not on a strict pixel grid,
    // and nearest-neighbour shimmered as it scaled and pitched.
    final paint = Paint()
      ..filterQuality = FilterQuality.medium
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
      final landing = frame == spec.frames.land;
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
