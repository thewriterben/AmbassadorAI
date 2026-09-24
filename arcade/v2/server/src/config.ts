// Every limit the plan says is "config-driven" (§4.2) lives here, overridable
// by environment so the Foundation can retune without a deploy.

const num = (k: string, d: number) => (process.env[k] ? Number(process.env[k]) : d);

export const config = {
  port: num('PORT', 8787),
  dbPath: process.env.ARCADE_DB ?? 'data/arcade.sqlite',
  // A directory of .md bank files, or a single file. The client never sees it.
  bankPath: process.env.ARCADE_BANK ?? 'data/bank',
  // HMAC key for signed question tokens. Must be set in production.
  secret: process.env.ARCADE_SECRET ?? 'dev-only-secret-change-me',
  production: process.env.NODE_ENV === 'production',
  corsOrigins: (process.env.ARCADE_CORS ?? '*').split(',').map((s) => s.trim()),
  // Set only when a proxy you control sits in front and appends
  // X-Forwarded-For. Off by default: trusting that header when nothing sets it
  // hands every client its own rate-limit bucket, which is no limit at all.
  trustProxy: process.env.ARCADE_TRUST_PROXY === '1',

  // XP rules (plan §3, §4.2). Explorer track only; no monetary value.
  xp: {
    tablet: 20,
    expedition: 100,
    ledger: 50,
    streak7: 100,
    levelSize: 500,
    miniPerRight: 5,
    miniCleanBonus: 40,
    chainSolved: 25,
    chainExtraCheck: 3,
  },

  tablets: {
    perExpedition: num('TABLETS_PER_EXPEDITION', 3), // 3 Explorer, 5 Validator
    answerWindowMs: 20_000, // player has 20 s once the tablet is issued
    graceMs: 4_000, // network + sheet animation slack
    minLatencyMs: { A: 1500, B: 2000, C: 2500, D: 3000 } as Record<string, number>,
    retireDays: 14,
    missDays: [1, 3, 7],
    // One retry per day per expedition (plan §3.1). We model it as: at most
    // N rewarded expeditions/day; further runs are XP-free practice.
    rewardedPerDay: num('REWARDED_EXPEDITIONS_PER_DAY', 2),
  },

  run: {
    // Client run: length 300*115 px at speed 300→375 px/s ≈ 102 s of pure
    // running. Pauses (tablets) only add time, so a finish that arrives sooner
    // than this after start is not a human run.
    minFinishMs: num('RUN_MIN_FINISH_MS', 85_000),
    // Tablet i sits at fraction (i+1)/(n+1)*0.92+0.04 of the run.
    tabletFractionSlack: 0.8,
    maxOpenExpeditionsMs: 30 * 60_000, // abandon after 30 min
  },

  ledger: {
    attempts: 6,
    epochUtc: Date.UTC(2026, 0, 1),
  },

  mini: {
    rewardedRoundsPerDay: num('MINI_REWARDED_ROUNDS_PER_DAY', 10),
    maxXpPerRound: 200,
    // A round must be opened by the server and cannot be claimed sooner than
    // this. These are floors a human cannot beat, not targets: Pillar Sort and
    // Design or Myth are 60-second games, Chain Builder is untimed but needs
    // real dragging, and a Coin Quest level takes far longer than 15 s.
    minDurationMs: {
      pillar_sort: 25_000,
      design_or_myth: 25_000,
      chain_builder: 10_000,
      coin_quest: 15_000,
      // A full passage is about 70 s, but the shortest legitimate run is a
      // player who taps once and then never again: the coin sinks, takes its
      // three strikes at 1.1 s of grace each, glides down and rolls to a
      // stop. That measures at about 5.3 s (see `passage_test.dart`, which
      // asserts it stays above 4.5 s), and it is a real run that earns a
      // real star, so the floor has to sit under it rather than under the
      // full passage.
      passage: 4_000,
    } as Record<string, number>,
    // A round left open longer than this can no longer be claimed.
    maxDurationMs: 60 * 60_000,
    // Upper bound on what a single round can legitimately report, per game.
    maxRight: { pillar_sort: 24, design_or_myth: 16, chain_builder: 3, coin_quest: 3, passage: 3 } as Record<
      string,
      number
    >,
    // Upper bound on the optional per-round `score`, per game. A game not
    // listed here has no score and anything it sends is clamped to zero.
    // Passage: 36 gold at 10, 35 trails of two silver at 3 and two copper
    // at 1, and a ×3 momentum multiplier on the best of them — a perfect run
    // is under two thousand.
    maxScore: { passage: 1999 } as Record<string, number>,
    // What a score is worth. Divided into the (capped) score and capped
    // again, so the bonus is a nudge on top of the star formula, never the
    // main event: the star formula is what the design pays for.
    scoreXp: { passage: { perPoints: 50, cap: 12 } } as Record<string, { perPoints: number; cap: number }>,
  },

  // When Pigs Fly (game id `passage`): the boar grows across runs from the
  // points a player has ever scored in it. Only rewarded rounds count, so
  // the daily cap above bounds growth the same way it bounds XP.
  //
  // The thresholds are provisional, set from a guess at casual play — about
  // four runs a day at about 150 points. First pass was a week to the
  // juvenile and a month to the razorback; lowered the same day (owner's
  // call) to two or three days and about ten. They are meant to be reset
  // from measured scores once real runs are on the server, which is why
  // both can be overridden without a deploy.
  passage: {
    stages: [
      { id: 'piglet', at: 0 },
      { id: 'juvenile', at: num('PASSAGE_JUVENILE_AT', 1_500) },
      { id: 'razorback', at: num('PASSAGE_RAZORBACK_AT', 6_000) },
    ] as Array<{ id: string; at: number }>,
  },

  rateLimit: {
    perMinute: num('RATE_PER_MINUTE', 120),
    // Anonymous player creation from one address, per hour. Registration is
    // unauthenticated and every identity can climb the board, so it needs a
    // cap far below the generic per-minute limit (audit R3). Ten covers a
    // household or a lab bench; a farm hits it in seconds.
    playersPerHour: num('PLAYERS_PER_HOUR', 10),
  },
};

