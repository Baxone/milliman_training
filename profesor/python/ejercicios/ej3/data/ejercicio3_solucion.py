"""
Ejercicio 3 - Siniestros y siniestralidad
----------------------------------------
Este script:
1. Carga `cartera_polizas.csv` y `siniestros.csv`.
2. Hace un join por `id_poliza`.
3. Calcula KPIs de siniestralidad.
4. Aplica validaciones básicas (pago ≥ 0, id_poliza existente).
"""

import pandas as pd

cartera = pd.read_csv("cartera_polizas.csv", parse_dates=["fecha_inicio"])
siniestros = pd.read_csv("siniestros.csv")

# Validaciones básicas de los datos de siniestros
assert (siniestros["pago"] >= 0).all(), "Hay siniestros con pago negativo"

# Comprobar que todos los id_poliza de siniestros están en cartera
polizas_cartera = set(cartera["id_poliza"])
polizas_siniestros = set(siniestros["id_poliza"])

polizas_fuera = polizas_siniestros - polizas_cartera
if polizas_fuera:
    print("Advertencia: Hay siniestros con pólizas no presentes en cartera:", polizas_fuera)

# Join cartera-siniestros
cartera_siniestros = siniestros.merge(cartera, on="id_poliza", how="left")

print("Cartera + siniestros (primeras filas):")
print(cartera_siniestros.head(), "\n")

# KPI básicos: total pagado y siniestralidad simple (pago / suma asegurada)
total_pagado = cartera_siniestros["pago"].sum()
suma_asegurada_total = cartera["suma_asegurada"].sum()
siniestralidad_simple = total_pagado / suma_asegurada_total

print(f"Total pagado en siniestros: {total_pagado:,.2f}")
print(f"Suma asegurada total cartera: {suma_asegurada_total:,.2f}")
print(f"Siniestralidad simple: {siniestralidad_simple:.4%}\n")

# Siniestralidad por tipo de siniestro
kpi_por_tipo = cartera_siniestros.groupby("tipo_siniestro")["pago"].sum()
print("Total pagado por tipo de siniestro:")
print(kpi_por_tipo)
