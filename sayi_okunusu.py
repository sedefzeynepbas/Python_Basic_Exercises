"""
birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10

    return onlar[ikinci] + " " + birler[birinci]


sayı =  int(input("Sayı:"))

print(okunus(sayı))
"""



birler = ["bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def sayi_okunusu(x):
    a = x[0]
    b = x[1]
    a = int(a)
    b = int(b)
    n = 0
    bb = 0
    ob = 0
    k = 0
    for i in birler:
        if n < 9:
            n += 1
            c = birler[n-1]
            if b == n:
                bb = c
    for m in birler:
        if k < 9:
            k += 1
            p = onlar[k-1]
            if a == k:
                ob = p
    return ob +" "+ bb


sayi = input("Sayı: ")
print(sayi_okunusu(sayi))
