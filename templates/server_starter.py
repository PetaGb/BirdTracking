import http.server
import socketserver

PORT_BLACK_TRIANGLE = 8000
PORT_PINK_TRIANGLE = 8001
DIRECTORY = '/home/peter/PycharmProjects/BirdTracking/templates'

class BlackTriangleRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/redirect.html'
        return super().do_GET()


class PinkTriangleRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/redirect_2.html'
        return super().do_GET()


with socketserver.TCPServer(("", PORT_BLACK_TRIANGLE), BlackTriangleRequestHandler) as httpd_black:
    print(f"Serving black triangle at http://localhost:{PORT_BLACK_TRIANGLE}")
    with socketserver.TCPServer(("", PORT_PINK_TRIANGLE), PinkTriangleRequestHandler) as httpd_pink:
        print(f"Serving pink triangle at http://localhost:{PORT_PINK_TRIANGLE}")
        httpd_pink.serve_forever()
    httpd_black.serve_forever()
