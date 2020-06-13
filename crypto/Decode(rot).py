l_text = """dwhhk"""


def encotion (a, text, encode_level):
    v_text = ""
    for i in text:
        if i in a:
            v_text += a[(a.index(i) + encode_level) % len(a)]
    return v_text


def bruteforceing_crypto (text=l_text):
    alle = []
    n = 0
    a = [i[0] for i in list(zip("abcdefghijklmnopqrstuvwxyz"))]
    while n < len(a):
        n_text = str(encotion(a, text, n))
        n += 1
        alle.append( n_text)
    n = 0
    a = [i[0] for i in list(zip("abcdefghijklmnopqrstuvwxyz1234567890"))]
    while n < len(a):
        n_text = str(encotion(a, text, n))
        n += 1
        alle.append( n_text)
    n = 0
    a = [i[0] for i in list(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))]
    while n < len(a):
        n_text = str(encotion(a, text, n))
        n += 1
        alle.append( n_text)
    n = 0
    a = [i[0] for i in list(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))]
    while n < len(a):
        n_text = str(encotion(a, text, n))
        n += 1
        alle.append( n_text)
    print(alle)
    with open("file.txt", "w") as f:
        f.write(str(alle))





def intelligentforcing_crypto ( text=l_text, language=0, manual_avable_letters=-1 ):
    print(text)