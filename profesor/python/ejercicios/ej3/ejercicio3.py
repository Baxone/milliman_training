import pandas as pd  # type: ignore
import numpy as np  # type: ignore

# parse_dates usa la columna fecha_inicio no como un texto si no como fecha
cartera = pd.read_csv('./data/cartera_polizas.csv',
                      parse_dates=['fecha_inicio'])
siniestro = pd.read_csv('./data/siniestros.csv')

# solo los cuatro primeros registros para comprobar que se han cargado correctamente
# print(cartera.head())
# print(siniestro.head())

# Validacion de que no hay siniestros con pago negativo
# ¿Son todo True? [True, False, False ...]
try:
    assert (siniestro['pago'] >= 0).all(), 'Hay sinestros con pago negativo'
except AssertionError:
    print('No puede haber siniestros con valor negativo')

# comprobar que las polizas que existe en cartera de sinestros. No hayas sinestros sin poliza
# set viene muy bien operaciones con conjuntos conviene eliminar duplicados.
polizas_cartera = set(cartera['id_poliza'])
polizas_siniestros = set(siniestro['id_poliza'])

polizas_fuera = polizas_siniestros - polizas_cartera
if polizas_fuera:
    print(
        f'Advertencia: Hay siniestros con polizas no presentes en la cartera: {polizas_fuera}')

# Juntar las dos tablas en mismo dataset usando id_poliza como elemento de union.
cartera_siniestros = siniestro.merge(cartera, on="id_poliza", how="left")
# print(cartera_sinestros.head())
# cada sinestro tiene los datos de el sinestro y de su poliza

total_pagado = cartera_siniestros['pago'].sum()
suma_asegurada_total = cartera_siniestros['suma_asegurada'].sum()
# calcula un porcentaje de sinestralidad
sinestralidad_simple = total_pagado / suma_asegurada_total

# de todo lo calculado que porcentaje se ha ido en sinestros.

print(f"Total pagado en sinestros: {total_pagado:.2f}")
print(f"Suma asegurada total de la cartera: {suma_asegurada_total:.2f}")
print(f"Porcentaje de siniestralidad: {sinestralidad_simple:.4%}")

# Agrupación siniestralidad por tipo de siniestro.
kpi_por_tipo = cartera_siniestros.groupby('tipo_siniestro')['pago'].sum()
print('Total pagado por tipo de sinestro:')
print(kpi_por_tipo)

# juntar las tablas de varios ficheros en un tabla virtual. Relacion entre tablas (merge)
# calculos básico (sum, mean, .....)
# agrupacion de resultado con groupby()
