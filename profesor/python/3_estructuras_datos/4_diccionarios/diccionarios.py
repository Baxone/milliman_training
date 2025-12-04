# un diccionario es un conjunto de datos que no tienen posicion, en otros lenguajes de programacion se llaman array asociativos. Clave: Valor

cliente = {
    'nombre': 'Juan Antonio',
    'edad': 43,
    'riesgo': 0.30,
    'activo': True
}

print(cliente['edad'])  # 43
print(cliente.get('nombre'))  # Juan Antonio

# modicar un valor concreto de mi diccionario
cliente['edad'] = 23
print(cliente)

# tengo varias formas de recorrerlo, dependiendo de lo que quiera obtener
# si quiero usar como dato tanto la clave como el valor
for clave, valor in cliente.items():
    print(clave, valor)

print('---------')

for valor in cliente.values():
    print(valor)

print('---------')


for clave in cliente.keys():
    print(clave)

cliente['direccion'] = 'Calle numero piso y puerta'
print(cliente)

# borrar un elemento del diccionario
cliente.pop('edad')
print(cliente)

# limpiar un diccionario
cliente.clear()

# borrar un diccionario
del cliente
