# Review of the Digital Gold native source

Handed over 2026-09-20. Source at `C:\src\dgd-native`, originals in
`F:\Documents\dgdappsource`. **Since 2026-09-20 that folder is a git
repository**: tag `as-delivered-2026-09-20` is the zip byte for byte, tag
`integrated-2026-09-20` (`7598533`) is everything done since, in three commits.

Monorepo `github.com/dogbones41/digital-gold-ticker`, two branches:

| | Branch | Tip |
|---|---|---|
| Apple | `apple-2` | `1d3755efb9c76db6bcf0edfb6e67ed39673b030c` |
| Android | `android-2` | `02bbbdb4cc8e7738f9f08def0a0624e22e8e6449` |

## Verdict on the handover itself

**Complete, accurate and clean.** Every claim in their summary that I could
check against the source, checked out — including the ones that contradicted
me. This is a better handover than most professional ones.

Their OkHttp answer deserves particular credit: my `Origin`-header hypothesis
was wrong, and they did not merely assert it. `LiveStatsClient` sets only
`Accept`, registers no interceptors, and there is a MockWebServer unit test,
`doesNotSendOriginHeader`, asserting the header is absent on the wire. That is
how you refute a hypothesis.

**So the dead ticker is still unexplained.** The remaining candidate from
`APK-FINDINGS.md` §5 is the one they name: the APK I analysed was commit
`92fd68c`, and the current tip is `02bbbdb`. Re-test before spending anything
on networking.

## Verified against the source, not the summary

| Claim | Verified |
|---|---|
| AGP 8.7.3 | ✅ `build.gradle.kts` |
| Gradle 8.11.1 | ✅ `gradle-wrapper.properties` |
| Kotlin 2.0.21 | ✅ |
| compileSdk 35 / minSdk 26 / targetSdk 35 | ✅ `app/build.gradle.kts` |
| Compose BOM 2024.12.01 | ✅ |
| Java 17 source/target | ✅ |
| iOS deployment target 17.0 | ✅ `project.yml` |
| SwiftUI, not UIKit | ✅ |
| Neither SPM nor CocoaPods | ✅ no `Package.swift`, no `Podfile`, anywhere |
| One repo, two branches | ✅ |
| `com.digitalgold.ticker` both platforms | ✅ |

**Independent secret scan: clean.** I ran my own rather than taking theirs on
trust — credential patterns, excluded-file check, and every host either binary
references. The single pattern hit was the literal string `BEGIN PRIVATE KEY`
inside their own scan report, describing what they searched for. No keys, no
certificates, no `local.properties`, no keystores. Nothing needs rotating.

One curiosity, not a problem: `digitalgoldx.com` and
`explorer.digitalgoldx.com` appear in the bundled `stats-source.json` and
`DATA_SOURCE.md` as documented aliases of `digitalgold.co`. No code calls
them. Worth knowing the alias exists; not worth acting on.

---

# The headline: the merged app has a category problem

This is the most consequential thing in the delivery, and it is not in their
summary because from where they sit it is not a problem at all.

**Their app is a Finance app, and they have already declared it one.**

- `project.yml`: `INFOPLIST_KEY_LSApplicationCategoryType:
  public.app-category.finance`
- `APP_STORE_REVIEW_NOTES.md`: "**Category:** Finance (informational ticker /
  network stats)"

**They have also already written a defence against Apple Guideline 3.1.5(v)** —
the rule that apps may not reward users with cryptocurrency for completing
tasks such as downloading apps, inviting others, or posting to social
networks. Their review notes carry a dedicated section headed *"What the app
does not do (Guideline 3.1.5(v) and related)"*, and a further *"Reviewer
talking points (3.1.5(v))"* at the end.

Now put the arcade inside that binary. The arcade awards XP and badges for
playing games, and ranks players on a weekly leaderboard.

Our position has always been that XP is not currency, has no monetary value,
and cannot be exchanged for anything. **I still believe that is correct and
defensible.** What changes is who has to defend it, and against what
background. A reviewer assessing "play games, earn points, climb a board"
inside an app that displays a live USD price for a cryptocurrency, in the
Finance category, with a referral system that encodes `?ref=USERNAME`, is
being asked a materially harder question than either half asks alone.

Two specific consequences:

**One app gets one primary category.** Finance or Games. Finance keeps their
existing positioning and puts a game catalogue somewhere reviewers do not
expect one. Games inverts it and puts a live crypto price inside a game. Both
are answerable; neither is obvious; nobody has picked.

**Their reviewer notes become our problem, and our disclaimers become
theirs.** Their submission states the app "does not award currency in-app".
That sentence has to survive the arcade being in the same binary. It does —
XP is not currency — but somebody at DGD has to be confident enough to sign
their name under it.

### One line in their notes is worth asking about

> "No $21 / $42 / 2× amounts."

That reads like a scar. It implies an earlier version showed dollar figures
for invites and they were removed. If that came out of an actual App Store
rejection, the rejection letter is the single most valuable document nobody
has shown us — it tells us exactly where this reviewer team draws the line.
**Ask.**

### It is also no longer just a ticker

`APK-FINDINGS.md` §3 was written against a ticker-only APK. The current tips
have grown:

