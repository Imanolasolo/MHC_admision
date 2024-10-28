import sqlite3

def init_db():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()

    # Crear tabla de usuarios
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            dni TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            UNIQUE(username)
        )
    ''')

    # Guardar cambios y cerrar conexión
    conn.commit()
    conn.close()
