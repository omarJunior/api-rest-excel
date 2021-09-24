import pandas as pd
import numpy as np
from helados.models import Helados

class Helado:
    archivo = ""

    def __init__(self, archivo):
        self.archivo = archivo

    def addHelados(self):
        df = pd.read_csv(self.archivo, encoding="latin-1", sep=";")
        columnas_helado = ['nombre', 'precio', 'stock']
        boleano = np.array_equal(columnas_helado, df.columns)
        if boleano == False:
            return False
        helados = []
        for i in range(len(df)):
            helados.append(
                Helados(
                    nombre = df.iloc[i][0],
                    precio = df.iloc[i][1],
                    stock = df.iloc[i][2]
                )
            )

        return helados