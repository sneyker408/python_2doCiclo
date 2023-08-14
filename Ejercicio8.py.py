# Inicializar la suma total
suma_total = 0

# Ciclo while para solicitar números enteros positivos y sumarlos
while True:
    numero = int(input("Ingresa un número entero positivo (ingresa un número negativo para detener): "))
    if numero >= 0:
        suma_total += numero
    else:
        break  # Salir del ciclo si se ingresa un número negativo

# Mostrar la suma total
print(f"La suma total de los números ingresados es: {suma_total}")
