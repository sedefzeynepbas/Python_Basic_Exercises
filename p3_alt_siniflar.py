import time


class Hayvanlar():

    def __init__(self, mama_stogu = 3):
        self.mama_stogu = mama_stogu

    def __str__(self):
        return "Mama stoğu: {} kg".format(self.mama_stogu)

    def parazit_asisi(self):
        print("Parazit aşısı için randevunuz oluşturulmuştur.")

    def goz_muayenesi(self):
        print("Göz muayenesi için randevunuz oluşturulmuştur.")

    def mama_alimi(self):
        d = float(input("Kaç kg mama siparişi vermek istiyorsunuz: "))
        self.mama_stogu += d


class Kopekler(Hayvanlar):

    def __init__(self, oyuncak_listesi = ["Top"], mama_stogu=3):
        super().__init__(mama_stogu=3)
        self.oyuncak_listesi = oyuncak_listesi

    def oyuncaklar(self, oyuncak):
        self.oyuncak_listesi.append(oyuncak)


class Kuslar(Hayvanlar):



    def __init__(self, kanat_uzunlugu=0, mama_stogu=3):
        super().__init__(mama_stogu=3)
        self.kanat_uzunlugu = kanat_uzunlugu

    def tuy_bakimi(self):
        if self.kanat_uzunlugu >= 2 and self.kanat_uzunlugu < 3:
            print("Tüy bakımı ücreti: 100 tl")
        elif self.kanat_uzunlugu >= 1 and self.kanat_uzunlugu < 2:
            print("Tüy bakımı ücreti 70 tl")
        elif self.kanat_uzunlugu >= 0.5 and self.kanat_uzunlugu < 1:
            print("Tüy bakımı ücreti: 50 tl")
        elif self.kanat_uzunlugu >= 0.1 and self.kanat_uzunlugu < 0.5:
            print("Tüy bakımı ücreti: 20 tl")
        else:
            print("Kanat boyu sebebiyle tüy bakımı işlemi yapılamayacaktır.")


class Atlar(Hayvanlar):



    def __init__(self, agirlik, mama_stogu=3):
        super().__init__(mama_stogu=3)
        self.agirlik = agirlik

    def yarisma(self):
        if self.agirlik <= 200 and self.agirlik>= 100:
            print("Yarışa katılabilir...")
        else:
            print("Yarışa katılamaz...")


animal1 = Hayvanlar()
animal2 = Hayvanlar()

dog1 = Kopekler()
dog2 = Kopekler()

kus1 = Kuslar(5)
kus2 = Kuslar(0.3)

at1 = Atlar(150)
at2 = Atlar(300)

animal1.goz_muayenesi()
print(animal2)

dog1.mama_alimi()
print(dog1)
dog1.parazit_asisi()

oyuncak_isimleri = input("Alınacak oyuncak isimlerini ',' ile ayırarak giriniz: ")
oyuncak_listesi = oyuncak_isimleri.split(",")
for m in oyuncak_listesi:
    print("Oyuncak alındı...")
    time.sleep(1)
    dog2.oyuncaklar(m)
print(dog2.oyuncak_listesi)

kus1.tuy_bakimi()
kus2.tuy_bakimi()
kus2.goz_muayenesi()

at1.yarisma()
at2.yarisma()
at1.parazit_asisi()

