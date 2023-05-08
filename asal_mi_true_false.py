

def asal_mi(s):
    if s > 1:
        if s == 1 or s == 0:
            return False
        elif s == 2:
            return True
        else:
            for i in range(2, s):
                if s % i == 0:
                    return False
            return True
    else:
        return False


while True:
    s = input("Sayı: ")
    if s == "q":
        break
    else:
        s = int(s)
        if asal_mi(s):
            print(s, "Asal bir sayıdır!")
        else:
            print(s, "Asal bir sayı değildir!")
