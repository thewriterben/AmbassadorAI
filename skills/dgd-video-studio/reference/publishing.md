# Reference — Publishing & Scheduling (Stage 6 → live)

Closes the last loop: take the finished, lint-passed video and **schedule it** to X,
TikTok, Instagram Reels, and YouTube Shorts via [Postiz](https://postiz.com), with
disclosures front-loaded and the communications discipline enforced on every caption
*before* anything is queued.

Driver: `tools/dgd_publish.py`. It is a **package builder + gate**, not an auto-poster —
it never publishes on its own. It tailors captions, gates them, and writes the exact
artifacts Postiz consumes, so it is safe to run as a dry run with no API key and ready
to schedule for real the moment `POSTIZ_API_KEY` is set.

## What it does

1. **Tailors a caption per platform** to `../../LLMWiki/craft/platform-specs.md`: X gets
   ≤3 hashtags and a 280-char guard; TikTok/IG/YT get ≤5; YouTube gets a searchable
   `title` in settings.
2. **Front-loads disclosures**: `--sponsored` → `#Ad` at the very front (FTC); `--ai-media`
   → "Made with AI." (realistic synthetic media); and **always** a `Not financial advice.
   Educational.` line — spoken *and* in caption, per `../../LLMWiki/compliance/ftc-disclosure.md`
   and `ai-disclosure.md`. (These are caption-level; you still flip each platform's
   branded-content / AI toggle, and keep both labels on-screen in the first 3–5s.)
3. **Gates every caption + the title** through `tools/compliance_lint.py`
   (`lint_text`). **Any FAIL aborts with exit 2 and writes nothing** — the rail sits
   between "draft" and "queue." `--strict` also blocks on WARN.
4. **Emits** into `--outdir`: `campaign.json` (Postiz `--json` multi-platform shape),
   `publish.sh` (uploads media, resolves integration IDs via `integrations:list`,
   `posts:create` per platform at the scheduled time), `captions.txt` (human preview),
   and one `<platform>.txt` per channel.

## Run it

```bash
python3 tools/dgd_publish.py \
  --caption "Money loses value quietly. Here's the mechanism, in 60s." \
  --title "Why money loses value - sound money explained in 60s" \
  --media raw/ep1/video.mp4 --thumb raw/ep1/02_thumb.png \
  --schedule 2026-07-01T15:00:00Z \
  --sponsored --ai-media \
  --platforms x,tiktok,instagram,youtube \
  --outdir raw/ep1/publish

# dry run prints the gate result + writes the package; then, to actually schedule:
export POSTIZ_API_KEY=...           # one-time; Postiz CLI must be installed
bash raw/ep1/publish/publish.sh
```

Use `--sponsored` only when the ambassador earns DGD recognition for the post (then the
FTC label is mandatory). Use `--ai-media` whenever a realistic AI voice/avatar/video is
used — abstract motif b-roll from `dgd_assets.py` does **not** by itself require it.

## Where this fits
- **Stage 6.** After assembly, build the package here; the gate is your pre-flight.
- **Stage 7.** The same linter backs `compliance-gate.md` — captions are gated by the
  identical rules, so a post can't go out with framing a script would have been stopped for.
- **Performance loop (auto).** Pass `--hook/--topic/--pillar/--format` to `dgd_publish.py`
  and it writes `post_meta.json`; the generated `publish.sh` logs each returned post-id to
  `published.tsv`. Then `python3 tools/dgd_performance.py sync --dir <publishdir>` pulls
  `postiz analytics:post` for every post and records it to the ledger with the right hook/
  topic attached — no manual entry. `report` turns the ledger into evidence in
  `../../LLMWiki/trends/performance/` that Jobs C & D read to pick winning hooks/topics.

## Connects to
- Rails: `compliance-gate.md` · `../../LLMWiki/compliance/ftc-disclosure.md` · `ai-disclosure.md`
- Specs: `../../LLMWiki/craft/platform-specs.md` · platform policy: `../../LLMWiki/compliance/platform-policies.md`
- Assets to attach: `asset-generation.md` (`kit` output) · Postiz usage: the `postiz` skill
