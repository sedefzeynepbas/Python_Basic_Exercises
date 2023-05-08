

liste = ["345","sadas","324a","14","kemal"]
sayilar = []

for i in liste:
    try:
        b = int(i)
        sayilar.append(b)
    except ValueError:
        pass
print(sayilar)

