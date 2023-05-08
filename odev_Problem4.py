"""Problem 4"""
print("Geometrik şeklin tipi belirlenecektir.\nGeometrik şekiller:\n1- Üçgen\n2- Dörtgen")


x = float(input("Tipini belirlemek istediğiniz geometrik şeklin numarasını giriniz: "))
if x == 2:
    k1 = float(input("1. Kenar Uzunluğu(m): "))
    k2 = float(input("2. Kenar Uzunluğu(m): "))
    k3 = float(input("3. Kenar Uzunluğu(m): "))
    k4 = float(input("4. Kenar Uzunluğu(m): "))
    if k1 == k2 == k3 == k4:
        print("Geometrik şekliniz bir karedir!")
    elif (k1 == k2 and k3 == k4) or (k1 == k3 and k2 == k4) or (k1 == k4 and k2 == k3):
        print("Geometrik şekliniz bir dikdörtgendir!")
    else:
        print("Geometrik şekliniz sıradan bir dörtgendir!")
elif x == 1:
    u1 = float(input("1. Kenar Uzunluğu(m): "))
    u2 = float(input("2. Kenar Uzunluğu(m): "))
    u3 = float(input("3. Kenar Uzunluğu(m): "))
    if u1 <= 0 or u2 <= 0 or u3 <= 0:
        print("Negatif kenar uzunluğu girdiniz, üçgen belirtmiyor!")
    elif not (u1 + u2 > u3 and u1 + u3 > u2 and u2 + u3 > u1):
        print("Üçgen belirtmiyor!")
    elif (u1 == u2 and u3 != u1) or (u1 == u3 and u2 != u1) or (u2 == u3 and u1 != u3):
        print("Geometrik şekliniz bir ikizkenar üçgendir!")
    elif u1 == u2 == u3:
        print("Geometrik şekliniz bir eşkenar üçgendir!")
    else:
        print("Geometrik şekliniz sıradan bir üçgendir!")
else:
    print("Hatalı geometrik şekil numarası!")
