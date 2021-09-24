import pandas as pd
import numpy as np
from calificaciones.models import Calificaciones

class Calificacion:
    archivo = ""
    
    def __init__(self, archivo):
        self.archivo = archivo

    def addCalificacion(self):
        df = pd.read_csv(self.archivo, encoding="latin-1", sep=";")
        columnas_calificaciones = [
            'codinst', 
            'nombreinstitucion', 
            'codigomunicipio', 
            'nombremunicipio', 
            'departamento', 
            'calendario', 
            'naturaleza', 
            'jornada', 
            'promediomatematica', 
            'promedioquimica',
            'promediofisica',
            'promediobiologia',
            'promediofilosofia',
            'promedioingles',
            'promediolenguaje',
            'promediosociales',
            'desviacionmatematica',
            'desviacionquimica',
            'desviacionfisica',
            'desviacionbiologia',
            'desviacionfilosofia',
            'desviacioningles',
            'desviacionlenguaje',
            'desviacionsociales',
            'evaluados',
            'periodo'
        ]
        boleano = np.array_equal(columnas_calificaciones, df.columns)
        if boleano == False:
            return False
        calificaciones = []
        for x in range(len(df)):
            calificaciones.append(
                Calificaciones(
                    codinst = df.iloc[x][0],
                    nombreinstitucion = df.iloc[x][1],
                    codigomunicipio = df.iloc[x][2],
                    nombremunicipio = df.iloc[x][3],
                    departamento = df.iloc[x][4],
                    calendario = df.iloc[x][5],
                    naturaleza = df.iloc[x][6],
                    jornada = df.iloc[x][7],
                    promediomatematica = df.iloc[x][8],
                    promedioquimica = df.iloc[x][9],
                    promediofisica = df.iloc[x][10],
                    promediobiologia = df.iloc[x][11],
                    promediofilosofia = df.iloc[x][12],
                    promedioingles = df.iloc[x][13],
                    promediolenguaje = df.iloc[x][14],
                    promediosociales = df.iloc[x][15],
                    desviacionmatematica = df.iloc[x][16],
                    desviacionquimica = df.iloc[x][17],
                    desviacionfisica = df.iloc[x][18],
                    desviacionbiologia = df.iloc[x][19],
                    desviacionfilosofia = df.iloc[x][20],
                    desviacioningles = df.iloc[x][21],
                    desviacionlenguaje = df.iloc[x][22],
                    desviacionsociales = df.iloc[x][23],
                    evaluados = df.iloc[x][24],
                    periodo = df.iloc[x][25],
                )
            )
        return calificaciones


