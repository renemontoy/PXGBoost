import streamlit as st
from modules.Data_Cleaner import DataCleaner

st.set_page_config(page_title="PXG Boost", layout="wide")


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
        .action-btn {
            background-color: var(--pxg-black) !important;
            color: var(--pxg-white) !important;
            border: 1px solid var(--pxg-gold) !important;
            border-radius: 2px;
            padding: 0.5rem 1rem;
            font-weight: 500;
            transition: all 0.3s;
            width: 100%;
        }
        
        .action-btn:hover {
            background-color: var(--pxg-gold) !important;
            color: var(--pxg-black) !important;
        }
                
        .tool-content {
            border-left: 3px solid var(--pxg-gold);
            padding-left: 1rem;
            margin-top: 1rem;
            display: none;
        }
        .tool-content.expanded {
            display: block;
        
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

def create_tool_card(name, description, category):
    """Crea una tarjeta de herramienta con botón Ejecutar"""
    with st.container():
        st.markdown(f"""
        <div class="tool-card">
            <h3>{name}</h3>
            <p>{description}</p>
            <button class="action-btn" onclick="toggleTool('{name}')">Ejecutar</button>
        </div>
        <div id="content-{name}" class="tool-content">
            <!-- El contenido se inyectará aquí -->
        </div>
        """, unsafe_allow_html=True)
        
        # Estado para controlar la visibilidad
        if f'show_{name}' not in st.session_state:
            st.session_state[f'show_{name}'] = False
        
        # Mostrar contenido si está activo
        if st.session_state[f'show_{name}']:
            if name == "Data Cleaner":
                DataCleaner.show_interface()

def main():
    inject_pxg_css()

    st.markdown("""
    <script>
    function toggleTool(toolName) {
        // Actualiza el estado en Streamlit
        window.parent.postMessage({
            type: 'streamlit:setComponentValue',
            key: 'toggle_' + toolName,
            value: true
        }, '*');
        
        // Muestra el contenido
        const content = document.getElementById('content-' + toolName);
        content.classList.add('expanded');
    }
    </script>
    """, unsafe_allow_html=True)

    # Manejar clics en los botones
    for tool in ["Data Cleaner", "Data Transformer", "Defect Warranty"]:
        if st.button(f"Toggle {tool}", key=f"toggle_{tool}", disabled=True, visible=False):
            st.session_state[f'show_{tool}'] = not st.session_state[f'show_{tool}']
            st.rerun()
    
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
            {"name": "Defect Warranty", "desc": "Herramienta de limpieza de datasets"},
            {"name": "Data Transformer", "desc": "Transformación de formatos de datos"}
        ],
        "IES": [
            {"name": "Data Transformer", "desc": "Creación de paneles interactivos"},
            {"name": "Data Cleaner", "desc": "Generador de gráficos avanzados"},
            {"name": "Map Visualizer", "desc": "Visualización geográfica de datos"}
        ],
        "Quality": [
            {"name": "Defect Warranty", "desc": "Entrenamiento de modelos ML"},
        ],
    }
    
    for tool in tools_data.get(st.session_state.selected_category, []):
        create_tool_card(tool["name"], tool["desc"], st.session_state.selected_category)
    
    # Footer
    st.markdown("---")
    st.markdown('<div class="footer">© 2025 PXG Boost | Created by René Montoy</div>', 
                unsafe_allow_html=True)

if __name__ == "__main__":
    main()