/// Daily Ledger — one puzzle per UTC day, the same for everyone. The puzzle
/// list, the answer and the scoring live on the server (arcade/server,
/// ledger.ts); the client only renders the state it is given. Fixed XP on
/// solve, so there is nothing to brute-force with alts.
library;

enum LedgerKind { word, number }

enum Mark { absent, present, correct }

Mark markFrom(String s) => switch (s) {
      'correct' => Mark.correct,
      'present' => Mark.present,
      _ => Mark.absent,
    };

/// Server state for today's ledger (`GET /v1/ledger/today`, `POST /v1/ledger/guess`).
class LedgerState {
  final int day;
  final LedgerKind kind;
  final int length;
  final String clue;
  final int attempts;
  final List<String> guesses;
  final List<List<Mark>> marks;
  final bool solved, over;
  final int xpGained;
  final String? answer, source; // only once the play is over
  final int streak;
  final List<String> badges;

  LedgerState.fromJson(Map<String, dynamic> j)
      : day = (j['day'] as num).toInt(),
        kind = j['kind'] == 'number' ? LedgerKind.number : LedgerKind.word,
        length = (j['length'] as num).toInt(),
        clue = j['clue'] as String,
        attempts = (j['attempts'] as num?)?.toInt() ?? 6,
        guesses = (j['guesses'] as List).cast<String>(),
        marks = [for (final row in j['marks'] as List) [for (final m in row as List) markFrom(m as String)]],
        solved = j['solved'] == true,
        over = j['over'] == true,
        xpGained = (j['xpGained'] as num?)?.toInt() ?? 0,
        answer = j['answer'] as String?,
        source = j['source'] as String?,
        streak = (j['streak'] as num?)?.toInt() ?? 0,
        badges = (j['badges'] as List?)?.cast<String>() ?? const [];
}

/// Shareable grid (no answer leaks).
String shareGrid(LedgerState s) {
  final rows = s.marks
      .map((r) => r.map((m) => switch (m) {
            Mark.correct => '🟩',
            Mark.present => '🟨',
            Mark.absent => '⬛',
          }).join())
      .join('\n');
  return 'Daily Ledger #${s.day} ${s.solved ? s.guesses.length : 'X'}/${s.attempts}\n$rows';
}
