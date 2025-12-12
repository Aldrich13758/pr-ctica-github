#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.
palabrasecreta=input("Introduce la palabra secreta: ")
letra=input("Introduce una letra: ")
for i in range(len(palabrasecreta)):
    if palabrasecreta[i]==letra:
        print("La letra se encuentra en la posición", i+1)

 
 