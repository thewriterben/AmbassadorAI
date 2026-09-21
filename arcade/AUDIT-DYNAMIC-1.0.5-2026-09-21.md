# Dynamic pass — v1.0.5

**2026-09-21.** The runtime half of the red-team work. The static sweep is
`REDTEAM-1.0.5-2026-09-21.md`; this is what the earlier report listed as not
covered.

---

## Header (REDTEAM-POLICY.md §5)

**Scope and authorisation.** Requested by Benji. Runtime behaviour of the
v1.0.5 review build and the suites that gate it. Loopback only.

**Commit hashes**

| Tree | Hash | Subject |
|---|---|---|
| `dgd-native` | `bc8c614` | Trim stats-source.json to the three fields the app reads |
| `puzzle-app` | `11dcd60` | Guard DevMenu at the call sites |
| `AmbassadorAI` | `dc91889` | Red team F1 and F2 fixed and re-swept |

Toolchain: Flutter 3.47.2 / Dart 3.13.2. Server suites run on Node 22.23.2 in
an isolated container.

**Suites, defines and counts** — see §2. Every Flutter test ran at least once
across two runs; the server suites ran complete.

### Exceptions to the policy, declared

Two, and both matter.

- **§2.6, independence — NOT MET.** This session wrote much of the code under
  test. The policy requires a pass "in a session that did not write the code",
  and that is not what this is. Everything below is a self-check, which is
  worth less than an independent one. It is not a substitute for the
  independent pass and should not be recorded as one.
- **§2.3, reproducibility — NOT DONE.** No byte-for-byte clean-room rebuild of
  the APK from the pinned commit. The artefact was analysed as shipped and its
  hash recorded, but "the shipped artefact must match a clean-room rebuild"
  was not tested.

One more, smaller: **§2.2 permits loopback only, and that was honoured.** No
traffic to `digitalgold.co` or any hosted service. The client suites talk to
an in-process `FakeServer` on `127.0.0.1:8799`; the server suites run against
their own in-process instance.

**Fixed the same day:** nothing. This pass changed no code. The one finding
below is a documentation and process change, left for a decision.

**How to re-run:** §5.

---

## 1. The finding

### D1 — the define gate can report green while skipping the invariant it exists to check

**Severity: MEDIUM.** Process, not product. Nothing in the app is wrong.

Policy §4 requires "Both Flutter suites **with the loopback and demo
defines**", and warns:

> *"A plain `flutter test` skips the network layer silently and reports green;
> that run does not count."*

That warning is correct and it is not sufficient. The natural reading — one
run per define — **also** reports green while skipping the most important
test.

Observed, with the actual numbers:

| Run | Defines | Passed | Skipped | Did the demo invariant run? |
|---|---|---|---|---|
| A | *(none)* | 45 | 8 | no |
| B | `DGD_DEMO=true` | 45 | **8** | **no** |
| C | `ARCADE_API=http://127.0.0.1:8799` | 52 | 1 | no |
| D | `ARCADE_API=…` **and** `DGD_DEMO=true` | 46 | 7 | **yes** |

Run B is the trap. It looks like the demo run. It reports *All tests passed*.
It executes **none** of the eight, including the one it appears to be for.

The cause is the skip expression at `test/arcade_api_test.dart:96`:

```dart
final needsDefine = loop && base.port != 8787
    ? null
    : 'needs --dart-define=ARCADE_API=http://127.0.0.1:<port> ...';
```

`needsDefine` is a **`??` prefix on every skip in the file**, so without
`ARCADE_API` nothing in it runs, whatever else is set. The demo test therefore
needs **both** defines.

That coupling is not a bug. The test asserts *zero requests*, and you cannot
prove zero without a listener to count arrivals — so it needs a live loopback
server precisely in order to watch nothing reach it. Correct design, easy to
misread.

**Why this matters.** §6 lists "a demo build makes zero requests" as an
invariant to check under fuzzing, and the shipped review build is a
`DGD_EMBED=demo` build. Until run D today, that invariant had never executed
in this project. Every `flutter test` reported in this session's earlier work
was a run A, and I reported those counts as if they were the gate. **They
were not.** The numbers were true; the claim they supported was weaker than I
implied.

**Recommended fix**, either or both:

1. Replace §4's wording with the exact commands — `flutter test
   --dart-define=ARCADE_API=http://127.0.0.1:8799` and the same plus
   `--dart-define=DGD_DEMO=true` — rather than "with the loopback and demo
   defines".
2. Make the run fail loudly instead of skipping quietly: a guard test that
   asserts `needsDefine == null`, so a run without the loopback define is red
   rather than green-with-skips.

Option 2 is the one that survives someone not reading the policy.

**State: OPEN.** No test asserts it yet; it is a policy and harness change,
not a product change.

---

## 2. What ran, and what it proves

### Flutter — client, against a loopback `FakeServer`

Run C, `ARCADE_API=http://127.0.0.1:8799`: **52 passed, 1 skipped.**

Exercised for the first time this session:

