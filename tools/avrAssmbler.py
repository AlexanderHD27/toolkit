#!/usr/bin/python3
import subprocess
import sys
import os

columns, rows = os.get_terminal_size(0)

GREEN = "\33[32m"
RED = "\33[31m"
RESET = "\33[0m"

if len(sys.argv) < 3:
    sys.stderr.write("Usage: <file> <port>\n")
    sys.stderr.flush()
    exit()

file = sys.argv[1]
port = sys.argv[2]

p1 = subprocess.run("avra {}".format(file), shell=True, capture_output=True)
out = [i + "\n" for i in p1.stdout.decode("utf-8").split("\n")]
error = p1.stderr.decode("utf-8")

print("="*int((columns-10)/2) + " compiler " + "="*int((columns-10)/2))



# com pil er

if len(error) > 0:
    print(RED + "ERROR:")
    print(error[:-1] + RESET)
    print("="*columns)
    exit()

else:
    print("".join(out[16:-2])[:-1])


print("="*int((columns-10)/2) + " flashing " + "="*int((columns-10)/2))


p2 = subprocess.run("avrdude -p m328p -c arduino -P {} -b 57600 -D -F -U flash:w:{}.hex".format(sys.argv[2], file.replace("." + file.split(".")[-1], "")), shell=True, capture_output=True)

if not "-p" in sys.argv:
    os.system("rm {file}.cof {file}.obj rm {file}.eep.hex {file}.hex".format(file=file.replace("." + file.split(".")[-1], "")))

if not "Fuses OK" in p2.stderr.decode("utf-8"):
    print(RED + "".join([i + "\n" for i in p2.stderr.decode("utf-8").split("\n")][:-4])[:-1] + RESET)
    print("="*columns)
    exit()

print("".join([i + "\n" for i in p2.stderr.decode("utf-8").split("\n")][1:-2])[1:-1])
print("="*columns)