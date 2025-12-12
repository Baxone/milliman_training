import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import openpyxl  # type: ignore
import time  # esta viene por defecto dentro de python


def get_data(file_name):
    df = pd.read_excel(f"./data/{file_name}")
    return df


curvas = get_data('curvas_descuento.xlsx')

# crear un funcion que me saque el vector de pago por año en funcion fichero de curvas.


def get_cashflow(df_curvas, cashflow):
    # devuelve cuantas filas tiene la tabla curvas, cuantos años
    n_anios = len(df_curvas)
    cashflow_anual = cashflow
    # tenemos un df (tabla excel) que queremos convertir vector(lista) vamos usar numpy
    cashflows = np.full(n_anios, cashflow_anual)
    # n_anios seria la cantidad de elementos de mi vector
    # seria el valor de cada posicion [1000.0,1000.0,1000.0......]
    return {'anios': n_anios, 'anual': cashflow_anual, 'vector': cashflows}


dict_cashflow = get_cashflow(curvas, 1000.0)
# un vector/list que contiene los valores de las tasas
tasas = curvas['tasa'].values

# numpy matriz vectorizada y mediremos el tiempo
inicio_vec = time.time()
periodos = np.arange(0, dict_cashflow['anios'])
vp_vectorizado = np.sum(dict_cashflow['anual'] / (1 + tasas) ** periodos)
fin_vec = time.time()

print('vector', vp_vectorizado)
print(f'vector:{fin_vec - inicio_vec:.7f}')


# metodo tradicional que es manejando bucles. present_value y calculamos el tiempo que tardamos en hacer ese calculo.
inicio_bucle = time.time()
vp_bucle = 0.0
for anio in range(0, dict_cashflow['anios']):
    tasa = tasas[anio]
    vp_bucle += dict_cashflow['anual'] / (1 + tasa) ** anio
fin_bucle = time.time()
print('bucle', vp_bucle)
print(f'bucle:{fin_bucle - inicio_bucle:.7f}')
