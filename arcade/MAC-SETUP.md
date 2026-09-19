# Mac setup — copy-paste run sheet

> ## A correction, 2026-09-17 — Xcode 27 is NOT the problem
>
> An earlier version of this file said, in bold, that Flutter could not build
> for iOS on macOS 27 with Xcode 27, citing flutter/flutter#192803. **That was
> wrong**, and it is worth recording how the mistake was made because it cost an
> evening and a 15 GB download.
>
> What actually happened: `flutter run` failed, the error was never read, and I
> proposed a diagnosis from a single *closed* GitHub issue with no comments and
> no confirmed fix. Then I recommended downgrading to Xcode 26.6 — which macOS
> 27 refuses to run, something I asserted was fine without checking. Two
> assumptions stacked on one unread error message.
>
> **`flutter doctor -v` on the actual machine said:**
>
> ```
> [!] Xcode - develop for iOS and macOS (Xcode 27.0)
>     • Xcode at /Applications/Xcode.app/Contents/Developer
>     ! CocoaPods not installed.
> [✓] Connected device (1 available)
>     • macOS (desktop)
> ```
>
> Xcode 27 detected cleanly. Two real problems, both ordinary:
>
> 1. **No iOS simulator was booted**, so Flutter reported "No supported devices
>    connected" and listed only macOS. That is what the failure actually was.
> 2. **CocoaPods is not installed.** It may not even matter here —
>    `enable-swift-package-manager` is on in this install, so Flutter uses SPM
>    for plugins that support it — but it is the one genuine gap in the
>    toolchain.
>
> **The lesson, written down so it is not repeated: read the error before
> proposing the fix.** Every minute spent guessing cost more than the question
> would have.
>
> Android was never affected by any of this.


Xcode is installed. This gets the code onto the Mac and DGD Arcade onto an
iPhone. About 45 minutes, most of it the Flutter download.

Paste each block, read the output, move on. If anything errors, stop and send me
the output rather than working around it — a wrong fix here costs more than the
question.

---

## 1. Move the code across — 2 minutes

`arcade/dist/puzzle-app.bundle` (11.5 MB) is a **git bundle**: the entire
repository, all history, in one file. No accounts, no remote, no network.

Get it onto the Mac however is easiest — USB stick, Drive, Dropbox, iCloud. Then:

```sh
cd ~
git clone ~/Downloads/puzzle-app.bundle puzzle-app
cd puzzle-app
git log --oneline
```

Expect two commits, the newest being the full-screen celebration work.

That clone leaves the bundle configured as the `origin` remote, which is a file
that will not exist on this Mac forever. Clear it so nothing tries to fetch from
it later:

```sh
git remote remove origin
```

When you settle on a real remote, `git remote add origin <url>` on either
machine and push.

## 2. Flutter — 15–20 minutes, mostly download

**It must be 3.47.2.** A different version resolves different package versions
and you end up debugging the toolchain instead of the app. The PC is on
3.47.2 / Dart 3.13.2.

Download the macOS stable 3.47.2 bundle from docs.flutter.dev — pick the
**Apple Silicon** build unless the Mac is Intel — then:

```sh
cd ~/development                     # or wherever you keep tools
unzip ~/Downloads/flutter_macos_*.zip
export PATH="$HOME/development/flutter/bin:$PATH"
echo 'export PATH="$HOME/development/flutter/bin:$PATH"' >> ~/.zshrc

flutter --version
```

Expect `Flutter 3.47.2 • channel stable` and `Dart 3.13.2`. If it says anything
else, stop — everything after this assumes those numbers.

## 3. Let Xcode finish setting itself up — 2 minutes

Opening Xcode once is not enough; the command-line side needs its own nudge.

```sh
sudo xcodebuild -runFirstLaunch
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
flutter doctor
```

`flutter doctor` will tell you exactly what iOS-side pieces are missing. Android
items can be ignored — that side lives on the PC.

## 4a. No iPhone to hand? Use the Simulator — skip straight to this

**A physical iPhone is not required, and the Simulator needs no Apple ID, no
signing team and no Trust dance.** Simulator builds are never signed, so step 4
below can be skipped entirely tonight.

**Xcode 27 moved the Simulator.** `open -a Simulator` and the old path inside
`Xcode.app/Contents/Developer/Applications/` both fail — there is no
Simulator.app to open any more. It now lives in Xcode under:

> **Xcode → Open Developer Tool → Device Hub → Simulator**

Boot an iPhone from there first. Then:

