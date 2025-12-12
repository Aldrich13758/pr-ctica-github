import math
var1=float(input("introduce la altura de un cilindro "))
var2=float(input("introduce el radio de un cilindro "))
total1=((2*math.pi*(var2**2))+2*math.pi*var2*var1)
total1=round(total1, 2)
print(f"el area del circulo es {total1}")
total2=math.pi*(var2**2)*var1
total2=round(total2, 2)
print(f"el volumen del circulo es {total2}")