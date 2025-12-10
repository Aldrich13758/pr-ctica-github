#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.
import random
n = random.randint(0, 1000)
intentos = 0
acertado = False

while not acertado:
    x = int(input("Introduce un valor entre 1 y 1000: "))
    intentos += 1

    if x < n:
        print("El número introducido es menor")
    elif x > n:
        print("El número introducido es mayor")
    else:
        print("Acertaste, has realizado", intentos, "intentos")
        acertado = True