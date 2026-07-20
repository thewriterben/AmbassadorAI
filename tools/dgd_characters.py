#!/usr/bin/env python3
"""
dgd_characters.py - character assistance for DGD Video Studio.

Three jobs, all of them fail-closed:

  1. PICK       match a character to a subject / mood / audience / intent
  2. GATE       block IP-unsafe usage before it reaches a render or a prompt
  3. LOCK       keep a character IDENTICAL across many videos

The consistency problem is the same one the coin has: a generator invents a
slightly different character every time, and a viewer who sees three different
"hosts" concludes the channel is slop. The fix is the same shape - a canonical,
verbatim description block plus a fixed seed, hashed so drift is detectable.

  python3 dgd_characters.py suggest --subject "why money loses value" --audience general
  python3 dgd_characters.py show tortoise-and-hare
  python3 dgd_characters.py new  --name "Assay" --role "a careful assayer" --out cast/assay.json
  python3 dgd_characters.py lock cast/assay.json
  python3 dgd_characters.py prompt cast/assay.json --shot "explaining a supply schedule"
  python3 dgd_characters.py gate --id mickey-mouse --jurisdiction US

ORIGINAL CHARACTERS ARE THE DEFAULT PATH. They carry no trademark exposure, are
fully brand-controllable, and are easier to keep consistent because you own the
design. Public-domain characters are available, gated, and always a trade.

Exit codes: 0 clear (or clear-with-warnings), 2 BLOCKED.
"""
import argparse
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REGISTRY = os.path.join(HERE, "characters.json")

sys.path.insert(0, HERE)
try:
    import compliance_lint as CL
except Exception:
    CL = None

# Trademarked design elements that must never appear in a description or prompt.
# This is the mechanical half of the gate - it catches the specific mistakes
# people actually make, regardless of which character they claim to be using.
TRAP_PHRASES = [
    (r"\bruby slipper", "MGM's ruby slippers - in Baum's books they are SILVER"),
    (r"\bneck bolt|\bflat[- ]head(ed)?\b.*\bmonster|\bgreen[- ]skinned?\b.*\b(monster|creature)",
     "Universal's 1931 Frankenstein design - the novel's Creature is articulate and yellow-skinned"),
    (r"\bred shirt\b.*\b(pooh|bear)|\b(pooh|bear)\b.*\bred shirt\b",
     "Disney's red-shirt Pooh - Shepard's original illustrations have no shirt"),
    (r"\bspinach\b.*\b(strength|strong|power)|\b(strength|power)\b.*\bspinach\b",
     "Popeye's spinach strength is from 1931 and is NOT public domain"),
    (r"\bwhite glove\b.*\bmouse|\bmouse\b.*\bwhite glove", "Disney's modern Mickey design"),
    (r"\bprincess aurora\b|\bbriar rose\b", "Disney trademarks for Sleeping Beauty"),
    (r"\b(sneezy|bashful|dopey|grumpy|happy|sleepy|doc)\b.*\bdwarf|\bdwarf\b.*\b(sneezy|bashful|dopey)\b",
     "Disney's dwarf names are trademarked"),
    (r"\bdeerstalker\b.*\bcalabash\b", "stage/illustrator additions to Holmes, not Doyle - check modern designs"),
    (r"\bemerald city\b.*\b(film|movie|1939)", "MGM's Emerald City design"),
]

# A character must never appear to endorse. This is the DGD rail, applied to
# people rather than words - a recognisable figure recommending a coin reads as
# an endorsement no matter how the script is worded.
ENDORSEMENT_PATTERNS = [
    (r"\b(endorse|endorsing|endorsement|recommends?|recommending)\b", "character appears to endorse"),
    (r"\b(vouch(es|ing)?|approves?|backs?|supports?)\b\s+(dgd|digital gold|the coin)",
     "character appears to vouch for DGD"),
    (r"\b(tells?|urges?|advises?)\b.*\b(you|viewers?|everyone)\b.*\b(buy|get|acquire|hold)\b",
     "character soliciting acquisition"),
    (r"\bofficial\b.*\b(mascot|spokes|ambassador)\b.*\b(disney|marvel|universal|mgm)\b",
     "implies affiliation with a rights-holder"),
]


