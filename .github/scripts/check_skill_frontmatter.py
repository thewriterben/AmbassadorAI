#!/usr/bin/env python3
"""
Robust SKILL.md frontmatter checker using PyYAML.
Exits non-zero if required keys are missing or malformed.
Usage: python3 .github/scripts/check_skill_frontmatter.py
"""
import sys
import os
import yaml

required = ["name", "description", "version", "tags"]

failures = []

for root, dirs, files in os.walk("skills"):
    for f in files:
        if f.lower() == "skill.md" or f == "SKILL.md":
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as fh:
                text = fh.read()
            # Extract frontmatter block
            if not text.startswith("---"):
                failures.append(f"{path}: missing YAML frontmatter (---) at top")
                continue
            try:
                parts = text.split("---", 2)
                if len(parts) < 3:
                    failures.append(f"{path}: malformed frontmatter")
                    continue
                front_text = parts[1]
                front = yaml.safe_load(front_text) or {}
            except Exception as e:
                failures.append(f"{path}: YAML parse error: {e}")
                continue

            missing = []
            for key in required:
                if key not in front or front[key] is None:
                    missing.append(key)
            # Additional checks
            if "tags" in front and not isinstance(front["tags"], (list, tuple)):
                failures.append(f"{path}: 'tags' should be a YAML list")
                continue

            if missing:
                failures.append(f"{path}: missing fields: {', '.join(missing)}")

if failures:
    print("SKILL.md frontmatter validation failed:\n")
    for line in failures:
        print(" - "+line)
    sys.exit(1)
else:
    print("All SKILL.md frontmatter files contain required fields: %s" % ", ".join(required))
    sys.exit(0)
