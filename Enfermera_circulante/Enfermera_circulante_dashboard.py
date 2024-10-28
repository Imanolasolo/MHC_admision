import streamlit as st
import subprocess
import os
from Modules.UCI import Dashboard_UCI
from Modules.Urgencias import Dashboard_urgencias
from Modules.Hospitalizacion import Dashboard_hospitalizacion
from Admisionista.admisionista_crud import read_patients  # Asegúrate de tener esta función

def main():
    st.title("Panel Enfermería Circulante")
    
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
        st.button("Volver al Panel Enfermería Circulante", on_click=go_back)
    elif st.session_state.current_view == 'hospitalizacion':
        Dashboard_hospitalizacion()
        st.button("Volver al Panel Enfermería Circulante", on_click=go_back)
    elif st.session_state.current_view == 'urgencias':
        Dashboard_urgencias()
        st.button("Volver al Panel Enfermería Circulante", on_click=go_back)

def show_dashboard():
    st.success("Gestión de Módulos Permitidos")
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
        # Crear un listado de apellidos para el selector
        last_names = sorted(set(patient[1] for patient in patients))  # Suponiendo que el segundo índice es el primer apellido
        selected_last_name = st.selectbox("Selecciona el primer apellido del paciente:", last_names)

        # Filtrar pacientes por el apellido seleccionado
        filtered_patients = [patient for patient in patients if patient[1] == selected_last_name]

        if filtered_patients:
            # Mostrar detalles del paciente en una tabla
            patient_data = []
            for patient in filtered_patients:
                patient_data.append({
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
                })

            # Mostrar los datos del paciente en formato de tabla
            st.table(patient_data)  # O st.dataframe(patient_data) para una tabla interactiva
        else:
            st.write("No hay pacientes registrados con ese apellido.")
    else:
        st.write("No hay pacientes registrados.")

 

if __name__ == "__main__":
    main()
