import struct
import sys

if len(sys.argv) < 2:
    sys.stderr.write("Usage: <hex>\n")
    sys.stderr.flush()
    exit(1)

CHUNKSIZE = 4 
hex_data = []
hex_string = ""

for i in sys.argv[1:]:   
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
    sys.stderr.write("\"{}\" is not hex!\n".format(i))
    sys.stderr.flush()
    exit(1)


for i in hex_data:
    sys.stdout.buffer.write(struct.pack("<H", i))