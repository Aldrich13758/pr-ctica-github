#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While
total = 0
cont = 0

while total <= 50:
    a = int(input())
    b = int(input())
    suma = a + b
    total += suma
    cont += 1

    print("El resultado de la suma es:", suma)
    print("El total acumulado es:", total, "y llevas", cont, "operación realizada")

print("Fin del programa")