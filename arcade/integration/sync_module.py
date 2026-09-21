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
v1 cannot silently go missing from the embedded build.
"""

import pathlib
import re
import shutil
import subprocess
import sys

V1 = pathlib.Path(r"C:\src\puzzle-app")
MODULE = pathlib.Path(r"C:\src\dgd_arcade_module")
MODULE_NAME = "dgd_arcade_module"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def check_v1_is_v1() -> None:
    """Refuse to build the embed from anything but frozen v1 on main."""
    branch = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=V1, capture_output=True, text=True,
    ).stdout.strip()
    if branch != "main":
        fail(
            f"{V1} is on branch '{branch}', expected 'main'.\n"
            "      The embed is built from v1 only. See arcade/VERSIONS.md."
        )
    if (V1 / "lib" / "arcade" / "passage").exists():
        fail("v1 contains Passage. That is v2 - the embed must not include it.")
    print("v1 check: on main, no v2 content")


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

    src = src.replace("  flutter_lints: ^4.0.0\n", "")

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


def stamp() -> None:
    (MODULE / "GENERATED.md").write_text(
        "# This directory is generated\n\n"
        "Produced from arcade v1 (`C:\\src\\puzzle-app`, branch `main`) by\n"
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
    check_v1_is_v1()
    make_pubspec()
    mirror("lib")
    mirror("assets")
    stamp()
    print("\nmodule is in sync with v1")
