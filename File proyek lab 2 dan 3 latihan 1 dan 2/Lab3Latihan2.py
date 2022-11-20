from random import random
n = int(input("Masukkan nilai n: "))
for i in range(n):
    while True:
        n = random()
        if (n < 0.5):
            break
    print(n)
print()