#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10
número=int(input("¿Cuántas notas quieres introducir? ")) 
for i in range(número): 
    nota=float(input("Introduce la nota: ")) 
    if 0<=nota<=10: 
        if nota>= 5: 
            print("Asignatura aprobada") 
        else:
            print("Asignatura suspendida") 
else:
        print("Has introducido una nota equivocada")