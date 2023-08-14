# Solicitar al usuario ingresar dos números enteros diferentes
numero1 = int(input("Ingresa el primer número entero: "))
numero2 = int(input("Ingresa el segundo número entero: "))

# Comparar los números y mostrar el resultado
if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}.")
elif numero2 > numero1:
    print(f"{numero2} es mayor que {numero1}.")
else:
    print("Los números son iguales.")
