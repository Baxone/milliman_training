# me permite aplicar a una lista y regla que se le asigne a todos los elementos de la lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
numeros_dobles = []

for numero in numeros:
    numeros_dobles.append(numero*2)

print(numeros_dobles)

# map

# opcion 1 lambda numeros_triples
numeros_triples = list(map(lambda numero: numero * 3, numeros))
print(numeros_triples)
# opcion 2 funcion externa la mitad


def dividir_por_2(numero):
    return numero/2


numeros_mitad = list(map(dividir_por_2, numeros))
print(numeros_mitad)

# limpiar una base de datos - normalizarla
# quitar espacio por delante y por detras, quitar los acentos y vamos minusculas
clientes = [' CArlos Perez ', 'Raúl LoPez  ', ' MaríA Pombo ']


def get_word_without_accents(word):
    conAcentos = ['á', 'é', 'í', 'ó', 'ú']
    sinAcentos = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(conAcentos)):
        word = word.replace(conAcentos[i], sinAcentos[i])
    return word


def normalizacion(nombre):
    # eliminar los espacio
    sinEspacio = nombre.strip()
    # pasarlo todo a minusculas()
    title = sinEspacio.lower()
    # quitar las tildes
    sinTildes = get_word_without_accents(title)
    return sinTildes.title()


lista_normalizada = list(map(normalizacion, clientes))
print(lista_normalizada)
