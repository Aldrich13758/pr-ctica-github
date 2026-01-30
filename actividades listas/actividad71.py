<<<<<<< HEAD
'''71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
esta lista no deben almacenarse las letras que se han introducido repetidas.'''
lista=[]

while True:
    letra=input("Introduce una letra: ")

    if letra.isalpha() and letra not in lista:
        lista.append(letra)

    if input("¿Deseas repetir s/n: ").lower()=="n":
        break

print(lista)
=======
'''71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
esta lista no deben almacenarse las letras que se han introducido repetidas.'''
lista = []

while True:
    letra = input("Introduce una letra: ")

    if letra.isalpha() and letra not in lista:
        lista.append(letra)

    if input("¿Deseas repetir s/n: ").lower() == "n":
        break

print(lista)
>>>>>>> 10afee69f9ffa62036085da55989bc2d90d8f0e8
