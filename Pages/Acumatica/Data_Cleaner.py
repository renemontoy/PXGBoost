import streamlit as st

st.set_page_config(
    page_title="Data Cleaner",
    page_icon="🧹",
    layout="wide"
)

# CSS personalizado para mantener consistencia
st.markdown("""
<style>
    /* Copia aquí los mismos estilos de tu main.py */
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🧹 Data Cleaner")
    st.markdown("---")
    
    # Widgets de input
    uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        st.success("Archivo cargado correctamente!")
        
        # Opciones de limpieza
        st.subheader("Opciones de limpieza")
        remove_duplicates = st.checkbox("Eliminar duplicados")
        fill_na = st.selectbox(
            "Tratamiento de valores nulos",
            ["Dejar como están", "Eliminar filas", "Rellenar con cero"]
        )
        
        if st.button("Ejecutar limpieza"):
            with st.spinner("Procesando..."):
                # Aquí iría tu lógica de limpieza
                import pandas as pd
                import time
                
                df = pd.read_csv(uploaded_file)
                
                if remove_duplicates:
                    df = df.drop_duplicates()
                
                if fill_na == "Eliminar filas":
                    df = df.dropna()
                elif fill_na == "Rellenar con cero":
                    df = df.fillna(0)
                
                time.sleep(2)  # Simulamos procesamiento
                
                st.success("Limpieza completada!")
                st.dataframe(df.head())
                
                # Botón para descargar el resultado
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    "Descargar datos limpios",
                    csv,
                    "datos_limpios.csv",
                    "text/csv"
                )

if __name__ == "__main__":
    main()