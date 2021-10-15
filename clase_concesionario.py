import pandas as pd
import numpy as np
from concesionario.models import Concesionario

class Concesionario_clase:
    archivo = ""

    def __init__(self, archivo):
        self.archivo = archivo

    def addConcesionario(self):
        df = pd.read_csv(self.archivo, encoding="latin-1", sep=";")
        longitud = len(df)
        columnas_concesionario = ['codigo', 'nombre', 'direccion', 'ciudad', 'tipo', 'cantidad_vehiculos', 'descripcion', 'renta', 'cordinador']
        boleano = np.array_equal(columnas_concesionario, df.columns)
        if boleano == False:
            return False
        concesionario = []
        for x in range(len(df)):
            concesionario.append(
                Concesionario(
                    codigo = df.iloc[x][0],
                    nombre = df.iloc[x][1],
                    direccion = df.iloc[x][2],
                    ciudad = df.iloc[x][3],
                    tipo = df.iloc[x][4],
                    cantidad_vehiculos = df.iloc[x][5],
                    descripcion = df.iloc[x][6],
                    renta = df.iloc[x][7],
                    cordinador = df.iloc[x][8]
                )
            )
        return [concesionario, longitud]
