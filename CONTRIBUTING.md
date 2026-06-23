# Contributing to AmbassadorAI

Thank you for contributing! AmbassadorAI is a content-first repository of agent skills, templates, and reference materials. Contributions are welcome (new skills, prompt improvements, templates, documentation, or example outputs).

Before you open a PR

- Run the skill prompts locally in a Claude sandbox or Cowork test environment where possible. Validate outputs and include example output files in the skill folder (see example-output/).
- Validate SKILL.md frontmatter contains at minimum: `name`, `description`, `version`, and `tags`.
- Keep templates small and single-purpose (e.g., `script-template.md`, `shot-list-template.md`). Put templates in `LLMWiki/templates/` and reference them from SKILL.md.
- Do not commit API keys, secrets, or private data.

How to structure a pull request

- Title: Add/Update skill: <skill-name> — short description
- Description: Include a one-paragraph summary of what the skill does and which prompts/templates it changes.
- Checklist (add in PR description):
  - [ ] SKILL.md frontmatter present and valid
  - [ ] Example output included (`skills/<skill-name>/example-output/`)
  - [ ] Templates referenced live in `LLMWiki/templates/` (if added/changed)
  - [ ] LLMWiki index updated (if adding a new skill)
  - [ ] Prompts validated in a Claude sandbox / Cowork test

Local testing recommendations

- For Claude Cowork desktop users: use a private Cowork workspace or test account to run prompts and confirm outputs before opening a PR.
- For local agent runners: place your skill folder under a local `skills/` path and run the runner in development mode (restart if necessary).

Review process

- Reviewer will run the prompts or load the SKILL.md in a Claude sandbox.
- If the skill uses tools (image fetch, voiceover, render), the reviewer will need info about the expected tool names and interfaces — document these in `skills/<skill>/reference/`.

License and attribution

- Contributor-submitted content will be added under the repository license (MIT) unless otherwise noted.
- If you include third-party assets (images, transcripts, whitepapers), include license and attribution notes in the skill's `reference/` folder.

Thanks for improving AmbassadorAI — your contributions help make the skill library more useful for creators and agents alike.
