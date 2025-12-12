#36 Programa que sume los n primeros números naturales. n Lo introduce el usuario.
número=int(input("Introduce un número: ")) 
suma = 0 
for i in range(1, número + 1): 
    suma += i 
print("La suma total de números naturales es:", suma)