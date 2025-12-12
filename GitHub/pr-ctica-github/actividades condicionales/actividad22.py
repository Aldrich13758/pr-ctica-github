#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
var1=int(input("introduce la nota del examen:"))
if var1==5 or var1>5:
    print("has aprovado")
else:
    print("has suspendido")