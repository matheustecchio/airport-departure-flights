import argparse
import html
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from main import main as refresh_flight_data


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DASHBOARD_PATHS = {
    "/web/index.html",
    "/web/cork.html",
    "/web/dublin.html",
    "/web/shannon.html",
}
REFRESH_LOCK = threading.Lock()


def should_refresh(path: str) -> bool:
    return urlsplit(path).path in DASHBOARD_PATHS


class DashboardRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PROJECT_ROOT, **kwargs)

    def do_GET(self):
        path = urlsplit(self.path).path

        if path in {"/", "/web", "/web/"}:
            self.send_response(302)
            self.send_header("Location", "/web/index.html")
            self.end_headers()
            return

        if should_refresh(self.path):
            try:
                with REFRESH_LOCK:
                    refresh_flight_data()
            except Exception as error:
                self.send_refresh_error(error)
                return

        super().do_GET()

    def end_headers(self):
        if urlsplit(self.path).path.endswith(".html"):
            self.send_header("Cache-Control", "no-store, max-age=0")
            self.send_header("Pragma", "no-cache")
        super().end_headers()

    def send_refresh_error(self, error: Exception):
        message = html.escape(str(error))
        body = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Refresh failed</title></head>
<body>
    <h1>Flight data refresh failed</h1>
    <p>{message}</p>
    <p>Check the server terminal for details, then reload this page to try again.</p>
</body>
</html>
""".encode("utf-8")

        self.send_response(503)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Serve the dashboard and refresh flight data on each page load."
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8000, type=int)
    return parser.parse_args()


def serve(host: str, port: int):
    server = ThreadingHTTPServer((host, port), DashboardRequestHandler)
    print(f"Dashboard available at http://{host}:{server.server_port}/web/index.html")
    print("Flight data refreshes before each dashboard page is served.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping dashboard server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    arguments = parse_args()
    serve(arguments.host, arguments.port)
