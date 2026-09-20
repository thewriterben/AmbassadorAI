# Nine games removed — 2026-09-16

Clearing the catalogue down to Coin Quest: Digital Gold, ahead of building a new
list of ten. The progression layer underneath was kept deliberately, so the new
games have working XP, badges, streak and standings to plug into rather than
starting from nothing.

`C:\src\puzzle-app` is **not** under version control, so before any of this a
snapshot of `lib/`, `test/`, `assets/` and `pubspec.yaml` went to
`arcade/v1/dist/puzzle-app-snapshot-2026-09-16.zip` (11.2 MB). That zip is the only
copy of the removed code. `arcade/v1/dist/` is git-ignored, so it lives on this
machine and nowhere else — worth putting somewhere that survives the laptop if
any of these nine are ever coming back.

## Gone

| Game | Files |
|---|---|
| Tablet Run | `lib/arcade/run/` |
| Daily Ledger | `lib/arcade/ledger/` |
| Pillar Sort, Design or Myth?, Chain Builder | `lib/arcade/mini/` |
| Merge, Words, Blocks, Rope | `lib/games/` |
| Tablet question UI | `lib/arcade/knowledge/tablet_sheet.dart` |

`lib/games/` was entirely self-contained — `asset_cache.dart` and
`game_scaffold.dart` had no consumers outside those four games — so the whole
directory went with them.

In `lib/main.dart`: nine imports, nine game cards, the three section headings,
and the `Dev.demoBuild` gating that used to hide those cards from the demo. The
gating is moot now that the games are gone from every build, and the `_Section`
widget went with its last caller. The Coin Quest card lost its `06 ·` prefix —
it was a position in a catalogue that no longer exists — and gained `primary`.

## Kept

- **XP, badges, streak, weekly standings** — `lib/arcade/api.dart`,
  `lib/arcade/progress.dart`, `lib/arcade/leaderboard_screen.dart`. Still wired
  to the home screen's XP bar.
- **The whole Node backend**, untouched. Its `/v1/tablet`, `/v1/ledger` and
  `/v1/mini/*` endpoints now have no client, but they are tested, hardened and
  cost nothing to leave in place.
- **The question bank** — 170 reviewed items, the spaced-repetition scheduler
  and `ALLOWLIST.md`. These live server-side, so nothing here touched them.
- **`lib/arcade/knowledge/content.dart`** — the pillar statements, the
  design-or-myth claims and the chain sequences. Reviewed educational content
  with no consumer at the moment; kept so a quiz-style game among the new ten
  can pick it straight back up.

## One loose end: three ghost files

These three could not be deleted:

    lib/arcade/mini/mini_shell.dart
    lib/arcade/ledger/daily_ledger_screen.dart
    lib/arcade/run/tablet_run_screen.dart

They are in Windows' **delete-pending** state: the delete was accepted, but some
process on this machine still holds an open handle, so the directory entry
lingers until it lets go. Every operation on them — open, stat, rename, even
moving the parent directory — returns "Access is denied". Nothing can read them,
including the Dart compiler, so **they have no effect on the app**: nothing
imports them and the analyzer skips them.

They disappear on their own when that process closes the handle. A reboot is the
reliable way. Afterwards:

```
rmdir /s /q C:\src\puzzle-app\lib\arcade\mini ^
            C:\src\puzzle-app\lib\arcade\ledger ^
            C:\src\puzzle-app\lib\arcade\run
```

`test/assets_test.dart` walks every `.dart` under `lib/` and used to fail on
these. It now skips files it cannot open and prints which ones, rather than
either crashing or ignoring them silently — an unreadable source file is worth
seeing, just not worth failing on.

## Art left behind — about 4 MB, not touched

Removing the code did not remove the art. A scan finds ~56 asset files with no
remaining reference: the `merge_*` tile set, `card_merge` / `card_words` /
`card_blocks` / `card_rope`, `rope_*`, `word_*`, `block_*`, plus some older
leftovers (`piece_sapphire`, `piece_emerald`, `piece_rose`, `coin_emerald`,
`coin_sapphire` from the pre-Material palette) and two dev contact sheets.

**I have deliberately not deleted any of them**, for two reasons. Some are
false positives — the level map builds `node_$state.png` by interpolation, so
`node_current`, `node_done` and `node_locked` look orphaned to a text scan but
are very much in use, and deleting them would put an unbounded Flutter error
box on the map. And the new ten games may well reuse tiles, cards or coin
variants that are already drawn.

Worth a pass once the new list is settled and it is clear what is actually
wanted. The DEV apk fell from 56.3 MB to 55.3 MB on code alone; the art is
where the rest of the saving is.

The demo apk did **not** change size (54.8 MB both before and after), which is
the expected result and a useful confirmation: those games were already being
compiled out of the demo by the `const` `Dev.demoBuild` gating, so removing the
source changed nothing for that build.

## Tests

`test/widget_test.dart` was asserting all ten cards were present. It now asserts
the opposite for the nine: they must be **absent** from the home screen. A
half-finished revert that put a card back pointing at a deleted screen would
otherwise only show up as a crash on tap.
