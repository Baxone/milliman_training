Ejercicio 3 - Siniestros y siniestralidad
----------------------------------------
Este script:
1. Carga `cartera_polizas.csv` y `siniestros.csv`.
2. Hace un join (junta los dos ficheros en un tabla relacionada por id_poliza) por `id_poliza`. OJO que puede haber polizas sin siniestros
3. Calcula KPIs de siniestralidad. total_pagado, sinestralidad
4. Aplica validaciones básicas (pago ≥ 0, id_poliza existente).