def load_registry():
    with open(REGISTRY, encoding="utf-8") as f:
        return json.load(f)


def find(reg, cid):
    for c in reg["characters"]:
        if c["id"] == cid:
            return c
    return None


# ------------------------------------------------------------------ gate ----
def scan_text(*texts):
    """Mechanical scan for trademarked design elements and endorsement framing."""
    trap_hits, endorse_hits = [], []
    for t in texts:
        if not t:
            continue
        low = t.lower()
        for pat, why in TRAP_PHRASES:
            if re.search(pat, low):
                trap_hits.append((why, t))
        for pat, why in ENDORSEMENT_PATTERNS:
            if re.search(pat, low):
                endorse_hits.append((why, t))
    return trap_hits, endorse_hits


def gate(character, jurisdiction="US", ack_version=False, cleared=False, text=None):
    """Fail-closed IP + endorsement gate. Returns (ok, findings)."""
    f = []
    tier = character["tier"]
    status = character.get("jurisdictions", {}).get(jurisdiction, "check")

    if status == "blocked":
        f.append(("BLOCK", f"{character['name']} is NOT public domain in {jurisdiction}."))
    elif status == "check":
        f.append(("BLOCK", f"Status in {jurisdiction} is unverified. Verify before use, "
                           f"or pick a folklore-tier character with no jurisdiction problem."))

    if tier == "high-risk" and not cleared:
        f.append(("BLOCK", f"{character['name']} is actively trademarked by a living "
                           f"rights-holder. Using it in crypto content is the exact fact "
                           f"pattern these holders litigate. Requires --i-have-legal-clearance."))

    if tier in ("version-locked", "jurisdiction-locked") and not ack_version:
        f.append(("BLOCK", f"{character['name']} is only usable in one specific version. "
                           f"Re-run with --ack-version once you have read: "
                           f"\"{character['safe_version']}\""))

    if tier == "folklore":
        f.append(("OK", "Folklore tier - no copyright ever attached. Lowest-risk option."))
    elif tier == "expired" and status == "clear":
        f.append(("OK", f"Copyright expired and clear in {jurisdiction}."))

    for t in character.get("traps", []):
        f.append(("WARN", t))

    if text:
        traps, endorse = scan_text(text)
        for why, src in traps:
            f.append(("BLOCK", f"Trademarked design element in your text: {why}"))
        for why, src in endorse:
            f.append(("BLOCK", f"Endorsement framing: {why}"))

    ok = not any(lvl == "BLOCK" for lvl, _ in f)
    return ok, f


def print_findings(findings):
    icon = {"OK": "  OK  ", "WARN": " WARN ", "BLOCK": "BLOCK "}
    for lvl, msg in findings:
        print(f"[{icon[lvl]}] {msg}")


# ---------------------------------------------------------------- suggest ---
def suggest(reg, subject="", mood="", audience="", intent="", jurisdiction="US", limit=5):
    """Rank characters against the brief. Safety is part of the score, not a filter
    applied afterwards - a risky character has to be much better to win."""
    terms = " ".join([subject, mood, intent]).lower()
    words = set(re.findall(r"[a-z]{4,}", terms))
    tier_bonus = {"folklore": 5.0, "expired": 3.0,
                  "version-locked": -2.0, "jurisdiction-locked": -6.0, "high-risk": -12.0}
    rows = []
    for c in reg["characters"]:
        score = tier_bonus.get(c["tier"], 0)
        hay = " ".join(c["themes"] + c["tone"] + c["intent"] +
                       [c.get("dgd_fit", "")]).lower()
        hay_words = set(re.findall(r"[a-z]{4,}", hay))
        score += 3.0 * len(words & hay_words)
        for w in words:
            if w in hay:
                score += 1.0
        if audience and audience.lower() in [a.lower() for a in c.get("audience", [])]:
            score += 2.0
        if mood and mood.lower() in [t.lower() for t in c["tone"]]:
            score += 3.0
        if intent and intent.lower() in [i.lower() for i in c["intent"]]:
            score += 3.0
        if c.get("jurisdictions", {}).get(jurisdiction) == "blocked":
            score -= 20.0
        rows.append((score, c))
    rows.sort(key=lambda r: -r[0])
    return rows[:limit]


