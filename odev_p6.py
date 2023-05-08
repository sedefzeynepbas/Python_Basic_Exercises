"""Problem 6
1den 100e kadar olan çift sayılar list comprehension:
liste = [x for x in range(1,101) if x % 2 == 0]
print(liste)
"""

liste = list(range(1,101))
liste_c = []


for m in liste:
    if m % 2 == 0:
        liste_c += [m]
print("1'den 100'e kadar olan çift sayılar: ", liste_c)

