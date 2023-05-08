"""

Fibonacci serisinde bir sayı kendinden önceki iki sayının toplamına eşittir
1,1,2,3,5,8,13,22,34......

"""
"""a ile bnin toplamını eklemem gerekiyor sürekli ama a ile b'yi de hep kaydırmam gerekiyor"""
a = 1
b = 1
fib = [a, b]
for i in range(10):
    a, b = b, a+b
    print("a:", a, "b:", b)
    fib += [b]
print(fib)
""" fib += [b] - ya da fib.append(b)"""