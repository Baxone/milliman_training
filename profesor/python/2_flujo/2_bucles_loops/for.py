# imprimir 100 numeros por pantalla
cantidad = 100

# for i in range(cantidad):
#     print(i)

# for i in range(10, cantidad + 1):
#     print(i)

# for i in range(2, 20, 2):
#     print(i)

# tambien tienen secuencia de escape else: solo se va ejecutar cuando el bucle termine.

for i in range(1, 10, 2):
    if i % 2 == 0:
        break
    print(f'valor: {i}')
else:
    print('el bucle ha terminado')

texto = "Solo se que no se nada"
print(len(texto))

for i in range(len(texto)):
    if texto[i] != " ":
        print(texto[i])
