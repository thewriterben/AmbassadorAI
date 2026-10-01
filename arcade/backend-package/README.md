# DGD Arcade server: what the backend team needs for DGD App 2.1

**30 September 2026, updated 1 October. For backend engineering (Oleksandr, and whoever runs the arcade service).**

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

**DGD App 2.1.0 is the live build. It is ready apart from the server.**

- It is built against `https://arcade-api.digitalgold.co` and waits only on that host.
- On 30 Sep it was rehearsed end to end against this server, running locally in production mode, with each step checked against the server's database:
  - registration;
  - a Coin Quest round;
  - a full When Pigs Fly flight, with growth;
  - the shop and the loadout;
  - the weekly standings, and a new name;
  - deletion.
- The rehearsal found two app bugs, both now fixed. It found nothing to change in the server.

**Going live does not change the app's games.** Turning the server on adds four things to the same two games:

- XP and levels;
- weekly standings, which are recognition only, with no prize and no monetary value;
- the When Pigs Fly growth and ability shop;
- server-side data deletion.

## What we are asking for

1. **Production at `https://arcade-api.digitalgold.co`** (decided 30 Sep), and a staging host before it.
   - Staging is for your own smoke tests. The app is built for production only.
   - Each is one process with one persistent volume: see `DEPLOY.md`.
   - Keep production apart from the web arcade: see "Separate from the web arcade" below.
2. **Generate and hold `ARCADE_SECRET`.**
   - It must be 32 characters or more, and different on staging and production.
   - It never comes to us and never goes in a repo.
   - The server refuses to start without one.
3. **Back up `/app/data` daily.** `DEPLOY.md` has a command that is safe to run while the server is live.
4. **Run `node smoke.mjs <url>` against staging, then production,** and send us the output.
5. **Decide on retention.** Nothing expires today. `DATA-AND-PRIVACY.md` proposes a rule.
6. **Tell us when production is up.** DGD App 2.1.0 already points at it.
   - We run it end to end against production, re-run the ship gate, and hand DGD the AAB to sign.
   - Our test records are removed with the app's own **Delete my play record**, just as `smoke.mjs` deletes its throwaway player.

## Separate from the web arcade

The web arcade at `digitalgold.co/arcade/` pays DGD and Top 100 credits, and it has its own rewards server under `/arcade/api/`. The app links to it as a neutral link only. The app's reviewer notes and DGD's 28 Sep decision on that link both rest on two claims: the site cannot tell app visitors apart from anyone else, and nothing done in the app counts there.

So `arcade-api.digitalgold.co` must stay a separate service:

- **its own host and process,** not routed through the web arcade's path or proxy rules;
- **its own database,** with no shared players, tokens, handles or standings;
- **nothing that reads its data to credit anything on the web arcade,** now or later.

If DGD ever wants app play to count towards web rewards, that reopens the B1 decision with counsel first. It is not a backend change.

## What traffic to expect

- **Registration:** one `POST /v1/players` per install.
  - It happens the first time the player opens the arcade (a game, the arcade's settings, or the standings), never at app launch. People who only use the ticker never reach the server.
  - It happens again if a player deletes their record and keeps playing.
- **Once per app session:** one `GET /v1/me`, when the arcade is first opened. Rounds, the shop and the standings bring fresh progress back with their own responses.
- **Each round:** one start and one claim. A Coin Quest claim comes at least 15 s after its start, a When Pigs Fly claim at least 4 s after.
- **The standings:** `GET /v1/leaderboard`, from the Arcade tab's "Weekly standings" row. A new name (`/v1/me/handle/reroll`) is allowed 3 times a day.
- **The shop:** an upgrade or a loadout change, now and then.
- **Retries:** every call has an 8-second client timeout, and there is no retry loop. A 401 on the session's `GET /v1/me` or on a round start registers once and tries once more. Nothing else retries.

**Watch the signup limit at launch.**

- `PLAYERS_PER_HOUR` allows 10 registrations per client address per hour.
- Mobile carriers put many phones behind one address. In a busy launch hour that limit can refuse real first opens with `429 signup_rate_limited`.
- When that happens, the app shows the arcade offline and tries again on the next open.
- In the first days, watch the proxy's 429 count on `POST /v1/players`. If it shows, raise `PLAYERS_PER_HOUR`; that needs a restart, not a deploy.

## What we do once production is up

- **Nothing needs rebuilding first.** The clean-room arcade is already built with `ARCADE_API=https://arcade-api.digitalgold.co`, and DGD App 2.1.0 is built on it. Both reproduce in the clean room.
- **Run 2.1.0 against production** on the emulator and a phone, with the same steps as the rehearsal.
- **Update the privacy policy draft and the Play Data safety answers.** Going live means the app sends game data for the first time, so DGD has to approve both before release.

## Files

| File | What it is |
|---|---|
| `DEPLOY.md` | Hosting runbook: environment, Docker, proxy, health, backups, tuning, and what to watch |
| `API.md` | The ten routes DGD App 2.1 calls, with their caps and refusals |
| `DATA-AND-PRIVACY.md` | What is stored, what is not, how deletion works, and the open retention decision |
| `env.example` | Every environment variable, with names and placeholders only |
| `smoke.mjs` | A post-deploy check that registers a throwaway player, exercises the routes, then deletes the player |
| `checks/` | The test-suite and smoke-test output, re-run on 1 Oct |
| `source/` | A `git archive` of the server at `50b46d5`, for anyone without repo access. It is in the zip only; this repo copy leaves it out. |

## Still open from 21 Sep, and not part of this package

- **The `/analytics` chart.** The app still shows no price-history chart. If one comes back, it must be plotted from `/analytics` and nothing else.
- **Referral crediting for app-originated `?ref=` codes.** This is the B1 question from the 21 Sep brief.
- **The web arcade at `digitalgold.co/arcade/`.** It is a separate build, designed elsewhere. DGD App 2.x only links to it.
