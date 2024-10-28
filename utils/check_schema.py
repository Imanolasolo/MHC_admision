import sqlite3

def check_user_table_schema():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()

    # Obtener información sobre la tabla users
    c.execute("PRAGMA table_info(users)")
    table_info = c.fetchall()
    print("Esquema de la tabla 'users':")
    for column in table_info:
        print(column)

    conn.close()

if __name__ == "__main__":
    check_user_table_schema()
