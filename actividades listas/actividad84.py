'''84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra.'''
import random

lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
print(random.choice(lista))