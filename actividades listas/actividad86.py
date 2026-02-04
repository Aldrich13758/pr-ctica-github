numero=input("Introduce tu DNI: ") 
if not numero.isdigit():
#el .isdigit sirve para comprobar que el valor sea numerico 
    print("Error: el valor introducido no es numérico.")
elif len(numero)!=8:
#el signo de exclamación sirve para validar que la longitud del valor introducido es de 8 cifras
    print("Error: el número no tiene 8 cifras.") 
else: print("Número válido")
letras=["T","R","W","A","G","M","Y","F","P","D","X","B", "N","J","Z","S","Q","V","H","L","C","K","E"]
#esta lista contiene todas las letras que se pueden asignar segun el número introducido
letra=letras[int(numero) % 23]
#operador % en Python se utiliza principalmente como operador de módulo,
#que devuelve el residuo de la división entre dos números y así poder 
#asignar una letra al valor introducido
print(f"{numero}-{letra}")