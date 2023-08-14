# Solicitar al usuario ingresar su salario anual y el número de años de empleo actual
salario_anual = float(input("Ingresa tu salario anual: "))
años_empleo = int(input("Ingresa el número de años de empleo actual: "))

# Verificar el salario y los años de empleo utilizando el operador "OR"
if salario_anual > 30000 or años_empleo >= 2:
    print("Préstamo aprobado.")
else:
    print("Préstamo no aprobado.")
    