#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
var1=float(input("introduce tu nota:"))
if var1>8.5 and var1<=10:
    print("has sacado un excelente")
elif var1<=8.5 and var1>=6.5:
    print("has sacado un notable")
elif var1<6.5 and var1>=5:
    print("has sacado un suficiente")
elif var1<5:
    print("has suspendido")