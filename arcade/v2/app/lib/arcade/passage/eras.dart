/// The nine monetary eras a Passage run flies through.
///
/// Every line here is a dated historical fact with a source attached. None of
/// them says anything about Digital Gold, about gold as an investment, or
/// about what any currency will do next. That is the entire point of the
/// framing settled in `arcade/TEN-GAMES.md` §1: the game teaches monetary
/// history and makes no claim about the product it ships inside.
///
/// Rules for anything added here, which exist so this file can be handed to
/// counsel and read in one sitting:
///
///  * A fact must be checkable against [Era.source]. No "widely regarded",
///    no "many believe".
///  * No comparatives. Not "held its value better than", not "unlike".
///  * No forward-looking language of any kind. Nothing about what happens
///    next, to anything.
///  * No adjectives doing argumentative work. "Prices doubled about every
///    four days" is a fact; "ruinous debasement" is an argument.
///  * No clause that editorialises on the fact it is attached to. The three
///    that were cut in review are recorded below so they do not come back.
///
/// If a line cannot be written inside those rules, it does not go in the game.
///
/// ## Review, 2026-09-20
///
/// The first draft was fact-checked line by line before any of it was drawn.
/// Four things were wrong and are fixed here; they are listed because the
/// same mistakes are easy to reintroduce:
///
///  1. **1971 cited the wrong instrument.** Executive Order 11615 is the
///     90-day wage and price freeze and says nothing about gold. The gold
///     suspension was announced in the address of 15 August 1971 and carried
///     out by direction to the Treasury Secretary. Also softened "ending the
///     Bretton Woods system" to "beginning the collapse of" — convertibility
///     was suspended in 1971, but the system limped through the Smithsonian
///     Agreement and did not fully break down until 1973.
///  2. **1923 cited the wrong date for the conversion rate.** The Rentenmark
///     was introduced on 15 November 1923; the rate was fixed on 20 November.
///     "A trillion" is also written out as a numeral here, because 10^12 is
///     a trillion on the short scale and historically a billion on the long
///     scale, and this app ships in both kinds of country.
///  3. **2009 claimed "the first blockchain".** Haber and Stornetta's 1991
///     hash-linked timestamping is cited in Bitcoin's own whitepaper, so the
///     claim loses to a single search. It now says *decentralized*.
///  4. **Three editorial clauses were cut** — "rather than leaving it to
///     practice" (1816), "moving the country onto gold alone" (1873, which
///     also asserts as settled the exact thing contemporaries fought over)
///     and "rather than decided by a committee" (2009). None was supported
///     by its source, and each was doing argument rather than teaching.
///
/// ## Why 1979 is in the list
///
/// Read as a sequence, the other eight items tell one story: hard money
/// adopted, hard money abandoned, paper money destroys savings, gold seized,
/// the last link to gold cut, and then a fixed issuance schedule arrives.
/// No individual line makes a claim, but the arc is an argument, and it is
/// the argument a compliance reviewer would expect this app to be making.
///
/// The Volcker disinflation is the counterexample, and it is a major monetary
/// event in its own right: it is the case of a central bank deliberately
/// ending a serious inflation. Including it is what makes the set read as
/// history rather than as a thesis with dates attached. It should not be
/// removed for pacing without replacing it with something that does the same
/// work.
library;

class Era {
  /// Shown on the banner as the run enters this era.
  final int year;

  /// Two or three words. Appears on the banner under the year.
  final String name;

  /// One or two sentences, shown on the banner and again on the landing
  /// summary.
  final String fact;

  /// Where the fact comes from, so it can be checked without a web search.
  /// Not shown in-game; it is here for review.
  final String source;

  /// Horizon tint for this era, as a 0xAARRGGBB value. Runs cool-to-warm
  /// across the passage so the player can feel distance travelled without
  /// reading anything.
  final int tint;

