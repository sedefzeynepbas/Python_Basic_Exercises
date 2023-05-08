"""Problem 2
Armstrong sayısı: eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı
( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

"""

sayi = input("Armstrong sayısı olması sorgulanacak sayıyı giriniz: ")
basamak = len(sayi)
u = 0
t = 0
liste = []
for i in sayi:
    i = int(i)
    liste = liste + [i]
for n in liste:
    u = n**basamak
    t = t + u
if t == int(sayi) and t != 0:
    print("{} bir Armstrong sayısıdır!".format(sayi))
else:
    print("{} bir Armstrong sayısı değildir!".format(sayi))
