import streamlit as st
import sqlite3
import bcrypt
import base64
from auth.jwt_handler import generate_token, decode_token
from admin.admin_dashboard import admin_dashboard
from TIC.TIC_dashboard import main as TIC_Dashboard
from Medico_general.Medico_general_dashboard import main as Medico_general_dashboard
from Enfermeria_hospitalizacion.Enfermeria_hospitalizacion_dashboard import main as Enfermeria_hospitalizacion_dashboard
from Admisionista.Admisionista_dashboard import admisionista_dashboard
from Enfermeria_UCI.Enfermeria_UCI_dashboard import main as Enfermeria_UCI_dashboard
from Cajero.Cajero_dashboard import main as Cajero_dashboard
from Medico_emergencias.Medico_emergencias_dashboard import main as Medico_emergencias_dashboard
from Enfermeria_emergencias.Enfermeria_emergencias_dashboard import main as Enfermeria_emergencias_dashboard
from Anestesiólogo.Anestesiologo_dashboard import main as Anestesiologo_dashboard
from Paciente.Paciente_dashboard import main as Paciente_dashboard
from Medico_especialista.Medico_especialista_dashboard import main as Medico_especialista_dashboard
from Enfermera_quirofano. Enfermeria_quirofano_dashboard import main as Enfermeria_quirofano_dashboard
from Medico_cirujano.Medico_cirujano_dashboard import main as Medico_cirujano_dashboard
from Jefe_enfermeria.Jefe_enfermería_dashboard import main as Jefe_enfermeria_dashboard
from Enfermera_postoperatorio.Enfermera_postoperatorio_dashboard import main as Enfermera_postoperatorio_dashboard
from Enfermera_circulante.Enfermera_circulante_dashboard import main as Enfermera_circulante_dashboard
from Prestador_de_servicios_de_farmacia.Prestador_servicios_farmacia_dashboard import main as Prestador_servicios_farmacia_dashboard
from Administrativo.Administrativo_dashboard import main as Administrativo_dashboard
from Contable.Contable_dashboard import main as Contable_dashboard
from Auditor.Auditor_dashboard import main as Auditor_dashboard
from database.db_setup import init_db

# Inicializar la base de datos
init_db()

# Configurar título de la página e ícono de pestaña
st.set_page_config(
    page_title="Manta Hospital Center",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://wa.me/5930993513082?text=Solicito%20ayuda%20con%20la%20app%20MHC',
        'Report a bug': "https://wa.me/5930993513082?text=Solicito%20ayuda%20con%20la%20app%20MHC",
        'About': "# App creada por CodeCodix"
    }
)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_base64 = get_base64_of_bin_file('MHC_Marketing_background.jpg')

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url('data:image/jpeg;base64,{img_base64}') no-repeat center center fixed;
        background-size: cover;
    }}

    .footer {{
        position: fixed;
        bottom: 0;
        width: 100%;
        # background-color: grey;
        text-align: left;
        padding: 10px;
        font-size: 14px;
        color: black;
        border-top: 1px solid #ddd;
    }}
    .footer .CodeCodix {{
        color: red;
        font-weight: bold;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# Función para verificar el login
def login():
    # Definir la estructura de la página usando columnas de Streamlit
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image('MHC_logo.png', width=200)
    
    with col2:
        st.header('Bienvenido/a a la plataforma MHC')
        
    st.text('Introduzca sus datos para comenzar a interactuar con la plataforma, por favor.')
        
        # Campos de entrada para nombre de usuario y contraseña
    username = st.text_input('Nombre de usuario', key='username_input')
    password = st.text_input('Contraseña', type='password', key='password_input')
        
        # Botón para iniciar sesión
    if st.button('Ingreso'):
            conn = sqlite3.connect('hospital.db')
            c = conn.cursor()
            
            # Consultar el usuario por nombre de usuario
            c.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = c.fetchone()
            
            if user:
                # Verificar la contraseña usando bcrypt
                if bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
                    st.success('Ingreso exitoso')
                    # Generar token con el ID de usuario y rol
                    token = generate_token(user[0], user[4])
                    st.session_state['token'] = token  # Guardar el token en la sesión
                    st.session_state['role'] = user[4]    # Guardar el rol del usuario en la sesión
                    st.rerun()  # Volver a cargar la aplicación para actualizar el estado
                else:
                    st.error('Usuario o contraseña incorrectos')
            else:
                st.error('Usuario o contraseña incorrectos')
            
            conn.close()

# Función principal de la aplicación
def main():
    if 'token' not in st.session_state:
        login()
    else:
        # Decodificar el token para obtener el payload
        payload = decode_token(st.session_state['token'])
        
        if payload:
            role_name = st.session_state['role']  # Obtener el rol desde la sesión
            st.sidebar.image('MHC_logo.png', width=150)
            st.sidebar.success(f'Ingreso como {role_name}')
            
            # Botón para cambiar de usuario
            if st.sidebar.button('Cambio usuario', key='switch_user_button'):
                st.session_state.clear()  # Limpiar la sesión
                st.rerun()
            
            # Mostrar dashboard según el rol
            if role_name == 'admin':
                admin_dashboard()
            elif role_name == 'TIC':
                TIC_Dashboard()
            elif role_name == 'Enfermera de hospitalización':
                Enfermeria_hospitalizacion_dashboard()
            elif role_name == 'Médico general':
                Medico_general_dashboard()
            elif role_name == 'Admisionista':
                admisionista_dashboard()
            elif role_name == 'Enfermera UCI':
                Enfermeria_UCI_dashboard()
            elif role_name == 'Cajero':
                Cajero_dashboard()
            elif role_name == 'Médico emergenciólogo':
                Medico_emergencias_dashboard()
            elif role_name == 'Enfermera emergencia':
                Enfermeria_emergencias_dashboard()
            elif role_name == 'Anestesiólogo':
                Anestesiologo_dashboard()
            elif role_name == 'Paciente':
                Paciente_dashboard()
            elif role_name == 'Médico especialista':
                Medico_especialista_dashboard()
            elif role_name == 'Enfermera quirófano':
                Enfermeria_quirofano_dashboard()
            elif role_name == 'Médico cirujano':
                Medico_cirujano_dashboard()
            elif role_name == 'Jefe enfermería':
                Jefe_enfermeria_dashboard()
            elif role_name == 'Enfermera postoperatorio':
                Enfermera_postoperatorio_dashboard()
            elif role_name == 'Enfermera circulante':
                Enfermera_circulante_dashboard()
            elif role_name == 'Prestador de servicios de farmacia':
                Prestador_servicios_farmacia_dashboard()
            elif role_name == 'Administrativo':
                Administrativo_dashboard()
            elif role_name == 'Contable':
                Contable_dashboard()
            elif role_name == 'Auditor':
                Auditor_dashboard()
            # Agrega más roles y dashboards según sea necesario
        else:
            st.error('Sesión finalizada, por favor ingrese de nuevo')
            login()

# Agregar pie de página
st.markdown(
    """
    <div class="footer">
        <p>© 2024 CodeCodix | All rights reserved </p>
    </div>
    """,
    unsafe_allow_html=True
)


if __name__ == '__main__':
    main()



