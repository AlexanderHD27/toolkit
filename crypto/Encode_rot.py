l_text = """programm proof 1234567890ß!"§$%&/()=?@+*~#'-_.:,;"""
l_sed = 1
def encotion (a, text, encode_level):
    v_text = ""
    for i in text:
        if i in a:
            v_text += a[(a.index(i) + encode_level) % len(a)]
    return v_text

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
    return(n_text)
a = encode("dies ist ein sehr sehr langer Text als Test für meine Programme eeeeeeeeeeeee", 3, 4)
print(a)