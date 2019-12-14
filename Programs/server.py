import os
from http.server import HTTPServer, BaseHTTPRequestHandler

data = {
    "username": "sathya"
}


class ServiceHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)

    # def _html(self, message):
    #     content = message
    #     return content.encode("utf8")

    # def do_GET(self):
    #     openfile(self)

    def do_POST(self):
        if self.path == '/register':
            pass


server = HTTPServer(('127.0.0.1', 8085), ServiceHandler)
server.serve_forever()
