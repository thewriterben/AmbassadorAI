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
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compliance_lint import lint_text  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", default=os.path.join(HERE, "compliance_cases.json"))
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    data = json.load(open(a.cases, encoding="utf-8"))
    cases = data["cases"]
    passed, failures = 0, []
    for c in cases:
        got = lint_text(c["text"])["verdict"]
        ok = got == c["expect"]
        if ok:
            passed += 1
            if a.verbose:
                print(f"  ok   {c['id']:12s} -> {got}")
        else:
            failures.append((c, got))
            print(f"  MISS {c['id']:12s} expected {c['expect']}, got {got}")
            print(f"       text: {c['text']!r}")

    n = len(cases)
    print(f"\ncompliance evals: {passed}/{n} passed"
          + (f", {len(failures)} MISMATCH" if failures else " — rails holding."))
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
