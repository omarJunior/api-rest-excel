import pandas as pd
import numpy as np
from vehiculos.models import Vehiculos

class Vehiculo:
    archivo = ""

    def __init__(self, archivo):
        self.archivo = archivo

    def addVehiculos(self):
        df = pd.read_csv(self.archivo, encoding="latin-1", sep=";")
        longitud = len(df)
        columnas_vehiculos = ['placa','modelo','marca','color','precio','descripcion']
        boleano = np.array_equal(columnas_vehiculos, df.columns)
        if boleano == False:
            return False
        vehiculos = []
        for i in range(len(df)):
            vehiculos.append(
                Vehiculos(
                    placa = df.iloc[i][0],
                    modelo = df.iloc[i][1],
                    marca = df.iloc[i][2],
                    color = df.iloc[i][3],
                    precio = df.iloc[i][4],
                    descripcion = df.iloc[i][5],
                )
            )
        return [vehiculos, longitud]