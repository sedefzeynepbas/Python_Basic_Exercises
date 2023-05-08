"""
Problem 4

Girilen sayıların toplamı ekrana bastırılacak.
"""
s = 0
t = 0
while True:
    s = input("Eklemek istediğiniz sayıyı giriniz: ")
    if s == "q":
        break
    t += int(s)
print("Girilen sayıların toplamı {} dır.".format(t))
