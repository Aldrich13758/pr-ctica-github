#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
#está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
var1=input("Introduce una letra: ")
letra=False
if var1.isupper():
    letra=True
if not var1.isupper():
    letra=False
print(f"La letra es mayuscula {letra}")
