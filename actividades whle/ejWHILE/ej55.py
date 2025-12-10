#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
total = 0
cont = 0

while total > 50 or total % 2 == 0:
    a = int(input())
    b = int(input())
    suma = a + b
    total += suma
    cont += 1

    print("El resultado de la suma es:", suma)
    print("El total acumulado es:", total, "y llevas", cont, "operación realizada")

print("Fin del programa")