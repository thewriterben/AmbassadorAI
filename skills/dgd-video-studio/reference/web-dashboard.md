# Reference — Web Control Panel (deployable static site)

There are **two web front-ends**, by design:

- **Static site** (`build_site.py` / `dgd site`) — public-hostable, no backend. View + draft;
  the linter and caption logic run client-side, baked from the Python tools.
- **Local server** (`dgd_web.py` / `dgd serve`) — runs on your machine and actually *runs*
  the tools: renders real PNGs, builds gated publish packages, reads the live ledger.

Use the static site to share/view; use the local server to do.

---

## Static site

A public-hostable, single-page **control panel** for the whole studio. Because it is a
*static* site (no backend), the interactive pieces are ported to client-side JavaScript
that is **baked from the Python tools**, so there is one source of truth and the browser
behaves like the CLI.

Build it with `tools/build_site.py` (or `python3 tools/dgd.py site`).

## Tabs

- **Performance** — KPIs, engagement-by-hook/topic/platform charts, sortable post table,
  from the ledger snapshot embedded at build time.
- **Lint a caption** — the compliance linter, live as you type. Its rules are exported
  straight from `compliance_lint.py` (`RULES`), so the page flags exactly what the CLI
  flags. Verified: client verdicts match Python on all 21 red-team eval cases.
- **Publish builder** — ports `dgd_publish.py`'s caption tailoring (per-platform hashtag
  limits, X 280-char guard, front-loaded `#Ad` / AI / not-financial-advice disclosure),
  gates each caption client-side, and offers `campaign.json` + `captions.txt` downloads.
  Actual scheduling still runs locally via the generated `publish.sh` + Postiz CLI.
- **Assets** — gallery of the baked asset images, plus a live in-browser title-card
  preview (canvas, downloadable PNG). Final PNGs and motif b-roll still come from
  `dgd_assets.py`.

Every text surface on the page is gated by the same rails; the footer carries the
educational / not-financial-advice note.

## Build & preview

```bash
python3 tools/dgd.py site                 # -> site/  (embeds the live ledger)
python3 tools/dgd.py site --no-ledger      # public build: omit performance data (privacy)
python3 tools/dgd.py site --out docs       # build into /docs for Pages
python3 -m http.server -d site 8000        # preview at http://localhost:8000
```

`build_site.py` copies `example-output/asset-pack/*.png` into `site/assets/` for the
gallery (override with `--assets-dir`).

## Deploy (public internet)

`.github/workflows/pages.yml` builds the site in CI **with `--no-ledger`** and publishes
it to GitHub Pages on every push to `main` (or via "Run workflow"). To enable:
Repo → Settings → Pages → Build and deployment → Source: **GitHub Actions**. The site then
lives at `https://<user>.github.io/<repo>/`. Any static host (Netlify, Cloudflare Pages,
S3) works too — just serve the `site/` folder.

**Privacy / compliance for a public build:** the default CI build omits the performance
ledger (your post metrics stay private). The publish tab only *builds* downloadable files
— it cannot post — and the linter runs entirely in the browser. Keep `--no-ledger` for
anything public unless you intend to share the numbers.

## Local server (the "do" app)

Zero-dependency stdlib server (no Flask), bound to localhost:

```bash
python3 tools/dgd.py serve            # -> http://127.0.0.1:8000 (local only)
python3 tools/dgd.py serve --port 9000
python3 tools/dgd.py serve --host 0.0.0.0  # LAN (prints a warning)
```

Endpoints actually run the toolchain: `/api/lint` (server-side `lint_text`), `/api/title.png` (real `make_title`, **422 if the text fails the rails**), `/api/kit`, `/api/publish` (fail-closed; returns download links to `campaign.json`/`captions.txt`/`publish.sh`), and `/api/perf` (live ledger). Generated files live under `.dgd_web_work/` and are served at `/work/…` (path-traversal guarded).

**Safety:** binds `127.0.0.1` by default; it builds packages and assets but **never posts** — you run `publish.sh` yourself in a terminal. All text is compliance-gated server-side, same rails as the CLI. Exposing it with `--host 0.0.0.0` lets others on your network run the local tools, so only do that on a trusted network.

## Connects to
- Rules source: `compliance-gate.md` · `../../../tools/compliance_lint.py`
- Caption logic: `publishing.md` · Assets: `asset-generation.md` · Data: `../../LLMWiki/trends/performance/`
