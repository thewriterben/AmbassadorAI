#!/usr/bin/env python3
"""
dgd_web.py - local control-panel SERVER for DGD Video Studio (the "do" app).

The static site (build_site.py) is for viewing and drafting in the browser. This is the
local companion that actually RUNS the tools: it renders real PNGs, builds gated publish
packages, reads the live ledger, and generates reports — all behind a small zero-
dependency stdlib HTTP server bound to localhost.

  python3 tools/dgd_web.py                 # -> http://127.0.0.1:8000  (local only)
  python3 tools/dgd_web.py --port 9000
  python3 tools/dgd_web.py --host 0.0.0.0  # expose on your LAN (prints a warning)

Endpoints (all local):
  GET  /                       the server-aware control panel
  GET  /api/perf               live ledger data (computed)
  POST /api/lint               {text, requireDisclosure} -> findings + verdict
  GET  /api/title.png?...      real make_title PNG (server-side compliance-gated)
  POST /api/kit                {headline,kicker,subtitle,episode} -> renders a kit
  POST /api/publish            {caption,title,...} -> fail-closed publish package
  POST /api/perf/report        regenerate the performance report
  GET  /work/<path>            generated files (assets, packages)

Safety: binds 127.0.0.1 by default. It executes local tools and writes under a work dir,
but it never posts — the publish endpoint only BUILDS the package; you run publish.sh
yourself in a terminal. Text is compliance-gated server-side (fail-closed), same rails
as the CLI.
"""
import argparse
import io
import json
import os
import subprocess
import sys
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import compliance_lint as CL          # noqa: E402
import dgd_assets as ASSETS           # noqa: E402
import dgd_performance as PERF        # noqa: E402

WORK = os.path.join(ROOT, ".dgd_web_work")


def _run(args):
    """Run a toolchain CLI, capture result."""
    p = subprocess.run([sys.executable, *args], capture_output=True, text=True, cwd=ROOT)
    return {"code": p.returncode, "out": p.stdout, "err": p.stderr}


def ledger_payload():
    rows = PERF.load_ledger()
    by = {k: PERF._rank(rows, k) for k in ("hook", "topic", "platform")}
    return {
        "posts": [{"post_id": r.get("post_id", ""), "platform": r.get("platform", ""),
                   "hook": r.get("hook", ""), "topic": r.get("topic", ""),
                   "impressions": r.get("impressions", 0),
                   "er": round(PERF.eng_rate(r), 4), "fy": round(PERF.follow_yield(r), 1)}
                  for r in rows],
        "by_hook": by["hook"], "by_topic": by["topic"], "by_platform": by["platform"],
        "totals": {"impressions": sum(r.get("impressions", 0) for r in rows),
                   "avg_er": (sum(PERF.eng_rate(r) for r in rows) / len(rows)) if rows else 0,
                   "fy": (sum(PERF.follow_yield(r) for r in rows) / len(rows)) if rows else 0},
    }


PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DGD Studio — Local Control Panel</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
<style>
:root{--navy:#10172a;--char:#0a0c12;--gold:#d4a853;--goldhi:#f0d082;--white:#f4f4f0;--mute:#969eb2;
--fail:#e2696b;--warn:#d9a441;--pass:#5fb98e}
*{box-sizing:border-box}body{margin:0;background:linear-gradient(180deg,var(--navy),var(--char));
color:var(--white);font-family:'Segoe UI',system-ui,Arial,sans-serif;min-height:100vh}
header{padding:22px 28px 0}.sub{color:var(--gold);font-weight:600;letter-spacing:.05em;font-size:12px;text-transform:uppercase}
h1{font-family:Georgia,serif;margin:2px 0 0;font-size:26px}.tag{color:var(--pass);font-size:12px}
nav{display:flex;gap:8px;padding:16px 28px 0;flex-wrap:wrap}
nav button{background:rgba(255,255,255,.04);color:var(--white);border:1px solid rgba(212,168,83,.3);border-radius:9px;padding:9px 16px;cursor:pointer}
nav button.active{background:var(--gold);color:#1a1205;font-weight:700}
main{padding:22px 28px 60px;max-width:1050px}section{display:none}section.active{display:block}
.card{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:18px;margin-bottom:18px}
.card h3{margin:0 0 12px;color:var(--gold);font-size:14px}
label{display:block;font-size:12px;color:var(--mute);margin:10px 0 4px}
input[type=text],textarea{width:100%;background:rgba(0,0,0,.25);border:1px solid rgba(255,255,255,.14);color:var(--white);border-radius:9px;padding:10px;font-family:inherit}
textarea{min-height:110px}.row{display:flex;gap:16px;flex-wrap:wrap}.row>*{flex:1;min-width:220px}
.chk{display:flex;gap:8px;align-items:center;font-size:14px;margin-top:8px}.chk input{width:auto}
button.act{background:var(--gold);color:#1a1205;border:none;border-radius:9px;padding:10px 18px;font-weight:700;cursor:pointer;margin-top:12px}
button.ghost{background:transparent;border:1px solid var(--gold);color:var(--gold)}
.badge{display:inline-block;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:700}
.b-pass{background:rgba(95,185,142,.18);color:var(--pass)}.b-warn{background:rgba(217,164,65,.18);color:var(--warn)}.b-fail{background:rgba(226,105,107,.18);color:var(--fail)}
.finding{border-left:3px solid var(--fail);padding:6px 10px;margin:8px 0;background:rgba(226,105,107,.06);font-size:13px}
.finding.warn{border-color:var(--warn);background:rgba(217,164,65,.06)}.finding .fix{color:var(--mute);font-size:12px}
.kpis{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:14px}.kpi{background:rgba(255,255,255,.04);border:1px solid rgba(212,168,83,.25);border-radius:12px;padding:14px 20px}
.kpi .n{font-size:24px;font-weight:700;color:var(--goldhi)}.kpi .l{color:var(--mute);font-size:11px}
table{width:100%;border-collapse:collapse;font-size:13px}th,td{padding:7px 9px;text-align:left;border-bottom:1px solid rgba(255,255,255,.07)}th{color:var(--mute)}
td.n,th.n{text-align:right}pre{background:rgba(0,0,0,.35);border-radius:9px;padding:12px;overflow:auto;font-size:12px;color:#cfe;white-space:pre-wrap}
.foot{color:var(--mute);font-size:12px;border-top:1px solid rgba(255,255,255,.08);padding:14px 28px;max-width:1050px}
img.preview{max-width:300px;border-radius:10px;border:1px solid rgba(255,255,255,.1)}a{color:var(--gold)}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:10px}
.gallery img{width:100%;border-radius:8px;background:#0b0e16}
</style></head><body>
<header><div class="sub">Digital Gold · Educational</div>
<h1>Local Control Panel</h1><div class="tag">● live · runs the tools on your machine</div></header>
<nav>
<button data-tab="perf" class="active">Performance</button>
<button data-tab="lint">Lint</button>
<button data-tab="assets">Assets</button>
<button data-tab="publish">Publish</button>
</nav>
<main>
<section id="perf" class="active"><div class="card"><h3>Performance (live ledger)</h3>
<button class="act ghost" onclick="loadPerf()">Refresh</button><div id="perfBody"></div></div></section>

<section id="lint"><div class="card"><h3>Compliance linter (server, fail-closed)</h3>
<textarea id="lintIn" placeholder="Paste a script/caption…"></textarea>
<label class="chk"><input type="checkbox" id="lintDiscl"> require “not financial advice”</label>
<span id="lintV"></span><div id="lintOut"></div></div></section>

<section id="assets"><div class="card"><h3>Title card — real renderer</h3>
<div class="row"><div><label>Headline</label><input id="aHead" type="text" value="Why your money quietly loses value"></div>
<div><label>Kicker</label><input id="aKick" type="text" value="Sound Money - Ep. 1"></div></div>
<label>Subtitle</label><input id="aSub" type="text" value="A two-minute explainer.">
<button class="act" onclick="renderTitle()">Render PNG</button><span id="aV"></span>
<div id="aOut" style="margin-top:12px"></div></div>
<div class="card"><h3>Build a full kit</h3>
<label>Episode folder name</label><input id="kEp" type="text" value="ep1">
<button class="act" onclick="buildKit()">Render kit</button><div id="kOut"></div></div></section>

<section id="publish"><div class="card"><h3>Publish package (gated, builds files — does not post)</h3>
<label>Base caption</label><textarea id="pCap">Money loses value quietly. Here's the mechanism, in 60s.</textarea>
<div class="row"><div><label>YouTube title</label><input id="pTitle" type="text" value="Why money loses value in 60s"></div>
<div><label>Episode/output name</label><input id="pEp" type="text" value="ep1"></div></div>
<div class="row"><div><label class="chk"><input type="checkbox" id="pSpon"> Sponsored (#Ad)</label>
<label class="chk"><input type="checkbox" id="pAI"> AI media</label></div></div>
<button class="act" onclick="buildPublish()">Build &amp; gate</button><span id="pV"></span><div id="pOut"></div></div></section>
</main>
<div class="foot">Runs locally on your machine. Engagement is a craft signal, kept educational
and never promotional. This app builds packages and assets; it never posts — run
<code>publish.sh</code> in a terminal to schedule.</div>
<script>
const $=id=>document.getElementById(id);
document.querySelectorAll('nav button').forEach(b=>b.onclick=()=>{
 document.querySelectorAll('nav button').forEach(x=>x.classList.remove('active'));
 document.querySelectorAll('main section').forEach(x=>x.classList.remove('active'));
 b.classList.add('active');$(b.dataset.tab).classList.add('active');});
const badge=v=>'<span class="badge b-'+v+'">'+v.toUpperCase()+'</span>';
const findings=f=>f.length?f.map(x=>'<div class="finding'+(x.severity==='WARN'?' warn':'')+'"><b>['+x.severity+']</b> '+
 (x.line?('L'+x.line+' '):'')+x.category+": '"+x.term+"'<div class=fix>"+x.fix+'</div></div>').join(''):'<p style="color:#969eb2">Clean.</p>';
async function api(path,body){const r=await fetch(path,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});return r.json();}
// lint
async function runLint(){const t=$('lintIn').value;if(!t){$('lintV').innerHTML='';$('lintOut').innerHTML='';return;}
 const d=await api('/api/lint',{text:t,requireDisclosure:$('lintDiscl').checked});
 $('lintV').innerHTML=badge(d.verdict);$('lintOut').innerHTML=findings(d.findings);}
$('lintIn').addEventListener('input',runLint);$('lintDiscl').addEventListener('change',runLint);
// title
async function renderTitle(){const q=new URLSearchParams({headline:$('aHead').value,kicker:$('aKick').value,subtitle:$('aSub').value});
 const r=await fetch('/api/title.png?'+q.toString());
 if(r.ok){const b=await r.blob();$('aV').innerHTML=badge('pass');$('aOut').innerHTML='<img class=preview src="'+URL.createObjectURL(b)+'">';}
 else{const d=await r.json();$('aV').innerHTML=badge('fail');$('aOut').innerHTML=findings((d.hits||[]).map(h=>({severity:'FAIL',category:'compliance',term:h,fix:'Reframe (mechanism, not forecast).',line:0})));}}
async function buildKit(){$('kOut').innerHTML='Rendering…';const d=await api('/api/kit',{episode:$('kEp').value,headline:$('aHead').value,kicker:$('aKick').value,subtitle:$('aSub').value});
 if(d.error){$('kOut').innerHTML=badge('fail')+' '+d.error;return;}
 $('kOut').innerHTML='<p>'+badge('pass')+' '+d.files.length+' files in '+d.dir+'</p><div class=gallery>'+
  d.files.filter(f=>f.endsWith('.png')&&!f.startsWith('_')).map(f=>'<img loading=lazy src="/work/'+d.rel+'/'+f+'">').join('')+'</div>';}
// publish
async function buildPublish(){$('pOut').innerHTML='Building…';const d=await api('/api/publish',
 {caption:$('pCap').value,title:$('pTitle').value,episode:$('pEp').value,sponsored:$('pSpon').checked,ai_media:$('pAI').checked});
 let h='<p>'+badge(d.verdict)+' '+(d.verdict==='fail'?'Publish blocked — reframe and rebuild.':'Gate passed.')+'</p><pre>'+d.out.replace(/</g,'&lt;')+'</pre>';
 if(d.verdict!=='fail'&&d.links)h+=d.links.map(l=>'<a href="'+l.href+'" download>'+l.name+'</a>').join(' · ');
 $('pOut').innerHTML=h;}
// perf
async function loadPerf(){const L=await (await fetch('/api/perf')).json();const el=$('perfBody');
 if(!L.posts.length){el.innerHTML='<p style="color:#969eb2">Ledger empty. Use Publish, post, then sync analytics.</p>';return;}
 const pct=n=>(n*100).toFixed(1)+'%',fmt=n=>n.toLocaleString();
 el.innerHTML='<div class=kpis><div class=kpi><div class=n>'+L.posts.length+'</div><div class=l>posts</div></div>'+
  '<div class=kpi><div class=n>'+fmt(L.totals.impressions)+'</div><div class=l>impressions</div></div>'+
  '<div class=kpi><div class=n>'+pct(L.totals.avg_er)+'</div><div class=l>avg engagement</div></div></div>'+
  '<canvas id=chk height=120></canvas><table><thead><tr><th>post</th><th>platform</th><th>hook</th><th>topic</th>'+
  '<th class=n>impr.</th><th class=n>eng.</th></tr></thead><tbody>'+
  L.posts.sort((a,b)=>b.er-a.er).map(p=>'<tr><td>'+p.post_id+'</td><td>'+p.platform+'</td><td>'+(p.hook||'')+'</td><td>'+(p.topic||'')+
  '</td><td class=n>'+fmt(p.impressions)+'</td><td class=n>'+pct(p.er)+'</td></tr>').join('')+'</tbody></table>';
 if(window.Chart)new Chart($('chk'),{type:'bar',data:{labels:L.by_hook.map(r=>r.key),
  datasets:[{data:L.by_hook.map(r=>+(r.er*100).toFixed(1)),backgroundColor:'#d4a853',borderRadius:5}]},
  options:{plugins:{legend:{display:false}},scales:{x:{ticks:{color:'#969eb2'},grid:{display:false}},y:{ticks:{color:'#969eb2',callback:v=>v+'%'},grid:{color:'rgba(255,255,255,.08)'}}}}});}
loadPerf();
</script></body></html>"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="application/json"):
        if isinstance(body, (dict, list)):
            body = json.dumps(body).encode()
        elif isinstance(body, str):
            body = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _body(self):
        n = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(n) or b"{}") if n else {}

    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        q = urllib.parse.parse_qs(u.query)
        if u.path == "/":
            return self._send(200, PAGE, "text/html; charset=utf-8")
        if u.path == "/api/perf":
            return self._send(200, ledger_payload())
        if u.path == "/api/title.png":
            head = (q.get("headline", [""])[0]); kick = q.get("kicker", [""])[0]; sub = q.get("subtitle", [""])[0]
            hits = ASSETS.compliance_scan(head, kick, sub)
            if hits:
                return self._send(422, {"error": "compliance", "hits": [h[1] for h in hits]})
            img = ASSETS.make_title(head, kick or None, sub or None)
            buf = io.BytesIO(); img.save(buf, "PNG")
            return self._send(200, buf.getvalue(), "image/png")
        if u.path.startswith("/work/"):
            return self._serve_work(u.path[len("/work/"):])
        return self._send(404, {"error": "not found"})

    def do_POST(self):
        u = urllib.parse.urlparse(self.path)
        b = self._body()
        if u.path == "/api/lint":
            res = CL.lint_text(b.get("text", ""), want_disclosure=b.get("requireDisclosure", False))
            return self._send(200, res)
        if u.path == "/api/kit":
            ep = _safe(b.get("episode", "ep"))
            out = os.path.join(WORK, ep)
            r = _run([os.path.join(HERE, "dgd_assets.py"), "kit",
                      "--headline", b.get("headline", "Untitled"),
                      "--kicker", b.get("kicker", ""), "--subtitle", b.get("subtitle", ""),
                      "--outdir", out])
            if r["code"] != 0:
                return self._send(200, {"error": (r["err"] or r["out"]).strip()})
            files = sorted(os.listdir(out)) if os.path.isdir(out) else []
            return self._send(200, {"dir": out, "rel": ep, "files": files})
        if u.path == "/api/publish":
            ep = _safe(b.get("episode", "ep"))
            out = os.path.join(WORK, ep, "publish")
            args = [os.path.join(HERE, "dgd_publish.py"),
                    "--caption", b.get("caption", ""), "--title", b.get("title", ""),
                    "--media", "video.mp4", "--schedule", "2026-07-01T15:00:00Z",
                    "--outdir", out]
            if b.get("sponsored"): args.append("--sponsored")
            if b.get("ai_media"): args.append("--ai-media")
            r = _run(args)
            verdict = "fail" if r["code"] == 2 else ("pass" if r["code"] == 0 else "warn")
            links = []
            if verdict != "fail" and os.path.isdir(out):
                for f in ("campaign.json", "captions.txt", "publish.sh"):
                    if os.path.exists(os.path.join(out, f)):
                        links.append({"name": f, "href": f"/work/{ep}/publish/{f}"})
            return self._send(200, {"verdict": verdict, "out": (r["out"] + r["err"]).strip(), "links": links})
        if u.path == "/api/perf/report":
            r = _run([os.path.join(HERE, "dgd_performance.py"), "report"])
            return self._send(200, {"out": (r["out"] + r["err"]).strip()})
        return self._send(404, {"error": "not found"})

    def _serve_work(self, rel):
        rel = rel.split("?")[0]
        full = os.path.normpath(os.path.join(WORK, rel))
        if not full.startswith(os.path.abspath(WORK)) or not os.path.isfile(full):
            return self._send(404, {"error": "not found"})
        ext = os.path.splitext(full)[1].lower()
        ctype = {".png": "image/png", ".json": "application/json",
                 ".txt": "text/plain", ".sh": "text/plain", ".html": "text/html"}.get(ext, "application/octet-stream")
        with open(full, "rb") as f:
            return self._send(200, f.read(), ctype)


def _safe(name):
    return "".join(c for c in str(name) if c.isalnum() or c in "-_") or "ep"


def main():
    ap = argparse.ArgumentParser(description="DGD local control-panel server")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8000)
    a = ap.parse_args()
    os.makedirs(WORK, exist_ok=True)
    if a.host not in ("127.0.0.1", "localhost"):
        print(f"⚠  Binding {a.host} — reachable beyond this machine. It can run local tools "
              "and write files; only do this on a trusted network.")
    srv = ThreadingHTTPServer((a.host, a.port), Handler)
    print(f"DGD Studio local control panel → http://{a.host}:{a.port}  (Ctrl+C to stop)")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped.")


if __name__ == "__main__":
    main()
