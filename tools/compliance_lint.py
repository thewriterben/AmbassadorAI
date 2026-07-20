#!/usr/bin/env python3
"""
compliance_lint.py - deterministic DGD communications-discipline linter.

Mechanical pre-filter for Stage 7. Scans any text surface (script, caption, hook,
title, on-screen text, hashtags) for framing banned by the Foundation's
communications discipline, and reports each hit with the rule it breaks and a
compliant rewrite. Fail-closed: any FAIL hit exits 2.

Source of truth for the rules:
  LLMWiki/compliance/do-and-dont-language.md   (phrase cheat-sheet)
  LLMWiki/compliance/communications-discipline.md
  skills/dgd-video-studio/reference/compliance-gate.md  (Section A)

Severities
  FAIL  banned investment / price / return / solicitation / "safe"-drift framing
  WARN  needs a human look: degen-contrast lingo, bare dollar figures, soft hype
        words ("early/cheap/deal"), or a missing "not financial advice" line

Usage
  python3 compliance_lint.py script.md            # lint a file
  python3 compliance_lint.py --text "Buy now!"     # lint a string
  cat caption.txt | python3 compliance_lint.py -   # lint stdin
  python3 compliance_lint.py script.md --json      # machine-readable
  python3 compliance_lint.py script.md --strict    # treat WARN as failure too

Exit codes: 0 clean · 1 warnings only · 2 one or more FAILs (or --strict warns)
"""
import argparse
import json
import re
import sys

