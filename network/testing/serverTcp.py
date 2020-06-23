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

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((address, port))
sock.settimeout(1)

try:
    while True:
        print("Listing...")
        while True:
            try:
                sock.listen()
                conn, addr = sock.accept()
                print("Got connection form {} on port {}".format(addr[0], addr[1]))
                break
            except socket.timeout:
                continue
            
        try:
            while True:
                conn.sendall(input("$ ").encode("utf-8"))
                print(recvall(conn).decode("utf-8"))
        except ConnectionAbortedError:
            print("Connection was closed by the client")


except KeyboardInterrupt:
    print("Abord")
    exit()