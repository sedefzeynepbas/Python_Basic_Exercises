"""

"""

def tam_bolenler(a):
    liste_tb = []
    for i in range(1, a + 1):
        if a % i == 0:
            liste_tb.append(i)
    return liste_tb


while True:
    b = input("Tam bölenleri bulunacak sayıyı giriniz:")
    if b == "q":
        print("Program sonlandırıldı...")
        break
    else:
        b = int(b)
        print("{} nın tam bölenleri: ".format(b), tam_bolenler(b))


