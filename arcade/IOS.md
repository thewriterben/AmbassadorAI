# iOS — getting DGD Arcade onto an iPhone

Written 2026-09-17, with a MacBook Air in hand. Everything below that says
"needs you" needs you because I am on the Windows PC and cannot drive the Mac.

There are two different goals here and they cost very different things.

| | What it takes | Cost | Time |
|---|---|---|---|
| **It runs on your own iPhone** | The Mac, Xcode, a free Apple ID | £0 | An afternoon, mostly downloads |
| **Other people can install it** | Apple Developer Program, TestFlight | $99/year | Days to weeks if enrolling as DGD |

The first needs nothing from anyone else and is worth doing first — it tells us
whether the app actually works on iOS before a penny is spent.

---

## Already done — I checked all of these

| | |
|---|---|
| Bundle ID | `co.digitalgold.arcade` — set, matches Android |
| Display name | `DGD Arcade` |
| Deployment target | iOS 15.0, so iPhone 6s and later |
| `ios/Runner` scaffold | Complete, untouched since `flutter create` |
| Plugins | shared_preferences, url_launcher, audioplayers, http, flame — all support iOS |
| **App icon** | **Was still the stock Flutter logo.** Fixed 2026-09-17 |

The icon is worth a note. `install_app_icon.py` wrote Android's adaptive,
legacy and themed mipmaps, the Play listing icon and the PWA set, but never
touched iOS — so the home screen icon and the TestFlight listing would both
have been the blue Flutter chevron. `tools/gen_ios_icon.py` now writes all 15
sizes from the same `assets/app_icon.png`, flattened onto the `#0E0D0C` plate.
Two iOS-specific rules it follows: **no alpha anywhere**, because iOS rejects
transparent app icons and validates the 1024 at upload, and **no rounded
corners of our own**, because iOS applies its own mask and a baked-in radius
leaves a pale halo inside it.

## What the MacBook needs

**Xcode 26 or newer is not optional any more.** Apple's requirement to build
with Xcode 26 and the iOS 26 SDK for App Store Connect uploads took effect on
28 April 2026, which has passed.

**Corrected 2026-09-17.** An earlier version of this file said macOS 14.5
Sonoma was enough. That was wrong and the floor is higher:

| Xcode | Minimum macOS |
|---|---|
| 26.0–26.3 | macOS 15.6 Sequoia |
| 26.4–26.6 (current stable) | macOS 26 Tahoe 26.2 |
| 27 (release candidate) | macOS 26 Tahoe 26.6 |

The Mac App Store only ever offers the *newest* Xcode, so on an older macOS it
refuses to install rather than offering an older build. Older Xcode versions are
downloadable from developer.apple.com/download/all with an Apple Developer
account — DGD has one — but nothing below Xcode 26 can be uploaded to App Store
Connect, and even Xcode 26.0 needs macOS 15.6.

Also needed: **about 40 GB free**, more with simulators. That is the one that
catches people out on a 256 GB Air.

**If the Mac cannot reach macOS 15.6**, it cannot build a submittable iOS app at
all, and the options are a newer Mac or a hosted macOS build service. See
"If the Mac is too old" below.

**Flutter must match this PC: 3.47.2, stable.** A different version on the Mac
will resolve different package versions and you will be debugging the toolchain
instead of the app.

One piece of good news: Flutter 3.44 and later use Swift Package Manager rather
than CocoaPods for iOS dependencies, so the usual CocoaPods-and-system-Ruby
mess is probably avoidable. If a plugin still needs CocoaPods it works fine —
just note the CocoaPods registry goes read-only on 2 December 2026, so it is
not a long-term answer.

## Step 1 — get the code onto the Mac

This is where the version-control loose end stops being cosmetic.

**With git** (recommended, ~1 minute): I put `C:\src\puzzle-app` under git,
push to a private repo, you `git clone` on the Mac. After that, changes flow
both ways with one command and both machines stay in step. Given we are about
to build ten games across two platforms, this is the right answer regardless.

**Without git**: zip the folder, move it by USB or Drive, and hand-carry every
change afterwards. Workable once; miserable as a habit, and it is how two
machines quietly drift out of sync.

## Step 2 — on the Mac, once

```sh
# 1. Xcode from the App Store. Open it once, accept the licence, let it
#    install the extra components it asks for.
sudo xcodebuild -runFirstLaunch

# 2. Flutter 3.47.2 — match the PC exactly.
#    Download the macOS stable 3.47.2 bundle, unzip, then add to PATH.
export PATH="$HOME/flutter/bin:$PATH"

flutter --version        # expect 3.47.2, Dart 3.13.2
flutter doctor           # fix anything it flags for iOS
```

