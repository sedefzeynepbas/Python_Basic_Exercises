"""

"""

def asal_mi(a):
    b = 0
    for i in range(1,a+1):
        liste_k = []
        k = a % 2
        liste_k += [k]
        if liste_k[1:a-1] == 0:
            b += 1
    if b == 0 and not a <=1:
        print("{} bir asal sayıdır!".format(a))
    else:
        print("{} bir asal sayı değildir!".format(a))
asal_mi(93)


