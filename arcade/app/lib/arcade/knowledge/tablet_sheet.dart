import 'dart:async';

import 'package:flutter/material.dart';

import '../../audio.dart';
import '../../theme.dart';
import '../api.dart';

/// One Knowledge Tablet as issued by the server: a signed, single-use
/// question with shuffled options and no answer key.
class TabletQuestion {
  final String token;
  final int index, total;
  final String tier, section, prompt;
  final List<String> options;
  final Duration minLatency, window;

  /// Throws [ApiException], never `TypeError` — see `field()` in api.dart.
  TabletQuestion.fromJson(Map<String, dynamic> j)
      : token = field(j, 'token'),
        index = intField(j, 'index'),
        total = intField(j, 'total'),
        tier = field(j, 'tier'),
        section = field(j, 'section'),
        prompt = field(j, 'prompt'),
        options = stringsField(j, 'options'),
        minLatency = Duration(milliseconds: intField(j, 'minLatencyMs')),
        window = Duration(milliseconds: intField(j, 'windowMs'));
}

/// The server's verdict on an answer.
class TabletVerdict {
  final bool correct;
  final int correctOption;
  final String correctText, explanation, source;
  final String? reason; // too_fast | timed_out

  TabletVerdict.fromJson(Map<String, dynamic> j)
      : correct = j['correct'] == true,
        correctOption = intField(j, 'correctOption'),
        correctText = field(j, 'correctText'),
        explanation = field(j, 'explanation'),
        source = field(j, 'source'),
        reason = j['reason'] is String ? j['reason'] as String : null;
}

typedef AnswerFn = Future<TabletVerdict> Function(int? choice);

/// Presents one tablet: the server's 20 s window, options locked until the
/// tier's minimum latency, explanation on a miss. Resolves true if correct.
Future<bool> showTablet(BuildContext context, TabletQuestion q, {required AnswerFn answer}) async {
  final result = await showModalBottomSheet<bool>(
    context: context,
    isDismissible: false,
    enableDrag: false,
    isScrollControlled: true,
    backgroundColor: Colors.transparent,
    builder: (_) => _TabletSheet(q: q, answer: answer),
  );
  return result ?? false;
}

class _TabletSheet extends StatefulWidget {
  final TabletQuestion q;
  final AnswerFn answer;
  const _TabletSheet({required this.q, required this.answer});

  @override
  State<_TabletSheet> createState() => _TabletSheetState();
}

class _TabletSheetState extends State<_TabletSheet> {
  late final DateTime shownAt = DateTime.now();
  Timer? _tick;
  double remaining = 1.0;
  bool unlocked = false;
  int? chosen;
  bool sending = false;
  TabletVerdict? verdict;
  String? error;

  @override
  void initState() {
    super.initState();
    Audio.instance.coinFlip();
    _tick = Timer.periodic(const Duration(milliseconds: 100), (_) {
      final elapsed = DateTime.now().difference(shownAt);
      setState(() {
        remaining = (1 - elapsed.inMilliseconds / widget.q.window.inMilliseconds).clamp(0.0, 1.0);
        unlocked = elapsed >= widget.q.minLatency;
      });
      if (elapsed >= widget.q.window && chosen == null && !sending) _answer(null);
    });
  }

  @override
  void dispose() {
    _tick?.cancel();
    super.dispose();
  }

  Future<void> _answer(int? opt) async {
    if (chosen != null || verdict != null || sending) return;
    _tick?.cancel();
    setState(() {
      chosen = opt ?? -1;
      sending = true;
    });
    try {
      final v = await widget.answer(opt);
      if (!mounted) return;
      setState(() {
        verdict = v;
        sending = false;
      });
      v.correct ? Audio.instance.ting() : Audio.instance.invalid();
    } catch (e) {
      if (!mounted) return;
      setState(() {
        error = 'Could not reach the arcade server — this tablet stays closed.';
        sending = false;
      });
      Audio.instance.invalid();
    }
  }

