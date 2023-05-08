
import random
import time

print("""
**************************************
Sayı tahmin oyunu

1 ile 40 arasında sayıyı tahmin edin.

**************************************
""")

rastgele_sayi = random.randint(1, 40)
tahmin_hakki = 7
while True:
    tahmin = int(input("Tahmininiz: "))
    if tahmin < rastgele_sayi:
        print("Bilgiler sorgulanıyor... ")
        time.sleep(1)
        print("Daha yüksek bir sayı tahmin edin")
        tahmin_hakki -= 1
    elif tahmin > rastgele_sayi:
        print("Bilgiler sorgulanıyor... ")
        time.sleep(1)
        print("Daha düşük bir sayı tahmin edin")
        tahmin_hakki -= 1
    else:
        print("Bilgiler sorgulanıyor... ")
        time.sleep(1)
        print("Tebrikler, bildiniz!", rastgele_sayi)
        break
    if tahmin_hakki == 0:
        print("Tahmin hakkınız bitti...")
        print("Sayımız:", rastgele_sayi)
        break
