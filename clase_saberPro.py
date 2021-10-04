from os import sep
import pandas as pd
import numpy as np
from saberpro.models import SaberPro

class Saber_pro:
    archivo = ""
    
    def __init__(self, archivo):
        self.archivo = archivo

    def addSaberPro(self):
        df = pd.read_csv(self.archivo, encoding="latin-1", sep=";")
        longitud = len(df)
        columnas_saber_pro = ['nombres','apellidos','genero','ciudad','matematicas','lenguaje','ciencias','ingles','ciudadanas','fisica']
        boleano = np.array_equal(columnas_saber_pro, df.columns)
        if boleano == False:
            return False
        saber_pro = []
        for i in range(len(df)):
            saber_pro.append(
                SaberPro(
                    nombres = df.iloc[i][0],
                    apellidos = df.iloc[i][1],
                    genero = df.iloc[i][2],
                    ciudad = df.iloc[i][3],
                    matematicas = df.iloc[i][4],
                    lenguaje = df.iloc[i][5],
                    ciencias = df.iloc[i][6],
                    ingles = df.iloc[i][7], 
                    ciudadanas = df.iloc[i][8],
                    fisica = df.iloc[i][9],
                )
            )
        return [saber_pro, longitud]

