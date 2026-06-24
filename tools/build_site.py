#!/usr/bin/env python3
"""
build_site.py - bake the deployable static control-panel site from the Python canon.

Single source of truth: the client-side linter rules are exported straight from
compliance_lint.RULES, the performance data from the ledger, and the asset gallery
from the asset folder. Output is a self-contained static site/ you can host anywhere
(GitHub Pages, Netlify, any static host) — no backend.

  python3 tools/build_site.py                       # -> site/  (default)
  python3 tools/build_site.py --out docs            # GitHub Pages /docs folder
  python3 tools/build_site.py --no-ledger           # omit performance data (privacy)
  python3 tools/build_site.py --assets-dir example-output/asset-pack

What ships in site/:
  index.html      the SPA (Performance / Lint / Publish / Assets)
  assets/*.png    copied asset images for the gallery
"""
import argparse
import datetime as dt
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import compliance_lint as CL  # noqa: E402
import dgd_performance as PERF  # noqa: E402

PUBLISH_PLATFORMS = {
    "x": {"ident": "twitter", "maxTags": 3, "budget": 280},
    "tiktok": {"ident": "tiktok", "maxTags": 5, "budget": 2200},
    "instagram": {"ident": "instagram", "maxTags": 5, "budget": 2200},
    "youtube": {"ident": "youtube", "maxTags": 5, "budget": 5000},
}


def ledger_data(ledger_path):
    rows = []
    if ledger_path and os.path.exists(ledger_path):
        rows = [json.loads(l) for l in open(ledger_path, encoding="utf-8") if l.strip()]
    if not rows:
        return None
    by = {k: PERF._rank(rows, k) for k in ("hook", "topic", "platform")}
    return {
        "totals": {
            "impressions": sum(r.get("impressions", 0) for r in rows),
            "avg_er": sum(PERF.eng_rate(r) for r in rows) / len(rows),
            "fy": sum(PERF.follow_yield(r) for r in rows) / len(rows),
        },
        "by_hook": by["hook"], "by_topic": by["topic"], "by_platform": by["platform"],
        "posts": [{"post_id": r.get("post_id", ""), "platform": r.get("platform", ""),
                   "hook": r.get("hook", ""), "topic": r.get("topic", ""),
                   "impressions": r.get("impressions", 0),
                   "er": round(PERF.eng_rate(r), 4), "fy": round(PERF.follow_yield(r), 1)}
                  for r in rows],
    }


def main():
    ap = argparse.ArgumentParser(description="Build the DGD static control-panel site")
    ap.add_argument("--out", default=os.path.join(ROOT, "site"))
    ap.add_argument("--assets-dir", default=os.path.join(ROOT, "example-output", "asset-pack"))
    ap.add_argument("--ledger", default=PERF.LEDGER, help="ledger.jsonl to embed")
    ap.add_argument("--no-ledger", action="store_true", help="omit performance data (privacy)")
    a = ap.parse_args()

    template = open(os.path.join(HERE, "site_template.html"), encoding="utf-8").read()

    # 1) rules from the Python source (single source of truth)
    rules = [{"category": c, "severity": sev, "pattern": p, "fix": fix}
             for (c, sev, p, fix) in CL.RULES]

    # 2) assets -> copy pngs into site/assets/
    out = a.out
    assets_out = os.path.join(out, "assets")
    os.makedirs(assets_out, exist_ok=True)
    asset_names = []
    if os.path.isdir(a.assets_dir):
        for fn in sorted(os.listdir(a.assets_dir)):
            if fn.lower().endswith(".png") and not fn.startswith("_"):
                shutil.copy(os.path.join(a.assets_dir, fn), os.path.join(assets_out, fn))
                asset_names.append(fn)

    # 3) ledger (optional)
    ledger = None if a.no_ledger else ledger_data(a.ledger)

    data = {
        "built": dt.date.today().isoformat(),
        "rules": rules,
        "allowed": ["not financial advice", "sponsored"],
        "platforms": PUBLISH_PLATFORMS,
        "safeTags": ["soundmoney", "economics", "monetarypolicy",
                     "austrianeconomics", "cryptoeducation", "fintecheducation"],
        "assets": asset_names,
        "ledger": ledger,
    }
    html = template.replace("/*__DATA__*/ null", json.dumps(data, ensure_ascii=False))
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)

    print(f"built static site -> {out}/")
    print(f"  rules: {len(rules)} · assets: {len(asset_names)} · "
          f"ledger: {'omitted' if ledger is None else str(len(ledger['posts']))+' posts'}")
    print(f"  preview locally:  python3 -m http.server -d {out} 8000  ->  http://localhost:8000")


if __name__ == "__main__":
    main()
