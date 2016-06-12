import os
import os.path
import socket
import json
from functools import partial

class Mpv(object):
    commands = ['']
    def __init__(self, sockfile='/tmp/mpvsock'):
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        if os.path.exists(sockfile):
            s.connect(sockfile)
            self.fd = s
            print(sockfile, 'loaded')

    def execute(self, command):
        data = json.dumps(command) + '\r\n'
        data = bytes(data, encoding='utf-8')
        self.fd.send(data)
        buf = self.fd.recv(1024)
        return buf

    def command(self, command, *args):
        return self.execute({'command': [command, *args]})

    def close(self):
        self.fd.close()

    def __getattr__(self, name):
        return partial(self.command, name)

