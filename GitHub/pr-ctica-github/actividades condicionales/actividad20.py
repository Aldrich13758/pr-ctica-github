#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
var1=int(input("introduce un primer valor entre 1-10:"))
var2=int(input("introduce un segundo valor entre 1-10:"))
if var1<0 or var1>10 or var2>10 or var2<0:
    print("alguno de los valores es mayor de 10 o menor de 0")
elif var1<var2:
    print("el segundo valor es mayor")
else:
    print("el primer valor es mayor")