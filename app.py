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
            --pxg-accent: #FF0000;
        }
        .stApp {
            background-color: var(--pxg-white);
            color: var(--pxg-black);
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
            width: 100%;
        }
        .stCheckbox>label {
            color: var(--pxg-white) !important;
            font-size: 1.1rem;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: var(--pxg-black) !important;
            font-weight: 700 !important;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            background-color: var(--pxg-white);
            border-top: 1px solid var(--pxg-black);
        }
        .tool-card {
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            transition: transform 0.2s;
        }
        .tool-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    </style>
    """, unsafe_allow_html=True)

# Diccionario de categorías y sus scripts
CATEGORIAS = {
    "Procesamiento": ["Data Cleaner", "Data Transformer", "Data Analyzer"],
    "Visualización": ["Dashboard Pro", "Chart Generator", "Map Visualizer"],
    "ML": ["Model Trainer", "Predictor", "Evaluator"],
    "Utilidades": ["File Converter", "Logger", "Config Manager"]
}

def main():
    inject_custom_css()
    
    # --- Header estilo PXG ---
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("https://www.pxg.com/hubfs/PXG_Logo.svg", width=100)
    with col2:
        st.title("PXG Boost")
    st.markdown("---")
    
    # --- Sidebar (Navegación estilo PXG) ---
    with st.sidebar:
        st.markdown("## Script Categories")
        
        # Checkboxes para categorías como en la imagen
        selected_category = None
        for category in CATEGORIAS.keys():
            if st.checkbox(category, key=f"cat_{category}"):
                selected_category = category
        
        st.markdown("---")
        st.markdown("## Configuración")
        modo_premium = st.checkbox("Modo Premium", key="premium_mode")
    
    # --- Main Content (Estilo tarjetas premium) ---
    if selected_category:
        st.header(f"{selected_category} Tools")
        
        # Mostrar herramientas de la categoría seleccionada
        for tool in CATEGORIAS[selected_category]:
            with st.container():
                st.markdown(f"""
                <div class="tool-card">
                    <h3>{tool}</h3>
                    <p>Descripción de {tool}</p>
                    <button class="stButton">Ejecutar</button>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("Selecciona una categoría en el menú lateral para ver las herramientas")
    
    # --- Footer estilo PXG ---
    st.markdown("""
    <div class="footer">
        © 2024 Tu Librería | Powered by Streamlit
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()