  const Era({
    required this.year,
    required this.name,
    required this.fact,
    required this.source,
    required this.tint,
  });
}

const eras = <Era>[
  Era(
    year: 1816,
    name: 'The pound, by weight',
    fact: 'Britain makes gold the sole legal standard for the pound and '
        'reduces silver to token coin. Notes become convertible into gold '
        'again in 1821.',
    source: 'Coin Act 1816 (UK), 56 Geo. 3 c. 68, assented 22 June 1816; '
        'resumption under Peel’s Act 1819',
    tint: 0xFF2A3550,
  ),
  Era(
    year: 1873,
    name: 'Silver steps back',
    fact: 'The United States drops the standard silver dollar from its '
        'authorised coinage, ending the free coinage of silver.',
    source: 'Coinage Act of 1873, ch. 131, 17 Stat. 424, signed '
        '12 February 1873',
    tint: 0xFF2E3A52,
  ),
  Era(
    year: 1913,
    name: 'A central banking system',
    fact: 'The Federal Reserve Act creates twelve regional Reserve Banks '
        'under a federal board, with the power to issue notes.',
    source: 'Federal Reserve Act, Pub. L. 63-43, 38 Stat. 251, signed '
        '23 December 1913',
    tint: 0xFF35384C,
  ),
  Era(
    year: 1923,
    name: 'The papiermark',
    fact: 'German prices double about every four days at the peak. The mark '
        'is replaced at a rate of one new mark to 1,000,000,000,000 old ones.',
    source: 'Statistisches Reichsamt price indices, peak October 1923; '
        'Rentenmark introduced 15 November 1923, conversion rate fixed '
        '20 November 1923',
    tint: 0xFF4A3A44,
  ),
  Era(
    year: 1933,
    name: 'Gold called in',
    fact: 'An executive order requires people in the United States to deliver '
        'most gold coin and bullion to the Federal Reserve or a member bank.',
    source: 'Executive Order 6102, 5 April 1933; exemptions for collectors, '
        'industrial use and holdings under \$100',
    tint: 0xFF553D3C,
  ),
  Era(
    year: 1944,
    name: 'Bretton Woods',
    fact: 'Delegates from 44 nations agree to anchor their currencies to the '
        'dollar, at its existing price of thirty-five dollars an ounce of '
        'gold.',
    source: 'United Nations Monetary and Financial Conference, 1–22 July '
        '1944; \$35 price set earlier by the Gold Reserve Act of 1934',
    tint: 0xFF5A452F,
  ),
  Era(
    year: 1971,
    name: 'The window closes',
    fact: 'The United States suspends conversion of dollars into gold, '
        'beginning the collapse of the Bretton Woods system.',
    source: 'Address to the Nation Outlining a New Economic Policy, '
        '15 August 1971; system fully floating by March 1973',
    tint: 0xFF63492A,
  ),
  Era(
    year: 1979,
    name: 'Rates raised',
    fact: 'The Federal Reserve raises its policy rate above nineteen per '
        'cent. United States inflation falls from about fourteen per cent in '
        '1980 to under four per cent by 1983.',
    source: 'Federal Reserve policy shift of 6 October 1979; effective fed '
        'funds rate peak June 1981; CPI-U annual change 1980 and 1983',
    tint: 0xFF5E4A33,
  ),
  Era(
    year: 2009,
    name: 'Issuance in code',
    fact: 'The first decentralized blockchain records its opening block, with '
        'an issuance schedule fixed in software.',
    source: 'Bitcoin genesis block, timestamped 3 January 2009; earlier '
        'hash-linked timestamping: Haber & Stornetta, 1991',
    tint: 0xFF6E5224,
  ),
];

/// Gates flown in each era. Nine eras at four gates is thirty-six gates,
/// which at the scroll speed in `passage_game.dart` lands a full passage at
/// roughly seventy seconds — long enough to feel like a journey, short enough
/// to retry on a bus.
const gatesPerEra = 4;
