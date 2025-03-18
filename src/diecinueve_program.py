num = int(input("Ingrese un número: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} no es un número primo.")
            break
    else:
        print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")
