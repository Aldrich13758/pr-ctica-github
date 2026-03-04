import random
lista_palabras=["python", "programacion", "ahorcado", "juego", "palabra", "secreta", "adivinar", "letras"]
palabra_secreta=random.choice(lista_palabras).lower()
letras_adivinadas=[]
intentos=8
aciertos=0
errores=0  
print("¡Bienvenido al juego del Ahorcado!")
print("La palabra secreta tiene", len(palabra_secreta),"letras.")
print("Tienes", intentos, "intentos para adivinarla.")
while intentos>0:
    if intentos==8:
        print("________")
    if intentos==7:
        print("A_______")
    if intentos==6:
        print("AH______")
    if intentos==5:
        print("AHO_____")
    if intentos==4:
        print("AHOR____")
    if intentos==3:
        print("AHORC___")
    if intentos==2:
        print("AHORCA__")
    if intentos==1:
        print("AHORCAD_")
    letra=input("Introduce una letra: ").lower()
    if letra in letras_adivinadas:
        print("Ya has adivinado esa letra. Intenta con otra.")
        continue
    letras_adivinadas.append(letra)
    if letra in palabra_secreta:
        print("¡Correcto!")
        aciertos += 1
    elif letra not in palabra_secreta:
        intentos -= 1
        errores += 1
        print("¡Incorrecto! Te quedan", intentos, "intentos.")
    palabra_mostrada=""
    if intentos==0:
        print("¡Has perdido! La palabra secreta era:", palabra_secreta)
        print("AHORCADO")
        print(f"aciertos: {aciertos}, errores: {errores}")
    for letra_palabra in palabra_secreta:
        if letra_palabra in letras_adivinadas:
            palabra_mostrada+=letra_palabra + " "
        else:
            palabra_mostrada+="_ "
    print(palabra_mostrada.strip())
    if "_" not in palabra_mostrada:
        print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
        print("Aciertos:", aciertos, "Errores:", errores)
        jugar_otra = input("\n¿Quieres jugar otra partida? (s/n): ").lower() 
        if jugar_otra != "s": 
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            palabra_secreta=random.choice(lista_palabras).lower()
            letras_adivinadas=[]
            intentos=8
            aciertos=0
            errores=0