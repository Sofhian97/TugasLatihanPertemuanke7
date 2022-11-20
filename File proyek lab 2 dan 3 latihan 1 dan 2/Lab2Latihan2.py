print("Program mengurutkan bilangan ")
a = (int (input("masukkan bilangan ke 1: ")))
b = (int (input("masukkan bilangan ke 2: ")))
c = (int (input("masukkan bilangan ke 3: ")))
if a < b and b < c:
    print("urutan bilangan adalah", a, b, c)
elif b < a and a < c:
    print("urutan bilangan adalah", b, a, c)
elif c < a and a < b:
    print("urutan bilangan adalah ", c, a, b)
