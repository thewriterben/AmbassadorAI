"""Dev server for build/web: correct MIME for .mjs/.wasm, gzip, the
COOP/COEP headers skwasm needs for multi-threading, and a same-origin
/api/* proxy to the Arcade backend (the production reverse proxy does the
same, which keeps the page cross-origin isolated without CORS)."""
import gzip, mimetypes, os, sys, urllib.request, urllib.error
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = sys.argv[1] if len(sys.argv) > 1 else r"C:\src\puzzle-app\build\web"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8765
API = sys.argv[3] if len(sys.argv) > 3 else "http://127.0.0.1:8787"
mimetypes.add_type("text/javascript", ".mjs")
mimetypes.add_type("text/javascript", ".js")
mimetypes.add_type("application/wasm", ".wasm")
mimetypes.add_type("application/json", ".json")
GZ = (".js", ".mjs", ".wasm", ".json", ".html", ".css", ".md", ".otf", ".ttf")

class H(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def _proxy(self):
        n = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(n) if n else None
        req = urllib.request.Request(API + self.path[len("/api"):], data=body, method=self.command)
        for h in ("Content-Type", "Authorization"):
            if self.headers.get(h):
                req.add_header(h, self.headers[h])
        try:
            with urllib.request.urlopen(req, timeout=10) as r:
                data, status, ctype = r.read(), r.status, r.headers.get("Content-Type", "application/json")
        except urllib.error.HTTPError as e:
            data, status, ctype = e.read(), e.code, e.headers.get("Content-Type", "application/json")
        except Exception as e:  # backend down
            data, status, ctype = ('{"error":"backend_unreachable","detail":"%s"}' % e).encode(), 502, "application/json"
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self.path.startswith("/api/"):
            return self._proxy()
        self.send_error(405)

    def do_GET(self):
        if self.path.startswith("/api/"):
            return self._proxy()
        path = self.translate_path(self.path.split("?")[0])
        if os.path.isdir(path):
            path = os.path.join(path, "index.html")
        if os.path.isfile(path) and path.endswith(GZ) and "gzip" in self.headers.get("Accept-Encoding", ""):
            data = gzip.compress(open(path, "rb").read(), 6)
            self.send_response(200)
            self.send_header("Content-Type", mimetypes.guess_type(path)[0] or "application/octet-stream")
            self.send_header("Content-Encoding", "gzip")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        super().do_GET()

    def log_message(self, *a):
        pass

ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
