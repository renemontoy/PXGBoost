import streamlit as st
import importlib
import os
from typing import Dict, List

# Configuración de la página
st.set_page_config(page_title="Mi Librería de Scripts", layout="wide")

# Diccionario de categorías y sus scripts
CATEGORIAS: Dict[str, List[str]] = {
    "Procesamiento de Datos": ["limpieza", "transformacion", "analisis"],
    "Visualización": ["graficos_basicos", "dashboard", "mapas"],
    "Machine Learning": ["clasificacion", "regresion", "clustering"]
}

def cargar_script(categoria: str, script: str):
    """Función para cargar dinámicamente un script"""
    try:
        modulo = importlib.import_module(f"apps.{categoria}.{script}")
        if hasattr(modulo, "main"):
            modulo.main()
        else:
            st.warning(f"El script {script} no tiene una función 'main'")
    except ImportError as e:
        st.error(f"No se pudo cargar el script: {e}")

def main():
    st.title("📚 Mi Librería de Scripts")
    
    # Sidebar para navegación
    with st.sidebar:
        st.header("Navegación")
        categoria_seleccionada = st.selectbox(
            "Selecciona una categoría", 
            list(CATEGORIAS.keys())
        )
        
        if categoria_seleccionada in CATEGORIAS:
            script_seleccionado = st.selectbox(
                "Selecciona un script",
                CATEGORIAS[categoria_seleccionada]
            )
            
            if st.button("Cargar Script"):
                st.session_state['script_actual'] = {
                    'categoria': categoria_seleccionada,
                    'script': script_seleccionado
                }
    
    # Área principal para mostrar el script seleccionado
    if 'script_actual' in st.session_state:
        st.header(f"{st.session_state['script_actual']['categoria']} > {st.session_state['script_actual']['script']}")
        cargar_script(
            st.session_state['script_actual']['categoria'],
            st.session_state['script_actual']['script']
        )
    else:
        st.info("Selecciona un script de la barra lateral para comenzar")

if __name__ == "__main__":
    main()