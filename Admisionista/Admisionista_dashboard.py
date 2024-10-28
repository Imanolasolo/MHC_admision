import streamlit as st
import pandas as pd
from Admisionista.admisionista_crud import create_patient, read_patients, update_patient, delete_patient, create_companion, read_companions, update_companion, delete_companion

def manage_patients():
    st.title("Gestión de Pacientes")
    
    option = st.selectbox("Seleccionar una opción", ["Crear", "Leer", "Actualizar", "Eliminar"])
    
    if option == "Crear":
        st.subheader("Crear Paciente")
        data = {
            'primer_apellido': st.text_input("Primer Apellido"),
            'segundo_apellido': st.text_input("Segundo Apellido"),
            'primer_nombre': st.text_input("Primer Nombre"),
            'segundo_nombre': st.text_input("Segundo Nombre"),
            'tipo_documento_identificacion': st.selectbox("Tipo de Documento de Identificación", ['cédula de ciudadanía', 'cédula de identidad', 'pasaporte', 'carnet de refugiado', 'S/D']),
            'estado_civil': st.text_input("Estado Civil"),
            'sexo': st.selectbox("Sexo", ['Masculino', 'Femenino']),
            'telefono_fijo': st.text_input("Teléfono Fijo"),
            'telefono_celular': st.text_input("Teléfono Celular"),
            'correo_electronico': st.text_input("Correo Electrónico"),
            'lugar_nacimiento': st.text_input("Lugar de Nacimiento"),
            'nacionalidad': st.text_input("Nacionalidad"),
            'edad': st.number_input("Edad", min_value=0),
            'condicion_edad': st.selectbox("Condición Edad", ['H', 'D', 'M', 'A']),
            'autocertificacion_etnica': st.text_input("Autocertificación Étnica"),
            'nacionalidad_etnica': st.text_input("Nacionalidad Étnica"),
            'pueblos': st.text_input("Pueblos"),
            'nivel_educacion': st.text_input("Nivel de Educación"),
            'estado_nivel_educacion': st.text_input("Estado Nivel de Educación"),
            'ocupacion': st.text_input("Ocupación"),
            'tipo_empresa_trabajo': st.text_input("Tipo de Empresa de Trabajo"),
            'seguro_salud_principal': st.text_input("Seguro de Salud Principal"),
            'tipo_bono_recibe': st.text_input("Tipo de Bono que Recibe"),
            'provincia': st.text_input("Provincia"),
            'canton': st.text_input("Cantón"),
            'parroquia': st.text_input("Parroquia"),
            'barrio_sector': st.text_input("Barrio o Sector"),
            'calle_principal': st.text_input("Calle Principal"),
            'calle_secundaria': st.text_input("Calle Secundaria"),
            'referencia': st.text_input("Referencia"),
            'en_caso_necesario_llamar_a': st.text_input("En caso necesario llamar a:"),
            'parentesco': st.text_input("Parentesco"),
            'direccion': st.text_input("Dirección"),
            'telefono_contacto': st.text_input("Nº Teléfono)"),
            'fecha_admision': st.text_input("Fecha admisión"),
            'fecha_egreso': st.text_input("Fecha egreso"),
            'numero_dis_estadia': st.text_input("Nº días de estadía"),
            'codigo_de_servicio_INEC': st.text_input("Código servicio (INEC)"),
            'diagnosticos_o_sindromes_principal': st.text_input("Diagnosticos o sindromes principales"),
            'CIE': st.text_input("CIE"),
            'definitivo': st.text_input("definitivo"),
            'diagnosticos_o_sindromes_secundario': st.text_input("Diagnosticos o sindromes secundario"),
            'CIE_secundario': st.text_input("CIE secundario"),
            'definitivo_secundario': st.text_input("definitivo secundario"),
            'alta': st.text_input("alta"),
            'muerte_menos_de_48_horas': st.text_input("Muerte menos de 48 horas"),
            'muerte_mas_de_48_horas': st.text_input("muerte mas de 48 horas"),
            'clinico': st.text_input("clínico"),
            'quirurgico': st.text_input("quirúrgico"),
            'procedimientos_clinicos_o_quirurgicos_principales': st.text_input("procedimientos clínicos o quirúrgicos principales"),
            'sello_y_firma_del_responsable': st.text_input("sello y firma del responsable")
        }
        if st.button("Crear Paciente"):
            create_patient(tuple(data.values()))
            st.success("Paciente creado con éxito")

    elif option == "Leer":
        st.subheader("Leer Pacientes")
        patients = read_patients()
        if patients:
            # Convertir la lista de pacientes a un formato adecuado para la tabla
            patient_data = []
            for patient in patients:
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

        # Mostrar los datos de los pacientes en formato de tabla
            st.table(patient_data)  # También puedes usar st.dataframe(patient_data) para hacerla interactiva.
        else:
            st.write("No hay pacientes registrados.")

    elif option == "Actualizar":
        st.subheader("Actualizar Paciente")
        patient_id = st.number_input("ID del Paciente", min_value=1)
        patient_data = next((p for p in read_patients() if p[0] == patient_id), None)
        if patient_data:
            data = {
                'primer_apellido': st.text_input("Primer Apellido"),
            'segundo_apellido': st.text_input("Segundo Apellido"),
            'primer_nombre': st.text_input("Primer Nombre"),
            'segundo_nombre': st.text_input("Segundo Nombre"),
            'tipo_documento_identificacion': st.selectbox("Tipo de Documento de Identificación", ['cédula de ciudadanía', 'cédula de identidad', 'pasaporte', 'carnet de refugiado', 'S/D']),
            'estado_civil': st.text_input("Estado Civil"),
            'sexo': st.selectbox("Sexo", ['Masculino', 'Femenino']),
            'telefono_fijo': st.text_input("Teléfono Fijo"),
            'telefono_celular': st.text_input("Teléfono Celular"),
            'correo_electronico': st.text_input("Correo Electrónico"),
            'lugar_nacimiento': st.text_input("Lugar de Nacimiento"),
            'nacionalidad': st.text_input("Nacionalidad"),
            'edad': st.number_input("Edad", min_value=0),
            'condicion_edad': st.selectbox("Condición Edad", ['H', 'D', 'M', 'A']),
            'autocertificacion_etnica': st.text_input("Autocertificación Étnica"),
            'nacionalidad_etnica': st.text_input("Nacionalidad Étnica"),
            'pueblos': st.text_input("Pueblos"),
            'nivel_educacion': st.text_input("Nivel de Educación"),
            'estado_nivel_educacion': st.text_input("Estado Nivel de Educación"),
            'ocupacion': st.text_input("Ocupación"),
            'tipo_empresa_trabajo': st.text_input("Tipo de Empresa de Trabajo"),
            'seguro_salud_principal': st.text_input("Seguro de Salud Principal"),
            'tipo_bono_recibe': st.text_input("Tipo de Bono que Recibe"),
            'provincia': st.text_input("Provincia"),
            'canton': st.text_input("Cantón"),
            'parroquia': st.text_input("Parroquia"),
            'barrio_sector': st.text_input("Barrio o Sector"),
            'calle_principal': st.text_input("Calle Principal"),
            'calle_secundaria': st.text_input("Calle Secundaria"),
            'referencia': st.text_input("Referencia"),
            'en_caso_necesario_llamar_a': st.text_input("En caso necesario llamar a:"),
            'parentesco': st.text_input("Parentesco"),
            'direccion': st.text_input("Dirección"),
            'telefono_contacto': st.text_input("Nº Teléfono)"),
            'fecha_admision': st.text_input("Fecha admisión"),
            'fecha_egreso': st.text_input("Fecha egreso"),
            'numero_dis_estadia': st.text_input("Nº días de estadía"),
            'codigo_de_servicio_INEC': st.text_input("Código servicio (INEC)"),
            'diagnosticos_o_sindromes_principal': st.text_input("Diagnosticos o sindromes principales"),
            'CIE': st.text_input("CIE"),
            'definitivo': st.text_input("definitivo"),
            'diagnosticos_o_sindromes_secundario': st.text_input("Diagnosticos o sindromes secundario"),
            'CIE_secundario': st.text_input("CIE secundario"),
            'definitivo_secundario': st.text_input("definitivo secundario"),
            'alta': st.text_input("alta"),
            'muerte_menos_de_48_horas': st.text_input("Muerte menos de 48 horas"),
            'muerte_mas_de_48_horas': st.text_input("muerte mas de 48 horas"),
            'clinico': st.text_input("clínico"),
            'quirurgico': st.text_input("quirúrgico"),
            'procedimientos_clinicos_o_quirurgicos_principales': st.text_input("procedimientos clínicos o quirúrgicos principales"),
            'sello_y_firma_del_responsable': st.text_input("sello y firma del responsable")
            }
            if st.button("Actualizar Paciente"):
                update_patient(patient_id, tuple(data.values()))
                st.success("Paciente actualizado con éxito")

    elif option == "Eliminar":
        st.subheader("Eliminar Paciente")
        patient_id = st.number_input("ID del Paciente", min_value=1)
        if st.button("Eliminar Paciente"):
            delete_patient(patient_id)
            st.success("Paciente eliminado con éxito")

