import streamlit as st
import pandas as pd

class DataCleaner:
    @staticmethod
    def show_interface():
        """Muestra la interfaz solo cuando se ha hecho clic en Ejecutar"""
        st.markdown("---")
        
        # 1. Subida de archivo
        uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])
        
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.success("Archivo cargado correctamente!")
            
            # 2. Opciones de limpieza (solo se muestra después de cargar archivo)
            st.subheader("Opciones de limpieza")
            col1, col2 = st.columns(2)
            
            with col1:
                remove_duplicates = st.checkbox("Eliminar duplicados")
                columns_to_drop = st.multiselect("Columnas a eliminar", options=df.columns)
                
            with col2:
                fill_na_method = st.selectbox(
                    "Tratamiento de valores nulos",
                    options=["Dejar como están", "Eliminar filas", "Rellenar con cero"]
                )
            
            # 3. Procesamiento
            if st.button("Procesar datos"):
                with st.spinner("Limpiando datos..."):
                    cleaned_df = DataCleaner.clean_data(df, remove_duplicates, columns_to_drop, fill_na_method)
                    st.session_state.cleaned_df = cleaned_df
                    st.success("¡Limpieza completada!")
                    
                    # Mostrar y permitir descarga
                    st.dataframe(cleaned_df.head())
                    DataCleaner.download_button(cleaned_df)
    
    @staticmethod
    def clean_data(df, remove_duplicates, columns_to_drop, fill_na_method):
        """Lógica de limpieza de datos"""
        if remove_duplicates:
            df = df.drop_duplicates()
        if columns_to_drop:
            df = df.drop(columns=columns_to_drop)
        if fill_na_method == "Eliminar filas":
            df = df.dropna()
        elif fill_na_method == "Rellenar con cero":
            df = df.fillna(0)
        return df
    
    @staticmethod
    def download_button(df):
        """Botón de descarga"""
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Descargar datos limpios",
            data=csv,
            file_name="datos_limpios.csv",
            mime="text/csv"
        )