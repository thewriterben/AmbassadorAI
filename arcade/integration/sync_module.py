"""Generate the Flutter module for add-to-app embedding, from an arcade line.

Why this exists
---------------
`flutter build aar` only works on a Flutter *module*, and a project cannot be
both a module and an app: adding a `module:` descriptor to v1's pubspec was
tested on 2026-09-20 and it breaks `flutter build apk` outright - Gradle
compiles, then the tool looks for the APK in the module output path and fails.

The arcade has to stay a standalone app as well, because it is also a store
candidate in its own right (`MERGE.md`, option C). So the module is
*generated* from it rather than being a second copy anyone edits.

The rule that follows: **never edit C:\\src\\dgd_arcade_module by hand.**
Edit the arcade and re-run this. Anything written into the module's lib/ or
assets/ is destroyed on the next sync.

Which arcade
------------
`DGD_ARCADE` picks the line, and defaults to v1 so every existing caller
builds what it always built:

  v1   C:\\src\\puzzle-app, branch main. What DGD App 1.0.x embeds. Must not
       contain Passage.
  v2   C:\\src\\puzzle-app-v2-wings, branch v2/ten-games. What DGD App 2.0
       embeds (the owner's call, 2026-09-30: "arcade ships in DGD 2.0").
       Must contain Passage, so a v2 build can't quietly be v1.

The pubspec is transformed rather than hand-written, so a dependency added to
the arcade cannot silently go missing from the embedded build. The lockfile
is copied as-is, so the versions compiled into the embed are the ones the
arcade committed (AUDIT-v1.0.8-2026-09-29.md, P2); build with `flutter pub
get --enforce-lockfile`.

The sync refuses a working tree with uncommitted changes and stamps the
commit it copied (P3): an embed is built from a commit, never from whatever
the working tree held that afternoon.

Paths default to the Windows machine. The release build runs in the Linux
clean-room container (cleanroom/build_aar_cleanroom.sh, P1), which sets
DGD_V1 (or DGD_V2) and DGD_MODULE.
"""

import os
import pathlib
import re
import shutil
import subprocess
import sys

LINES = {
    "v1": {"env": "DGD_V1", "path": r"C:\src\puzzle-app", "branch": "main", "passage": False},
    "v2": {"env": "DGD_V2", "path": r"C:\src\puzzle-app-v2-wings", "branch": "v2/ten-games", "passage": True},
}
ARCADE = os.environ.get("DGD_ARCADE", "v1")
if ARCADE not in LINES:
    print(f"FAIL: DGD_ARCADE={ARCADE!r}; it must be one of {', '.join(LINES)}")
    sys.exit(1)
LINE = LINES[ARCADE]
SRC = pathlib.Path(os.environ.get(LINE["env"], LINE["path"]))
BRANCH = LINE["branch"]
MODULE = pathlib.Path(os.environ.get("DGD_MODULE", r"C:\src\dgd_arcade_module"))
MODULE_NAME = "dgd_arcade_module"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=SRC, capture_output=True, text=True,
    ).stdout.strip()


def check_source() -> str:
    """Refuse to build the embed from anything but a clean, committed arcade on
    its line's branch.

    Returns the full commit hash that is being copied.
    """
    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    head = git("rev-parse", "HEAD")
    # A detached checkout of a tag is fine (that is how the clean room builds),
    # provided the commit is on the branch's history.
    on_branch = branch == BRANCH or any(
        subprocess.run(
            ["git", "merge-base", "--is-ancestor", "HEAD", ref], cwd=SRC,
            capture_output=True,
        ).returncode == 0
        for ref in (BRANCH, f"origin/{BRANCH}")
    )
    if not on_branch:
        fail(
            f"{SRC} is at '{branch}' ({head[:7]}), which is not on {BRANCH}.\n"
            f"      The {ARCADE} embed is built from {BRANCH} only. See arcade/VERSIONS.md."
        )
    dirty = git("status", "--porcelain")
    if dirty:
        fail(
            f"{SRC} has uncommitted changes:\n{dirty}\n"
            "      Commit them first; the embed is built from a commit."
        )
    has_passage = (SRC / "lib" / "arcade" / "passage").exists()
    if has_passage != LINE["passage"]:
        fail(
            f"{SRC} {'contains' if has_passage else 'lacks'} Passage, so it is not {ARCADE}.\n"
            "      Check DGD_ARCADE and the source path."
        )
    print(f"{ARCADE} check: {head} on {BRANCH}, clean, Passage {'present' if has_passage else 'absent'}")
    return head


