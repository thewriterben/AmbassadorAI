# Merging the arcade into the main DGD app

Written 2026-09-18, against a proposed Monday submission.

## The short version

**An APK cannot be merged.** Flutter release builds compile Dart to native ARM
machine code inside `libapp.so`. The images, sounds and Android manifest survive
decompilation; not one line of the app's logic does. A merge needs the other
app's **source**.

**The arcade was built to be embedded.** There is a `DGD_APP_TAB` compile-time
flag already threaded through it, and the celebration behaviour already keys off
it — fireworks and the spoken winner line are suppressed in-app, because the
arcade plan's §4.3 bars prize-style celebration inside the DGD app. Embedding is
the designed path, not a retrofit.

**Monday is not a merge problem.** See "What actually gates submission" below.

---

## What to send the other builder

They are building with an AI assistant and are not a developer — asking them for
a `pubspec.lock` will not land. So do not ask them for anything. Send them a
prompt to paste into their AI, and let the AI do the packaging.

Send this message:

---

> Hi — we are combining your DGD app with the arcade module so they ship as one
> app. To do that, the developer on my side needs your project's **source
> files**, plus a few facts about how it is set up.
>
> You do not need to work any of this out yourself. **Paste the text below into
> the same AI you have been building the app with**, and it will do it. Then
> send me whatever it produces.
>
> ---
>
> **PASTE THIS TO YOUR AI:**
>
> I need to hand this project over to another developer so it can be merged
> with a second Flutter app. Please do two things.
>
> **1. Package the source for handover.** Create a zip of this project
> containing only what is needed to build it:
>
> - `lib/` in full
> - `pubspec.yaml` and `pubspec.lock`
> - `android/` and `ios/`
> - `assets/` or wherever images, fonts and audio live
> - `analysis_options.yaml`, `README`, and any other top-level config
>
> **Exclude these** — they are either rebuildable or must never be shared:
>
> - `build/`, `.dart_tool/`, `.idea/`, `node_modules/`, `Pods/`
> - `android/key.properties`, and any `.jks`, `.keystore` or `.p12` file
> - any `.env`, API key, password, service-account JSON or signing certificate
>
> Before you zip it, **search the project for hard-coded secrets** — API keys,
> tokens, passwords, database URLs — and tell me every file and line you find
> them in. Do not remove them; just list them so we can rotate anything that has
> been exposed.
>
> **2. Write a short handover summary** answering these, as a separate text file:
>
> - The exact output of `flutter --version`
> - Every package in `pubspec.yaml`, with its version
> - Is there a backend or API? What language, where is it hosted, and does the
>   app talk to it directly?
> - What is used for state management and for navigation?
> - Roughly how many screens, and what is each one for?
> - Does it store anything on the device or collect any personal data?
> - What is currently broken, unfinished or known not to work?
> - Is the app ID (`applicationId` in `android/app/build.gradle`) final, and
>   what is it?
>
> Be honest about what is unfinished. The receiving developer would much rather
> know now than discover it during the merge.

---

### If they cannot produce a zip

Ask them for the folder their project lives in and have them share it by Drive
or Dropbox, minus the excluded items above. Failing that, a screen-share where
they open `pubspec.yaml` and run `flutter --version` gets us the two facts that
decide the schedule.

## Why those questions matter

**The Flutter version** is the single biggest predictor of how long this takes.
The arcade is on **3.47.2**. If they are close, the merge is mostly mechanical.
If they are several majors behind, one project has to be migrated first, and
that can eat the whole schedule on its own.

**`pubspec.lock`** tells me whether our dependency sets can coexist. Two Flutter
apps that each work perfectly can be impossible to merge without upgrades if
they pin incompatible versions of a shared package. This is the classic way a
"two-day merge" becomes two weeks, and it is knowable in ten minutes from the
lockfile.

**Their backend**, if any, decides whether we run two services or consolidate.
The arcade's is Node + SQLite and already handles XP, badges, streaks and the
weekly leaderboard.

**Known-broken bits** because inheriting someone's unfinished work without being
told is how a release slips at the last moment.

## What actually gates submission

The merge is unlikely to be the long pole. These are, and most are not started:

| Blocker | Owner | Status |
|---|---|---|
| Privacy policy hosted, five blanks filled | DGD | Draft written, blanks empty |
| Financial-products sign-off | DGD compliance | Not started |
| Content rating questionnaire | DGD compliance | Draft answers ready |
| Signup CTA legal review | DGD legal | Not started |
| Signing model chosen, keys available | DGD | Undecided — three options in `MEETING-BRIEF.md` §1.1 |
| Backend hosted, real secret set | DGD | Runs only on the build PC |
| Store listings created | DGD | Copy and graphics ready in `STORE-LISTING.md` |

And the one people forget: **first-time review takes days on both stores.**
Submitting on Monday is achievable. Being *live* on Monday is not. If the
financial-products answer is wrong, a rejection costs another cycle.

## A shape worth considering instead

Rushing two codebases together in four days, one of them unseen, to hit a date
that store review will not honour anyway, is how avoidable bugs ship.

The alternative: **submit the arcade as its own app now** — it is finished,
tested and has its listing copy written — and fold it into the main app as a tab
in the next release. Two submissions instead of one, and the first one is ready
today rather than maybe-Friday.

That is a product call, not a technical one. But it is worth having on the table
before Monday becomes the reason for shortcuts.
