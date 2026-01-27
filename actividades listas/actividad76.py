'''76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras 
y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás 
en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.'''
lista=['a','b','D','x','r','X','3','h','w','2','i']

letras=sorted([x for x in lista if x.isalpha()], key=str.lower)
numeros=sorted([int(x) for x in lista if x.isdigit()])

op=int(input("Elige el orden de los valores, 1=ascendente o 2=descendente: "))

if op==2:
    letras.reverse()
    numeros.reverse()

print(numeros)
print(letras)