- `HOLDS RC1` — a build with no backend makes zero requests on refresh and
  level start, and a direct API call is refused **before any socket opens**.
- Concurrent `init()` registers exactly one anonymous player (the F4 fix).
- The local cache paints first and is then overwritten by the server, and **is
  never sent**.
- A 401 from any endpoint drops the identity; the next call registers afresh.
- **A malformed or wrong-shaped body surfaces as `ApiException`, never
  `TypeError`** — this is §1's fifth row, "parsing that rejects rather than
  coerces", tested against a hostile server rather than assumed.
- A server that never answers times out as offline and leaves the identity
  alone.

Run D, both defines: **46 passed, 7 skipped** — and the demo invariant ran.
A `DGD_EMBED=demo` build makes **zero requests** across cold start, refresh
and a level start, with a live listener counting.

### Server — v1, complete

```
test/redteam.test.ts    12 tests   12 pass   0 fail   0 todo
test/api.test.ts        18 tests   18 pass   0 fail   0 todo
```

**`0 todo` is the result that matters.** Policy §3 tags OPEN findings `todo`,
so zero todo means **no OPEN finding in the regression ledger** — which is the
§4 ship gate for the server.

Installed with `npm ci --ignore-scripts` from the lockfile, per §2.2. Two
packages, no vulnerabilities reported.

The ledger, in full:

| | | State |
|---|---|---|
| R1 | mini-game daily cap binds across UTC midnight | HOLDS |
| R2 | a mini-game score is whatever the client says, bounded only by caps | **ACCEPTED** |
| R3 | anonymous player creation throttled below the generic limiter | HOLDS |
| R4 | limiter admits no double burst at the window boundary | HOLDS |
| R5 | `X-Forwarded-For` ignored unless a proxy is trusted, last hop only | HOLDS |
| R6 | a tablet cannot be answered once its expedition is finished | HOLDS |
| R7 | a bank question vanishing between issue and answer is 4xx, not 500 | HOLDS |
| R8 | `status="xp_only"` means zero XP and is never set by the server | **ACCEPTED** |
| R9 | a corrupt server-written JSON column is handled, not a 500 | HOLDS |
| R10 | the board carries no ids or tokens; handle rerolls hit a daily cap | HOLDS |
| R11 | `/healthz` is the only unauthenticated read | HOLDS |
| R12 | CORS is a wildcard unless `ARCADE_CORS` is set, whatever `NODE_ENV` says | **ACCEPTED** |

---

## 3. For backend, before the service is exposed

Three accepted risks are live decisions, not settled ones, and hosting is when
they start to matter. Worth putting in front of whoever deploys.

- **R12 — wildcard CORS unless `ARCADE_CORS` is set.** On a service that
  issues bearer tokens, this is the one to fix at deploy time rather than
  after. It does not key off `NODE_ENV`, so a production deployment is not
  automatically safe.
- **`ARCADE_SECRET` is still unset.** It signs the single-use question tokens;
  with a default or empty value the server's authority over XP is decorative.
  R1–R11 all assume it is real.
- **R2 — mini-game scores are client-asserted**, bounded only by per-round and
  per-day caps. Accepted for the current games; worth re-reading before any
  game where a score is worth something.

---

## 4. Still not covered

Honestly, because a list of what a pass did not do is part of the pass.

- **Independence and reproducibility** — the two declared exceptions above.
  The reproducibility check in particular is mechanical and worth doing:
  rebuild from `bc8c614` in a clean container and compare entry by entry.
- **On-device traffic capture.** Not attempted. Under §2.2 it would need a
  stated exception, because the app's only endpoint is `digitalgold.co`. The
  loopback suites cover the client's *logic* against a hostile server, which
  is most of the value; what they do not cover is what the OS actually emits.
- **Device storage and logs.** Whether the credential prefs are encrypted at
  rest as intended, and whether anything sensitive reaches logcat. The backup
  exclusions were verified statically; their runtime effect was not.
- **Intent fuzzing of the exported `MainActivity`.** Crafted `?ref=` deep
  links beyond the single well-formed one tried during the API-33 fix.
- **v2 server suite.** Only v1 was run — v1 is what ships.
- **Dependency CVEs.** `npm ci` reported no advisories for the two server
  packages; the Flutter dependency tree was not scanned.

---

## 5. How to re-run

```bash
# client, loopback
cd puzzle-app
flutter test --dart-define=ARCADE_API=http://127.0.0.1:8799

# client, demo invariant — needs BOTH defines (see D1)
flutter test --dart-define=ARCADE_API=http://127.0.0.1:8799 \
             --dart-define=DGD_DEMO=true

# server, in a container, from the lockfile
cd arcade/v1/server
npm ci --ignore-scripts
node --test test/redteam.test.ts
node --test test/api.test.ts
```

---

*Related: `REDTEAM-POLICY.md`, `REDTEAM-1.0.5-2026-09-21.md` (static half),
`AUDIT-RC-2026-09-20.md` (RC1), `FOR-BACKEND-2026-09-21.md`.*
