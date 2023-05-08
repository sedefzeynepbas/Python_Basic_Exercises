import random
import time


class Kumanda():

    def __init__(self, tv_durum="Off", tv_ses=0, kanal_listesi=["TRT"], kanal="TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durum == "On":
            print("TV is already on")
        else:
            print("TV is opening...")
            self.tv_durum = "On"

    def tv_kapat(self):
        if self.tv_durum == "Off":
            print("TV is already off.")
        else:
            print("Turning off the TV...")
            self.tv_durum = "Off"

    def ses_ayarla(self):

        while True:
            cevap = input("To Decrease Volume: '<'\nTo Increase Volume: '>'\nTo Exit: 'exit'\n:")
            if cevap == "<" and self.tv_ses != 0:
                self.tv_ses -= 1
                print("Volume: {}".format(self.tv_ses))
            elif cevap == ">" and self.tv_ses != 20:
                self.tv_ses += 1
                print("Volume: {}".format(self.tv_ses))
            elif cevap == "exit":
                print("Volume arranging is finished!")
                break

    def kanal_ekle(self, kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi += [kanal_ismi]

    def rastgele_kanal(self):
        if self.tv_durum == "On":
            print("Rastgele bir kanal seçiliyor...")
            time.sleep(2)
            self.kanal = random.choice(self.kanal_listesi)
            print("{} açıldı".format(self.kanal))
        else:
            print("Televizyon kapalı!")

    def kanal_sil(self):

        for i in range(0, len(self.kanal_listesi)):
            print("Kanal {}:".format(i+1), self.kanal_listesi[i])
        silinecek_kanal = int(input("Silinecek kanalın sırasını giriniz:"))
        print("Kanal siliniyor...")
        time.sleep(2)
        self.kanal_listesi.pop(silinecek_kanal-1)
        print("Kanallar: ", self.kanal_listesi)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "TV Durumu: {}\nVolume: {}\nKanal Listesi: {}\nEn Son Açık Kanal: {} ".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)


print("""
Televizyon Uygulaması

1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sil
6. Kanal Sayısını Öğrenme
7. Rastgele Kanala Geçme
8. Televizyon Bilgileri

Çıkmak için "q"ya basın.
""")

kumanda = Kumanda()

while True:

    islem = input("İşlemi Seçiniz:")
    if islem == "q":
        break
    elif islem == "1":
        kumanda.tv_ac()
    elif islem == "2":
        kumanda.tv_kapat()
    elif islem == "3":
        kumanda.ses_ayarla()
    elif islem == "4":
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin: ")
        kanal_listesi = kanal_isimleri.split(",")
        for m in kanal_listesi:
            kumanda.kanal_ekle(m)
    elif islem == "5":
        kumanda.kanal_sil()
    elif islem == "6":
        print("Kanal Sayısı: ", len(kumanda))
    elif islem == "7":
        kumanda.rastgele_kanal()
    elif islem == "8":
        print(kumanda)
    else:
        print("Geçersiz işlem!")
