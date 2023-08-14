# Solicitar al usuario ingresar dos números enteros como límites
limite_inferior = int(input("Ingresa el límite inferior: "))
limite_superior = int(input("Ingresa el límite superior: "))

# Asegurarse de que el límite superior sea mayor o igual al límite inferior
while limite_superior < limite_inferior:
    print("El límite superior debe ser mayor o igual al límite inferior.")
    limite_superior = int(input("Ingresa el límite superior: "))

# Utilizar un bucle "for" para imprimir los números pares dentro del rango
print(f"Números pares dentro del rango [{limite_inferior}, {limite_superior}]:")
for numero in range(limite_inferior, limite_superior + 1):
    if numero % 2 == 0:
        print(numero)
