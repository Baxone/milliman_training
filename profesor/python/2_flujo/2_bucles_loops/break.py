# break para el bucle cuando decidamos
# continue parar el bucle una sola iteracion

"""
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
"""
# continue en esta caso se salta los numeros impares.
for i in range(1, 10):
    if i % 2 != 0:
        continue
    print(i)
print('-'*40)
# break si se cumple que el numero es divisible por 5 para.
for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i)
