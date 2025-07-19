import streamlit as st
import importlib
import os
from typing import Dict, List

# Configuración de la página
st.set_page_config(page_title="PXG Boost", layout="wide")

def inject_custom_css():
    st.markdown("""
    <style>
        :root {
            --pxg-black: #000000;
            --pxg-white: #FFFFFF;
            --pxg-accent: #FF0000;  /* Rojo PXG (puedes usar #FFD700 para dorado) */
        }
        .stApp {
            background-color: var(--pxg-white);
            color: var(--pxg-black);
        }
        h1, h2, h3 {
            color: var(--pxg-black) !important;
            font-family: 'Helvetica Neue', sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: var(--pxg-black) !important;
            color: var(--pxg-white) !important;
        }
        .stButton>button {
            background-color: var(--pxg-accent) !important;
            color: white !important;
            border: none;
            font-weight: bold;
        }
        .stTextInput>div>div>input {
            border: 2px solid var(--pxg-black) !important;
        }
    </style>
    """, unsafe_allow_html=True)

# Diccionario de categorías y sus scripts
CATEGORIAS: Dict[str, List[str]] = {
    "IES": ["Ferrule", "Amazon", "IES Balances"],
    "Acumatica": ["Canada","Adyen", "Shopify", "Global Payments"],
    "Quality": ["Spec Check","Warranty & Defect", "Weight Log"],
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
    inject_custom_css()
    
    # --- Header estilo PXG ---
    st.image("https://www.pxg.com/hubfs/PXG_Logo.svg", width=200)  # Usa tu propio logo
    st.markdown("---")
    
    # --- Sidebar (Navegación minimalista) ---
    with st.sidebar:
        st.markdown("## 🏆 Script Categories")
        categoria = st.radio(
            "Selecciona una categoría",
            ("Procesamiento", "Visualización", "ML", "Utilidades"),
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        st.markdown("**⚙️ Configuración**")
        modo_oscuro = st.toggle("Modo Premium", False)  # Inspirado en el "lujo" PXG
    
    # --- Main Content (Estilo tarjetas premium) ---
    st.header(f"{categoria} Tools")
    
    # Ejemplo de "tarjetas" de scripts (como productos PXG)
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.markdown("**🔧 Data Cleaner**")
            st.markdown("*Limpieza automática de datasets*")
            if st.button("Ejecutar", key="cleaner"):
                st.switch_page("pages/cleaner.py")
    
    with col2:
        with st.container(border=True):
            st.markdown("**📊 Dashboard Pro**")
            st.markdown("*Visualización interactiva*")
            if st.button("Ejecutar", key="dashboard"):
                st.switch_page("pages/dashboard.py")
    
    # --- Footer estilo PXG ---
    st.markdown("---")
    st.markdown("**© 2024 Tu Librería** | *Powered by Streamlit*")
if __name__ == "__main__":
    main()