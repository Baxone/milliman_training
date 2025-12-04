# set es un conjunto de datos desordenados (aleatorios) y unicos. (elimina los duplicados)
lista = [1, 1, 1, 1, 1, 2, 2, 2, 22, 2, 5, 5, 5, 5, 56, 34, 2, 1]
lista_desordenada = [2, 4, 3, 12, 56, 7, 22, 34]
mi_set = {1, 1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 5, 5, 56, 34, 22, 2, 1}
lista_ordenada = sorted(mi_set)
frutas = {'Manzana', 'Naranja', 'Pera', 'Platano'}
print(lista)
print(mi_set)
print(frutas)
print(lista_ordenada)
lista_desordenada.sort()
print(lista_desordenada)

# lista de comunidades duplicadas y en distintos caracteres
lista_ciudades = ['Madrid', 'Barcelona', 'Coruña',
                  'Sevilla', 'Madrid', 'sevilla', 'oviedo']
# crear un lista para almacenar todas las ciudade en forma capitalize (Madrid)
lista_ciudades_capitalize = []
# recorre la lista original transformando cada ciudad en capitalize y insertando transforma en lista final
for ciudad in lista_ciudades:
    lista_ciudades_capitalize.append(ciudad.capitalize())
# aplicamos un set a la lista para eliminar los duplicados
conjunto = set(lista_ciudades_capitalize)
# el resultado de ese set no es un lista es un conjunto lo convertimos a lista
lista_ciudades_no_duplicados = list(conjunto)
# ordenamos la lista resultada A-Z
lista_ciudades_no_duplicados.sort(reverse=True)
# imprimimos
print(lista_ciudades_no_duplicados)

# añadir un elemento al set de frutas no duplicados
frutas.add('Melón')
print(frutas)

# borrar elementos que existan en el set y si no existe me da un error
frutas.remove('Naranja')
# borrar que elimina el elemento y no da error si no existe.
frutas.discard('Piña')

# vacia un set
frutas.clear()

# eliminar un set
del frutas
