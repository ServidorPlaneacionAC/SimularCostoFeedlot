import pandas as pd

class Cls_Transformacion:
    def __init__(self,BL,Esc1):
        self.BL = BL
        self.Esc1 = Esc1
    
    def Costo_Fijos(self,escenario):
        escenario['Fijos Alimento Res']=1