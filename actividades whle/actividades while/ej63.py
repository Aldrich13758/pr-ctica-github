#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número.
c1=c2=c3=c4=c5=c6 = 0

for i in range(100):
    n = random.randint(1, 6)
    if n == 1: c1 += 1
    if n == 2: c2 += 1
    if n == 3: c3 += 1
    if n == 4: c4 += 1
    if n == 5: c5 += 1
    if n == 6: c6 += 1

print("Uno:", c1)
print("Dos:", c2)
print("Tres:", c3)
print("Cuatro:", c4)
print("Cinco:", c5)
print("Seis:", c6)