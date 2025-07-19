import streamlit as st

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
        
        /* Botones de navegación */
        .nav-btn {
            width: 100%;
            margin: 0.25rem 0;
            text-align: left;
            border-radius: 4px !important;
        }
        
        .nav-btn:not(.active-nav) {
            background-color: transparent !important;
            color: var(--pxg-white) !important;
            border: 1px solid var(--pxg-gray) !important;
        }
        
        .active-nav {
            background-color: var(--pxg-gold) !important;
            color: var(--pxg-black) !important;
            border: 1px solid var(--pxg-gold) !important;
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
        
        /* Títulos */
        .stMarkdown h1 {
            color: var(--pxg-black) !important;
            font-weight: 700;
            padding-bottom: 0.5rem;
            margin-top: 0;
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
        <button class="action-btn">Ejecutar</button>
    </div>
    """, unsafe_allow_html=True)

def main():
    inject_pxg_css()
    
    # Estado para la categoría seleccionada
    if 'selected_category' not in st.session_state:
        st.session_state.selected_category = "Visualización"
    
    # Header simplificado
    st.title("PXG Boost")
    st.markdown("---")
    
    # Sidebar con botones de navegación
    with st.sidebar:
        st.markdown("### Script Categories")
        
        categories = ["Procesamiento", "Visualización", "ML", "Utilidades"]
        
        for cat in categories:
            if st.button(
                cat,
                key=f"nav_{cat}",
                on_click=lambda c=cat: setattr(st.session_state, 'selected_category', c)
            ):
                pass
            
            # Aplicar clase CSS dinámica
            if st.session_state.selected_category == cat:
                st.markdown(
                    f"<style>.stButton button[key='nav_{cat}'] {{ background-color: var(--pxg-gold) !important; color: var(--pxg-black) !important; }}</style>",
                    unsafe_allow_html=True
                )
        
        st.markdown("---")
        st.markdown("### Configuración")
        st.checkbox("Modo Premium", key="premium_mode")
    
    # Contenido principal basado en la categoría seleccionada
    st.header(f"{st.session_state.selected_category} Tools")
    
    # Ejemplo de herramientas por categoría
    tools_data = {
        "Procesamiento": [
            {"name": "Data Cleaner", "desc": "Herramienta de limpieza de datasets"},
            {"name": "Data Transformer", "desc": "Transformación de formatos de datos"}
        ],
        "Visualización": [
            {"name": "Dashboard Pro", "desc": "Creación de paneles interactivos"},
            {"name": "Chart Generator", "desc": "Generador de gráficos avanzados"},
            {"name": "Map Visualizer", "desc": "Visualización geográfica de datos"}
        ],
        "ML": [
            {"name": "Model Trainer", "desc": "Entrenamiento de modelos ML"},
            {"name": "Predictor", "desc": "Generación de predicciones"}
        ],
        "Utilidades": [
            {"name": "File Converter", "desc": "Conversión entre formatos de archivo"},
            {"name": "Logger", "desc": "Sistema de registro de actividades"}
        ]
    }
    
    for tool in tools_data.get(st.session_state.selected_category, []):
        create_tool_card(tool["name"], tool["desc"])
    
    # Footer
    st.markdown("---")
    st.markdown('<div class="footer">© 2024 Tu Librería | Powered by Streamlit</div>', 
                unsafe_allow_html=True)

if __name__ == "__main__":
    main()