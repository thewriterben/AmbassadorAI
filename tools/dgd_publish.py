#!/usr/bin/env python3
"""
dgd_publish.py - Stage 6 publish loop: compliant caption tailoring + Postiz hand-off.

Closes the last loop. Given a base caption, media, and a schedule time, it:
  1. tailors a caption per platform (X / TikTok / Instagram Reels / YouTube Shorts)
     to the wiki's platform-specs.md rules (hashtag counts, X 280-char habit, YT
     searchable title);
  2. front-loads the required disclosures - FTC (#Ad) when sponsored, an AI-media
     note when realistic synthetic media is used, and ALWAYS a "Not financial
     advice. Educational." line (the discipline requires it spoken + in caption);
  3. runs every final caption + title through compliance_lint.lint_text and
     **refuses to emit anything if a FAIL is found** (fail-closed);
  4. writes a Postiz `--json` campaign file + a runnable publish.sh (upload media,
     resolve integration IDs, posts:create per platform) + a human caption preview.

It does NOT post by itself - it produces the exact artifacts Postiz consumes, so it
is safe to run as a dry run with no API key, and ready to schedule for real the
moment `POSTIZ_API_KEY` is set and the Postiz CLI is installed.

Source shapes:
  Postiz CLI + --json schema:  postiz skill (posts:create --json, per-provider settings)
  Platform rules:              LLMWiki/craft/platform-specs.md
  Disclosure rules:            LLMWiki/compliance/{ftc-disclosure,ai-disclosure}.md
  Caption rails:               tools/compliance_lint.py (the Stage-7 gate)

Usage
-----
  python3 tools/dgd_publish.py \
    --caption "Money loses value quietly. Here's the mechanism, in 60s." \
    --title "Why money loses value - sound money explained" \
    --media raw/ep1/video.mp4 --thumb raw/ep1/02_thumb.png \
    --schedule 2026-07-01T15:00:00Z --sponsored --ai-media \
    --platforms x,tiktok,instagram,youtube --outdir raw/ep1/publish
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compliance_lint import lint_text  # noqa: E402

# platform -> (postiz identifier, max hashtags, caption char budget or None)
PLATFORMS = {
    "x":         ("twitter",   3, 280),
    "tiktok":    ("tiktok",    5, 2200),
    "instagram": ("instagram", 5, 2200),
    "youtube":   ("youtube",   5, 5000),
}
SAFE_TAGS = ["soundmoney", "economics", "monetarypolicy",
             "austrianeconomics", "cryptoeducation", "fintecheducation"]
DISCLOSURE = "Not financial advice. Educational."


def build_caption(platform, base, tags, sponsored, ai_media):
    ident, max_tags, budget = PLATFORMS[platform]
    front = []
    if sponsored:
        front.append("#Ad")           # FTC: disclosure at the FRONT, not buried
    discl = DISCLOSURE + (" Made with AI." if ai_media else "")
    tagline = " ".join("#" + t for t in tags[:max_tags])
    head = (" ".join(front) + "\n") if front else ""
    caption = f"{head}{base.strip()}\n\n{discl}\n{tagline}".strip()
    # X is tight: drop hashtags first, then flag if still over budget
    warns = []
    if budget and len(caption) > budget:
        caption = f"{head}{base.strip()}\n\n{discl}".strip()
        if len(caption) > budget:
            warns.append(f"{platform}: caption {len(caption)} chars > {budget}; shorten the base.")
    return caption, warns


def provider_settings(platform, title, tags, ai_media):
    if platform == "youtube":
        return {"title": title or "Sound money, explained",
                "type": "public",
                "tags": [{"value": t, "label": t} for t in tags[:5]]}
    if platform == "tiktok":
        return {"privacy": "PUBLIC_TO_EVERYONE", "duet": True, "stitch": True}
    if platform == "instagram":
        return {"post_type": "post"}   # Reel when media is video
    if platform == "x":
        return {"who_can_reply_post": "everyone"}
    return {}


def main():
    ap = argparse.ArgumentParser(description="DGD Stage-6 publish package builder")
    ap.add_argument("--caption", required=True, help="base educational caption / hook")
    ap.add_argument("--title", default="", help="YouTube searchable title")
    ap.add_argument("--media", required=True, help="primary media file (video)")
    ap.add_argument("--thumb", default="", help="optional thumbnail/cover image")
    ap.add_argument("--schedule", required=True, help="ISO 8601, e.g. 2026-07-01T15:00:00Z")
    ap.add_argument("--platforms", default="x,tiktok,instagram,youtube")
    ap.add_argument("--hashtags", help="comma-separated override (no #)")
    ap.add_argument("--sponsored", action="store_true", help="ambassador earns DGD recognition -> FTC #Ad")
    ap.add_argument("--ai-media", action="store_true", help="realistic AI voice/avatar/video used")
    ap.add_argument("--hook", default="", help="hook type used (for the performance ledger)")
    ap.add_argument("--topic", default="", help="topic (for the performance ledger)")
    ap.add_argument("--pillar", default="", help="DGD pillar (for the performance ledger)")
    ap.add_argument("--format", default="", help="format, e.g. faceless/talking-head")
    ap.add_argument("--strict", action="store_true", help="also abort on WARN")
    ap.add_argument("--outdir", required=True)
    a = ap.parse_args()

    platforms = [p.strip() for p in a.platforms.split(",") if p.strip()]
    bad = [p for p in platforms if p not in PLATFORMS]
    if bad:
        sys.exit(f"unknown platform(s): {', '.join(bad)}; choose from {', '.join(PLATFORMS)}")
    tags = [t.strip().lstrip("#") for t in a.hashtags.split(",")] if a.hashtags else SAFE_TAGS

    # ---- build + GATE every caption (fail-closed) ----------------------------
    built, all_warns, gate_fail = {}, [], False
    print("compliance gate (per-platform caption):")
    for p in platforms:
        cap, warns = build_caption(p, a.caption, tags, a.sponsored, a.ai_media)
        res = lint_text(cap, want_disclosure=True)
        built[p] = cap
        all_warns += [f"{p}: {w['category']} '{w['term']}'" for w in res["findings"] if w["severity"] == "WARN"]
        all_warns += warns
        tag = res["verdict"].upper()
        print(f"  {p:10s} -> {tag}")
        if res["verdict"] == "fail":
            gate_fail = True
            for f in res["findings"]:
                if f["severity"] == "FAIL":
                    print(f"      [FAIL] {f['category']}: '{f['term']}' — {f['fix']}")
    # also gate the YouTube title
    if a.title:
        tres = lint_text(a.title)
        if tres["verdict"] == "fail":
            gate_fail = True
            print("  title      -> FAIL")
            for f in tres["findings"]:
                if f["severity"] == "FAIL":
                    print(f"      [FAIL] {f['category']}: '{f['term']}'")

    if gate_fail:
        sys.stderr.write("\nPUBLISH BLOCKED — a caption/title fails the communications discipline. "
                         "Reframe (mechanism, not forecast) and re-run.\n")
        sys.exit(2)
    if all_warns and a.strict:
        sys.stderr.write("\nPUBLISH BLOCKED (--strict) — warnings:\n  " + "\n  ".join(all_warns) + "\n")
        sys.exit(2)

    # ---- emit artifacts ------------------------------------------------------
    os.makedirs(a.outdir, exist_ok=True)
    media = [a.media] + ([a.thumb] if a.thumb else [])

    campaign = {"integrations": [f"<{PLATFORMS[p][0]}-id>" for p in platforms], "posts": []}
    for p in platforms:
        campaign["posts"].append({
            "provider": PLATFORMS[p][0],
            "post": [{"content": built[p], "image": [a.media]}],
            "settings": provider_settings(p, a.title, tags, a.ai_media),
        })
    camp_path = os.path.join(a.outdir, "campaign.json")
    json.dump(campaign, open(camp_path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    # human-readable caption preview
    prev = ["DGD publish preview — schedule: " + a.schedule,
            "sponsored: %s | ai-media: %s\n" % (a.sponsored, a.ai_media)]
    for p in platforms:
        prev += [f"===== {p.upper()} =====", built[p], ""]
    open(os.path.join(a.outdir, "captions.txt"), "w", encoding="utf-8").write("\n".join(prev))

    # metadata sidecar so the performance loop can auto-record (no manual entry)
    meta = {"schedule": a.schedule, "hook": a.hook, "topic": a.topic,
            "pillar": a.pillar, "format": a.format,
            "sponsored": a.sponsored, "ai_media": a.ai_media,
            "platforms": [{"platform": p, "identifier": PLATFORMS[p][0]} for p in platforms]}
    json.dump(meta, open(os.path.join(a.outdir, "post_meta.json"), "w", encoding="utf-8"), indent=2)

    # runnable publish.sh (uploads media, resolves integration IDs, schedules)
    sh = ['#!/usr/bin/env bash',
          'set -euo pipefail',
          '# Generated by dgd_publish.py — schedules the lint-passed post via Postiz.',
          '# Requires: postiz CLI installed + POSTIZ_API_KEY exported.',
          ': "${POSTIZ_API_KEY:?export POSTIZ_API_KEY first}"',
          f'SCHEDULE="{a.schedule}"',
          'echo "Uploading media…"',
          ': > "$(dirname "$0")/published.tsv"  # platform<TAB>post_id, for dgd_performance sync',
          f'VIDEO_URL=$(postiz upload "{a.media}" | jq -r .path)']
    if a.thumb:
        sh.append(f'THUMB_URL=$(postiz upload "{a.thumb}" | jq -r .path)')
    sh.append('echo "Resolving integration IDs…"')
    for p in platforms:
        ident = PLATFORMS[p][0]
        sh.append(f'{p.upper()}_ID=$(postiz integrations:list | jq -r \'.[]|select(.identifier=="{ident}").id\')')
    for p in platforms:
        ident = PLATFORMS[p][0]
        settings = json.dumps(provider_settings(p, a.title, tags, a.ai_media))
        capfile = f"{p}.txt"
        open(os.path.join(a.outdir, capfile), "w", encoding="utf-8").write(built[p])
        P = p.upper()
        sh += [f'echo "Scheduling {p}…"',
               f'OUT_{P}=$(postiz posts:create \\',
               f'  -c "$(cat "$(dirname "$0")/{capfile}")" \\',
               f'  -m "$VIDEO_URL" \\',
               f'  -s "$SCHEDULE" \\',
               f"  --settings '{settings}' \\",
               f'  -i "${P}_ID")',
               f'PID_{P}=$(echo "$OUT_{P}" | jq -r \'.id // .postId // (.[0].id) // empty\')',
               f'printf "%s\\t%s\\n" "{p}" "$PID_{P}" >> "$(dirname "$0")/published.tsv"',
               f'echo "  {p} -> post id: $PID_{P}"']
    sh.append('echo "Done. Verify in Postiz, then publish/approve as configured."')
    sh_path = os.path.join(a.outdir, "publish.sh")
    open(sh_path, "w", encoding="utf-8").write("\n".join(sh) + "\n")
    os.chmod(sh_path, 0o755)

    print(f"\nGATE PASSED. Wrote:\n  {camp_path}\n  {sh_path}\n  "
          + os.path.join(a.outdir, "captions.txt"))
    if all_warns:
        print("\nWARN (human confirm, not blocking):\n  " + "\n  ".join(all_warns))
    print("\nDry run: review captions.txt. To schedule: export POSTIZ_API_KEY=… && "
          f"bash {sh_path}")


if __name__ == "__main__":
    main()
