<<<<<<< HEAD
'''72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
no deben almacenarse en la lista'''

=======
'''72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
no deben almacenarse en la lista'''
import unicodedata

lista = []
vocales = "aeiou"

while True:
    letra = input("Introduce una letra: ").lower()
    letra = unicodedata.normalize("NFD", letra)[0]

    if letra in vocales and letra not in lista:
        lista.append(letra)

    if input("¿Deseas repetir s/n: ").lower() == "n":
        break

print(lista)
>>>>>>> 10afee69f9ffa62036085da55989bc2d90d8f0e8