def manage_companions():
    st.title("Gestión de Acompañantes")
    
    option = st.selectbox("Seleccionar una opción", ["Crear", "Leer", "Actualizar", "Eliminar"])
    
    if option == "Crear":
        st.subheader("Crear Acompañante")
        data = {
            'en_caso_necesario_llamar_a': st.text_input("En caso necesario llamar a"),
            'parentesco': st.text_input("Parentesco"),
            'direccion': st.text_input("Dirección"),
            'telefono_acompanante': st.text_input("Teléfono Acompañante"),
            'nombre_apellido_representante': st.text_input("Nombre y Apellido del Representante"),
            'identificacion_representante': st.text_input("Número de Identificación del Representante"),
            'telefono_representante': st.text_input("Teléfono del Representante")
        }
        if st.button("Crear Acompañante"):
            create_companion(tuple(data.values()))
            st.success("Acompañante creado con éxito")

    elif option == "Leer":
        st.subheader("Leer Acompañantes")
        companions = read_companions()
        if companions:
            # Convertir los datos de acompañantes a un DataFrame
            df_companions = pd.DataFrame(companions, columns=[
                'ID', 'En caso necesario llamar a', 'Parentesco', 'Dirección', 'Teléfono Acompañante',
                'Nombre y Apellido del Representante', 'Número de Identificación del Representante',
                'Teléfono del Representante'
            ])
            st.dataframe(df_companions)
        else:
            st.write("No hay acompañantes registrados.")

    elif option == "Actualizar":
        st.subheader("Actualizar Acompañante")
        companion_id = st.number_input("ID del Acompañante", min_value=1)
        companion_data = next((c for c in read_companions() if c[0] == companion_id), None)
        if companion_data:
            data = {
                'en_caso_necesario_llamar_a': st.text_input("En caso necesario llamar a", value=companion_data[1]),
                'parentesco': st.text_input("Parentesco", value=companion_data[2]),
                'direccion': st.text_input("Dirección", value=companion_data[3]),
                'telefono_acompanante': st.text_input("Teléfono Acompañante", value=companion_data[4]),
                'nombre_apellido_representante': st.text_input("Nombre y Apellido del Representante", value=companion_data[5]),
                'identificacion_representante': st.text_input("Número de Identificación del Representante", value=companion_data[6]),
                'telefono_representante': st.text_input("Teléfono del Representante", value=companion_data[7])
            }
            if st.button("Actualizar Acompañante"):
                update_companion(companion_id, tuple(data.values()))
                st.success("Acompañante actualizado con éxito")

    elif option == "Eliminar":
        st.subheader("Eliminar Acompañante")
        companion_id = st.number_input("ID del Acompañante", min_value=1)
        if st.button("Eliminar Acompañante"):
            delete_companion(companion_id)
            st.success("Acompañante eliminado con éxito")

def admisionista_dashboard():
    st.sidebar.title("Panel de Admisión")
    option = st.sidebar.selectbox("Seleccionar un módulo", ["Gestión de Pacientes", "Gestión de Acompañantes"])
    
    if option == "Gestión de Pacientes":
        manage_patients()
    elif option == "Gestión de Acompañantes":
        manage_companions()
