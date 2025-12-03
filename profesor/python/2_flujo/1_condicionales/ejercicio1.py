# Portero de discoteca. Le pregunta la edad a la persona con input y le dejamos entrar siempre y cuando sea mayor edad. OJO mayor de edad no es igual en distintos paises y tengo que tener en cuenta.

# plantear como resolver y la mejor forma de hacerlo. Hay varias posibilidades
age = int(input('Dime tu edad: '))
age_max = 21
msg = ""

# opcion 1
if age < age_max:
    msg = "Un vasito de leche y la cama"
else:
    msg = 'Bienvenido'

print(msg)


# opcion 2 condicional abreviado - operador ternario.
msg2 = 'No puedes pasar' if age < age_max else 'Bienvenido'
print(msg2)

# opcion 3: condicionales anidados.
msg_anidados = ""

if age >= 0 and age < 18:
    msg_anidados = 'no esta permito pasar'
elif age >= 18 and age <= 70:
    msg_anidados = 'felicidades'
else:
    msg_anidados = 'edad no valida'

print(msg_anidados)
