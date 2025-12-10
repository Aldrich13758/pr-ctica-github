#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
n = random.randint(1, 5)

i = 0
while i < 3:
    x = int(input("Adivina (1-5): "))
    if x == n:
        print("Número acertado")
        break
    i += 1