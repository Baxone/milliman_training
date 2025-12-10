from lib.poliza import Poliza


def main():
    menu = """Analisis de polizas
[1]. Calcular prima media
[2]. Calcular suma total asegurada
[3]. Calcular edad media
[x]. Salir del programa
     """
    print(menu)
    option = input('Selecciona una opción: ')
    if option == '1':
        # calcular prima media
        cartera = Poliza('cartera_polizas', 'csv')
    elif option == '2':
        # calcular suma total asegurada
        pass
    elif option == '3':
        # calcular edad media
        pass
    elif option == 'x':
        print('Hasta pronto')
    else:
        print('Opción no valida')
        main()


if __name__ == '__main__':
    main()
