import streamlit as st
#from streamlit import session_state
import pandas as pd
import mplcursors
from plotly.subplots import make_subplots
import plotly.graph_objs as go
from Cargar_Datos import Cls_Cargar_Datos

class Visualizacion_Formulario:
    '''
    La idea de esta clase es generar campos para ingresar informacion numerica y de texto, generar df para
    descargar, cargar información desde los equipos locales y permitir una navegabilidad basica
    '''

    def __init__(self):
        self.df = pd.DataFrame()

    def ingresar_informacion(self):
        st.subheader("Ingrese información numérica:")
        num_input = st.number_input("Ingrese un número:", value=0.0)

        st.subheader("Ingrese información de texto:")
        text_input = st.text_input("Ingrese texto:")

        return num_input, text_input

    def generar_df(self, data):
        self.df = pd.DataFrame(data, columns=["Número", "Texto"])
        return self.df

    def descargar_df(self):
        if not self.df.empty:
            st.subheader("Descargar DataFrame:")
            csv = self.df.to_csv(index=False)
            st.download_button(
                label="Descargar CSV",
                data=csv,
                file_name='mi_dataframe.csv',
                mime='text/csv'
            )

    def cargar_informacion(self):
        st.subheader("Cargar información desde un archivo CSV:")
        uploaded_file = st.file_uploader("Cargar archivo CSV", type=['csv'])
        if uploaded_file is not None:
            self.df = pd.read_csv(uploaded_file)

    def mostrar_navegabilidad(self):
        st.sidebar.header("Navegación")
        page = st.sidebar.radio("Ir a:", ["Inicio", "Ingresar información", "Ver DataFrame"])

        if page == "Inicio":
            st.title("Bienvenido a la aplicación")
            st.write("Utilice el menú de la izquierda para navegar por la aplicación.")
            carga=Cls_Cargar_Datos()
            st.write(carga.DF)
        elif page == "Ingresar información":
            st.title("Ingresar Información")
            num_input, text_input = self.ingresar_informacion()
            if st.button("Generar DataFrame"):
                data = {"Número": [num_input], "Texto": [text_input]}
                self.generar_df(data)
        elif page == "Ver DataFrame":
            st.title("Ver DataFrame")
            st.write(self.df)
            self.descargar_df()

