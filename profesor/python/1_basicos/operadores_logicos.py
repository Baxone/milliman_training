# operadores logicos me permiten evaluar diferentes operaciones. True o False
# AND, OR, NOT(negacion)

# quiero un numero que sea par y divisible por 5
my_number = 10
resultado = (my_number % 2 == 0) and (my_number % 5 == 0)
print(resultado)
"""
AND
    False and False => False
    False and True => False
    True and False => False
    True and True => True

"""
# quiero un producto de mas de 40 euros o de menos 10.
price = 34
resultado = (price < 10) or (price > 40)
# resultado = 10 < price < 40  # entre 10 y 40
print(resultado)

"""
OR 
    False or False => False
    True or False => True
    False or True => True 
    True or True => True
"""

# la negación solo se usa en valores booleanos y para buscar el contrario.
is_active = True
print(not is_active)  # False
