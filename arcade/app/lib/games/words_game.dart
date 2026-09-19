import 'dart:math';

import 'package:flutter/material.dart';

import '../audio.dart';
import '../theme.dart';
import 'game_scaffold.dart';
import 'word_list.dart';

enum _Mark { none, absent, present, correct }

/// Five-letter word guessing game. Six tries, color feedback.
class WordsGame extends StatefulWidget {
  const WordsGame({super.key});

  @override
  State<WordsGame> createState() => _WordsGameState();
}

class _WordsGameState extends State<WordsGame> {
  static const rows = 6;
  static const cols = 5;

  late String answer;
  final guesses = <String>[];
  String current = '';
  bool won = false;
  bool lost = false;
  final keyMarks = <String, _Mark>{};
  String? toast;

  @override
  void initState() {
    super.initState();
    _reset();
  }

  void _reset() {
    answer = wordList[Random().nextInt(wordList.length)];
    guesses.clear();
    current = '';
    won = false;
    lost = false;
    keyMarks.clear();
    toast = null;
  }

  List<_Mark> _markGuess(String guess) {
    final marks = List.filled(cols, _Mark.absent);
    final remaining = answer.split('');
    for (var i = 0; i < cols; i++) {
      if (guess[i] == answer[i]) {
        marks[i] = _Mark.correct;
        remaining[i] = '';
      }
    }
    for (var i = 0; i < cols; i++) {
      if (marks[i] == _Mark.correct) continue;
      final idx = remaining.indexOf(guess[i]);
      if (idx != -1) {
        marks[i] = _Mark.present;
        remaining[idx] = '';
      }
    }
    return marks;
  }

  void _key(String k) {
    if (won || lost) return;
    Audio.instance.tap();
    setState(() {
      toast = null;
      if (k == '⌫') {
        if (current.isNotEmpty) current = current.substring(0, current.length - 1);
      } else if (k == 'ENTER') {
        if (current.length < cols) {
          toast = 'Not enough letters';
          Audio.instance.invalid();
          return;
        }
        if (!wordSet.contains(current)) {
          toast = 'Not in word list';
          Audio.instance.invalid();
          return;
        }
        final marks = _markGuess(current);
        for (var i = 0; i < cols; i++) {
          final c = current[i];
          final prev = keyMarks[c] ?? _Mark.none;
          if (marks[i].index > prev.index) keyMarks[c] = marks[i];
        }
        guesses.add(current);
        if (current == answer) {
          won = true;
          Audio.instance.win();
        } else if (guesses.length == rows) {
          lost = true;
          Audio.instance.lose();
        } else {
          Audio.instance.pop(marks.where((m) => m == _Mark.correct).length.clamp(1, 3));
        }
        current = '';
      } else if (current.length < cols) {
        current += k;
      }
    });
  }

  static String _assetFor(_Mark m) => switch (m) {
        _Mark.correct => 'assets/images/word_correct.png',
        _Mark.present => 'assets/images/word_present.png',
        _Mark.absent => 'assets/images/word_absent.png',
        _Mark.none => 'assets/images/word_empty.png',
      };

  static Color _textFor(_Mark m) => m == _Mark.correct ? const Color(0xFF030303) : AppTheme.text;

  @override
  Widget build(BuildContext context) {
    return GameScaffold(
      title: 'Words',
      onReset: () => setState(_reset),
      gameOver: won || lost,
      gameOverText: won ? 'You got it' : 'It was $answer',
      bottom: _Keyboard(marks: keyMarks, onKey: _key),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          SizedBox(
            height: 28,
            child: toast == null
                ? null
                : Text(toast!,
                    style: const TextStyle(fontFamily: AppTheme.fontMono, color: AppTheme.accent)),
          ),
          for (var r = 0; r < rows; r++)
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 3),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [for (var c = 0; c < cols; c++) _cell(r, c)],
              ),
            ),
        ],
      ),
    );
  }

  Widget _cell(int r, int c) {
    String letter = '';
    _Mark mark = _Mark.none;
    if (r < guesses.length) {
      letter = guesses[r][c];
      mark = _markGuess(guesses[r])[c];
    } else if (r == guesses.length && c < current.length) {
      letter = current[c];
    }
    return Container(
      width: 56,
      height: 56,
      margin: const EdgeInsets.symmetric(horizontal: 3),
      child: Stack(
        fit: StackFit.expand,
        children: [
          Image.asset(_assetFor(mark), fit: BoxFit.fill),
          Center(
            child: Text(letter,
                style: TextStyle(
                    fontFamily: AppTheme.fontMono,
                    fontSize: 26,
                    fontWeight: FontWeight.w700,
                    color: _textFor(mark))),
          ),
        ],
      ),
    );
  }
}

class _Keyboard extends StatelessWidget {
  final Map<String, _Mark> marks;
  final void Function(String) onKey;
  const _Keyboard({required this.marks, required this.onKey});

  static const rowsKeys = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM'];

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        for (var i = 0; i < rowsKeys.length; i++)
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 3),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                if (i == 2) _key('ENTER', flex: 3),
                for (final k in rowsKeys[i].split('')) _key(k),
                if (i == 2) _key('⌫', flex: 3),
              ],
            ),
          ),
      ],
    );
  }

  Widget _key(String k, {int flex = 2}) {
    final mark = marks[k] ?? _Mark.none;
    final (fill, outline, fg) = switch (mark) {
      _Mark.correct => (AppTheme.accent, AppTheme.accentHover, const Color(0xFF030303)),
      _Mark.present => (const Color(0x33EA952D), const Color(0xAAEA952D), AppTheme.text),
      _Mark.absent => (AppTheme.surface, AppTheme.border, AppTheme.dim),
      _Mark.none => (AppTheme.glassFill, AppTheme.borderStrong, AppTheme.text),
    };
    return Expanded(
      flex: flex,
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 2),
        child: Material(
          color: Colors.transparent,
          child: InkWell(
            borderRadius: BorderRadius.circular(8),
            onTap: () => onKey(k),
            child: Container(
              height: 48,
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
