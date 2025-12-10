#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos
pares = impares = pos = neg = ceros = suma = 0

n = int(input("Introduce un número: "))
while n != -99:

    if n == 0:
        ceros += 1
    elif n > 0:
        pos += 1
    else:
        neg += 1

    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

    suma += n
    n = int(input("Introduce un número: "))

print("El número de pares es", pares)
print("El número de impares es", impares)
print("El número de positivos es", pos)
print("El número de negativos es", neg)
print("El total es", suma)