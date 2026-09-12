import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

port = int(os.environ.get('PORT', '8080'))
server = ThreadingHTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
print(f'Serving EVO Sites demo on port {port}', flush=True)
server.serve_forever()
