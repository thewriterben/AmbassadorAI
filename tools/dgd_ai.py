#!/usr/bin/env python3
"""
dgd_ai.py - true AI generation for DGD content, wrapped in the compliance rails.

The combinatorial generator on the public hub recombines an approved playbook. This is
the open-ended counterpart: it asks a real LLM to write fresh scripts / ideas / hooks /
captions — then runs the model's output through the SAME deterministic compliance linter,
fail-closed, with one automatic retry that feeds the violations back. The model drafts;
the rails decide what's allowed. It belongs in the LOCAL creator tools, never the public
static site (it needs a model + API key).

Provider: whichever key is set — ANTHROPIC_API_KEY (preferred) or OPENAI_API_KEY.
No SDK required (stdlib urllib). Override the model with DGD_AI_MODEL.

  python3 tools/dgd_ai.py script  --brief "why money loses value" --audience "general public"
  python3 tools/dgd_ai.py ideas   --brief "the six pillars"
  python3 tools/dgd_ai.py hooks   --brief "decentralization"
  python3 tools/dgd_ai.py caption --brief "inflation, for TikTok"

Exit 0 if the gated result is clean/warn, 2 if it still fails the rails after retry.
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compliance_lint as CL  # noqa: E402

SYSTEM = """You write EDUCATIONAL short-form video content for Digital Gold (DGD) ambassadors.

ABSOLUTE RULES — never violate, in any field (spoken, on-screen text, captions, hashtags):
- Educational, never promotional. Never financial advice.
- Never call DGD an investment, asset to hold, store of value, or portfolio item.
- Never predict, project, or imply a price. The price curve is a DISTRIBUTION MECHANISM, not a forecast.
- Never promise or imply returns, profit, gains, passive income, or that anyone will be financially better off.
- Never solicit: no "buy", "get in", "don't miss out", "ape in", "secure your bag", "100x", "moon", "pump".
- "Safe harbor" is ONLY a legal term (designed to qualify as a digital commodity, not a security). Never use it to mean a safe place for money.
- Degen lingo (rekt, casino) may be used ONLY to hook attention and contrast DGD as the anti-speculation coin — never to imply gains.
- Describe HOW THE SYSTEM IS DESIGNED TO WORK, never how someone profits. Mechanism, not forecast.
- Define jargon on first use. Tone: calm, curious, clear — explainer, not hype.
- Do not invent figures. If a number is needed, write [WP: figure] for the ambassador to source from the white paper.
- End with a soft call to action: "follow to learn more" or "read the white paper" — never "buy".

The gut check for everything you write: if a viewer never acquires a single coin, is this still a useful, honest, educational video? If not, rewrite it.
Output ONLY the requested deliverable, no preamble."""

PROMPTS = {
    "script": ("Write a 45–60 second educational script about: {brief}. Audience: {audience}. "
               "Deliver a 4-column Markdown table with header row exactly: "
               "Time | Spoken | On-screen text | Suggested visual. "
               "Use the structure Hook → Gap → Payoff → Loop across the rows. "
               "After the table, add one line starting 'CAPTION:' with a platform caption that "
               "ends 'Not financial advice. Educational.'"),
    "ideas": ("Generate 5 distinct, scroll-stopping video IDEAS about: {brief}. Audience: {audience}. "
              "For each, give: a one-line topic, the single takeaway, a hook line, and a suggested "
              "abstract b-roll visual. Number them 1–5."),
    "hooks": ("Write 8 distinct, scroll-stopping, compliance-safe HOOK lines (first 3 seconds) for a "
              "short video about: {brief}. One per line, no numbering."),
    "caption": ("Write a social caption for a short video about: {brief}. Audience: {audience}. "
                "Keep it under 280 characters so it fits X. Front-load any disclosure. "
                "End with 'Not financial advice. Educational.' Add 3–5 relevant hashtags."),
}


def _http_json(url, headers, payload, timeout=60):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                headers={**headers, "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def call_llm(system, user):
    """Return (text, provider). Raises RuntimeError if no key / on API error."""
    ak, ok = os.environ.get("ANTHROPIC_API_KEY"), os.environ.get("OPENAI_API_KEY")
    try:
        if ak:
            model = os.environ.get("DGD_AI_MODEL", "claude-sonnet-4-6")
            data = _http_json("https://api.anthropic.com/v1/messages",
                              {"x-api-key": ak, "anthropic-version": "2023-06-01"},
                              {"model": model, "max_tokens": 1200, "system": system,
                               "messages": [{"role": "user", "content": user}]})
            return "".join(b.get("text", "") for b in data.get("content", [])), f"anthropic:{model}"
        if ok:
            model = os.environ.get("DGD_AI_MODEL", "gpt-4o-mini")
            data = _http_json("https://api.openai.com/v1/chat/completions",
                              {"authorization": f"Bearer {ok}"},
                              {"model": model, "max_tokens": 1200,
                               "messages": [{"role": "system", "content": system},
                                            {"role": "user", "content": user}]})
            return data["choices"][0]["message"]["content"], f"openai:{model}"
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"LLM API error {e.code}: {e.read().decode()[:200]}")
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(f"LLM call failed: {e}")
    raise RuntimeError("No LLM key set. Export ANTHROPIC_API_KEY or OPENAI_API_KEY.")


def generate(kind, brief, audience="the general public", retries=1):
    """Draft with the LLM, then gate fail-closed with one feedback retry."""
    if kind not in PROMPTS:
        raise ValueError(f"unknown kind '{kind}'; choose: {', '.join(PROMPTS)}")
    user = PROMPTS[kind].format(brief=brief, audience=audience)
    notes, text, res = "", "", {"findings": []}
    for attempt in range(retries + 1):
        text, provider = call_llm(SYSTEM, user + notes)
        res = CL.lint_text(text)
        if res["verdict"] != "fail":
            return {"text": text, "verdict": res["verdict"], "findings": res["findings"],
                    "attempts": attempt + 1, "provider": provider}
        terms = sorted({f["term"] for f in res["findings"] if f["severity"] == "FAIL"})
        notes = ("\n\nYOUR PREVIOUS DRAFT BROKE THE RULES with these banned terms: "
                 f"{', '.join(terms)}. Rewrite completely, removing every one of them, "
                 "reframing to mechanism (how the system is designed) not forecast. Same format.")
    return {"text": text, "verdict": "fail", "findings": res["findings"],
            "attempts": retries + 1, "provider": provider}


def main():
    ap = argparse.ArgumentParser(description="AI generation for DGD, compliance-gated")
    ap.add_argument("kind", choices=list(PROMPTS))
    ap.add_argument("--brief", required=True)
    ap.add_argument("--audience", default="the general public")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    try:
        r = generate(a.kind, a.brief, a.audience)
    except RuntimeError as e:
        sys.exit(str(e))
    if a.json:
        print(json.dumps(r, indent=2))
    else:
        print(r["text"])
        print(f"\n— {r['verdict'].upper()} · {r['provider']} · {r['attempts']} attempt(s)")
        if r["verdict"] == "fail":
            sys.stderr.write("WARNING: still failed the rails after retry — do not publish as-is.\n")
    sys.exit(2 if r["verdict"] == "fail" else 0)


if __name__ == "__main__":
    main()
