import pickle
import socket
import socketserver

from FPrinter_Driver.FP_Tremol import FP_Tremol as FPT
from datetime import *

class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(40960).strip()
        msg_client = str(data)
        start_code = msg_client.find('/s')
        res = tremol.fiscal_receipt(msg_client[start_code + 2:], 'server')
        print(res)


if __name__ == '__main__':
    tremol = FPT()
    tremol.OpenPort()
    try:
        print('Server Start')
        server = socketserver.TCPServer(('', 8880), EchoTCPHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print(': exit server ok')