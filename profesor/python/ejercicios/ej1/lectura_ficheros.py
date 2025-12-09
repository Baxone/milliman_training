mi_fichero = open('data/siniestros.csv', 'r')

# read() me permite leer el contenido del fichero
# print(mi_fichero.read())

# readlines() me permite leer linea a linea
# print(mi_fichero.readlines())
lista_polizas = []
for linea in mi_fichero.readlines():
    linea = linea.replace('\n', '')
    data = linea.split(',')
    poliza = {
        'id': data[0],
        'anio': data[1],
        'pago': data[2],
        'tipo_siniestro': data[3]
    }
    lista_polizas.append(poliza)

print(lista_polizas[12])
