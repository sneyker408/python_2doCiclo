# Solicitar al usuario ingresar las longitudes de los lados del triángulo
lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

# Determinar la clasificación del triángulo según sus lados
if lado1 == lado2 == lado3:
    clasificacion = "Equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    clasificacion = "Isósceles"
else:
    clasificacion = "Escaleno"

# Mostrar la clasificación del triángulo
print(f"El triángulo es de tipo '{clasificacion}'.")
