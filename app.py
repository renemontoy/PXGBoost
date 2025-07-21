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
            background-color: var(--pxg-black) !important;
            color: var(--pxg-white) !important;
            border: 1px solid var(--pxg-gold) !important;
            border-radius: 2px;
            padding: 0.5rem 1rem;
            font-weight: 500;
            transition: all 0.3s;
            width: 100%;
        }
        .stButton button:hover {
            background-color: var(--pxg-gold) !important;
            color: var(--pxg-black) !important;
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
    
def main():
    inject_pxg_css()
    
    # Configuración de página DEBE SER LA PRIMERA LÍNEA
    st.set_page_config(page_title="PXG Boost", layout="wide")
    
    # Estado para controlar la vista actual
    if 'current_view' not in st.session_state:
        st.session_state.current_view = "home"
        st.session_state.current_category = None
        st.session_state.current_tool = None
    
    # Header
    st.title("PXG Boost")
    st.markdown("---")
    
    # Sidebar - Navegación principal
    with st.sidebar:
        st.markdown("### Categories")
        
        # Botones de categorías
        if st.button("🏠 Inicio", key="nav_home"):
            st.session_state.current_view = "home"
            st.rerun()
            
        st.markdown("---")
        
        if st.button("Acumatica", key="nav_acumatica"):
            st.session_state.current_view = "category"
            st.session_state.current_category = "Acumatica"
            st.rerun()
            
        if st.button("IES", key="nav_ies"):
            st.session_state.current_view = "category"
            st.session_state.current_category = "IES"
            st.rerun()
            
        if st.button("Quality", key="nav_quality"):
            st.session_state.current_view = "category"
            st.session_state.current_category = "Quality"
            st.rerun()
    
    # Lógica de navegación
    if st.session_state.current_view == "home":
        show_home()
    elif st.session_state.current_view == "category":
        show_category_tools(st.session_state.current_category)
    elif st.session_state.current_view == "tool":
        run_tool(st.session_state.current_tool)

def show_home():
    """Vista de inicio"""
    st.header("Bienvenido a PXG Boost")
    st.markdown("""
    Selecciona una categoría en el menú lateral para acceder a las herramientas disponibles.
    """)
    st.image("https://via.placeholder.com/800x400?text=PXG+Boost+Dashboard", use_column_width=True)

def show_category_tools(category):
    """Muestra las herramientas de una categoría específica"""
    st.header(f"{category} Tools")
    
    # Diccionario de herramientas por categoría
    tools_data = {
        "Acumatica": [
            {"name": "Data Cleaner", "desc": "Herramienta de limpieza de datasets", "func": data_cleaner},
            {"name": "Data Transformer", "desc": "Transformación de formatos de datos", "func": data_transformer}
        ],
        "IES": [
            {"name": "Dashboard Pro", "desc": "Creación de paneles interactivos", "func": dashboard_pro},
            {"name": "Chart Generator", "desc": "Generador de gráficos avanzados", "func": None},
            {"name": "Map Visualizer", "desc": "Visualización geográfica de datos", "func": None}
        ],
        "Quality": [
            {"name": "Model Trainer", "desc": "Entrenamiento de modelos ML", "func": None},
            {"name": "Predictor", "desc": "Generación de predicciones", "func": None}
        ]
    }
    
    # Mostrar herramientas de la categoría seleccionada
    for tool in tools_data.get(category, []):
        with st.container():
            st.markdown(f"""
            <div class="tool-card">
                <h3>{tool['name']}</h3>
                <p>{tool['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Ejecutar {tool['name']}", key=f"exec_{tool['name']}"):
                if tool['func']:
                    st.session_state.current_view = "tool"
                    st.session_state.current_tool = tool['func']
                    st.rerun()
                else:
                    st.warning("Esta herramienta aún no está implementada")

def run_tool(tool_func):
    """Ejecuta una herramienta específica"""
    # Botón para volver atrás
    if st.button("← Volver a la categoría"):
        st.session_state.current_view = "category"
        st.session_state.current_tool = None
        st.rerun()
    
    st.markdown("---")
    # Ejecutar la función de la herramienta
    tool_func()

# Footer (se muestra en todas las vistas)
st.markdown("---")
st.markdown('<div class="footer">© 2025 PXG Boost | Created by René Montoy</div>', 
            unsafe_allow_html=True)

if __name__ == "__main__":
    main()