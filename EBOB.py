

def ebob(liste):
    liste_l= []
    b = []
    c =[]
    eks = min(liste)
    for i in range(1, eks+1):
        for n in liste:
            if n % i == 0:
                c += [i]
    for j in c:
        if j not in liste_l:
            liste_l += [j]
        else:
            b += [j]
    for h in b:
        if b.count(h) == (len(liste)-1):
            ebob = h
    return ebob

print(ebob([7,14,21]))
