# Solicitar al usuario ingresar su nombre de usuario y edad
nombre_usuario = input("Ingresa tu nombre de usuario: ")
edad = int(input("Ingresa tu edad: "))

# Utilizar el operador "AND" para evaluar las condiciones
if nombre_usuario != "" and edad >= 18:
    print("Usuario válido.")
else:
    print("Usuario no válido.")