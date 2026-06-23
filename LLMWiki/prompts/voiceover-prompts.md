---
tags: [prompts, voiceover, tts]
updated: 2026-06-16
---

# Prompt Library — Voiceover & Delivery

Settings and micro-prompts for natural AI narration, plus phonetic guides. → [voiceover tools](../tools/voiceover-tts.md)

## Voice-direction settings (ElevenLabs & similar)
- **Voice type:** warm, clear, mid-energy "explainer" voice. Avoid over-the-top hype announcers (also off-brand for educational content).
- **Stability:** medium (too high = monotone; too low = erratic).
- **Pace:** slightly faster than conversational.
- **Style/emotion:** "curious and friendly teacher."

## Add delivery cues in your script text
Most TTS tools respond to punctuation and line breaks:
- Use **short sentences** and line breaks for natural pauses.
- Add a **comma or ellipsis** for a beat: "Saving money… is making you poorer."
- ALL-CAPS a single word sparingly for emphasis: "Each unit buys LESS."
- Put a hard pause after the hook and before the payoff.

## Phonetic guide (type these spellings into TTS if it mispronounces)
| Term | Say it | TTS spelling |
|---|---|---|
| Hayek | HY-ek | "Hy-ek" |
| Menger | MENG-er | "Meng-er" |
| Mises | MEE-zes | "Mee-zes" |
| Menger's regression | — | spell out normally |
| DGSB | say letters | "D-G-S-B" |
| CFV | say letters | "C-F-V" |
| DGD | say letters | "D-G-D" |
| SegWit | SEG-wit | "Seg-wit" |
| fiat | FEE-aht | "Fee-aht" |

## Optional script-to-SSML prompt (for tools that accept SSML)
```
Convert this narration to SSML for a natural explainer delivery:
- add brief pauses after the hook and before the key payoff,
- slight emphasis on numbers and the single key term,
- keep an even, friendly pace.
Narration: [PASTE]
```

## Disclosure in audio
If the voice is AI, you still owe an **on-screen** "AI voice" note (audio alone won't satisfy platforms). And weave the spoken **sponsorship + not-financial-advice** line into the first seconds. → [FTC](../compliance/ftc-disclosure.md) · [AI disclosure](../compliance/ai-disclosure.md)

## Quality pass
- Listen on phone speakers.
- Fix any robotic term with phonetic spelling.
- Normalize to ~-14 LUFS; duck music under voice. → [music & sound](../tools/music-and-sound.md)

## Connects to
- [Voiceover tools](../tools/voiceover-tts.md) · [Script prompts](script-prompts.md) · [Captions & editing](../tools/captions-and-editing.md)
