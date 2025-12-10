#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.
total = 0
pedidos = 0

print("MENÚ")
print("1. Calamares 9€")
print("2. Chistorra 4.5€")
print("3. Bikini 2.5€")

print("ACOMPAÑAMIENTO")
print("1. Finas 1.5€")
print("2. Gruesas 1.75€")
print("3. Rústicas 2€")

print("BEBIDAS")
print("1. Coca cola 2€")
print("2. Aquarius 1.5€")
print("3. Agua 1€")

seguir = "s"

while seguir == "s":
    pedidos += 1

    b = int(input())
    if b == 1: total += 9
    if b == 2: total += 4.5
    if b == 3: total += 2.5

    a = int(input())
    if a == 1: total += 1.5
    if a == 2: total += 1.75
    if a == 3: total += 2

    d = int(input())
    if d == 1: total += 2
    if d == 2: total += 1.5
    if d == 3: total += 1

    seguir = input("¿Otro pedido s/n?: ")

# IVA
iva = total * 1.10

# DESCUENTOS
if 20 <= total <= 30:
    final = iva * 0.95
elif total > 30:
    final = iva * 0.85
else:
    final = iva

print("RESUMEN")
print("Número de pedidos:", pedidos)
print("Total a pagar:", total)
print("Total con IVA:", iva)
print("Precio total con descuento:", round(final, 2))