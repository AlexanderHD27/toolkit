#!/usr/bin/python3
import sys
sys.path.append("..")

try:
    from network import basic
except:
    import basic

import datetime
import logging
import time
import sys
import os

if len(sys.argv) < 3:
    sys.stderr.write("Usage: <host> <port>\n")
    sys.stderr.flush()
    exit()

def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1).encode("utf-8")
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

getchr = _find_getch()

logging.basicConfig(filename="http.log", format="%(message)s", level=logging.DEBUG)

size = os.get_terminal_size() 

def handler(conn,addr,args):
    try:
        msg = basic.recvall(conn).decode("utf-8")
        if len(msg) > 0:
            address = " {}:{} ".format(addr[0], addr[1])
            logging.debug("="*8 + address + "="*(size[0]-8-len(address)))
            logging.debug(msg)
            logging.debug(datetime.datetime.now())
        conn.sendall(b"HTTP/1.0 404 Not Found\r\nContent-Encoding: utf-8\r\nAccess-Control-Allow-Headers: *\r\nContent-Type: text/html\r\nContent-Length: 0\r\n\r\n")
    except Exception as E:
        logging.debug("="*8 + address + "="*(size[0]-8-len(address)))
        logging.error(str(E))
    
server = basic.Server(sys.argv[1], int(sys.argv[2]))
server.deamon = True
server.start(handler,[])

while True:
    try:
        pass
    except KeyboardInterrupt:
        exit()
