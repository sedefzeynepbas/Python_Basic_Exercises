print("""
********************************
Faktöriyel Bulma Programı

Çıkmak için 'q' ya basınız.
********************************
""")

while True:
    faktoriyel = 1
    f = input("Faktöriyelini bulmak istediğiniz sayıyı giriniz: ")
    if f == "q":
        print("İyi günler! ")
        break
    else:
        for x in range(1, int(f) + 1):
            faktoriyel *= x
    print("{} in faktöriyeli {} dir.".format(int(f), faktoriyel))

