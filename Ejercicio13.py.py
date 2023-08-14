# Solicitar al usuario ingresar su edad y si está acompañado de un adulto
edad = int(input("Ingresa tu edad: "))
acompañado = input("¿Estás acompañado de un adulto? (Sí/No): ").lower()

# Verificar la edad y si está acompañado utilizando el operador "OR"
if edad >= 18 or acompañado == "sí":
    print("¡Bienvenido! Puedes ingresar a la película.")
else:
    print("Acceso restringido. Debes ser mayor de 18 años o estar acompañado por un adulto.")
