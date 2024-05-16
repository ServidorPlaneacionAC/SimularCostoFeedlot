import pandas as pd
import streamlit as st

class Cls_Cargar_Datos:
    def __init__(self):
        self.BL = pd.DataFrame(self.InicializarDatos())
        self.Esc1 = pd.DataFrame(self.InicializarDatos())


    def InicializarDatos(self):
        # Datos proporcionados
        Datos = {
            "Fijos Alimento Mes": [8739605.571],
            "Variable Alimento Mes": [11783432.33],
            "Variable Energeticos Alimento Mes": [3904343.863],
            "Variable MDO Alimento Res /Mes": [6476254.667],
            "Fijos Producción Mes": [53464981.42],
            "Variable Producción Mes": [2746430.05],
            "Fijos Energeticos Producción Mes": [3218670],
            "Variable MDO Producción Mes": [12952509.33],
            "Fijos Proyectos infraestructura Mes": [19877000],
            "Variable Plan Sanitario 3 meses/res": [9293],
            "MDO Valor x persona": [3238127.333]
        }
        return Datos
    
    def definir_parametros(self,escenario):

        # Valores predeterminados
        default_values = {
            'Inventario Reses':2000,
            'Numero de Reses Salida': 10,
            'Tiempo permanencia': 30.0,
            'Peso Inicial': 200.0,
            'Precio Res Flaca Kg': 2.5,
            'Precio Res Flaca': 500.0,
            '% Animales Descartados': 5.0,
            '% Mortalidad': 1.0
        }
        if escenario=='BL':
        # Input boxes para las variables con valores predeterminados
            self.BL[f'Inventario Reses'] = st.number_input(f'{escenario} Inventario Reses', min_value=0, step=1, value=default_values['Inventario Reses'])
            self.BL[f'Numero de Reses Salida'] = st.number_input(f'{escenario} Numero de Reses Salida', min_value=0, step=1, value=default_values['Numero de Reses Salida'])
            self.BL[f'Tiempo permanencia (días)'] = st.number_input(f'{escenario} Tiempo permanencia (días)', min_value=0.0, step=0.1, value=default_values['Tiempo permanencia'])
            self.BL[f'Peso Inicial (kg)'] = st.number_input(f'{escenario} Peso Inicial (kg)', min_value=0.0, step=0.1, value=default_values['Peso Inicial'])
            self.BL[f'Precio Res Flaca Kg ($)'] = st.number_input(f'{escenario} Precio Res Flaca Kg ($)', min_value=0.0, step=0.1, value=default_values['Precio Res Flaca Kg'])
            self.BL[f'Precio Res Flaca ($)'] = st.number_input(f'{escenario} Precio Res Flaca ($)', min_value=0.0, step=0.1, value=default_values['Precio Res Flaca'])
            self.BL[f'% Animales Descartados'] = st.number_input(f'{escenario} % Animales Descartados', min_value=0.0, step=0.1, format="%.2f", value=default_values['% Animales Descartados'])
            self.BL[f'% Mortalidad'] = st.number_input(f'{escenario} % Mortalidad', min_value=0.0, step=0.1, format="%.2f", value=default_values['% Mortalidad'])
        else:
            self.Esc1[f'Inventario Reses'] = st.number_input(f'{escenario} Inventario Reses', min_value=0, step=1, value=default_values['Inventario Reses'])
            self.Esc1[f'Inventario Reses'] = st.number_input(f'{escenario} Inventario Reses', min_value=0, step=1, value=default_values['Inventario Reses'])
            self.Esc1[f'Numero de Reses Salida'] = st.number_input(f'{escenario} Numero de Reses Salida', min_value=0, step=1, value=default_values['Numero de Reses Salida'])
            self.Esc1[f'Tiempo permanencia (días)'] = st.number_input(f'{escenario} Tiempo permanencia (días)', min_value=0.0, step=0.1, value=default_values['Tiempo permanencia'])
            self.Esc1[f'Peso Inicial (kg)'] = st.number_input(f'{escenario} Peso Inicial (kg)', min_value=0.0, step=0.1, value=default_values['Peso Inicial'])
            self.Esc1[f'Precio Res Flaca Kg ($)'] = st.number_input(f'{escenario} Precio Res Flaca Kg ($)', min_value=0.0, step=0.1, value=default_values['Precio Res Flaca Kg'])
            self.Esc1[f'Precio Res Flaca ($)'] = st.number_input(f'{escenario} Precio Res Flaca ($)', min_value=0.0, step=0.1, value=default_values['Precio Res Flaca'])
            self.Esc1[f'% Animales Descartados'] = st.number_input(f'{escenario} % Animales Descartados', min_value=0.0, step=0.1, format="%.2f", value=default_values['% Animales Descartados'])
            self.Esc1[f'% Mortalidad'] = st.number_input(f'{escenario} % Mortalidad', min_value=0.0, step=0.1, format="%.2f", value=default_values['% Mortalidad'])
        

