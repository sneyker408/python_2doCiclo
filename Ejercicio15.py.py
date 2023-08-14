def verificar_sesion(inicio_sesion):
    if not inicio_sesion:
        print("Debes iniciar sesión para acceder a la función.")
    else:
        print("Acceso permitido.")
        
# Ejemplo de uso:
ha_iniciado_sesion = False
verificar_sesion(ha_iniciado_sesion)