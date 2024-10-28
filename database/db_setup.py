import sys
import os
import sqlite3
import bcrypt

# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crud import generate_token  # Importar generate_token desde crud.py

def init_db():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    
    # Crear tabla de usuarios
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            dni TEXT NOT NULL,  -- Nueva columna para DNI
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    
    # Crear tabla de roles
    c.execute('''
        CREATE TABLE IF NOT EXISTS roles (
            id INTEGER PRIMARY KEY,
            role_name TEXT UNIQUE NOT NULL,
            permissions TEXT NOT NULL
        )
    ''')
    
    # Crear tabla de pacientes
    c.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            primer_apellido TEXT NOT NULL,
            segundo_apellido TEXT,
            primer_nombre TEXT NOT NULL,
            segundo_nombre TEXT,
            tipo_documento_identificacion TEXT NOT NULL CHECK(tipo_documento_identificacion IN ('cédula de ciudadanía', 'cédula de identidad', 'pasaporte', 'carnet de refugiado', 'S/D')),
            estado_civil TEXT NOT NULL,
            sexo TEXT NOT NULL,
            telefono_fijo TEXT,
            telefono_celular TEXT,
            correo_electronico TEXT,
            lugar_nacimiento TEXT NOT NULL,
            nacionalidad TEXT NOT NULL,
            edad INTEGER NOT NULL,
            condicion_edad TEXT NOT NULL CHECK(condicion_edad IN ('H', 'D', 'M', 'A')),
            autocertificacion_etnica TEXT,
            nacionalidad_etnica TEXT,
            pueblos TEXT,
            nivel_educacion TEXT,
            estado_nivel_educacion TEXT,
            ocupacion TEXT,
            tipo_empresa_trabajo TEXT,
            seguro_salud_principal TEXT,
            tipo_bono_recibe TEXT,
            provincia TEXT,
            canton TEXT,
            parroquia TEXT,
            barrio_sector TEXT,
            calle_principal TEXT,
            calle_secundaria TEXT,
            referencia TEXT,
            en_caso_necesario_llamar_a TEXT,
                parentesco TEXT,
                direccion TEXT,
                telefono_contacto TEXT,
                fecha_admision TEXT,
                fecha_egreso TEXT,
                numero_dis_estadia INTEGER,
                codigo_de_servicio_INEC TEXT,
                diagnosticos_o_sindromes_principal TEXT,
                CIE TEXT,
                definitivo TEXT,
                diagnosticos_o_sindromes_secundario TEXT,
                CIE_secundario TEXT,
                definitivo_secundario TEXT,
                alta TEXT,
                muerte_menos_de_48_horas TEXT,
                muerte_mas_de_48_horas TEXT,
                clinico TEXT,
                quirurgico TEXT,
                procedimientos_clinicos_o_quirurgicos_principales TEXT,
                sello_y_firma_del_responsable TEXT
        )
    ''')

    # Crear tabla de acompañantes
    c.execute('''
        CREATE TABLE IF NOT EXISTS acompanantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            en_caso_necesario_llamar_a TEXT,
            parentesco TEXT NOT NULL,
            direccion TEXT,
            telefono_acompanante TEXT,
            nombre_apellido_representante TEXT,
            identificacion_representante TEXT,
            telefono_representante TEXT
        )
    ''')

    # Crear usuario administrador por defecto
    admin_username = 'admin'
    admin_password = 'Ilargietaeguzki1'  # Contraseña inicial
    admin_role = 'admin'

    # Comprobar si el usuario administrador ya existe
    c.execute('SELECT * FROM users WHERE username = ?', (admin_username,))
    if not c.fetchone():
        hashed_password = bcrypt.hashpw(admin_password.encode('utf-8'), bcrypt.gensalt())
        admin_id = generate_token(admin_username, admin_role)  # Usar el nombre de usuario para generar el token
        c.execute('INSERT INTO users (id, dni, username, password, role) VALUES (?, ?, ?, ?, ?)', 
                  (admin_id, 'admin_dni', admin_username, hashed_password.decode('utf-8'), admin_role))
        print("Usuario administrador creado con éxito.")
    else:
        print("Usuario administrador ya existe.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
