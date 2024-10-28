import sqlite3

# Funciones CRUD para pacientes

def connect_db():
    """Crea y retorna una conexión a la base de datos SQLite."""
    return sqlite3.connect('hospital.db')

def create_patient(data):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        INSERT INTO pacientes (
            primer_apellido, segundo_apellido, primer_nombre, segundo_nombre, tipo_documento_identificacion,
            estado_civil, sexo, telefono_fijo, telefono_celular, correo_electronico, lugar_nacimiento,
            nacionalidad, edad, condicion_edad, autocertificacion_etnica, nacionalidad_etnica, pueblos,
            nivel_educacion, estado_nivel_educacion, ocupacion, tipo_empresa_trabajo, seguro_salud_principal,
            tipo_bono_recibe, provincia, canton, parroquia, barrio_sector, calle_principal, calle_secundaria,
            referencia
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('primer_apellido'), data.get('segundo_apellido', None), data.get('primer_nombre'),
        data.get('segundo_nombre', None), data.get('tipo_documento_identificacion'), data.get('estado_civil'),
        data.get('sexo'), data.get('telefono_fijo', None), data.get('telefono_celular', None),
        data.get('correo_electronico', None), data.get('lugar_nacimiento'), data.get('nacionalidad'),
        data.get('edad'), data.get('condicion_edad'), data.get('autocertificacion_etnica', None),
        data.get('nacionalidad_etnica', None), data.get('pueblos', None), data.get('nivel_educacion', None),
        data.get('estado_nivel_educacion', None), data.get('ocupacion', None),
        data.get('tipo_empresa_trabajo', None), data.get('seguro_salud_principal', None),
        data.get('tipo_bono_recibe', None), data.get('provincia', None), data.get('canton', None),
        data.get('parroquia', None), data.get('barrio_sector', None), data.get('calle_principal', None),
        data.get('calle_secundaria', None), data.get('referencia', None)
    ))
    conn.commit()
    conn.close()


def read_patients():
    """Lee todos los pacientes de la base de datos."""
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute('SELECT * FROM pacientes')
        patients = c.fetchall()
        return patients
    except sqlite3.Error as e:
        print(f"Error al leer pacientes: {e}")
        return []
    finally:
        conn.close()

def update_patient(patient_id, data):
    """Actualiza la información de un paciente en la base de datos."""
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute('''
            UPDATE pacientes
            SET primer_apellido = ?, segundo_apellido = ?, primer_nombre = ?, segundo_nombre = ?, tipo_documento_identificacion = ?,
                estado_civil = ?, sexo = ?, telefono_fijo = ?, telefono_celular = ?, correo_electronico = ?, lugar_nacimiento = ?,
                nacionalidad = ?, edad = ?, condicion_edad = ?, autocertificacion_etnica = ?, nacionalidad_etnica = ?, pueblos = ?,
                nivel_educacion = ?, estado_nivel_educacion = ?, ocupacion = ?, tipo_empresa_trabajo = ?, seguro_salud_principal = ?,
                tipo_bono_recibe = ?, provincia = ?, canton = ?, parroquia = ?, barrio_sector = ?, calle_principal = ?, calle_secundaria = ?,
                referencia = ?
            WHERE id = ?
        ''', (
            data['primer_apellido'], data.get('segundo_apellido', None), data['primer_nombre'],
            data.get('segundo_nombre', None), data['tipo_documento_identificacion'], data['estado_civil'],
            data['sexo'], data.get('telefono_fijo', None), data.get('telefono_celular', None),
            data.get('correo_electronico', None), data['lugar_nacimiento'], data['nacionalidad'],
            data['edad'], data['condicion_edad'], data.get('autocertificacion_etnica', None),
            data.get('nacionalidad_etnica', None), data.get('pueblos', None), data.get('nivel_educacion', None),
            data.get('estado_nivel_educacion', None), data.get('ocupacion', None),
            data.get('tipo_empresa_trabajo', None), data.get('seguro_salud_principal', None),
            data.get('tipo_bono_recibe', None), data.get('provincia', None), data.get('canton', None),
            data.get('parroquia', None), data.get('barrio_sector', None), data.get('calle_principal', None),
            data.get('calle_secundaria', None), data.get('referencia', None), patient_id
        ))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al actualizar paciente: {e}")
    finally:
        conn.close()

