# Solicitar al usuario ingresar un número entero
numero = int(input("Ingresa un número entero: "))

# Utilizar un bucle "for" para imprimir la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
