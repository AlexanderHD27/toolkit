l_text = """programm proof 1234567890ß!"§$%&/()=?@+*~#'-_.:,;"""
l_sed = 1
def encotion (a, text, encode_level):
    z = len(a) - 1
    while z > 0:
        z =z-1
        text = text.replace(a[z], a[z + encode_level])
        print(text)
    return text

def encode ( text=l_text, encode_level=1, sed=l_sed ):
    l_text = text
    l_sed = sed
    if sed==1 :
        a = [i[0] for i in list(zip("abcdefghijklmnopqrstuvwxyz"))]
        n_text=encotion(a, text, encode_level)
    elif sed==2 :
        a = [i[0] for i in list(zip("abcdefghijklmnopqrstuvwxyz1234567890"))]
        encotion(a, text, encode_level)
        n_text = encotion(a, text, encode_level)
    elif sed==3 :
        a = [i[0] for i in list(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))]
        encotion(a, text, encode_level)
        n_text = encotion(a, text, encode_level)
    elif sed==4 :
        a = [i[0] for i in list(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))]
        encotion(a, text, encode_level)
        n_text = encotion(a, text, encode_level)
    else :
       a = [i[0] for i in list(zip(sed))]
       encotion(a, text, encode_level)
       n_text = encotion(a, text, encode_level)
    print(a)
    print(n_text)
encode()
