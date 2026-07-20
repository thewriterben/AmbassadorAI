#!/usr/bin/env python3
"""
run_compliance_evals.py - prove the compliance linter still holds.

Loads tools/compliance_cases.json (red-team prompts + expected verdicts) and runs
each through compliance_lint.lint_text, checking the linter catches what it must and
does not over-flag safe, on-brand content. Exit 0 only if every case matches.

Run this whenever you change the linter, the wiki rules, or - on Hermes - the model
or after the self-improving Curator touches anything. It is the regression guard on
the rails.

  python3 tools/run_compliance_evals.py
  python3 tools/run_compliance_evals.py --verbose

SINGLE SOURCE OF TRUTH for how a case is evaluated.
`tests/test_core.py` imports run_cases() from here rather than reimplementing it.
It used to have its own copy, and when `doc_context` was added to the case schema
only this file was updated - so the suite failed while the runner passed. Any new
case field must be added to KNOWN_FIELDS below, which makes forgetting it loud
instead of silent.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compliance_lint import lint_text  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CASES_PATH = os.path.join(HERE, "compliance_cases.json")

# Every field a case may carry. Anything else is a typo or a field someone added
# without teaching the runner to honour it - which is the exact failure this
# module now exists to prevent. Fail loudly rather than silently ignoring it.
KNOWN_FIELDS = {"id", "expect", "text", "why", "doc_context"}
REQUIRED_FIELDS = {"id", "expect", "text"}
VALID_VERDICTS = {"pass", "warn", "fail"}


def load_cases(path=CASES_PATH):
    """Load and validate the case file. Raises on a malformed or unknown field."""
    cases = json.load(open(path, encoding="utf-8"))["cases"]
    seen = set()
    for i, c in enumerate(cases):
        cid = c.get("id", f"<index {i}>")
        missing = REQUIRED_FIELDS - set(c)
        if missing:
            raise ValueError(f"case {cid}: missing required field(s) {sorted(missing)}")
        unknown = set(c) - KNOWN_FIELDS
        if unknown:
            raise ValueError(
                f"case {cid}: unknown field(s) {sorted(unknown)}. Add them to "
                f"KNOWN_FIELDS and make run_case() honour them, or the field will "
                f"be silently ignored by every consumer.")
        if c["expect"] not in VALID_VERDICTS:
            raise ValueError(f"case {cid}: expect={c['expect']!r} not in {sorted(VALID_VERDICTS)}")
        if cid in seen:
            raise ValueError(f"duplicate case id: {cid}")
        seen.add(cid)
    return cases


def run_case(case):
    """Evaluate one case. Returns (ok, actual_verdict)."""
    got = lint_text(case["text"], doc_context=case.get("doc_context", False))["verdict"]
    return got == case["expect"], got


def run_cases(cases=None):
    """Run every case. Returns (passed, failures) where failures is [(case, got)]."""
    if cases is None:
        cases = load_cases()
    passed, failures = 0, []
    for c in cases:
        ok, got = run_case(c)
        if ok:
            passed += 1
        else:
            failures.append((c, got))
    return passed, failures


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", default=CASES_PATH)
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    try:
        cases = load_cases(a.cases)
    except ValueError as e:
        print(f"case file invalid: {e}")
        sys.exit(2)

    passed, failures = run_cases(cases)
    if a.verbose:
        failed_ids = {c["id"] for c, _ in failures}
        for c in cases:
            if c["id"] not in failed_ids:
                print(f"  ok   {c['id']:12s} -> {c['expect']}")
    for c, got in failures:
        print(f"  MISS {c['id']:12s} expected {c['expect']}, got {got}")
        print(f"       text: {c['text']!r}")

    n = len(cases)
    print(f"\ncompliance evals: {passed}/{n} passed"
          + (f", {len(failures)} MISMATCH" if failures else " - rails holding."))
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
