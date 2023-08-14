# Solicitar al usuario ingresar su edad
edad = int(input("Ingresa tu edad: "))

# Clasificar la edad en categorías
if edad >= 0 and edad <= 12:
    categoria = "Niño"
elif edad >= 13 and edad <= 19:
    categoria = "Adolescente"
elif edad >= 20 and edad <= 39:
    categoria = "Adulto Joven"
elif edad >= 40 and edad <= 59:
    categoria = "Adulto"
else:
    categoria = "Adulto Mayor"

# Mostrar la categoría correspondiente
print(f"Tu edad de {edad} años corresponde a la categoría '{categoria}'.")
