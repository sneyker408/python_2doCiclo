# Solicitar al usuario ingresar su nombre de usuario y contraseña
nombre_usuario = input("Ingresa tu nombre de usuario: ")
contraseña = input("Ingresa tu contraseña: ")

# Verificar el nombre de usuario y contraseña utilizando el operador "AND"
if nombre_usuario == "admin" and contraseña == "12345":
    print("Bienvenido al sistema.")
else:
    print("Acceso denegado. Nombre de usuario o contraseña incorrectos.")
