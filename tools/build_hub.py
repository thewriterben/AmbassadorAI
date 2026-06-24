#!/usr/bin/env python3
"""
build_hub.py - generate the DGD Ambassador Resource Hub (static, public).

A docs-style site built FROM the curated LLMWiki content, plus a client-side
**idea & prompt generator** that recombines the approved playbook (topics, hooks,
audiences, formats, and the wiki's prompt library) so every "Regenerate" yields a
fresh-but-compliant starting point. Server-rendered to one self-contained index.html.

Every generator building block is run through the compliance linter at BUILD time;
a FAIL aborts the build, so the generator can only ever emit safe content.

  python3 tools/build_hub.py            # -> site/
Requires (build-time): pip install markdown
"""
import argparse
import datetime as dt
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "LLMWiki")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compliance_lint as CL  # noqa: E402

SECTIONS = [
    ("How it works", [
        ("start/how-it-works.md", "How it all works \u2014 start here"),
        ("start/your-first-video.md", "Make your first video"),
        ("start/using-the-generator.md", "Using the idea generator"),
        ("start/what-the-rules-mean.md", "The rules, in plain English"),
        ("start/disclosures-explained.md", "Disclosures, explained"),
    ]),
    ("Start here", [
        ("dgd/dgd-overview.md", "What is Digital Gold?"),
        ("dgd/participation-pathways.md", "Ways to take part"),
    ]),
    ("What Digital Gold is", [
        ("dgd/approved-talking-points.md", "Approved talking points"),
        ("dgd/six-pillars.md", "The six pillars"),
        ("dgd/positioning-safe-harbor.md", "“Safe harbor” — the legal term"),
        ("dgd/supply-and-distribution.md", "Supply & distribution"),
        ("dgd/valuation-cfv-dgsb.md", "Valuation (CFV / DGSB)"),
        ("dgd/glossary.md", "Glossary"),
    ]),
    ("Make it land", [
        ("craft/hooks-library.md", "Hooks that work"),
        ("craft/viral-principles.md", "Viral principles"),
        ("craft/story-structures.md", "Story structures"),
        ("craft/positioning-and-audiences.md", "Positioning & audiences"),
        ("craft/platform-specs.md", "Platform specs"),
    ]),
    ("Stay compliant", [
        ("compliance/communications-discipline.md", "Communications discipline"),
        ("compliance/do-and-dont-language.md", "Do / Don’t language"),
        ("compliance/ftc-disclosure.md", "FTC / sponsorship disclosure"),
        ("compliance/ai-disclosure.md", "AI-media disclosure"),
        ("compliance/platform-policies.md", "Platform policies"),
        ("compliance/compliance-overview.md", "Compliance overview"),
    ]),
    ("Prompt library", [
        ("prompts/script-prompts.md", "Script prompts"),
        ("prompts/image-and-video-prompts.md", "Image & video prompts"),
        ("prompts/voiceover-prompts.md", "Voiceover prompts"),
    ]),
    ("Templates & series", [
        ("templates/video-brief-template.md", "Video brief template"),
        ("templates/pre-publish-checklist.md", "Pre-publish checklist"),
        ("templates/content-engine.md", "The content engine"),
        ("templates/content-calendar-and-series.md", "Content calendar & series"),
        ("templates/series-ideas.md", "Series ideas"),
        ("templates/six-pillars-series-scripts.md", "Six-pillars series scripts"),
        ("templates/positioning-series-scripts.md", "Positioning series scripts"),
    ]),
    ("Free AI toolkit", [
        ("tools/toolkit-overview.md", "The free AI toolkit"),
        ("tools/ideation-and-scripting.md", "Ideation & scripting"),
        ("tools/voiceover-tts.md", "Voiceover / TTS"),
        ("tools/video-generation.md", "Video generation"),
        ("tools/images-and-thumbnails.md", "Images & thumbnails"),
        ("tools/captions-and-editing.md", "Captions & editing"),
        ("tools/music-and-sound.md", "Music & sound"),
        ("tools/workflows.md", "End-to-end workflows"),
    ]),
]

