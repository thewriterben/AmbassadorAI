# Puzzle Pack

Five classic puzzle mechanics, one app, iOS + Android. Pure Flutter, no game engine.

| Game   | Mechanic                     | File                      |
|--------|------------------------------|---------------------------|
| Merge  | 2048-style swipe & merge     | `lib/games/merge_game.dart`  |
| Words  | 5-letter guess, 6 tries      | `lib/games/words_game.dart`  |
| Blocks | Falling shapes, clear lines  | `lib/games/blocks_game.dart` |
| Match  | Match-3 swap & cascade       | `lib/games/match_game.dart`  |
| Rope   | Cut-the-rope Verlet physics  | `lib/games/rope_game.dart`   |

Re-skin everything from `lib/theme.dart` (names, colors, and later image assets).

## 1. Install Flutter on Windows (one time, ~30 min)

1. Install Git for Windows if you don't have it: https://git-scm.com/download/win
2. Download the Flutter SDK zip: https://docs.flutter.dev/get-started/install/windows/mobile
3. Extract to `C:\src\flutter` (no spaces in the path).
4. Add `C:\src\flutter\bin` to your PATH (Settings → System → About → Advanced → Environment Variables).
5. Install Android Studio: https://developer.android.com/studio
   - During setup, install: Android SDK, SDK Platform, Android Virtual Device.
   - Open Android Studio → More Actions → SDK Manager → SDK Tools → check **Android SDK Command-line Tools** → Apply.
6. Open a new PowerShell and run:
   ```powershell
   flutter doctor
   flutter doctor --android-licenses   # type y to each
   ```
   Everything under "Android toolchain" should be green. Ignore Chrome/Visual Studio warnings.

## 2. Run the app

```powershell
cd C:\src\puzzle-app
flutter create . --org com.yourcompany --project-name puzzle_pack
flutter pub get
flutter run
```

`flutter create .` generates the `android/` and `ios/` folders around the existing `lib/`. Run it once.
Pick an emulator or a USB-connected Android phone (enable Developer Options → USB debugging) when prompted.

Hot reload: press `r` in the terminal after editing code.

## 3. iOS

Building for iPhone requires macOS + Xcode. Options:
- Borrow/buy a Mac and run `flutter run` there with your iPhone plugged in.
- Use a cloud build service (Codemagic has a free tier) to build and upload to TestFlight from this repo.

## 4. Store submission checklist

**Start these on day 1 — they have waiting periods.**

- [ ] Apple Developer Program ($99/yr): https://developer.apple.com/programs/enroll/ — approval 1–3 days
- [ ] Google Play Console ($25 once): https://play.google.com/console/signup
  - New personal accounts must run a closed test with **12 testers for 14 days** before going to production.
- [ ] Decide the final app name (check it's free on both stores and not a trademark)
- [ ] Icon (1024×1024), screenshots for phone sizes, short + long description
- [ ] Privacy policy URL (required by both stores, even with no data collection)
- [ ] Content rating questionnaire (Play) / age rating (App Store)

## 5. Legal notes

Game mechanics aren't copyrightable, but names, characters, art, and sounds are.
Never use the original game names, logos, or look-alike art. "Blocks" in particular:
keep our own palette and don't imitate the classic seven-piece color scheme.

## Roadmap

- [ ] Persist high scores (`shared_preferences` is already a dependency)
- [ ] Daily challenge + streak per game
- [ ] Sounds and haptics
- [ ] Real word list (~12k valid guesses)
- [ ] More rope levels + level editor
- [ ] Match specials (4-in-a-row, 5-in-a-row bombs)
- [ ] Ads / IAP
- [ ] Game Center / Play Games leaderboards
