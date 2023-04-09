#! /usr/bin/env python3

import http.server
import subprocess
import os
import sys

global stream

print('NetBoot Server')


class RequestHandle(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            executeScript = subprocess.run(
                ["python3", os.getcwd() + "/netboot/netdimm_menu", os.environ['DIMM_IP'], os.getcwd()+"/netboot/roms"])
            print("booted with %d" % executeScript.returncode)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Menu booted')
        else:
            self.send_response_only(404)


try:
    os.environ["DIMM_IP"]
except:
    print("Please set DIMM_IP en var")
    sys.exit()


server = http.server.HTTPServer(('', 8000), RequestHandle)

server.serve_forever()
