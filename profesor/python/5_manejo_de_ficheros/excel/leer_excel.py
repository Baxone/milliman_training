import pandas as pd
# necesito instalar openpyxl por que pandas no lo instala por defecto.
# pip install openpyxl
df = pd.read_excel('../data/mortalidad_tabla.xlsx', sheet_name="Sheet1")

# dataframe completo
# print(df)
# cuatro primeros registros
print(df.head())

lista_dict = df.to_dict('records')
print(lista_dict)
