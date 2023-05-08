
with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\kedilervetakımlar.txt", "r", encoding="utf-8") as file:
    ödül = []
    yaş_mama = []
    kuru_mama = []
    for i in file:
        if "Ödül Mama" in i:
            ödül.append(i)
        elif "Yaş Mama" in i:
            yaş_mama.append(i)
        elif "Kuru Mama" in i:
            kuru_mama.append(i)
    with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\ödül_takımı.txt", "w",encoding="utf-8") as file1:
        for j in ödül:
            file1.write(j)

    with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\yaş_mama_takımı.txt", "w",encoding="utf-8") as file2:
        for k in yaş_mama:
            file2.write(k)

    with open("C:\\Users\\BSS5BU\\Desktop\\pycharm_files\\egzersiz_dosyalar\\kuru_mama_takımı.txt", "w",encoding="utf-8") as file3:
        for l in kuru_mama:
            file3.write(l)

