


"""
***********************
- HARF NOTU HESAPLAMA -
***********************

"""

def not_hesapla(satır):

    satır = satır[:-1]
    liste = satır.split(",")
    numara = liste[0]
    isim = liste[1]
    not1 = int(liste[2])
    not2 = int(liste[3])
    not3 = int(liste[4])
    son_not = not1*0.2 + not2*0.2 + not3*0.6
    if son_not >= 90:
        harf = "AA"
    elif son_not >= 85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    elif son_not >= 55:
        harf = "FD"
    else:
        harf = "FF"

    return numara + " " + isim + "----->" + harf + "\n"

with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\üç_notlar.txt","r", encoding= "utf-8") as file:

    eklenecekler = []

    for i in file:

        eklenecekler.append(not_hesapla(i))

    with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\harf_notları.txt", "w", encoding= "utf-8") as file1:
        for i in eklenecekler:
            file1.write(i)

with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\harf_notları.txt", "r", encoding= "utf-8") as file1:

    geçenler = []
    kalanlar = []
    for m in file1:
        if "FF" in m or "FD" in m:
            kalanlar.append(m)
        else:
            geçenler.append(m)
    with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\kalanlar.txt", "w", encoding="utf-8") as file2:
        for z in kalanlar:
            file2.write(z)
    with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\geçenler.txt", "w", encoding="utf-8") as file3:
        for g in geçenler:
            file3.write(g)
