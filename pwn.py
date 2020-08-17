import socket
import struct
import sys

class Tcp:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.status = True

    def __repr__(self):
        return "Tcp({}, {})".format(self.host, self.port)

    def b2h(self, bindata):
        return bindata.hex()     

    def h2b(self, hexdata, CHUNKSIZE = 4, packFormat="<H"):
        if hexdata is list:
            raw = hexdata
        else:
            raw = [hexdata]

        hex_data = []
        hex_string = ""

        for i in raw:
            if i is int:
                hex_string +=  hex(i).replace("0x", "")
            elif i is str:   
                hex_string += i.replace("0x", "")

        while len(hex_string) >= CHUNKSIZE:
            hex_data.append(hex_string[:CHUNKSIZE])
            hex_string = hex_string[CHUNKSIZE:]

        if hex_string != "":
            hex_data.append("0"*(CHUNKSIZE-len(hex_string)) + hex_string)

        try:
            for i,j in enumerate(hex_data):
                hex_data[i] = int(j, 16)
        except ValueError:
            raise(ValueError("\"{}\" is not hex!\n".format(i)))
        res = b""
        for i in hex_data:
            res += struct.pack(packFormat, i)


    def connect(self):
        if self.status:
            self.conn.close()
        self.conn.connect((self.host, self.port))

    def disconnect(self):
        if self.status:
            self.conn.close()


    def sendstring(self, string, encoding="utf-8"):
        self.conn.sendall(string.encode(encoding))

    def sendbin(self, bytestring):
        self.conn.sendall(bytestring)

    def sendhex(self, hexdata, CHUNKSIZE=4, packFormat="<H"):
        self.sendbin(self.h2b(hexdata, CHUNKSIZE=CHUNKSIZE=, packFormat=packFormat))

    def sendstringln(self, string, encoding="utf-8", linending=b"\n"):
        self.conn.sendall(string.encode(encoding + linending))

    def sendbinln(self, bytestring, linending=b"\n"):
        self.conn.sendall(bytestring + linending)

    def sendhexln(self, hexdata, CHUNKSIZE=4, packFormat="<H", linending=b"\n"):
        self.sendbin(self.h2b(hexdata + linending, CHUNKSIZE=CHUNKSIZE=, packFormat=packFormat))


    def recvall(self, BUFF_SIZE = 2048):
        data = b""
        while True:
            part = self.conn.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data

    def recvuntil(self, char, BUFF_SIZE = 2048):
        data = b""
        while True:
            part = self.conn.recv(BUFF_SIZE)
            data += part
            if char in part:
                break
        return data

    def recvuntilfunc(self, func, BUFF_SIZE = 2048, args=[]):
        data = b""
        while True:
            part = self.conn.recv(BUFF_SIZE)
            data += part
            if func(self, conn, data, part, BUFF_SIZE, args)) == True:
                break
        return data