# ----- generator pools (curated, grounded in the wiki, compliance-safe) -------
GEN = {
    "topics": [
        {"short": "scarcity", "Short": "Scarcity", "name": "Scarcity & sound money",
         "angle": "why a fixed, transparent supply behaves differently from money that can be printed",
         "question": "some money keeps its value and some doesn't",
         "myth": "scarcity alone makes something valuable", "motif": "scarcity"},
        {"short": "inflation", "Short": "Inflation", "name": "Inflation & debasement",
         "angle": "how purchasing power erodes when money is created faster than the goods behind it",
         "question": "your money covers a little less each year",
         "myth": "inflation just means prices go up", "motif": "erosion"},
        {"short": "decentralization", "Short": "Decentralization", "name": "Decentralization",
         "angle": "what it means for a network to run with no single point of control",
         "question": "no one is in charge yet it keeps working",
         "myth": "decentralized just means there are no rules", "motif": "network"},
        {"short": "monetary history", "Short": "Monetary history", "name": "Monetary history",
         "angle": "what past forms of money teach us about what makes money last",
         "question": "so many currencies have come and gone",
         "myth": "money has always looked the way it does now", "motif": "monetary-history"},
        {"short": "circulation", "Short": "Circulation", "name": "Supply & circulation",
         "angle": "how a coin is designed to move through an economy instead of sitting idle",
         "question": "money actually moves through an economy",
         "myth": "a coin's only job is to sit still", "motif": "supply-chain"},
        {"short": "the valuation method", "Short": "The valuation method", "name": "How it's valued",
         "angle": "the design-based way DGD's value is reasoned about - a method, not a forecast",
         "question": "you can reason about value from design alone",
         "myth": "value only comes from what people will pay later", "motif": "vault"},
        {"short": "what backs money", "Short": "What backs money", "name": "What backs a currency",
         "angle": "what actually gives a currency its value when nothing physical sits behind it",
         "question": "a piece of paper is worth anything at all",
         "myth": "money only means something if gold sits behind it", "motif": "vault"},
        {"short": "fixed rules", "Short": "Fixed rules", "name": "Fixed rules vs. a printer",
         "angle": "why a currency governed by transparent code behaves differently from one a committee can expand at will",
         "question": "who actually decides how much money exists",
         "myth": "someone has to be in charge of the money supply", "motif": "network"},
        {"short": "who gets new money first", "Short": "Who gets new money first", "name": "The Cantillon effect",
         "angle": "why it matters who receives newly created money before prices adjust",
         "question": "new money reaches some people sooner than others",
         "myth": "printing money lifts everyone equally", "motif": "supply-chain"},
        {"short": "money vs. currency", "Short": "Money vs. currency", "name": "Money vs. currency",
         "angle": "the difference between a unit you transact with and a system designed to hold its purchasing power",
         "question": "people use 'money' and 'currency' to mean different things",
         "myth": "money and currency are exactly the same thing", "motif": "monetary-history"},
        {"short": "good money vs. bad money", "Short": "Good money vs. bad money", "name": "Gresham's law",
         "angle": "why people tend to spend the weaker money and set the stronger money aside",
         "question": "the 'worse' money ends up circulating most",
         "myth": "the best money always wins automatically", "motif": "supply-chain"},
        {"short": "the cost of holding cash", "Short": "The cost of holding cash", "name": "The hidden cost of cash",
         "angle": "how sitting in a currency that expands over time quietly shrinks what it can do",
         "question": "doing nothing with cash still carries a cost",
         "myth": "cash just sits there with no downside", "motif": "erosion"},
        {"short": "competing currencies", "Short": "Competing currencies", "name": "Private currency (Hayek)",
         "angle": "the idea that currencies could compete the way products do, and what that would change",
         "question": "there could be more than one kind of money to choose from",
         "myth": "a country can only ever have one currency", "motif": "monetary-history"},
        {"short": "fees burned by design", "Short": "Fees burned by design", "name": "Fees burned by design",
         "angle": "why a system can remove units from circulation as a rule instead of paying them to anyone",
         "question": "no one actually collects the network's fees",
         "myth": "someone must be skimming a cut from every transaction", "motif": "vault"},
        {"short": "the shrinking per-person share", "Short": "The shrinking per-person share", "name": "The per-person share",
         "angle": "how coins released as the network grows are split among everyone, so each person's share gets smaller as more join",
         "question": "joining sooner doesn't simply mean ending up with more",
         "myth": "being there first automatically means a bigger slice forever", "motif": "scarcity"},
        {"short": "trust without a middleman", "Short": "Trust without a middleman", "name": "Trust without a middleman",
         "angle": "how a network can make people confident in a system without a bank or company vouching for it",
         "question": "strangers can rely on a system no single company runs",
         "myth": "you always need a trusted company in the middle", "motif": "network"},
        {"short": "what makes money last", "Short": "What makes money last", "name": "What makes money durable",
         "angle": "the properties - hard to fake, easy to verify, costly to expand - that let a money survive over time",
         "question": "some forms of money endure and others vanish",
         "myth": "any popular money will naturally last", "motif": "monetary-history"},
        {"short": "transparent rules", "Short": "Transparent rules", "name": "Transparency vs. discretion",
         "angle": "why being able to read and predict the rules can matter more than trusting a person to do the right thing",
         "question": "rules you can read beat promises you can't",
         "myth": "you just have to trust the people in charge to behave", "motif": "scarcity"},
    ],
    "hooks": [
        {"name": "Contrarian Claim", "tpl": "Most people misread ${short}. Here's the mechanism they miss."},
        {"name": "Mistake Warning", "tpl": "The biggest misunderstanding about ${short}? Let's clear it up in 60 seconds."},
        {"name": "List Tease", "tpl": "3 things about ${short} that quietly change how you see money."},
        {"name": "Question Hook", "tpl": "Ever wonder why ${question}? It's in the design."},
        {"name": "Story Open", "tpl": "Money has been reinvented many times. ${Short} is the chapter most people skip."},
        {"name": "Myth-bust", "tpl": "\"${myth}\" - not the whole story. Here's how ${short} really works."},
        {"name": "Then vs. Now", "tpl": "How people thought about ${short} a century ago vs. today."},
        {"name": "Analogy", "tpl": "${Short}, explained with something you already understand."},
        {"name": "Did You Know", "tpl": "Almost no one was ever taught this about ${short}."},
        {"name": "Reframe", "tpl": "You've been picturing ${short} wrong. Here's a cleaner mental model."},
        {"name": "Plain Truth", "tpl": "The honest version of ${short}, with nothing to sell."},
        {"name": "Common Trap", "tpl": "The trap most people fall into with ${short} - and how the design sidesteps it."},
        {"name": "Two Minutes", "tpl": "${Short} in two minutes - the part that finally clicks."},
        {"name": "If/Then", "tpl": "If you've ever wondered ${question}, this one's for you."},
    ],
    "audiences": ["the general public (new to all this)", "the crypto-curious",
                  "former 'degens' tired of the casino", "long-term savers worried about prices",
                  "people who find crypto confusing or off-putting", "students of economics and history"],
    "formats": ["Faceless explainer (~1 hr, no camera)", "Talking head + b-roll (most trust)",
                "Batch a week in a half-day", "One pillar per episode (a series)",
                "Quick myth-bust (under 30s)"],
    "platforms": ["TikTok", "Instagram Reels", "YouTube Shorts", "X"],
    "prompts": {
        "image": {
            "scarcity": [
                "A single gleaming gold coin on dark marble, dramatic rim light, a faint engraved grid suggesting a fixed supply limit, premium editorial product photography, gold and charcoal palette, vertical 9:16, no text",
                "A precise grid of identical gold tokens with one space deliberately left empty, top-down, dark slate background, soft directional light, minimalist editorial, gold and charcoal, vertical 9:16, no text"],
            "erosion": [
                "A stack of paper banknotes slowly dissolving into fine dust at the edges, dark moody background, conceptual finance illustration, amber light, vertical 9:16, no text",
                "A single banknote held up to warm light, its edges fraying into floating particles, deep shadow background, conceptual macro photography, amber and charcoal, vertical 9:16, no text"],
            "network": [
                "An abstract 3D network of thousands of softly glowing nodes connected by thin gold threads, dark navy void, a sense of vastness and no center, vertical 9:16, no text",
                "Aerial view of countless small points of warm light scattered edge to edge with faint gold threads between them, no point brighter than the rest, deep navy, vertical 9:16, no text"],
            "monetary-history": [
                "A classical engraving aesthetic of abstract statue busts and columns in a softly lit gallery, sepia and gold tones, editorial, vertical 9:16, no text",
                "A weathered stone ledger wall with abstract engraved tally marks fading left to right, museum lighting, sepia and gold, editorial still life, vertical 9:16, no text"],
            "supply-chain": [
                "Minimalist isometric scene: a glowing coin passing along a chain of simple icons - shop, truck, factory, raw materials - connected by a flowing gold line of light, dark background, vertical 9:16, no text",
                "A continuous looping gold ribbon weaving through simple geometric shapes representing a shop, a truck and a workshop, dark studio backdrop, isometric, premium, vertical 9:16, no text"],
            "vault": [
                "Slow reveal of a sleek modern vault door opening to a soft golden glow, minimal, premium, no logos, vertical 9:16, no text",
                "A polished circular vault dial in close-up, warm rim light catching the engraving, deep shadow, premium product photography, gold on charcoal, vertical 9:16, no text"],
        },
        "video": {
            "scarcity": [
                "Slow cinematic push-in on a single gold coin rotating on dark marble, dust particles drifting in a shaft of warm light, shallow depth of field, premium, 9:16",
                "Macro slow pan across a tight grid of gold tokens with one slot empty, dust drifting in a warm beam, shallow focus, premium, 9:16"],
            "erosion": [
                "A tall stack of banknotes slowly crumbling to dust from the top down, slow motion, moody dark studio, amber backlight, conceptual, 9:16",
                "A banknote dissolving particle by particle from one corner in slow motion, warm backlight, dark studio, conceptual, 9:16"],
            "network": [
                "Camera drifts through a 3D field of glowing nodes that light up one by one and connect with thin gold lines, dark navy space, calm and vast, 9:16",
                "A vast field of small lights gently pulsing in and out of sync, faint gold threads flickering between them, slow drift, deep navy, calm, 9:16"],
            "monetary-history": [
                "Slow pan across abstract classical busts and columns in a softly lit gallery, sepia and gold, dust motes in the light, 9:16",
                "Slow dolly along an engraved stone wall as tally marks fade in and out under museum light, sepia and gold, dust motes, 9:16"],
            "supply-chain": [
                "A glowing point of light travels along a continuous gold line through minimalist isometric icons (shop, truck, factory, mine), smooth motion, dark backdrop, 9:16",
                "A ribbon of light loops smoothly through simple shop, truck and workshop shapes in a continuous path, isometric, dark backdrop, 9:16"],
            "vault": [
                "Slow reveal of a sleek modern vault door opening to a soft golden glow, minimal, premium, no logos, 9:16",
                "Extreme close-up of a vault dial slowly turning, warm light sweeping across the engraving, deep shadow, premium, 9:16"],
        },
        "voiceover": [
            "Calm, curious, clear narrator. Conversational pace (~130 wpm for ~60s). Warm and measured - explainer, not hype. Define any jargon on first use. Label as an AI voice in the caption if synthetic.",
            "Friendly, plain-spoken narrator - like explaining to a smart friend over coffee. Short sentences, one idea per breath, jargon defined instantly. Steady pace, light warmth, zero hype. Add the AI-voice label in the caption if the voice is synthetic."],
        "script": [
            "Write a 45-60s educational script about ${angle}. Audience: ${audience}. Tone: calm, curious, clear. Rules: educational only - describe how the system is designed, not personal financial outcomes; keep it to mechanics; no price predictions; define jargon; end with a soft 'follow to learn more / read the white paper.' Structure: Hook -> Gap -> Payoff -> Loop. Deliver as a 4-column table: [Time] | [Spoken] | [On-screen text] | [Suggested visual].",
            "Draft a 60-second explainer on ${angle}. Audience: ${audience}. Open with a sharp hook, name the common misunderstanding, then walk the mechanics step by step with a simple visual for each beat. Keep it educational - how the design works, never personal financial outcomes; no price predictions; define jargon; close with 'follow for more / the white paper has the full picture.' Output a 4-column table: [Time] | [Spoken] | [On-screen] | [Visual]."],
    },
}
GEN_PANE = """<article class="doc gen" id="generate">
  <div class="crumb">Create</div>
  <h1>Idea &amp; prompt generator</h1>
  <p class="lead">Spin up a compliant starting point in one click. Everything here
    recombines the approved playbook — so every idea, hook, and prompt stays educational
    and on-message by construction. Hit regenerate for a fresh take, then copy it across
    to your editor or the local creator app.</p>
  <div class="gcard"><div class="grow"><h3>🎬 Video idea</h3><button class="rg" onclick="genIdea()">↻ Regenerate</button></div><div id="ideaOut"></div></div>
  <div class="gcard"><div class="grow"><h3>🪝 Hooks for a topic</h3><button class="rg" onclick="genHooks()">↻ New topic</button></div><div id="hookOut"></div></div>
  <div class="gcard"><div class="grow"><h3>✍️ Prompt set — image · video · voice · script</h3><button class="rg" onclick="genPrompt()">↻ Regenerate</button></div><div id="promptOut"></div></div>
</article>"""

