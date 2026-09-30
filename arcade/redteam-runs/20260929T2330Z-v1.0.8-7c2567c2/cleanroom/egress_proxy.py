"""Logging HTTP/HTTPS forward proxy for the emulator's -http-proxy flag.
One line per CONNECT host:port or plain-HTTP request; bytes are tunnelled.
Usage: egress_proxy.py <port> <logfile>"""
import datetime, select, socket, sys, threading

LOG = sys.argv[2]
lock = threading.Lock()


def log(line):
    with lock, open(LOG, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now():%H:%M:%S} {line}\n")


def pump(a, b):
    try:
        while True:
            r, _, _ = select.select([a, b], [], [], 60)
            if not r:
                break
            for s in r:
                data = s.recv(65536)
                if not data:
                    return
                (b if s is a else a).sendall(data)
    except OSError:
        pass
    finally:
        for s in (a, b):
            try:
                s.close()
            except OSError:
                pass


def handle(c):
    try:
        head = b""
        while b"\r\n\r\n" not in head:
            chunk = c.recv(4096)
            if not chunk:
                return
            head += chunk
        method, target, _ = head.split(b"\r\n", 1)[0].decode("latin-1").split(" ", 2)
        if method == "CONNECT":
            host, port = target.rsplit(":", 1)
            log(f"CONNECT {host}:{port}")
            up = socket.create_connection((host.strip("[]"), int(port)), timeout=15)
            c.sendall(b"HTTP/1.1 200 Connection established\r\n\r\n")
            pump(c, up)
        else:
            rest = target.split("://", 1)[1]
            hostport, _, path = rest.partition("/")
            host, _, port = hostport.partition(":")
            log(f"{method} {hostport} /{path}")
            up = socket.create_connection((host, int(port or 80)), timeout=15)
            up.sendall(head)
            pump(c, up)
    except Exception as e:  # noqa: BLE001
        log(f"ERROR {e}")
    finally:
        try:
            c.close()
        except OSError:
            pass


srv = socket.socket()
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("127.0.0.1", int(sys.argv[1])))
srv.listen(64)
while True:
    conn, _ = srv.accept()
    threading.Thread(target=handle, args=(conn,), daemon=True).start()
