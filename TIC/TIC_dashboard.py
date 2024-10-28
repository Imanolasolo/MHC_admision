import streamlit as st
import subprocess
import os
from Modules.UCI import Dashboard_UCI
from Modules.Urgencias import Dashboard_urgencias
from Modules.Hospitalizacion import Dashboard_hospitalizacion

def main():
    st.title("Panel TIC")
    
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
        st.button("Volver al Panel TIC", on_click=go_back)
    elif st.session_state.current_view == 'hospitalizacion':
        Dashboard_hospitalizacion()
        st.button("Volver al Panel TIC", on_click=go_back)
    elif st.session_state.current_view == 'urgencias':
        Dashboard_urgencias()
        st.button("Volver al Panel TIC", on_click=go_back)

def show_dashboard():
    st.success("Gestión de modulos permitidos")
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

    # Botón para abrir ViewCalendar.py
    if st.button("Ver calendario quirofanos"):
        # Ejecutar la aplicación ViewCalendar.py en un nuevo proceso
        subprocess.Popen(["streamlit", "run", "Modules/Calendar/ViewCalendar_quirofano.py"], cwd=os.getcwd())
        st.write("**La aplicación de calendario se ha abierto en una nueva ventana.**")

if __name__ == "__main__":
    main()



