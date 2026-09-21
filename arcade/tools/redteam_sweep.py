"""Red-team sweep of a built APK. Static only.

Deliberately makes NO network calls. The red-team policy for this project
forbids traffic to digitalgold.co, and a sweep that phoned home to check a
host would break the rule it exists to enforce. Everything below is read out
of the artefact.
"""
import hashlib, re, sys, zipfile, collections, math, json, subprocess, os

APK = "/tmp/cleanroom/target.apk"
z = zipfile.ZipFile(APK)
raw = open(APK, "rb").read()

def hdr(t):
    print("\n" + "=" * 74); print(t); print("=" * 74)

FINDINGS = []           # (severity, section, text)
def find(sev, sec, txt): FINDINGS.append((sev, sec, txt))

# ---------------------------------------------------------------- identity
hdr("1. IDENTITY")
print(f"  sha256   {hashlib.sha256(raw).hexdigest()}")
print(f"  size     {len(raw):,} bytes")
print(f"  entries  {len(z.namelist()):,}")

from androguard.core.apk import APK as AX
a = AX(APK)
print(f"  package  {a.get_package()}")
print(f"  version  {a.get_androidversion_name()} ({a.get_androidversion_code()})")
print(f"  minSdk   {a.get_min_sdk_version()}    targetSdk {a.get_target_sdk_version()}")

# ---------------------------------------------------------------- signing
hdr("2. SIGNING")
try:
    certs = a.get_certificates()
    for c in certs:
        subj = c.subject.native
        print(f"  subject  {subj}")
        print(f"  issuer   {c.issuer.native}")
        print(f"  serial   {c.serial_number}")
        print(f"  sha256   {hashlib.sha256(c.dump()).hexdigest()}")
        cn = str(subj.get('common_name', ''))
        if 'Android Debug' in cn:
            find("EXPECTED", "signing",
                 "Signed with the Android debug key. Intended for this review "
                 "build; Play will refuse it. NOT a shippable artefact.")
        else:
            find("HIGH", "signing",
                 f"Signed with a non-debug key ({cn}). If this was meant to be "
                 "a review build, a real key has leaked into the build path.")
except Exception as e:
    print("  could not read certificates:", e)
print(f"  v1(JAR)={a.is_signed_v1()}  v2={a.is_signed_v2()}  v3={a.is_signed_v3()}")

# ---------------------------------------------------------------- manifest
hdr("3. MANIFEST POSTURE")
appattr = lambda k: a.get_attribute_value("application", k)
dbg   = appattr("debuggable")
bkp   = appattr("allowBackup")
clear = appattr("usesCleartextTraffic")
print(f"  debuggable            {dbg}")
print(f"  allowBackup           {bkp}")
print(f"  usesCleartextTraffic  {clear}")
print(f"  networkSecurityConfig {appattr('networkSecurityConfig')}")
if str(dbg).lower() == "true":
    find("CRITICAL", "manifest", "android:debuggable=true in a release build.")
if str(clear).lower() == "true":
    find("HIGH", "manifest", "usesCleartextTraffic=true - plaintext HTTP permitted.")
if str(bkp).lower() == "true":
    find("NOTE", "manifest",
         "allowBackup=true. Check backup_rules.xml excludes credential prefs.")

hdr("4. PERMISSIONS")
perms = sorted(a.get_permissions())
for p in perms: print("   ", p)
DANGEROUS = ("LOCATION","CAMERA","RECORD_AUDIO","READ_CONTACTS","READ_SMS",
             "READ_PHONE_STATE","READ_EXTERNAL","WRITE_EXTERNAL","QUERY_ALL_PACKAGES",
             "REQUEST_INSTALL","SYSTEM_ALERT")
for p in perms:
    if any(d in p for d in DANGEROUS):
        find("HIGH", "permissions", f"Sensitive permission requested: {p}")
if not perms: print("    (none)")