## Step 3 — run it on your iPhone, free

```sh
cd <wherever the project landed>
flutter pub get
open ios/Runner.xcworkspace
```

In Xcode: select **Runner** in the sidebar → **Signing & Capabilities** → tick
*Automatically manage signing* → under *Team*, add your personal Apple ID and
pick it. Xcode will create a free provisioning profile.

Then plug in the iPhone, unlock it, tap **Trust** on the prompt, and:

```sh
flutter devices          # the iPhone should be listed
flutter run --release
```

First launch will refuse with an untrusted-developer error. On the phone:
**Settings → General → VPN & Device Management** → your Apple ID → **Trust**.

**Free provisioning expires after 7 days.** The app stops launching and you
re-run the command. That is fine for "does it work", useless for handing to
anyone.

## Step 4 — other people (needs the paid program)

$99/year, individual or organisation. The number that is sometimes quoted as
$299 is the Apple Developer *Enterprise* Program, which is for internal-only
distribution inside a company and is not what we want.

**The thing with lead time:** enrolling as an organisation — so the App Store
listing says *Digital Gold* and not *Benjamin Snider* — requires a legal entity,
a D-U-N-S number for it, and Apple verifying both. If DGD does not already have
a D-U-N-S, getting one takes days, and Apple's review adds more. This is the
same class of blocker as the Play developer account, and it is worth starting
both at once.

Once enrolled, TestFlight is the iOS equivalent of Play internal testing:
builds go to App Store Connect, testers install through the TestFlight app.
Same declarations as Play — privacy policy URL, age rating, data collection —
so `PRIVACY-DRAFT.md` covers both.

## What I actually expect to break

Not the build. The build will almost certainly just work — it is the same Dart,
and Flame and Flutter are platform-agnostic.

**Audio is the real risk, and it is not a small one.** The entire audio engine
was written against Android and tuned on it: one persistent player per file,
SoundPool low-latency mode, an audio focus context set to `mixWithOthers`, and
`ReleaseMode.stop`. iOS has none of those concepts — it uses AVAudioPlayer
under an AVAudioSession with completely different category and activation
semantics. The specific things to check on the phone, in order:

1. **Does the ringer/silent switch mute the game?** Depending on the session
   category iOS will silence everything when the switch is flipped. Players
   will not connect the two and will report it as broken audio.
2. **Re-run the soak.** The 10-minute drift test that just passed at 1.02× on
   Android proves nothing about iOS — different player, different pool, a
   different leak surface. It is in the DEV build already; run it there.
3. **Latency on first play.** iOS often has a long first-touch delay per sound
   unless the session is pre-warmed.

**Smaller things:** haptics map to different iOS feedback generators, so the
heavy impacts may feel wrong or do nothing; the Dynamic Island and home
indicator need a look on the Flame game surface, which draws outside the
widget-level `SafeArea`.

## If the Mac is too old

A MacBook Air that cannot reach macOS 15.6 cannot produce a submittable iOS
build, and no amount of fiddling changes that. Three ways round it, cheapest
first:

1. **Update macOS, if the hardware allows it.** Any Apple Silicon Air (M1, 2020
   onward) runs Tahoe. Intel Airs from 2018–2020 can generally reach Sequoia
   15.6, which is enough for Xcode 26.0–26.3 but not the later points. Anything
   older is a dead end.
2. **A hosted macOS build service** — Codemagic, Bitrise, GitHub Actions macOS
   runners, MacStadium. These build and sign iOS apps in the cloud from the
   repo, with no Mac in the room. Given DGD already has the Apple Developer
   account, this is genuinely viable and is worth asking the publishing team
   whether there is already a CI budget or account. It also solves the problem
   permanently rather than until the next macOS floor moves.
3. **A newer Mac.** A base Mac mini is the cheapest machine that will build iOS
   for years.

Option 2 is the one I would raise in the meeting, because it is a procurement
question with a lead time and the team may already have an answer.

## Suggested order

1. Say yes to git, so the code can move.
2. Tell me the Mac's model and macOS version.
3. You do Steps 2 and 3 — I will give exact commands and read any output you
   paste back.
4. Run the audio soak and the silent-switch check, and send me what you see.
5. Only then decide about the $99 and the D-U-N-S.