# ------------------------------------------------------------------ lock ----
LOCK_FIELDS = ("name", "role", "look", "wardrobe", "palette", "voice", "manner", "seed")


def lock_hash(sheet):
    """Hash the identity fields only. Changing any of them means the character
    has DRIFTED from earlier videos - that is what the lock detects."""
    blob = " ".join(str(sheet.get(k, "")).strip().lower() for k in LOCK_FIELDS)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:12]


def new_sheet(name, role, base=None, seed=None, look="", wardrobe="", palette="",
              voice="", manner=""):
    sheet = {
        "schema": 1,
        "name": name,
        "role": role,
        "base": base or "original",
        "look": look or "TODO - one sentence, physical, unchanging",
        "wardrobe": wardrobe or "TODO - the silhouette a viewer recognises",
        "palette": palette or "gold #D4A853, deep navy #101728, warm white #F4F4F0",
        "voice": voice or "TODO - how they sound",
        "manner": manner or "TODO - how they behave on camera",
        "seed": seed if seed is not None else abs(hash(name)) % 100000,
        "negative": [],
        "notes": "",
    }
    sheet["lock"] = lock_hash(sheet)
    return sheet


def build_prompt(sheet, shot="", style="editorial, gold and deep navy, clean, premium"):
    """The canonical block. Paste it VERBATIM into every generation, every time -
    that verbatim reuse is what produces consistency."""
    neg = list(sheet.get("negative", []))
    neg += ["no logos", "no brand marks", "no text", "no price charts",
            "no stacks of coins", "no rocket or casino imagery"]
    lines = [
        f"CHARACTER (do not vary - lock {sheet['lock']}):",
        f"  {sheet['name']}, {sheet['role']}.",
        f"  Look: {sheet['look']}",
        f"  Wardrobe: {sheet['wardrobe']}",
        f"  Palette: {sheet['palette']}",
        f"  Manner: {sheet['manner']}",
        "",
        f"SHOT: {shot}" if shot else "SHOT: neutral three-quarter portrait, calm expression",
        f"STYLE: {style}, vertical 9:16",
        f"SEED: {sheet['seed']}  (reuse this seed in every render)",
        "NEGATIVE: " + ", ".join(neg),
    ]
    return "\n".join(lines)


