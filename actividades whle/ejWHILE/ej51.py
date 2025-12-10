#51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el 
#número de veces que desea que repita la frase Buenos días. Con While
veces = int(input("¿Cuántas veces quieres repetir Buenos días?: "))
i = 0
while i < veces:
    print("Buenos días")
    i += 1
    