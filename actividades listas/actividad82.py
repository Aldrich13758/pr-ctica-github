<<<<<<< HEAD
'''82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
la palabra'''
import random

lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
secreta=random.choice(lista)

intentos=0
while True:
    intentos+=1
    palabra=input("Introduce la palabra secreta: ")
    if palabra==secreta:
        print("ACERTASTE")
        break
    else:
        print("SIGUE JUGANDO")
=======
'''82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
la palabra'''
>>>>>>> 10afee69f9ffa62036085da55989bc2d90d8f0e8