# (category, severity, pattern, fix) — patterns are matched case-insensitively.
RULES = [
    # ---- FAIL: investment framing -------------------------------------------
    ("investment", "FAIL", r"\binvest(?:ment|ing|or|ors)?\b",
     "Describe DGD as 'a monetary system designed to work like sound money,' not an investment."),
    ("investment", "FAIL", r"\b(?:asset to hold|store of value)\b",
     "Frame as a 'digital commodity / monetary design,' not a thing to hold for value."),
    ("investment", "FAIL", r"\bstore (?:your )?(?:wealth|money|value)\b",
     "Don't position DGD as where to store wealth; describe the mechanism instead."),
    ("investment", "FAIL", r"\bhold (?:it )?(?:for )?(?:the )?long[- ]?term\b",
     "Avoid hold-for-gain framing; explain how the design works."),
    ("investment", "FAIL", r"\bportfolio\b",
     "Drop portfolio framing; DGD content is educational, not allocation advice."),
    # ---- FAIL: price prediction ---------------------------------------------
    ("price_prediction", "FAIL", r"\bto the moon\b|\bmoon(?:ing|shot)?\b",
     "Replace with: 'price advances along a fixed curve as the network grows.'"),
    ("price_prediction", "FAIL", r"\bpump(?:ing|s)?\b",
     "No pump language; describe the distribution mechanism."),
    ("price_prediction", "FAIL",
     r"(?<![\d,.])\d+(?:\.\d+)?x\b(?!\s*(?:speed|faster|slower|zoom|resolution))",
     "No multiplier claims (2x, 5x, 100x). The curve is a mechanism, not a forecast."),
    ("price_prediction", "FAIL", r"\b(?:double|triple|quadruple)\s+(?:your|their|his|her)\s+money\b",
     "No multiplier claims. Describe the mechanism, never an outcome."),
    ("price_prediction", "FAIL", r"\bprice target\b|\bnext (?:bitcoin|ethereum|gem)\b",
     "No targets or 'next X' framing; explain how the design differs."),
    # Economy-scale sums (billions/trillions) are factual macro figures, not coin
    # price targets - "from $3 billion to $21 trillion" must not read as a forecast.
    ("price_prediction", "FAIL",
     r"\bto \$\s?\d(?![\d,.]*\s*(?:billion|trillion|bn|tn)\b)",
     "A '$X' price target (incl. on thumbnails) is a forecast — remove it."),
    ("price_prediction", "FAIL", r"\bundervalued\b",
     "Avoid valuation-as-bargain framing; cite the WP valuation method instead."),
    # ---- FAIL: return / profit promise --------------------------------------
    ("return_promise", "FAIL",
     r"\breturns?\b(?!\s+to\s+(?:the\s+)?(?:treasury|foundation))|\bROI\b|\bprofit(?:s|able)?\b|\bgains?\b",
     "No returns/profit/gains. 'No one earns income from operating the network — fees are burned by design.'"),
    ("return_promise", "FAIL", r"\bpassive income\b|\bmake money\b|\bmade \$?\d",
     "No income claims; explain validation/mechanics, not earnings."),
    ("return_promise", "FAIL", r"\bfinancial freedom\b|\bretire\b",
     "Replace with 'a design aimed at preserving purchasing power.'"),
    ("return_promise", "FAIL", r"\bguaranteed\b|\brisk[- ]?free\b",
     "Nothing is guaranteed; it's a reasoned design and the WP says so."),
    ("investment", "FAIL",
     r"\bhedge\s+(?:against|for)\b|\binflation\s+hedge\b",
     "'Hedge against inflation' is investment framing. Describe the supply mechanism instead."),
    ("investment", "FAIL",
     r"\btreat\s+it\s+like\s+an?\s+experiment\b|\bresearch[- ]first\s+approach\b"
     r"|\bstart\s+small\b|\bdip\s+a\s+toe\b|\btest\s+the\s+waters\b",
     "A soft suggestion to acquire is still a solicitation. Point to the white paper instead."),
    ("solicitation", "FAIL",
     r"\b(?:check|see|link|links)\s+(?:in\s+)?(?:the\s+)?(?:description|bio)\b"
     r"(?!\s*(?:for\s+)?(?:the\s+)?(?:white\s*paper|official))",
     "Only ever point to the white paper / official channels, and say so explicitly."),
    # ---- FAIL: solicitation -------------------------------------------------
    ("solicitation", "FAIL",
     r"\bbuy\s+(?:dgd|digital gold|\$?\d|it|in|now|the dip|some|more|coins?|tokens?|crypto|here|today|the bag)\b",
     "Don't solicit buying DGD. 'Read the white paper / official channels in bio to learn more.'"),
    ("solicitation", "FAIL", r"\b(?:where|how)\s+to\s+(?:buy|get|acquire|purchase)\b|\bgo\s+buy\b|\blink\s+to\s+buy\b",
     "Don't point people to buy. Point to the white paper / official channels instead."),
    ("solicitation", "FAIL",
     r"\b(?:purchase|acquire|grab|snag|claim)\s+(?:dgd|digital gold|some|your|the)\b"
     r"|\b(?:purchase|acquire)\s+\w+\s+(?:today|now)\b",
     "Don't solicit acquisition. Point to the white paper instead."),
    ("solicitation", "FAIL",
     r"\bDM\s+me\b|\bmessage\s+me\s+(?:to|for|and)\b|\blink\s+in\s+bio\s+to\s+(?:buy|get|join|start)\b"
     r"|\bsign\s+up\s+(?:with|under)\s+me\b",
     "No direct-response solicitation. Educational content points to public sources, not to you."),
    ("solicitation", "WARN", r"\bbuy(?:ing|s)?\b",
     "'buy' as a plain verb (e.g. 'money buys less') is fine; confirm it isn't soliciting acquisition of DGD."),
    ("solicitation", "FAIL", r"\bget in\b|\bdon'?t miss out\b|\blast chance\b|\bFOMO\b",
     "No urgency/solicitation; 'if the idea interests you, the white paper explains it.'"),
    ("solicitation", "FAIL", r"\bape in\b|\bload up\b|\bsecure your bag\b|\bget rich\b",
     "No acquisition hype; keep it educational."),
    # ---- FAIL: the "safe" drift (note: "safe harbor" is allowed) ------------
    ("safe_drift", "FAIL", r"\bsafe (?:investment|haven|bet|place)\b",
     "'Safe harbor' is a LEGAL term (digital commodity, not a security) — never a safe-money claim."),
    ("safe_drift", "FAIL", r"\bcan'?t lose\b",
     "Safe harbor is about regulation, not your wallet."),
    ("safe_drift", "FAIL", r"\bregulators? approved\b",
     "It's 'designed to align' with the framework — a reasoned position, not an approval (WP §12.16)."),
    # ---- FAIL: MLM / recruiting framing -------------------------------------
    # The live model is pay-in (USDC/USDT) -> receive coins on each release, and
    # referrals are single-level with a one-time bonus. That combination makes
    # network-marketing language both INACCURATE and legally dangerous: it invites
    # exactly the reading the Foundation's structure is built to avoid.
    ("mlm_framing", "FAIL",
     r"\bdown[- ]?line\b|\bup[- ]?line\b|\b(?:forced|binary|\dx\d)\s+matrix\b|\bmatrix\s+(?:plan|comp|compensation|position|spillover)\b",
     "There are no downlines. Inviting is single-level with a one-time bonus (WP §10.1)."),
    ("mlm_framing", "FAIL", r"\bmulti[- ]?level\b|\bMLM\b|\bnetwork marketing\b",
     "DGD is not multi-level. Say: 'inviting is single-level and doesn't change what anyone earns.'"),
    ("mlm_framing", "FAIL", r"\b(?:build|grow|your)\s+(?:your\s+)?team\b|\bget people under you\b",
     "Recruiting-for-income framing. The referral bonus never changes release amounts."),
    ("mlm_framing", "FAIL",
     r"\bresidual income\b|\b(?:generation|team|group|level)\s+(?:override|bonus|commission)s?\b"
     r"|\bcommissions?\s+(?:on|from)\s+(?:your|their|the)\s+(?:team|network|referrals?|downline)\b",
     "No residuals, overrides or commissions exist in the model."),
    ("mlm_framing", "FAIL", r"\b(?:tier|rank|level)\s+(?:up|bonus|system)\b|\bhigher tier\b",
     "There are no tiers, ranks or levels — the distribution curve is continuous (WP §5.1)."),
    ("mlm_framing", "FAIL",
     r"\bearn\b[^.]{0,40}\b(?:per|every|each)\s+(?:signup|sign-up|referral|person|recruit)\b",
     "Per-recruit earnings framing. Releases go to funded accounts equally, not per referral."),
    # ---- FAIL: misstating who receives a release ----------------------------
    # Negation-aware: "they DON'T get shared out to everyone" is the correct
    # statement of the model and must not be blocked by the rule protecting it.
    ("distribution_error", "FAIL",
     r"\b(?:split|shared?|divided|allocated|distributed)\b"
     r"[^.]{0,40}\b(?:among|across|between|to)\s+(?:all\s+(?:current\s+)?)?"
     r"(?:everyone|everybody|all\s+(?:users|accounts|members|holders|participants)"
     r"|users|members|holders|participants)\b",
     "Releases go to accounts with an ACTIVE VALIDATION BALANCE, not to all users/everyone."),
    ("distribution_error", "FAIL",
     r"\b(?:everyone|all users|all accounts)\s+(?:gets?|receives?|earns?)\b[^.]{0,25}\brelease",
     "Unfunded accounts receive nothing. Unclaimed shares return to treasury, not to others."),
    # Negation-aware: "a bigger balance DOESN'T get you a bigger share" is the
    # correct teaching sentence and must not be flagged as the error it corrects.
    ("distribution_error", "FAIL",
     r"\bbigger\s+(?:balance|wallet|stake)\b"
     r"(?![^.]{0,40}\b(?:doesn'?t|does not|don'?t|won'?t|will not|never|isn'?t|is not|no|not)\b)"
     r"[^.]{0,30}\b(?:more|bigger|larger)\b",
     "A bigger balance lasts LONGER; it never earns a larger share of a release."),
    # ---- WARN: review needed ------------------------------------------------
    ("mlm_framing", "WARN", r"\brefer(?:ral|ring)?\b|\binvite\b",
     "Referral mention — confirm you say it's single-level, one-time, and doesn't change release amounts."),
    ("degen_contrast", "WARN", r"\brekt\b|\bcasino\b|\bdegen\b|\bgambl(?:e|ing)\b",
     "Degen lingo may HOOK/contrast, but must sell no play. Confirm it's contrast, not a pitch."),
    ("soft_hype", "WARN", r"\bearly\b|\bcheap\b|\bdeal\b|\bget rich quick\b",
     "Soft hype word — ensure it isn't implying the viewer profits."),
    ("dollar_figure", "WARN", r"\$\s?\d[\d,]*\s?[kKmMbB]?\b",
     "Dollar figure — make sure it's a fact/illustration, not a price target or earnings claim."),
]

