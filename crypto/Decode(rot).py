from crypto import Encode_rot
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
    with open("file.txt", "w") as f:
        f.write(str(alle))
    return(alle)





def intelligentforcing_crypto ( text=l_text, language=0, manual_avable_letters=-1 ):
    b = [i[0] for i in list(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))]
    print(text)
    a = []
    a+=text
    n = 0
    ab = {}
    for n in b:
        ab.update({n:a.count(n)})

    print(ab)
    a_ab = [i[0] for i in list(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890   "))]
    a_ab += ab
    a_ab = str(a_ab)
    with open("file2.txt", "w") as f:
        f.write(str(a_ab ))
    biggest = list(ab.values()).index(sorted(list(ab.values()))[-1])
    print(biggest)
    big_difference = 4-biggest
    print(big_difference)
    returne = Encode_rot.encode(text, big_difference, 4)
    print(returne)

intelligentforcing_crypto("glhvlvwhlqvhkuvhkuodqjhuWhAwdovWhvwiuphlqhSurjudpphh")
