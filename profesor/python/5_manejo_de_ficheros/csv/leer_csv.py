import pandas as pd

df = pd.read_csv('../data/siniestros.csv')

# Convertir mi dataframe un lista de listas
lista = df.values.tolist()
# print(lista[0])

# Convertir una sola columna en una lista.
lista_columna = df['tipo_siniestro'].unique().tolist()
# print(lista_columna)


# Convertir a lista de diccionarios (lista JSON a APIs)

lista_dict = df.to_dict(orient="records")
# print(lista_dict)

# Convertir cada fila en una tupla.
lista_tuplas = list(df.itertuples(index=False, name=None))
print(lista_tuplas[0])
