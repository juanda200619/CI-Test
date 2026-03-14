from app import calcular_prioridad


def test_calcular_prioridad_normal():
    assert calcular_prioridad(3) == "normal"


def test_calcular_prioridad_alta():
    assert calcular_prioridad(7) == "alta"


def test_dias_negativos():
    expected = "Error: Días abierto no puede ser negativo"
    assert calcular_prioridad(-1) == expected
