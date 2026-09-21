# Message to forward to the other builder

Everything below the line is for them. Nothing above it is.

The answer to their question is **A** — package the native Apple and Android
sources. The one thing to clear up first is the premise of their option B:
**the Flutter project is ours, not theirs.** They were not being asked to find
a Flutter app in their own repo. They were being asked to package theirs, so
ours can be embedded inside it.

That was our wording's fault, not their misreading. The original prompt said
"merged with a second Flutter app", which reads as though both halves are
Flutter. Fixed below.

---

Hi — thanks, and your AI is right. That was our mistake in how we asked, not
yours.

To clear up the confusion: **the Flutter project is on our side, not yours.**
We weren't asking you to find a Flutter app in your repo — we were asking you
to package yours, so that ours can be embedded into it as a screen. Your app
stays the app; the arcade becomes a part of it. Native Swift and Kotlin on your
side is exactly what we expected, and it is a supported setup.

So: **option A, please** — package the native Apple and Android sources.

One extra thing worth doing before anything else, because it may be a ten
minute fix rather than a week: the Android build you shared does not run, and
there is a specific likely reason. It is the last item in the prompt below.

Paste this into the same AI you have been building with, and send me whatever
it produces.

---

**PASTE THIS TO YOUR AI:**

This project is being handed to another developer, who will embed a Flutter
module — a games/arcade screen — inside it. Their module is Flutter; this app
is native Swift and Kotlin. That is expected and supported, and it is why the
questions below are about build configuration rather than features.

Please do three things.

**1. Package both platforms' source.** One zip with an `apple/` folder and an
`android/` folder, or two zips. Include only what is needed to build.

*Android*

- the whole `app/src/` tree
- every `build.gradle` or `build.gradle.kts`, plus `settings.gradle(.kts)` and
  `gradle.properties`
- `gradle/libs.versions.toml` if there is a version catalogue
- `gradle/wrapper/gradle-wrapper.properties`
- `proguard-rules.pro` and any `consumer-rules.pro`
- `google-services.json` if it exists — and say so explicitly, so the other
  side knows it is in there

*Apple*

- the whole Swift source folder and `Assets.xcassets`
- the `.xcodeproj` and `.xcworkspace`
- `Package.swift` and `Package.resolved`, or `Podfile` and `Podfile.lock`
- `Info.plist` and any `.entitlements` file

**Exclude these** — they are either rebuildable or must never be shared:

- `build/`, `.gradle/`, `DerivedData/`, `Pods/`, `.idea/`, `xcuserdata/`
- `local.properties`, `keystore.properties`, and any `.jks`, `.keystore`,
  `.p12`, `.cer` or `.mobileprovision`
- any `.env`, API key, password, service-account JSON or signing certificate

Before zipping, **search both projects for hard-coded secrets** — API keys,
tokens, passwords, database URLs — and list every file and line where you find
them. **Do not remove them.** List them, so anything already exposed can be
rotated.

**2. Write a handover summary** as a separate text file.

*Versions — these decide the schedule more than anything else*

- Android: Android Gradle Plugin version, Gradle version, Kotlin version,
  `compileSdk`, `minSdk`, `targetSdk`, and the Compose BOM version
- Apple: Xcode version, Swift version, minimum deployment target, and whether
  the UI is SwiftUI or UIKit
- Whether Apple dependencies come from Swift Package Manager or CocoaPods

*Structure*

- Are Android and Apple in one repository or two?
- The `applicationId` (Android) and bundle identifier (Apple), and whether they
  are final
- How many screens on each platform, and what each one is for
- Is there a backend, or does the app call `digitalgold.co` directly?
- Does either app store anything on the device, or collect personal data?

*State of play — be blunt here*

- Which of the two is further along?
- Does the Apple app run? Does the Android app run?
- What is broken, unfinished, or known not to work?

**3. One specific diagnostic.** The Android build shared earlier did not
function, and there is a likely cause worth ten minutes before anything else.

Check whether your OkHttp client sends an **`Origin` header** on the request to
`digitalgold.co/api/forms/stats`. The project's own `stats-source.json` states
that a foreign `Origin` makes that endpoint return HTTP 500 — but that note was
written for iOS `URLSession`, which omits `Origin` by default. OkHttp does not
necessarily do the same. If an `Origin` is going out, every price fetch fails
and the ticker simply has no data.

Report what you find, plus the actual error or crash if there is one.

Be blunt about what is unfinished. The receiving developer would far rather
know now than discover it mid-merge.
