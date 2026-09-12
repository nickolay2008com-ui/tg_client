import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler


class DemoHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("X-Robots-Tag", "noindex, nofollow, noarchive")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        super().end_headers()


port = int(os.environ.get("PORT", "8080"))
server = ThreadingHTTPServer(("0.0.0.0", port), DemoHandler)
print(f"Serving EVO Sites demo on port {port}", flush=True)
server.serve_forever()
