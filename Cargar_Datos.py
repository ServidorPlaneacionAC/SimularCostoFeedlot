import pandas as pd

class Cls_Cargar_Datos:
    def __init__(self):
        self.DF = pd.DataFrame(self.InicializarDatos())
    
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