# ------------------------------------------------------------------ main ----
def main(argv=None):
    p = argparse.ArgumentParser(description="DGD character assistant")
    sub = p.add_subparsers(dest="cmd", required=True)

    sg = sub.add_parser("suggest", help="match a character to the brief")
    sg.add_argument("--subject", default="")
    sg.add_argument("--mood", default="")
    sg.add_argument("--audience", default="")
    sg.add_argument("--intent", default="")
    sg.add_argument("--jurisdiction", default="US")
    sg.add_argument("--limit", type=int, default=5)

    sh = sub.add_parser("show", help="full record incl. traps")
    sh.add_argument("id")
    sh.add_argument("--jurisdiction", default="US")

    ls = sub.add_parser("list", help="the roster")
    ls.add_argument("--tier")

    gt = sub.add_parser("gate", help="fail-closed IP + endorsement check")
    gt.add_argument("--id", required=True)
    gt.add_argument("--jurisdiction", default="US")
    gt.add_argument("--ack-version", action="store_true")
    gt.add_argument("--i-have-legal-clearance", dest="cleared", action="store_true")
    gt.add_argument("--text", help="description or prompt to scan")

    nw = sub.add_parser("new", help="create an ORIGINAL character sheet (preferred)")
    nw.add_argument("--name", required=True)
    nw.add_argument("--role", required=True)
    nw.add_argument("--base", help="registry id to draw inspiration from (optional)")
    nw.add_argument("--look", default="")
    nw.add_argument("--wardrobe", default="")
    nw.add_argument("--palette", default="")
    nw.add_argument("--voice", default="")
    nw.add_argument("--manner", default="")
    nw.add_argument("--seed", type=int)
    nw.add_argument("--out", required=True)

    lk = sub.add_parser("lock", help="verify a sheet has not drifted")
    lk.add_argument("sheet")
    lk.add_argument("--update", action="store_true", help="re-lock after an intentional edit")

    pr = sub.add_parser("prompt", help="emit the canonical prompt block")
    pr.add_argument("sheet")
    pr.add_argument("--shot", default="")
    pr.add_argument("--style", default="editorial, gold and deep navy, clean, premium")

    a = p.parse_args(argv)
    reg = load_registry()

    if a.cmd == "list":
        for c in reg["characters"]:
            if a.tier and c["tier"] != a.tier:
                continue
            print(f"  {c['id']:24s} {c['tier']:20s} {c['name']}")
        print(f"\n{len(reg['characters'])} characters. Reviewed {reg['reviewed']}.")
        print("NOT LEGAL ADVICE - verify before publishing.")
        return 0

    if a.cmd == "suggest":
        rows = suggest(reg, a.subject, a.mood, a.audience, a.intent, a.jurisdiction, a.limit)
        print(f"Brief: subject={a.subject!r} mood={a.mood!r} "
              f"audience={a.audience!r} intent={a.intent!r} ({a.jurisdiction})\n")
        print("An ORIGINAL character beats every option below: no trademark exposure,")
        print("full brand control, and easier to keep consistent. See `character new`.\n")
        for score, c in rows:
            flag = {"folklore": "safest", "expired": "low risk",
                    "version-locked": "VERSION-LOCKED", "jurisdiction-locked": "JURISDICTION-LOCKED",
                    "high-risk": "HIGH RISK"}[c["tier"]]
            print(f"  [{score:5.1f}] {c['name']}  ({flag})")
            print(f"          {c.get('dgd_fit','')}")
        print("\nInspect one with: character show <id>")
        return 0

    if a.cmd == "show":
        c = find(reg, a.id)
        if not c:
            sys.stderr.write(f"unknown character '{a.id}'. Try: character list\n")
            return 2
        print(f"{c['name']}  [{c['id']}]")
        print(f"  source     {c['source']}")
        print(f"  tier       {c['tier']}")
        print(f"  status     {json.dumps(c.get('jurisdictions', {}))}")
        print(f"  safe use   {c['safe_version']}")
        print(f"  fit        {c.get('dgd_fit','')}")
        print(f"  themes     {', '.join(c['themes'])}")
        print(f"  tone       {', '.join(c['tone'])}")
        if c.get("traps"):
            print("  TRAPS:")
            for t in c["traps"]:
                print(f"    - {t}")
        ok, findings = gate(c, a.jurisdiction)
        print()
        print_findings(findings)
        return 0

    if a.cmd == "gate":
        c = find(reg, a.id)
        if not c:
            sys.stderr.write(f"unknown character '{a.id}'\n")
            return 2
        ok, findings = gate(c, a.jurisdiction, a.ack_version, a.cleared, a.text)
        print(f"gate: {c['name']} in {a.jurisdiction}\n")
        print_findings(findings)
        print("\n" + ("CLEAR - proceed (still not legal advice)." if ok
                      else "BLOCKED - do not render. Pick a folklore-tier character or "
                           "create an original one."))
        return 0 if ok else 2

    if a.cmd == "new":
        base = None
        if a.base:
            b = find(reg, a.base)
            if not b:
                sys.stderr.write(f"unknown base '{a.base}'\n")
                return 2
            ok, findings = gate(b, "US")
            if not ok:
                print(f"Cannot base a character on {b['name']}:\n")
                print_findings([f for f in findings if f[0] == "BLOCK"])
                return 2
            base = a.base
        sheet = new_sheet(a.name, a.role, base, a.seed, a.look, a.wardrobe,
                          a.palette, a.voice, a.manner)
        traps, endorse = scan_text(a.role, a.look, a.wardrobe, a.manner)
        if traps or endorse:
            print("BLOCKED - your description contains protected or endorsing elements:\n")
            for why, _ in traps + endorse:
                print(f"  [BLOCK] {why}")
            return 2
        os.makedirs(os.path.dirname(os.path.abspath(a.out)) or ".", exist_ok=True)
        with open(a.out, "w", encoding="utf-8") as f:
            json.dump(sheet, f, indent=2)
        print(f"wrote {a.out}")
        print(f"  lock {sheet['lock']}  seed {sheet['seed']}")
        print("\nFill in every TODO, then re-lock:  character lock "
              f"{a.out} --update")
        print("Reuse the SAME sheet and seed in every video - that is the consistency.")
        return 0

    if a.cmd == "lock":
        with open(a.sheet, encoding="utf-8") as f:
            sheet = json.load(f)
        todos = [k for k in LOCK_FIELDS if str(sheet.get(k, "")).startswith("TODO")]
        current = lock_hash(sheet)
        stored = sheet.get("lock")
        if a.update:
            sheet["lock"] = current
            with open(a.sheet, "w", encoding="utf-8") as f:
                json.dump(sheet, f, indent=2)
            print(f"re-locked {a.sheet}: {stored} -> {current}")
            if todos:
                print(f"  still unfilled: {', '.join(todos)}")
            return 0
        if todos:
            print(f"INCOMPLETE - unfilled fields: {', '.join(todos)}")
            return 2
        if stored != current:
            print(f"DRIFT DETECTED\n  stored  {stored}\n  current {current}")
            print("\nThe character's identity changed since it was locked. Earlier videos")
            print("used the old description. Either revert, or accept the change and")
            print("re-lock with --update (and expect a visible difference on screen).")
            return 2
        print(f"lock OK: {stored} - identity unchanged since last lock.")
        return 0

    if a.cmd == "prompt":
        with open(a.sheet, encoding="utf-8") as f:
            sheet = json.load(f)
        if lock_hash(sheet) != sheet.get("lock"):
            sys.stderr.write("REFUSING: sheet has drifted from its lock. "
                             "Run `character lock <sheet>` first.\n")
            return 2
        # Gate the SHOT/STYLE text before it can reach a generator. --shot is
        # free text and is exactly where "buy DGD now, guaranteed 100x" lands.
        traps, endorse = scan_text(a.shot, a.style)
        if traps or endorse:
            sys.stderr.write("BLOCKED - shot/style contains protected or endorsing elements:\n")
            for why, _ in traps + endorse:
                sys.stderr.write(f"  [BLOCK] {why}\n")
            return 2
        block = build_prompt(sheet, a.shot, a.style)
        if CL is None:
            sys.stderr.write("REFUSING: compliance_lint unavailable, cannot gate the prompt.\n")
            return 2
        # Lint the USER-SUPPLIED parts only. The negative list is our own
        # boilerplate ("no rocket or casino imagery") and linting it made every
        # prompt warn about a word we ourselves added to forbid it.
        authored = "\n".join([sheet.get("name", ""), sheet.get("role", ""),
                              sheet.get("look", ""), sheet.get("wardrobe", ""),
                              sheet.get("manner", ""), sheet.get("voice", ""),
                              a.shot or "", a.style or ""])
        res = CL.lint_text(authored)
        if res["verdict"] == "fail":
            sys.stderr.write("BLOCKED - the prompt breaks the communications discipline:\n")
            for f in res["findings"]:
                if f["severity"] == "FAIL":
                    sys.stderr.write(f"  [FAIL] {f['category']}: '{f['term']}'\n")
                    sys.stderr.write(f"         {f['fix']}\n")
            return 2
        print(block)
        warns = [f for f in res["findings"] if f["severity"] == "WARN"]
        if warns:
            sys.stderr.write("\n(warnings - review before generating)\n")
            for f in warns:
                sys.stderr.write(f"  [WARN] {f['category']}: '{f['term']}'\n")
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
