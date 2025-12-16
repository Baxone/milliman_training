import pandas as pd

def main():
    # leer archivos cdv, excel, json, txt
    polizas = pd.read_csv('./data/cartera_polizas.csv', parse_dates=["fecha_inicio"])
    siniestros = pd.read_csv('./data/siniestros.csv')
    
    
    # convertir fechas y elimando las fechas incorrectas
    polizas['fecha_inicio'] = pd.to_datetime(polizas['fecha_inicio'], errors="coerce")
    ##print(polizas.head())
    
    # unir dos tablas siniestros y polizas por el id de la poliza
    tabla_final = siniestros.merge(polizas, on="id_poliza", how='left')
    #tabla_final = siniestros.merge(polizas[['id_poliza', 'producto', 'suma_asegurada']], on="id_poliza", how='left')
    #print(tabla_final.head())
    
    # frecuencia (siniestro por poliza)
    freq = tabla_final.groupby('id_poliza').size().rename('n_sinestros')
    #print(freq.head())
    
    #media de una columna de un dataset
    #importe medio por sientros
    importe_medio = tabla_final['prima_anual'].mean()
    #print(importe_medio)
    
    # crear rangos de edad
    cortes = [18,30,40,50,60,120]
    labels = ['18-29', '30-39', '40-49', '50-59', '60+' ]
    tabla_final['banda_edad'] = pd.cut(tabla_final['edad'], bins=cortes, labels=labels)
    print(tabla_final.head())

if __name__ == "__main__":
    main()