def delete_patient(patient_id):
    """Elimina un paciente de la base de datos."""
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute('DELETE FROM pacientes WHERE id = ?', (patient_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al eliminar paciente: {e}")
    finally:
        conn.close()

# Funciones CRUD para acompañantes

def create_companion(data):
    """Inserta un nuevo acompañante en la base de datos."""
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute('''
            INSERT INTO acompanantes (
                en_caso_necesario_llamar_a, parentesco, direccion, telefono_acompanante, nombre_apellido_representante,
                identificacion_representante, telefono_representante
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            data.get('en_caso_necesario_llamar_a', None), data.get('parentesco', None), data.get('direccion', None),
            data.get('telefono_acompanante', None), data.get('nombre_apellido_representante', None),
            data.get('identificacion_representante', None), data.get('telefono_representante', None)
        ))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al crear acompañante: {e}")
    finally:
        conn.close()

def read_companions():
    """Lee todos los acompañantes de la base de datos."""
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute('SELECT * FROM acompanantes')
        companions = c.fetchall()
        return companions
    except sqlite3.Error as e:
        print(f"Error al leer acompañantes: {e}")
        return []
    finally:
        conn.close()

def update_companion(companion_id, data):
    """Actualiza la información de un acompañante en la base de datos."""
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute('''
            UPDATE acompanantes
            SET en_caso_necesario_llamar_a = ?, parentesco = ?, direccion = ?, telefono_acompanante = ?, nombre_apellido_representante = ?,
                identificacion_representante = ?, telefono_representante = ?
            WHERE id = ?
        ''', (
            data.get('en_caso_necesario_llamar_a', None), data.get('parentesco', None), data.get('direccion', None),
            data.get('telefono_acompanante', None), data.get('nombre_apellido_representante', None),
            data.get('identificacion_representante', None), data.get('telefono_representante', None), companion_id
        ))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al actualizar acompañante: {e}")
    finally:
        conn.close()

def delete_companion(companion_id):
    """Elimina un acompañante de la base de datos."""
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute('DELETE FROM acompanantes WHERE id = ?', (companion_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al eliminar acompañante: {e}") 
    finally:
        conn.close()

# Ejemplo de uso
def manage_patients():
    # Simulación de datos de un paciente
    patient_data = {
        'primer_apellido': "García",
        'segundo_apellido': "Pérez",
        'primer_nombre': "Juan",
        'segundo_nombre': "Carlos",
        'tipo_documento_identificacion': "Cédula",
        'estado_civil': "Soltero",
        'sexo': "Masculino",
        'telefono_fijo': "123456789",
        'telefono_celular': "987654321",
        'correo_electronico': "juan.garcia@example.com",
        'lugar_nacimiento': "Quito",
        'nacionalidad': "Ecuatoriano",
        'edad': 30,
        'condicion_edad': "Adulto",
        'autocertificacion_etnica': "No",
        'nacionalidad_etnica': "Indígena",
        'pueblos': "Kichwa",
        'nivel_educacion': "Universitario",
        'estado_nivel_educacion': "Completo",
        'ocupacion': "Ingeniero",
        'tipo_empresa_trabajo': "Privada",
        'seguro_salud_principal': "IESS",
        'tipo_bono_recibe': "Ninguno",
        'provincia': "Pichincha",
        'canton': "Quito",
        'parroquia': "Quito",
        'barrio_sector': "La Mariscal",
        'calle_principal': "Av. 6 de Diciembre",
        'calle_secundaria': "Calle Juan León Mera",
        'referencia': "Cerca del parque"
    }

    # Crear un nuevo paciente
    create_patient(patient_data)

# Llama a la función para probar la creación de un paciente
manage_patients()