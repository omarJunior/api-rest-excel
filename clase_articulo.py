import pandas as pd
import numpy as np
from articulos.models import Articulos

class Articulo:
    archivo = ""

    def __init__(self, archivo):
        self.archivo = archivo
        
    def addArticulos(self):
        df = pd.read_csv(self.archivo, encoding="latin-1", sep=";")
        longitud = len(df)
        columnas_articulos = ['nombres', 'precio', 'iva', 'descripcion', 'stock', 'cantidad', 'tipo']
        boleano = np.array_equal(columnas_articulos, df.columns)
        if boleano == False:
            return False
        articulos = []
        for i in range(len(df)):
            articulos.append(
                Articulos(
                    nombres = df.iloc[i][0],
                    precio = df.iloc[i][1],
                    iva = df.iloc[i][2],
                    descripcion = df.iloc[i][3],
                    stock = df.iloc[i][4],
                    cantidad = df.iloc[i][5],
                    tipo = df.iloc[i][6],
                )
            )
        return [articulos, longitud]