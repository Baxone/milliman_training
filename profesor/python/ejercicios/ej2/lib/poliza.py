import pandas as pd  # type: ignore
import openpyxl as op  # type: ignore
import numpy as np  # type: ignore


class Poliza:
    cartera = ""
    fichero = ""

    def __init__(self, nombre_fichero, ext):
        self.fichero = f'./data/{nombre_fichero}.{ext}'
        # cargar el fichero
        if ext == 'csv':
            self.cartera = pd.read_csv(self.fichero)
        else:
            self.cartera = pd.read_excel(self.fichero)

    # crear una funcion que me calcule prima media
    def promedio(self, cabecera) -> float:
        return self.cartera[cabecera].mean()

    # crear una funcion que me calcule la suma total asegura (pandas)
    def sumatorio(self, cabecera) -> float:
        return self.cartera[cabecera].sum()

    def filter_by_head(self, cabecera, min, max):
        # me devuelve una lista de booleanos con aquellos que cumplen o no la condicion [True, False,.....]
        filtro = (self.cartera[cabecera] >= min) & (
            self.cartera[cabecera] <= max)
        # print(filtro)
        # a cartera le paso la lista de boleanos activar solo los que son True
        return self.cartera[filtro]

    def get_present_value(self, tasa, numero_anios):
        porcentaje = tasa / 100
        spot = (1 + porcentaje) ** np.arange(numero_anios)  # [0,1,2]
        prima = self.cartera['prima_anual'].to_numpy()
        prima = prima.reshape(-1, 1)
        prima = np.tile(prima, numero_anios)
        df_primas = pd.DataFrame(prima/spot)
        df_present_value = pd.DataFrame(prima/spot).sum(axis=1)
        # df_final = pd.concat([df_primas, df_present_value], axis=1)
        return df_present_value
