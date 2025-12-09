import pandas as pd

# cargar un fichero con pandas. Dataset
df = pd.read_csv('data/siniestros.csv')
# print(df.head())  # las primeras columnas

# sacar una lista con los sinestros que hay.
# .unique() no repite tipo_siniestro
tipo_siniestro = df['tipo_siniestro'].unique()
print(tipo_siniestro)

# filtro = df[df['tipo_siniestro'] == 'Fallecimiento']
# print(filtro)


def filter_by_siniestro(tipo, df):
    filtro = df[df['tipo_siniestro'] == tipo]
    print(filtro)


for siniestro in tipo_siniestro:
    filter_by_siniestro(siniestro, df)


# sacar el pago maximo por fallecimiento y los datos del registro del cliente
# df_fallecimientos = df[df['tipo_siniestro'] == 'Fallecimiento']
# el maximo valor por columna del registro
# max_pago = df_fallecimientos['pago'].max()
# id_max_pago = df_fallecimientos['pago'].idxmax()
# print(max_pago)
# print(id_max_pago)
# print(df.loc[id_max_pago])


def get_data_by_max_value(tipo, df, campo):
    # filtro por tipo de sinestro creamos un dateframe con el resultado del filtro
    df_filter = df[df['tipo_siniestro'] == tipo]
    # max() del df me saca el valor maximo por ese campo
    max_value = df_filter[campo].max()
    # idxmax() del df me saca el id del valor maximo
    id_max_value = df_filter[campo].idxmax()
    print(max_value)
    # df.loc me permite sacar el registro por id del dataframe. Recordar que el dataframe tiene su propio id no coincide con la posicion.
    print(df.loc[id_max_value])
    diccionario = df.loc[id_max_value].to_dict()
    print(diccionario['anio'])


get_data_by_max_value('Enfermedad Grave', df, 'pago')
