""" Problem 1
Bir sayı kendi hariç bölenlerinin toplamına eşitse bu sayıya mükemmel sayı denir

Örnek: 1 + 2 + 3 = 6


"""
a = int(input("Mükemmel sayı olması sorgulanacak sayıyı giriniz: "))
liste = []
b = 0
for i in range(1,a+1):
    if a % i == 0:
        liste = liste + [i]
if liste != []:
    liste.pop()
for m in liste:
    b = b + m
if b == a and a != 0:
    print("{} bir mükemmel sayıdır!".format(a))
else:
    print("{} bir mükemmel sayı değildir!".format(a))


