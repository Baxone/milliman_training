# import lib.functions as fn
from lib.functions import percent_global, get_data, get_clients_by_tramo


def main():
    data = get_data()
    menu = """### Simulador de caidas ###
    [1]. Porcentaje global caidas
    [2]. Porcentaje por edad
    [x]. Salir
    """
    print(menu)
    option = input('Selecciona un opción: ')
    if option == "1":
        percent_global(data)
    elif option == "2":
        tramo = int(input('Dime cuantos años quieres por tramo: '))
        clients_filter = get_clients_by_tramo(data, tramo)
        print(clients_filter)
    elif option == "x":
        print('Hasta pronto')
    else:
        print('opcion no permitida')
        main()


# siempre que trabajemos con modulos tiene haber uno que sea el inicial. Para marcar el incial tiene que tener es condicional. Se pone siempre al final del script
if __name__ == "__main__":
    main()
