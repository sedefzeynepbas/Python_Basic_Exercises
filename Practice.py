class IkiBasamak:

    def __init__(self, onlar_bas, birler_bas):
        self.onlar_bas = onlar_bas
        self.birler_bas = birler_bas

    def sayi_birlestirme(self):
        ys = str(self.onlar_bas)+str(self.birler_bas)
        print("Basamaklar birleştirildi, sayı: {} ".format(ys))

    def toplama(self):
        ys = self.onlar_bas+self.birler_bas
        print("Sayılar toplandı, sayı: {} ".format(ys))

    def sinus_kosinus(self):
        from math import sin, cos, radians
        print(self.onlar_bas, "'in sinüsü (rad): ", sin(radians(self.onlar_bas)))
        print(self.onlar_bas, "'in kosinüsü (rad): ", cos(radians(self.onlar_bas)))
        print(self.birler_bas, "'in sinüsü (rad): ", sin(radians(self.birler_bas)))
        print(self.birler_bas, "'in kosinüsü (rad): ", cos(radians(self.birler_bas)))

    def onlar_bas_arti_sayi(self, b1, b2):
        c = b1+b2+str(self.onlar_bas)
        print(c)

    def deneme(self, k, h, m):
        import time
        if k == 5 and h == 4 and m == 3:
            print("Tüm sayılar doğru...")
        elif k == 5 and h != 4 and m != 3:
            print("Sadece 1. Sayı doğru!")
        elif k != 5 and h == 4 and m != 3:
            print("Sadece 2. Sayı doğru!")
        elif k != 5 and h != 4 and m == 3:
            print("Sadece 3. Sayı doğru!")
        elif k == 5 and h == 4 and m != 3:
            print("1. ve 2. Sayı doğru!")
        elif k != 5 and h == 4 and m == 3:
            print("2. ve 3. Sayı doğru!")
        elif k == 5 and h != 4 and m == 3:
            print("1. ve 3. Sayı doğru!")
        else:
            print("Bekleyiniz...")
            time.sleep(2)
            print("Tüm sayılar yanlış!")

    def tan_atan(self, y):
        import math
        print("Tanjant", self.onlar_bas + y, "=", math.tan(math.radians(self.onlar_bas + y)))
        print(self.onlar_bas)
        print("ArcTanjant", self.onlar_bas + y, "=", math.atan(math.radians(self.onlar_bas + y)))
        print(self.onlar_bas)


class Sayilar(IkiBasamak):
    def __init__(self, yuzler_bas, onlar_bas, birler_bas, ):
        super().__init__(onlar_bas, birler_bas)
        self.yuzler_bas = yuzler_bas

    def sayi_birlestirme(self):
        ys = str(self.yuzler_bas) + str(self.onlar_bas) + str(self.birler_bas)
        print("Basamaklar birleştirildi, sayı: {} ".format(ys))

    def toplama(self):
        ys = self.onlar_bas + self.birler_bas + self.yuzler_bas
        print("Sayılar toplandı, sayı: {} ".format(ys))

    def sayma(self, r):
        print(*range(self.onlar_bas, r+1))

    def t_at_rad(self, y, z):
        super().tan_atan(y)
        import math
        ç = math.radians(z)
        print("{}'in radyanı: {}'dir.".format(z, ç))



class Stringler():
    def __init__(self, kelime, cümle, şiir):
        self.kelime = kelime
        self.cümle = cümle
        self.şiir = şiir
    def kac_kelime(self):
        b = 0
        c = 0
        k = self.cümle.split(" ")
        l = self.şiir.split(" ")
        f = input("Hangisinin kelime sayısını öğrenmek istiyorsunuz yazınız (Şiir veya Cümle): ")
        print(l)
        if f == "Cümle":
            for i in k:
                b += 1
            print("Cümleniz {} kelimeden oluşmaktadır.".format(b))
        else:
            for j in l:
                c += 1
            print("Şiiriniz {} kelimeden oluşmaktadır.".format(c))

    def kac_harf(self):
        f = input("Hangisinin harf sayısını öğrenmek istiyorsunuz yazınız (Şiir, Cümle veya Kelime): ")
        if f == "Şiir":
            b = 0
            for i in self.şiir:
                if i != " " and i != "," and i != "!" and i != ".":
                    b +=1
            print("Şiiriniz {} harften oluşmaktadır.".format(b))
        elif f == "Cümle":
            c = 0
            for j in self.cümle:
                if j != " " and j != "," and j != "!" and j != ".":
                    c += 1
            print("Cümleniz {} harften oluşmaktadır.".format(c))
        else:
            d = 0
            for z in self.kelime:
                d += 1
            print("Kelimeniz {} harften oluşmaktadır.".format(d))

    def kac_hece(self):
        hece = 0
        sesli_harfler = "aeıioöuüAEIİOÖUÜ"
        f = input("Hangisinin hece sayısını öğrenmek istiyorsunuz yazınız (Şiir, Cümle veya Kelime): ")
        if f == "Şiir":
            for i in self.şiir:
                for j in sesli_harfler:
                    if j in i:
                        hece += 1
            print("Şiiriniz {} heceden oluşmaktadır.".format(hece))
        elif f == "Cümle":
            for i in self.cümle:
                for j in sesli_harfler:
                    if j in i:
                        hece += 1
            print("Cümleniz {} heceden oluşmaktadır.".format(hece))
        else:
            for i in self.kelime:
                for j in sesli_harfler:
                    if j in i:
                        hece += 1
            print("Kelimeniz {} heceden oluşmaktadır.".format(hece))


    def __str__(self):
        b = ""
        for i in self.şiir:
            if i == i.upper() and i != " " and i != "," and i != "!" and i != ".":
                b += "\n"+i
            else:
                b += i
        return "Kelime:\n{}\n\nCümle:\n{}\n\nŞiir:\n{}".format(self.kelime,self.cümle,b)


    def ayrıstırma(self):
        with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\üç_notlar.txt", "r", encoding="utf-8") as file:
            numaralar = []
            isimler = []
            notlar = []

            for satır in file:
                b = satır.split(",")
                numaralar.extend([b[0],"\n"])
                isimler.extend([b[1],"\n"])
                notlar.extend([b[2],b[3],b[4]])
            with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\numaralar.txt", "w", encoding="utf-8") as file1:
                for i in numaralar:
                    file1.write(i)
            with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\isimler.txt", "w", encoding="utf-8") as file2:
                for j in isimler:
                    file2.write(j)
            with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\notlar.txt", "w", encoding="utf-8") as file3:
                for z in notlar:
                    file3.write(z)
sayib = IkiBasamak(0, 180)
sayit = IkiBasamak(270, 360)
sayic = IkiBasamak(0, 0)


inherit_practice = Sayilar(1, 90, 3)


metin = Stringler("Hilal","İçimde korku nedir kalmıyor yok olmaktan.","Hayatı rayiha gibi sihriyle sindiren toprak, Bugün ne semtine baksam, çiçek, çimen, yaprak! İçinde rahata varmış yatan aziz ölüler, Demek ki böyle bahar örtüsüyle örtülüler!")


class Kumanda():
    def __init__(self,kanal_listesi):
        self.kanal_listesi = kanal_listesi
        self.index = -1

kumanda = Kumanda(["a","b","c","d","e"])
try:
    for i in kumanda:
        print(i)
except TypeError:
        print("TypeError: 'Kumanda' object is not iterable -hatası-")




"""
:).........
"""