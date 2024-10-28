import streamlit as st
from Modules.UCI import Dashboard_UCI
from Modules.Urgencias import Dashboard_urgencias
from Modules.Hospitalizacion import Dashboard_hospitalizacion
from Admisionista.admisionista_crud import read_patients  # Maintain read_patients import
import sqlite3  # Import sqlite3 to handle database operations

def update_patient_directly(patient_id, data):
    """Updates the patient record directly in the database."""
    conn = sqlite3.connect('hospital.db')  # Ensure you have the correct path to your database
    cursor = conn.cursor()
    query = """
        UPDATE pacientes SET 
            fecha_admision = ?, 
            fecha_egreso = ?, 
            numero_dis_estadia = ?, 
            codigo_de_servicio_INEC = ?, 
            diagnosticos_o_sindromes_principal = ?, 
            CIE = ?, 
            definitivo = ?, 
            diagnosticos_o_sindromes_secundario = ?, 
            CIE_secundario = ?, 
            definitivo_secundario = ?, 
            alta = ?, 
            muerte_menos_de_48_horas = ?, 
            muerte_mas_de_48_horas = ?, 
            clinico = ?, 
            quirurgico = ?, 
            procedimientos_clinicos_o_quirurgicos_principales = ?, 
            sello_y_firma_del_responsable = ? 
        WHERE id = ?
    """
    cursor.execute(query, (
        data['fecha_admision'],
        data['fecha_egreso'],
        data['numero_dis_estadia'],
        data['codigo_de_servicio_INEC'],
        data['diagnosticos_o_sindromes_principal'],
        data['CIE'],
        data['definitivo'],
        data['diagnosticos_o_sindromes_secundario'],
        data['CIE_secundario'],
        data['definitivo_secundario'],
        data['alta'],
        data['muerte_menos_de_48_horas'],
        data['muerte_mas_de_48_horas'],
        data['clinico'],
        data['quirurgico'],
        data['procedimientos_clinicos_o_quirurgicos_principales'],
        data['sello_y_firma_del_responsable'],
        patient_id
    ))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0  # Returns True if at least one row was updated

def main():
    st.title("Panel Médico General")
    
    # Inicializa la variable de estado si no está presente
    if 'current_view' not in st.session_state:
        st.session_state.current_view = 'dashboard'

    # Función para volver al dashboard principal
    def go_back():
        st.session_state.current_view = 'dashboard'

    # Mostrar la vista según el estado actual
    if st.session_state.current_view == 'dashboard':
        show_dashboard()
    elif st.session_state.current_view == 'uci':
        Dashboard_UCI()
        st.button("Volver al Panel Médico General", on_click=go_back)
    elif st.session_state.current_view == 'hospitalizacion':
        Dashboard_hospitalizacion()
        st.button("Volver al Panel Médico General", on_click=go_back)
    elif st.session_state.current_view == 'urgencias':
        Dashboard_urgencias()
        st.button("Volver al Panel Médico General", on_click=go_back)

