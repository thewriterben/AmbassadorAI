#!/usr/bin/env python3
"""
dgd.py - one entry point for the whole DGD Video Studio toolchain.

A thin router so the agent (and you) drive every stage from a single command:

  dgd assets   …    -> brand assets / kit / motif / contact-sheet   (dgd_assets.py)
  dgd lint     …    -> compliance linter (Stage 7 floor)            (compliance_lint.py)
  dgd evals         -> red-team rails regression suite              (run_compliance_evals.py)
  dgd publish  …    -> Stage-6 publish package + gate               (dgd_publish.py)
  dgd perf     …    -> performance ledger: record / sync / report / show / dashboard
  dgd dashboard …   -> shortcut for `perf dashboard`
  dgd site      …   -> build the deployable static control-panel site  (build_site.py)
  dgd serve     …   -> run the LOCAL control-panel server (runs the tools)  (dgd_web.py)
  dgd doctor        -> health check: tools present, rails passing, deps, Postiz status
  dgd help          -> this overview

Everything after the sub-command is passed straight through, e.g.
  python3 tools/dgd.py assets kit --headline "Why money loses value" --outdir raw/ep1
  python3 tools/dgd.py lint script.md --require-disclosure
  python3 tools/dgd.py perf report
"""
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROUTES = {
    "assets":    "dgd_assets.py",
    "lint":      "compliance_lint.py",
    "evals":     "run_compliance_evals.py",
    "publish":   "dgd_publish.py",
    "perf":      "dgd_performance.py",
}


def run(script, args):
    return subprocess.call([sys.executable, os.path.join(HERE, script), *args])


def doctor():
    ok = True

    def check(label, good, detail="", required=True):
        nonlocal ok
        mark = "✓" if good else ("✗" if required else "·")
        if not good and required:
            ok = False
        print(f"  {mark} {label}" + (f" — {detail}" if detail else ""))

    print("DGD toolchain doctor\n--------------------")
    print("tools present:")
    for s in set(ROUTES.values()) | {"dgd_performance.py"}:
        check(s, os.path.exists(os.path.join(HERE, s)))

    print("dependencies:")
    try:
        import PIL  # noqa
        check("Pillow (asset rendering)", True, f"v{PIL.__version__}")
    except Exception as e:
        check("Pillow (asset rendering)", False, str(e))
    check("jq (publish.sh helper)", shutil.which("jq") is not None,
          "needed only when running publish.sh", required=False)

    print("compliance rails:")
    rc = subprocess.run([sys.executable, os.path.join(HERE, "run_compliance_evals.py")],
                        capture_output=True, text=True)
    last = (rc.stdout.strip().splitlines() or ["(no output)"])[-1]
    check("red-team eval suite", rc.returncode == 0, last)

    print("publishing (Postiz):")
    check("POSTIZ_API_KEY set", bool(os.environ.get("POSTIZ_API_KEY")),
          "needed only to actually schedule", required=False)
    check("postiz CLI on PATH", shutil.which("postiz") is not None,
          "dry-run works without it", required=False)

    print("\n" + ("ALL GREEN — pipeline ready." if ok else
                  "Some checks failed (see ✗). Dry-run features still work."))
    return 0 if ok else 1


def main(argv):
    if not argv or argv[0] in ("help", "-h", "--help"):
        print(__doc__)
        return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "doctor":
        return doctor()
    if cmd == "dashboard":
        return run("dgd_performance.py", ["dashboard", *rest])
    if cmd == "site":
        return run("build_site.py", rest)
    if cmd == "serve":
        return run("dgd_web.py", rest)
    if cmd in ROUTES:
        return run(ROUTES[cmd], rest)
    sys.stderr.write(f"unknown command '{cmd}'. Try: dgd help\n")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
