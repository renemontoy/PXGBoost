import streamlit as st
import importlib
import os
from typing import Dict, List

def inject_pxg_css():
    st.markdown("""
    <style>
        /* Paleta PXG oficial */
        :root {
            --pxg-black: #000000;
            --pxg-white: #FFFFFF;
            --pxg-gold: #D4AF37;  /* Dorado característico */
            --pxg-light: #F5F5F5;  /* Fondo claro */
            --pxg-gray: #333333;   /* Texto secundario */
        }
        
        /* Estructura principal */
        .stApp {
            background-color: var(--pxg-white);
            color: var(--pxg-black);
        }
        
        /* Sidebar estilo PXG */
        [data-testid="stSidebar"] {
            background-color: var(--pxg-black) !important;
            border-right: 1px solid var(--pxg-gold) !important;
        }
        
        /* Checkboxes en sidebar */
        [data-testid="stSidebar"] .stCheckbox label {
            color: var(--pxg-white) !important;
            font-size: 1rem;
        }
        
        [data-testid="stSidebar"] .stCheckbox input:checked + label {
            color: var(--pxg-gold) !important;
            font-weight: 600;
        }
        
        /* Tarjetas de herramientas */
        .tool-card {
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            background: var(--pxg-white);
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        .tool-card h3 {
            color: var(--pxg-black) !important;
            border-bottom: 2px solid var(--pxg-gold);
            padding-bottom: 0.5rem;
            margin-top: 0;
        }
        
        /* Botones estilo PXG */
        .stButton button {
            background-color: var(--pxg-black) !important;
            color: var(--pxg-white) !important;
            border: 1px solid var(--pxg-gold) !important;
            border-radius: 2px;
            padding: 0.5rem 1rem;
            font-weight: 500;
            transition: all 0.3s;
        }
        
        .stButton button:hover {
            background-color: var(--pxg-gold) !important;
            color: var(--pxg-black) !important;
        }
        
        /* Header y títulos */
        .stMarkdown h1 {
            color: var(--pxg-black) !important;
            font-weight: 700;
            border-bottom: 3px solid var(--pxg-gold);
            padding-bottom: 0.5rem;
        }
        
        .stMarkdown h2 {
            color: var(--pxg-gray) !important;
            font-weight: 600;
        }
        
        /* Footer */
        .footer {
            color: var(--pxg-gray);
            text-align: center;
            padding: 1rem;
            margin-top: 2rem;
            border-top: 1px solid var(--pxg-gold);
            font-size: 0.9rem;
        }
    </style>
    """, unsafe_allow_html=True)

def create_tool_card(name, description):
    st.markdown(f"""
    <div class="tool-card">
        <h3>{name}</h3>
        <p>{description}</p>
        <div class="stButton">
            <button>Ejecutar</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    inject_pxg_css()
    
    # Header con logo (simulado)
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("""
        <div style="padding:10px;">
            <svg width="50" height="50" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                <rect width="100" height="100" fill="black"/>
                <text x="50" y="60" font-family="Arial" font-size="40" 
                      font-weight="bold" fill="#D4AF37" text-anchor="middle">PXG</text>
            </svg>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.title("PXG Boost")
    
    st.markdown("---")
    
    # Sidebar - Navegación
    with st.sidebar:
        st.markdown("### Script Categories")
        categories = ["Procesamiento", "Visualización", "ML", "Utilidades"]
        selected = "Visualización"  # Ejemplo seleccionado
        
        for cat in categories:
            st.checkbox(cat, value=(cat == selected), key=f"cat_{cat}")
        
        st.markdown("---")
        st.markdown("### Configuración")
        st.checkbox("Modo Premium", key="premium_mode")
    
    # Contenido principal
    st.header("Visualización Tools")
    
    # Herramientas
    tools = [
        {"name": "Dashboard Pro", "desc": "Descripción de Dashboard Pro"},
        {"name": "Chart Generator", "desc": "Descripción de Chart Generator"},
        {"name": "Map Visualizer", "desc": "Descripción de Map Visualizer"}
    ]
    
    for tool in tools:
        create_tool_card(tool["name"], tool["desc"])
    
    # Footer
    st.markdown("---")
    st.markdown('<div class="footer">© 2024 Tu Librería | Powered by Streamlit</div>', 
                unsafe_allow_html=True)

if __name__ == "__main__":
    main()