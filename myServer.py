from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, world!')

def run_server():
    host = '127.0.0.1'
    port = 8000

    server = HTTPServer((host, port), SimpleHTTPRequestHandler)
    print("working")
    # print(f'Server running on http://{host}:{port}/')

    server.serve_forever()

run_server()

