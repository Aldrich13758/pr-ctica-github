numero=input("Introduce un número de 8 cifras: ") 
if not numero.isdigit(): 
    print("Error: el valor introducido no es numérico.")
elif len(numero)!=8:
#el signo de exclamación sirve para validar que la longitud del valor introducido es de 8 cifras
    print("Error: el número no tiene 8 cifras.") 
else: print("Número válido")

letras=["T","R","W","A","G","M","Y","F","P","D","X","B", "N","J","Z","S","Q","V","H","L","C","K","E"] 
letra=letras[int(numero) % 23] 
print(f"{numero}-{letra}")