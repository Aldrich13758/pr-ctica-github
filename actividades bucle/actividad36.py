#36 Programa que sume los n primeros números naturales. n Lo introduce el usuario.
# Python

# Función para sumar los n primeros números naturales con un bucle
def suma_numeros_bucle(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

# Función para sumar los n primeros números naturales usando la fórmula
def suma_numeros_formula(n):
    return n * (n + 1) // 2  # División entera para obtener un número entero

# Programa principal
def main():
    try:
        n = int(input("Introduce un número entero positivo n: "))
        if n < 0:
            print("Por favor, introduce un número positivo.")
            return
        suma_bucle = suma_numeros_bucle(n)
        suma_formula = suma_numeros_formula(n)
        print(f"La suma de los {n} primeros números naturales usando bucle es: {suma_bucle}")
        print(f"La suma de los {n} primeros números naturales usando fórmula es: {suma_formula}")
    except ValueError:
        print("Entrada inválida. Debes introducir un número entero.")

# Llamada al programa principal
if __name__ == "__main__":
    main()