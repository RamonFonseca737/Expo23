numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  
  
pares = [num for num in numeros if num % 2 == 0]  
impares = [num for num in numeros if num % 2 != 0]  
  
print("Los números pares son:", pares)  
print("Los números impares son:", impares)  