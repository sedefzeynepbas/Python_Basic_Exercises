"""
Print Prime Number in a range
"""

liste = []
for n in range(1, 101):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n)
            liste.append(n)
print(liste)