export type Config = typeof config;

export const DEV_SECRET = 'dev-only-secret-change-me';

/**
 * Refuses to start a production process on the development secret.
 *
 * That secret signs the single-use tablet tokens. On the default — which is in
 * the repository — anyone can forge a signature and claim XP for questions they
 * were never asked, which defeats the entire point of the server being the
 * authority. A warning is not enough here: warnings get deployed past.
 */
export function assertProductionConfig(): void {
  const fatal: string[] = [];

  // The dev secret is in this repository, so anyone holding a copy can mint
  // tablet tokens. That is fatal wherever it happens, not only when NODE_ENV
  // says "production" — a systemd unit, a bare `npm start` or a PaaS that
  // doesn't inject NODE_ENV would all have sailed past the old check. Local
  // development opts out explicitly instead.
  if (config.secret === DEV_SECRET && process.env.ARCADE_ALLOW_DEV_SECRET !== '1') {
    fatal.push(
      'ARCADE_SECRET is the development default, which is published in this repo.\n' +
        '    Set a real one, or set ARCADE_ALLOW_DEV_SECRET=1 for local development.',
    );
  }
  if (config.secret !== DEV_SECRET && config.secret.length < 32) {
    fatal.push('ARCADE_SECRET is shorter than 32 characters');
  }
  // These only matter once the process is actually serving the public.
  if (config.production && config.corsOrigins.includes('*')) {
    fatal.push('ARCADE_CORS is "*" — name the origins that may call this');
  }
  if (config.production && !config.trustProxy) {
    // Not fatal, but worth saying out loud: without a trusted proxy the rate
    // limiter keys on the socket address, which is right for a direct bind and
    // wrong behind a load balancer (every client looks like the balancer).
    console.warn('ARCADE_TRUST_PROXY is not set — rate limiting will key on the socket address.');
  }

  if (fatal.length) {
    throw new Error(
      `Refusing to start:\n  - ${fatal.join('\n  - ')}\n` +
        'Generate a secret with:  node -e "console.log(crypto.randomUUID()+crypto.randomUUID())"',
    );
  }
}
