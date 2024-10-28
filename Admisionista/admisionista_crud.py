import sqlite3

def connect_db():
    return sqlite3.connect('hospital.db')

# Funciones para Pacientes
def create_patient(data):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        INSERT INTO pacientes (primer_apellido, segundo_apellido, primer_nombre, segundo_nombre, tipo_documento_identificacion, estado_civil, sexo, telefono_fijo, telefono_celular, correo_electronico, lugar_nacimiento, nacionalidad, edad, condicion_edad, autocertificacion_etnica, nacionalidad_etnica, pueblos, nivel_educacion, estado_nivel_educacion, ocupacion, tipo_empresa_trabajo, seguro_salud_principal, tipo_bono_recibe, provincia, canton, parroquia, barrio_sector, calle_principal, calle_secundaria, referencia, en_caso_necesario_llamar_a, parentesco, direccion, telefono_contacto, fecha_admision, fecha_egreso, numero_dis_estadia, codigo_de_servicio_INEC, diagnosticos_o_sindromes_principal, CIE, definitivo, diagnosticos_o_sindromes_secundario, CIE_secundario, definitivo_secundario, alta, muerte_menos_de_48_horas, muerte_mas_de_48_horas, clinico, quirurgico, procedimientos_clinicos_o_quirurgicos_principales, sello_y_firma_del_responsable )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

def read_patients():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('SELECT * FROM pacientes')
    patients = c.fetchall()
    conn.close()
    return patients

def update_patient(patient_id, data):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        UPDATE pacientes SET primer_apellido = ?, segundo_apellido = ?, primer_nombre = ?, segundo_nombre = ?, tipo_documento_identificacion = ?, estado_civil = ?, sexo = ?, telefono_fijo = ?, telefono_celular = ?, correo_electronico = ?, lugar_nacimiento = ?, nacionalidad = ?, edad = ?, condicion_edad = ?, autocertificacion_etnica = ?, nacionalidad_etnica = ?, pueblos = ?, nivel_educacion = ?, estado_nivel_educacion = ?, ocupacion = ?, tipo_empresa_trabajo = ?, seguro_salud_principal = ?, tipo_bono_recibe = ?, provincia = ?, canton = ?, parroquia = ?, barrio_sector = ?, calle_principal = ?, calle_secundaria = ?, referencia = ? WHERE id = ?
    ''', data + (patient_id,))
    conn.commit()
    conn.close()

def delete_patient(patient_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('DELETE FROM pacientes WHERE id = ?', (patient_id,))
    conn.commit()
    conn.close()

# Funciones para Acompañantes
def create_companion(data):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        INSERT INTO acompanantes (en_caso_necesario_llamar_a, parentesco, direccion, telefono_acompanante, nombre_apellido_representante, identificacion_representante, telefono_representante)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

def read_companions():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM acompanantes')
    rows = c.fetchall()
    conn.close()
    return rows

def update_companion(companion_id, data):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        UPDATE acompanantes SET en_caso_necesario_llamar_a = ?, parentesco = ?, direccion = ?, telefono_acompanante = ?, nombre_apellido_representante = ?, identificacion_representante = ?, telefono_representante = ? WHERE id = ?
    ''', data + (companion_id,))
    conn.commit()
    conn.close()

def delete_companion(companion_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('DELETE FROM acompanantes WHERE id = ?', (companion_id,))
    conn.commit()
    conn.close()
