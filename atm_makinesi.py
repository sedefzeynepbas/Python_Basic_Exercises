print("""
************************************
Atm Makinesine Hoşgeldiniz.

İşlemler:

1-Bakiye Sorgulama
2-Para Yatırma
3-Para çekme

Programdan çıkmak için 'q' ya basın.
************************************
""")

bakiye = 1000

while True:
    islem = input("İşlemi seçiniz: ")
    if islem == "q":
        print("Yine bekleriz!")
        break
    elif islem == "1":
        print("Bakiyeniz {} tldir.".format(bakiye))
    elif islem == "2":
        miktar = float(input("Yatırılacak miktarı giriniz: "))
        bakiye += miktar
        print("Paranız başarıyla yatırılmıştır! ")
    elif islem == "3":
        miktar = float(input("Çekilecek miktarı giriniz: "))
        if bakiye < miktar:
            print("Yetersiz Bakiye! ")
            continue
        else:
            print("Paranızı almayı unutmayın! ")
            bakiye -= miktar
    else:
        print("Geçersiz İşlem...")
