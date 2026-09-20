# DGD Arcade — red-team directive

> **Paranoid security is the standing posture, not a phase.** When two
> implementations are plausible, pick the one that assumes the attacker already
> controls the input, the disk, the clock and the previous round. Re-derive
> trust from the reference *source* at a pinned commit, never from a working
> copy, a summary or memory; verify against the running artefact, never against
> what it "should" do. **Every milestone gets an independent adversarial pass
> whose only job is to break it, run in a clean room that did not write the
> code.** Prefer the smaller, more boring, more defensive option; cleverness we
> cannot audit is a liability. When a choice trades speed or convenience for a
> guarantee against adversarial input, take the guarantee.

This file is the policy. Audits point here instead of restating it. Where an
audit departs from it, the audit says so in its header and says why.

## 1. Threat model

The pass is not only bug hunting. It asks whether the artefact does anything
it should not, and it names who would have put that there:

| Attacker | What they control | What the pass therefore checks |
|---|---|---|
| A player | Every byte the client sends, the clock, the device | Server-side authority for XP, tokens, caps, rate limits; nothing trusted from the client |
| A contributor, or the AI that writes the code | Any diff | Every change reviewed against its stated intent; code not needed for the intent is a finding even when harmless |
| A dependency | Install scripts, lockfile drift, a substituted package | Lockfile-only installs with scripts disabled; unexplained lockfile changes are findings |
| The toolchain or a hand-copied mirror | The gap between source and binary | Reproducible builds; the shipped artefact must match a clean-room rebuild byte for byte |
| A hosted service we call | Every response | Parsing that rejects rather than coerces; no behaviour keyed on a response we do not validate |

The intentionally placed breach is the third, fourth and fifth rows. Fuzzing
does not find it; provenance, enumeration and diff-scoped review do.

## 2. Clean room

1. **Start from a commit hash.** The runner creates a detached worktree at the
   hash, never at a branch name and never from the working copy. Third-party
   code enters as a commit in their repository or a signed tag, not as a zip.
   Where only a zip exists, its hash is recorded and the zip is the reference.
2. **No network except loopback.** Installs come from lockfiles with integrity
   checks and install scripts disabled. A build step that wants the network is
   a finding. Dynamic runs talk only to an in-process fake server.
3. **Reproduce the artefact.** Rebuild it from the pinned source with a fresh
   dependency cache and compare entry by entry with the shipped file. Any
   difference in the manifest, resources or assets fails the run; any
   difference in code is reviewed, and only D8's incremental-build checksum
   line is an accepted explanation.
4. **Enumerate, then account.** Every route, environment flag, host,
   permission, exported component and debug-only path is listed by the runner
   and must map to a line in the spec or become a finding.
5. **Nothing is touched.** No fixes are applied in the pass beyond test
   fixtures. No traffic to `digitalgold.co`, the DGD App or any hosted service
   without a stated exception in the audit header. Third-party source is never
   modified. The worktree and caches are deleted afterwards.
6. **Independence.** The pass runs in a session that did not write the code,
   given only the artefact, the spec and the previous audit.

## 3. Findings

- **Every finding gets a stable ID** (`R7`, `A1`, `N3`) that carries across
  audits, a severity (HIGH, MEDIUM, LOW, INFO) and one of three states in
  `test/redteam.test.ts`:
  - **OPEN** — the test asserts the secure behaviour and is tagged `todo`. It
    stays green while the hole exists and flips to a passing todo when a fix
    lands; that flip is the signal to drop the tag and close the finding.
  - **ACCEPTED** — a behaviour we have chosen to live with. The test states
    exactly what it is and must keep passing. Acceptance is a signed decision,
    not a default.
  - **HOLDS** — a property that should already hold. A hard regression test.
- **Every finding is a test or a recorded reproduction.** A finding that cannot
  be reproduced is a note, not a finding.
- **Severity decides the gate**, below. Fixing is a separate change with its own
  review, recorded in the audit header as a fix pass.

## 4. Gates

- **Ship gate.** Nothing ships with an OPEN finding at HIGH, or an artefact the
  clean room could not reproduce, or a suite that was not run with its defines.
- **Exemption gate.** Every waiver (the bank `ALLOWLIST.md`, a lint exemption, an
  accepted finding) needs two named sign-offs. An unreviewed waiver is the
  cleanest place to hide a bypass; `reviewer: unreviewed` is itself a finding.
- **CI gate.** Both server suites, both Flutter suites *with* the loopback and
  demo defines, and the analyzer. A plain `flutter test` skips the network
  layer silently and reports green; that run does not count.
- **Branch gate.** `main` is protected; commits are signed; a mirror copied by
  hand is not a source of truth and will drift.

## 5. What an audit header must say

Scope and authorisation. The commit hash. Which suites ran, with which defines,
and the counts. Any exception to §2 and why. What was fixed the same day and
what was not. How to re-run. Then the findings, ordered by what blocks what.

## 6. Checklist for the adversarial pass

Run every time, whatever the change was:

- Routes: enumerated from the source, each crossed with unauthenticated,
  another user's token, an expired token, a forged signature.
- Flags: every `process.env` and every `--dart-define` read, and what each one
  unlocks. A flag that widens behaviour in a release build is a finding.
- Hosts: every URL in the app's own code and in the artefact. Anything off the
  allowlist is a finding.
- Secrets: anything key-, token- or certificate-shaped in source or artefact.
- Shapes of intent: auth paths skipped on a header, flag or date; compares that
  are not constant-time; base64 or hex blobs; install scripts; build plugins
  without a reason; date comparisons that change behaviour later.
- Invariants under fuzzing, not examples: XP changes only through a
  server-issued token; caps bind across a UTC day boundary; a demo build makes
  zero requests.
- The diff, read against its stated intent, by someone who did not write it.

## 7. How to run

```
arcade/tools/redteam.sh --ref <commit> --mirror v2
arcade/tools/redteam.sh --ref <commit> --mirror v1 --apk arcade/v1/dist/DGD-Arcade-v1.0.0-demo.apk
arcade/tools/redteam.sh --ref <commit> --native-zip <delivered.zip> --native-patch arcade/dgd-native-fix --apk arcade/dgd-native-fix/DigitalGold-Android-FIXED-debug.apk
```

The runner writes a report under `arcade/redteam-runs/` and exits 0 on pass,
2 when something needs a human read, 1 on failure. Its report is an input to
the audit, not the audit.

*Earlier audits: `AUDIT-2026-09-16.md`, `AUDIT-2026-09-18.md`,
`AUDIT-NATIVE-FIX-2026-09-20.md`. The regression ledger is
`v*/server/test/redteam.test.ts`.*