FRONTMATTER = re.compile(r"^---\s*\n.*?\n---\s*\n", re.S)
DEAD_RE = re.compile(r'<a href="#" onclick="return false" class="dead">(.*?)</a>', re.S)


def docid(relpath):
    return os.path.splitext(os.path.basename(relpath))[0]


def strip_fm(text):
    return FRONTMATTER.sub("", text, count=1)


def rewrite_links(html, known):
    def repl(m):
        base = os.path.splitext(os.path.basename(m.group(1).split("#")[0]))[0]
        if base in known:
            return 'href="#%s"' % base
        return 'href="#" onclick="return false" class="dead"'
    return re.sub(r'href="([^"]+?\.md(?:#[^"]*)?)"', repl, html)


def gen_strings():
    """Every leaf string in GEN, for build-time compliance checking."""
    out = []
    for t in GEN["topics"]:
        out += [t["name"], t["angle"], t["short"], t["question"], t["myth"]]
    out += [h["tpl"] for h in GEN["hooks"]]
    out += GEN["audiences"] + GEN["formats"] + GEN["platforms"]
    for d in (GEN["prompts"]["image"], GEN["prompts"]["video"]):
        for v in d.values():
            out += v
    out += GEN["prompts"]["voiceover"] + GEN["prompts"]["script"]
    return out