COMPILED = [(c, sev, re.compile(p, re.IGNORECASE), fix) for c, sev, p, fix in RULES]
DISCLOSURE_RE = re.compile(r"not financial advice", re.IGNORECASE)


# --------------------------------------------------------- doc context ------
# The wiki's own rules pages QUOTE banned language in order to ban it, so the
# linter fails them - 9 of 11 compliance/craft pages. That noise trains reviewers
# to ignore FAIL output, which is how real defects have slipped through.
#
# These patterns identify a line as INSTRUCTION ABOUT the rules rather than a
# breach of them. They are deliberately narrow, and they are only consulted when
# doc_context=True - which is NEVER the default, and never used when linting a
# script, caption or any other publishable surface. A false negative here would
# be far worse than the noise it removes, so the bar is:
#
#   the negation must attach to a SPEECH VERB ("never SAY x", "don't WRITE x").
#   A bare negation is not enough - "Don't miss out, buy DGD now" contains
#   "Don't" and is a violation, not a lesson.
INSTRUCTIONAL = [
    r"[❌✅🚫⛔]",                                    # do/don't markers
    r"^\s*>",                                        # blockquote - quoting a rule
    r"^\s*#{1,6}\s",                                 # heading, e.g. "### Never call it an investment"
    r"\b(?:never|not?|don'?t|do not|avoid|stop|refuse)\s+"
    r"(?:\w+\s+){0,3}?"
    r"(?:say|saying|said|write|writing|use|using|call|calling|claim|claiming|"
    r"promise|promising|imply|implying|frame|framing|characteri[sz]e|project|"
    r"market|marketing|pitch|pitching|sell|selling|position|positioning|"
    r"advertise|promote|promoting|"
    r"tip into|pivot to|post|posting|describe|describing)\b",
    r"\b(?:instead of|rather than|replace\b.{0,40}\bwith)\b",
    r"\b(?:banned|prohibited|forbidden|off[- ]limits|violat\w+|non-?compliant)\b",
    r"\bwords? to avoid\b|\bdo\s*/\s*don'?t\b|\bnever\b.{0,20}\b(?:list|words)\b",
    r"\bno\s+[\"“‘']",                     # No "to the moon", No "returns"
    r"\bcompliance[- ]safe\b|\bslang for\b",         # meta / definitional
]
INSTRUCTIONAL_RE = [re.compile(p, re.IGNORECASE) for p in INSTRUCTIONAL]

