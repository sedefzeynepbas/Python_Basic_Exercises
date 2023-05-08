print("""************************
Hesap Makinesi Programı

İşlemler;
1- Toplama
2- Çıkarma
3- Çarpma
4- Bölme
************************
""")

a = float(input("Birinci Sayı: "))
b = float(input("İkinci Sayı: "))
işlem = float(input("İşlemi giriniz: "))
if işlem == 1:
    print("{} + {}'in toplamı {}'dır.".format(a,b,a+b))
elif işlem == 2:
    print("{} - {}'in farkı {}'dır.".format(a,b,a-b))
elif işlem == 3:
    print("{}'nın * {} ile çarpımı {}'dır.".format(a,b,a*b))
elif işlem == 4:
    print("{}'nın / {}'ya bölümü {}'dır.".format(a,b,a/b))
else:
    print("Geçersiz İşlem!")