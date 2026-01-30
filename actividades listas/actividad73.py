<<<<<<< HEAD
'''73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
repiten y cuales no'''
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]

repetidas=list(set(lista1) & set(lista2))
norepetidas=[palabra for palabra in lista2 if palabra not in lista1]

print("Están repetidas:", repetidas)
print("No están repetidas:", norepetidas)
=======
'''73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
repiten y cuales no'''
lista1 = ["casa","mesa","sal","sol","agua"]
lista2 = ["casa","luz","tres","tren","sol","pan"]

repetidas = list(set(lista1) & set(lista2))
norepetidas = [palabra for palabra in lista2 if palabra not in lista1]

print("Están repetidas:", repetidas)
print("No están repetidas:", norepetidas)
>>>>>>> 10afee69f9ffa62036085da55989bc2d90d8f0e8
