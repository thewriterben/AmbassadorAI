# Clean-room red-team run — 20260930T223223Z

Commit `03e121d2f202447f25da1277ad643c00c25b918b` (`03e121d`). Policy: `arcade/REDTEAM-POLICY.md`.
Worktree is detached at the hash; the working copy is not consulted.

| Check | Result | Detail |
|---|---|---|
| worktree | PASS | detached at 03e121d2f202 |
| v2 server tests | PASS | 39 tests: 39 pass, 0 todo |
| v2 server hosts | PASS | only allowlisted hosts in src/ |
| v2 server secrets | PASS | no secret-shaped strings |
| v2 app analyze | PASS | no issues |
| v2 app tests (plain) | PASS | +183 ~14: All tests passed |
| v2 app tests (ARCADE_API loopback) | PASS | +192 ~5: All tests passed |
| v2 app tests (demo, loopback) | PASS | +184 ~13: All tests passed |
| v2 app network cases ran | PASS | 9 more cases with the define |
| v2 app hosts | PASS | only allowlisted hosts in lib/ |
| v2 app secrets | PASS | no secret-shaped strings |


### v2 server red-team ledger

- ✔ HOLDS R1 the mini-game daily cap still binds when rounds straddle UTC midnight
- ✔ ACCEPTED R2 a mini-game score is whatever the client says, bounded only by the per-round and per-day caps
- ✔ HOLDS R3 anonymous player creation is throttled well below the generic limiter
- ✔ HOLDS R4 the rate limiter does not admit a double burst at the window boundary
- ✔ HOLDS R5 X-Forwarded-For is ignored unless a proxy is trusted, and then only its last hop counts
- ✔ HOLDS R6 a tablet cannot be answered once its expedition is finished
- ✔ HOLDS R7 a bank question that disappears between issue and answer is a 4xx, not a 500
- ✔ ACCEPTED R8 status="xp_only" means zero XP, not "XP only", and is never set by the server
- ✔ HOLDS R9 a corrupt server-written JSON column is a handled error, not a 500
- ✔ HOLDS R10 the board never carries ids or tokens, and handle rerolls stop at the daily cap
- ✔ HOLDS R11 /healthz is the only unauthenticated read and says only that the bank is loaded
- ✔ ACCEPTED R12 CORS is a wildcard unless ARCADE_CORS is set, whatever NODE_ENV says

### v2 server routes (from source)

```
DELETE /v1/me
GET /healthz
GET /v1/leaderboard
GET /v1/ledger/today
GET /v1/me
POST /v1/expeditions
POST /v1/expeditions/:id/finish
POST /v1/expeditions/:id/tablets/:idx
POST /v1/expeditions/:id/tablets/:idx/answer
POST /v1/ledger/guess
POST /v1/me/handle/reroll
POST /v1/mini/:game
POST /v1/mini/:game/start
POST /v1/passage/abilities/:ability/upgrade
POST /v1/passage/loadout
POST /v1/players
```

### v2 server environment flags

```
ARCADE_ALLOW_DEV_SECRET ARCADE_BANK ARCADE_CORS ARCADE_DB ARCADE_SECRET ARCADE_TRUST_PROXY NODE_ENV 
```

### v2 app dart-defines read by the code

```
ARCADE_API DGD_APP_TAB DGD_DEMO DGD_DEV 
```

**Verdict: PASS**. Report: F:/Documents/GitHub/AmbassadorAI/arcade/redteam-runs/20260930T223223Z-03e121d/report.md
