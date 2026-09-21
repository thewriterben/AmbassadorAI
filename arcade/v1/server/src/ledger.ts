import { config } from './config.ts';

// Daily Ledger — one puzzle per UTC day, same for everyone. The answer never
// leaves the server until the play is over. Mirrors the client's old
// daily_ledger.dart item lists exactly so #day numbering stays continuous.

export type LedgerKind = 'word' | 'number';
export type Mark = 'absent' | 'present' | 'correct';

interface Item { answer: string; clue: string; source: string }

const words: Item[] = [
  { answer: 'SCARCITY', clue: 'Pillar: supply limited by transparent, predictable rules', source: 'WP §2.2' },
  { answer: 'PILLAR', clue: 'One of six in the framework of perfect money', source: 'WP §2.2' },
  { answer: 'HAYEK', clue: 'Economist behind "let the best money win"', source: 'dgd-overview.md' },
  { answer: 'TREASURY', clue: 'Where unclaimed coins stay — never redistributed to others', source: 'WP §5.6' },
  { answer: 'WALLET', clue: 'Where released coins actually land (QT, desktop only)', source: 'WP §5.6' },
  { answer: 'BURNED', clue: 'What happens to transaction fees and staking rewards', source: 'WP §5' },
  { answer: 'BENCHMARK', clue: 'DGSB: a frozen reference point, like the meter', source: 'WP §3.1' },
  { answer: 'HOLDERS', clue: 'The adoption metric carrying 70% of CFV weight', source: 'WP §4' },
  { answer: 'DECREE', clue: 'Free Adoption: money must be chosen, not imposed by ___', source: 'WP §2.2' },
  { answer: 'ONION', clue: "Tor V3 ___ addressing, DGD's native privacy layer", source: 'WP §2.2' },
  { answer: 'STAKING', clue: '2,000,000 DGD are permanently locked for this', source: 'WP §5' },
  { answer: 'ESCROW', clue: 'Planned Marketplace & ___ — coming, not live', source: 'platform-and-tools.md' },
  { answer: 'CIRCULATE', clue: 'A coin becomes money when it can ___ link by link', source: 'WP Abstract, §9' },
  { answer: 'RELEASE', clue: 'Each confirmed account advances the curve one ___', source: 'WP §5' },
  { answer: 'ADOPTION', clue: 'Pillar of free choice; also the 70% CFV metric', source: 'WP §2.2, §4' },
  { answer: 'MERCHANT', clue: 'Under single price, a ___ can hold DGD and pay suppliers in it', source: 'WP §8–9' },
  { answer: 'VOLUNTARY', clue: 'Participation is this — money chosen, never imposed', source: 'WP §2.2' },
  { answer: 'CONTINUOUS', clue: 'The distribution curve has no tiers; it is ___', source: 'WP §5.1' },
  { answer: 'INVERSION', clue: 'The White Paper calls fixed-at-inception rules an "___ of governance"', source: 'WP §12.14' },
  { answer: 'STANDARD', clue: 'The DGSB is a measurement ___, not a prediction', source: 'WP §3.1' },
];

const numbers: Item[] = [
  { answer: '21000000', clue: 'Total supply cap, in coins', source: 'WP §5' },
  { answer: '19000000', clue: 'Coins that can ever circulate', source: 'WP §5' },
  { answer: '2000000', clue: 'Coins permanently locked for staking', source: 'WP §5' },
  { answer: '80000000', clue: 'Account count at which distribution ends', source: 'WP §5' },
  { answer: '11712952', clue: 'Total per-signup releases across the whole curve', source: 'WP §5' },
  { answer: '96', clue: 'Percent of purchasing power the dollar lost since 1913', source: 'WP Abstract' },
  { answer: '35', clue: 'Years to halve purchasing power at a 2% inflation target', source: 'WP §2.2' },
  { answer: '1913', clue: 'The year the expedition starts', source: 'WP Abstract' },
  { answer: '70', clue: 'CFV weight, in percent, on adoption', source: 'WP §4' },
  { answer: '100000', clue: 'Bitcoin price, in dollars, at the moment the DGSB froze', source: 'WP §3.2' },
  { answer: '6', clue: 'Pillars of perfect money', source: 'WP §2.2' },
  { answer: '7000', clue: 'Fold increase in US money supply since 1913 (not percent)', source: 'six-pillars.md' },
  { answer: '1', clue: 'Referral levels DGD has', source: 'WP §10.1' },
  { answer: '2024', clue: 'Year the DGSB was frozen', source: 'WP §3.2' },
  { answer: '1976', clue: "Year of Hayek's \"The Denationalisation of Money\"", source: 'dgd-overview.md' },
];

export interface Puzzle { day: number; kind: LedgerKind; answer: string; clue: string; source: string }

export function todayIndex(now = Date.now()): number {
  return Math.floor((now - config.ledger.epochUtc) / 86_400_000);
}

export function puzzleFor(day: number): Puzzle {
  const word = day % 2 === 0;
  const list = word ? words : numbers;
  const i = Math.floor((day * 7919) / 2) % list.length;
  const it = list[i];
  return { day, kind: word ? 'word' : 'number', ...it };
}

/** Wordle-style marks with duplicate handling — identical to the client's old markGuess. */
export function markGuess(guess: string, answer: string): Mark[] {
  const n = answer.length;
  const marks: Mark[] = Array(n).fill('absent');
  const remaining = answer.split('');
  for (let i = 0; i < n; i++) {
    if (guess[i] === answer[i]) {
      marks[i] = 'correct';
      remaining[i] = '';
    }
  }
  for (let i = 0; i < n; i++) {
    if (marks[i] === 'correct') continue;
    const idx = remaining.indexOf(guess[i]);
    if (idx !== -1) {
      marks[i] = 'present';
      remaining[idx] = '';
    }
  }
  return marks;
}

export function validGuess(guess: string, p: Puzzle): boolean {
  if (guess.length !== p.answer.length) return false;
  return p.kind === 'word' ? /^[A-Z]+$/.test(guess) : /^[0-9]+$/.test(guess);
}
