"""

EKOK = x * y / EBOB

"""

def ebek(x, y):
    eb = 1
    for i in range(1, y+1):
        if x % i == 0 and y % i == 0:
            eb = i
            ek = x * y / eb
    return eb, ek


s1 = int(input("Sayı 1:"))
s2 = int(input("Sayı 2:"))
print("EBOB, EKOK: ", ebek(s1, s2))



