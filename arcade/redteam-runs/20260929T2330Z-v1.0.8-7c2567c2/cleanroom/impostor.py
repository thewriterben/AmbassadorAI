"""Impersonates the arcade backend on localhost:8787 (via adb reverse).
Issues a token to POST /v1/players, 503s everything else, logs every request.
Usage: impostor.py <port> <logfile>"""
import datetime, http.server, json, sys

LOG = sys.argv[2]


class H(http.server.BaseHTTPRequestHandler):
    def _log(self):
        n = int(self.headers.get("content-length") or 0)
        body = self.rfile.read(n) if n else b""
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now():%H:%M:%S} {self.command} {self.path} auth={self.headers.get('authorization', '-')} body={body[:120]!r}\n")
        if self.command == "POST" and self.path == "/v1/players":
            out = json.dumps({"token": "IMPOSTOR-TOKEN", "playerId": "impostor"}).encode()
            self.send_response(200)
        else:
            out = b'{"error":"impostor"}'
            self.send_response(503)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)

    do_GET = do_POST = do_DELETE = do_PUT = _log

    def log_message(self, *a):
        pass


http.server.ThreadingHTTPServer(("127.0.0.1", int(sys.argv[1])), H).serve_forever()
