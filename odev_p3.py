"""
Problem 3

1'den 10'a kadar olan sayılarla ekrana çarpım tablosu bastırılacak.

"""\

a = list(range(1, 11))
b = []
print(a)
for i in range(1, 11):
    for m in a:
        b = [i*m]
        print("{} * {} =".format(i,m), b)