  @override
  Widget build(BuildContext context) {
    final q = widget.q;
    final v = verdict;
    final done = v != null || error != null;
    return Padding(
      padding: EdgeInsets.only(bottom: MediaQuery.viewInsetsOf(context).bottom),
      child: Container(
        margin: const EdgeInsets.all(12),
        padding: const EdgeInsets.all(22),
        decoration: AppTheme.glass(radius: 24, fill: AppTheme.card, outline: AppTheme.borderStrong),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(children: [
              Image.asset('assets/images/logo_orange.png', width: 18, height: 18),
              const SizedBox(width: 8),
              Expanded(
                child: Text('TABLET ${q.index}/${q.total} · ${q.section.toUpperCase()}',
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(
                        fontFamily: AppTheme.fontMono, fontSize: 10, letterSpacing: 1.1, color: AppTheme.muted)),
              ),
              const SizedBox(width: 8),
              _Tier(q.tier),
            ]),
            const SizedBox(height: 10),
            ClipRRect(
              borderRadius: BorderRadius.circular(999),
              child: LinearProgressIndicator(
                value: done ? 1 : remaining,
                minHeight: 4,
                backgroundColor: AppTheme.surface,
                color: !done
                    ? (remaining < 0.25 ? AppTheme.danger : AppTheme.accent)
                    : ((v?.correct ?? false) ? AppTheme.success : AppTheme.danger),
              ),
            ),
            const SizedBox(height: 16),
            Text(q.prompt,
                style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w600, height: 1.3, color: AppTheme.text)),
            const SizedBox(height: 16),
            for (var i = 0; i < q.options.length; i++) _option(i),
            if (sending)
              const Padding(
                padding: EdgeInsets.symmetric(vertical: 8),
                child: Center(child: SizedBox(width: 18, height: 18, child: CircularProgressIndicator(strokeWidth: 2, color: AppTheme.accent))),
              ),
            if (done) ...[
              const SizedBox(height: 12),
              Container(
                padding: const EdgeInsets.all(14),
                decoration: AppTheme.glass(
                    radius: 14,
                    fill: (v?.correct ?? false) ? const Color(0x1428C93F) : const Color(0x14FF6568),
                    outline: (v?.correct ?? false) ? AppTheme.success : AppTheme.danger),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                        v == null
                            ? 'CONNECTION LOST'
                            : v.correct
                                ? 'TABLET OPENED'
                                : v.reason == 'too_fast'
                                    ? 'TOO FAST — ${v.correctText.toUpperCase()}'
                                    : v.reason == 'timed_out'
                                        ? 'OUT OF TIME — ${v.correctText.toUpperCase()}'
                                        : 'NOT QUITE — ${v.correctText.toUpperCase()}',
                        style: TextStyle(
                            fontFamily: AppTheme.fontMono,
                            fontSize: 10,
                            letterSpacing: 1.1,
                            color: (v?.correct ?? false) ? AppTheme.success : AppTheme.danger)),
                    const SizedBox(height: 6),
                    Text(v?.explanation ?? error!,
                        style: const TextStyle(fontSize: 14, height: 1.4, color: AppTheme.text)),
                    if (v != null) ...[
                      const SizedBox(height: 4),
                      Text(v.source,
                          style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, color: AppTheme.muted)),
                    ],
                  ],
                ),
              ),
              const SizedBox(height: 14),
              SizedBox(
                width: double.infinity,
                child: FilledButton(
                  onPressed: () => Navigator.pop(context, v?.correct ?? false),
                  child: Text((v?.correct ?? false) ? 'Keep running' : 'Continue'),
                ),
              ),
            ],
          ],
        ),
      ),
    );
  }

  Widget _option(int i) {
    final o = widget.q.options[i];
    final picked = chosen == i;
    final v = verdict;
    Color outline = AppTheme.borderStrong;
    Color fill = AppTheme.glassFill;
    if (v != null) {
      if (i == v.correctOption) {
        outline = AppTheme.success;
        fill = const Color(0x2228C93F);
      } else if (picked) {
        outline = AppTheme.danger;
        fill = const Color(0x22FF6568);
      }
    } else if (picked) {
      outline = AppTheme.accent;
    }
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          borderRadius: BorderRadius.circular(14),
          onTap: (unlocked && chosen == null) ? () => _answer(i) : null,
          child: AnimatedOpacity(
            duration: const Duration(milliseconds: 200),
            opacity: unlocked || v != null ? 1 : 0.55,
            child: Container(
              width: double.infinity,
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 13),
              decoration: AppTheme.glass(radius: 14, fill: fill, outline: outline),
              child: Text(o, style: const TextStyle(fontSize: 15, color: AppTheme.text)),
            ),
          ),
        ),
      ),
    );
  }
}

class _Tier extends StatelessWidget {
  final String tier;
  const _Tier(this.tier);

  @override
  Widget build(BuildContext context) {
    final label = switch (tier) {
      'A' => 'DEFINITION',
      'B' => 'MECHANICS',
      'C' => 'TRAP',
      _ => 'NUMBERS',
    };
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
      decoration: AppTheme.glass(radius: 999),
      child: Text(label,
          style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 9, letterSpacing: 1, color: AppTheme.accent)),
    );
  }
}
