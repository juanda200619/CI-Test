import sqlite3
from app import calcular_prioridad


def test_db_connection_and_ticket_creation():
    # Configurar conexión a la base de datos con DB
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Crear tabla de tickets si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY,
            ubicacion TEXT NOT NULL,
            prioridad TEXT NOT NULL
        )
    ''')

    # Lógica de negocio + persistencia
    ubicacion = "Laboratorio de redes"
    prioridad = calcular_prioridad(10)  # Debería retornar "alta"

    cursor.execute(
        'INSERT INTO tickets (id, ubicacion, prioridad) VALUES (?, ?, ?)',
        (1, ubicacion, prioridad)
    )
    conn.commit()

    # Verificar (Assert)
    cursor.execute('SELECT prioridad FROM tickets WHERE id = 1')
    resultado = cursor.fetchone()

    assert resultado[0] == "alta"

    # Cerrar conexión
    conn.close()
