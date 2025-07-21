import streamlit as st
import pandas as pd
from io import StringIO

def show_interface():
    """Interfaz para el Data Cleaner"""
    st.title("🧹 Data Cleaner")
    st.markdown("---")
    
    # 1. Subida de archivo
    uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        # Leer el archivo
        df = pd.read_csv(uploaded_file)
        st.success("Archivo cargado correctamente!")
        
        # Mostrar vista previa
        with st.expander("Vista previa de datos"):
            st.dataframe(df.head())
        
        # 2. Opciones de limpieza
        st.subheader("Opciones de limpieza")
        col1, col2 = st.columns(2)
        
        with col1:
            remove_duplicates = st.checkbox("Eliminar duplicados")
            columns_to_drop = st.multiselect(
                "Columnas a eliminar",
                options=df.columns
            )
            
        with col2:
            fill_na_method = st.selectbox(
                "Tratamiento de valores nulos",
                options=["Dejar como están", "Eliminar filas", "Rellenar con cero"]
            )
        
        # 3. Procesamiento
        if st.button("Ejecutar limpieza"):
            with st.spinner("Procesando..."):
                # Aplicar transformaciones
                if remove_duplicates:
                    df = df.drop_duplicates()
                
                if len(columns_to_drop) > 0:
                    df = df.drop(columns=columns_to_drop)
                
                if fill_na_method == "Eliminar filas":
                    df = df.dropna()
                elif fill_na_method == "Rellenar con cero":
                    df = df.fillna(0)
                
                # Mostrar resultados
                st.success("Limpieza completada!")
                st.dataframe(df.head())
                
                # 4. Descarga de resultados
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    "Descargar datos limpios",
                    data=csv,
                    file_name="datos_limpios.csv",
                    mime="text/csv"
                )