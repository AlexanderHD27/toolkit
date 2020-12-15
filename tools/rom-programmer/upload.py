import os
import sys
import time
import serial

max_size = 256

def progressbar(sum, iteration, suffix="", prefix="", length=50):
    percent = ("{0:." + str(1) + "f}").format(100 * (iteration / sum))
    filledLength = int(length * iteration // sum)
    bar = "█" * filledLength + '-' * (length - filledLength)
    sys.stdout.write('\r%s |%s| %s%% %s' % (suffix, bar, percent, prefix))
    sys.stdout.flush()

def getNumber(s, line):
    if len(s) > 2:
        if s[:2] == "0x":
            try:
                return int(s, 16)
            except ValueError:
                sys.stderr.write("Invalid Number {} in line {}\n".format(s, line))
                sys.stderr.flush()
                exit()
        elif s[:2] == "0b":
            try:
                return int(s, 2)
            except ValueError:
                sys.stderr.write("Invalid Number {} in line {}\n".format(s, line))
                sys.stderr.flush()
                exit()

    try:
        return int(s)
    except ValueError:
        sys.stderr.write("Invalid Number {} in line {}\n".format(s, line))
        sys.stderr.flush()
        exit()

if len(sys.argv) < 3:
    sys.stderr.write("Usage: <file> <port>\n")
    sys.stderr.flush()
    exit()

path = sys.argv[1]
port = sys.argv[2]

if "--clean" in sys.argv or "-c" in sys.argv:
    clean = True
else:
    clean = False

if not (os.path.isfile(path) and os.access(path, os.R_OK)):
    sys.stderr.write("File doesn't exist or doesn't have the right permssions\n")
    sys.stderr.flush()
    exit()

# Compiling
with open(path, "r") as f:
    data = f.read().strip().split("\n")

pages = []
already_in = []

if clean:
    sys.stdout.write("Compiling... ")
    sys.stdout.flush()

for j,i in enumerate(data):
    if not clean:
        progressbar(len(data), j+1, "Compiling:")

    page = i.strip().split(" ")

    if len(page) > 65:
        sys.stderr.write("Page in line {} to large".format(j+1))

    if len(page) < 1:
        continue

    elif not (len(page) > 1 and page[0][-1] == ":"):
        sys.stderr.write("Wrong format in line {}\n".format(j+1))
        sys.stderr.flush()
        exit()

    pages.append([])
    page[0] = page[0][:-1]
    for k in page:
        n = getNumber(k, j)
        if n >= max_size:
            sys.stderr.write("Value to large in line {}\n".format(j))
            sys.stderr.flush()
            exit()
        pages[-1].append(n)

    if pages[-1][0] in already_in:
        sys.stderr.write("Same page can not be written twice\n")
        sys.stderr.flush()
        exit()
    else:
        already_in.append(i[0])


if clean:
    sys.stdout.write("Done")
    sys.stdout.flush()

print()

# Upload
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=None)
except Exception as E:
    sys.stderr.write("An error occurred while opening port: {}".format(E))
    sys.stderr.flush()
    exit()

while ser.inWaiting() == 0:
    pass
ser.read_all()

if not clean:
    progressbar(1, 0, "Uploading:", "{}/{}".format(len(pages), 0))
else:
    sys.stdout.write("Uploading... ")
    sys.stdout.flush()

total_size = 0

for n,i in enumerate(pages):
    page = i[1:]

    ser.write(i[0].to_bytes(1, "big") + len(page).to_bytes(1, "big"))
    while ser.inWaiting() == 0:
        pass
    ser.read_all()

    data = b""
    size = len(page)
    data_pointer = 0

    while size > 32:
        data = b""
        for j in range(32):
            data += page[j+data_pointer].to_bytes(1, "big")
        ser.write(data)

        while ser.inWaiting() == 0:
            pass
        ser.read_all()
        data_pointer += 32
        size -= 32
        total_size += 32
    
    data = b""
    for j in range(size):
        data += page[j+data_pointer].to_bytes(1, "big")
    ser.write(data)
    total_size += size

    while ser.inWaiting() == 0:
        pass
    ser.read_all()

    ser.write(b"OK")

    while ser.inWaiting() == 0:
        pass
    ser.read_all()

    if not clean:
        progressbar(len(pages), n, "Uploading:", "{}/{}".format(len(pages), n))

ser.close()

if not clean:
    progressbar(len(pages), len(pages), "Uploading:", "{}/{}".format(len(pages), len(pages)))
else:
    sys.stdout.write("Done")
    sys.stdout.flush()

print()
print("\nUpload: {} pages worth {} bytes\nDone".format(len(pages), total_size))