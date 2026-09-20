import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';

import 'audio.dart';
import 'theme.dart';

/// Fires effects continuously and reports whether the audio path degrades.
///
/// This exists because "the effects lag and then stop" is a failure you only
/// notice once it has already happened, and only after a long session — which
/// makes it expensive to test by playing and easy to declare fixed on
/// insufficient evidence.
///
/// The number that matters is not the totals, it is the **last decile latency
/// against the first**. The old bug was an accumulation: every `FlameAudio.play`
/// left a live player behind, so each new sound had more work to do than the
/// last. That shows as latency climbing steadily long before anything actually
/// goes silent. A flat line across thousands of effects is the evidence that
/// the per-file player pool is holding.
///
/// Test builds only — reached from the DEV menu.
class DevSoakScreen extends StatefulWidget {
  const DevSoakScreen({super.key});

  @override
  State<DevSoakScreen> createState() => _DevSoakScreenState();
}

class _DevSoakScreenState extends State<DevSoakScreen> {
  static const _perSecond = 10; // roughly a busy cascade, sustained
  Timer? _timer;
  int _elapsed = 0;
  int _durationS = 180;
  bool _running = false;
  final _rng = Random();
  late List<String> _pool;

  @override
  void initState() {
    super.initState();
    _pool = Audio.instance.allSfx
        // Voice lines are long and heavily rate-limited; including them would
        // mostly measure the limiter rather than the audio path.
        .where((f) => !f.startsWith('vo_'))
        .toList();
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  void _start() {
    Audio.instance.resetStats();
    setState(() {
      _running = true;
      _elapsed = 0;
    });
    final tick = Duration(milliseconds: (1000 / _perSecond).round());
    _timer = Timer.periodic(tick, (t) {
      // minGapMs 0: the point is to push the platform, not to sound nice.
      Audio.instance.play(_pool[_rng.nextInt(_pool.length)], volume: 0.35);
      if (t.tick % _perSecond == 0) {
        setState(() => _elapsed = t.tick ~/ _perSecond);
        if (_elapsed >= _durationS) _stop();
      }
    });
  }

  void _stop() {
    _timer?.cancel();
    _timer = null;
    if (mounted) setState(() => _running = false);
  }

  /// Mean of a slice of the latency samples, in order of when they happened.
  double _decile(bool last) {
    final l = Audio.instance.sfxLatencies;
    if (l.length < 20) return 0;
    final n = max(1, l.length ~/ 10);
    final slice = last ? l.sublist(l.length - n) : l.sublist(0, n);
    return slice.reduce((a, b) => a + b) / slice.length;
  }

  int _percentile(int p) {
    final l = [...Audio.instance.sfxLatencies]..sort();
    if (l.isEmpty) return 0;
    return l[(l.length * p ~/ 100).clamp(0, l.length - 1)];
  }

  @override
  Widget build(BuildContext context) {
    final a = Audio.instance;
    final first = _decile(false), last = _decile(true);
    // Under 1.3x is noise; a real accumulation climbs much harder than this.
    final drift = first > 0 ? last / first : 1.0;
    final healthy = a.sfxFailed == 0 && drift < 1.3;

    return Scaffold(
      backgroundColor: AppTheme.bg,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        title: const Text('Audio soak', style: TextStyle(fontSize: 18)),
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Text(
                'Fires $_perSecond effects a second, drawn at random from '
                '${_pool.length} samples. Watch the drift: a leak shows up '
                'there long before anything goes silent.',
                style: const TextStyle(fontSize: 13, color: AppTheme.body, height: 1.4),
              ),
              const SizedBox(height: 18),
              Row(
                children: [
                  for (final d in [60, 180, 600])
                    Padding(
                      padding: const EdgeInsets.only(right: 8),
                      child: ChoiceChip(
                        label: Text(d < 60 ? '${d}s' : '${d ~/ 60}m'),
                        selected: _durationS == d,
                        onSelected:
                            _running ? null : (_) => setState(() => _durationS = d),
                      ),
                    ),
                  const Spacer(),
                  FilledButton(
                    onPressed: _running ? _stop : _start,
                    child: Text(_running ? 'Stop' : 'Run'),
                  ),
                ],
              ),
              const SizedBox(height: 18),
              LinearProgressIndicator(
                value: _running ? _elapsed / _durationS : (_elapsed > 0 ? 1 : 0),
                backgroundColor: AppTheme.card,
                color: AppTheme.accent,
              ),
              const SizedBox(height: 22),
              _row('elapsed', '${_elapsed}s / ${_durationS}s'),
              _row('attempted', '${a.sfxAttempts}'),
              _row('played', '${a.sfxPlayed}'),
              _row('failed', '${a.sfxFailed}', bad: a.sfxFailed > 0),
              _row('dropped by limiter', '${a.sfxLimited}'),
              const Divider(height: 28, color: AppTheme.border),
              _row('latency p50', '${_percentile(50)} ms'),
              _row('latency p95', '${_percentile(95)} ms'),
              _row('latency max', '${_percentile(100)} ms'),
              const SizedBox(height: 8),
              _row('first decile', '${first.toStringAsFixed(1)} ms'),
              _row('last decile', '${last.toStringAsFixed(1)} ms'),
              _row('drift', '${drift.toStringAsFixed(2)}x',
                  bad: drift >= 1.3, good: drift < 1.3 && first > 0),
              const Spacer(),
              if (_elapsed > 0 && !_running)
                Container(
                  padding: const EdgeInsets.all(14),
                  decoration: AppTheme.glass(
                      radius: 14,
                      outline: healthy ? AppTheme.accent : const Color(0xFFE0566A)),
                  child: Text(
                    healthy
                        ? 'Flat. No failures and latency is not climbing — the '
                            'player pool is holding.'
                        : 'Degrading. ${a.sfxFailed} failures, latency '
                            '${drift.toStringAsFixed(2)}x higher at the end than '
                            'the start. Something is accumulating.',
                    style: const TextStyle(fontSize: 13, color: AppTheme.text, height: 1.4),
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _row(String label, String value, {bool bad = false, bool good = false}) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 3),
      child: Row(
        children: [
          Text(label,
              style: const TextStyle(
                  fontFamily: AppTheme.fontMono, fontSize: 12, color: AppTheme.muted)),
          const Spacer(),
          Text(value,
              style: TextStyle(
                  fontFamily: AppTheme.fontMono,
                  fontSize: 13,
                  color: bad
                      ? const Color(0xFFE0566A)
                      : good
                          ? AppTheme.accent
                          : AppTheme.text)),
        ],
      ),
    );
  }
}
