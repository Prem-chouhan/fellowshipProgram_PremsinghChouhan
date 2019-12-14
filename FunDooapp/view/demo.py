# import requests
# import json
#
#
# payload = {"fname": "prem",
#            "lname": "Chouhan",
#            "Email": "premchouhan007@gmail.com",
#            "password": "premsingh",
#            "confirm_password": "premsingh"
#            }
# r = requests.post("http://127.0.0.1:8000", data=payload, json="register.json")
#
# print(r)

import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html("hi!"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(self._html("POST!"))

