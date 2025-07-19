import streamlit as st
import importlib
import os
from typing import Dict, List

def inject_custom_css():
    st.markdown("""
    <style>
        /* Estilos generales */
        html, body, [class*="css"] {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: #000000;
        }
        
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #000000 !important;
        }
        
        [data-testid="stSidebar"] .stCheckbox label {
            color: white !important;
            font-size: 16px;
        }
        
        /* Checkboxes seleccionados */
        [data-testid="stSidebar"] .stCheckbox input:checked + label {
            color: #FF0000 !important;
            font-weight: bold;
        }
        
        /* Contenido principal */
        .stApp {
            background-color: white;
        }
        
        /* Tarjetas de herramientas */
        .tool-card {
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
            background-color: white;
        }
        
        .tool-card h3 {
            color: #000000 !important;
            margin-top: 0;
        }
        
        /* Botones */
        .stButton button {
            background-color: #FF0000 !important;
            color: white !important;
            border: none;
            border-radius: 4px;
            padding: 8px 16px;
            font-weight: bold;
            width: 100%;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 16px;
            border-top: 1px solid #e0e0e0;
            margin-top: 32px;
        }
    </style>
    """, unsafe_allow_html=True)

def main():
    inject_custom_css()
    
    # Header
    st.title("PXG Boost")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.markdown("**Script Categories**")
        
        # Checkboxes para categorías
        categories = ["Procesamiento", "Visualización", "ML", "Utilidades"]
        selected_category = "Visualización"  # Valor por defecto para el ejemplo
        
        for category in categories:
            checked = category == selected_category
            st.checkbox(category, value=checked, key=f"cat_{category}")
        
        st.markdown("---")
        st.markdown("**Configuración**")
        st.checkbox("Modo Premium", key="premium_mode")
    
    # Contenido principal
    st.header("Visualización Tools")
    
    # Tarjetas de herramientas
    tools = [
        {"name": "Dashboard Pro", "desc": "Descripción de Dashboard Pro"},
        {"name": "Chart Generator", "desc": "Descripción de Chart Generator"},
        {"name": "Map Visualizer", "desc": "Descripción de Map Visualizer"}
    ]
    
    for tool in tools:
        with st.container():
            st.markdown(f"""
            <div class="tool-card">
                <h3>{tool['name']}</h3>
                <p>{tool['desc']}</p>
                <div class="stButton">
                    <button>Ejecutar</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown('<div class="footer">© 2024 Tu Librería | Powered by Streamlit</div>', 
                unsafe_allow_html=True)

if __name__ == "__main__":
    main()