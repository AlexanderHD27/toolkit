try:
    from network import basic
except:
    import basic

import socket
import json
import sys

class Server_comunicator:

    def __init__(self, conn: socket.socket):
        self.conn = conn
        self.encoding = "utf-8"

    def print(self, msg, ending = "\n"):
        self.conn.sendall(b'{"op":"print"}')
        basic.recvall(self.conn)
        msg = str(msg).encode(self.encoding) + str(ending).encode(self.encoding)
        self.conn.sendall(msg)
        basic.recvall(self.conn)

    def input(self, start):
        self.conn.sendall(b'{"op":"input"}')
        basic.recvall(self.conn)
        msg = str(start).encode(self.encoding)
        self.conn.sendall(msg)
        return basic.recvall(self.conn).decode(self.encoding)

    def recvFile(self, name):
        self.conn.sendall(b'{"op":"sendFile"}')
        basic.recvall(self.conn)
        self.conn.sendall(str(name).encode(self.encoding))
        return basic.recvall(self.conn)

    def sendFile(self, name, data: bytes):
        self.conn.sendall(b'{"op":"recvFile"}')
        basic.recvall(self.conn)
        self.conn.sendall(str(name).encode(self.encoding))
        basic.recvall(self.conn)
        self.conn.sendall(data)
        basic.recvall(self.conn)        

    def exit(self):
        self.conn.sendall(b'{"op":"exit"}')
        basic.recvall(self.conn)

class Client_comunicator:

    def __init__(self, sock: socket.socket):
        self.sock = sock
        self.encoding = "utf-8"
        self.operations = {
            "print"    : self.print,
            "input"    : self.input,
            "sendFile" : self.sendFile,
            "recvFile" : self.recvFile
        }

    def print(self, data):
        self.sock.sendall(b"{}")
        sys.stdout.write(basic.recvall(self.sock).decode(self.encoding))
        self.sock.sendall(b"{}")

    def input(self, data):
        self.sock.sendall(b"{}")
        start = basic.recvall(self.sock).decode(self.encoding)
        self.sock.sendall(input(start).encode(self.encoding))

    def sendFile(self, data):
        self.sock.sendall(b"{}")
        name = basic.recvall(self.sock).decode(self.encoding)

        try:
            with open(name, "rb") as f:
                c = f.read()
        except:
            c = b""

        self.sock.sendall(c)

    def recvFile(self, data):
        self.sock.sendall(b"{}")
        name = basic.recvall(self.sock).decode(self.encoding)
        self.sock.sendall(b"{}")
        conntend = basic.recvall(self.sock)
        self.sock.sendall(b"{}")

        with open(name, "wb") as f:
            f.write(conntend)

    def start(self):
        try:
            while True:
                op = json.loads(basic.recvall(self.sock).decode("utf-8"))
                if "op" in op.keys() and op["op"] == "exit":
                    self.sock.sendall(b"{}")
                    return

                if "op" in op.keys() and op["op"] in self.operations.keys():
                    self.operations[op["op"]](op)
            
        except KeyboardInterrupt:
            return self.sock
