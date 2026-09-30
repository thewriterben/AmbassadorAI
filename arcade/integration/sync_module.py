"""Generate the Flutter module for add-to-app embedding, from arcade v1.

Why this exists
---------------
`flutter build aar` only works on a Flutter *module*, and a project cannot be
both a module and an app: adding a `module:` descriptor to v1's pubspec was
tested on 2026-09-20 and it breaks `flutter build apk` outright - Gradle
compiles, then the tool looks for the APK in the module output path and fails.

v1 has to stay a standalone app, because it is also a store candidate in its
own right (`MERGE.md`, option C). So the module is *generated* from v1 rather
than being a second copy anyone edits.

The rule that follows: **never edit C:\\src\\dgd_arcade_module by hand.**
Edit v1 and re-run this. Anything written into the module's lib/ or assets/
is destroyed on the next sync.

The pubspec is transformed rather than hand-written, so a dependency added to
v1 cannot silently go missing from the embedded build. The lockfile is copied
as-is, so the versions compiled into the embed are the ones v1 committed
(AUDIT-v1.0.8-2026-09-29.md, P2); build with `flutter pub get
--enforce-lockfile`.

The sync refuses a v1 working tree with uncommitted changes and stamps the
commit it copied (P3): an embed is built from a commit, never from whatever
the working tree held that afternoon.

Paths default to the Windows machine. The release build runs in the Linux
clean-room container (cleanroom/build_aar_cleanroom.sh, P1), which sets
DGD_V1 and DGD_MODULE.
"""

import os
import pathlib
import re
import shutil
import subprocess
import sys

V1 = pathlib.Path(os.environ.get("DGD_V1", r"C:\src\puzzle-app"))
MODULE = pathlib.Path(os.environ.get("DGD_MODULE", r"C:\src\dgd_arcade_module"))
MODULE_NAME = "dgd_arcade_module"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=V1, capture_output=True, text=True,
    ).stdout.strip()


def check_v1_is_v1() -> str:
    """Refuse to build the embed from anything but a clean, committed v1 on main.

    Returns the full commit hash that is being copied.
    """
    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    head = git("rev-parse", "HEAD")
    # A detached checkout of a tag is fine (that is how the clean room builds),
    # provided the commit is on main's history.
    on_main = branch == "main" or any(
        subprocess.run(
            ["git", "merge-base", "--is-ancestor", "HEAD", ref], cwd=V1,
            capture_output=True,
        ).returncode == 0
        for ref in ("main", "origin/main")
    )
    if not on_main:
        fail(
            f"{V1} is at '{branch}' ({head[:7]}), which is not on main.\n"
            "      The embed is built from v1 only. See arcade/VERSIONS.md."
        )
    dirty = git("status", "--porcelain")
    if dirty:
        fail(
            f"{V1} has uncommitted changes:\n{dirty}\n"
            "      Commit them first; the embed is built from a commit."
        )
    if (V1 / "lib" / "arcade" / "passage").exists():
        fail("v1 contains Passage. That is v2 - the embed must not include it.")
    print(f"v1 check: {head} on main, clean, no v2 content")
    return head


def make_pubspec() -> None:
    src = (V1 / "pubspec.yaml").read_text(encoding="utf-8")

    src = re.sub(r"^name: .*$", f"name: {MODULE_NAME}", src, count=1, flags=re.M)
    src = re.sub(
        r"^description: .*$",
        "description: GENERATED from arcade v1. Do not edit.",
        src, count=1, flags=re.M,
    )

    # The module descriptor is what makes `flutter build aar` possible. It is
    # also exactly what breaks `flutter build apk`, which is why it lives here
    # and never in v1.
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
        fail("could not inject the module descriptor - v1's pubspec shape changed")

    # flutter_lints stays, although the module never runs the analyzer: dropping
    # it would make the module's resolution differ from v1's lockfile, and
    # `--enforce-lockfile` would then refuse the build. It has no Dart code, so
    # nothing of it reaches the binary.

    header = (
        "# GENERATED FILE - DO NOT EDIT.\n"
        "# Produced from C:\\src\\puzzle-app by arcade/integration/sync_module.py.\n"
        "# Edit v1 and re-run the sync; changes made here are destroyed.\n\n"
    )
    (MODULE / "pubspec.yaml").write_text(header + src, encoding="utf-8")
    print("pubspec: generated from v1")


def mirror(name: str) -> None:
    dst = MODULE / name
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(V1 / name, dst)
    n = sum(1 for p in dst.rglob("*") if p.is_file())
    print(f"{name}: mirrored, {n} files")


def copy_lock() -> None:
    shutil.copyfile(V1 / "pubspec.lock", MODULE / "pubspec.lock")
    print("pubspec.lock: copied from v1 (build with --enforce-lockfile)")


def stamp(commit: str) -> None:
    (MODULE / "SOURCE_COMMIT").write_text(commit + "\n", encoding="utf-8")
    (MODULE / "GENERATED.md").write_text(
        "# This directory is generated\n\n"
        f"Produced from arcade v1 commit `{commit}` by\n"
        "`arcade/integration/sync_module.py`.\n\n"
        "**Do not edit `lib/` or `assets/` here.** Edit v1 and re-run the sync.\n"
        "Anything you write here is deleted on the next run.\n\n"
        "The only hand-maintained parts are the `.android/` and `.ios/` host\n"
        "folders that `flutter create -t module` produced.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    if not V1.exists():
        fail(f"{V1} not found")
    if not MODULE.exists():
        fail(f"{MODULE} not found - run `flutter create -t module` first")
    commit = check_v1_is_v1()
    make_pubspec()
    copy_lock()
    mirror("lib")
    mirror("assets")
    stamp(commit)
    print(f"\nmodule is in sync with v1 {commit[:7]}")
