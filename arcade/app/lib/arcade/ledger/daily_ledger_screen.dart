import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../audio.dart';
import '../../theme.dart';
import '../api.dart';
import '../progress.dart';
import 'daily_ledger.dart';

class DailyLedgerScreen extends StatefulWidget {
  const DailyLedgerScreen({super.key});

  @override
  State<DailyLedgerScreen> createState() => _DailyLedgerScreenState();
}

class _DailyLedgerScreenState extends State<DailyLedgerScreen> {
  LedgerState? s;
  String current = '';
  bool sending = false;
  String? toast;
  String? error;
  final keyMarks = <String, Mark>{};

  int get rows => s?.attempts ?? 6;
  bool get over => s?.over ?? true;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    setState(() => error = null);
    try {
      await ArcadeApi.instance.init();
      _apply(LedgerState.fromJson(await ArcadeApi.instance.ledgerToday()));
    } on ApiException catch (e) {
      ArcadeProgress.instance.offline = e.offline;
      if (!mounted) return;
      setState(() => error = e.offline
          ? 'The arcade server is unreachable. The Daily Ledger is scored there, so it needs a connection.'
          : 'Could not load today\'s ledger (${e.code}).');
    }
  }

  void _apply(LedgerState next) {
    // Every caller reaches here after an await that can take up to the 8 s HTTP
    // timeout, so the screen may well be gone by now.
    if (!mounted) return;
    keyMarks.clear();
    for (var g = 0; g < next.guesses.length; g++) {
      final guess = next.guesses[g], m = next.marks[g];
      for (var i = 0; i < guess.length; i++) {
        final prev = keyMarks[guess[i]];
        if (prev == null || m[i].index > prev.index) keyMarks[guess[i]] = m[i];
      }
    }
    setState(() => s = next);
  }

  Future<void> _submit() async {
    final st = s;
    if (st == null || st.over || sending) return;
    if (current.length < st.length) {
      setState(() => toast = 'Not enough ${st.kind == LedgerKind.word ? 'letters' : 'digits'}');
      Audio.instance.invalid();
      return;
    }
    Audio.instance.coinFlip();
    setState(() {
      toast = null;
      sending = true;
    });
    try {
      final r = await ArcadeApi.instance.ledgerGuess(current);
      final next = LedgerState.fromJson(r);
      current = '';
      _apply(next);
      if (r['progress'] is Map<String, dynamic>) {
        ArcadeProgress.instance.apply(r['progress'] as Map<String, dynamic>);
      }
      if (next.over) next.solved ? Audio.instance.win() : Audio.instance.lose();
    } on ApiException catch (e) {
      if (e.body != null && e.body!['day'] != null) _apply(LedgerState.fromJson(e.body!));
      if (!mounted) return;
      setState(() => toast = e.offline ? 'Server unreachable — guess not counted' : 'Rejected: ${e.code}');
      Audio.instance.invalid();
    } finally {
      if (mounted) setState(() => sending = false);
    }
  }

  void _key(String k) {
    final st = s;
    if (st == null || st.over || sending) return;
    Audio.instance.tap();
    setState(() {
      toast = null;
      if (k == '⌫') {
        if (current.isNotEmpty) current = current.substring(0, current.length - 1);
      } else if (k == 'ENTER') {
        _submit();
      } else if (current.length < st.length) {
        current += k;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    final st = s;
    if (st == null) {
      return Scaffold(
        backgroundColor: AppTheme.bg,
        body: SafeArea(
          child: Stack(children: [
            Align(
              alignment: Alignment.topLeft,
              child: IconButton(onPressed: () => Navigator.pop(context), icon: const Icon(Icons.arrow_back, color: AppTheme.text)),
            ),
            Center(
              child: error == null
                  ? const CircularProgressIndicator(color: AppTheme.accent)
                  : Container(
                      margin: const EdgeInsets.all(24),
                      padding: const EdgeInsets.all(20),
                      decoration: AppTheme.glass(radius: 18, fill: AppTheme.card, outline: AppTheme.danger),
                      child: Column(mainAxisSize: MainAxisSize.min, children: [
                        const Icon(Icons.cloud_off_rounded, color: AppTheme.danger),
                        const SizedBox(height: 10),
                        Text(error!, textAlign: TextAlign.center, style: const TextStyle(color: AppTheme.text, height: 1.4)),
                        const SizedBox(height: 14),
                        FilledButton(onPressed: _load, child: const Text('Try again')),
                      ]),
                    ),
            ),
          ]),
        ),
      );
    }
    final puzzle = st;
    final day = st.day;
    final isWord = puzzle.kind == LedgerKind.word;
    final p = ArcadeProgress.instance;
    return Scaffold(
      backgroundColor: AppTheme.bg,
      body: Stack(
        children: [
          Positioned.fill(child: Image.asset('assets/images/bg_dark.png', fit: BoxFit.cover)),
          SafeArea(
            child: Column(
              children: [
                Padding(
                  padding: const EdgeInsets.fromLTRB(8, 6, 16, 0),
                  child: Row(children: [
                    IconButton(
                        onPressed: () => Navigator.pop(context),
                        icon: const Icon(Icons.arrow_back, color: AppTheme.text)),
                    Text('DAILY LEDGER #$day',
                        style: const TextStyle(
                            fontFamily: AppTheme.fontMono, fontSize: 11, letterSpacing: 1.2, color: AppTheme.muted)),
                    const Spacer(),
                    ListenableBuilder(
                      listenable: p,
                      builder: (_, __) => Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                        decoration: AppTheme.glass(radius: 999, outline: AppTheme.borderStrong),
                        child: Row(children: [
                          const Icon(Icons.local_fire_department_rounded, size: 14, color: AppTheme.accent),
                          const SizedBox(width: 4),
                          Text('${p.streak}',
                              style: const TextStyle(
                                  fontFamily: AppTheme.fontMono, fontSize: 13, fontWeight: FontWeight.w700, color: AppTheme.text)),
                        ]),
                      ),
                    ),
                  ]),
                ),
                Padding(
                  padding: const EdgeInsets.fromLTRB(24, 10, 24, 0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(isWord ? 'GLOSSARY TERM' : 'WHITE PAPER FIGURE',
                          style: const TextStyle(
                              fontFamily: AppTheme.fontMono, fontSize: 10, letterSpacing: 1.2, color: AppTheme.accent)),
                      const SizedBox(height: 6),
                      Text(puzzle.clue,
                          style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w600, height: 1.3, color: AppTheme.text)),
                    ],
                  ),
                ),
                const SizedBox(height: 10),
                SizedBox(
                    height: 22,
                    child: toast == null
                        ? null
                        : Text(toast!, style: const TextStyle(fontFamily: AppTheme.fontMono, color: AppTheme.accent))),
                Expanded(
                  child: Center(
                    child: FittedBox(
                      fit: BoxFit.scaleDown,
                      child: Column(
                        mainAxisSize: MainAxisSize.min,
                        children: [for (var r = 0; r < rows; r++) _row(r)],
                      ),
                    ),
                  ),
                ),
                if (over) _endCard(),
                Padding(
                  padding: const EdgeInsets.fromLTRB(6, 6, 6, 12),
                  child: isWord ? _lettersKeyboard() : _digitsKeyboard(),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _row(int r) {
    final st = s!;
    final n = st.length;
    String text = '';
    List<Mark>? marks;
    if (r < st.guesses.length) {
      text = st.guesses[r];
      marks = st.marks[r];
    } else if (r == st.guesses.length) {
      text = current;
    }
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 3),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          for (var c = 0; c < n; c++)
            Container(
              width: 46,
              height: 46,
              margin: const EdgeInsets.symmetric(horizontal: 3),
              child: Stack(fit: StackFit.expand, children: [
                Image.asset(
                    marks == null
                        ? 'assets/images/word_empty.png'
                        : switch (marks[c]) {
                            Mark.correct => 'assets/images/word_correct.png',
                            Mark.present => 'assets/images/word_present.png',
                            Mark.absent => 'assets/images/word_absent.png',
                          },
                    fit: BoxFit.fill),
                Center(
                  child: Text(c < text.length ? text[c] : '',
                      style: TextStyle(
                          fontFamily: AppTheme.fontMono,
                          fontSize: 22,
                          fontWeight: FontWeight.w700,
                          color: marks != null && marks[c] == Mark.correct ? const Color(0xFF030303) : AppTheme.text)),
                ),
              ]),
            ),
        ],
      ),
    );
  }

  Widget _endCard() {
    final st = s!;
    final solved = st.solved;
    final grid = shareGrid(st);
    return Container(
      margin: const EdgeInsets.fromLTRB(16, 0, 16, 8),
      padding: const EdgeInsets.all(16),
      decoration: AppTheme.glass(radius: 18, fill: AppTheme.card, outline: solved ? AppTheme.success : AppTheme.borderStrong),
      child: Row(children: [
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(solved ? 'LEDGER BALANCED' : 'IT WAS ${st.answer ?? '?'}',
                style: TextStyle(
                    fontFamily: AppTheme.fontMono, fontSize: 10, letterSpacing: 1.2, color: solved ? AppTheme.success : AppTheme.danger)),
            const SizedBox(height: 4),
            Text('${st.answer ?? ''}  ·  ${st.source ?? ''}',
                style: const TextStyle(fontSize: 14, color: AppTheme.text)),
            Text('+${st.xpGained} XP  ·  streak ${st.streak}',
                style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 12, color: AppTheme.accent)),
            const Text('Next ledger at 00:00 UTC',
                style: TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, color: AppTheme.muted)),
          ]),
        ),
        IconButton(
          tooltip: 'Copy result',
          onPressed: () {
            Clipboard.setData(ClipboardData(text: grid));
            Audio.instance.ting();
            ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Result copied')));
          },
          icon: const Icon(Icons.copy_rounded, color: AppTheme.text),
        ),
      ]),
    );
  }

  Widget _lettersKeyboard() {
    const rowsKeys = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM'];
    return Column(mainAxisSize: MainAxisSize.min, children: [
      for (var i = 0; i < rowsKeys.length; i++)
        Padding(
          padding: const EdgeInsets.symmetric(vertical: 3),
          child: Row(mainAxisAlignment: MainAxisAlignment.center, children: [
            if (i == 2) _keyBtn('ENTER', flex: 3),
            for (final k in rowsKeys[i].split('')) _keyBtn(k),
            if (i == 2) _keyBtn('⌫', flex: 3),
          ]),
        ),
    ]);
  }

  Widget _digitsKeyboard() {
    return Column(mainAxisSize: MainAxisSize.min, children: [
      Row(mainAxisAlignment: MainAxisAlignment.center, children: [for (final k in '12345'.split('')) _keyBtn(k)]),
      const SizedBox(height: 6),
      Row(mainAxisAlignment: MainAxisAlignment.center, children: [for (final k in '67890'.split('')) _keyBtn(k)]),
      const SizedBox(height: 6),
      Row(mainAxisAlignment: MainAxisAlignment.center, children: [_keyBtn('ENTER', flex: 3), _keyBtn('⌫', flex: 3)]),
    ]);
  }

  Widget _keyBtn(String k, {int flex = 2}) {
    final mark = keyMarks[k];
    final (fill, outline, fg) = switch (mark) {
      Mark.correct => (AppTheme.accent, AppTheme.accentHover, const Color(0xFF030303)),
      Mark.present => (const Color(0x33EA952D), const Color(0xAAEA952D), AppTheme.text),
      Mark.absent => (AppTheme.surface, AppTheme.border, AppTheme.dim),
      null => (AppTheme.glassFill, AppTheme.borderStrong, AppTheme.text),
    };
    return Expanded(
      flex: flex,
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 2),
        child: Material(
          color: Colors.transparent,
          child: InkWell(
            borderRadius: BorderRadius.circular(8),
            onTap: over ? null : () => _key(k),
            child: Container(
              height: 46,
              decoration: AppTheme.glass(radius: 8, fill: fill, outline: outline),
              child: Center(
                child: Text(k,
                    style: TextStyle(
                        fontFamily: AppTheme.fontMono,
                        fontSize: k.length > 1 ? 11 : 16,
                        fontWeight: FontWeight.w700,
                        color: fg)),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
