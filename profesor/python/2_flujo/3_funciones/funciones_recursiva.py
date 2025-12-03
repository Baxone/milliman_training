# Recursividad: Es una función que se llama a si misma.

# Crear una funcion que me pida un numero de telefono, este numero tiene que ser string, si meto un meto un numero , me volvera a pedir el telefono.

# print('12324a256'.isdigit())

def get_phone():
    phone = input('introduce un numero: ')  # 12345
    # isdigit => cadena.isdigit() True si solo esta formada por digitos y false si caracter no digito
    if not phone.isdigit():
        print('Esto no es un numero de telefono')
        get_phone()
    else:
        print(phone)


get_phone()
