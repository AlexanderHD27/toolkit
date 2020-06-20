import os
import struct

def create(pixelarray, path, colordeth=256, resolutionX=64, resolutionY=64):
    with open(path, "bw+") as bmp:
        # Header
        bmp.write(b"\x00\x00")
        bmp.write(b"\x00\x00")
        bmp.write(b"\x36\x00\x00\x00") # Offset

        # DIB-Header
        bmp.write(b"\x28\x00\x00\x00") # size of DIB-Header
        bmp.write(struct.pack('<Q', len(pixelarray[0]))[:4]) # wight
        bmp.write(struct.pack('<Q', len(pixelarray))[:4]) # hight
        bmp.write(b"\x01\x00") # planes
        bmp.write(struct.pack('<Q', colordeth)[:2]) # color deapht
        bmp.write(b"\x00\x00\x00\x00") # Compression
        bmp.write(struct.pack('<Q', 3)[:4]) # Bytes in the picture
        bmp.write(struct.pack('<Q', resolutionX)[:4]) # Resoltion X
        bmp.write(struct.pack('<Q', resolutionY)[:4]) # Resoltion Y
        bmp.write(b"\x00\x00\x00\x00") # Colors in the Colortable
        bmp.write(b"\x00\x00\x00\x00") # Importend Colors

        # Pixel Data
        bmp.write(b"\x00\xFF\x00")

    with open(path, "rb") as bmp:
        imageContend = bmp.read()

    with open(path, "bw") as bmp:
        bmp.write(b"BM")
        bmp.write(struct.pack('<Q', 2+os.path.getsize(path))[:4])
        bmp.write(imageContend)