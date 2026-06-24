#!/usr/bin/env python3
"""
dgd_performance.py - the performance loop: post metrics -> ledger -> evidence.

Closes Job C's open claim ("diagnose a retention drop-off / fix a weak hook") by
giving it data. It records how each published post performed, keyed to the choices
that produced it (hook type, topic, pillar, platform, format), and turns the ledger
into a compliance-safe report the agent reads to make EVIDENCE-BASED recommendations
instead of guesses.

Where metrics come from:
  * live:  `postiz analytics:post <id>` (when the Postiz CLI + POSTIZ_API_KEY exist)
  * offline: a metrics JSON file (same shape) or explicit --impressions/--likes/... flags

Subcommands
  record   add/update one post in the ledger (flags, --metrics-json, or --from-postiz)
  report   rank hooks / topics / platforms by engagement + follow rate; write markdown
  show     print the ledger as a table

Ledger: LLMWiki/trends/performance/ledger.jsonl  (one JSON object per line)
Reports: LLMWiki/trends/performance/PERF-YYYY-MM-DD.md  (+ index.md)

Engagement rate = (likes+comments+shares+saves) / impressions
Follow yield     = follows per 1,000 impressions

Examples
  python3 tools/dgd_performance.py record --post-id x_001 --platform x \
     --topic inflation --hook "Contrarian Claim" --pillar scarcity \
     --impressions 12000 --likes 540 --comments 60 --shares 90 --follows 110
  python3 tools/dgd_performance.py record --post-id tt_009 --platform tiktok \
     --topic scarcity --hook "List Tease" --from-postiz 7321... --days 14
  python3 tools/dgd_performance.py report
"""
import argparse
import datetime as dt
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PERF_DIR = os.environ.get("DGD_PERF_DIR", os.path.join(ROOT, "LLMWiki", "trends", "performance"))
LEDGER = os.path.join(PERF_DIR, "ledger.jsonl")
METRIC_FIELDS = ["impressions", "likes", "comments", "shares", "saves", "follows"]

# Postiz analytics metric-name -> our field (tolerant, case-insensitive contains)
METRIC_MAP = [
    (("impression", "view", "reach", "play"), "impressions"),
    (("like", "favorite"), "likes"),
    (("comment", "reply"), "comments"),
    (("share", "retweet", "repost"), "shares"),
    (("save", "bookmark"), "saves"),
    (("follow",), "follows"),
]


def _metric_total(entry):
    """Pull a single number from one Postiz metric entry (tolerant of shape)."""
    for k in ("total", "value", "count", "sum"):
        if isinstance(entry.get(k), (int, float)):
            return float(entry[k])
    data = entry.get("data") or entry.get("points") or entry.get("values")
    if isinstance(data, list) and data:
        last = data[-1]
        if isinstance(last, dict):
            for k in ("total", "value", "count", "y"):
                if isinstance(last.get(k), (int, float)):
                    return float(last[k])
        elif isinstance(last, (int, float)):
            return float(last)
    return 0.0


def parse_postiz_metrics(payload):
    """Map a Postiz analytics:post array into our metric fields."""
    if isinstance(payload, dict) and payload.get("missing"):
        raise SystemExit("analytics returned {'missing': true}: run "
                         "`postiz posts:missing <id>` then `posts:connect` first.")
    arr = payload if isinstance(payload, list) else payload.get("metrics", [])
    out = {f: 0.0 for f in METRIC_FIELDS}
    for entry in arr:
        if not isinstance(entry, dict):
            continue
        name = str(entry.get("name") or entry.get("label") or entry.get("metric") or "").lower()
        for needles, field in METRIC_MAP:
            if any(n in name for n in needles):
                out[field] = _metric_total(entry)
                break
    return out


def fetch_from_postiz(post_id, days):
    try:
        raw = subprocess.run(["postiz", "analytics:post", post_id, "-d", str(days)],
                             capture_output=True, text=True, check=True).stdout
    except FileNotFoundError:
        raise SystemExit("postiz CLI not found; install it or use --metrics-json / flags.")
    except subprocess.CalledProcessError as e:
        raise SystemExit(f"postiz analytics:post failed: {e.stderr.strip()}")
    return parse_postiz_metrics(json.loads(raw))


