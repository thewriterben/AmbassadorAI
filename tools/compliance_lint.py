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
    ("price_prediction", "FAIL", r"\b\d{2,}x\b",
     "No multiplier claims (e.g. 100x). The curve is a mechanism, not a forecast."),
    ("price_prediction", "FAIL", r"\bprice target\b|\bnext (?:bitcoin|ethereum|gem)\b",
     "No targets or 'next X' framing; explain how the design differs."),
    ("price_prediction", "FAIL", r"\bto \$\s?\d",
     "A '$X' price target (incl. on thumbnails) is a forecast — remove it."),
    ("price_prediction", "FAIL", r"\bundervalued\b",
     "Avoid valuation-as-bargain framing; cite the WP valuation method instead."),
    # ---- FAIL: return / profit promise --------------------------------------
    ("return_promise", "FAIL", r"\breturns?\b|\bROI\b|\bprofit(?:s|able)?\b|\bgains?\b",
     "No returns/profit/gains. 'No one earns income from operating the network — fees are burned by design.'"),
    ("return_promise", "FAIL", r"\bpassive income\b|\bmake money\b|\bmade \$?\d",
     "No income claims; explain validation/mechanics, not earnings."),
    ("return_promise", "FAIL", r"\bfinancial freedom\b|\bretire\b",
     "Replace with 'a design aimed at preserving purchasing power.'"),
    ("return_promise", "FAIL", r"\bguaranteed\b|\brisk[- ]?free\b",
     "Nothing is guaranteed; it's a reasoned design and the WP says so."),
    # ---- FAIL: solicitation -------------------------------------------------
    ("solicitation", "FAIL", r"\bbuy(?:ing|s)?\b",
     "Don't solicit buying. 'Read the white paper / official channels in bio to learn more.'"),
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
    # ---- WARN: review needed ------------------------------------------------
    ("degen_contrast", "WARN", r"\brekt\b|\bcasino\b|\bdegen\b|\bgambl(?:e|ing)\b",
     "Degen lingo may HOOK/contrast, but must sell no play. Confirm it's contrast, not a pitch."),
    ("soft_hype", "WARN", r"\bearly\b|\bcheap\b|\bdeal\b|\bget rich quick\b",
     "Soft hype word — ensure it isn't implying the viewer profits."),
    ("dollar_figure", "WARN", r"\$\s?\d[\d,]*\s?[kKmMbB]?\b",
     "Dollar figure — make sure it's a fact/illustration, not a price target or earnings claim."),
]

COMPILED = [(c, sev, re.compile(p, re.IGNORECASE), fix) for c, sev, p, fix in RULES]
DISCLOSURE_RE = re.compile(r"not financial advice", re.IGNORECASE)


def lint_text(text, want_disclosure=False):
    """Return {'findings': [...], 'verdict': 'pass'|'warn'|'fail'}."""
    findings = []
    for ln_no, line in enumerate(text.splitlines(), start=1):
        for cat, sev, rx, fix in COMPILED:
            for m in rx.finditer(line):
                findings.append({
                    "line": ln_no, "col": m.start() + 1, "severity": sev,
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
    return {"findings": findings, "verdict": verdict}


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
    a = ap.parse_args()

    if a.text is not None:
        text, source = a.text, "<--text>"
    elif a.path in (None, "-"):
        text, source = sys.stdin.read(), "<stdin>"
    else:
        text, source = open(a.path, encoding="utf-8").read(), a.path

    result = lint_text(text, want_disclosure=a.require_disclosure)
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
