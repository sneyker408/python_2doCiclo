# Solicitar al usuario ingresar su edad
edad = int(input("Ingresa tu edad: "))

# Verificar si el usuario es menor de edad utilizando el operador "NOT"
if not edad >= 18:
    print("Debes ser mayor de edad para acceder a esta funcionalidad.")
else:
    print("Acceso permitido.")
