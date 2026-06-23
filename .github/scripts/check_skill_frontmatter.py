#!/usr/bin/env python3
"""
Simple frontmatter checker for SKILL.md files. Exits non-zero if required fields are missing.
Usage: python3 .github/scripts/check_skill_frontmatter.py
"""
import sys
import re
import os

required = ["name", "description", "version", "tags"]

failures = []

for root, dirs, files in os.walk("skills"):
    for f in files:
        if f.lower() == "skill.md" or f == "SKILL.md":
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as fh:
                text = fh.read()
            m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
            if not m:
                failures.append(f"{path}: missing YAML frontmatter (---) at top")
                continue
            front = m.group(1)
            missing = []
            for key in required:
                if re.search(r"^\s*%s\s*:\s*" % re.escape(key), front, re.M) is None:
                    missing.append(key)
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
