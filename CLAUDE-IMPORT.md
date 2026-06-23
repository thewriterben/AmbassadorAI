# CLAUDE-IMPORT: One-click / Paste prompt bundle (dgd-video-studio)

This file contains two things:
1) Quick instructions for installing `skills/dgd-video-studio/SKILL.md` into Claude Cowork (desktop)
2) A paste-ready prompt bundle you can copy into a Claude chat to run the example workflow without installing the skill.

---

Installing via Claude Cowork (desktop)

1. Open Claude Cowork on your desktop and sign in to your workspace.
2. Open the "Skills" or "Developer" section (UI name may vary).
3. Choose "Import skill" or "Upload skill". If there is a folder drag-and-drop area you can upload the whole `skills/dgd-video-studio` folder.
4. If the UI expects a single file, open `skills/dgd-video-studio/SKILL.md` in a text editor, copy its entire contents, and paste into the import text area.
5. Follow the UI prompts to enable/activate the skill. Test it in a private chat or sandbox workspace.

If the Cowork UI provides a validation log, address missing frontmatter fields (name/version) or template references by editing the SKILL.md and re-importing.

---

Paste-ready prompt bundle (manual run in Claude chat)

Copy the entire block below and paste it into a new Claude chat. Replace the brief where noted.

--- BEGIN PROMPT BUNDLE ---

System / Instruction:
You are a short-form video writer and production assistant specialized in "Digital Gold" style explainer videos. You will follow structured steps and produce clearly labeled sections. Use calm, confident, and accessible language. When asked for deliverables, produce output in Markdown with explicit section headings.

User / Task Brief:
Create a short video package from this brief.

Brief: "Produce a 60-second explainer about why 'Digital Gold' (Bitcoin) is considered 'sound money' by some investors. Audience: general-interest adults (45–65), curious but not expert. Tone: confident, calm, educational. Deliverables: (1) 60s script with six time-stamped beats, (2) six-shot storyboard with short visual descriptions and B-roll suggestions, (3) 3 thumbnail/title options, (4) suggested on-screen captions and keywords/hashtags, (5) a short QC checklist to validate the output."

Instructions (how you should respond):
1. Output a short Planning summary (one paragraph).
2. Produce the 60s script split into six labeled beats with time or word guidance.
3. Produce a 6-shot storyboard: for each shot include camera type (close/medium/wide), duration in seconds, visuals, on-screen text, and suggested B-roll.
4. Produce 3 thumbnail/title options (each with a 6–8 word title and a thumbnail description).
5. Produce suggested hashtags and 6–8 SEO keywords.
6. End with a QC checklist (3–6 checks) — short and actionable.

Tone and constraints:
- Keep the script approximately 120–160 words total (spoken at a conversational pace ~130 wpm ≈ 60s).
- Use simple sentences; no jargon without brief explanation.
- Use lists and short labeled sections so the content is easy to copy into a video editor.

--- END PROMPT BUNDLE ---

Notes:
- This bundle is intentionally verbose so an out-of-the-box Claude chat run yields consistent, copy-pasteable outputs.
- After running the bundle, you can iterate on the brief or constraints to refine tone, length, or audience.

---

If you want, I can add a small desktop automation script that opens Cowork and pre-fills the import form (requires knowledge of your OS and Cowork version).