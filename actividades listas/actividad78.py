<<<<<<< HEAD
'''78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir'''
lista=['a','b','D','x','r','X','3','h','w','2','i']

while True:
    valor=input("Introduce el valor que deseas eliminar: ")

    if valor.isdigit():
        if valor in lista:
            lista.remove(valor)
            print(lista)
        else:
            print("El valor introducido no está en la lista")
    else:
        print("Introduce valor numérico")

    if input("Deseas introducir otro valor s/n: ").lower()=="n":
        break 
=======
'''78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir'''
lista=['a','b','D','x','r','X','3','h','w','2','i']

while True:
    valor=input("Introduce el valor que deseas eliminar: ")

    if valor.isdigit():
        if valor in lista:
            lista.remove(valor)
            print(lista)
        else:
            print("El valor introducido no está en la lista")
    else:
        print("Introduce valor numérico")

    if input("Deseas introducir otro valor s/n: ").lower()=="n":
        print("Fin del programa")
        break 
>>>>>>> 10afee69f9ffa62036085da55989bc2d90d8f0e8
