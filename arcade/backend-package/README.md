# DGD Arcade server: what the backend team needs for DGD App 2.0

**30 September 2026. For backend engineering (Oleksandr, and whoever runs the arcade service).**

This package replaces two earlier briefs:

- `FOR-BACKEND-2026-09-21.md` still holds for credentials ownership, the ticker's endpoint and the referral question.
- `BACKEND-BRIEF-PATH-C.md` no longer applies. Path A shipped on Android 1.0.6, so Path C will not happen.

Nothing secret is in this package, and it should stay that way when you forward it.

## Where things stand

**DGD App 2.0 is ready to release on Android as an unsigned AAB.** It embeds the new arcade (Coin Quest and When Pigs Fly), redesigned from the 30 Sep design return.

**The arcade ships in demo mode.** Demo mode has no server:

- progress stays on the phone;
- there are no XP, standings, handle or When Pigs Fly shop;
- the only network call the app makes is the ticker's existing `GET https://digitalgold.co/api/forms/stats`.

**The server is ready to host, but is not hosted anywhere.** Details:

- Repo: `thewriterben/dgd-arcade-server`, branch `v2/ten-games`, commit `50b46d5`. A snapshot is in `source/`.
- The suite passes: 39 of 39 tests, including the red-team cases.
- `smoke.mjs` passes 16 of 16 checks against a local instance.

**Going live does not change the app's games.** Turning the server on adds four things to the same two games:

- XP and levels;
- weekly standings, which are recognition only, with no prize and no monetary value;
- the When Pigs Fly growth and ability shop;
- server-side data deletion.

## What we are asking for

1. **Production at `https://arcade-api.digitalgold.co`** (decided 30 Sep), and a staging host before it. Each is one process with one persistent volume: see `DEPLOY.md`. Keep it apart from the web arcade: see "Separate from the web arcade" below.
2. **Generate and hold `ARCADE_SECRET`.**
   - It must be 32 characters or more, and different on staging and production.
   - It never comes to us and never goes in a repo.
   - The server refuses to start without one.
3. **Back up `/app/data` daily.** `DEPLOY.md` has a command that is safe to run while the server is live.
4. **Run `node smoke.mjs <url>` against staging, then production,** and send us the output.
5. **Decide on retention.** Nothing expires today. `DATA-AND-PRIVACY.md` proposes a rule.
6. **Tell us when production is up.** The live build already points at `https://arcade-api.digitalgold.co`. We then rebuild the arcade in the clean room with `ARCADE_API=<url>` instead of demo mode, re-run the ship gate against staging, and hand DGD a new AAB to sign.

## Separate from the web arcade

The web arcade at `digitalgold.co/arcade/` pays DGD and Top 100 credits, and it has its own rewards server under `/arcade/api/`. The app links to it as a neutral link only. The app's reviewer notes and DGD's 28 Sep decision on that link both rest on two claims: the site cannot tell app visitors apart from anyone else, and nothing done in the app counts there.

So `arcade-api.digitalgold.co` must stay a separate service:

- **its own host and process,** not routed through the web arcade's path or proxy rules;
- **its own database,** with no shared players, tokens, handles or standings;
- **nothing that reads its data to credit anything on the web arcade,** now or later.

If DGD ever wants app play to count towards web rewards, that reopens the B1 decision with counsel first. It is not a backend change.

## What we do once production is up

- **The live build is ready.** The clean-room arcade is already built with `ARCADE_API=https://arcade-api.digitalgold.co`, and DGD App 2.1.0 is built on it. It waits on the server.
- **Re-verify the embed.** The provenance gate in the native build already checks that the embed came from the clean room.
- **Run the app against staging on a phone and on the emulator.** This covers registration, a Coin Quest level, a When Pigs Fly run, the shop, the standings and deletion from Settings.
- **Update the privacy policy draft and the Play Data safety answers.** Going live means the app sends game data for the first time, so DGD has to approve both before release.

## Files

| File | What it is |
|---|---|
| `DEPLOY.md` | Hosting runbook: environment, Docker, proxy, health, backups, tuning, and what to watch |
| `API.md` | The ten routes DGD App 2.0 calls, with their caps and refusals |
| `DATA-AND-PRIVACY.md` | What is stored, what is not, how deletion works, and the open retention decision |
| `env.example` | Every environment variable, with names and placeholders only |
| `smoke.mjs` | A post-deploy check that registers a throwaway player, exercises the routes, then deletes the player |
| `checks/` | The test-suite and smoke-test output from 30 Sep |
| `source/` | A `git archive` of the server at `50b46d5`, for anyone without repo access. It is in the zip only; this repo copy leaves it out. |

## Still open from 21 Sep, and not part of this package

- **The `/analytics` chart.** The app still shows no price-history chart. If one comes back, it must be plotted from `/analytics` and nothing else.
- **Referral crediting for app-originated `?ref=` codes.** This is the B1 question from the 21 Sep brief.
- **The web arcade at `digitalgold.co/arcade/`.** It is a separate build, designed elsewhere. DGD App 2.0 only links to it.
