#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
var1=(input("introduzca un primer valor:"))
var2=(input("introduzca un segundo valor:"))
if var1==var2:
    print(f"ambos valores son iguales")
elif var1>var2:
    print(f"el primer valor es mas grande")
else:
    print(f"el segundo valor es mas grande")