#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
a = int(input())
b = int(input())

if a > b:
    a, b = b, a

pares = []
impares = []

for x in range(a, b):
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print("Los números pares son", pares)
print("Los números impares son", impares)