# Reference — Characters: casting, IP safety, and consistency

A recurring character is the cheapest way to make a channel feel like a channel. It is
also two traps at once: an **IP trap** (public-domain characters are rarely as free as
they look) and a **consistency trap** (generators invent a slightly different person every
time, and three different hosts across three videos reads as slop).

This page and `dgd.py character` handle both.

> **NOT LEGAL ADVICE.** The registry is a research aid and a mechanical guard rail, not a
> clearance opinion. Copyright and trademark status changes, varies by country, and is
> fact-specific. Verify before publishing anything commercial.

---

## 1. Start here: original beats public domain

**The default path is an original character.** Not because public-domain characters are
unusable, but because for *this* channel the trade is bad:

| | Original | Public domain |
|---|---|---|
| Trademark exposure | none | permanent, and copyright expiry does not touch it |
| Brand control | total | you inherit someone else's associations |
| Consistency | easy — you own the design | harder — "correct" is defined elsewhere |
| Recognition | you have to build it | instant |

The one real advantage of a PD character is **instant recognition**, and it is worth
something. But recognition cuts both ways: the more recognisable the character, the more
likely the rights-holder is to be actively enforcing.

```
python tools/dgd.py character new --name "Assay" --role "a careful assayer who tests claims" \
    --look "..." --wardrobe "..." --manner "..." --out cast/assay.json
```

---

## 2. Why "public domain" is not a green light

Copyright expiring is only one of three questions. The registry encodes all three.

**Trademark is separate and never expires.** Disney's copyright on *Steamboat Willie*
lapsed; Disney's *trademark* in Mickey as a brand identifier did not, and never will.

**Public domain is usually version-locked.** Only one specific early form is free:

| Character | Free | NOT free |
|---|---|---|
| Mickey Mouse | 1928 *Steamboat Willie* / *Plane Crazy* | red shorts, white gloves, modern proportions |
| Winnie-the-Pooh | Milne's 1926 text, Shepard's line art | **the red shirt** (Disney's) |
| Frankenstein's Creature | Shelley's 1818 novel — articulate, yellow-skinned | **flat head, neck bolts, green skin** (Universal 1931) |
| Dorothy Gale | Baum's novels — slippers are **silver** | **ruby slippers** (MGM 1939) |
| Popeye | 1929 Segar strip | **spinach-derived strength** (1931) |
| Sleeping Beauty | the fairy tale | "Aurora", "Briar Rose" (Disney) |
| Snow White | the fairy tale | Sneezy, Bashful, Dopey (Disney) |

**Public domain is jurisdiction-specific**, and short-form video does not respect borders:

- **Tintin** — US public domain since 2025, **copyrighted in the EU until 2054**.
- **Peter Pan** — US public domain; still under a perpetual Great Ormond Street right in the UK.
- **James Bond** — Canada only, and only if produced and distributed there.

A character that is only clear in one territory is effectively unusable on TikTok,
Reels, Shorts or X, all of which distribute globally by default.

**And one risk specific to this channel:** putting a recognisable character in content
about a *cryptocurrency* is a different fact pattern from using one in a comic. It invites
an implied-endorsement or dilution claim on top of the copyright question. That is why
the gate blocks high-risk characters outright rather than warning.

---

## 3. Risk tiers

| Tier | Meaning | Gate behaviour |
|---|---|---|
| `folklore` | Myth, fable, legend. No copyright ever attached. | allowed |
| `expired` | Source copyright lapsed; low trademark heat. | allowed |
| `version-locked` | Only one early version is free. | **blocked** until `--ack-version` |
| `jurisdiction-locked` | Free in some countries only. | **blocked** outside the clear list |
| `high-risk` | Actively enforced by a living rights-holder. | **blocked** unless cleared |

### The useful coincidence

**The safest characters are also the best-suited.** Fables and myths carry no copyright at
all *and* they are already about the exact things this channel explains:

| Character | Theme |
|---|---|
| The Tortoise and the Hare | anti-speculation — degen energy as the hare, selling nothing |
| The Ant and the Grasshopper | time-preference, storing value across seasons |
| King Midas | gold you cannot spend is not wealth |
| Icarus | overreach and leverage, without naming a token |
| Sisyphus | the debasement treadmill, without conspiracy framing |
| The Three Little Pigs | straw / sticks / brick as monetary foundations |
| The Boy Who Cried Wolf | credibility as the scarce good |
| Robinson Crusoe | first-principles money, built up from one person |
| Ebenezer Scrooge | hoarding versus circulation |
| Sherlock Holmes | reading a white paper as evidence, not faith |

You almost never need to reach into the risky tiers.

---

## 4. The gate

```
python tools/dgd.py character gate --id dorothy-gale --ack-version \
    --text "Dorothy clicks her ruby slippers three times"
```

Fail-closed, exit 2 on any block. It checks four things:

1. **Jurisdiction** — status in your target territory; unverified counts as blocked.
2. **Tier** — high-risk needs clearance; version-locked needs `--ack-version`.
3. **Trap phrases in your actual text** — this is the one that earns its keep. Even after
   you acknowledge Dorothy's version, writing "ruby slippers" still blocks.
4. **Endorsement framing** — a character who "recommends", "vouches for", or urges viewers
   to acquire anything is blocked. A recognisable figure recommending a coin reads as an
   endorsement regardless of how the script is worded.

---

## 5. Consistency: the character sheet lock

Same problem as the coin, same shape of solution. Identity is locked; everything else
varies.

A **character sheet** is a JSON file holding the identity fields — name, role, look,
wardrobe, palette, voice, manner, seed. Those fields are hashed into a **lock**.

```
python tools/dgd.py character lock cast/assay.json      # verify
python tools/dgd.py character prompt cast/assay.json --shot "at a workbench"
```

- `lock` **fails if the sheet is incomplete** (any `TODO` left) or if the identity has
  **drifted** from the stored hash.
- `prompt` **refuses to emit** while a sheet is drifted, so a changed character cannot
  silently reach a generator.
- Changing the character is allowed — but it must be deliberate: `lock --update` re-locks
  and tells you the hash moved. Expect a visible difference on screen.

### What actually produces consistency

1. **Paste the canonical block verbatim** into every generation. Not paraphrased. The
   verbatim reuse *is* the mechanism.
2. **Reuse the seed** the sheet carries, in every render, in any tool that accepts one.
3. **Keep the negative list** — it carries the compliance rail into image space: no price
   charts, no coin stacks, no rocket or casino imagery.
4. **Feed back a reference image** once you have a frame you like. Image-to-image against
   a locked reference beats text alone every time.

The block also inherits the studio palette, so the character sits inside the existing
gold-and-navy identity rather than fighting it.

---

## 6. Compliance — characters are not exempt

Everything in the prime directive applies to a character exactly as it applies to a script.

- A character **may explain**; a character **may not recommend**. The gate enforces this.
- A character must not be framed as an official mascot of, or affiliated with, any
  rights-holder.
- **An AI-generated character needs the AI disclosure**, same as any synthetic footage.
- Keep characters **illustrative, not testimonial** — no "I bought this and here's what
  happened", which is a solicitation wearing a costume.
- The gut check still holds: *if a viewer never acquires a single coin, is this character
  still doing honest educational work?*

---

## Connects to
- Registry: `../../tools/characters.json` · Tool: `../../tools/dgd_characters.py`
- Rails: `compliance-gate.md` · `../../LLMWiki/compliance/communications-discipline.md`
- Visual identity: `coin-assets.md` (same lock-the-identity philosophy) · `asset-generation.md`
- Audience framing: `../../LLMWiki/craft/positioning-and-audiences.md`
