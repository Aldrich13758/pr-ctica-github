'''69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
ordenados de menor a mayor.'''
milista=[]
longitud=int(input("introduce la longitud de la lista: "))


for x in range (0,longitud):
    numero=int(input("introduce un valor:"))
    milista.append(numero)

milista.sort()

print(milista)