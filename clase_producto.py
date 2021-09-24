import pandas as pd
import numpy as np
from productos.models import Productos

class Producto:
    archivo = ""
    
    def __init__(self, archivo):
        self.archivo = archivo

    def addProductos(self):
        df = pd.read_csv(self.archivo, encoding="latin-1", sep=";")
        columnas_productos = ['codigo','productoName','precio','stock','unidad','descuento','total']
        boleano = np.array_equal(columnas_productos, df.columns)
        if boleano == False:
            return False
        productos = []
        for i in range(len(df)):
            productos.append(
                Productos(
                    codigo = df.iloc[i][0],
                    productoName = df.iloc[i][1],
                    precio = df.iloc[i][2],
                    stock = df.iloc[i][3],
                    unidad = df.iloc[i][4],
                    descuento = df.iloc[i][5],
                    total = df.iloc[i][6],
                )
            )

        return productos