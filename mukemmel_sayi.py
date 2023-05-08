"""

"""


def muk(sayi):
    top = 0
    for n in range(1, sayi):
        if sayi % n == 0:
            top += n
    if top == sayi:
        return sayi


for i in range(1, 1000):
    if muk(i):
        print("Mükemmel Sayı:", i)
