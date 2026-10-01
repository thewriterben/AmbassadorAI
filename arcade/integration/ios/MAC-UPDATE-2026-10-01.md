# Update for a Mac session already in progress (1 Oct, afternoon)

The first iOS 2.0 package was put together on the morning of 1 Oct (files
stamped 08:46–08:48). Several things changed after that. If your copy of
`IOS-2.0-JOB.md` still says `ab23aef` and `3c4e42d`, you have the morning
version: read this, then take the new files listed at the end.

## What changed

1. **The game's name is "Coin Quest: DGD"** in titles and on buttons (the
   owner's call). On iOS that means the Arcade tab's Coin Quest card:
   - the title is **"Coin Quest: DGD"**, at the same 40 pt, wrapping to three lines as on Android;
   - the button is **"Play Coin Quest: DGD"**.

   Sentences keep the short "Coin Quest". The arcade's own screens (level
   map, level, result) change by themselves, through the new arcade commit
   in point 2.
2. **New commits.** Android was recut as rc3 for the rename:

   | | Morning package | Now |
   |---|---|---|
   | Android 2.0 (`dgd-2.0`) | `ab23aef` (rc2) | **`16394ec` (rc3)** |
   | Android 2.1 (`dgd-2.1-live`) | `2791096` | **`f1c1f43`** |
   | Arcade for iOS 2.0 *and* 2.1 | `3c4e42d` (2.0), `d70534a` (2.1) | **`85e621c` (both)** |

   Every arcade change between `3c4e42d` and `85e621c` is either inert without
   a server or a small fix, so demo-mode behaviour is the same apart from the
   name.
3. **The Invite Friends logos** (R11, decided by the owner):
   - keep the official **white** Facebook and LinkedIn logos;
   - X must be **X's official logo in white**, not Hugeicons' outline `new-twitter`. The designer is supplying the file. Until it arrives, leave what iOS has and don't redraw it.

   This is in the job, phase 2.
4. **`reference/`** now holds the rc3 release record and Android's rc3
   screenshots, which show the new name.
5. **A design review is out with the designer.** It covers the Coin Quest
   card's title treatment, the 2.1 standings row and screen, the podium icon,
   and the X logo. Build what the job says today. If the designer changes
   something, the PC will send it as a small follow-up.

## If you've already started

- **Already branched `ios-2.0` from `ab23aef`?** Fetch the new bundle and move your work onto rc3:

  ```sh
  git fetch ~/Downloads/dgd-native-2.0.bundle 'refs/heads/*:refs/remotes/pc/*'
  git rebase pc/dgd-2.0        # your commits only touch apple/; rc3 only touched android/
  ```

  If you've already sent a bundle back, use `git merge pc/dgd-2.0` instead, so
  history isn't rewritten.
- **Already built the frameworks from `3c4e42d`?** Rebuild from `85e621c`. The
  arcade's own titles live in those frameworks.

  ```sh
  ./build_ios_frameworks.sh ~/Downloads/puzzle-app-v2.bundle 85e621c demo ~/dgd-ios-frameworks
  ```

- **Already built the Arcade tab card?** Change its title and button text as in point 1.
- **Path A** (phase 1) is unaffected.

## Files to take from the PC again

- `dgd-native-2.0.bundle` and `puzzle-app-v2.bundle` (remade 11:15).
- `IOS-2.0-JOB.md` (now final, with points 1 to 3 in it).
- `ios-2.0-scripts/build_ios_frameworks.sh`: only a comment changed, to the new commit.
- `reference/` (refreshed).
