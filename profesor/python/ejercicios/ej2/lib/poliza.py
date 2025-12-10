import pandas as pd
import openpyxl as op


class Poliza:
    cartera = ""
    fichero = ""

    def __init__(self, nombre_fichero, ext):
        self.fichero = f'./data/{nombre_fichero}.{ext}'
        # cargar el fichero
        if ext == 'csv':
            self.cartera = pd.read_csv(self.fichero)
            print(self.cartera.head())
        else:
            self.cartera = pd.read_excel(self.fichero)
            print(self.cartera.head())

    # crear una funcion que me calcule prima media
    # crear una funcion que me calcule la suma total asegura (pandas)