def make_pubspec() -> None:
    src = (SRC / "pubspec.yaml").read_text(encoding="utf-8")

    src = re.sub(r"^name: .*$", f"name: {MODULE_NAME}", src, count=1, flags=re.M)
    src = re.sub(
        r"^description: .*$",
        f"description: GENERATED from arcade {ARCADE}. Do not edit.",
        src, count=1, flags=re.M,
    )

    # The module descriptor is what makes `flutter build aar` possible. It is
    # also exactly what breaks `flutter build apk`, which is why it lives here
    # and never in the arcade.
    src = src.replace(
        "flutter:\n  uses-material-design: true",
        "flutter:\n"
        "  module:\n"
        "    androidX: true\n"
        "    androidPackage: co.digitalgold.arcade.module\n"
        "    iosBundleIdentifier: co.digitalgold.arcade.module\n"
        "  uses-material-design: true",
        1,
    )
    if "module:" not in src:
        fail(f"could not inject the module descriptor - {ARCADE}'s pubspec shape changed")

    # flutter_lints stays, although the module never runs the analyzer: dropping
    # it would make the module's resolution differ from the arcade's lockfile,
    # and `--enforce-lockfile` would then refuse the build. It has no Dart code,
    # so nothing of it reaches the binary.

    header = (
        "# GENERATED FILE - DO NOT EDIT.\n"
        f"# Produced from {LINE['path']} ({ARCADE}) by arcade/integration/sync_module.py.\n"
        "# Edit the arcade and re-run the sync; changes made here are destroyed.\n\n"
    )
    (MODULE / "pubspec.yaml").write_text(header + src, encoding="utf-8")
    print(f"pubspec: generated from {ARCADE}")


def mirror(name: str) -> None:
    dst = MODULE / name
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(SRC / name, dst)
    n = sum(1 for p in dst.rglob("*") if p.is_file())
    print(f"{name}: mirrored, {n} files")


def copy_lock() -> None:
    shutil.copyfile(SRC / "pubspec.lock", MODULE / "pubspec.lock")
    print(f"pubspec.lock: copied from {ARCADE} (build with --enforce-lockfile)")


def stamp(commit: str) -> None:
    (MODULE / "SOURCE_COMMIT").write_text(commit + "\n", encoding="utf-8")
    (MODULE / "SOURCE_LINE").write_text(ARCADE + "\n", encoding="utf-8")
    (MODULE / "GENERATED.md").write_text(
        "# This directory is generated\n\n"
        f"Produced from arcade {ARCADE} commit `{commit}` by\n"
        "`arcade/integration/sync_module.py`.\n\n"
        "**Do not edit `lib/` or `assets/` here.** Edit the arcade and re-run the\n"
        "sync. Anything you write here is deleted on the next run.\n\n"
        "The only hand-maintained parts are the `.android/` and `.ios/` host\n"
        "folders that `flutter create -t module` produced.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    if not SRC.exists():
        fail(f"{SRC} not found")
    if not MODULE.exists():
        fail(f"{MODULE} not found - run `flutter create -t module` first")
    commit = check_source()
    make_pubspec()
    copy_lock()
    mirror("lib")
    mirror("assets")
    stamp(commit)
    print(f"\nmodule is in sync with {ARCADE} {commit[:7]}")