def show_dashboard():
    st.success("Gestión de módulos permitidos")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Acceder al Módulo de UCI"):
            st.session_state.current_view = 'uci'
    with col2:
        if st.button("Acceder al Módulo de Hospitalización"):
            st.session_state.current_view = 'hospitalizacion'
    with col3:
        if st.button("Acceder al Módulo de Urgencias"):
            st.session_state.current_view = 'urgencias'

    # Selector para pacientes por primer apellido
    st.subheader("Seleccionar Paciente")
    patients = read_patients()  # Asumiendo que esta función devuelve todos los pacientes
    if patients:
        last_names = sorted(set(patient[1] for patient in patients))
        selected_last_name = st.selectbox("Selecciona el primer apellido del paciente:", last_names)

        # Filtrar pacientes por el apellido seleccionado
        filtered_patients = [patient for patient in patients if patient[1] == selected_last_name]

        if filtered_patients:
            # Mostrar detalles del paciente en una tabla
            patient_data = [{ 
                "ID": patient[0],
                "Primer Apellido": patient[1],
                "Segundo Apellido": patient[2],
                "Primer Nombre": patient[3],
                "Segundo Nombre": patient[4],
                "Tipo de Documento": patient[5],
                "Estado Civil": patient[6],
                "Sexo": patient[7],
                "Teléfono Fijo": patient[8],
                "Teléfono Celular": patient[9],
                "Correo Electrónico": patient[10],
                "Lugar de Nacimiento": patient[11],
                "Nacionalidad": patient[12],
                "Edad": patient[13],
                "Condición de Edad": patient[14],
                "Autocertificación Étnica": patient[15],
                "Nacionalidad Étnica": patient[16],
                "Pueblos": patient[17],
                "Nivel de Educación": patient[18],
                "Estado de Nivel de Educación": patient[19],
                "Ocupación": patient[20],
                "Tipo de Empresa": patient[21],
                "Seguro de Salud": patient[22],
                "Tipo de Bono": patient[23],
                "Provincia": patient[24],
                "Cantón": patient[25],
                "Parroquia": patient[26],
                "Barrio/Sector": patient[27],
                "Calle Principal": patient[28],
                "Calle Secundaria": patient[29],
                "Referencia": patient[30],
                "En caso necesario llamar a": patient[31],
                "Parentesco": patient[32],
                "Dirección": patient[33],
                "Teléfono Acompañante": patient[34],
                "Fecha de Admisión": patient[35],
                "Fecha de Egreso": patient[36],
                "Nº Días de Estadía": patient[37],
                "Código Servicio INEC": patient[38],
                "Diagnósticos Principales": patient[39],
                "CIE": patient[40],
                "Definitivo": patient[41],
                "Diagnósticos Secundarios": patient[42],
                "CIE Secundario": patient[43],
                "Definitivo Secundario": patient[44],
                "Alta": patient[45],
                "Muerte Menos de 48 Horas": patient[46],
                "Muerte Más de 48 Horas": patient[47],
                "Clínico": patient[48],
                "Quirúrgico": patient[49],
                "Procedimientos Principales": patient[50],
                "Sello y Firma del Responsable": patient[51]
            } for patient in filtered_patients]

            st.table(patient_data)
        else:
            st.write("No hay pacientes registrados con ese apellido.")
    else:
        st.write("No hay pacientes registrados.")

    # Sección para actualizar paciente
    st.subheader("Actualizar Paciente")
    
    if filtered_patients:
        patient_ids = [patient[0] for patient in filtered_patients]
        selected_patient_id = st.selectbox("Selecciona un paciente para actualizar:", patient_ids)

        # Obtener datos del paciente seleccionado
        selected_patient = next(patient for patient in filtered_patients if patient[0] == selected_patient_id)
        patient_name = f"{selected_patient[3]} {selected_patient[1]} {selected_patient[2]}"
        st.write(f"Actualizando paciente: {patient_name}")

        # Campos de actualización
        fecha_admision = st.text_input("Fecha admisión", value=selected_patient[35])
        fecha_egreso = st.text_input("Fecha egreso", value=selected_patient[36])
        numero_dis_estadia = st.text_input("Nº días de estadía", value=selected_patient[37])
        codigo_de_servicio_INEC = st.text_input("Código servicio (INEC)", value=selected_patient[38])
        diagnosticos_o_sindromes_principal = st.text_input("Diagnósticos o síndromes principales", value=selected_patient[39])
        CIE = st.text_input("CIE", value=selected_patient[40])
        definitivo = st.text_input("Definitivo", value=selected_patient[41])
        diagnosticos_o_sindromes_secundario = st.text_input("Diagnósticos o síndromes secundarios", value=selected_patient[42])
        CIE_secundario = st.text_input("CIE secundario", value=selected_patient[43])
        definitivo_secundario = st.text_input("Definitivo secundario", value=selected_patient[44])
        alta = st.text_input("Alta", value=selected_patient[45])
        muerte_menos_de_48_horas = st.text_input("Muerte menos de 48 horas", value=selected_patient[46])
        muerte_mas_de_48_horas = st.text_input("Muerte más de 48 horas", value=selected_patient[47])
        clinico = st.text_input("Clínico", value=selected_patient[48])
        quirurgico = st.text_input("Quirúrgico", value=selected_patient[49])
        procedimientos_clinicos_o_quirurgicos_principales = st.text_input("Procedimientos principales", value=selected_patient[50])
        sello_y_firma_del_responsable = st.text_input("Sello y firma del responsable", value=selected_patient[51])

        # Crear un diccionario con los datos actualizados
        update_data = {
            'fecha_admision': fecha_admision,
            'fecha_egreso': fecha_egreso,
            'numero_dis_estadia': numero_dis_estadia,
            'codigo_de_servicio_INEC': codigo_de_servicio_INEC,
            'diagnosticos_o_sindromes_principal': diagnosticos_o_sindromes_principal,
            'CIE': CIE,
            'definitivo': definitivo,
            'diagnosticos_o_sindromes_secundario': diagnosticos_o_sindromes_secundario,
            'CIE_secundario': CIE_secundario,
            'definitivo_secundario': definitivo_secundario,
            'alta': alta,
            'muerte_menos_de_48_horas': muerte_menos_de_48_horas,
            'muerte_mas_de_48_horas': muerte_mas_de_48_horas,
            'clinico': clinico,
            'quirurgico': quirurgico,
            'procedimientos_clinicos_o_quirurgicos_principales': procedimientos_clinicos_o_quirurgicos_principales,
            'sello_y_firma_del_responsable': sello_y_firma_del_responsable
        }

        if st.button("Actualizar Paciente"):
            if update_patient_directly(selected_patient_id, update_data):
                st.success("Paciente actualizado correctamente.")
            else:
                st.error("Error al actualizar el paciente. Por favor, verifica los datos.")

if __name__ == "__main__":
    main()

