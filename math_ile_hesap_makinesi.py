
print("""
Yapılabilecek işlemler:

1- +
2- -
3- x
4- /
5- sin()
6- cos()
7- tan()
8- ln(x)
9- log(x)
10- kök x
11- 10^x
12- x^3
13- x^2

İşlem numarasını giriniz, çıkmak için "0"a basınız.
""")





from math import *

def hesap_makinesi():
    while True:
        islem = int(input("İşlemi giriniz: "))
        if islem == 0:
            break
        elif islem == 1:
            s1 = float(input("1. Sayı: "))
            s2 = float(input("2. Sayı: "))
            print(s1 + s2)
        elif islem == 2:
            s1 = float(input("1. Sayı: "))
            s2 = float(input("2. Sayı: "))
            print(s1-s2)
        elif islem == 3:
            s1 = float(input("1. Sayı: "))
            s2 = float(input("2. Sayı: "))
            print(s1*s2)
        elif islem == 4:
            s1 = float(input("1. Sayı: "))
            s2 = float(input("2. Sayı: "))
            print(s1/s2)
        elif islem == 5:
            s1 = float(input("Sayı: "))
            print(sin(radians(s1)))
        elif islem == 6:
            s1 = float(input("Sayı: "))
            print(cos(radians(s1)))

hesap_makinesi()


