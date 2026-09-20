/// Mini-game content. Every line traces to LLMWiki/dgd/* (WP section cited).
/// No price content, no "earn" language.
library;

// ---------------------------------------------------------------- Pillar Sort

const pillars = [
  'Scarcity',
  'Stable Pricing',
  'Free Adoption',
  'Decentralized Governance',
  'Freedom to Transact',
  'Adequate Circulation',
];

class PillarStatement {
  final String text;
  final int pillar; // index into [pillars]
  const PillarStatement(this.text, this.pillar);
}

const pillarStatements = <PillarStatement>[
  // Scarcity — WP §2.2, §5
  PillarStatement('Supply is capped at 21,000,000 coins', 0),
  PillarStatement('Fees and staking rewards are burned, so supply can only shrink', 0),
  PillarStatement('Supply is limited by transparent, predictable rules', 0),
  PillarStatement('2,000,000 coins are permanently locked for staking', 0),
  // Stable Pricing — WP §3, §4, §8, §11
  PillarStatement('One published price replaces bid/ask trading', 1),
  PillarStatement('Price comes from the CFV calculation, not an order book', 1),
  PillarStatement('The DGSB is a frozen benchmark, like the meter', 1),
  PillarStatement('After distribution, price is recalculated monthly from DGD\'s own metrics', 1),
  // Free Adoption — WP §2.2
  PillarStatement('Money must be chosen, not imposed by decree', 2),
  PillarStatement('Participation is voluntary', 2),
  PillarStatement('"Let the best money win" — Hayek', 2),
  PillarStatement('Nobody is required to accept it', 2),
  // Decentralized Governance — WP §12.14–12.15
  PillarStatement('Rules were fixed at inception — there is nothing to vote on', 3),
  PillarStatement('The Foundation cannot change the supply cap', 3),
  PillarStatement('"Rules rather than discretion"', 3),
  PillarStatement('Every running QT wallet is a full node', 3),
  // Freedom to Transact — WP §2.2
  PillarStatement('Tor V3 onion addressing is built in', 4),
  PillarStatement('Transactions need no permission from an intermediary', 4),
  PillarStatement('Coins live in a self-custody QT wallet', 4),
  PillarStatement('Encrypted, anonymous transactions', 4),
  // Adequate Circulation — WP Abstract, §9, §10
  PillarStatement('A coin becomes money when it flows link by link through the supply chain', 5),
  PillarStatement('A merchant can hold DGD and pay suppliers in it', 5),
  PillarStatement('Converted to dollars after one payment, it was only a payment instrument', 5),
  PillarStatement('Circulation reaches all the way back to the raw-material owner', 5),
];

// ---------------------------------------------------------------- Design or Myth?

class MythCard {
  final String text;
  final bool design; // true = how DGD is designed; false = myth
  final String why;
  final String source;
  const MythCard(this.text, this.design, this.why, this.source);
}

