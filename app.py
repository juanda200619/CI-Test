def calcular_prioridad(dias):
    if dias < 0:
        return "Error: Días abierto no puede ser negativo"
    if dias > 5:
        return "alta"
    return "normal"
