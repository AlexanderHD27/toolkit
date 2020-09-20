#!/usr/bin/python3
import sys
import os

if len(sys.argv) < 2:
    sys.stderr.write("Usage: <file> [<format>] [<loader>]\n")
    sys.stderr.flush()
    exit()

if len(sys.argv) > 2:
    FORMAT = sys.argv[2]
else:
    FORMAT = "elf32"

if len(sys.argv) > 3:
    LOADER = sys.argv[3]
else:
    LOADER = "elf_x86_64"


name = ""

for i in sys.argv[1].split(".")[:-1]:
    name += i

os.system("nasm -f elf64 {} -o {}.o".format(sys.argv[1], name)) 
os.system("ld -m {} -o {} {}.o ".format(LOADER, name, name))
os.system("rm {}.o".format(name))