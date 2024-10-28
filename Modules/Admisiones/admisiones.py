import streamlit as st
from patient_crud import create_patient, read_patients, update_patient, delete_patient, create_companion, read_companions, update_companion, delete_companion

def manage_patients():
    st.title("Gestión de Pacientes")
    
    # Crear paciente
    st.subheader("Añadir Paciente")
    with st.form("form_create_patient"):
        primer_apellido = st.text_input("Primer Apellido")
        segundo_apellido = st.text_input("Segundo Apellido")
        primer_nombre = st.text_input("Primer Nombre")
        segundo_nombre = st.text_input("Segundo Nombre")
        tipo_documento_identificacion = st.selectbox("Tipo de Documento de Identificación", ["cédula de ciudadanía", "cédula de identidad", "pasaporte", "carnet de refugiado", "S/D"])
        estado_civil = st.text_input("Estado Civil")
        sexo = st.selectbox("Sexo", ["Masculino", "Femenino"])
        telefono_fijo = st.text_input("Número Teléfono Fijo")
        telefono_celular = st.text_input("Número Teléfono Celular")
        correo_electronico = st.text_input("Correo Electrónico")
        lugar_nacimiento = st.text_input("Lugar de Nacimiento")
        nacionalidad = st.text_input("Nacionalidad")
        edad = st.number_input("Edad")
        condicion_edad = st.selectbox("Condición Edad", ["horas (H)", "días (D)", "meses (M)", "años (A)"])
        autocertificacion_etnica = st.text_input("Autocertificación Étnica")
        nacionalidad_etnica = st.text_input("Nacionalidad Étnica")
        pueblos = st.text_input("Pueblos")
        nivel_educacion = st.text_input("Nivel de Educación")
        estado_nivel_educacion = st.text_input("Estado Nivel de Educación")
        ocupacion = st.text_input("Ocupación/Profesión Principal")
        tipo_empresa_trabajo = st.text_input("Tipo de Empresa de Trabajo")
        seguro_salud_principal = st.text_input("Seguro de Salud Principal")
        tipo_bono_recibe = st.text_input("Tipo de Bono que Recibe")
        provincia = st.text_input("Provincia")
        canton = st.text_input("Cantón")
        parroquia = st.text_input("Parroquia")
        barrio_sector = st.text_input("Barrio o Sector")
        calle_principal = st.text_input("Calle Principal")
        calle_secundaria = st.text_input("Calle Secundaria")
        referencia = st.text_input("Referencia")
        
        if st.form_submit_button("Añadir Paciente"):
            success = create_patient(primer_apellido, segundo_apellido, primer_nombre, segundo_nombre, tipo_documento_identificacion, estado_civil, sexo,
                                    telefono_fijo, telefono_celular, correo_electronico, lugar_nacimiento, nacionalidad, edad, condicion_edad,
                                    autocertificacion_etnica, nacionalidad_etnica, pueblos, nivel_educacion, estado_nivel_educacion, ocupacion,
                                    tipo_empresa_trabajo, seguro_salud_principal, tipo_bono_recibe, provincia, canton, parroquia, barrio_sector,
                                    calle_principal, calle_secundaria, referencia)
            if success:
                st.success("Paciente añadido exitosamente.")
            else:
                st.error("Error al añadir el paciente.")
    
    # Leer pacientes
    st.subheader("Lista de Pacientes")
    patients = read_patients()
    st.write(patients)
    
    # Actualizar paciente
    st.subheader("Actualizar Paciente")
    patient_id = st.text_input("ID del Paciente para Actualizar")
    if patient_id:
        patient = next((p for p in patients if p[0] == patient_id), None)
        if patient:
            with st.form("form_update_patient"):
                primer_apellido = st.text_input("Primer Apellido", value=patient[1])
                segundo_apellido = st.text_input("Segundo Apellido", value=patient[2])
                primer_nombre = st.text_input("Primer Nombre", value=patient[3])
                segundo_nombre = st.text_input("Segundo Nombre", value=patient[4])
                tipo_documento_identificacion = st.text_input("Tipo de Documento de Identificación", value=patient[5])
                estado_civil = st.text_input("Estado Civil", value=patient[6])
                sexo = st.text_input("Sexo", value=patient[7])
                telefono_fijo = st.text_input("Número Teléfono Fijo", value=patient[8])
                telefono_celular = st.text_input("Número Teléfono Celular", value=patient[9])
                correo_electronico = st.text_input("Correo Electrónico", value=patient[10])
                lugar_nacimiento = st.text_input("Lugar de Nacimiento", value=patient[11])
                nacionalidad = st.text_input("Nacionalidad", value=patient[12])
                edad = st.number_input("Edad", value=patient[13])
                condicion_edad = st.text_input("Condición Edad", value=patient[14])
                autocertificacion_etnica = st.text_input("Autocertificación Étnica", value=patient[15])
                nacionalidad_etnica = st.text_input("Nacionalidad Étnica", value=patient[16])
                pueblos = st.text_input("Pueblos", value=patient[17])
                nivel_educacion = st.text_input("Nivel de Educación", value=patient[18])
                estado_nivel_educacion = st.text_input("Estado Nivel de Educación", value=patient[19])
                ocupacion = st.text_input("Ocupación/Profesión Principal", value=patient[20])
                tipo_empresa_trabajo = st.text_input("Tipo de Empresa de Trabajo", value=patient[21])
                seguro_salud_principal = st.text_input("Seguro de Salud Principal", value=patient[22])
                tipo_bono_recibe = st.text_input("Tipo de Bono que Recibe", value=patient[23])
                provincia = st.text_input("Provincia", value=patient[24])
                canton = st.text_input("Cantón", value=patient[25])
                parroquia = st.text_input("Parroquia", value=patient[26])
                barrio_sector = st.text_input("Barrio o Sector", value=patient[27])
                calle_principal = st.text_input("Calle Principal", value=patient[28])
                calle_secundaria = st.text_input("Calle Secundaria", value=patient[29])
                referencia = st.text_input("Referencia", value=patient[30])
                
                if st.form_submit_button("Actualizar Paciente"):
                    update_patient(patient_id, primer_apellido, segundo_apellido, primer_nombre, segundo_nombre, tipo_documento_identificacion, estado_civil, sexo,
                                    telefono_fijo, telefono_celular, correo_electronico, lugar_nacimiento, nacionalidad, edad, condicion_edad,
                                    autocertificacion_etnica, nacionalidad_etnica, pueblos, nivel_educacion, estado_nivel_educacion, ocupacion,
                                    tipo_empresa_trabajo, seguro_salud_principal, tipo_bono_recibe, provincia, canton, parroquia, barrio_sector,
                                    calle_principal, calle_secundaria, referencia)
                    st.success("Paciente actualizado exitosamente.")
    
    # Eliminar paciente
    st.subheader("Eliminar Paciente")
    patient_id_to_delete = st.text_input("ID del Paciente para Eliminar")
    if st.button("Eliminar Paciente"):
        delete_patient(patient_id_to_delete)
        st.success("Paciente eliminado exitosamente.")

