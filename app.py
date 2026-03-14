def calcular_prioridad(dias):
    if dias < 0:
        return "Error: Días abierto no puede ser negativo"
    if dias >= 7:
        return "alta"
    return "normal"
