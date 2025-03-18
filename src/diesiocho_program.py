n = int(input("Ingrese un número: "))
a, b = 0, 1
while a <= n:
    print(a, end=" ")
    a, b = b, a + b