def manage_companions():
    st.title("Gestión de Acompañantes")
    
    # Crear acompañante
    st.subheader("Añadir Acompañante")
    with st.form("form_create_companion"):
        en_caso_necesario_llamar_a = st.text_input("En caso necesario llamar a")
        parentesco = st.text_input("Parentesco")
        direccion = st.text_input("Dirección")
        telefono_acompanante = st.text_input("Número Teléfono Acompañante")
        nombre_apellido_representante = st.text_input("Nombre y Apellido del Representante")
        identificacion_representante = st.text_input("Número de Identificación del Representante")
        telefono_representante = st.text_input("Número Teléfono del Representante")
        
        if st.form_submit_button("Añadir Acompañante"):
            success = create_companion(en_caso_necesario_llamar_a, parentesco, direccion, telefono_acompanante, nombre_apellido_representante, identificacion_representante, telefono_representante)
            if success:
                st.success("Acompañante añadido exitosamente.")
            else:
                st.error("Error al añadir el acompañante.")
    
    # Leer acompañantes
    st.subheader("Lista de Acompañantes")
    companions = read_companions()
    st.write(companions)
    
    # Actualizar acompañante
    st.subheader("Actualizar Acompañante")
    companion_id = st.text_input("ID del Acompañante para Actualizar")
    if companion_id:
        companion = next((c for c in companions if c[0] == companion_id), None)
        if companion:
            with st.form("form_update_companion"):
                en_caso_necesario_llamar_a = st.text_input("En caso necesario llamar a", value=companion[1])
                parentesco = st.text_input("Parentesco", value=companion[2])
                direccion = st.text_input("Dirección", value=companion[3])
                telefono_acompanante = st.text_input("Número Teléfono Acompañante", value=companion[4])
                nombre_apellido_representante = st.text_input("Nombre y Apellido del Representante", value=companion[5])
                identificacion_representante = st.text_input("Número de Identificación del Representante", value=companion[6])
                telefono_representante = st.text_input("Número Teléfono del Representante", value=companion[7])
                
                if st.form_submit_button("Actualizar Acompañante"):
                    update_companion(companion_id, en_caso_necesario_llamar_a, parentesco, direccion, telefono_acompanante, nombre_apellido_representante, identificacion_representante, telefono_representante)
                    st.success("Acompañante actualizado exitosamente.")
    
    # Eliminar acompañante
    st.subheader("Eliminar Acompañante")
    companion_id_to_delete = st.text_input("ID del Acompañante para Eliminar")
    if st.button("Eliminar Acompañante"):
        delete_companion(companion_id_to_delete)
        st.success("Acompañante eliminado exitosamente.")