hdr("5. EXPORTED COMPONENTS")
# Walk the manifest XML directly rather than via helper methods, so this does
# not depend on one androguard release's API and so every attribute is visible.
ANDROID = "{http://schemas.android.com/apk/res/android}"
root = a.get_android_manifest_axml().get_xml_obj()
app = root.find("application")
LAUNCHER_OK = set()
for kind in ("activity", "activity-alias", "service", "receiver", "provider"):
    for el in (app.findall(kind) if app is not None else []):
        name = el.get(ANDROID + "name")
        ex   = el.get(ANDROID + "exported")
        perm = el.get(ANDROID + "permission")
        filters = el.findall("intent-filter")
        # An intent-filter with no explicit exported= is exported on old SDKs;
        # targetSdk 31+ requires it to be explicit, so trust the attribute.
        is_exp = str(ex).lower() == "true"
        if not is_exp:
            continue
        acts = [f.find("action").get(ANDROID + "name")
                for f in filters if f.find("action") is not None]
        launcher = any("MAIN" in str(x) for x in acts)
        viewer   = any("VIEW" in str(x) for x in acts)
        guard = f"  permission={perm}" if perm else "  NO PERMISSION GUARD"
        print(f"  {kind:14} {name}")
        print(f"                 exported=true{guard}")
        if acts:
            print(f"                 actions: {', '.join(str(x).split('.')[-1] for x in acts)}")
        if perm:
            continue
        if launcher or viewer:
            find("EXPECTED", "exported",
                 f"{name} is exported without a permission - it is the "
                 "launcher and the app-link target, which must be reachable.")
        else:
            find("REVIEW", "exported",
                 f"{kind} {name} is exported with no permission and no "
                 "launcher/VIEW filter to justify it.")

# Anything NOT exported is the safe case; count it so the report is complete.
notexp = 0
for kind in ("activity", "activity-alias", "service", "receiver", "provider"):
    for el in (app.findall(kind) if app is not None else []):
        if str(el.get(ANDROID + "exported")).lower() != "true":
            notexp += 1
print(f"\n  {notexp} component(s) not exported.")

hdr("5b. APP LINKS")
for el in (app.findall("activity") if app is not None else []):
    for f in el.findall("intent-filter"):
        av = f.get(ANDROID + "autoVerify")
        if str(av).lower() == "true":
            hosts_ = [d.get(ANDROID + "host") for d in f.findall("data")]
            paths  = [d.get(ANDROID + "pathPrefix") for d in f.findall("data")]
            hosts_ = sorted({h for h in hosts_ if h})
            paths  = sorted({p for p in paths if p})
            print(f"  autoVerify on {el.get(ANDROID + 'name')}")
            print(f"    hosts {hosts_}")
            print(f"    paths {paths}")
            find("NOTE", "applinks",
                 f"App Links claim {hosts_} {paths}. Verification needs "
                 "assetlinks.json on the site and the release signing cert, "
                 "so it cannot succeed for this debug-signed build.")

# ------------------------------------------------------- network surface
hdr("6. NETWORK SURFACE  (every host the binary contains)")
URL = re.compile(rb"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]{4,200}")
urls = set()
for n in z.namelist():
    try: blob = z.read(n)
    except Exception: continue
    for m in URL.findall(blob):
        try: urls.add(m.decode("utf-8", "ignore"))
        except Exception: pass

HOST = re.compile(r"https?://([^/:\s\"']+)")
hosts = collections.Counter()
for u in urls:
    m = HOST.match(u)
    if m: hosts[m.group(1).lower()] += 1

EXPECTED_HOSTS = {
    "digitalgold.co", "www.digitalgold.co",
    "schemas.android.com", "www.w3.org", "www.apache.org", "apache.org",
    "developer.android.com", "android.googlesource.com", "source.android.com",
    "goo.gle", "g.co", "fonts.gstatic.com", "fonts.googleapis.com",
    "github.com", "www.google.com", "policies.google.com",
    "support.google.com", "play.google.com", "apps.apple.com",
    "flutter.dev", "docs.flutter.dev", "api.flutter.dev", "dart.dev",
    "opensource.org", "creativecommons.org", "unicode.org", "www.unicode.org",
    "127.0.0.1", "localhost", "example.com", "www.example.com",
}
print(f"  {len(hosts)} distinct hosts, {len(urls)} distinct URLs\n")
unexpected = []
for h, c in hosts.most_common():
    mark = "" if h in EXPECTED_HOSTS else "   <-- UNEXPECTED"
    if mark: unexpected.append(h)
    print(f"    {c:>5}  {h}{mark}")
for h in unexpected:
    find("REVIEW", "network", f"Unexpected host in the binary: {h}")

