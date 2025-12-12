#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
var1=float(input("introduce tu nota:"))
if var1>8.5 and var1<=10:
    print("has sacado un excelente")
elif var1<=8.5 and var1>=6.5:
    print("has sacado un notable")
elif var1<6.5 and var1>=5:
    print("has sacado un suficiente")
elif var1<5:
    print("has suspendido")