def load_ledger():
    if not os.path.exists(LEDGER):
        return []
    return [json.loads(l) for l in open(LEDGER, encoding="utf-8") if l.strip()]


def save_ledger(rows):
    os.makedirs(PERF_DIR, exist_ok=True)
    with open(LEDGER, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def eng_rate(r):
    imp = r.get("impressions", 0) or 0
    if imp <= 0:
        return 0.0
    return (r.get("likes", 0) + r.get("comments", 0)
            + r.get("shares", 0) + r.get("saves", 0)) / imp


def follow_yield(r):
    imp = r.get("impressions", 0) or 0
    return (r.get("follows", 0) / imp * 1000) if imp > 0 else 0.0


def cmd_record(a):
    metrics = {f: 0.0 for f in METRIC_FIELDS}
    if a.from_postiz:
        metrics.update(fetch_from_postiz(a.from_postiz, a.days))
    elif a.metrics_json:
        metrics.update(parse_postiz_metrics(json.load(open(a.metrics_json, encoding="utf-8"))))
    for f in METRIC_FIELDS:
        v = getattr(a, f)
        if v is not None:
            metrics[f] = float(v)
    row = {"date": a.date or dt.date.today().isoformat(), "post_id": a.post_id,
           "platform": a.platform, "topic": a.topic or "", "hook": a.hook or "",
           "pillar": a.pillar or "", "format": a.format or "",
           **{k: int(v) for k, v in metrics.items()},
           "source": "postiz" if a.from_postiz else ("json" if a.metrics_json else "manual")}
    rows = [r for r in load_ledger() if r.get("post_id") != a.post_id]
    rows.append(row)
    save_ledger(rows)
    print(f"recorded {a.post_id}: ER={eng_rate(row):.1%}  follows/1k={follow_yield(row):.1f}")


def _rank(rows, key):
    groups = {}
    for r in rows:
        k = r.get(key) or "(unset)"
        groups.setdefault(k, []).append(r)
    out = []
    for k, g in groups.items():
        imp = sum(r.get("impressions", 0) for r in g)
        out.append({
            "key": k, "posts": len(g), "impressions": imp,
            "er": sum(eng_rate(r) for r in g) / len(g),
            "fy": sum(follow_yield(r) for r in g) / len(g),
        })
    return sorted(out, key=lambda x: x["er"], reverse=True)


def _table(rows, label):
    out = [f"### By {label}\n",
           f"| {label} | posts | impressions | avg engagement | follows/1k |",
           "|---|--:|--:|--:|--:|"]
    for r in rows:
        out.append(f"| {r['key']} | {r['posts']} | {r['impressions']:,} "
                   f"| {r['er']:.1%} | {r['fy']:.1f} |")
    return "\n".join(out)


def cmd_report(a):
    rows = load_ledger()
    if not rows:
        sys.exit("ledger is empty — record some posts first.")
    today = dt.date.today().isoformat()
    by_hook = _rank(rows, "hook")
    by_topic = _rank(rows, "topic")
    by_platform = _rank(rows, "platform")
    top = sorted(rows, key=eng_rate, reverse=True)[:5]

    lead_hook = by_hook[0]["key"] if by_hook else "(n/a)"
    lead_topic = by_topic[0]["key"] if by_topic else "(n/a)"
    lead_plat = by_platform[0]["key"] if by_platform else "(n/a)"
    total_imp = sum(r.get("impressions", 0) for r in rows)

    md = [f"# Performance report — {today}", "",
          "> Auto-generated by `tools/dgd_performance.py` from the post ledger. "
          "Use it to choose hooks and topics from evidence, and keep every video "
          "educational, not promotional, exactly as the communications discipline "
          "requires. Engagement is a craft signal — not a goal that excuses hype.",
          "",
          f"**{len(rows)} posts · {total_imp:,} impressions.** Current leaders: "
          f"hook **{lead_hook}**, topic **{lead_topic}**, platform **{lead_plat}** "
          "(by average engagement rate).",
          "",
          _table(by_hook, "hook"), "",
          _table(by_topic, "topic"), "",
          _table(by_platform, "platform"), "",
          "### Top posts by engagement", "",
          "| post | platform | hook | topic | ER | follows/1k |",
          "|---|---|---|---|--:|--:|"]
    for r in top:
        md.append(f"| {r['post_id']} | {r['platform']} | {r.get('hook','')} "
                  f"| {r.get('topic','')} | {eng_rate(r):.1%} | {follow_yield(r):.1f} |")
    md += ["",
           "### What to do with this",
           f"- Lean into the **{lead_hook}** hook and **{lead_topic}** topic next cycle; "
           "they're earning the most engagement per impression.",
           "- Re-cut a weak post using a top-ranked hook before assuming the topic failed.",
           "- Confirm the leader on *follows/1k* too — engagement without follows is a "
           "reach signal, not audience growth.",
           "", "→ Feed these picks back into the [DGD Video Studio](../../../skills/dgd-video-studio/SKILL.md) "
           "walkthrough (Stage 1 idea, Stage 2 hook). Rails unchanged: "
           "[communications discipline](../../compliance/communications-discipline.md).", ""]
    report_text = "\n".join(md)

    os.makedirs(PERF_DIR, exist_ok=True)
    path = os.path.join(PERF_DIR, f"PERF-{today}.md")
    open(path, "w", encoding="utf-8").write(report_text)

    # maintain an index
    idx = os.path.join(PERF_DIR, "index.md")
    line = f"- [{today}](PERF-{today}.md) — {len(rows)} posts, leaders: {lead_hook} / {lead_topic} / {lead_plat}"
    existing = ""
    if os.path.exists(idx):
        existing = open(idx, encoding="utf-8").read()
    if "# Performance reports" not in existing:
        existing = ("# Performance reports\n\nNewest first. Generated by "
                    "`tools/dgd_performance.py report`.\n\n")
    lines = existing.splitlines()
    lines = [l for l in lines if f"(PERF-{today}.md)" not in l]
    head = lines[:4]
    body = [l for l in lines[4:] if l.strip()]
    open(idx, "w", encoding="utf-8").write("\n".join(head + [line] + body) + "\n")

    print(f"wrote {path}\nleaders -> hook: {lead_hook} | topic: {lead_topic} | platform: {lead_plat}")


def cmd_show(a):
    rows = load_ledger()
    if not rows:
        sys.exit("ledger is empty.")
    print(f"{'post_id':12s}{'plat':10s}{'hook':18s}{'topic':14s}{'ER':>7s}{'f/1k':>7s}")
    for r in sorted(rows, key=eng_rate, reverse=True):
        print(f"{r['post_id'][:11]:12s}{r['platform'][:9]:10s}{r.get('hook','')[:17]:18s}"
              f"{r.get('topic','')[:13]:14s}{eng_rate(r):6.1%}{follow_yield(r):7.1f}")


def cmd_sync(a):
    """Auto-record a published episode: read its publish dir, pull Postiz analytics."""
    meta_path = os.path.join(a.dir, "post_meta.json")
    pub_path = os.path.join(a.dir, "published.tsv")
    if not os.path.exists(meta_path):
        sys.exit(f"no post_meta.json in {a.dir} (was it built by dgd_publish.py?)")
    if not os.path.exists(pub_path):
        sys.exit(f"no published.tsv in {a.dir} — run publish.sh first so post IDs exist.")
    meta = json.load(open(meta_path, encoding="utf-8"))
    rows = load_ledger()
    n = 0
    for line in open(pub_path, encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 2 or not parts[1]:
            if line.strip():
                print(f"  skip {parts[0] if parts else '?'}: no post id yet "
                      "(provider may not return one immediately; re-sync later)")
            continue
        platform, post_id = parts[0], parts[1]
        metrics = fetch_from_postiz(post_id, a.days)
        row = {"date": dt.date.today().isoformat(), "post_id": post_id, "platform": platform,
               "topic": meta.get("topic", ""), "hook": meta.get("hook", ""),
               "pillar": meta.get("pillar", ""), "format": meta.get("format", ""),
               **{k: int(metrics.get(k, 0)) for k in METRIC_FIELDS}, "source": "postiz-sync"}
        rows = [r for r in rows if r.get("post_id") != post_id]
        rows.append(row)
        n += 1
        print(f"  synced {platform} {post_id}: ER={eng_rate(row):.1%}  follows/1k={follow_yield(row):.1f}")
    save_ledger(rows)
    print(f"sync complete: {n} post(s) recorded from {a.dir}")


DASHBOARD_HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DGD Performance Dashboard</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
<style>
  :root{ --navy:#10172a; --char:#0a0c12; --gold:#d4a853; --goldhi:#f0d082;
         --white:#f4f4f0; --mute:#969eb2; }
  *{box-sizing:border-box} body{margin:0;background:linear-gradient(180deg,var(--navy),var(--char));
    color:var(--white);font-family:'Segoe UI',system-ui,Arial,sans-serif;padding:28px;min-height:100vh}
  h1{font-family:Georgia,'Times New Roman',serif;color:var(--white);margin:0 0 2px;font-size:30px}
  .sub{color:var(--gold);font-weight:600;letter-spacing:.04em;font-size:13px;text-transform:uppercase}
  .kpis{display:flex;gap:16px;flex-wrap:wrap;margin:22px 0}
  .kpi{background:rgba(255,255,255,.04);border:1px solid rgba(212,168,83,.25);border-radius:14px;
       padding:16px 22px;min-width:150px}
  .kpi .n{font-size:30px;font-weight:700;color:var(--goldhi)} .kpi .l{color:var(--mute);font-size:12px;margin-top:4px}
  .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px;margin-bottom:18px}
  .card{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);border-radius:14px;padding:16px}
  .card h3{margin:0 0 10px;font-size:14px;color:var(--gold);font-weight:600}
  table{width:100%;border-collapse:collapse;font-size:13px}
  th,td{padding:8px 10px;text-align:left;border-bottom:1px solid rgba(255,255,255,.07)}
  th{color:var(--mute);font-weight:600;cursor:pointer;user-select:none} td.n,th.n{text-align:right}
  tr:hover td{background:rgba(212,168,83,.06)}
  .foot{color:var(--mute);font-size:12px;margin-top:22px;border-top:1px solid rgba(255,255,255,.08);padding-top:12px}
  .empty{color:var(--mute);padding:40px;text-align:center}
</style></head>
<body>
  <div class="sub">Digital Gold · Educational</div>
  <h1>Performance Dashboard</h1>
  <div id="gen" class="sub" style="color:var(--mute);font-weight:400"></div>
  <div id="app"></div>
  <div class="foot">Engagement is a craft signal for choosing hooks and topics —
    kept educational, never promotional. Source: local post ledger.</div>
<script>
const DATA = __DATA__;
const fmt = n => n.toLocaleString();
const pct = n => (n*100).toFixed(1)+'%';
document.getElementById('gen').textContent = 'Generated ' + DATA.generated + ' · ' + DATA.posts.length + ' posts';
const app = document.getElementById('app');
if(!DATA.posts.length){ app.innerHTML='<div class="empty">Ledger is empty. Record posts, then rebuild.</div>'; }
else{
  app.innerHTML = `
    <div class="kpis">
      <div class="kpi"><div class="n">${DATA.posts.length}</div><div class="l">posts</div></div>
      <div class="kpi"><div class="n">${fmt(DATA.totals.impressions)}</div><div class="l">impressions</div></div>
      <div class="kpi"><div class="n">${pct(DATA.totals.avg_er)}</div><div class="l">avg engagement</div></div>
      <div class="kpi"><div class="n">${DATA.totals.fy.toFixed(1)}</div><div class="l">avg follows / 1k</div></div>
    </div>
    <div class="grid">
      <div class="card"><h3>Avg engagement by hook</h3><canvas id="c_hook"></canvas></div>
      <div class="card"><h3>Avg engagement by topic</h3><canvas id="c_topic"></canvas></div>
      <div class="card"><h3>Avg engagement by platform</h3><canvas id="c_plat"></canvas></div>
    </div>
    <div class="card"><h3>Posts (click a header to sort)</h3>
      <table id="tbl"><thead><tr>
        <th data-k="post_id">post</th><th data-k="platform">platform</th>
        <th data-k="hook">hook</th><th data-k="topic">topic</th>
        <th class="n" data-k="impressions">impressions</th>
        <th class="n" data-k="er">engagement</th><th class="n" data-k="fy">follows/1k</th>
      </tr></thead><tbody></tbody></table></div>`;
  const GOLD='#d4a853', GRID='rgba(255,255,255,.08)';
  const bar = (id,rows)=> new Chart(document.getElementById(id),{type:'bar',
    data:{labels:rows.map(r=>r.key),datasets:[{data:rows.map(r=>+(r.er*100).toFixed(1)),
      backgroundColor:GOLD,borderRadius:5}]},
    options:{plugins:{legend:{display:false}},scales:{
      x:{ticks:{color:'#969eb2'},grid:{display:false}},
      y:{ticks:{color:'#969eb2',callback:v=>v+'%'},grid:{color:GRID}}}}});
  bar('c_hook',DATA.by_hook); bar('c_topic',DATA.by_topic); bar('c_plat',DATA.by_platform);
  const tb=document.querySelector('#tbl tbody'); let dir=1,last='er';
  const render=k=>{ DATA.posts.sort((a,b)=>{const x=a[k],y=b[k];
      return (typeof x==='number'? x-y : (''+x).localeCompare(y))*dir;});
    tb.innerHTML=DATA.posts.map(p=>`<tr><td>${p.post_id}</td><td>${p.platform}</td>
      <td>${p.hook||''}</td><td>${p.topic||''}</td><td class="n">${fmt(p.impressions)}</td>
      <td class="n">${pct(p.er)}</td><td class="n">${p.fy.toFixed(1)}</td></tr>`).join(''); };
  document.querySelectorAll('#tbl th').forEach(th=>th.onclick=()=>{const k=th.dataset.k;
    dir = (k===last)? -dir : 1; last=k; render(k);});
  render('er');
}
</script></body></html>"""


def cmd_dashboard(a):
    rows = load_ledger()
    by = {k: _rank(rows, k) for k in ("hook", "topic", "platform")}
    total_imp = sum(r.get("impressions", 0) for r in rows)
    data = {
        "generated": dt.date.today().isoformat(),
        "totals": {"impressions": total_imp,
                   "avg_er": (sum(eng_rate(r) for r in rows) / len(rows)) if rows else 0,
                   "fy": (sum(follow_yield(r) for r in rows) / len(rows)) if rows else 0},
        "by_hook": by["hook"], "by_topic": by["topic"], "by_platform": by["platform"],
        "posts": [{"post_id": r.get("post_id", ""), "platform": r.get("platform", ""),
                   "hook": r.get("hook", ""), "topic": r.get("topic", ""),
                   "impressions": r.get("impressions", 0),
                   "er": round(eng_rate(r), 4), "fy": round(follow_yield(r), 1)} for r in rows],
    }
    html = DASHBOARD_HTML.replace("__DATA__", json.dumps(data, ensure_ascii=False))
    out = a.out or os.path.join(PERF_DIR, "dashboard.html")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    open(out, "w", encoding="utf-8").write(html)
    print(f"wrote {out}  ({len(rows)} posts)")


def main():
    ap = argparse.ArgumentParser(description="DGD performance loop")
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("record")
    r.add_argument("--post-id", required=True)
    r.add_argument("--platform", required=True)
    r.add_argument("--topic"); r.add_argument("--hook")
    r.add_argument("--pillar"); r.add_argument("--format")
    r.add_argument("--date")
    for f in METRIC_FIELDS:
        r.add_argument(f"--{f}", type=float)
    r.add_argument("--metrics-json")
    r.add_argument("--from-postiz")
    r.add_argument("--days", type=int, default=14)
    r.set_defaults(func=cmd_record)

    rep = sub.add_parser("report")
    rep.set_defaults(func=cmd_report)

    sh = sub.add_parser("show")
    sh.set_defaults(func=cmd_show)

    sy = sub.add_parser("sync")
    sy.add_argument("--dir", required=True,
                    help="a dgd_publish.py --outdir (has post_meta.json + published.tsv)")
    sy.add_argument("--days", type=int, default=14)
    sy.set_defaults(func=cmd_sync)

    db = sub.add_parser("dashboard")
    db.add_argument("--out", help="HTML output path (default: trends/performance/dashboard.html)")
    db.set_defaults(func=cmd_dashboard)

    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