```sh
cd ~/puzzle-app
flutter run
```

**No `--release` on a simulator.** Flutter refuses it — "Release mode is not
supported by iPhone 16 Pro" — because release builds are ahead-of-time compiled
for real device hardware and a simulator is not that. Debug is the only mode
that runs there.

That costs nothing for what we want from the Simulator: layout, navigation and
proof it builds all look the same. It does mean **frame rate is not
representative** — debug mode is slow by design, so do not read anything into
how the animations feel. The app already sets `debugShowCheckedModeBanner:
false`, so there is no DEBUG ribbon in the corner of your screenshots.

Pick an iPhone 16 Pro or similar so you get the Dynamic Island and the home
indicator to check the layout against.

Because this moved, Flutter's own `flutter emulators --launch
apple_ios_simulator` may not find it either — Flutter usually lags a major
Xcode release. Booting it from Device Hub by hand sidesteps that entirely.

**What the Simulator proves, and what it does not.** This distinction matters,
because the Simulator is honest about layout and actively misleading about
everything I expect to go wrong on iOS:

| Trustworthy | Not trustworthy |
|---|---|
| It builds and launches | **Audio** — the Simulator uses the Mac's sound stack, not iOS's AVAudioSession on real hardware |
| Layout, notch, home indicator | **The silent switch** — there isn't one, and this is the bug I most expect |
| Navigation, level map, settings | **Haptics** — do not exist on the Simulator |
| Text fitting, truncation | **Performance** — it runs on your Mac's processor |

So the Simulator is worth doing tonight: it proves the iOS build works at all,
which is the big unknown. Keep every audio check on the list for whenever an
iPhone is in your hands — and do not let a clean Simulator run persuade either
of us that the audio is fine.

## 4. Build and run on your iPhone — 10 minutes

```sh
cd ~/puzzle-app
flutter pub get
open ios/Runner.xcworkspace
```

In Xcode: select **Runner** in the left sidebar → **Signing & Capabilities** →
tick *Automatically manage signing* → under **Team**, add your personal Apple ID
and select it. Xcode creates a free provisioning profile. You should see
`co.digitalgold.arcade` as the bundle identifier — it is already set.

Then plug the iPhone in, unlock it, tap **Trust** on the prompt, and:

```sh
flutter devices                      # the iPhone should appear
flutter run --release
```

First launch will refuse with an untrusted-developer error. On the phone:
**Settings → General → VPN & Device Management** → your Apple ID → **Trust**.
Then launch it from the home screen.

**Free provisioning expires after seven days.** The app stops launching and you
re-run `flutter run --release`. Fine for "does it work", useless for handing to
anyone — that needs the DGD Apple Developer account, which exists.

---

## What to check once it launches, in this order

The build will probably just work; it is the same Dart, and Flame and Flutter do
not care which platform they are on. What I actually expect to misbehave:

1. **The silent switch.** Flip the ringer switch while the game is making noise.
   On iOS the audio session category decides whether that mutes the app.
   Players never connect the two — they report it as broken audio. This is my
   top suspect.
2. **The audio soak.** Level map → DEV → Audio soak test → 10 minutes. The
   Android run was perfect (6000 effects, zero failures, drift 1.02×) and proves
   nothing about iOS: different player, different pool, different leak surface.
   Send me failed / limited / p95 / drift.

   *(Only in the DEV build — build it with
   `flutter run --release --dart-define=DGD_DEV=true`.)*
3. **First-touch latency.** iOS often has a long delay the first time each sound
   plays unless the session is pre-warmed. Listen to the first few taps.
4. **The notch and the home indicator.** The Flame surface now fills the whole
   area below the goal bar, so check the board is not tucked under the Dynamic
   Island and the bottom row is clear of the home indicator.
5. **Haptics.** They map to different generators on iOS. The heavy impacts on a
   vault break may feel wrong or do nothing.

## If Xcode 27 fights Flutter

Xcode 27 is new and Flutter usually lags a major Xcode release by a few weeks.
The tell is an error inside Flutter's own build plumbing — typically
`xcode_backend.dart` — rather than a real compile error in our code.

If that happens, do not debug it. Download **Xcode 26.6** from
developer.apple.com/download/all (the DGD Apple Developer account gives you
access), point at it, and carry on:

```sh
sudo xcode-select -s /Applications/Xcode-26.6.app/Contents/Developer
```

Xcode 26 still satisfies App Store Connect's requirement, so nothing is lost.
