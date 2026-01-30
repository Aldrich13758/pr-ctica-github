<<<<<<< HEAD
'''70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
formato de entrada y salida tal y como se muestra en el testeo.'''

milista=[]
longitud=int(input("introduce la longitud de la lista: "))

for x in range (0,longitud):
    palabra=(input("introduce un valor:"))
    milista.append(palabra)

milista.sort()
print(milista)
milista2=milista.copy()
milista2.reverse()
=======
'''70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
formato de entrada y salida tal y como se muestra en el testeo.'''

milista=[]
longitud=int(input("introduce la longitud de la lista: "))

for x in range (0,longitud):
    palabra=(input("introduce un valor:"))
    milista.append(palabra)

milista.sort()
print(milista)
milista2=milista.copy()
milista2.reverse()
>>>>>>> 10afee69f9ffa62036085da55989bc2d90d8f0e8
print(milista2)