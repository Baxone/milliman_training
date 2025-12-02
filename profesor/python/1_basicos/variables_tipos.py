# comentario de una sola linea
"""
    escribir 
    varias 
    lineas
"""

# tipos de datos - tipos basicos python es conoce debilmente tipado.
name_student = "Juan"
print(name_student)  # Juan
print(type(name_student))  # tipo de dato str => string

age = 43
print(age)  # 43
print(type(age))  # int

# cadenas de caracteres - string - texto
# "es texto" "23"
text = "En un lugar de la mancha"
other_text = 'Hola como estas'
text_multiline = """
varias
lineas de texto
"""  # valen tambien las comillas simples
print(text_multiline)

name = 'Juan'
surname = 'Perez'
# concatenacion de variables string + hacer una suma
name_complete = name + " " + surname
print(name_complete)
# funcion fprint
name_complete_fprint = f"{name} {surname} tiene {age} años"
print(name_complete_fprint)


# tipos numericos - python trabaja int, float, negativos
age_student = 34  # int
grades = -23  # negativo
price = 39.90  # float
print(price * 2)

# tipo booleano - tipo de valor enchufe - encendio y apagado - 0 False - 1 True
status = True
order = False
