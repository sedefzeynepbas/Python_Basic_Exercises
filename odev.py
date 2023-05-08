"""Problem 1"""
print("Beden kitle indeksiniz değerlendirilecektir")
kilo = float(input("Kilo (kg): "))
boy = float(input("Boy (m): "))
bki= kilo / boy**2
print("Beden kitle indeksiniz {}'dir".format(bki))
if bki < 18.5:
    print("Zayıf")
elif bki >= 18.5 and bki <= 25:
    print("Normal")
elif bki > 25 and bki <30:
    print("Fazla Kilolu")
else:
    print("Obez")

"""Problem 2"""
print("\n\nEn büyük sayı bulunacaktır.")
a = float(input("1.Sayı: "))
b = float(input("2.Sayı: "))
c = float(input("3.Sayı: "))
if a >= b and a >= c:
    print("En büyük sayı 1. sayıdır ve {}'dır.".format(a))
elif b >= a and b >= c:
    print("En büyük sayı 2. sayıdır ve {}'dır.".format(b))
else:
    print("En büyük sayı 3. sayıdır ve {}'dır.".format(c))

"""Problem 3"""
print("\n\nHarf Notunuz Hesaplanacaktır.")
vize1 = float(input("1. Vize Notu: "))
vize2 = float(input("2. Vize Notu: "))
final = float(input("Final Notu: "))
note = vize1*0.3 + vize2*0.3 + final*0.4
print("Notunuz {}'dir".format(note))
print("Harf Notunuz:")
if note >= 90:
    print("AA")
elif note>= 85:
    print("BA")
elif note>= 80:
    print("BB")
elif note>= 75:
    print("CB")
elif note>= 70:
    print("CC")
elif note>= 65:
    print("DC")
elif note>= 60:
    print("DD")
elif note>= 55:
    print("FD")
else:
    print("FF")

"""Problem 4"""
print("\n\nGeometrik şeklin tipi belirlenecektir.\nGeometrik şekiller:\n1- Üçgen\n2- Dörtgen")


x = float(input(("Tipini belirlemek istediğiniz geometrik şeklin numarasını giriniz: ")))
if x == 2:
    k1 = float(input("1. Kenar Uzunluğu(m): "))
    k2 = float(input("2. Kenar Uzunluğu(m): "))
    k3 = float(input("3. Kenar Uzunluğu(m): "))
    k4 = float(input("4. Kenar Uzunluğu(m): "))
    if k1 == k2 == k3 == k4:
        print("Geometrik şekliniz bir karedir!")
    elif (k1==k2 and k3==k4) or (k1==k3 and k2==k4) or (k1==k4 and k2==k3):
        print("Geometrik şekliniz bir dikdörtgendir!")
    else:
        print("Geometrik şekliniz sıradan bir dörtgendir!")
elif x == 1:
    u1 = float(input("1. Kenar Uzunluğu(m): "))
    u2 = float(input("2. Kenar Uzunluğu(m): "))
    u3 = float(input("3. Kenar Uzunluğu(m): "))
    if u1 <= 0 or u2 <=0 or u3<=0:
        print("Negatif kenar uzunluğu girdiniz, üçgen belirtmiyor!")
    elif not (u1+u2>u3 and u1+u3>u2 and u2+u3>u1):
        print("Üçgen belirtmiyor!")
    elif (u1 == u2 and u3 != u1 ) or (u1 == u3 and u2 != u1 ) or (u2 == u3 and u1 != u3):
        print("Geometrik şekliniz bir ikizkenar üçgendir!")
    elif u1 == u2 == u3:
        print("Geometrik şekliniz bir eşkenar üçgendir!")
    else:
        print("Geometrik şekliniz sıradan bir üçgendir!")
else:
    print("Hatalı geometrik şekil numarası!")