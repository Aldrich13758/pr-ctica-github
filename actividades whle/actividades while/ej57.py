#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
n = random.randint(1, 5)
x = int(input("Adivina (1-5): "))

if x == n:
    print("Número acertado")
else:
    print("Número no acertado")