import time
import random
import math


class Bilgisayar():

    def __init__(self, pc_durumu = "Off", browser_listesi = ["Yandex", "Chrome"], sekme_listesi = ["Google"], program_listesi = ["MexX"]):
        self.browser_listesi = browser_listesi
        self.sekme_listesi = sekme_listesi
        self.program_listesi = program_listesi
        self.pc_durumu = pc_durumu

    def __str__(self):
        return "Bilgisayar Durumu: {}\nBrowser Listesi: {}\nSekme Listesi: {}\nProgram Listesi: {}".format(self.pc_durumu,self.browser_listesi,self.sekme_listesi,self.program_listesi)

    def __len__(self):
        return len(self.program_listesi)

    def sekme_ac(self, sekme_ismi):
            self.sekme_listesi.append(sekme_ismi)

    def sekme_kapat(self):
        l = 1
        for i in self.sekme_listesi:
            print(l, ". Sekme: ", i)
            l += 1
        d = int(input("Kapatılacak sekmenin numarasını giriniz: "))
        self.sekme_listesi.pop(d-1)

    def program_yukle(self, program_ismi):
        self.program_listesi.append(program_ismi)

    def program_sil(self):
        l = 1
        for i in self.program_listesi:
            print(l, ". Sekme: ", i)
            l += 1
        d = int(input("Silinecek programın numarasını giriniz: "))
        self.program_listesi.pop(d - 1)
bilgisayar1 = Bilgisayar()

while True:

    islem = input("İşlem numarasını giriniz: ")
    if islem == "q":
        print("Bilgisayar Kapatılıyor...")
        break
    elif islem == "1":
        print(bilgisayar1)
    elif islem == "2":
        print("Program sayısı: ", len(bilgisayar1))
    elif islem == "3":
        sekme_isimleri = input("Açılacak sekme isimlerini ',' ile ayırarak giriniz: ")
        sekme_listesi = sekme_isimleri.split(",")
        for m in sekme_listesi:
            print("Sekme Açılıyor...")
            time.sleep(1)
            bilgisayar1.sekme_ac(m)
    elif islem == "4":
        bilgisayar1.sekme_kapat()
    elif islem == "5":
        program_isimleri = input("Yüklenecek program isimlerini '-' ile ayırarak giriniz: ")
        program_listesi = program_isimleri.split("-")
        for j in program_listesi:
            bilgisayar1.program_yukle(j)
    elif islem == "6":
        bilgisayar1.program_sil()



