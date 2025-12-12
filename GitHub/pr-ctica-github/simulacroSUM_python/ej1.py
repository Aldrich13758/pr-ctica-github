nombre=input("Introduce tu nombre: ")
edad=int(input("Introduce tu edad: "))
año_actual=2025
if edad>0 and edad<100:
    futuro=año_actual+(100-edad)
    print(f"Hola {nombre} cumplirás 100 años en el año {futuro}")
else:
    print("Edad no válida")