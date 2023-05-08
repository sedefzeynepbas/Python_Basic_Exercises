
class Dosya():
    def __init__(self):
        with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\metin_inceleme.txt", "r", encoding="utf-8") as file:
            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split(" ")
            self.sade_kelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(".")
                i = i.strip(":")
                i = i.strip(",")
                i = i.strip(" ")
                self.sade_kelimeler.append(i)
    def tüm_kelimeler(self):
        kelimeler_kümesi = set()
        for i in self.sade_kelimeler:
            kelimeler_kümesi.add(i)
        print("Tüm kelimeler......")
        for i in kelimeler_kümesi:
            print(i) #Tekrar edenlerden sadece bir tanesini atar kümeye
            print("******************")
    def kelime_frekansi(self):
        kelime_sözlük = dict()
        for i in self.sade_kelimeler:
            if i in kelime_sözlük:
                kelime_sözlük[i] +=1
            else:
                kelime_sözlük[i] = 1
        for kelime,sayı in kelime_sözlük.items():
            print("{} kelimesi {} defa geçiyor".format(kelime, sayı))
            print("--------------------------------")

    def kelime_aratma(self, kelime):

        if kelime in self.sade_kelimeler:
            s = self.sade_kelimeler.count(kelime)
            print("{} kelimesi {} defa geçiyor".format(kelime, s))
        else:
            print("{} diye bir kelime metin içinde bulunmamaktadır...".format(kelime))



dosya = Dosya()

dosya.kelime_aratma("greas")
dosya.kelime_frekansi()
