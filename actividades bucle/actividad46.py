#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
palabra = input("Introduce una palabra: ").lower() 
vocales = "" 
consonantes = "" 
for letra in palabra: 
    if letra in "aeiouáéíóú": 
        vocales += letra 
    else: 
        consonantes += letra 
print("Las vocales son:", vocales) 
print("Las consonantes son:", consonantes)