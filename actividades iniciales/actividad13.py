import math
var1=int(input("introduce el valor del diámetro de un círculo:"))
var2=var1/2
total1=math.pi*var2**2
total1= round(total1, 1)
total2=2*math.pi*var2
total2=round(total2, 1)
print(f"el valor del área es: {total1} y el valor del perímetro es: {total2}")