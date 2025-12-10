#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While
repetir = "s"

while repetir == "s":
    a = int(input())
    b = int(input())
    print("El resultado de la suma es:", a + b)
    repetir = input("Deseas repetir la operación s/n: ")
print("Programa finalizado")
