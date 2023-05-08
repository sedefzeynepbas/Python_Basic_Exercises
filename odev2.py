

def cift_mi(x):
    if x % 2 == 0:
        return x
    else:
        raise ValueError("whyyyy????????")


liste = [2, 3, 4, 5, 6, 7, 8, 9, 22, 101, 102]

for i in liste:
    try:
        print(cift_mi(i))
    except:
        pass

