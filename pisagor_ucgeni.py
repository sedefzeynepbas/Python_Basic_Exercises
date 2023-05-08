
def pisagor(sayi):
    liste = []
    for i in range(1, sayi+1):
        for j in range(1, sayi+1):
            c = (i**2+j**2)**0.5
            if c == int(c):
                liste.append([i, j, int(c)])
    return liste


aralik = int(input("a ve b için maksimum sayı: "))

for i in pisagor(aralik):
    print(i)
