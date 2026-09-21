# Merging the arcade into the main DGD app

> **The thing being merged is v1**, tagged `v1.0.0` and frozen. Source:
> `arcade/v1/app`, or clone `arcade/v1/dist/DGD-Arcade-v1.0.0.bundle` for the
> full history. Nothing from v2 is part of this merge. See `VERSIONS.md`.

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

## Correction, 2026-09-20 — the first version of this prompt was wrong

The prompt below originally asked for a Flutter project: `lib/`,
`pubspec.yaml`, `flutter --version`. **Their app is not Flutter**, and it was
not Flutter when that was written either.

The order of events matters, because it is the lesson. The prompt was written
before the APK arrived, on an assumption. The teardown a few hours later
(`APK-FINDINGS.md` §1) proved the assumption wrong — no `flutter_assets`, no
`libflutter.so`, Kotlin and Jetpack Compose throughout — and the prompt was
never revised to match. It went out asking a Kotlin team for a lockfile that
cannot exist, and their AI correctly refused to guess.

Their reply also answers the open question in `APK-FINDINGS.md` §6: **there is
an iOS app as well**, in Swift. The iOS guidance found inside the Android APK
was not a stray document; it belongs to a real second codebase.

A finding that invalidates a document already sent is not finished when it is
written down. It is finished when the document is fixed.

## What to send the other builder

They are building with an AI assistant and are not a developer — asking them
for build files by name will not land. So do not ask them for anything. Send
them a prompt to paste into their AI, and let the AI do the packaging.

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
> This project is being handed to another developer, who will embed a Flutter
> module — a games/arcade screen — inside it. Their module is Flutter; this
> app is native Swift and Kotlin. That is expected and supported, and it is
> why the questions below are about build configuration rather than features.
>
> Please do three things.
>
> **1. Package both platforms' source.** One zip with an `apple/` folder and
> an `android/` folder, or two zips. Include only what is needed to build.
>
> *Android*
> - the whole `app/src/` tree
> - every `build.gradle` or `build.gradle.kts`, plus `settings.gradle(.kts)`
>   and `gradle.properties`
> - `gradle/libs.versions.toml` if there is a version catalogue
> - `gradle/wrapper/gradle-wrapper.properties`
> - `proguard-rules.pro` and any `consumer-rules.pro`
> - `google-services.json` if it exists — and say so explicitly, so the other
>   side knows it is in there
>
> *Apple*
> - the whole Swift source folder and `Assets.xcassets`
> - the `.xcodeproj` and `.xcworkspace`
> - `Package.swift` and `Package.resolved`, or `Podfile` and `Podfile.lock`
> - `Info.plist` and any `.entitlements` file
>
> **Exclude these** — rebuildable, or must never be shared:
>
> - `build/`, `.gradle/`, `DerivedData/`, `Pods/`, `.idea/`, `xcuserdata/`
> - `local.properties`, `keystore.properties`, and any `.jks`, `.keystore`,
>   `.p12`, `.cer` or `.mobileprovision`
> - any `.env`, API key, password, service-account JSON or signing certificate
>
> Before zipping, **search both projects for hard-coded secrets** — API keys,
> tokens, passwords, database URLs — and list every file and line where you
> find them. **Do not remove them.** List them, so anything already exposed
> can be rotated.
>
> **2. Write a handover summary** as a separate text file.
>
> *Versions — these decide the schedule more than anything else*
> - Android: Android Gradle Plugin version, Gradle version, Kotlin version,
>   `compileSdk`, `minSdk`, `targetSdk`, and the Compose BOM version
> - Apple: Xcode version, Swift version, minimum deployment target, and
>   whether the UI is SwiftUI or UIKit
> - Whether Apple dependencies come from Swift Package Manager or CocoaPods
>
> *Structure*
> - Are Android and Apple in one repository or two?
> - The `applicationId` (Android) and bundle identifier (Apple), and whether
>   they are final
> - How many screens on each platform, and what each one is for
> - Is there a backend, or does the app call `digitalgold.co` directly?
> - Does either app store anything on the device, or collect personal data?
>
> *State of play — be blunt here*
> - Which of the two is further along?
> - Does the Apple app run? Does the Android app run?
> - What is broken, unfinished, or known not to work?
>
> **3. One specific diagnostic.** The Android build shared earlier did not
> function, and there is a likely cause worth ten minutes before anything
> else.
>
> Check whether your OkHttp client sends an **`Origin` header** on the request
> to `digitalgold.co/api/forms/stats`. The project's own `stats-source.json`
> states that a foreign `Origin` makes that endpoint return HTTP 500 — but
> that note was written for iOS `URLSession`, which omits `Origin` by default.
> OkHttp does not necessarily do the same. If an `Origin` is going out, every
> price fetch fails and the ticker simply has no data.
>
> Report what you find, plus the actual error or crash if there is one.
>
> Be blunt about what is unfinished. The receiving developer would far rather
> know now than discover it mid-merge.

---

### If they cannot produce a zip

Ask them for the folder the projects live in and have them share it by Drive or
Dropbox, minus the excluded items above. Failing that, a screen-share showing
the Android `build.gradle` and Xcode's version gets the facts that decide the
schedule.

## Why those questions matter

Two native codebases and one Flutter module is **add-to-app**, not a merge.
Flutter supports it on both platforms — the arcade becomes a screen inside
their app — but the constraints are theirs, not ours, which is why every
question above is about their build rather than their features.

**Android Gradle Plugin, Gradle and Kotlin versions** are the single biggest
predictor of effort. A Flutter module is added to an Android app as a Gradle
subproject, so their build has to be modern enough to accept it and to
tolerate Flutter's own AGP floor. If they are close to current this is
configuration; if they are years behind, their build gets upgraded first and
that can eat the whole schedule on its own.

**`minSdk`** has to be at least Flutter's floor. If theirs is lower, raising it
drops old devices — a product decision, not a technical one, and one somebody
at DGD has to actually make.

**SPM or CocoaPods** decides how painful iOS is. Flutter's documented iOS
embedding path goes through CocoaPods. A SwiftPM-only project can still do it,
via a pre-built `.xcframework`, but that is a different and less well-trodden
route. Worth knowing before anyone promises a date.

**One repository or two** decides whether this is one integration or two
parallel ones with separate review cycles.

**Their backend**, if any, decides whether we run two services or consolidate.
The arcade's is Node + SQLite and already handles XP, badges, streaks and the
weekly leaderboard. On present evidence the ticker has no backend — it computes
the price on the device, which is its own problem (`APK-FINDINGS.md` §4).

**Known-broken bits**, because inheriting someone's unfinished work without
being told is how a release slips at the last moment. Their Android build does
not currently run, and nobody has said why.

### The size cost, which nobody has priced yet

Embedding Flutter adds its engine to the host app: roughly **+15 MB on Android
and +20 MB on iOS**, on top of the arcade's own assets. Their ticker is
currently 18.8 MB. The combined app is a different object from either half, and
if anyone has a download-size expectation, now is when to say so.

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
