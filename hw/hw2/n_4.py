def skobki(r):
    ot = r.count("(")
    zk = r.count(")")
    if ot > zk:
        return "Ne hvataet" + str(ot - zk) + "zakrivaushih skobki!"
    elif ot < zk:
        return "Ne hvataet" + str(zk - ot) + "otkrivaushey skobki!"
    return "Ok!"
kek = input("Vvod: ")
otv = skobki(kek)
print(otv)