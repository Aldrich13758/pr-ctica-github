#35. Programa que al introducir un número por teclado permita mostrar ese número de veces tu nombre
nombre = input("Introduce tu nombre: ")
repeticiones=int(input("cuantas veces quieres que muestre tu nombre?: "))
for i in range(repeticiones):
    print(nombre)