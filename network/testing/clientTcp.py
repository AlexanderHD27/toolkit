import socket
import sys

def recvall(sock, BUFF_SIZE = 2048):
        data = b""
        while True:
            part = sock.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data   

if len(sys.argv) < 3:
    sys.stderr.write("Usage: <host> <port>\n")
    exit()
else:
    try:
        port = int(sys.argv[2])
    except ValueError:
        sys.stderr.write("Invaild Port Number\n")
        exit()

    address = sys.argv[1]

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print("Connecting...")
    conn.connect((address, port))
    print("Got connection to {} on port {}".format(address[0], address[1]))
except ConnectionRefusedError:
    sys.stderr.write("Connection Refused\n")
    exit()
except socket.gaierror:
    sys.stderr.write("Invaild Address\n")
    exit()

try:
    while True:
        print(recvall(conn).decode("utf-8"))
        conn.sendall(input("$ ").encode("utf-8"))
except ConnectionAbortedError:
    print("The Connection was closed by the server")
except KeyboardInterrupt:
    print("Abord")