# A do/don't table declares itself in its HEADER row. Script tables
# ("| Time | Spoken | On-screen text | Visual |") do not match this, so their
# rows keep the full strict treatment.
# A heading that declares the section enumerates banned language.
BAN_HEADING_RE = re.compile(
    r"\b(?:words?\s+to\s+avoid|banned|never\s+use|forbidden|avoid\s+entirely|"
    r"don'?t\s+say|red\s+flags?)\b", re.IGNORECASE)

DONT_TABLE_HEADER_RE = re.compile(
    r"^\s*\|.*(?:[❌✅]|\bdon'?t say\b|\bsay instead\b|\bavoid\b|\binstead\b|"
    r"\bbanned\b|\brewrite\b|\bnever say\b).*\|", re.IGNORECASE)


_EMPHASIS_RE = re.compile(r"[*_`~]+")


def is_instructional(line):
    """True if the line teaches the rule rather than breaking it.

    Markdown emphasis is stripped first: "Do **not** market DGD as a degen play"
    would otherwise fail to match "not market", because the asterisks sit between
    the negation and the verb. That gap made the whole check unreliable on the
    wiki's own prose, which is heavily emphasised.
    """
    return any(rx.search(line) or rx.search(_EMPHASIS_RE.sub("", line))
               for rx in INSTRUCTIONAL_RE)


# Categories where stating the NEGATIVE is the correct, expected phrasing:
#   "they DON'T get shared out to everyone"   (the corrected model)
#   "not a GUARANTEED safe harbor"            (the correct caveat)
# Scoped deliberately. Solicitation and price_prediction are NOT here, so
# "This isn't a scam, buy DGD now" still fails on the second clause.
NEGATION_SENSITIVE = {"distribution_error"}
NEGATION_SENSITIVE_TERMS = {"guaranteed"}
NEG_CUE_RE = re.compile(
    r"\b(?:not|never|no|nothing|isn'?t|aren'?t|doesn'?t|don'?t|won'?t|cannot|can'?t)\b"
    r"[^.;:!?]{0,30}$", re.IGNORECASE)


def _negated(line, start, cat, term):
    """Is this match governed by a negation earlier in the same clause?"""
    if cat not in NEGATION_SENSITIVE and term.lower() not in NEGATION_SENSITIVE_TERMS:
        return False
    return bool(NEG_CUE_RE.search(line[:start]))


