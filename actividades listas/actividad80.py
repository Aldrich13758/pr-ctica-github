'''80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no'''
valor=input()
try:
    float(valor)
    if "." in valor:
        print("Es un número con decimales")
    else:
        print("No es un número con decimales")
except:
    print("No es un número con decimales")
