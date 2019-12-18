import argparse
import sys
import json

sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/templates/')
sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/view/')

from http.server import HTTPServer, BaseHTTPRequestHandler
from registration import registration
from response import Response


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "json")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        pass
        # self._set_headers()
        if self.path == '/forgot':
            obj = registration
            obj.forgot_password(self)
            # response_data = {'success': True, "data": [], "message": "Password Updated  Successfully"}
            # Response(self).jsonResponse(status=200, data=response_data)


        # if self.path == '/register':
        #     # with open('templates/register.html', 'r') as f:
        #     #     html_string_register = f.read()
        #     #     self.wfile.write(self._html(html_string_register))
        #     response_data = {'success': True, "data": [], "message": "Registered Successfully"}
        #     Response(self).jsonResponse(status=200, data=response_data)
        #
        # elif self.path == '/login':
        #     # with open('templates/login.html', 'r') as f:
        #     #     html_string_login = f.read()
        #     #     self.wfile.write(self._html(html_string_login))
        #     response_data = {'success': True, "data": [], "message": "Login Successfully"}
        #     Response(self).jsonResponse(status=200, data=response_data)

        # else:
            # with open('templates/error.html', 'r') as f:
            #     html_string_register = f.read()
            #     self.wfile.write(self._html(html_string_register))
            # response_data = {'success': False, "data": [], "message": "URL Invalid"}
            # Response(self).jsonResponse(status=404, data=response_data)

    def do_HEAD(self):
        # self._set_headers()
        pass

    def do_POST(self):
        # Doesn't do anything with posted data
        if self.path == '/register':
            obj = registration
            obj.register(self)
        elif self.path == '/login':
            obj = registration
            obj.login(self)
        else:
            response_data = {'success': False, "data": [], "message": "URL Invalid"}
            Response(self).jsonResponse(status=404, data=response_data)
        # self._set_headers()


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8888):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8888,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)
