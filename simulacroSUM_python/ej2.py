import math
frase=input("Introduce una frase: ").strip().lower()
print(f"Esta es la frase sin espacios al inicio ni en el final: {frase}")
num1=input("Introduce un número real: ")
num2=input("Introduce otro número real: ")
num3=input("Introduce el último número real: ")
total1=num1+num2+num3
round1= round(total1 ,2)
total2=(num1+num2+num3)/3
round2= round(total2 ,2)
total3=num1*num2*num3
print(f"La suma de los números es: {round1}")
print(f"La media de lso números es: {round2}")
if total1>total3:
    print("La suma es mayor que el producto")
else:
    print("El producto es mayor")