def build(out_dir):
    try:
        import markdown
    except ImportError:
        sys.exit("This build needs the 'markdown' package:  pip install markdown")

    # compliance gate on every generator building block (fail-closed)
    bad = [s for s in gen_strings() if CL.lint_text(s)["verdict"] == "fail"]
    if bad:
        sys.exit("BUILD BLOCKED — generator pool has non-compliant text:\n  "
                 + "\n  ".join(bad))

    known = {docid(rp) for _, items in SECTIONS for rp, _ in items}
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list"])

    nav_html = ['<div class="navgroup">Create</div>',
                '<a class="navlink" data-doc="generate" href="#generate">Idea &amp; prompt generator</a>']
    docs_html = []
    for group, items in SECTIONS:
        nav_html.append('<div class="navgroup">%s</div>' % group)
        for relpath, title in items:
            did = docid(relpath)
            full = os.path.join(WIKI, relpath)
            if not os.path.exists(full):
                continue
            md.reset()
            body = rewrite_links(md.convert(strip_fm(open(full, encoding="utf-8").read())), known)
            body = DEAD_RE.sub(r'<span class="dead">\1</span>', body)
            nav_html.append('<a class="navlink" data-doc="%s" href="#%s">%s</a>' % (did, did, title))
            docs_html.append('<article class="doc" id="%s"><div class="crumb">%s</div>%s</article>'
                             % (did, group, body))

    home = """<article class="doc home" id="home">
      <div class="sub">Digital Gold · Ambassador Resource Hub</div>
      <h1>Make compliant, educational Digital&nbsp;Gold videos.</h1>
      <p class="lead">Everything an ambassador needs in one place — what you can say, how to
        make it land, the disclosure rules, ready-to-use templates, and a free AI toolkit.
        New here? Start below, or spin up an idea with the generator.</p>
      <div class="prime"><strong>The one rule everything follows:</strong> DGD content is
        <em>educational, not promotional, and never financial advice.</em> Describe how the
        system is designed to work — never how someone will profit. When in doubt, read
        <a href="#communications-discipline">the communications discipline</a>.</div>
      <div class="cards">
        <a class="hcard" href="#generate"><b>⚡ Generate an idea</b><span>Topic, hook, format, prompts — one click.</span></a>
        <a class="hcard" href="#how-it-works"><b>New here? Start here</b><span>How it all works, in 5 steps.</span></a>
        <a class="hcard" href="#approved-talking-points"><b>What can I say?</b><span>Approved, safe talking points.</span></a>
        <a class="hcard" href="#hooks-library"><b>Stop the scroll</b><span>Hooks that work, compliantly.</span></a>
        <a class="hcard" href="#do-and-dont-language"><b>Do / Don’t</b><span>The phrase cheat-sheet.</span></a>
        <a class="hcard" href="#pre-publish-checklist"><b>Before you post</b><span>The pre-publish checklist.</span></a>
      </div>
    </article>"""

    html = (TEMPLATE
            .replace("__NAV__", "\n".join(nav_html))
            .replace("__DOCS__", home + "\n" + GEN_PANE + "\n" + "\n".join(docs_html))
            .replace("__GENDATA__", json.dumps(GEN, ensure_ascii=False))
            .replace("__BUILT__", dt.date.today().isoformat()))
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8").write(html)
    n = sum(len(items) for _, items in SECTIONS)
    print("built ambassador hub -> %s/index.html  (%d docs + generator, %d sections)"
          % (out_dir, n, len(SECTIONS)))
    print("  preview:  python3 -m http.server -d %s 8000  ->  http://localhost:8000" % out_dir)


