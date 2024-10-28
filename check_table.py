import sqlite3

def describe_table(table_name):
    try:
        conn = sqlite3.connect('hospital.db')  # Cambia el nombre de la base de datos si es necesario
        c = conn.cursor()
        
        # Ejecuta la consulta PRAGMA para obtener información sobre la tabla
        c.execute(f"PRAGMA table_info({table_name});")
        
        # Obtén los resultados
        columns = c.fetchall()
        
        if not columns:
            print(f"No se encontró la tabla '{table_name}'.")
        else:
            # Muestra la estructura de la tabla
            for column in columns:
                print(f"Nombre de Columna: {column[1]}")
                print(f"Tipo de Datos: {column[2]}")
                print(f"No Nulo: {column[3]}")
                print(f"Valor Predeterminado: {column[4]}")
                print(f"Clave Primaria: {column[5]}")
                print()
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Error de SQLite: {e}")

# Llama a la función para la tabla deseada
describe_table('pacientes')  # Cambia el nombre de la tabla si es necesario