def lint_text(text, want_disclosure=False, doc_context=False):
    """Return {'findings': [...], 'verdict': 'pass'|'warn'|'fail', 'suppressed': N}.

    doc_context=True downgrades findings on instructional lines to INFO. Use it
    ONLY when linting the wiki's own rules documentation. Never for scripts,
    captions, hooks, titles, hashtags or anything that ships.
    """
    findings, suppressed = [], 0
    in_dont_table = False
    under_ban_heading = False
    for ln_no, line in enumerate(text.splitlines(), start=1):
        # A do/don't table's ROWS are instruction, but only because its HEADER
        # says so. Script tables are also tables - "| Time | Spoken | ... |" -
        # so a bare "is this a table row?" test would exempt real scripts.
        if doc_context:
            if not line.strip().startswith("|"):
                in_dont_table = False
            elif DONT_TABLE_HEADER_RE.search(line):
                in_dont_table = True
            # A bare list of banned words sits under a heading that says so.
            if line.strip().startswith("#"):
                under_ban_heading = bool(BAN_HEADING_RE.search(line))
            elif not line.strip():
                under_ban_heading = under_ban_heading and True
        teaching = doc_context and (is_instructional(line) or under_ban_heading or
                                    (in_dont_table and line.strip().startswith("|")))
        for cat, sev, rx, fix in COMPILED:
            for m in rx.finditer(line):
                if sev == "FAIL" and _negated(line, m.start(), cat, m.group(0)):
                    suppressed += 1
                    continue
                if teaching and sev == "FAIL":
                    suppressed += 1
                    sev_out = "INFO"
                else:
                    sev_out = sev
                findings.append({
                    "line": ln_no, "col": m.start() + 1, "severity": sev_out,
                    "category": cat, "term": m.group(0),
                    "snippet": line.strip()[:120], "fix": fix,
                })
    if want_disclosure and not DISCLOSURE_RE.search(text):
        findings.append({
            "line": 0, "col": 0, "severity": "WARN", "category": "disclosure",
            "term": "(none)", "snippet": "",
            "fix": "No 'not financial advice' line found — add it (spoken + caption).",
        })
    has_fail = any(f["severity"] == "FAIL" for f in findings)
    has_warn = any(f["severity"] == "WARN" for f in findings)
    verdict = "fail" if has_fail else ("warn" if has_warn else "pass")
    return {"findings": findings, "verdict": verdict, "suppressed": suppressed}


def _report(result, source):
    by_sev = {"FAIL": [], "WARN": []}
    for f in result["findings"]:
        by_sev[f["severity"]].append(f)
    out = [f"compliance-lint: {source}  ->  {result['verdict'].upper()}"]
    for sev in ("FAIL", "WARN"):
        for f in by_sev[sev]:
            loc = f"L{f['line']}:{f['col']}" if f["line"] else "doc"
            out.append(f"  [{sev}] {loc} {f['category']}: '{f['term']}'")
            if f["snippet"]:
                out.append(f"        > {f['snippet']}")
            out.append(f"        fix: {f['fix']}")
    if result["verdict"] == "pass":
        out.append("  clean — no banned framing detected.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="DGD communications-discipline linter")
    ap.add_argument("path", nargs="?", help="file to lint (use '-' for stdin)")
    ap.add_argument("--text", help="lint this literal string")
    ap.add_argument("--require-disclosure", action="store_true",
                    help="WARN if no 'not financial advice' line is present")
    ap.add_argument("--strict", action="store_true", help="treat WARN as failure")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--doc-context", action="store_true",
                    help="linting the RULES DOCUMENTATION, not publishable content: "
                         "downgrade findings on instructional lines ('never say X') to "
                         "INFO. Never use this on a script, caption or hashtag.")
    a = ap.parse_args()

    if a.text is not None:
        text, source = a.text, "<--text>"
    elif a.path in (None, "-"):
        text, source = sys.stdin.read(), "<stdin>"
    else:
        text, source = open(a.path, encoding="utf-8").read(), a.path

    result = lint_text(text, want_disclosure=a.require_disclosure,
                       doc_context=a.doc_context)
    if a.json:
        print(json.dumps({"source": source, **result}, indent=2))
    else:
        print(_report(result, source))

    if result["verdict"] == "fail":
        sys.exit(2)
    if result["verdict"] == "warn":
        sys.exit(2 if a.strict else 1)
    sys.exit(0)


if __name__ == "__main__":
    main()
