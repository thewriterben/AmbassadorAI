#!/usr/bin/env python3
"""One entry point. Reads config.json, writes all four deliverables.

    python3 scripts/build_all.py                 # everything
    python3 scripts/build_all.py --only html,md  # a subset

Formats: xlsx, md, html, docx (docx also produces the PDF if LibreOffice is present).
Set DGD_OUT to change the output directory (default ./out), DGD_SLUG for the filename stem.
"""
import argparse, os, subprocess, sys, shutil, glob

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.environ.get("DGD_OUT", "out")

ap = argparse.ArgumentParser()
ap.add_argument("--only", default="xlsx,md,html,docx",
                help="comma-separated subset of xlsx,md,html,docx")
ap.add_argument("--no-pdf", action="store_true", help="skip the LibreOffice PDF render")
ap.add_argument("--config", default=os.environ.get("DGD_CONFIG", "config.json"),
                help="path to this run's config.json (default ./config.json)")
a = ap.parse_args()
want = {x.strip() for x in a.only.split(",") if x.strip()}

CFG = os.path.abspath(a.config)
if not os.path.exists(CFG):
    sys.exit(f"No config.json at {CFG}.\nWrite one first — see reference/build-and-deliver.md "
             "for the schema, or copy data/_TEMPLATE_config.json.")
OUT = os.path.abspath(OUT)
os.makedirs(OUT, exist_ok=True)
env = dict(os.environ, DGD_OUT=OUT, DGD_CONFIG=CFG)

def run(cmd, label):
    r = subprocess.run(cmd, cwd=HERE, env=env, capture_output=True, text=True)
    if r.returncode:
        print(f"✗ {label}\n{r.stdout}\n{r.stderr}"); sys.exit(1)
    print("  " + (r.stdout.strip().splitlines() or [label])[-1])

print(f"Building into {os.path.abspath(OUT)}/")
if "xlsx" in want: run([sys.executable, "build_xlsx.py"],  "xlsx")
if "md"   in want: run([sys.executable, "build_briefs.py"],"md")
if "html" in want: run([sys.executable, "build_html.py"],  "html")
if "docx" in want:
    run([sys.executable, "mk_json.py"], "json")
    if shutil.which("node") is None:
        print("  ! node not found — skipping the DOCX/PDF report. "
              "The other formats carry the same content.")
    else:
        run(["node", "build_docx.js"], "docx")
        docx = glob.glob(os.path.join(OUT, "*-Report.docx"))
        if docx and not a.no_pdf:
            soffice = shutil.which("soffice") or shutil.which("libreoffice")
            if soffice:
                subprocess.run([soffice, "--headless", "--convert-to", "pdf",
                                "--outdir", OUT, docx[0]],
                               capture_output=True, timeout=900)
                pdf = docx[0].replace(".docx", ".pdf")
                if os.path.exists(pdf):
                    print(f"  PDF   {os.path.getsize(pdf)//1024} KB")
            else:
                print("  ! LibreOffice not found — DOCX written, PDF skipped.")
print("\nDone. Deliver every file in the output directory, then read it back to the "
      "ambassador as: what is urgent, what is closed, what still needs a phone call.")
