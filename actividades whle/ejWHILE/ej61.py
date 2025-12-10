#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
#superior o igual a 40.
n = int(input())
i = 1

while True:
    r = n * i
    print(r)
    if r >= 40:
        print("Fin de programa")
        break
    i += 1