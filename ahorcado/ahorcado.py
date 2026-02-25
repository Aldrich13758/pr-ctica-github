import random
import time
lista_palabras = ["python", "programacion", "ahorcado", "juego", "palabra", "secreta", "adivinar", "letras"]
palabra_secreta = random.choice(lista_palabras).lower()
letras_adivinadas = []
intentos=8                        
print("¡Bienvenido al juego del Ahorcado!")
print("La palabra secreta tiene", len(palabra_secreta)
        , "letras. Tienes", intentos, "intentos para adivinarla.")
while intentos > 0:
    letra = input("Introduce una letra: ").lower()
    if letra in letras_adivinadas:
        print("Ya has adivinado esa letra. Intenta con otra.")
        continue
    letras_adivinadas.append(letra)
    if letra in palabra_secreta:
        print("¡Correcto!")
    else:
        intentos -= 1
        print("¡Incorrecto! Te quedan", intentos, "intentos.")
    palabra_mostrada = ""
    for letra_palabra in palabra_secreta:
        if letra_palabra in letras_adivinadas:
            palabra_mostrada += letra_palabra + " "
        else:
            palabra_mostrada += "_ "
    print(palabra_mostrada.strip())
    if "_" not in palabra_mostrada:
        print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
        break