# Solicitar al usuario ingresar un número entero positivo
numero = int(input("Ingresa un número entero positivo: "))

# Validar si el número es positivo
if numero <= 0:
    print("Ingresa un número entero positivo.")
else:
    suma_digitos = 0
    while numero > 0:
        digito = numero % 10
        suma_digitos += digito
        numero //= 10

    print(f"La suma de los dígitos del número es: {suma_digitos}")