print("\n  -- digitalgold.co URLs (the ones that matter for B1) --")
for u in sorted(x for x in urls if "digitalgold.co" in x):
    print("   ", u[:160])

# ------------------------------------------------------------ RC1 / RC4
hdr("7. KNOWN REGRESSIONS")
loopback = sorted(u for u in urls if "8787" in u or "10.0.2.2" in u)
print("  RC1 - localhost:8787 arcade fallback")
if loopback:
    for u in loopback: print("    FOUND:", u)
    find("HIGH", "RC1", "Loopback arcade endpoint present in the binary.")
else:
    print("    clean - no loopback arcade endpoint")

print("\n  RC4 - declared ABIs vs native libs actually present")
abis = collections.defaultdict(set)
for n in z.namelist():
    if n.startswith("lib/") and n.endswith(".so"):
        abis[n.split("/")[1]].add(n.split("/")[-1])
for abi, libs in sorted(abis.items()):
    has_flutter = "libflutter.so" in libs
    has_app = "libapp.so" in libs
    ok = has_flutter and has_app
    print(f"    {abi:14} {len(libs)} libs   flutter={has_flutter} app={has_app}  {'ok' if ok else 'INCOMPLETE'}")
    if not ok:
        find("HIGH", "RC4",
             f"ABI {abi} is declared but is missing the Flutter engine - the "
             "arcade would throw UnsatisfiedLinkError there.")

# ------------------------------------------------- arcade configuration
hdr("8. ARCADE CONFIGURATION")
libapp = b""
for n in z.namelist():
    if n.endswith("arm64-v8a/libapp.so"): libapp = z.read(n)
def inso(s): return len(re.findall(s.encode(), libapp))
checks = [
    ("voWinner",     0, "the §4.3 winner-line suppression"),
    ("fireworkShow", 0, "the §4.3 firework suppression"),
    ("voPraise",     None, "cascade praise (should survive)"),
    ("voEncourage",  None, "loss encouragement (should survive)"),
]
for sym, want, why in checks:
    n = inso(sym)
    if want is None:
        status = "present" if n else "ABSENT"
        print(f"  {sym:14} {n:>3}  {status:8} {why}")
        if not n: find("REVIEW", "arcade", f"{sym} is absent - {why}")
    else:
        ok = (n == want)
        print(f"  {sym:14} {n:>3}  {'ok' if ok else 'PRESENT':8} {why}")
        if not ok:
            find("CRITICAL", "arcade",
                 f"{sym} is present in the shipped binary - {why} has regressed.")

# -------------------------------------------------- compliance language
hdr("9. COMPLIANCE VOCABULARY")
BANNED = [rb"\bearn(ing|ed|s)?\b", rb"\bcash\b", rb"\bdollars?\b",
          rb"\bjackpot\b", rb"\bcasino\b", rb"\bpayout\b", rb"\bwinnings\b",
          rb"\bprize\b", rb"\bwager\b", rb"\bbet\b", rb"\$\d+"]
ASSET_TEXT = [n for n in z.namelist()
              if n.startswith("assets/") and
              n.endswith((".json", ".txt", ".md", ".csv", ".yaml", ".yml"))]
scan = {"dex": b"".join(z.read(n) for n in z.namelist() if n.endswith(".dex")),
        "libapp.so": libapp}
for n in ASSET_TEXT: scan[n] = z.read(n)
for pat in BANNED:
    tot = {}
    for where, blob in scan.items():
        c = len(re.findall(pat, blob, re.I))
        if c: tot[where] = c
    label = pat.decode()
    if tot:
        print(f"  {label:26} {tot}")
        find("REVIEW", "vocabulary",
             f"Banned-vocabulary pattern {label} appears in {list(tot)}. "
             "Check whether it is user-facing copy or library noise.")
    else:
        print(f"  {label:26} clean")

