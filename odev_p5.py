"""
1-100 aralığında 3'e bölünen sayılar ekrana yazdırılacak.
"""
b = 0

for i in range(1,101):
    if i % 3 == 0:
        print(i)
    else:
        continue