TEMPLATE = r"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DGD Ambassador Resource Hub</title>
<style>
:root{--navy:#10172a;--char:#0b0e16;--panel:#0e1626;--gold:#d4a853;--goldhi:#f0d082;
--white:#f4f4f0;--mute:#9aa3b8;--line:rgba(255,255,255,.09);--maxw:820px}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--char);color:var(--white);
font-family:'Segoe UI',system-ui,-apple-system,Arial,sans-serif;line-height:1.6}
a{color:var(--gold);text-decoration:none}a:hover{text-decoration:underline}
.layout{display:flex;min-height:100vh}
aside{width:288px;flex:none;background:var(--panel);border-right:1px solid var(--line);
position:sticky;top:0;height:100vh;overflow-y:auto;padding:20px 16px}
aside .brand{font-family:Georgia,serif;font-size:18px;color:var(--white);padding:0 8px 4px}
aside .brand b{color:var(--gold)}
.search{width:100%;margin:12px 0 8px;background:rgba(0,0,0,.3);border:1px solid var(--line);
color:var(--white);border-radius:9px;padding:9px 12px;font-size:14px}
.navgroup{color:var(--gold);font-size:11px;letter-spacing:.08em;text-transform:uppercase;
font-weight:700;margin:16px 8px 6px}
.navlink{display:block;padding:7px 10px;border-radius:8px;color:var(--white);font-size:14.5px}
.navlink:hover{background:rgba(255,255,255,.05);text-decoration:none}
.navlink.active{background:var(--gold);color:#1a1205;font-weight:700}
main{flex:1;min-width:0;display:flex;justify-content:center;padding:40px 32px 80px}
.content{width:100%;max-width:var(--maxw)}
.doc{display:none;animation:fade .2s ease}.doc.active{display:block}
@keyframes fade{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
.crumb{color:var(--gold);font-size:11px;letter-spacing:.07em;text-transform:uppercase;font-weight:700;margin-bottom:10px}
.doc h1{font-family:Georgia,serif;font-size:30px;line-height:1.25;margin:.2em 0 .5em}
.doc h2{font-family:Georgia,serif;font-size:22px;margin:1.4em 0 .5em;padding-top:.3em;border-top:1px solid var(--line)}
.doc h3{font-size:16px;color:var(--goldhi);margin:1.2em 0 .4em}
.doc p,.doc li{font-size:15.5px}.doc strong{color:#fff}
.doc table{width:100%;border-collapse:collapse;margin:14px 0;font-size:14px}
.doc th,.doc td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
.doc th{background:rgba(212,168,83,.12);color:var(--goldhi)}
.doc code{background:rgba(255,255,255,.08);padding:1px 6px;border-radius:5px;font-size:13.5px}
.doc pre{background:#06080e;border:1px solid var(--line);border-radius:10px;padding:14px;overflow:auto}
.doc pre code{background:none;padding:0}
.doc blockquote{border-left:3px solid var(--gold);margin:14px 0;padding:4px 16px;color:var(--mute);background:rgba(212,168,83,.05)}
.doc hr{border:0;border-top:1px solid var(--line);margin:22px 0}
.dead{color:var(--mute);cursor:default}
.home .sub,.gen .crumb{color:var(--gold);font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:12px}
.home h1{font-size:38px;margin:.1em 0 .3em}.lead{color:var(--mute);font-size:17px;max-width:64ch}
.prime{background:rgba(212,168,83,.08);border:1px solid rgba(212,168,83,.3);border-radius:12px;padding:16px 18px;margin:22px 0}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px;margin-top:8px}
.hcard{display:block;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.hcard:hover{border-color:var(--gold);text-decoration:none}.hcard b{display:block;color:var(--white)}
.hcard span{color:var(--mute);font-size:13.5px}
.foot{color:var(--mute);font-size:12px;margin-top:30px;border-top:1px solid var(--line);padding-top:14px}
/* generator */
.gcard{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:16px 0}
.grow{display:flex;align-items:center;justify-content:space-between;gap:12px}
.gcard h3{margin:0;color:var(--goldhi);font-size:15px}
.rg{background:var(--gold);color:#1a1205;border:none;border-radius:8px;padding:7px 14px;font-weight:700;cursor:pointer;font-size:13px}
.rg:hover{background:var(--goldhi)}
.kv{display:flex;gap:12px;padding:6px 0;border-bottom:1px dashed var(--line);font-size:15px}
.kv b{color:var(--gold);min-width:108px;flex:none;font-weight:600}.kv i{color:var(--mute)}
.hk{padding:8px 0;border-bottom:1px dashed var(--line);font-size:15px}
.tag{display:inline-block;background:rgba(212,168,83,.15);color:var(--goldhi);font-size:11px;font-weight:700;
border-radius:20px;padding:2px 9px;margin-right:8px}
.pb{margin:10px 0}.pbh{color:var(--gold);font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:4px}
.pb pre{background:#06080e;border:1px solid var(--line);border-radius:9px;padding:11px;white-space:pre-wrap;font-size:13px;margin:0}
.copy{margin-top:12px;background:transparent;border:1px solid var(--gold);color:var(--gold);border-radius:8px;padding:6px 14px;cursor:pointer;font-size:13px}
.copy:hover{background:rgba(212,168,83,.12)}
#toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:var(--gold);color:#1a1205;
font-weight:700;padding:9px 18px;border-radius:24px;opacity:0;transition:opacity .2s;pointer-events:none;z-index:50}
#toast.show{opacity:1}
.menubtn{display:none}
@media(max-width:820px){aside{position:fixed;left:-300px;z-index:20;transition:left .2s;box-shadow:0 0 40px #000}
aside.open{left:0}.menubtn{display:inline-block;position:fixed;top:12px;left:12px;z-index:30;
background:var(--gold);color:#1a1205;border:none;border-radius:8px;padding:8px 12px;font-weight:700}
main{padding-top:60px}.kv{flex-direction:column;gap:2px}.kv b{min-width:0}}
.noresult{color:var(--mute);padding:10px;font-size:13px;display:none}
</style></head><body>
<button class="menubtn" onclick="document.querySelector('aside').classList.toggle('open')">☰ Menu</button>
<div class="layout">
<aside>
  <div class="brand"><b>DGD</b> Ambassador Hub</div>
  <input class="search" id="q" placeholder="Search topics…" autocomplete="off">
  <a class="navlink" data-doc="home" href="#home">Home</a>
  __NAV__
  <div class="noresult" id="nores">No topic matches.</div>
</aside>
<main><div class="content">
  __DOCS__
  <div class="foot">Educational, not financial advice. Built from the DGD Ambassador Wiki ·
    last updated __BUILT__. Mechanism, not forecast.</div>
</div></main>
</div>
<div id="toast"></div>
<script>
const docs=[...document.querySelectorAll('.doc')], links=[...document.querySelectorAll('.navlink')];
function show(id){ if(!document.getElementById(id)) id='home';
  docs.forEach(d=>d.classList.toggle('active',d.id===id));
  links.forEach(l=>l.classList.toggle('active',l.dataset.doc===id));
  window.scrollTo(0,0); document.querySelector('aside').classList.remove('open');}
function route(){ show((location.hash||'#home').slice(1)); }
window.addEventListener('hashchange',route);
const q=document.getElementById('q'), nores=document.getElementById('nores'),
      groups=[...document.querySelectorAll('.navgroup')];
q.addEventListener('input',()=>{ const t=q.value.trim().toLowerCase(); let any=false;
  links.forEach(l=>{ if(l.dataset.doc==='home'){l.style.display=t?'none':'';return;}
    const hit=l.textContent.toLowerCase().includes(t); l.style.display=hit?'':'none'; if(hit)any=true;});
  groups.forEach(g=>{ let n=g.nextElementSibling, vis=false;
    while(n&&!n.classList.contains('navgroup')){ if(n.classList.contains('navlink')&&n.style.display!=='none')vis=true; n=n.nextElementSibling;}
    g.style.display=vis?'':'none';});
  nores.style.display=any?'none':'block';});

/* ---- idea & prompt generator ---- */
const GEN = __GENDATA__;
const pick = a => a[Math.floor(Math.random()*a.length)];
const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
function fillHook(tpl,t){ return tpl.replace(/\$\{short\}/g,t.short).replace(/\$\{Short\}/g,t.Short)
  .replace(/\$\{question\}/g,t.question).replace(/\$\{myth\}/g,t.myth); }
let toastT;
function copy(text){ navigator.clipboard.writeText(text).then(()=>{ const el=document.getElementById('toast');
  el.textContent='Copied'; el.classList.add('show'); clearTimeout(toastT); toastT=setTimeout(()=>el.classList.remove('show'),1200);}); }
function genIdea(){ const t=pick(GEN.topics),h=pick(GEN.hooks),a=pick(GEN.audiences),f=pick(GEN.formats),p=pick(GEN.platforms);
  const hook=fillHook(h.tpl,t);
  window._idea=`Topic: ${t.name}\nAngle: ${t.angle}\nHook (${h.name}): ${hook}\nAudience: ${a}\nFormat: ${f}\nPlatform: ${p}\nB-roll motif: ${t.motif}\n\nKeep it educational — mechanism, not forecast. End with a soft "follow / read the white paper."`;
  document.getElementById('ideaOut').innerHTML=
    `<div class="kv"><b>Topic</b><span>${t.name}</span></div>
     <div class="kv"><b>Angle</b><span>${t.angle}</span></div>
     <div class="kv"><b>Hook</b><span>“${esc(hook)}” <i>(${h.name})</i></span></div>
     <div class="kv"><b>Audience</b><span>${a}</span></div>
     <div class="kv"><b>Format</b><span>${f}</span></div>
     <div class="kv"><b>Platform</b><span>${p}</span></div>
     <div class="kv"><b>B-roll motif</b><span>${t.motif}</span></div>
     <button class="copy" onclick="copy(window._idea)">Copy brief</button>`;
}
function genHooks(){ const t=pick(GEN.topics);
  const items=GEN.hooks.map(h=>({n:h.name,txt:fillHook(h.tpl,t)}));
  window._hooks=`Hooks for ${t.name}:\n`+items.map(i=>`• [${i.n}] ${i.txt}`).join('\n');
  document.getElementById('hookOut').innerHTML=
    `<div class="kv"><b>Topic</b><span>${t.name}</span></div>`+
    items.map(i=>`<div class="hk"><span class="tag">${i.n}</span>${esc(i.txt)}</div>`).join('')+
    `<button class="copy" onclick="copy(window._hooks)">Copy all</button>`;
}
function pb(label,text){ return `<div class="pb"><div class="pbh">${label}</div><pre>${esc(text)}</pre></div>`; }
function genPrompt(){ const t=pick(GEN.topics),a=pick(GEN.audiences);
  const img=pick(GEN.prompts.image[t.motif]), vid=pick(GEN.prompts.video[t.motif]), vo=pick(GEN.prompts.voiceover);
  const sc=pick(GEN.prompts.script).replace(/\$\{angle\}/g,t.angle).replace(/\$\{audience\}/g,a);
  window._prompts=`Topic: ${t.name}\n\nIMAGE PROMPT\n${img}\n\nVIDEO PROMPT\n${vid}\n\nVOICEOVER\n${vo}\n\nSCRIPT PROMPT\n${sc}`;
  document.getElementById('promptOut').innerHTML=
    `<div class="kv"><b>Topic</b><span>${t.name} → motif: ${t.motif}</span></div>`+
    pb('Image prompt',img)+pb('Video prompt',vid)+pb('Voiceover',vo)+pb('Script prompt',sc)+
    `<button class="copy" onclick="copy(window._prompts)">Copy all</button>`;
}
genIdea(); genHooks(); genPrompt(); route();
</script></body></html>"""


def main():
    ap = argparse.ArgumentParser(description="Build the DGD Ambassador Resource Hub")
    ap.add_argument("--out", default=os.path.join(ROOT, "site"))
    build(ap.parse_args().out)


if __name__ == "__main__":
    main()