# ------------------------------------------------------------- secrets
hdr("10. SECRETS")
KEYPATS = [
  ("AWS access key",      rb"AKIA[0-9A-Z]{16}"),
  ("Google API key",      rb"AIza[0-9A-Za-z_\-]{35}"),
  ("Slack token",         rb"xox[baprs]-[0-9A-Za-z-]{10,}"),
  ("Stripe key",          rb"[sr]k_(live|test)_[0-9A-Za-z]{16,}"),
  ("GitHub token",        rb"gh[pousr]_[0-9A-Za-z]{36,}"),
  ("JWT",                 rb"eyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\."),
  ("PEM private key",     rb"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
  ("RSA private key",     rb"-----BEGIN RSA"),
  ("Bearer literal",      rb"Bearer\s+[A-Za-z0-9_\-\.]{20,}"),
  ("password= literal",   rb"password\s*[=:]\s*[\"'][^\"']{4,}"),
  ("secret= literal",     rb"(api[_-]?secret|client[_-]?secret|arcade_secret)\s*[=:]\s*[\"'][^\"']{4,}"),
]
hits = 0
for label, pat in KEYPATS:
    found = []
    for n in z.namelist():
        try: blob = z.read(n)
        except Exception: continue
        for m in re.findall(pat, blob):
            found.append((n, m[:60] if isinstance(m, bytes) else str(m)[:60]))
    if found:
        hits += len(found)
        print(f"  {label:20} {len(found)} hit(s)")
        for n, s in found[:4]:
            print(f"      {n}: {s}")
        find("HIGH", "secrets", f"{label}: {len(found)} occurrence(s).")
    else:
        print(f"  {label:20} clean")
if not hits: print("\n  No credential patterns matched.")

# -------------------------------------------------------------- trackers
hdr("11. THIRD-PARTY SDKs / TRACKERS")
TRACKERS = {
  "Firebase Analytics": rb"com/google/firebase/analytics",
  "Google Analytics":   rb"com/google/android/gms/analytics",
  "Crashlytics":        rb"com/google/firebase/crashlytics",
  "AdMob / GMA":        rb"com/google/android/gms/ads",
  "Facebook SDK":       rb"com/facebook/",
  "AppsFlyer":          rb"com/appsflyer",
  "Adjust":             rb"com/adjust/sdk",
  "Branch":             rb"io/branch/",
  "Mixpanel":           rb"com/mixpanel",
  "Amplitude":          rb"com/amplitude",
  "Sentry":             rb"io/sentry/",
  "Bugsnag":            rb"com/bugsnag",
  "OneSignal":          rb"com/onesignal",
  "Segment":            rb"com/segment/analytics",
}
dex = scan["dex"]
any_tracker = False
for label, pat in TRACKERS.items():
    n = len(re.findall(pat, dex))
    if n:
        any_tracker = True
        print(f"  {label:22} {n:>5} refs   <-- PRESENT")
        find("REVIEW", "trackers",
             f"{label} appears in the dex. The privacy policy and Data Safety "
             "form both state the app has no analytics.")
    else:
        print(f"  {label:22} absent")
if not any_tracker:
    print("\n  No known analytics, ads or crash-reporting SDK found.")

# --------------------------------------------------------------- assets
hdr("12. ASSET SURFACE")
big = sorted(((z.getinfo(n).file_size, n) for n in z.namelist()
              if n.startswith("assets/")), reverse=True)[:12]
print(f"  {len([n for n in z.namelist() if n.startswith('assets/')])} asset entries; largest:")
for s, n in big: print(f"    {s:>10,}  {n}")
SUSPECT = [n for n in z.namelist()
           if re.search(r"\.(pem|p12|jks|keystore|key|env|sql|db|bak|log)$", n, re.I)]
if SUSPECT:
    print("\n  Files with credential-ish or data-ish extensions:")
    for n in SUSPECT: print("   ", n)
    find("HIGH", "assets", f"{len(SUSPECT)} file(s) with sensitive extensions packaged.")
else:
    print("\n  No .pem/.jks/.keystore/.env/.db/.sql/.log files packaged.")

# --------------------------------------------------------------- verdict
hdr("SUMMARY")
order = {"CRITICAL":0,"HIGH":1,"REVIEW":2,"NOTE":3,"EXPECTED":4}
FINDINGS.sort(key=lambda f: order.get(f[0], 9))
counts = collections.Counter(f[0] for f in FINDINGS)
print("  " + "  ".join(f"{k}={v}" for k, v in sorted(counts.items(), key=lambda x: order.get(x[0],9))) or "  nothing")
print()
for sev, sec, txt in FINDINGS:
    print(f"  [{sev:8}] {sec:12} {txt}")
