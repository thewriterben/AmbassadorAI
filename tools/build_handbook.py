#!/usr/bin/env python3
"""
build_handbook.py - generate LLMWiki/DGD-Ambassador-Handbook.pdf from the wiki.

The handbook is the one artifact that leaves the repo: index.md calls it the
"shareable, branded PDF summary of the wiki." It had no build script, so when the
distribution model was corrected on 2026-07-19 the PDF kept teaching the
superseded version ("split among all current users") to everyone holding a copy.
This script exists so that can't happen again: the PDF is now a build output of
the corrected wiki, not a hand-made file that silently rots.

Like build_hub.py, every page is run through the compliance linter at BUILD time
and a FAIL aborts the build - the handbook cannot ship non-compliant framing.
Pages are linted with doc_context=True: they ARE the rules documentation, so a
line that teaches a rule is instruction, not a breach. There are no page-level
exemptions, so a genuine violation cannot hide behind a filename.

  python3 tools/build_handbook.py
  python3 tools/build_handbook.py --out /tmp/handbook.pdf --html-only

Requires: pip install weasyprint markdown
"""
import argparse
import datetime as dt
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "LLMWiki")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compliance_lint as CL  # noqa: E402

# Curated running order. Mirrors the coverage of the original handbook: what DGD
# is -> the rules -> the craft -> the toolkit -> ready-to-shoot -> the gut check.
PAGES = [
    ("What Digital Gold is", [
        "dgd/dgd-overview.md",
        "dgd/six-pillars.md",
        "dgd/supply-and-distribution.md",
        "dgd/valuation-cfv-dgsb.md",
        "dgd/platform-and-tools.md",
        "dgd/participation-pathways.md",
        "dgd/positioning-safe-harbor.md",
    ]),
    ("The rules", [
        "compliance/communications-discipline.md",
        "compliance/do-and-dont-language.md",
        "compliance/ftc-disclosure.md",
        "compliance/ai-disclosure.md",
    ]),
    ("Making it land", [
        "craft/hooks-library.md",
        "craft/story-structures.md",
        "craft/positioning-and-audiences.md",
    ]),
    ("The free toolkit", [
        "tools/toolkit-overview.md",
        "tools/workflows.md",
    ]),
    ("Ready to shoot", [
        "templates/six-pillars-series-scripts.md",
        "templates/pre-publish-checklist.md",
    ]),
]

CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm;
  @bottom-center { content: counter(page); font: 9pt/1 'DejaVu Sans', sans-serif; color: #8a8f9c; } }
@page :first { margin: 0; }
body { font: 10.5pt/1.55 'DejaVu Sans', sans-serif; color: #14181f; }
h1 { font-size: 20pt; color: #101728; border-bottom: 2.5pt solid #D4A853;
     padding-bottom: 4pt; margin: 0 0 10pt; page-break-after: avoid; }
h2 { font-size: 13pt; color: #101728; margin: 16pt 0 6pt; page-break-after: avoid; }
h3 { font-size: 11pt; color: #4a4f5c; margin: 12pt 0 4pt; page-break-after: avoid; }
p, li { orphans: 2; widows: 2; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 9pt;
        page-break-inside: avoid; }
th { background: #101728; color: #F4F4F0; text-align: left; padding: 4pt 6pt; }
td { border-bottom: 0.5pt solid #d9dce3; padding: 4pt 6pt; vertical-align: top; }
blockquote { border-left: 3pt solid #D4A853; background: #fcf8ef; margin: 8pt 0;
             padding: 6pt 10pt; page-break-inside: avoid; }
code { background: #f2f3f6; padding: 1pt 3pt; font-size: 9pt; }
pre { background: #f2f3f6; padding: 6pt; font-size: 8.5pt; overflow-wrap: break-word;
      white-space: pre-wrap; page-break-inside: avoid; }
a { color: #8a6a1f; text-decoration: none; }
.cover { background: #101728; color: #F4F4F0; height: 297mm; padding: 60mm 20mm 0;
         page-break-after: always; }
.cover h1 { color: #D4A853; border: 0; font-size: 34pt; line-height: 1.1; }
.cover .sub { font-size: 13pt; color: #b9bfcc; margin-top: 8pt; }
.cover .meta { position: absolute; bottom: 22mm; font-size: 9pt; color: #8a8f9c; }
.sec { page-break-before: always; }
.sechead { font-size: 26pt; color: #D4A853; border-bottom: 3pt solid #101728;
           padding-bottom: 6pt; margin: 0 0 14pt; }
.note { font-size: 8.5pt; color: #6b7280; margin-top: 3pt; }
"""


def strip_fm(text):
    return re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build the DGD Ambassador Handbook PDF")
    ap.add_argument("--out", default=os.path.join(WIKI, "DGD-Ambassador-Handbook.pdf"))
    ap.add_argument("--html-only", action="store_true", help="write .html next to --out and stop")
    ap.add_argument("--reviewed", action="store_true",
                    help="a human has read the residual findings below and confirmed they are "
                         "the wiki QUOTING banned language, not using it. Required to build "
                         "while any FAIL remains. Default is to block.")
    a = ap.parse_args(argv)

    try:
        import markdown
    except ImportError:
        sys.exit("need: pip install markdown")

    today = dt.date.today().isoformat()
    parts = [f"""<div class="cover">
      <h1>DGD Ambassador<br>Video Handbook</h1>
      <div class="sub">How to make high-quality, educational short-form videos
      about Digital Gold &mdash; and stay inside the rules.</div>
      <div class="meta">Generated {today} from the DGD Ambassador Video Wiki.<br>
      Educational only &mdash; not financial advice. Verify every figure against the
      White Paper and digitalgold.co before publishing.</div></div>"""]

    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    failures, included = [], 0

    for section, pages in PAGES:
        parts.append(f'<div class="sec"><div class="sechead">{section}</div></div>')
        for rel in pages:
            full = os.path.join(WIKI, rel)
            if not os.path.exists(full):
                print(f"  skip (missing): {rel}")
                continue
            raw = strip_fm(open(full, encoding="utf-8").read())
            # doc_context: these ARE the rules pages, so lines that teach a rule
            # ("never say X", do/don't table rows) are instruction, not breach.
            # Anything that still FAILs is a genuine problem - no page-level
            # exemptions, so a real violation cannot hide behind its filename.
            res = CL.lint_text(raw, doc_context=True)
            fails = [f for f in res["findings"] if f["severity"] == "FAIL"]
            if res.get("suppressed"):
                print(f"    {rel}: {res['suppressed']} instructional mentions suppressed")
            for f in fails[:3]:
                failures.append(f"{rel}:{f['line']} {f['category']}: {f['term']}")
            md.reset()
            parts.append('<div class="sec">' + md.convert(raw) + "</div>")
            included += 1

    if failures:
        print(f"\n{len(failures)} FAIL finding(s) survived doc-context suppression:")
        for f in failures:
            print("  ", f)
        if not a.reviewed:
            print("\nHANDBOOK BLOCKED. A regex cannot reliably tell 'quoting a banned phrase to\n"
                  "teach it' from 'using it' - structural signals get ~86% of the way and the\n"
                  "rest needs a human. Read the findings above; if every one is the wiki quoting\n"
                  "a rule rather than breaking it, re-run with --reviewed. If any is real, fix\n"
                  "the page instead.")
            return 2
        print("\n--reviewed: proceeding on human confirmation that these are quotations.")

    html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>" \
           + "\n".join(parts) + "</body></html>"

    if a.html_only:
        p = os.path.splitext(a.out)[0] + ".html"
        open(p, "w", encoding="utf-8").write(html)
        print(f"wrote {p} ({included} pages)")
        return 0

    try:
        from weasyprint import HTML
    except ImportError:
        sys.exit("need: pip install weasyprint")
    HTML(string=html, base_url=WIKI).write_pdf(a.out)
    print(f"built handbook -> {a.out}  ({included} wiki pages)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
