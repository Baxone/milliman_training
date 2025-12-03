# una tupla es un listado de elementos INMUTABLE, no se puede modificar, ni añadir ni quitar elementos.

tupla = ('Juan', 32, True)
tupla2 = ('Juan', 'Pepe', 'Maria', 'Alba', 'Lucia', 'Rodrigo')

print(tupla)
# cantidad de items que tiene mi tupla se numeran de 0 a n-1 siendo n la len de tupla
print(len(tupla))

print(tupla[1])  # 32
print(tupla[-2])  # 32

# copias de una tupla
# ERROR no podemos añadir elementos a la tupla ni modificarlos
# tupla[3] = 'hola' añadir
# tupla[1] = 45
# si es posible por que es un sobrescritura de tupla
tupla = ()
print(tupla)

# copiar un tupla
tupla_mujeres = tupla2[2:5]
print(tupla_mujeres)
copia_tupla = tupla2[1:5:2]
print(copia_tupla)

# escoger elemento concretos
copia_tupla2 = (tupla2[1], tupla2[5], tupla2[3])
print(copia_tupla2)
# recorrer tupla
for item in tupla2:
    print(item)
