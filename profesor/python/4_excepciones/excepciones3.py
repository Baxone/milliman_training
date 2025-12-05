def get_number_by_index(number_list):
    try:
        indice = int(
            input(f"Ingresa un indice de mi lista, valor maximo {len(number_list) - 1}: "))
        print("Valor:", number_list[indice])
    except ValueError:
        print('Error: El indice debe ser número entero')
    except IndexError:
        print('Error: el indice introducido no esta en rango')
    finally:
        # que ocurre siempre da igual que hayamos fallado o hayamos ido por el lado correcto
        print('El intento de acceso al dato ha terminado, intentalo de nuevo más tarde')
        # get_number_by_index(number_list)


lista_numeros = [1, 2, 3, 4, 5, 56, 743, 32,
                 34, 546, 456, 2, 6, 8, 9, 0, 6, 4, 43]
get_number_by_index(lista_numeros)
