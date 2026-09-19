import 'dart:math';

import 'package:flutter/material.dart';

import '../../audio.dart';
import '../../theme.dart';
import '../knowledge/content.dart';
import '../progress.dart';
import 'mini_shell.dart';

/// Chain Builder — drag the steps into the right order. Three chains a round.
class ChainBuilderScreen extends StatefulWidget {
  const ChainBuilderScreen({super.key});

  @override
  State<ChainBuilderScreen> createState() => _ChainBuilderScreenState();
}

class _ChainBuilderScreenState extends State<ChainBuilderScreen> {
  late List<Chain> round;
  int which = 0;
  late List<String> order;
  int solved = 0, checks = 0;
  List<bool>? marks; // per-position correctness after a check

  @override
  void initState() {
    super.initState();
    _begin();
  }

  /// See PillarSort: opened as play begins, awaited at the results sheet.
  Future<String?>? _round;

  void _begin() {
    _round = ArcadeProgress.instance.startMini('chain_builder');
    round = (List.of(chains)..shuffle(Random())).take(3).toList();
    which = 0;
    solved = checks = 0;
    _load();
    Audio.instance.coinsPour();
  }

  void _load() {
    final c = round[which];
    do {
      order = List.of(c.steps)..shuffle(Random());
    } while (order.join() == c.steps.join());
    marks = null;
  }

  Future<void> _check() async {
    final c = round[which];
    checks++;
    final m = [for (var i = 0; i < order.length; i++) order[i] == c.steps[i]];
    setState(() => marks = m);
    if (m.every((x) => x)) {
      solved++;
      Audio.instance.ting();
      await Future.delayed(const Duration(milliseconds: 700));
      if (!mounted) return;
      if (which + 1 < round.length) {
        setState(() {
          which++;
          _load();
        });
      } else {
        _finish();
      }
    } else {
      Audio.instance.invalid();
    }
  }

  bool _finishing = false;

  Future<void> _finish() async {
    // Re-entrancy guard. "Check the chain" stayed live through the 700 ms
    // advance delay, so a double-tap on the last chain double-counted the
    // solve, skipped a chain, and stacked two results sheets.
    if (_finishing) return;
    _finishing = true;
    final token = await _round;
    if (!mounted) return;
    final action = await showMiniResults(context,
        game: 'chain_builder',
        headline: 'Chain Builder',
        roundToken: token,
        right: solved,
        total: round.length,
        extra: max(0, checks - solved),
        note: 'Adequate Circulation: a coin is money once it flows link by link back to the raw material.');
    if (!mounted) return;
    action == 'again' ? setState(_begin) : Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    final c = round[which];
    return MiniShell(
      kicker: 'CHAIN BUILDER · ${which + 1}/${round.length}',
      title: c.title,
      pills: [('SOLVED', '$solved')],
      bottom: Padding(
        padding: const EdgeInsets.fromLTRB(16, 4, 16, 16),
        child: SizedBox(
          width: double.infinity,
          child: FilledButton(onPressed: _check, child: const Text('Check the chain')),
        ),
      ),
      child: Padding(
        padding: const EdgeInsets.fromLTRB(16, 12, 16, 0),
        child: Column(
          children: [
            Text('Drag the steps into order. Source: ${c.source}',
                style: const TextStyle(fontFamily: AppTheme.fontMono, fontSize: 11, color: AppTheme.muted)),
            const SizedBox(height: 10),
            Expanded(
              child: ReorderableListView(
                buildDefaultDragHandles: false,
                proxyDecorator: (child, _, __) => Material(color: Colors.transparent, child: child),
                onReorderItem: (a, b) {
                  setState(() {
                    if (b > a) b--;
                    final it = order.removeAt(a);
                    order.insert(b, it);
                    marks = null;
                  });
                  Audio.instance.coinRoll();
                },
                children: [
                  for (var i = 0; i < order.length; i++)
                    ReorderableDelayedDragStartListener(
                      key: ValueKey(order[i]),
                      index: i,
                      child: Container(
                        margin: const EdgeInsets.only(bottom: 8),
                        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 14),
                        decoration: AppTheme.glass(
                            radius: 14,
                            fill: AppTheme.card,
                            outline: marks == null
                                ? AppTheme.borderStrong
                                : (marks![i] ? AppTheme.success : AppTheme.danger)),
                        child: Row(children: [
                          Container(
                            width: 28,
                            height: 28,
                            alignment: Alignment.center,
                            decoration: const BoxDecoration(color: AppTheme.surface, shape: BoxShape.circle),
                            child: Text('${i + 1}',
                                style: const TextStyle(
                                    fontFamily: AppTheme.fontMono, fontSize: 12, fontWeight: FontWeight.w700, color: AppTheme.accent)),
                          ),
                          const SizedBox(width: 12),
                          Expanded(child: Text(order[i], style: const TextStyle(fontSize: 14, color: AppTheme.text, height: 1.3))),
                          ReorderableDragStartListener(
                              index: i, child: const Icon(Icons.drag_handle_rounded, color: AppTheme.muted)),
                        ]),
                      ),
                    ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
