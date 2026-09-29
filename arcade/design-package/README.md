# Design resource package for Med

`build_design_pkg.mjs` builds `dgdappsource/design-package/DGD-Design-Resources-<date>` from the three codebases (app shell, in-app arcade, web arcade); `zipfwd.ps1` zips it with forward-slash paths so it unpacks on a Mac. `START-HERE.html`, `RETURN-SPEC.md` and `CHANGES-TEMPLATE.txt` are the guide files it copies in. `manifest-2026-09-29.csv` maps every packaged file to its source path, which is how a returned design is put back in place.
