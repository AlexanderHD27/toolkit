


def inteligent_saveing (Filename, changeplace, Changes):
    f1 = open(Filename, "r")
    f1.seek(changeplace)
    f1.write(Changes)
    print(f1)
    f1.close()

inteligent_saveing("file.txt", 0, "61")