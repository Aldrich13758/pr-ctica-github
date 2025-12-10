#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While
repetir = "s"
total = 0
cont = 0

while repetir == "s":
    a = int(input())
    b = int(input())

    suma = a + b
    total += suma
    cont += 1

    print("El resultado de la suma es:", suma)
    repetir = input("Deseas repetir la operación s/n: ")

print("Resumen:")
print("La suma total es:", total, "y el número de repeticiones es:", cont)