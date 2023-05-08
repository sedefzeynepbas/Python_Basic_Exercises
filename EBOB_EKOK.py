"""
*********************
EBOB - EKOK BULUNMASI
*********************
"""


def primenumbers(start, stop):
    primenumbers = []
    numbers = []
    for i in range(start, stop):
        numbers.append(i)
        remainder = [i % n for n in numbers]
        if remainder.count(0) == 2:
            primenumbers.append(i)
    return primenumbers


def ebobekok(liste, type):

    if type == "EKOK":
        numberlist = liste
        primelist = primenumbers(1, max(numberlist)+1)
        i = 0
        ekok = 1
        while True:
            remainder = [n % primelist[i] for n in numberlist]
            for j in range(len(numberlist)):
                if numberlist[j]/primelist[i] == int(numberlist[j]/primelist[i]):
                    numberlist[j] = numberlist[j]/primelist[i]
            if remainder.count(0) == 0:
                i += 1
                continue
            ekok*=primelist[i]
            if numberlist.count(1) == len(numberlist):
                break
        return ekok


    if type == "EBOB":
        liste_l = []
        b = []
        c = []
        eks = min(liste)
        for i in range(1, eks + 1):
            for n in liste:
                if n % i == 0:
                    c += [i]
        for j in c:
            if j not in liste_l:
                liste_l += [j]
            else:
                b += [j]
        for h in b:
            if b.count(h) == (len(liste) - 1):
                ebob = h
        return ebob

print(ebobekok([5,20,82,76], "EKOK"))

"""
**********************
İşlemler:
EBOB
EKOK
**********************
"""






