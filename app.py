import streamlit as st
from modules.data_cleaner import data_cleaner

def inject_pxg_css():
    st.markdown("""
    <style>
        /* Paleta PXG oficial */
        :root {
            --pxg-black: #000000;
            --pxg-white: #FFFFFF;
            --pxg-gold: #D4AF37;
            --pxg-light: #F5F5F5;
            --pxg-gray: #333333;
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
        
        .stButton button {
            width: 100%;
            margin: 0.25rem 0;
            text-align: left;
            border-radius: 4px !important;
            transition: all 0.3s;
        }

        /* Botones INACTIVOS */
        .stButton button:not(:active) {
            background-color: transparent !important;
            color: white !important;
            border: 1px solid #333333 !important;
        }

        /* Botones ACTIVOS (seleccionados) */
        .stButton button:active, 
        .stButton button:focus {
            background-color: #D4AF37 !important;
            color: black !important;
            border: 1px solid #D4AF37 !important;
            font-weight: 600;
}
        .active-nav {
            background-color: var(--pxg-gold) !important;
            color: var(--pxg-black) !important;
            border: 1px solid var(--pxg-gold) !important;
            font-weight: 600;
        }
                
        [data-testid="stSidebar"] .stMarkdown h3 {
            color: white !important;
            border-bottom: 1px solid #D4AF37;
            padding-bottom: 0.5rem;
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
        
        /* Botones de acción */
        .action-btn-wrapper button {
            background-color: var(--pxg-black) !important;
            color: var(--pxg-white) !important;
            border: 1px solid var(--pxg-gold) !important;
            border-radius: 2px;
            padding: 0.5rem 1rem;
            font-weight: 500;
            transition: all 0.3s;
            width: 100%;
            text-align: center;
            margin-top: 0.5rem;
        }

        .action-btn-wrapper button:hover {
            background-color: var(--pxg-gold) !important;
            color: var(--pxg-black) !important;
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
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="action-btn-wrapper">', unsafe_allow_html=True)
    if st.button(f"Ejecutar {name}", key=f"exec_{name}"):
        st.session_state.active_tool = name
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    inject_pxg_css()
    
    # Estado para la categoría seleccionada
    if 'selected_category' not in st.session_state:
        st.session_state.selected_category = "Acumatica"
    
    # Header simplificado
    st.title("PXG Boost")
    st.markdown("---")
    
    # Sidebar con botones de navegación
    with st.sidebar:
        st.markdown("### Categories")
        
        categories = ["Acumatica","IES", "Quality"]
        
        for cat in categories:
            if st.button(
                cat,
                key=f"nav_{cat}",
                on_click=lambda c=cat: setattr(st.session_state, 'selected_category', c)
            ):
                pass
            
    
    # Contenido principal basado en la categoría seleccionada
    st.header(f"{st.session_state.selected_category} Tools")
    
    # Ejemplo de herramientas por categoría
    tools_data = {
        "Acumatica": [
            {"name": "Data Cleaner", "desc": "Herramienta de limpieza de datasets"},
            {"name": "Data Transformer", "desc": "Transformación de formatos de datos"}
        ],
        "IES": [
            {"name": "Dashboard Pro", "desc": "Creación de paneles interactivos"},
            {"name": "Chart Generator", "desc": "Generador de gráficos avanzados"},
            {"name": "Map Visualizer", "desc": "Visualización geográfica de datos"}
        ],
        "Quality": [
            {"name": "Model Trainer", "desc": "Entrenamiento de modelos ML"},
            {"name": "Predictor", "desc": "Generación de predicciones"}
        ],
    }
    
    tool_functions = {
        "Data Cleaner": data_cleaner,
        # Aquí puedes registrar más funciones: "Data Transformer": data_transformer, etc.
    }

    # Mostrar botones por categoría
    for tool in tools_data.get(st.session_state.selected_category, []):
        tool_name = tool["name"]
        st.markdown(f"### {tool_name}")
        st.markdown(tool["desc"])
        if st.button(f"Ejecutar {tool_name}", key=f"exec_{tool_name}"):
            st.session_state.active_tool = tool_name
        st.markdown("---")

    # Ejecutar herramienta seleccionada
    if 'active_tool' in st.session_state:
        selected_tool = st.session_state.active_tool
        st.markdown("## 🔧 Herramienta en ejecución:")
        tool_func = tool_functions.get(selected_tool)
        if tool_func:
            tool_func()
        else:
            st.warning("Herramienta aún no implementada.")
        
    # Footer
    st.markdown("---")
    st.markdown('<div class="footer">© 2025 PXG Boost | Created by René Montoy</div>', 
                unsafe_allow_html=True)

if __name__ == "__main__":
    main()