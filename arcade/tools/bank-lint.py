#!/usr/bin/env python3
"""Lint the Knowledge Tablet question bank.

Runs the repo's communications-discipline linter over every bank file, then
subtracts the reviewed exemptions in ALLOWLIST.md. Tier C items put a
misconception in front of the player in order to mark it false, so the banned
phrase has to appear — see the allow-list for why each one is permitted.

Anything not on the list is reported and fails the run, so a genuinely new
violation cannot hide behind a blanket waiver.

    python arcade/tools/bank-lint.py                  # default paths
    python arcade/tools/bank-lint.py --bank DIR --json
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_BANK = REPO / "arcade" / "server" / "data" / "bank"
DEFAULT_LINTER = REPO / "tools" / "compliance_lint.py"


def load_allowlist(path: Path) -> set[tuple[str, str, str]]:
    """Parses the markdown table into (file, category, term) triples, lowercased."""
    allowed: set[tuple[str, str, str]] = set()
    if not path.exists():
        return allowed
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 6 or cells[1] in ("File", "") or cells[1].startswith("-"):
            continue
        allowed.add((cells[1].lower(), cells[2].lower(), cells[3].lower()))
    return allowed


def is_allowed(allowed: set[tuple[str, str, str]], fname: str, cat: str, term: str) -> bool:
    f, c, t = fname.lower(), (cat or "").lower(), (term or "").lower()
    return any(
        (af in ("*", f)) and (ac in ("*", c)) and (at in ("*", t))
        for af, ac, at in allowed
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="Lint the DGD Arcade question bank")
    ap.add_argument("--bank", type=Path, default=DEFAULT_BANK)
    ap.add_argument("--linter", type=Path, default=DEFAULT_LINTER)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--warn-as-error", action="store_true")
    args = ap.parse_args()

    allowed = load_allowlist(args.bank / "ALLOWLIST.md")
    files = sorted(p for p in args.bank.glob("*.md") if p.name != "ALLOWLIST.md")
    if not files:
        print(f"no bank files in {args.bank}", file=sys.stderr)
        return 2

    report, unreviewed, exempted = [], 0, 0
    for f in files:
        proc = subprocess.run(
            [sys.executable, str(args.linter), "--doc-context", "--json", str(f)],
            capture_output=True, text=True,
        )
        if proc.returncode not in (0, 1) and not proc.stdout.strip():
            print(f"linter failed on {f.name}: {proc.stderr.strip()[:300]}", file=sys.stderr)
            return 2
        data = json.loads(proc.stdout)
        kept = []
        for finding in data.get("findings", []):
            if finding.get("severity") == "INFO":
                continue
            if is_allowed(allowed, f.name, finding.get("category", ""), finding.get("term", "")):
                exempted += 1
                continue
            kept.append(finding)
        fails = [x for x in kept if x["severity"] == "FAIL"]
        warns = [x for x in kept if x["severity"] == "WARN"]
        unreviewed += len(fails) + (len(warns) if args.warn_as_error else 0)
        report.append({"file": f.name, "fail": fails, "warn": warns})

    if args.json:
        print(json.dumps({"unreviewed": unreviewed, "exempted": exempted, "files": report}, indent=1))
        return 1 if unreviewed else 0

    for entry in report:
        rows = entry["fail"] + entry["warn"]
        status = "FAIL" if entry["fail"] else ("warn" if entry["warn"] else "clean")
        print(f"{entry['file']:<34} {status}")
        for x in rows:
            print(f"   [{x['severity']}] L{x['line']} {x['category']}: '{x['term']}'")
            print(f"        fix: {x['fix']}")
    print(f"\n{exempted} reviewed exemption(s) applied · {unreviewed} unreviewed finding(s)")
    return 1 if unreviewed else 0


if __name__ == "__main__":
    raise SystemExit(main())
