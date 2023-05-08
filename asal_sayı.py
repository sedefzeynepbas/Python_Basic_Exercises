"""
Asal sayılar: Sadece 1'e ve kendisine bölünebilen pozitif tam sayılardır.
"""

a = int(input("Asallığını sorgulamak istediğiniz bir pozitif tam sayı giriniz: "))
k = 0
liste_k = []
b = 0
if a < 0:
    print("Negatif bir sayı girdiniz! ")
else:
    for i in range(1, a+1):
        k = a % i
        liste_k += [k]
    for m in liste_k[1:a-1]:
        if m == 0:
            b += 1
    if b > 0 or a == 0 or a == 1:
        print("{} bir asal sayı değildir! ".format(a))
    else:
        print("{} bir asal sayıdır! ".format(a))