- membership credentials capture — username, email, password
- password stored in Keychain (Apple) and EncryptedSharedPreferences (Android)
- a QT wallet receive address, view-only
- invite and referral with QR codes and social share

Their summary is clear that none of it posts to `digitalgold.co` — it is a
local preview pointing people at the website. But it means the privacy
declarations in `PRIVACY-DRAFT.md` and `STORE-LISTING.md` are now understated
on two counts, not one: financial info **and** stored credentials.

---

# Add-to-app: what it actually takes

## Android — one real obstacle, and it is not obvious

`settings.gradle.kts` sets:

```kotlin
repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
```

Flutter's published add-to-app instructions tell you to add Flutter's artifact
repository (`https://storage.googleapis.com/download.flutter.io`) to the app
module's own `repositories { }` block. **That is precisely what this setting
forbids**, and the resulting error does not mention Flutter.

The fix is small — declare the Flutter repository in
`dependencyResolutionManagement` in `settings.gradle.kts` instead — but it is
an afternoon lost to a confusing message if you do not know it going in. It is
the single most useful thing I found in their build files.

Everything else on Android is favourable:

- **minSdk 26 clears Flutter's floor with room to spare.** No product decision
  about dropping old devices. I had flagged this as a likely blocker before
  seeing the source; it is not one.
- AGP 8.7.3 and Java 17 are both comfortably inside Flutter's supported range.
- No version catalogue, so dependency edits are local to one file.

## Apple — no dependency manager at all, which is better than it sounds

No `Podfile`, no `Package.swift`, and **zero third-party iOS dependencies**.
The project is generated from `project.yml` by XcodeGen, with a checked-in
`pbxproj` so it opens without it.

This rules out the obvious route and points at the better one:

**Do not adopt CocoaPods.** Flutter's documented iOS path integrates through
CocoaPods, which works by rewriting the `pbxproj` and creating a workspace.
Here the `pbxproj` is *generated* — every `xcodegen generate` would silently
discard the Pods integration. That is a trap that would be discovered weeks
later by someone who did not set it up.

**Use `flutter build ios-framework` instead.** It emits `.xcframework`
bundles, which can be declared directly in `project.yml` and therefore survive
regeneration, because `project.yml` is the source of truth. For an XcodeGen
project this is not a workaround; it is the cleaner fit.

The cost is that the frameworks must be rebuilt whenever the arcade changes.
For a module that ships on its own cadence, that is acceptable — and it makes
the arcade a versioned artefact rather than a live source dependency, which is
arguably what we want anyway.

Other iOS notes:

- `TARGETED_DEVICE_FAMILY: 1` — **iPhone only, no iPad.** The arcade is
  portrait-locked, so this is consistent, but it is a product decision
  somebody made and should know they made.
- iOS 17.0 minimum is far above Flutter's floor. No constraint.

## Size, still unpriced

Embedding the Flutter engine adds roughly **+15 MB on Android and +20 MB on
iOS**, before the arcade's own assets. Their ticker APK was 18.8 MB. If anyone
has a download-size expectation, now is the time to say it out loud.

---

# I could not build it here, and the reason is mine not theirs

The only JDK on this machine is the one bundled with Android Studio: **OpenJDK
25.0.3**. Their build fails on it:

```
java.lang.IllegalArgumentException: 25.0.3
    at org.jetbrains.kotlin.com.intellij.util.lang.JavaVersion.parse
    ...
    at org.gradle.initialization.ScriptEvaluatingSettingsProcessor.applySettingsScript
```

**Gradle 8.11.1's embedded Kotlin DSL compiler cannot parse a two-digit Java
version.** It fails while compiling `settings.gradle.kts`, before any of their
code is touched. Nothing is wrong with their project — their CI builds it and
their unit tests pass.

Recording two wrong guesses I made getting to that, because the pattern is the
point:

1. I assumed it was a Gradle-versus-Java ceiling and bumped **Kotlin** to
   2.1.21. Failed identically.
2. I bumped Kotlin again, to 2.2.20. Failed identically.

Both were wrong for the same reason: the stack trace said
`applySettingsScript`, which is Gradle's *own* embedded Kotlin, fixed by the
Gradle version and untouched by any plugin version in `build.gradle.kts`. The
answer was in the first trace I read. I changed things before I finished
reading it — the same mistake as the Mac toolchain session.

Their source has been reverted to exactly as delivered.

**To actually run their Android app on the Pixel, this machine needs a JDK 21
or 17 alongside the existing one.** That is a five-minute install and it is
worth doing, because their team has no Android hardware — nobody has run this
build on a real device yet, and "does it work" is still open.

---

# What to ask them next

1. **Was there an App Store rejection behind "No $21 / $42 / 2× amounts"?**
   If so, send the rejection letter.
2. **Finance or Games for the merged app?** A DGD decision, needed before
   anything is submitted, and it is upstream of the store listing copy that is
   already written.
3. **Re-test the Android build on tip `02bbbdb`** — or send me a JDK-compatible
   build and I will test it on the Pixel.
4. Nothing else. The handover gave us everything else we asked for.

---

*See `MERGE.md` for the handover prompt and the submission blockers,
`APK-FINDINGS.md` for the original teardown, and `VERSIONS.md` for which
arcade version is the merge candidate — it is v1, frozen, tagged `v1.0.0`.*