const mythCards = <MythCard>[
  MythCard('Unclaimed coins are redistributed to everyone else', false,
      'Unclaimed coins stay in or return to the treasury. Your share does not grow.', 'WP §5.6'),
  MythCard('A bigger validation balance gets a bigger share of each release', false,
      'Same amount per funded account; a larger balance just lasts longer.', 'WP §5.6'),
  MythCard('The CFV framework guarantees the price will rise', false,
      'If metrics deteriorate, the Fair Coin Price falls.', 'WP §11.2'),
  MythCard('Stable Pricing means the price can never go down', false,
      'The framework explicitly does not guarantee appreciation.', 'WP §11.2'),
  MythCard('DGD has three referral levels', false,
      'One level, one-time bonus. No cascade.', 'WP §10.1'),
  MythCard('Referrals increase how much you receive from releases', false,
      'Referral recognition is separate from releases.', 'participation-pathways.md'),
  MythCard('There are ten distribution tiers', false, 'The curve is continuous — no tiers.', 'WP §5.1'),
  MythCard('The QT wallet runs on iOS and Android', false,
      'Desktop only: Windows, macOS, Linux.', 'platform-and-tools.md'),
  MythCard('The Marketplace & Escrow is live today', false,
      'Planned, not live. Say "coming", never "available".', 'platform-and-tools.md'),
  MythCard('Transaction fees are paid to validators', false, 'Fees are burned.', 'WP §5'),
  MythCard('Token holders vote monthly on the rules', false,
      'Rules were fixed at inception; there is nothing to govern.', 'WP §12.14'),
  MythCard('"Safe harbor" means the regulator approved DGD', false,
      'It is a reasoned design position, not an approval.', 'WP §12.16'),
  MythCard('The US money supply grew 7,000 percent since 1913', false,
      'It grew roughly 7,000-fold (~700,000%). The wiki flags the percent version as a misstatement.',
      'six-pillars.md'),
  MythCard('Released coins land in your web account balance', false,
      'Web account = validation interface; coins land in the QT wallet.', 'WP §5.6'),
  MythCard('Fees and staking rewards are burned', true, 'Supply can only decrease.', 'WP §5'),
  MythCard('Each release goes equally to every funded account', true,
      'Same amount per funded account.', 'WP §5.6'),
  MythCard('The distribution curve is continuous', true, 'No discrete levels or tiers.', 'WP §5.1'),
  MythCard('Per-account releases shrink toward zero as the network grows', true,
      'Near N=1,000 ≈ 88.69 coins; near the end ≈ 0.05.', 'WP §5'),
  MythCard('Distribution ends permanently at 80,000,000 accounts', true,
      '19M coins circulating at that point.', 'WP §5'),
  MythCard('Coins land in a self-custody QT wallet', true, 'Wallet = custody.', 'WP §5.6'),
  MythCard('The DGSB froze when Bitcoin first touched \$100,000', true,
      'December 2024; market cap ≈ \$1.983T at that moment.', 'WP §3.2'),
  MythCard('Adoption carries 70% of the CFV weight', true, 'The other three metrics are 10% each.', 'WP §4'),
  MythCard('There is exactly one referral level', true, 'Single-level, one-time.', 'WP §10.1'),
  MythCard('Every running QT wallet is also a full node', true, 'It supports the network.', 'platform-and-tools.md'),
  MythCard('21,000,000 cap; 19,000,000 can ever circulate', true, '2M is locked for staking.', 'WP §5'),
  MythCard('Tor V3 onion addressing is integrated natively', true,
      'Encrypted, anonymous transactions without an intermediary.', 'WP §2.2'),
];

// ---------------------------------------------------------------- Chain Builder

class Chain {
  final String title;
  final List<String> steps; // correct order
  final String source;
  const Chain(this.title, this.steps, this.source);
}

const chains = <Chain>[
  Chain('The lumber chain — money that circulates', [
    'A customer pays the furniture store in DGD',
    'The store pays the furniture maker',
    'The furniture maker pays the lumber mill',
    'The mill pays the logging company',
    'The logging company pays the forest owner — raw material',
  ], 'WP §10'),
  Chain('From account to coins', [
    'An account is created on the platform',
    'The account is validated and funded',
    'N advances one step along the curve',
    'A release goes equally to every funded account',
    'Coins land in the self-custody QT wallet',
  ], 'WP §5, §5.6'),
  Chain('Setting up custody', [
    'Download the QT wallet (desktop only)',
    'Verify the download hash',
    'Install and sync — it runs as a full node',
    'Back up your keys',
    'Receive releases into the wallet',
  ], 'platform-and-tools.md'),
  Chain('A century of money', [
    '1913 — a new central bank',
    'The dollar loses 96% of its purchasing power',
    '1976 — Hayek: let the best money win',
    '2024 — the DGSB freezes a fixed benchmark',
    'A 21,000,000-coin network',
  ], 'WP Abstract, §3'),
];
