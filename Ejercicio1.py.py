# Solicitar al usuario ingresar una calificación numérica
calificacion = int(input("Ingresa una calificación numérica del 0 al 100: "))

# Determinar la clasificación de la calificación
if calificacion >= 90 and calificacion <= 100:
    clasificacion = "A"
elif calificacion >= 80 and calificacion < 90:
    clasificacion = "B"
elif calificacion >= 70 and calificacion < 80:
    clasificacion = "C"
elif calificacion >= 60 and calificacion < 70:
    clasificacion = "D"
else:
    clasificacion = "F"

# Mostrar la clasificación correspondiente
print(f"La calificación {calificacion} corresponde a la clasificación '{clasificacion}'.")
