import pandas as pd
import numpy as np
from clientes.models import Clientes

class Cliente:
    archivo = ""

    def __init__(self, archivo):
        self.archivo = archivo

    def addClientes(self):  
        df = pd.read_csv(self.archivo, encoding="latin-1", sep=";")
        columnas_cliente = ['nombres', 'apellidos', 'direccion', 'telefono', 'correo', 'ciudad', 'empresa', 'estatus']
        boleano = np.array_equal(columnas_cliente, df.columns)
        if boleano == False:
            return False
        clientes = []
        for i in range(len(df)):
            clientes.append(
                Clientes(
                    nombres = df.iloc[i][0],
                    apellidos = df.iloc[i][1],
                    direccion = df.iloc[i][2],
                    telefono = df.iloc[i][3],
                    correo = df.iloc[i][4],
                    ciudad = df.iloc[i][5],
                    empresa = df.iloc[i][6],
                    estatus = df.iloc[i][7]
                )                
            )
        return clientes

    


